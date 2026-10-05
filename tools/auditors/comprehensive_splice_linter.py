import os
import glob
import re

files = glob.glob("SOMNARAK-WORLD/**/*.md", recursive=True)

patterns = [
    ("Period followed by lowercase", re.compile(r'\b[a-zA-Z]{2,}\.\s+[a-z][a-z]')),
    ("Period followed by comma or comma period", re.compile(r'(\.,|,\.)')),
    ("Orphaned conjunction before period", re.compile(r'\b(and|or|but|because|with|the)\.\s+', re.IGNORECASE)),
    ("Duplicate phrase/fragment", re.compile(r'not cured\.,\s*not permanent healing', re.IGNORECASE)),
    ("Broken tiers. the entity", re.compile(r'different tiers\.\s+the entity', re.IGNORECASE)),
]

findings = {p[0]: [] for p in patterns}

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    for idx, line in enumerate(lines):
        for name, pat in patterns:
            m = pat.search(line)
            if m:
                # filter out markdown links like e.g. or common abbreviations
                snippet = m.group(0)
                if "e.g." in line or "i.e." in line or "etc." in line or ".md" in line:
                    continue
                findings[name].append((f, idx + 1, line.strip()))

for name in findings:
    print(f"=== {name} (Matches: {len(findings[name])}) ===")
    for item in findings[name][:5]:
        print(f"  {item[0]}:{item[1]} -> {item[2][:80]}...")
    if len(findings[name]) > 5:
        print(f"  ... and {len(findings[name]) - 5} more.")
    print()
