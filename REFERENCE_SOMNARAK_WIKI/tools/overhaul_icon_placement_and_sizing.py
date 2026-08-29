import os, glob, re
from bs4 import BeautifulSoup

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# 1. Clean up tiny inline icon tags from inside <p> paragraphs across all HTML files
# Replace <a href="..." class="wiki-link"><img ... class="wiki-icon" ...> Text</a> with <a href="..." class="wiki-link">Text</a>
for html_path in glob.glob(os.path.join(WIKI_DIR, "**/*.html"), recursive=True):
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip inline wiki-icon from links inside paragraphs
    cleaned = re.sub(r'<img[^>]*class=[\'"][^\'"]*wiki-icon[^\'"]*[\'"][^>]*>\s*', '', content)
    
    if cleaned != content:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(cleaned)

print("Stripped tiny inline text icon clutter from all body paragraphs.")

# 2. Re-generate all Hub Landing Portals with prominent, large (80px - 100px) icons
import sys
sys.path.insert(0, '/home/user')
import tools.generate_all_super_hub_portals
import tools.generate_entities_maw_departments_super_hubs

print("All Hub landing pages rebuilt with large prominent icons.")
