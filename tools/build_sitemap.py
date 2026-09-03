#!/usr/bin/env python3
"""Generate docs/sitemap.xml and docs/robots.txt from the docs tree."""
from __future__ import annotations

import re

VERIFY_RE = re.compile(r"^(?:google|bing|yandex|facebook|twitter)[0-9a-zA-Z]{10,}\.(?:html|txt)$", re.I)
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
BASE = "https://redditor008.github.io/PROJECT.SOMNARAK-WIKI"
LASTMOD = "2026-09-03"

def priority(url: str) -> float:
    if url in ("", "index.html"):
        return 1.0
    depth = url.count("/")
    return 0.8 if depth <= 1 else 0.6

def main() -> int:
    pages = sorted(p.relative_to(DOCS).as_posix() for p in DOCS.rglob("*.html") if p.name != "404.html" and not VERIFY_RE.match(p.name))
    if len(pages) < 100:
        print(f"FAIL: only {len(pages)} pages found — refusing to write a truncated sitemap")
        return 1
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for rel in pages:
        lines.append("  <url>")
        lines.append(f"    <loc>{BASE}/{rel}</loc>")
        lines.append(f"    <lastmod>{LASTMOD}</lastmod>")
        lines.append("    <changefreq>weekly</changefreq>")
        lines.append(f"    <priority>{priority(rel):.1f}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    (DOCS / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    robots = (
        "# Somnarak Wiki — GitHub Pages\n"
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {BASE}/sitemap.xml\n"
    )
    (DOCS / "robots.txt").write_text(robots, encoding="utf-8")
    print(f"PASS: sitemap.xml with {len(pages)} URLs + robots.txt (Sitemap: {BASE}/sitemap.xml)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
