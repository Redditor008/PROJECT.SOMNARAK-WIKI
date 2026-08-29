import os
import glob
import re
from bs4 import BeautifulSoup

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# 1. On index.html: Ensure class="wiki-shell home-shell" and keep .floor-rail
index_path = os.path.join(WIKI_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    c = f.read()
if 'class="wiki-shell"' in c:
    c = c.replace('class="wiki-shell"', 'class="wiki-shell home-shell"')
with open(index_path, "w", encoding="utf-8") as f:
    f.write(c)

# 2. On ALL other HTML files: Remove <aside class="floor-rail">...</aside>
count = 0
for html_path in glob.glob(os.path.join(WIKI_DIR, "**/*.html"), recursive=True):
    rel = os.path.relpath(html_path, WIKI_DIR).replace("\\", "/")
    if rel == "index.html":
        continue
        
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    orig = content
    # Remove floor-rail aside
    content = re.sub(r'<aside class="floor-rail"[^>]*>.*?</aside>', '', content, flags=re.DOTALL)
    
    # Ensure wiki-shell does NOT have home-shell class
    content = content.replace('class="wiki-shell home-shell"', 'class="wiki-shell"')
    
    if orig != content:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

print(f"Removed right floor-rail sidebar from {count} article pages.")
