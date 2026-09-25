import glob
import re

files = glob.glob("SOMNARAK-WORLD/**/*.md", recursive=True)

checks = [
    ("double_punct", re.compile(r'(\.,|,\.|\.\.|\?\!|!\?|,,)')),
    ("orphan_before", re.compile(r'\.\s+before the next assignment', re.IGNORECASE)),
    ("orphan_or_fed", re.compile(r'\.\s+or fed the entity', re.IGNORECASE)),
    ("not_permanent", re.compile(r'not permanent healing', re.IGNORECASE)),
    ("lower_after_dot", re.compile(r'\.\s+[a-z]{3,}')),
]

for name, pat in checks:
    matched = []
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            txt = fp.read()
        m = pat.findall(txt)
        if m:
            matched.append((f, len(m)))
    print(f"=== {name}: {len(matched)} files ===")
