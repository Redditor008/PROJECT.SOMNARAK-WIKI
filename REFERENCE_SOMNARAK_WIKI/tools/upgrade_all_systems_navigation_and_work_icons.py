import os

def upgrade_systems_and_navigation_icons():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    icons_dir = os.path.join(wiki_root, "assets/icons")
    user_icons_dir = "/home/user/icons"

    rich_icons = {}

    # 1. COHERENCE COUNTER GAUGES (coh_1.svg to coh_5.svg & coherence.svg)
    for i in range(1, 6):
        fill_bars = "".join([f'<rect x="{14 + j*18}" y="36" width="14" height="24" rx="2" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>' for j in range(i)])
        empty_bars = "".join([f'<rect x="{14 + j*18}" y="36" width="14" height="24" rx="2" fill="#0c4a6e" stroke="#38bdf8" stroke-width="0.8" opacity="0.4"/>' for j in range(i, 5)])
        
        rich_icons[f"coh_{i}.svg"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="6,12 114,12 114,108 6,108" fill="#031526" stroke="#38bdf8" stroke-width="3"/>
  <text x="14" y="28" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">COHERENCE [{i}/5]</text>
  {fill_bars}
  {empty_bars}
  <line x1="14" y1="74" x2="106" y2="74" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4 2"/>
  <text x="60" y="96" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">STABILITY: T-{i}</text>
</svg>'''

    rich_icons["coherence.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,32 114,88 60,114 6,88 6,32" fill="#031526" stroke="#38bdf8" stroke-width="3.5"/>
  <circle cx="60" cy="60" r="28" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6 3"/>
  <circle cx="60" cy="60" r="16" fill="#0c4a6e" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="60" cy="60" r="6" fill="#ffffff"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">COHERENCE COUNTER</text>
</svg>'''

    # 2. NAVIGATION ICONS (Rich Cybernetic Terminal Navigation)
    rich_icons["nav_home.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#04140d" stroke="#71efaf" stroke-width="3.5"/>
  <path d="M 30,56 L 60,30 L 90,56 L 82,56 L 82,86 L 38,86 L 38,56 Z" fill="#064e3b" stroke="#71efaf" stroke-width="2.5"/>
  <rect x="52" y="62" width="16" height="24" rx="2" fill="#f1df76"/>
  <circle cx="60" cy="46" r="4" fill="#ffffff"/>
  <text x="60" y="104" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">FACILITY 01</text>
</svg>'''

    rich_icons["nav_entities.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1f0608" stroke="#ef5b55" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="26" fill="none" stroke="#ef5b55" stroke-width="2" stroke-dasharray="6 3"/>
  <polygon points="60,26 84,68 36,68" fill="#450a0a" stroke="#ffffff" stroke-width="1.8"/>
  <circle cx="60" cy="54" r="7" fill="#f1df76" stroke="#ef5b55" stroke-width="1.5"/>
  <circle cx="60" cy="54" r="3" fill="#ffffff"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">SORROW ENTITIES</text>
</svg>'''

    rich_icons["nav_maw.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="60,22 88,38 80,78 60,90 40,78 32,38" fill="#451a03" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="30" y1="84" x2="90" y2="24" stroke="#ffffff" stroke-width="3"/>
  <circle cx="60" cy="54" r="6" fill="#ef5b55"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">M.A.W. SUITE</text>
</svg>'''

    rich_icons["nav_characters.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#031526" stroke="#38bdf8" stroke-width="3.5"/>
  <circle cx="60" cy="42" r="14" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 32,84 C 32,64 88,64 88,84 Z" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="60,24 66,32 54,32" fill="#f1df76"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">PERSONNEL</text>
</svg>'''

    rich_icons["nav_locations.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#130421" stroke="#c084fc" stroke-width="3.5"/>
  <polygon points="60,24 88,40 88,72 60,88 32,72 32,40" fill="#3b0764" stroke="#c084fc" stroke-width="2"/>
  <circle cx="60" cy="56" r="8" fill="#f1df76"/>
  <line x1="60" y1="24" x2="60" y2="88" stroke="#38bdf8" stroke-width="1.2"/>
  <line x1="32" y1="56" x2="88" y2="56" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="60" y="104" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">ATLAS & ZONES</text>
</svg>'''

    rich_icons["nav_factions.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c0709" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="60,22 92,76 28,76" fill="#450a0a" stroke="#ef5b55" stroke-width="2"/>
  <polygon points="60,38 76,70 44,70" fill="#f1df76"/>
  <circle cx="60" cy="54" r="4" fill="#ffffff"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">FACTIONS</text>
</svg>'''

    rich_icons["nav_lore.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <path d="M 28,34 Q 60,44 60,82 Q 60,44 92,34 L 92,74 Q 60,84 60,84 Q 60,84 28,74 Z" fill="#451a03" stroke="#f1df76" stroke-width="2.2"/>
  <line x1="60" y1="44" x2="60" y2="84" stroke="#ffffff" stroke-width="2"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">CHRONICLES</text>
</svg>'''

    rich_icons["nav_ordeals.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1f0407" stroke="#ef5b55" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="26" fill="none" stroke="#ef5b55" stroke-width="2" stroke-dasharray="8 4"/>
  <polygon points="60,20 68,46 94,54 68,62 60,88 52,62 26,54 52,46" fill="#f1df76" stroke="#ffffff" stroke-width="1.2"/>
  <circle cx="60" cy="54" r="5" fill="#ef5b55"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">ORDEALS</text>
</svg>'''

    # 3. WORK PROCESS ICONS (120x120 viewBox)
    work_methods = {
        "instinct": {
            "name": "INSTINCT // COHERENCE",
            "col": "#71efaf",
            "bg": "#021f14",
            "desc": "BIOLOGICAL / SOMATIC",
            "svg": '''<path d="M 40,24 Q 60,44 40,64 Q 60,84 40,94" fill="none" stroke="#71efaf" stroke-width="3"/>
<path d="M 80,24 Q 60,44 80,64 Q 60,84 80,94" fill="none" stroke="#71efaf" stroke-width="3"/>
<line x1="42" y1="36" x2="78" y2="36" stroke="#f1df76" stroke-width="2"/>
<line x1="50" y1="54" x2="70" y2="54" stroke="#ffffff" stroke-width="2.5"/>
<line x1="42" y1="72" x2="78" y2="72" stroke="#f1df76" stroke-width="2"/>'''
        },
        "insight": {
            "name": "INSIGHT // NEURAL",
            "col": "#f1df76",
            "bg": "#1c1402",
            "desc": "COGNITIVE / RESEARCH",
            "svg": '''<circle cx="60" cy="54" r="26" fill="none" stroke="#f1df76" stroke-width="2" stroke-dasharray="6 3"/>
<polygon points="60,32 78,64 42,64" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
<circle cx="60" cy="54" r="6" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
<line x1="32" y1="30" x2="88" y2="78" stroke="#ffffff" stroke-width="1" stroke-dasharray="2 2"/>'''
        },
        "attachment": {
            "name": "ATTACHMENT // HARMONIC",
            "col": "#38bdf8",
            "bg": "#031526",
            "desc": "EMOTIONAL / COMMUNION",
            "svg": '''<path d="M 60,78 C 30,56 30,34 46,34 C 54,34 60,42 60,42 C 60,42 66,34 74,34 C 90,34 90,56 60,78 Z" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2.5"/>
<circle cx="60" cy="52" r="6" fill="#f1df76"/>
<ellipse cx="60" cy="52" rx="28" ry="12" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="4 2"/>'''
        },
        "repression": {
            "name": "REPRESSION // STRUCTURAL",
            "col": "#ef5b55",
            "bg": "#1f0608",
            "desc": "SUPPRESSION / FORCE",
            "svg": '''<rect x="30" y="32" width="60" height="12" rx="2" fill="#450a0a" stroke="#ef5b55" stroke-width="2"/>
<rect x="30" y="64" width="60" height="12" rx="2" fill="#450a0a" stroke="#ef5b55" stroke-width="2"/>
<line x1="44" y1="44" x2="44" y2="64" stroke="#ffffff" stroke-width="3"/>
<line x1="76" y1="44" x2="76" y2="64" stroke="#ffffff" stroke-width="3"/>
<polygon points="60,46 66,54 54,54" fill="#f1df76"/>
<polygon points="60,62 66,54 54,54" fill="#f1df76"/>'''
        }
    }

    for k, data in work_methods.items():
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="{data['bg']}" stroke="{data['col']}" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="none" stroke="{data['col']}" stroke-width="1.2" stroke-dasharray="6 3"/>
  {data['svg']}
  <text x="60" y="98" fill="{data['col']}" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">{data['name']}</text>
  <text x="60" y="108" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="6" font-weight="bold" text-anchor="middle">{data['desc']}</text>
</svg>'''
        rich_icons[f"work_{k}.svg"] = svg
        rich_icons[f"icon_work_{k}.svg"] = svg

    # 4. WORK OUTCOME RESULTS (good_result.svg, normal_result.svg, bad_result.svg)
    rich_icons["good_result.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#021f14" stroke="#71efaf" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="26" fill="#064e3b" stroke="#71efaf" stroke-width="2"/>
  <polyline points="44,54 54,64 78,40" fill="none" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="60" y="104" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">GOOD // +FLUX</text>
</svg>'''

    rich_icons["normal_result.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="26" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
  <line x1="42" y1="54" x2="78" y2="54" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">NORMAL // MID</text>
</svg>'''

    rich_icons["bad_result.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1f0608" stroke="#ef5b55" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="26" fill="#450a0a" stroke="#ef5b55" stroke-width="2"/>
  <line x1="44" y1="38" x2="76" y2="70" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round"/>
  <line x1="76" y1="38" x2="44" y2="70" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">BAD // BREACH RISK</text>
</svg>'''

    # 5. MANIFESTATION & ORIGIN CATEGORIES
    rich_icons["man_subject.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#031526" stroke="#38bdf8" stroke-width="3.5"/>
  <circle cx="60" cy="44" r="14" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 36,80 C 36,62 84,62 84,80 Z" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">SUBJECT // TYPE</text>
</svg>'''
    rich_icons["subject.svg"] = rich_icons["man_subject.svg"]

    rich_icons["man_object.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="60,26 88,42 88,72 60,88 32,72 32,42" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
  <line x1="60" y1="26" x2="60" y2="88" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="32" y1="42" x2="88" y2="72" stroke="#ffffff" stroke-width="1.5"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">OBJECT // TYPE</text>
</svg>'''
    rich_icons["object_type.svg"] = rich_icons["man_object.svg"]

    rich_icons["man_place.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#130421" stroke="#c084fc" stroke-width="3.5"/>
  <polygon points="60,26 88,48 76,82 44,82 32,48" fill="#3b0764" stroke="#c084fc" stroke-width="2"/>
  <circle cx="60" cy="54" r="6" fill="#f1df76"/>
  <text x="60" y="104" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">PLACE // LOCUS</text>
</svg>'''
    rich_icons["place.svg"] = rich_icons["man_place.svg"]

    rich_icons["man_time.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="26" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
  <line x1="60" y1="36" x2="60" y2="54" stroke="#ffffff" stroke-width="3"/>
  <line x1="60" y1="54" x2="74" y2="54" stroke="#f1df76" stroke-width="2.5"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">TIME // TEMPORAL</text>
</svg>'''

    rich_icons["man_hazard.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1f0608" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="60,24 94,80 26,80" fill="#450a0a" stroke="#ef5b55" stroke-width="2.5"/>
  <line x1="60" y1="42" x2="60" y2="62" stroke="#f1df76" stroke-width="4" stroke-linecap="round"/>
  <circle cx="60" cy="72" r="3" fill="#f1df76"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">HAZARD // EVENT</text>
</svg>'''

    rich_icons["hybrid.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#090d16" stroke="#38bdf8" stroke-width="3.5"/>
  <circle cx="48" cy="54" r="18" fill="#ef5b55" opacity="0.6"/>
  <circle cx="72" cy="54" r="18" fill="#38bdf8" opacity="0.6"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">HYBRID // DUAL</text>
</svg>'''

    # 6. FACTIONS (fac_rd.svg, fac_council.svg, fac_keepers.svg, fac_architects.svg)
    rich_icons["fac_rd.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#04140d" stroke="#71efaf" stroke-width="3.5"/>
  <polygon points="60,22 88,40 80,80 60,92 40,80 32,40" fill="#064e3b" stroke="#71efaf" stroke-width="2"/>
  <circle cx="60" cy="52" r="12" fill="#f1df76"/>
  <text x="60" y="104" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">REVERIE DIRECTORATE</text>
</svg>'''

    rich_icons["fac_council.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="60,24 90,74 30,74" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
  <circle cx="60" cy="46" r="6" fill="#ffffff"/>
  <circle cx="48" cy="64" r="5" fill="#ffffff"/>
  <circle cx="72" cy="64" r="5" fill="#ffffff"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">CITY COUNCIL</text>
</svg>'''

    rich_icons["fac_keepers.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c0709" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="60,20 86,36 78,80 60,90 42,80 34,36" fill="#450a0a" stroke="#ef5b55" stroke-width="2"/>
  <line x1="32" y1="84" x2="88" y2="28" stroke="#ffffff" stroke-width="2.5"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">KEEPERS OF SORROW</text>
</svg>'''

    rich_icons["fac_architects.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#241903" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="56,20 64,20 86,84 76,84" fill="#f1df76"/>
  <polygon points="56,20 64,20 44,84 34,84" fill="#f1df76"/>
  <circle cx="60" cy="22" r="6" fill="#eab308"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">HIGH ARCHITECTS</text>
</svg>'''
    rich_icons["icon_faction_architects.svg"] = rich_icons["fac_architects.svg"]

    # 7. M.A.W. AND LORE EQUIPMENT ICONS (suit, tool, gift, fracture, taboo, resonance, han, etc.)
    rich_icons["suit.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#041b2c" stroke="#38bdf8" stroke-width="3.5"/>
  <path d="M 36,30 L 60,46 L 84,30 L 92,44 L 80,84 L 40,84 L 28,44 Z" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
  <line x1="60" y1="46" x2="60" y2="84" stroke="#f1df76" stroke-width="2"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">M.A.W. SUIT</text>
</svg>'''

    rich_icons["tool.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <line x1="34" y1="84" x2="78" y2="40" stroke="#94a3b8" stroke-width="4"/>
  <polygon points="74,28 92,46 82,56 64,38" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">M.A.W. WEAPON</text>
</svg>'''

    rich_icons["gift.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#130421" stroke="#c084fc" stroke-width="3.5"/>
  <polygon points="60,26 84,54 60,82 36,54" fill="#3b0764" stroke="#c084fc" stroke-width="2"/>
  <circle cx="60" cy="54" r="6" fill="#fef08a"/>
  <text x="60" y="104" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">M.A.W. GIFT</text>
</svg>'''

    rich_icons["fracture.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1f0608" stroke="#ef5b55" stroke-width="3.5"/>
  <path d="M 30,30 L 54,50 L 46,62 L 72,70 L 64,88" fill="none" stroke="#ef5b55" stroke-width="3.5"/>
  <circle cx="54" cy="50" r="4" fill="#f1df76"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">FRACTURE</text>
</svg>'''

    rich_icons["taboo.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1f0608" stroke="#ef5b55" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="24" fill="none" stroke="#ef5b55" stroke-width="3"/>
  <line x1="42" y1="36" x2="78" y2="72" stroke="#ef5b55" stroke-width="3"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">TABOO // BAN</text>
</svg>'''

    rich_icons["han.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#041b2c" stroke="#38bdf8" stroke-width="3.5"/>
  <path d="M 60,26 C 60,26 84,54 84,70 C 84,84 73,92 60,92 C 47,92 36,84 36,70 C 36,54 60,26 60,26 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="60" cy="74" r="6" fill="#ffffff"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">HAN FLUX (한)</text>
</svg>'''

    rich_icons["resonance.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="10" fill="#f1df76"/>
  <ellipse cx="60" cy="54" rx="20" ry="8" fill="none" stroke="#38bdf8" stroke-width="1.8"/>
  <ellipse cx="60" cy="54" rx="30" ry="14" fill="none" stroke="#71efaf" stroke-width="1.2" stroke-dasharray="4 2"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">RESONANCE</text>
</svg>'''

    # Write all icons to both directories
    for fname, code in rich_icons.items():
        with open(os.path.join(icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(code)
        with open(os.path.join(user_icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(code)

    print(f"Upgraded {len(rich_icons)} system, navigation, and work icons to rich detailed SVGs!")

if __name__ == "__main__":
    upgrade_systems_and_navigation_icons()
