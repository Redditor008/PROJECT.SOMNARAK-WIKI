import os

ICONS_DIR = "/home/user/01_Somnarak_Wiki/assets/icons"
BANNERS_DIR = "/home/user/01_Somnarak_Wiki/assets/banners"
AVATARS_DIR = "/home/user/01_Somnarak_Wiki/assets/avatars"
BG_DIR = "/home/user/01_Somnarak_Wiki/assets/backgrounds"

os.makedirs(ICONS_DIR, exist_ok=True)
os.makedirs(BANNERS_DIR, exist_ok=True)
os.makedirs(AVATARS_DIR, exist_ok=True)
os.makedirs(BG_DIR, exist_ok=True)

print("Creating Master Multi-Scale SVG Suite...")

# 1. WIDE HERO BANNERS (1200x300)
banners = {
    "banner_hero_somnarak_city.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300">
  <defs>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#020408"/>
      <stop offset="60%" stop-color="#0a101d"/>
      <stop offset="100%" stop-color="#14080c"/>
    </linearGradient>
    <linearGradient id="treeGrad" x1="50%" y1="0%" x2="50%" y2="100%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#ef5b55" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.2"/>
    </linearGradient>
    <radialGradient id="veilShield" cx="50%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.25"/>
      <stop offset="60%" stop-color="#38bdf8" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <!-- Background -->
  <rect width="1200" height="300" fill="url(#skyGrad)"/>
  <circle cx="600" cy="100" r="450" fill="url(#veilShield)"/>
  
  <!-- Subtle Grid Lines -->
  <g stroke="#1e293b" stroke-width="0.75" opacity="0.4">
    <line x1="0" y1="50" x2="1200" y2="50"/>
    <line x1="0" y1="100" x2="1200" y2="100"/>
    <line x1="0" y1="150" x2="1200" y2="150"/>
    <line x1="0" y1="200" x2="1200" y2="200"/>
    <line x1="0" y1="250" x2="1200" y2="250"/>
    <line x1="200" y1="0" x2="200" y2="300"/>
    <line x1="400" y1="0" x2="400" y2="300"/>
    <line x1="600" y1="0" x2="600" y2="300"/>
    <line x1="800" y1="0" x2="800" y2="300"/>
    <line x1="1000" y1="0" x2="1000" y2="300"/>
  </g>

  <!-- City Skyline Silhouette Background -->
  <path d="M0,280 L50,280 L50,220 L90,220 L90,250 L140,250 L140,190 L180,190 L180,270 L240,270 L240,170 L270,170 L270,280 L340,280 L340,150 L380,150 L380,280 L460,280 L460,180 L510,180 L510,280 L690,280 L690,180 L740,180 L740,280 L820,280 L820,150 L860,150 L860,280 L930,280 L930,170 L960,170 L960,270 L1020,270 L1020,190 L1060,190 L1060,250 L1110,250 L1110,220 L1150,220 L1150,280 L1200,280 L1200,300 L0,300 Z" fill="#070c14"/>

  <!-- Alpha Tree Center Glow -->
  <g filter="url(#glow)">
    <!-- Central Trunk -->
    <path d="M590,300 Q600,180 600,80 Q600,180 610,300 Z" fill="url(#treeGrad)"/>
    <!-- Branches -->
    <path d="M600,140 Q550,110 500,120 Q560,90 600,110" fill="none" stroke="#f1df76" stroke-width="3.5" opacity="0.85"/>
    <path d="M600,140 Q650,110 700,120 Q640,90 600,110" fill="none" stroke="#f1df76" stroke-width="3.5" opacity="0.85"/>
    <path d="M600,100 Q530,60 460,80 Q540,40 600,70" fill="none" stroke="#ef5b55" stroke-width="3" opacity="0.8"/>
    <path d="M600,100 Q670,60 740,80 Q660,40 600,70" fill="none" stroke="#ef5b55" stroke-width="3" opacity="0.8"/>
    <!-- Crown Nexus -->
    <circle cx="600" cy="70" r="28" fill="#f1df76" fill-opacity="0.3" stroke="#f1df76" stroke-width="2"/>
    <circle cx="600" cy="70" r="12" fill="#ffffff"/>
  </g>

  <!-- Foreground Directorate Spire Tower -->
  <polygon points="600,20 618,160 582,160" fill="#0d1829" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="600" y1="0" x2="600" y2="30" stroke="#ef5b55" stroke-width="3"/>
  <circle cx="600" cy="5" r="4" fill="#ef5b55"/>

  <!-- Lower Weeping River Flow -->
  <rect x="0" y="280" width="1200" height="20" fill="#050d1a"/>
  <path d="M0,290 Q300,282 600,290 T1200,290" fill="none" stroke="#38bdf8" stroke-width="3" opacity="0.8"/>
  <path d="M0,294 Q300,286 600,294 T1200,294" fill="none" stroke="#ef5b55" stroke-width="1.5" opacity="0.6"/>

  <!-- Tactical Header Overlay -->
  <text x="30" y="45" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="3">SOMNARAK // METROPOLITAN ATLAS</text>
  <text x="30" y="70" fill="#38bdf8" font-family="monospace" font-size="12" font-weight="bold">[ AXIOM: PRESERVE THE NAME // VEIL STABILITY: 99.4% ]</text>
  <text x="1170" y="45" fill="#ef5b55" font-family="monospace" font-size="14" font-weight="bold" text-anchor="end">YEAR 4,238 // 1,778 CYCLES</text>
  <text x="1170" y="68" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="end">REVERIE DIRECTORATE JURISDICTION</text>
</svg>''',

    "banner_hero_hand_of_change.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300">
  <defs>
    <linearGradient id="facGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#140608"/>
      <stop offset="50%" stop-color="#091220"/>
      <stop offset="100%" stop-color="#140608"/>
    </linearGradient>
    <pattern id="hatch" width="20" height="20" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="20" stroke="#ef5b55" stroke-width="1.5" opacity="0.15"/>
    </pattern>
  </defs>
  <rect width="1200" height="300" fill="url(#facGrad)"/>
  <rect width="1200" height="300" fill="url(#hatch)"/>
  
  <!-- Facility 8 Floor Level Lines -->
  <g stroke="#38bdf8" stroke-width="1.5" opacity="0.6">
    <line x1="80" y1="60" x2="1120" y2="60"/>
    <line x1="80" y1="90" x2="1120" y2="90"/>
    <line x1="80" y1="120" x2="1120" y2="120"/>
    <line x1="80" y1="150" x2="1120" y2="150"/>
    <line x1="80" y1="180" x2="1120" y2="180"/>
    <line x1="80" y1="210" x2="1120" y2="210"/>
    <line x1="80" y1="240" x2="1120" y2="240"/>
    <line x1="80" y1="270" x2="1120" y2="270"/>
  </g>

  <!-- Central Elevator Shaft -->
  <rect x="570" y="30" width="60" height="255" fill="#05080e" stroke="#f1df76" stroke-width="2"/>
  <line x1="600" y1="30" x2="600" y2="285" stroke="#ef5b55" stroke-width="2" stroke-dasharray="6,4"/>

  <!-- Left/Right Floor Tags -->
  <text x="90" y="55" fill="#ef5b55" font-family="monospace" font-size="11" font-weight="bold">[F1: NEUTRAL COMMAND]</text>
  <text x="90" y="85" fill="#5b75e8" font-family="monospace" font-size="11" font-weight="bold">[F2: MAW'S KEEP]</text>
  <text x="90" y="115" fill="#e6c843" font-family="monospace" font-size="11" font-weight="bold">[F3: EXTRACTION HALL]</text>
  <text x="90" y="145" fill="#47c978" font-family="monospace" font-size="11" font-weight="bold">[F4: INSIGHT FORGE]</text>
  <text x="1110" y="175" fill="#d4d4d8" font-family="monospace" font-size="11" font-weight="bold" text-anchor="end">[F5: BORDER WATCH]</text>
  <text x="1110" y="205" fill="#be123c" font-family="monospace" font-size="11" font-weight="bold" text-anchor="end">[F6: DEEP VAULT]</text>
  <text x="1110" y="235" fill="#f43f5e" font-family="monospace" font-size="11" font-weight="bold" text-anchor="end">[F7: SHADOW CORPS]</text>
  <text x="1110" y="265" fill="#fbbf24" font-family="monospace" font-size="11" font-weight="bold" text-anchor="end">[F8: GATE WATCH]</text>

  <!-- Main Banner Header -->
  <text x="600" y="45" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="4" text-anchor="middle">FACILITY 01 // THE HAND OF CHANGE</text>
  <text x="600" y="295" fill="#38bdf8" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">[ SUBTERRANEAN CONTAINMENT COMPLEX // 8 OPERATIONAL SECTORS ]</text>
</svg>'''
}

for bname, bcontent in banners.items():
    with open(os.path.join(BANNERS_DIR, bname), "w", encoding="utf-8") as f:
        f.write(bcontent)

print(f"Generated {len(banners)} Wide Hero Banners.")

# 2. CIRCULAR & STYLIZED ECHO-CORE AVATARS (160x160 SVGs)
avatars = {
    "avatar_core_majin.svg": {
        "name": "DIRECTOR MAJIN", "color": "#ef5b55", "sub": "THE DIRECTOR", "bg": "#180608",
        "art": '''<circle cx="80" cy="80" r="72" fill="#180608" stroke="#ef5b55" stroke-width="4"/>
        <circle cx="80" cy="80" r="62" fill="none" stroke="#f1df76" stroke-width="2" stroke-dasharray="6,4"/>
        <polygon points="80,24 130,52 130,108 80,136 30,108 30,52" fill="#ef5b55" fill-opacity="0.25" stroke="#ef5b55" stroke-width="3"/>
        <circle cx="80" cy="80" r="28" fill="#0a0506" stroke="#f1df76" stroke-width="3"/>
        <path d="M64,96 L64,64 L80,80 L96,64 L96,96" fill="none" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round"/>
        <polygon points="80,32 88,44 72,44" fill="#f1df76"/>'''
    },
    "avatar_core_seiyon.svg": {
        "name": "SECRETARY SEIYON", "color": "#5b75e8", "sub": "THE SECRETARY", "bg": "#080c1c",
        "art": '''<circle cx="80" cy="80" r="72" fill="#080c1c" stroke="#5b75e8" stroke-width="4"/>
        <circle cx="80" cy="80" r="62" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,4"/>
        <rect x="42" y="42" width="76" height="76" rx="8" fill="#5b75e8" fill-opacity="0.25" stroke="#5b75e8" stroke-width="3"/>
        <circle cx="80" cy="80" r="28" fill="#060914" stroke="#38bdf8" stroke-width="3"/>
        <path d="M96,64 Q64,58 68,78 Q72,98 94,98" fill="none" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round"/>
        <circle cx="80" cy="80" r="6" fill="#f1df76"/>'''
    },
    "avatar_core_dekan.svg": {
        "name": "LEAD DEKAN", "color": "#38bdf8", "sub": "CONTAINMENT LEAD", "bg": "#06131f",
        "art": '''<circle cx="80" cy="80" r="72" fill="#06131f" stroke="#38bdf8" stroke-width="4"/>
        <circle cx="80" cy="80" r="62" fill="none" stroke="#ffffff" stroke-width="2" stroke-dasharray="8,4"/>
        <polygon points="80,30 126,56 126,104 80,130 34,104 34,56" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="3"/>
        <rect x="55" y="55" width="50" height="50" rx="6" fill="#081826" stroke="#ffffff" stroke-width="3"/>
        <path d="M68,64 L68,96 L82,96 Q92,96 92,80 Q92,64 82,64 Z" fill="none" stroke="#38bdf8" stroke-width="4.5"/>'''
    },
    "avatar_core_zyrak.svg": {
        "name": "LEAD ZYRAK", "color": "#e6c843", "sub": "EXTRACTION LEAD", "bg": "#1c1806",
        "art": '''<circle cx="80" cy="80" r="72" fill="#1c1806" stroke="#e6c843" stroke-width="4"/>
        <polygon points="80,24 132,120 28,120" fill="#e6c843" fill-opacity="0.25" stroke="#e6c843" stroke-width="3.5"/>
        <circle cx="80" cy="88" r="26" fill="#0e0c03" stroke="#f1df76" stroke-width="3"/>
        <path d="M66,74 L94,74 L66,102 L94,102" fill="none" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round"/>'''
    },
    "avatar_core_ayshuk.svg": {
        "name": "LEAD AYSHUK", "color": "#47c978", "sub": "RESEARCH LEAD", "bg": "#06180e",
        "art": '''<circle cx="80" cy="80" r="72" fill="#06180e" stroke="#47c978" stroke-width="4"/>
        <polygon points="80,24 130,52 130,108 80,136 30,108 30,52" fill="#47c978" fill-opacity="0.25" stroke="#47c978" stroke-width="3"/>
        <circle cx="80" cy="80" r="28" fill="#040e08" stroke="#f1df76" stroke-width="3"/>
        <path d="M80,48 L104,108 L56,108 Z" fill="none" stroke="#ffffff" stroke-width="3"/>
        <line x1="66" y1="90" x2="94" y2="90" stroke="#47c978" stroke-width="4"/>'''
    },
    "avatar_core_mellda.svg": {
        "name": "LEAD MELLDA", "color": "#d4d4d8", "sub": "BORDER LEAD", "bg": "#121418",
        "art": '''<circle cx="80" cy="80" r="72" fill="#121418" stroke="#d4d4d8" stroke-width="4"/>
        <path d="M80,24 L128,48 L128,98 Q80,138 80,138 Q32,98 32,98 L32,48 Z" fill="#d4d4d8" fill-opacity="0.25" stroke="#d4d4d8" stroke-width="3.5"/>
        <circle cx="80" cy="80" r="26" fill="#0a0b0d" stroke="#f1df76" stroke-width="3"/>
        <path d="M65,96 L65,66 L80,80 L95,66 L95,96" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>'''
    },
    "avatar_core_marjuk.svg": {
        "name": "LEAD MARJUK", "color": "#be123c", "sub": "ARCHIVE LEAD", "bg": "#18060c",
        "art": '''<circle cx="80" cy="80" r="72" fill="#18060c" stroke="#be123c" stroke-width="4"/>
        <rect x="42" y="36" width="76" height="88" rx="6" fill="#be123c" fill-opacity="0.25" stroke="#be123c" stroke-width="3.5"/>
        <circle cx="80" cy="80" r="24" fill="#0d0306" stroke="#f1df76" stroke-width="2.5"/>
        <line x1="56" y1="62" x2="104" y2="62" stroke="#ffffff" stroke-width="4"/>
        <line x1="56" y1="80" x2="104" y2="80" stroke="#f1df76" stroke-width="3.5"/>
        <line x1="56" y1="98" x2="88" y2="98" stroke="#ffffff" stroke-width="3.5"/>'''
    },
    "avatar_core_ishall.svg": {
        "name": "LEAD ISHALL", "color": "#f43f5e", "sub": "THE OUTSIDER", "bg": "#180610",
        "art": '''<circle cx="80" cy="80" r="72" fill="#180610" stroke="#f43f5e" stroke-width="4"/>
        <polygon points="80,20 138,80 80,140 22,80" fill="#f43f5e" fill-opacity="0.25" stroke="#f43f5e" stroke-width="3.5"/>
        <circle cx="80" cy="80" r="26" fill="#0d0309" stroke="#ffffff" stroke-width="3"/>
        <line x1="80" y1="58" x2="80" y2="102" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
        <line x1="68" y1="58" x2="92" y2="58" stroke="#f1df76" stroke-width="4"/>
        <line x1="68" y1="102" x2="92" y2="102" stroke="#f1df76" stroke-width="4"/>'''
    },
    "avatar_core_xyan.svg": {
        "name": "LEAD XYAN", "color": "#fbbf24", "sub": "THE EXILE", "bg": "#1a1205",
        "art": '''<circle cx="80" cy="80" r="72" fill="#1a1205" stroke="#fbbf24" stroke-width="4"/>
        <circle cx="80" cy="80" r="60" fill="none" stroke="#fbbf24" stroke-width="3" stroke-dasharray="10,5"/>
        <circle cx="80" cy="80" r="28" fill="#0f0a03" stroke="#ef5b55" stroke-width="3"/>
        <line x1="56" y1="56" x2="104" y2="104" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
        <line x1="104" y1="56" x2="56" y2="104" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
        <circle cx="80" cy="80" r="8" fill="#ef5b55"/>'''
    }
}

for aname, adata in avatars.items():
    svg_str = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <defs>
    <filter id="glow_{aname[:8]}">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <g filter="url(#glow_{aname[:8]})">
    {adata['art']}
  </g>
</svg>'''
    with open(os.path.join(AVATARS_DIR, aname), "w", encoding="utf-8") as f:
        f.write(svg_str)

print(f"Generated {len(avatars)} Circular Echo-Core Avatars.")

# 3. BESPOKE FLOOR MINI-BANNERS FOR RIGHT SIDEBAR (340x85 SVGs)
floor_banners = {
    "floor_banner_f1_neutral.svg": {
        "floor": "SECTOR 01 // PALM CORE", "name": "NEUTRAL COMMAND", "lead": "MAJIN", "color": "#ef5b55", "bg1": "#22080c", "bg2": "#090406",
        "glyph": '''<circle cx="45" cy="42" r="30" fill="#ef5b55" fill-opacity="0.2" stroke="#ef5b55" stroke-width="2.5"/><polygon points="45,22 65,42 45,62 25,42" fill="#ef5b55"/><circle cx="45" cy="42" r="8" fill="#ffffff"/>'''
    },
    "floor_banner_f2_maws_keep.svg": {
        "floor": "SECTOR 02 // WARD KEEP", "name": "MAW'S KEEP", "lead": "DEKAN", "color": "#5b75e8", "bg1": "#0b1226", "bg2": "#040712",
        "glyph": '''<rect x="18" y="16" width="54" height="54" rx="6" fill="#5b75e8" fill-opacity="0.2" stroke="#5b75e8" stroke-width="2.5"/><path d="M28,26 L62,26 L62,60 L28,60 Z" fill="none" stroke="#ffffff" stroke-width="2"/><circle cx="45" cy="43" r="10" fill="#38bdf8"/>'''
    },
    "floor_banner_f3_extraction.svg": {
        "floor": "SECTOR 03 // SIPHON FORGE", "name": "EXTRACTION HALL", "lead": "ZYRAK", "color": "#e6c843", "bg1": "#221d06", "bg2": "#0a0802",
        "glyph": '''<polygon points="45,14 74,68 16,68" fill="#e6c843" fill-opacity="0.2" stroke="#e6c843" stroke-width="2.5"/><circle cx="45" cy="50" r="14" fill="#e6c843"/><polygon points="45,36 54,54 36,54" fill="#ffffff"/>'''
    },
    "floor_banner_f4_insight_forge.svg": {
        "floor": "SECTOR 04 // RESEARCH CORE", "name": "INSIGHT FORGE", "lead": "AYSHUK", "color": "#47c978", "bg1": "#092214", "bg2": "#030d07",
        "glyph": '''<polygon points="45,16 72,32 72,60 45,76 18,60 18,32" fill="#47c978" fill-opacity="0.2" stroke="#47c978" stroke-width="2.5"/><circle cx="45" cy="46" r="12" fill="#47c978"/><line x1="45" y1="26" x2="45" y2="66" stroke="#ffffff" stroke-width="2.5"/>'''
    },
    "floor_banner_f5_border_watch.svg": {
        "floor": "SECTOR 05 // BORDER BASTION", "name": "BORDER WATCH", "lead": "MELLDA", "color": "#d4d4d8", "bg1": "#181a1f", "bg2": "#090a0d",
        "glyph": '''<path d="M45,16 L72,28 L72,56 Q45,76 45,76 Q18,56 18,56 L18,28 Z" fill="#d4d4d8" fill-opacity="0.2" stroke="#d4d4d8" stroke-width="2.5"/><circle cx="45" cy="44" r="12" fill="#d4d4d8"/><circle cx="45" cy="44" r="5" fill="#181a1f"/>'''
    },
    "floor_banner_f6_deep_vault.svg": {
        "floor": "SECTOR 06 // CRYO ARCHIVE", "name": "DEEP VAULT", "lead": "MARJUK", "color": "#be123c", "bg1": "#220811", "bg2": "#0a0307",
        "glyph": '''<rect x="20" y="16" width="50" height="54" rx="4" fill="#be123c" fill-opacity="0.2" stroke="#be123c" stroke-width="2.5"/><line x1="30" y1="30" x2="60" y2="30" stroke="#ffffff" stroke-width="3"/><line x1="30" y1="44" x2="60" y2="44" stroke="#f1df76" stroke-width="2.5"/><line x1="30" y1="56" x2="52" y2="56" stroke="#ffffff" stroke-width="2.5"/>'''
    },
    "floor_banner_f7_shadow_corps.svg": {
        "floor": "SECTOR 07 // VOID DIVERS", "name": "SHADOW CORPS", "lead": "ISHALL", "color": "#f43f5e", "bg1": "#220817", "bg2": "#0a030b",
        "glyph": '''<polygon points="45,14 75,44 45,74 15,44" fill="#f43f5e" fill-opacity="0.2" stroke="#f43f5e" stroke-width="2.5"/><circle cx="45" cy="44" r="14" fill="#f43f5e"/><line x1="45" y1="28" x2="45" y2="60" stroke="#ffffff" stroke-width="3"/>'''
    },
    "floor_banner_f8_gate_watch.svg": {
        "floor": "SECTOR 08 // TABOO GATE", "name": "GATE WATCH", "lead": "XYAN", "color": "#fbbf24", "bg1": "#241806", "bg2": "#0c0802",
        "glyph": '''<circle cx="45" cy="44" r="30" fill="#fbbf24" fill-opacity="0.2" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="6,3"/><line x1="28" y1="28" x2="62" y2="62" stroke="#ffffff" stroke-width="3.5"/><line x1="62" y1="28" x2="28" y2="62" stroke="#ffffff" stroke-width="3.5"/><circle cx="45" cy="44" r="6" fill="#ef5b55"/>'''
    }
}

for fname, fdata in floor_banners.items():
    svg_str = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="340" height="85">
  <defs>
    <linearGradient id="bg_{fname[:8]}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{fdata['bg1']}"/>
      <stop offset="100%" stop-color="{fdata['bg2']}"/>
    </linearGradient>
  </defs>
  <!-- Base Background -->
  <rect width="340" height="85" rx="6" fill="url(#bg_{fname[:8]})" stroke="{fdata['color']}" stroke-width="2"/>
  
  <!-- Left Glyph Emblem -->
  {fdata['glyph']}
  
  <!-- Content Typography -->
  <text x="85" y="24" fill="#94a3b8" font-family="monospace" font-size="9" font-weight="bold" letter-spacing="1">[{fdata['floor']}]</text>
  <text x="85" y="48" fill="{fdata['color']}" font-family="Impact" font-size="18" letter-spacing="1">{fdata['name']}</text>
  <text x="85" y="68" fill="#e2e8f0" font-family="monospace" font-size="10">COMMAND: <tspan fill="#f1df76">{fdata['lead']}</tspan> | STATUS: <tspan fill="#10b981">STABLE</tspan></text>
  
  <!-- Right Accent Chevron -->
  <polygon points="320,42 308,30 312,26 328,42 312,58 308,54" fill="{fdata['color']}"/>
</svg>'''
    with open(os.path.join(BANNERS_DIR, fname), "w", encoding="utf-8") as f:
        f.write(svg_str)

print(f"Generated {len(floor_banners)} Bespoke Floor Mini-Banners.")

# 4. BACKGROUND PATTERNS & WATERMARKS
bg_grid_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
  <defs>
    <pattern id="tacticalGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#182333" stroke-width="0.75" opacity="0.3"/>
      <circle cx="0" cy="0" r="1.5" fill="#38bdf8" opacity="0.4"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#tacticalGrid)"/>
</svg>'''

with open(os.path.join(BG_DIR, "bg_tactical_grid.svg"), "w", encoding="utf-8") as f:
    f.write(bg_grid_svg)

print("Generated Background Patterns.")
