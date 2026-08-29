import os

extra_entities = {
    'se-004': {
        'name': 'The Rust-Bleeding Sentry',
        'code': 'SE-004',
        'risk': 'MORPHEAN',
        'risk_badge': 'risk-MORPHEAN',
        'dmg': 'GRUDGE (Physical)',
        'color': '#ef5b55',
        'sub_color': '#f97316',
        'profile': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="pGrad_004" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#431407" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#1c0702" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#050201" stop-opacity="1"/>
    </radialGradient>
    <filter id="pGlow_004" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="500" height="500" rx="8" fill="url(#pGrad_004)" stroke="#f97316" stroke-width="3"/>
  <rect x="15" y="15" width="470" height="470" rx="4" fill="none" stroke="#ef5b55" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.6"/>

  <g filter="url(#pGlow_004)">
    <!-- Cogwheel Helmet Halo -->
    <circle cx="250" cy="200" r="130" fill="none" stroke="#f97316" stroke-width="3" stroke-dasharray="16 8"/>
    
    <!-- Iron Knight Sentinel Visor & Horns -->
    <polygon points="180,100 250,50 320,100 330,220 250,300 170,220" fill="#1e293b" stroke="#ef5b55" stroke-width="3.5"/>
    
    <!-- Slit Eye Visor Weeping Oxidized Rust Sludge -->
    <rect x="200" y="160" width="100" height="14" rx="3" fill="#450a0a" stroke="#f97316" stroke-width="2"/>
    <line x1="205" y1="167" x2="295" y2="167" stroke="#ef5b55" stroke-width="3"/>
    <path d="M220,174 L215,260" stroke="#f97316" stroke-width="3.5" stroke-linecap="round"/>
    <path d="M280,174 L285,260" stroke="#f97316" stroke-width="3.5" stroke-linecap="round"/>
    
    <!-- Crossed Halberd Blades Behind -->
    <line x1="100" y1="360" x2="400" y2="60" stroke="#94a3b8" stroke-width="6"/>
    <polygon points="380,40 420,40 400,80" fill="#f97316"/>
  </g>

  <!-- HUD Footer -->
  <rect x="30" y="440" width="440" height="36" rx="4" fill="#030712" stroke="#f97316" stroke-width="1.5"/>
  <text x="45" y="463" fill="#f97316" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">SE-004 // RUST-BLEEDING SENTRY</text>
  <text x="455" y="463" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">MORPHEAN · GRUDGE</text>
</svg>''',
        'banner': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bGrad_004" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#431407"/>
      <stop offset="50%" stop-color="#1c0702"/>
      <stop offset="100%" stop-color="#050201"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#bGrad_004)"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#f97316" stroke-width="3"/>
  <g transform="translate(140, 50)">
    <circle cx="140" cy="140" r="100" fill="none" stroke="#f97316" stroke-width="2.5" stroke-dasharray="12 6"/>
    <polygon points="90,70 140,30 190,70 190,160 140,210 90,160" fill="#1e293b" stroke="#ef5b55" stroke-width="2.5"/>
  </g>
  <g transform="translate(480, 70)">
    <rect width="640" height="260" rx="6" fill="rgba(28, 7, 2, 0.9)" stroke="#f97316" stroke-width="2"/>
    <rect x="10" y="10" width="620" height="34" fill="#431407"/>
    <text x="24" y="33" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold">CONTAINMENT CHAMBER MK-04 // COHERENCE: 04</text>
    <text x="24" y="80" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-004 — RUST-BLEEDING SENTRY</text>
    <text x="24" y="112" fill="#f97316" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold">SECC RANK: γ (MORPHEAN) · DAMAGE: GRUDGE · YIELD: 22 PE</text>
    <line x1="24" y1="128" x2="616" y2="128" stroke="#f97316" stroke-width="1" stroke-dasharray="4 2"/>
    <text x="24" y="160" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Special Work: Subjugation (Ferrehan 65%) | Danger: Rust Corrosion Armor Rot</text>
  </g>
</svg>'''
    },

    'se-006': {
        'name': 'The Siphon Leech',
        'code': 'SE-006',
        'risk': 'SOMNA',
        'risk_badge': 'risk-SOMNA',
        'dmg': 'WEIGHT (Dual)',
        'color': '#10b981',
        'sub_color': '#38bdf8',
        'profile': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="pGrad_006" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#064e3b" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#02231a" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#010a08" stop-opacity="1"/>
    </radialGradient>
    <filter id="pGlow_006" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="500" height="500" rx="8" fill="url(#pGrad_006)" stroke="#10b981" stroke-width="3"/>
  <rect x="15" y="15" width="470" height="470" rx="4" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.6"/>

  <g filter="url(#pGlow_006)">
    <!-- Concentric Siphon Rings of Razor Teeth -->
    <circle cx="250" cy="220" r="130" fill="#04231b" stroke="#10b981" stroke-width="3.5"/>
    <circle cx="250" cy="220" r="90" fill="#021410" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="8 4"/>
    <circle cx="250" cy="220" r="50" fill="#000000" stroke="#10b981" stroke-width="2"/>
    
    <!-- Radial Siphon Teeth -->
    <polygon points="250,90 256,120 244,120" fill="#f1df76"/>
    <polygon points="250,350 256,320 244,320" fill="#f1df76"/>
    <polygon points="120,220 150,226 150,214" fill="#f1df76"/>
    <polygon points="380,220 350,226 350,214" fill="#f1df76"/>
    
    <!-- Central Effluent Abyss Core -->
    <circle cx="250" cy="220" r="22" fill="#10b981"/>
    <circle cx="250" cy="220" r="8" fill="#ffffff"/>
  </g>

  <!-- HUD Footer -->
  <rect x="30" y="440" width="440" height="36" rx="4" fill="#030712" stroke="#10b981" stroke-width="1.5"/>
  <text x="45" y="463" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">SE-006 // SIPHON LEECH</text>
  <text x="455" y="463" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">SOMNA · WEIGHT</text>
</svg>''',
        'banner': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bGrad_006" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#064e3b"/>
      <stop offset="50%" stop-color="#02231a"/>
      <stop offset="100%" stop-color="#010a08"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#bGrad_006)"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#10b981" stroke-width="3"/>
  <g transform="translate(140, 50)">
    <circle cx="140" cy="140" r="100" fill="#04231b" stroke="#10b981" stroke-width="2.5"/>
    <circle cx="140" cy="140" r="60" fill="#021410" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="140" cy="140" r="20" fill="#10b981"/>
  </g>
  <g transform="translate(480, 70)">
    <rect width="640" height="260" rx="6" fill="rgba(2, 35, 26, 0.9)" stroke="#10b981" stroke-width="2"/>
    <rect x="10" y="10" width="620" height="34" fill="#064e3b"/>
    <text x="24" y="33" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold">CONTAINMENT CHAMBER MK-06 // COHERENCE: 03</text>
    <text x="24" y="80" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-006 — THE SIPHON LEECH</text>
    <text x="24" y="112" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold">SECC RANK: β (SOMNA) · DAMAGE: WEIGHT (DUAL) · YIELD: 20 PE</text>
    <line x1="24" y1="128" x2="616" y2="128" stroke="#10b981" stroke-width="1" stroke-dasharray="4 2"/>
    <text x="24" y="160" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Special Work: Extraction (Hausuhan 70%) | Danger: Effluent Siphon Drain</text>
  </g>
</svg>'''
    },

    'se-007': {
        'name': 'The Ashen Scribe',
        'code': 'SE-007',
        'risk': 'SOMNA',
        'risk_badge': 'risk-SOMNA',
        'dmg': 'LAMENT (Mental)',
        'color': '#94a3b8',
        'sub_color': '#38bdf8',
        'profile': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="pGrad_007" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#0f172a" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#020617" stop-opacity="1"/>
    </radialGradient>
    <filter id="pGlow_007" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="500" height="500" rx="8" fill="url(#pGrad_007)" stroke="#94a3b8" stroke-width="3"/>
  <rect x="15" y="15" width="470" height="470" rx="4" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.6"/>

  <g filter="url(#pGlow_007)">
    <!-- Ashen Slate Tablet -->
    <rect x="140" y="80" width="220" height="280" rx="6" fill="#0f172a" stroke="#94a3b8" stroke-width="3.5"/>
    <line x1="170" y1="130" x2="330" y2="130" stroke="#38bdf8" stroke-width="2"/>
    <line x1="170" y1="170" x2="330" y2="170" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8 4"/>
    <line x1="170" y1="210" x2="330" y2="210" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8 4"/>
    <line x1="170" y1="250" x2="280" y2="250" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8 4"/>
    
    <!-- Weeping Bone Quill -->
    <polygon points="320,60 360,40 330,180 310,180" fill="#e2e8f0" stroke="#f1df76" stroke-width="2"/>
    <circle cx="320" cy="180" r="4" fill="#38bdf8"/>
  </g>

  <!-- HUD Footer -->
  <rect x="30" y="440" width="440" height="36" rx="4" fill="#030712" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="45" y="463" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">SE-007 // ASHEN SCRIBE</text>
  <text x="455" y="463" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">SOMNA · LAMENT</text>
</svg>''',
        'banner': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bGrad_007" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#bGrad_007)"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#94a3b8" stroke-width="3"/>
  <g transform="translate(140, 50)">
    <rect x="60" y="30" width="160" height="220" rx="4" fill="#0f172a" stroke="#94a3b8" stroke-width="2.5"/>
    <polygon points="190,20 220,10 200,100 185,100" fill="#e2e8f0" stroke="#f1df76" stroke-width="1.5"/>
  </g>
  <g transform="translate(480, 70)">
    <rect width="640" height="260" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#94a3b8" stroke-width="2"/>
    <rect x="10" y="10" width="620" height="34" fill="#1e293b"/>
    <text x="24" y="33" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold">CONTAINMENT CHAMBER MK-07 // COHERENCE: 04</text>
    <text x="24" y="80" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-007 — THE ASHEN SCRIBE</text>
    <text x="24" y="112" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold">SECC RANK: β (SOMNA) · DAMAGE: LAMENT · YIELD: 16 PE</text>
    <line x1="24" y1="128" x2="616" y2="128" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 2"/>
    <text x="24" y="160" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Special Work: Insight (Viderehan 70%) | Danger: Amnestic Name Erasure</text>
  </g>
</svg>'''
    },

    'se-009': {
        'name': 'The Memory Weaver',
        'code': 'SE-009',
        'risk': 'SOMNA',
        'risk_badge': 'risk-SOMNA',
        'dmg': 'LAMENT (Mental)',
        'color': '#0284c7',
        'sub_color': '#38bdf8',
        'profile': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="pGrad_009" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0369a1" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#082f49" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#020617" stop-opacity="1"/>
    </radialGradient>
    <filter id="pGlow_009" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="500" height="500" rx="8" fill="url(#pGrad_009)" stroke="#0284c7" stroke-width="3"/>
  <rect x="15" y="15" width="470" height="470" rx="4" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.6"/>

  <g filter="url(#pGlow_009)">
    <!-- Sunken Aquatic Bell in Subterranean Weeping -->
    <circle cx="250" cy="220" r="140" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="10 5"/>
    <path d="M230,120 C225,160 160,220 150,330 C210,350 290,350 350,330 C340,220 275,160 270,120 Z" fill="#0f172a" stroke="#0284c7" stroke-width="3.5"/>
    <!-- Water Lilies & Tendrils -->
    <circle cx="200" cy="300" r="14" fill="#38bdf8"/>
    <circle cx="300" cy="300" r="14" fill="#38bdf8"/>
    <circle cx="250" cy="260" r="18" fill="#f1df76"/>
  </g>

  <!-- HUD Footer -->
  <rect x="30" y="440" width="440" height="36" rx="4" fill="#030712" stroke="#0284c7" stroke-width="1.5"/>
  <text x="45" y="463" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">SE-009 // DROWNED BELL</text>
  <text x="455" y="463" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">SOMNA · LAMENT</text>
</svg>''',
        'banner': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bGrad_009" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0369a1"/>
      <stop offset="50%" stop-color="#082f49"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#bGrad_009)"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#0284c7" stroke-width="3"/>
  <g transform="translate(140, 50)">
    <circle cx="140" cy="140" r="100" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <path d="M120,60 C120,100 80,140 70,220 C120,230 160,230 210,220 C200,140 160,100 160,60 Z" fill="#0f172a" stroke="#0284c7" stroke-width="2.5"/>
  </g>
  <g transform="translate(480, 70)">
    <rect width="640" height="260" rx="6" fill="rgba(8, 47, 73, 0.9)" stroke="#0284c7" stroke-width="2"/>
    <rect x="10" y="10" width="620" height="34" fill="#0369a1"/>
    <text x="24" y="33" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold">CONTAINMENT CHAMBER MK-09 // COHERENCE: 03</text>
    <text x="24" y="80" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-009 — THE DROWNED BELL</text>
    <text x="24" y="112" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold">SECC RANK: β (SOMNA) · DAMAGE: LAMENT · YIELD: 18 PE</text>
    <line x1="24" y1="128" x2="616" y2="128" stroke="#0284c7" stroke-width="1" stroke-dasharray="4 2"/>
    <text x="24" y="160" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Special Work: Communion (Docerehan 70%) | Danger: Submersion Chimes</text>
  </g>
</svg>'''
    },

    'se-011': {
        'name': 'The Whispering Walls',
        'code': 'SE-011',
        'risk': 'PHANTASM',
        'risk_badge': 'risk-PHANTASM',
        'dmg': 'LAMENT (Mental)',
        'color': '#ef4444',
        'sub_color': '#38bdf8',
        'profile': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="pGrad_011" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#450a0a" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#1c0406" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#060203" stop-opacity="1"/>
    </radialGradient>
    <filter id="pGlow_011" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="500" height="500" rx="8" fill="url(#pGrad_011)" stroke="#ef4444" stroke-width="3"/>
  <rect x="15" y="15" width="470" height="470" rx="4" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.6"/>

  <g filter="url(#pGlow_011)">
    <!-- Living Iron Wall Partition with Screaming Faces -->
    <rect x="120" y="80" width="260" height="280" rx="6" fill="#1c1917" stroke="#ef4444" stroke-width="3.5"/>
    <circle cx="200" cy="160" r="24" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
    <circle cx="300" cy="160" r="24" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
    <circle cx="250" cy="260" r="32" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
    <!-- Whispering sound lines -->
    <path d="M160,260 Q120,240 80,260" stroke="#38bdf8" stroke-width="2" fill="none"/>
    <path d="M340,260 Q380,240 420,260" stroke="#38bdf8" stroke-width="2" fill="none"/>
  </g>

  <!-- HUD Footer -->
  <rect x="30" y="440" width="440" height="36" rx="4" fill="#030712" stroke="#ef4444" stroke-width="1.5"/>
  <text x="45" y="463" fill="#ef4444" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">SE-011 // WHISPERING WALLS</text>
  <text x="455" y="463" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">PHANTASM · LAMENT</text>
</svg>''',
        'banner': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bGrad_011" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#450a0a"/>
      <stop offset="50%" stop-color="#1c0406"/>
      <stop offset="100%" stop-color="#060203"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#bGrad_011)"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#ef4444" stroke-width="3"/>
  <g transform="translate(140, 50)">
    <rect x="60" y="40" width="160" height="200" rx="4" fill="#1c1917" stroke="#ef4444" stroke-width="2.5"/>
    <circle cx="140" cy="140" r="30" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
  </g>
  <g transform="translate(480, 70)">
    <rect width="640" height="260" rx="6" fill="rgba(28, 4, 6, 0.9)" stroke="#ef4444" stroke-width="2"/>
    <rect x="10" y="10" width="620" height="34" fill="#450a0a"/>
    <text x="24" y="33" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold">CONTAINMENT CHAMBER MK-11 // COHERENCE: 04</text>
    <text x="24" y="80" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-011 — THE WHISPERING WALLS</text>
    <text x="24" y="112" fill="#ef4444" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold">SECC RANK: δ (PHANTASM) · DAMAGE: LAMENT · YIELD: 28 PE</text>
    <line x1="24" y1="128" x2="616" y2="128" stroke="#ef4444" stroke-width="1" stroke-dasharray="4 2"/>
    <text x="24" y="160" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Special Work: Insight (Viderehan 60%) | Danger: Hallucinatory Acoustic Screams</text>
  </g>
</svg>'''
    },

    'se-014': {
        'name': 'The Hollow Debt Eater',
        'code': 'SE-014',
        'risk': 'APOCRYPHA',
        'risk_badge': 'risk-APOCRYPHA',
        'dmg': 'WEIGHT (Dual)',
        'color': '#f1df76',
        'sub_color': '#ef5b55',
        'profile': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="pGrad_014" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#422006" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#1c0e03" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#060301" stop-opacity="1"/>
    </radialGradient>
    <filter id="pGlow_014" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="500" height="500" rx="8" fill="url(#pGrad_014)" stroke="#f1df76" stroke-width="3"/>
  <rect x="15" y="15" width="470" height="470" rx="4" fill="none" stroke="#ef5b55" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.6"/>

  <g filter="url(#pGlow_014)">
    <!-- Ledger Vault Jaws -->
    <polygon points="150,120 350,120 380,240 350,340 150,340 120,240" fill="#1c1917" stroke="#f1df76" stroke-width="3.5"/>
    <circle cx="250" cy="230" r="60" fill="#000000" stroke="#ef5b55" stroke-width="3"/>
    <!-- Gold Coin Scales Eaten -->
    <circle cx="230" cy="220" r="14" fill="#f1df76"/>
    <circle cx="270" cy="240" r="14" fill="#f1df76"/>
  </g>

  <!-- HUD Footer -->
  <rect x="30" y="440" width="440" height="36" rx="4" fill="#030712" stroke="#f1df76" stroke-width="1.5"/>
  <text x="45" y="463" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">SE-014 // HOLLOW DEBT EATER</text>
  <text x="455" y="463" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">APOCRYPHA · WEIGHT</text>
</svg>''',
        'banner': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bGrad_014" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#422006"/>
      <stop offset="50%" stop-color="#1c0e03"/>
      <stop offset="100%" stop-color="#060301"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#bGrad_014)"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#f1df76" stroke-width="3"/>
  <g transform="translate(140, 50)">
    <polygon points="90,70 190,70 210,140 190,210 90,210 70,140" fill="#1c1917" stroke="#f1df76" stroke-width="2.5"/>
    <circle cx="140" cy="140" r="30" fill="#000" stroke="#ef5b55" stroke-width="2"/>
  </g>
  <g transform="translate(480, 70)">
    <rect width="640" height="260" rx="6" fill="rgba(28, 14, 3, 0.9)" stroke="#f1df76" stroke-width="2"/>
    <rect x="10" y="10" width="620" height="34" fill="#422006"/>
    <text x="24" y="33" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold">CONTAINMENT CHAMBER MK-14 // COHERENCE: 02</text>
    <text x="24" y="80" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-014 — THE HOLLOW DEBT EATER</text>
    <text x="24" y="112" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold">SECC RANK: ε (APOCRYPHA) · DAMAGE: WEIGHT · YIELD: 38 PE</text>
    <line x1="24" y1="128" x2="616" y2="128" stroke="#f1df76" stroke-width="1" stroke-dasharray="4 2"/>
    <text x="24" y="160" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Special Work: Restraint (Custodihan 40%) | Danger: Financial Ruin Devour</text>
  </g>
</svg>'''
    },

    'se-015': {
        'name': 'The Sovereign Debt Scale',
        'code': 'SE-015',
        'risk': 'APOCRYPHA',
        'risk_badge': 'risk-APOCRYPHA',
        'dmg': 'VOID (Soul)',
        'color': '#f8fafc',
        'sub_color': '#f1df76',
        'profile': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="pGrad_015" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e1b4b" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#0c0a24" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#020208" stop-opacity="1"/>
    </radialGradient>
    <filter id="pGlow_015" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="500" height="500" rx="8" fill="url(#pGrad_015)" stroke="#f8fafc" stroke-width="3"/>
  <rect x="15" y="15" width="470" height="470" rx="4" fill="none" stroke="#f1df76" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.6"/>

  <g filter="url(#pGlow_015)">
    <!-- Golden Balance Scale -->
    <line x1="120" y1="160" x2="380" y2="160" stroke="#f1df76" stroke-width="5"/>
    <line x1="250" y1="100" x2="250" y2="360" stroke="#f8fafc" stroke-width="6"/>
    <polygon points="250,80 270,120 230,120" fill="#f1df76"/>
    
    <!-- Left Scale Pan (Weeping Heart) -->
    <line x1="140" y1="160" x2="110" y2="260" stroke="#f1df76" stroke-width="2"/>
    <line x1="140" y1="160" x2="170" y2="260" stroke="#f1df76" stroke-width="2"/>
    <ellipse cx="140" cy="265" rx="35" ry="10" fill="#1e1b4b" stroke="#ef5b55" stroke-width="2"/>
    
    <!-- Right Scale Pan (Lead Slate) -->
    <line x1="360" y1="160" x2="330" y2="260" stroke="#f1df76" stroke-width="2"/>
    <line x1="360" y1="160" x2="390" y2="260" stroke="#f1df76" stroke-width="2"/>
    <ellipse cx="360" cy="265" rx="35" ry="10" fill="#1e1b4b" stroke="#38bdf8" stroke-width="2"/>
  </g>

  <!-- HUD Footer -->
  <rect x="30" y="440" width="440" height="36" rx="4" fill="#030712" stroke="#f8fafc" stroke-width="1.5"/>
  <text x="45" y="463" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">SE-015 // SOVEREIGN DEBT SCALE</text>
  <text x="455" y="463" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">APOCRYPHA · VOID</text>
</svg>''',
        'banner': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bGrad_015" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b"/>
      <stop offset="50%" stop-color="#0c0a24"/>
      <stop offset="100%" stop-color="#020208"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#bGrad_015)"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#f8fafc" stroke-width="3"/>
  <g transform="translate(140, 50)">
    <line x1="60" y1="100" x2="220" y2="100" stroke="#f1df76" stroke-width="3"/>
    <line x1="140" y1="60" x2="140" y2="220" stroke="#f8fafc" stroke-width="4"/>
  </g>
  <g transform="translate(480, 70)">
    <rect width="640" height="260" rx="6" fill="rgba(12, 10, 36, 0.9)" stroke="#f8fafc" stroke-width="2"/>
    <rect x="10" y="10" width="620" height="34" fill="#1e1b4b"/>
    <text x="24" y="33" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold">CONTAINMENT CHAMBER MK-15 // COHERENCE: 01</text>
    <text x="24" y="80" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-015 — THE SOVEREIGN DEBT SCALE</text>
    <text x="24" y="112" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold">SECC RANK: ε (APOCRYPHA) · DAMAGE: VOID · YIELD: 42 PE</text>
    <line x1="24" y1="128" x2="616" y2="128" stroke="#f8fafc" stroke-width="1" stroke-dasharray="4 2"/>
    <text x="24" y="160" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Special Work: Restraint (Custodihan 35%) | Danger: Existential Debt Eradication</text>
  </g>
</svg>'''
    }
}

dirs_profile = ['/home/user/01_Somnarak_Wiki/assets/art/entities', '/home/user/icons']
dirs_banner = ['/home/user/01_Somnarak_Wiki/assets/art/entities', '/home/user/01_Somnarak_Wiki/assets/banners', '/home/user/icons']

for code, data in extra_entities.items():
    p_svg = data['profile']
    b_svg = data['banner']
    num = code.replace('se-', '')
    
    p_names = [f'profile_entity_se_{num}.svg', f'profile_entity_se_{int(num):03d}.svg', f'{code}-profile.svg']
    for p_name in p_names:
        for d in dirs_profile:
            os.makedirs(d, exist_ok=True)
            path = os.path.join(d, p_name)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(p_svg)
    
    b_names = [f'banner_entity_se_{num}.svg', f'banner_entity_se_{int(num):03d}.svg', f'{code}-banner.svg']
    for b_name in b_names:
        for d in dirs_banner:
            os.makedirs(d, exist_ok=True)
            path = os.path.join(d, b_name)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(b_svg)

print('SUCCESS: Upgraded all remaining entity vector profile and banner suites!')
