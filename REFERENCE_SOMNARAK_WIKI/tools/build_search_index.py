import os
import glob
import re
import json

WIKI_ROOT = "/home/user/01_Somnarak_Wiki"
SEARCH_JSON = os.path.join(WIKI_ROOT, "data", "search.json")

html_files = sorted(glob.glob(os.path.join(WIKI_ROOT, "**", "*.html"), recursive=True))

index_entries = []

for fpath in html_files:
    rel_path = os.path.relpath(fpath, WIKI_ROOT)
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    title_match = re.search(r"<title>([^<]+)</title>", content)
    title = title_match.group(1).split("—")[0].strip() if title_match else rel_path
    
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
    subtitle = desc_match.group(1) if desc_match else ""
    
    # Extract headers and paragraphs for search terms
    text_content = re.sub(r"<[^>]+>", " ", content)
    words = re.findall(r"[A-Za-z0-9\uAC00-\uD7A3\u3000-\u303F\u4E00-\u9FFFα-ωΑ-Ω]+", text_content)
    
    # Filter common words and take unique
    stop_words = {"the", "a", "an", "and", "or", "in", "of", "to", "for", "with", "on", "at", "by", "from", "is", "are", "was", "were", "this", "that", "it", "as", "be", "all"}
    unique_terms = []
    seen = set()
    for w in words:
        wl = w.lower()
        if wl not in stop_words and len(w) > 1 and wl not in seen:
            seen.add(wl)
            unique_terms.append(w)
            if len(unique_terms) >= 30:
                break
                
    terms_str = " ".join(unique_terms)
    
    index_entries.append({
        "title": title,
        "subtitle": subtitle[:120] if len(subtitle) > 120 else subtitle,
        "url": rel_path,
        "terms": terms_str
    })

with open(SEARCH_JSON, "w", encoding="utf-8") as f:
    json.dump(index_entries, f, ensure_ascii=False, indent=2)

print(f"Indexed {len(index_entries)} pages into {SEARCH_JSON}")
