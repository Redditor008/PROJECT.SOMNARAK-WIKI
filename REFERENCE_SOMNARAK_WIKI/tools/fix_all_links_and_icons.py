import os, glob, re
from bs4 import BeautifulSoup

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

char_slug_map = {
    "director": "the-director-majin.html",
    "seiyon": "the-secretary-seiyon.html",
    "dekan": "the-containment-lead-dekan.html",
    "zyrak": "the-extraction-lead-zyrak.html",
    "ayshuk": "the-research-lead-ayshuk.html",
    "mellda": "the-border-lead-mellda.html",
    "marjuk": "the-archive-lead-marjuk.html",
    "ishall": "the-outsider-ishall.html",
    "xyan": "the-exile-xyan.html",
}

for html_path in glob.glob(os.path.join(WIKI_DIR, '**/*.html'), recursive=True):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix character links
    for slug, real_file in char_slug_map.items():
        content = re.sub(rf'href=([\'"])(?:\.\./)?characters/{slug}\.html\1', rf'href=\1../characters/{real_file}\1', content)
        content = re.sub(rf'href=([\'"]){slug}\.html\1', rf'href=\1{real_file}\1', content)

    # Fix relative icon and asset paths based on folder depth
    rel_depth = len(os.path.relpath(html_path, WIKI_DIR).split(os.sep)) - 1
    prefix = "../" * rel_depth

    def fix_src(m):
        attr = m.group(1)
        quote = m.group(2)
        val = m.group(3)
        if val.startswith('data:') or val.startswith('http://') or val.startswith('https://'):
            return f'{attr}={quote}{val}{quote}'
        # clean off leading ../
        clean_val = re.sub(r'^(\.\./)+', '', val)
        return f'{attr}={quote}{prefix}{clean_val}{quote}'

    content = re.sub(r'(src|href)=([\'"])((?:\.\./)*assets/[^\'"]+)\2', fix_src, content)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Links and asset paths sanitized.")
