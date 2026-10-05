import os
import glob
import re

files = glob.glob("SOMNARAK-WORLD/**/*.md", recursive=True)
p1_count = 0
p2_count = 0
p3_count = 0

p1 = re.compile(r"different tiers\.\s+the entity’s classification\.", re.IGNORECASE)
p2 = re.compile(r"cured\.,\s*not permanent healing\.", re.IGNORECASE)
p3 = re.compile(r"not predicted\.\s+before the next assignment\.", re.IGNORECASE)

p1_files = []
p2_files = []
p3_files = []

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    if p1.search(content):
        p1_files.append(f)
    if p2.search(content):
        p2_files.append(f)
    if p3.search(content):
        p3_files.append(f)

print(f"Files matching 'different tiers. the entity classification': {len(p1_files)}")
print(f"Files matching 'cured., not permanent healing.': {len(p2_files)}")
print(f"Files matching 'not predicted. before the next assignment.': {len(p3_files)}")
