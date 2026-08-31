#!/usr/bin/env python3
"""Audit public routes, resources, anchors, search, and canonical global chrome."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:  # Support both `python tools/...` and package-style imports in tests.
    from .sync_global_bottom_bar import validate_bottom_bars
    from .sync_global_top_bar import validate_top_bars
except ImportError:
    from sync_global_bottom_bar import validate_bottom_bars
    from sync_global_top_bar import validate_top_bars

REFERENCE_ATTRIBUTES = {
    "a": ("href",),
    "audio": ("src",),
    "embed": ("src",),
    "iframe": ("src",),
    "img": ("src",),
    "link": ("href",),
    "object": ("data",),
    "script": ("src",),
    "source": ("src",),
    "track": ("src",),
    "video": ("poster", "src"),
}
IGNORED_SCHEMES = {"data", "http", "https", "javascript", "mailto", "tel"}


@dataclass(frozen=True)
class Reference:
    tag: str
    attribute: str
    value: str


class InventoryParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.references: list[Reference] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if element_id := attributes.get("id"):
            self.ids.append(element_id)
        for attribute in REFERENCE_ATTRIBUTES.get(tag, ()):
            if value := attributes.get(attribute):
                self.references.append(Reference(tag, attribute, value))

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self.handle_starttag(tag, attrs)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check every page's paths, IDs, fragments, global bars, and search record."
    )
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path("docs"),
        help="public HTML root (default: docs)",
    )
    parser.add_argument(
        "--search-index",
        type=Path,
        default=Path("docs/data/search.json"),
        help="search index to reconcile (default: docs/data/search.json)",
    )
    parser.add_argument(
        "--json-output",
        type=Path,
        help="optionally write the complete audit as JSON",
    )
    return parser.parse_args()


def resolve_local_path(root: Path, source: Path, url_path: str) -> Path:
    decoded = unquote(url_path)
    if decoded.startswith("/"):
        target = root / decoded.lstrip("/")
    elif decoded:
        target = source.parent / decoded
    else:
        target = source
    target = target.resolve()
    if decoded.endswith("/") or (target.exists() and target.is_dir()):
        target = target / "index.html"
    return target


def relative_label(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    search_index = args.search_index.resolve()
    if not root.is_dir():
        print(f"error: public root does not exist: {root}", file=sys.stderr)
        return 2

    html_files = sorted(root.rglob("*.html"))
    parsed: dict[Path, InventoryParser] = {}
    for path in html_files:
        parser = InventoryParser()
        parser.feed(path.read_text(encoding="utf-8", errors="replace"))
        parsed[path.resolve()] = parser

    failures: list[dict[str, str]] = []
    checked_local_references = 0
    checked_fragments = 0
    external_references = 0

    for source, inventory in parsed.items():
        source_label = relative_label(source, root)
        for element_id, count in Counter(inventory.ids).items():
            if count > 1:
                failures.append(
                    {
                        "page": source_label,
                        "kind": "duplicate-id",
                        "value": f"#{element_id} ({count} occurrences)",
                    }
                )

        for reference in inventory.references:
            split = urlsplit(reference.value)
            if split.scheme.lower() in IGNORED_SCHEMES or split.netloc:
                external_references += 1
                continue
            target = resolve_local_path(root, source, split.path)
            checked_local_references += 1
            if not target.exists():
                failures.append(
                    {
                        "page": source_label,
                        "kind": f"missing-{reference.tag}-{reference.attribute}",
                        "value": reference.value,
                    }
                )
                continue
            if split.fragment:
                checked_fragments += 1
                fragment = unquote(split.fragment)
                target_inventory = parsed.get(target.resolve())
                if target_inventory is not None and fragment not in target_inventory.ids:
                    failures.append(
                        {
                            "page": source_label,
                            "kind": "missing-fragment",
                            "value": reference.value,
                        }
                    )

    top_bar_issues = validate_top_bars(root)
    for issue in top_bar_issues:
        failures.append(
            {"page": issue.page, "kind": issue.kind, "value": issue.detail}
        )

    bottom_bar_issues = validate_bottom_bars(root)
    for issue in bottom_bar_issues:
        failures.append(
            {"page": issue.page, "kind": issue.kind, "value": issue.detail}
        )

    search_failures: list[dict[str, str]] = []
    expected_urls = {
        path.relative_to(root).as_posix()
        for path in parsed
        if path.relative_to(root).as_posix() != "404.html"
    }
    search_records = 0
    unique_search_urls = 0
    try:
        records = json.loads(search_index.read_text(encoding="utf-8"))
        urls = [record["url"] for record in records]
        search_records = len(urls)
        unique_search_urls = len(set(urls))
        for url, count in Counter(urls).items():
            if count > 1:
                search_failures.append(
                    {"page": "data/search.json", "kind": "duplicate-url", "value": url}
                )
        for url in sorted(expected_urls - set(urls)):
            search_failures.append(
                {"page": "data/search.json", "kind": "missing-page", "value": url}
            )
        for url in sorted(set(urls) - expected_urls):
            search_failures.append(
                {"page": "data/search.json", "kind": "stale-url", "value": url}
            )
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        search_failures.append(
            {"page": "data/search.json", "kind": "invalid-index", "value": str(error)}
        )

    failures.extend(search_failures)
    passed = not failures
    print(
        f"Somnarak structure audit: {len(html_files)} HTML files; "
        f"{checked_local_references} local references; {checked_fragments} fragments"
    )
    print(
        f"Search coverage: {search_records} records; {unique_search_urls} unique URLs; "
        f"{len(expected_urls)} expected pages"
    )
    print(
        f"Global top bar: {len(html_files)} expected components; "
        f"{len(top_bar_issues)} consistency issues"
    )
    print(
        f"Global bottom bar: {len(html_files)} expected components; "
        f"{len(bottom_bar_issues)} consistency issues"
    )
    if passed:
        print("PASS: paths, IDs, fragments, search coverage, and global bars are complete")
    else:
        print(f"FAIL: {len(failures)} structural issue(s)")
        for failure in failures:
            print(
                f"  {failure['page']}: {failure['kind']}: {failure['value']}"
            )

    if args.json_output:
        report = {
            "result": "PASS" if passed else "FAIL",
            "html_pages": len(html_files),
            "local_references_checked": checked_local_references,
            "fragments_checked": checked_fragments,
            "external_references_skipped": external_references,
            "search_records": search_records,
            "unique_search_urls": unique_search_urls,
            "expected_search_pages": len(expected_urls),
            "top_bar_components": len(html_files),
            "top_bar_issues": len(top_bar_issues),
            "bottom_bar_components": len(html_files),
            "bottom_bar_issues": len(bottom_bar_issues),
            "failures": failures,
        }
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"JSON report: {args.json_output}")

    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
