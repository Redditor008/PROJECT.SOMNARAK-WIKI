import os

ICONS_DIR = "/home/user/01_Somnarak_Wiki/assets/icons"
os.makedirs(ICONS_DIR, exist_ok=True)

# 1. Faction Sigils (13 SVGs)
factions = {
    "icon_faction_reverie_directorate.svg": {
        "title": "REVERIE DIRECTORATE",
        "color1": "#f1df76", "color2": "#ef5b55", "bg": "#120b08",
        "symbol": '''<polygon points="50,12 85,32 85,72 50,92 15,72 15,32" fill="none" stroke="#f1df76" stroke-width="4"/>
        <circle cx="50" cy="52" r="22" fill="#ef5b55" fill-opacity="0.25" stroke="#ef5b55" stroke-width="3"/>
        <path d="M50,30 L50,74 M30,52 L70,52" stroke="#f1df76" stroke-width="3"/>
        <polygon points="50,38 62,52 50,66 38,52" fill="#f1df76"/>'''
    },
    "icon_faction_high_council.svg": {
        "title": "HIGH COUNCIL",
        "color1": "#f1df76", "color2": "#e2e8f0", "bg": "#0c0d14",
        "symbol": '''<circle cx="50" cy="50" r="38" fill="none" stroke="#f1df76" stroke-width="3" stroke-dasharray="6,4"/>
        <polygon points="50,20 78,74 22,74" fill="none" stroke="#e2e8f0" stroke-width="3.5"/>
        <circle cx="50" cy="50" r="14" fill="#f1df76" fill-opacity="0.3" stroke="#f1df76" stroke-width="2.5"/>
        <circle cx="50" cy="50" r="5" fill="#ffffff"/>'''
    },
    "icon_faction_sed_corps.svg": {
        "title": "SED CORPS",
        "color1": "#38bdf8", "color2": "#0284c7", "bg": "#06131f",
        "symbol": '''<polygon points="50,14 82,42 70,86 30,86 18,42" fill="none" stroke="#38bdf8" stroke-width="3.5"/>
        <path d="M50,24 L72,78 L28,78 Z" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="50" cy="56" r="12" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
        <path d="M50,36 L50,76 M35,56 L65,56" stroke="#ffffff" stroke-width="2.5"/>'''
    },
    "icon_faction_ucd_strike.svg": {
        "title": "UCD STRIKE FORCE",
        "color1": "#ef5b55", "color2": "#991b1b", "bg": "#1a0608",
        "symbol": '''<rect x="22" y="22" width="56" height="56" rx="6" fill="none" stroke="#ef5b55" stroke-width="3.5"/>
        <path d="M50,15 L50,85 M15,50 L85,50" stroke="#ef5b55" stroke-width="2.5" stroke-dasharray="4,4"/>
        <polygon points="50,30 68,50 50,70 32,50" fill="#991b1b" fill-opacity="0.5" stroke="#ffffff" stroke-width="2"/>
        <circle cx="50" cy="50" r="6" fill="#ef5b55"/>'''
    },
    "icon_faction_architects.svg": {
        "title": "THE ARCHITECTS",
        "color1": "#38bdf8", "color2": "#818cf8", "bg": "#090d1c",
        "symbol": '''<polygon points="50,16 84,36 84,76 50,96 16,76 16,36" fill="none" stroke="#38bdf8" stroke-width="3"/>
        <path d="M50,16 L50,96 M16,36 L84,76 M16,76 L84,36" stroke="#818cf8" stroke-width="2" stroke-opacity="0.7"/>
        <circle cx="50" cy="56" r="10" fill="#38bdf8"/>'''
    },
    "icon_faction_weavers.svg": {
        "title": "THE WEAVERS",
        "color1": "#c084fc", "color2": "#a855f7", "bg": "#14081c",
        "symbol": '''<circle cx="50" cy="50" r="36" fill="none" stroke="#c084fc" stroke-width="3"/>
        <path d="M25,25 Q50,75 75,25 Q50,75 25,75 Q50,25 75,75" fill="none" stroke="#a855f7" stroke-width="2.5"/>
        <circle cx="50" cy="50" r="8" fill="#f1df76" stroke="#ffffff" stroke-width="1.5"/>'''
    },
    "icon_faction_wardens.svg": {
        "title": "THE WARDENS",
        "color1": "#f59e0b", "color2": "#b45309", "bg": "#1c1206",
        "symbol": '''<path d="M50,14 L82,28 L82,60 Q50,90 50,90 Q18,60 18,60 L18,28 Z" fill="none" stroke="#f59e0b" stroke-width="3.5"/>
        <path d="M50,24 L72,35 L72,58 Q50,80 50,80 Q28,58 28,58 L28,35 Z" fill="#f59e0b" fill-opacity="0.2" stroke="#b45309" stroke-width="2"/>
        <rect x="42" y="44" width="16" height="20" rx="3" fill="#ffffff"/>
        <circle cx="50" cy="40" r="5" fill="none" stroke="#ffffff" stroke-width="3"/>'''
    },
    "icon_faction_collectors.svg": {
        "title": "THE COLLECTORS",
        "color1": "#10b981", "color2": "#047857", "bg": "#061811",
        "symbol": '''<rect x="20" y="26" width="60" height="52" rx="4" fill="none" stroke="#10b981" stroke-width="3"/>
        <path d="M34,26 L34,16 Q34,12 38,12 L62,12 Q66,12 66,16 L66,26" fill="none" stroke="#10b981" stroke-width="3"/>
        <circle cx="50" cy="52" r="14" fill="#047857" stroke="#f1df76" stroke-width="2"/>
        <path d="M46,52 L50,56 L56,48" stroke="#ffffff" stroke-width="2.5" fill="none"/>'''
    },
    "icon_faction_horizon_caravan.svg": {
        "title": "HORIZON CARAVAN",
        "color1": "#f97316", "color2": "#ea580c", "bg": "#1c0d05",
        "symbol": '''<path d="M15,75 Q50,25 85,75" fill="none" stroke="#f97316" stroke-width="4"/>
        <polygon points="50,20 62,45 38,45" fill="#f97316"/>
        <circle cx="50" cy="58" r="10" fill="#ea580c" stroke="#ffffff" stroke-width="2"/>
        <path d="M20,78 L80,78" stroke="#f1df76" stroke-width="3"/>'''
    },
    "icon_faction_memory_washers.svg": {
        "title": "MEMORY WASHERS",
        "color1": "#06b6d4", "color2": "#0891b2", "bg": "#05161c",
        "symbol": '''<circle cx="50" cy="50" r="36" fill="none" stroke="#06b6d4" stroke-width="3" stroke-dasharray="10,5"/>
        <path d="M30,50 Q50,25 70,50 Q50,75 30,50" fill="#0891b2" fill-opacity="0.3" stroke="#06b6d4" stroke-width="2.5"/>
        <circle cx="50" cy="50" r="8" fill="#ffffff"/>
        <path d="M50,18 L50,30 M50,70 L50,82 M18,50 L30,50 M70,50 L82,50" stroke="#06b6d4" stroke-width="2.5"/>'''
    },
    "icon_faction_giltong_enforcers.svg": {
        "title": "GILTONG ENFORCERS",
        "color1": "#e11d48", "color2": "#9f1239", "bg": "#1a060d",
        "symbol": '''<polygon points="50,15 85,50 50,85 15,50" fill="none" stroke="#e11d48" stroke-width="3.5"/>
        <polygon points="50,28 72,50 50,72 28,50" fill="#9f1239" fill-opacity="0.4" stroke="#ffffff" stroke-width="2"/>
        <line x1="32" y1="32" x2="68" y2="68" stroke="#f1df76" stroke-width="3"/>
        <line x1="68" y1="32" x2="32" y2="68" stroke="#f1df76" stroke-width="3"/>'''
    },
    "icon_faction_founding_corps.svg": {
        "title": "FOUNDING CORPS",
        "color1": "#94a3b8", "color2": "#64748b", "bg": "#0d1117",
        "symbol": '''<rect x="18" y="18" width="64" height="64" rx="2" fill="none" stroke="#94a3b8" stroke-width="3"/>
        <rect x="28" y="28" width="44" height="44" fill="#64748b" fill-opacity="0.2" stroke="#94a3b8" stroke-width="2"/>
        <path d="M18,50 L82,50 M50,18 L50,82" stroke="#f1df76" stroke-width="2"/>
        <circle cx="50" cy="50" r="7" fill="#f1df76"/>'''
    },
    "icon_faction_underworld.svg": {
        "title": "UNDERWORLD & WOUND WALKERS",
        "color1": "#a855f7", "color2": "#6b21a8", "bg": "#11061a",
        "symbol": '''<path d="M20,25 L50,80 L80,25 Z" fill="none" stroke="#a855f7" stroke-width="3.5"/>
        <path d="M30,32 L50,70 L70,32 Z" fill="#6b21a8" fill-opacity="0.4" stroke="#f1df76" stroke-width="2"/>
        <circle cx="50" cy="45" r="9" fill="#ef5b55"/>
        <path d="M50,16 L50,30" stroke="#a855f7" stroke-width="3"/>'''
    }
}

for fname, data in factions.items():
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="bg_{fname[:8]}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{data['color1']}" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="{data['bg']}" stop-opacity="0.95"/>
    </radialGradient>
    <filter id="glow_{fname[:8]}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="100" height="100" rx="8" fill="url(#bg_{fname[:8]})" stroke="{data['color1']}" stroke-width="2"/>
  <g filter="url(#glow_{fname[:8]})">
    {data['symbol']}
  </g>
</svg>'''
    path = os.path.join(ICONS_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content)

print(f"Generated {len(factions)} Faction SVGs.")

# 2. Echo-Core Character Badges (9 SVGs)
echo_cores = {
    "icon_core_majin.svg": {"name": "MAJIN", "title": "THE DIRECTOR", "color": "#ef5b55", "bg": "#18080a", "glyph": "M", "sym": '<polygon points="50,14 84,34 84,74 50,94 16,74 16,34" fill="none" stroke="#ef5b55" stroke-width="3"/><circle cx="50" cy="54" r="20" fill="#ef5b55" fill-opacity="0.3" stroke="#f1df76" stroke-width="2"/><path d="M40,64 L40,44 L50,54 L60,44 L60,64" fill="none" stroke="#ffffff" stroke-width="3.5" stroke-linecap="round"/>'},
    "icon_core_seiyon.svg": {"name": "SEIYON", "title": "THE SECRETARY", "color": "#5b75e8", "bg": "#080e1c", "glyph": "S", "sym": '<circle cx="50" cy="50" r="36" fill="none" stroke="#5b75e8" stroke-width="3"/><rect x="30" y="30" width="40" height="40" rx="4" fill="#5b75e8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="2"/><path d="M60,40 Q40,36 42,48 Q44,60 58,60" fill="none" stroke="#ffffff" stroke-width="3.5" stroke-linecap="round"/>'},
    "icon_core_dekan.svg": {"name": "DEKAN", "title": "CONTAINMENT LEAD", "color": "#38bdf8", "bg": "#06131c", "glyph": "D", "sym": '<rect x="20" y="20" width="60" height="60" rx="6" fill="none" stroke="#38bdf8" stroke-width="3.5"/><polygon points="50,28 72,50 50,72 28,50" fill="#38bdf8" fill-opacity="0.3" stroke="#ffffff" stroke-width="2"/><path d="M42,38 L42,62 L52,62 Q60,62 60,50 Q60,38 52,38 Z" fill="none" stroke="#ffffff" stroke-width="3.5"/>'},
    "icon_core_zyrak.svg": {"name": "ZYRAK", "title": "EXTRACTION LEAD", "color": "#e6c843", "bg": "#181406", "glyph": "Z", "sym": '<polygon points="50,15 82,78 18,78" fill="none" stroke="#e6c843" stroke-width="3.5"/><circle cx="50" cy="56" r="16" fill="#e6c843" fill-opacity="0.3" stroke="#f1df76" stroke-width="2"/><path d="M40,44 L60,44 L40,64 L60,64" fill="none" stroke="#ffffff" stroke-width="3.5" stroke-linecap="round"/>'},
    "icon_core_ayshuk.svg": {"name": "AYSHUK", "title": "RESEARCH LEAD", "color": "#47c978", "bg": "#06180e", "glyph": "A", "sym": '<polygon points="50,16 84,36 84,76 50,96 16,76 16,36" fill="none" stroke="#47c978" stroke-width="3"/><path d="M50,26 L68,68 L32,68 Z" fill="#47c978" fill-opacity="0.3" stroke="#ffffff" stroke-width="2"/><line x1="38" y1="56" x2="62" y2="56" stroke="#ffffff" stroke-width="3"/>'},
    "icon_core_mellda.svg": {"name": "MELLDA", "title": "BORDER LEAD", "color": "#d4d4d8", "bg": "#121418", "glyph": "M", "sym": '<path d="M50,15 L80,30 L80,62 Q50,88 50,88 Q20,62 20,62 L20,30 Z" fill="none" stroke="#d4d4d8" stroke-width="3.5"/><circle cx="50" cy="50" r="15" fill="#d4d4d8" fill-opacity="0.25" stroke="#f1df76" stroke-width="2"/><path d="M40,60 L40,42 L50,52 L60,42 L60,60" fill="none" stroke="#ffffff" stroke-width="3"/>'},
    "icon_core_marjuk.svg": {"name": "MARJUK", "title": "ARCHIVE LEAD", "color": "#be123c", "bg": "#18060c", "glyph": "M", "sym": '<rect x="22" y="18" width="56" height="64" rx="4" fill="none" stroke="#be123c" stroke-width="3.5"/><line x1="32" y1="34" x2="68" y2="34" stroke="#f1df76" stroke-width="3"/><line x1="32" y1="48" x2="68" y2="48" stroke="#ffffff" stroke-width="2.5"/><line x1="32" y1="62" x2="56" y2="62" stroke="#ffffff" stroke-width="2.5"/>'},
    "icon_core_ishall.svg": {"name": "ISHALL", "title": "OUTSIDER / VOID", "color": "#f43f5e", "bg": "#18060f", "glyph": "I", "sym": '<polygon points="50,12 88,50 50,88 12,50" fill="none" stroke="#f43f5e" stroke-width="3.5"/><circle cx="50" cy="50" r="18" fill="#f43f5e" fill-opacity="0.3" stroke="#ffffff" stroke-width="2"/><line x1="50" y1="36" x2="50" y2="64" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/><line x1="42" y1="36" x2="58" y2="36" stroke="#ffffff" stroke-width="3.5"/><line x1="42" y1="64" x2="58" y2="64" stroke="#ffffff" stroke-width="3.5"/>'},
    "icon_core_xyan.svg": {"name": "XYAN", "title": "THE EXILE / GATE", "color": "#fbbf24", "bg": "#1a1205", "glyph": "X", "sym": '<circle cx="50" cy="50" r="38" fill="none" stroke="#fbbf24" stroke-width="3.5" stroke-dasharray="8,4"/><polygon points="34,34 66,66 M66,34 34,66" stroke="#fbbf24" stroke-width="4.5" stroke-linecap="round"/><circle cx="50" cy="50" r="7" fill="#ef5b55"/>'}
}

for fname, data in echo_cores.items():
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="bg_{fname[:8]}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{data['color']}" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="{data['bg']}" stop-opacity="0.95"/>
    </radialGradient>
    <filter id="glow_{fname[:8]}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="100" height="100" rx="8" fill="url(#bg_{fname[:8]})" stroke="{data['color']}" stroke-width="2.5"/>
  <g filter="url(#glow_{fname[:8]})">
    {data['sym']}
  </g>
</svg>'''
    path = os.path.join(ICONS_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content)

print(f"Generated {len(echo_cores)} Echo-Core SVGs.")

# 3. Damage Type & Work Type Badges (8 SVGs)
combat_svgs = {
    "icon_damage_physical_red.svg": {
        "color": "#ef4444", "bg": "#1c0606",
        "sym": '<polygon points="50,14 84,50 50,86 16,50" fill="#ef4444" fill-opacity="0.3" stroke="#ef4444" stroke-width="3.5"/><path d="M38,36 L62,64 M62,36 L38,64" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/><text x="50" y="96" fill="#ef4444" font-family="Impact" font-size="10" text-anchor="middle">PHYSICAL</text>'
    },
    "icon_damage_mental_white.svg": {
        "color": "#38bdf8", "bg": "#06131c",
        "sym": '<circle cx="50" cy="50" r="34" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="3.5"/><circle cx="50" cy="50" r="16" fill="none" stroke="#ffffff" stroke-width="3" stroke-dasharray="4,4"/><circle cx="50" cy="50" r="6" fill="#ffffff"/><text x="50" y="96" fill="#38bdf8" font-family="Impact" font-size="10" text-anchor="middle">MENTAL</text>'
    },
    "icon_damage_corrosive_black.svg": {
        "color": "#a855f7", "bg": "#14061a",
        "sym": '<polygon points="50,16 84,76 16,76" fill="#a855f7" fill-opacity="0.3" stroke="#a855f7" stroke-width="3.5"/><circle cx="50" cy="56" r="14" fill="#14061a" stroke="#f1df76" stroke-width="2.5"/><path d="M46,46 L54,66 M54,46 L46,66" stroke="#ffffff" stroke-width="2.5"/><text x="50" y="96" fill="#a855f7" font-family="Impact" font-size="10" text-anchor="middle">CORROSIVE</text>'
    },
    "icon_damage_pale_cyan.svg": {
        "color": "#f1df76", "bg": "#161405",
        "sym": '<circle cx="50" cy="50" r="34" fill="#f1df76" fill-opacity="0.25" stroke="#f1df76" stroke-width="3.5"/><polygon points="50,22 62,50 50,78 38,50" fill="#ffffff" stroke="#f1df76" stroke-width="2"/><circle cx="50" cy="50" r="4" fill="#ef5b55"/><text x="50" y="96" fill="#f1df76" font-family="Impact" font-size="10" text-anchor="middle">PALE</text>'
    },
    "icon_work_instinct_red.svg": {
        "color": "#ef4444", "bg": "#1a0606",
        "sym": '<circle cx="50" cy="50" r="34" fill="none" stroke="#ef4444" stroke-width="3.5"/><path d="M35,65 Q50,25 65,65" fill="#ef4444" fill-opacity="0.4" stroke="#ffffff" stroke-width="3"/><circle cx="50" cy="42" r="6" fill="#f1df76"/>'
    },
    "icon_work_insight_white.svg": {
        "color": "#38bdf8", "bg": "#06131c",
        "sym": '<rect x="22" y="22" width="56" height="56" rx="4" fill="none" stroke="#38bdf8" stroke-width="3.5"/><circle cx="50" cy="50" r="16" fill="#38bdf8" fill-opacity="0.3" stroke="#ffffff" stroke-width="2.5"/><path d="M50,30 L50,70 M30,50 L70,50" stroke="#f1df76" stroke-width="2.5"/>'
    },
    "icon_work_attachment_black.svg": {
        "color": "#a855f7", "bg": "#14061a",
        "sym": '<polygon points="50,15 82,75 18,75" fill="none" stroke="#a855f7" stroke-width="3.5"/><path d="M40,55 Q50,40 60,55 Q50,70 40,55 Z" fill="#a855f7" fill-opacity="0.5" stroke="#ffffff" stroke-width="2"/>'
    },
    "icon_work_repression_cyan.svg": {
        "color": "#f1df76", "bg": "#161405",
        "sym": '<polygon points="50,14 84,34 84,74 50,94 16,74 16,34" fill="none" stroke="#f1df76" stroke-width="3.5"/><rect x="36" y="36" width="28" height="28" fill="#ef5b55" stroke="#ffffff" stroke-width="2.5"/><line x1="30" y1="50" x2="70" y2="50" stroke="#ffffff" stroke-width="3"/>'
    }
}

for fname, data in combat_svgs.items():
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="bg_{fname[:8]}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{data['color']}" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="{data['bg']}" stop-opacity="0.95"/>
    </radialGradient>
  </defs>
  <rect width="100" height="100" rx="8" fill="url(#bg_{fname[:8]})" stroke="{data['color']}" stroke-width="2"/>
  <g>{data['sym']}</g>
</svg>'''
    path = os.path.join(ICONS_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content)

print(f"Generated {len(combat_svgs)} Combat/Work SVGs.")

# 4. SECC Risk Tier Badges (5 SVGs)
risk_tiers = {
    "icon_risk_t01_can.svg": {"tier": "T-01 CAN", "color": "#10b981", "bg": "#061811", "sym": '<polygon points="50,15 85,50 50,85 15,50" fill="#10b981" fill-opacity="0.25" stroke="#10b981" stroke-width="3"/><text x="50" y="56" fill="#10b981" font-family="Impact" font-size="16" font-weight="bold" text-anchor="middle">CAN</text>'},
    "icon_risk_t02_teth.svg": {"tier": "T-02 TETH", "color": "#38bdf8", "bg": "#06131f", "sym": '<rect x="20" y="20" width="60" height="60" rx="4" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="3"/><text x="50" y="56" fill="#38bdf8" font-family="Impact" font-size="16" font-weight="bold" text-anchor="middle">TETH</text>'},
    "icon_risk_t03_he.svg": {"tier": "T-03 HE", "color": "#f1df76", "bg": "#181506", "sym": '<polygon points="50,14 84,34 84,74 50,94 16,74 16,34" fill="#f1df76" fill-opacity="0.25" stroke="#f1df76" stroke-width="3"/><text x="50" y="57" fill="#f1df76" font-family="Impact" font-size="18" font-weight="bold" text-anchor="middle">HE</text>'},
    "icon_risk_t04_waw.svg": {"tier": "T-04 WAW", "color": "#a855f7", "bg": "#14061a", "sym": '<polygon points="50,12 88,50 50,88 12,50" fill="#a855f7" fill-opacity="0.3" stroke="#a855f7" stroke-width="3.5"/><text x="50" y="57" fill="#a855f7" font-family="Impact" font-size="16" font-weight="bold" text-anchor="middle">WAW</text>'},
    "icon_risk_t05_aleph.svg": {"tier": "T-05 ALEPH", "color": "#ef4444", "bg": "#1a0606", "sym": '<polygon points="50,10 88,78 12,78" fill="#ef4444" fill-opacity="0.35" stroke="#ef4444" stroke-width="4"/><text x="50" y="62" fill="#ffffff" font-family="Impact" font-size="16" font-weight="bold" text-anchor="middle">ALEPH</text>'}
}

for fname, data in risk_tiers.items():
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="bg_{fname[:8]}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{data['color']}" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="{data['bg']}" stop-opacity="0.95"/>
    </radialGradient>
  </defs>
  <rect width="100" height="100" rx="8" fill="url(#bg_{fname[:8]})" stroke="{data['color']}" stroke-width="2"/>
  <g>{data['sym']}</g>
</svg>'''
    path = os.path.join(ICONS_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content)

print(f"Generated {len(risk_tiers)} Risk Tier SVGs.")

# 5. Tactical HUD Schematics & Visualizers (4 SVGs)
huds = {
    "hud_resonance_wave.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 80" width="400" height="80">
  <rect width="400" height="80" fill="#04070d" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
  <line x1="0" y1="40" x2="400" y2="40" stroke="#1e293b" stroke-width="1"/>
  <path d="M0,40 Q25,10 50,40 T100,40 T150,15 T200,65 T250,20 T300,55 T350,30 T400,40" fill="none" stroke="#38bdf8" stroke-width="2.5" opacity="0.9"/>
  <path d="M0,40 Q35,60 70,40 T140,40 T210,65 T280,15 T350,50 T400,40" fill="none" stroke="#ef5b55" stroke-width="1.8" opacity="0.75"/>
  <circle cx="150" cy="15" r="4" fill="#f1df76"/>
  <circle cx="280" cy="15" r="4" fill="#f1df76"/>
  <text x="12" y="20" fill="#38bdf8" font-family="monospace" font-size="10" font-weight="bold">[RESONANCE FLUX: 94.2% STABLE]</text>
  <text x="310" y="20" fill="#ef5b55" font-family="monospace" font-size="10" font-weight="bold">CODE: AMBER</text>
</svg>''',
    "hud_facility_radar.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <circle cx="50" cy="50" r="45" fill="#050a14" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="50" cy="50" r="30" fill="none" stroke="#1e293b" stroke-width="1.5" stroke-dasharray="4,3"/>
  <circle cx="50" cy="50" r="15" fill="none" stroke="#1e293b" stroke-width="1.5"/>
  <line x1="50" y1="5" x2="50" y2="95" stroke="#38bdf8" stroke-width="1" stroke-opacity="0.6"/>
  <line x1="5" y1="50" x2="95" y2="50" stroke="#38bdf8" stroke-width="1" stroke-opacity="0.6"/>
  <path d="M50,50 L80,20 A45,45 0 0,0 50,5 Z" fill="#38bdf8" fill-opacity="0.3"/>
  <circle cx="68" cy="32" r="3" fill="#ef5b55"/>
  <circle cx="35" cy="65" r="3" fill="#f1df76"/>
</svg>''',
    "hud_han_gauge.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <circle cx="60" cy="60" r="50" fill="#090d18" stroke="#ef5b55" stroke-width="3"/>
  <path d="M25,85 A42,42 0 1,1 95,85" fill="none" stroke="#1e293b" stroke-width="8" stroke-linecap="round"/>
  <path d="M25,85 A42,42 0 1,1 82,32" fill="none" stroke="#f1df76" stroke-width="8" stroke-linecap="round"/>
  <text x="60" y="65" fill="#ffffff" font-family="Impact" font-size="20" text-anchor="middle">84%</text>
  <text x="60" y="80" fill="#ef5b55" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">HAN FLUX</text>
</svg>''',
    "hud_containment_lock.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <polygon points="50,10 88,32 88,68 50,90 12,68 12,32" fill="#090d18" stroke="#f1df76" stroke-width="3"/>
  <rect x="34" y="44" width="32" height="28" rx="4" fill="#ef5b55" stroke="#ffffff" stroke-width="2"/>
  <path d="M40,44 L40,34 Q40,24 50,24 Q60,24 60,34 L60,44" fill="none" stroke="#ffffff" stroke-width="4"/>
  <circle cx="50" cy="56" r="3.5" fill="#ffffff"/>
</svg>'''
}

for fname, svg_content in huds.items():
    path = os.path.join(ICONS_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content)

print(f"Generated {len(huds)} HUD Schematics.")
