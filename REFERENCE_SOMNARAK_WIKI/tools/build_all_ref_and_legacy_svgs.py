#!/usr/bin/env python3
"""
tools/build_all_ref_and_legacy_svgs.py
Ensures all ref_*.svg, somnarak_icon.svg, weapon.svg, and remaining legacy SVGs
have proper insets, no border clipping, and follow canonical Somnarak styling.
"""

import os, glob

WIKI_DIR = "/home/user/01_Somnarak_Wiki"
ASSETS_ICONS = os.path.join(WIKI_DIR, "assets/icons")
HAND_ICONS = os.path.join(WIKI_DIR, "assets/layout/hand/icons")
ICONS_DIR = "/home/user/icons"

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

# Somnarak Main Emblem (Inset)
SOMNARAK_ICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
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
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <!-- Background Shield Plate with 3px safe margin -->
  <rect x="3" y="3" width="114" height="114" rx="16" fill="#060910" stroke="url(#goldGlow)" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="44" fill="url(#cyanBackdrop)"/>
  <circle cx="60" cy="60" r="40" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6 3"/>
  
  <!-- Outer Diamond Mandate -->
  <polygon points="60,14 104,60 60,106 16,60" fill="#090e18" stroke="url(#goldGlow)" stroke-width="2.5" filter="url(#neonDrop)"/>
  
  <!-- Inner Alpha Tree & Weeping Eye -->
  <path d="M 32,60 Q 60,30 88,60 Q 60,90 32,60 Z" fill="#030508" stroke="#ef4444" stroke-width="2"/>
  <circle cx="60" cy="60" r="13" fill="url(#goldGlow)" stroke="#f8fafc" stroke-width="1.5"/>
  <circle cx="60" cy="60" r="5.5" fill="#030508"/>
  <circle cx="60" cy="60" r="2.2" fill="#38bdf8"/>
</svg>"""

save_svg(SOMNARAK_ICON, ["assets/icons/somnarak_icon.svg"])

# Weapon Icon
WEAPON_ICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="3" y="3" width="114" height="114" rx="14" fill="#0d0e14" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="44" fill="#1e1014"/>
  <line x1="24" y1="96" x2="96" y2="24" stroke="#ef4444" stroke-width="5" stroke-linecap="round"/>
  <polygon points="88,16 104,32 94,40 80,26" fill="#f1df76"/>
  <line x1="96" y1="96" x2="24" y2="24" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>
  <circle cx="60" cy="60" r="14" fill="#090d16" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="5" fill="#f1df76"/>
</svg>"""

save_svg(WEAPON_ICON, ["assets/icons/weapon.svg", "assets/icons/art_maw.svg"])

# Ensure all 32 ref_*.svg have inset frames
REF_LIST = [
    "ref_absolvohan", "ref_battle_system", "ref_cheongula", "ref_corporations",
    "ref_daily_life", "ref_dawn_of_hope", "ref_document_rules", "ref_dream_realm",
    "ref_enemy_list", "ref_entities_overview", "ref_entity_codex", "ref_entity_tales",
    "ref_faction_relations", "ref_faction_tech", "ref_full_cast", "ref_han_relics",
    "ref_horizon_caravan", "ref_maw_codex", "ref_memory_archive", "ref_name_registry",
    "ref_named_fractures", "ref_ordeals_framework", "ref_project_somnarak", "ref_reverie_directorate",
    "ref_sed", "ref_taboo_resonance", "ref_the_desolate", "ref_the_weeping", "ref_ucd",
    "ref_underworld", "ref_unknown_cities", "ref_wound_walkers"
]

for ref_name in REF_LIST:
    title = ref_name.replace("ref_", "").replace("_", " ").upper()
    ref_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="3" y="3" width="114" height="114" rx="14" fill="#060910" stroke="#38bdf8" stroke-width="2"/>
  <rect x="6" y="6" width="108" height="108" rx="10" fill="none" stroke="rgba(241, 223, 118, 0.25)" stroke-width="1"/>
  <circle cx="60" cy="52" r="28" fill="#0c1726" stroke="#f1df76" stroke-width="2"/>
  <polygon points="60,34 76,52 60,70 44,52" fill="#38bdf8"/>
  <circle cx="60" cy="52" r="5" fill="#fff"/>
  <text x="60" y="104" fill="#f1df76" font-family="Arial, sans-serif" font-size="7" font-weight="bold" text-anchor="middle">ARCHIVE DOC</text>
</svg>"""
    save_svg(ref_svg, [f"assets/icons/{ref_name}.svg"])

print("All reference and legacy SVGs updated with proper insets!")
