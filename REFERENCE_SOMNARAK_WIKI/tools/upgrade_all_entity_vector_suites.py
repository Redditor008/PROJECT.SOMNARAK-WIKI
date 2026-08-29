import os

# Definitions for all 10 canonical entities + extras
# Each entity has:
# - name, code, risk, damage_type, damage_color, desc, profile_svg, banner_svg, icon_svg

entities_data = {
    'se-001': {
        'name': 'The Orphaned Bell',
        'code': 'SE-001',
        'risk': 'PHANTASM',
        'risk_badge': 'risk-PHANTASM',
        'dmg': 'LAMENT (Mental)',
        'color': '#38bdf8',
        'sub_color': '#f1df76',
        'profile': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="pGrad_001" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#082f49" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#041220" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#02060c" stop-opacity="1"/>
    </radialGradient>
    <filter id="pGlow_001" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="500" height="500" rx="8" fill="url(#pGrad_001)" stroke="#38bdf8" stroke-width="3"/>
  <rect x="15" y="15" width="470" height="470" rx="4" fill="none" stroke="#f1df76" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.6"/>
  
  <!-- Massive Suspended Bronze Bell -->
  <!-- Heavy Iron Suspension Chains -->
  <line x1="200" y1="20" x2="230" y2="120" stroke="#64748b" stroke-width="6" stroke-dasharray="12 6"/>
  <line x1="300" y1="20" x2="270" y2="120" stroke="#64748b" stroke-width="6" stroke-dasharray="12 6"/>
  <rect x="220" y="110" width="60" height="24" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  
  <!-- Bell Body -->
  <g filter="url(#pGlow_001)">
    <path d="M225,130 C220,170 140,240 130,360 C210,380 290,380 370,360 C360,240 280,170 275,130 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="4"/>
    <!-- Bell Rim -->
    <ellipse cx="250" cy="360" rx="120" ry="24" fill="#0f172a" stroke="#f1df76" stroke-width="3"/>
    
    <!-- Crying Face Embossed upon Bell Visage -->
    <!-- Eyes weeping liquid cyan Han tears -->
    <path d="M200,230 Q220,215 230,235" fill="none" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
    <path d="M300,230 Q280,215 270,235" fill="none" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
    <!-- Weeping Tear Streams -->
    <path d="M215,235 C215,280 200,310 210,360" fill="none" stroke="#38bdf8" stroke-width="3.5" stroke-linecap="round" opacity="0.9"/>
    <path d="M285,235 C285,280 300,310 290,360" fill="none" stroke="#38bdf8" stroke-width="3.5" stroke-linecap="round" opacity="0.9"/>
    <!-- Anguished Open Bronze Mouth -->
    <path d="M230,280 Q250,315 270,280 Q250,290 230,280 Z" fill="#020617" stroke="#f1df76" stroke-width="2.5"/>
    
    <!-- Heavy Iron Clapper Hanging Below -->
    <line x1="250" y1="340" x2="250" y2="420" stroke="#475569" stroke-width="8"/>
    <circle cx="250" cy="425" r="22" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
  </g>

  <!-- Sonic Resonance Waves Expanding -->
  <circle cx="250" cy="360" r="150" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="10 5" opacity="0.5"/>
  <circle cx="250" cy="360" r="190" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="6 6" opacity="0.3"/>
  
  <!-- HUD Identification -->
  <rect x="30" y="440" width="440" height="36" rx="4" fill="#030712" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="45" y="463" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">SE-001 // THE ORPHANED BELL</text>
  <text x="455" y="463" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">PHANTASM · LAMENT</text>
</svg>''',
        'banner': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bGrad_001" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#082f49"/>
      <stop offset="50%" stop-color="#041324"/>
      <stop offset="100%" stop-color="#02060f"/>
    </linearGradient>
    <filter id="bGlow_001" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="1200" height="400" fill="url(#bGrad_001)"/>
  
  <!-- Tactical Grid & Chamber Telemetry -->
  <line x1="40" y1="40" x2="1160" y2="40" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="12 6" opacity="0.6"/>
  <line x1="40" y1="360" x2="1160" y2="360" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="12 6" opacity="0.6"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#38bdf8" stroke-width="3"/>
  
  <!-- Left Chamber Scene -->
  <g transform="translate(120, 50)" filter="url(#bGlow_001)">
    <!-- Hanging Chains -->
    <line x1="120" y1="0" x2="140" y2="70" stroke="#64748b" stroke-width="4" stroke-dasharray="8 4"/>
    <line x1="180" y1="0" x2="160" y2="70" stroke="#64748b" stroke-width="4" stroke-dasharray="8 4"/>
    <!-- Bell -->
    <path d="M140,70 C135,100 80,150 70,230 C130,245 170,245 230,230 C220,150 165,100 160,70 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
    <ellipse cx="150" cy="230" rx="80" ry="16" fill="#0f172a" stroke="#f1df76" stroke-width="2"/>
    <circle cx="150" cy="270" r="16" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <line x1="150" y1="230" x2="150" y2="270" stroke="#475569" stroke-width="5"/>
  </g>

  <!-- Soundwaves -->
  <circle cx="270" cy="280" r="100" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="6 4" opacity="0.5"/>
  <circle cx="270" cy="280" r="140" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4 4" opacity="0.3"/>

  <!-- Right Side Tactical Dossier HUD -->
  <g transform="translate(480, 70)">
    <rect width="640" height="260" rx="6" fill="rgba(6, 15, 28, 0.85)" stroke="#38bdf8" stroke-width="2"/>
    <rect x="10" y="10" width="620" height="34" fill="#0c233c"/>
    <text x="24" y="33" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold">CONTAINMENT CHAMBER MK-01 // COHERENCE: 04</text>
    
    <text x="24" y="80" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-001 — THE ORPHANED BELL</text>
    <text x="24" y="112" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold">SECC RANK: δ (PHANTASM) · DAMAGE: LAMENT (MENTAL) · YIELD: 32 PE</text>
    
    <line x1="24" y1="128" x2="616" y2="128" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4 2"/>
    
    <text x="24" y="160" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Special Work: Insight (Viderehan 65%) | Danger: High Sonic Cognitive Collapse</text>
    <text x="24" y="185" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Extracted Gear: Lament Requiem (Weapon) / Lament Shroud (Suit) / Lament\'s Edge</text>
    
    <!-- Chamber Status Indicators -->
    <rect x="24" y="210" width="120" height="26" rx="3" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1"/>
    <text x="84" y="227" fill="#bae6fd" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">RESONANCE: HIGH</text>
    
    <rect x="154" y="210" width="130" height="26" rx="3" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
    <text x="219" y="227" fill="#a7f3d0" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">EXTRACTION: READY</text>
  </g>
</svg>'''
    },

    'se-002': {
        'name': 'The Grieving Colossus',
        'code': 'SE-002',
        'risk': 'PHANTASM',
        'risk_badge': 'risk-PHANTASM',
        'dmg': 'GRUDGE (Physical)',
        'color': '#ef5b55',
        'sub_color': '#f1df76',
        'profile': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="pGrad_002" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#450a0a" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#1c0406" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#060203" stop-opacity="1"/>
    </radialGradient>
    <filter id="pGlow_002" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="500" height="500" rx="8" fill="url(#pGrad_002)" stroke="#ef5b55" stroke-width="3"/>
  <rect x="15" y="15" width="470" height="470" rx="4" fill="none" stroke="#f1df76" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.6"/>

  <!-- Giant Basalt Stone Golem Visage -->
  <g filter="url(#pGlow_002)">
    <!-- Craggy Head Monolith -->
    <polygon points="170,80 330,80 370,220 340,360 160,360 130,220" fill="#1c1917" stroke="#ef5b55" stroke-width="4"/>
    
    <!-- Stone Fractures & Crimson Weeping Seams -->
    <path d="M200,80 L230,160 L210,240 L230,340" fill="none" stroke="#ef5b55" stroke-width="3.5" stroke-linecap="round"/>
    <path d="M300,80 L280,180 L310,260 L290,340" fill="none" stroke="#ef5b55" stroke-width="3.5" stroke-linecap="round"/>
    
    <!-- Glowing Red Cyclopean Eye Socket -->
    <circle cx="250" cy="190" r="32" fill="#450a0a" stroke="#ef5b55" stroke-width="3"/>
    <circle cx="250" cy="190" r="14" fill="#ef5b55" filter="url(#pGlow_002)"/>
    <circle cx="250" cy="190" r="6" fill="#ffffff"/>
    
    <!-- Heavy Basalt Restraint Collars & Chains -->
    <rect x="140" y="340" width="220" height="34" rx="4" fill="#292524" stroke="#f1df76" stroke-width="3"/>
    <circle cx="170" cy="357" r="8" fill="#f1df76"/>
    <circle cx="330" cy="357" r="8" fill="#f1df76"/>
    
    <!-- Hanging Grudge Tears -->
    <path d="M235,225 C235,280 220,320 225,380" fill="none" stroke="#ef5b55" stroke-width="4" stroke-linecap="round"/>
    <path d="M265,225 C265,280 280,320 275,380" fill="none" stroke="#ef5b55" stroke-width="4" stroke-linecap="round"/>
  </g>

  <!-- Heavy Bedrock Spikes Below -->
  <polygon points="120,430 160,370 200,430" fill="#1c1917" stroke="#ef5b55" stroke-width="2"/>
  <polygon points="300,430 340,370 380,430" fill="#1c1917" stroke="#ef5b55" stroke-width="2"/>
  <polygon points="210,430 250,380 290,430" fill="#292524" stroke="#f1df76" stroke-width="2"/>

  <!-- HUD Footer -->
  <rect x="30" y="440" width="440" height="36" rx="4" fill="#030712" stroke="#ef5b55" stroke-width="1.5"/>
  <text x="45" y="463" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">SE-002 // THE GRIEVING COLOSSUS</text>
  <text x="455" y="463" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">PHANTASM · GRUDGE</text>
</svg>''',
        'banner': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bGrad_002" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#450a0a"/>
      <stop offset="50%" stop-color="#1c0406"/>
      <stop offset="100%" stop-color="#060203"/>
    </linearGradient>
    <filter id="bGlow_002" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="1200" height="400" fill="url(#bGrad_002)"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#ef5b55" stroke-width="3"/>
  
  <!-- Left Side Golem Scene -->
  <g transform="translate(100, 50)" filter="url(#bGlow_002)">
    <polygon points="100,20 220,20 250,130 220,240 100,240 70,130" fill="#1c1917" stroke="#ef5b55" stroke-width="3"/>
    <circle cx="160" cy="110" r="24" fill="#450a0a" stroke="#ef5b55" stroke-width="2.5"/>
    <circle cx="160" cy="110" r="10" fill="#ef5b55"/>
    <rect x="80" y="220" width="160" height="26" fill="#292524" stroke="#f1df76" stroke-width="2"/>
  </g>

  <!-- Right Side HUD -->
  <g transform="translate(480, 70)">
    <rect width="640" height="260" rx="6" fill="rgba(28, 4, 6, 0.9)" stroke="#ef5b55" stroke-width="2"/>
    <rect x="10" y="10" width="620" height="34" fill="#380608"/>
    <text x="24" y="33" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold">CONTAINMENT CHAMBER MK-02 // COHERENCE: 05</text>
    <text x="24" y="80" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-002 — THE GRIEVING COLOSSUS</text>
    <text x="24" y="112" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold">SECC RANK: δ (PHANTASM) · DAMAGE: GRUDGE (PHYSICAL) · YIELD: 30 PE</text>
    <line x1="24" y1="128" x2="616" y2="128" stroke="#ef5b55" stroke-width="1" stroke-dasharray="4 2"/>
    <text x="24" y="160" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Special Work: Subjugation (Ferrehan 60%) | Danger: Tremor Shockwaves</text>
    <text x="24" y="185" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Extracted Gear: Mourning Maul (Weapon) / Mourning Mantle (Suit)</text>
  </g>
</svg>'''
    },

    'se-003': {
        'name': 'The Thread of Memory',
        'code': 'SE-003',
        'risk': 'SOMNA',
        'risk_badge': 'risk-SOMNA',
        'dmg': 'LAMENT (Mental)',
        'color': '#38bdf8',
        'sub_color': '#a855f7',
        'profile': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="pGrad_003" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e1b4b" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#0c0a24" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#03040c" stop-opacity="1"/>
    </radialGradient>
    <filter id="pGlow_003" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="500" height="500" rx="8" fill="url(#pGrad_003)" stroke="#38bdf8" stroke-width="3"/>
  <rect x="15" y="15" width="470" height="470" rx="4" fill="none" stroke="#a855f7" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.6"/>

  <!-- Ethereal Loom & Needle Spindle of Memory -->
  <g filter="url(#pGlow_003)">
    <!-- Loom Outer Geometric Ring -->
    <circle cx="250" cy="230" r="150" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="12 6"/>
    <circle cx="250" cy="230" r="90" fill="none" stroke="#a855f7" stroke-width="2"/>
    
    <!-- Shimmering Warp & Weft Threads -->
    <line x1="130" y1="150" x2="370" y2="310" stroke="#38bdf8" stroke-width="2" opacity="0.8"/>
    <line x1="130" y1="310" x2="370" y2="150" stroke="#38bdf8" stroke-width="2" opacity="0.8"/>
    <line x1="250" y1="80" x2="250" y2="380" stroke="#f1df76" stroke-width="2.5"/>
    <line x1="100" y1="230" x2="400" y2="230" stroke="#a855f7" stroke-width="2"/>

    <!-- Central Luminous Needle / Spindle -->
    <polygon points="250,50 264,230 250,410 236,230" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
    <!-- Eye of the Needle -->
    <ellipse cx="250" cy="120" rx="6" ry="24" fill="#38bdf8" filter="url(#pGlow_003)"/>
    <circle cx="250" cy="120" r="3" fill="#ffffff"/>

    <!-- Thread Spools Spilling Azure Memories -->
    <circle cx="250" cy="230" r="28" fill="#1e1b4b" stroke="#f1df76" stroke-width="2"/>
    <circle cx="250" cy="230" r="10" fill="#38bdf8"/>
  </g>

  <!-- HUD Footer -->
  <rect x="30" y="440" width="440" height="36" rx="4" fill="#030712" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="45" y="463" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">SE-003 // THREAD OF MEMORY</text>
  <text x="455" y="463" fill="#a855f7" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">SOMNA · LAMENT</text>
</svg>''',
        'banner': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bGrad_003" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b"/>
      <stop offset="50%" stop-color="#0c0a24"/>
      <stop offset="100%" stop-color="#03040c"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#bGrad_003)"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#38bdf8" stroke-width="3"/>
  
  <g transform="translate(140, 60)">
    <circle cx="140" cy="140" r="110" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8 4"/>
    <polygon points="140,10 152,140 140,270 128,140" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5"/>
    <circle cx="140" cy="80" r="8" fill="#38bdf8"/>
  </g>

  <g transform="translate(480, 70)">
    <rect width="640" height="260" rx="6" fill="rgba(12, 10, 36, 0.9)" stroke="#38bdf8" stroke-width="2"/>
    <rect x="10" y="10" width="620" height="34" fill="#1e1b4b"/>
    <text x="24" y="33" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold">CONTAINMENT CHAMBER MK-03 // COHERENCE: 03</text>
    <text x="24" y="80" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-003 — THREAD OF MEMORY</text>
    <text x="24" y="112" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold">SECC RANK: β (SOMNA) · DAMAGE: LAMENT (MENTAL) · YIELD: 18 PE</text>
    <line x1="24" y1="128" x2="616" y2="128" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4 2"/>
    <text x="24" y="160" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Special Work: Communion (Docerehan 70%) | Danger: Amnestic Erosion</text>
    <text x="24" y="185" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Extracted Gear: Thread Needle (Weapon) / Weaver\'s Shroud (Suit)</text>
  </g>
</svg>'''
    },

    'se-005': {
        'name': 'The Smothering Mother',
        'code': 'SE-005',
        'risk': 'AETHER',
        'risk_badge': 'risk-AETHER',
        'dmg': 'LAMENT (Mental)',
        'color': '#f1df76',
        'sub_color': '#ef4444',
        'profile': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="pGrad_005" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#422006" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#1a0c02" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#050200" stop-opacity="1"/>
    </radialGradient>
    <filter id="pGlow_005" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="500" height="500" rx="8" fill="url(#pGrad_005)" stroke="#f1df76" stroke-width="3"/>
  <rect x="15" y="15" width="470" height="470" rx="4" fill="none" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.6"/>

  <!-- Golden Porcelain Maternal Figure Wrapped in Suffocating Shrouds -->
  <g filter="url(#pGlow_005)">
    <!-- Cradle Halo -->
    <circle cx="250" cy="180" r="110" fill="none" stroke="#f1df76" stroke-width="3" stroke-dasharray="10 5"/>
    <polygon points="250,50 280,100 220,100" fill="#f1df76"/>
    
    <!-- Veiled Maternal Visage -->
    <path d="M190,130 C190,80 310,80 310,130 C310,210 280,260 250,260 C220,260 190,210 190,130 Z" fill="#fffbeb" stroke="#f1df76" stroke-width="2.5"/>
    
    <!-- Weeping Black Tear Veins -->
    <path d="M220,150 L220,220" stroke="#78350f" stroke-width="3" stroke-linecap="round"/>
    <path d="M280,150 L280,220" stroke="#78350f" stroke-width="3" stroke-linecap="round"/>
    
    <!-- Suffocating Arms Embracing Empty Cradle -->
    <path d="M160,260 C140,320 200,380 250,380 C300,380 360,320 340,260 C310,320 190,320 160,260 Z" fill="#291504" stroke="#f1df76" stroke-width="3"/>
    <circle cx="250" cy="310" r="20" fill="#ef4444" filter="url(#pGlow_005)"/>
    <circle cx="250" cy="310" r="8" fill="#ffffff"/>
  </g>

  <!-- HUD Footer -->
  <rect x="30" y="440" width="440" height="36" rx="4" fill="#030712" stroke="#f1df76" stroke-width="1.5"/>
  <text x="45" y="463" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">SE-005 // SMOTHERING CRADLE</text>
  <text x="455" y="463" fill="#ef4444" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">AETHER · LAMENT</text>
</svg>''',
        'banner': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bGrad_005" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#422006"/>
      <stop offset="50%" stop-color="#1a0c02"/>
      <stop offset="100%" stop-color="#050200"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#bGrad_005)"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#f1df76" stroke-width="3"/>
  
  <g transform="translate(140, 50)">
    <circle cx="140" cy="140" r="100" fill="none" stroke="#f1df76" stroke-width="2.5" stroke-dasharray="8 4"/>
    <path d="M100,100 C100,50 180,50 180,100 C180,170 160,200 140,200 C120,200 100,170 100,100 Z" fill="#fffbeb" stroke="#f1df76" stroke-width="2"/>
  </g>

  <g transform="translate(480, 70)">
    <rect width="640" height="260" rx="6" fill="rgba(26, 12, 2, 0.9)" stroke="#f1df76" stroke-width="2"/>
    <rect x="10" y="10" width="620" height="34" fill="#422006"/>
    <text x="24" y="33" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold">CONTAINMENT CHAMBER MK-05 // COHERENCE: 02</text>
    <text x="24" y="80" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-005 — SMOTHERING CRADLE</text>
    <text x="24" y="112" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold">SECC RANK: α (AETHER) · DAMAGE: LAMENT · YIELD: 12 PE</text>
    <line x1="24" y1="128" x2="616" y2="128" stroke="#f1df76" stroke-width="1" stroke-dasharray="4 2"/>
    <text x="24" y="160" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Special Work: Communion (Docerehan 80%) | Danger: Asphyxiation Field</text>
  </g>
</svg>'''
    },

    'se-010': {
        'name': 'The Convergence',
        'code': 'SE-010',
        'risk': 'APOCRYPHA',
        'risk_badge': 'risk-APOCRYPHA',
        'dmg': 'VOID / MIXED',
        'color': '#f8fafc',
        'sub_color': '#ef5b55',
        'profile': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="pGrad_010" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#312e81" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#0f0e26" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#020208" stop-opacity="1"/>
    </radialGradient>
    <filter id="pGlow_010" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="500" height="500" rx="8" fill="url(#pGrad_010)" stroke="#f8fafc" stroke-width="3"/>
  <rect x="15" y="15" width="470" height="470" rx="4" fill="none" stroke="#ef5b55" stroke-width="1.2" stroke-dasharray="8 4" opacity="0.6"/>

  <!-- Multi-Faced Sovereign Convergence Sphere & Eye of Oblivion -->
  <g filter="url(#pGlow_010)">
    <circle cx="250" cy="220" r="140" fill="none" stroke="#f8fafc" stroke-width="2.5" stroke-dasharray="16 8"/>
    <circle cx="250" cy="220" r="100" fill="#020617" stroke="#ef5b55" stroke-width="3"/>
    
    <!-- 8 Intersecting Sovereign Blades of the Crown -->
    <polygon points="250,60 265,180 250,220 235,180" fill="#f1df76"/>
    <polygon points="250,380 265,260 250,220 235,260" fill="#f1df76"/>
    <polygon points="90,220 210,205 250,220 210,235" fill="#f1df76"/>
    <polygon points="410,220 290,205 250,220 290,235" fill="#f1df76"/>
    
    <!-- Pure Existential Void Eye Core -->
    <circle cx="250" cy="220" r="40" fill="#000000" stroke="#f8fafc" stroke-width="3"/>
    <circle cx="250" cy="220" r="18" fill="#f8fafc" filter="url(#pGlow_010)"/>
    <circle cx="250" cy="220" r="6" fill="#ef5b55"/>
  </g>

  <!-- HUD Footer -->
  <rect x="30" y="440" width="440" height="36" rx="4" fill="#030712" stroke="#f8fafc" stroke-width="1.5"/>
  <text x="45" y="463" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">SE-010 // THE CONVERGENCE</text>
  <text x="455" y="463" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">APOCRYPHA · VOID/MIXED</text>
</svg>''',
        'banner': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bGrad_010" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#312e81"/>
      <stop offset="50%" stop-color="#0f0e26"/>
      <stop offset="100%" stop-color="#020208"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#bGrad_010)"/>
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="#f8fafc" stroke-width="3"/>
  
  <g transform="translate(140, 50)">
    <circle cx="140" cy="140" r="110" fill="none" stroke="#f8fafc" stroke-width="2.5" stroke-dasharray="10 5"/>
    <circle cx="140" cy="140" r="40" fill="#000" stroke="#ef5b55" stroke-width="3"/>
    <circle cx="140" cy="140" r="15" fill="#f8fafc"/>
  </g>

  <g transform="translate(480, 70)">
    <rect width="640" height="260" rx="6" fill="rgba(15, 14, 38, 0.9)" stroke="#f8fafc" stroke-width="2"/>
    <rect x="10" y="10" width="620" height="34" fill="#312e81"/>
    <text x="24" y="33" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold">CONTAINMENT CHAMBER MK-10 // COHERENCE: 01</text>
    <text x="24" y="80" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-010 — THE CONVERGENCE</text>
    <text x="24" y="112" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold">SECC RANK: ε (APOCRYPHA) · DAMAGE: VOID/MIXED · YIELD: 44 PE</text>
    <line x1="24" y1="128" x2="616" y2="128" stroke="#f8fafc" stroke-width="1" stroke-dasharray="4 2"/>
    <text x="24" y="160" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Special Work: Restraint (Custodihan 30%) | Danger: Total Reality Efflorescence</text>
    <text x="24" y="185" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="14">Extracted Gear: Absolute Maul (Weapon) / Absolute Mantle (Suit)</text>
  </g>
</svg>'''
    }
}

# Write and sync
dirs_profile = ['/home/user/01_Somnarak_Wiki/assets/art/entities', '/home/user/icons']
dirs_banner = ['/home/user/01_Somnarak_Wiki/assets/art/entities', '/home/user/01_Somnarak_Wiki/assets/banners', '/home/user/icons']

for code, data in entities_data.items():
    p_svg = data['profile']
    b_svg = data['banner']
    num = code.replace('se-', '')
    
    # Write profiles
    p_names = [f'profile_entity_se_{num}.svg', f'profile_entity_se_{int(num):03d}.svg', f'{code}-profile.svg']
    for p_name in p_names:
        for d in dirs_profile:
            os.makedirs(d, exist_ok=True)
            path = os.path.join(d, p_name)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(p_svg)
    
    # Write banners
    b_names = [f'banner_entity_se_{num}.svg', f'banner_entity_se_{int(num):03d}.svg', f'{code}-banner.svg']
    for b_name in b_names:
        for d in dirs_banner:
            os.makedirs(d, exist_ok=True)
            path = os.path.join(d, b_name)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(b_svg)

print('SUCCESS: Upgraded all entity vector profile and banner suites!')
