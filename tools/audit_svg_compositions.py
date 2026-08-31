#!/usr/bin/env python3
"""Validate SVG XML and detect recolor-only page-art compositions.

The uniqueness scan is deliberately limited to ``docs/assets/art``: that directory
contains editorial, page-facing artwork. Other asset directories include shared UI
controls and intentional deployment aliases, for which byte-level reuse is normal.

A structural signature discards paint, labels, IDs, and descriptive metadata while
retaining geometry, element order, transforms, dimensions, and text placement. Two
assets with the same signature therefore have the same underlying composition even
when their colors or labels differ. Same-subject filename aliases are reported but
allowed; matching compositions assigned to different subjects fail the audit.

Page coverage is a triage gate, not a claim about artistic merit: each HTML file must
contain inline SVG or reference at least one local SVG used by no more than the
configured number of pages. This filters sitewide chrome; the binding manual review
still decides whether the candidate actually derives from the page and source.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

PAINT_ATTRIBUTES = {
    "color",
    "fill",
    "fill-opacity",
    "flood-color",
    "flood-opacity",
    "lighting-color",
    "opacity",
    "stop-color",
    "stop-opacity",
    "stroke",
    "stroke-opacity",
}
SEMANTIC_ATTRIBUTES = {
    "aria-describedby",
    "aria-label",
    "aria-labelledby",
    "class",
    "id",
    "role",
}
METADATA_ELEMENTS = {"desc", "metadata", "title"}
PAINT_STYLE_PROPERTIES = PAINT_ATTRIBUTES | {
    "background",
    "background-color",
    "box-shadow",
    "filter",
    "text-shadow",
}
ROLE_TOKENS = {"avatar", "banner", "background", "icon", "profile", "diagram", "map"}
GENERIC_TOKENS = {"art", "entity", "hero", "image", "img", "styled", "visual"}
URL_REFERENCE_RE = re.compile(r"url\(#[^)]+\)", re.IGNORECASE)
SE_SUBJECT_RE = re.compile(r"(?:^|[_-])se[_-]?(\d{3})(?:[_-]|$)", re.IGNORECASE)
TOKEN_RE = re.compile(r"[a-z]+|\d+")


class PageVisualParser(HTMLParser):
    """Collect inline and locally referenced SVG candidates from one HTML page."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.has_inline_svg = False
        self.local_svg_paths: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "svg":
            self.has_inline_svg = True
        candidates = []
        if tag in {"img", "script", "source"}:
            candidates.append(attributes.get("src"))
        elif tag in {"a", "link", "use"}:
            candidates.append(attributes.get("href"))
        elif tag == "object":
            candidates.append(attributes.get("data"))
        for candidate in candidates:
            if not candidate:
                continue
            split = urlsplit(candidate)
            if not split.scheme and not split.netloc and split.path.lower().endswith(".svg"):
                self.local_svg_paths.append(unquote(split.path))

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self.handle_starttag(tag, attrs)


def local_name(name: str) -> str:
    """Remove an ElementTree namespace from a tag or attribute name."""

    return name.rsplit("}", 1)[-1]


def normalize_style(value: str) -> str:
    """Drop paint-only declarations while preserving structural CSS declarations."""

    retained: list[tuple[str, str]] = []
    for declaration in value.split(";"):
        if ":" not in declaration:
            continue
        name, raw_value = declaration.split(":", 1)
        name = name.strip().lower()
        if name in PAINT_STYLE_PROPERTIES:
            continue
        normalized_value = URL_REFERENCE_RE.sub("url(#REF)", " ".join(raw_value.split()))
        retained.append((name, normalized_value))
    return ";".join(f"{name}:{raw_value}" for name, raw_value in sorted(retained))


def structural_signature(element: ET.Element) -> tuple[Any, ...] | None:
    """Return a hashable, paint- and label-insensitive element representation."""

    tag = local_name(element.tag)
    if tag in METADATA_ELEMENTS:
        return None

    attributes: list[tuple[str, str]] = []
    for raw_name, raw_value in element.attrib.items():
        name = local_name(raw_name)
        if name in PAINT_ATTRIBUTES or name in SEMANTIC_ATTRIBUTES:
            continue
        if name == "style":
            value = normalize_style(raw_value)
            if not value:
                continue
        else:
            value = " ".join(raw_value.split())
            value = URL_REFERENCE_RE.sub("url(#REF)", value)
            if name in {"href", "xlink:href"} and value.startswith("#"):
                value = "#REF"
        attributes.append((name, value))

    children = tuple(
        signature
        for child in element
        if (signature := structural_signature(child)) is not None
    )
    # Text labels are intentionally omitted. The <text> element and its placement
    # attributes remain, allowing title-swapped templates to be detected.
    return tag, tuple(sorted(attributes)), children


def composition_hash(path: Path) -> str:
    root = ET.parse(path).getroot()
    signature = structural_signature(root)
    return hashlib.sha256(repr(signature).encode("utf-8")).hexdigest()


def asset_identity(path: Path) -> tuple[str, str]:
    """Infer a subject and visual role from a curated-art filename."""

    stem = path.stem.lower()
    se_match = SE_SUBJECT_RE.search(stem)
    subject = f"se-{se_match.group(1)}" if se_match else ""

    tokens = TOKEN_RE.findall(stem)
    role = next((token for token in tokens if token in ROLE_TOKENS), "art")
    if not subject:
        subject_tokens = [
            token
            for token in tokens
            if token not in ROLE_TOKENS and token not in GENERIC_TOKENS
        ]
        subject = "-".join(subject_tokens) or stem
    return subject, role


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate Somnarak SVG XML and reject cross-subject recolor templates."
    )
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path("docs/assets"),
        help="asset root containing SVG files (default: docs/assets)",
    )
    parser.add_argument(
        "--art-root",
        type=Path,
        default=Path("docs/assets/art"),
        help="curated page-art root for composition comparison",
    )
    parser.add_argument(
        "--html-root",
        type=Path,
        default=Path("docs"),
        help="public HTML root for page-level SVG coverage (default: docs)",
    )
    parser.add_argument(
        "--shared-use-threshold",
        type=int,
        default=20,
        help="maximum page reuse for an SVG to count as a page-visual candidate (default: 20)",
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
    art_root = args.art_root.resolve()
    html_root = args.html_root.resolve()
    if not root.is_dir() or not art_root.is_dir() or not html_root.is_dir():
        print("error: SVG, curated-art, or public HTML root does not exist", file=sys.stderr)
        return 2
    if args.shared_use_threshold < 1:
        print("error: --shared-use-threshold must be at least 1", file=sys.stderr)
        return 2

    svg_files = sorted(root.rglob("*.svg"))
    malformed: list[dict[str, str]] = []
    for path in svg_files:
        try:
            ET.parse(path)
        except (ET.ParseError, OSError) as error:
            malformed.append(
                {"path": path.relative_to(root).as_posix(), "error": str(error)}
            )

    art_files = sorted(art_root.rglob("*.svg"))
    groups: dict[str, list[Path]] = defaultdict(list)
    if not malformed:
        for path in art_files:
            groups[composition_hash(path)].append(path)

    alias_groups: list[list[str]] = []
    cross_subject_groups: list[list[str]] = []
    for paths in groups.values():
        if len(paths) < 2:
            continue
        relative_paths = [path.relative_to(art_root).as_posix() for path in paths]
        identities = {asset_identity(path) for path in paths}
        if len(identities) == 1:
            alias_groups.append(relative_paths)
        else:
            cross_subject_groups.append(relative_paths)

    alias_groups.sort(key=lambda group: group[0])
    cross_subject_groups.sort(key=lambda group: group[0])

    html_files = sorted(html_root.rglob("*.html"))
    page_visuals: dict[Path, PageVisualParser] = {}
    svg_usage: dict[Path, set[Path]] = defaultdict(set)
    for page in html_files:
        parser = PageVisualParser()
        parser.feed(page.read_text(encoding="utf-8", errors="replace"))
        page_visuals[page] = parser
        for raw_path in parser.local_svg_paths:
            svg_path = (page.parent / raw_path).resolve()
            svg_usage[svg_path].add(page)

    pages_without_visual_candidate: list[str] = []
    for page, parser in page_visuals.items():
        has_low_reuse_asset = any(
            len(svg_usage[(page.parent / raw_path).resolve()])
            <= args.shared_use_threshold
            for raw_path in parser.local_svg_paths
        )
        if not parser.has_inline_svg and not has_low_reuse_asset:
            pages_without_visual_candidate.append(page.relative_to(html_root).as_posix())

    passed = (
        not malformed
        and not cross_subject_groups
        and not pages_without_visual_candidate
    )

    print(
        f"Somnarak SVG audit: {len(svg_files)} XML files; "
        f"{len(art_files)} curated page-art compositions"
    )
    print(
        f"Page visual coverage: {len(html_files)} HTML files; "
        f"shared-use threshold {args.shared_use_threshold} pages"
    )
    if malformed:
        print(f"FAIL: {len(malformed)} malformed SVG file(s)")
        for item in malformed:
            print(f"  {item['path']}: {item['error']}")
    if cross_subject_groups:
        print(
            "FAIL: "
            f"{len(cross_subject_groups)} cross-subject paint/text-only duplicate group(s)"
        )
        for group in cross_subject_groups:
            print("  " + " | ".join(group))
    if pages_without_visual_candidate:
        print(
            "FAIL: "
            f"{len(pages_without_visual_candidate)} page(s) have only widely shared SVG chrome"
        )
        for page in pages_without_visual_candidate:
            print(f"  {page}")
    if passed:
        print(
            "PASS: SVG XML, page-level visual coverage, and cross-subject "
            "composition checks pass"
        )
    print(f"Allowed same-subject alias groups: {len(alias_groups)}")

    if args.json_output:
        report = {
            "result": "PASS" if passed else "FAIL",
            "svg_files": len(svg_files),
            "curated_art_files": len(art_files),
            "html_pages": len(html_files),
            "page_visual_shared_use_threshold": args.shared_use_threshold,
            "pages_without_visual_candidate": pages_without_visual_candidate,
            "malformed_svg_files": malformed,
            "cross_subject_duplicate_groups": cross_subject_groups,
            "same_subject_alias_groups": alias_groups,
            "composition_scope": "docs/assets/art; paint, labels, IDs, and metadata ignored",
            "coverage_scope": "inline SVG or a local SVG referenced by no more than the shared-use threshold; manual source-relevance review remains required",
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
