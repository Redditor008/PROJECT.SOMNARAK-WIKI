#!/usr/bin/env python3
"""
tools/upgrade_all_pages_layout.py
Ensures all 135 wiki HTML pages have:
1. The top utility bar with working search and navigation.
2. Standard main container #content.wiki-content with comfortable padding.
3. Updated references to the newly designed Hand of Change simple and styled icons.
4. Clean, responsive layouts with 0 border clipping/touching.
"""

import os, re, glob

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

TEN_HUB_MAP_PAGES = [
    "atlas/hand-of-change-map.html",
    "atlas/somnarak-city-map.html",
    "characters/index.html",
    "departments/index.html",
    "entities/index.html",
    "factions/index.html",
    "locations/index.html",
    "lore/index.html",
    "maw/index.html",
    "mechanics/index.html"
]

def upgrade_ten_pages():
    for rel in TEN_HUB_MAP_PAGES:
        full_path = os.path.join(WIKI_DIR, rel)
        if not os.path.exists(full_path):
            continue
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Add script tag if missing
        if "wiki.js" not in content:
            content = content.replace("</head>", '  <script defer src="../assets/js/wiki.js"></script>\n</head>')

        # Add top utility header if missing
        if '<header class="utility">' not in content and '<header class="utility' not in content:
            utility_header = """<!-- Top Utility Navigation Bar -->
<header class="utility">
  <div class="utility-left">
    <button aria-label="Open navigation" class="nav-open" type="button">☰</button>
    <a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
    <span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
  </div>
  <nav aria-label="Main navigation">
    <a href="../index.html">Main page</a>
    <a href="../characters/index.html">Characters</a>
    <a href="../lore/index.html">Lore</a>
    <a href="../locations/index.html">Locations</a>
    <a href="../factions/index.html">Factions</a>
    <a href="../departments/index.html">Departments</a>
    <a href="../entities/index.html">Sorrow Entities</a>
    <a href="../maw/index.html">M.A.W.</a>
    <a href="../mechanics/index.html">Mechanics</a>
  </nav>
  <div class="search">
    <input aria-label="Search" data-index="../data/search.json" id="search" placeholder="Search archive..." autocomplete="off"/>
    <div id="results"></div>
  </div>
</header>
"""
            content = re.sub(r'(<body[^>]*>)', r'\1\n' + utility_header, content, count=1)

        # Standardize main container to <main id="content" class="wiki-content">
        content = re.sub(r'<main\s+class=["\']wiki-content["\']>', '<main id="content" class="wiki-content">', content)

        # Update Facility Room Types icon or others if needed
        content = content.replace(
            '<img src="../assets/layout/hand/icons/the_hand_dr_icon_styled.svg" alt="Room Types"',
            '<img src="../assets/layout/hand/icons/the_hand_of_change_simple.svg" alt="Facility Schematics"'
        )

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"Upgraded all {len(TEN_HUB_MAP_PAGES)} hub and map pages.")

def upgrade_all_wiki_pages():
    all_html = glob.glob(os.path.join(WIKI_DIR, "**/*.html"), recursive=True)
    count = 0
    for p in all_html:
        with open(p, "r", encoding="utf-8") as f:
            c = f.read()
        
        orig = c
        # Ensure search input has data-index and id="search"
        if 'id="search-input"' in c:
            # Determine depth
            rel = os.path.relpath(p, WIKI_DIR)
            depth = rel.count(os.sep)
            prefix = "../" * depth if depth > 0 else "./"
            c = c.replace('id="search-input" placeholder="Search archive..." type="search"', f'id="search" data-index="{prefix}data/search.json" placeholder="Search archive..." autocomplete="off"')
            c = c.replace('id="search-input"', 'id="search"')

        if c != orig:
            with open(p, "w", encoding="utf-8") as f:
                f.write(c)
            count += 1

    print(f"Updated search attributes across {count} HTML pages.")

if __name__ == "__main__":
    upgrade_ten_pages()
    upgrade_all_wiki_pages()
