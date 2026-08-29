import os

def upgrade_all_entity_art_suite():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    assets_dir = os.path.join(wiki_root, "assets")
    banners_dir = os.path.join(assets_dir, "banners")
    profiles_dir = os.path.join(assets_dir, "profiles")
    icons_dir = os.path.join(assets_dir, "icons")
    entity_art_dir = os.path.join(assets_dir, "art/entities")
    user_icons_dir = "/home/user/icons"

    os.makedirs(banners_dir, exist_ok=True)
    os.makedirs(profiles_dir, exist_ok=True)
    os.makedirs(icons_dir, exist_ok=True)
    os.makedirs(entity_art_dir, exist_ok=True)
    os.makedirs(user_icons_dir, exist_ok=True)

    # -------------------------------------------------------------
    # 10 CANONICAL SORROW ENTITIES COMPLETE VECTOR SUITE
    # -------------------------------------------------------------
    entities = {
        "se_001": {
            "id": "SE-001",
            "name": "WEEPING COLOSSUS",
            "korean": "통곡의 거상 (Tonggok-ui Geosang)",
            "risk": "PHANTASM (δ)",
            "color": "#ef5b55",
            "bg": "#200609",
            "dmg": "GRUDGE // PHYSICAL",
            "work": "ATTACHMENT / REPRESSION",
            "banner_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgSE001" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2a060a"/>
      <stop offset="50%" stop-color="#120204"/>
      <stop offset="100%" stop-color="#050001"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#bgSE001)"/>
  <!-- Containment Blast Chamber Frame -->
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#ef5b55" stroke-width="3"/>
  <line x1="20" y1="60" x2="1180" y2="60" stroke="#ef5b55" stroke-width="0.8" stroke-dasharray="8 4" opacity="0.5"/>
  <line x1="20" y1="340" x2="1180" y2="340" stroke="#ef5b55" stroke-width="0.8" stroke-dasharray="8 4" opacity="0.5"/>
  
  <!-- Central Containment Platform & Colossus Titan Silhouette -->
  <g transform="translate(600, 200)">
    <!-- Platform Base -->
    <polygon points="-160,120 160,120 120,150 -120,150" fill="#450a0a" stroke="#ef5b55" stroke-width="2"/>
    <!-- Colossal Titan Torso & Shoulders -->
    <path d="M -110,110 L -90,-20 L -60,-60 L 60,-60 L 90,-20 L 110,110 Z" fill="#180407" stroke="#ef5b55" stroke-width="3"/>
    <!-- Basalt Mask with Bleeding Fissures -->
    <polygon points="-40,-110 40,-110 32,-40 0,-20 -32,-40" fill="#3b080d" stroke="#f1df76" stroke-width="2.5"/>
    <!-- Molten Silver Weeping Tears -->
    <path d="M -18,-70 L -18,-20 Q -24,0 -16,10" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <path d="M 18,-70 L 18,-20 Q 24,0 16,10" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <!-- Bleeding Crimson Han Veins -->
    <line x1="0" y1="-110" x2="0" y2="-50" stroke="#ef5b55" stroke-width="2"/>
    <line x1="0" y1="-50" x2="-20" y2="-30" stroke="#ef5b55" stroke-width="2"/>
    <circle cx="-18" cy="-76" r="4" fill="#000000" stroke="#ef5b55" stroke-width="1.5"/>
    <circle cx="18" cy="-76" r="4" fill="#000000" stroke="#ef5b55" stroke-width="1.5"/>
    <!-- Quad Heavy Containment Chains -->
    <line x1="-90,-20" x2="-260,-120" stroke="#f1df76" stroke-width="2.5" stroke-dasharray="8 4"/>
    <line x1="90,-20" x2="260,-120" stroke="#f1df76" stroke-width="2.5" stroke-dasharray="8 4"/>
    <line x1="-110,80" x2="-280,120" stroke="#f1df76" stroke-width="2.5" stroke-dasharray="8 4"/>
    <line x1="110,80" x2="280,120" stroke="#f1df76" stroke-width="2.5" stroke-dasharray="8 4"/>
  </g>

  <!-- HUD Telemetry & Containment Data -->
  <text x="60" y="110" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" letter-spacing="3">[ CONTAINMENT CELL // SE-001 ]</text>
  <text x="60" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="32" font-weight="bold">WEEPING COLOSSUS</text>
  <text x="60" y="180" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="15">RISK: PHANTASM (δ) | DAMAGE: GRUDGE // HP</text>
  <text x="60" y="210" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="13">COHERENCE THRESHOLD: 3 | WORK: ATTACHMENT</text>
  
  <rect x="60" y="240" width="220" height="10" rx="2" fill="#450a0a" stroke="#ef5b55" stroke-width="1"/>
  <rect x="62" y="242" width="180" height="6" rx="1" fill="#ef5b55"/>
  <text x="290" y="250" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">COHERENCE: 82%</text>
</svg>''',
            "profile_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <rect width="500" height="500" fill="#180407" stroke="#ef5b55" stroke-width="4"/>
  <!-- Basalt Armor Plating & Mask -->
  <polygon points="120,440 380,440 340,160 160,160" fill="#2d060a" stroke="#ef5b55" stroke-width="3"/>
  <polygon points="190,80 310,80 290,200 250,240 210,200" fill="#3b080d" stroke="#f1df76" stroke-width="3"/>
  <!-- Molten Silver Tears -->
  <path d="M 220,140 L 220,240 Q 210,280 230,300" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <path d="M 280,140 L 280,240 Q 290,280 270,300" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="220" cy="130" r="8" fill="#000000" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="280" cy="130" r="8" fill="#000000" stroke="#ef5b55" stroke-width="2"/>
  <text x="250" y="475" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">SE-001 // WEEPING COLOSSUS</text>
</svg>'''
        },

        "se_003": {
            "id": "SE-003",
            "name": "THREAD OF MEMORY",
            "korean": "기억의 실타래 (Gieok-ui Siltarae)",
            "risk": "SOMNA (β)",
            "color": "#38bdf8",
            "bg": "#031526",
            "dmg": "LAMENT // SP",
            "work": "INSIGHT / REPRESSION",
            "banner_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect width="1200" height="400" fill="#041527"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <!-- Central Spider-Silk Memory Web -->
  <g transform="translate(600, 200)">
    <circle cx="0" cy="0" r="140" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6 3"/>
    <circle cx="0" cy="0" r="90" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6 3"/>
    <circle cx="0" cy="0" r="40" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <line x1="-140" y1="0" x2="140" y2="0" stroke="#ffffff" stroke-width="1.5"/>
    <line x1="0" y1="-140" x2="0" y2="140" stroke="#ffffff" stroke-width="1.5"/>
    <line x1="-100" y1="-100" x2="100" y2="100" stroke="#ffffff" stroke-width="1.5"/>
    <line x1="-100" y1="100" x2="100" y2="-100" stroke="#ffffff" stroke-width="1.5"/>
    <!-- Sapphire Siphon Needle -->
    <polygon points="0,-120 12,0 0,120 -12,0" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
    <circle cx="0" cy="-40" r="8" fill="#ffffff"/>
  </g>
  <text x="60" y="110" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" letter-spacing="3">[ CONTAINMENT CELL // SE-003 ]</text>
  <text x="60" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="32" font-weight="bold">THREAD OF MEMORY</text>
  <text x="60" y="180" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="15">RISK: SOMNA (β) | DAMAGE: LAMENT // SP</text>
  <text x="60" y="210" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="13">COHERENCE THRESHOLD: 2 | WORK: INSIGHT</text>
</svg>''',
            "profile_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <rect width="500" height="500" fill="#031526" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="250" cy="230" r="160" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8 4"/>
  <circle cx="250" cy="230" r="100" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8 4"/>
  <polygon points="250,60 270,230 250,400 230,230" fill="#0284c7" stroke="#ffffff" stroke-width="3"/>
  <circle cx="250" cy="160" r="12" fill="#ffffff"/>
  <text x="250" y="475" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">SE-003 // THREAD OF MEMORY</text>
</svg>'''
        },

        "se_004": {
            "id": "SE-004",
            "name": "OBSIDIAN MIRROR",
            "korean": "흑요석 거울 (Heugyoseok Geoul)",
            "risk": "MORPHEAN (γ)",
            "color": "#c084fc",
            "bg": "#130421",
            "dmg": "VOID // % MAX HP",
            "work": "INSIGHT / ATTACHMENT",
            "banner_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect width="1200" height="400" fill="#140224"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#c084fc" stroke-width="3"/>
  <!-- Central Obsidian Mirror Frame -->
  <g transform="translate(600, 200)">
    <polygon points="0,-130 110,-40 90,110 0,140 -90,110 -110,-40" fill="#2e1065" stroke="#c084fc" stroke-width="4"/>
    <line x1="0" y1="-130" x2="0" y2="140" stroke="#ffffff" stroke-width="2"/>
    <line x1="-110" y1="-40" x2="90" y2="110" stroke="#ffffff" stroke-width="2"/>
    <circle cx="0" cy="0" r="30" fill="#ef5b55" stroke="#ffffff" stroke-width="3"/>
    <circle cx="0" cy="0" r="10" fill="#000000"/>
  </g>
  <text x="60" y="110" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" letter-spacing="3">[ CONTAINMENT CELL // SE-004 ]</text>
  <text x="60" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="32" font-weight="bold">OBSIDIAN MIRROR</text>
  <text x="60" y="180" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="15">RISK: MORPHEAN (γ) | DAMAGE: VOID // % HP</text>
  <text x="60" y="210" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="13">COHERENCE THRESHOLD: 3 | WORK: INSIGHT</text>
</svg>''',
            "profile_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <rect width="500" height="500" fill="#130421" stroke="#c084fc" stroke-width="4"/>
  <polygon points="250,50 400,160 360,370 250,420 140,370 100,160" fill="#2e1065" stroke="#c084fc" stroke-width="4"/>
  <line x1="250" y1="50" x2="250" y2="420" stroke="#ffffff" stroke-width="2.5"/>
  <line x1="100" y1="160" x2="360" y2="370" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="250" cy="235" r="40" fill="#ef5b55" stroke="#ffffff" stroke-width="4"/>
  <circle cx="250" cy="235" r="14" fill="#000000"/>
  <text x="250" y="475" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">SE-004 // OBSIDIAN MIRROR</text>
</svg>'''
        },

        "se_006": {
            "id": "SE-006",
            "name": "CLOCKWORK HEART",
            "korean": "태엽 심장 (Taeyeop Simjang)",
            "risk": "MORPHEAN (γ)",
            "color": "#f1df76",
            "bg": "#1c1402",
            "dmg": "WEIGHT // DUAL",
            "work": "INSTINCT / REPRESSION",
            "banner_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect width="1200" height="400" fill="#1a1202"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#f1df76" stroke-width="3"/>
  <g transform="translate(600, 200)">
    <circle cx="0" cy="0" r="110" fill="#451a03" stroke="#f1df76" stroke-width="4"/>
    <circle cx="0" cy="0" r="60" fill="#1c1402" stroke="#f1df76" stroke-width="2.5"/>
    <circle cx="0" cy="0" r="24" fill="#ef5b55"/>
    <line x1="-110" y1="0" x2="110" y2="0" stroke="#f1df76" stroke-width="3"/>
    <line x1="0" y1="-110" x2="0" y2="110" stroke="#f1df76" stroke-width="3"/>
  </g>
  <text x="60" y="110" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" letter-spacing="3">[ CONTAINMENT CELL // SE-006 ]</text>
  <text x="60" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="32" font-weight="bold">CLOCKWORK HEART</text>
  <text x="60" y="180" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="15">RISK: MORPHEAN (γ) | DAMAGE: WEIGHT // DUAL</text>
</svg>''',
            "profile_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <rect width="500" height="500" fill="#1c1402" stroke="#f1df76" stroke-width="4"/>
  <circle cx="250" cy="235" r="140" fill="#451a03" stroke="#f1df76" stroke-width="4"/>
  <circle cx="250" cy="235" r="80" fill="#1c1402" stroke="#f1df76" stroke-width="3"/>
  <circle cx="250" cy="235" r="30" fill="#ef5b55"/>
  <text x="250" y="475" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">SE-006 // CLOCKWORK HEART</text>
</svg>'''
        },

        "se_007": {
            "id": "SE-007",
            "name": "ASHEN SCRIBE",
            "korean": "잿빛 필경사 (Jaetbit Pilgyeongsa)",
            "risk": "SOMNA (β)",
            "color": "#ef5b55",
            "bg": "#1f0608",
            "dmg": "GRUDGE // PHYSICAL",
            "work": "INSIGHT / ATTACHMENT",
            "banner_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect width="1200" height="400" fill="#1f0608"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#ef5b55" stroke-width="3"/>
  <g transform="translate(600, 200)">
    <rect x="-90" y="-100" width="180" height="200" rx="4" fill="#450a0a" stroke="#ef5b55" stroke-width="3"/>
    <line x1="-70" y1="-60" x2="70" y2="-60" stroke="#f1df76" stroke-width="3"/>
    <line x1="-70" y1="-20" x2="70" y2="-20" stroke="#f1df76" stroke-width="3"/>
    <line x1="-70" y1="20" x2="70" y2="20" stroke="#f1df76" stroke-width="3"/>
    <polygon points="40,-120 80,-40 20,40" fill="#ffffff" stroke="#ef5b55" stroke-width="2"/>
  </g>
  <text x="60" y="110" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" letter-spacing="3">[ CONTAINMENT CELL // SE-007 ]</text>
  <text x="60" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="32" font-weight="bold">ASHEN SCRIBE</text>
  <text x="60" y="180" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="15">RISK: SOMNA (β) | DAMAGE: GRUDGE // HP</text>
</svg>''',
            "profile_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <rect width="500" height="500" fill="#1f0608" stroke="#ef5b55" stroke-width="4"/>
  <rect x="130" y="100" width="240" height="280" rx="6" fill="#450a0a" stroke="#ef5b55" stroke-width="4"/>
  <line x1="160" y1="160" x2="340" y2="160" stroke="#f1df76" stroke-width="4"/>
  <line x1="160" y1="220" x2="340" y2="220" stroke="#f1df76" stroke-width="4"/>
  <line x1="160" y1="280" x2="340" y2="280" stroke="#f1df76" stroke-width="4"/>
  <text x="250" y="475" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">SE-007 // ASHEN SCRIBE</text>
</svg>'''
        },

        "se_008": {
            "id": "SE-008",
            "name": "FORGOTTEN CRADLE",
            "korean": "잊혀진 요람 (Ichyeojin Yoram)",
            "risk": "AETHER (α)",
            "color": "#71efaf",
            "bg": "#02140d",
            "dmg": "LAMENT // SP",
            "work": "ATTACHMENT / INSTINCT",
            "banner_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect width="1200" height="400" fill="#02140d"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#71efaf" stroke-width="3"/>
  <g transform="translate(600, 200)">
    <path d="M -100,-20 L 100,-20 L 80,60 L -80,60 Z" fill="#064e3b" stroke="#71efaf" stroke-width="3"/>
    <path d="M -110,80 Q 0,120 110,80" fill="none" stroke="#f1df76" stroke-width="4"/>
    <polygon points="0,-100 8,-80 28,-75 14,-60 18,-40 0,-50 -18,-40 -14,-60 -28,-75 -8,-80" fill="#ffffff"/>
  </g>
  <text x="60" y="110" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" letter-spacing="3">[ CONTAINMENT CELL // SE-008 ]</text>
  <text x="60" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="32" font-weight="bold">FORGOTTEN CRADLE</text>
  <text x="60" y="180" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="15">RISK: AETHER (α) | DAMAGE: LAMENT // SP</text>
</svg>''',
            "profile_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <rect width="500" height="500" fill="#02140d" stroke="#71efaf" stroke-width="4"/>
  <path d="M 100,180 L 400,180 L 360,320 L 140,320 Z" fill="#064e3b" stroke="#71efaf" stroke-width="4"/>
  <path d="M 90,360 Q 250,420 410,360" fill="none" stroke="#f1df76" stroke-width="5"/>
  <text x="250" y="475" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">SE-008 // FORGOTTEN CRADLE</text>
</svg>'''
        },

        "se_009": {
            "id": "SE-009",
            "name": "DROWNED BELL",
            "korean": "익사의 종 (Iksa-ui Jong)",
            "risk": "SOMNA (β)",
            "color": "#38bdf8",
            "bg": "#041b2c",
            "dmg": "LAMENT // SP",
            "work": "INSIGHT / REPRESSION",
            "banner_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect width="1200" height="400" fill="#041b2c"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <g transform="translate(600, 200)">
    <path d="M -50,-100 L 50,-100 L 80,40 L 110,70 L -110,70 L -80,40 Z" fill="#0e7490" stroke="#38bdf8" stroke-width="4"/>
    <circle cx="0" cy="90" r="16" fill="#f1df76" stroke="#ffffff" stroke-width="3"/>
  </g>
  <text x="60" y="110" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" letter-spacing="3">[ CONTAINMENT CELL // SE-009 ]</text>
  <text x="60" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="32" font-weight="bold">DROWNED BELL</text>
  <text x="60" y="180" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="15">RISK: SOMNA (β) | DAMAGE: LAMENT // SP</text>
</svg>''',
            "profile_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <rect width="500" height="500" fill="#041b2c" stroke="#38bdf8" stroke-width="4"/>
  <path d="M 180,90 L 320,90 L 370,280 L 410,340 L 90,340 L 130,280 Z" fill="#0e7490" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="250" cy="380" r="24" fill="#f1df76" stroke="#ffffff" stroke-width="3"/>
  <text x="250" y="475" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">SE-009 // DROWNED BELL</text>
</svg>'''
        },

        "se_011": {
            "id": "SE-011",
            "name": "IRON MAIDEN OF REGRET",
            "korean": "후회의 철처녀 (Huhoe-ui Cheolcheonyeo)",
            "risk": "PHANTASM (δ)",
            "color": "#ef5b55",
            "bg": "#1f0608",
            "dmg": "GRUDGE // PHYSICAL",
            "work": "REPRESSION / ATTACHMENT",
            "banner_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect width="1200" height="400" fill="#1f0608"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#ef5b55" stroke-width="3"/>
  <g transform="translate(600, 200)">
    <path d="M -60,-120 L 60,-120 L 90,-30 L 70,110 L -70,110 L -90,-30 Z" fill="#450a0a" stroke="#ef5b55" stroke-width="4"/>
    <circle cx="0" cy="-60" r="20" fill="#2d060a" stroke="#ffffff" stroke-width="2"/>
  </g>
  <text x="60" y="110" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" letter-spacing="3">[ CONTAINMENT CELL // SE-011 ]</text>
  <text x="60" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="32" font-weight="bold">IRON MAIDEN OF REGRET</text>
  <text x="60" y="180" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="15">RISK: PHANTASM (δ) | DAMAGE: GRUDGE // HP</text>
</svg>''',
            "profile_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <rect width="500" height="500" fill="#1f0608" stroke="#ef5b55" stroke-width="4"/>
  <path d="M 170,60 L 330,60 L 380,180 L 350,380 L 150,380 L 120,180 Z" fill="#450a0a" stroke="#ef5b55" stroke-width="4"/>
  <circle cx="250" cy="140" r="30" fill="#2d060a" stroke="#ffffff" stroke-width="3"/>
  <text x="250" y="475" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">SE-011 // IRON MAIDEN</text>
</svg>'''
        },

        "se_014": {
            "id": "SE-014",
            "name": "HOLLOW SINGER",
            "korean": "공허의 가희 (Gongheo-ui Gahui)",
            "risk": "APOCRYPHA (ω)",
            "color": "#c084fc",
            "bg": "#130421",
            "dmg": "VOID // % MAX HP",
            "work": "INSIGHT / ATTACHMENT",
            "banner_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect width="1200" height="400" fill="#130421"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#c084fc" stroke-width="3"/>
  <g transform="translate(600, 200)">
    <ellipse cx="0" cy="0" rx="70" ry="90" fill="#f8fafc" stroke="#c084fc" stroke-width="4"/>
    <ellipse cx="-30" cy="-25" rx="10" ry="16" fill="#000000"/>
    <ellipse cx="30" cy="-25" rx="10" ry="16" fill="#000000"/>
    <ellipse cx="0" cy="30" rx="26" ry="36" fill="#3b0764" stroke="#c084fc" stroke-width="3"/>
  </g>
  <text x="60" y="110" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" letter-spacing="3">[ CONTAINMENT CELL // SE-014 ]</text>
  <text x="60" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="32" font-weight="bold">HOLLOW SINGER</text>
  <text x="60" y="180" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="15">RISK: APOCRYPHA (ω) | DAMAGE: VOID // % HP</text>
</svg>''',
            "profile_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <rect width="500" height="500" fill="#130421" stroke="#c084fc" stroke-width="4"/>
  <ellipse cx="250" cy="220" rx="110" ry="140" fill="#f8fafc" stroke="#c084fc" stroke-width="5"/>
  <ellipse cx="205" cy="180" rx="15" ry="24" fill="#000000"/>
  <ellipse cx="295" cy="180" rx="15" ry="24" fill="#000000"/>
  <ellipse cx="250" cy="265" rx="40" ry="55" fill="#3b0764" stroke="#c084fc" stroke-width="4"/>
  <text x="250" y="475" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">SE-014 // HOLLOW SINGER</text>
</svg>'''
        },

        "se_015": {
            "id": "SE-015",
            "name": "SOVEREIGN CROWN",
            "korean": "군주의 왕관 (Gunju-ui Wanggwan)",
            "risk": "APOCRYPHA (ω)",
            "color": "#f1df76",
            "bg": "#1c1402",
            "dmg": "HOPE // RESTORATION",
            "work": "ATTACHMENT / INSIGHT",
            "banner_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect width="1200" height="400" fill="#1c1402"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#f1df76" stroke-width="3"/>
  <g transform="translate(600, 200)">
    <circle cx="0" cy="0" r="100" fill="none" stroke="#fef08a" stroke-width="4" stroke-dasharray="10 5"/>
    <polygon points="-80,40 -60,-40 -30,20 0,-60 30,20 60,-40 80,40 -80,40" fill="#0f172a" stroke="#f1df76" stroke-width="4"/>
    <circle cx="0" cy="0" r="12" fill="#ef5b55"/>
  </g>
  <text x="60" y="110" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" letter-spacing="3">[ CONTAINMENT CELL // SE-015 ]</text>
  <text x="60" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="32" font-weight="bold">SOVEREIGN CROWN</text>
  <text x="60" y="180" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="15">RISK: APOCRYPHA (ω) | DAMAGE: HOPE // RESTORATION</text>
</svg>''',
            "profile_svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <rect width="500" height="500" fill="#1c1402" stroke="#f1df76" stroke-width="4"/>
  <circle cx="250" cy="220" r="130" fill="none" stroke="#fef08a" stroke-width="4" stroke-dasharray="12 6"/>
  <polygon points="140,260 170,140 210,220 250,110 290,220 330,140 360,260 140,260" fill="#0f172a" stroke="#f1df76" stroke-width="4"/>
  <circle cx="250" cy="210" r="16" fill="#ef5b55"/>
  <text x="250" y="475" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">SE-015 // SOVEREIGN CROWN</text>
</svg>'''
        }
    }

    for k, data in entities.items():
        dash_id = data["id"].lower()
        underscore_id = k

        # 1. Banners
        b_svg = data["banner_svg"]
        for fn in [f"banner_entity_{underscore_id}.svg", f"{dash_id}-banner.svg"]:
            with open(os.path.join(banners_dir, fn), "w", encoding="utf-8") as f:
                f.write(b_svg)
            with open(os.path.join(entity_art_dir, fn), "w", encoding="utf-8") as f:
                f.write(b_svg)

        # 2. Profiles
        p_svg = data["profile_svg"]
        for fn in [f"profile_entity_{underscore_id}.svg", f"{dash_id}-profile.svg"]:
            with open(os.path.join(profiles_dir, fn), "w", encoding="utf-8") as f:
                f.write(p_svg)
            with open(os.path.join(entity_art_dir, fn), "w", encoding="utf-8") as f:
                f.write(p_svg)

    # Sync legacy names if any
    legacy_entities = ["se-002", "se-005", "se-010"]
    for leg in legacy_entities:
        targ = "se-001"
        for ext in ["-icon.svg", "-banner.svg", "-profile.svg", ".svg"]:
            src = os.path.join(entity_art_dir, f"{targ}{ext}")
            dst = os.path.join(entity_art_dir, f"{leg}{ext}")
            if os.path.exists(src):
                with open(src, "r", encoding="utf-8") as f:
                    c = f.read()
                with open(dst, "w", encoding="utf-8") as f:
                    f.write(c)

    print("Upgraded all 10 Sorrow Entity Banners and Profiles!")

if __name__ == "__main__":
    upgrade_all_entity_art_suite()
