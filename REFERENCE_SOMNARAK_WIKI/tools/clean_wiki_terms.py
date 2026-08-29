import os
import glob
import re

WIKI_ROOT = "/home/user/01_Somnarak_Wiki"
html_files = sorted(glob.glob(os.path.join(WIKI_ROOT, "**", "*.html"), recursive=True))

replacements = [
    ("Archival Dossier", "Article"),
    ("archival dossier", "article"),
    ("Dossier", "Article"),
    ("dossier", "article"),
    ("Institutional Dossier", "Article"),
    ("Facility Dossier", "Article"),
    ("Cartographic Dossier", "Article"),
    ("DOSSIER CLASSIFICATION", "KEY INFORMATION"),
    ("GUILD DOSSIER", "OVERVIEW"),
    ("REVERIE DIRECTORATE // DOSSIER CLASSIFICATION", "KEY INFORMATION"),
    ("REVERIE DIRECTORATE // CARTOGRAPHIC DOSSIER", "OVERVIEW"),
    ("Official Reverie Directorate archival dossier for ", ""),
    ("Official archival record on ", ""),
    ("Official geographical and architectural dossier for ", ""),
    ("Official operational dossier for ", ""),
    ("Archival record of ", ""),
    ("Archival dossier for ", ""),
    ("Archival dossier on ", ""),
    ("Encyclopedia of the city built around the Alpha Tree above the Weeping, its manifestations of Han, the Reverie Directorate, and the people who endure beyond the 1,778 Cycles.", "Encyclopedia of Somnarak, its manifestations of Han, the Reverie Directorate, and the institutions enduring beyond the 1,778 Cycles."),
    ("Encyclopedia of the City of Unresolved Sorrow", "Encyclopedia of Somnarak"),
    ("Content is available under the Reverie Directorate Archival License", "Content is available under the Somnarak Archival Documentation License"),
    ("Curated Canonical System", "System Overview"),
    ("Curated", "Article"),
    ("curated", "article")
]

modified_count = 0
for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    orig = content
    for old, new in replacements:
        content = content.replace(old, new)
        
    # Also clean up any data-article-status="curated" -> data-article-status="article"
    content = content.replace('data-article-status="curated"', 'data-article-status="article"')
    
    if content != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        modified_count += 1

print(f"Cleaned terminology across {modified_count} HTML files to 100% authentic Wiki standards.")
