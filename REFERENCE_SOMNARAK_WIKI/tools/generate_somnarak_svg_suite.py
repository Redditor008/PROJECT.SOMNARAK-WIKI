import os, sys

ICONS_DIR = "/home/user/01_Somnarak_Wiki/assets/icons"
ART_ENT_DIR = "/home/user/01_Somnarak_Wiki/assets/art/entities"
ART_MAW_DIR = "/home/user/01_Somnarak_Wiki/assets/art/maw"
os.makedirs(ICONS_DIR, exist_ok=True)
os.makedirs(ART_ENT_DIR, exist_ok=True)
os.makedirs(ART_MAW_DIR, exist_ok=True)

# 5 Somnarak Canonical Colors:
# Gold: #f1df76, #cfc566
# Cyan/Blue: #38bdf8, #0ea5e9, #075985
# Crimson/Red: #ef5b55, #dc2626, #641a22
# Dark/Black: #05070a, #0f172a, #1e293b
# Pale/White: #f8fafc, #cbd5e1, #94a3b8

svg_library = {}

# 1. Master Somnarak Emblem (The Alpha Tree Eye & Gilded Sorrow Crown)
svg_library["somnarak_icon.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff3a0"/>
      <stop offset="50%" stop-color="#f1df76"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <radialGradient id="cyanGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="100" height="100" rx="14" fill="#05070a" stroke="#f1df76" stroke-width="2"/>
  <circle cx="50" cy="50" r="38" fill="url(#cyanGlow)" opacity="0.35"/>
  <circle cx="50" cy="50" r="32" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,2"/>
  <!-- Diamond Seal -->
  <polygon points="50,14 86,50 50,86 14,50" fill="#090d16" stroke="url(#goldGrad)" stroke-width="2.5"/>
  <!-- Inner Sorrow Eye -->
  <path d="M 28 50 Q 50 28 72 50 Q 50 72 28 50 Z" fill="#040609" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="50" cy="50" r="10" fill="url(#goldGrad)"/>
  <circle cx="50" cy="50" r="4" fill="#040609"/>
  <!-- Rays -->
  <line x1="50" y1="6" x2="50" y2="14" stroke="#f1df76" stroke-width="2"/>
  <line x1="50" y1="86" x2="50" y2="94" stroke="#f1df76" stroke-width="2"/>
  <line x1="6" y1="50" x2="14" y2="50" stroke="#f1df76" stroke-width="2"/>
  <line x1="86" y1="50" x2="94" y2="50" stroke="#f1df76" stroke-width="2"/>
</svg>'''

# 2. Category Nav Icons
svg_library["nav_characters.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <rect width="48" height="48" rx="8" fill="#080c14" stroke="#38bdf8" stroke-width="1.5"/>
  <circle cx="24" cy="18" r="8" fill="#111a28" stroke="#f1df76" stroke-width="1.8"/>
  <path d="M 12 38 C 12 28, 36 28, 36 38" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>
  <circle cx="24" cy="18" r="3" fill="#ef5b55"/>
</svg>'''

svg_library["nav_lore.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <rect width="48" height="48" rx="8" fill="#080c14" stroke="#f1df76" stroke-width="1.5"/>
  <!-- Tree & Tome -->
  <path d="M 10 36 L 24 30 L 38 36 L 38 14 L 24 8 L 10 14 Z" fill="#0f172a" stroke="#f1df76" stroke-width="1.8"/>
  <line x1="24" y1="8" x2="24" y2="30" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="24" cy="18" r="4" fill="#38bdf8"/>
</svg>'''

svg_library["nav_locations.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <rect width="48" height="48" rx="8" fill="#080c14" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Compass / Zone Map -->
  <circle cx="24" cy="24" r="15" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,1.5"/>
  <polygon points="24,11 28,24 24,21 20,24" fill="#ef5b55"/>
  <polygon points="24,37 28,24 24,27 20,24" fill="#f1df76"/>
</svg>'''

svg_library["nav_factions.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <rect width="48" height="48" rx="8" fill="#080c14" stroke="#ef5b55" stroke-width="1.5"/>
  <!-- Heraldic Crest -->
  <polygon points="24,8 38,14 38,28 24,40 10,28 10,14" fill="#18111b" stroke="#f1df76" stroke-width="1.8"/>
  <path d="M 17 22 L 24 16 L 31 22 L 24 32 Z" fill="#ef5b55"/>
</svg>'''

svg_library["floor-1-command.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <rect width="48" height="48" rx="8" fill="#080c14" stroke="#f1df76" stroke-width="1.5"/>
  <!-- Facility Floor Stack -->
  <line x1="12" y1="14" x2="36" y2="14" stroke="#38bdf8" stroke-width="2"/>
  <line x1="12" y1="22" x2="36" y2="22" stroke="#f1df76" stroke-width="2"/>
  <line x1="12" y1="30" x2="36" y2="30" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="24" cy="22" r="5" fill="#f1df76" stroke="#05070a" stroke-width="1.5"/>
</svg>'''

svg_library["nav_entities.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <rect width="48" height="48" rx="8" fill="#080c14" stroke="#ef5b55" stroke-width="1.5"/>
  <!-- Sorrow Entity Crystalline Tear -->
  <path d="M 24 8 C 34 20, 36 30, 24 40 C 12 30, 14 20, 24 8 Z" fill="#2b0d12" stroke="#ef5b55" stroke-width="1.8"/>
  <circle cx="24" cy="26" r="4" fill="#f1df76"/>
</svg>'''

svg_library["maw.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <rect width="48" height="48" rx="8" fill="#080c14" stroke="#f1df76" stroke-width="1.5"/>
  <!-- Crossed Weapon & Shield -->
  <line x1="12" y1="12" x2="36" y2="36" stroke="#ef5b55" stroke-width="2.2" stroke-linecap="round"/>
  <line x1="36" y1="12" x2="12" y2="36" stroke="#38bdf8" stroke-width="2.2" stroke-linecap="round"/>
  <circle cx="24" cy="24" r="6" fill="#f1df76" stroke="#05070a" stroke-width="1.5"/>
</svg>'''

svg_library["nav_mechanics.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <rect width="48" height="48" rx="8" fill="#080c14" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Cog & Circuit -->
  <circle cx="24" cy="24" r="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <line x1="24" y1="8" x2="24" y2="14" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="24" y1="34" x2="24" y2="40" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="8" y1="24" x2="14" y2="24" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="34" y1="24" x2="40" y2="24" stroke="#f1df76" stroke-width="2.5"/>
</svg>'''

# 3. Damage Type Icons (RED, WHITE, BLACK, PALE)
svg_library["damage_red.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="6" fill="#1f090b" stroke="#ef4444" stroke-width="1.5"/>
  <polygon points="16,6 26,24 6,24" fill="#ef4444"/>
  <circle cx="16" cy="18" r="3" fill="#fff"/>
</svg>'''

svg_library["damage_white.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="6" fill="#0d1b2a" stroke="#f8fafc" stroke-width="1.5"/>
  <polygon points="16,6 26,16 16,26 6,16" fill="#f8fafc"/>
  <circle cx="16" cy="16" r="3" fill="#38bdf8"/>
</svg>'''

svg_library["damage_black.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="6" fill="#090514" stroke="#a855f7" stroke-width="1.5"/>
  <circle cx="16" cy="16" r="10" fill="#a855f7"/>
  <path d="M 16 8 L 19 14 L 25 16 L 19 18 L 16 24 L 13 18 L 7 16 L 13 14 Z" fill="#090514"/>
</svg>'''

svg_library["damage_pale.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="6" fill="#081820" stroke="#38bdf8" stroke-width="1.5"/>
  <circle cx="16" cy="16" r="9" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="16" cy="16" r="4" fill="#38bdf8"/>
  <line x1="16" y1="4" x2="16" y2="28" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="4" y1="16" x2="28" y2="16" stroke="#38bdf8" stroke-width="1.5"/>
</svg>'''

# 4. Work Type Icons (Insight, Attachment, Repression, Extraction)
svg_library["work_insight.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="6" fill="#081826" stroke="#38bdf8" stroke-width="1.5"/>
  <circle cx="16" cy="16" r="7" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="16" cy="16" r="2.5" fill="#f1df76"/>
  <line x1="16" y1="4" x2="16" y2="7" stroke="#38bdf8" stroke-width="2"/>
  <line x1="16" y1="25" x2="16" y2="28" stroke="#38bdf8" stroke-width="2"/>
</svg>'''

svg_library["work_attachment.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="6" fill="#1a1808" stroke="#f1df76" stroke-width="1.5"/>
  <path d="M 16 24 C 10 18, 8 13, 11 9 C 14 6, 16 10, 16 10 C 16 10, 18 6, 21 9 C 24 13, 22 18, 16 24 Z" fill="#f1df76"/>
</svg>'''

svg_library["work_repression.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="6" fill="#1f090b" stroke="#ef4444" stroke-width="1.5"/>
  <polygon points="16,6 26,12 26,22 16,28 6,22 6,12" fill="#ef4444"/>
  <line x1="11" y1="11" x2="21" y2="21" stroke="#0f172a" stroke-width="2"/>
  <line x1="21" y1="11" x2="11" y2="21" stroke="#0f172a" stroke-width="2"/>
</svg>'''

svg_library["work_extraction.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="6" fill="#14081c" stroke="#c084fc" stroke-width="1.5"/>
  <path d="M 16 6 L 24 16 L 16 26 L 8 16 Z" fill="#c084fc"/>
  <circle cx="16" cy="16" r="3" fill="#f8fafc"/>
</svg>'''

# 5. Risk Classification Icons (ZAYIN, TETH, HE, WAW, ALEPH)
svg_library["risk_zayin.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="6" fill="#042f2e" stroke="#2dd4bf" stroke-width="1.5"/>
  <text x="16" y="22" font-family="Impact, sans-serif" font-size="14" fill="#2dd4bf" text-anchor="middle">Z</text>
</svg>'''

svg_library["risk_teth.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="6" fill="#082f49" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="16" y="22" font-family="Impact, sans-serif" font-size="14" fill="#38bdf8" text-anchor="middle">T</text>
</svg>'''

svg_library["risk_he.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="6" fill="#2e2004" stroke="#facc15" stroke-width="1.5"/>
  <text x="16" y="22" font-family="Impact, sans-serif" font-size="14" fill="#facc15" text-anchor="middle">HE</text>
</svg>'''

svg_library["risk_waw.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="6" fill="#2e0827" stroke="#e879f9" stroke-width="1.5"/>
  <text x="16" y="22" font-family="Impact, sans-serif" font-size="14" fill="#e879f9" text-anchor="middle">W</text>
</svg>'''

svg_library["risk_aleph.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="6" fill="#3b0707" stroke="#f87171" stroke-width="1.5"/>
  <text x="16" y="22" font-family="Impact, sans-serif" font-size="14" fill="#f87171" text-anchor="middle">A</text>
</svg>'''

# 6. Write all SVGs into assets/icons/
for fname, svg_code in svg_library.items():
    with open(os.path.join(ICONS_DIR, fname), 'w', encoding='utf-8') as f:
        f.write(svg_code)
    print(f"Written SVG: {fname}")

print(f"\nSuccessfully generated {len(svg_library)} canonical SVGs.")
