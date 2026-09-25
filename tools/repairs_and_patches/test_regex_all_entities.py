import glob
import re

files = glob.glob("SOMNARAK-WORLD/**/*.md", recursive=True)
pattern = re.compile(r'(\.)\s+the entity[\'’]s classification\.\s+', re.IGNORECASE)

matched_files = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    if pattern.search(txt):
        matched_files.append(f)

print(f"Total files matching pattern: {len(matched_files)}")
