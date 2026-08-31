#!/usr/bin/env python3
"""Render and verify one canonical Somnarak footer on every public HTML page."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

try:  # Support direct execution and package-style imports.
    from .sync_global_top_bar import page_prefix
except ImportError:
    from sync_global_top_bar import page_prefix

BOTTOM_BAR_RE = re.compile(
    r'<footer\b[^>]*\bdata-component=["\']global-bottom-bar["\'][^>]*>.*?</footer>',
    re.IGNORECASE | re.DOTALL,
)
ANY_FOOTER_RE = re.compile(r'<footer\b[^>]*>.*?</footer>', re.IGNORECASE | re.DOTALL)


@dataclass(frozen=True)
class BottomBarIssue:
    page: str
    kind: str
    detail: str


def render_bottom_bar(path: Path, root: Path) -> str:
    prefix = page_prefix(path, root)
    return f'''<footer class="wiki-footer global-footer" data-component="global-bottom-bar">
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
      </div>
    </nav>
  </div>

  <section class="footer-register" aria-label="Publication register">
    <header><span>Publication register</span><b>VERIFIED WORKING-TREE BASELINE</b></header>
    <dl>
      <div><dt>Public pages</dt><dd>197</dd><small>HTML records</small></div>
      <div><dt>Editorial corpus</dt><dd>256,745</dd><small>Counted words</small></div>
      <div><dt>Visual assets</dt><dd>1,414</dd><small>SVG + PNG</small></div>
      <div><dt>Editorial floor</dt><dd>200+</dd><small>Words per page</small></div>
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
