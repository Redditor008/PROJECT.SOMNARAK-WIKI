import os
import glob
from bs4 import BeautifulSoup

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

count = 0
for html_path in glob.glob(os.path.join(WIKI_DIR, "**/*.html"), recursive=True):
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    soup = BeautifulSoup(content, "html.parser")
    tables = soup.find_all("table")
    
    modified = False
    for table in tables:
        parent = table.parent
        # If parent is not already a table-wrap
        if parent and "table-wrap" not in parent.get("class", []):
            wrapper = soup.new_tag("div", attrs={"class": "table-wrap"})
            table.wrap(wrapper)
            modified = True
            
    if modified:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        count += 1

print(f"Wrapped tables with responsive .table-wrap across {count} HTML files.")
