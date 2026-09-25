#!/usr/bin/env python3
"""
tools/fix_maw_codex_links.py
Maps and fixes all broken entity links in SOMNARAK_MAW_CODEX.md to their exact canonical filenames.
"""

import os
import re

entities_dir = "SOMNARAK-WORLD/Sorrow_Entities"
real_files = set(os.listdir(entities_dir))

fpath = "SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md"
with open(fpath, "r", encoding="utf-8") as fp:
    content = fp.read()

matches = re.findall(r"\[([^\]]+)\]\(\.\./\.\./Sorrow_Entities/([^)]+\.md)\)", content)

fix_map = {}
for text, fname in matches:
    if fname in real_files:
        continue
    if fname in fix_map:
        continue
    # try removing "_The_"
    c1 = fname.replace("_The_", "_")
    if c1 in real_files:
        fix_map[fname] = c1
        continue
    # try adding "_The_"
    c2 = re.sub(r"(SE-[A-Z]-[A-Z0-9]+[α-ω]?-[0-9]+_)", r"\1The_", fname)
    if c2 in real_files:
        fix_map[fname] = c2
        continue
    # match code
    code_match = re.search(r"SE-[A-Z]-[A-Z0-9]+[α-ω]?-[0-9]+", fname)
    if code_match:
        code = code_match.group(0)
        candidates = [rf for rf in real_files if code in rf]
        if candidates:
            fix_map[fname] = candidates[0]

print(f"Applying {len(fix_map)} link mappings...")
for old_fname, new_fname in fix_map.items():
    content = content.replace(f"../../Sorrow_Entities/{old_fname}", f"../../Sorrow_Entities/{new_fname}")

with open(fpath, "w", encoding="utf-8") as fp:
    fp.write(content)

print(f"Updated {fpath} successfully!")
