import glob
import re

ordeal_files = glob.glob("SOMNARAK-WORLD/Ordeals/*.md")
print(f"Total ordeal files: {len(ordeal_files)}")

c2_matches = []
c3_matches = []
c5_double_dots = []

p_c2 = re.compile(r'out of 1000', re.IGNORECASE)
p_c3 = re.compile(r'themed to its form and element', re.IGNORECASE)
p_c5 = re.compile(r'\.\.')

for f in ordeal_files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    if p_c2.search(txt):
        c2_matches.append(f)
    if p_c3.search(txt):
        c3_matches.append(f)
    if p_c5.search(txt):
        c5_double_dots.append(f)

print(f"Files with 'out of 1000' (C2): {len(c2_matches)}")
print(f"Files with 'themed to its form and element' (C3): {len(c3_matches)}")
print(f"Files with double period '..' (C5): {len(c5_double_dots)}")
if c3_matches:
    print("C3 files:", c3_matches)
