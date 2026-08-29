import os

HAND_BLUEPRINTS_DIR = "/home/user/01_Somnarak_Wiki/assets/layout/hand/blueprints"
CITY_BLUEPRINTS_DIR = "/home/user/01_Somnarak_Wiki/assets/layout/city/blueprints"

os.makedirs(HAND_BLUEPRINTS_DIR, exist_ok=True)
os.makedirs(CITY_BLUEPRINTS_DIR, exist_ok=True)

print("Generating Modular High-Resolution Map Cutaway SVGs...")

# =========================================================================
# THE HAND OF CHANGE CUTAWAYS (1600x900)
# =========================================================================

# Cut 1: Upper Command & Containment Ward (Floors 1 & 2)
hand_cut_1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900">
  <defs>
    <linearGradient id="bgH1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070c18"/>
      <stop offset="100%" stop-color="#020408"/>
    </linearGradient>
    <pattern id="gridH1" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#16253b" stroke-width="0.8"/>
    </pattern>
  </defs>
  <rect width="1600" height="900" fill="url(#bgH1)"/>
  <rect width="1600" height="900" fill="url(#gridH1)"/>

  <!-- Master Title Block -->
  <rect x="40" y="30" width="1520" height="70" rx="6" fill="#0d1829" stroke="#ef5b55" stroke-width="2.5"/>
  <text x="65" y="72" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="2">FACILITY 01 // SECTOR CUT 01: UPPER COMMAND &amp; CONTAINMENT WARD</text>
  <text x="1530" y="72" fill="#ef5b55" font-family="monospace" font-size="14" font-weight="bold" text-anchor="end">[ FLOORS 1 &amp; 2: NEUTRAL COMMAND &amp; MAW'S KEEP ]</text>

  <!-- FLOOR 1: NEUTRAL COMMAND (Y: 130 to 480) -->
  <rect x="40" y="130" width="1520" height="340" rx="8" fill="#0b1322" stroke="#ef5b55" stroke-width="2"/>
  <rect x="40" y="130" width="280" height="40" fill="#ef5b55"/>
  <text x="55" y="156" fill="#ffffff" font-family="Impact" font-size="18" letter-spacing="1">FLOOR 1: NEUTRAL COMMAND</text>
  <text x="340" y="156" fill="#f1df76" font-family="monospace" font-size="13">LEAD: DIRECTOR MAJIN // ELEVATION: -50M</text>

  <!-- Floor 1 Rooms -->
  <!-- Room 1: Director's Office -->
  <rect x="70" y="190" width="320" height="250" rx="4" fill="#060a12" stroke="#ef5b55" stroke-width="1.5"/>
  <text x="90" y="225" fill="#f1df76" font-family="Impact" font-size="18">01-A: DIRECTOR'S OFFICE</text>
  <text x="90" y="250" fill="#94a3b8" font-family="monospace" font-size="11">Executive Command &amp; Reset Terminal</text>
  <circle cx="230" cy="320" r="40" fill="#ef5b55" fill-opacity="0.2" stroke="#ef5b55" stroke-width="2"/>
  <text x="230" y="326" fill="#ffffff" font-family="monospace" font-size="11" text-anchor="middle">RESET DIAL</text>

  <!-- Room 2: Central Observation Deck -->
  <rect x="420" y="190" width="480" height="250" rx="4" fill="#060a12" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="440" y="225" fill="#38bdf8" font-family="Impact" font-size="18">01-B: MAIN OBSERVATION HUB</text>
  <text x="440" y="250" fill="#94a3b8" font-family="monospace" font-size="11">Multi-Screen Containment Oversight Matrix</text>
  <line x1="440" y1="320" x2="880" y2="320" stroke="#1e2e46" stroke-width="6"/>
  <circle cx="500" cy="320" r="10" fill="#10b981"/>
  <circle cx="660" cy="320" r="10" fill="#f1df76"/>
  <circle cx="820" cy="320" r="10" fill="#ef5b55"/>
  <text x="660" y="380" fill="#cbd5e1" font-family="monospace" font-size="12" text-anchor="middle">LIVE QLIPHOTH SENSOR CONSOLE</text>

  <!-- Room 3: Main Power & Decon Airlocks -->
  <rect x="930" y="190" width="600" height="250" rx="4" fill="#060a12" stroke="#f1df76" stroke-width="1.5"/>
  <text x="950" y="225" fill="#f1df76" font-family="Impact" font-size="18">01-C: SE-001 ISOLATION VAULT</text>
  <text x="950" y="250" fill="#94a3b8" font-family="monospace" font-size="11">Containment Chamber: The Orphaned Bell (T-01 CAN)</text>
  <polygon points="1230,270 1280,360 1180,360" fill="#10b981" fill-opacity="0.3" stroke="#10b981" stroke-width="2.5"/>
  <circle cx="1230" cy="320" r="16" fill="#f1df76"/>
  <text x="1230" y="395" fill="#10b981" font-family="Impact" font-size="15" text-anchor="middle">ACOUSTIC DAMPENER ACTIVE</text>

  <!-- FLOOR 2: MAW'S KEEP (Y: 500 to 860) -->
  <rect x="40" y="500" width="1520" height="360" rx="8" fill="#091022" stroke="#5b75e8" stroke-width="2"/>
  <rect x="40" y="500" width="280" height="40" fill="#5b75e8"/>
  <text x="55" y="526" fill="#ffffff" font-family="Impact" font-size="18" letter-spacing="1">FLOOR 2: MAW'S KEEP</text>
  <text x="340" y="526" fill="#38bdf8" font-family="monospace" font-size="13">LEAD: DEKAN // ELEVATION: -140M // HEAVY CONTAINMENT</text>

  <!-- Floor 2 Chambers -->
  <rect x="70" y="560" width="460" height="270" rx="4" fill="#050812" stroke="#5b75e8" stroke-width="1.5"/>
  <text x="90" y="595" fill="#5b75e8" font-family="Impact" font-size="18">02-A: SE-002 VAULT (COLOSSUS)</text>
  <text x="90" y="620" fill="#94a3b8" font-family="monospace" font-size="11">Basalt Monolith Chamber // Risk: T-02 TETH</text>
  <rect x="220" y="650" width="160" height="140" fill="#5b75e8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2"/>
  <text x="300" y="725" fill="#ffffff" font-family="Impact" font-size="16" text-anchor="middle">KINETIC SEALS</text>

  <rect x="560" y="560" width="460" height="270" rx="4" fill="#050812" stroke="#f1df76" stroke-width="1.5"/>
  <text x="580" y="595" fill="#f1df76" font-family="Impact" font-size="18">02-B: SE-005 VAULT (SMOTHERING MOTHER)</text>
  <text x="580" y="620" fill="#94a3b8" font-family="monospace" font-size="11">Mourning Silk Enclosure // Risk: T-03 HE</text>
  <circle cx="790" cy="710" r="55" fill="#f1df76" fill-opacity="0.2" stroke="#f1df76" stroke-width="2"/>
  <text x="790" y="716" fill="#ffffff" font-family="Impact" font-size="14" text-anchor="middle">SILK WEAVE SHIELD</text>

  <rect x="1050" y="560" width="480" height="270" rx="4" fill="#050812" stroke="#ef5b55" stroke-width="1.5"/>
  <text x="1070" y="595" fill="#ef5b55" font-family="Impact" font-size="18">02-C: RAPID RESPONSE GARRISON</text>
  <text x="1070" y="620" fill="#94a3b8" font-family="monospace" font-size="11">Dekan Heavy Riot Staging &amp; Kinetic Ammo</text>
  <rect x="1140" y="660" width="300" height="120" fill="#1a0a10" stroke="#ef5b55" stroke-width="2"/>
  <text x="1290" y="725" fill="#ef5b55" font-family="Impact" font-size="16" text-anchor="middle">RIOT BREACH SQUAD</text>
</svg>'''

with open(os.path.join(HAND_BLUEPRINTS_DIR, "the_hand_cut_1_upper_command.svg"), "w", encoding="utf-8") as f:
    f.write(hand_cut_1)

# Cut 2: Siphon Forge & Research Laboratories (Floors 3 & 4)
hand_cut_2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900">
  <defs>
    <linearGradient id="bgH2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141106"/>
      <stop offset="100%" stop-color="#050f09"/>
    </linearGradient>
  </defs>
  <rect width="1600" height="900" fill="url(#bgH2)"/>
  <rect x="40" y="30" width="1520" height="70" rx="6" fill="#181507" stroke="#e6c843" stroke-width="2.5"/>
  <text x="65" y="72" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="2">FACILITY 01 // SECTOR CUT 02: EXTRACTION HALL &amp; INSIGHT FORGE</text>
  <text x="1530" y="72" fill="#e6c843" font-family="monospace" font-size="14" font-weight="bold" text-anchor="end">[ FLOORS 3 &amp; 4: SIPHON FORGE &amp; RESEARCH CORE ]</text>

  <!-- FLOOR 3: EXTRACTION HALL -->
  <rect x="40" y="130" width="1520" height="340" rx="8" fill="#141005" stroke="#e6c843" stroke-width="2"/>
  <rect x="40" y="130" width="280" height="40" fill="#e6c843"/>
  <text x="55" y="156" fill="#000000" font-family="Impact" font-size="18">FLOOR 3: EXTRACTION HALL</text>
  <text x="340" y="156" fill="#f1df76" font-family="monospace" font-size="13">LEAD: ZYRAK // AGONY SIPHON &amp; M.A.W. FOUNDRIES</text>

  <rect x="70" y="190" width="460" height="250" rx="4" fill="#080602" stroke="#e6c843" stroke-width="1.5"/>
  <text x="90" y="225" fill="#f1df76" font-family="Impact" font-size="18">03-A: AGONY SMELTING CRUCIBLE</text>
  <circle cx="300" cy="330" r="60" fill="#e6c843" fill-opacity="0.25" stroke="#f1df76" stroke-width="3"/>
  <text x="300" y="336" fill="#ffffff" font-family="Impact" font-size="16" text-anchor="middle">MOLTEN HAN (1,400°C)</text>

  <rect x="560" y="190" width="460" height="250" rx="4" fill="#080602" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="580" y="225" fill="#38bdf8" font-family="Impact" font-size="18">03-B: M.A.W. WEAPON SMITHY</text>
  <line x1="680" y1="280" x2="900" y2="380" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
  <line x1="900" y1="280" x2="680" y2="380" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
  <text x="790" y="415" fill="#38bdf8" font-family="monospace" font-size="12" text-anchor="middle">RESONANCE TUNING ANVIL</text>

  <rect x="1050" y="190" width="480" height="250" rx="4" fill="#080602" stroke="#10b981" stroke-width="1.5"/>
  <text x="1070" y="225" fill="#10b981" font-family="Impact" font-size="18">03-C: SUIT &amp; GIFT SYNAPSE LOOM</text>
  <rect x="1150" y="270" width="280" height="120" fill="#0c1810" stroke="#10b981" stroke-width="2"/>
  <text x="1290" y="335" fill="#f1df76" font-family="Impact" font-size="15" text-anchor="middle">VEIL WEAVING SPINDLE</text>

  <!-- FLOOR 4: INSIGHT FORGE -->
  <rect x="40" y="500" width="1520" height="360" rx="8" fill="#06160d" stroke="#47c978" stroke-width="2"/>
  <rect x="40" y="500" width="280" height="40" fill="#47c978"/>
  <text x="55" y="526" fill="#000000" font-family="Impact" font-size="18">FLOOR 4: INSIGHT FORGE</text>
  <text x="340" y="526" fill="#47c978" font-family="monospace" font-size="13">LEAD: AYSHUK // METAPHYSICAL ALCHEMY &amp; COGNITIVE MAPPING</text>

  <rect x="70" y="560" width="460" height="270" rx="4" fill="#030c07" stroke="#47c978" stroke-width="1.5"/>
  <text x="90" y="595" fill="#47c978" font-family="Impact" font-size="18">04-A: SE-007 VAULT (BRUME)</text>
  <circle cx="300" cy="710" r="60" fill="#47c978" fill-opacity="0.2" stroke="#47c978" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="300" y="716" fill="#ffffff" font-family="Impact" font-size="15" text-anchor="middle">VAPOR DISTILLER</text>

  <rect x="560" y="560" width="460" height="270" rx="4" fill="#030c07" stroke="#a855f7" stroke-width="1.5"/>
  <text x="580" y="595" fill="#a855f7" font-family="Impact" font-size="18">04-B: SE-009 VAULT (MEMORY WEAVER)</text>
  <polygon points="790,640 860,710 790,780 720,710" fill="#a855f7" fill-opacity="0.25" stroke="#a855f7" stroke-width="2"/>
  <text x="790" y="716" fill="#ffffff" font-family="Impact" font-size="14" text-anchor="middle">CRYSTAL SPINNERET</text>

  <rect x="1050" y="560" width="480" height="270" rx="4" fill="#030c07" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="1070" y="595" fill="#38bdf8" font-family="Impact" font-size="18">04-C: HAN ALCHEMY DISTILLERY</text>
  <circle cx="1290" cy="710" r="50" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2"/>
  <text x="1290" y="716" fill="#f1df76" font-family="Impact" font-size="15" text-anchor="middle">PURIFIED EXTRACT 99.8%</text>
</svg>'''

with open(os.path.join(HAND_BLUEPRINTS_DIR, "the_hand_cut_2_industrial_core.svg"), "w", encoding="utf-8") as f:
    f.write(hand_cut_2)

# Cut 3: Defense Bastion & Cryo Vault (Floors 5 & 6)
hand_cut_3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900">
  <defs>
    <linearGradient id="bgH3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#121418"/>
      <stop offset="100%" stop-color="#1a060c"/>
    </linearGradient>
  </defs>
  <rect width="1600" height="900" fill="url(#bgH3)"/>
  <rect x="40" y="30" width="1520" height="70" rx="6" fill="#1a1c22" stroke="#d4d4d8" stroke-width="2.5"/>
  <text x="65" y="72" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="2">FACILITY 01 // SECTOR CUT 03: BORDER DEFENSE &amp; DEEP CRYO VAULT</text>
  <text x="1530" y="72" fill="#d4d4d8" font-family="monospace" font-size="14" font-weight="bold" text-anchor="end">[ FLOORS 5 &amp; 6: BORDER WATCH &amp; DEEP VAULT ]</text>

  <!-- FLOOR 5: BORDER WATCH -->
  <rect x="40" y="130" width="1520" height="340" rx="8" fill="#14171d" stroke="#d4d4d8" stroke-width="2"/>
  <rect x="40" y="130" width="280" height="40" fill="#d4d4d8"/>
  <text x="55" y="156" fill="#000000" font-family="Impact" font-size="18">FLOOR 5: BORDER WATCH</text>
  <text x="340" y="156" fill="#d4d4d8" font-family="monospace" font-size="13">LEAD: MELLDA // PERIMETER DEFENSE &amp; SE-011</text>

  <rect x="70" y="190" width="460" height="250" rx="4" fill="#090a0d" stroke="#d4d4d8" stroke-width="1.5"/>
  <text x="90" y="225" fill="#f1df76" font-family="Impact" font-size="18">05-A: SUBTERRANEAN BULWARK</text>
  <rect x="130" y="260" width="340" height="130" fill="#1e222a" stroke="#d4d4d8" stroke-width="2"/>
  <text x="300" y="330" fill="#ffffff" font-family="Impact" font-size="16" text-anchor="middle">TITANIUM SHIELD GARRISON</text>

  <rect x="560" y="190" width="460" height="250" rx="4" fill="#090a0d" stroke="#f1df76" stroke-width="1.5"/>
  <text x="580" y="225" fill="#f1df76" font-family="Impact" font-size="18">05-B: SE-011 (WHISPERING WALLS)</text>
  <circle cx="790" cy="330" r="55" fill="#f1df76" fill-opacity="0.2" stroke="#f1df76" stroke-width="2"/>
  <text x="790" y="336" fill="#ffffff" font-family="Impact" font-size="14" text-anchor="middle">VOCAL CHORD BULWARK</text>

  <rect x="1050" y="190" width="480" height="250" rx="4" fill="#090a0d" stroke="#ef5b55" stroke-width="1.5"/>
  <text x="1070" y="225" fill="#ef5b55" font-family="Impact" font-size="18">05-C: AUTOMATED TURRET BATTERY</text>
  <circle cx="1290" cy="330" r="45" fill="#ef5b55" fill-opacity="0.2" stroke="#ef5b55" stroke-width="2"/>
  <text x="1290" y="336" fill="#ef5b55" font-family="Impact" font-size="14" text-anchor="middle">AUTO-CANNON ARRAY</text>

  <!-- FLOOR 6: DEEP VAULT -->
  <rect x="40" y="500" width="1520" height="360" rx="8" fill="#1a080f" stroke="#be123c" stroke-width="2"/>
  <rect x="40" y="500" width="280" height="40" fill="#be123c"/>
  <text x="55" y="526" fill="#ffffff" font-family="Impact" font-size="18">FLOOR 6: DEEP VAULT</text>
  <text x="340" y="526" fill="#be123c" font-family="monospace" font-size="13">LEAD: MARJUK // CRYO ARCHIVES &amp; SE-010 THE CONVERGENCE</text>

  <rect x="70" y="560" width="680" height="270" rx="4" fill="#0d0307" stroke="#ef4444" stroke-width="2"/>
  <text x="90" y="595" fill="#ef4444" font-family="Impact" font-size="20">06-A: SE-010 THE CONVERGENCE (T-05 ALEPH)</text>
  <polygon points="410,640 480,710 410,780 340,710" fill="#ef4444" fill-opacity="0.4" stroke="#ffffff" stroke-width="3"/>
  <circle cx="410" cy="710" r="22" fill="#000000" stroke="#f1df76" stroke-width="2"/>
  <text x="410" y="810" fill="#ef4444" font-family="Impact" font-size="16" text-anchor="middle">CRITICAL SINGULARITY STASIS MATRIX</text>

  <rect x="780" y="560" width="750" height="270" rx="4" fill="#0d0307" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="800" y="595" fill="#38bdf8" font-family="Impact" font-size="18">06-B: PRE-CATACLYSM CRYO ARCHIVE VAULTS</text>
  <rect x="850" y="650" width="120" height="140" fill="#06131f" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="910" y="725" fill="#38bdf8" font-family="monospace" font-size="11" text-anchor="middle">POD 01-44</text>
  <rect x="1000" y="650" width="120" height="140" fill="#06131f" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="1060" y="725" fill="#38bdf8" font-family="monospace" font-size="11" text-anchor="middle">POD 45-88</text>
  <rect x="1150" y="650" width="120" height="140" fill="#06131f" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="1210" y="725" fill="#38bdf8" font-family="monospace" font-size="11" text-anchor="middle">POD 89-132</text>
  <rect x="1300" y="650" width="120" height="140" fill="#06131f" stroke="#f1df76" stroke-width="2"/>
  <text x="1360" y="725" fill="#f1df76" font-family="monospace" font-size="11" text-anchor="middle">RESET LOGS</text>
</svg>'''

with open(os.path.join(HAND_BLUEPRINTS_DIR, "the_hand_cut_3_defense_vault.svg"), "w", encoding="utf-8") as f:
    f.write(hand_cut_3)

# Cut 4: Void Docks & The Taboo Gate (Floors 7 & 8)
hand_cut_4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900">
  <defs>
    <linearGradient id="bgH4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1c0615"/>
      <stop offset="100%" stop-color="#181204"/>
    </linearGradient>
  </defs>
  <rect width="1600" height="900" fill="url(#bgH4)"/>
  <rect x="40" y="30" width="1520" height="70" rx="6" fill="#200a18" stroke="#fbbf24" stroke-width="2.5"/>
  <text x="65" y="72" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="2">FACILITY 01 // SECTOR CUT 04: VOID DIVING DOCKS &amp; THE TABOO GATE</text>
  <text x="1530" y="72" fill="#fbbf24" font-family="monospace" font-size="14" font-weight="bold" text-anchor="end">[ FLOORS 7 &amp; 8: SHADOW CORPS &amp; GATE WATCH ]</text>

  <!-- FLOOR 7: SHADOW CORPS -->
  <rect x="40" y="130" width="1520" height="340" rx="8" fill="#180714" stroke="#f43f5e" stroke-width="2"/>
  <rect x="40" y="130" width="280" height="40" fill="#f43f5e"/>
  <text x="55" y="156" fill="#ffffff" font-family="Impact" font-size="18">FLOOR 7: SHADOW CORPS</text>
  <text x="340" y="156" fill="#f43f5e" font-family="monospace" font-size="13">LEAD: ISHALL // VOID DOCKING SUBMARINES &amp; SE-014</text>

  <rect x="70" y="190" width="460" height="250" rx="4" fill="#0d030a" stroke="#f43f5e" stroke-width="1.5"/>
  <text x="90" y="225" fill="#f43f5e" font-family="Impact" font-size="18">07-A: VOID DIVER SUB-DOCK 01</text>
  <ellipse cx="300" cy="330" rx="90" ry="40" fill="#f43f5e" fill-opacity="0.25" stroke="#ffffff" stroke-width="2"/>
  <text x="300" y="336" fill="#ffffff" font-family="Impact" font-size="15" text-anchor="middle">SUBMERSIBLE 'ABYSS-09'</text>

  <rect x="560" y="190" width="460" height="250" rx="4" fill="#0d030a" stroke="#a855f7" stroke-width="1.5"/>
  <text x="580" y="225" fill="#a855f7" font-family="Impact" font-size="18">07-B: SE-014 VAULT (DEBT EATER)</text>
  <rect x="700" y="270" width="180" height="120" fill="#14061a" stroke="#a855f7" stroke-width="2"/>
  <text x="790" y="335" fill="#f1df76" font-family="Impact" font-size="16" text-anchor="middle">PORCELAIN FURNACE</text>

  <rect x="1050" y="190" width="480" height="250" rx="4" fill="#0d030a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="1070" y="225" fill="#38bdf8" font-family="Impact" font-size="18">07-C: NEURAL DIVER STABILIZATION</text>
  <circle cx="1290" cy="330" r="50" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2"/>
  <text x="1290" y="336" fill="#38bdf8" font-family="Impact" font-size="14" text-anchor="middle">SANITY ANCHOR GRID</text>

  <!-- FLOOR 8: GATE WATCH -->
  <rect x="40" y="500" width="1520" height="360" rx="8" fill="#1a1205" stroke="#fbbf24" stroke-width="2"/>
  <rect x="40" y="500" width="280" height="40" fill="#fbbf24"/>
  <text x="55" y="526" fill="#000000" font-family="Impact" font-size="18">FLOOR 8: GATE WATCH</text>
  <text x="340" y="526" fill="#fbbf24" font-family="monospace" font-size="13">LEAD: XYAN // THE COSMIC TABOO THRESHOLD &amp; SE-015</text>

  <rect x="70" y="560" width="600" height="270" rx="4" fill="#0d0a02" stroke="#f1df76" stroke-width="2"/>
  <text x="90" y="595" fill="#f1df76" font-family="Impact" font-size="20">08-A: SE-015 (THE DEBT SCALE)</text>
  <circle cx="370" cy="710" r="60" fill="#f1df76" fill-opacity="0.2" stroke="#f1df76" stroke-width="3"/>
  <line x1="320" y1="710" x2="420" y2="710" stroke="#ffffff" stroke-width="4"/>
  <circle cx="320" cy="730" r="14" fill="#ef5b55"/>
  <circle cx="420" cy="690" r="14" fill="#38bdf8"/>
  <text x="370" y="810" fill="#f1df76" font-family="Impact" font-size="15" text-anchor="middle">SOUL BALANCE APERTURE</text>

  <rect x="700" y="560" width="830" height="270" rx="4" fill="#0d0a02" stroke="#ef5b55" stroke-width="3"/>
  <text x="720" y="595" fill="#ef5b55" font-family="Impact" font-size="22">08-B: THE ABSOLUTE TABOO GATE (FINAL BOUNDARY)</text>
  <!-- Cosmic Gate Graphic -->
  <circle cx="1115" cy="710" r="75" fill="#050005" stroke="#fbbf24" stroke-width="4" stroke-dasharray="10,5"/>
  <polygon points="1115,645 1175,710 1115,775 1055,710" fill="#ef5b55" fill-opacity="0.4" stroke="#ffffff" stroke-width="3"/>
  <circle cx="1115" cy="710" r="16" fill="#ffffff"/>
  <text x="1115" y="815" fill="#ef5b55" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">[ WARNING: CONTACT WITH VOID THRESHOLD CAUSES TOTAL ERASURE ]</text>
</svg>'''

with open(os.path.join(HAND_BLUEPRINTS_DIR, "the_hand_cut_4_abyss_gate.svg"), "w", encoding="utf-8") as f:
    f.write(hand_cut_4)

print("Generated 4 Hand of Change High-Res Sector Cutaways.")

# =========================================================================
# SOMNARAK CITY ATLAS CUTAWAYS (1600x900)
# =========================================================================

# Cut 1: Metropolitan Core (Zone A & B)
city_cut_1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900">
  <defs>
    <linearGradient id="bgC1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#040a14"/>
      <stop offset="100%" stop-color="#020408"/>
    </linearGradient>
  </defs>
  <rect width="1600" height="900" fill="url(#bgC1)"/>
  <rect x="40" y="30" width="1520" height="70" rx="6" fill="#081426" stroke="#ef5b55" stroke-width="2.5"/>
  <text x="65" y="72" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="2">SOMNARAK URBAN ATLAS // CUT 01: METROPOLITAN CORE &amp; WEST WARD</text>
  <text x="1530" y="72" fill="#ef5b55" font-family="monospace" font-size="14" font-weight="bold" text-anchor="end">[ ZONE A: CORE NEXUS &amp; ZONE B: WEST WARD ]</text>

  <!-- ZONE A: CORE NEXUS -->
  <rect x="40" y="130" width="740" height="730" rx="8" fill="#081020" stroke="#ef5b55" stroke-width="2"/>
  <rect x="40" y="130" width="260" height="40" fill="#ef5b55"/>
  <text x="55" y="156" fill="#ffffff" font-family="Impact" font-size="18">ZONE A: CORE NEXUS</text>
  <text x="320" y="156" fill="#f1df76" font-family="monospace" font-size="13">SPIRE OF SIGHS // ALPHA TREE ROOTWELLS</text>

  <circle cx="410" cy="460" r="180" fill="#ef5b55" fill-opacity="0.15" stroke="#f1df76" stroke-width="3"/>
  <polygon points="410,310 440,540 380,540" fill="#0d1f38" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="410" cy="300" r="14" fill="#ef5b55"/>
  <text x="410" y="600" fill="#f1df76" font-family="Impact" font-size="20" text-anchor="middle">DIRECTORATE COMMAND SPIRE</text>
  <text x="410" y="630" fill="#cbd5e1" font-family="monospace" font-size="12" text-anchor="middle">ALPHA TREE ROOT CONDUITS // 100% HAN DENSITY</text>

  <!-- ZONE B: WEST WARD -->
  <rect x="820" y="130" width="740" height="730" rx="8" fill="#06121f" stroke="#38bdf8" stroke-width="2"/>
  <rect x="820" y="130" width="260" height="40" fill="#38bdf8"/>
  <text x="835" y="156" fill="#000000" font-family="Impact" font-size="18">ZONE B: WEST WARD</text>
  <text x="1100" y="156" fill="#38bdf8" font-family="monospace" font-size="13">RESIDENTIAL MEGA-BLOCKS // POP: 420,000</text>

  <!-- Residential Blocks -->
  <g fill="#0b1e33" stroke="#38bdf8" stroke-width="1.5">
    <rect x="860" y="220" width="140" height="180" rx="4"/>
    <rect x="1030" y="220" width="140" height="180" rx="4"/>
    <rect x="1200" y="220" width="140" height="180" rx="4"/>
    <rect x="1370" y="220" width="140" height="180" rx="4"/>

    <rect x="860" y="440" width="140" height="180" rx="4"/>
    <rect x="1030" y="440" width="140" height="180" rx="4"/>
    <rect x="1200" y="440" width="140" height="180" rx="4"/>
    <rect x="1370" y="440" width="140" height="180" rx="4"/>
  </g>
  <text x="1190" y="670" fill="#38bdf8" font-family="Impact" font-size="20" text-anchor="middle">ATMOSPHERIC VEIL FILTRATION DOME</text>
  <text x="1190" y="700" fill="#cbd5e1" font-family="monospace" font-size="12" text-anchor="middle">CIVILIAN RATIONING TERMINALS &amp; MEMORY DISPENSARIES</text>
</svg>'''

with open(os.path.join(CITY_BLUEPRINTS_DIR, "city_cut_1_core_and_west.svg"), "w", encoding="utf-8") as f:
    f.write(city_cut_1)

# Cut 2: Industrial East & Relic Bazaars (Zone C & D)
city_cut_2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900">
  <defs>
    <linearGradient id="bgC2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#04120a"/>
      <stop offset="100%" stop-color="#020805"/>
    </linearGradient>
  </defs>
  <rect width="1600" height="900" fill="url(#bgC2)"/>
  <rect x="40" y="30" width="1520" height="70" rx="6" fill="#081e11" stroke="#10b981" stroke-width="2.5"/>
  <text x="65" y="72" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="2">SOMNARAK URBAN ATLAS // CUT 02: COLLECTOR'S ROW &amp; FORGE GARDENS</text>
  <text x="1530" y="72" fill="#10b981" font-family="monospace" font-size="14" font-weight="bold" text-anchor="end">[ ZONE C: EAST SCRAP &amp; ZONE D: R&amp;D FLANKS ]</text>

  <!-- ZONE C -->
  <rect x="40" y="130" width="740" height="730" rx="8" fill="#06180e" stroke="#10b981" stroke-width="2"/>
  <rect x="40" y="130" width="280" height="40" fill="#10b981"/>
  <text x="55" y="156" fill="#000000" font-family="Impact" font-size="18">ZONE C: COLLECTOR'S ROW</text>
  <text x="340" y="156" fill="#10b981" font-family="monospace" font-size="13">RELIC BAZAARS &amp; HAN SCRAP FOUNDRIES</text>

  <rect x="80" y="210" width="660" height="580" rx="6" fill="#030d07" stroke="#10b981" stroke-width="1.5"/>
  <text x="410" y="260" fill="#f1df76" font-family="Impact" font-size="22" text-anchor="middle">PRE-CATACLYSM BLACK MARKET MATRIX</text>
  <circle cx="250" cy="420" r="70" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="2"/>
  <text x="250" y="426" fill="#ffffff" font-family="Impact" font-size="15" text-anchor="middle">BAZAAR 01</text>
  <circle cx="550" cy="420" r="70" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="2"/>
  <text x="550" y="426" fill="#ffffff" font-family="Impact" font-size="15" text-anchor="middle">BAZAAR 02</text>
  <rect x="180" y="550" width="460" height="180" fill="#081c10" stroke="#f1df76" stroke-width="2"/>
  <text x="410" y="645" fill="#f1df76" font-family="Impact" font-size="18" text-anchor="middle">DOHA'S UNDERGROUND REFINERY</text>

  <!-- ZONE D -->
  <rect x="820" y="130" width="740" height="730" rx="8" fill="#04140b" stroke="#47c978" stroke-width="2"/>
  <rect x="820" y="130" width="280" height="40" fill="#47c978"/>
  <text x="835" y="156" fill="#000000" font-family="Impact" font-size="18">ZONE D: FORGE &amp; GARDENS</text>
  <text x="1120" y="156" fill="#47c978" font-family="monospace" font-size="13">HAN BOTANICAL GREENHOUSES &amp; RESEARCH</text>

  <rect x="860" y="210" width="660" height="580" rx="6" fill="#020a05" stroke="#47c978" stroke-width="1.5"/>
  <circle cx="1190" cy="460" r="160" fill="#47c978" fill-opacity="0.2" stroke="#47c978" stroke-width="3"/>
  <text x="1190" y="440" fill="#f1df76" font-family="Impact" font-size="22" text-anchor="middle">BIO-SYNTHETIC BOTANICAL DOME</text>
  <text x="1190" y="470" fill="#cbd5e1" font-family="monospace" font-size="12" text-anchor="middle">Cultivation of Han Flora &amp; Neural Sap Extraction</text>
  <text x="1190" y="660" fill="#47c978" font-family="Impact" font-size="18" text-anchor="middle">AYSHUK RESEARCH FOUNDRY EXTENSION</text>
</svg>'''

with open(os.path.join(CITY_BLUEPRINTS_DIR, "city_cut_2_industrial_east.svg"), "w", encoding="utf-8") as f:
    f.write(city_cut_2)

# Cut 3: Outer Bulwark & Wasteland Frontier (Zone E)
city_cut_3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900">
  <defs>
    <linearGradient id="bgC3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#140d04"/>
      <stop offset="100%" stop-color="#1a0404"/>
    </linearGradient>
  </defs>
  <rect width="1600" height="900" fill="url(#bgC3)"/>
  <rect x="40" y="30" width="1520" height="70" rx="6" fill="#201004" stroke="#f59e0b" stroke-width="2.5"/>
  <text x="65" y="72" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="2">SOMNARAK URBAN ATLAS // CUT 03: PERIMETER BULWARK &amp; THE DESOLATE</text>
  <text x="1530" y="72" fill="#f59e0b" font-family="monospace" font-size="14" font-weight="bold" text-anchor="end">[ ZONE E: 400M BATTLEMENTS &amp; WASTELAND FRONTIER ]</text>

  <!-- Left: 400m Wall Cutaway -->
  <rect x="40" y="130" width="740" height="730" rx="8" fill="#140e06" stroke="#f59e0b" stroke-width="2"/>
  <rect x="40" y="130" width="280" height="40" fill="#f59e0b"/>
  <text x="55" y="156" fill="#000000" font-family="Impact" font-size="18">ZONE E: PERIMETER BULWARK</text>
  <text x="340" y="156" fill="#f59e0b" font-family="monospace" font-size="13">TITANIUM CURTAIN WALL // 400M HEIGHT</text>

  <!-- Tower Schematics -->
  <rect x="100" y="220" width="180" height="540" fill="#1e1408" stroke="#f59e0b" stroke-width="2"/>
  <text x="190" y="480" fill="#f1df76" font-family="Impact" font-size="20" text-anchor="middle">WATCHTOWER 01</text>
  <rect x="360" y="280" width="360" height="480" fill="#1e1408" stroke="#f59e0b" stroke-width="2"/>
  <text x="540" y="480" fill="#ffffff" font-family="Impact" font-size="22" text-anchor="middle">GATE OF SIGHS (MAIN EXIT)</text>
  <text x="540" y="520" fill="#cbd5e1" font-family="monospace" font-size="12" text-anchor="middle">Wasteland Expedition Airlock</text>

  <!-- Right: The Desolate Frontiers -->
  <rect x="820" y="130" width="740" height="730" rx="8" fill="#180608" stroke="#ef4444" stroke-width="2"/>
  <rect x="820" y="130" width="280" height="40" fill="#ef4444"/>
  <text x="835" y="156" fill="#ffffff" font-family="Impact" font-size="18">THE DESOLATE (황무지)</text>
  <text x="1120" y="156" fill="#ef4444" font-family="monospace" font-size="13">RADIOACTIVE CRYSTALLINE WASTELAND</text>

  <circle cx="1190" cy="380" r="140" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="8,4"/>
  <text x="1190" y="375" fill="#f1df76" font-family="Impact" font-size="22" text-anchor="middle">HOLLOW GLASS SECTOR</text>
  <text x="1190" y="405" fill="#ffffff" font-family="monospace" font-size="12" text-anchor="middle">Vitrified Desert // Frozen Resonance</text>

  <rect x="880" y="580" width="620" height="200" rx="6" fill="#0d0305" stroke="#fbbf24" stroke-width="2"/>
  <text x="1190" y="660" fill="#fbbf24" font-family="Impact" font-size="20" text-anchor="middle">HORIZON CARAVAN DEPARTURE TRAIL</text>
  <text x="1190" y="695" fill="#cbd5e1" font-family="monospace" font-size="12" text-anchor="middle">Route to Cheonbulok Ruins &amp; Precursor Citadels</text>
</svg>'''

with open(os.path.join(CITY_BLUEPRINTS_DIR, "city_cut_3_perimeter_frontier.svg"), "w", encoding="utf-8") as f:
    f.write(city_cut_3)

# Cut 4: Subterranean Canal Grid & The Weeping
city_cut_4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900">
  <defs>
    <linearGradient id="bgC4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050a16"/>
      <stop offset="100%" stop-color="#020409"/>
    </linearGradient>
  </defs>
  <rect width="1600" height="900" fill="url(#bgC4)"/>
  <rect x="40" y="30" width="1520" height="70" rx="6" fill="#0a1226" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="65" y="72" fill="#f1df76" font-family="Impact" font-size="28" letter-spacing="2">SOMNARAK URBAN ATLAS // CUT 04: THE WEEPING &amp; SUB-RAIL GRID</text>
  <text x="1530" y="72" fill="#38bdf8" font-family="monospace" font-size="14" font-weight="bold" text-anchor="end">[ HYDROLOGICAL NETWORK &amp; UNDER-RAIL TRANSPORT ]</text>

  <!-- The Weeping River Channel -->
  <rect x="40" y="130" width="1520" height="730" rx="8" fill="#060c18" stroke="#38bdf8" stroke-width="2"/>
  
  <!-- Flowing Waterway Graphic -->
  <path d="M40,500 Q400,300 800,500 T1560,500 L1560,700 Q1200,900 800,700 T40,700 Z" fill="#0b243d" stroke="#38bdf8" stroke-width="3"/>
  <text x="800" y="615" fill="#f1df76" font-family="Impact" font-size="32" letter-spacing="3" text-anchor="middle">THE WEEPING (비탄의 강) // SUBTERRANEAN EFFLUENT ARTERY</text>

  <!-- Hydraulic Pylons & Filters -->
  <rect x="250" y="240" width="220" height="220" rx="6" fill="#091424" stroke="#f1df76" stroke-width="2"/>
  <text x="360" y="330" fill="#f1df76" font-family="Impact" font-size="18" text-anchor="middle">SIPHON STATION A-1</text>
  <text x="360" y="360" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="middle">Pumping to Floor 3</text>

  <rect x="690" y="240" width="220" height="220" rx="6" fill="#091424" stroke="#f1df76" stroke-width="2"/>
  <text x="800" y="330" fill="#f1df76" font-family="Impact" font-size="18" text-anchor="middle">SIPHON STATION B-4</text>
  <text x="800" y="360" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="middle">Pumping to Maw's Keep</text>

  <rect x="1130" y="240" width="220" height="220" rx="6" fill="#091424" stroke="#f1df76" stroke-width="2"/>
  <text x="1240" y="330" fill="#f1df76" font-family="Impact" font-size="18" text-anchor="middle">SIPHON STATION C-8</text>
  <text x="1240" y="360" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="middle">Pumping to Deep Vault</text>
</svg>'''

with open(os.path.join(CITY_BLUEPRINTS_DIR, "city_cut_4_subterranean_canals.svg"), "w", encoding="utf-8") as f:
    f.write(city_cut_4)

print("Generated 4 Somnarak City High-Res District Cutaways.")
