import glob
import re

files = glob.glob("SOMNARAK-WORLD/Sorrow_Entities/*.md")
files = [f for f in files if "README" not in f]

non_subjects = []
two_work_compliant = []
needs_fix = []

for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        t = fp.read()
    m = re.search(r"\*\*(?:Entity Type|Type)\*\*\s*\|\s*([^|\n]+)", t)
    if m:
        etype_raw = m.group(1).strip()
        etype = etype_raw.split("—")[0].split("-")[0].strip()
        if etype in ["**Object/Place**", "**Time**", "**Object**", "**Place**", "**Place (Special Transform Type)**"]:
            non_subjects.append(f)
            
            # Check Section 2: Operational Parameters -> Work Types table
            # Must have Flerehan = N/A and Pugnahan = N/A
            op_match = re.search(r"## Operational Parameters.*?(?=## Combat Record|## Appearance)", t, re.DOTALL)
            if op_match:
                op_text = op_match.group(0)
                flerehan_na = bool(re.search(r"\|\s*\*{0,2}Flerehan\*{0,2}\s*\|[^|\n]*(?:N/A|Prohibited|Not Applicable)", op_text, re.IGNORECASE))
                pugnahan_na = bool(re.search(r"\|\s*\*{0,2}Pugnahan\*{0,2}\s*\|[^|\n]*(?:N/A|Prohibited|Not Applicable)", op_text, re.IGNORECASE))
                if flerehan_na and pugnahan_na:
                    two_work_compliant.append(f)
                else:
                    needs_fix.append((f, flerehan_na, pugnahan_na))
            else:
                needs_fix.append((f, False, False))

print(f"Total Non-Subject Entities (Object, Place, Time): {len(non_subjects)}")
print(f"Compliant with Two-Work-Type Rule: {len(two_work_compliant)} / {len(non_subjects)} ({len(two_work_compliant)/len(non_subjects)*100:.1f}%)")
print(f"Entities needing Two-Work-Type Rule alignment: {len(needs_fix)}")
if needs_fix:
    print(f"Sample needing alignment: {[os.path.basename(x[0]) for x in needs_fix[:5]]}")
