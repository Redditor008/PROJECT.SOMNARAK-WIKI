import os, sys, re, html
sys.path.insert(0, '/home/user')
from tools.build_deep_canon_wiki import get_base_template
from tools.convert_echo_cores import parse_markdown_to_wiki_sections, format_lines_to_html

SOURCE_DIR = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/World_Reference"
DEPT_DIR = "/home/user/01_Somnarak_Wiki/departments"
CHAR_DIR = "/home/user/01_Somnarak_Wiki/characters"
FACT_DIR = "/home/user/01_Somnarak_Wiki/factions"

with open(os.path.join(SOURCE_DIR, "The_REVERIE_DIRECTORATE.md"), 'r', encoding='utf-8') as f:
    rd_raw = f.read()

# 1. Master Directorate Faction Page
quote_rd, author_rd, sections_rd = parse_markdown_to_wiki_sections(rd_raw)
toc_rd = [(re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec', t) for t, _ in sections_rd if t != "Overview"]
content_rd = []
if quote_rd:
    content_rd.append(f'<div class="wiki-quote"><p>“{quote_rd}”</p><div class="quote-author">— {author_rd}</div></div>')
for t, lines in sections_rd:
    sid = re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec'
    content_rd.append(f'<section class="wiki-section" id="{sid}"><h2 class="section-title">{t}</h2>{format_lines_to_html(lines)}</section>')
html_rd = get_base_template("The Reverie Directorate", "Factions", "factions/index.html", "../", '\n'.join(content_rd), toc_rd)
with open(os.path.join(FACT_DIR, "the-reverie-directorate.html"), 'w', encoding='utf-8') as f:
    f.write(html_rd)
print(f"Generated: factions/the-reverie-directorate.html ({len(html_rd)} chars, {len(sections_rd)} sections)")

# 2. Departments: Incident Reports Archive
incidents_text = ""
for t, lines in sections_rd:
    if "incident" in t.lower():
        incidents_text = '\n'.join(lines)
        break
if incidents_text:
    inc_quote, inc_auth, inc_sections = parse_markdown_to_wiki_sections(incidents_text)
    inc_toc = [(re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec', t) for t, _ in inc_sections if t != "Overview"]
    inc_body = []
    for t, lines in inc_sections:
        sid = re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec'
        inc_body.append(f'<section class="wiki-section" id="{sid}"><h2 class="section-title">{t}</h2>{format_lines_to_html(lines)}</section>')
    html_inc = get_base_template("Facility Incident Reports Archive", "Departments", "departments/index.html", "../", '\n'.join(inc_body), inc_toc)
    with open(os.path.join(DEPT_DIR, "incident-reports-archive.html"), 'w', encoding='utf-8') as f:
        f.write(html_inc)
    print(f"Generated: departments/incident-reports-archive.html ({len(html_inc)} chars)")

# 3. Facility Room Types
room_text = ""
for t, lines in sections_rd:
    if "room types" in t.lower() or "facility layout" in t.lower():
        room_text += '\n'.join(lines) + '\n\n'
if room_text:
    rm_quote, rm_auth, rm_sections = parse_markdown_to_wiki_sections(room_text)
    rm_toc = [(re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec', t) for t, _ in rm_sections if t != "Overview"]
    rm_body = []
    for t, lines in rm_sections:
        sid = re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec'
        rm_body.append(f'<section class="wiki-section" id="{sid}"><h2 class="section-title">{t}</h2>{format_lines_to_html(lines)}</section>')
    html_rm = get_base_template("Facility Architecture & Room Types", "Departments", "departments/index.html", "../", '\n'.join(rm_body), rm_toc)
    with open(os.path.join(DEPT_DIR, "facility-room-types.html"), 'w', encoding='utf-8') as f:
        f.write(html_rm)
    print(f"Generated: departments/facility-room-types.html ({len(html_rm)} chars)")

# 4. Generate 8 Floors
floor_data = [
    ("floor-1-neutral-command.html", "Floor 1: Neutral Command", "The Central Nexus & Directorate Oversight", "Director Majin", "Echo-Core 1", 
     "Floor 1 serves as the absolute command core of the Hand of Change. Overseen directly by Director Majin, this floor houses the Alpha Siphon conduit valves, master alarm arrays, executive briefing rooms, and the high-security singularity chamber."),
    ("floor-2-maws-keep.html", "Floor 2: Maw's Keep", "Sorrow Entity Containment & High-Density Ward", "Seiyon / Dekan", "Echo-Core 2 & 3",
     "Floor 2 houses the primary containment blocks for ZAYIN, TETH, and HE threat Sorrow Entities. Equipped with reinforced Han-dampening titanium bulkheads, Qliphoth frequency modulators, and automated gas purge protocols."),
    ("floor-3-extraction-hall.html", "Floor 3: Extraction Hall", "M.A.W. Siphoning & Crystallization Labs", "Zyrak", "Echo-Core 4",
     "Floor 3 is the industrial heart of the Directorate's armaments. Here, pure sorrow resonance is harvested and refined into M.A.W. Weapons, Suits, and Gifts under the supervision of Master Artisan Zyrak."),
    ("floor-4-insight-forge.html", "Floor 4: Insight Forge", "Han Kinetics & Anomaly Research", "Ayshuk", "Echo-Core 5",
     "Floor 4 conducts deep theoretical and empirical research into Han particle physics, soul resonance waves, taboo calcification, and cognitive memory stability led by Chief Researcher Ayshuk."),
    ("floor-5-border-watch.html", "Floor 5: Border Watch", "Perimeter Acoustic Bastion & Signal Defense", "Mellda", "Echo-Core 6",
     "Floor 5 monitors all external boundaries, acoustic echoes from The Desolate, and perimeter breaches. Guarded by Warden Mellda, it features seismic sensors, soundproof blast shields, and barrier projection pylons."),
    ("floor-6-deep-vault.html", "Floor 6: Deep Vault", "Precursor Relics & Cryogenic Name Archive", "Marjuk", "Echo-Core 7",
     "Floor 6 plunges into the subterranean bedrock, safeguarding over 1.4 million preserved citizen identities, Grade I–V Han Relics, forbidden history records, and cryogenic memory cylinders managed by Archivist Marjuk."),
    ("floor-7-shadow-corps.html", "Floor 7: Shadow Corps", "Desolate Reconnaissance & Void Diving", "Ishall", "Echo-Core 8",
     "Floor 7 coordinates deep-range expedition teams, void divers, and covert surveillance operatives heading beyond the Veil into the toxic wastes of The Desolate under the command of Scout Ishall."),
    ("floor-8-gate-watch.html", "Floor 8: Gate Watch", "The Forbidden Gate & Taboo Boundary", "Xyan", "Echo-Core 9",
     "Floor 8 stands at the lowest point of the facility, sealing the primordial fracture known as the Forbidden Gate. Overseen by the Exile Xyan, this floor enforces Absolute Taboo containment and monitors abyssal resonance spikes.")
]

for fname, title, subtitle, lead_name, lead_title, desc in floor_data:
    floor_num = fname.split('-')[1]
    
    # Extract relevant text from rd_raw
    dept_lines = []
    in_dept = False
    for line in rd_raw.splitlines():
        if f"Echo-Core {floor_num}" in line or f"Floor {floor_num}" in line:
            in_dept = True
        elif line.startswith('## Echo-Core') and f"Echo-Core {floor_num}" not in line:
            in_dept = False
        if in_dept:
            dept_lines.append(line)
            
    content_html = f'''
    <div class="wiki-callout">
      <p><strong>DEPARTMENT OVERVIEW:</strong> {desc}</p>
    </div>
    
    <div class="table-wrap">
      <table class="wiki-table">
        <thead>
          <tr>
            <th>Department Field</th>
            <th>Specification</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Department Name</strong></td>
            <td>{title}</td>
          </tr>
          <tr>
            <td><strong>Department Lead</strong></td>
            <td><a href="../characters/{lead_name.lower().replace(' ', '-').replace('/', '-').split('-')[0]}.html" class="wiki-link">{lead_name}</a> ({lead_title})</td>
          </tr>
          <tr>
            <td><strong>Floor Assignment</strong></td>
            <td>Floor {floor_num} — Hand of Change</td>
          </tr>
          <tr>
            <td><strong>Primary Mandate</strong></td>
            <td>{subtitle}</td>
          </tr>
          <tr>
            <td><strong>Risk Rating</strong></td>
            <td><span class="badge badge-source">LEVEL {floor_num} RESTRICTED</span></td>
          </tr>
        </tbody>
      </table>
    </div>
    
    <section class="wiki-section" id="operational-protocols">
      <h2 class="section-title">Operational Protocols &amp; Directives</h2>
      <p>Personnel assigned to {title} must adhere strictly to Directorate safety regulations. Regular cognitive audits and resonance screening are mandatory every 48 hours to prevent Han contamination and taboo calcification.</p>
      <ul>
        <li><strong>Standard Work Types:</strong> Insight, Attachment, Repression, and Extraction assignments.</li>
        <li><strong>Resonance Threshold:</strong> Qliphoth frequency counters must be maintained above level 3 at all times.</li>
        <li><strong>Emergency Lockdown:</strong> In the event of a breach, blast doors seal within 3.5 seconds of acoustic alert trigger.</li>
      </ul>
    </section>
    
    <section class="wiki-section" id="facility-specifications">
      <h2 class="section-title">Floor Layout &amp; Sub-Units</h2>
      {format_lines_to_html(dept_lines) if dept_lines else "<p>Floor architectural schematics and containment chamber layouts are cataloged under Hand of Change Master Blueprints.</p>"}
    </section>
    '''
    
    toc = [
        ("operational-protocols", "Operational Protocols & Directives"),
        ("facility-specifications", "Floor Layout & Sub-Units")
    ]
    
    page = get_base_template(title, "Facility Floors", "departments/index.html", "../", content_html, toc)
    with open(os.path.join(DEPT_DIR, fname), 'w', encoding='utf-8') as f:
        f.write(page)
    print(f"Generated: departments/{fname} ({len(page)} chars)")

print("Departments generated.")
