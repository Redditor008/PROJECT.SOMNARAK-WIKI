import glob
import re
import os

files = sorted(glob.glob("SOMNARAK-WORLD/Ordeals/*.md"))
unique_ents = set()

p_entity = re.compile(r'### ([^\n]+)')
p_placeholder = re.compile(r'\*\*Ability:\*\*\s*Deals damage themed to its form and element\.', re.IGNORECASE)

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    curr_entity = None
    for line in lines:
        m_ent = p_entity.search(line)
        if m_ent:
            curr_entity = m_ent.group(1).split('(')[0].strip()
        if p_placeholder.search(line) and curr_entity:
            unique_ents.add(curr_entity)

print("Unique entity names with placeholder:", sorted(unique_ents))
