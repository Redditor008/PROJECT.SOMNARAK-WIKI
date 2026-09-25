import glob
import re

files = glob.glob("SOMNARAK-WORLD/**/*.md", recursive=True)
p = re.compile(r'\b([a-z]{2,})\.,\s*([a-zA-Z])')

unique_patterns = set()
count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    for m in p.finditer(txt):
        unique_patterns.add((m.group(1), m.group(2)))
        count += 1

print(f"Total occurrences of word.,: {count}")
for w, next_c in sorted(unique_patterns):
    print(f" - {w}., {next_c}")
