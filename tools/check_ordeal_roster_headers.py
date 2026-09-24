import glob
import re

files = glob.glob("SOMNARAK-WORLD/Ordeals/*.md")
headers = set()
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    m = re.findall(r'## Spawn Roster.*', txt)
    for h in m:
        headers.add(h)

print("Headers found:")
for h in sorted(headers):
    print(" -", h)
