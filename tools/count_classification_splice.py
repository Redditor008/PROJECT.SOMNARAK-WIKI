import glob
import re

files = glob.glob("SOMNARAK-WORLD/Sorrow_Entities/*.md")
pattern = re.compile(r'\.\s+the entity[\'’]s classification\.', re.IGNORECASE)

matches = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    if pattern.search(txt):
        matches.append(f)

print(f"Files with '. the entity classification.': {len(matches)} / {len(files)}")
