#!/usr/bin/env python3
"""Render and verify the canonical Somnarak top bar on every public HTML page.

The wiki is static, so the shared navigation is intentionally expanded into each
HTML file. This tool keeps that repeated component, its relative destinations,
and its CSS/JavaScript cache versions synchronized.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

ASSET_VERSION = "20260901b"

# key, primary label, terminal sublabel, route, Directorate slot
NAV_ITEMS = (
    ("main", "Main", "Terminal", "index.html", "00"),
    ("characters", "Characters", "Echo-Cores", "characters/index.html", "01"),
    ("lore", "Lore", "Cycles", "lore/index.html", "02"),
    ("atlas", "Atlas", "City", "locations/index.html", "03"),
    ("factions", "Factions", "Orders", "factions/index.html", "04"),
    ("facility", "Facility", "Floors", "departments/index.html", "05"),
    ("entities", "Entities", "SECC", "entities/index.html", "06"),
    ("maw", "M.A.W.", "Arsenal", "maw/index.html", "07"),
    ("mechanics", "Mechanics", "Systems", "mechanics/index.html", "08"),
    ("downloads", "Downloads", "Files", "downloads.html", "09"),
)

TOP_BAR_RE = re.compile(
    r'<header\b[^>]*\bclass=["\'][^"\']*\butility\b[^"\']*["\'][^>]*>.*?</header>',
    re.IGNORECASE | re.DOTALL,
)
CSS_RE = re.compile(
    r'(?P<before><link\b[^>]*\bhref=["\'])(?P<path>[^"\']*assets/css/wiki\.css)'
    r'(?:\?[^"\']*)?(?P<after>["\'][^>]*>)',
    re.IGNORECASE,
)
JS_RE = re.compile(
    r'(?P<before><script\b[^>]*\bsrc=["\'])(?P<path>[^"\']*assets/js/wiki\.js)'
    r'(?:\?[^"\']*)?(?P<after>["\'][^>]*>)',
    re.IGNORECASE,
)


@dataclass(frozen=True)
class TopBarIssue:
    page: str
    kind: str
    detail: str


def page_prefix(path: Path, root: Path) -> str:
    """Return a relative prefix from ``path`` to the public ``root``."""
    relative = path.resolve().relative_to(root.resolve())
    depth = len(relative.parent.parts) if relative.parent != Path(".") else 0
    return "../" * depth


def current_archive(path: Path, root: Path) -> str | None:
    """Map a public route to the primary archive represented in the top bar."""
    relative = path.resolve().relative_to(root.resolve())
    route = relative.as_posix()
    first = relative.parts[0]

    if route == "index.html":
        return "main"
    if route == "downloads.html" or route == "project/downloads.html":
        return "downloads"
    if route == "assets/icons/icons_gallery.html":
        return "downloads"

    return {
        "characters": "characters",
        "lore": "lore",
        "locations": "atlas",
        "atlas": "atlas",
        "factions": "factions",
        "departments": "facility",
        "entities": "entities",
        "maw": "maw",
        "mechanics": "mechanics",
    }.get(first)


def render_top_bar(path: Path, root: Path) -> str:
    prefix = page_prefix(path, root)
    current = current_archive(path, root)
    links: list[str] = []
    for key, label, sublabel, route, slot in NAV_ITEMS:
        state = ' class="is-current" aria-current="page"' if key == current else ""
        links.append(
            f'      <a href="{prefix}{route}" data-archive="{slot}"{state}>'
            f'<span>{label}</span><small>{sublabel}</small></a>'
        )

    return f'''<header class="utility" data-component="global-top-bar">
  <div class="utility-left">
    <button class="nav-open" type="button" aria-controls="primary-archive-navigation" aria-expanded="false" aria-label="Open primary archive navigation">
      <span class="nav-open-glyph" aria-hidden="true"><i></i><i></i><i></i></span>
      <span class="nav-open-text">MENU</span>
    </button>
    <a class="utility-brand" href="{prefix}index.html" aria-label="Somnarak Wiki main page">
      <img src="{prefix}assets/icons/somnarak_icon.svg" width="34" height="34" alt=""/>
      <span class="utility-brand-copy"><b>SOMNARAK.WIKI</b><small>DIRECTORATE ARCHIVE</small></span>
    </a>
    <span class="utility-era"><i aria-hidden="true"></i><span>YEAR 4,238</span><b>DAWN INITIATIVE</b></span>
  </div>
  <nav class="utility-nav" id="primary-archive-navigation" aria-label="Primary archive">
{chr(10).join(links)}
  </nav>
  <div class="search" role="search">
    <label for="search"><span aria-hidden="true">⌕</span><span class="sr-only">Search Somnarak Wiki</span></label>
    <input id="search" type="search" aria-label="Search Somnarak Wiki" aria-controls="results" aria-expanded="false" data-index="{prefix}data/search.json" placeholder="Search the archive" autocomplete="off" spellcheck="false"/>
    <kbd aria-hidden="true">/</kbd>
    <div id="results" aria-live="polite"></div>
  </div>
</header>'''


def sync_asset_versions(text: str, prefix: str) -> str:
    """Update existing shared assets or add them to the standalone art gallery."""
    css = CSS_RE.search(text)
    if css:
        text = CSS_RE.sub(
            lambda match: (
                match.group("before")
                + match.group("path")
                + f"?v={ASSET_VERSION}"
                + match.group("after")
            ),
            text,
            count=1,
        )
    else:
        addition = f'  <link rel="stylesheet" href="{prefix}assets/css/wiki.css?v={ASSET_VERSION}">\n'
        text = text.replace("</head>", addition + "</head>", 1)

    js = JS_RE.search(text)
    if js:
        text = JS_RE.sub(
            lambda match: (
                match.group("before")
                + match.group("path")
                + f"?v={ASSET_VERSION}"
                + match.group("after")
            ),
            text,
            count=1,
        )
    else:
        addition = f'  <script defer src="{prefix}assets/js/wiki.js?v={ASSET_VERSION}"></script>\n'
        text = text.replace("</head>", addition + "</head>", 1)
    return text


def prepare_standalone_gallery(text: str) -> str:
    """Make the legacy standalone gallery compatible with the global shell."""
    text = re.sub(
        r'<body(?:\s+class=["\'][^"\']*["\'])?\s*>',
        '<body class="asset-gallery-page">',
        text,
        count=1,
        flags=re.IGNORECASE,
    )
    text = text.replace("    header {", "    .gallery-heading {", 1)
    text = re.sub(
        r'(<div\s+class=["\']container["\']>\s*)<header>',
        r'\1<header class="gallery-heading">',
        text,
        count=1,
        flags=re.IGNORECASE,
    )
    return text


def update_page(path: Path, root: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    text = original
    prefix = page_prefix(path, root)

    if path.resolve().relative_to(root.resolve()).as_posix() == "assets/icons/icons_gallery.html":
        text = prepare_standalone_gallery(text)

    expected = render_top_bar(path, root)
    match = TOP_BAR_RE.search(text)
    if match:
        text = text[: match.start()] + expected + text[match.end() :]
    else:
        text = re.sub(
            r'(<body\b[^>]*>)',
            lambda match: match.group(1) + "\n" + expected,
            text,
            count=1,
            flags=re.IGNORECASE,
        )

    text = sync_asset_versions(text, prefix)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def validate_top_bars(root: Path) -> list[TopBarIssue]:
    """Return all top-bar, shared-style, and shared-script consistency issues."""
    root = root.resolve()
    issues: list[TopBarIssue] = []
    for path in sorted(root.rglob("*.html")):
        label = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        matches = list(TOP_BAR_RE.finditer(text))
        if len(matches) != 1:
            issues.append(
                TopBarIssue(label, "top-bar-count", f"expected 1, found {len(matches)}")
            )
        elif matches[0].group(0) != render_top_bar(path, root):
            issues.append(
                TopBarIssue(label, "top-bar-drift", "markup, labels, links, or active state differ")
            )

        css = CSS_RE.search(text)
        if not css:
            issues.append(TopBarIssue(label, "top-bar-css", "shared wiki stylesheet missing"))
        elif f"?v={ASSET_VERSION}" not in css.group(0):
            issues.append(TopBarIssue(label, "top-bar-css-version", css.group(0)))

        js = JS_RE.search(text)
        if not js:
            issues.append(TopBarIssue(label, "top-bar-js", "shared wiki script missing"))
        elif f"?v={ASSET_VERSION}" not in js.group(0):
            issues.append(TopBarIssue(label, "top-bar-js-version", js.group(0)))
    return issues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Synchronize or verify the canonical top bar across all public pages."
    )
    parser.add_argument(
        "root", nargs="?", type=Path, default=Path("docs"), help="public root (default: docs)"
    )
    parser.add_argument(
        "--write", action="store_true", help="rewrite drifted pages instead of only checking"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"error: public root does not exist: {root}")
        return 2

    if args.write:
        changed = sum(update_page(path, root) for path in sorted(root.rglob("*.html")))
        print(f"Synchronized global top bar: {changed} of {len(list(root.rglob('*.html')))} pages updated")

    issues = validate_top_bars(root)
    if issues:
        print(f"FAIL: {len(issues)} top-bar consistency issue(s)")
        for issue in issues:
            print(f"  {issue.page}: {issue.kind}: {issue.detail}")
        if not args.write:
            print("Run with --write to synchronize the static pages.")
        return 1

    print(
        f"PASS: canonical top-bar labels, destinations, active states, search paths, and assets "
        f"match across {len(list(root.rglob('*.html')))} pages"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
