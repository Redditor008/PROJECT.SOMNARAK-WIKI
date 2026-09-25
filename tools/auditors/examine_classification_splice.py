import glob
import re

files = glob.glob("SOMNARAK-WORLD/Sorrow_Entities/*.md")
pattern = re.compile(r'([^.\n]+?\.\s+the entity[\'’]s classification\.\s+[^.\n]+?\.)', re.IGNORECASE)

examples = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    m = pattern.search(txt)
    if m:
        examples.append((f, m.group(0)))
    if len(examples) >= 5:
        break

for f, ex in examples:
    print(f"FILE: {f}")
    print(f"SNIPPET: {ex}\n")
