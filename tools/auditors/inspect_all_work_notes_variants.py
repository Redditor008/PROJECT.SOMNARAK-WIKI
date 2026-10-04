import glob
import re

files = glob.glob("SOMNARAK-WORLD/Sorrow_Entities/*.md")

v_cured = set()
v_fed = set()
v_before = set()

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    m1 = re.search(r'([^.\n]+?\.,\s*not permanent healing\.)', txt)
    if m1:
        v_cured.add(m1.group(0))
    m2 = re.search(r'([^.\n]+?\.\s+or fed the entity[\'’]s originating sorrow\.)', txt)
    if m2:
        v_fed.add(m2.group(0))
    m3 = re.search(r'([^.\n]+?\.\s+before the next assignment\.)', txt)
    if m3:
        v_before.add(m3.group(0))

print("=== V_CURED VARIANTS ===")
for v in sorted(v_cured):
    print(" -", repr(v))

print("\n=== V_FED VARIANTS ===")
for v in sorted(v_fed):
    print(" -", repr(v))

print("\n=== V_BEFORE VARIANTS ===")
for v in sorted(v_before):
    print(" -", repr(v))
