#!/usr/bin/env python3
"""Render and verify the canonical homepage left sidebar on every public page.

Somnarak is a static archive, so shared chrome is expanded into each HTML file.
This tool makes the homepage rail authoritative, adjusts paths by page depth,
marks the relevant archive/current record, and rejects sidebar drift.
"""

from __future__ import annotations

import argparse
import re

VERIFY_RE = re.compile(r"^(?:google|bing|yandex|facebook|twitter)[0-9a-zA-Z]{10,}\.(?:html|txt)$", re.I)
from dataclasses import dataclass
from html import escape
from pathlib import Path

try:  # Support direct execution and package-style imports.
    from .sync_global_top_bar import current_archive, page_prefix
except ImportError:
    from sync_global_top_bar import current_archive, page_prefix

# key, rail code, label, descriptor, route, accent
HUB_ITEMS = (
    ("main", "00", "Main Overview", "Release terminal", "index.html", "#f1df76"),
    ("entities", "06", "Sorrow Entities", "SECC registry", "entities/index.html", "#fb7185"),
    ("maw", "07", "M.A.W. Armory", "Materialized agony", "maw/index.html", "#f1df76"),
    ("characters", "01", "Echo-Cores & Cast", "Personnel index", "characters/index.html", "#c084fc"),
    ("facility", "05", "Hand of Change", "Facility 01", "departments/index.html", "#71efaf"),
    ("factions", "04", "Factions & Guilds", "Orders and syndicates", "factions/index.html", "#f59e0b"),
    ("atlas", "03", "Atlas & Maps", "Five city zones", "locations/index.html", "#38bdf8"),
    ("lore", "02", "Lore & Cosmology", "The 1,778 Cycles", "lore/index.html", "#a78bfa"),
    ("mechanics", "08", "Battle Mechanics", "Han systems", "mechanics/index.html", "#60a5fa"),
)

# rail code, label, role, route, accent
CORE_ITEMS = (
    ("C01", "Majin", "Director", "characters/the-director-majin.html", "#f1df76"),
    ("C02", "Seiyon", "Secretary", "characters/the-secretary-seiyon.html", "#e2e8f0"),
    ("C03", "Dekan", "Containment", "characters/the-containment-lead-dekan.html", "#ef5b55"),
    ("C04", "Zyrak", "Extraction", "characters/the-extraction-lead-zyrak.html", "#fb923c"),
    ("C05", "Ayshuk", "Research", "characters/the-research-lead-ayshuk.html", "#38bdf8"),
    ("C06", "Mellda", "Border", "characters/the-border-lead-mellda.html", "#71efaf"),
    ("C07", "Marjuk", "Archive", "characters/the-archive-lead-marjuk.html", "#a78bfa"),
    ("C08", "Ishall", "Shadow Corps", "characters/the-outsider-ishall.html", "#94a3b8"),
    ("C09", "Xyan", "Gate Watch", "characters/the-exile-xyan.html", "#fb7185"),
)

# rail code, label, descriptor, route, accent
UTILITY_ITEMS = (
    ("M01", "Facility 01 Map", "Hand cutaway", "atlas/hand-of-change-map.html", "#71efaf"),
    ("M02", "Somnarak City Map", "Five-zone blueprint", "atlas/somnarak-city-map.html", "#38bdf8"),
    ("R01", "Offline Archives", "Download center", "downloads.html", "#f1df76"),
)

LEFT_RAIL_RE = re.compile(
    r'<aside\b(?=[^>]*\bclass=["\'][^"\']*\bleft-rail\b[^"\']*["\'])[^>]*>.*?</aside>',
    re.IGNORECASE | re.DOTALL,
)
GLOBAL_LEFT_RAIL_RE = re.compile(
    r'<aside\b(?=[^>]*\bclass=["\'][^"\']*\bleft-rail\b[^"\']*["\'])'
    r'(?=[^>]*\bdata-component=["\']global-left-sidebar["\'])[^>]*>.*?</aside>',
    re.IGNORECASE | re.DOTALL,
)
LEGACY_TALE_RAIL_RE = re.compile(
    r'<aside\b[^>]*\bclass=["\']rail["\'][^>]*>.*?</aside>',
    re.IGNORECASE | re.DOTALL,
)


@dataclass(frozen=True)
class LeftSidebarIssue:
    page: str
    kind: str
    detail: str


def relative_route(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def link_state(path: Path, root: Path, route: str, archive_key: str | None = None) -> str:
    """Return exact-page or parent-archive state for a canonical rail link."""
    current_route = relative_route(path, root)
    if current_route == route:
        return ' class="is-current" aria-current="page"'
    if archive_key and current_archive(path, root) == archive_key:
        return ' class="is-archive-current" aria-current="location"'
    if route == "downloads.html" and current_archive(path, root) == "downloads":
        return ' class="is-archive-current" aria-current="location"'
    return ""


def render_link(
    *,
    path: Path,
    root: Path,
    code: str,
    label: str,
    descriptor: str,
    route: str,
    accent: str,
    archive_key: str | None = None,
) -> str:
    prefix = page_prefix(path, root)
    state = link_state(path, root, route, archive_key)
    return (
        f'          <a href="{prefix}{route}" data-rail-code="{code}" '
        f'style="--rail-accent:{accent}"{state}>'
        f'<span><b>{escape(label)}</b><small>{escape(descriptor)}</small></span>'
        f'<i aria-hidden="true"></i></a>'
    )


def render_left_sidebar(path: Path, root: Path) -> str:
    prefix = page_prefix(path, root)
    hubs = "\n".join(
        render_link(
            path=path,
            root=root,
            code=code,
            label=label,
            descriptor=descriptor,
            route=route,
            accent=accent,
            archive_key=key,
        )
        for key, code, label, descriptor, route, accent in HUB_ITEMS
    )
    cores = "\n".join(
        render_link(
            path=path,
            root=root,
            code=code,
            label=label,
            descriptor=role,
            route=route,
            accent=accent,
        )
        for code, label, role, route, accent in CORE_ITEMS
    )
    utilities = "\n".join(
        render_link(
            path=path,
            root=root,
            code=code,
            label=label,
            descriptor=descriptor,
            route=route,
            accent=accent,
        )
        for code, label, descriptor, route, accent in UTILITY_ITEMS
    )

    return f'''<aside class="left-rail" data-component="global-left-sidebar" aria-label="Wiki navigation">
  <div class="left-rail-frame">
    <div class="rail-signal" aria-hidden="true">
      <span><i></i> PUBLIC NETWORK</span><b>NODE RD-01</b>
    </div>

    <div class="site-mark">
      <a href="{prefix}index.html" aria-label="Somnarak Wiki main overview">
        <span class="site-mark-emblem"><img src="{prefix}assets/icons/somnarak_icon.svg" width="104" height="104" alt=""/></span>
        <span class="site-mark-copy"><b>SOMNARAK</b><small>OFFICIAL WIKI ARCHIVE</small></span>
      </a>
      <p>CITY OF UNRESOLVED SORROW</p>
    </div>

    <div class="rail-classification" aria-label="Archive era">
      <span>YEAR 4,238</span><b>DAWN INITIATIVE</b>
    </div>

    <nav class="left-links" aria-label="Somnarak archive directory">
      <section class="rail-nav-section" data-rail-group="archives">
        <header><span>01</span><div><h2>DATABASE HUBS</h2><small>PRIMARY ARCHIVE MATRIX</small></div></header>
        <div class="rail-link-stack">
{hubs}
        </div>
      </section>

      <section class="rail-nav-section" data-rail-group="cores">
        <header><span>02</span><div><h2>THE NINE ECHO-CORES</h2><small>DIRECTORATE PERSONNEL</small></div></header>
        <div class="rail-link-stack">
{cores}
        </div>
      </section>

      <section class="rail-nav-section" data-rail-group="maps">
        <header><span>03</span><div><h2>CARTOGRAPHY</h2><small>SCHEMATICS &amp; FILES</small></div></header>
        <div class="rail-link-stack">
{utilities}
        </div>
      </section>
    </nav>

    <div class="rail-status" aria-label="Current archive release">
      <span><i aria-hidden="true"></i> ARCHIVE ONLINE</span>
      <strong>1.9.0</strong>
      <small>1,041 PUBLIC RECORDS // CYCLE ENDED</small>
    </div>
  </div>
</aside>'''


def prepare_entity_tales(text: str) -> str:
    """Bring the one legacy anthology shell into the same two-column contract."""
    text = re.sub(
        r'<div\s+class=["\']layout["\']>',
        '<div class="wiki-shell tale-shell">',
        text,
        count=1,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r'<main\s+class=["\']content["\']>',
        '<main class="content tale-main" id="content">',
        text,
        count=1,
        flags=re.IGNORECASE,
    )
    return text


def insert_gallery_sidebar(text: str, expected: str) -> str:
    """Wrap the standalone icon repository in the public sidebar shell."""
    opening = re.search(r'<div\s+class=["\']container["\']>', text, re.IGNORECASE)
    footer = text.find('<footer class="wiki-footer')
    container_close = text.rfind("</div>", 0, footer) if footer != -1 else -1
    if not opening or container_close == -1 or container_close <= opening.end():
        return text

    replacement = (
        '<div class="wiki-shell gallery-shell">\n'
        + expected
        + '\n  <main class="container gallery-main" id="content">'
    )
    return (
        text[: opening.start()]
        + replacement
        + text[opening.end() : container_close]
        + "</main>\n</div>"
        + text[container_close + len("</div>") :]
    )


def update_page(path: Path, root: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    text = original
    route = relative_route(path, root)
    expected = render_left_sidebar(path, root)

    left_matches = list(LEFT_RAIL_RE.finditer(text))
    if left_matches:
        # Drifted pages historically contain one rail. Replacing all also repairs
        # accidental duplicates, and validation below enforces exactly one.
        text = LEFT_RAIL_RE.sub(expected, text)
    elif route == "lore/entity-tales.html" and LEGACY_TALE_RAIL_RE.search(text):
        text = prepare_entity_tales(text)
        text = LEGACY_TALE_RAIL_RE.sub(expected, text, count=1)
    elif route == "assets/icons/icons_gallery.html":
        text = insert_gallery_sidebar(text, expected)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def validate_left_sidebars(root: Path) -> list[LeftSidebarIssue]:
    """Return every missing, duplicate, or drifted global left-sidebar issue."""
    root = root.resolve()
    issues: list[LeftSidebarIssue] = []
    for path in (p for p in sorted(root.rglob("*.html")) if not VERIFY_RE.match(p.name)):
        label = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        all_rails = list(LEFT_RAIL_RE.finditer(text))
        canonical = list(GLOBAL_LEFT_RAIL_RE.finditer(text))
        if len(all_rails) != 1:
            issues.append(
                LeftSidebarIssue(label, "left-sidebar-count", f"expected 1, found {len(all_rails)}")
            )
            continue
        if len(canonical) != 1:
            issues.append(
                LeftSidebarIssue(label, "left-sidebar-component", "sidebar is not canonical global chrome")
            )
            continue
        if canonical[0].group(0) != render_left_sidebar(path, root):
            issues.append(
                LeftSidebarIssue(
                    label,
                    "left-sidebar-drift",
                    "identity, groups, labels, destinations, or active state differ",
                )
            )
    return issues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Synchronize or verify the homepage left sidebar across all public pages."
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

    html_files = [p for p in sorted(root.rglob("*.html")) if not VERIFY_RE.match(p.name)]
    if args.write:
        changed = sum(update_page(path, root) for path in html_files)
        print(f"Synchronized global left sidebar: {changed} of {len(html_files)} pages updated")

    issues = validate_left_sidebars(root)
    if issues:
        print(f"FAIL: {len(issues)} left-sidebar consistency issue(s)")
        for issue in issues:
            print(f"  {issue.page}: {issue.kind}: {issue.detail}")
        if not args.write:
            print("Run with --write to synchronize the static pages.")
        return 1

    print(
        f"PASS: homepage identity, archive groups, labels, destinations, and active states match "
        f"across {len(html_files)} left sidebars"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
