import os, sys, re, html
sys.path.insert(0, '/home/user')
from tools.build_deep_canon_wiki import get_base_template
from tools.convert_echo_cores import parse_markdown_to_wiki_sections, format_lines_to_html

SOURCE_DIR = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/World_Reference"
CHAR_DIR = "/home/user/01_Somnarak_Wiki/characters"

with open(os.path.join(SOURCE_DIR, "SOMNARAK_CAST.md"), 'r', encoding='utf-8') as f:
    cast_text = f.read()

# Let's inspect sections in SOMNARAK_CAST.md
quote_c, auth_c, cast_sections = parse_markdown_to_wiki_sections(cast_text)

# Build a comprehensive cast page / individual pages
cast_targets = {
    "kael.html": ("Kael (The Wanderer)", "Resonant Pilgrim & Outskirts Survivor", ["kael", "wanderer", "pilgrim"]),
    "soojin.html": ("Soojin (The Archivist's Apprentice)", "Fray Weaver & Memory Transcriber", ["soojin", "apprentice", "weaver"]),
    "yeonhwa.html": ("Yeonhwa (Lead Cartographer)", "SED Field Expedition Commander", ["yeonhwa", "cartographer", "sed"]),
    "taeho.html": ("Taeho (Strike Commander)", "UCD Containment Tactical Lead", ["taeho", "commander", "ucd"]),
    "minho.html": ("Minho (Containment Specialist)", "UCD Heavy Shield & Breach Suppression", ["minho", "containment specialist"]),
    "sora.html": ("Sora (Acoustic Scout)", "SED Soundwave Mapper & Doorspeech Listener", ["sora", "acoustic scout"]),
    "doha.html": ("Doha (Resonance Stabilizer)", "SED Field Medic & Han Therapist", ["doha", "stabilizer", "medic"]),
    "joon.html": ("Joon (Breach Specialist)", "UCD Vanguard & Kinetic Shock Operative", ["joon", "breach specialist"]),
    "high-architects.html": ("The High Architects of Cheonbulok", "Spire Engineering & Precursor Masonry Guild", ["architect", "cheonbulok", "spire"]),
    "cheonbulok-refugees.html": ("Cheonbulok Refugees Collective", "Subterranean Survivors & Displaced Citizens", ["refugee", "displaced", "survivor"]),
}

for dst_file, (char_title, char_sub, keywords) in cast_targets.items():
    # Filter matching sections from cast_text
    relevant_sections = []
    for s_title, s_lines in cast_sections:
        s_text_all = (s_title + " " + "\n".join(s_lines)).lower()
        if any(kw in s_text_all for kw in keywords):
            relevant_sections.append((s_title, s_lines))
            
    if not relevant_sections:
        # include general cast overview
        relevant_sections = cast_sections[:3]
        
    toc = [(re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec', t) for t, _ in relevant_sections]
    body_parts = []
    
    body_parts.append(f'''
    <div class="wiki-callout">
      <p><strong>CHARACTER DOSSIER:</strong> {char_title} — {char_sub}. Sourced directly from the official Somnarak Cast Register and personnel archives.</p>
    </div>
    ''')
    
    for t, lines in relevant_sections:
        sid = re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec'
        body_parts.append(f'<section class="wiki-section" id="{sid}"><h2 class="section-title">{t}</h2>{format_lines_to_html(lines)}</section>')
        
    html_page = get_base_template(
        title=char_title,
        category_label="Characters",
        category_href="characters/index.html",
        rel_prefix="../",
        content_html='\n'.join(body_parts),
        toc_items=toc
    )
    
    out_path = os.path.join(CHAR_DIR, dst_file)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_page)
    print(f"Generated cast dossier: characters/{dst_file} ({len(html_page)} chars, {len(relevant_sections)} sections)")

print("All secondary cast member pages built directly from SOMNARAK_CAST.md.")
