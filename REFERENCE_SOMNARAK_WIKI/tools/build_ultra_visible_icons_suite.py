import os

def generate_ultra_visible_icons():
    dirs = [
        "/home/user/01_Somnarak_Wiki/assets/icons",
        "/home/user/icons"
    ]

    for d in dirs:
        os.makedirs(d, exist_ok=True)

    icons = {}

    # 1. DAMAGE TYPE ICONS (Bold, high-luminance, massive icons)
    icons["damage_red.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="redGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff4d4d" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#b91c1c" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#450a0a" stop-opacity="0.95"/>
    </radialGradient>
    <filter id="crimsonNeon" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <!-- Chamfered Outer Shield Frame -->
  <polygon points="60,6 114,24 114,84 60,114 6,84 6,24" fill="url(#redGlow)" stroke="#ff4d4d" stroke-width="4"/>
  <polygon points="60,14 104,28 104,78 60,104 16,78 16,28" fill="#180404" stroke="#f1df76" stroke-width="2"/>
  
  <!-- Massive Radiant Flame Cleaver Blade -->
  <g filter="url(#crimsonNeon)">
    <!-- Radiating Fire Spikes -->
    <polygon points="60,18 68,34 60,30 52,34" fill="#f1df76"/>
    <polygon points="96,50 80,54 84,60 92,64" fill="#ff4d4d"/>
    <polygon points="24,50 40,54 36,60 28,64" fill="#ff4d4d"/>
    
    <!-- Central Jagged Greatsword Core -->
    <polygon points="60,20 74,48 70,82 60,94 50,82 46,48" fill="#ffffff" stroke="#ef4444" stroke-width="3"/>
    <polygon points="60,28 68,50 64,78 60,86 56,78 52,50" fill="#ef4444"/>
    
    <!-- Crossguard & Hilt -->
    <rect x="42" y="76" width="36" height="8" rx="2" fill="#f1df76" stroke="#991b1b" stroke-width="1.5"/>
    <rect x="56" y="84" width="8" height="18" rx="2" fill="#ffffff"/>
    <circle cx="60" cy="104" r="5" fill="#f1df76" stroke="#ef4444" stroke-width="2"/>
  </g>
</svg>'''

    icons["damage_white.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="cyanGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#0284c7" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#082f49" stop-opacity="0.95"/>
    </radialGradient>
    <filter id="cyanNeon" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <!-- Chamfered Diamond Frame -->
  <polygon points="60,6 114,60 60,114 6,60" fill="url(#cyanGlow)" stroke="#38bdf8" stroke-width="4"/>
  <polygon points="60,16 102,60 60,102 18,60" fill="#04121e" stroke="#ffffff" stroke-width="2"/>

  <!-- Massive Weeping Acoustic Eye & Resonance Crystal -->
  <g filter="url(#cyanNeon)">
    <!-- Radiating Acoustic Shockwaves -->
    <path d="M 30,60 Q 60,26 90,60 Q 60,94 30,60 Z" fill="#0c4a6e" stroke="#38bdf8" stroke-width="3"/>
    <ellipse cx="60" cy="60" rx="20" ry="20" fill="#0284c7" stroke="#ffffff" stroke-width="2.5"/>
    
    <!-- Central Shining Iris Prism -->
    <polygon points="60,44 72,60 60,76 48,60" fill="#ffffff" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="60" cy="60" r="6" fill="#082f49" stroke="#f1df76" stroke-width="2"/>

    <!-- Flowing Tear Conduit -->
    <path d="M 60,76 L 60,98" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
    <circle cx="60" cy="100" r="3.5" fill="#ffffff"/>
  </g>
</svg>'''

    icons["damage_black.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="goldGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#eab308" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#713f12" stop-opacity="0.95"/>
    </radialGradient>
    <filter id="goldNeon" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <!-- Octagonal Gold Frame -->
  <polygon points="40,6 80,6 114,40 114,80 80,114 40,114 6,80 6,40" fill="url(#goldGlow)" stroke="#f1df76" stroke-width="4"/>
  <polygon points="42,14 78,14 106,42 106,78 78,106 42,106 14,78 14,42" fill="#140f04" stroke="#fef08a" stroke-width="2"/>

  <!-- Massive Cosmic Void Vortex & Radiant Sun Rays -->
  <g filter="url(#goldNeon)">
    <!-- Golden Corona Rays -->
    <line x1="60" y1="18" x2="60" y2="30" stroke="#f1df76" stroke-width="4" stroke-linecap="round"/>
    <line x1="60" y1="90" x2="60" y2="102" stroke="#f1df76" stroke-width="4" stroke-linecap="round"/>
    <line x1="18" y1="60" x2="30" y2="60" stroke="#f1df76" stroke-width="4" stroke-linecap="round"/>
    <line x1="90" y1="60" x2="102" y2="60" stroke="#f1df76" stroke-width="4" stroke-linecap="round"/>

    <!-- Dual Channel Swirling Vortex Body -->
    <circle cx="60" cy="60" r="28" fill="#3a2505" stroke="#f1df76" stroke-width="3"/>
    
    <!-- Dark Singularity Core with Amber Edge -->
    <circle cx="60" cy="60" r="18" fill="#050301" stroke="#eab308" stroke-width="2.5"/>
    <polygon points="60,48 68,60 60,72 52,60" fill="#f1df76"/>
    <circle cx="60" cy="60" r="4" fill="#ffffff"/>
  </g>
</svg>'''

    icons["damage_pale.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="paleGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
      <stop offset="40%" stop-color="#e0e7ff" stop-opacity="0.9"/>
      <stop offset="80%" stop-color="#818cf8" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#1e1b4b" stop-opacity="0.95"/>
    </radialGradient>
    <filter id="paleNeon" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <!-- Hexagonal Pale Sovereign Frame -->
  <polygon points="60,6 110,32 110,88 60,114 10,88 10,32" fill="url(#paleGlow)" stroke="#ffffff" stroke-width="4"/>
  <polygon points="60,16 100,38 100,82 60,104 20,82 20,38" fill="#0b0a1a" stroke="#c7d2fe" stroke-width="2"/>

  <!-- Massive Soul-Severing Scythe & Radiant Stigmata Star -->
  <g filter="url(#paleNeon)">
    <!-- 8-Pointed Sovereign Star -->
    <polygon points="60,20 66,48 94,54 70,68 76,96 60,78 44,96 50,68 26,54 54,48" fill="#ffffff" stroke="#818cf8" stroke-width="2.5"/>
    
    <!-- Central Radiant Cyan/White Core -->
    <circle cx="60" cy="60" r="14" fill="#38bdf8" stroke="#ffffff" stroke-width="2.5"/>
    <circle cx="60" cy="60" r="6" fill="#ffffff"/>

    <!-- Orbital Diamond Shards -->
    <polygon points="60,12 64,18 60,24 56,18" fill="#ffffff"/>
    <polygon points="60,96 64,102 60,108 56,102" fill="#ffffff"/>
  </g>
</svg>'''

    # Copy to alternate names
    icons["icon_damage_grudge.svg"] = icons["damage_red.svg"]
    icons["icon_damage_physical_red.svg"] = icons["damage_red.svg"]
    icons["icon_damage_lament.svg"] = icons["damage_white.svg"]
    icons["icon_damage_mental_white.svg"] = icons["damage_white.svg"]
    icons["icon_damage_void.svg"] = icons["damage_black.svg"]
    icons["icon_damage_corrosive_black.svg"] = icons["damage_black.svg"]
    icons["icon_damage_weight.svg"] = icons["damage_black.svg"]
    icons["icon_damage_pale_cyan.svg"] = icons["damage_pale.svg"]

    # 2. WORK TYPE ICONS (Massive, bold, 120x120 vector artwork)
    icons["work_instinct.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,32 114,88 60,114 6,88 6,32" fill="#2d0505" stroke="#ef4444" stroke-width="4"/>
  <polygon points="60,14 104,36 104,84 60,106 16,84 16,36" fill="#130202" stroke="#f1df76" stroke-width="2"/>
  <!-- Bold Beast Heart & Claw Slashes -->
  <path d="M 60,40 C 45,20 25,35 35,60 C 45,80 60,96 60,96 C 60,96 75,80 85,60 C 95,35 75,20 60,40 Z" fill="#ef4444" stroke="#ffffff" stroke-width="3"/>
  <line x1="30" y1="40" x2="50" y2="70" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
  <line x1="45" y1="35" x2="65" y2="65" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
  <line x1="60" y1="35" x2="80" y2="65" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
</svg>'''

    icons["work_insight.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,60 60,114 6,60" fill="#041824" stroke="#38bdf8" stroke-width="4"/>
  <polygon points="60,16 102,60 60,102 18,60" fill="#020d14" stroke="#ffffff" stroke-width="2"/>
  <!-- Bold Observing Eye Prism -->
  <path d="M 24,60 Q 60,25 96,60 Q 60,95 24,60 Z" fill="#0c4a6e" stroke="#38bdf8" stroke-width="3.5"/>
  <circle cx="60" cy="60" r="18" fill="#0284c7" stroke="#ffffff" stroke-width="3"/>
  <circle cx="60" cy="60" r="8" fill="#ffffff"/>
</svg>'''

    icons["work_attachment.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="40,6 80,6 114,40 114,80 80,114 40,114 6,80 6,40" fill="#022c22" stroke="#10b981" stroke-width="4"/>
  <polygon points="42,14 78,14 106,42 106,78 78,106 42,106 14,78 14,42" fill="#01140f" stroke="#71efaf" stroke-width="2"/>
  <!-- Entwined Covenant Rings & Heart -->
  <circle cx="48" cy="58" r="20" fill="none" stroke="#71efaf" stroke-width="4"/>
  <circle cx="72" cy="58" r="20" fill="none" stroke="#f1df76" stroke-width="4"/>
  <circle cx="60" cy="58" r="8" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
</svg>'''

    icons["work_repression.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,32 114,88 60,114 6,88 6,32" fill="#2d1c08" stroke="#f1df76" stroke-width="4"/>
  <polygon points="60,14 104,36 104,84 60,106 16,84 16,36" fill="#130b02" stroke="#ef4444" stroke-width="2"/>
  <!-- Heavy Iron Padlock & Restraint Shackle -->
  <rect x="36" y="52" width="48" height="42" rx="6" fill="#3a2505" stroke="#f1df76" stroke-width="3.5"/>
  <path d="M 46,52 L 46,36 C 46,24 74,24 74,36 L 74,52" fill="none" stroke="#f1df76" stroke-width="5" stroke-linecap="round"/>
  <circle cx="60" cy="70" r="6" fill="#ef4444"/>
  <polygon points="58,70 62,70 64,84 56,84" fill="#ef4444"/>
</svg>'''

    icons["work_extraction.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,60 60,114 6,60" fill="#082f49" stroke="#38bdf8" stroke-width="4"/>
  <polygon points="60,16 102,60 60,102 18,60" fill="#021420" stroke="#f1df76" stroke-width="2"/>
  <!-- Glowing Siphon Crucible & Han Crystal Core -->
  <polygon points="60,24 88,60 60,96 32,60" fill="#0284c7" stroke="#ffffff" stroke-width="3"/>
  <polygon points="60,36 76,60 60,84 44,60" fill="#ffffff"/>
  <circle cx="60" cy="60" r="7" fill="#f1df76"/>
</svg>'''

    # Copy work icons to synonyms
    icons["icon_work_instinct_red.svg"] = icons["work_instinct.svg"]
    icons["icon_work_insight_white.svg"] = icons["work_insight.svg"]
    icons["icon_work_attachment_black.svg"] = icons["work_attachment.svg"]
    icons["icon_work_repression_cyan.svg"] = icons["work_repression.svg"]
    icons["icon_work_extraction.svg"] = icons["work_extraction.svg"]
    icons["wt_pugnahan.svg"] = icons["work_instinct.svg"]
    icons["wt_viderehan.svg"] = icons["work_insight.svg"]
    icons["wt_ferrehan.svg"] = icons["work_attachment.svg"]
    icons["wt_flerehan.svg"] = icons["work_repression.svg"]

    # 3. CORE AVATARS (Majin, Dekan, Zyrak, Ayshuk, Mellda, Marjuk, Ishall, Xyan, Seiyon)
    core_avatars = {
        "avatar_core_majin.svg": ("#ef5b55", "#f1df76", "MAJIN", "01"),
        "avatar_core_seiyon.svg": ("#38bdf8", "#ffffff", "SEIYON", "02"),
        "avatar_core_dekan.svg": ("#ef5b55", "#38bdf8", "DEKAN", "03"),
        "avatar_core_zyrak.svg": ("#f1df76", "#ef5b55", "ZYRAK", "04"),
        "avatar_core_ayshuk.svg": ("#38bdf8", "#71efaf", "AYSHUK", "05"),
        "avatar_core_mellda.svg": ("#ef5b55", "#f1df76", "MELLDA", "06"),
        "avatar_core_marjuk.svg": ("#c084fc", "#38bdf8", "MARJUK", "07"),
        "avatar_core_ishall.svg": ("#ef5b55", "#ffffff", "ISHALL", "08"),
        "avatar_core_xyan.svg": ("#f1df76", "#c084fc", "XYAN", "09")
    }

    for fname, (col1, col2, name, num) in core_avatars.items():
        icons[fname] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="avBg_{num}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{col1}" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#090d16" stop-opacity="0.95"/>
    </radialGradient>
  </defs>
  <!-- Circular Glowing Avatar Border -->
  <circle cx="60" cy="60" r="56" fill="url(#avBg_{num})" stroke="{col1}" stroke-width="4"/>
  <circle cx="60" cy="60" r="48" fill="#070c14" stroke="{col2}" stroke-width="2" stroke-dasharray="8 4"/>

  <!-- Distinct Silhouetted Core Visage & Headgear -->
  <circle cx="60" cy="46" r="20" fill="#182333" stroke="{col1}" stroke-width="2.5"/>
  <!-- Glowing Eye / Visor Strip -->
  <rect x="46" y="42" width="28" height="8" rx="3" fill="{col2}" stroke="#ffffff" stroke-width="1.5"/>
  <!-- Neck and Pauldron Armor -->
  <path d="M 32,96 C 32,74 44,68 60,68 C 76,68 88,74 88,96 Z" fill="#111927" stroke="{col1}" stroke-width="2.5"/>
  <polygon points="60,68 66,80 54,80" fill="{col2}"/>

  <!-- Bottom Core ID Badge -->
  <rect x="36" y="96" width="48" height="18" rx="4" fill="#04070d" stroke="{col1}" stroke-width="1.5"/>
  <text x="60" y="109" fill="{col2}" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" text-anchor="middle">{name}</text>
</svg>'''
        icons[f"icon_core_{fname.split('_')[-1]}"] = icons[fname]

    # Write all icons to both directories
    for d in dirs:
        for fname, svg_str in icons.items():
            fpath = os.path.join(d, fname)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(svg_str)

    print(f"Successfully generated and wrote {len(icons)} ultra-visible master icons!")

if __name__ == "__main__":
    generate_ultra_visible_icons()
