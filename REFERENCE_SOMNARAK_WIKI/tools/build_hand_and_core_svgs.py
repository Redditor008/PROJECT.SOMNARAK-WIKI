#!/usr/bin/env python3
"""
tools/build_hand_and_core_svgs.py
Generates the upgraded Hand of Change suite (including new simple icons)
and all department, faction, and character core SVGs with proper insets
and 5 canonical Somnarak colors (Gold, Cyan, Crimson, Black/Dark, White/Pale).
"""

import os

WIKI_DIR = "/home/user/01_Somnarak_Wiki"
HAND_ICONS_DIR = os.path.join(WIKI_DIR, "assets/layout/hand/icons")
ASSETS_ICONS_DIR = os.path.join(WIKI_DIR, "assets/icons")
ICONS_DIR = "/home/user/icons"
AVATARS_DIR = os.path.join(WIKI_DIR, "assets/avatars")

for d in [HAND_ICONS_DIR, ASSETS_ICONS_DIR, ICONS_DIR, AVATARS_DIR]:
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
# 1. THE HAND OF CHANGE - BRAND NEW SIMPLE ICONS
# ==============================================================================

# New Ultra-Clean The Hand of Change Simple Icon (Square Tactical Outline)
HAND_SIMPLE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="handSimpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#030712"/>
    </linearGradient>
    <filter id="handSimpleGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  
  <!-- Outer Tactical Chamfered Frame (Inset with 4px margin so it never touches border) -->
  <polygon points="16,4 104,4 116,16 116,104 104,116 16,116 4,104 4,16" fill="url(#handSimpleGrad)" stroke="#f1df76" stroke-width="2.5"/>
  <polygon points="19,10 101,10 110,19 110,101 101,110 19,110 10,101 10,19" fill="none" stroke="rgba(56, 189, 248, 0.35)" stroke-width="1" stroke-dasharray="4 2"/>

  <!-- Alpha Tree Spire (Top 0m Surface Root Entrance) -->
  <path d="M 52,14 L 68,14 L 64,24 L 56,24 Z" fill="#38bdf8" stroke="#f1df76" stroke-width="1.2"/>
  <line x1="60" y1="24" x2="60" y2="34" stroke="#38bdf8" stroke-width="2.5" filter="url(#handSimpleGlow)"/>

  <!-- The Palm Core (F1 Neutral Command, F2 Maw's Keep, F3 Extraction Hall) -->
  <path d="M 34,34 L 86,34 L 92,54 L 84,68 L 36,68 L 28,54 Z" fill="#1e293b" stroke="#f1df76" stroke-width="2"/>
  <circle cx="60" cy="51" r="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.8"/>
  <polygon points="60,45 66,51 60,57 54,51" fill="#f1df76"/>

  <!-- Subterranean Transit Core Elevator Spine -->
  <line x1="60" y1="68" x2="60" y2="76" stroke="#38bdf8" stroke-width="3"/>
  <line x1="22" y1="76" x2="98" y2="76" stroke="#38bdf8" stroke-width="2"/>

  <!-- The Four Plunging Finger Vaults (F4 Insight Forge, F5 Border Watch, F6 Deep Vault, F7 Shadow Corps) -->
  <!-- Finger 1 (F4 - West) -->
  <rect x="20" y="79" width="16" height="26" rx="3" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
  <line x1="28" y1="84" x2="28" y2="100" stroke="#a7f3d0" stroke-width="1"/>

  <!-- Finger 2 (F5 - Central West) -->
  <rect x="42" y="79" width="16" height="30" rx="3" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="50" y1="84" x2="50" y2="104" stroke="#bae6fd" stroke-width="1"/>

  <!-- Finger 3 (F6 - Central East) -->
  <rect x="62" y="79" width="16" height="30" rx="3" fill="#3b0764" stroke="#a855f7" stroke-width="1.5"/>
  <line x1="70" y1="84" x2="70" y2="104" stroke="#e9d5ff" stroke-width="1"/>

  <!-- Finger 4 (F7 - Deep East) -->
  <rect x="84" y="79" width="16" height="26" rx="3" fill="#4c0519" stroke="#ef4444" stroke-width="1.5"/>
  <line x1="92" y1="84" x2="92" y2="100" stroke="#fecaca" stroke-width="1"/>

  <!-- Lateral F8 Gate Watch Outpost -->
  <rect x="94" y="44" width="14" height="14" rx="2" fill="#1e293b" stroke="#94a3b8" stroke-width="1.2"/>
  <line x1="86" y1="51" x2="94" y2="51" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="2 1"/>
</svg>"""

# New Radiant Gold Command Variant
HAND_GOLD_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="handGoldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1808"/>
      <stop offset="100%" stop-color="#070603"/>
    </linearGradient>
    <filter id="handGoldGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="16,4 104,4 116,16 116,104 104,116 16,116 4,104 4,16" fill="url(#handGoldGrad)" stroke="#f1df76" stroke-width="2.5"/>
  <polygon points="20,10 100,10 110,20 110,100 100,110 20,110 10,100 10,20" fill="none" stroke="rgba(241, 223, 118, 0.4)" stroke-width="1" stroke-dasharray="4 2"/>
  <path d="M 52,14 L 68,14 L 64,24 L 56,24 Z" fill="#f1df76" stroke="#fbbf24" stroke-width="1.2"/>
  <line x1="60" y1="24" x2="60" y2="34" stroke="#f1df76" stroke-width="2.5" filter="url(#handGoldGlow)"/>
  <path d="M 34,34 L 86,34 L 92,54 L 84,68 L 36,68 L 28,54 Z" fill="#2d2208" stroke="#f1df76" stroke-width="2"/>
  <circle cx="60" cy="51" r="10" fill="#140f04" stroke="#f1df76" stroke-width="2"/>
  <polygon points="60,44 67,51 60,58 53,51" fill="#f1df76" filter="url(#handGoldGlow)"/>
  <line x1="60" y1="68" x2="60" y2="76" stroke="#f1df76" stroke-width="3"/>
  <line x1="22" y1="76" x2="98" y2="76" stroke="#f1df76" stroke-width="2"/>
  <rect x="20" y="79" width="16" height="26" rx="3" fill="#281f07" stroke="#f1df76" stroke-width="1.5"/>
  <rect x="42" y="79" width="16" height="30" rx="3" fill="#382d09" stroke="#f1df76" stroke-width="1.5"/>
  <rect x="62" y="79" width="16" height="30" rx="3" fill="#382d09" stroke="#f1df76" stroke-width="1.5"/>
  <rect x="84" y="79" width="16" height="26" rx="3" fill="#281f07" stroke="#f1df76" stroke-width="1.5"/>
</svg>"""

# New Radiant Cyan Electric Technical Variant
HAND_CYAN_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="handCyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#081826"/>
      <stop offset="100%" stop-color="#02080f"/>
    </linearGradient>
    <filter id="handCyanGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <polygon points="16,4 104,4 116,16 116,104 104,116 16,116 4,104 4,16" fill="url(#handCyanGrad)" stroke="#38bdf8" stroke-width="2.5"/>
  <polygon points="20,10 100,10 110,20 110,100 100,110 20,110 10,100 10,20" fill="none" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1" stroke-dasharray="4 2"/>
  <path d="M 52,14 L 68,14 L 64,24 L 56,24 Z" fill="#38bdf8" stroke="#7dd3fc" stroke-width="1.2"/>
  <line x1="60" y1="24" x2="60" y2="34" stroke="#38bdf8" stroke-width="2.5" filter="url(#handCyanGlow)"/>
  <path d="M 34,34 L 86,34 L 92,54 L 84,68 L 36,68 L 28,54 Z" fill="#0c2338" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="60" cy="51" r="10" fill="#04121d" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="60,44 67,51 60,58 53,51" fill="#38bdf8" filter="url(#handCyanGlow)"/>
  <line x1="60" y1="68" x2="60" y2="76" stroke="#38bdf8" stroke-width="3"/>
  <line x1="22" y1="76" x2="98" y2="76" stroke="#38bdf8" stroke-width="2"/>
  <rect x="20" y="79" width="16" height="26" rx="3" fill="#092033" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="42" y="79" width="16" height="30" rx="3" fill="#0f304d" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="62" y="79" width="16" height="30" rx="3" fill="#0f304d" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="84" y="79" width="16" height="26" rx="3" fill="#092033" stroke="#38bdf8" stroke-width="1.5"/>
</svg>"""

# High-Detail Tactical Schematics Facility Icon (Upgraded styled replacement)
HAND_STYLED_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="handCoreGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#f1df76" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="handBgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c121d"/>
      <stop offset="50%" stop-color="#060910"/>
      <stop offset="100%" stop-color="#020406"/>
    </linearGradient>
    <filter id="glowFilt" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Inset Border with 4px margin so no stroke is cut off -->
  <rect x="4" y="4" width="112" height="112" rx="14" fill="url(#handBgGrad)" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="10" fill="none" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1" stroke-dasharray="3 3"/>

  <!-- Radial Background Flare -->
  <circle cx="60" cy="54" r="44" fill="url(#handCoreGlow)"/>

  <!-- Alpha Tree Spire & Surface Interface -->
  <polygon points="53,12 67,12 64,22 56,22" fill="#475569" stroke="#94a3b8" stroke-width="1.2"/>
  <line x1="60" y1="22" x2="60" y2="32" stroke="#38bdf8" stroke-width="2.5" filter="url(#glowFilt)"/>

  <!-- Palm Chamber Complex (F1, F2, F3) -->
  <!-- Floor 1 Neutral Command -->
  <rect x="36" y="32" width="48" height="12" rx="2" fill="#78350f" stroke="#f1df76" stroke-width="1.5"/>
  <text x="60" y="41" fill="#fff" font-family="Arial, sans-serif" font-size="7" font-weight="bold" text-anchor="middle">F1 PALM</text>

  <!-- Floor 2 Maw's Keep -->
  <rect x="34" y="46" width="52" height="12" rx="2" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.5"/>
  <text x="60" y="55" fill="#fecaca" font-family="Arial, sans-serif" font-size="7" font-weight="bold" text-anchor="middle">F2 MAW</text>

  <!-- Floor 3 Extraction Hall -->
  <rect x="38" y="60" width="44" height="11" rx="2" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="68.5" fill="#bae6fd" font-family="Arial, sans-serif" font-size="6.5" font-weight="bold" text-anchor="middle">F3 EXT</text>

  <!-- Distribution Bus Line -->
  <line x1="60" y1="71" x2="60" y2="78" stroke="#38bdf8" stroke-width="2.5"/>
  <line x1="18" y1="78" x2="102" y2="78" stroke="#38bdf8" stroke-width="2"/>

  <!-- The 4 Vertical Finger Drops -->
  <!-- F4 Insight Forge -->
  <rect x="16" y="80" width="18" height="26" rx="2" fill="#064e3b" stroke="#10b981" stroke-width="1.2"/>
  <text x="25" y="96" fill="#a7f3d0" font-family="Arial, sans-serif" font-size="6" font-weight="bold" text-anchor="middle">F4</text>

  <!-- F5 Border Watch -->
  <rect x="38" y="80" width="18" height="30" rx="2" fill="#0c4a6e" stroke="#0284c7" stroke-width="1.2"/>
  <text x="47" y="97" fill="#bae6fd" font-family="Arial, sans-serif" font-size="6" font-weight="bold" text-anchor="middle">F5</text>

  <!-- F6 Deep Vault -->
  <rect x="64" y="80" width="18" height="30" rx="2" fill="#3b0764" stroke="#8b5cf6" stroke-width="1.2"/>
  <text x="73" y="97" fill="#e9d5ff" font-family="Arial, sans-serif" font-size="6" font-weight="bold" text-anchor="middle">F6</text>

  <!-- F7 Shadow Corps -->
  <rect x="86" y="80" width="18" height="26" rx="2" fill="#4c0519" stroke="#e11d48" stroke-width="1.2"/>
  <text x="95" y="96" fill="#fecaca" font-family="Arial, sans-serif" font-size="6" font-weight="bold" text-anchor="middle">F7</text>

  <!-- Lateral F8 Gate Watch Outpost -->
  <rect x="92" y="44" width="18" height="12" rx="2" fill="#1e293b" stroke="#94a3b8" stroke-width="1.2"/>
  <text x="101" y="52.5" fill="#f1f5f9" font-family="Arial, sans-serif" font-size="5.5" font-weight="bold" text-anchor="middle">F8</text>
  <line x1="86" y1="50" x2="92" y2="50" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2 1"/>
</svg>"""

# Minimal Reverie Directorate Crest (Properly Inset)
DIRECTORATE_MINIMAL_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <filter id="dirMinGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <!-- Inset frame with 3px safe border -->
  <rect x="3" y="3" width="94" height="94" rx="12" fill="#060910" stroke="#38bdf8" stroke-width="2"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(241, 223, 118, 0.3)" stroke-width="1"/>
  
  <circle cx="50" cy="50" r="30" fill="#0b1320" stroke="#f1df76" stroke-width="2"/>
  <polygon points="50,22 74,68 26,68" fill="#1e293b" stroke="#38bdf8" stroke-width="1.8"/>
  <circle cx="50" cy="52" r="8" fill="#ef4444" stroke="#f1df76" stroke-width="1.5" filter="url(#dirMinGlow)"/>
  
  <!-- 4 Radiating Finger Nodes -->
  <line x1="50" y1="68" x2="32" y2="84" stroke="#f1df76" stroke-width="1.5"/>
  <line x1="50" y1="68" x2="44" y2="86" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="50" y1="68" x2="56" y2="86" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="50" y1="68" x2="68" y2="84" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="32" cy="84" r="2.5" fill="#10b981"/>
  <circle cx="44" cy="86" r="2.5" fill="#38bdf8"/>
  <circle cx="56" cy="86" r="2.5" fill="#8b5cf6"/>
  <circle cx="68" cy="84" r="2.5" fill="#ef4444"/>
</svg>"""

# Directorate Insignia Badge (Full Official Insignia)
DIRECTORATE_BADGE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="100%" height="100%">
  <defs>
    <radialGradient id="badgeGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="70%" stop-color="#0b1322"/>
      <stop offset="100%" stop-color="#030712"/>
    </radialGradient>
    <filter id="badgeGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Inset Double Ring with 4px breathing room -->
  <circle cx="80" cy="80" r="74" fill="url(#badgeGrad)" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="80" cy="80" r="68" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6 3"/>

  <!-- Tactical Hazard Notches -->
  <path d="M 80,8 L 80,16 M 80,144 L 80,152 M 8,80 L 16,80 M 144,80 L 152,80" stroke="#ef4444" stroke-width="3"/>

  <!-- Central Crest: The Hand of Change Core -->
  <polygon points="80,24 126,50 126,110 80,136 34,110 34,50" fill="#0d1829" stroke="#f1df76" stroke-width="2"/>
  <polygon points="80,32 118,54 118,106 80,128 42,106 42,54" fill="#060c16" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1"/>

  <!-- The Alpha Tree Root Spire -->
  <polygon points="74,36 86,36 83,46 77,46" fill="#38bdf8" stroke="#f1df76" stroke-width="1"/>
  <line x1="80" y1="46" x2="80" y2="56" stroke="#38bdf8" stroke-width="2"/>

  <!-- The Palm Core -->
  <path d="M 56,56 L 104,56 L 108,76 L 100,88 L 60,88 L 52,76 Z" fill="#1e293b" stroke="#f1df76" stroke-width="1.8"/>
  <circle cx="80" cy="72" r="9" fill="#ef4444" stroke="#f1df76" stroke-width="1.5" filter="url(#badgeGlow)"/>
  <polygon points="80,67 85,72 80,77 75,72" fill="#fff"/>

  <!-- 4 Finger Pillars -->
  <line x1="80" y1="88" x2="80" y2="94" stroke="#38bdf8" stroke-width="2"/>
  <line x1="48" y1="94" x2="112" y2="94" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="46" y="96" width="12" height="18" rx="2" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
  <rect x="62" y="96" width="12" height="22" rx="2" fill="#0c4a6e" stroke="#0284c7" stroke-width="1"/>
  <rect x="86" y="96" width="12" height="22" rx="2" fill="#3b0764" stroke="#8b5cf6" stroke-width="1"/>
  <rect x="102" y="96" width="12" height="18" rx="2" fill="#4c0519" stroke="#e11d48" stroke-width="1"/>
</svg>"""

save_svg(HAND_SIMPLE_SVG, [
    "assets/layout/hand/icons/the_hand_of_change_simple.svg",
    "assets/layout/hand/icons/icon_hand_of_change_simple.svg",
    "assets/icons/the_hand_of_change_simple.svg",
    "assets/icons/icon_hand_of_change_simple.svg",
    "assets/icons/the_hand_dr_simple_icon.svg"
])

save_svg(HAND_GOLD_SVG, [
    "assets/layout/hand/icons/icon_hand_of_change_gold.svg",
    "assets/icons/icon_hand_of_change_gold.svg"
])

save_svg(HAND_CYAN_SVG, [
    "assets/layout/hand/icons/icon_hand_of_change_cyan.svg",
    "assets/icons/icon_hand_of_change_cyan.svg",
    "assets/layout/hand/icons/the_hand_of_change_blueprint_icon.svg",
    "assets/icons/the_hand_of_change_blueprint_icon.svg"
])

save_svg(HAND_STYLED_SVG, [
    "assets/layout/hand/icons/the_hand_dr_icon_styled.svg",
    "assets/icons/the_hand_dr_icon_styled.svg",
    "assets/layout/hand/icons/the_hand_dr_icon.svg",
    "assets/icons/the_hand_dr_icon.svg"
])

save_svg(DIRECTORATE_MINIMAL_SVG, [
    "assets/layout/hand/icons/icon_reverie_directorate_minimal.svg",
    "assets/icons/icon_reverie_directorate_minimal.svg"
])

save_svg(DIRECTORATE_BADGE_SVG, [
    "assets/layout/hand/icons/icon_reverie_directorate_badge.svg",
    "assets/icons/icon_reverie_directorate_badge.svg"
])

print("Hand of Change icons built successfully!")

# ==============================================================================
# 2. ALL 8 DEPARTMENT ICONS & BADGES (Properly Inset & Canonical)
# ==============================================================================

DEPTS = [
    ("f1_neutral", "NEUTRAL COMMAND", "PALM CORE", "#f1df76", "#78350f", "#451a03", "F1",
     """<polygon points="50,22 75,37 75,67 50,82 25,67 25,37" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
        <circle cx="50" cy="52" r="14" fill="#78350f" stroke="#f1df76" stroke-width="1.8"/>
        <polygon points="50,44 57,52 50,60 43,52" fill="#fff"/>
        <line x1="50" y1="22" x2="50" y2="82" stroke="#f1df76" stroke-width="1" stroke-dasharray="2 2"/>"""),
        
    ("f2_maws_keep", "MAW'S KEEP", "CONTAINMENT", "#ef4444", "#7f1d1d", "#450a0a", "F2",
     """<polygon points="50,20 78,35 78,69 50,84 22,69 22,35" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
        <path d="M 36,44 Q 50,34 64,44 Q 50,74 36,44 Z" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.8"/>
        <line x1="36" y1="44" x2="64" y2="44" stroke="#fecaca" stroke-width="1.5"/>
        <polygon points="46,44 48,52 50,44 52,52 54,44" fill="#fff"/>"""),
        
    ("f3_extraction", "EXTRACTION HALL", "REFINING", "#38bdf8", "#1e3a8a", "#172554", "F3",
     """<polygon points="50,20 78,35 78,69 50,84 22,69 22,35" fill="#172554" stroke="#38bdf8" stroke-width="2"/>
        <path d="M 50,32 L 66,66 L 34,66 Z" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.8"/>
        <circle cx="50" cy="54" r="8" fill="#0284c7" stroke="#fff" stroke-width="1.5"/>
        <line x1="50" y1="20" x2="50" y2="84" stroke="#7dd3fc" stroke-width="1" stroke-dasharray="3 2"/>"""),
        
    ("f4_insight_forge", "INSIGHT FORGE", "RESEARCH CORE", "#10b981", "#064e3b", "#022c22", "F4",
     """<polygon points="50,20 78,35 78,69 50,84 22,69 22,35" fill="#022c22" stroke="#10b981" stroke-width="2"/>
        <circle cx="50" cy="52" r="18" fill="#064e3b" stroke="#10b981" stroke-width="1.8"/>
        <circle cx="50" cy="52" r="9" fill="#047857" stroke="#a7f3d0" stroke-width="1.5"/>
        <line x1="50" y1="28" x2="50" y2="76" stroke="#10b981" stroke-width="1.2"/>
        <line x1="26" y1="52" x2="74" y2="52" stroke="#10b981" stroke-width="1.2"/>"""),
        
    ("f5_border_watch", "BORDER WATCH", "PERIMETER DEFENSE", "#0284c7", "#0c4a6e", "#082f49", "F5",
     """<polygon points="50,20 78,35 78,69 50,84 22,69 22,35" fill="#082f49" stroke="#0284c7" stroke-width="2"/>
        <path d="M 50,30 L 70,40 L 70,62 L 50,74 L 30,62 L 30,40 Z" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.8"/>
        <polygon points="50,38 62,45 62,58 50,65 38,58 38,45" fill="#0369a1" stroke="#bae6fd" stroke-width="1.2"/>"""),
        
    ("f6_deep_vault", "DEEP VAULT", "CRYO ARCHIVE", "#8b5cf6", "#3b0764", "#2e1065", "F6",
     """<polygon points="50,20 78,35 78,69 50,84 22,69 22,35" fill="#2e1065" stroke="#8b5cf6" stroke-width="2"/>
        <rect x="36" y="38" width="28" height="28" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="1.8"/>
        <circle cx="50" cy="52" r="6" fill="#7c3aed" stroke="#e9d5ff" stroke-width="1.5"/>
        <line x1="50" y1="20" x2="50" y2="38" stroke="#8b5cf6" stroke-width="1.5"/>
        <line x1="50" y1="66" x2="50" y2="84" stroke="#8b5cf6" stroke-width="1.5"/>"""),
        
    ("f7_shadow_corps", "SHADOW CORPS", "VOID DIVERS", "#e11d48", "#4c0519", "#2d0505", "F7",
     """<polygon points="50,20 78,35 78,69 50,84 22,69 22,35" fill="#2d0505" stroke="#e11d48" stroke-width="2"/>
        <path d="M 34,42 Q 50,26 66,42 Q 74,62 50,76 Q 26,62 34,42 Z" fill="#4c0519" stroke="#f43f5e" stroke-width="1.8"/>
        <circle cx="50" cy="48" r="6" fill="#be123c" stroke="#fecaca" stroke-width="1.5"/>"""),
        
    ("f8_gate_watch", "GATE WATCH", "TABOO GATE", "#94a3b8", "#1e293b", "#0f172a", "F8",
     """<polygon points="50,20 78,35 78,69 50,84 22,69 22,35" fill="#0f172a" stroke="#94a3b8" stroke-width="2"/>
        <path d="M 35,36 L 65,36 L 65,72 L 35,72 Z" fill="#1e293b" stroke="#cbd5e1" stroke-width="1.8"/>
        <line x1="50" y1="36" x2="50" y2="72" stroke="#f1df76" stroke-width="2"/>
        <circle cx="50" cy="54" r="5" fill="#f1df76"/>""")
]

for tag, name, role, primary_col, dark_col, deep_col, code, inner_gfx in DEPTS:
    # Standard Inset Dept Icon (100x100)
    dept_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <radialGradient id="deptGrad_{tag}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{primary_col}" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="{deep_col}" stop-opacity="0"/>
    </radialGradient>
    <filter id="deptGlow_{tag}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <!-- Inset frame with 3px safe border -->
  <rect x="3" y="3" width="94" height="94" rx="12" fill="{deep_col}" stroke="{primary_col}" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1" stroke-dasharray="4 2"/>
  <circle cx="50" cy="52" r="38" fill="url(#deptGrad_{tag})"/>
  {inner_gfx}
  <rect x="8" y="7" width="22" height="12" rx="2" fill="{dark_col}" stroke="{primary_col}" stroke-width="1"/>
  <text x="19" y="15.5" fill="{primary_col}" font-family="Arial, sans-serif" font-size="7.5" font-weight="bold" text-anchor="middle">{code}</text>
</svg>"""

    # Badge Variant (120x120)
    badge_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="{deep_col}" stroke="{primary_col}" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="48" fill="none" stroke="rgba(255, 255, 255, 0.25)" stroke-width="1" stroke-dasharray="4 2"/>
  <g transform="translate(10, 8) scale(1)">
    {inner_gfx}
  </g>
  <rect x="38" y="94" width="44" height="15" rx="3" fill="{dark_col}" stroke="{primary_col}" stroke-width="1.5"/>
  <text x="60" y="104.5" fill="#fff" font-family="Impact, Arial, sans-serif" font-size="8" letter-spacing="1" text-anchor="middle">{code}</text>
</svg>"""

    save_svg(dept_svg, [
        f"assets/layout/hand/icons/icon_dept_{tag}.svg",
        f"assets/icons/icon_dept_{tag}.svg"
    ])
    save_svg(badge_svg, [
        f"assets/layout/hand/icons/icon_dept_{tag}_badge.svg",
        f"assets/icons/icon_dept_{tag}_badge.svg"
    ])

print("Department icons and badges generated!")

# ==============================================================================
# 3. ALL 13 FACTION ICONS (Properly Inset & High Contrast)
# ==============================================================================

FACTIONS = [
    ("reverie_directorate", "THE REVERIE DIRECTORATE", "#f1df76", "#1e293b",
     """<polygon points="50,18 82,36 82,72 50,90 18,72 18,36" fill="#0b1320" stroke="#f1df76" stroke-width="2.5"/>
        <circle cx="50" cy="54" r="16" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <polygon points="50,44 58,54 50,64 42,54" fill="#ef4444"/>"""),
        
    ("high_council", "THE HIGH COUNCIL OF SEVEN", "#fbbf24", "#3b1e08",
     """<polygon points="50,16 84,38 84,76 50,94 16,76 16,38" fill="#1f1004" stroke="#fbbf24" stroke-width="2.5"/>
        <circle cx="50" cy="55" r="22" fill="#3b1e08" stroke="#fbbf24" stroke-width="1.8"/>
        <!-- 7 Radiating Stars -->
        <circle cx="50" cy="38" r="3" fill="#fff"/><circle cx="62" cy="44" r="3" fill="#fff"/><circle cx="65" cy="58" r="3" fill="#fff"/><circle cx="58" cy="70" r="3" fill="#fff"/><circle cx="42" cy="70" r="3" fill="#fff"/><circle cx="35" cy="58" r="3" fill="#fff"/><circle cx="38" cy="44" r="3" fill="#fff"/>
        <circle cx="50" cy="55" r="5" fill="#fbbf24"/>"""),
        
    ("sed_corps", "SED CORPS (SPECIAL EXPEDITION)", "#ef4444", "#3b080d",
     """<polygon points="50,16 84,38 84,76 50,94 16,76 16,38" fill="#200407" stroke="#ef4444" stroke-width="2.5"/>
        <path d="M 50,28 L 74,72 L 50,64 L 26,72 Z" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
        <circle cx="50" cy="52" r="6" fill="#fff" stroke="#ef4444" stroke-width="1.5"/>"""),
        
    ("ucd_strike", "UCD STRIKE FORCE", "#38bdf8", "#082035",
     """<polygon points="50,16 84,38 84,76 50,94 16,76 16,38" fill="#041220" stroke="#38bdf8" stroke-width="2.5"/>
        <path d="M 50,26 L 76,40 L 76,68 L 50,82 L 24,68 L 24,40 Z" fill="#0c2d4a" stroke="#38bdf8" stroke-width="2"/>
        <polygon points="50,36 66,45 66,63 50,72 34,63 34,45" fill="#0369a1" stroke="#fff" stroke-width="1.5"/>"""),
        
    ("architects", "THE ARCHITECTS GUILD", "#a855f7", "#280838",
     """<polygon points="50,16 84,38 84,76 50,94 16,76 16,38" fill="#170420" stroke="#a855f7" stroke-width="2.5"/>
        <rect x="34" y="38" width="32" height="32" rx="3" fill="#3b0764" stroke="#c084fc" stroke-width="2"/>
        <line x1="34" y1="38" x2="66" y2="70" stroke="#f1df76" stroke-width="1.8"/>
        <line x1="66" y1="38" x2="34" y2="70" stroke="#f1df76" stroke-width="1.8"/>"""),
        
    ("weavers", "THE WEAVERS SYNDICATE", "#ec4899", "#350820",
     """<polygon points="50,16 84,38 84,76 50,94 16,76 16,38" fill="#1f0312" stroke="#ec4899" stroke-width="2.5"/>
        <circle cx="50" cy="55" r="20" fill="#4c0519" stroke="#f472b6" stroke-width="1.8"/>
        <path d="M 34,45 Q 50,75 66,45 Q 50,15 34,45" fill="none" stroke="#fdf2f8" stroke-width="2"/>
        <path d="M 34,65 Q 50,35 66,65 Q 50,95 34,65" fill="none" stroke="#f1df76" stroke-width="2"/>"""),
        
    ("wardens", "THE VEIL WARDENS", "#10b981", "#062b1a",
     """<polygon points="50,16 84,38 84,76 50,94 16,76 16,38" fill="#03170e" stroke="#10b981" stroke-width="2.5"/>
        <path d="M 50,26 L 74,38 L 74,66 Q 50,84 50,84 Q 26,66 26,38 Z" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <line x1="50" y1="36" x2="50" y2="72" stroke="#fff" stroke-width="2"/>
        <line x1="38" y1="50" x2="62" y2="50" stroke="#fff" stroke-width="2"/>"""),
        
    ("collectors", "THE COLLECTORS ENCLAVE", "#f59e0b", "#361c04",
     """<polygon points="50,16 84,38 84,76 50,94 16,76 16,38" fill="#1e1002" stroke="#f59e0b" stroke-width="2.5"/>
        <circle cx="50" cy="55" r="20" fill="#451a03" stroke="#fbbf24" stroke-width="2"/>
        <rect x="40" y="45" width="20" height="20" rx="3" fill="#78350f" stroke="#fff" stroke-width="1.5"/>
        <circle cx="50" cy="55" r="4" fill="#f1df76"/>"""),
        
    ("horizon_caravan", "THE HORIZON CARAVAN", "#eab308", "#332204",
     """<polygon points="50,16 84,38 84,76 50,94 16,76 16,38" fill="#1c1202" stroke="#eab308" stroke-width="2.5"/>
        <path d="M 26,66 L 50,30 L 74,66 Z" fill="#451a03" stroke="#facc15" stroke-width="2"/>
        <circle cx="50" cy="46" r="6" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
        <line x1="22" y1="72" x2="78" y2="72" stroke="#f1df76" stroke-width="2"/>"""),
        
    ("memory_washers", "THE MEMORY WASHERS", "#06b6d4", "#042830",
     """<polygon points="50,16 84,38 84,76 50,94 16,76 16,38" fill="#02161b" stroke="#06b6d4" stroke-width="2.5"/>
        <circle cx="50" cy="55" r="22" fill="#083344" stroke="#22d3ee" stroke-width="1.8"/>
        <path d="M 32,55 Q 50,32 68,55 Q 50,78 32,55 Z" fill="#0e7490" stroke="#cffafe" stroke-width="1.5"/>
        <circle cx="50" cy="55" r="5" fill="#fff"/>"""),
        
    ("giltong_enforcers", "THE GILTONG ENFORCERS", "#dc2626", "#360606",
     """<polygon points="50,16 84,38 84,76 50,94 16,76 16,38" fill="#1c0202" stroke="#dc2626" stroke-width="2.5"/>
        <polygon points="50,26 72,40 72,70 50,84 28,70 28,40" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
        <line x1="36" y1="42" x2="64" y2="68" stroke="#fff" stroke-width="2.5"/>
        <line x1="64" y1="42" x2="36" y2="68" stroke="#fff" stroke-width="2.5"/>"""),
        
    ("founding_corps", "THE FOUNDING CORPORATIONS", "#64748b", "#121926",
     """<polygon points="50,16 84,38 84,76 50,94 16,76 16,38" fill="#080c14" stroke="#94a3b8" stroke-width="2.5"/>
        <rect x="32" y="36" width="36" height="36" rx="4" fill="#1e293b" stroke="#cbd5e1" stroke-width="2"/>
        <rect x="40" y="44" width="20" height="20" rx="2" fill="#334155" stroke="#f1df76" stroke-width="1.5"/>"""),
        
    ("underworld", "THE UNDERWORLD & WOUND WALKERS", "#713f12", "#241002",
     """<polygon points="50,16 84,38 84,76 50,94 16,76 16,38" fill="#120601" stroke="#d97706" stroke-width="2.5"/>
        <path d="M 30,68 L 50,32 L 70,68 L 50,56 Z" fill="#451a03" stroke="#f59e0b" stroke-width="2"/>
        <circle cx="50" cy="46" r="4" fill="#ef4444"/>""")
]

for tag, name, col, dark_col, inner_gfx in FACTIONS:
    fac_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <radialGradient id="facGrad_{tag}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{col}" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="{dark_col}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <!-- Inset frame with 3px safe border -->
  <rect x="3" y="3" width="94" height="94" rx="12" fill="{dark_col}" stroke="{col}" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1" stroke-dasharray="4 2"/>
  <circle cx="50" cy="50" r="40" fill="url(#facGrad_{tag})"/>
  {inner_gfx}
</svg>"""

    save_svg(fac_svg, [
        f"assets/icons/icon_faction_{tag}.svg",
        f"assets/icons/fac_{tag}.svg"
    ])

print("Faction icons generated!")

# ==============================================================================
# 4. ALL 9 CHARACTER ECHO-CORE ICONS & AVATARS (Inset & Canonical Colors)
# ==============================================================================

CORES = [
    ("majin", "DIRECTOR MAJIN", "FLOOR 1 COMMAND", "#f1df76", "#78350f", "#451a03", "CORE 1",
     """<circle cx="50" cy="50" r="26" fill="#78350f" stroke="#f1df76" stroke-width="2.2"/>
        <polygon points="50,30 66,42 66,58 50,70 34,58 34,42" fill="#451a03" stroke="#f1df76" stroke-width="1.8"/>
        <circle cx="50" cy="50" r="7" fill="#fff"/>"""),
        
    ("seiyon", "SECRETARY SEIYON", "EXECUTIVE ARCHIVE", "#38bdf8", "#0c4a6e", "#082f49", "CORE 2",
     """<circle cx="50" cy="50" r="26" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2.2"/>
        <path d="M 50,30 L 68,64 L 32,64 Z" fill="#082f49" stroke="#7dd3fc" stroke-width="1.8"/>
        <circle cx="50" cy="52" r="7" fill="#f1df76"/>"""),
        
    ("dekan", "CONTAINMENT LEAD DEKAN", "FLOOR 2 MAW'S KEEP", "#ef4444", "#7f1d1d", "#450a0a", "CORE 3",
     """<circle cx="50" cy="50" r="26" fill="#7f1d1d" stroke="#ef4444" stroke-width="2.2"/>
        <rect x="36" y="36" width="28" height="28" rx="4" fill="#450a0a" stroke="#fca5a5" stroke-width="1.8"/>
        <circle cx="50" cy="50" r="6" fill="#fff"/>"""),
        
    ("zyrak", "EXTRACTION LEAD ZYRAK", "FLOOR 3 EXTRACTION", "#f59e0b", "#78350f", "#451a03", "CORE 4",
     """<circle cx="50" cy="50" r="26" fill="#78350f" stroke="#f59e0b" stroke-width="2.2"/>
        <polygon points="50,28 68,66 32,66" fill="#451a03" stroke="#fbbf24" stroke-width="1.8"/>
        <polygon points="50,40 60,60 40,60" fill="#38bdf8"/>"""),
        
    ("ayshuk", "RESEARCH LEAD AYSHUK", "FLOOR 4 INSIGHT FORGE", "#10b981", "#064e3b", "#022c22", "CORE 5",
     """<circle cx="50" cy="50" r="26" fill="#064e3b" stroke="#10b981" stroke-width="2.2"/>
        <circle cx="50" cy="50" r="15" fill="#022c22" stroke="#6ee7b7" stroke-width="1.8"/>
        <polygon points="50,40 58,50 50,60 42,50" fill="#f1df76"/>"""),
        
    ("mellda", "BORDER LEAD MELLDA", "FLOOR 5 BORDER WATCH", "#0284c7", "#0c4a6e", "#082f49", "CORE 6",
     """<circle cx="50" cy="50" r="26" fill="#0c4a6e" stroke="#0284c7" stroke-width="2.2"/>
        <path d="M 50,30 L 68,40 L 68,60 L 50,70 L 32,60 L 32,40 Z" fill="#082f49" stroke="#38bdf8" stroke-width="1.8"/>
        <circle cx="50" cy="50" r="6" fill="#fff"/>"""),
        
    ("marjuk", "ARCHIVE LEAD MARJUK", "FLOOR 6 DEEP VAULT", "#8b5cf6", "#3b0764", "#2e1065", "CORE 7",
     """<circle cx="50" cy="50" r="26" fill="#3b0764" stroke="#8b5cf6" stroke-width="2.2"/>
        <rect x="36" y="36" width="28" height="28" rx="4" fill="#2e1065" stroke="#c084fc" stroke-width="1.8"/>
        <polygon points="50,42 56,50 50,58 44,50" fill="#f1df76"/>"""),
        
    ("ishall", "OUTSIDER ISHALL", "FLOOR 7 SHADOW CORPS", "#e11d48", "#4c0519", "#2d0505", "CORE 8",
     """<circle cx="50" cy="50" r="26" fill="#4c0519" stroke="#e11d48" stroke-width="2.2"/>
        <path d="M 36,44 Q 50,28 64,44 Q 70,62 50,72 Q 30,62 36,44 Z" fill="#2d0505" stroke="#fb7185" stroke-width="1.8"/>
        <circle cx="50" cy="50" r="5" fill="#fff"/>"""),
        
    ("xyan", "EXILE XYAN", "FLOOR 8 GATE WATCH", "#94a3b8", "#1e293b", "#0f172a", "CORE 9",
     """<circle cx="50" cy="50" r="26" fill="#1e293b" stroke="#94a3b8" stroke-width="2.2"/>
        <polygon points="50,30 68,40 68,62 50,72 32,62 32,40" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.8"/>
        <line x1="50" y1="30" x2="50" y2="72" stroke="#f1df76" stroke-width="2"/>""")
]

for tag, name, role, col, dark_col, deep_col, code, inner_gfx in CORES:
    # Core Icon
    core_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect x="3" y="3" width="94" height="94" rx="12" fill="{deep_col}" stroke="{col}" stroke-width="2.5"/>
  <rect x="6" y="6" width="88" height="88" rx="9" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1" stroke-dasharray="4 2"/>
  {inner_gfx}
  <rect x="8" y="7" width="26" height="12" rx="2" fill="{dark_col}" stroke="{col}" stroke-width="1"/>
  <text x="21" y="15.5" fill="{col}" font-family="Arial, sans-serif" font-size="7" font-weight="bold" text-anchor="middle">{code}</text>
</svg>"""

    # Avatar Badge
    avatar_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="{deep_col}" stroke="{col}" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="48" fill="none" stroke="rgba(255, 255, 255, 0.25)" stroke-width="1" stroke-dasharray="4 2"/>
  <g transform="translate(10, 10)">
    {inner_gfx}
  </g>
</svg>"""

    save_svg(core_svg, [f"assets/icons/icon_core_{tag}.svg"])
    save_svg(avatar_svg, [f"assets/avatars/avatar_core_{tag}.svg"])

print("Echo-Core icons and avatars built!")
