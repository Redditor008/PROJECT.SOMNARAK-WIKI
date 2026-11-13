"""audit_pan_se_status.py — how many dossiers are non-Subject, and do they bar the pair?

Scratch report, not a gate. The Two-Work-Type figure was measured by looking for
`N/A` in the Flerehan and Pugnahan cells, which batches 155b–159 retired; it read
0% against a rule that no longer exists. It now reads the same cells the gate
reads (`check_work_preference.vector_of`), so the figure means what `R-41` means.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import check_work_preference as pref  # noqa: E402

files = glob.glob("SOMNARAK-WORLD/Sorrow_Entities/*.md")
files = [f for f in files if "README" not in f]

total_entities = len(files)
two_work_compliant = 0
relic_entities = 0
special_transform_entities = []
stat_line_compliant = 0

for f in files:
    bn = os.path.basename(f)
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
        
    m = re.search(r"\*\*(?:Entity Type|Type)\*\*\s*\|\s*([^|\n]+)", content)
    if m:
        etype_raw = m.group(1).strip()
        etype = etype_raw.split("—")[0].split("-")[0].strip()
    else:
        etype = "Unknown"
        
    if etype in ["**Object/Place**", "**Time**", "**Object**", "**Place**", "**Place (Special Transform Type)**"]:
        relic_entities += 1
        vec = pref.vector_of(content)
        if vec and vec[0] in pref.BAR and vec[1] in pref.BAR:
            two_work_compliant += 1
            
    # Check transform breach
    if "C-IVω-001-B" in content or "Transform" in content or "Transformation" in content:
        special_transform_entities.append(bn)
        
    # Check core stat line
    has_speed = "Speed" in content
    has_sorrow_gauge = "Sorrow Gauge" in content or "HP" in content
    has_han_pressure = "Han Pressure" in content or "ATK" in content
    has_resistance = "Resistance" in content or "DMG" in content
    if has_speed and has_sorrow_gauge and has_han_pressure and has_resistance:
        stat_line_compliant += 1

print(f"Total Entities Audited: {total_entities}")
print(f"Relic / Tool Entities: {relic_entities} / {total_entities} ({relic_entities/total_entities*100:.2f}%)")
print(f"Barred pair written as words: {two_work_compliant} / {relic_entities} ({two_work_compliant/relic_entities*100:.1f}%)")
print(f"Core Stat Line Compliant: {stat_line_compliant} / {total_entities} ({stat_line_compliant/total_entities*100:.1f}%)")
