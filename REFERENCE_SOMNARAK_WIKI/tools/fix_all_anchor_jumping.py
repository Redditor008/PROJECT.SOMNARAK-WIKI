import os, re
from bs4 import BeautifulSoup

WIKI_DIR = "/home/user/01_Somnarak_Wiki"
CSS_PATH = os.path.join(WIKI_DIR, "assets/css/wiki.css")

# 1. Append scroll-margin-top and smooth scroll CSS
scroll_fix_css = '''
/* ==========================================================================
   ANCHOR JUMP SCROLL FIX (PERFECT POSITIONING & SMOOTH JUMP)
   ========================================================================== */

html {
  scroll-behavior: smooth !important;
}

[id] {
  scroll-margin-top: 85px !important;
}

h1[id], h2[id], h3[id], h4[id], section[id], div[id], article[id] {
  scroll-margin-top: 85px !important;
}
'''

with open(CSS_PATH, "a", encoding="utf-8") as f:
    f.write("\n" + scroll_fix_css)

print("Appended scroll-margin-top CSS.")

# 2. Clean all hrefs with trailing spaces and fix anchor IDs
fixed_links = [0]
for root, dirs, files in os.walk(WIKI_DIR):
    for f in files:
        if not f.endswith(".html"):
            continue
        full_path = os.path.join(root, f)
        
        with open(full_path, "r", encoding="utf-8") as fp:
            content = fp.read()
            
        def fix_href(match):
            href = match.group(1)
            if '#' in href:
                parts = href.split('#')
                cleaned = parts[0] + '#' + parts[1].strip()
                if cleaned != href:
                    fixed_links[0] += 1
                    return f'href="{cleaned}"'
            return match.group(0)
            
        new_content = re.sub(r'href=[\'"]([^\'"]+)[\'"]', fix_href, content)
        
        # Ensure index.html has missing IDs like id="city-atlas", id="hand-access" if referenced
        if f == "index.html":
            if 'id="city-atlas"' not in new_content:
                new_content = new_content.replace('class="city-atlas"', 'class="city-atlas" id="city-atlas"', 1)
            if 'id="hand-access"' not in new_content:
                new_content = new_content.replace('class="hand-access"', 'class="hand-access" id="hand-access"', 1)
                    
        if new_content != content:
            with open(full_path, "w", encoding="utf-8") as fp:
                fp.write(new_content)

print(f"Fixed {fixed_links[0]} trailing-space anchor hrefs across all HTML pages.")
