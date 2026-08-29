import os, glob, re
from bs4 import BeautifulSoup

wiki_root = '/home/user/01_Somnarak_Wiki'

entity_files = glob.glob(f'{wiki_root}/entities/*.html')

for ef in entity_files:
    fname = os.path.basename(ef)
    if fname == 'index.html': continue
    
    with open(ef, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check if page has <div class="entity-article">
    if '<div class="entity-article">' in html:
        # Check if it already has <div class="entity-main-content">
        if '<div class="entity-main-content">' in html:
            print(f"Skipping {fname}, already has entity-main-content")
            continue
            
        # Parse and restructure so <div class="entity-article"> has exactly 2 direct children:
        # 1. <div class="entity-main-content"> (everything except the aside)
        # 2. <aside class="entity-infobox">
        
        pattern = r'<div class="entity-article">([\s\S]*?)(<aside class="entity-infobox"[\s\S]*?<\/aside>)\s*<\/div>'
        match = re.search(pattern, html)
        
        if match:
            main_body = match.group(1).strip()
            infobox = match.group(2).strip()
            
            replacement = f'<div class="entity-article">\n  <div class="entity-main-content">\n    {main_body}\n  </div>\n  {infobox}\n</div>'
            new_html = html[:match.start()] + replacement + html[match.end():]
            
            with open(ef, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f"SUCCESS: Restructured {fname} into clean 2-column Grid with entity-main-content!")
        else:
            print(f"Could not regex match structure in {fname}")

print("Completed wrapping entity article grids!")
