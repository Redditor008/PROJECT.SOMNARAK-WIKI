import os

# 1. Master The Hand of Change Architectural Schematic Icon (the_hand_dr_icon_styled.svg)
hand_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="100%" height="100%">
  <defs>
    <linearGradient id="handBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1424"/>
      <stop offset="40%" stop-color="#060a12"/>
      <stop offset="100%" stop-color="#020408"/>
    </linearGradient>
    <radialGradient id="coreGlow" cx="50%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.6"/>
      <stop offset="45%" stop-color="#f1df76" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="goldBeam" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f1df76"/>
      <stop offset="50%" stop-color="#ef5b55"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <filter id="hudGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Cybernetic Outer Chassis -->
  <rect x="6" y="6" width="228" height="228" rx="12" fill="url(#handBg)" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="12" y="12" width="216" height="216" rx="8" fill="none" stroke="#f1df76" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.6"/>

  <!-- Blueprint Background Grid -->
  <line x1="20" y1="60" x2="220" y2="60" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 2"/>
  <line x1="20" y1="110" x2="220" y2="110" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 2"/>
  <line x1="20" y1="160" x2="220" y2="160" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 2"/>
  <line x1="60" y1="20" x2="60" y2="220" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 2"/>
  <line x1="120" y1="20" x2="120" y2="220" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 2"/>
  <line x1="180" y1="20" x2="180" y2="220" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 2"/>

  <!-- Core Ambient Glow -->
  <circle cx="120" cy="110" r="90" fill="url(#coreGlow)"/>

  <!-- Surface Spire & Alpha Tree Interface (Top) -->
  <polygon points="108,18 132,18 126,38 114,38" fill="#1e293b" stroke="#f1df76" stroke-width="1.8"/>
  <line x1="120" y1="18" x2="120" y2="45" stroke="#f1df76" stroke-width="3" filter="url(#hudGlow)"/>
  <circle cx="120" cy="22" r="3.5" fill="#38bdf8"/>

  <!-- CENTRAL ELEVATOR / HAN FLUX AXIS CONDUIT -->
  <rect x="115" y="44" width="10" height="170" fill="#091322" stroke="#38bdf8" stroke-width="1.2"/>
  <line x1="120" y1="44" x2="120" y2="214" stroke="url(#goldBeam)" stroke-width="2.5" stroke-dasharray="6 3"/>

  <!-- ================= PALM SECTORS (UPPER COMPLEX) ================= -->
  <!-- Floor 1: Neutral Command (Director Majin) -->
  <g transform="translate(68, 44)">
    <rect width="104" height="20" rx="3" fill="#171204" stroke="#f1df76" stroke-width="1.8"/>
    <circle cx="10" cy="10" r="4" fill="#f1df76"/>
    <text x="52" y="14" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" text-anchor="middle">F1 · NEUTRAL CORE</text>
  </g>

  <!-- Floor 2: Maw\'s Keep (Lead Dekan) -->
  <g transform="translate(62, 68)">
    <rect width="116" height="22" rx="3" fill="#200608" stroke="#ef5b55" stroke-width="1.8"/>
    <polygon points="10,6 15,15 5,15" fill="#ef5b55"/>
    <text x="58" y="15" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" text-anchor="middle">F2 · MAW\'S KEEP</text>
  </g>

  <!-- Floor 3: Extraction Hall (Lead Zyrak) -->
  <g transform="translate(72, 94)">
    <rect width="96" height="20" rx="3" fill="#041a2e" stroke="#38bdf8" stroke-width="1.8"/>
    <rect x="7" y="6" width="7" height="7" fill="#38bdf8"/>
    <text x="48" y="14" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" text-anchor="middle">F3 · EXTRACTION</text>
  </g>

  <!-- Distribution Bus Header Line -->
  <line x1="28" y1="120" x2="212" y2="120" stroke="#f1df76" stroke-width="2.2" filter="url(#hudGlow)"/>
  <circle cx="28" cy="120" r="3" fill="#f1df76"/>
  <circle cx="212" cy="120" r="3" fill="#f1df76"/>

  <!-- ================= FINGER SHAFTS (LOWER COMPLEX) ================= -->
  <!-- Floor 4: Insight Forge (Lead Ayshuk) -->
  <g transform="translate(26, 126)">
    <rect width="38" height="66" rx="3" fill="#041e15" stroke="#71efaf" stroke-width="1.5"/>
    <rect x="6" y="8" width="26" height="12" fill="#073322" stroke="#71efaf" stroke-width="1"/>
    <text x="19" y="17" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">F4</text>
    <text x="19" y="38" fill="#a7f3d0" font-family="'JetBrains Mono', monospace" font-size="7" text-anchor="middle">INSIGHT</text>
    <text x="19" y="52" fill="#6ee7b7" font-family="'JetBrains Mono', monospace" font-size="6.5" text-anchor="middle">FORGE</text>
    <!-- Han conduit drops -->
    <line x1="19" y1="58" x2="19" y2="64" stroke="#71efaf" stroke-width="2"/>
  </g>

  <!-- Floor 5: Border Watch (Lead Mellda) -->
  <g transform="translate(70, 126)">
    <rect width="38" height="74" rx="3" fill="#082238" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="6" y="8" width="26" height="12" fill="#0c3252" stroke="#38bdf8" stroke-width="1"/>
    <text x="19" y="17" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">F5</text>
    <text x="19" y="40" fill="#bae6fd" font-family="'JetBrains Mono', monospace" font-size="7" text-anchor="middle">BORDER</text>
    <text x="19" y="56" fill="#7dd3fc" font-family="'JetBrains Mono', monospace" font-size="6.5" text-anchor="middle">WATCH</text>
    <line x1="19" y1="64" x2="19" y2="72" stroke="#38bdf8" stroke-width="2"/>
  </g>

  <!-- Floor 6: Deep Vault (Lead Marjuk) -->
  <g transform="translate(132, 126)">
    <rect width="38" height="74" rx="3" fill="#240838" stroke="#c084fc" stroke-width="1.5"/>
    <rect x="6" y="8" width="26" height="12" fill="#3b0d5c" stroke="#c084fc" stroke-width="1"/>
    <text x="19" y="17" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">F6</text>
    <text x="19" y="40" fill="#e9d5ff" font-family="'JetBrains Mono', monospace" font-size="7" text-anchor="middle">DEEP</text>
    <text x="19" y="56" fill="#d8b4fe" font-family="'JetBrains Mono', monospace" font-size="6.5" text-anchor="middle">VAULT</text>
    <line x1="19" y1="64" x2="19" y2="72" stroke="#c084fc" stroke-width="2"/>
  </g>

  <!-- Floor 7: Shadow Corps (Lead Ishall) -->
  <g transform="translate(176, 126)">
    <rect width="38" height="66" rx="3" fill="#2e050c" stroke="#ef5b55" stroke-width="1.5"/>
    <rect x="6" y="8" width="26" height="12" fill="#4a0a15" stroke="#ef5b55" stroke-width="1"/>
    <text x="19" y="17" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">F7</text>
    <text x="19" y="38" fill="#fecaca" font-family="'JetBrains Mono', monospace" font-size="7" text-anchor="middle">SHADOW</text>
    <text x="19" y="52" fill="#fca5a5" font-family="'JetBrains Mono', monospace" font-size="6.5" text-anchor="middle">CORPS</text>
    <line x1="19" y1="58" x2="19" y2="64" stroke="#ef5b55" stroke-width="2"/>
  </g>

  <!-- Floor 8: Lateral Gate Watch (Lead Xyan) -->
  <g transform="translate(182, 70)">
    <rect width="44" height="24" rx="3" fill="#0f172a" stroke="#f1df76" stroke-width="1.5"/>
    <text x="22" y="12" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">F8 GATE</text>
    <text x="22" y="21" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="6" text-anchor="middle">SEALED</text>
    <line x1="-4" y1="12" x2="0" y2="12" stroke="#f1df76" stroke-width="1.5" stroke-dasharray="2 1"/>
  </g>

  <!-- Subterranean Bedrock Base & Weeping Rift -->
  <polygon points="20,214 220,214 200,226 40,226" fill="#080e18" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="120" y="223" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" letter-spacing="1" text-anchor="middle">SUBTERRANEAN BEDROCK // THE WEEPING</text>
  
  <!-- Corner Tech HUD Marks -->
  <path d="M12,24 L24,12" stroke="#38bdf8" stroke-width="2"/>
  <path d="M228,24 L216,12" stroke="#38bdf8" stroke-width="2"/>
  <path d="M12,216 L24,228" stroke="#38bdf8" stroke-width="2"/>
  <path d="M228,216 L216,228" stroke="#38bdf8" stroke-width="2"/>
</svg>'''

# 2. Master Somnarak Metropolitan Radial Blueprint Icon (somnarak_city_icon.svg)
city_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="100%" height="100%">
  <defs>
    <radialGradient id="cityBgGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e1035"/>
      <stop offset="50%" stop-color="#0b0816"/>
      <stop offset="100%" stop-color="#020307"/>
    </radialGradient>
    <radialGradient id="treePulse" cx="50%" cy="50%" r="40%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.9"/>
      <stop offset="40%" stop-color="#38bdf8" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0"/>
    </radialGradient>
    <filter id="cityGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Outer Octagonal Boundary Frame -->
  <polygon points="40,8 200,8 232,40 232,200 200,232 40,232 8,200 8,40" fill="url(#cityBgGrad)" stroke="#c084fc" stroke-width="2.5"/>
  <polygon points="44,14 196,14 226,44 226,196 196,226 44,226 14,196 14,44" fill="none" stroke="#f1df76" stroke-width="1.2" stroke-dasharray="6 3" opacity="0.6"/>

  <!-- Radial Grid Spokes (The 8 Great Boulevards) -->
  <line x1="120" y1="14" x2="120" y2="226" stroke="#334155" stroke-width="1" stroke-dasharray="4 2"/>
  <line x1="14" y1="120" x2="226" y2="120" stroke="#334155" stroke-width="1" stroke-dasharray="4 2"/>
  <line x1="45" y1="45" x2="195" y2="195" stroke="#334155" stroke-width="1" stroke-dasharray="4 2"/>
  <line x1="195" y1="45" x2="45" y2="195" stroke="#334155" stroke-width="1" stroke-dasharray="4 2"/>

  <!-- 5 CONCENTRIC METROPOLITAN ZONES -->
  <!-- Zone E: Perimeter Bulwark & Outer Ramparts -->
  <circle cx="120" cy="120" r="96" fill="none" stroke="#fb923c" stroke-width="2" stroke-dasharray="10 4" opacity="0.8"/>
  <text x="120" y="32" fill="#fb923c" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="bold" letter-spacing="1" text-anchor="middle">ZONE E · BULWARK</text>

  <!-- Zone D: Industrial Flanks & Han Refineries -->
  <circle cx="120" cy="120" r="76" fill="rgba(113, 239, 175, 0.05)" stroke="#71efaf" stroke-width="1.8" stroke-dasharray="6 3"/>
  <text x="120" y="52" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="bold" letter-spacing="1" text-anchor="middle">ZONE D · FOUNDRY</text>

  <!-- Zone C: Commercial Ring & Auction Row -->
  <circle cx="120" cy="120" r="56" fill="rgba(56, 189, 248, 0.07)" stroke="#38bdf8" stroke-width="1.8"/>
  <text x="120" y="72" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="bold" letter-spacing="1" text-anchor="middle">ZONE C · COMMERCE</text>

  <!-- Zone B: Inner Residential Wards -->
  <circle cx="120" cy="120" r="38" fill="rgba(192, 132, 252, 0.1)" stroke="#c084fc" stroke-width="2"/>
  <text x="120" y="90" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="6.5" font-weight="bold" text-anchor="middle">ZONE B</text>

  <!-- Zone A: Central Spire & Directorate Core -->
  <circle cx="120" cy="120" r="22" fill="#2e1065" stroke="#f1df76" stroke-width="2.5" filter="url(#cityGlow)"/>

  <!-- Radiant Alpha Tree Spire (Axis Mundi) -->
  <circle cx="120" cy="120" r="16" fill="url(#treePulse)"/>
  <polygon points="120,104 125,120 120,128 115,120" fill="#f1df76"/>
  <circle cx="120" cy="120" r="5" fill="#ffffff" filter="url(#cityGlow)"/>

  <!-- 4 Great Outer Bastion Fortresses -->
  <rect x="112" y="10" width="16" height="12" rx="2" fill="#1e293b" stroke="#fb923c" stroke-width="1.5"/>
  <rect x="112" y="218" width="16" height="12" rx="2" fill="#1e293b" stroke="#fb923c" stroke-width="1.5"/>
  <rect x="10" y="112" width="12" height="16" rx="2" fill="#1e293b" stroke="#fb923c" stroke-width="1.5"/>
  <rect x="218" y="112" width="12" height="16" rx="2" fill="#1e293b" stroke="#fb923c" stroke-width="1.5"/>

  <!-- Compass Cardinal Accents -->
  <polygon points="120,2 124,10 116,10" fill="#f1df76"/>
  <polygon points="120,238 124,230 116,230" fill="#fb923c"/>
  <polygon points="2,120 10,116 10,124" fill="#fb923c"/>
  <polygon points="238,120 230,116 230,124" fill="#fb923c"/>

  <!-- HUD Telemetry Labels -->
  <text x="120" y="210" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="bold" letter-spacing="1" text-anchor="middle">SOMNARAK ATLAS // 5 ZONES</text>
</svg>'''

paths = [
    '/home/user/01_Somnarak_Wiki/assets/layout/hand/icons/the_hand_dr_icon_styled.svg',
    '/home/user/01_Somnarak_Wiki/assets/icons/the_hand_dr_icon_styled.svg',
    '/home/user/icons/the_hand_dr_icon_styled.svg',
]

for p in paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(hand_svg)
    print(f'Wrote {p}')

city_paths = [
    '/home/user/01_Somnarak_Wiki/assets/layout/city/icons/somnarak_city_icon.svg',
    '/home/user/01_Somnarak_Wiki/assets/layout/city/icons/somnarak_city_icon_styled.svg',
    '/home/user/01_Somnarak_Wiki/assets/layout/hand/icons/somnarak_city_icon.svg',
    '/home/user/01_Somnarak_Wiki/assets/icons/somnarak_city_icon.svg',
    '/home/user/01_Somnarak_Wiki/assets/icons/somnarak_city_icon_styled.svg',
    '/home/user/icons/somnarak_city_icon.svg',
    '/home/user/icons/somnarak_city_icon_styled.svg'
]

for p in city_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(city_svg)
    print(f'Wrote {p}')
