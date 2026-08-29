import os, re, glob
from bs4 import BeautifulSoup

wiki_root = '/home/user/01_Somnarak_Wiki'

# Character Master Metadata & Stats
CHARACTERS_DATA = {
    'the-director-majin.html': {
        'id': 'CORE-01',
        'title_en': 'Director Majin',
        'title_kr': '관장 마진',
        'dept': 'Executive Suite // Central Control',
        'clearance': 'Level 5 Sovereign',
        'resonance': 'Dawn Absolvohan (528 Hz)',
        'status': 'Active · Dawn Initiative Leader',
        'icon': 'assets/icons/avatar_core_majin.svg',
        'color': '#f1df76',
        'stats': {'fortitude': 'Level V (EX) · 140 HP', 'prudence': 'Level V (EX) · 150 SP', 'temperance': 'Level V (EX) · 100%', 'justice': 'Level V (EX) · 1.5s'},
        'gear': {'weapon': 'Absolvohan Sovereign Scepter', 'suit': 'Director Imperial Greatcoat', 'artifact': 'Core Fusion Chronometer'}
    },
    'the-secretary-seiyon.html': {
        'id': 'CORE-02',
        'title_en': 'Secretary Seiyon',
        'title_kr': '비서 세이연',
        'dept': 'Administrative Intelligence // Gate Watch',
        'clearance': 'Level 5 High Admin',
        'resonance': 'Harmonic Logic (440 Hz)',
        'status': 'Active · AI Construct Synced',
        'icon': 'assets/icons/avatar_core_seiyon.svg',
        'color': '#38bdf8',
        'stats': {'fortitude': 'Level III (Normal) · 90 HP', 'prudence': 'Level V (EX) · 160 SP', 'temperance': 'Level V (EX) · 100%', 'justice': 'Level III (Normal) · 2.0s'},
        'gear': {'weapon': 'Logic Grid Stave', 'suit': 'Secretary Chiffon Uniform', 'artifact': 'Year 4233 Awakening Core'}
    },
    'the-containment-lead-dekan.html': {
        'id': 'CORE-03',
        'title_en': 'Containment Lead Dekan',
        'title_kr': '감금 책임자 데칸',
        'dept': 'Floor 1 // Neutral Core',
        'clearance': 'Level 4 Senior Overseer',
        'resonance': 'Basalt Dampening (120 Hz)',
        'status': 'Active · Sector 1 Stable',
        'icon': 'assets/icons/avatar_core_dekan.svg',
        'color': '#f1df76',
        'stats': {'fortitude': 'Level V (EX) · 130 HP', 'prudence': 'Level IV (Master) · 110 SP', 'temperance': 'Level V (EX) · 95%', 'justice': 'Level III (Normal) · 2.2s'},
        'gear': {'weapon': 'Trench Barricade Shield', 'suit': 'Lead Containment Cuirass', 'artifact': 'Acoustic Dampening Lock'}
    },
    'the-extraction-lead-zyrak.html': {
        'id': 'CORE-04',
        'title_en': 'Extraction Lead Zyrak',
        'title_kr': '추출 책임자 지락',
        'dept': 'Floor 2 // Maw\'s Keep',
        'clearance': 'Level 4 Senior Overseer',
        'resonance': 'Siphon Resonance (280 Hz)',
        'status': 'Active · Forge Operational',
        'icon': 'assets/icons/avatar_core_zyrak.svg',
        'color': '#ef5b55',
        'stats': {'fortitude': 'Level IV (Master) · 120 HP', 'prudence': 'Level IV (Master) · 115 SP', 'temperance': 'Level V (EX) · 95%', 'justice': 'Level IV (Master) · 1.8s'},
        'gear': {'weapon': 'Heavy Forge Maul', 'suit': 'Foundry Basalt Apron', 'artifact': 'Han Fluid Siphon Dial'}
    },
    'the-research-lead-ayshuk.html': {
        'id': 'CORE-05',
        'title_en': 'Research Lead Ayshuk',
        'title_kr': '연구 책임자 아이슉',
        'dept': 'Floor 3 // Insight Forge',
        'clearance': 'Level 4 Senior Overseer',
        'resonance': 'Spectral Prism (620 Hz)',
        'status': 'Active · Analysis Online',
        'icon': 'assets/icons/avatar_core_ayshuk.svg',
        'color': '#38bdf8',
        'stats': {'fortitude': 'Level III (Normal) · 85 HP', 'prudence': 'Level V (EX) · 145 SP', 'temperance': 'Level V (EX) · 100%', 'justice': 'Level III (Normal) · 2.4s'},
        'gear': {'weapon': 'Prism Analysis Scalpel', 'suit': 'Insulated Lab Shroud', 'artifact': 'Resonance Microscope Lens'}
    },
    'the-border-lead-mellda.html': {
        'id': 'CORE-06',
        'title_en': 'Border Lead Mellda',
        'title_kr': '경계 책임자 멜다',
        'dept': 'Floor 4 // Shadow Corps',
        'clearance': 'Level 4 Senior Overseer',
        'resonance': 'Kinetic Strike (180 Hz)',
        'status': 'Active · Sentinel Ready',
        'icon': 'assets/icons/avatar_core_mellda.svg',
        'color': '#f97316',
        'stats': {'fortitude': 'Level V (EX) · 135 HP', 'prudence': 'Level III (Normal) · 95 SP', 'temperance': 'Level IV (Master) · 85%', 'justice': 'Level V (EX) · 1.2s'},
        'gear': {'weapon': 'Border Guard Halberd', 'suit': 'Garrison Flak Armor', 'artifact': 'Outskirts Radar Compass'}
    },
    'the-archive-lead-marjuk.html': {
        'id': 'CORE-07',
        'title_en': 'Archive Lead Marjuk',
        'title_kr': '기록 책임자 마르죽',
        'dept': 'Floor 5 // Deep Vault',
        'clearance': 'Level 4 Senior Overseer',
        'resonance': 'Cryogenic Void (95 Hz)',
        'status': 'Active · Cryo Preserved',
        'icon': 'assets/icons/avatar_core_marjuk.svg',
        'color': '#cbd5e1',
        'stats': {'fortitude': 'Level IV (Master) · 105 HP', 'prudence': 'Level V (EX) · 150 SP', 'temperance': 'Level IV (Master) · 90%', 'justice': 'Level III (Normal) · 2.5s'},
        'gear': {'weapon': 'Basalt Scribe Quill', 'suit': 'Cryo Vault Shroud', 'artifact': 'Basalt Tablet of 1,778 Cycles'}
    },
    'the-outsider-ishall.html': {
        'id': 'CORE-08',
        'title_en': 'The Outsider Ishall',
        'title_kr': '외부인 이샬',
        'dept': 'Floor 6 // Cryo Archive',
        'clearance': 'Level 4 Senior Overseer',
        'resonance': 'Android Sync (360 Hz)',
        'status': 'Active · Monitored',
        'icon': 'assets/icons/avatar_core_ishall.svg',
        'color': '#10b981',
        'stats': {'fortitude': 'Level IV (Master) · 115 HP', 'prudence': 'Level IV (Master) · 120 SP', 'temperance': 'Level IV (Master) · 90%', 'justice': 'Level IV (Master) · 1.6s'},
        'gear': {'weapon': 'Synthetic Filament Wire', 'suit': 'Android Ceramic Frame', 'artifact': 'External Frequency Receiver'}
    },
    'the-exile-xyan.html': {
        'id': 'CORE-09',
        'title_en': 'The Exile Xyan',
        'title_kr': '추방자 시안',
        'dept': 'Floor 7 // Penal Watch',
        'clearance': 'Level 4 Senior Overseer',
        'resonance': 'Execution Pulse (50 Hz)',
        'status': 'Active · Penance Protocol',
        'icon': 'assets/icons/avatar_core_xyan.svg',
        'color': '#ef4444',
        'stats': {'fortitude': 'Level V (EX) · 140 HP', 'prudence': 'Level III (Normal) · 90 SP', 'temperance': 'Level III (Normal) · 75%', 'justice': 'Level V (EX) · 1.1s'},
        'gear': {'weapon': 'Penal Execution Cleaver', 'suit': 'Shackled Iron Plate', 'artifact': 'Guilt Calibration Collar'}
    },
    'taeho.html': {
        'id': 'UCD-01',
        'title_en': 'Commander Taeho',
        'title_kr': '지휘관 태호',
        'dept': 'Underworld Cleanup Descend // Task Force',
        'clearance': 'Level 4 Strike Leader',
        'resonance': 'Tactical Command (210 Hz)',
        'status': 'Active · Operation Ongoing',
        'icon': 'assets/icons/avatar_char_taeho.svg',
        'color': '#ef5b55',
        'stats': {'fortitude': 'Level V (EX) · 130 HP', 'prudence': 'Level IV (Master) · 110 SP', 'temperance': 'Level IV (Master) · 88%', 'justice': 'Level IV (Master) · 1.4s'},
        'gear': {'weapon': 'Heavy Breach Shotgun', 'suit': 'Reinforced Tactical Carapace', 'artifact': 'Strike Telemetry Beacon'}
    },
    'yeonhwa.html': {
        'id': 'SED-01',
        'title_en': 'Cartographer Yeonhwa',
        'title_kr': '지도제작자 연화',
        'dept': 'Somnarak Exploration Decreed // Corps',
        'clearance': 'Level 4 Frontier Lead',
        'resonance': 'Spatial Compass (315 Hz)',
        'status': 'Active · Sector Mapping',
        'icon': 'assets/icons/avatar_char_yeonhwa.svg',
        'color': '#38bdf8',
        'stats': {'fortitude': 'Level III (Normal) · 95 HP', 'prudence': 'Level V (EX) · 140 SP', 'temperance': 'Level V (EX) · 95%', 'justice': 'Level III (Normal) · 2.1s'},
        'gear': {'weapon': 'Surveyor Sextant Rapier', 'suit': 'Topographer Weather Shroud', 'artifact': 'Zone Mapping Astrolabe'}
    },
    'minho.html': {
        'id': 'UCD-02',
        'title_en': 'Investigator Minho',
        'title_kr': '수사관 민호',
        'dept': 'UCD Intelligence Division',
        'clearance': 'Level 3 Detective',
        'resonance': 'Inquiry Logic (480 Hz)',
        'status': 'Active · Infiltration',
        'icon': 'assets/icons/avatar_char_minho.svg',
        'color': '#38bdf8',
        'stats': {'fortitude': 'Level III (Normal) · 90 HP', 'prudence': 'Level IV (Master) · 125 SP', 'temperance': 'Level IV (Master) · 90%', 'justice': 'Level IV (Master) · 1.7s'},
        'gear': {'weapon': 'Forensic Taser Stave', 'suit': 'Concealment Trench Coat', 'artifact': 'Memory Scanner Eyepiece'}
    },
    'soojin.html': {
        'id': 'UCD-03',
        'title_en': 'Entity Handler Soojin',
        'title_kr': '개체 조련사 수진',
        'dept': 'UCD Containment Wing',
        'clearance': 'Level 3 Specialist',
        'resonance': 'Beast Whisper (330 Hz)',
        'status': 'Active · Field Pacification',
        'icon': 'assets/icons/avatar_char_soojin.svg',
        'color': '#10b981',
        'stats': {'fortitude': 'Level IV (Master) · 110 HP', 'prudence': 'Level IV (Master) · 130 SP', 'temperance': 'Level V (EX) · 95%', 'justice': 'Level III (Normal) · 2.0s'},
        'gear': {'weapon': 'Pacification Whip', 'suit': 'Pheromone Neutralizer Vest', 'artifact': 'Sorrow Calming Whistle'}
    },
    'doha.html': {
        'id': 'SED-02',
        'title_en': 'Master Mason Doha',
        'title_kr': '석공 도하',
        'dept': 'SED Defensive Vanguard',
        'clearance': 'Level 3 Vanguard',
        'resonance': 'Granite Ward (110 Hz)',
        'status': 'Active · Fortifying Base',
        'icon': 'assets/icons/avatar_char_doha.svg',
        'color': '#f59e0b',
        'stats': {'fortitude': 'Level V (EX) · 145 HP', 'prudence': 'Level III (Normal) · 85 SP', 'temperance': 'Level IV (Master) · 80%', 'justice': 'Level III (Normal) · 2.4s'},
        'gear': {'weapon': 'Mason Sledge Hammer', 'suit': 'Basalt Reinforced Harness', 'artifact': 'Granite Anchor Chisel'}
    },
    'joon.html': {
        'id': 'UCD-04',
        'title_en': 'Acoustic Engineer Joon',
        'title_kr': '음향 기술자 준',
        'dept': 'UCD Technology Division',
        'clearance': 'Level 3 Tech Officer',
        'resonance': 'Waveform Phase (580 Hz)',
        'status': 'Active · Frequency Grid',
        'icon': 'assets/icons/avatar_char_joon.svg',
        'color': '#38bdf8',
        'stats': {'fortitude': 'Level III (Normal) · 85 HP', 'prudence': 'Level IV (Master) · 135 SP', 'temperance': 'Level V (EX) · 98%', 'justice': 'Level III (Normal) · 2.2s'},
        'gear': {'weapon': 'Sonic Pulse Emitter', 'suit': 'Acoustic Insulated Jumpsuit', 'artifact': 'Tuning Fork Resonator'}
    },
    'sora.html': {
        'id': 'SED-03',
        'title_en': 'The Dreamer Sora',
        'title_kr': '몽상가 소라',
        'dept': 'SED Ethereal Reconnaissance',
        'clearance': 'Level 3 Psychic Lead',
        'resonance': 'Dream Frequency (710 Hz)',
        'status': 'Active · Deep Dive',
        'icon': 'assets/icons/avatar_char_sora.svg',
        'color': '#a855f7',
        'stats': {'fortitude': 'Level II (Vulnerable) · 75 HP', 'prudence': 'Level V (EX) · 165 SP', 'temperance': 'Level V (EX) · 100%', 'justice': 'Level II (Slow) · 2.8s'},
        'gear': {'weapon': 'Dream Needle Dagger', 'suit': 'Ethereal Weave Robes', 'artifact': 'Lucid Sleep Bell'}
    },
    'kael.html': {
        'id': 'OUT-01',
        'title_en': 'Kael the Exile',
        'title_kr': '추방자 카엘',
        'dept': 'Desolate Outskirts // Nomad Sovereign',
        'clearance': 'External Sovereign Leader',
        'resonance': 'Han Storm Surge (85 Hz)',
        'status': 'Active · Independent',
        'icon': 'assets/icons/avatar_char_kael.svg',
        'color': '#ef4444',
        'stats': {'fortitude': 'Level V (EX) · 150 HP', 'prudence': 'Level IV (Master) · 110 SP', 'temperance': 'Level III (Normal) · 75%', 'justice': 'Level V (EX) · 1.2s'},
        'gear': {'weapon': 'Storm Cleaver Greatsword', 'suit': 'Nomad Warlord Cuirass', 'artifact': 'The Scar Horizon Compass'}
    },
    'high-architects.html': {
        'id': 'ORG-01',
        'title_en': 'The High Architects',
        'title_kr': '상위 건축가 길드',
        'dept': 'Zone C // Master Guild Council',
        'clearance': 'Civic Master Authority',
        'resonance': 'Geometric Harmony (400 Hz)',
        'status': 'Active · Infrastructure Control',
        'icon': 'assets/icons/avatar_char_high_architects.svg',
        'color': '#f1df76',
        'stats': {'fortitude': 'Level IV (Master) · 110 HP', 'prudence': 'Level V (EX) · 140 SP', 'temperance': 'Level V (EX) · 100%', 'justice': 'Level III (Normal) · 2.0s'},
        'gear': {'weapon': 'Guild Master Compass Staff', 'suit': 'Ceremonial Draftsman Robes', 'artifact': 'City Blueprint Keystone'}
    },
    'cheonbulok-refugees.html': {
        'id': 'REF-02',
        'title_en': 'Cheonbulok Refugees',
        'title_kr': '천불록 난민 연합',
        'dept': 'Zone E // Corner 2 Colony',
        'clearance': 'Displaced Sovereign Colony',
        'resonance': 'Furnace Ash (150 Hz)',
        'status': 'Active · Survival Vigil',
        'icon': 'assets/icons/avatar_char_cheonbulok_refugees.svg',
        'color': '#f97316',
        'stats': {'fortitude': 'Level IV (Master) · 125 HP', 'prudence': 'Level III (Normal) · 90 SP', 'temperance': 'Level IV (Master) · 85%', 'justice': 'Level IV (Master) · 1.6s'},
        'gear': {'weapon': 'Refugee Defense Speargun', 'suit': 'Ash-Coated Scavenger Cloak', 'artifact': 'Furnace Shard Ember'}
    }
}

# Function to build the side table HTML for a character
def generate_character_infobox(ch_data):
    stats = ch_data['stats']
    gear = ch_data['gear']
    return f"""
      <aside class="character-infobox" style="--entity: {ch_data['color']};">
        <h2 id="{ch_data['id'].lower()}">{ch_data['title_en'].upper()}</h2>
        <div class="infobox-image-wrap">
          <img src="../{ch_data['icon']}" alt="{ch_data['title_en']} Regalia" class="character-portrait" style="border: 2px solid {ch_data['color']};">
          <div style="font-family:'Cinzel', serif; font-size:1.1rem; color:#f8fafc; margin-top:8px; font-weight:bold;">{ch_data['title_en']}</div>
          <div style="font-family:'JetBrains Mono', monospace; font-size:0.85rem; color:{ch_data['color']};">{ch_data['title_kr']}</div>
        </div>

        <dl class="fact-grid">
          <dt>Formal ID</dt>
          <dd>{ch_data['id']}</dd>
          <dt>Department</dt>
          <dd>{ch_data['dept']}</dd>
          <dt>Clearance</dt>
          <dd>{ch_data['clearance']}</dd>
          <dt>Resonance</dt>
          <dd>{ch_data['resonance']}</dd>
          <dt>Status</dt>
          <dd>{ch_data['status']}</dd>
        </dl>

        <h3 id="attribute-ratings">Attribute Ratings</h3>
        <table class="infobox-stat-table">
          <tbody>
            <tr>
              <th>FORTITUDE (HP)</th>
              <td>{stats['fortitude']}</td>
            </tr>
            <tr>
              <th>PRUDENCE (SP)</th>
              <td>{stats['prudence']}</td>
            </tr>
            <tr>
              <th>TEMPERANCE</th>
              <td>{stats['temperance']}</td>
            </tr>
            <tr>
              <th>JUSTICE (SPD)</th>
              <td>{stats['justice']}</td>
            </tr>
          </tbody>
        </table>

        <h3 id="signature-loadout">Signature Loadout</h3>
        <dl class="fact-grid">
          <dt>Weapon</dt>
          <dd style="color:#f1df76;">{gear['weapon']}</dd>
          <dt>Suit / Attire</dt>
          <dd style="color:#38bdf8;">{gear['suit']}</dd>
          <dt>Artifact</dt>
          <dd style="color:#10b981;">{gear['artifact']}</dd>
        </dl>
      </aside>
"""

# Process all character files
char_files = glob.glob(f'{wiki_root}/characters/*.html')

for cf in char_files:
    fname = os.path.basename(cf)
    if fname == 'index.html': continue
    if fname not in CHARACTERS_DATA: continue
    
    with open(cf, 'r', encoding='utf-8') as f:
        html = f.read()
    
    ch = CHARACTERS_DATA[fname]
    infobox_html = generate_character_infobox(ch)
    
    # Check if page already has <div class="character-article">
    if '<div class="character-article">' in html or '<aside class="character-infobox"' in html:
        # Already wrapped or partially updated, let's ensure clean replacement
        continue
    
    # Find main content start
    # Usually right after breadcrumbs or after article-header / toc
    soup = BeautifulSoup(html, 'html.parser')
    main_el = soup.find('main', id='content')
    if not main_el:
        main_el = soup.find('main')
    if not main_el: continue
    
    # Extract child elements after header/breadcrumb/TOC
    # We want to wrap all content sections in <div class="character-article"><div class="character-main-content">...</div>{infobox_html}</div>
    # Let's do regex insertion right before footer or after TOC
    # Let's find toc or article-header
    
    # We can transform by string manipulation to preserve exact styles:
    pattern = r'(<div class="toc" id="toc">[\s\S]*?<\/div>)([\s\S]*?)(<footer class="footer"|<nav class="article-nav"|<!-- Bottom Cross-Reference)'
    match = re.search(pattern, html)
    
    if match:
        toc_part = match.group(1)
        body_part = match.group(2)
        tail_part = match.group(3)
        
        new_middle = f"""{toc_part}
        <div class="character-article">
          <div class="character-main-content">
            {body_part.strip()}
          </div>
          {infobox_html}
        </div>
        {tail_part}"""
        
        new_html = html[:match.start()] + new_middle + html[match.end():]
        with open(cf, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"SUCCESS: Injected 2-Column Side Table Infobox into {fname}")

print("Completed processing all character pages!")
