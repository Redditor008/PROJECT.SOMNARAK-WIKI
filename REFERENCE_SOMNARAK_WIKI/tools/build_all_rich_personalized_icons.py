#!/usr/bin/env python3
"""
tools/build_all_rich_personalized_icons.py
Builds personalized, high-detail vector SVG icons for Locations, Lore, Mechanics,
Departments, and Factions.
"""

import os

WIKI_ASSETS_ICONS = "/home/user/01_Somnarak_Wiki/assets/icons"
WIKI_ASSETS_CITY = "/home/user/01_Somnarak_Wiki/assets/layout/city/icons"
WIKI_ASSETS_HAND = "/home/user/01_Somnarak_Wiki/assets/layout/hand/icons"
WORKSPACE_ICONS = "/home/user/icons"

def get_location_icons():
    return {
        # The Maw - Subterranean Chasm Vortex & Descent Cables
        "icon_loc_the_maw.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="mawVortex" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#070a12" stop-opacity="1"/>
      <stop offset="50%" stop-color="#0284c7" stop-opacity="0.8"/>
      <stop offset="80%" stop-color="#ef4444" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#0284c7" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  
  <!-- Outer Chasm Rim -->
  <circle cx="60" cy="54" r="38" fill="url(#mawVortex)" stroke="#38bdf8" stroke-width="1.5"/>
  
  <!-- Spiraling Han Chasm Rings -->
  <ellipse cx="60" cy="54" rx="30" ry="22" fill="none" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="6,4"/>
  <ellipse cx="60" cy="54" rx="20" ry="14" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,2"/>
  <ellipse cx="60" cy="54" rx="10" ry="7" fill="none" stroke="#f1df76" stroke-width="1.8"/>
  <circle cx="60" cy="54" r="3" fill="#070a12" stroke="#ffffff" stroke-width="1"/>

  <!-- Descent Cables & Elevator Rig -->
  <line x1="60" y1="16" x2="60" y2="52" stroke="#f1df76" stroke-width="1.5"/>
  <rect x="56" y="42" width="8" height="6" fill="#0f172a" stroke="#f1df76" stroke-width="1"/>
  <line x1="26" y1="36" x2="60" y2="54" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="94" y1="36" x2="60" y2="54" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2,2"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0c192c" stroke="#0284c7" stroke-width="1"/>
  <text x="60" y="108.5" fill="#38bdf8" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">THE MAW // CHASM</text>
</svg>""",

        # The Desolate - Scorched Red Wasteland & Broken Telegraph Poles
        "icon_loc_the_desolate.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="desSky" cx="50%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#7f1d1d" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <rect x="10" y="10" width="100" height="78" rx="8" fill="url(#desSky)"/>

  <!-- Scorched Cracked Earth Horizon -->
  <path d="M 10 66 Q 35 58 60 64 Q 85 70 110 62 L 110 88 L 10 88 Z" fill="#1c0a0a" stroke="#ef4444" stroke-width="1.5"/>
  <!-- Ground Fissures -->
  <path d="M 30 76 L 46 68 L 56 74 L 72 66 L 86 76" fill="none" stroke="#f87171" stroke-width="1.2"/>
  <line x1="56" y1="74" x2="60" y2="86" stroke="#f87171" stroke-width="1"/>

  <!-- Broken Telegraph Posts -->
  <line x1="36" y1="70" x2="36" y2="42" stroke="#ef4444" stroke-width="1.8"/>
  <line x1="30" y1="48" x2="42" y2="48" stroke="#ef4444" stroke-width="1.5"/>
  <line x1="80" y1="72" x2="84" y2="50" stroke="#ef4444" stroke-width="1.8"/>
  <line x1="76" y1="56" x2="88" y2="54" stroke="#ef4444" stroke-width="1.5"/>
  <path d="M 36 48 Q 60 58 84 54" fill="none" stroke="#ef4444" stroke-width="1" stroke-dasharray="2,2"/>

  <!-- Radioactive Red Sun / Dust Moon -->
  <circle cx="60" cy="34" r="10" fill="#991b1b" stroke="#fca5a5" stroke-width="1.2"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#200a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="60" y="108.5" fill="#ef4444" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">THE DESOLATE</text>
</svg>""",

        # The Hollow Glass - Towering Vitrified Crystalline Spire
        "icon_loc_the_hollow_glass.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="glassGlow" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#glassGlow)"/>

  <!-- Vitrified Glass Spire Monolith -->
  <polygon points="60,16 76,78 60,88 44,78" fill="#0c2340" stroke="#38bdf8" stroke-width="2"/>
  <line x1="60" y1="16" x2="60" y2="88" stroke="#ffffff" stroke-width="1.5"/>
  
  <!-- Facet Reflection Planes -->
  <polygon points="60,16 76,78 60,88" fill="#0369a1" opacity="0.6"/>
  <polygon points="60,16 44,78 60,88" fill="#0284c7" opacity="0.4"/>

  <!-- Refraction Beams -->
  <line x1="60" y1="36" x2="24" y2="28" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="3,2"/>
  <line x1="60" y1="36" x2="96" y2="28" stroke="#f1df76" stroke-width="1.2" stroke-dasharray="3,2"/>
  <line x1="60" y1="56" x2="20" y2="60" stroke="#71efaf" stroke-width="1.2" stroke-dasharray="3,2"/>
  <line x1="60" y1="56" x2="100" y2="60" stroke="#ef5b55" stroke-width="1.2" stroke-dasharray="3,2"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0c192c" stroke="#38bdf8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#38bdf8" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">HOLLOW GLASS</text>
</svg>""",

        # Library of Stolen Pasts - Cathedral of Book Arches & Memory Spheres
        "icon_loc_the_library_of_stolen_pasts.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="libGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#818cf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#libGlow)"/>

  <!-- Towering Archway of Memory Bookshelves -->
  <path d="M 28 88 L 28 44 Q 60 16 92 44 L 92 88 Z" fill="#0f172a" stroke="#818cf8" stroke-width="2"/>
  <path d="M 38 88 L 38 48 Q 60 26 82 48 L 82 88 Z" fill="#1e1b4b" stroke="#a5b4fc" stroke-width="1.2"/>

  <!-- Floating Open Memory Codex -->
  <polygon points="60,66 40,54 42,76 60,86" fill="#312e81" stroke="#f1df76" stroke-width="1.2"/>
  <polygon points="60,66 80,54 78,76 60,86" fill="#3730a3" stroke="#f1df76" stroke-width="1.2"/>
  <line x1="60" y1="66" x2="60" y2="86" stroke="#f1df76" stroke-width="1.5"/>

  <!-- Spectral Floating Memory Orbs -->
  <circle cx="60" cy="40" r="5" fill="#e0e7ff" stroke="#818cf8" stroke-width="1.5"/>
  <circle cx="44" cy="38" r="3" fill="#818cf8"/>
  <circle cx="76" cy="38" r="3" fill="#818cf8"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1e1b4b" stroke="#818cf8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#a5b4fc" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">STOLEN PASTS</text>
</svg>""",

        # Orphan Bell Tower - Gothic Resonating Belfry & Acoustic Waves
        "icon_loc_the_orphan_bell_tower.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="bellGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.7"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f59e0b" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#bellGlow)"/>

  <!-- Tower Spire Structure -->
  <polygon points="60,14 74,40 46,40" fill="#1c1917" stroke="#f59e0b" stroke-width="1.5"/>
  <rect x="46" y="40" width="28" height="48" fill="#292524" stroke="#d97706" stroke-width="1.5"/>

  <!-- Belfry Arch & Great Bronze Bell -->
  <path d="M 50 56 Q 60 48 70 56 L 70 76 L 50 76 Z" fill="#0c0a09" stroke="#fbbf24" stroke-width="1.2"/>
  <path d="M 54 62 Q 60 54 66 62 L 68 72 L 52 72 Z" fill="#b45309" stroke="#fef08a" stroke-width="1.5"/>
  <circle cx="60" cy="74" r="2.5" fill="#fef08a"/>

  <!-- Resonant Sonic Rings -->
  <circle cx="60" cy="66" r="22" fill="none" stroke="#fbbf24" stroke-width="1" stroke-dasharray="4,3"/>
  <circle cx="60" cy="66" r="32" fill="none" stroke="#f59e0b" stroke-width="1" stroke-dasharray="3,4"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#291804" stroke="#f59e0b" stroke-width="1"/>
  <text x="60" y="108.5" fill="#fbbf24" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">BELL TOWER</text>
</svg>""",

        # Unknown Cities - Long-Range Sonar Radar & Sunken Towers
        "icon_loc_unknown_cities.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="unkGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#10b981" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#unkGlow)"/>

  <!-- Radar Rings -->
  <circle cx="60" cy="52" r="32" fill="none" stroke="#34d399" stroke-width="1"/>
  <circle cx="60" cy="52" r="20" fill="none" stroke="#059669" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="60" y1="18" x2="60" y2="86" stroke="#047857" stroke-width="1"/>
  <line x1="26" y1="52" x2="94" y2="52" stroke="#047857" stroke-width="1"/>

  <!-- Sonar Sweep Beam -->
  <polygon points="60,52 86,26 86,52" fill="#34d399" opacity="0.3"/>
  <line x1="60" y1="52" x2="86" y2="26" stroke="#6ee7b7" stroke-width="1.8"/>

  <!-- Sunken Skyscraper Silhouettes in Fog -->
  <rect x="34" y="56" width="10" height="24" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
  <rect x="48" y="44" width="12" height="36" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
  <rect x="68" y="50" width="10" height="30" fill="#064e3b" stroke="#34d399" stroke-width="1"/>

  <!-- Blip Signals -->
  <circle cx="78" cy="36" r="3" fill="#ef4444"/>
  <circle cx="40" cy="40" r="2.5" fill="#f1df76"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#062e22" stroke="#10b981" stroke-width="1"/>
  <text x="60" y="108.5" fill="#34d399" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">UNKNOWN CITIES</text>
</svg>"""
    }

def main():
    icons = get_location_icons()
    for name, svg in icons.items():
        p1 = os.path.join(WIKI_ASSETS_ICONS, name)
        p2 = os.path.join(WORKSPACE_ICONS, name)
        for path in [p1, p2]:
            with open(path, "w", encoding="utf-8") as f:
                f.write(svg)
        print(f"Generated Location Icon: {name}")

if __name__ == "__main__":
    main()
