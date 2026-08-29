#!/usr/bin/env python3
"""
tools/generate_final_bespoke_hub_icons.py
Creates bespoke SVG icons for:
- icon_lore_efflorescence.svg
- icon_lore_three_sorrows.svg
- icon_lore_cosmology.svg
- icon_mech_relic_tools.svg
"""

import os

ICONS_DIR = "/home/user/01_Somnarak_Wiki/assets/icons"
WORKSPACE_ICONS_DIR = "/home/user/icons"

def make_efflorescence_icon():
    # Crystalline / biological Han crystallization bloom
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="effGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#be123c" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="56" r="38" fill="url(#effGlow)"/>
  
  <!-- Crystalline Petals -->
  <path d="M 60 22 L 68 46 L 60 56 L 52 46 Z" fill="#38bdf8" opacity="0.9"/>
  <path d="M 60 90 L 68 66 L 60 56 L 52 66 Z" fill="#ef5b55" opacity="0.9"/>
  <path d="M 26 56 L 50 48 L 60 56 L 50 64 Z" fill="#71efaf" opacity="0.9"/>
  <path d="M 94 56 L 70 48 L 60 56 L 70 64 Z" fill="#f1df76" opacity="0.9"/>
  
  <!-- Diagonal Petals -->
  <path d="M 36 32 L 54 48 L 60 56 L 46 58 Z" fill="#38bdf8" opacity="0.75"/>
  <path d="M 84 32 L 74 48 L 60 56 L 66 58 Z" fill="#f1df76" opacity="0.75"/>
  <path d="M 36 80 L 46 58 L 60 56 L 54 64 Z" fill="#71efaf" opacity="0.75"/>
  <path d="M 84 80 L 66 58 L 60 56 L 74 64 Z" fill="#ef5b55" opacity="0.75"/>
  
  <!-- Center Core -->
  <circle cx="60" cy="56" r="8" fill="#070a12" stroke="#f1df76" stroke-width="2"/>
  <circle cx="60" cy="56" r="3" fill="#f1df76"/>
  
  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0c192c" stroke="#38bdf8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#38bdf8" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">EFFLORESCENCE</text>
</svg>"""

def make_three_sorrows_icon():
    # Tri-fold Sorrow Trinity (Grudge, Lament, Void)
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="triGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef5b55" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#ef5b55" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="54" r="36" fill="url(#triGlow)"/>

  <!-- Triquetra / Triangular Sorrow Nodes -->
  <!-- Top Node: Grudge (Crimson) -->
  <circle cx="60" cy="30" r="14" fill="#1c0a0a" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="60" cy="30" r="5" fill="#ef5b55"/>
  
  <!-- Bottom-Left Node: Lament (Cyan) -->
  <circle cx="38" cy="68" r="14" fill="#07192c" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="38" cy="68" r="5" fill="#38bdf8"/>
  
  <!-- Bottom-Right Node: Void (Gold/Black) -->
  <circle cx="82" cy="68" r="14" fill="#1f1807" stroke="#f1df76" stroke-width="2"/>
  <circle cx="82" cy="68" r="5" fill="#f1df76"/>

  <!-- Connecting Resonant Arcs -->
  <path d="M 60 30 Q 38 49 38 68 Q 60 68 82 68 Q 82 49 60 30 Z" fill="none" stroke="#f1df76" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="60" cy="56" r="6" fill="#070a12" stroke="#ffffff" stroke-width="1.5"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1f0a0a" stroke="#ef5b55" stroke-width="1"/>
  <text x="60" y="108.5" fill="#ef5b55" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">THREE SORROWS</text>
</svg>"""

def make_cosmology_icon():
    # Celestial sphere, Alpha Tree root system, 1778 cycles
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="cosmoGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="54" r="38" fill="url(#cosmoGlow)"/>

  <!-- Outer Ring with Orbit Marks -->
  <circle cx="60" cy="54" r="32" fill="none" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="60" cy="54" r="24" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4,3"/>
  
  <!-- Axis of the Sphere -->
  <line x1="60" y1="18" x2="60" y2="90" stroke="#f1df76" stroke-width="1.5"/>
  <line x1="24" y1="54" x2="96" y2="54" stroke="#f1df76" stroke-width="1.5"/>

  <!-- Center Tree / City Core Pivot -->
  <polygon points="60,34 72,54 60,74 48,54" fill="#141c09" stroke="#71efaf" stroke-width="1.5"/>
  <circle cx="60" cy="54" r="4" fill="#f1df76"/>

  <!-- Orbiting Moons / Cycles -->
  <circle cx="84" cy="36" r="3.5" fill="#ef5b55"/>
  <circle cx="36" cy="72" r="3.5" fill="#38bdf8"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1a1805" stroke="#f1df76" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f1df76" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">COSMOLOGY</text>
</svg>"""

def make_relic_tools_icon():
    # Han-Relic Tool & Industrial Containment Apparatus
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="toolGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#71efaf" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#71efaf" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="54" r="36" fill="url(#toolGlow)"/>

  <!-- Crossed Han Measuring Implement and Extractor Rod -->
  <path d="M 30 78 L 78 30 L 88 40 L 40 88 Z" fill="#0b2416" stroke="#71efaf" stroke-width="1.5"/>
  <path d="M 78 78 L 30 30 L 40 20 L 88 68 Z" fill="#0b2416" stroke="#38bdf8" stroke-width="1.5"/>

  <!-- Central Containment Gauge -->
  <circle cx="60" cy="54" r="14" fill="#070a12" stroke="#f1df76" stroke-width="2"/>
  <path d="M 60 54 L 68 46" stroke="#ef5b55" stroke-width="2" stroke-linecap="round"/>
  <circle cx="60" cy="54" r="3" fill="#f1df76"/>

  <!-- Industrial Fasteners -->
  <circle cx="34" cy="34" r="2.5" fill="#71efaf"/>
  <circle cx="84" cy="34" r="2.5" fill="#38bdf8"/>
  <circle cx="34" cy="84" r="2.5" fill="#38bdf8"/>
  <circle cx="84" cy="84" r="2.5" fill="#71efaf"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#061e11" stroke="#71efaf" stroke-width="1"/>
  <text x="60" y="108.5" fill="#71efaf" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">RELIC TOOLS</text>
</svg>"""

def main():
    icons = {
        "icon_lore_efflorescence.svg": make_efflorescence_icon(),
        "icon_lore_three_sorrows.svg": make_three_sorrows_icon(),
        "icon_lore_cosmology.svg": make_cosmology_icon(),
        "icon_mech_relic_tools.svg": make_relic_tools_icon(),
    }

    for name, svg in icons.items():
        p1 = os.path.join(ICONS_DIR, name)
        p2 = os.path.join(WORKSPACE_ICONS_DIR, name)
        with open(p1, "w", encoding="utf-8") as f:
            f.write(svg)
        with open(p2, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"Generated: {name}")

if __name__ == "__main__":
    main()
