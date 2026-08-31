#!/usr/bin/env python3
"""Render and verify one canonical Somnarak footer on every public HTML page.

The footer now carries three per-page data rows on top of the shared chrome:

1. A FILED UNDER strip (section gateway, wiki registry code, source reference
   code / designation, and the Korean name) joined from REFERENCE_SOMNARAK_WIKI.
2. A Random Archive action button (routed client-side by wiki.js).
3. A last-verified stamp in the publication register.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

try:  # Support direct execution and package-style imports.
    from .sync_global_top_bar import ASSET_VERSION, page_prefix
except ImportError:
    from sync_global_top_bar import ASSET_VERSION, page_prefix

BOTTOM_BAR_RE = re.compile(
    r'<footer\b[^>]*\bdata-component=["\']global-bottom-bar["\'][^>]*>.*?</footer>',
    re.IGNORECASE | re.DOTALL,
)
ANY_FOOTER_RE = re.compile(r'<footer\b[^>]*>.*?</footer>', re.IGNORECASE | re.DOTALL)

LAST_VERIFIED = "2026-09-01"

_ENTITY_PAGE_RE = re.compile(r"^se-(\d{3})-(.+)$")
_MAW_PAGE_RE = re.compile(r"^maw-([WSGwsg])-(\d{3})-(\d{2})-(.+)$")
_CODE_PREFIXES = ("SE-", "HT-", "MAW-", "ORDEAL")
_HANGUL_RE = re.compile(r"[\uac00-\ud7a3]")


@dataclass(frozen=True)
class BottomBarIssue:
    page: str
    kind: str
    detail: str


# ---------------------------------------------------------------------------
# Reference join: map a public page to its REFERENCE_SOMNARAK_WIKI source file
# ---------------------------------------------------------------------------


def _is_hangul(token: str) -> bool:
    return bool(_HANGUL_RE.search(token))


@lru_cache(maxsize=None)
def _reference_entries() -> tuple:
    """Index every reference markdown file.

    Returns tuples of (name_tokens, codes, hangul, path).
    """
    entries: list[tuple] = []
    ref_root = Path(__file__).resolve().parent.parent / "REFERENCE_SOMNARAK_WIKI"
    if not ref_root.is_dir():
        return tuple(entries)
    for path in ref_root.rglob("*.md"):
        stem = path.stem
        head, sep, tail = stem.partition("__")
        parts = [head, *tail.split("_")] if sep else stem.split("_")
        hangul = " ".join(p for p in parts if _is_hangul(p))
        ascii_parts = [p for p in parts if not _is_hangul(p)]
        codes = [
            p
            for p in ascii_parts
            if p.upper().startswith(_CODE_PREFIXES) or p.upper() in ("MAW-W", "MAW-S", "MAW-G")
        ]
        name_tokens = frozenset(p.lower() for p in ascii_parts if p not in codes)
        if not name_tokens:
            continue
        entries.append((name_tokens, tuple(codes), hangul, path.as_posix()))
    return tuple(entries)


def _best_match(
    name_tokens: frozenset,
    section_filter: tuple[str, ...],
    require_code: str | None = None,
    set_hint: str | None = None,
) -> tuple[tuple[str, ...], str] | None:
    """Pick the unique best reference file for a page's name tokens.

    When set_hint is given it is a hard constraint: the reference path must
    contain an exact path segment equal to the set number (e.g. "004"), so a
    set-004 page can never be joined to a set-1014 file that merely shares
    generic name words.
    """
    if not name_tokens:
        return None
    scored: list[tuple] = []
    for tokens, codes, hangul, where in _reference_entries():
        if not any(part in where for part in section_filter):
            continue
        if require_code and require_code.upper() not in tuple(c.upper() for c in codes):
            continue
        if set_hint:
            segments = set(where.split("/"))
            segments.update(part for seg in where.split("/") for part in seg.split("_"))
            if set_hint not in segments:
                continue
        shared = len(name_tokens & tokens)
        if shared < min(2, len(name_tokens)):
            continue
        scored.append((shared, where, codes, hangul))
    if not scored:
        return None
    scored.sort(key=lambda item: (-item[0], item[1]))
    top = [item for item in scored if item[0] == scored[0][0]]
    if len(top) != 1:
        return None
    return top[0][2], top[0][3]


def _filing_strip(path: Path, root: Path) -> str:
    """Render the per-page FILED UNDER strip inside the footer."""
    rel = path.relative_to(root).as_posix()
    parts = rel.split("/")
    top = parts[0] if len(parts) > 1 else path.stem
    sections = {
        "index": ("MAIN ARCHIVE", "index.html"),
        "404": ("SIGNAL LOST", "index.html"),
        "characters": ("01 · ECHO-CORES", "characters/index.html"),
        "lore": ("02 · CYCLE ARCHIVE", "lore/index.html"),
        "locations": ("03 · CITY ATLAS", "locations/index.html"),
        "factions": ("04 · ORDERS", "factions/index.html"),
        "departments": ("05 · HAND OF CHANGE", "departments/index.html"),
        "entities": ("06 · SECC REGISTRY", "entities/index.html"),
        "maw": ("07 · M.A.W. ARSENAL", "maw/index.html"),
        "mechanics": ("08 · SYSTEMS CODEX", "mechanics/index.html"),
        "project": ("PROVENANCE", "project/source-map.html"),
    }
    label, hub = sections.get(top, ("PUBLIC CODEX", "index.html"))
    prefix = page_prefix(path, root)
    extras: list[str] = []
    stem = path.stem

    entity_match = _ENTITY_PAGE_RE.match(stem)
    maw_match = _MAW_PAGE_RE.match(stem)
    if top == "entities" and entity_match:
        extras.append(f'<code class="footer-filed-code">SE-{entity_match.group(1)}</code>')
        match = _best_match(
            frozenset(entity_match.group(2).split("-")),
            ("01_Sorrow_Entities", "02_Hope_Transformation", "03_Unknown_Entities"),
        )
        if match:
            codes, hangul = match
            name = entity_match.group(2).split("-")
            extras.append(f'<span class="footer-filed-name">{" ".join(name)}</span>')
            if hangul:
                extras.append(f'<span class="footer-filed-ko">{hangul}</span>')
            if codes:
                designation = codes[0][3:] if codes[0].startswith("SE-") else codes[0]
                extras.append(f'<code class="footer-filed-src">DESIGNATION {designation}</code>')
    elif top == "maw" and maw_match:
        mtype, mset, mvar, rest = (
            maw_match.group(1).upper(),
            maw_match.group(2),
            maw_match.group(3),
            maw_match.group(4),
        )
        extras.append(f'<code class="footer-filed-code">MAW-{mtype}-{mset}-{mvar}</code>')
        match = _best_match(
            frozenset(rest.split("-")),
            ("M.A.W. Codex_Set Registry",),
            require_code=f"MAW-{mtype}",
            set_hint=mset,
        )
        if match:
            codes, hangul = match
            extras.append(f'<span class="footer-filed-name">{" ".join(rest.split("-"))}</span>')
            if hangul:
                extras.append(f'<span class="footer-filed-ko">{hangul}</span>')
            parent = next((c for c in codes if not c.startswith("MAW-")), None)
            if parent:
                extras.append(f'<code class="footer-filed-src">ITEM ID {parent}</code>')

    extra_html = "".join(extras)
    return (
        f'<div class="footer-filed" aria-label="Filing record">'
        f'<span class="footer-filed-tag">FILED UNDER</span>'
        f'<a class="footer-filed-section" href="{prefix}{hub}">{label}</a>'
        f"{extra_html}"
        f"</div>"
    )


def render_bottom_bar(path: Path, root: Path) -> str:
    prefix = page_prefix(path, root)
    filed = _filing_strip(path, root)
    return f'''<footer class="wiki-footer global-footer" data-component="global-bottom-bar">
  {filed}
  <div class="footer-signal" aria-hidden="true">
    <span>RD://PUBLIC-NET</span><i></i>
    <span>SECC LINK STABLE</span><i></i>
    <span>FACILITY 01 // GATE WATCH</span><i></i>
    <span>PUBLICATION GATES PASSING</span>
  </div>

  <div class="footer-hero">
    <section class="footer-identity" aria-label="Somnarak Wiki">
      <span class="footer-kicker">CITY OF UNRESOLVED SORROW // YEAR 4,238</span>
      <a class="footer-brand" href="{prefix}index.html">
        <span class="footer-emblem"><img src="{prefix}assets/icons/somnarak_icon.svg" width="78" height="78" alt=""/></span>
        <span><b>SOMNARAK</b><small>OFFICIAL WIKI ARCHIVE</small></span>
      </a>
      <h2>Witness the sorrow.<br/><em>Preserve the name.</em></h2>
      <p>The public record follows Somnarak from the Alpha Tree and five city zones into Facility 01, where witnessed canon is curated without replacing absence with invention.</p>
      <div class="footer-badges" aria-label="Archive classification">
        <span>FACILITY 01</span><span>DIRECTORATE</span><span>PUBLIC CODEX</span>
      </div>
    </section>

    <figure class="footer-network">
      <div class="footer-network-frame">
        <img src="{prefix}assets/layout/footer-directorate-network.svg" alt="Directorate archive topology linking the Alpha Tree, five city zones, Facility 01, Gate Watch, and eight public archive gateways"/>
        <span class="footer-network-scan" aria-hidden="true"></span>
      </div>
      <figcaption><span>Live archive topology</span><b>ALPHA TREE → FACILITY 01 → PUBLIC CODEX</b></figcaption>
    </figure>

    <section class="footer-status" aria-label="Current archive status">
      <span>Verified repository snapshot</span>
      <strong>1.8.31</strong>
      <p><i aria-hidden="true"></i> ARCHIVE ONLINE</p>
      <dl>
        <div><dt>Public records</dt><dd>197 HTML</dd></div>
        <div><dt>Search corpus</dt><dd>196 ROUTES</dd></div>
        <div><dt>Current era</dt><dd>YEAR 4,238</dd></div>
        <div><dt>Cycle state</dt><dd>ENDED</dd></div>
        <div><dt>Gate command</dt><dd>XYAN</dd></div>
      </dl>
    </section>
  </div>

  <div class="footer-directory">
    <section class="footer-archives" aria-labelledby="footer-archives-title">
      <header><span>Primary collections</span><h2 id="footer-archives-title">Eight Archive Gateways</h2><p>Continue through the complete public taxonomy.</p></header>
      <div>
        <a href="{prefix}characters/index.html" data-footer-archive="01" style="--gateway:#ef5b55"><span>01</span><b>Echo-Cores</b><small>Characters</small></a>
        <a href="{prefix}lore/index.html" data-footer-archive="02" style="--gateway:#a78bfa"><span>02</span><b>Cycle Archive</b><small>Lore</small></a>
        <a href="{prefix}locations/index.html" data-footer-archive="03" style="--gateway:#38bdf8"><span>03</span><b>City Atlas</b><small>Locations</small></a>
        <a href="{prefix}factions/index.html" data-footer-archive="04" style="--gateway:#f59e0b"><span>04</span><b>Orders</b><small>Factions</small></a>
        <a href="{prefix}departments/index.html" data-footer-archive="05" style="--gateway:#71efaf"><span>05</span><b>Hand of Change</b><small>Facility</small></a>
        <a href="{prefix}entities/index.html" data-footer-archive="06" style="--gateway:#fb7185"><span>06</span><b>SECC Registry</b><small>Entities</small></a>
        <a href="{prefix}maw/index.html" data-footer-archive="07" style="--gateway:#f1df76"><span>07</span><b>M.A.W. Arsenal</b><small>Equipment</small></a>
        <a href="{prefix}mechanics/index.html" data-footer-archive="08" style="--gateway:#60a5fa"><span>08</span><b>Systems Codex</b><small>Mechanics</small></a>
      </div>
    </section>

    <nav class="footer-links" aria-label="Archive resources">
      <header><span>Project access</span><h2>Archive Resources</h2><p>Inspect provenance, files, and visual infrastructure.</p></header>
      <div>
        <a href="{prefix}project/source-map.html" data-footer-link="R-01"><b>Source Map</b><small>Canon provenance</small></a>
        <a href="{prefix}downloads.html" data-footer-link="R-02"><b>Download Center</b><small>Reader snapshot</small></a>
        <a href="{prefix}assets/icons/icons_gallery.html" data-footer-link="R-03"><b>Icon Library</b><small>Visual registry</small></a>
        <a href="https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI" data-footer-link="R-04" target="_blank" rel="noopener noreferrer"><b>Repository</b><small>Revision history</small></a>
        <button type="button" class="footer-link-button" data-footer-link="R-05" data-random-archive><b>Random Archive</b><small>Jump to a random record</small></button>
      </div>
    </nav>
  </div>

  <section class="footer-register" aria-label="Publication register">
    <header><span>Publication register</span><b>VERIFIED WORKING-TREE BASELINE</b></header>
    <dl>
      <div><dt>Public pages</dt><dd>197</dd><small>HTML records</small></div>
      <div><dt>Editorial corpus</dt><dd>253,515</dd><small>Counted words</small></div>
      <div><dt>Visual assets</dt><dd>448</dd><small>SVG</small></div>
      <div><dt>Editorial floor</dt><dd>200+</dd><small>Words per page</small></div>
      <div><dt>Last verified</dt><dd>{LAST_VERIFIED}</dd><small>SYNC {ASSET_VERSION}</small></div>
    </dl>
    <div class="footer-protocols">
      <span><b>01</b> SOURCE-LED CONTENT</span>
      <span><b>02</b> DISTINCT VISUAL FORM</span>
      <span><b>03</b> NO RECOLOR-ONLY ART</span>
      <span><b>04</b> VERIFIED LOCAL ROUTES</span>
    </div>
  </section>

  <div class="footer-base">
    <span><i aria-hidden="true"></i> REVERIE DIRECTORATE // PUBLIC ACCESS NODE</span>
    <span>WITNESS THE SORROW · PRESERVE THE NAME</span>
    <a href="https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/main/CHANGELOG.md" target="_blank" rel="noopener noreferrer">RELEASE 1.8.31 CHANGELOG <b aria-hidden="true">↗</b></a>
  </div>
</footer>'''


def update_page(path: Path, root: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    text = ANY_FOOTER_RE.sub("", original)
    expected = render_bottom_bar(path, root)
    text, substitutions = re.subn(
        r'\s*</body>',
        "\n" + expected + "\n</body>",
        text,
        count=1,
        flags=re.IGNORECASE,
    )
    if substitutions != 1:
        return False
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def validate_bottom_bars(root: Path) -> list[BottomBarIssue]:
    root = root.resolve()
    issues: list[BottomBarIssue] = []
    for path in sorted(root.rglob("*.html")):
        label = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        all_footers = list(ANY_FOOTER_RE.finditer(text))
        canonical = list(BOTTOM_BAR_RE.finditer(text))
        if len(all_footers) != 1:
            issues.append(
                BottomBarIssue(label, "bottom-bar-count", f"expected 1, found {len(all_footers)}")
            )
            continue
        if len(canonical) != 1:
            issues.append(
                BottomBarIssue(label, "bottom-bar-component", "footer is not canonical global chrome")
            )
            continue
        if canonical[0].group(0) != render_bottom_bar(path, root):
            issues.append(
                BottomBarIssue(label, "bottom-bar-drift", "topology, gateways, resources, metrics, or text differ")
            )
        body_close = text.lower().rfind("</body>")
        trailing_body = text[canonical[0].end() : body_close]
        if body_close < canonical[0].end() or re.search(
            r'</(?:main|div|aside|section|article)>', trailing_body, re.IGNORECASE
        ):
            issues.append(
                BottomBarIssue(
                    label,
                    "bottom-bar-placement",
                    "footer must follow the page shell and precede the body close",
                )
            )
    return issues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Synchronize or verify the canonical bottom bar across all public pages."
    )
    parser.add_argument(
        "root", nargs="?", type=Path, default=Path("docs"), help="public root (default: docs)"
    )
    parser.add_argument(
        "--write", action="store_true", help="rewrite drifted pages instead of only checking"
    )
    parser.add_argument(
        "--report-joins",
        action="store_true",
        help="print the reference join used for every page's filing strip",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"error: public root does not exist: {root}")
        return 2

    html_files = sorted(root.rglob("*.html"))
    if args.write:
        changed = sum(update_page(path, root) for path in html_files)
        print(f"Synchronized global bottom bar: {changed} of {len(html_files)} pages updated")

    if args.report_joins:
        for path in html_files:
            strip = _filing_strip(path, root)
            print(f"{path.relative_to(root).as_posix()}  ::  {re.sub('<[^>]+>', ' ', strip)}")

    issues = validate_bottom_bars(root)
    if issues:
        print(f"FAIL: {len(issues)} bottom-bar consistency issue(s)")
        for issue in issues:
            print(f"  {issue.page}: {issue.kind}: {issue.detail}")
        if not args.write:
            print("Run with --write to synchronize the static pages.")
        return 1

    print(
        f"PASS: expanded bottom-bar topology, gateways, resources, metrics, and placement match "
        f"across {len(html_files)} pages"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
