#!/usr/bin/env python3
"""
tools/build_all_entity_maw_and_banner_svgs.py
Generates high-detail, inset vector SVGs for all Sorrow Entities (se-001 to se-015),
all 27 M.A.W. equipment pieces (weapons, suits, gifts), category banners,
and reference icons in the 5 canonical Somnarak colors without border clipping.
"""

import os

WIKI_DIR = "/home/user/01_Somnarak_Wiki"
ENTITIES_DIR = os.path.join(WIKI_DIR, "assets/art/entities")
MAW_DIR = os.path.join(WIKI_DIR, "assets/art/maw")
BANNERS_DIR = os.path.join(WIKI_DIR, "assets/banners")
ASSETS_ICONS = os.path.join(WIKI_DIR, "assets/icons")
ICONS_DIR = "/home/user/icons"

for d in [ENTITIES_DIR, MAW_DIR, BANNERS_DIR, ASSETS_ICONS, ICONS_DIR]:
    os.makedirs(d, exist_ok=True)

def save_svg(content, relative_paths):
    for rel in relative_paths:
        full_path = os.path.join(WIKI_DIR, rel) if not rel.startswith("/") else rel
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        if "icons/" in rel:
            fname = os.path.basename(rel)
            root_icon_path = os.path.join(ICONS_DIR, fname)
            with open(root_icon_path, "w", encoding="utf-8") as f:
                f.write(content.strip() + "\n")

# ==============================================================================
# 1. ALL 10 CANONICAL SORROW ENTITY SVGs (200x200 Inset)
# ==============================================================================

ENTITIES = {
    "se-001": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <radialGradient id="se001Glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#090d16" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="192" height="192" rx="16" fill="#090d16" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="184" height="184" rx="12" fill="none" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1" stroke-dasharray="6 3"/>
  <circle cx="100" cy="100" r="75" fill="url(#se001Glow)"/>
  
  <!-- Bell Structure -->
  <path d="M 68 52 Q 100 32 132 52 L 142 128 Q 152 152 156 156 L 44 156 Q 48 152 58 128 Z" fill="#182333" stroke="#f1df76" stroke-width="2.8"/>
  <ellipse cx="100" cy="156" rx="56" ry="12" fill="#0e1724" stroke="#f1df76" stroke-width="2"/>
  <circle cx="100" cy="156" r="14" fill="#ef5b55" stroke="#f1df76" stroke-width="2"/>
  
  <!-- Crying Face Engravings & Tear Cracks -->
  <path d="M 100 72 L 95 94 L 108 114 L 100 138" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="86" cy="86" r="4.5" fill="#38bdf8"/>
  <circle cx="114" cy="86" r="4.5" fill="#38bdf8"/>
  <path d="M 86 90 Q 86 110 82 122" fill="none" stroke="#38bdf8" stroke-width="1.8"/>
  <path d="M 114 90 Q 114 110 118 122" fill="none" stroke="#38bdf8" stroke-width="1.8"/>
  <path d="M 90 106 Q 100 96 110 106" fill="none" stroke="#f1df76" stroke-width="2"/>
</svg>""",

    "se-002": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <radialGradient id="se002Glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#090d16" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="192" height="192" rx="16" fill="#090d16" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="8" y="8" width="184" height="184" rx="12" fill="none" stroke="rgba(241, 223, 118, 0.25)" stroke-width="1" stroke-dasharray="6 3"/>
  <circle cx="100" cy="100" r="75" fill="url(#se002Glow)"/>
  
  <!-- Grieving Colossus Monolithic Torso & Head -->
  <polygon points="100,26 142,52 142,126 100,166 58,126 58,52" fill="#1e1814" stroke="#f1df76" stroke-width="2.5"/>
  <polygon points="100,38 132,58 132,118 100,152 68,118 68,58" fill="#120c08" stroke="#ef4444" stroke-width="1.8"/>
  
  <!-- Weeping Golden Oil Eyes & Molten Fissures -->
  <circle cx="86" cy="68" r="6" fill="#f1df76"/>
  <circle cx="114" cy="68" r="6" fill="#f1df76"/>
  <path d="M 86,74 L 84,116 L 90,136" fill="none" stroke="#f1df76" stroke-width="2.5"/>
  <path d="M 114,74 L 116,116 L 110,136" fill="none" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="100" cy="102" r="14" fill="#ef4444" stroke="#f1df76" stroke-width="2"/>
</svg>""",

    "se-003": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <radialGradient id="se003Glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#090d16" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="192" height="192" rx="16" fill="#090d16" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="184" height="184" rx="12" fill="none" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1" stroke-dasharray="6 3"/>
  <circle cx="100" cy="100" r="75" fill="url(#se003Glow)"/>
  
  <!-- Wilderness Tide Vortex & Crimson Waves -->
  <path d="M 32,142 Q 60,60 100,100 Q 140,140 168,58 Q 140,154 100,154 Q 60,154 32,142 Z" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2.5"/>
  <path d="M 44,124 Q 72,52 100,88 Q 128,124 156,48 Q 132,138 100,138 Q 68,138 44,124 Z" fill="#ef4444" stroke="#fca5a5" stroke-width="1.8"/>
  <circle cx="100" cy="94" r="12" fill="#fff" stroke="#38bdf8" stroke-width="2"/>
</svg>""",

    "se-005": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect x="4" y="4" width="192" height="192" rx="16" fill="#090d16" stroke="#10b981" stroke-width="2.5"/>
  <rect x="8" y="8" width="184" height="184" rx="12" fill="none" stroke="rgba(16, 185, 129, 0.25)" stroke-width="1" stroke-dasharray="6 3"/>
  
  <!-- Smothering Mother Shroud & Embracing Arms -->
  <path d="M 100,32 C 70,32 46,70 46,120 C 46,162 100,168 100,168 C 100,168 154,162 154,120 C 154,70 130,32 100,32 Z" fill="#064e3b" stroke="#10b981" stroke-width="2.5"/>
  <path d="M 68,90 Q 100,140 132,90" fill="none" stroke="#f1df76" stroke-width="2.2"/>
  <circle cx="100" cy="62" r="14" fill="#022c22" stroke="#a7f3d0" stroke-width="1.8"/>
  <circle cx="100" cy="118" r="10" fill="#38bdf8" stroke="#fff" stroke-width="1.5"/>
</svg>""",

    "se-007": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect x="4" y="4" width="192" height="192" rx="16" fill="#090d16" stroke="#f8fafc" stroke-width="2.5"/>
  <rect x="8" y="8" width="184" height="184" rx="12" fill="none" stroke="rgba(248, 250, 252, 0.25)" stroke-width="1" stroke-dasharray="6 3"/>
  
  <!-- Brume Cloud & Spectral Floating Lanterns -->
  <path d="M 40,110 C 30,80 70,50 100,60 C 130,50 170,80 160,110 C 170,140 130,160 100,150 C 70,160 30,140 40,110 Z" fill="#1e293b" stroke="#f8fafc" stroke-width="2"/>
  <circle cx="76" cy="96" r="8" fill="#38bdf8" stroke="#fff" stroke-width="1.5"/>
  <circle cx="124" cy="96" r="8" fill="#f1df76" stroke="#fff" stroke-width="1.5"/>
  <circle cx="100" cy="120" r="10" fill="#ef4444" stroke="#fff" stroke-width="1.5"/>
</svg>""",

    "se-009": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect x="4" y="4" width="192" height="192" rx="16" fill="#090d16" stroke="#a855f7" stroke-width="2.5"/>
  <rect x="8" y="8" width="184" height="184" rx="12" fill="none" stroke="rgba(168, 85, 247, 0.25)" stroke-width="1" stroke-dasharray="6 3"/>
  
  <!-- Memory Weaver Silk Loom & Arachnid Limbs -->
  <circle cx="100" cy="100" r="32" fill="#2e1065" stroke="#a855f7" stroke-width="2.5"/>
  <polygon points="100,76 118,100 100,124 82,100" fill="#3b0764" stroke="#f1df76" stroke-width="1.8"/>
  <!-- 8 Silk Thread Limbs -->
  <line x1="80" y1="80" x2="36" y2="46" stroke="#c084fc" stroke-width="2"/>
  <line x1="120" y1="80" x2="164" y2="46" stroke="#c084fc" stroke-width="2"/>
  <line x1="72" y1="100" x2="28" y2="100" stroke="#c084fc" stroke-width="2"/>
  <line x1="128" y1="100" x2="172" y2="100" stroke="#c084fc" stroke-width="2"/>
  <line x1="80" y1="120" x2="36" y2="154" stroke="#c084fc" stroke-width="2"/>
  <line x1="120" y1="120" x2="164" y2="154" stroke="#c084fc" stroke-width="2"/>
  <circle cx="100" cy="100" r="6" fill="#f1df76"/>
</svg>""",

    "se-010": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <radialGradient id="se010Hole" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#000000"/>
      <stop offset="60%" stop-color="#1e082b"/>
      <stop offset="85%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#f1df76"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="192" height="192" rx="16" fill="#090d16" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="8" y="8" width="184" height="184" rx="12" fill="none" stroke="rgba(239, 68, 68, 0.25)" stroke-width="1" stroke-dasharray="6 3"/>
  
  <!-- Gravitational Event Horizon Singularity -->
  <circle cx="100" cy="100" r="68" fill="url(#se010Hole)" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="100" cy="100" r="38" fill="#000000" stroke="#38bdf8" stroke-width="2"/>
  <!-- Accretion Disk Orbit Lines -->
  <ellipse cx="100" cy="100" rx="82" ry="24" fill="none" stroke="#f1df76" stroke-width="2" stroke-dasharray="8 4" transform="rotate(-25 100 100)"/>
  <ellipse cx="100" cy="100" rx="82" ry="24" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6 4" transform="rotate(35 100 100)"/>
</svg>""",

    "se-011": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect x="4" y="4" width="192" height="192" rx="16" fill="#090d16" stroke="#f59e0b" stroke-width="2.5"/>
  <rect x="8" y="8" width="184" height="184" rx="12" fill="none" stroke="rgba(245, 158, 11, 0.25)" stroke-width="1" stroke-dasharray="6 3"/>
  
  <!-- Whispering Wall Stones with Open Mouths -->
  <rect x="36" y="36" width="128" height="128" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2.5"/>
  <!-- Wall Bricks & Mouths -->
  <circle cx="68" cy="68" r="14" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.8"/>
  <ellipse cx="68" cy="72" rx="5" ry="3" fill="#ef4444"/>
  <circle cx="132" cy="68" r="14" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.8"/>
  <ellipse cx="132" cy="72" rx="5" ry="3" fill="#ef4444"/>
  <circle cx="100" cy="124" r="16" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.8"/>
  <ellipse cx="100" cy="128" rx="6" ry="4" fill="#ef4444"/>
  <path d="M 68,52 Q 100,32 132,52" fill="none" stroke="#38bdf8" stroke-width="1.8"/>
</svg>""",

    "se-014": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect x="4" y="4" width="192" height="192" rx="16" fill="#090d16" stroke="#d97706" stroke-width="2.5"/>
  <rect x="8" y="8" width="184" height="184" rx="12" fill="none" stroke="rgba(217, 119, 6, 0.25)" stroke-width="1" stroke-dasharray="6 3"/>
  
  <!-- Debt Eater Serrated Coin Maw -->
  <polygon points="100,28 156,68 156,132 100,172 44,132 44,68" fill="#451a03" stroke="#f59e0b" stroke-width="2.5"/>
  <ellipse cx="100" cy="100" rx="38" ry="24" fill="#1c0a02" stroke="#ef4444" stroke-width="2"/>
  <!-- Gold Coin Teeth -->
  <circle cx="76" cy="90" r="5" fill="#f1df76"/><circle cx="92" cy="84" r="5" fill="#f1df76"/><circle cx="108" cy="84" r="5" fill="#f1df76"/><circle cx="124" cy="90" r="5" fill="#f1df76"/>
  <circle cx="76" cy="110" r="5" fill="#f1df76"/><circle cx="92" cy="116" r="5" fill="#f1df76"/><circle cx="108" cy="116" r="5" fill="#f1df76"/><circle cx="124" cy="110" r="5" fill="#f1df76"/>
</svg>""",

    "se-015": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect x="4" y="4" width="192" height="192" rx="16" fill="#090d16" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="184" height="184" rx="12" fill="none" stroke="rgba(241, 223, 118, 0.25)" stroke-width="1" stroke-dasharray="6 3"/>
  
  <!-- The Debt Scale (Cosmic Balance) -->
  <line x1="100" y1="36" x2="100" y2="164" stroke="#f1df76" stroke-width="4"/>
  <line x1="42" y1="62" x2="158" y2="62" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="100,32 108,46 92,46" fill="#ef4444"/>
  
  <!-- Left Pan (Heart) -->
  <line x1="52" y1="62" x2="38" y2="108" stroke="#38bdf8" stroke-width="1.8"/>
  <line x1="52" y1="62" x2="66" y2="108" stroke="#38bdf8" stroke-width="1.8"/>
  <ellipse cx="52" cy="110" rx="22" ry="6" fill="#1e293b" stroke="#f1df76" stroke-width="1.8"/>
  <circle cx="52" cy="102" r="7" fill="#ef4444"/>

  <!-- Right Pan (Debt Coins) -->
  <line x1="148" y1="62" x2="134" y2="108" stroke="#38bdf8" stroke-width="1.8"/>
  <line x1="148" y1="62" x2="162" y2="108" stroke="#38bdf8" stroke-width="1.8"/>
  <ellipse cx="148" cy="110" rx="22" ry="6" fill="#1e293b" stroke="#f1df76" stroke-width="1.8"/>
  <circle cx="144" cy="102" r="5" fill="#f1df76"/><circle cx="152" cy="102" r="5" fill="#f1df76"/>
</svg>"""
}

for code, svg_content in ENTITIES.items():
    save_svg(svg_content, [f"assets/art/entities/{code}.svg"])

print("All 10 Sorrow Entity vector SVGs built!")

# ==============================================================================
# 2. ALL 27 M.A.W. WEAPONS, SUITS, AND GIFTS (160x160 Inset)
# ==============================================================================

# 9 Canonical Sets x 3 Types (Weapon, Suit, Gift)
MAW_SETS = [
    ("001-01", "LAMENT'S", "#38bdf8", "#0c4a6e", "#1e293b"),
    ("002-01", "MOURNING", "#ef4444", "#7f1d1d", "#2d0505"),
    ("005-01", "EMBRACE", "#10b981", "#064e3b", "#022c22"),
    ("007-01", "HOPE", "#f8fafc", "#475569", "#0f172a"),
    ("009-01", "FORGOTTEN", "#a855f7", "#3b0764", "#2e1065"),
    ("010-01", "ABSOLUTE", "#ef4444", "#7f1d1d", "#000000"),
    ("011-01", "LISTENING", "#f59e0b", "#78350f", "#1e293b"),
    ("014-01", "DEBT", "#d97706", "#78350f", "#451a03"),
    ("015-01", "BALANCE", "#f1df76", "#78350f", "#0f172a")
]

for set_code, name, col, dark_col, deep_col in MAW_SETS:
    # 1. Weapon (maw-w)
    weapon_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="100%" height="100%">
  <rect x="4" y="4" width="152" height="152" rx="12" fill="{deep_col}" stroke="{col}" stroke-width="2.5"/>
  <rect x="7" y="7" width="146" height="146" rx="9" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1"/>
  <!-- Weapon Blade / Staff / Maul -->
  <line x1="28" y1="132" x2="132" y2="28" stroke="{col}" stroke-width="5" stroke-linecap="round"/>
  <polygon points="120,20 140,40 120,45" fill="#f1df76"/>
  <circle cx="50" cy="110" r="9" fill="#ef4444" stroke="#fff" stroke-width="1.5"/>
  <text x="16" y="24" fill="{col}" font-family="Impact, Arial, sans-serif" font-size="9" letter-spacing="1">M.A.W. WEAPON</text>
</svg>"""

    # 2. Suit (maw-s)
    suit_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="100%" height="100%">
  <rect x="4" y="4" width="152" height="152" rx="12" fill="{deep_col}" stroke="{col}" stroke-width="2.5"/>
  <rect x="7" y="7" width="146" height="146" rx="9" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1"/>
  <!-- Suit Cuirass / Shroud -->
  <polygon points="80,36 122,54 112,122 80,138 48,122 38,54" fill="{dark_col}" stroke="{col}" stroke-width="2.5"/>
  <polygon points="80,48 106,62 98,112 80,124 62,112 54,62" fill="#0f172a" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="80" cy="76" r="8" fill="#ef4444" stroke="#fff" stroke-width="1.5"/>
  <text x="16" y="24" fill="{col}" font-family="Impact, Arial, sans-serif" font-size="9" letter-spacing="1">M.A.W. SUIT</text>
</svg>"""

    # 3. Gift (maw-g)
    gift_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="100%" height="100%">
  <rect x="4" y="4" width="152" height="152" rx="12" fill="{deep_col}" stroke="{col}" stroke-width="2.5"/>
  <rect x="7" y="7" width="146" height="146" rx="9" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1"/>
  <!-- Gift Relic Crest -->
  <polygon points="80,34 118,56 118,104 80,126 42,104 42,56" fill="{dark_col}" stroke="#f1df76" stroke-width="2"/>
  <circle cx="80" cy="80" r="18" fill="#0f172a" stroke="{col}" stroke-width="2"/>
  <polygon points="80,68 89,80 80,92 71,80" fill="#fff"/>
  <text x="16" y="24" fill="{col}" font-family="Impact, Arial, sans-serif" font-size="9" letter-spacing="1">M.A.W. GIFT</text>
</svg>"""

    save_svg(weapon_svg, [f"assets/art/maw/maw-w-{set_code}.svg"])
    save_svg(suit_svg, [f"assets/art/maw/maw-s-{set_code}.svg"])
    save_svg(gift_svg, [f"assets/art/maw/maw-g-{set_code}.svg"])

print("All 27 M.A.W. equipment SVGs built!")

# ==============================================================================
# 3. CATEGORY BANNERS & REFERENCE ICONS
# ==============================================================================

BANNERS = [
    ("characters", "PERSONNEL & ECHO-CORES", "#f1df76", "#78350f"),
    ("entities", "SORROW ENTITIES CODEX", "#ef4444", "#7f1d1d"),
    ("factions", "FACTIONS & SYNDICATES", "#a855f7", "#3b0764"),
    ("locations", "ATLAS & CARTOGRAPHY", "#38bdf8", "#0c4a6e"),
    ("lore", "LORE & COSMOLOGY", "#fbbf24", "#451a03"),
    ("mechanics", "SYSTEMS & MECHANICS", "#10b981", "#064e3b"),
    ("maw", "M.A.W. ARSENAL", "#f59e0b", "#78350f")
]

for tag, title, col, dark_col in BANNERS:
    ban_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="3" y="3" width="114" height="114" rx="14" fill="#070a12" stroke="{col}" stroke-width="2.5"/>
  <rect x="6" y="6" width="108" height="108" rx="10" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1"/>
  <circle cx="60" cy="54" r="32" fill="{dark_col}" stroke="{col}" stroke-width="2"/>
  <polygon points="60,34 76,54 60,74 44,54" fill="#fff"/>
</svg>"""
    save_svg(ban_svg, [f"assets/icons/banner_{tag}.svg"])

print("Category banners generated!")
