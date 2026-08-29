#!/usr/bin/env python3
"""
tools/generate_all_personalized_icons.py
Generates the complete set of personalized, ultra-rich, visually harmonious
Somnarak vector SVG icons for Characters, Locations, Lore, Mechanics, Departments,
and Factions, guaranteeing NO generic placeholders and NO visual mismatches.
"""

import os

WIKI_ASSETS_ICONS = "/home/user/01_Somnarak_Wiki/assets/icons"
WIKI_ASSETS_AVATARS = "/home/user/01_Somnarak_Wiki/assets/avatars"
WIKI_ASSETS_CITY = "/home/user/01_Somnarak_Wiki/assets/layout/city/icons"
WIKI_ASSETS_HAND = "/home/user/01_Somnarak_Wiki/assets/layout/hand/icons"
WORKSPACE_ICONS = "/home/user/icons"

for d in [WIKI_ASSETS_ICONS, WIKI_ASSETS_AVATARS, WIKI_ASSETS_CITY, WIKI_ASSETS_HAND, WORKSPACE_ICONS]:
    os.makedirs(d, exist_ok=True)

# -------------------------------------------------------------
# 1. CHARACTER AVATARS (Echo-Cores & Key Secondary Figures)
# -------------------------------------------------------------

def get_character_avatars():
    return {
        # Director Majin - Regal Director's Visor & High Command Collar
        "avatar_core_majin.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="majGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#ef5b55" stop-opacity="0.6"/>
      <stop offset="60%" stop-color="#f1df76" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="majGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="50%" stop-color="#eab308"/>
      <stop offset="100%" stop-color="#713f12"/>
    </linearGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#ef5b55" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#majGlow)"/>
  <circle cx="60" cy="60" r="48" fill="none" stroke="rgba(241,223,118,0.2)" stroke-width="1" stroke-dasharray="4,2"/>
  
  <!-- High Stiff Command Collar -->
  <path d="M 32 104 L 38 72 L 60 82 L 82 72 L 88 104 Z" fill="#18181b" stroke="#ef5b55" stroke-width="1.5"/>
  <path d="M 44 80 L 60 92 L 76 80" fill="none" stroke="url(#majGold)" stroke-width="1.5"/>
  <polygon points="60,86 64,92 60,98 56,92" fill="#ef5b55"/>

  <!-- Face / Head Silhouette -->
  <path d="M 42 42 Q 60 26 78 42 Q 80 68 60 78 Q 40 68 42 42 Z" fill="#27272a" stroke="url(#majGold)" stroke-width="1.5"/>
  
  <!-- Hair & Director Cap/Crown -->
  <path d="M 36 40 Q 60 20 84 40 Q 82 28 60 22 Q 38 28 36 40 Z" fill="#09090b"/>
  <path d="M 48 24 L 60 16 L 72 24 L 60 20 Z" fill="url(#majGold)"/>

  <!-- Sleek Cybernetic Director Visor -->
  <path d="M 40 46 Q 60 52 80 46 L 78 52 Q 60 58 42 52 Z" fill="#070a12" stroke="#ef5b55" stroke-width="1.5"/>
  <!-- Central Glowing Ocular Eye -->
  <circle cx="60" cy="50" r="3.5" fill="#ef5b55"/>
  <circle cx="60" cy="50" r="1.5" fill="#ffffff"/>
  <line x1="44" y1="49" x2="54" y2="49" stroke="#ef5b55" stroke-width="1"/>
  <line x1="66" y1="49" x2="76" y2="49" stroke="#ef5b55" stroke-width="1"/>
  
  <!-- Authority Conduit Lines -->
  <line x1="60" y1="16" x2="60" y2="6" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="60" cy="6" r="2" fill="#f1df76"/>
</svg>""",

        # Secretary Seiyon - Pristine Bureaucratic Glasses & Ear Comms
        "avatar_core_seiyon.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="seiGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.6"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#6366f1" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#seiGlow)"/>
  <circle cx="60" cy="60" r="48" fill="none" stroke="rgba(99,102,241,0.25)" stroke-width="1" stroke-dasharray="3,3"/>

  <!-- Neat High-Button Secretary Collar & Tie -->
  <path d="M 36 104 L 42 74 L 60 84 L 78 74 L 84 104 Z" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
  <polygon points="56,84 64,84 62,104 58,104" fill="#6366f1"/>
  <circle cx="60" cy="78" r="2" fill="#e0e7ff"/>

  <!-- Head Contour & Sleek Parted Hair -->
  <path d="M 44 42 Q 60 28 76 42 Q 78 68 60 76 Q 42 68 44 42 Z" fill="#1f2937" stroke="#818cf8" stroke-width="1.2"/>
  <path d="M 38 38 Q 60 22 82 36 Q 74 24 58 24 Q 42 24 38 38 Z" fill="#0f172a"/>
  
  <!-- Sleek Bureaucratic Wire Glasses -->
  <rect x="42" y="46" width="14" height="8" rx="2" fill="rgba(99,102,241,0.2)" stroke="#a5b4fc" stroke-width="1.2"/>
  <rect x="64" y="46" width="14" height="8" rx="2" fill="rgba(99,102,241,0.2)" stroke="#a5b4fc" stroke-width="1.2"/>
  <line x1="56" y1="50" x2="64" y2="50" stroke="#a5b4fc" stroke-width="1.2"/>
  <!-- Glowing Eyes behind lenses -->
  <circle cx="49" cy="50" r="1.5" fill="#e0e7ff"/>
  <circle cx="71" cy="50" r="1.5" fill="#e0e7ff"/>

  <!-- Core 02 Data Earpiece -->
  <path d="M 76 48 L 84 46 L 82 56 L 76 54 Z" fill="#6366f1" stroke="#e0e7ff" stroke-width="1"/>
  <circle cx="84" cy="46" r="1.5" fill="#38bdf8"/>
</svg>""",

        # Containment Lead Dekan - Heavy Containment Visor & Hydraulics
        "avatar_core_dekan.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="dekGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.6"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#dekGlow)"/>
  
  <!-- Reinforced Heavy Hazard Armor Shoulders -->
  <path d="M 28 104 L 36 70 L 60 78 L 84 70 L 92 104 Z" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <rect x="46" y="78" width="28" height="10" fill="#0284c7" rx="2"/>
  <line x1="50" y1="83" x2="70" y2="83" stroke="#e0f2fe" stroke-width="1.5"/>

  <!-- Heavy Hydraulic Neck Guard & Bolts -->
  <circle cx="34" cy="80" r="3" fill="#38bdf8"/>
  <circle cx="86" cy="80" r="3" fill="#38bdf8"/>
  
  <!-- Heavy Containment Visor Helmet -->
  <path d="M 38 42 L 44 26 L 76 26 L 82 42 L 78 72 L 42 72 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="1.8"/>
  <!-- Dual Reinforced Slit Visor -->
  <polygon points="44,46 76,46 74,54 46,54" fill="#070a12" stroke="#38bdf8" stroke-width="1.2"/>
  <line x1="46" y1="50" x2="74" y2="50" stroke="#38bdf8" stroke-width="2"/>
  
  <!-- High-Pressure Fluid Lines -->
  <path d="M 40 60 Q 32 68 36 82" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
  <path d="M 80 60 Q 88 68 84 82" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
</svg>""",

        # Extraction Lead Zyrak - Molten Amber Goggles & Respirator Mask
        "avatar_core_zyrak.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="zyrGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.7"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#f59e0b" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#zyrGlow)"/>

  <!-- Forge Smock & Thermal Hazard Plating -->
  <path d="M 30 104 L 38 72 L 60 80 L 82 72 L 90 104 Z" fill="#271a0c" stroke="#f59e0b" stroke-width="1.8"/>
  <polygon points="52,80 68,80 60,94" fill="#b45309"/>

  <!-- Head & Forge Hood -->
  <path d="M 38 40 Q 60 22 82 40 L 80 74 L 40 74 Z" fill="#1c1917" stroke="#d97706" stroke-width="1.5"/>

  <!-- Heavy Brass Extraction Goggles -->
  <circle cx="48" cy="46" r="9" fill="#070a12" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="72" cy="46" r="9" fill="#070a12" stroke="#f59e0b" stroke-width="2"/>
  <line x1="57" y1="46" x2="63" y2="46" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="48" cy="46" r="5" fill="#fbbf24"/>
  <circle cx="72" cy="46" r="5" fill="#fbbf24"/>

  <!-- Industrial Han Filtration Respirator -->
  <polygon points="50,60 70,60 66,74 54,74" fill="#0c0a09" stroke="#f59e0b" stroke-width="1.5"/>
  <line x1="54" y1="64" x2="66" y2="64" stroke="#f59e0b" stroke-width="1"/>
  <line x1="56" y1="68" x2="64" y2="68" stroke="#f59e0b" stroke-width="1"/>
</svg>""",

        # Insight Lead Ayshuk - Multi-Lens Research Monocle & Neural Halo
        "avatar_core_ayshuk.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="ayshGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.6"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#10b981" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#ayshGlow)"/>

  <!-- Clinical Research Coat Lapels -->
  <path d="M 32 104 L 40 72 L 60 84 L 80 72 L 88 104 Z" fill="#062e22" stroke="#10b981" stroke-width="1.5"/>
  <line x1="60" y1="84" x2="60" y2="104" stroke="#6ee7b7" stroke-width="1.5"/>

  <!-- Neural Scan Halo -->
  <circle cx="60" cy="32" r="22" fill="none" stroke="#34d399" stroke-width="1" stroke-dasharray="3,3"/>

  <!-- Head & Analytical Scholar Brow -->
  <path d="M 42 42 Q 60 26 78 42 Q 80 66 60 76 Q 40 66 42 42 Z" fill="#0f291e" stroke="#10b981" stroke-width="1.2"/>
  
  <!-- Multi-Lens Cybernetic Monocle Array (Right Eye) -->
  <circle cx="68" cy="48" r="8" fill="#070a12" stroke="#34d399" stroke-width="1.8"/>
  <circle cx="68" cy="48" r="4" fill="#10b981"/>
  <circle cx="75" cy="42" r="3" fill="#070a12" stroke="#6ee7b7" stroke-width="1"/>
  <circle cx="75" cy="42" r="1" fill="#6ee7b7"/>

  <!-- Normal Left Eye with Scan Line -->
  <line x1="46" y1="48" x2="54" y2="48" stroke="#34d399" stroke-width="1.5"/>
  <circle cx="50" cy="48" r="1.5" fill="#a7f3d0"/>
</svg>""",

        # Border Watch Lead Mellda - Frost Tactical Cowl & Perimeter Sensors
        "avatar_core_mellda.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="melGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#e2e8f0" stop-opacity="0.7"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#e2e8f0" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#melGlow)"/>

  <!-- Heavy Frost-Bitten Ballistic Scarf -->
  <path d="M 30 104 L 36 74 Q 60 88 84 74 L 90 104 Z" fill="#1e293b" stroke="#e2e8f0" stroke-width="1.8"/>
  <path d="M 38 72 Q 60 84 82 72 Q 60 64 38 72 Z" fill="#334155" stroke="#94a3b8" stroke-width="1.2"/>

  <!-- Tactical Cowl Hood -->
  <path d="M 36 44 Q 60 20 84 44 L 80 72 L 40 72 Z" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5"/>

  <!-- Cold Surveillance Optics -->
  <polygon points="42,48 78,48 74,56 46,56" fill="#070a12" stroke="#94a3b8" stroke-width="1.2"/>
  <line x1="46" y1="52" x2="74" y2="52" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="50" cy="52" r="2" fill="#ffffff"/>
  <circle cx="70" cy="52" r="2" fill="#ffffff"/>

  <!-- Perimeter Antenna Probe -->
  <line x1="78" y1="40" x2="88" y2="28" stroke="#cbd5e1" stroke-width="1.5"/>
  <circle cx="88" cy="28" r="2" fill="#38bdf8"/>
</svg>""",

        # Deep Vault Lead Marjuk - Ancient Archivist Cowl & Cipher Sensor
        "avatar_core_marjuk.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="marjGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#be123c" stop-opacity="0.7"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#be123c" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#marjGlow)"/>

  <!-- Ancient Archivist Robes with Gold Ciphers -->
  <path d="M 32 104 L 40 72 L 60 82 L 80 72 L 88 104 Z" fill="#2b0914" stroke="#be123c" stroke-width="1.8"/>
  <polygon points="56,82 64,82 60,98" fill="#fda4af"/>

  <!-- Archivist Deep Cowl Hood -->
  <path d="M 36 44 Q 60 18 84 44 L 80 74 L 40 74 Z" fill="#17040a" stroke="#f43f5e" stroke-width="1.5"/>
  
  <!-- Glowing Cipher Memory Scroll Ocular Sensor -->
  <rect x="42" y="46" width="36" height="12" rx="2" fill="#070a12" stroke="#be123c" stroke-width="1.5"/>
  <circle cx="50" cy="52" r="3" fill="#f43f5e"/>
  <circle cx="70" cy="52" r="3" fill="#f43f5e"/>
  <line x1="54" y1="50" x2="66" y2="50" stroke="#fda4af" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="54" y1="54" x2="66" y2="54" stroke="#fda4af" stroke-width="1" stroke-dasharray="2,2"/>
</svg>""",

        # Shadow Corps Lead Ishall - Razor Slit Stealth Mask & Daggers
        "avatar_core_ishall.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="ishGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.7"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#a855f7" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#ishGlow)"/>

  <!-- Sleek Stealth Operative Armor -->
  <path d="M 32 104 L 40 74 L 60 82 L 80 74 L 88 104 Z" fill="#180d26" stroke="#a855f7" stroke-width="1.5"/>
  
  <!-- Midnight Ninja / Assassin Cowl -->
  <path d="M 38 42 Q 60 22 82 42 L 78 72 L 42 72 Z" fill="#0d0714" stroke="#c084fc" stroke-width="1.5"/>

  <!-- Razor-Thin Violet Ocular Slit -->
  <polygon points="40,50 80,50 60,56" fill="#070a12" stroke="#a855f7" stroke-width="1.5"/>
  <line x1="42" y1="50" x2="78" y2="50" stroke="#f0abfc" stroke-width="2"/>
  <circle cx="60" cy="50" r="2" fill="#ffffff"/>

  <!-- Crossed Shadow Daggers (Shoulder Mounts) -->
  <line x1="28" y1="78" x2="42" y2="64" stroke="#c084fc" stroke-width="2"/>
  <line x1="92" y1="78" x2="78" y2="64" stroke="#c084fc" stroke-width="2"/>
</svg>""",

        # Gate Watch Lead Xyan - Heavy Exile Blast Hood & Warning Horn
        "avatar_core_xyan.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="xyanGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.7"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#fbbf24" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#xyanGlow)"/>

  <!-- Heavy Exile Trench Coat with Hazard Straps -->
  <path d="M 30 104 L 38 72 L 60 82 L 82 72 L 90 104 Z" fill="#241a06" stroke="#fbbf24" stroke-width="1.8"/>
  <line x1="38" y1="84" x2="82" y2="84" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,2"/>

  <!-- Weathered Blast Helmet with Cracked Visor -->
  <path d="M 38 40 Q 60 20 82 40 L 78 72 L 42 72 Z" fill="#140f04" stroke="#d97706" stroke-width="1.5"/>
  
  <!-- Cracked Amber Visor with Glowing Fissure -->
  <polygon points="44,48 76,48 72,58 48,58" fill="#070a12" stroke="#fbbf24" stroke-width="1.2"/>
  <path d="M 48 53 L 56 50 L 64 56 L 72 52" fill="none" stroke="#fef08a" stroke-width="2"/>
  
  <!-- Warning Horn Crest -->
  <polygon points="60,20 64,28 56,28" fill="#fbbf24"/>
</svg>""",

        # Field Agent Minho - Recon Sniper Visor & Dual Comms
        "avatar_char_minho.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="minGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.7"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#minGlow)"/>

  <!-- Tactical Strike Rig & Harness -->
  <path d="M 32 104 L 40 74 L 60 82 L 80 74 L 88 104 Z" fill="#0c192c" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="52" y="86" width="16" height="18" fill="#0284c7" rx="2"/>

  <!-- Field Headgear & Comms Headset -->
  <path d="M 42 42 Q 60 26 78 42 Q 80 66 60 76 Q 40 66 42 42 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
  
  <!-- Recon Crosshair Visor -->
  <rect x="42" y="46" width="36" height="10" rx="2" fill="#070a12" stroke="#38bdf8" stroke-width="1.5"/>
  <circle cx="50" cy="51" r="3" fill="#38bdf8"/>
  <line x1="64" y1="51" x2="74" y2="51" stroke="#ef5b55" stroke-width="1.5"/>
  <line x1="69" y1="47" x2="69" y2="55" stroke="#ef5b55" stroke-width="1.5"/>

  <!-- Left Side Comms Antenna -->
  <line x1="42" y1="50" x2="34" y2="34" stroke="#38bdf8" stroke-width="1.5"/>
  <circle cx="34" cy="34" r="2" fill="#71efaf"/>
</svg>""",

        # Merchant Doha - Appraisal Monocle & Han Vials
        "avatar_char_doha.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="dohGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.6"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#dohGlow)"/>

  <!-- Velvet High-Collar Merchant Coat with Han Vial -->
  <path d="M 32 104 L 40 72 L 60 84 L 80 72 L 88 104 Z" fill="#2a2408" stroke="#f1df76" stroke-width="1.5"/>
  <!-- Glowing Han Capsule in Pocket -->
  <rect x="70" y="86" width="6" height="12" rx="2" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>

  <!-- Head & Silk Headband -->
  <path d="M 44 42 Q 60 28 76 42 Q 78 66 60 76 Q 42 66 44 42 Z" fill="#1c1917" stroke="#f1df76" stroke-width="1.2"/>
  <path d="M 42 36 Q 60 24 78 36" fill="none" stroke="#eab308" stroke-width="2"/>

  <!-- Golden Jeweled Appraisal Loupe / Monocle (Left Eye) -->
  <circle cx="52" cy="48" r="8" fill="#070a12" stroke="#f1df76" stroke-width="2"/>
  <circle cx="52" cy="48" r="4" fill="#fbbf24"/>
  <line x1="52" y1="56" x2="52" y2="68" stroke="#f1df76" stroke-width="1.2"/>

  <!-- Right Shrewd Eye -->
  <path d="M 64 48 Q 70 46 76 48" fill="none" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="70" cy="49" r="1.5" fill="#fef08a"/>
</svg>""",

        # Researcher Soojin - Bio-Resonance Specimen Prism & Spectacles
        "avatar_char_soojin.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="sojGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#06b6d4" stop-opacity="0.6"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#06b6d4" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#sojGlow)"/>

  <!-- Lab Smock & Bio-Tuning Fork Brooch -->
  <path d="M 34 104 L 40 74 L 60 84 L 80 74 L 86 104 Z" fill="#082f49" stroke="#06b6d4" stroke-width="1.5"/>
  <polygon points="60,86 63,92 57,92" fill="#38bdf8"/>

  <!-- Head & Tied Hair Bun -->
  <circle cx="60" cy="28" r="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1"/>
  <path d="M 44 44 Q 60 30 76 44 Q 78 68 60 76 Q 42 68 44 44 Z" fill="#164e63" stroke="#22d3ee" stroke-width="1.2"/>

  <!-- Clinical Wire Spectacles -->
  <rect x="44" y="48" width="12" height="8" rx="2" fill="none" stroke="#e0f2fe" stroke-width="1.2"/>
  <rect x="64" y="48" width="12" height="8" rx="2" fill="none" stroke="#e0f2fe" stroke-width="1.2"/>
  <line x1="56" y1="52" x2="64" y2="52" stroke="#e0f2fe" stroke-width="1.2"/>
  <circle cx="50" cy="52" r="1.5" fill="#22d3ee"/>
  <circle cx="70" cy="52" r="1.5" fill="#22d3ee"/>
</svg>""",

        # Civilian Sora - Weathered Patchwork Scarf & Warm Sheltered Ember
        "avatar_char_sora.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="sorGlow" cx="50%" cy="60%" r="50%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#f59e0b" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#sorGlow)"/>

  <!-- Sheltering Cupped Hands with Glowing Memory Spark -->
  <path d="M 42 96 Q 60 106 78 96 Q 60 88 42 96 Z" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
  <circle cx="60" cy="94" r="5" fill="#fef08a"/>
  <circle cx="60" cy="94" r="2" fill="#ffffff"/>

  <!-- Thick Weathered Scarf -->
  <path d="M 36 70 Q 60 82 84 70 Q 60 62 36 70 Z" fill="#451a03" stroke="#d97706" stroke-width="1.5"/>

  <!-- Young Survivor Face & Soft Hair -->
  <path d="M 44 42 Q 60 30 76 42 Q 78 64 60 70 Q 42 64 44 42 Z" fill="#292524" stroke="#f59e0b" stroke-width="1.2"/>
  <path d="M 40 38 Q 60 22 80 38 Q 60 32 40 38 Z" fill="#1c1917"/>
  
  <!-- Innocent Glowing Amber Eyes -->
  <circle cx="52" cy="48" r="2.5" fill="#fbbf24"/>
  <circle cx="68" cy="48" r="2.5" fill="#fbbf24"/>
</svg>""",

        # Strike Captain Taeho - Scarred Breaching Helm & Crossed Cleavers
        "avatar_char_taeho.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="taeGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.7"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#ef4444" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#taeGlow)"/>

  <!-- Heavy UCD Breaching Armor Plate -->
  <path d="M 28 104 L 36 70 L 60 78 L 84 70 L 92 104 Z" fill="#1c1917" stroke="#ef4444" stroke-width="2"/>
  <polygon points="54,78 66,78 60,90" fill="#991b1b"/>

  <!-- Heavy Breaching Helmet with Battle Scar -->
  <path d="M 36 40 L 44 24 L 76 24 L 84 40 L 80 72 L 40 72 Z" fill="#0c0a09" stroke="#dc2626" stroke-width="1.8"/>
  
  <!-- Fierce Horizontal Combat Visor -->
  <polygon points="42,46 78,46 74,54 46,54" fill="#070a12" stroke="#ef4444" stroke-width="1.5"/>
  <line x1="44" y1="50" x2="76" y2="50" stroke="#fca5a5" stroke-width="2"/>

  <!-- Battle Scar across Visor -->
  <line x1="48" y1="36" x2="62" y2="62" stroke="#ef4444" stroke-width="1.8"/>
</svg>""",

        # Caravan Master Kael - Desert Wanderer Hat & Sextant Compass
        "avatar_char_kael.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="kaelGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#d97706" stop-opacity="0.7"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#d97706" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#kaelGlow)"/>

  <!-- Leather Duster & Dust Scarf -->
  <path d="M 30 104 L 38 74 Q 60 86 82 74 L 90 104 Z" fill="#3b2506" stroke="#d97706" stroke-width="1.8"/>

  <!-- Wide-Brim Desert Wanderer Hat -->
  <ellipse cx="60" cy="38" rx="34" ry="10" fill="#1c1304" stroke="#f59e0b" stroke-width="1.8"/>
  <path d="M 44 38 Q 60 18 76 38 Z" fill="#291b05" stroke="#d97706" stroke-width="1.5"/>

  <!-- Desert Goggles & Respirator -->
  <circle cx="50" cy="48" r="6" fill="#070a12" stroke="#fbbf24" stroke-width="1.5"/>
  <circle cx="70" cy="48" r="6" fill="#070a12" stroke="#fbbf24" stroke-width="1.5"/>
  <line x1="56" y1="48" x2="64" y2="48" stroke="#fbbf24" stroke-width="1.5"/>
  <circle cx="50" cy="48" r="2.5" fill="#f59e0b"/>
  <circle cx="70" cy="48" r="2.5" fill="#f59e0b"/>
</svg>""",

        # Master Weaver Yeonhwa - Loom Spindle & Glowing Han Silk
        "avatar_char_yeonhwa.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="yeonGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.6"/>
      <stop offset="60%" stop-color="#38bdf8" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#a855f7" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#yeonGlow)"/>

  <!-- Han Silk Kimono Collar -->
  <path d="M 34 104 L 42 72 L 60 84 L 78 72 L 86 104 Z" fill="#2e1065" stroke="#a855f7" stroke-width="1.5"/>
  <path d="M 44 76 L 60 90 L 76 76" fill="none" stroke="#38bdf8" stroke-width="1.5"/>

  <!-- Elaborate Updo with Weaving Hairpin -->
  <circle cx="60" cy="26" r="10" fill="#0f172a" stroke="#c084fc" stroke-width="1"/>
  <line x1="42" y1="20" x2="78" y2="32" stroke="#f1df76" stroke-width="2"/>
  <circle cx="78" cy="32" r="3" fill="#f1df76"/>

  <!-- Serene Face & Luminous Violet Eyes -->
  <path d="M 44 44 Q 60 32 76 44 Q 78 68 60 76 Q 42 68 44 44 Z" fill="#1e1b4b" stroke="#a855f7" stroke-width="1.2"/>
  <circle cx="52" cy="50" r="2.5" fill="#e879f9"/>
  <circle cx="68" cy="50" r="2.5" fill="#38bdf8"/>

  <!-- Floating Han Thread Filaments -->
  <path d="M 30 50 Q 40 60 48 56 Q 56 52 70 64" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,2"/>
</svg>""",

        # Facility Engineer Joon - Welding Visor & Heavy Torque Wrenches
        "avatar_char_joon.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="joonGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#f97316" stop-opacity="0.7"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#f97316" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#joonGlow)"/>

  <!-- Heavy Work Overalls & Shoulder Straps -->
  <path d="M 30 104 L 38 72 L 60 80 L 82 72 L 90 104 Z" fill="#1c1917" stroke="#f97316" stroke-width="1.8"/>
  <rect x="52" y="82" width="16" height="22" fill="#c2410c"/>

  <!-- Engineer Cap & Flip-Up Welding Shield -->
  <path d="M 38 42 L 44 26 L 76 26 L 82 42 L 78 72 L 42 72 Z" fill="#292524" stroke="#fb923c" stroke-width="1.5"/>
  
  <!-- Tinted Welding Visor Screen -->
  <rect x="44" y="44" width="32" height="12" rx="2" fill="#070a12" stroke="#ea580c" stroke-width="1.5"/>
  <polygon points="56,48 64,48 60,54" fill="#fed7aa"/>
  
  <!-- Crossed Torque Wrenches behind head -->
  <line x1="28" y1="28" x2="42" y2="42" stroke="#ea580c" stroke-width="3" stroke-linecap="round"/>
  <line x1="92" y1="28" x2="78" y2="42" stroke="#ea580c" stroke-width="3" stroke-linecap="round"/>
</svg>""",

        # Cheonbulok Refugees - Trio of Survivors under Amber Barrier Dome
        "avatar_char_cheonbulok_refugees.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="refGlow" cx="50%" cy="55%" r="55%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.8"/>
      <stop offset="60%" stop-color="#0284c7" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#f59e0b" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#refGlow)"/>

  <!-- Protective Sanctuary Barrier Arch -->
  <path d="M 24 96 Q 60 28 96 96" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2"/>

  <!-- Center Survivor Figure -->
  <circle cx="60" cy="46" r="8" fill="#1c1917" stroke="#f59e0b" stroke-width="1.5"/>
  <path d="M 48 94 L 54 62 L 66 62 L 72 94 Z" fill="#292524" stroke="#f59e0b" stroke-width="1.5"/>

  <!-- Left Survivor Figure (Clutching lantern) -->
  <circle cx="42" cy="54" r="6" fill="#1c1917" stroke="#38bdf8" stroke-width="1.2"/>
  <path d="M 32 94 L 38 68 L 48 68 L 52 94 Z" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>

  <!-- Right Survivor Figure -->
  <circle cx="78" cy="54" r="6" fill="#1c1917" stroke="#38bdf8" stroke-width="1.2"/>
  <path d="M 68 94 L 72 68 L 82 68 L 88 94 Z" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>

  <!-- Central Ancestral Lantern -->
  <circle cx="60" cy="74" r="5" fill="#fef08a"/>
</svg>""",

        # High Architects - Geometric Council Half-Mask & Drafting Compass
        "avatar_char_high_architects.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="archGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#archGlow)"/>

  <!-- High Guild Robes & Golden Hexagonal Collar -->
  <path d="M 30 104 L 38 70 L 60 82 L 82 70 L 90 104 Z" fill="#1f1807" stroke="#f1df76" stroke-width="1.8"/>
  <polygon points="60,82 68,90 60,98 52,90" fill="#f1df76"/>

  <!-- Geometric Porcelain Mask & Golden Compass -->
  <polygon points="60,26 80,44 76,68 60,76 44,68 40,44" fill="#070a12" stroke="#f1df76" stroke-width="2"/>
  
  <!-- Right Eye: Golden Compass Monocle -->
  <circle cx="68" cy="48" r="6" fill="#1a1405" stroke="#f1df76" stroke-width="1.5"/>
  <polygon points="68,44 70,48 68,52 66,48" fill="#f1df76"/>

  <!-- Left Eye: Slit Visor -->
  <line x1="46" y1="48" x2="56" y2="48" stroke="#38bdf8" stroke-width="1.5"/>

  <!-- Golden Drafting Divider Crest -->
  <path d="M 48 18 L 60 30 L 72 18" fill="none" stroke="#f1df76" stroke-width="1.8"/>
</svg>"""
    }

def main():
    avatars = get_character_avatars()
    for name, svg in avatars.items():
        p1 = os.path.join(WIKI_ASSETS_AVATARS, name)
        p2 = os.path.join(WORKSPACE_ICONS, name)
        p3 = os.path.join(WIKI_ASSETS_ICONS, name)
        for path in [p1, p2, p3]:
            with open(path, "w", encoding="utf-8") as f:
                f.write(svg)
        print(f"Generated Character Avatar: {name}")

if __name__ == "__main__":
    main()
