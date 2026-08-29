import os

BANNERS_DIR = "/home/user/01_Somnarak_Wiki/assets/banners"

banners = {
    "banner_hero_sorrow_entities.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300">
  <defs>
    <linearGradient id="bgEntities" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#18060a"/>
      <stop offset="50%" stop-color="#0d0e1c"/>
      <stop offset="100%" stop-color="#18060a"/>
    </linearGradient>
    <filter id="glowE"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="1200" height="300" fill="url(#bgEntities)"/>
  <g stroke="#22324d" stroke-width="1" opacity="0.4">
    <circle cx="600" cy="150" r="120" fill="none" stroke-dasharray="6,4"/>
    <circle cx="600" cy="150" r="220" fill="none"/>
    <line x1="0" y1="150" x2="1200" y2="150"/>
  </g>
  <!-- Entity Runes & Icons Left and Right -->
  <g filter="url(#glowE)">
    <circle cx="200" cy="150" r="45" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="3"/>
    <text x="200" y="157" fill="#10b981" font-family="Impact" font-size="20" text-anchor="middle">T-01 CAN</text>

    <circle cx="380" cy="150" r="45" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="3"/>
    <text x="380" y="157" fill="#38bdf8" font-family="Impact" font-size="20" text-anchor="middle">T-02 TETH</text>

    <!-- Center Master Abyss Nexus -->
    <polygon points="600,40 690,150 600,260 510,150" fill="#ef4444" fill-opacity="0.25" stroke="#ef4444" stroke-width="4"/>
    <circle cx="600" cy="150" r="35" fill="#0c0507" stroke="#f1df76" stroke-width="3"/>
    <text x="600" y="158" fill="#ffffff" font-family="Impact" font-size="24" text-anchor="middle">ALEPH</text>

    <circle cx="820" cy="150" r="45" fill="#f1df76" fill-opacity="0.2" stroke="#f1df76" stroke-width="3"/>
    <text x="820" y="157" fill="#f1df76" font-family="Impact" font-size="20" text-anchor="middle">T-03 HE</text>

    <circle cx="1000" cy="150" r="45" fill="#a855f7" fill-opacity="0.2" stroke="#a855f7" stroke-width="3"/>
    <text x="1000" y="157" fill="#a855f7" font-family="Impact" font-size="20" text-anchor="middle">T-04 WAW</text>
  </g>
  <text x="600" y="40" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="4" text-anchor="middle">SORROW ENTITY CONTAINMENT CODEX</text>
  <text x="600" y="285" fill="#38bdf8" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">[ SECC THREAT MATRIX // 10 CANONICAL PHENOMENA // CONTAINMENT MANDATE ]</text>
</svg>''',

    "banner_hero_maw_arsenal.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300">
  <defs>
    <linearGradient id="bgMaw" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1c1605"/>
      <stop offset="50%" stop-color="#0a1220"/>
      <stop offset="100%" stop-color="#1c1605"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="300" fill="url(#bgMaw)"/>
  <!-- Forge Anvil & Extraction Laser Rays -->
  <line x1="300" y1="0" x2="600" y2="150" stroke="#f1df76" stroke-width="3" opacity="0.7"/>
  <line x1="900" y1="0" x2="600" y2="150" stroke="#f1df76" stroke-width="3" opacity="0.7"/>
  <circle cx="600" cy="150" r="60" fill="#f1df76" fill-opacity="0.2" stroke="#ef5b55" stroke-width="4"/>
  <!-- Crossed Weapons Vector -->
  <line x1="550" y1="100" x2="650" y2="200" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>
  <line x1="650" y1="100" x2="550" y2="200" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>
  <circle cx="600" cy="150" r="14" fill="#ef5b55"/>
  <!-- Left/Right Triad Categories -->
  <text x="180" y="160" fill="#f1df76" font-family="Impact" font-size="24" text-anchor="middle">9 WEAPONS</text>
  <text x="180" y="185" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">AGONY FORGE</text>
  <text x="1020" y="160" fill="#38bdf8" font-family="Impact" font-size="24" text-anchor="middle">9 SUITS &amp; GIFTS</text>
  <text x="1020" y="185" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">SYNAPSE WEAVES</text>
  <!-- Header Overlay -->
  <text x="600" y="45" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="4" text-anchor="middle">M.A.W. ARMAMENT ARSENAL</text>
  <text x="600" y="285" fill="#ef5b55" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">[ MATERIALIZED AGONY WEAPONRY // TRIAD GEAR SYSTEM // EXTRACTION HALL ]</text>
</svg>''',

    "banner_hero_echo_cores.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300">
  <defs>
    <linearGradient id="bgCores" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#18080c"/>
      <stop offset="50%" stop-color="#081022"/>
      <stop offset="100%" stop-color="#18080c"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="300" fill="url(#bgCores)"/>
  <!-- 9 Pedestals for Echo Cores -->
  <g stroke="#f1df76" stroke-width="2" opacity="0.8">
    <circle cx="120" cy="150" r="32" fill="#ef5b55" fill-opacity="0.3"/>
    <circle cx="240" cy="150" r="32" fill="#5b75e8" fill-opacity="0.3"/>
    <circle cx="360" cy="150" r="32" fill="#38bdf8" fill-opacity="0.3"/>
    <circle cx="480" cy="150" r="32" fill="#e6c843" fill-opacity="0.3"/>
    <circle cx="600" cy="150" r="42" fill="#ef5b55" fill-opacity="0.5" stroke-width="4"/>
    <circle cx="720" cy="150" r="32" fill="#47c978" fill-opacity="0.3"/>
    <circle cx="840" cy="150" r="32" fill="#d4d4d8" fill-opacity="0.3"/>
    <circle cx="960" cy="150" r="32" fill="#be123c" fill-opacity="0.3"/>
    <circle cx="1080" cy="150" r="32" fill="#fbbf24" fill-opacity="0.3"/>
  </g>
  <text x="600" y="158" fill="#ffffff" font-family="Impact" font-size="20" text-anchor="middle">MAJIN</text>
  <text x="600" y="45" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="4" text-anchor="middle">THE NINE ECHO-CORES &amp; EXECUTIVE COMMAND</text>
  <text x="600" y="285" fill="#38bdf8" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">[ IMMORTAL MEMORY RETENTION // 1,778 CYCLES // SECTOR LEADS ]</text>
</svg>''',

    "banner_hero_combat_mechanics.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300">
  <defs>
    <linearGradient id="bgMech" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#060c18"/>
      <stop offset="50%" stop-color="#14061a"/>
      <stop offset="100%" stop-color="#060c18"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="300" fill="url(#bgMech)"/>
  <!-- 4 Damage Type Pillars -->
  <g>
    <rect x="150" y="90" width="180" height="120" rx="6" fill="#1a0606" stroke="#ef4444" stroke-width="2.5"/>
    <text x="240" y="145" fill="#ef4444" font-family="Impact" font-size="22" text-anchor="middle">PHYSICAL (RED)</text>
    <text x="240" y="170" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">HP DAMAGE</text>

    <rect x="390" y="90" width="180" height="120" rx="6" fill="#06131c" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="480" y="145" fill="#38bdf8" font-family="Impact" font-size="22" text-anchor="middle">MENTAL (WHITE)</text>
    <text x="480" y="170" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">SANITY SP</text>

    <rect x="630" y="90" width="180" height="120" rx="6" fill="#14061a" stroke="#a855f7" stroke-width="2.5"/>
    <text x="720" y="145" fill="#a855f7" font-family="Impact" font-size="22" text-anchor="middle">CORROSIVE (BLACK)</text>
    <text x="720" y="170" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">HP + SP EROSION</text>

    <rect x="870" y="90" width="180" height="120" rx="6" fill="#181505" stroke="#f1df76" stroke-width="2.5"/>
    <text x="960" y="145" fill="#f1df76" font-family="Impact" font-size="22" text-anchor="middle">PALE (EXTINCTION)</text>
    <text x="960" y="170" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">% MAX HP</text>
  </g>
  <text x="600" y="45" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="4" text-anchor="middle">SYSTEMS &amp; COMBAT CALCULATIONS</text>
  <text x="600" y="285" fill="#ef5b55" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">[ RESONANT CLASH FORMULAS // WORK AFFINITY // ORDEALS FRAMEWORK ]</text>
</svg>''',

    "banner_hero_factions_council.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300">
  <defs>
    <linearGradient id="bgFacs" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#12080a"/>
      <stop offset="50%" stop-color="#0c121e"/>
      <stop offset="100%" stop-color="#12080a"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="300" fill="url(#bgFacs)"/>
  <!-- Grand Rotunda Council Circle -->
  <circle cx="600" cy="150" r="110" fill="none" stroke="#f1df76" stroke-width="2" stroke-dasharray="10,6"/>
  <circle cx="600" cy="150" r="60" fill="#ef5b55" fill-opacity="0.25" stroke="#ef5b55" stroke-width="3"/>
  <polygon points="600,110 635,150 600,190 565,150" fill="#f1df76"/>
  
  <text x="180" y="150" fill="#ef5b55" font-family="Impact" font-size="22" text-anchor="middle">THE DIRECTORATE</text>
  <text x="180" y="175" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="middle">SUPREME GOVERNANCE</text>

  <text x="1020" y="150" fill="#38bdf8" font-family="Impact" font-size="22" text-anchor="middle">THE 4 GUILDS</text>
  <text x="1020" y="175" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="middle">ARCHITECTS • WEAVERS • WARDENS • COLLECTORS</text>

  <text x="600" y="45" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="4" text-anchor="middle">FACTIONS &amp; METROPOLITAN GUILDS</text>
  <text x="600" y="285" fill="#38bdf8" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">[ 14 CANONICAL POWERS // HIGH COUNCIL OF SIGHS // SYNDICATES ]</text>
</svg>''',

    "banner_hero_lore_absolvohan.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300">
  <defs>
    <linearGradient id="bgLore" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#14080c"/>
      <stop offset="50%" stop-color="#080c16"/>
      <stop offset="100%" stop-color="#14080c"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="300" fill="url(#bgLore)"/>
  <!-- Timeline Arc -->
  <path d="M100,200 Q600,50 1100,200" fill="none" stroke="#f1df76" stroke-width="3.5"/>
  <circle cx="100" cy="200" r="10" fill="#ef5b55"/>
  <circle cx="350" cy="125" r="10" fill="#38bdf8"/>
  <circle cx="600" cy="100" r="14" fill="#f1df76" stroke="#ffffff" stroke-width="3"/>
  <circle cx="850" cy="125" r="10" fill="#a855f7"/>
  <circle cx="1100" cy="200" r="10" fill="#10b981"/>

  <text x="100" y="235" fill="#ef5b55" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">DAY 0: RESET</text>
  <text x="350" y="105" fill="#38bdf8" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">CHEONGULA (3,892)</text>
  <text x="600" y="75" fill="#f1df76" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">1,778 CYCLES OF RESET</text>
  <text x="850" y="105" fill="#a855f7" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">TABOO CODE</text>
  <text x="1100" y="235" fill="#10b981" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">DAWN OF HOPE (4,238)</text>

  <text x="600" y="40" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="4" text-anchor="middle">LORE &amp; COSMOLOGICAL CHRONICLES</text>
  <text x="600" y="285" fill="#38bdf8" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">[ THE 9-PART ABSOLVOHAN SAGA // THE THREE SORROWS // THE ALPHA TREE ]</text>
</svg>'''
}

for bname, bcontent in banners.items():
    with open(os.path.join(BANNERS_DIR, bname), "w", encoding="utf-8") as f:
        f.write(bcontent)

print(f"Generated all {len(banners)} Category Hero Banners.")
