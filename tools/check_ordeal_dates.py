import glob
import re

ordeal_files = glob.glob("SOMNARAK-WORLD/Ordeals/*.md")
dates = set()
for f in ordeal_files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    m = re.findall(r'\*\*Date:\*\*\s*(.*)', txt)
    for d in m:
        dates.add(d.strip())

print("Ordeal dates found:", dates)
