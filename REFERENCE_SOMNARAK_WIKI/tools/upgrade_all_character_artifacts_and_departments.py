import os

def upgrade_character_artifacts_and_departments():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    icons_dir = os.path.join(wiki_root, "assets/icons")
    avatars_dir = os.path.join(wiki_root, "assets/avatars")
    user_icons_dir = "/home/user/icons"

    # 1. THE 19 HIGHLY PERSONALIZED CHARACTER ARTIFACT & SIGNATURE REGALIA BADGES (120x120 viewBox)
    char_artifacts = {
        # 1. Majin: The Sovereign Crown of 1,778 Cycles atop the Golden Sandglass of Perpetual Command
        "majin": {
            "title": "SOVEREIGN COMMAND",
            "name": "MAJIN",
            "color": "#f1df76",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="gradMajin" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#3d2c05"/>
      <stop offset="70%" stop-color="#1c1402"/>
      <stop offset="100%" stop-color="#080501"/>
    </radialGradient>
    <filter id="glowMajin" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <!-- Chamfered Directorate Crest Frame -->
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="url(#gradMajin)" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="none" stroke="#71efaf" stroke-width="1.2" stroke-dasharray="6 3"/>
  
  <!-- Crossed Sovereign Gold Scepters -->
  <line x1="24" y1="24" x2="96" y2="96" stroke="#f1df76" stroke-width="3.5"/>
  <circle cx="24" cy="24" r="5" fill="#ef5b55" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="96" y1="24" x2="24" y2="96" stroke="#f1df76" stroke-width="3.5"/>
  <circle cx="96" cy="24" r="5" fill="#ef5b55" stroke="#ffffff" stroke-width="1.5"/>
  
  <!-- Dual Celestial Orbital Rings -->
  <ellipse cx="60" cy="58" rx="34" ry="12" fill="none" stroke="#71efaf" stroke-width="1.5" stroke-dasharray="6 3" transform="rotate(-20 60 58)"/>
  <ellipse cx="60" cy="58" rx="34" ry="12" fill="none" stroke="#f1df76" stroke-width="1.5" stroke-dasharray="6 3" transform="rotate(20 60 58)"/>
  
  <!-- Sovereign Golden Hourglass Core -->
  <polygon points="40,38 80,38 46,78 74,78" fill="#450a0a" stroke="#f1df76" stroke-width="2.5"/>
  <!-- Flowing Golden Sand of Cycles -->
  <polygon points="46,42 74,42 60,56" fill="#f1df76" filter="url(#glowMajin)"/>
  <polygon points="60,60 52,74 68,74" fill="#f1df76" filter="url(#glowMajin)"/>
  <line x1="60" y1="56" x2="60" y2="60" stroke="#ffffff" stroke-width="2"/>
  
  <!-- Sovereign Crown Finial -->
  <polygon points="46,26 52,14 60,22 68,14 74,26 46,26" fill="#f1df76" stroke="#ffffff" stroke-width="1"/>
  <circle cx="60" cy="24" r="2.5" fill="#ef5b55"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">SOVEREIGN CORE</text>
</svg>'''
        },

        # 2. Dekan: The Bulwark Gate of Molten Basalt with Triple Hydraulic Clamps & Chains
        "dekan": {
            "title": "CONTAINMENT WARD",
            "name": "DEKAN",
            "color": "#ef5b55",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="gradDekan" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#3b080d"/>
      <stop offset="70%" stop-color="#1f0407"/>
      <stop offset="100%" stop-color="#0a0102"/>
    </radialGradient>
    <filter id="glowDekan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="url(#gradDekan)" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="none" stroke="#ef5b55" stroke-width="1.2" stroke-dasharray="6 3"/>
  
  <!-- Heavy Basalt Vault Gate Slabs -->
  <rect x="24" y="28" width="34" height="60" fill="#2d060a" stroke="#ef5b55" stroke-width="2"/>
  <rect x="62" y="28" width="34" height="60" fill="#2d060a" stroke="#ef5b55" stroke-width="2"/>
  
  <!-- Glowing Magma Runes along Gate Seam -->
  <line x1="59" y1="28" x2="59" y2="88" stroke="#f1df76" stroke-width="2.5" filter="url(#glowDekan)"/>
  <line x1="61" y1="28" x2="61" y2="88" stroke="#ef5b55" stroke-width="1.5"/>
  
  <!-- Triple Heavy Hydraulic Locking Clamps -->
  <rect x="18" y="36" width="84" height="8" rx="2" fill="#ef5b55" stroke="#ffffff" stroke-width="1"/>
  <circle cx="28" cy="40" r="2" fill="#f1df76"/>
  <circle cx="92" cy="40" r="2" fill="#f1df76"/>
  
  <rect x="18" y="54" width="84" height="8" rx="2" fill="#ef5b55" stroke="#ffffff" stroke-width="1"/>
  <circle cx="28" cy="58" r="2" fill="#f1df76"/>
  <circle cx="92" cy="58" r="2" fill="#f1df76"/>
  
  <rect x="18" y="72" width="84" height="8" rx="2" fill="#ef5b55" stroke="#ffffff" stroke-width="1"/>
  <circle cx="28" cy="76" r="2" fill="#f1df76"/>
  <circle cx="92" cy="76" r="2" fill="#f1df76"/>
  
  <!-- Heavy Tungsten Chain Links -->
  <circle cx="20" cy="24" r="4" fill="none" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="100" cy="24" r="4" fill="none" stroke="#f1df76" stroke-width="1.5"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">BASALT BULWARK</text>
</svg>'''
        },

        # 3. Zyrak: The Quartz Reflux Distillation Column with Pressurized Han Siphon Coils
        "zyrak": {
            "title": "FLUX EXTRACTION",
            "name": "ZYRAK",
            "color": "#38bdf8",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="gradZyrak" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#082b4a"/>
      <stop offset="70%" stop-color="#031526"/>
      <stop offset="100%" stop-color="#01070e"/>
    </radialGradient>
    <filter id="glowCyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="url(#gradZyrak)" stroke="#38bdf8" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="6 3"/>
  
  <!-- Distillation Column Quartz Body -->
  <path d="M 46,20 L 74,20 L 74,48 L 88,78 C 90,88 80,94 60,94 C 40,94 30,88 32,78 L 46,48 Z" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2.2"/>
  
  <!-- Glowing Han-Flux Reservoir Fluid -->
  <path d="M 36,80 C 44,72 54,84 60,76 C 66,72 76,82 84,78 C 86,86 78,92 60,92 C 42,92 34,86 36,80 Z" fill="#38bdf8" filter="url(#glowCyan)"/>
  <circle cx="52" cy="62" r="3" fill="#ffffff"/>
  <circle cx="68" cy="54" r="2" fill="#ffffff"/>
  
  <!-- Reflux Cooling Coil Spirals -->
  <path d="M 52,24 C 68,24 68,32 52,32 C 36,32 36,40 52,40 C 68,40 68,48 52,48" fill="none" stroke="#f1df76" stroke-width="2"/>
  
  <!-- Siphon Valves & Brass Pressure Gauge -->
  <circle cx="86" cy="34" r="7" fill="#075985" stroke="#f1df76" stroke-width="1.5"/>
  <line x1="86" y1="34" x2="89" y2="30" stroke="#ef5b55" stroke-width="1.5"/>
  <line x1="74" y1="34" x2="79" y2="34" stroke="#38bdf8" stroke-width="2"/>
  
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">REFLUX SIPHON</text>
</svg>'''
        },

        # 4. Ayshuk: The Armillary Neural Astrolabe with Triple Concentric Rings & Optics
        "ayshuk": {
            "title": "NEURAL FORGE",
            "name": "AYSHUK",
            "color": "#f1df76",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="gradAyshuk" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#3b2b04"/>
      <stop offset="70%" stop-color="#1c1402"/>
      <stop offset="100%" stop-color="#080501"/>
    </radialGradient>
    <filter id="glowGold" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="url(#gradAyshuk)" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="none" stroke="#71efaf" stroke-width="1.2" stroke-dasharray="6 3"/>
  
  <!-- Triple Armillary Brass Rings -->
  <circle cx="60" cy="56" r="30" fill="none" stroke="#f1df76" stroke-width="2" stroke-dasharray="6 3"/>
  <ellipse cx="60" cy="56" rx="30" ry="12" fill="none" stroke="#f1df76" stroke-width="1.8" transform="rotate(-30 60 56)"/>
  <ellipse cx="60" cy="56" rx="30" ry="12" fill="none" stroke="#38bdf8" stroke-width="1.8" transform="rotate(30 60 56)"/>
  <ellipse cx="60" cy="56" rx="12" ry="30" fill="none" stroke="#71efaf" stroke-width="1.2"/>
  
  <!-- Central Prismatic Crystal Core -->
  <polygon points="60,36 76,66 44,66" fill="#fef08a" stroke="#ffffff" stroke-width="1.5" filter="url(#glowGold)"/>
  <circle cx="60" cy="56" r="5" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>
  
  <!-- Dual Microscope Optical Objective Lens Vectors -->
  <line x1="32" y1="28" x2="88" y2="84" stroke="#ffffff" stroke-width="1.2" stroke-dasharray="3 3"/>
  <line x1="88" y1="28" x2="32" y2="84" stroke="#ffffff" stroke-width="1.2" stroke-dasharray="3 3"/>
  
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">ARMILLARY OPTIC</text>
</svg>'''
        },

        # 5. Mellda: The Fortified Trench Aegis Shield with Spiked Parapet Crest & Slit
        "mellda": {
            "title": "BULWARK WATCH",
            "name": "MELLDA",
            "color": "#ef5b55",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="gradMellda" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#3b080d"/>
      <stop offset="70%" stop-color="#1f0407"/>
      <stop offset="100%" stop-color="#0a0102"/>
    </radialGradient>
    <filter id="glowMellda" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="url(#gradMellda)" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="none" stroke="#ef5b55" stroke-width="1.2" stroke-dasharray="6 3"/>
  
  <!-- Heavy Trench Tower Shield Silhouette -->
  <polygon points="34,22 86,22 80,82 60,94 40,82" fill="#450a0a" stroke="#ef5b55" stroke-width="2.5"/>
  
  <!-- Spiked Parapet Battlements atop Shield -->
  <polygon points="34,22 42,14 50,22 60,12 70,22 78,14 86,22" fill="#ef5b55" stroke="#ffffff" stroke-width="1"/>
  
  <!-- Glowing Horizontal Visor Slit -->
  <rect x="42" y="44" width="36" height="6" rx="2" fill="#f1df76" stroke="#ffffff" stroke-width="1" filter="url(#glowMellda)"/>
  
  <!-- Heavy Tungsten Rivets -->
  <circle cx="40" cy="32" r="2" fill="#e2e8f0"/>
  <circle cx="80" cy="32" r="2" fill="#e2e8f0"/>
  <circle cx="44" cy="74" r="2" fill="#e2e8f0"/>
  <circle cx="76" cy="74" r="2" fill="#e2e8f0"/>
  <circle cx="60" cy="84" r="2" fill="#e2e8f0"/>
  
  <!-- Crossed Trench Barbed Wires -->
  <line x1="26" y1="56" x2="94" y2="56" stroke="#f1df76" stroke-width="1.8"/>
  <line x1="38" y1="52" x2="42" y2="60" stroke="#f1df76" stroke-width="2"/>
  <line x1="78" y1="52" x2="82" y2="60" stroke="#f1df76" stroke-width="2"/>
  
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">AEGIS BULWARK</text>
</svg>'''
        },

        # 6. Marjuk: The Deep Vault Chronometer with Tri-Axial Rotary Gears & Data Slate
        "marjuk": {
            "title": "CRYO ARCHIVES",
            "name": "MARJUK",
            "color": "#c084fc",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="gradMarjuk" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2c0b4d"/>
      <stop offset="70%" stop-color="#140424"/>
      <stop offset="100%" stop-color="#07010d"/>
    </radialGradient>
    <filter id="glowPurple" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="url(#gradMarjuk)" stroke="#c084fc" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="6 3"/>
  
  <!-- Outer Chronometer Gear Rim -->
  <circle cx="60" cy="56" r="30" fill="#3b0764" stroke="#c084fc" stroke-width="2.5"/>
  <!-- Gear Teeth -->
  <rect x="57" y="22" width="6" height="6" fill="#f1df76"/>
  <rect x="57" y="84" width="6" height="6" fill="#f1df76"/>
  <rect x="26" y="53" width="6" height="6" fill="#f1df76"/>
  <rect x="88" y="53" width="6" height="6" fill="#f1df76"/>
  
  <!-- Hexagonal Encrypted Cryo Data Slate -->
  <polygon points="60,36 78,46 78,66 60,76 42,66 42,46" fill="#1e053a" stroke="#38bdf8" stroke-width="1.8"/>
  
  <!-- Sub-Zero Frost Starburst -->
  <polygon points="60,42 63,53 74,56 63,59 60,70 57,59 46,56 57,53" fill="#c084fc" filter="url(#glowPurple)"/>
  <circle cx="60" cy="56" r="4" fill="#ffffff"/>
  
  <text x="60" y="104" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">CRYO CHRONOMETER</text>
</svg>'''
        },

        # 7. Ishall: Twin Serrated Obsidian Assassin Daggers with Void Smoke Shroud & HUD
        "ishall": {
            "title": "SHADOW CORPS",
            "name": "ISHALL",
            "color": "#ef5b55",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="gradIshall" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2b050a"/>
      <stop offset="70%" stop-color="#120204"/>
      <stop offset="100%" stop-color="#050001"/>
    </radialGradient>
    <filter id="glowIshall" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="url(#gradIshall)" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="none" stroke="#ffffff" stroke-width="1.2" stroke-dasharray="6 3"/>
  
  <!-- Stealth HUD Target Crosshair -->
  <circle cx="60" cy="56" r="28" fill="none" stroke="#ef5b55" stroke-width="1" stroke-dasharray="4 3" opacity="0.7"/>
  <line x1="60" y1="24" x2="60" y2="88" stroke="#ef5b55" stroke-width="0.8" opacity="0.6"/>
  <line x1="28" y1="56" x2="92" y2="56" stroke="#ef5b55" stroke-width="0.8" opacity="0.6"/>
  
  <!-- Twin Serrated Obsidian Daggers Crossed -->
  <g filter="url(#glowIshall)">
    <polygon points="32,28 78,74 72,80 26,34" fill="#0f172a" stroke="#f8fafc" stroke-width="1.5"/>
    <polygon points="88,28 42,74 48,80 94,34" fill="#0f172a" stroke="#f8fafc" stroke-width="1.5"/>
  </g>
  
  <!-- Serrated Blade Teeth & Crimson Edge Glow -->
  <line x1="36" y1="32" x2="74" y2="70" stroke="#ef5b55" stroke-width="2"/>
  <line x1="84" y1="32" x2="46" y2="70" stroke="#ef5b55" stroke-width="2"/>
  
  <!-- Hilt Guards with Golden Inlay -->
  <rect x="22" y="32" width="10" height="4" rx="1" fill="#f1df76"/>
  <rect x="88" y="32" width="10" height="4" rx="1" fill="#f1df76"/>
  
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">OBSIDIAN STILETTO</text>
</svg>'''
        },

        # 8. Xyan: Shattered Iron Exile Shackles with Abyssal Boundary Keystones
        "xyan": {
            "title": "ABYSSAL GATE",
            "name": "XYAN",
            "color": "#f1df76",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="gradXyan" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#3b2605"/>
      <stop offset="70%" stop-color="#1c1303"/>
      <stop offset="100%" stop-color="#080400"/>
    </radialGradient>
    <filter id="glowXyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="url(#gradXyan)" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="none" stroke="#c084fc" stroke-width="1.2" stroke-dasharray="6 3"/>
  
  <!-- Cyclopean Stone Gate Silhouette -->
  <path d="M 28,84 L 28,34 Q 60,16 92,34 L 92,84 L 80,84 L 80,44 Q 60,30 40,44 L 40,84 Z" fill="#451a03" stroke="#f1df76" stroke-width="2.2"/>
  
  <!-- Shattered Exile Shackles -->
  <g transform="translate(60, 56)">
    <!-- Left Broken Cuff -->
    <path d="M -22,-8 A 12 12 0 1 0 -10,8" fill="none" stroke="#e2e8f0" stroke-width="3.5"/>
    <!-- Right Broken Cuff -->
    <path d="M 22,-8 A 12 12 0 1 1 10,8" fill="none" stroke="#e2e8f0" stroke-width="3.5"/>
    <!-- Snapped Central Chain Link -->
    <line x1="-8" y1="0" x2="-2" y2="0" stroke="#f1df76" stroke-width="2.5"/>
    <line x1="2" y1="0" x2="8" y2="0" stroke="#f1df76" stroke-width="2.5"/>
    <polygon points="0,-4 3,4 -3,4" fill="#ef5b55" filter="url(#glowXyan)"/>
  </g>
  
  <!-- Abyssal Ward Runes -->
  <circle cx="60" cy="24" r="4.5" fill="#c084fc" filter="url(#glowXyan)"/>
  <circle cx="60" cy="24" r="2" fill="#ffffff"/>
  
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">EXILE SHACKLES</text>
</svg>'''
        },

        # 9. Doha: The Golden Balance Scales of Antiquity
        "doha": {
            "title": "ANTIQUITIES MERCH",
            "name": "DOHA",
            "color": "#f1df76",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#261704" stroke="#f1df76" stroke-width="3.5"/>
  <!-- Central Balance Pillar -->
  <line x1="60" y1="22" x2="60" y2="84" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="50,84 70,84 60,78" fill="#f1df76"/>
  <!-- Balance Beam -->
  <line x1="26" y1="36" x2="94" y2="36" stroke="#f1df76" stroke-width="3"/>
  <circle cx="60" cy="36" r="4" fill="#ffffff"/>
  <!-- Left Pan with Ancient Coins -->
  <line x1="28" y1="36" x2="22" y2="60" stroke="#94a3b8" stroke-width="1.2"/>
  <line x1="28" y1="36" x2="34" y2="60" stroke="#94a3b8" stroke-width="1.2"/>
  <path d="M 18,60 Q 28,66 38,60 Z" fill="#eab308" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="28" cy="54" r="3.5" fill="#fef08a"/>
  <!-- Right Pan with Raw Runic Ore Ingot -->
  <line x1="92" y1="36" x2="86" y2="60" stroke="#94a3b8" stroke-width="1.2"/>
  <line x1="92" y1="36" x2="98" y2="60" stroke="#94a3b8" stroke-width="1.2"/>
  <path d="M 82,60 Q 92,66 102,60 Z" fill="#eab308" stroke="#f1df76" stroke-width="1.5"/>
  <rect x="86" y="50" width="12" height="8" rx="1" fill="#ef5b55" stroke="#f1df76" stroke-width="1"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">BALANCE OF ANTIQUITY</text>
</svg>'''
        },

        # 10. Minho: Heavy Pneumatic War Hammer with Shockwave Vents
        "minho": {
            "title": "KINETIC WARDEN",
            "name": "MINHO",
            "color": "#ef5b55",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#260408" stroke="#ef5b55" stroke-width="3.5"/>
  <!-- Pneumatic Hammer Shaft -->
  <line x1="30" y1="90" x2="76" y2="44" stroke="#94a3b8" stroke-width="4"/>
  <rect x="26" y="84" width="12" height="6" rx="1" fill="#ef5b55"/>
  <!-- Colossal Hammer Head with Pneumatic Vents -->
  <rect x="66" y="24" width="36" height="24" rx="3" fill="#450a0a" stroke="#ef5b55" stroke-width="2" transform="rotate(-45 84 36)"/>
  <!-- Kinetic Impact Piston -->
  <rect x="80" y="28" width="8" height="16" fill="#f1df76" transform="rotate(-45 84 36)"/>
  <!-- Shockwave Cones -->
  <polygon points="86,18 96,12 92,24" fill="#f1df76"/>
  <polygon points="98,30 106,28 100,38" fill="#f1df76"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">PNEUMATIC SLEDGE</text>
</svg>'''
        },

        # 11. Yeonhwa: Multi-Chamber Glass Siphon Needle with Micro-Valves
        "yeonhwa": {
            "title": "MASTER SIPHON",
            "name": "YEONHWA",
            "color": "#38bdf8",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#041b2c" stroke="#38bdf8" stroke-width="3.5"/>
  <!-- Siphon Needle Plunger & Glass Barrel -->
  <rect x="52" y="20" width="16" height="56" rx="2" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
  <!-- Han Fluid Level -->
  <rect x="54" y="44" width="12" height="30" fill="#38bdf8"/>
  <line x1="52" y1="50" x2="68" y2="50" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="52" y1="60" x2="68" y2="60" stroke="#ffffff" stroke-width="1.5"/>
  <!-- Needle Tip -->
  <polygon points="56,76 64,76 60,94" fill="#94a3b8" stroke="#ffffff" stroke-width="1"/>
  <!-- Top Plunger Handle -->
  <line x1="44" y1="16" x2="76" y2="16" stroke="#f1df76" stroke-width="3"/>
  <line x1="60" y1="16" x2="60" y2="20" stroke="#f1df76" stroke-width="3"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">SIPHON NEEDLE</text>
</svg>'''
        },

        # 12. Seiyon: Prismatic Neural Crystal Lattice
        "seiyon": {
            "title": "NEURAL WEAVER",
            "name": "SEIYON",
            "color": "#71efaf",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#021f14" stroke="#71efaf" stroke-width="3.5"/>
  <!-- Neural Synaptic Lattice -->
  <circle cx="60" cy="54" r="8" fill="#71efaf" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="34" cy="38" r="5" fill="#064e3b" stroke="#71efaf" stroke-width="1.5"/>
  <circle cx="86" cy="38" r="5" fill="#064e3b" stroke="#71efaf" stroke-width="1.5"/>
  <circle cx="34" cy="70" r="5" fill="#064e3b" stroke="#71efaf" stroke-width="1.5"/>
  <circle cx="86" cy="70" r="5" fill="#064e3b" stroke="#71efaf" stroke-width="1.5"/>
  <circle cx="60" cy="24" r="4" fill="#f1df76"/>
  <circle cx="60" cy="84" r="4" fill="#f1df76"/>
  <!-- Interconnecting Synaptic Lasers -->
  <line x1="60" y1="54" x2="34" y2="38" stroke="#71efaf" stroke-width="1.5"/>
  <line x1="60" y1="54" x2="86" y2="38" stroke="#71efaf" stroke-width="1.5"/>
  <line x1="60" y1="54" x2="34" y2="70" stroke="#71efaf" stroke-width="1.5"/>
  <line x1="60" y1="54" x2="86" y2="70" stroke="#71efaf" stroke-width="1.5"/>
  <line x1="60" y1="54" x2="60" y2="24" stroke="#f1df76" stroke-width="1.5"/>
  <line x1="60" y1="54" x2="60" y2="84" stroke="#f1df76" stroke-width="1.5"/>
  <text x="60" y="104" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">SYNAPSE LATTICE</text>
</svg>'''
        },

        # 13. Taeho: Heavy Barricade Barrier Shield with Titanium Rebar
        "taeho": {
            "title": "BULWARK SENTINEL",
            "name": "TAEHO",
            "color": "#ef5b55",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#260408" stroke="#ef5b55" stroke-width="3.5"/>
  <!-- Barricade Shield Body -->
  <polygon points="26,26 94,26 84,84 60,94 36,84" fill="#450a0a" stroke="#ef5b55" stroke-width="2.5"/>
  <!-- Warning Hazard Stripes -->
  <line x1="36" y1="36" x2="84" y2="36" stroke="#f1df76" stroke-width="3"/>
  <line x1="40" y1="48" x2="80" y2="48" stroke="#ef5b55" stroke-width="3"/>
  <line x1="44" y1="60" x2="76" y2="60" stroke="#f1df76" stroke-width="3"/>
  <!-- Titanium Cross Rebar -->
  <line x1="34" y1="28" x2="86" y2="80" stroke="#e2e8f0" stroke-width="2"/>
  <line x1="86" y1="28" x2="34" y2="80" stroke="#e2e8f0" stroke-width="2"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">TITANIUM BARRICADE</text>
</svg>'''
        },

        # 14. Soojin: Cryogenic Scroll Capsule with Holographic Data Projection
        "soojin": {
            "title": "CRYO ARCHIVIST",
            "name": "SOOJIN",
            "color": "#c084fc",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1b062c" stroke="#c084fc" stroke-width="3.5"/>
  <!-- Cylindrical Cryo Capsule -->
  <rect x="42" y="24" width="36" height="58" rx="6" fill="#3b0764" stroke="#c084fc" stroke-width="2"/>
  <line x1="42" y1="36" x2="78" y2="36" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="42" y1="70" x2="78" y2="70" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Holographic Projected Data Rings -->
  <ellipse cx="60" cy="53" rx="28" ry="8" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 2"/>
  <circle cx="60" cy="53" r="6" fill="#c084fc" stroke="#ffffff" stroke-width="1"/>
  <text x="60" y="104" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">CRYO DATA CAPSULE</text>
</svg>'''
        },

        # 15. Kael: Triple Obsidian Kunai on Sonar HUD Compass
        "kael": {
            "title": "SHADOW INFILTRATOR",
            "name": "KAEL",
            "color": "#ef5b55",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#140205" stroke="#ef5b55" stroke-width="3.5"/>
  <!-- Radar Sonar Sweep Grid -->
  <circle cx="60" cy="54" r="26" fill="none" stroke="#ef5b55" stroke-width="1" stroke-dasharray="4 2"/>
  <line x1="60" y1="26" x2="60" y2="82" stroke="#ef5b55" stroke-width="0.8"/>
  <line x1="32" y1="54" x2="88" y2="54" stroke="#ef5b55" stroke-width="0.8"/>
  <!-- Triple Fanned Obsidian Kunai -->
  <polygon points="60,18 64,52 60,62 56,52" fill="#e2e8f0" stroke="#ef5b55" stroke-width="1.2"/>
  <polygon points="34,30 52,60 48,68 40,56" fill="#e2e8f0" stroke="#ef5b55" stroke-width="1.2"/>
  <polygon points="86,30 80,56 72,68 68,60" fill="#e2e8f0" stroke="#ef5b55" stroke-width="1.2"/>
  <circle cx="60" cy="66" r="3" fill="#f1df76"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">TRIPLE OBSIDIAN KUNAI</text>
</svg>'''
        },

        # 16. Sora: Heavy Iron Boundary Lantern with Violet Flame & Ward Bells
        "sora": {
            "title": "THRESHOLD WATCHER",
            "name": "SORA",
            "color": "#f1df76",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#241502" stroke="#f1df76" stroke-width="3.5"/>
  <!-- Boundary Iron Lantern Frame -->
  <polygon points="46,30 74,30 80,72 40,72" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
  <polygon points="42,30 60,16 78,30" fill="#f1df76"/>
  <circle cx="60" cy="14" r="3" fill="none" stroke="#f1df76" stroke-width="1.5"/>
  <!-- Violet Abyssal Ward Flame Core -->
  <circle cx="60" cy="52" r="10" fill="#c084fc"/>
  <polygon points="60,38 65,50 55,50" fill="#ffffff"/>
  <!-- Dangling Ward Bells -->
  <circle cx="40" cy="78" r="3.5" fill="#f1df76"/>
  <circle cx="80" cy="78" r="3.5" fill="#f1df76"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">BOUNDARY LANTERN</text>
</svg>'''
        },

        # 17. Joon: Pressurized Han Storage Cylinder with Pressure Gauge
        "joon": {
            "title": "HAN REFINER",
            "name": "JOON",
            "color": "#38bdf8",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#041b2c" stroke="#38bdf8" stroke-width="3.5"/>
  <!-- High Pressure Gas Cylinder -->
  <rect x="42" y="26" width="36" height="56" rx="8" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
  <rect x="46" y="40" width="28" height="34" rx="2" fill="#0284c7"/>
  <!-- Pressure Dial Gauge -->
  <circle cx="60" cy="18" r="7" fill="#082f49" stroke="#f1df76" stroke-width="1.5"/>
  <line x1="60" y1="18" x2="64" y2="15" stroke="#ef5b55" stroke-width="1.5"/>
  <line x1="60" y1="24" x2="60" y2="28" stroke="#38bdf8" stroke-width="2"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">PRESSURE CYLINDER</text>
</svg>'''
        },

        # 18. High Architects: Geometric Drafting Compass & Sovereign Ratio Calipers
        "high_architects": {
            "title": "INNER RING",
            "name": "ARCHITECTS",
            "color": "#f1df76",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#241903" stroke="#f1df76" stroke-width="3.5"/>
  <!-- Drafting Compass Arms -->
  <polygon points="56,20 64,20 86,84 76,84" fill="#f1df76" stroke="#ffffff" stroke-width="1"/>
  <polygon points="56,20 64,20 44,84 34,84" fill="#f1df76" stroke="#ffffff" stroke-width="1"/>
  <circle cx="60" cy="22" r="6" fill="#eab308" stroke="#ffffff" stroke-width="1.5"/>
  <!-- Circular Measuring Arc -->
  <path d="M 40,62 Q 60,72 80,62" fill="none" stroke="#71efaf" stroke-width="2" stroke-dasharray="3 3"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">DRAFTING COMPASS</text>
</svg>'''
        },

        # 19. Cheonbulok Refugees: Cracked Nomadic Stone Bowl Sheltering Spark of Hope
        "cheonbulok_refugees": {
            "title": "THE DISPLACED",
            "name": "REFUGEES",
            "color": "#cbd5e1",
            "svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#111827" stroke="#cbd5e1" stroke-width="3.5"/>
  <!-- Cracked Nomadic Stone Vessel -->
  <path d="M 28,52 C 28,78 92,78 92,52 L 28,52 Z" fill="#334155" stroke="#cbd5e1" stroke-width="2"/>
  <!-- Fissure Crack in Bowl -->
  <path d="M 60,74 L 56,64 L 64,58 L 60,52" fill="none" stroke="#f1df76" stroke-width="1.8"/>
  <!-- Glowing Spark of Hope Sheltered Inside -->
  <circle cx="60" cy="44" r="7" fill="#fef08a" stroke="#ffffff" stroke-width="1.5"/>
  <polygon points="60,32 63,40 70,44 63,48 60,56 57,48 50,44 57,40" fill="#f1df76"/>
  <text x="60" y="104" fill="#cbd5e1" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">SHELTERED SPARK</text>
</svg>'''
        }
    }

    # Write avatars and character icons
    for k, data in char_artifacts.items():
        # avatar_core_*.svg / avatar_char_*.svg
        prefix = "avatar_core" if k in ["majin", "dekan", "zyrak", "ayshuk", "mellda", "marjuk", "ishall", "xyan"] else "avatar_char"
        fname_avatar = f"{prefix}_{k}.svg"
        fname_icon = f"icon_char_{k}.svg"
        fname_core = f"icon_core_{k}.svg"
        fname_char = f"char_{k}.svg"

        for fn in [fname_avatar, fname_icon, fname_core, fname_char]:
            with open(os.path.join(avatars_dir, fn), "w", encoding="utf-8") as f:
                f.write(data["svg"])
            with open(os.path.join(icons_dir, fn), "w", encoding="utf-8") as f:
                f.write(data["svg"])
            with open(os.path.join(user_icons_dir, fn), "w", encoding="utf-8") as f:
                f.write(data["svg"])

    print("Created 19 ultra-detailed, highly personalized Character Artifact & Signature Regalia Emblems!")

    # -------------------------------------------------------------
    # 2. DEPARTMENT & SECTOR CRESTS (120x120 & 200x200 viewBox)
    # -------------------------------------------------------------
    departments = {
        "f1_neutral": ("NEUTRAL CORE", "#71efaf", "#02140d", "01"),
        "f2_maws_keep": ("MAW'S KEEP", "#ef5b55", "#1f0608", "02"),
        "f3_extraction": ("EXTRACTION", "#38bdf8", "#031526", "03"),
        "f4_insight_forge": ("INSIGHT FORGE", "#f1df76", "#1c1402", "04"),
        "f5_border_watch": ("BORDER WATCH", "#ef5b55", "#1c0709", "05"),
        "f6_deep_vault": ("DEEP VAULT", "#c084fc", "#130421", "06"),
        "f7_shadow_corps": ("SHADOW CORPS", "#ef5b55", "#120204", "07"),
        "f8_gate_watch": ("GATE WATCH", "#f1df76", "#1c1303", "08")
    }

    for k, (name, col, bg, num) in departments.items():
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="{bg}" stroke="{col}" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="none" stroke="{col}" stroke-width="1.2" stroke-dasharray="6 3"/>
  <circle cx="60" cy="50" r="22" fill="none" stroke="{col}" stroke-width="2"/>
  <text x="60" y="58" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="bold" text-anchor="middle">{num}</text>
  <text x="60" y="86" fill="{col}" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">{name}</text>
  <text x="60" y="98" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="6.5" font-weight="bold" text-anchor="middle">FACILITY 01 // SECTOR</text>
</svg>'''
        for prefix in ["icon_dept_", "icon_dept_badge_", "dept_", "fac_"]:
            fname = f"{prefix}{k}.svg"
            with open(os.path.join(icons_dir, fname), "w", encoding="utf-8") as f:
                f.write(svg)
            with open(os.path.join(user_icons_dir, fname), "w", encoding="utf-8") as f:
                f.write(svg)

    print("Created Department and Sector Crests!")

if __name__ == "__main__":
    upgrade_character_artifacts_and_departments()
