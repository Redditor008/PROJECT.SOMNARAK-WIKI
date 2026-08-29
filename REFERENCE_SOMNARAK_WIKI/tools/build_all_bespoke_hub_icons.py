#!/usr/bin/env python3
"""
tools/build_all_bespoke_hub_icons.py
Generates individual, bespoke, 100% non-repeated vector SVG icons for every card
across all Hub pages (Characters, Locations, Lore, Mechanics, Departments, Factions)
matching the unified Somnarak 5-color aesthetic with 0 mismatched styles.
"""

import os

WIKI_DIR = "/home/user/01_Somnarak_Wiki"
ASSETS_ICONS = os.path.join(WIKI_DIR, "assets/icons")
AVATARS_DIR = os.path.join(WIKI_DIR, "assets/avatars")
CITY_ICONS = os.path.join(WIKI_DIR, "assets/layout/city/icons")
HAND_ICONS = os.path.join(WIKI_DIR, "assets/layout/hand/icons")
ICONS_DIR = "/home/user/icons"

for d in [ASSETS_ICONS, AVATARS_DIR, CITY_ICONS, HAND_ICONS, ICONS_DIR]:
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
# 1. BESPOKE SECONDARY & KEY CHARACTER AVATARS (120x120 Circular Badges)
# ==============================================================================

SECONDARY_CHARS = [
    ("doha", "DOHA", "BLACK MARKET BROKER", "#f59e0b", "#78350f", "#241204",
     """<circle cx="60" cy="50" r="24" fill="#78350f" stroke="#f59e0b" stroke-width="2.2"/>
        <polygon points="60,32 74,48 60,64 46,48" fill="#f1df76"/>
        <circle cx="60" cy="50" r="5" fill="#fff"/>
        <text x="60" y="104" fill="#f59e0b" font-family="Impact" font-size="10" letter-spacing="1" text-anchor="middle">BROKER DOHA</text>"""),

    ("joon", "JOON", "VETERAN MENDER", "#10b981", "#064e3b", "#021c14",
     """<circle cx="60" cy="50" r="24" fill="#064e3b" stroke="#10b981" stroke-width="2.2"/>
        <path d="M 46,50 L 60,36 L 74,50 L 60,64 Z" fill="#a7f3d0" stroke="#10b981" stroke-width="1.5"/>
        <line x1="60" y1="36" x2="60" y2="64" stroke="#064e3b" stroke-width="2"/>
        <text x="60" y="104" fill="#10b981" font-family="Impact" font-size="10" letter-spacing="1" text-anchor="middle">MENDER JOON</text>"""),

    ("yeonhwa", "YEONHWA", "SED LEAD CARTOGRAPHER", "#38bdf8", "#0c4a6e", "#041424",
     """<circle cx="60" cy="50" r="24" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2.2"/>
        <polygon points="60,30 76,64 44,64" fill="#1e3a8a" stroke="#7dd3fc" stroke-width="1.8"/>
        <circle cx="60" cy="52" r="6" fill="#f1df76"/>
        <text x="60" y="104" fill="#38bdf8" font-family="Impact" font-size="10" letter-spacing="1" text-anchor="middle">YEONHWA</text>"""),

    ("taeho", "TAEHO", "CARAVAN MASTER", "#eab308", "#713f12", "#241402",
     """<circle cx="60" cy="50" r="24" fill="#713f12" stroke="#eab308" stroke-width="2.2"/>
        <path d="M 40,62 L 60,34 L 80,62 Z" fill="#a16207" stroke="#fef08a" stroke-width="1.8"/>
        <circle cx="60" cy="48" r="5" fill="#fff"/>
        <text x="60" y="104" fill="#eab308" font-family="Impact" font-size="10" letter-spacing="1" text-anchor="middle">TAEHO</text>"""),

    ("kael", "KAEL", "SED VANGUARD DIVER", "#ef4444", "#7f1d1d", "#240408",
     """<circle cx="60" cy="50" r="24" fill="#7f1d1d" stroke="#ef4444" stroke-width="2.2"/>
        <polygon points="60,32 78,54 60,68 42,54" fill="#991b1b" stroke="#fca5a5" stroke-width="1.8"/>
        <circle cx="60" cy="50" r="5" fill="#fff"/>
        <text x="60" y="104" fill="#ef4444" font-family="Impact" font-size="10" letter-spacing="1" text-anchor="middle">KAEL DIVER</text>"""),

    ("minho", "MINHO", "ARCHIVES CODEX RECORD", "#8b5cf6", "#3b0764", "#160424",
     """<circle cx="60" cy="50" r="24" fill="#3b0764" stroke="#8b5cf6" stroke-width="2.2"/>
        <rect x="48" y="38" width="24" height="24" rx="3" fill="#2e1065" stroke="#c084fc" stroke-width="1.8"/>
        <line x1="60" y1="38" x2="60" y2="62" stroke="#f1df76" stroke-width="1.5"/>
        <text x="60" y="104" fill="#8b5cf6" font-family="Impact" font-size="10" letter-spacing="1" text-anchor="middle">MINHO CODEX</text>"""),

    ("sora", "SORA", "RESONANCE RESEARCHER", "#06b6d4", "#0e7490", "#021c22",
     """<circle cx="60" cy="50" r="24" fill="#0e7490" stroke="#06b6d4" stroke-width="2.2"/>
        <circle cx="60" cy="50" r="14" fill="#083344" stroke="#67e8f9" stroke-width="1.8"/>
        <polygon points="60,42 66,50 60,58 54,50" fill="#fff"/>
        <text x="60" y="104" fill="#06b6d4" font-family="Impact" font-size="10" letter-spacing="1" text-anchor="middle">SORA R&amp;D</text>"""),

    ("soojin", "SOOJIN", "VEIL PATROL VANGUARD", "#14b8a6", "#0f766e", "#04201c",
     """<circle cx="60" cy="50" r="24" fill="#0f766e" stroke="#14b8a6" stroke-width="2.2"/>
        <path d="M 60,32 L 76,44 L 76,60 L 60,70 L 44,60 L 44,44 Z" fill="#115e59" stroke="#5eead4" stroke-width="1.8"/>
        <circle cx="60" cy="51" r="5" fill="#f1df76"/>
        <text x="60" y="104" fill="#14b8a6" font-family="Impact" font-size="10" letter-spacing="1" text-anchor="middle">SOOJIN</text>"""),

    ("cheonbulok_refugees", "CHEONBULOK", "FRONTIER REFUGEES", "#d97706", "#78350f", "#241202",
     """<circle cx="60" cy="50" r="24" fill="#78350f" stroke="#d97706" stroke-width="2.2"/>
        <polygon points="46,60 60,36 74,60" fill="#451a03" stroke="#fbbf24" stroke-width="1.8"/>
        <circle cx="48" cy="52" r="4" fill="#fff"/><circle cx="72" cy="52" r="4" fill="#fff"/>
        <text x="60" y="104" fill="#d97706" font-family="Impact" font-size="9" letter-spacing="1" text-anchor="middle">REFUGEES</text>"""),

    ("high_architects", "HIGH ARCHITECTS", "METROPOLIS GUILD", "#a855f7", "#3b0764", "#160424",
     """<circle cx="60" cy="50" r="24" fill="#3b0764" stroke="#a855f7" stroke-width="2.2"/>
        <polygon points="60,30 78,44 78,66 60,78 42,66 42,44" fill="#2e1065" stroke="#f1df76" stroke-width="1.8"/>
        <circle cx="60" cy="54" r="6" fill="#fff"/>
        <text x="60" y="104" fill="#a855f7" font-family="Impact" font-size="9" letter-spacing="1" text-anchor="middle">ARCHITECTS</text>""")
]

for tag, name, role, col, dark_col, deep_col, inner_gfx in SECONDARY_CHARS:
    avatar_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="{deep_col}" stroke="{col}" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="48" fill="none" stroke="rgba(255, 255, 255, 0.2)" stroke-width="1" stroke-dasharray="4 2"/>
  {inner_gfx}
</svg>"""
    save_svg(avatar_svg, [
        f"assets/avatars/avatar_char_{tag}.svg",
        f"assets/icons/avatar_char_{tag}.svg"
    ])

print("Bespoke secondary character avatars generated!")

# ==============================================================================
# 2. BESPOKE LOCATION LANDMARK ICONS (100x100 Inset)
# ==============================================================================

LOCATIONS = [
    ("the_maw", "THE MAW", "#ef4444", "#7f1d1d", "#240408",
     """<ellipse cx="50" cy="52" rx="30" ry="20" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
        <polygon points="32,46 40,54 48,46 56,54 64,46 68,54" fill="#fff"/>
        <circle cx="50" cy="54" r="6" fill="#f1df76"/>"""),

    ("the_desolate", "THE DESOLATE", "#d97706", "#78350f", "#241202",
     """<path d="M 20,70 L 50,28 L 80,70 Z" fill="#451a03" stroke="#f59e0b" stroke-width="2"/>
        <circle cx="50" cy="46" r="6" fill="#fef08a"/>
        <line x1="16" y1="76" x2="84" y2="76" stroke="#f1df76" stroke-width="2"/>"""),

    ("the_hollow_glass", "HOLLOW GLASS", "#38bdf8", "#0c4a6e", "#041424",
     """<polygon points="50,18 78,42 70,82 30,82 22,42" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
        <polygon points="50,28 68,46 62,74 38,74 32,46" fill="#0c4a6e" stroke="#7dd3fc" stroke-width="1.5"/>
        <circle cx="50" cy="52" r="6" fill="#fff"/>"""),

    ("the_library_of_stolen_pasts", "STOLEN PASTS", "#8b5cf6", "#3b0764", "#160424",
     """<rect x="28" y="28" width="44" height="48" rx="4" fill="#2e1065" stroke="#8b5cf6" stroke-width="2"/>
        <line x1="50" y1="28" x2="50" y2="76" stroke="#f1df76" stroke-width="2"/>
        <line x1="34" y1="42" x2="44" y2="42" stroke="#c084fc" stroke-width="1.5"/>
        <line x1="56" y1="42" x2="66" y2="42" stroke="#c084fc" stroke-width="1.5"/>
        <line x1="34" y1="56" x2="44" y2="56" stroke="#c084fc" stroke-width="1.5"/>
        <line x1="56" y1="56" x2="66" y2="56" stroke="#c084fc" stroke-width="1.5"/>"""),

    ("the_orphan_bell_tower", "BELL TOWER", "#f1df76", "#78350f", "#241804",
     """<polygon points="40,24 60,24 66,74 34,74" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
        <ellipse cx="50" cy="74" rx="18" ry="6" fill="#78350f" stroke="#f1df76" stroke-width="1.5"/>
        <circle cx="50" cy="74" r="5" fill="#ef4444"/>
        <line x1="50" y1="24" x2="50" y2="14" stroke="#38bdf8" stroke-width="2"/>"""),

    ("unknown_cities", "UNKNOWN CITIES", "#64748b", "#1e293b", "#080c14",
     """<polygon points="50,20 80,44 70,82 30,82 20,44" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
        <circle cx="50" cy="52" r="14" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.8"/>
        <text x="50" y="58" fill="#f1df76" font-family="Impact" font-size="16" text-anchor="middle">?</text>""")
]

for tag, name, col, dark_col, deep_col, inner_gfx in LOCATIONS:
    loc_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="{deep_col}" stroke="{col}" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1" stroke-dasharray="4 2"/>
  {inner_gfx}
</svg>"""
    save_svg(loc_svg, [
        f"assets/icons/icon_loc_{tag}.svg",
        f"assets/layout/city/icons/icon_loc_{tag}.svg"
    ])

print("Bespoke location landmark icons generated!")

# ==============================================================================
# 3. BESPOKE LORE COMPENDIUM ICONS (100x100 Inset)
# ==============================================================================

LORE_ITEMS = [
    ("three_ages", "THREE AGES", "#f1df76", "#78350f", "#241804",
     """<circle cx="50" cy="50" r="28" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
        <polygon points="50,26 70,66 30,66" fill="#78350f" stroke="#fbbf24" stroke-width="1.8"/>
        <circle cx="50" cy="52" r="6" fill="#38bdf8"/>"""),

    ("absolvohan", "ABSOLVOHAN", "#38bdf8", "#0c4a6e", "#041424",
     """<circle cx="50" cy="50" r="30" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
        <line x1="50" y1="24" x2="50" y2="50" stroke="#f1df76" stroke-width="2.5"/>
        <line x1="50" y1="50" x2="70" y2="50" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="50" cy="50" r="4" fill="#fff"/>"""),

    ("doorspeech", "DOORSPEECH", "#ef4444", "#7f1d1d", "#240408",
     """<rect x="32" y="24" width="36" height="56" rx="4" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
        <line x1="50" y1="24" x2="50" y2="80" stroke="#f1df76" stroke-width="1.8"/>
        <circle cx="62" cy="54" r="3" fill="#f1df76"/>"""),

    ("dawn_of_hope", "DAWN OF HOPE", "#f1df76", "#78350f", "#241804",
     """<circle cx="50" cy="52" r="28" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
        <polygon points="50,28 58,46 76,48 62,60 68,78 50,68 32,78 38,60 24,48 42,46" fill="#f1df76"/>"""),

    ("taboo_resonance", "TABOO LAWS", "#a855f7", "#3b0764", "#160424",
     """<polygon points="50,18 80,44 70,82 30,82 20,44" fill="#2e1065" stroke="#a855f7" stroke-width="2"/>
        <polygon points="50,30 68,48 60,72 40,72 32,48" fill="#3b0764" stroke="#f1df76" stroke-width="1.5"/>
        <circle cx="50" cy="52" r="6" fill="#ef4444"/>"""),

    ("cheongula", "CHEONGULA", "#06b6d4", "#0e7490", "#021c22",
     """<circle cx="50" cy="50" r="28" fill="#083344" stroke="#06b6d4" stroke-width="2"/>
        <path d="M 34,50 Q 50,28 66,50 Q 50,72 34,50 Z" fill="#0e7490" stroke="#67e8f9" stroke-width="1.8"/>
        <circle cx="50" cy="50" r="5" fill="#f1df76"/>"""),

    ("night_hazards", "NIGHT HAZARDS", "#ef4444", "#7f1d1d", "#240408",
     """<polygon points="50,20 82,78 18,78" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
        <circle cx="50" cy="56" r="8" fill="#ef4444"/>
        <line x1="50" y1="46" x2="50" y2="62" stroke="#fff" stroke-width="2.2"/>
        <circle cx="50" cy="70" r="2" fill="#fff"/>"""),

    ("named_fractures", "FRACTURES", "#eab308", "#713f12", "#241402",
     """<polygon points="50,18 80,50 50,82 20,50" fill="#451a03" stroke="#eab308" stroke-width="2"/>
        <path d="M 32,40 L 48,56 L 68,36" fill="none" stroke="#ef4444" stroke-width="2.5"/>"""),

    ("dream_realm", "DREAM REALM", "#8b5cf6", "#3b0764", "#160424",
     """<circle cx="50" cy="50" r="28" fill="#2e1065" stroke="#8b5cf6" stroke-width="2"/>
        <circle cx="50" cy="50" r="14" fill="#3b0764" stroke="#c084fc" stroke-width="1.8"/>
        <circle cx="50" cy="50" r="5" fill="#f1df76"/>"""),

    ("weeping_effluent", "WEEPING CANALS", "#0284c7", "#0c4a6e", "#041424",
     """<circle cx="50" cy="50" r="28" fill="#082f49" stroke="#0284c7" stroke-width="2"/>
        <path d="M 30,50 Q 40,32 50,50 T 70,50" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
        <path d="M 30,62 Q 40,44 50,62 T 70,62" fill="none" stroke="#7dd3fc" stroke-width="2"/>"""),

    ("daily_life", "DAILY LIFE", "#10b981", "#064e3b", "#021c14",
     """<rect x="28" y="28" width="44" height="44" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
        <polygon points="50,34 64,48 50,62 36,48" fill="#047857" stroke="#a7f3d0" stroke-width="1.5"/>
        <circle cx="50" cy="48" r="4" fill="#f1df76"/>"""),

    ("name_registry", "NAME REGISTRY", "#d97706", "#78350f", "#241202",
     """<rect x="28" y="24" width="44" height="52" rx="4" fill="#451a03" stroke="#d97706" stroke-width="2"/>
        <line x1="36" y1="36" x2="64" y2="36" stroke="#f1df76" stroke-width="2"/>
        <line x1="36" y1="48" x2="64" y2="48" stroke="#f1df76" stroke-width="2"/>
        <line x1="36" y1="60" x2="54" y2="60" stroke="#f1df76" stroke-width="2"/>""")
]

for tag, name, col, dark_col, deep_col, inner_gfx in LORE_ITEMS:
    lore_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="{deep_col}" stroke="{col}" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1" stroke-dasharray="4 2"/>
  {inner_gfx}
</svg>"""
    save_svg(lore_svg, [f"assets/icons/icon_lore_{tag}.svg"])

print("Bespoke lore compendium icons generated!")

# ==============================================================================
# 4. BESPOKE MECHANICS TACTICAL ICONS (100x100 Inset)
# ==============================================================================

MECHANICS_ITEMS = [
    ("four_work_types", "WORK TYPES", "#ef4444", "#7f1d1d", "#240408",
     """<rect x="26" y="26" width="22" height="22" rx="2" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.5"/>
        <rect x="52" y="26" width="22" height="22" rx="2" fill="#0f172a" stroke="#f8fafc" stroke-width="1.5"/>
        <rect x="26" y="52" width="22" height="22" rx="2" fill="#050508" stroke="#f1df76" stroke-width="1.5"/>
        <rect x="52" y="52" width="22" height="22" rx="2" fill="#041824" stroke="#38bdf8" stroke-width="1.5"/>"""),

    ("han_energy_damage", "DAMAGE MATRIX", "#38bdf8", "#0c4a6e", "#041424",
     """<circle cx="50" cy="50" r="28" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
        <polygon points="50,28 66,44 50,60 34,44" fill="#ef4444"/>
        <polygon points="50,44 66,60 50,76 34,60" fill="#38bdf8"/>"""),

    ("resonant_clash", "CLASH SYSTEM", "#f1df76", "#78350f", "#241804",
     """<line x1="28" y1="72" x2="72" y2="28" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
        <line x1="28" y1="28" x2="72" y2="72" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
        <circle cx="50" cy="50" r="10" fill="#f1df76" stroke="#fff" stroke-width="2"/>"""),

    ("fracture_therapy", "PANIC THERAPY", "#10b981", "#064e3b", "#021c14",
     """<circle cx="50" cy="50" r="28" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
        <rect x="44" y="30" width="12" height="40" fill="#fff" rx="2"/>
        <rect x="30" y="44" width="40" height="12" fill="#fff" rx="2"/>"""),

    ("containment_suppression", "CONTAINMENT OPS", "#8b5cf6", "#3b0764", "#160424",
     """<rect x="28" y="28" width="44" height="44" rx="4" fill="#2e1065" stroke="#8b5cf6" stroke-width="2"/>
        <circle cx="50" cy="50" r="12" fill="#ef4444" stroke="#f1df76" stroke-width="1.8"/>"""),

    ("secc_classification", "SECC MATRIX", "#f59e0b", "#78350f", "#241402",
     """<polygon points="50,18 84,38 84,76 50,94 16,76 16,38" fill="#451a03" stroke="#f59e0b" stroke-width="2"/>
        <circle cx="50" cy="55" r="14" fill="#78350f" stroke="#fff" stroke-width="1.5"/>
        <text x="50" y="60" fill="#fff" font-family="Impact" font-size="12" text-anchor="middle">SECC</text>"""),

    ("ordeals_framework", "ORDEALS SYSTEM", "#ef4444", "#7f1d1d", "#240408",
     """<polygon points="50,18 88,82 12,82" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
        <circle cx="50" cy="56" r="12" fill="#7f1d1d" stroke="#f1df76" stroke-width="1.8"/>
        <polygon points="50,48 56,56 50,64 44,56" fill="#fff"/>"""),

    ("maw_equipment_system", "M.A.W. SYSTEM", "#f59e0b", "#78350f", "#241402",
     """<line x1="28" y1="72" x2="72" y2="28" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
        <polygon points="64,22 78,36 70,44 56,30" fill="#f1df76"/>
        <circle cx="44" cy="56" r="10" fill="#090d16" stroke="#38bdf8" stroke-width="2"/>"""),

    ("agent_stats", "OPERATIVE STATS", "#38bdf8", "#0c4a6e", "#041424",
     """<polygon points="50,22 76,38 76,68 50,84 24,68 24,38" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
        <polygon points="50,32 66,44 66,62 50,72 34,62 34,44" fill="#0c4a6e" stroke="#f1df76" stroke-width="1.5"/>"""),

    ("enemy_bestiary", "ENEMY BESTIARY", "#dc2626", "#450a0a", "#200204",
     """<circle cx="50" cy="50" r="28" fill="#450a0a" stroke="#dc2626" stroke-width="2"/>
        <polygon points="36,40 44,52 36,64" fill="#fff"/>
        <polygon points="64,40 56,52 64,64" fill="#fff"/>
        <ellipse cx="50" cy="52" rx="8" ry="12" fill="#ef4444"/>"""),

    ("han_relic_registry", "RELIC REGISTRY", "#d97706", "#78350f", "#241202",
     """<rect x="30" y="26" width="40" height="48" rx="4" fill="#451a03" stroke="#d97706" stroke-width="2"/>
        <circle cx="50" cy="46" r="10" fill="#f1df76" stroke="#fff" stroke-width="1.5"/>
        <line x1="38" y1="64" x2="62" y2="64" stroke="#f1df76" stroke-width="2"/>"""),

    ("standard_equipment", "STANDARD GEAR", "#64748b", "#1e293b", "#080c14",
     """<polygon points="50,24 74,38 68,76 32,76 26,38" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
        <circle cx="50" cy="50" r="10" fill="#334155" stroke="#f1df76" stroke-width="1.5"/>"""),

    ("taboo_resonance_mech", "TABOO DOCTRINE", "#a855f7", "#3b0764", "#160424",
     """<polygon points="50,18 82,44 72,82 28,82 18,44" fill="#2e1065" stroke="#a855f7" stroke-width="2"/>
        <line x1="32" y1="34" x2="68" y2="66" stroke="#ef4444" stroke-width="2.5"/>
        <line x1="68" y1="34" x2="32" y2="66" stroke="#ef4444" stroke-width="2.5"/>""")
]

for tag, name, col, dark_col, deep_col, inner_gfx in MECHANICS_ITEMS:
    mech_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="{deep_col}" stroke="{col}" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1" stroke-dasharray="4 2"/>
  {inner_gfx}
</svg>"""
    save_svg(mech_svg, [f"assets/icons/icon_mech_{tag}.svg"])

print("Bespoke mechanics tactical icons generated!")

# ==============================================================================
# 5. BESPOKE DEPARTMENT EXTRA ICONS & FACTION TECH (100x100 Inset)
# ==============================================================================

# Department Room Types
ROOM_TYPES_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#08101a" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1" stroke-dasharray="4 2"/>
  <!-- Blueprint Rooms Grid -->
  <rect x="22" y="22" width="24" height="24" rx="2" fill="#0c2338" stroke="#38bdf8" stroke-width="1.8"/>
  <rect x="54" y="22" width="24" height="24" rx="2" fill="#0c2338" stroke="#38bdf8" stroke-width="1.8"/>
  <rect x="22" y="54" width="24" height="24" rx="2" fill="#0c2338" stroke="#38bdf8" stroke-width="1.8"/>
  <rect x="54" y="54" width="24" height="24" rx="2" fill="#180a14" stroke="#ef4444" stroke-width="1.8"/>
  <line x1="46" y1="34" x2="54" y2="34" stroke="#f1df76" stroke-width="2"/>
  <line x1="34" y1="46" x2="34" y2="54" stroke="#f1df76" stroke-width="2"/>
</svg>"""

# Department Incident Reports Archive
INCIDENTS_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#180406" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(239, 68, 68, 0.2)" stroke-width="1" stroke-dasharray="4 2"/>
  <polygon points="50,18 84,78 16,78" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
  <text x="50" y="68" fill="#fff" font-family="Impact" font-size="28" text-anchor="middle">!</text>
</svg>"""

# Faction Technology
FACTION_TECH_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#12061c" stroke="#a855f7" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(168, 85, 247, 0.2)" stroke-width="1" stroke-dasharray="4 2"/>
  <circle cx="50" cy="50" r="26" fill="#2e1065" stroke="#a855f7" stroke-width="2"/>
  <polygon points="50,30 68,50 50,70 32,50" fill="#3b0764" stroke="#f1df76" stroke-width="1.8"/>
  <circle cx="50" cy="50" r="5" fill="#38bdf8"/>
</svg>"""

save_svg(ROOM_TYPES_SVG, [
    "assets/icons/icon_dept_room_types.svg",
    "assets/layout/hand/icons/icon_dept_room_types.svg"
])
save_svg(INCIDENTS_SVG, [
    "assets/icons/icon_dept_incident_archive.svg",
    "assets/layout/hand/icons/icon_dept_incident_archive.svg"
])
save_svg(FACTION_TECH_SVG, [
    "assets/icons/icon_faction_technology.svg"
])

print("All bespoke hub icons generated successfully!")
