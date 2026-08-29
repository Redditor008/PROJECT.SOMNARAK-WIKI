import os, sys, re, html
sys.path.insert(0, '/home/user')
from tools.build_deep_canon_wiki import get_base_template
from tools.convert_echo_cores import parse_markdown_to_wiki_sections, format_lines_to_html

SOURCE_DIR = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/World_Reference"
CHAR_DIR = "/home/user/01_Somnarak_Wiki/characters"
FACT_DIR = "/home/user/01_Somnarak_Wiki/factions"

with open(os.path.join(SOURCE_DIR, "SOMNARAK_CAST.md"), 'r', encoding='utf-8') as f:
    cast_raw = f.read()

with open(os.path.join(SOURCE_DIR, "SOMNARAK_SED.md"), 'r', encoding='utf-8') as f:
    sed_raw = f.read()

with open(os.path.join(SOURCE_DIR, "SOMNARAK_UCD.md"), 'r', encoding='utf-8') as f:
    ucd_raw = f.read()

def extract_section_by_header(text, header_pattern):
    lines = text.splitlines()
    found = False
    section_lines = []
    level = 2
    for line in lines:
        if re.search(header_pattern, line, re.IGNORECASE):
            found = True
            # determine level
            m = re.match(r'^(#+)', line)
            if m:
                level = len(m.group(1))
            section_lines.append(line)
            continue
        if found:
            # check if next section of same or higher level starts
            m = re.match(r'^(#+)\s', line)
            if m and len(m.group(1)) <= level:
                break
            section_lines.append(line)
    return '\n'.join(section_lines)

# 1. Build SED Corps Faction Page
quote_sed, author_sed, sections_sed = parse_markdown_to_wiki_sections(sed_raw)
toc_sed = [(re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec', t) for t, _ in sections_sed if t != "Overview"]
content_sed = []
if quote_sed:
    content_sed.append(f'<div class="wiki-quote"><p>“{quote_sed}”</p><div class="quote-author">— {author_sed}</div></div>')
for t, lines in sections_sed:
    sid = re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec'
    content_sed.append(f'<section class="wiki-section" id="{sid}"><h2 class="section-title">{t}</h2>{format_lines_to_html(lines)}</section>')
html_sed = get_base_template("Sorrow Exploration Division (SED)", "Factions", "factions/index.html", "../", '\n'.join(content_sed), toc_sed)
with open(os.path.join(FACT_DIR, "the-sed-corps.html"), 'w', encoding='utf-8') as f:
    f.write(html_sed)
print(f"Generated: factions/the-sed-corps.html ({len(html_sed)} chars, {len(sections_sed)} sections)")

# 2. Build UCD Strike Force Faction Page
quote_ucd, author_ucd, sections_ucd = parse_markdown_to_wiki_sections(ucd_raw)
toc_ucd = [(re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec', t) for t, _ in sections_ucd if t != "Overview"]
content_ucd = []
if quote_ucd:
    content_ucd.append(f'<div class="wiki-quote"><p>“{quote_ucd}”</p><div class="quote-author">— {author_ucd}</div></div>')
for t, lines in sections_ucd:
    sid = re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec'
    content_ucd.append(f'<section class="wiki-section" id="{sid}"><h2 class="section-title">{t}</h2>{format_lines_to_html(lines)}</section>')
html_ucd = get_base_template("Underworld Containment Division (UCD)", "Factions", "factions/index.html", "../", '\n'.join(content_ucd), toc_ucd)
with open(os.path.join(FACT_DIR, "the-ucd-strike-force.html"), 'w', encoding='utf-8') as f:
    f.write(html_ucd)
print(f"Generated: factions/the-ucd-strike-force.html ({len(html_ucd)} chars, {len(sections_ucd)} sections)")

