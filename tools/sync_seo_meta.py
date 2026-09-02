#!/usr/bin/env python3
"""Sync per-page SEO meta (description / canonical / Open Graph) across all HTML pages."""
from __future__ import annotations

import json
import re

VERIFY_RE = re.compile(r"^(?:google|bing|yandex|facebook|twitter)[0-9a-zA-Z]{10,}\.(?:html|txt)$", re.I)
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
BASE = "https://redditor008.github.io/PROJECT.SOMNARAK-WIKI"
SITE_NAME = "Somnarak Wiki"

TAG_RE = re.compile(r"<[^>]+>")

def derive_description(html: str) -> str:
    m = re.search(r"<div id=\"content\"[^>]*>(.*)", html, re.S)
    body = m.group(1) if m else html
    for pm in re.finditer(r"<p[^>]*>(.*?)</p>", body, re.S):
        text = re.sub(r"<[^>]+>", " ", pm.group(1))
        text = re.sub(r"\s+", " ", text).strip()
        if len(text) >= 60:
            return (text[:155].rsplit(" ", 1)[0] + "…") if len(text) > 155 else text
    return f"Somnarak Wiki archive page."

def block_for(rel: str, title: str, desc: str) -> str:
    url = f"{BASE}/{rel}"
    return (
        f'\n  <meta name="description" content="{desc}">\n'
        f'  <link rel="canonical" href="{url}">\n'
        f'  <meta property="og:type" content="website">\n'
        f'  <meta property="og:site_name" content="{SITE_NAME}">\n'
        f'  <meta property="og:title" content="{title}">\n'
        f'  <meta property="og:description" content="{desc}">\n'
        f'  <meta property="og:url" content="{url}">\n'
        f'  <meta name="twitter:card" content="summary">'
    )

def strip_old(html: str) -> str:
    html = re.sub(r'\n?\s*<meta[^>]*name="description"[^>]*/?>', "", html)
    html = re.sub(r'\n?\s*<link[^>]*rel="canonical"[^>]*/?>', "", html)
    html = re.sub(r'\n?\s*<meta[^>]*property="og:(?:type|site_name|title|description|url)"[^>]*/?>', "", html)
    html = re.sub(r'\n?\s*<meta[^>]*name="twitter:card"[^>]*/?>', "", html)
    return html

def main() -> int:
    write = "--write" in sys.argv
    descs = {}
    sp = DOCS / "data" / "search.json"
    if sp.exists():
        for rec in json.loads(sp.read_text(encoding="utf-8")):
            descs[rec["url"]] = rec.get("description", "")
    issues, pages = [], 0
    for path in sorted(DOCS.rglob("*.html")):
        rel = path.relative_to(DOCS).as_posix()
        if rel == "404.html" or VERIFY_RE.match(Path(rel).name):
            continue
        pages += 1
        html = path.read_text(encoding="utf-8")
        m = re.search(r"<title>([^<]*)</title>", html)
        title = re.sub(r"\s*—\s*Somnarak Wiki\s*$", "", m.group(1)).strip() if m else SITE_NAME
        desc = descs.get(rel, "").strip() or derive_description(html)
        desc = desc.replace('"', "&quot;")
        new = strip_old(html)
        tm = re.search(r"<title>[^<]*</title>", new)
        new = new[:tm.end()] + block_for(rel, title, desc) + new[tm.end():]
        if new != html:
            if write:
                path.write_text(new, encoding="utf-8")
            else:
                issues.append(f"{rel}: meta differs")
    if write:
        print(f"PASS: SEO meta written on {pages} pages (canonical base {BASE})")
    else:
        if issues:
            print(f"FAIL: {len(issues)} pages differ")
            for i in issues[:10]:
                print("  " + i)
            return 1
        print(f"PASS: SEO meta (description/canonical/OG) consistent across {pages} pages")
    return 0

if __name__ == "__main__":
    sys.exit(main())
