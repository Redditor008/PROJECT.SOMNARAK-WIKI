import glob
import re

files = glob.glob("SOMNARAK-WORLD/Sorrow_Entities/*.md")
print(f"Total SE files: {len(files)}")

broken_notes = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    issues = []
    if "cured.," in txt:
        issues.append("cured.,")
    if "different tiers. the entity" in txt or "different tiers. The entity" in txt:
        issues.append("different tiers. the entity")
    if "not predicted. before" in txt:
        issues.append("not predicted. before")
    if "not healing. or fed" in txt:
        issues.append("not healing. or fed")
    if issues:
        broken_notes.append((f, issues))

print(f"Files with Operational Work Notes splice issues: {len(broken_notes)}")
for b in broken_notes[:10]:
    print(b[0], b[1])
