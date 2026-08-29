#!/usr/bin/env python3
"""
tools/build_all_system_and_category_svgs.py
Generates all Damage types, Work types, Risk Tiers, HUD Widgets,
Category Banners, Somnarak City icons, and Reference SVGs
with proper 3-6px insets, non-clipping geometry, and 5 canonical Somnarak colors.
"""

import os

WIKI_DIR = "/home/user/01_Somnarak_Wiki"
ASSETS_ICONS = os.path.join(WIKI_DIR, "assets/icons")
CITY_ICONS = os.path.join(WIKI_DIR, "assets/layout/city/icons")
ICONS_DIR = "/home/user/icons"

for d in [ASSETS_ICONS, CITY_ICONS, ICONS_DIR]:
    os.makedirs(d, exist_ok=True)

def save_svg(content, relative_paths):
    for rel in relative_paths:
        full_path = os.path.join(WIKI_DIR, rel) if not rel.startswith("/") else rel
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        # Also copy to root /home/user/icons if it's an icon
        if "icons/" in rel:
            fname = os.path.basename(rel)
            root_icon_path = os.path.join(ICONS_DIR, fname)
            with open(root_icon_path, "w", encoding="utf-8") as f:
                f.write(content.strip() + "\n")

# ==============================================================================
# 1. DAMAGE TYPES (Inset & 5 Canonical Colors)
# ==============================================================================

# Physical (Red)
DAMAGE_RED = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#2d0505" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(239, 68, 68, 0.2)" stroke-width="1"/>
  <polygon points="50,18 78,42 66,78 34,78 22,42" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
  <path d="M 50,26 L 68,44 L 58,70 L 42,70 L 32,44 Z" fill="#991b1b"/>
  <circle cx="50" cy="50" r="7" fill="#fff" stroke="#ef4444" stroke-width="1.5"/>
</svg>"""

# Mental (White / Pale)
DAMAGE_WHITE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#0f172a" stroke="#f8fafc" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(248, 250, 252, 0.2)" stroke-width="1"/>
  <circle cx="50" cy="50" r="28" fill="#1e293b" stroke="#f8fafc" stroke-width="2"/>
  <polygon points="50,26 66,42 50,58 34,42" fill="#f8fafc"/>
  <polygon points="50,42 66,58 50,74 34,58" fill="#cbd5e1"/>
</svg>"""

# Corrosive / Agony (Black / Dark Violet)
DAMAGE_BLACK = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#050508" stroke="#a855f7" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(168, 85, 247, 0.2)" stroke-width="1"/>
  <path d="M 50,20 C 70,20 80,40 76,64 C 72,82 50,86 50,86 C 50,86 28,82 24,64 C 20,40 30,20 50,20 Z" fill="#2e1065" stroke="#a855f7" stroke-width="2"/>
  <circle cx="42" cy="48" r="4" fill="#a855f7"/>
  <circle cx="58" cy="48" r="4" fill="#a855f7"/>
  <circle cx="50" cy="66" r="3" fill="#f1df76"/>
</svg>"""

# Pale / Existential (Cyan / Pure Han)
DAMAGE_PALE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#041824" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1"/>
  <polygon points="50,18 78,50 50,82 22,50" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="50,28 66,50 50,72 34,50" fill="#0284c7" stroke="#7dd3fc" stroke-width="1.5"/>
  <circle cx="50" cy="50" r="5" fill="#f1df76"/>
</svg>"""

save_svg(DAMAGE_RED, ["assets/icons/icon_damage_physical_red.svg", "assets/icons/damage_red.svg"])
save_svg(DAMAGE_WHITE, ["assets/icons/icon_damage_mental_white.svg", "assets/icons/damage_white.svg"])
save_svg(DAMAGE_BLACK, ["assets/icons/icon_damage_corrosive_black.svg", "assets/icons/damage_black.svg"])
save_svg(DAMAGE_PALE, ["assets/icons/icon_damage_pale_cyan.svg", "assets/icons/damage_pale.svg"])

# ==============================================================================
# 2. WORK TYPES (Instinct, Insight, Attachment, Repression, Extraction)
# ==============================================================================

WORK_INSTINCT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#2d0505" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(239, 68, 68, 0.2)" stroke-width="1"/>
  <polygon points="50,20 78,44 68,78 32,78 22,44" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
  <path d="M 38,54 L 50,34 L 62,54 Z" fill="#fecaca"/>
</svg>"""

WORK_INSIGHT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#0f172a" stroke="#f8fafc" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(248, 250, 252, 0.2)" stroke-width="1"/>
  <circle cx="50" cy="50" r="26" fill="#1e293b" stroke="#f8fafc" stroke-width="2"/>
  <circle cx="50" cy="50" r="12" fill="#0f172a" stroke="#f1df76" stroke-width="1.8"/>
  <circle cx="50" cy="50" r="5" fill="#f8fafc"/>
</svg>"""

WORK_ATTACHMENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#050508" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(241, 223, 118, 0.2)" stroke-width="1"/>
  <path d="M 50,32 C 40,18 20,28 26,48 C 32,68 50,82 50,82 C 50,82 68,68 74,48 C 80,28 60,18 50,32 Z" fill="#78350f" stroke="#f1df76" stroke-width="2"/>
  <circle cx="50" cy="48" r="6" fill="#fff"/>
</svg>"""

WORK_REPRESSION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#041824" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1"/>
  <rect x="28" y="28" width="44" height="44" rx="4" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
  <line x1="28" y1="28" x2="72" y2="72" stroke="#ef4444" stroke-width="2.5"/>
  <line x1="72" y1="28" x2="28" y2="72" stroke="#ef4444" stroke-width="2.5"/>
</svg>"""

WORK_EXTRACTION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#1e1b04" stroke="#eab308" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(234, 179, 8, 0.2)" stroke-width="1"/>
  <polygon points="50,20 76,46 50,78 24,46" fill="#713f12" stroke="#eab308" stroke-width="2"/>
  <line x1="50" y1="20" x2="50" y2="78" stroke="#38bdf8" stroke-width="2"/>
</svg>"""

save_svg(WORK_INSTINCT, ["assets/icons/icon_work_instinct_red.svg", "assets/icons/work_instinct.svg", "assets/icons/wt_pugnahan.svg", "assets/icons/pugnahan.svg"])
save_svg(WORK_INSIGHT, ["assets/icons/icon_work_insight_white.svg", "assets/icons/work_insight.svg", "assets/icons/wt_viderehan.svg", "assets/icons/viderehan.svg"])
save_svg(WORK_ATTACHMENT, ["assets/icons/icon_work_attachment_black.svg", "assets/icons/work_attachment.svg", "assets/icons/wt_ferrehan.svg", "assets/icons/ferrehan.svg"])
save_svg(WORK_REPRESSION, ["assets/icons/icon_work_repression_cyan.svg", "assets/icons/work_repression.svg", "assets/icons/wt_flerehan.svg", "assets/icons/flerehan.svg"])
save_svg(WORK_EXTRACTION, ["assets/icons/icon_work_extraction.svg", "assets/icons/work_extraction.svg"])

# ==============================================================================
# 3. RISK TIERS (Can / Zayin, Teth, He, Waw, Aleph)
# ==============================================================================

RISKS = [
    ("t01_can", "CAN", "ZAYIN", "#10b981", "#064e3b", "#022c22", "assets/icons/risk_zayin.svg"),
    ("t02_teth", "TETH", "TETH", "#0284c7", "#0c4a6e", "#082f49", "assets/icons/risk_teth.svg"),
    ("t03_he", "HE", "HE", "#f59e0b", "#78350f", "#451a03", "assets/icons/risk_he.svg"),
    ("t04_waw", "WAW", "WAW", "#8b5cf6", "#3b0764", "#2e1065", "assets/icons/risk_waw.svg"),
    ("t05_aleph", "ALEPH", "ALEPH", "#ef4444", "#7f1d1d", "#450a0a", "assets/icons/risk_aleph.svg")
]

for tag, label, alt, col, dark_col, deep_col, extra_rel in RISKS:
    risk_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <polygon points="50,4 94,26 94,74 50,96 6,74 6,26" fill="{deep_col}" stroke="{col}" stroke-width="2.5"/>
  <polygon points="50,10 88,29 88,71 50,90 12,71 12,29" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1"/>
  <circle cx="50" cy="50" r="26" fill="{dark_col}" stroke="{col}" stroke-width="1.8"/>
  <text x="50" y="56" fill="#fff" font-family="Impact, Arial, sans-serif" font-size="14" letter-spacing="1" text-anchor="middle">{label}</text>
</svg>"""
    save_svg(risk_svg, [f"assets/icons/icon_risk_{tag}.svg", extra_rel])

# ==============================================================================
# 4. HUD WIDGETS (Facility Radar, Resonance Wave, Han Gauge, Containment Lock)
# ==============================================================================

HUD_RADAR = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 140" width="100%" height="100%">
  <rect x="4" y="4" width="132" height="132" rx="12" fill="#05080e" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="70" cy="70" r="54" fill="none" stroke="#1e293b" stroke-width="1.5"/>
  <circle cx="70" cy="70" r="38" fill="none" stroke="#334155" stroke-width="1"/>
  <circle cx="70" cy="70" r="20" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="70" y1="12" x2="70" y2="128" stroke="#1e293b" stroke-width="1"/>
  <line x1="12" y1="70" x2="128" y2="70" stroke="#1e293b" stroke-width="1"/>
  <line x1="70" y1="70" x2="108" y2="36" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="108" cy="36" r="4" fill="#ef4444"/>
  <circle cx="52" cy="84" r="3" fill="#f1df76"/>
  <circle cx="70" cy="70" r="3" fill="#38bdf8"/>
</svg>"""

HUD_RESONANCE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 40" width="100%" height="100%">
  <rect x="2" y="2" width="136" height="36" rx="4" fill="#060a12" stroke="#ef4444" stroke-width="1.5"/>
  <path d="M 6,20 Q 20,4 34,20 T 62,20 T 90,20 T 118,20 T 134,20" fill="none" stroke="#ef4444" stroke-width="2"/>
  <path d="M 6,20 Q 20,28 34,20 T 62,20 T 90,20 T 118,20 T 134,20" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="2 2"/>
</svg>"""

HUD_HAN_GAUGE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 50" width="100%" height="100%">
  <rect x="2" y="2" width="136" height="46" rx="6" fill="#070c14" stroke="#f1df76" stroke-width="1.8"/>
  <rect x="10" y="16" width="120" height="18" rx="3" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <rect x="12" y="18" width="92" height="14" rx="2" fill="linear-gradient(90deg, #38bdf8, #f1df76)"/>
  <line x1="104" y1="12" x2="104" y2="38" stroke="#ef4444" stroke-width="2.5"/>
</svg>"""

HUD_LOCK = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#1a0608" stroke="#ef4444" stroke-width="2.5"/>
  <circle cx="50" cy="50" r="30" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
  <rect x="36" y="44" width="28" height="22" rx="3" fill="#7f1d1d" stroke="#fecaca" stroke-width="1.5"/>
  <path d="M 42,44 L 42,36 A 8,8 0 0,1 58,36 L 58,44" fill="none" stroke="#fff" stroke-width="2.5"/>
  <circle cx="50" cy="54" r="3" fill="#fff"/>
</svg>"""

save_svg(HUD_RADAR, ["assets/icons/hud_facility_radar.svg"])
save_svg(HUD_RESONANCE, ["assets/icons/hud_resonance_wave.svg"])
save_svg(HUD_HAN_GAUGE, ["assets/icons/hud_han_gauge.svg"])
save_svg(HUD_LOCK, ["assets/icons/hud_containment_lock.svg"])

# ==============================================================================
# 5. SOMNARAK CITY & ZONE ICONS
# ==============================================================================

CITY_MAIN_ICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="16,4 104,4 116,16 116,104 104,116 16,116 4,104 4,16" fill="#090514" stroke="#a855f7" stroke-width="2.5"/>
  <polygon points="19,10 101,10 110,19 110,101 101,110 19,110 10,101 10,19" fill="none" stroke="rgba(241, 223, 118, 0.35)" stroke-width="1" stroke-dasharray="4 2"/>
  
  <!-- Alpha Tree Spire & Radiant Canopy -->
  <circle cx="60" cy="42" r="22" fill="#2e1065" stroke="#f1df76" stroke-width="2"/>
  <path d="M 60,20 L 74,44 L 46,44 Z" fill="#3b0764" stroke="#38bdf8" stroke-width="1.5"/>
  <circle cx="60" cy="42" r="6" fill="#f1df76"/>

  <!-- 5 Concentric Ring Spines -->
  <circle cx="60" cy="62" r="42" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6 3"/>
  <circle cx="60" cy="62" r="30" fill="none" stroke="#a855f7" stroke-width="1.2"/>
  
  <!-- City Wall Bastions -->
  <rect x="22" y="74" width="14" height="18" rx="2" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="84" y="74" width="14" height="18" rx="2" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="22" y1="92" x2="98" y2="92" stroke="#f1df76" stroke-width="2"/>
</svg>"""

save_svg(CITY_MAIN_ICON, [
    "assets/layout/city/icons/somnarak_city_icon.svg",
    "assets/layout/city/icons/somnarak_city_icon_styled.svg",
    "assets/layout/city/icons/icon_somnarak_city_badge.svg",
    "assets/icons/somnarak_city_icon.svg",
    "assets/icons/city.svg"
])

ZONES = [
    ("a_core", "ZONE A", "ALPHA CORE", "#f1df76", "#78350f", "#451a03"),
    ("b_west", "ZONE B", "WEST METROPOLIS", "#38bdf8", "#0c4a6e", "#082f49"),
    ("c_east", "ZONE C", "EAST INDUSTRIAL", "#ef4444", "#7f1d1d", "#450a0a"),
    ("d_flanks", "ZONE D", "COMMERCE FLANKS", "#10b981", "#064e3b", "#022c22"),
    ("e_bulwark", "ZONE E", "OUTER BULWARK", "#a855f7", "#3b0764", "#2e1065")
]

for tag, label, subtitle, col, dark_col, deep_col in ZONES:
    z_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <polygon points="50,4 94,26 94,74 50,96 6,74 6,26" fill="{deep_col}" stroke="{col}" stroke-width="2.5"/>
  <polygon points="50,10 88,29 88,71 50,90 12,71 12,29" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1"/>
  <circle cx="50" cy="50" r="24" fill="{dark_col}" stroke="{col}" stroke-width="1.8"/>
  <text x="50" y="55" fill="#fff" font-family="Impact, Arial, sans-serif" font-size="11" letter-spacing="1" text-anchor="middle">{label}</text>
</svg>"""
    save_svg(z_svg, [
        f"assets/layout/city/icons/icon_zone_{tag}.svg",
        f"assets/icons/icon_zone_{tag}.svg"
    ])

print("System, city, damage, work, and risk SVGs generated!")
