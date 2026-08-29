import os
import glob
import json
import re
from bs4 import BeautifulSoup

WIKI_DIR = "/home/user/01_Somnarak_Wiki"
SEARCH_JSON_PATH = os.path.join(WIKI_DIR, "data", "search.json")

entries = []

for html_path in sorted(glob.glob(os.path.join(WIKI_DIR, "**/*.html"), recursive=True)):
    rel_path = os.path.relpath(html_path, WIKI_DIR).replace("\\", "/")
    
    if rel_path == "404.html":
        continue
        
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    title_el = soup.find("title")
    title = title_el.get_text().replace(" — Somnarak Wiki", "").replace("Somnarak Wiki — ", "").strip() if title_el else rel_path
    
    desc_el = soup.find("meta", attrs={"name": "description"})
    desc = desc_el["content"].strip() if desc_el and "content" in desc_el.attrs else ""
    
    # Category based on directory
    folder = rel_path.split("/")[0] if "/" in rel_path else "main"
    cat_map = {
        "characters": "Characters",
        "lore": "Lore & Cosmology",
        "factions": "Factions & Guilds",
        "departments": "Hand of Change",
        "locations": "Atlas & Locations",
        "mechanics": "Battle & Systems",
        "entities": "Sorrow Entities",
        "maw": "M.A.W. Codex",
        "atlas": "Atlas & Maps",
        "main": "Main Canon"
    }
    category = cat_map.get(folder, folder.capitalize())
    
    # Extract headings and text snippets
    headings = [h.get_text().strip() for h in soup.find_all(["h1", "h2", "h3"])]
    
    # Extract meta cards
    meta_cards = []
    for card in soup.find_all("div", class_="meta-card"):
        meta_cards.append(card.get_text(separator=": ").strip())
        
    keywords = [title, category, folder] + headings + meta_cards
    
    entries.append({
        "title": title,
        "url": rel_path,
        "category": category,
        "description": desc,
        "keywords": " ".join(keywords)
    })

os.makedirs(os.path.dirname(SEARCH_JSON_PATH), exist_ok=True)
with open(SEARCH_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)

print(f"Rebuilt search index at {SEARCH_JSON_PATH} with {len(entries)} indexed articles.")
