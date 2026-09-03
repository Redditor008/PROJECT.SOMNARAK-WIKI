#!/usr/bin/env python3
"""Reconcile docs/data/search.json with the public page tree.

Existing entries are kept verbatim (they carry hand-tuned categories and
keywords). Every public HTML page (except 404.html and search-engine
verification files) must have exactly one record — the structure audit
fails on missing, stale, or duplicate URLs. Missing pages get a derived
entry: title, category by folder, meta description, and keywords built
from the page's headings.

Run after adding or removing pages:
    python tools/build_search_index.py
"""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
INDEX = DOCS / "data" / "search.json"

VERIFY_RE = re.compile(r"^(?:google|bing|yandex|facebook|twitter)[0-9a-zA-Z]{10,}\.(?:html|txt)$", re.I)

CATEGORY_BY_FOLDER = {
    "assets": "Assets",
    "atlas": "Atlas & Maps",
    "characters": "Characters",
    "departments": "Hand of Change",
    "entities": "Sorrow Entities",
    "factions": "Factions & Guilds",
    "locations": "Atlas & Locations",
    "lore": "Lore & Cosmology",
    "maw": "M.A.W. Codex",
    "mechanics": "Battle & Systems",
    "project": "Project",
}


class HeadingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.description = ""
        self.headings: list[str] = []
        self._in_title = False
        self._in_h: int | None = None
        self._h_buf: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag in {"h1", "h2", "h3"}:
            self._in_h = int(tag[1])
            self._h_buf = []
        elif tag == "meta" and a.get("name") == "description":
            self.description = a.get("content") or ""

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag in {"h1", "h2", "h3"} and self._in_h:
            self.headings.append(" ".join("".join(self._h_buf).split()))
            self._in_h = None

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h:
            self._h_buf.append(data)


def build_entry(page: Path) -> dict:
    parser = HeadingParser()
    parser.feed(page.read_text(encoding="utf-8", errors="replace"))
    rel = page.relative_to(DOCS).as_posix()
    parts = rel.split("/")
    category = CATEGORY_BY_FOLDER.get(parts[0] if len(parts) > 1 else "", "Somnarak")
    title = " ".join(parser.title.split())
    keywords = " ".join([title, category, parts[0] if len(parts) > 1 else "main", *parser.headings[:40]])
    return {
        "title": title,
        "url": rel,
        "category": category,
        "description": parser.description or "",
        "keywords": " ".join(keywords.split()),
    }


def main() -> int:
    pages = [
        p for p in sorted(DOCS.rglob("*.html"))
        if p.name != "404.html" and not VERIFY_RE.match(p.name)
    ]
    expected = {p.relative_to(DOCS).as_posix() for p in pages}

    existing: list[dict] = []
    if INDEX.exists():
        existing = json.loads(INDEX.read_text(encoding="utf-8"))
    have = {e["url"] for e in existing if isinstance(e, dict) and e.get("url")}
    duplicates = len(have) - len([e for e in existing if e.get("url") in have])

    missing = sorted(expected - have)
    stale = sorted(have - expected)
    for url in missing:
        existing.append(build_entry(DOCS / url))

    if stale:
        print("removing stale records:")
        for url in stale:
            print("  " + url)
        existing = [e for e in existing if e.get("url") not in stale]

    existing.sort(key=lambda e: e["url"])
    urls = [e["url"] for e in existing]
    assert len(urls) == len(set(urls)), "duplicate URLs after reconcile"
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(json.dumps(existing, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"search index: {len(existing)} records (+{len(missing)} added, {len(stale)} removed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
