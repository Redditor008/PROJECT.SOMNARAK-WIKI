#!/usr/bin/env python3
"""Audit the Somnarak public HTML tree against its editorial word floor.

The count intentionally excludes shared interface chrome so navigation cannot make a
thin page pass. It uses only Python's standard library and can run in CI or locally.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path

WORD_RE = re.compile(r"[^\W_]+(?:[’'\-][^\W_]+)*", re.UNICODE)
SKIP_TAGS = {
    "aside",
    "footer",
    "header",
    "nav",
    "noscript",
    "script",
    "style",
    "template",
}
SKIP_CLASSES = {
    "article-nav",
    "breadcrumbs",
    "breadcrumb-trail",
    "cross-reference-section",
    "fast-jump-nav",
    "float-toc",
    "floor-rail",
    "left-rail",
    "page-tabs",
    "spotlight-actions",
    "tactical-directive-box",
    "tactical-hud-bar",
    "toc",
    "utility",
    "wiki-footer",
}


@dataclass(frozen=True)
class PageResult:
    path: str
    words: int
    passes: bool


class EditorialTextParser(HTMLParser):
    """Collect non-chrome text from <main>, falling back to <body>."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._stack: list[tuple[bool, bool, bool, str]] = []
        self.main_text: list[str] = []
        self.body_text: list[str] = []
        self.has_main = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        classes = set((attributes.get("class") or "").split())
        parent_in_main = self._stack[-1][0] if self._stack else False
        parent_skipped = self._stack[-1][1] if self._stack else False
        parent_in_body = self._stack[-1][2] if self._stack else False

        in_main = parent_in_main or tag == "main"
        in_body = parent_in_body or tag == "body"
        skipped = parent_skipped or tag in SKIP_TAGS or bool(classes & SKIP_CLASSES)
        if tag == "main":
            self.has_main = True
        self._stack.append((in_main, skipped, in_body, tag))

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        # Void elements do not contain editorial text.
        return

    def handle_endtag(self, tag: str) -> None:
        # Pop to the matching tag so one malformed nested element does not poison
        # the rest of the count.
        for index in range(len(self._stack) - 1, -1, -1):
            if self._stack[index][3] == tag:
                del self._stack[index:]
                return

    def handle_data(self, data: str) -> None:
        if not self._stack:
            return
        in_main, skipped, in_body, _ = self._stack[-1]
        if skipped:
            return
        if in_main:
            self.main_text.append(data)
        if in_body:
            self.body_text.append(data)

    def editorial_text(self) -> str:
        chunks = self.main_text if self.has_main else self.body_text
        return " ".join(chunks)


def count_page(path: Path, root: Path, minimum: int) -> PageResult:
    parser = EditorialTextParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    words = len(WORD_RE.findall(parser.editorial_text()))
    return PageResult(
        path=path.relative_to(root).as_posix(),
        words=words,
        passes=words >= minimum,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check every public HTML page against the Somnarak editorial word floor."
    )
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path("docs"),
        help="public HTML root (default: docs)",
    )
    parser.add_argument(
        "--minimum",
        type=int,
        default=200,
        help="minimum meaningful editorial words per page (default: 200)",
    )
    parser.add_argument(
        "--json-output",
        type=Path,
        help="optionally write the complete audit as JSON",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"error: public root does not exist: {root}", file=sys.stderr)
        return 2
    if args.minimum < 1:
        print("error: --minimum must be at least 1", file=sys.stderr)
        return 2

    pages = sorted(root.rglob("*.html"))
    results = [count_page(path, root, args.minimum) for path in pages]
    failures = sorted(
        (result for result in results if not result.passes),
        key=lambda result: (result.words, result.path),
    )

    print(
        f"Somnarak editorial word-floor audit: {len(results)} pages, "
        f"minimum {args.minimum} words"
    )
    if failures:
        print(f"FAIL: {len(failures)} page(s) below the floor")
        for result in failures:
            print(f"  {result.words:4d}  {result.path}")
    else:
        minimum_result = min(results, key=lambda result: result.words) if results else None
        print("PASS: every public HTML page meets the floor")
        if minimum_result:
            print(
                f"Lowest qualifying page: {minimum_result.path} "
                f"({minimum_result.words} words)"
            )

    if args.json_output:
        report = {
            "result": "PASS" if not failures else "FAIL",
            "minimum_words": args.minimum,
            "count_scope": "Primary page content excluding shared navigation and interface chrome",
            "html_pages": len(results),
            "pages_below_floor": len(failures),
            "pages": [asdict(result) for result in results],
        }
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"JSON report: {args.json_output}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
