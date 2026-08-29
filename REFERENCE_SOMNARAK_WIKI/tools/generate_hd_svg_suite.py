import os

ICONS_DIR = "/home/user/01_Somnarak_Wiki/assets/icons"
ART_ENT_DIR = "/home/user/01_Somnarak_Wiki/assets/art/entities"
ART_MAW_DIR = "/home/user/01_Somnarak_Wiki/assets/art/maw"
LAYOUT_HAND_DIR = "/home/user/01_Somnarak_Wiki/assets/layout/hand/icons"
LAYOUT_CITY_DIR = "/home/user/01_Somnarak_Wiki/assets/layout/city/icons"

for d in [ICONS_DIR, ART_ENT_DIR, ART_MAW_DIR, LAYOUT_HAND_DIR, LAYOUT_CITY_DIR]:
    os.makedirs(d, exist_ok=True)

# 1. High-Definition Master Emblem (somnarak_icon.svg)
somnarak_icon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <linearGradient id="goldGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff8cc"/>
      <stop offset="40%" stop-color="#f1df76"/>
      <stop offset="80%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
    <radialGradient id="cyanBackdrop" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#0284c7" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#05070a" stop-opacity="0"/>
    </radialGradient>
    <filter id="neonDrop" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <!-- Background Shield Plate -->
  <rect width="120" height="120" rx="18" fill="#060910" stroke="url(#goldGlow)" stroke-width="3"/>
  <circle cx="60" cy="60" r="46" fill="url(#cyanBackdrop)"/>
  <circle cx="60" cy="60" r="42" fill="none" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="6,3"/>
  
  <!-- Outer Diamond Mandate -->
  <polygon points="60,10 108,60 60,110 12,60" fill="#090e18" stroke="url(#goldGlow)" stroke-width="3.5" filter="url(#neonDrop)"/>
  
  <!-- Inner The Alpha Tree & Weeping Eye -->
  <path d="M 28 60 Q 60 26 92 60 Q 60 94 28 60 Z" fill="#030508" stroke="#ef4444" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="14" fill="url(#goldGlow)" stroke="#f8fafc" stroke-width="1.5"/>
  <circle cx="60" cy="60" r="6" fill="#030508"/>
  <circle cx="60" cy="60" r="2.5" fill="#38bdf8"/>
  
  <!-- Cardinal Alignment Pylons -->
  <line x1="60" y1="2" x2="60" y2="14" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
  <line x1="60" y1="106" x2="60" y2="118" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
  <line x1="2" y1="60" x2="14" y2="60" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
  <line x1="106" y1="60" x2="118" y2="60" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
</svg>'''

with open(os.path.join(ICONS_DIR, "somnarak_icon.svg"), "w", encoding="utf-8") as f:
    f.write(somnarak_icon_svg)

# 2. Category Banner & Portal Icons (HD 120x120)
category_svgs = {
    "banner_characters.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="charGlow" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="16" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#charGlow)"/>
  <!-- Glowing Character Bust Silhouette -->
  <circle cx="60" cy="42" r="20" fill="#131d2e" stroke="#f1df76" stroke-width="3"/>
  <circle cx="60" cy="42" r="8" fill="#ef5b55"/>
  <path d="M 26 96 C 26 68, 94 68, 94 96 Z" fill="#131d2e" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="60,62 70,82 50,82" fill="#f1df76"/>
</svg>''',

    "banner_entities.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="entGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="16" fill="#100608" stroke="#ef4444" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#entGlow)"/>
  <!-- Crystalline Sorrow Tear -->
  <path d="M 60 16 C 85 45, 92 75, 60 104 C 28 75, 35 45, 60 16 Z" fill="#240a0e" stroke="#ef4444" stroke-width="3.5"/>
  <circle cx="60" cy="68" r="12" fill="#f1df76" stroke="#fff" stroke-width="2"/>
  <path d="M 45 68 L 75 68 M 60 53 L 60 83" stroke="#000" stroke-width="2.5"/>
</svg>''',

    "weapon.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="mawGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="16" fill="#0d0e14" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#mawGlow)"/>
  <!-- Crossed Siphon Greatblade and Shield -->
  <line x1="22" y1="98" x2="98" y2="22" stroke="#ef4444" stroke-width="6" stroke-linecap="round"/>
  <polygon points="90,14 106,30 96,38 82,24" fill="#f1df76"/>
  <line x1="98" y1="98" x2="22" y2="22" stroke="#38bdf8" stroke-width="6" stroke-linecap="round"/>
  <circle cx="60" cy="60" r="16" fill="#090d16" stroke="#f1df76" stroke-width="3"/>
  <circle cx="60" cy="60" r="6" fill="#f1df76"/>
</svg>''',

    "banner_mechanics.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="mechGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="16" fill="#070c16" stroke="#38bdf8" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#mechGlow)"/>
  <!-- High Tech Gear & Resonance Meter -->
  <circle cx="60" cy="60" r="28" fill="#0f172a" stroke="#38bdf8" stroke-width="4"/>
  <!-- Teeth -->
  <line x1="60" y1="18" x2="60" y2="30" stroke="#f1df76" stroke-width="5" stroke-linecap="round"/>
  <line x1="60" y1="90" x2="60" y2="102" stroke="#f1df76" stroke-width="5" stroke-linecap="round"/>
  <line x1="18" y1="60" x2="30" y2="60" stroke="#f1df76" stroke-width="5" stroke-linecap="round"/>
  <line x1="90" y1="60" x2="102" y2="60" stroke="#f1df76" stroke-width="5" stroke-linecap="round"/>
  <circle cx="60" cy="60" r="10" fill="#f1df76"/>
</svg>''',

    "banner_factions.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="facGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef5b55" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="16" fill="#12080a" stroke="#ef5b55" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#facGlow)"/>
  <!-- Sovereign Faction Heraldic Crest -->
  <polygon points="60,18 96,32 96,72 60,102 24,72 24,32" fill="#200d11" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="60,35 78,55 60,82 42,55" fill="#ef4444" stroke="#fff" stroke-width="1.5"/>
  <circle cx="60" cy="58" r="6" fill="#f1df76"/>
</svg>''',

    "banner_locations.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="locGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#22c55e" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="16" fill="#06120b" stroke="#4ade80" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#locGlow)"/>
  <!-- City Spire & Compass Radar -->
  <circle cx="60" cy="60" r="40" fill="none" stroke="#4ade80" stroke-width="2" stroke-dasharray="6,4"/>
  <polygon points="60,20 70,60 60,52 50,60" fill="#ef4444"/>
  <polygon points="60,100 70,60 60,68 50,60" fill="#f1df76"/>
  <circle cx="60" cy="60" r="6" fill="#4ade80" stroke="#000" stroke-width="2"/>
</svg>''',

    "banner_lore.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="loreGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="16" fill="#0e0616" stroke="#c084fc" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#loreGlow)"/>
  <!-- The Alpha Tree Roots & Ancient Tome -->
  <path d="M 26 88 L 60 76 L 94 88 L 94 36 L 60 24 L 26 36 Z" fill="#1b0c2c" stroke="#c084fc" stroke-width="3"/>
  <line x1="60" y1="24" x2="60" y2="76" stroke="#f1df76" stroke-width="3"/>
  <circle cx="60" cy="50" r="10" fill="#f1df76" stroke="#fff" stroke-width="1.5"/>
</svg>''',
}

for fn, code in category_svgs.items():
    with open(os.path.join(ICONS_DIR, fn), "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Generated HD Category Icon: {fn}")

# 3. Department Floor Badges (HD 80x80) in layout/hand/icons/
floor_badges = {
    "icon_dept_f1_neutral.svg": ("#ef5b55", "F1", "COMMAND", '''<circle cx="40" cy="40" r="22" fill="#1a080a" stroke="#ef5b55" stroke-width="2.5"/><polygon points="40,24 54,48 26,48" fill="#ef5b55"/><circle cx="40" cy="40" r="4" fill="#fff"/>'''),
    "icon_dept_f2_maws_keep.svg": ("#6f7ee8", "F2", "CONTAIN", '''<rect x="20" y="20" width="40" height="40" rx="8" fill="#0d1124" stroke="#6f7ee8" stroke-width="2.5"/><path d="M 28 40 L 52 40 M 40 28 L 40 52" stroke="#6f7ee8" stroke-width="3"/><circle cx="40" cy="40" r="6" fill="#f1df76"/>'''),
    "icon_dept_f3_extraction.svg": ("#e6c94d", "F3", "EXTRACT", '''<circle cx="40" cy="40" r="22" fill="#1c1808" stroke="#e6c94d" stroke-width="2.5"/><polygon points="40,22 56,36 40,58 24,36" fill="#e6c94d"/><circle cx="40" cy="40" r="5" fill="#ef4444"/>'''),
    "icon_dept_f4_insight_forge.svg": ("#47c978", "F4", "RESEARCH", '''<circle cx="40" cy="40" r="22" fill="#071a0f" stroke="#47c978" stroke-width="2.5"/><circle cx="40" cy="40" r="10" fill="none" stroke="#47c978" stroke-width="2.5"/><circle cx="40" cy="40" r="4" fill="#f1df76"/>'''),
    "icon_dept_f5_border_watch.svg": ("#d7d7d7", "F5", "BORDER", '''<polygon points="40,18 62,30 62,54 40,64 18,54 18,30" fill="#18181b" stroke="#d7d7d7" stroke-width="2.5"/><circle cx="40" cy="41" r="8" fill="#38bdf8"/>'''),
    "icon_dept_f6_deep_vault.svg": ("#8d2e42", "F6", "VAULT", '''<rect x="22" y="22" width="36" height="36" rx="6" fill="#1c0a0e" stroke="#8d2e42" stroke-width="2.5"/><circle cx="40" cy="40" r="8" fill="none" stroke="#f1df76" stroke-width="2"/><circle cx="40" cy="40" r="3" fill="#f1df76"/>'''),
    "icon_dept_f7_shadow_corps.svg": ("#f0a6c4", "F7", "SHADOW", '''<circle cx="40" cy="40" r="22" fill="#1e0a14" stroke="#f0a6c4" stroke-width="2.5"/><path d="M 26 40 Q 40 24 54 40 Q 40 56 26 40 Z" fill="#f0a6c4"/><circle cx="40" cy="40" r="4" fill="#000"/>'''),
    "icon_dept_f8_gate_watch.svg": ("#f4efa0", "F8", "GATE", '''<polygon points="40,16 64,58 16,58" fill="#181808" stroke="#f4efa0" stroke-width="2.5"/><circle cx="40" cy="44" r="8" fill="#ef4444"/><circle cx="40" cy="44" r="3" fill="#fff"/>'''),
    "the_hand_dr_icon_styled.svg": ("#f1df76", "HAND", "DIRECTORATE", '''<polygon points="40,14 66,28 66,58 40,70 14,58 14,28" fill="#141108" stroke="#f1df76" stroke-width="2.5"/><circle cx="40" cy="42" r="10" fill="#38bdf8"/>'''),
    "icon_reverie_directorate_minimal.svg": ("#38bdf8", "RD", "DIRECTORATE", '''<circle cx="40" cy="40" r="24" fill="#08101a" stroke="#38bdf8" stroke-width="2.5"/><polygon points="40,20 60,55 20,55" fill="#f1df76"/>'''),
}

for fn, (color, code_txt, label_txt, inner_svg) in floor_badges.items():
    code = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="80" height="80">
  <rect width="80" height="80" rx="12" fill="#05070a" stroke="{color}" stroke-width="2"/>
  {inner_svg}
</svg>'''
    with open(os.path.join(LAYOUT_HAND_DIR, fn), "w", encoding="utf-8") as f:
        f.write(code)
    # also save copy to assets/icons/ for fallback
    with open(os.path.join(ICONS_DIR, fn), "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Generated Floor Badge: {fn}")

# 4. City Zone Badges (HD 80x80) in layout/city/icons/
city_badges = {
    "icon_zone_a_core.svg": ("#f1df76", "ZONE A", '''<polygon points="40,16 64,58 16,58" fill="#181404" stroke="#f1df76" stroke-width="2.5"/><circle cx="40" cy="44" r="7" fill="#f1df76"/>'''),
    "icon_zone_b_west.svg": ("#38bdf8", "ZONE B", '''<circle cx="40" cy="40" r="22" fill="#06121a" stroke="#38bdf8" stroke-width="2.5"/><path d="M 28 40 Q 40 26 52 40 Q 40 54 28 40 Z" fill="#38bdf8"/>'''),
    "icon_zone_c_east.svg": ("#eab308", "ZONE C", '''<rect x="20" y="20" width="40" height="40" rx="6" fill="#181304" stroke="#eab308" stroke-width="2.5"/><polygon points="30,50 40,30 50,50" fill="#eab308"/>'''),
    "icon_zone_d_flanks.svg": ("#22c55e", "ZONE D", '''<circle cx="40" cy="40" r="22" fill="#06140a" stroke="#22c55e" stroke-width="2.5"/><polygon points="40,24 54,48 26,48" fill="#22c55e"/>'''),
    "icon_zone_e_bulwark.svg": ("#ef4444", "ZONE E", '''<polygon points="40,16 64,28 64,56 40,66 16,56 16,28" fill="#1a0608" stroke="#ef4444" stroke-width="2.5"/><circle cx="40" cy="42" r="8" fill="#fff"/>'''),
    "somnarak_city_icon.svg": ("#38bdf8", "CITY", '''<circle cx="40" cy="40" r="24" fill="#08101a" stroke="#38bdf8" stroke-width="2.5"/><polygon points="40,18 58,54 22,54" fill="#f1df76"/>'''),
}

for fn, (color, label_txt, inner_svg) in city_badges.items():
    code = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="80" height="80">
  <rect width="80" height="80" rx="12" fill="#05070a" stroke="{color}" stroke-width="2"/>
  {inner_svg}
</svg>'''
    with open(os.path.join(LAYOUT_CITY_DIR, fn), "w", encoding="utf-8") as f:
        f.write(code)
    # also save copy to assets/icons/ for fallback
    with open(os.path.join(ICONS_DIR, fn), "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Generated City Zone Badge: {fn}")

print("\nComplete HD SVG Suite Generated.")
