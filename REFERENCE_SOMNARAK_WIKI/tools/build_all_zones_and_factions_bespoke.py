#!/usr/bin/env python3
"""
tools/build_all_zones_and_factions_bespoke.py
Generates personalized, high-detail vector SVG icons for Zones A-E, City Badges,
and all 14 Factions.
"""

import os

WIKI_ASSETS_ICONS = "/home/user/01_Somnarak_Wiki/assets/icons"
WIKI_ASSETS_CITY = "/home/user/01_Somnarak_Wiki/assets/layout/city/icons"
WORKSPACE_ICONS = "/home/user/icons"

def get_zone_and_city_icons():
    return {
        # Zone A Core - The Alpha Spire & Directorate Citadel
        "icon_zone_a_core.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="zA_Glow" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#f59e0b" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#zA_Glow)"/>

  <!-- Directorate Spire & Alpha Trunk Core -->
  <polygon points="60,14 74,74 60,86 46,74" fill="#291b05" stroke="#f1df76" stroke-width="2"/>
  <line x1="60" y1="14" x2="60" y2="86" stroke="#ffffff" stroke-width="1.5"/>

  <!-- Energy Rings surrounding Spire -->
  <ellipse cx="60" cy="40" rx="26" ry="8" fill="none" stroke="#fef08a" stroke-width="1.5"/>
  <ellipse cx="60" cy="58" rx="34" ry="10" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,2"/>

  <!-- Core Citadel Base -->
  <rect x="42" y="74" width="36" height="14" rx="2" fill="#1c1917" stroke="#f1df76" stroke-width="1.5"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1f1807" stroke="#f1df76" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f1df76" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">ZONE A // CORE</text>
</svg>""",

        # Zone B West - Industrial Han Refineries & Heavy Smokestacks
        "icon_zone_b_west.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="zB_Glow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#f97316" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f97316" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#zB_Glow)"/>

  <!-- Heavy Industrial Refinery Chimneys -->
  <rect x="32" y="28" width="12" height="58" fill="#1c1917" stroke="#f97316" stroke-width="1.5"/>
  <rect x="52" y="20" width="16" height="66" fill="#292524" stroke="#fb923c" stroke-width="1.5"/>
  <rect x="76" y="34" width="12" height="52" fill="#1c1917" stroke="#f97316" stroke-width="1.5"/>

  <!-- Glowing Smoke & Molten Vents -->
  <circle cx="38" cy="22" r="4" fill="#fb923c"/>
  <circle cx="60" cy="14" r="5" fill="#fed7aa"/>
  <circle cx="82" cy="28" r="4" fill="#fb923c"/>

  <!-- Interconnecting Refinery Pipes -->
  <path d="M 28 62 L 92 62" stroke="#f97316" stroke-width="2"/>
  <path d="M 28 74 L 92 74" stroke="#ea580c" stroke-width="2"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#271305" stroke="#f97316" stroke-width="1"/>
  <text x="60" y="108.5" fill="#fb923c" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">ZONE B // REFINERY</text>
</svg>""",

        # Zone C East - High-Tech Arcologies & Commercial Skyways
        "icon_zone_c_east.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="zC_Glow" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#zC_Glow)"/>

  <!-- Sleek Corporate Glass Skyscrapers -->
  <polygon points="40,24 54,24 54,86 40,86" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="56,16 72,16 72,86 56,86" fill="#1e293b" stroke="#7dd3fc" stroke-width="1.8"/>
  <polygon points="74,32 86,32 86,86 74,86" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>

  <!-- Illuminated Sky-Bridges -->
  <line x1="38" y1="46" x2="88" y2="46" stroke="#38bdf8" stroke-width="2"/>
  <line x1="42" y1="64" x2="84" y2="64" stroke="#38bdf8" stroke-width="2"/>

  <!-- Holographic Window Grids -->
  <line x1="60" y1="24" x2="68" y2="24" stroke="#e0f2fe" stroke-width="1.2"/>
  <line x1="60" y1="32" x2="68" y2="32" stroke="#e0f2fe" stroke-width="1.2"/>
  <line x1="60" y1="40" x2="68" y2="40" stroke="#e0f2fe" stroke-width="1.2"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0c192c" stroke="#38bdf8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#38bdf8" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">ZONE C // ARCOLOGY</text>
</svg>""",

        # Zone D Flanks - High-Density Residential Tenements & Bastions
        "icon_zone_d_flanks.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="zD_Glow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#10b981" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#zD_Glow)"/>

  <!-- Stepped Modular Tenement Blocks -->
  <polygon points="26,86 26,52 46,52 46,40 74,40 74,48 94,48 94,86" fill="#062e22" stroke="#10b981" stroke-width="1.8"/>

  <!-- Watchtowers & Defense Antennas -->
  <line x1="36" y1="52" x2="36" y2="34" stroke="#34d399" stroke-width="1.5"/>
  <circle cx="36" cy="34" r="2" fill="#71efaf"/>
  <line x1="84" y1="48" x2="84" y2="30" stroke="#34d399" stroke-width="1.5"/>
  <circle cx="84" cy="30" r="2" fill="#71efaf"/>

  <!-- Lit Habitation Windows -->
  <circle cx="54" cy="52" r="2" fill="#fef08a"/>
  <circle cx="66" cy="52" r="2" fill="#fef08a"/>
  <circle cx="54" cy="64" r="2" fill="#fef08a"/>
  <circle cx="66" cy="64" r="2" fill="#fef08a"/>
  <circle cx="36" cy="68" r="2" fill="#fef08a"/>
  <circle cx="84" cy="68" r="2" fill="#fef08a"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#062e22" stroke="#10b981" stroke-width="1"/>
  <text x="60" y="108.5" fill="#34d399" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">ZONE D // FLANKS</text>
</svg>""",

        # Zone E Bulwark - Fortified Shield Battlements & Projectors
        "icon_zone_e_bulwark.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="zE_Glow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#zE_Glow)"/>

  <!-- Colossal Shield Barrier Arc -->
  <path d="M 22 82 Q 60 22 98 82" fill="none" stroke="#ef4444" stroke-width="2.5"/>
  <path d="M 28 84 Q 60 30 92 84" fill="none" stroke="#fca5a5" stroke-width="1" stroke-dasharray="3,3"/>

  <!-- Heavy Bastion Wall & Massive Blast Gate -->
  <polygon points="20,86 20,66 38,66 44,74 76,74 82,66 100,66 100,86" fill="#1c0a0a" stroke="#ef4444" stroke-width="1.8"/>
  <rect x="52" y="74" width="16" height="12" fill="#7f1d1d" stroke="#fca5a5" stroke-width="1"/>

  <!-- Shield Projector Emitters -->
  <circle cx="34" cy="62" r="4" fill="#ef4444" stroke="#ffffff" stroke-width="1"/>
  <circle cx="86" cy="62" r="4" fill="#ef4444" stroke="#ffffff" stroke-width="1"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#200a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="60" y="108.5" fill="#ef4444" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">ZONE E // BULWARK</text>
</svg>""",

        # Alpha Tree - Bioluminescent World Tree & Subterranean Roots
        "icon_alpha_tree.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="treeGlow" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#71efaf" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#38bdf8" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#71efaf" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#treeGlow)"/>

  <!-- Tree Trunk & Branching Canopy -->
  <path d="M 56 86 L 56 50 L 40 32 L 48 30 L 58 44 L 58 20 L 62 20 L 62 44 L 72 30 L 80 32 L 64 50 L 64 86 Z" fill="#064e3b" stroke="#71efaf" stroke-width="1.8"/>

  <!-- Bioluminescent Canopy Spheres -->
  <circle cx="60" cy="18" r="5" fill="#fef08a"/>
  <circle cx="44" cy="28" r="4" fill="#71efaf"/>
  <circle cx="76" cy="28" r="4" fill="#71efaf"/>
  <circle cx="34" cy="40" r="3" fill="#38bdf8"/>
  <circle cx="86" cy="40" r="3" fill="#38bdf8"/>

  <!-- Deep Subterranean Roots in Weeping -->
  <path d="M 56 86 Q 44 94 36 96" stroke="#38bdf8" stroke-width="1.5" fill="none"/>
  <path d="M 64 86 Q 76 94 84 96" stroke="#38bdf8" stroke-width="1.5" fill="none"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#062e22" stroke="#71efaf" stroke-width="1"/>
  <text x="60" y="108.5" fill="#71efaf" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">ALPHA TREE</text>
</svg>""",

        # District Structure - Concentric City Ring Map Badge
        "icon_somnarak_city_badge.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="mapGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.8"/>
      <stop offset="60%" stop-color="#0284c7" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#mapGlow)"/>

  <!-- Concentric District Rings (A, B, C, D, E) -->
  <circle cx="60" cy="52" r="32" fill="none" stroke="#ef4444" stroke-width="1.5"/>
  <circle cx="60" cy="52" r="24" fill="none" stroke="#10b981" stroke-width="1.2"/>
  <circle cx="60" cy="52" r="16" fill="none" stroke="#38bdf8" stroke-width="1.2"/>
  <circle cx="60" cy="52" r="8" fill="#f1df76" stroke="#ffffff" stroke-width="1.5"/>

  <!-- 4 Coordinate Axis Crosshairs -->
  <line x1="60" y1="16" x2="60" y2="88" stroke="#f1df76" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="24" y1="52" x2="96" y2="52" stroke="#f1df76" stroke-width="1" stroke-dasharray="2,2"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1f1807" stroke="#f1df76" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f1df76" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">CITY DISTRICTS</text>
</svg>"""
    }

def get_faction_icons():
    return {
        # Reverie Directorate - Grand Eagle/Eye of Authority
        "icon_faction_reverie_directorate.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="dirGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#ef5b55" stop-opacity="0.8"/>
      <stop offset="60%" stop-color="#f1df76" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#ef5b55" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#dirGlow)"/>

  <!-- Stylized Authority Wings -->
  <path d="M 20 42 Q 40 28 60 48 Q 80 28 100 42 Q 78 64 60 54 Q 42 64 20 42 Z" fill="#1c0a0a" stroke="#f1df76" stroke-width="1.8"/>

  <!-- Central Directorate Ocular Crest -->
  <circle cx="60" cy="50" r="14" fill="#070a12" stroke="#ef5b55" stroke-width="2"/>
  <ellipse cx="60" cy="50" rx="10" ry="6" fill="#7f1d1d"/>
  <circle cx="60" cy="50" r="3" fill="#fef08a"/>

  <!-- Descending Han Lightning -->
  <polygon points="60,66 64,74 58,74 62,84 56,84 60,94 56,82 62,82" fill="#f1df76"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#200a0a" stroke="#ef5b55" stroke-width="1"/>
  <text x="60" y="108.5" fill="#ef5b55" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">THE DIRECTORATE</text>
</svg>""",

        # High Council of Sights - 7 Monoliths & Golden Laurels
        "icon_faction_high_council.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="hcGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#hcGlow)"/>

  <!-- Golden Council Laurel Arc -->
  <path d="M 30 76 Q 20 40 46 26" fill="none" stroke="#f1df76" stroke-width="2"/>
  <path d="M 90 76 Q 100 40 74 26" fill="none" stroke="#f1df76" stroke-width="2"/>

  <!-- 7 Monolith Council Seats (Radial) -->
  <circle cx="60" cy="24" r="4" fill="#fef08a"/>
  <circle cx="42" cy="32" r="4" fill="#fef08a"/>
  <circle cx="78" cy="32" r="4" fill="#fef08a"/>
  <circle cx="34" cy="50" r="4" fill="#fef08a"/>
  <circle cx="86" cy="50" r="4" fill="#fef08a"/>
  <circle cx="44" cy="68" r="4" fill="#fef08a"/>
  <circle cx="76" cy="68" r="4" fill="#fef08a"/>

  <!-- Central Great Eye of Sight -->
  <polygon points="60,38 72,52 60,66 48,52" fill="#1f1807" stroke="#f1df76" stroke-width="1.8"/>
  <circle cx="60" cy="52" r="3" fill="#ffffff"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1f1807" stroke="#f1df76" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f1df76" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">HIGH COUNCIL</text>
</svg>""",

        # SED Corps - Heavy Tactical Shield & Crossed Rifles
        "icon_faction_sed_corps.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Heavy SED Riot Shield -->
  <polygon points="36,22 84,22 84,62 60,86 36,62" fill="#0c192c" stroke="#38bdf8" stroke-width="2"/>

  <!-- Hazard Chevron on Shield -->
  <path d="M 44 38 L 60 52 L 76 38" fill="none" stroke="#f1df76" stroke-width="2.5"/>
  <path d="M 44 50 L 60 64 L 76 50" fill="none" stroke="#f1df76" stroke-width="2.5"/>

  <!-- Crossed Strike Rifles behind shield -->
  <line x1="22" y1="84" x2="98" y2="20" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>
  <line x1="98" y1="84" x2="22" y2="20" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0c192c" stroke="#38bdf8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#38bdf8" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">SED EXTRACTION</text>
</svg>""",

        # UCD Strike - Lightning Bolt & Breaching Dagger
        "icon_faction_ucd_strike.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Heavy Combat Breaching Dagger -->
  <polygon points="60,18 68,52 64,82 56,82 52,52" fill="#1c0a0a" stroke="#ef4444" stroke-width="2"/>
  <line x1="60" y1="18" x2="60" y2="82" stroke="#ffffff" stroke-width="1.5"/>

  <!-- Rapid Assault Lightning Bolt Crossing Blade -->
  <polygon points="76,26 44,52 58,52 38,82 74,48 58,48" fill="#f1df76" stroke="#ef4444" stroke-width="1"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#200a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="60" y="108.5" fill="#ef4444" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">UCD STRIKE CORPS</text>
</svg>""",

        # Architects Guild - Drafting Divider & City Blueprint Hexagon
        "icon_faction_architects.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Hexagonal Blueprint Grid -->
  <polygon points="60,20 88,36 88,68 60,84 32,68 32,36" fill="#1f1807" stroke="#f1df76" stroke-width="1.5"/>

  <!-- Golden Drafting Divider Compass -->
  <line x1="60" y1="26" x2="42" y2="76" stroke="#fef08a" stroke-width="3" stroke-linecap="round"/>
  <line x1="60" y1="26" x2="78" y2="76" stroke="#fef08a" stroke-width="3" stroke-linecap="round"/>
  <circle cx="60" cy="26" r="5" fill="#f1df76"/>
  <line x1="48" y1="56" x2="72" y2="56" stroke="#f1df76" stroke-width="1.8"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1f1807" stroke="#f1df76" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f1df76" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">HIGH ARCHITECTS</text>
</svg>""",

        # Master Weavers - Loom Shuttle & Iridescent Silk Threads
        "icon_faction_weavers.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#a855f7" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Loom Shuttle Silhouette -->
  <polygon points="28,52 60,38 92,52 60,66" fill="#2e1065" stroke="#a855f7" stroke-width="2"/>
  <circle cx="60" cy="52" r="5" fill="#f1df76"/>

  <!-- Shimmering Warp & Weft Threads -->
  <line x1="36" y1="24" x2="36" y2="80" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="48" y1="20" x2="48" y2="84" stroke="#a855f7" stroke-width="1.5"/>
  <line x1="60" y1="18" x2="60" y2="86" stroke="#e879f9" stroke-width="1.8"/>
  <line x1="72" y1="20" x2="72" y2="84" stroke="#a855f7" stroke-width="1.5"/>
  <line x1="84" y1="24" x2="84" y2="80" stroke="#38bdf8" stroke-width="1.5"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1e102f" stroke="#a855f7" stroke-width="1"/>
  <text x="60" y="108.5" fill="#e879f9" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">HAN WEAVERS</text>
</svg>""",

        # Bulwark Wardens - Fortified Gate Bastion & Halberds
        "icon_faction_wardens.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#10b981" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Fortified Gatehouse Bastion -->
  <polygon points="34,84 34,44 48,34 72,34 86,44 86,84" fill="#062e22" stroke="#10b981" stroke-width="2"/>
  <rect x="52" y="60" width="16" height="24" fill="#0f172a" stroke="#71efaf" stroke-width="1.5"/>

  <!-- Crossed Guard Halberds -->
  <line x1="22" y1="84" x2="98" y2="20" stroke="#71efaf" stroke-width="2"/>
  <line x1="98" y1="84" x2="22" y2="20" stroke="#71efaf" stroke-width="2"/>
  <polygon points="98,20 90,20 98,28" fill="#71efaf"/>
  <polygon points="22,20 30,20 22,28" fill="#71efaf"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#062e22" stroke="#10b981" stroke-width="1"/>
  <text x="60" y="108.5" fill="#34d399" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">BULWARK WARDENS</text>
</svg>""",

        # Relic Collectors - Mechanical Grasping Gauntlet & Crystal
        "icon_faction_collectors.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f59e0b" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Glowing Relic Crystal -->
  <polygon points="60,20 74,40 60,60 46,40" fill="#fef08a" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="60" cy="40" r="4" fill="#ffffff"/>

  <!-- Mechanical Grasping Claw Gauntlet -->
  <path d="M 32 64 Q 46 54 60 70 Q 74 54 88 64 L 82 86 L 38 86 Z" fill="#292524" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="60" cy="78" r="3" fill="#ef4444"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#241403" stroke="#f59e0b" stroke-width="1"/>
  <text x="60" y="108.5" fill="#fbbf24" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">RELIC COLLECTORS</text>
</svg>""",

        # Horizon Caravan - Armored Desert Crawler Truck
        "icon_faction_horizon_caravan.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#d97706" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Armored Crawler Body & Cab -->
  <polygon points="24,68 34,44 76,44 96,60 96,72 24,72" fill="#291b05" stroke="#f59e0b" stroke-width="1.8"/>
  <rect x="42" y="50" width="16" height="10" fill="#070a12" stroke="#fbbf24" stroke-width="1"/>
  <polygon points="74,50 86,60 74,60" fill="#070a12" stroke="#fbbf24" stroke-width="1"/>

  <!-- Heavy Off-Road Tread Wheels -->
  <circle cx="36" cy="74" r="8" fill="#1c1917" stroke="#d97706" stroke-width="2"/>
  <circle cx="58" cy="74" r="8" fill="#1c1917" stroke="#d97706" stroke-width="2"/>
  <circle cx="80" cy="74" r="8" fill="#1c1917" stroke="#d97706" stroke-width="2"/>

  <!-- Expedition Mast & Banner -->
  <line x1="38" y1="44" x2="38" y2="20" stroke="#f59e0b" stroke-width="1.8"/>
  <polygon points="38,20 62,28 38,36" fill="#ef4444"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#241403" stroke="#d97706" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f59e0b" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">HORIZON CARAVAN</text>
</svg>""",

        # Memory Washers - Amnestic Mirror Slate & Psychic Waves
        "icon_faction_memory_washers.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="mwGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#mwGlow)"/>

  <!-- Blank Amnestic Mirror Slate -->
  <polygon points="60,18 84,36 84,68 60,86 36,68 36,36" fill="#0f172a" stroke="#e0f2fe" stroke-width="2"/>

  <!-- Concentric Psychic Amnesia Waves -->
  <circle cx="60" cy="52" r="20" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="60" cy="52" r="12" fill="none" stroke="#7dd3fc" stroke-width="1.8"/>
  <circle cx="60" cy="52" r="4" fill="#ffffff"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0c192c" stroke="#38bdf8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#38bdf8" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">MEMORY WASHERS</text>
</svg>""",

        # Giltong Enforcers - Ceremonial Golden Mask & Dual Submachine Guns
        "icon_faction_giltong_enforcers.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Golden Ceremonial Noh Mask -->
  <path d="M 40 28 Q 60 18 80 28 Q 86 64 60 82 Q 34 64 40 28 Z" fill="#1f1807" stroke="#f1df76" stroke-width="2"/>
  
  <!-- Slit Mask Eyes -->
  <line x1="46" y1="44" x2="56" y2="44" stroke="#ef5b55" stroke-width="2"/>
  <line x1="64" y1="44" x2="74" y2="44" stroke="#ef5b55" stroke-width="2"/>
  <polygon points="60,54 63,60 57,60" fill="#f1df76"/>
  <line x1="52" y1="68" x2="68" y2="68" stroke="#f1df76" stroke-width="1.5"/>

  <!-- Dual Silenced Submachine Guns -->
  <line x1="22" y1="84" x2="44" y2="62" stroke="#f1df76" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="98" y1="84" x2="76" y2="62" stroke="#f1df76" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1f1807" stroke="#f1df76" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f1df76" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">GILTONG ENFORCERS</text>
</svg>""",

        # Founding Corps - Heavy Cogwheel & Miner's Pickaxe
        "icon_faction_founding_corps.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#94a3b8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Heavy Steel Industrial Cogwheel -->
  <circle cx="60" cy="50" r="28" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="60" cy="50" r="16" fill="#070a12" stroke="#cbd5e1" stroke-width="1.8"/>
  <circle cx="60" cy="50" r="6" fill="#f1df76"/>

  <!-- Crossed Miner's Pickaxes -->
  <line x1="26" y1="80" x2="94" y2="20" stroke="#f1df76" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="94" y1="80" x2="26" y2="20" stroke="#f1df76" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 86 16 Q 94 20 98 28" stroke="#cbd5e1" stroke-width="3" fill="none"/>
  <path d="M 34 16 Q 26 20 22 28" stroke="#cbd5e1" stroke-width="3" fill="none"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1e293b" stroke="#94a3b8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#cbd5e1" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">FOUNDING CORPS</text>
</svg>""",

        # Underworld Syndicates - Shadow Dagger & Poison Cyan Han
        "icon_faction_underworld.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="undGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#06b6d4" stop-opacity="0.7"/>
      <stop offset="60%" stop-color="#3b0764" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#06b6d4" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#undGlow)"/>

  <!-- Shadow Alley Archway -->
  <path d="M 32 86 L 32 44 Q 60 20 88 44 L 88 86 Z" fill="#0f091c" stroke="#a855f7" stroke-width="1.8"/>

  <!-- Concealed Shadow Stiletto Dagger -->
  <polygon points="60,24 65,54 62,82 58,82 55,54" fill="#064e3b" stroke="#22d3ee" stroke-width="1.5"/>
  <!-- Dripping Cyan Han Poison Drop -->
  <circle cx="60" cy="88" r="3" fill="#22d3ee"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0f091c" stroke="#06b6d4" stroke-width="1"/>
  <text x="60" y="108.5" fill="#22d3ee" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">UNDERWORLD</text>
</svg>""",

        # Directorate Faction Technology - Circuit Core & Biomechanical Han Cell
        "icon_faction_technology.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="techGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#techGlow)"/>

  <!-- Central Microchip Processor -->
  <rect x="44" y="34" width="32" height="32" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="60" cy="50" r="8" fill="#0284c7" stroke="#f1df76" stroke-width="1.5"/>

  <!-- Radiating Printed Circuit Traces -->
  <line x1="44" y1="42" x2="24" y2="42" stroke="#38bdf8" stroke-width="1.8"/>
  <circle cx="24" cy="42" r="2.5" fill="#f1df76"/>

  <line x1="44" y1="58" x2="24" y2="58" stroke="#38bdf8" stroke-width="1.8"/>
  <circle cx="24" cy="58" r="2.5" fill="#f1df76"/>

  <line x1="76" y1="42" x2="96" y2="42" stroke="#38bdf8" stroke-width="1.8"/>
  <circle cx="96" cy="42" r="2.5" fill="#f1df76"/>

  <line x1="76" y1="58" x2="96" y2="58" stroke="#38bdf8" stroke-width="1.8"/>
  <circle cx="96" cy="58" r="2.5" fill="#f1df76"/>

  <line x1="52" y1="34" x2="52" y2="18" stroke="#38bdf8" stroke-width="1.8"/>
  <circle cx="52" cy="18" r="2.5" fill="#f1df76"/>

  <line x1="68" y1="34" x2="68" y2="18" stroke="#38bdf8" stroke-width="1.8"/>
  <circle cx="68" cy="18" r="2.5" fill="#f1df76"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0c192c" stroke="#38bdf8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#38bdf8" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">FACTION TECH</text>
</svg>"""
    }

def main():
    zones = get_zone_and_city_icons()
    for name, svg in zones.items():
        p1 = os.path.join(WIKI_ASSETS_CITY, name)
        p2 = os.path.join(WIKI_ASSETS_ICONS, name)
        p3 = os.path.join(WORKSPACE_ICONS, name)
        for p in [p1, p2, p3]:
            with open(p, "w", encoding="utf-8") as f:
                f.write(svg)
        print(f"Generated Zone/City Icon: {name}")

    factions = get_faction_icons()
    for name, svg in factions.items():
        p1 = os.path.join(WIKI_ASSETS_ICONS, name)
        p2 = os.path.join(WORKSPACE_ICONS, name)
        for p in [p1, p2]:
            with open(p, "w", encoding="utf-8") as f:
                f.write(svg)
        print(f"Generated Faction Icon: {name}")

if __name__ == "__main__":
    main()
