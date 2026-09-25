import glob
import re

files = glob.glob("SOMNARAK-WORLD/Sorrow_Entities/*.md")
target_pat = re.compile(r'not permanent healing', re.IGNORECASE)

sampled = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    if target_pat.search(txt):
        sampled += 1
        print(f"=== SAMPLE {sampled}: {f} ===")
        idx = txt.find("### Operational Work Notes")
        end = txt.find("## Breach Behavior", idx)
        if end == -1: end = idx + 1000
        print(txt[idx:end])
        if sampled >= 3:
            break
