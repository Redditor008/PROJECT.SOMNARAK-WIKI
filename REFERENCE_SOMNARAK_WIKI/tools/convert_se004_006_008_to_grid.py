import os, re
from bs4 import BeautifulSoup

wiki_root = '/home/user/01_Somnarak_Wiki'

for fname, data in {
    'se-004-the-rust-bleeding-sentry.html': {
        'id': 'SE-004',
        'name_en': 'The Rust-Bleeding Sentry',
        'name_kr': '녹을 흘리는 보초',
        'color': '#f97316',
        'secc': 'C-IIIγ-004 [VS]',
        'class': 'Normal SE',
        'origin': 'City Sorrow',
        'coherence': 'III — Fragment',
        'potency': 'γ — Major',
        'element': 'Grudge — Crimson',
        'manifestation': 'Subject-Automaton',
        'location': 'SECTOR-E-05 — Border Gate 14',
        'observation': '3 — Advanced / Understood',
        'status': 'Active — contained border outpost',
        'gauge': '450 / 450',
        'starting_gauge': '30–50%',
        'pressure': '14–28 Grudge',
        'resistance': '50% Grudge; 20% other',
        'speed': '1.80 m/s',
        'icon': 'assets/art/entities/se-004-icon.svg',
        'profile': 'assets/art/entities/se-004-profile.svg'
    },
    'se-006-the-siphon-leech.html': {
        'id': 'SE-006',
        'name_en': 'The Siphon Leech',
        'name_kr': '착취하는 거머리',
        'color': '#10b981',
        'secc': 'C-IIβ-006 [VO]',
        'class': 'Normal SE',
        'origin': 'City Sorrow',
        'coherence': 'II — Echo',
        'potency': 'β — Moderate',
        'element': 'Weight — Dual HP+SP',
        'manifestation': 'Subject-Organism',
        'location': 'SECTOR-B-03 — Subterranean Drainage',
        'observation': '3 — Advanced / Understood',
        'status': 'Active — contained flume basin',
        'gauge': '380 / 380',
        'starting_gauge': '40–60%',
        'pressure': '10–20 Weight',
        'resistance': '40% Weight; 20% other',
        'speed': '1.40 m/s',
        'icon': 'assets/art/entities/se-006-icon.svg',
        'profile': 'assets/art/entities/se-006-profile.svg'
    },
    'se-008-the-iron-maiden-of-regret.html': {
        'id': 'SE-008',
        'name_en': 'The Iron Maiden of Regret',
        'name_kr': '후회의 철처녀',
        'color': '#ef4444',
        'secc': 'C-IVδ-008 [VS]',
        'class': 'Normal SE',
        'origin': 'Inner Sorrow',
        'coherence': 'IV — Entity',
        'potency': 'δ — Critical',
        'element': 'Grudge/Lament — Dual Strike',
        'manifestation': 'Subject-Reliquary',
        'location': 'SECTOR-F-08 — Deep Vault Sector 6',
        'observation': '3 — Advanced / Understood',
        'status': 'Active — locked containment chamber',
        'gauge': '680 / 680',
        'starting_gauge': '50–70%',
        'pressure': '20–35 Grudge / 20–35 Lament',
        'resistance': '40% Grudge; 40% Lament; 20% Void',
        'speed': '0.00 m/s (Stationary)',
        'icon': 'assets/art/entities/se-008-icon.svg',
        'profile': 'assets/art/entities/se-008-profile.svg'
    }
}.items():
    fpath = f'{wiki_root}/entities/{fname}'
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    infobox_aside = f"""
        <aside class="entity-infobox" style="--entity: {data['color']};">
          <h2 id="{data['id'].lower()}">{data['id']}</h2>
          <div class="infobox-image-wrap">
            <img src="../{data['profile']}" alt="{data['name_en']}" class="character-portrait" style="border: 2px solid {data['color']};">
            <div style="font-family:'Cinzel', serif; font-size:1.1rem; color:#f8fafc; margin-top:8px; font-weight:bold;">{data['name_en']}</div>
            <div style="font-family:'JetBrains Mono', monospace; font-size:0.85rem; color:{data['color']};">{data['name_kr']}</div>
          </div>

          <dl class="fact-grid">
            <dt>Formal ID</dt>
            <dd>{data['id']}</dd>
            <dt>Source SECC</dt>
            <dd>{data['secc']}</dd>
            <dt>Wiki Class</dt>
            <dd>{data['class']}</dd>
            <dt>Origin</dt>
            <dd>{data['origin']}</dd>
            <dt>Coherence</dt>
            <dd>{data['coherence']}</dd>
            <dt>Potency</dt>
            <dd>{data['potency']}</dd>
            <dt>Element</dt>
            <dd>{data['element']}</dd>
            <dt>Location</dt>
            <dd>{data['location']}</dd>
            <dt>Observation</dt>
            <dd>{data['observation']}</dd>
            <dt>Status</dt>
            <dd>{data['status']}</dd>
          </dl>

          <h3 id="operational-data">Operational Data</h3>
          <dl class="fact-grid">
            <dt>Sorrow Gauge</dt>
            <dd>{data['gauge']}</dd>
            <dt>Starting Gauge</dt>
            <dd>{data['starting_gauge']}</dd>
            <dt>Han Pressure</dt>
            <dd>{data['pressure']}</dd>
            <dt>Resistance</dt>
            <dd>{data['resistance']}</dd>
            <dt>Speed / Scale</dt>
            <dd>{data['speed']}</dd>
          </dl>
        </aside>"""

    # Strip existing <div class="infobox-wrapper">...</div>
    html = re.sub(r'<div class="infobox-wrapper"[\s\S]*?<\/div>\s*<\/div>', '', html)
    
    # Wrap main sections into <div class="entity-article"><div class="entity-main-content">...</div>{infobox_aside}</div>
    match = re.search(r'(<div class="toc" id="toc">[\s\S]*?<\/div>)([\s\S]*?)(<footer class="footer"|<footer class="wiki-footer")', html)
    if match:
        toc_part = match.group(1)
        body_part = match.group(2).strip()
        tail_part = match.group(3)
        
        replacement = f"""{toc_part}
      <div class="entity-article">
        <div class="entity-main-content">
          {body_part}
        </div>
        {infobox_aside}
      </div>
      {tail_part}"""
        new_html = html[:match.start()] + replacement + html[match.end():]
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"SUCCESS: Converted {fname} to 2-column Grid with Side Infobox!")

print("All entity pages now follow identical 2-column Grid format with Side Infobox!")
