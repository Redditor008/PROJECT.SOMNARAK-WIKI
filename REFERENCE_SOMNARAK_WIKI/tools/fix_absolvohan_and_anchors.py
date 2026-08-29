import re
from bs4 import BeautifulSoup

ABSOLVOHAN_PATH = "/home/user/01_Somnarak_Wiki/lore/the-cycle-and-absolvohan.html"

with open(ABSOLVOHAN_PATH, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# Find all <a class="wiki-link" href="#..."> inside headers
for a in soup.find_all("a", href=True):
    href = a["href"]
    if href.startswith("#"):
        target_id = href[1:]
        parent = a.find_parent(["h1", "h2", "h3", "h4", "h5", "section", "div"])
        if parent:
            parent["id"] = target_id

with open(ABSOLVOHAN_PATH, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Fixed all anchor target IDs in the-cycle-and-absolvohan.html!")
