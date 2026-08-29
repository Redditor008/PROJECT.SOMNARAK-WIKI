#!/usr/bin/env python3
"""
tools/build_all_super_banners.py
Generates masterwork vector SVG banners for:
1. All 8 Panoramic Hero Banners (1200x320)
2. All 8 Floor Mini-Banners (340x85)
3. All 18 Category & Theme Banners (120x120)
With 100% pure canonical Somnarak styling, 5 canonical colors,
proper 4-8px insets, non-clipping typography, and rich vector illustrations.
"""

import os

WIKI_DIR = "/home/user/01_Somnarak_Wiki"
BANNERS_DIR = os.path.join(WIKI_DIR, "assets/banners")
ASSETS_ICONS = os.path.join(WIKI_DIR, "assets/icons")
ICONS_DIR = "/home/user/icons"

for d in [BANNERS_DIR, ASSETS_ICONS, ICONS_DIR]:
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
# 1. PANORAMIC HERO BANNERS (1200 x 320)
# ==============================================================================

# 1.1 Facility 01: The Hand of Change (Departments Hub)
HERO_HAND = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="100%">
  <defs>
    <linearGradient id="handBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a121e"/>
      <stop offset="50%" stop-color="#04070d"/>
      <stop offset="100%" stop-color="#0a0507"/>
    </linearGradient>
    <linearGradient id="goldBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f1df76"/>
      <stop offset="50%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="handGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Inset Outer Frame -->
  <rect x="4" y="4" width="1192" height="312" rx="8" fill="url(#handBg)" stroke="#1e293b" stroke-width="2"/>
  <rect x="8" y="8" width="1184" height="304" rx="6" fill="none" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1" stroke-dasharray="8 4"/>

  <!-- Top Tactical Status Bar -->
  <rect x="12" y="12" width="1176" height="26" rx="3" fill="#080e18" stroke="#223854" stroke-width="1"/>
  <text x="24" y="29" fill="#38bdf8" font-family="monospace" font-size="11" font-weight="bold">/// REVERIE DIRECTORATE // FACILITY 01 SUBTERRANEAN SYSTEM</text>
  <text x="1164" y="29" fill="#f1df76" font-family="monospace" font-size="11" font-weight="bold" text-anchor="end">CLEARANCE: LEVEL 5 RESTRICTED // DEPTH: -2,000M</text>

  <!-- Left: Schematic Diagram of The Hand Architecture -->
  <g transform="translate(40, 50)">
    <!-- Alpha Tree Surface Spire -->
    <polygon points="120,4 140,4 135,16 125,16" fill="#38bdf8" stroke="#f1df76" stroke-width="1.2"/>
    <line x1="130" y1="16" x2="130" y2="30" stroke="#38bdf8" stroke-width="2"/>
    <!-- Palm Core (F1, F2, F3) -->
    <rect x="80" y="30" width="100" height="22" rx="3" fill="#78350f" stroke="#f1df76" stroke-width="1.5"/>
    <text x="130" y="45" fill="#fff" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">F1 NEUTRAL COMMAND</text>

    <rect x="75" y="58" width="110" height="22" rx="3" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.5"/>
    <text x="130" y="73" fill="#fff" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">F2 MAW'S KEEP</text>

    <rect x="85" y="86" width="90" height="22" rx="3" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="130" y="101" fill="#fff" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">F3 EXTRACTION</text>

    <!-- Elevator Conduit -->
    <line x1="130" y1="108" x2="130" y2="124" stroke="#38bdf8" stroke-width="3"/>
    <line x1="40" y1="124" x2="220" y2="124" stroke="#38bdf8" stroke-width="2"/>

    <!-- 4 Finger Vaults -->
    <rect x="30" y="130" width="40" height="70" rx="3" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="50" y="168" fill="#a7f3d0" font-family="monospace" font-size="8" font-weight="bold" text-anchor="middle">F4 INSIGHT</text>

    <rect x="78" y="130" width="40" height="85" rx="3" fill="#0c4a6e" stroke="#0284c7" stroke-width="1.5"/>
    <text x="98" y="176" fill="#bae6fd" font-family="monospace" font-size="8" font-weight="bold" text-anchor="middle">F5 BORDER</text>

    <rect x="142" y="130" width="40" height="85" rx="3" fill="#3b0764" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="162" y="176" fill="#e9d5ff" font-family="monospace" font-size="8" font-weight="bold" text-anchor="middle">F6 VAULT</text>

    <rect x="190" y="130" width="40" height="70" rx="3" fill="#4c0519" stroke="#e11d48" stroke-width="1.5"/>
    <text x="210" y="168" fill="#fecaca" font-family="monospace" font-size="8" font-weight="bold" text-anchor="middle">F7 SHADOW</text>

    <!-- F8 Outpost -->
    <rect x="200" y="58" width="45" height="22" rx="3" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="222" y="73" fill="#fff" font-family="monospace" font-size="8" font-weight="bold" text-anchor="middle">F8 GATE</text>
    <line x1="185" y1="69" x2="200" y2="69" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3 2"/>
  </g>

  <!-- Center-Right: Grand Title & Sector Overview -->
  <g transform="translate(360, 60)">
    <rect x="0" y="0" width="800" height="230" rx="6" fill="rgba(8, 14, 24, 0.75)" stroke="#223854" stroke-width="1.5"/>
    <rect x="0" y="0" width="800" height="4" fill="url(#goldBar)"/>
    
    <text x="28" y="44" fill="#f1df76" font-family="Impact, sans-serif" font-size="34" letter-spacing="3">THE HAND OF CHANGE</text>
    <text x="28" y="70" fill="#38bdf8" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="1">FACILITY 01 SUBTERRANEAN HEADQUARTERS // ALL 8 SECTORS</text>

    <line x1="28" y1="84" x2="772" y2="84" stroke="#1e293b" stroke-width="1.5"/>

    <!-- Sector Quick Matrix -->
    <g transform="translate(28, 102)" font-family="monospace" font-size="11">
      <!-- Row 1 -->
      <text x="0" y="0" fill="#ef5b55" font-weight="bold">[F1] NEUTRAL COMMAND</text>
      <text x="0" y="16" fill="#94a3b8">Director Majin · Palm Core</text>

      <text x="200" y="0" fill="#38bdf8" font-weight="bold">[F2] MAW'S KEEP</text>
      <text x="200" y="16" fill="#94a3b8">Dekan · Kinetic Containment</text>

      <text x="400" y="0" fill="#f59e0b" font-weight="bold">[F3] EXTRACTION HALL</text>
      <text x="400" y="16" fill="#94a3b8">Zyrak · M.A.W. Siphon Forge</text>

      <text x="600" y="0" fill="#10b981" font-weight="bold">[F4] INSIGHT FORGE</text>
      <text x="600" y="16" fill="#94a3b8">Ayshuk · Metaphysical R&amp;D</text>

      <!-- Row 2 -->
      <text x="0" y="60" fill="#0284c7" font-weight="bold">[F5] BORDER WATCH</text>
      <text x="0" y="76" fill="#94a3b8">Mellda · Bastion Defense</text>

      <text x="200" y="60" fill="#8b5cf6" font-weight="bold">[F6] DEEP VAULT</text>
      <text x="200" y="76" fill="#94a3b8">Marjuk · Cryo Seal &amp; Archive</text>

      <text x="400" y="60" fill="#e11d48" font-weight="bold">[F7] SHADOW CORPS</text>
      <text x="400" y="76" fill="#94a3b8">Ishall · Abyssal Void Divers</text>

      <text x="600" y="60" fill="#94a3b8" font-weight="bold">[F8] GATE WATCH</text>
      <text x="600" y="76" fill="#94a3b8">Xyan · Taboo Boundary Vigil</text>
    </g>
  </g>

  <!-- Bottom Coordinates & Integrity Bar -->
  <rect x="12" y="286" width="1176" height="22" rx="2" fill="#05080e" stroke="#1e293b" stroke-width="1"/>
  <text x="24" y="301" fill="#64748b" font-family="monospace" font-size="10">COHERENCE STABILITY: 99.4% NOMINAL | FACILITY STATUS: GREEN | TABOO RESTRAINT: ACTIVE</text>
  <text x="1164" y="301" fill="#f1df76" font-family="monospace" font-size="10" text-anchor="end">AUTONOMOUS CONTAINMENT PROTOCOL // THE DAWN INITIATIVE</text>
</svg>"""

# 1.2 Somnarak City Master Cartography (Locations Hub)
HERO_CITY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="100%">
  <defs>
    <linearGradient id="cityBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#140924"/>
      <stop offset="50%" stop-color="#070410"/>
      <stop offset="100%" stop-color="#091426"/>
    </linearGradient>
    <linearGradient id="cityPurple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#f1df76"/>
    </linearGradient>
  </defs>

  <rect x="4" y="4" width="1192" height="312" rx="8" fill="url(#cityBg)" stroke="#2e1065" stroke-width="2"/>
  <rect x="8" y="8" width="1184" height="304" rx="6" fill="none" stroke="rgba(168, 85, 247, 0.2)" stroke-width="1" stroke-dasharray="8 4"/>

  <!-- Top Bar -->
  <rect x="12" y="12" width="1176" height="26" rx="3" fill="#0a0516" stroke="#3b0764" stroke-width="1"/>
  <text x="24" y="29" fill="#c084fc" font-family="monospace" font-size="11" font-weight="bold">/// CARTOGRAPHY ARCHIVE // SOMNARAK METROPOLITAN ATLAS</text>
  <text x="1164" y="29" fill="#f1df76" font-family="monospace" font-size="11" font-weight="bold" text-anchor="end">GRID: 5 DIAMOND ZONES + SUBTERRANEAN CANALS + WASTELAND</text>

  <!-- Left: City Diamond Cartography Schematic -->
  <g transform="translate(40, 50)">
    <!-- Outer Diamond City Wall -->
    <polygon points="130,10 240,115 130,220 20,115" fill="#090514" stroke="#a855f7" stroke-width="2.5"/>
    <!-- Concentric Zone Rings -->
    <circle cx="130" cy="115" r="75" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6 3"/>
    <circle cx="130" cy="115" r="45" fill="#1e1038" stroke="#f1df76" stroke-width="2"/>
    <!-- Alpha Tree Center Spire -->
    <polygon points="130,85 145,125 115,125" fill="#f1df76" stroke="#fff" stroke-width="1"/>
    <circle cx="130" cy="115" r="8" fill="#ef4444"/>
    <text x="130" y="145" fill="#f1df76" font-family="monospace" font-size="8" font-weight="bold" text-anchor="middle">ZONE A: CORE</text>
    <!-- Zone Labels -->
    <text x="45" y="118" fill="#38bdf8" font-family="monospace" font-size="7" font-weight="bold">ZONE B</text>
    <text x="195" y="118" fill="#ef4444" font-family="monospace" font-size="7" font-weight="bold">ZONE C</text>
    <text x="130" y="35" fill="#10b981" font-family="monospace" font-size="7" font-weight="bold" text-anchor="middle">ZONE D</text>
    <text x="130" y="200" fill="#a855f7" font-family="monospace" font-size="7" font-weight="bold" text-anchor="middle">ZONE E</text>
  </g>

  <!-- Center-Right: Title & Zone Details -->
  <g transform="translate(360, 60)">
    <rect x="0" y="0" width="800" height="230" rx="6" fill="rgba(10, 5, 20, 0.75)" stroke="#3b0764" stroke-width="1.5"/>
    <rect x="0" y="0" width="800" height="4" fill="url(#cityPurple)"/>

    <text x="28" y="44" fill="#f1df76" font-family="Impact, sans-serif" font-size="34" letter-spacing="3">SOMNARAK CITY METROPOLIS</text>
    <text x="28" y="70" fill="#a855f7" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="1">PLANETARY CAPITAL OF MUGENHAN // 5 CONCENTRIC SECTORS</text>

    <line x1="28" y1="84" x2="772" y2="84" stroke="#2e1065" stroke-width="1.5"/>

    <g transform="translate(28, 102)" font-family="monospace" font-size="11">
      <text x="0" y="0" fill="#f1df76" font-weight="bold">[ZONE A] THE ALPHA CORE</text>
      <text x="0" y="16" fill="#cbd5e1">The Alpha Tree &amp; High Council of Seven</text>

      <text x="260" y="0" fill="#38bdf8" font-weight="bold">[ZONE B] WEST METROPOLIS</text>
      <text x="260" y="16" fill="#cbd5e1">The Maw &amp; Civilian Residential Wards</text>

      <text x="520" y="0" fill="#ef4444" font-weight="bold">[ZONE C] EAST INDUSTRIAL</text>
      <text x="520" y="16" fill="#cbd5e1">Collector's Row &amp; Han Relic Bazaars</text>

      <text x="0" y="60" fill="#10b981" font-weight="bold">[ZONE D] NORTH COMMERCE</text>
      <text x="0" y="76" fill="#cbd5e1">Weavers Syndicate &amp; Trade Flanks</text>

      <text x="260" y="60" fill="#a855f7" font-weight="bold">[ZONE E] OUTER BULWARK</text>
      <text x="260" y="76" fill="#cbd5e1">Fortress Wall &amp; Perimeter Bastions</text>

      <text x="520" y="60" fill="#d97706" font-weight="bold">[THE DESOLATE] FRONTIER</text>
      <text x="520" y="76" fill="#cbd5e1">Cheonbulok, Raw Han &amp; Mugeukji Wasteland</text>
    </g>
  </g>

  <!-- Bottom Status -->
  <rect x="12" y="286" width="1176" height="22" rx="2" fill="#06030c" stroke="#2e1065" stroke-width="1"/>
  <text x="24" y="301" fill="#94a3b8" font-family="monospace" font-size="10">VEIL EMISSION: 100% SECURE | EXTERIOR PRESSURE: CRITICAL | HORIZON ROUTE: OPEN</text>
  <text x="1164" y="301" fill="#a855f7" font-family="monospace" font-size="10" text-anchor="end">CARTOGRAPHIC MASTER ARCHIVE // REVERIE SURVEY DIVISION</text>
</svg>"""

# 1.3 Sorrow Entities Containment Codex (Entities Hub)
HERO_ENTITIES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="100%">
  <defs>
    <linearGradient id="entBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#180407"/>
      <stop offset="50%" stop-color="#080812"/>
      <stop offset="100%" stop-color="#180407"/>
    </linearGradient>
    <linearGradient id="entCrimson" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="50%" stop-color="#f1df76"/>
      <stop offset="100%" stop-color="#ef4444"/>
    </linearGradient>
  </defs>

  <rect x="4" y="4" width="1192" height="312" rx="8" fill="url(#entBg)" stroke="#7f1d1d" stroke-width="2"/>
  <rect x="8" y="8" width="1184" height="304" rx="6" fill="none" stroke="rgba(239, 68, 68, 0.25)" stroke-width="1" stroke-dasharray="8 4"/>

  <!-- Top Status -->
  <rect x="12" y="12" width="1176" height="26" rx="3" fill="#140306" stroke="#450a0a" stroke-width="1"/>
  <text x="24" y="29" fill="#ef4444" font-family="monospace" font-size="11" font-weight="bold">/// SECC CODEX // SORROW ENTITY CONTAINMENT CLASSIFICATION</text>
  <text x="1164" y="29" fill="#f1df76" font-family="monospace" font-size="11" font-weight="bold" text-anchor="end">CATALOGED: 246 PHENOMENA // 10 CANONICAL FOCAL ENTITIES</text>

  <!-- Left: Threat Matrix Badges -->
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="280" height="230" rx="6" fill="rgba(20, 4, 8, 0.85)" stroke="#7f1d1d" stroke-width="1.5"/>
    <text x="140" y="30" fill="#f1df76" font-family="Impact" font-size="16" letter-spacing="2" text-anchor="middle">SECC THREAT HIERARCHY</text>
    
    <!-- 5 Risk Badges -->
    <g transform="translate(18, 48)" font-family="Impact" font-size="12">
      <rect x="0" y="0" width="44" height="30" rx="3" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
      <text x="22" y="20" fill="#fff" text-anchor="middle">CAN</text>
      <text x="56" y="20" fill="#10b981" font-family="monospace" font-size="10">T-01 // Minimal Threat</text>

      <rect x="0" y="36" width="44" height="30" rx="3" fill="#0c4a6e" stroke="#0284c7" stroke-width="1.5"/>
      <text x="22" y="56" fill="#fff" text-anchor="middle">TETH</text>
      <text x="56" y="56" fill="#38bdf8" font-family="monospace" font-size="10">T-02 // Moderate Grief</text>

      <rect x="0" y="72" width="44" height="30" rx="3" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="22" y="92" fill="#fff" text-anchor="middle">HE</text>
      <text x="56" y="92" fill="#f1df76" font-family="monospace" font-size="10">T-03 // High Volatility</text>

      <rect x="0" y="108" width="44" height="30" rx="3" fill="#3b0764" stroke="#8b5cf6" stroke-width="1.5"/>
      <text x="22" y="128" fill="#fff" text-anchor="middle">WAW</text>
      <text x="56" y="128" fill="#c084fc" font-family="monospace" font-size="10">T-04 // Severe Hazard</text>

      <rect x="0" y="144" width="44" height="30" rx="3" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.5"/>
      <text x="22" y="164" fill="#fff" text-anchor="middle">ALEPH</text>
      <text x="56" y="164" fill="#ef4444" font-family="monospace" font-size="10">T-05 // Cataclysmic</text>
    </g>
  </g>

  <!-- Right: Title & Focal Manifestations -->
  <g transform="translate(360, 60)">
    <rect x="0" y="0" width="800" height="230" rx="6" fill="rgba(20, 4, 8, 0.75)" stroke="#7f1d1d" stroke-width="1.5"/>
    <rect x="0" y="0" width="800" height="4" fill="url(#entCrimson)"/>

    <text x="28" y="44" fill="#f1df76" font-family="Impact, sans-serif" font-size="34" letter-spacing="3">SORROW ENTITIES CODEX</text>
    <text x="28" y="70" fill="#ef4444" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="1">MANIFESTATIONS OF PLANETARY AGONY // SE-001 TO SE-015</text>

    <line x1="28" y1="84" x2="772" y2="84" stroke="#450a0a" stroke-width="1.5"/>

    <g transform="translate(28, 102)" font-family="monospace" font-size="11">
      <text x="0" y="0" fill="#10b981" font-weight="bold">SE-001 THE ORPHANED BELL</text>
      <text x="0" y="16" fill="#94a3b8">T-01 CAN · Resonant Iron Grief</text>

      <text x="260" y="0" fill="#f59e0b" font-weight="bold">SE-002 GRIEVING COLOSSUS</text>
      <text x="260" y="16" fill="#94a3b8">T-03 HE · Weeping Molten Core</text>

      <text x="520" y="0" fill="#c084fc" font-weight="bold">SE-003 WILDERNESS TIDE</text>
      <text x="520" y="16" fill="#94a3b8">T-04 WAW · Deluge of Agony</text>

      <text x="0" y="60" fill="#38bdf8" font-weight="bold">SE-005 SMOTHERING MOTHER</text>
      <text x="0" y="76" fill="#94a3b8">T-02 TETH · Protective Shroud</text>

      <text x="260" y="60" fill="#c084fc" font-weight="bold">SE-009 MEMORY WEAVER</text>
      <text x="260" y="76" fill="#94a3b8">T-04 WAW · Silk Loom of Pasts</text>

      <text x="520" y="60" fill="#ef4444" font-weight="bold">SE-010 THE CONVERGENCE</text>
      <text x="520" y="76" fill="#94a3b8">T-05 ALEPH · Gravitational Event</text>
    </g>
  </g>

  <!-- Bottom -->
  <rect x="12" y="286" width="1176" height="22" rx="2" fill="#080203" stroke="#450a0a" stroke-width="1"/>
  <text x="24" y="301" fill="#64748b" font-family="monospace" font-size="10">CONTAINMENT PROTOCOL: COHERENCE FLUX &gt; LEVEL 3 REQUIRED | BREACH HAZARD: CRITICAL</text>
  <text x="1164" y="301" fill="#ef4444" font-family="monospace" font-size="10" text-anchor="end">PERMANENT OBSERVATION MANDATE // REVERIE CONTAINMENT DIVISION</text>
</svg>"""

# 1.4 M.A.W. Equipment Arsenal (M.A.W. Hub)
HERO_MAW = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="100%">
  <defs>
    <linearGradient id="mawBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1204"/>
      <stop offset="50%" stop-color="#080a14"/>
      <stop offset="100%" stop-color="#1e1204"/>
    </linearGradient>
    <linearGradient id="mawGold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#f1df76"/>
    </linearGradient>
  </defs>

  <rect x="4" y="4" width="1192" height="312" rx="8" fill="url(#mawBg)" stroke="#78350f" stroke-width="2"/>
  <rect x="8" y="8" width="1184" height="304" rx="6" fill="none" stroke="rgba(245, 158, 11, 0.25)" stroke-width="1" stroke-dasharray="8 4"/>

  <rect x="12" y="12" width="1176" height="26" rx="3" fill="#140b02" stroke="#451a03" stroke-width="1"/>
  <text x="24" y="29" fill="#f59e0b" font-family="monospace" font-size="11" font-weight="bold">/// M.A.W. ARSENAL // MOURNING AGONY WEAPONRY &amp; WEAVE</text>
  <text x="1164" y="29" fill="#38bdf8" font-family="monospace" font-size="11" font-weight="bold" text-anchor="end">FORGED FROM ENTITY SORROW RESISTANCE // WEAPON · SUIT · GIFT</text>

  <!-- Left: Triad Equipment Graphic -->
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="280" height="230" rx="6" fill="rgba(20, 12, 4, 0.85)" stroke="#78350f" stroke-width="1.5"/>
    <text x="140" y="30" fill="#f1df76" font-family="Impact" font-size="16" letter-spacing="2" text-anchor="middle">M.A.W. EQUIPMENT TRIAD</text>

    <!-- Triad Elements -->
    <g transform="translate(20, 50)">
      <!-- Weapon -->
      <rect x="0" y="0" width="240" height="46" rx="4" fill="#091220" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="16" y="22" fill="#38bdf8" font-family="Impact" font-size="14">WEAPON [W]</text>
      <text x="16" y="38" fill="#94a3b8" font-family="monospace" font-size="10">Kinetic / Pale / Corrosive Offense</text>

      <!-- Suit -->
      <rect x="0" y="56" width="240" height="46" rx="4" fill="#180a10" stroke="#ef4444" stroke-width="1.5"/>
      <text x="16" y="78" fill="#ef4444" font-family="Impact" font-size="14">SUIT [S]</text>
      <text x="16" y="94" fill="#94a3b8" font-family="monospace" font-size="10">Defensive Agony Dispersion Weave</text>

      <!-- Gift -->
      <rect x="0" y="112" width="240" height="46" rx="4" fill="#181404" stroke="#f1df76" stroke-width="1.5"/>
      <text x="16" y="134" fill="#f1df76" font-family="Impact" font-size="14">GIFT [G]</text>
      <text x="16" y="150" fill="#94a3b8" font-family="monospace" font-size="10">Metaphysical Resonance Relic</text>
    </g>
  </g>

  <!-- Right: Grand Title & Sets -->
  <g transform="translate(360, 60)">
    <rect x="0" y="0" width="800" height="230" rx="6" fill="rgba(20, 12, 4, 0.75)" stroke="#78350f" stroke-width="1.5"/>
    <rect x="0" y="0" width="800" height="4" fill="url(#mawGold)"/>

    <text x="28" y="44" fill="#f1df76" font-family="Impact, sans-serif" font-size="34" letter-spacing="3">M.A.W. ARSENAL &amp; EQUIPMENT</text>
    <text x="28" y="70" fill="#f59e0b" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="1">FLOOR 3 EXTRACTION FORGE // 9 CANONICAL SETS // 27 PIECES</text>

    <line x1="28" y1="84" x2="772" y2="84" stroke="#451a03" stroke-width="1.5"/>

    <g transform="translate(28, 102)" font-family="monospace" font-size="11">
      <text x="0" y="0" fill="#38bdf8" font-weight="bold">SET 001: LAMENT'S REQUIEM</text>
      <text x="0" y="16" fill="#cbd5e1">SE-001 · Pale Han Cleaver</text>

      <text x="260" y="0" fill="#ef4444" font-weight="bold">SET 002: MOURNING MAUL</text>
      <text x="260" y="16" fill="#cbd5e1">SE-002 · Heavy Kinetic Impact</text>

      <text x="520" y="0" fill="#10b981" font-weight="bold">SET 005: THE EMBRACE</text>
      <text x="520" y="16" fill="#cbd5e1">SE-005 · Maternal Shroud Barrier</text>

      <text x="0" y="60" fill="#f8fafc" font-weight="bold">SET 007: HOPE LANTERN</text>
      <text x="0" y="76" fill="#cbd5e1">SE-007 · Pure Luminous Beam</text>

      <text x="260" y="60" fill="#c084fc" font-weight="bold">SET 009: FORGOTTEN MASK</text>
      <text x="260" y="76" fill="#cbd5e1">SE-009 · Psychic Thread Lens</text>

      <text x="520" y="60" fill="#f1df76" font-weight="bold">SET 015: BALANCE SCALE</text>
      <text x="520" y="76" fill="#cbd5e1">SE-015 · Karmic Verdict Gavel</text>
    </g>
  </g>

  <!-- Bottom -->
  <rect x="12" y="286" width="1176" height="22" rx="2" fill="#0a0502" stroke="#451a03" stroke-width="1"/>
  <text x="24" y="301" fill="#64748b" font-family="monospace" font-size="10">SIPHON FORGE CAPACITY: MAXIMUM | EXTRACTION PURITY: 99.8% | WEAPON INTEGRITY: PRIME</text>
  <text x="1164" y="301" fill="#f1df76" font-family="monospace" font-size="10" text-anchor="end">MANUFACTURING DIVISION // FLOOR 3 EXTRACTION HALL</text>
</svg>"""

# 1.5 The Nine Echo-Cores & Cast (Characters Hub)
HERO_CORES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="100%">
  <defs>
    <linearGradient id="coresBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141004"/>
      <stop offset="50%" stop-color="#080e18"/>
      <stop offset="100%" stop-color="#140804"/>
    </linearGradient>
  </defs>

  <rect x="4" y="4" width="1192" height="312" rx="8" fill="url(#coresBg)" stroke="#78350f" stroke-width="2"/>
  <rect x="8" y="8" width="1184" height="304" rx="6" fill="none" stroke="rgba(241, 223, 118, 0.25)" stroke-width="1" stroke-dasharray="8 4"/>

  <rect x="12" y="12" width="1176" height="26" rx="3" fill="#0d0902" stroke="#451a03" stroke-width="1"/>
  <text x="24" y="29" fill="#f1df76" font-family="monospace" font-size="11" font-weight="bold">/// PERSONNEL DIRECTORY // THE NINE ECHO-CORES &amp; EXECUTIVE ROSTER</text>
  <text x="1164" y="29" fill="#38bdf8" font-family="monospace" font-size="11" font-weight="bold" text-anchor="end">RESONANCE SYNC: 9 LEADS // 1,778 CYCLES OF COGNITIVE CONTINUITY</text>

  <!-- Left: Command Avatars Graphic -->
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="280" height="230" rx="6" fill="rgba(16, 12, 4, 0.85)" stroke="#78350f" stroke-width="1.5"/>
    <text x="140" y="30" fill="#f1df76" font-family="Impact" font-size="16" letter-spacing="2" text-anchor="middle">EXECUTIVE COMMAND</text>
    
    <g transform="translate(30, 50)">
      <!-- Majin Avatar -->
      <circle cx="50" cy="50" r="36" fill="#78350f" stroke="#f1df76" stroke-width="2.5"/>
      <text x="50" y="56" fill="#fff" font-family="Impact" font-size="14" text-anchor="middle">MAJIN</text>
      <text x="50" y="102" fill="#f1df76" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">THE DIRECTOR</text>

      <!-- Seiyon Avatar -->
      <circle cx="170" cy="50" r="36" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="170" y="56" fill="#fff" font-family="Impact" font-size="14" text-anchor="middle">SEIYON</text>
      <text x="170" y="102" fill="#38bdf8" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">THE SECRETARY</text>

      <text x="110" y="136" fill="#94a3b8" font-family="monospace" font-size="9" text-anchor="middle">+ 7 DEPARTMENT LEADS</text>
    </g>
  </g>

  <!-- Right: Roster Grid -->
  <g transform="translate(360, 60)">
    <rect x="0" y="0" width="800" height="230" rx="6" fill="rgba(16, 12, 4, 0.75)" stroke="#78350f" stroke-width="1.5"/>
    <rect x="0" y="0" width="800" height="4" fill="#f1df76"/>

    <text x="28" y="44" fill="#f1df76" font-family="Impact, sans-serif" font-size="34" letter-spacing="3">PERSONNEL &amp; ECHO-CORES</text>
    <text x="28" y="70" fill="#38bdf8" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="1">THE NINE ANCHORS OF FACILITY 01 &amp; THE DAWN INITIATIVE</text>

    <line x1="28" y1="84" x2="772" y2="84" stroke="#451a03" stroke-width="1.5"/>

    <g transform="translate(28, 102)" font-family="monospace" font-size="11">
      <text x="0" y="0" fill="#ef4444" font-weight="bold">CORE 3: DEKAN</text>
      <text x="0" y="16" fill="#cbd5e1">Floor 2 · Containment Lead</text>

      <text x="260" y="0" fill="#f59e0b" font-weight="bold">CORE 4: ZYRAK</text>
      <text x="260" y="16" fill="#cbd5e1">Floor 3 · Extraction Lead</text>

      <text x="520" y="0" fill="#10b981" font-weight="bold">CORE 5: AYSHUK</text>
      <text x="520" y="16" fill="#cbd5e1">Floor 4 · Research Lead</text>

      <text x="0" y="60" fill="#0284c7" font-weight="bold">CORE 6: MELLDA</text>
      <text x="0" y="76" fill="#cbd5e1">Floor 5 · Border Lead</text>

      <text x="260" y="60" fill="#8b5cf6" font-weight="bold">CORE 7: MARJUK</text>
      <text x="260" y="76" fill="#cbd5e1">Floor 6 · Archive Lead</text>

      <text x="520" y="60" fill="#e11d48" font-weight="bold">CORE 8: ISHALL &amp; CORE 9: XYAN</text>
      <text x="520" y="76" fill="#cbd5e1">Floors 7 &amp; 8 · Void &amp; Gate Watch</text>
    </g>
  </g>

  <!-- Bottom -->
  <rect x="12" y="286" width="1176" height="22" rx="2" fill="#080602" stroke="#451a03" stroke-width="1"/>
  <text x="24" y="301" fill="#64748b" font-family="monospace" font-size="10">NEURAL STABILITY: NOMINAL | PSYCHIC LOAD: 98.2% | TOTAL SYNCHRONIZATION CYCLES: 1,778</text>
  <text x="1164" y="301" fill="#f1df76" font-family="monospace" font-size="10" text-anchor="end">EXECUTIVE DOSSIERS // THE REVERIE DIRECTORATE</text>
</svg>"""

# 1.6 Factions & Sovereign Guilds (Factions Hub)
HERO_FACTIONS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="100%">
  <defs>
    <linearGradient id="facBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#14081c"/>
      <stop offset="50%" stop-color="#080612"/>
      <stop offset="100%" stop-color="#14081c"/>
    </linearGradient>
  </defs>

  <rect x="4" y="4" width="1192" height="312" rx="8" fill="url(#facBg)" stroke="#3b0764" stroke-width="2"/>
  <rect x="8" y="8" width="1184" height="304" rx="6" fill="none" stroke="rgba(168, 85, 247, 0.25)" stroke-width="1" stroke-dasharray="8 4"/>

  <rect x="12" y="12" width="1176" height="26" rx="3" fill="#0e0416" stroke="#2e1065" stroke-width="1"/>
  <text x="24" y="29" fill="#c084fc" font-family="monospace" font-size="11" font-weight="bold">/// FACTIONS DIRECTORY // SOVEREIGN ORGANIZATIONS &amp; GUILDS</text>
  <text x="1164" y="29" fill="#f1df76" font-family="monospace" font-size="11" font-weight="bold" text-anchor="end">13 POWER BLOCS // THE VEIL CONCORDAT</text>

  <!-- Left: Faction Insignia Wheel -->
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="280" height="230" rx="6" fill="rgba(16, 6, 24, 0.85)" stroke="#3b0764" stroke-width="1.5"/>
    <text x="140" y="30" fill="#f1df76" font-family="Impact" font-size="16" letter-spacing="2" text-anchor="middle">SOVEREIGN GUILDS</text>
    
    <circle cx="140" cy="130" r="70" fill="none" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="6 3"/>
    <circle cx="140" cy="130" r="32" fill="#2e1065" stroke="#f1df76" stroke-width="2"/>
    <text x="140" y="136" fill="#fff" font-family="Impact" font-size="12" text-anchor="middle">DIRECTORATE</text>
    
    <!-- Outer Node Dots -->
    <circle cx="140" cy="60" r="6" fill="#fbbf24"/>
    <circle cx="210" cy="130" r="6" fill="#ef4444"/>
    <circle cx="140" cy="200" r="6" fill="#10b981"/>
    <circle cx="70" cy="130" r="6" fill="#38bdf8"/>
  </g>

  <!-- Right: Factions Grid -->
  <g transform="translate(360, 60)">
    <rect x="0" y="0" width="800" height="230" rx="6" fill="rgba(16, 6, 24, 0.75)" stroke="#3b0764" stroke-width="1.5"/>
    <rect x="0" y="0" width="800" height="4" fill="#a855f7"/>

    <text x="28" y="44" fill="#f1df76" font-family="Impact, sans-serif" font-size="34" letter-spacing="3">FACTIONS &amp; POWER BLOCS</text>
    <text x="28" y="70" fill="#c084fc" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="1">13 SOVEREIGN FORCES SHAPING THE FATE OF SOMNARAK</text>

    <line x1="28" y1="84" x2="772" y2="84" stroke="#2e1065" stroke-width="1.5"/>

    <g transform="translate(28, 102)" font-family="monospace" font-size="11">
      <text x="0" y="0" fill="#f1df76" font-weight="bold">THE REVERIE DIRECTORATE</text>
      <text x="0" y="16" fill="#cbd5e1">Subterranean Facility Sovereign</text>

      <text x="260" y="0" fill="#fbbf24" font-weight="bold">HIGH COUNCIL OF SEVEN</text>
      <text x="260" y="16" fill="#cbd5e1">Zone A Metropolitan Rule</text>

      <text x="520" y="0" fill="#ef4444" font-weight="bold">SED EXPEDITION CORPS</text>
      <text x="520" y="16" fill="#cbd5e1">Undercity Deep Divers</text>

      <text x="0" y="60" fill="#38bdf8" font-weight="bold">UCD STRIKE FORCE</text>
      <text x="0" y="76" fill="#cbd5e1">Urban Containment Tactical Unit</text>

      <text x="260" y="60" fill="#a855f7" font-weight="bold">ARCHITECTS GUILD</text>
      <text x="260" y="76" fill="#cbd5e1">Geometric Geometry Masters</text>

      <text x="520" y="60" fill="#10b981" font-weight="bold">VEIL WARDENS &amp; WEAVERS</text>
      <text x="520" y="76" fill="#cbd5e1">Perimeter Vigil &amp; Silk Market</text>
    </g>
  </g>

  <!-- Bottom -->
  <rect x="12" y="286" width="1176" height="22" rx="2" fill="#08020e" stroke="#2e1065" stroke-width="1"/>
  <text x="24" y="301" fill="#64748b" font-family="monospace" font-size="10">POLITICAL BALANCE: ARMED TRUCE | CONCORDAT STATUS: ENFORCED | EMBARGO LEVEL: ZERO</text>
  <text x="1164" y="301" fill="#a855f7" font-family="monospace" font-size="10" text-anchor="end">DIPLOMATIC ARCHIVES // REVERIE LIAISON BUREAU</text>
</svg>"""

# 1.7 Lore & Absolvohan Timeline (Lore Hub)
HERO_LORE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="100%">
  <defs>
    <linearGradient id="loreBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#140804"/>
      <stop offset="50%" stop-color="#060910"/>
      <stop offset="100%" stop-color="#140804"/>
    </linearGradient>
  </defs>

  <rect x="4" y="4" width="1192" height="312" rx="8" fill="url(#loreBg)" stroke="#78350f" stroke-width="2"/>
  <rect x="8" y="8" width="1184" height="304" rx="6" fill="none" stroke="rgba(241, 223, 118, 0.25)" stroke-width="1" stroke-dasharray="8 4"/>

  <rect x="12" y="12" width="1176" height="26" rx="3" fill="#0e0602" stroke="#451a03" stroke-width="1"/>
  <text x="24" y="29" fill="#f1df76" font-family="monospace" font-size="11" font-weight="bold">/// LORE CHRONICLES // COSMOLOGY, ABSOLVOHAN &amp; THE 1,778 CYCLES</text>
  <text x="1164" y="29" fill="#38bdf8" font-family="monospace" font-size="11" font-weight="bold" text-anchor="end">THE THREE AGES // THE VEIL REVELATION</text>

  <!-- Left: Timeline Cycle Diagram -->
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="280" height="230" rx="6" fill="rgba(16, 8, 4, 0.85)" stroke="#78350f" stroke-width="1.5"/>
    <text x="140" y="30" fill="#f1df76" font-family="Impact" font-size="16" letter-spacing="2" text-anchor="middle">ABSOLVOHAN TIMELINE</text>
    
    <line x1="40" y1="60" x2="40" y2="200" stroke="#f1df76" stroke-width="3"/>
    <circle cx="40" cy="75" r="8" fill="#38bdf8" stroke="#fff" stroke-width="2"/>
    <text x="60" y="80" fill="#38bdf8" font-family="Impact" font-size="13">DAY 0: THE RESET</text>

    <circle cx="40" cy="130" r="8" fill="#f1df76" stroke="#fff" stroke-width="2"/>
    <text x="60" y="135" fill="#f1df76" font-family="Impact" font-size="13">DAY 180: THE CRISIS</text>

    <circle cx="40" cy="185" r="8" fill="#ef4444" stroke="#fff" stroke-width="2"/>
    <text x="60" y="190" fill="#ef4444" font-family="Impact" font-size="13">DAY 365: DAWN OF HOPE</text>
  </g>

  <!-- Right: Lore Compendium -->
  <g transform="translate(360, 60)">
    <rect x="0" y="0" width="800" height="230" rx="6" fill="rgba(16, 8, 4, 0.75)" stroke="#78350f" stroke-width="1.5"/>
    <rect x="0" y="0" width="800" height="4" fill="#f1df76"/>

    <text x="28" y="44" fill="#f1df76" font-family="Impact, sans-serif" font-size="34" letter-spacing="3">LORE &amp; COSMOLOGY COMPENDIUM</text>
    <text x="28" y="70" fill="#f59e0b" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="1">CHRONICLING 4,238 YEARS OF MUGENHAN HISTORY &amp; METAPHYSICS</text>

    <line x1="28" y1="84" x2="772" y2="84" stroke="#451a03" stroke-width="1.5"/>

    <g transform="translate(28, 102)" font-family="monospace" font-size="11">
      <text x="0" y="0" fill="#38bdf8" font-weight="bold">THE THREE AGES OF SOMNARAK</text>
      <text x="0" y="16" fill="#cbd5e1">The Golden Age, The Cataclysm &amp; The Veil</text>

      <text x="260" y="0" fill="#f1df76" font-weight="bold">ABSOLVOHAN (1,778 CYCLES)</text>
      <text x="260" y="16" fill="#cbd5e1">The 365-Day Repeating Facility Spiral</text>

      <text x="520" y="0" fill="#ef4444" font-weight="bold">THE DOORSPEECH COVENANT</text>
      <text x="520" y="16" fill="#cbd5e1">The 10 Founding Axioms of Majin</text>

      <text x="0" y="60" fill="#10b981" font-weight="bold">THE DAWN OF HOPE</text>
      <text x="0" y="76" fill="#cbd5e1">The 8 Reconstruction Arcs of Year 4,238</text>

      <text x="260" y="60" fill="#a855f7" font-weight="bold">TABOO RESONANCE</text>
      <text x="260" y="76" fill="#cbd5e1">The Unwritten Laws &amp; Karmic Debt</text>

      <text x="520" y="60" fill="#d97706" font-weight="bold">HORIZON WASTELAND SAGA</text>
      <text x="520" y="76" fill="#cbd5e1">The 6 Caravan Expedition Chapters</text>
    </g>
  </g>

  <!-- Bottom -->
  <rect x="12" y="286" width="1176" height="22" rx="2" fill="#080402" stroke="#451a03" stroke-width="1"/>
  <text x="24" y="301" fill="#64748b" font-family="monospace" font-size="10">TIMELINE STABILITY: 100% SYNCHRONIZED | CURRENT CYCLE: 1,778 | SINGULARITY THRESHOLD: IMMINENT</text>
  <text x="1164" y="301" fill="#f1df76" font-family="monospace" font-size="10" text-anchor="end">HISTORICAL RECORDS // REVERIE MEMORY ARCHIVE</text>
</svg>"""

# 1.8 Combat Systems & Battle Mechanics (Mechanics Hub)
HERO_MECHANICS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="100%">
  <defs>
    <linearGradient id="mechBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#041812"/>
      <stop offset="50%" stop-color="#060910"/>
      <stop offset="100%" stop-color="#140608"/>
    </linearGradient>
  </defs>

  <rect x="4" y="4" width="1192" height="312" rx="8" fill="url(#mechBg)" stroke="#064e3b" stroke-width="2"/>
  <rect x="8" y="8" width="1184" height="304" rx="6" fill="none" stroke="rgba(16, 185, 129, 0.25)" stroke-width="1" stroke-dasharray="8 4"/>

  <rect x="12" y="12" width="1176" height="26" rx="3" fill="#02140e" stroke="#064e3b" stroke-width="1"/>
  <text x="24" y="29" fill="#10b981" font-family="monospace" font-size="11" font-weight="bold">/// SYSTEMS &amp; MECHANICS // COMBAT MATRIX, WORK TYPES &amp; DAMAGE</text>
  <text x="1164" y="29" fill="#f1df76" font-family="monospace" font-size="11" font-weight="bold" text-anchor="end">4 WORK TYPES // 4 DAMAGE TYPES // COHERENCE GAUGE</text>

  <!-- Left: Damage Matrix Wheel -->
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="280" height="230" rx="6" fill="rgba(4, 20, 14, 0.85)" stroke="#064e3b" stroke-width="1.5"/>
    <text x="140" y="30" fill="#f1df76" font-family="Impact" font-size="16" letter-spacing="2" text-anchor="middle">DAMAGE QUADRANT</text>

    <!-- 4 Damage Badges -->
    <g transform="translate(25, 48)">
      <rect x="0" y="0" width="110" height="70" rx="4" fill="#2d0505" stroke="#ef4444" stroke-width="1.5"/>
      <text x="55" y="30" fill="#ef4444" font-family="Impact" font-size="14" text-anchor="middle">RED</text>
      <text x="55" y="52" fill="#fff" font-family="monospace" font-size="9" text-anchor="middle">PHYSICAL HP</text>

      <rect x="120" y="0" width="110" height="70" rx="4" fill="#0f172a" stroke="#f8fafc" stroke-width="1.5"/>
      <text x="175" y="30" fill="#f8fafc" font-family="Impact" font-size="14" text-anchor="middle">WHITE</text>
      <text x="175" y="52" fill="#fff" font-family="monospace" font-size="9" text-anchor="middle">MENTAL SP</text>

      <rect x="0" y="80" width="110" height="70" rx="4" fill="#050508" stroke="#a855f7" stroke-width="1.5"/>
      <text x="55" y="110" fill="#a855f7" font-family="Impact" font-size="14" text-anchor="middle">BLACK</text>
      <text x="55" y="132" fill="#fff" font-family="monospace" font-size="9" text-anchor="middle">CORROSIVE</text>

      <rect x="120" y="80" width="110" height="70" rx="4" fill="#041824" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="175" y="110" fill="#38bdf8" font-family="Impact" font-size="14" text-anchor="middle">PALE</text>
      <text x="175" y="132" fill="#fff" font-family="monospace" font-size="9" text-anchor="middle">EXISTENTIAL</text>
    </g>
  </g>

  <!-- Right: Title & Systems Overview -->
  <g transform="translate(360, 60)">
    <rect x="0" y="0" width="800" height="230" rx="6" fill="rgba(4, 20, 14, 0.75)" stroke="#064e3b" stroke-width="1.5"/>
    <rect x="0" y="0" width="800" height="4" fill="#10b981"/>

    <text x="28" y="44" fill="#f1df76" font-family="Impact, sans-serif" font-size="34" letter-spacing="3">COMBAT SYSTEMS &amp; MECHANICS</text>
    <text x="28" y="70" fill="#10b981" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="1">FACILITY OPERATIONS // CONTAINMENT PROCEDURES &amp; TACTICAL CLASH</text>

    <line x1="28" y1="84" x2="772" y2="84" stroke="#064e3b" stroke-width="1.5"/>

    <g transform="translate(28, 102)" font-family="monospace" font-size="11">
      <text x="0" y="0" fill="#ef4444" font-weight="bold">THE FOUR WORK TYPES</text>
      <text x="0" y="16" fill="#cbd5e1">Instinct, Insight, Attachment, Repression</text>

      <text x="260" y="0" fill="#38bdf8" font-weight="bold">HAN ENERGY &amp; DAMAGE MATRIX</text>
      <text x="260" y="16" fill="#cbd5e1">Red, White, Black, Pale Resistances</text>

      <text x="520" y="0" fill="#f1df76" font-weight="bold">RESONANT CLASH SYSTEM</text>
      <text x="520" y="16" fill="#cbd5e1">Speed Dice, Skill Slots &amp; Coin Flips</text>

      <text x="0" y="60" fill="#a855f7" font-weight="bold">FRACTURE &amp; PANIC THERAPY</text>
      <text x="0" y="76" fill="#cbd5e1">Psychic Breakdowns &amp; Restoration</text>

      <text x="260" y="60" fill="#10b981" font-weight="bold">ORDEALS FRAMEWORK</text>
      <text x="260" y="76" fill="#cbd5e1">Dawn, Noon, Dusk &amp; Midnight Incursions</text>

      <text x="520" y="60" fill="#d97706" font-weight="bold">HAN RELICS &amp; TOOLS</text>
      <text x="520" y="76" fill="#cbd5e1">Pre-Cataclysm Artifact Siphons</text>
    </g>
  </g>

  <!-- Bottom -->
  <rect x="12" y="286" width="1176" height="22" rx="2" fill="#020a06" stroke="#064e3b" stroke-width="1"/>
  <text x="24" y="301" fill="#64748b" font-family="monospace" font-size="10">TACTICAL ENGINE: ACTIVE | CLASH COMPUTATION: READY | MELTDOWN TIMERS: ARMED</text>
  <text x="1164" y="301" fill="#10b981" font-family="monospace" font-size="10" text-anchor="end">OPERATIONAL MANUAL // REVERIE TACTICAL DOCTRINE</text>
</svg>"""

save_svg(HERO_HAND, ["assets/banners/banner_hero_hand_of_change.svg"])
save_svg(HERO_CITY, ["assets/banners/banner_hero_somnarak_city.svg"])
save_svg(HERO_ENTITIES, ["assets/banners/banner_hero_sorrow_entities.svg"])
save_svg(HERO_MAW, ["assets/banners/banner_hero_maw_arsenal.svg"])
save_svg(HERO_CORES, ["assets/banners/banner_hero_echo_cores.svg"])
save_svg(HERO_FACTIONS, ["assets/banners/banner_hero_factions_council.svg"])
save_svg(HERO_LORE, ["assets/banners/banner_hero_lore_absolvohan.svg"])
save_svg(HERO_MECHANICS, ["assets/banners/banner_hero_combat_mechanics.svg"])

print("All 8 Panoramic Hero Banners built successfully!")

# ==============================================================================
# 2. FLOOR MINI-BANNERS (340 x 85)
# ==============================================================================

FLOORS = [
    ("f1_neutral", "F1", "NEUTRAL COMMAND", "MAJIN", "PALM CORE", "-200M", "#ef5b55", "#78350f", "#22080c"),
    ("f2_maws_keep", "F2", "MAW'S KEEP", "DEKAN", "CONTAINMENT", "-400M", "#38bdf8", "#0c4a6e", "#081826"),
    ("f3_extraction", "F3", "EXTRACTION HALL", "ZYRAK", "SIPHON FORGE", "-600M", "#f59e0b", "#78350f", "#221404"),
    ("f4_insight_forge", "F4", "INSIGHT FORGE", "AYSHUK", "RESEARCH CORE", "-800M", "#10b981", "#064e3b", "#041810"),
    ("f5_border_watch", "F5", "BORDER WATCH", "MELLDA", "PERIMETER BASTION", "-1200M", "#0284c7", "#0c4a6e", "#041424"),
    ("f6_deep_vault", "F6", "DEEP VAULT", "MARJUK", "CRYO ARCHIVE", "-1600M", "#8b5cf6", "#3b0764", "#140424"),
    ("f7_shadow_corps", "F7", "SHADOW CORPS", "ISHALL", "VOID DIVERS", "-1900M", "#e11d48", "#4c0519", "#24040c"),
    ("f8_gate_watch", "F8", "GATE WATCH", "XYAN", "TABOO GATE", "-2000M", "#94a3b8", "#1e293b", "#080c14")
]

for tag, code, name, lead, role, depth, primary_col, dark_col, bg_col in FLOORS:
    floor_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <rect x="2" y="2" width="336" height="81" rx="6" fill="{bg_col}" stroke="{primary_col}" stroke-width="2"/>
  
  <!-- Left Department Badge -->
  <circle cx="44" cy="42" r="28" fill="{dark_col}" stroke="{primary_col}" stroke-width="2"/>
  <polygon points="44,24 60,42 44,60 28,42" fill="{primary_col}"/>
  <circle cx="44" cy="42" r="6" fill="#fff"/>
  
  <!-- Content Details -->
  <text x="84" y="24" fill="#94a3b8" font-family="monospace" font-size="9" font-weight="bold" letter-spacing="1">[{code} // {role}]</text>
  <text x="84" y="46" fill="{primary_col}" font-family="Impact" font-size="17" letter-spacing="1">{name}</text>
  <text x="84" y="66" fill="#cbd5e1" font-family="monospace" font-size="9.5">LEAD: <tspan fill="#f1df76">{lead}</tspan> | DEPTH: <tspan fill="#38bdf8">{depth}</tspan></text>
  
  <!-- Right Accent Chevron -->
  <polygon points="320,42 308,30 312,26 328,42 312,58 308,54" fill="{primary_col}"/>
</svg>"""

    save_svg(floor_svg, [f"assets/banners/floor_banner_{tag}.svg"])

print("All 8 Floor Mini-Banners built successfully!")

# ==============================================================================
# 3. CATEGORY & THEME BANNERS (120 x 120 Inset)
# ==============================================================================

CATEGORIES = [
    ("characters", "ECHO-CORES", "#f1df76", "#78350f",
     """<circle cx="60" cy="46" r="20" fill="#78350f" stroke="#f1df76" stroke-width="2.2"/>
        <path d="M 28,94 C 28,68 92,68 92,94 Z" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
        <circle cx="60" cy="46" r="7" fill="#fff"/>"""),

    ("entities", "ENTITIES", "#ef4444", "#7f1d1d",
     """<polygon points="60,18 96,54 60,90 24,54" fill="#7f1d1d" stroke="#ef4444" stroke-width="2.5"/>
        <ellipse cx="60" cy="54" rx="20" ry="12" fill="#120406" stroke="#f1df76" stroke-width="1.8"/>
        <circle cx="60" cy="54" r="5" fill="#ef4444"/>"""),

    ("factions", "FACTIONS", "#a855f7", "#3b0764",
     """<polygon points="60,18 94,38 94,76 60,96 26,76 26,38" fill="#3b0764" stroke="#a855f7" stroke-width="2.5"/>
        <circle cx="60" cy="57" r="18" fill="#170420" stroke="#f1df76" stroke-width="1.8"/>
        <polygon points="60,46 68,57 60,68 52,57" fill="#c084fc"/>"""),

    ("locations", "ATLAS", "#38bdf8", "#0c4a6e",
     """<polygon points="60,18 98,57 60,96 22,57" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2.5"/>
        <circle cx="60" cy="57" r="20" fill="#041424" stroke="#f1df76" stroke-width="1.8"/>
        <circle cx="60" cy="57" r="6" fill="#38bdf8"/>"""),

    ("lore", "LORE", "#fbbf24", "#451a03",
     """<circle cx="60" cy="57" r="34" fill="#381e04" stroke="#fbbf24" stroke-width="2.5"/>
        <polygon points="60,32 78,57 60,82 42,57" fill="#78350f" stroke="#fff" stroke-width="1.5"/>
        <circle cx="60" cy="57" r="6" fill="#fbbf24"/>"""),

    ("mechanics", "SYSTEMS", "#10b981", "#064e3b",
     """<rect x="28" y="28" width="64" height="64" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2.5"/>
        <circle cx="60" cy="60" r="18" fill="#021c14" stroke="#f1df76" stroke-width="1.8"/>
        <line x1="60" y1="36" x2="60" y2="84" stroke="#10b981" stroke-width="2"/>
        <line x1="36" y1="60" x2="84" y2="60" stroke="#10b981" stroke-width="2"/>"""),

    ("maw", "M.A.W.", "#f59e0b", "#78350f",
     """<line x1="28" y1="92" x2="92" y2="28" stroke="#ef4444" stroke-width="6" stroke-linecap="round"/>
        <line x1="92" y1="92" x2="28" y2="28" stroke="#38bdf8" stroke-width="6" stroke-linecap="round"/>
        <circle cx="60" cy="60" r="18" fill="#090d16" stroke="#f1df76" stroke-width="2.5"/>
        <circle cx="60" cy="60" r="6" fill="#f1df76"/>"""),

    ("maw2", "ARSENAL", "#f59e0b", "#78350f",
     """<polygon points="60,20 90,40 80,90 60,100 40,90 30,40" fill="#78350f" stroke="#f59e0b" stroke-width="2.5"/>
        <circle cx="60" cy="58" r="14" fill="#0f172a" stroke="#fff" stroke-width="1.5"/>"""),

    ("timeline", "TIMELINE", "#38bdf8", "#0c4a6e",
     """<circle cx="60" cy="60" r="36" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2.5"/>
        <line x1="60" y1="32" x2="60" y2="60" stroke="#f1df76" stroke-width="3"/>
        <line x1="60" y1="60" x2="82" y2="60" stroke="#38bdf8" stroke-width="2.5"/>
        <circle cx="60" cy="60" r="5" fill="#fff"/>"""),

    ("categories", "HUBS", "#f1df76", "#78350f",
     """<polygon points="60,18 96,40 96,80 60,102 24,80 24,40" fill="#451a03" stroke="#f1df76" stroke-width="2.5"/>
        <circle cx="60" cy="60" r="18" fill="#140702" stroke="#38bdf8" stroke-width="2"/>
        <polygon points="60,48 68,60 60,72 52,60" fill="#f1df76"/>"""),

    ("zonemap", "ZONE MAP", "#a855f7", "#3b0764",
     """<polygon points="60,20 98,60 60,100 22,60" fill="#2e1065" stroke="#a855f7" stroke-width="2.5"/>
        <circle cx="60" cy="60" r="18" fill="#090312" stroke="#38bdf8" stroke-width="1.8"/>
        <circle cx="60" cy="60" r="6" fill="#f1df76"/>"""),

    ("ordeals", "ORDEALS", "#ef4444", "#7f1d1d",
     """<polygon points="60,18 96,54 60,90 24,54" fill="#450a0a" stroke="#ef4444" stroke-width="2.5"/>
        <circle cx="60" cy="54" r="16" fill="#7f1d1d" stroke="#f1df76" stroke-width="2"/>
        <polygon points="60,42 66,54 60,66 54,54" fill="#fff"/>"""),

    ("hope", "HOPE", "#f1df76", "#78350f",
     """<circle cx="60" cy="60" r="36" fill="#451a03" stroke="#f1df76" stroke-width="2.5"/>
        <polygon points="60,28 70,50 94,54 76,70 82,94 60,80 38,94 44,70 26,54 50,50" fill="#f1df76"/>"""),

    ("grudge", "GRUDGE", "#ef4444", "#7f1d1d",
     """<polygon points="60,20 94,84 26,84" fill="#450a0a" stroke="#ef4444" stroke-width="2.5"/>
        <circle cx="60" cy="58" r="12" fill="#ef4444"/>
        <line x1="60" y1="46" x2="60" y2="70" stroke="#fff" stroke-width="2"/>"""),

    ("lament", "LAMENT", "#38bdf8", "#0c4a6e",
     """<circle cx="60" cy="60" r="36" fill="#041424" stroke="#38bdf8" stroke-width="2.5"/>
        <path d="M 60,34 C 44,56 44,74 60,86 C 76,74 76,56 60,34 Z" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="60" cy="66" r="6" fill="#fff"/>"""),

    ("void", "VOID", "#a855f7", "#3b0764",
     """<circle cx="60" cy="60" r="36" fill="#000" stroke="#a855f7" stroke-width="2.5"/>
        <circle cx="60" cy="60" r="18" fill="#1e042e" stroke="#c084fc" stroke-width="1.8"/>
        <circle cx="60" cy="60" r="6" fill="#f1df76"/>"""),

    ("weight", "WEIGHT", "#d97706", "#451a03",
     """<line x1="60" y1="24" x2="60" y2="96" stroke="#f1df76" stroke-width="3"/>
        <line x1="28" y1="44" x2="92" y2="44" stroke="#f1df76" stroke-width="2.5"/>
        <circle cx="34" cy="74" r="12" fill="#451a03" stroke="#d97706" stroke-width="1.8"/>
        <circle cx="86" cy="74" r="12" fill="#451a03" stroke="#d97706" stroke-width="1.8"/>"""),

    ("compare", "COMPARE", "#10b981", "#064e3b",
     """<rect x="24" y="28" width="32" height="64" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
        <rect x="64" y="28" width="32" height="64" rx="4" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
        <line x1="24" y1="60" x2="96" y2="60" stroke="#f1df76" stroke-width="2"/>""")
]

for tag, title, col, dark_col, inner_gfx in CATEGORIES:
    cat_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="3" y="3" width="114" height="114" rx="14" fill="#070a12" stroke="{col}" stroke-width="2.5"/>
  <rect x="6" y="6" width="108" height="108" rx="10" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1"/>
  {inner_gfx}
  <rect x="20" y="98" width="80" height="15" rx="3" fill="{dark_col}" stroke="{col}" stroke-width="1"/>
  <text x="60" y="108.5" fill="#fff" font-family="Impact, Arial, sans-serif" font-size="8" letter-spacing="1" text-anchor="middle">{title}</text>
</svg>"""

    save_svg(cat_svg, [f"assets/icons/banner_{tag}.svg"])

print("All 18 Category Banners generated successfully!")
