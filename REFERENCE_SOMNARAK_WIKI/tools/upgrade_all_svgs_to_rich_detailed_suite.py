import os

def generate_rich_svg_suite():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    assets_dir = os.path.join(wiki_root, "assets")
    icons_dir = os.path.join(assets_dir, "icons")
    banners_dir = os.path.join(assets_dir, "banners")
    avatars_dir = os.path.join(assets_dir, "avatars")
    user_icons_dir = "/home/user/icons"

    os.makedirs(icons_dir, exist_ok=True)
    os.makedirs(banners_dir, exist_ok=True)
    os.makedirs(avatars_dir, exist_ok=True)
    os.makedirs(user_icons_dir, exist_ok=True)

    # -------------------------------------------------------------
    # 1. BESPOKE RICH FLOOR MINI-BANNERS (340x85 Tactical HUD Layouts)
    # -------------------------------------------------------------
    floor_banners = {
        "floor_banner_f1_neutral.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <defs>
    <linearGradient id="bgF1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#02140d"/>
      <stop offset="50%" stop-color="#052418"/>
      <stop offset="100%" stop-color="#020d09"/>
    </linearGradient>
    <linearGradient id="goldGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="50%" stop-color="#f1df76"/>
      <stop offset="100%" stop-color="#ca8a04"/>
    </linearGradient>
    <filter id="glowF1" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <!-- Background with Chamfered Cybernetic Border -->
  <polygon points="2,8 8,2 332,2 338,8 338,77 332,83 8,83 2,77" fill="url(#bgF1)" stroke="#71efaf" stroke-width="2"/>
  <!-- Tactical Gridlines & Crosshairs -->
  <line x1="8" y1="20" x2="332" y2="20" stroke="#71efaf" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="8" y1="65" x2="332" y2="65" stroke="#71efaf" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="72" y1="6" x2="72" y2="79" stroke="#71efaf" stroke-width="0.8" opacity="0.4"/>
  
  <!-- Left Chamber Centerpiece: High-Tech Sovereign Command Ziggurat -->
  <g transform="translate(10, 8)">
    <polygon points="28,6 50,56 6,56" fill="#064e3b" stroke="#71efaf" stroke-width="1.8"/>
    <!-- Layered Pyramid Levels -->
    <polygon points="28,14 42,46 14,46" fill="#042f24" stroke="#71efaf" stroke-width="1"/>
    <polygon points="28,22 36,36 20,36" fill="#021f18" stroke="#f1df76" stroke-width="1"/>
    <!-- Sovereign Golden Halo Rings -->
    <ellipse cx="28" cy="24" rx="22" ry="7" fill="none" stroke="url(#goldGrad1)" stroke-width="1.5" stroke-dasharray="5 3"/>
    <ellipse cx="28" cy="24" rx="14" ry="4.5" fill="none" stroke="#71efaf" stroke-width="1"/>
    <!-- Apex Beacon Eye -->
    <circle cx="28" cy="10" r="4.5" fill="url(#goldGrad1)" filter="url(#glowF1)"/>
    <circle cx="28" cy="10" r="1.5" fill="#ffffff"/>
    <!-- Base Pedestal & Tech Struts -->
    <rect x="10" y="56" width="36" height="5" rx="1" fill="#0f766e" stroke="#71efaf" stroke-width="1"/>
    <line x1="16" y1="61" x2="16" y2="67" stroke="#71efaf" stroke-width="1.5"/>
    <line x1="40" y1="61" x2="40" y2="67" stroke="#71efaf" stroke-width="1.5"/>
  </g>

  <!-- Department & Lead Metadata -->
  <text x="82" y="21" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" letter-spacing="1.5">[F1 // SOVEREIGN PALM CORE]</text>
  <text x="82" y="42" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" letter-spacing="0.5">NEUTRAL COMMAND</text>
  <text x="82" y="58" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">DIRECTOR: <tspan fill="#f1df76" font-weight="bold">MAJIN</tspan> | DEPTH: <tspan fill="#71efaf">-200M</tspan></text>
  
  <!-- Mini Status Gauge & Telemetry -->
  <rect x="82" y="66" width="60" height="6" rx="1" fill="#064e3b" stroke="#71efaf" stroke-width="0.8"/>
  <rect x="83" y="67" width="52" height="4" rx="0.5" fill="#71efaf"/>
  <text x="148" y="72" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="7.5">RES: 98.6%</text>

  <!-- Right Hazard Bar & Dynamic Chevron -->
  <g transform="translate(306, 22)">
    <polygon points="12,20 0,8 4,4 20,20 4,36 0,32" fill="#71efaf"/>
    <line x1="-10" y1="0" x2="-10" y2="40" stroke="#71efaf" stroke-width="1" stroke-dasharray="3 3"/>
  </g>
</svg>''',

        "floor_banner_f2_maws_keep.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <defs>
    <linearGradient id="bgF2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#200609"/>
      <stop offset="50%" stop-color="#3d0c12"/>
      <stop offset="100%" stop-color="#140305"/>
    </linearGradient>
    <linearGradient id="crimsonGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fca5a5"/>
      <stop offset="50%" stop-color="#ef5b55"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <filter id="glowF2" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="2,8 8,2 332,2 338,8 338,77 332,83 8,83 2,77" fill="url(#bgF2)" stroke="#ef5b55" stroke-width="2"/>
  <!-- Tactical Gridlines -->
  <line x1="8" y1="20" x2="332" y2="20" stroke="#ef5b55" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="8" y1="65" x2="332" y2="65" stroke="#ef5b55" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="72" y1="6" x2="72" y2="79" stroke="#ef5b55" stroke-width="0.8" opacity="0.4"/>

  <!-- Left Chamber Centerpiece: Basalt Containment Blast Forge & Heavy Kinetic Hammer -->
  <g transform="translate(10, 8)">
    <!-- Heavy Anvil Foundation -->
    <path d="M 12,48 L 48,48 L 44,58 L 38,58 L 42,68 L 52,72 L 8,72 L 18,68 L 22,58 L 16,58 Z" fill="#4c0519" stroke="#ef5b55" stroke-width="1.8"/>
    <!-- Molten Glowing Crevices -->
    <line x1="20" y1="52" x2="40" y2="52" stroke="#f1df76" stroke-width="2" filter="url(#glowF2)"/>
    <!-- Kinetic Power Hammer Striking Anvil -->
    <rect x="22" y="24" width="16" height="14" rx="2" fill="url(#crimsonGrad2)" stroke="#ffffff" stroke-width="1.2"/>
    <rect x="18" y="32" width="24" height="4" fill="#f1df76"/>
    <line x1="30" y1="8" x2="30" y2="24" stroke="#e2e8f0" stroke-width="3"/>
    <!-- Heavy Containment Chain Brackets -->
    <circle cx="10" cy="30" r="4" fill="none" stroke="#f1df76" stroke-width="1.5"/>
    <circle cx="50" cy="30" r="4" fill="none" stroke="#f1df76" stroke-width="1.5"/>
    <line x1="14" y1="30" x2="22" y2="30" stroke="#ef5b55" stroke-width="1.2"/>
    <line x1="38" y1="30" x2="46" y2="30" stroke="#ef5b55" stroke-width="1.2"/>
  </g>

  <!-- Metadata -->
  <text x="82" y="21" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" letter-spacing="1.5">[F2 // KINETIC FORGE]</text>
  <text x="82" y="42" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" letter-spacing="0.5">MAW'S KEEP</text>
  <text x="82" y="58" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">LEAD: <tspan fill="#f1df76" font-weight="bold">DEKAN</tspan> | DEPTH: <tspan fill="#ef5b55">-400M</tspan></text>
  
  <rect x="82" y="66" width="60" height="6" rx="1" fill="#4c0519" stroke="#ef5b55" stroke-width="0.8"/>
  <rect x="83" y="67" width="46" height="4" rx="0.5" fill="#ef5b55"/>
  <text x="148" y="72" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="7.5">DAMP: 88.2%</text>

  <g transform="translate(306, 22)">
    <polygon points="12,20 0,8 4,4 20,20 4,36 0,32" fill="#ef5b55"/>
    <line x1="-10" y1="0" x2="-10" y2="40" stroke="#ef5b55" stroke-width="1" stroke-dasharray="3 3"/>
  </g>
</svg>''',

        "floor_banner_f3_extraction.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <defs>
    <linearGradient id="bgF3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#031526"/>
      <stop offset="50%" stop-color="#082b4a"/>
      <stop offset="100%" stop-color="#020e1a"/>
    </linearGradient>
    <linearGradient id="cyanGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#bae6fd"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <filter id="glowF3" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="2,8 8,2 332,2 338,8 338,77 332,83 8,83 2,77" fill="url(#bgF3)" stroke="#38bdf8" stroke-width="2"/>
  <line x1="8" y1="20" x2="332" y2="20" stroke="#38bdf8" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="8" y1="65" x2="332" y2="65" stroke="#38bdf8" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="72" y1="6" x2="72" y2="79" stroke="#38bdf8" stroke-width="0.8" opacity="0.4"/>

  <!-- Left Centerpiece: Reflux Han-Flux Distillation Tower & Pressure Tubes -->
  <g transform="translate(10, 8)">
    <!-- Glass Retort Chamber -->
    <path d="M 24,14 L 36,14 L 36,32 L 48,56 C 52,66 42,72 30,72 C 18,72 8,66 12,56 L 24,32 Z" fill="#082f49" stroke="#38bdf8" stroke-width="1.8"/>
    <!-- Glowing Boiling Han-Flux Fluid -->
    <path d="M 14,58 C 18,52 26,62 30,56 C 34,52 42,60 46,58 C 47,65 40,70 30,70 C 20,70 13,65 14,58 Z" fill="url(#cyanGrad3)" filter="url(#glowF3)"/>
    <circle cx="26" cy="46" r="2.5" fill="#ffffff"/>
    <circle cx="34" cy="40" r="1.5" fill="#ffffff"/>
    <!-- Condenser Spiral Coil -->
    <path d="M 28,18 C 34,18 34,24 28,24 C 22,24 22,30 28,30" fill="none" stroke="#f1df76" stroke-width="1.5"/>
    <!-- Siphon Valve & Pressure Dials -->
    <circle cx="48" cy="24" r="5" fill="#0c4a6e" stroke="#f1df76" stroke-width="1.2"/>
    <line x1="48" y1="24" x2="50" y2="21" stroke="#ef5b55" stroke-width="1.2"/>
    <line x1="36" y1="24" x2="43" y2="24" stroke="#38bdf8" stroke-width="1.5"/>
  </g>

  <text x="82" y="21" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" letter-spacing="1.5">[F3 // FLUX SIPHON HALL]</text>
  <text x="82" y="42" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" letter-spacing="0.5">EXTRACTION HALL</text>
  <text x="82" y="58" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">LEAD: <tspan fill="#f1df76" font-weight="bold">ZYRAK</tspan> | DEPTH: <tspan fill="#38bdf8">-600M</tspan></text>
  
  <rect x="82" y="66" width="60" height="6" rx="1" fill="#082f49" stroke="#38bdf8" stroke-width="0.8"/>
  <rect x="83" y="67" width="56" height="4" rx="0.5" fill="#38bdf8"/>
  <text x="148" y="72" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="7.5">FLUX: 94.7%</text>

  <g transform="translate(306, 22)">
    <polygon points="12,20 0,8 4,4 20,20 4,36 0,32" fill="#38bdf8"/>
    <line x1="-10" y1="0" x2="-10" y2="40" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3 3"/>
  </g>
</svg>''',

        "floor_banner_f4_insight_forge.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <defs>
    <linearGradient id="bgF4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1c1402"/>
      <stop offset="50%" stop-color="#3d2c05"/>
      <stop offset="100%" stop-color="#120c01"/>
    </linearGradient>
    <linearGradient id="goldGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="50%" stop-color="#f1df76"/>
      <stop offset="100%" stop-color="#eab308"/>
    </linearGradient>
    <filter id="glowF4" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="2,8 8,2 332,2 338,8 338,77 332,83 8,83 2,77" fill="url(#bgF4)" stroke="#f1df76" stroke-width="2"/>
  <line x1="8" y1="20" x2="332" y2="20" stroke="#f1df76" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="8" y1="65" x2="332" y2="65" stroke="#f1df76" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="72" y1="6" x2="72" y2="79" stroke="#f1df76" stroke-width="0.8" opacity="0.4"/>

  <!-- Left Centerpiece: Armillary Astrolabe & Prismatic Neural Prism -->
  <g transform="translate(10, 8)">
    <!-- Concentric Armillary Rings -->
    <circle cx="30" cy="38" r="24" fill="none" stroke="#f1df76" stroke-width="1.5" stroke-dasharray="6 3"/>
    <ellipse cx="30" cy="38" rx="24" ry="10" fill="none" stroke="#f1df76" stroke-width="1.2"/>
    <ellipse cx="30" cy="38" rx="10" ry="24" fill="none" stroke="#38bdf8" stroke-width="1.2"/>
    <!-- Central Prismatic Core -->
    <polygon points="30,22 42,46 18,46" fill="url(#goldGrad4)" stroke="#ffffff" stroke-width="1.2" filter="url(#glowF4)"/>
    <circle cx="30" cy="38" r="4" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>
    <!-- Optical Sensor Beams -->
    <line x1="8" y1="16" x2="52" y2="60" stroke="#71efaf" stroke-width="1" stroke-dasharray="2 2"/>
    <line x1="8" y1="60" x2="52" y2="16" stroke="#ef5b55" stroke-width="1" stroke-dasharray="2 2"/>
  </g>

  <text x="82" y="21" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" letter-spacing="1.5">[F4 // NEURAL FORGE]</text>
  <text x="82" y="42" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" letter-spacing="0.5">INSIGHT FORGE</text>
  <text x="82" y="58" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">LEAD: <tspan fill="#71efaf" font-weight="bold">AYSHUK</tspan> | DEPTH: <tspan fill="#f1df76">-800M</tspan></text>
  
  <rect x="82" y="66" width="60" height="6" rx="1" fill="#422006" stroke="#f1df76" stroke-width="0.8"/>
  <rect x="83" y="67" width="50" height="4" rx="0.5" fill="#f1df76"/>
  <text x="148" y="72" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="7.5">NEUR: 91.5%</text>

  <g transform="translate(306, 22)">
    <polygon points="12,20 0,8 4,4 20,20 4,36 0,32" fill="#f1df76"/>
    <line x1="-10" y1="0" x2="-10" y2="40" stroke="#f1df76" stroke-width="1" stroke-dasharray="3 3"/>
  </g>
</svg>''',

        "floor_banner_f5_border_watch.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <defs>
    <linearGradient id="bgF5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1c0709"/>
      <stop offset="50%" stop-color="#3b0d13"/>
      <stop offset="100%" stop-color="#120305"/>
    </linearGradient>
    <filter id="glowF5" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="2,8 8,2 332,2 338,8 338,77 332,83 8,83 2,77" fill="url(#bgF5)" stroke="#ef5b55" stroke-width="2"/>
  <line x1="8" y1="20" x2="332" y2="20" stroke="#ef5b55" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="8" y1="65" x2="332" y2="65" stroke="#ef5b55" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="72" y1="6" x2="72" y2="79" stroke="#ef5b55" stroke-width="0.8" opacity="0.4"/>

  <!-- Left Centerpiece: Fortified Trench Bastion Ramparts & Perimeter Turrets -->
  <g transform="translate(10, 8)">
    <!-- Crenellated Fortress Wall -->
    <polygon points="8,30 16,30 16,38 24,38 24,30 36,30 36,38 44,38 44,30 52,30 52,68 8,68" fill="#450a0a" stroke="#ef5b55" stroke-width="1.8"/>
    <!-- Tungsten Armor Plating & Rivets -->
    <line x1="8" y1="48" x2="52" y2="48" stroke="#ef5b55" stroke-width="1.2"/>
    <circle cx="14" cy="58" r="1.5" fill="#f1df76"/>
    <circle cx="30" cy="58" r="1.5" fill="#f1df76"/>
    <circle cx="46" cy="58" r="1.5" fill="#f1df76"/>
    <!-- Searchlight Cones -->
    <polygon points="20,24 8,8 32,8" fill="#f1df76" opacity="0.25" filter="url(#glowF5)"/>
    <circle cx="20" cy="24" r="3.5" fill="#f1df76" stroke="#ffffff" stroke-width="1"/>
    <!-- Sentry Cannon Barrel -->
    <rect x="36" y="22" width="14" height="4" rx="1" fill="#e2e8f0" stroke="#ef5b55" stroke-width="1"/>
  </g>

  <text x="82" y="21" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" letter-spacing="1.5">[F5 // BULWARK BASTION]</text>
  <text x="82" y="42" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" letter-spacing="0.5">BORDER WATCH</text>
  <text x="82" y="58" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">LEAD: <tspan fill="#f1df76" font-weight="bold">MELLDA</tspan> | DEPTH: <tspan fill="#ef5b55">-1000M</tspan></text>
  
  <rect x="82" y="66" width="60" height="6" rx="1" fill="#450a0a" stroke="#ef5b55" stroke-width="0.8"/>
  <rect x="83" y="67" width="58" height="4" rx="0.5" fill="#ef5b55"/>
  <text x="148" y="72" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="7.5">PERIM: 99.1%</text>

  <g transform="translate(306, 22)">
    <polygon points="12,20 0,8 4,4 20,20 4,36 0,32" fill="#ef5b55"/>
    <line x1="-10" y1="0" x2="-10" y2="40" stroke="#ef5b55" stroke-width="1" stroke-dasharray="3 3"/>
  </g>
</svg>''',

        "floor_banner_f6_deep_vault.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <defs>
    <linearGradient id="bgF6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#130421"/>
      <stop offset="50%" stop-color="#2d0a4e"/>
      <stop offset="100%" stop-color="#0a0212"/>
    </linearGradient>
    <linearGradient id="purpleGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e9d5ff"/>
      <stop offset="50%" stop-color="#c084fc"/>
      <stop offset="100%" stop-color="#7e22ce"/>
    </linearGradient>
    <filter id="glowF6" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="2,8 8,2 332,2 338,8 338,77 332,83 8,83 2,77" fill="url(#bgF6)" stroke="#c084fc" stroke-width="2"/>
  <line x1="8" y1="20" x2="332" y2="20" stroke="#c084fc" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="8" y1="65" x2="332" y2="65" stroke="#c084fc" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="72" y1="6" x2="72" y2="79" stroke="#c084fc" stroke-width="0.8" opacity="0.4"/>

  <!-- Left Centerpiece: Massive Bank Vault Gear & Cryogenic Lock Tumblers -->
  <g transform="translate(10, 8)">
    <!-- Outer Gear Wheel -->
    <circle cx="30" cy="38" r="26" fill="#3b0764" stroke="#c084fc" stroke-width="2"/>
    <!-- Gear Teeth -->
    <rect x="27" y="9" width="6" height="6" fill="#f1df76"/>
    <rect x="27" y="61" width="6" height="6" fill="#f1df76"/>
    <rect x="1" y="35" width="6" height="6" fill="#f1df76"/>
    <rect x="53" y="35" width="6" height="6" fill="#f1df76"/>
    <!-- Inner Lock Chamber -->
    <circle cx="30" cy="38" r="16" fill="#1e053a" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 2"/>
    <!-- Cryogenic Starburst -->
    <polygon points="30,26 33,35 42,38 33,41 30,50 27,41 18,38 27,35" fill="url(#purpleGrad6)" filter="url(#glowF6)"/>
    <circle cx="30" cy="38" r="3" fill="#ffffff"/>
  </g>

  <text x="82" y="21" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" letter-spacing="1.5">[F6 // CRYO ARCHIVES]</text>
  <text x="82" y="42" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" letter-spacing="0.5">DEEP VAULT</text>
  <text x="82" y="58" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">LEAD: <tspan fill="#38bdf8" font-weight="bold">MARJUK</tspan> | DEPTH: <tspan fill="#c084fc">-1200M</tspan></text>
  
  <rect x="82" y="66" width="60" height="6" rx="1" fill="#3b0764" stroke="#c084fc" stroke-width="0.8"/>
  <rect x="83" y="67" width="54" height="4" rx="0.5" fill="#c084fc"/>
  <text x="148" y="72" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="7.5">CRYO: -180°C</text>

  <g transform="translate(306, 22)">
    <polygon points="12,20 0,8 4,4 20,20 4,36 0,32" fill="#c084fc"/>
    <line x1="-10" y1="0" x2="-10" y2="40" stroke="#c084fc" stroke-width="1" stroke-dasharray="3 3"/>
  </g>
</svg>''',

        "floor_banner_f7_shadow_corps.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <defs>
    <linearGradient id="bgF7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#120204"/>
      <stop offset="50%" stop-color="#2b050a"/>
      <stop offset="100%" stop-color="#080102"/>
    </linearGradient>
    <filter id="glowF7" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="2,8 8,2 332,2 338,8 338,77 332,83 8,83 2,77" fill="url(#bgF7)" stroke="#ef5b55" stroke-width="2"/>
  <line x1="8" y1="20" x2="332" y2="20" stroke="#ef5b55" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="8" y1="65" x2="332" y2="65" stroke="#ef5b55" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="72" y1="6" x2="72" y2="79" stroke="#ef5b55" stroke-width="0.8" opacity="0.4"/>

  <!-- Left Centerpiece: Dual Crescent Executioner Scythes & Obsidian Stiletto Reticle -->
  <g transform="translate(10, 8)">
    <!-- Radar Tracking Reticle -->
    <circle cx="30" cy="38" r="22" fill="none" stroke="#ef5b55" stroke-width="1" stroke-dasharray="4 2" opacity="0.6"/>
    <line x1="30" y1="12" x2="30" y2="64" stroke="#ef5b55" stroke-width="0.8" opacity="0.5"/>
    <line x1="4" y1="38" x2="56" y2="38" stroke="#ef5b55" stroke-width="0.8" opacity="0.5"/>
    <!-- Twin Crossed Crescent Blades -->
    <path d="M 8,20 Q 30,38 8,62 Q 26,44 8,20 Z" fill="#ef5b55" stroke="#ffffff" stroke-width="1.2" filter="url(#glowF7)"/>
    <path d="M 52,20 Q 30,38 52,62 Q 34,44 52,20 Z" fill="#ef5b55" stroke="#ffffff" stroke-width="1.2" filter="url(#glowF7)"/>
    <!-- Central Obsidian Stiletto Dagger -->
    <polygon points="30,14 34,50 30,64 26,50" fill="#f8fafc" stroke="#f1df76" stroke-width="1"/>
    <rect x="23" y="48" width="14" height="3" rx="1" fill="#f1df76"/>
  </g>

  <text x="82" y="21" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" letter-spacing="1.5">[F7 // STRIKE CORPS]</text>
  <text x="82" y="42" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" letter-spacing="0.5">SHADOW CORPS</text>
  <text x="82" y="58" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">LEAD: <tspan fill="#ffffff" font-weight="bold">ISHALL</tspan> | DEPTH: <tspan fill="#ef5b55">-1400M</tspan></text>
  
  <rect x="82" y="66" width="60" height="6" rx="1" fill="#450a0a" stroke="#ef5b55" stroke-width="0.8"/>
  <rect x="83" y="67" width="52" height="4" rx="0.5" fill="#ef5b55"/>
  <text x="148" y="72" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="7.5">STEALTH: ON</text>

  <g transform="translate(306, 22)">
    <polygon points="12,20 0,8 4,4 20,20 4,36 0,32" fill="#ef5b55"/>
    <line x1="-10" y1="0" x2="-10" y2="40" stroke="#ef5b55" stroke-width="1" stroke-dasharray="3 3"/>
  </g>
</svg>''',

        "floor_banner_f8_gate_watch.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <defs>
    <linearGradient id="bgF8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1c1303"/>
      <stop offset="50%" stop-color="#3b2605"/>
      <stop offset="100%" stop-color="#120a01"/>
    </linearGradient>
    <linearGradient id="amberGrad8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="50%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <filter id="glowF8" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="2,8 8,2 332,2 338,8 338,77 332,83 8,83 2,77" fill="url(#bgF8)" stroke="#f1df76" stroke-width="2"/>
  <line x1="8" y1="20" x2="332" y2="20" stroke="#f1df76" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="8" y1="65" x2="332" y2="65" stroke="#f1df76" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <line x1="72" y1="6" x2="72" y2="79" stroke="#f1df76" stroke-width="0.8" opacity="0.4"/>

  <!-- Left Centerpiece: Cyclopean Stone Gate Arch & Spiked Portcullis Grate -->
  <g transform="translate(10, 8)">
    <!-- Heavy Gateway Archway -->
    <path d="M 8,70 L 8,30 Q 30,10 52,30 L 52,70 L 42,70 L 42,38 Q 30,24 18,38 L 18,70 Z" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
    <!-- Drop Portcullis Steel Bars -->
    <line x1="24" y1="32" x2="24" y2="70" stroke="#ef5b55" stroke-width="1.8"/>
    <line x1="30" y1="28" x2="30" y2="70" stroke="#ef5b55" stroke-width="1.8"/>
    <line x1="36" y1="32" x2="36" y2="70" stroke="#ef5b55" stroke-width="1.8"/>
    <line x1="18" y1="52" x2="42" y2="52" stroke="#ef5b55" stroke-width="1.5"/>
    <!-- Glowing Abyssal Seal Keystone -->
    <polygon points="30,12 36,22 24,22" fill="url(#amberGrad8)" stroke="#ffffff" stroke-width="1" filter="url(#glowF8)"/>
    <circle cx="30" cy="18" r="2" fill="#c084fc"/>
  </g>

  <text x="82" y="21" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" letter-spacing="1.5">[F8 // ABYSSAL THRESHOLD]</text>
  <text x="82" y="42" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" letter-spacing="0.5">GATE WATCH</text>
  <text x="82" y="58" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">LEAD: <tspan fill="#c084fc" font-weight="bold">XYAN</tspan> | DEPTH: <tspan fill="#f1df76">-1600M</tspan></text>
  
  <rect x="82" y="66" width="60" height="6" rx="1" fill="#451a03" stroke="#f1df76" stroke-width="0.8"/>
  <rect x="83" y="67" width="58" height="4" rx="0.5" fill="#f59e0b"/>
  <text x="148" y="72" fill="#f59e0b" font-family="'JetBrains Mono', monospace" font-size="7.5">GATE: SEALED</text>

  <g transform="translate(306, 22)">
    <polygon points="12,20 0,8 4,4 20,20 4,36 0,32" fill="#f1df76"/>
    <line x1="-10" y1="0" x2="-10" y2="40" stroke="#f1df76" stroke-width="1" stroke-dasharray="3 3"/>
  </g>
</svg>'''
    }

    for fname, svg_code in floor_banners.items():
        with open(os.path.join(banners_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg_code)

    print("Created 8 ultra-rich, deeply personalized Floor Mini-Banners!")

    # -------------------------------------------------------------
    # 2. CANONICAL DAMAGE TYPE ICONS (Ultra-Detailed, High-Res SVGs)
    # -------------------------------------------------------------
    damage_icons = {
        # Grudge: Crimson Physical / HP
        "damage_grudge.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="gradGrudge" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="70%" stop-color="#991b1b"/>
      <stop offset="100%" stop-color="#450a0a"/>
    </radialGradient>
    <filter id="glowRed" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <!-- Chamfered Outer Shield -->
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="url(#gradGrudge)" stroke="#ef5b55" stroke-width="4"/>
  <!-- Inner Technical Frame -->
  <polygon points="60,12 106,28 106,82 60,108 14,82 14,28" fill="#180407" stroke="#f1df76" stroke-width="1.5" stroke-dasharray="8 4"/>
  
  <!-- Dual Jagged Blood Cleavers with Fuller Grooves -->
  <path d="M 24,32 L 68,76 L 62,88 L 48,82 L 20,46 Z" fill="#b91c1c" stroke="#ffffff" stroke-width="1.8" filter="url(#glowRed)"/>
  <path d="M 96,32 L 52,76 L 58,88 L 72,82 L 100,46 Z" fill="#b91c1c" stroke="#ffffff" stroke-width="1.8" filter="url(#glowRed)"/>
  <line x1="32" y1="42" x2="58" y2="68" stroke="#fca5a5" stroke-width="1.5"/>
  <line x1="88" y1="42" x2="62" y2="68" stroke="#fca5a5" stroke-width="1.5"/>
  
  <!-- Impact Trauma Star & Dripping Blood Shards -->
  <circle cx="60" cy="60" r="8" fill="#ffffff" filter="url(#glowRed)"/>
  <polygon points="60,46 64,56 74,60 64,64 60,74 56,64 46,60 56,56" fill="#f1df76"/>
  <polygon points="60,84 63,94 60,100 57,94" fill="#ef5b55"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">GRUDGE // HP</text>
</svg>''',

        # Lament: Deep Blue Mental / SP
        "damage_lament.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="gradLament" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="60%" stop-color="#0369a1"/>
      <stop offset="100%" stop-color="#082f49"/>
    </radialGradient>
    <filter id="glowBlue" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="url(#gradLament)" stroke="#38bdf8" stroke-width="4"/>
  <polygon points="60,12 106,28 106,82 60,108 14,82 14,28" fill="#031322" stroke="#bae6fd" stroke-width="1.5" stroke-dasharray="8 4"/>
  
  <!-- Weeping Abyssal Eye -->
  <path d="M 22,54 Q 60,20 98,54 Q 60,88 22,54 Z" fill="#082f49" stroke="#38bdf8" stroke-width="2.5"/>
  <circle cx="60" cy="54" r="15" fill="#0284c7" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="60" cy="54" r="8" fill="#031322"/>
  <circle cx="63" cy="51" r="3" fill="#ffffff" filter="url(#glowBlue)"/>
  
  <!-- Cascading Tears of Despair & Sonic Wave Distortion -->
  <path d="M 60,68 C 56,76 54,82 60,88 C 66,82 64,76 60,68 Z" fill="#38bdf8" stroke="#ffffff" stroke-width="1" filter="url(#glowBlue)"/>
  <ellipse cx="60" cy="54" rx="28" ry="24" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4 4" opacity="0.7"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">LAMENT // SP</text>
</svg>''',

        # Void: Pale White Existential / % Max HP
        "damage_void.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="gradVoid" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="40%" stop-color="#cbd5e1"/>
      <stop offset="100%" stop-color="#334155"/>
    </radialGradient>
    <filter id="glowWhite" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1e293b" stroke="#f8fafc" stroke-width="4"/>
  <polygon points="60,12 106,28 106,82 60,108 14,82 14,28" fill="#090d16" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="8 4"/>
  
  <!-- Cosmic Event Horizon & Radiant Lensing Rings -->
  <circle cx="60" cy="54" r="24" fill="none" stroke="#f8fafc" stroke-width="2" stroke-dasharray="8 4" opacity="0.8"/>
  <ellipse cx="60" cy="54" rx="34" ry="12" fill="none" stroke="#ffffff" stroke-width="1.5" transform="rotate(-25 60 54)"/>
  <ellipse cx="60" cy="54" rx="34" ry="12" fill="none" stroke="#94a3b8" stroke-width="1.5" transform="rotate(25 60 54)"/>
  
  <!-- Pure White Singularity Core -->
  <circle cx="60" cy="54" r="14" fill="#000000" stroke="#ffffff" stroke-width="3" filter="url(#glowWhite)"/>
  <circle cx="60" cy="54" r="6" fill="#ffffff"/>
  
  <!-- Dissolving Soul Dust Particles -->
  <circle cx="40" cy="38" r="1.8" fill="#ffffff"/>
  <circle cx="82" cy="42" r="1.8" fill="#ffffff"/>
  <circle cx="36" cy="70" r="1.5" fill="#cbd5e1"/>
  <circle cx="80" cy="68" r="1.5" fill="#cbd5e1"/>
  <text x="60" y="104" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">VOID // %HP</text>
</svg>''',

        # Weight: Black Gravitational / Dual HP + SP
        "damage_weight.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="gradWeight" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="70%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#020617"/>
    </radialGradient>
    <filter id="glowPurple" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="url(#gradWeight)" stroke="#94a3b8" stroke-width="4"/>
  <polygon points="60,12 106,28 106,82 60,108 14,82 14,28" fill="#020408" stroke="#ef5b55" stroke-width="1.5" stroke-dasharray="8 4"/>
  
  <!-- Gravitational Compression Grid -->
  <line x1="24" y1="84" x2="96" y2="84" stroke="#64748b" stroke-width="2"/>
  <line x1="30" y1="88" x2="90" y2="88" stroke="#475569" stroke-width="1.5"/>
  <polygon points="60,84 64,74 56,74" fill="#ef5b55"/>
  
  <!-- Massive Obsidian Sphere with Heavy Downward Force Vectors -->
  <circle cx="60" cy="48" r="22" fill="#090d16" stroke="#c084fc" stroke-width="2.5" filter="url(#glowPurple)"/>
  <circle cx="60" cy="48" r="14" fill="#000000" stroke="#f1df76" stroke-width="1"/>
  
  <!-- Downward Gravitational Arrows -->
  <polygon points="42,28 46,38 38,38" fill="#c084fc"/>
  <polygon points="60,22 65,34 55,34" fill="#f1df76"/>
  <polygon points="78,28 82,38 74,38" fill="#c084fc"/>
  
  <text x="60" y="104" fill="#cbd5e1" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">WEIGHT // DUAL</text>
</svg>''',

        # Mixed: Rainbow Multi-Spectral
        "damage_mixed.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="rainbowGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="20%" stop-color="#f59e0b"/>
      <stop offset="40%" stop-color="#10b981"/>
      <stop offset="60%" stop-color="#06b6d4"/>
      <stop offset="80%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#8b5cf6"/>
    </linearGradient>
  </defs>
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#090d16" stroke="url(#rainbowGrad)" stroke-width="4"/>
  <polygon points="60,12 106,28 106,82 60,108 14,82 14,28" fill="#030712" stroke="#ffffff" stroke-width="1.2" stroke-dasharray="6 3"/>
  
  <!-- 6-Faceted Prismatic Crystal Vortex -->
  <polygon points="60,20 88,38 88,70 60,88 32,70 32,38" fill="none" stroke="url(#rainbowGrad)" stroke-width="3"/>
  <polygon points="60,30 78,42 78,64 60,76 42,64 42,42" fill="url(#rainbowGrad)" opacity="0.3"/>
  <line x1="60" y1="20" x2="60" y2="88" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="32" y1="38" x2="88" y2="70" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="32" y1="70" x2="88" y2="38" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="60" cy="54" r="6" fill="#ffffff"/>
  <text x="60" y="104" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">MIXED // HYBRID</text>
</svg>''',

        # Hope: Golden Dawn / Absolvohan
        "damage_hope.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="gradHope" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="60%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#78350f"/>
    </radialGradient>
    <filter id="glowGold" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="url(#gradHope)" stroke="#fef08a" stroke-width="4"/>
  <polygon points="60,12 106,28 106,82 60,108 14,82 14,28" fill="#1c1202" stroke="#f1df76" stroke-width="1.5" stroke-dasharray="8 4"/>
  
  <!-- Radiant 12-Point Sovereign Solar Dawn -->
  <g transform="translate(60, 54)">
    <circle cx="0" cy="0" r="14" fill="url(#gradHope)" filter="url(#glowGold)"/>
    <circle cx="0" cy="0" r="7" fill="#ffffff"/>
    <!-- Solar Rays -->
    <line x1="0" y1="-26" x2="0" y2="26" stroke="#fef08a" stroke-width="3"/>
    <line x1="-26" y1="0" x2="26" y2="0" stroke="#fef08a" stroke-width="3"/>
    <line x1="-18" y1="-18" x2="18" y2="18" stroke="#fef08a" stroke-width="2.2"/>
    <line x1="-18" y1="18" x2="18" y2="-18" stroke="#fef08a" stroke-width="2.2"/>
    <!-- Outstretched Wings of Dawn -->
    <path d="M -30,-6 Q -15,-18 0,-6 Q 15,-18 30,-6 Q 15,-2 0,10 Q -15,-2 -30,-6 Z" fill="none" stroke="#ffffff" stroke-width="1.8"/>
  </g>
  <text x="60" y="104" fill="#fef08a" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">HOPE // DAWN</text>
</svg>'''
    }

    # Write damage icons to all standard aliases
    for fname, svg_code in damage_icons.items():
        with open(os.path.join(icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg_code)
        with open(os.path.join(user_icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg_code)

    # Aliases
    aliases = {
        "icon_damage_grudge.svg": "damage_grudge.svg",
        "icon_damage_physical_red.svg": "damage_grudge.svg",
        "el_grudge.svg": "damage_grudge.svg",
        "grudge.svg": "damage_grudge.svg",

        "icon_damage_lament.svg": "damage_lament.svg",
        "icon_damage_pale_cyan.svg": "damage_lament.svg",
        "el_lament.svg": "damage_lament.svg",
        "lament.svg": "damage_lament.svg",

        "icon_damage_void.svg": "damage_void.svg",
        "icon_damage_mental_white.svg": "damage_void.svg",
        "el_void.svg": "damage_void.svg",
        "void.svg": "damage_void.svg",

        "icon_damage_weight.svg": "damage_weight.svg",
        "icon_damage_corrosive_black.svg": "damage_weight.svg",
        "el_weight.svg": "damage_weight.svg",
        "element.svg": "damage_weight.svg",

        "or_hope.svg": "damage_hope.svg",
        "hope_icon.svg": "damage_hope.svg",
        "shield_hope.svg": "damage_hope.svg"
    }

    for alias, target in aliases.items():
        code = damage_icons[target]
        with open(os.path.join(icons_dir, alias), "w", encoding="utf-8") as f:
            f.write(code)
        with open(os.path.join(user_icons_dir, alias), "w", encoding="utf-8") as f:
            f.write(code)

    print("Created ultra-rich canonical damage icons with all aliases!")

    # -------------------------------------------------------------
    # 3. SECC CANONICAL RISK TIER BADGES (Ultra-Detailed Tactical Badges)
    # -------------------------------------------------------------
    risk_tiers = {
        "icon_risk_t01_aether.svg": {
            "name": "AETHER",
            "greek": "α",
            "tier": "TIER 01 // LOW",
            "color": "#71efaf",
            "bg1": "#064e3b",
            "bg2": "#022c22"
        },
        "icon_risk_t02_somna.svg": {
            "name": "SOMNA",
            "greek": "β",
            "tier": "TIER 02 // MED",
            "color": "#38bdf8",
            "bg1": "#0369a1",
            "bg2": "#082f49"
        },
        "icon_risk_t03_morphean.svg": {
            "name": "MORPHEAN",
            "greek": "γ",
            "tier": "TIER 03 // HIGH",
            "color": "#f1df76",
            "bg1": "#a16207",
            "bg2": "#451a03"
        },
        "icon_risk_t04_phantasm.svg": {
            "name": "PHANTASM",
            "greek": "δ",
            "tier": "TIER 04 // CRIT",
            "color": "#ef5b55",
            "bg1": "#b91c1c",
            "bg2": "#450a0a"
        },
        "icon_risk_t05_apocrypha.svg": {
            "name": "APOCRYPHA",
            "greek": "ω",
            "tier": "TIER 05 // CATA",
            "color": "#c084fc",
            "bg1": "#7e22ce",
            "bg2": "#2e1065"
        }
    }

    for fname, data in risk_tiers.items():
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="grad_{data['name']}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{data['color']}"/>
      <stop offset="60%" stop-color="{data['bg1']}"/>
      <stop offset="100%" stop-color="{data['bg2']}"/>
    </radialGradient>
  </defs>
  <!-- Tactical Diamond Outer Bevel -->
  <polygon points="60,4 116,60 60,116 4,60" fill="url(#grad_{data['name']})" stroke="{data['color']}" stroke-width="4"/>
  <!-- Inner Circuit Traces -->
  <polygon points="60,14 106,60 60,106 14,60" fill="#040711" stroke="{data['color']}" stroke-width="1.5" stroke-dasharray="6 3"/>
  <!-- Corner Hazard Pips -->
  <polygon points="60,18 64,24 56,24" fill="#ffffff"/>
  <polygon points="60,102 64,96 56,96" fill="#ffffff"/>
  <polygon points="18,60 24,56 24,64" fill="#ffffff"/>
  <polygon points="102,60 96,56 96,64" fill="#ffffff"/>
  <!-- Central Greek Tier Rune -->
  <text x="60" y="58" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold" text-anchor="middle">{data['greek']}</text>
  <!-- Risk Classification Name & Tier -->
  <text x="60" y="78" fill="{data['color']}" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" text-anchor="middle">{data['name']}</text>
  <text x="60" y="90" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="6.5" font-weight="bold" text-anchor="middle">{data['tier']}</text>
</svg>'''
        with open(os.path.join(icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg)
        with open(os.path.join(user_icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg)

    # Legacy mappings
    risk_aliases = {
        "icon_risk_t01_can.svg": "icon_risk_t01_aether.svg",
        "icon_risk_t02_teth.svg": "icon_risk_t02_somna.svg",
        "icon_risk_t03_he.svg": "icon_risk_t03_morphean.svg",
        "icon_risk_t04_waw.svg": "icon_risk_t04_phantasm.svg",
        "icon_risk_t05_aleph.svg": "icon_risk_t05_apocrypha.svg",
        "risk_zayin.svg": "icon_risk_t01_aether.svg",
        "risk_teth.svg": "icon_risk_t02_somna.svg",
        "risk_he.svg": "icon_risk_t03_morphean.svg",
        "risk_waw.svg": "icon_risk_t04_phantasm.svg",
        "risk_aleph.svg": "icon_risk_t05_apocrypha.svg",
        "pot_a.svg": "icon_risk_t01_aether.svg",
        "pot_b.svg": "icon_risk_t02_somna.svg",
        "pot_g.svg": "icon_risk_t03_morphean.svg",
        "pot_d.svg": "icon_risk_t04_phantasm.svg",
        "pot_w.svg": "icon_risk_t05_apocrypha.svg",
        "potency.svg": "icon_risk_t03_morphean.svg"
    }

    for alias, target in risk_aliases.items():
        with open(os.path.join(icons_dir, target), "r", encoding="utf-8") as f:
            c = f.read()
        with open(os.path.join(icons_dir, alias), "w", encoding="utf-8") as f:
            f.write(c)
        with open(os.path.join(user_icons_dir, alias), "w", encoding="utf-8") as f:
            f.write(c)

    print("Created ultra-rich SECC Risk Tier Badges with all aliases!")

if __name__ == "__main__":
    generate_rich_svg_suite()
