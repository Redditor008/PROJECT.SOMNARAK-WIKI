import glob
import re

files = glob.glob("SOMNARAK-WORLD/Sorrow_Entities/*.md")
files = [f for f in files if "README" not in f]

type_counts = {}
entities_by_type = {}

for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        t = fp.read()
    m = re.search(r"\*\*(?:Entity Type|Type)\*\*\s*\|\s*([^|\n]+)", t)
    if m:
        etype_raw = m.group(1).strip()
        # simplify
        etype = etype_raw.split("—")[0].split("-")[0].strip()
        type_counts[etype] = type_counts.get(etype, 0) + 1
        if etype not in entities_by_type:
            entities_by_type[etype] = []
        entities_by_type[etype].append(f)
    else:
        print(f"No type match for {f}")

print("Entity Types across 292 Sorrow Entities:")
for k, v in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  {k}: {v}")
