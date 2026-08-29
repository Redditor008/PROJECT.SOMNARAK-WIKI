import os
import glob
import re
from bs4 import BeautifulSoup

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

for html_path in glob.glob(os.path.join(WIKI_DIR, "**/*.html"), recursive=True):
    rel_path = os.path.relpath(html_path, WIKI_DIR).replace("\\", "/")
    
    # Calculate rel_root
    depth = len(rel_path.split("/")) - 1
    rel_root = "." if depth == 0 else ".."
    
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Standard header template
    new_header = f"""<header class="utility">
  <div class="utility-left">
    <button class="nav-open" type="button" aria-label="Open navigation">☰</button>
    <a class="utility-brand" href="{rel_root}/index.html">SOMNARAK.WIKI</a>
    <span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
  </div>
  <nav aria-label="Main navigation">
    <a href="{rel_root}/index.html">Main page</a>
    <a href="{rel_root}/characters/index.html">Characters</a>
    <a href="{rel_root}/lore/index.html">Lore</a>
    <a href="{rel_root}/factions/index.html">Factions</a>
    <a href="{rel_root}/departments/index.html">Departments</a>
    <a href="{rel_root}/locations/index.html">Locations</a>
    <a href="{rel_root}/mechanics/index.html">Mechanics</a>
    <a href="{rel_root}/entities/index.html">Sorrow Entities</a>
    <a href="{rel_root}/maw/index.html">M.A.W.</a>
  </nav>
  <div class="search">
    <input id="search" data-index="{rel_root}/data/search.json" aria-label="Search" placeholder="Search Somnarak Wiki">
    <div id="results"></div>
  </div>
</header>"""

    # Replace <header class="utility">...</header>
    content = re.sub(r'<header class="utility">.*?</header>', new_header, content, flags=re.DOTALL)
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Standardized all headers across all 118 HTML files.")
