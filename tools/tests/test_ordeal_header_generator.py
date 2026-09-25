import glob
import re

files = glob.glob("SOMNARAK-WORLD/Ordeals/*.md")
p_form = re.compile(r'\*\*Physical Form:\*\*\s*([A-Za-z0-9\-]+)')

for f in files[:5]:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    forms = []
    for line in txt.splitlines():
        m = p_form.search(line)
        if m:
            forms.append(m.group(1))
    unique_forms = sorted(list(set(forms)))
    print(f"{os.path.basename(f)}: actual forms = {unique_forms}")
