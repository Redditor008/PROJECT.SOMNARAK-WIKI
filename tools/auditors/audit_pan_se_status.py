import os
import glob
import re

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
        flerehan_na = bool(re.search(r"\|\s*\*{0,2}Flerehan\*{0,2}[^|\n]*\|\s*N/A", content, re.IGNORECASE))
        pugnahan_na = bool(re.search(r"\|\s*\*{0,2}Pugnahan\*{0,2}[^|\n]*\|\s*N/A", content, re.IGNORECASE))
        if flerehan_na and pugnahan_na:
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
print(f"Two-Work-Type Compliant: {two_work_compliant} / {relic_entities} ({two_work_compliant/relic_entities*100:.1f}%)")
print(f"Core Stat Line Compliant: {stat_line_compliant} / {total_entities} ({stat_line_compliant/total_entities*100:.1f}%)")
