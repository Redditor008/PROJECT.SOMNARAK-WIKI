import glob
import re
import os

files = sorted(glob.glob("SOMNARAK-WORLD/Ordeals/*.md"))
entities_with_placeholder = []

p_entity = re.compile(r'### ([^\n]+)')
p_placeholder = re.compile(r'\*\*Ability:\*\*\s*Deals damage themed to its form and element\.\s*(\*\*\[.*?\]\*\*)?', re.IGNORECASE)

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    curr_entity = None
    for idx, line in enumerate(lines):
        m_ent = p_entity.search(line)
        if m_ent:
            curr_entity = m_ent.group(1).strip()
        m_pl = p_placeholder.search(line)
        if m_pl:
            entities_with_placeholder.append((f, curr_entity, line.strip()))

print(f"Total entities with placeholder: {len(entities_with_placeholder)}")
for f, ent, l in entities_with_placeholder[:15]:
    print(f"{os.path.basename(f)} -> {ent} : {l}")
