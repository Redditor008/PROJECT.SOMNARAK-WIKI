import os

def generate_all_bespoke_svgs():
    target_dirs = [
        "/home/user/01_Somnarak_Wiki/assets/icons",
        "/home/user/01_Somnarak_Wiki/assets/avatars",
        "/home/user/01_Somnarak_Wiki/assets/layout/hand/icons",
        "/home/user/01_Somnarak_Wiki/assets/layout/city/icons",
        "/home/user/icons"
    ]

    for d in target_dirs:
        os.makedirs(d, exist_ok=True)

    svgs = {}

    # ==========================================
    # 1. CHARACTER & ECHO-CORE AVATARS (100% Bespoke Shapes)
    # ==========================================

    # Majin: Director - Crowned Monolith with Blindfolded Sovereign Face & Hourglass
    svgs["avatar_core_majin.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="majGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef5b55" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#090d16" stop-opacity="0.95"/>
    </radialGradient>
  </defs>
  <!-- Crowned Imperial Frame -->
  <polygon points="60,4 82,18 114,18 106,60 114,102 82,102 60,116 38,102 6,102 14,60 6,18 38,18" fill="url(#majGlow)" stroke="#f1df76" stroke-width="3"/>
  <rect x="22" y="22" width="76" height="76" fill="#080c14" stroke="#ef5b55" stroke-width="2"/>
  
  <!-- Director's Golden Crown Antennas -->
  <polygon points="40,24 50,10 60,20 70,10 80,24" fill="#f1df76" stroke="#ffffff" stroke-width="1.5"/>
  
  <!-- Majestic Visage & Golden Sovereign Blindfold -->
  <rect x="42" y="34" width="36" height="42" rx="4" fill="#141c2b" stroke="#38bdf8" stroke-width="2"/>
  <rect x="38" y="44" width="44" height="12" rx="2" fill="#f1df76" stroke="#991b1b" stroke-width="2"/>
  <!-- Glowing Blindfold Glyphs -->
  <line x1="44" y1="50" x2="76" y2="50" stroke="#000000" stroke-width="2" stroke-dasharray="3 3"/>
  
  <!-- Hourglass Core Symbol on Gorget -->
  <path d="M 50,86 L 70,86 L 50,102 L 70,102 Z" fill="#ef5b55" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="60" cy="94" r="3" fill="#ffffff"/>
</svg>'''

    # Seiyon: Secretary - Floating Cybernetic Slate Monocle & Data Veils
    svgs["avatar_core_seiyon.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <!-- Diamond Data Frame -->
  <polygon points="60,4 116,60 60,116 4,60" fill="#05131f" stroke="#38bdf8" stroke-width="3.5"/>
  <polygon points="60,16 104,60 60,104 16,60" fill="#03080f" stroke="#f1df76" stroke-width="1.5"/>

  <!-- Sleek Analytical Hair & Cybernetic Hairpin -->
  <path d="M 36,36 Q 60,18 84,36 L 86,72 Q 60,90 34,72 Z" fill="#0c2238" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="76,20 98,14 90,36" fill="#f1df76" stroke="#ffffff" stroke-width="1.5"/>

  <!-- Twin Floating Holographic Monocle Slates -->
  <rect x="40" y="46" width="16" height="12" rx="2" fill="#38bdf8" opacity="0.85" stroke="#ffffff" stroke-width="1.5"/>
  <rect x="64" y="46" width="16" height="12" rx="2" fill="#38bdf8" opacity="0.85" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="56" y1="52" x2="64" y2="52" stroke="#ffffff" stroke-width="1.5"/>

  <!-- Audio Headset & Data Waveform Collar -->
  <path d="M 32,58 Q 30,76 42,88 L 78,88 Q 90,76 88,58" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <line x1="44" y1="96" x2="76" y2="96" stroke="#f1df76" stroke-width="3"/>
</svg>'''

    # Dekan: Containment Lead - Heavy Basalt Fortress Helmet & 3 Slit Crimson Visor
    svgs["avatar_core_dekan.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <!-- Heavy Shield-Shaped Frame -->
  <polygon points="60,6 114,26 98,96 60,116 22,96 6,26" fill="#1c0a0d" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="60,16 102,32 88,88 60,104 32,88 18,32" fill="#0c0406" stroke="#f1df76" stroke-width="1.5"/>

  <!-- Massive Basalt Crag Helmet -->
  <polygon points="36,30 84,30 90,78 60,94 30,78" fill="#2d161a" stroke="#ef5b55" stroke-width="2.5"/>
  
  <!-- Triple Horizontal Glowing Crimson Slit Visors -->
  <rect x="42" y="42" width="36" height="6" rx="2" fill="#ef5b55" stroke="#ffffff" stroke-width="1"/>
  <rect x="44" y="52" width="32" height="6" rx="2" fill="#ef5b55" stroke="#ffffff" stroke-width="1"/>
  <rect x="48" y="62" width="24" height="6" rx="2" fill="#ef5b55" stroke="#ffffff" stroke-width="1"/>

  <!-- Heavy Hydraulic Neck Bolting Collar -->
  <rect x="36" y="86" width="48" height="12" rx="3" fill="#110507" stroke="#f1df76" stroke-width="2"/>
  <circle cx="44" cy="92" r="3" fill="#ef5b55"/>
  <circle cx="76" cy="92" r="3" fill="#ef5b55"/>
</svg>'''

    # Zyrak: Extraction Lead - Alchemical Welding Mask with Twin Han Glass Tubes
    svgs["avatar_core_zyrak.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <!-- Octagonal Industrial Crucible Frame -->
  <polygon points="36,4 84,4 116,36 116,84 84,116 36,116 4,84 4,36" fill="#1e1302" stroke="#f1df76" stroke-width="3.5"/>
  
  <!-- Hooded Cowl & Welder Mask Housing -->
  <path d="M 28,34 Q 60,14 92,34 L 96,86 L 24,86 Z" fill="#2d1d05" stroke="#f1df76" stroke-width="2"/>
  <rect x="38" y="38" width="44" height="28" rx="6" fill="#080400" stroke="#ef5b55" stroke-width="2.5"/>
  
  <!-- Welder Viewport & Molten Core Glow -->
  <rect x="44" y="46" width="32" height="12" rx="3" fill="#f1df76" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="60" y1="46" x2="60" y2="58" stroke="#ef5b55" stroke-width="2"/>

  <!-- Twin Vertical Glowing Han Glass Siphon Tubes -->
  <rect x="30" y="52" width="8" height="36" rx="3" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
  <rect x="82" y="52" width="8" height="36" rx="3" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
  <path d="M 38,82 Q 60,98 82,82" fill="none" stroke="#f1df76" stroke-width="3"/>
</svg>'''

    # Ayshuk: Research Lead - Triple Microscope Lens Array & Neural Mandala
    svgs["avatar_core_ayshuk.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <!-- Hexagonal Science Frame -->
  <polygon points="60,4 112,32 112,88 60,116 8,88 8,32" fill="#031a19" stroke="#71efaf" stroke-width="3.5"/>

  <!-- Floating Holographic Neural Rings -->
  <circle cx="60" cy="54" r="32" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 4"/>
  
  <!-- Triple Prismatic Microscope Ocular Lenses -->
  <circle cx="48" cy="42" r="11" fill="#083344" stroke="#71efaf" stroke-width="2.5"/>
  <circle cx="48" cy="42" r="4" fill="#ffffff"/>

  <circle cx="72" cy="42" r="11" fill="#083344" stroke="#71efaf" stroke-width="2.5"/>
  <circle cx="72" cy="42" r="4" fill="#ffffff"/>

  <circle cx="60" cy="62" r="13" fill="#064e3b" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="60" cy="62" r="5" fill="#ffffff"/>

  <!-- High Collared White Research Mantle -->
  <polygon points="34,80 60,72 86,80 92,106 28,106" fill="#0f2928" stroke="#71efaf" stroke-width="2"/>
  <polygon points="60,72 66,92 54,92" fill="#38bdf8"/>
</svg>'''

    # Mellda: Border Lead - Razor-Wire Halo & Barbed Tactical Trench Visor
    svgs["avatar_core_mellda.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <!-- Razor Crested Boundary Frame -->
  <polygon points="60,6 80,18 114,18 104,50 116,84 84,84 60,114 36,84 4,84 16,50 6,18 40,18" fill="#1f0a0d" stroke="#ef5b55" stroke-width="3.5"/>

  <!-- Jagged Razor-Wire Halo -->
  <path d="M 28,26 L 40,32 L 50,22 L 60,34 L 70,22 L 80,32 L 92,26" fill="none" stroke="#f1df76" stroke-width="2.5"/>

  <!-- High-Tech Trench Recon Visor -->
  <polygon points="34,44 86,44 82,70 60,82 38,70" fill="#2d0f14" stroke="#ef5b55" stroke-width="2"/>
  <line x1="38" y1="56" x2="82" y2="56" stroke="#38bdf8" stroke-width="3.5"/>
  <circle cx="60" cy="56" r="4" fill="#ffffff"/>

  <!-- Barbed Wire Gorget Collar -->
  <rect x="32" y="86" width="56" height="14" rx="3" fill="#0a0304" stroke="#f1df76" stroke-width="2"/>
  <line x1="36" y1="93" x2="84" y2="93" stroke="#ef5b55" stroke-width="2" stroke-dasharray="4 3"/>
</svg>'''

    # Marjuk: Archive Lead - Clockwork Gear Eyepiece, Floating Quill & Old Parchment
    svgs["avatar_core_marjuk.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <!-- Antique Archival Arch Frame -->
  <path d="M 16,110 L 16,46 Q 60,6 104,46 L 104,110 Z" fill="#140824" stroke="#c084fc" stroke-width="3.5"/>

  <!-- Deep Hooded Cowl Silhouette -->
  <path d="M 26,44 Q 60,22 94,44 L 88,86 Q 60,98 32,86 Z" fill="#200d38" stroke="#f1df76" stroke-width="2"/>

  <!-- Clockwork Cog Left Eyepiece & Monocle Chain -->
  <circle cx="48" cy="56" r="14" fill="#0e041a" stroke="#f1df76" stroke-width="2.5" stroke-dasharray="4 3"/>
  <circle cx="48" cy="56" r="5" fill="#38bdf8"/>
  <path d="M 48,70 Q 56,86 70,86" fill="none" stroke="#f1df76" stroke-width="1.5"/>

  <!-- Floating Glowing Quill Feather -->
  <path d="M 76,30 Q 94,20 90,44 Q 84,40 76,46 Z" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>

  <!-- Rolled Archive Scroll Clasp -->
  <rect x="40" y="92" width="40" height="14" rx="4" fill="#fef08a" stroke="#7e22ce" stroke-width="2"/>
  <line x1="48" y1="99" x2="72" y2="99" stroke="#3b0764" stroke-width="2"/>
</svg>'''

    # Ishall: The Outsider - Asymmetrical Shadow Cowl & Inverted Crossed Daggers
    svgs["avatar_core_ishall.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <!-- Jagged Shadow Crescent Frame -->
  <polygon points="60,4 114,20 100,70 114,114 60,98 6,114 20,70 6,20" fill="#0a050f" stroke="#ef5b55" stroke-width="3.5"/>

  <!-- Crossed Inverted Throwing Daggers Behind Head -->
  <line x1="24" y1="20" x2="96" y2="96" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>
  <polygon points="96,96 86,94 94,86" fill="#ef5b55"/>
  <line x1="96" y1="20" x2="24" y2="96" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>
  <polygon points="24,96 34,94 26,86" fill="#ef5b55"/>

  <!-- Asymmetric Phantom Shadow Mask -->
  <polygon points="34,34 86,28 92,76 64,88 28,70" fill="#170d24" stroke="#ffffff" stroke-width="2"/>
  
  <!-- Single Predatory Glowing Red Eye -->
  <polygon points="44,52 68,48 62,60" fill="#ef5b55" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="56" cy="54" r="3" fill="#ffffff"/>
</svg>'''

    # Xyan: The Exile - Weathered Frontier Goggles, Sand Scarf & Compass
    svgs["avatar_core_xyan.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <!-- Weathered Desolate Star Frame -->
  <polygon points="60,4 76,26 106,14 100,44 118,66 92,78 94,110 64,98 44,116 34,88 6,86 16,56 4,28 34,32" fill="#1f1807" stroke="#f1df76" stroke-width="3.5"/>

  <!-- Broad Desert Wanderer Cowl -->
  <path d="M 28,40 Q 60,18 92,40 L 96,92 Q 60,108 24,92 Z" fill="#382908" stroke="#d97706" stroke-width="2"/>

  <!-- Heavy Reinforced Sand Goggles -->
  <rect x="34" y="44" width="22" height="16" rx="4" fill="#082f49" stroke="#f1df76" stroke-width="2"/>
  <circle cx="45" cy="52" r="5" fill="#38bdf8"/>
  <rect x="64" y="44" width="22" height="16" rx="4" fill="#082f49" stroke="#f1df76" stroke-width="2"/>
  <circle cx="75" cy="52" r="5" fill="#38bdf8"/>
  <line x1="56" y1="52" x2="64" y2="52" stroke="#f1df76" stroke-width="3"/>

  <!-- Barbed Sand-Scarf & Compass Medallion -->
  <path d="M 32,74 Q 60,90 88,74 L 84,94 L 36,94 Z" fill="#523d0c" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="60" cy="88" r="7" fill="#ef5b55" stroke="#ffffff" stroke-width="1.5"/>
</svg>'''

    # Secondary Characters Avatars
    # Agent Minho: Tactical Helmet with Cracked Visor & Antenna
    svgs["avatar_char_minho.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 110,24 110,84 60,114 10,84 10,24" fill="#081422" stroke="#38bdf8" stroke-width="3.5"/>
  <!-- Tactical Radio Antenna -->
  <line x1="86" y1="20" x2="102" y2="4" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
  <circle cx="102" cy="4" r="3" fill="#ef5b55"/>
  <!-- Helmet Dome & Cracked Blue Visor Glass -->
  <path d="M 32,36 Q 60,18 88,36 L 90,78 L 30,78 Z" fill="#16273c" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="38,46 82,46 78,66 42,66" fill="#0284c7" stroke="#ffffff" stroke-width="1.5"/>
  <path d="M 60,48 L 54,58 L 68,62" fill="none" stroke="#ffffff" stroke-width="2"/>
  <rect x="36" y="82" width="48" height="14" rx="3" fill="#0a121c" stroke="#f1df76" stroke-width="1.5"/>
</svg>'''

    # Merchant Doha: Ornate Coin Turban & Scales Monocle
    svgs["avatar_char_doha.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="#261704" stroke="#f1df76" stroke-width="4"/>
  <!-- Gold Merchant Turban with Giant Jewel -->
  <path d="M 28,42 C 28,18 92,18 92,42 C 92,54 28,54 28,42 Z" fill="#452a07" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="60" cy="30" r="9" fill="#ef5b55" stroke="#ffffff" stroke-width="2"/>
  <!-- Gold Monocle & Mustache -->
  <circle cx="48" cy="58" r="11" fill="#fef08a" stroke="#d97706" stroke-width="2.5"/>
  <path d="M 40,78 Q 60,86 80,78" fill="none" stroke="#f1df76" stroke-width="3"/>
  <rect x="42" y="88" width="36" height="14" rx="3" fill="#140b02" stroke="#f1df76" stroke-width="1.5"/>
</svg>'''

    # Researcher Soojin: Dual Vials & Safety Goggles
    svgs["avatar_char_soojin.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,60 60,114 6,60" fill="#042022" stroke="#06b6d4" stroke-width="3.5"/>
  <!-- Safety Goggles on Forehead -->
  <rect x="34" y="24" width="22" height="14" rx="4" fill="#083344" stroke="#38bdf8" stroke-width="2"/>
  <rect x="64" y="24" width="22" height="14" rx="4" fill="#083344" stroke="#38bdf8" stroke-width="2"/>
  <line x1="56" y1="31" x2="64" y2="31" stroke="#38bdf8" stroke-width="2"/>
  <!-- Face & Hair -->
  <circle cx="60" cy="56" r="22" fill="#153638" stroke="#71efaf" stroke-width="2"/>
  <!-- Dual Glowing Chemical Vials on Coat -->
  <rect x="32" y="78" width="12" height="26" rx="3" fill="#06b6d4" stroke="#ffffff" stroke-width="1.5"/>
  <rect x="76" y="78" width="12" height="26" rx="3" fill="#ef4444" stroke="#ffffff" stroke-width="1.5"/>
</svg>'''

    # Civilian Sora: Weeping Locket & Mourning Shawl
    svgs["avatar_char_sora.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 110,32 110,88 60,116 10,88 10,32" fill="#1f1404" stroke="#f59e0b" stroke-width="3.5"/>
  <!-- Weeping Mourning Shawl Silhouette -->
  <path d="M 30,34 Q 60,16 90,34 L 96,96 L 24,96 Z" fill="#3b2707" stroke="#f1df76" stroke-width="2"/>
  <!-- Weeping Tear Glass Locket on Neck -->
  <path d="M 60,60 C 50,48 40,62 60,82 C 80,62 70,48 60,60 Z" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
  <circle cx="60" cy="68" r="4" fill="#ffffff"/>
</svg>'''

    # Captain Taeho: Blast Shield Helmet & Crossed Batons
    svgs["avatar_char_taeho.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,24 100,94 60,114 20,94 6,24" fill="#240707" stroke="#ef4444" stroke-width="3.5"/>
  <!-- Crossed Heavy Riot Batons -->
  <line x1="26" y1="24" x2="94" y2="92" stroke="#f1df76" stroke-width="5" stroke-linecap="round"/>
  <line x1="94" y1="24" x2="26" y2="92" stroke="#f1df76" stroke-width="5" stroke-linecap="round"/>
  <!-- Heavy Vanguard Blast Visor -->
  <rect x="32" y="40" width="56" height="34" rx="6" fill="#120404" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="38" y="48" width="44" height="12" rx="2" fill="#ef4444" stroke="#ffffff" stroke-width="1.5"/>
</svg>'''

    # Caravan Master Kael: Sextant Compass & Broad Hat
    svgs["avatar_char_kael.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="40,4 80,4 116,40 116,80 80,116 40,116 4,80 4,40" fill="#241503" stroke="#d97706" stroke-width="3.5"/>
  <!-- Broad Brimmed Desert Navigator Hat -->
  <ellipse cx="60" cy="40" rx="44" ry="14" fill="#4d3007" stroke="#f1df76" stroke-width="2"/>
  <path d="M 42,40 Q 60,20 78,40 Z" fill="#694109" stroke="#f1df76" stroke-width="1.5"/>
  <!-- Navigational Sextant Compass Emblem -->
  <circle cx="60" cy="74" r="18" fill="#140b02" stroke="#d97706" stroke-width="2"/>
  <line x1="60" y1="58" x2="60" y2="90" stroke="#f1df76" stroke-width="2"/>
  <line x1="44" y1="74" x2="76" y2="74" stroke="#f1df76" stroke-width="2"/>
  <polygon points="60,62 64,74 60,70 56,74" fill="#ef4444"/>
</svg>'''

    # Weaver Yeonhwa: Spindle Hairpins & Silk Loom Web
    svgs["avatar_char_yeonhwa.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="#18072b" stroke="#a855f7" stroke-width="4"/>
  <!-- Clockwork Spindle Hairpins -->
  <line x1="28" y1="18" x2="92" y2="52" stroke="#f1df76" stroke-width="3"/>
  <circle cx="28" cy="18" r="5" fill="#38bdf8"/>
  <line x1="92" y1="18" x2="28" y2="52" stroke="#f1df76" stroke-width="3"/>
  <circle cx="92" cy="18" r="5" fill="#38bdf8"/>
  <!-- Spider Web Silk Pattern -->
  <polygon points="60,32 82,50 74,78 46,78 38,50" fill="none" stroke="#c084fc" stroke-width="2"/>
  <line x1="60" y1="32" x2="60" y2="78" stroke="#a855f7" stroke-width="1.5"/>
  <circle cx="60" cy="55" r="7" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
</svg>'''

    # Engineer Joon: Furnace Smelter Visor & Crucible Tongs
    svgs["avatar_char_joon.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,32 114,88 60,114 6,88 6,32" fill="#260f04" stroke="#ea580c" stroke-width="3.5"/>
  <!-- Smelter Crucible Tongs Insignia -->
  <path d="M 30,30 Q 60,60 90,30" fill="none" stroke="#f1df76" stroke-width="4"/>
  <!-- Welder Hood with Glowing Molten Hearth Window -->
  <rect x="34" y="38" width="52" height="38" rx="6" fill="#120602" stroke="#ea580c" stroke-width="2.5"/>
  <ellipse cx="60" cy="56" rx="20" ry="10" fill="#f97316" stroke="#fef08a" stroke-width="2"/>
  <circle cx="60" cy="56" r="4" fill="#ffffff"/>
  <rect x="38" y="86" width="44" height="14" rx="3" fill="#0a0301" stroke="#f1df76" stroke-width="1.5"/>
</svg>'''

    # High Architects Group Icon: Masonry Compass & Golden Plumb-Bob
    svgs["avatar_char_high_architects.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 116,60 60,116 4,60" fill="#1a1402" stroke="#f1df76" stroke-width="4"/>
  <!-- Drafting Compass & Hexagonal Grid -->
  <polygon points="60,20 92,76 28,76" fill="none" stroke="#f1df76" stroke-width="3.5"/>
  <line x1="60" y1="20" x2="60" y2="96" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="60" cy="98" r="6" fill="#ef5b55" stroke="#ffffff" stroke-width="2"/>
  <circle cx="60" cy="20" r="7" fill="#f1df76"/>
</svg>'''

    # Cheonbulok Refugees Group Icon: Huddled Shelter with Glowing Hope Lantern
    svgs["avatar_char_cheonbulok_refugees.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 112,32 112,88 60,114 8,88 8,32" fill="#0f1926" stroke="#38bdf8" stroke-width="3.5"/>
  <!-- Tent Shelter Canopy -->
  <polygon points="60,22 102,74 18,74" fill="#1b2a3d" stroke="#f1df76" stroke-width="2.5"/>
  <!-- Huddled Silhouettes & Golden Lantern -->
  <circle cx="44" cy="62" r="8" fill="#080f17" stroke="#38bdf8" stroke-width="1.5"/>
  <circle cx="76" cy="62" r="8" fill="#080f17" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="54" y="52" width="12" height="20" rx="3" fill="#f1df76" stroke="#ffffff" stroke-width="2"/>
  <circle cx="60" cy="62" r="3" fill="#ef5b55"/>
</svg>'''

    # ==========================================
    # 2. DEPARTMENT FLOOR ICONS (100% Bespoke Shapes & Numerals)
    # ==========================================

    # Floor 1: Neutral Command - Pyramid Spire & Sovereign Eye
    svgs["icon_dept_f1_neutral.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,84 60,116 6,84 6,24" fill="#051f15" stroke="#71efaf" stroke-width="3.5"/>
  <!-- Stepped Pyramid Spire -->
  <polygon points="60,16 92,82 28,82" fill="#0a3827" stroke="#71efaf" stroke-width="2.5"/>
  <line x1="44" y1="52" x2="76" y2="52" stroke="#f1df76" stroke-width="2"/>
  <line x1="36" y1="68" x2="84" y2="68" stroke="#f1df76" stroke-width="2"/>
  <!-- Sovereign Eye Core -->
  <circle cx="60" cy="38" r="8" fill="#f1df76" stroke="#ffffff" stroke-width="1.5"/>
  <text x="60" y="104" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">F-01</text>
</svg>'''

    # Floor 2: Maw's Keep - Heavy Anvil & Sledgehammer
    svgs["icon_dept_f2_maws_keep.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,26 98,96 60,116 22,96 6,26" fill="#24070a" stroke="#ef5b55" stroke-width="3.5"/>
  <!-- Heavy Anvil Silhouette -->
  <path d="M 28,40 L 92,40 L 84,54 L 72,54 L 76,74 L 88,80 L 32,80 L 44,74 L 48,54 L 36,54 Z" fill="#421016" stroke="#ef5b55" stroke-width="2.5"/>
  <!-- Crushing Sledgehammer Head -->
  <rect x="46" y="22" width="28" height="14" rx="2" fill="#f1df76" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="60" y1="12" x2="60" y2="34" stroke="#ffffff" stroke-width="3"/>
  <text x="60" y="102" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">F-02</text>
</svg>'''

    # Floor 3: Extraction Hall - Alchemical Retort & Siphon Tubes
    svgs["icon_dept_f3_extraction.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="36,4 84,4 116,36 116,84 84,116 36,116 4,84 4,36" fill="#041a29" stroke="#38bdf8" stroke-width="3.5"/>
  <!-- Distillation Retort Flask with Bubbling Fluid -->
  <path d="M 52,20 L 68,20 L 68,42 L 86,74 C 92,86 78,92 60,92 C 42,92 28,86 34,74 L 52,42 Z" fill="#083a5c" stroke="#38bdf8" stroke-width="2.5"/>
  <circle cx="60" cy="74" r="10" fill="#f1df76"/>
  <circle cx="48" cy="68" r="4" fill="#ffffff"/>
  <circle cx="70" cy="62" r="3" fill="#ffffff"/>
  <text x="60" y="108" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">F-03</text>
</svg>'''

    # Floor 4: Insight Forge - Prismatic Compass Star & Neural Brain
    svgs["icon_dept_f4_insight_forge.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 112,32 112,88 60,116 8,88 8,32" fill="#211802" stroke="#f1df76" stroke-width="3.5"/>
  <!-- 6-Pointed Prismatic Compass Star -->
  <polygon points="60,18 70,42 96,44 76,60 84,84 60,70 36,84 44,60 24,44 50,42" fill="#4d3b07" stroke="#f1df76" stroke-width="2"/>
  <circle cx="60" cy="54" r="12" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
  <text x="60" y="106" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">F-04</text>
</svg>'''

    # Floor 5: Border Watch - Fortress Bulwark Parapet & Searchlight
    svgs["icon_dept_f5_border_watch.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,24 100,94 60,114 20,94 6,24" fill="#24070a" stroke="#ef5b55" stroke-width="3.5"/>
  <!-- Battlement Wall Parapets -->
  <polygon points="28,34 40,34 40,44 52,44 52,34 68,34 68,44 80,44 80,34 92,34 88,80 32,80" fill="#421217" stroke="#ef5b55" stroke-width="2.5"/>
  <!-- Crossed Searchlight Cones -->
  <polygon points="60,54 36,24 48,24" fill="#f1df76" opacity="0.8"/>
  <polygon points="60,54 84,24 72,24" fill="#f1df76" opacity="0.8"/>
  <circle cx="60" cy="58" r="6" fill="#ffffff" stroke="#ef5b55" stroke-width="1.5"/>
  <text x="60" y="102" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">F-05</text>
</svg>'''

    # Floor 6: Deep Vault - Giant Bank Vault Gear & Triple Lock Tumblers
    svgs["icon_dept_f6_deep_vault.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="#150626" stroke="#c084fc" stroke-width="4"/>
  <!-- Giant Vault Gear Teeth -->
  <circle cx="60" cy="52" r="32" fill="#250d40" stroke="#f1df76" stroke-width="2.5" stroke-dasharray="6 4"/>
  <!-- 3 Concentric Keyhole Tumblers -->
  <circle cx="60" cy="52" r="18" fill="#08020f" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="60" cy="48" r="5" fill="#f1df76"/>
  <polygon points="57,48 63,48 65,60 55,60" fill="#f1df76"/>
  <text x="60" y="106" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">F-06</text>
</svg>'''

    # Floor 7: Shadow Corps - Twin Crescent Scythes & Shadow Dagger
    svgs["icon_dept_f7_shadow_corps.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,20 100,70 114,114 60,98 6,114 20,70 6,20" fill="#140407" stroke="#ef5b55" stroke-width="3.5"/>
  <!-- Twin Inverted Crescent Scythe Blades -->
  <path d="M 30,30 Q 60,50 30,80 Q 54,60 30,30 Z" fill="#ef5b55" stroke="#ffffff" stroke-width="1.5"/>
  <path d="M 90,30 Q 60,50 90,80 Q 66,60 90,30 Z" fill="#ef5b55" stroke="#ffffff" stroke-width="1.5"/>
  <!-- Center Shadow Stiletto -->
  <polygon points="60,18 66,66 60,82 54,66" fill="#f1df76" stroke="#ffffff" stroke-width="1.5"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">F-07</text>
</svg>'''

    # Floor 8: Gate Watch - Stone Gateway Arch & Portcullis
    svgs["icon_dept_f8_gate_watch.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="36,4 84,4 116,36 116,84 84,116 36,116 4,84 4,36" fill="#211802" stroke="#f1df76" stroke-width="3.5"/>
  <!-- Monumental Stone Archway -->
  <path d="M 28,84 L 28,42 Q 60,14 92,42 L 92,84 L 76,84 L 76,52 Q 60,34 44,52 L 44,84 Z" fill="#4d3b07" stroke="#f1df76" stroke-width="2.5"/>
  <!-- Dropped Iron Portcullis Grate -->
  <line x1="50" y1="46" x2="50" y2="84" stroke="#ef5b55" stroke-width="2"/>
  <line x1="60" y1="40" x2="60" y2="84" stroke="#ef5b55" stroke-width="2"/>
  <line x1="70" y1="46" x2="70" y2="84" stroke="#ef5b55" stroke-width="2"/>
  <text x="60" y="106" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">F-08</text>
</svg>'''

    # Sync synonyms for Floor icons
    svgs["floor-1-command.svg"] = svgs["icon_dept_f1_neutral.svg"]
    svgs["floor-2-maw.svg"] = svgs["icon_dept_f2_maws_keep.svg"]
    svgs["floor-3-extraction.svg"] = svgs["icon_dept_f3_extraction.svg"]
    svgs["floor-4-insight.svg"] = svgs["icon_dept_f4_insight_forge.svg"]
    svgs["floor-5-border.svg"] = svgs["icon_dept_f5_border_watch.svg"]
    svgs["floor-6-vault.svg"] = svgs["icon_dept_f6_deep_vault.svg"]
    svgs["floor-7-shadow.svg"] = svgs["icon_dept_f7_shadow_corps.svg"]
    svgs["floor-8-gate.svg"] = svgs["icon_dept_f8_gate_watch.svg"]

    # ==========================================
    # 3. FACTION CRESTS (100% Bespoke Insignias)
    # ==========================================

    # The Reverie Directorate: Open Palm Cradling All-Seeing Eye with 5 Flux Beacons
    svgs["icon_faction_reverie_directorate.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,84 60,116 6,84 6,24" fill="#24070a" stroke="#ef5b55" stroke-width="3.5"/>
  <!-- Open Palm Cradling Eye -->
  <path d="M 32,82 C 30,56 42,40 50,22 L 58,22 C 58,34 60,42 62,20 L 70,20 C 70,34 72,42 74,24 L 82,24 C 80,44 88,54 88,82 Z" fill="#4a1219" stroke="#f1df76" stroke-width="2"/>
  <!-- Radiant All-Seeing Central Eye -->
  <ellipse cx="60" cy="58" rx="16" ry="10" fill="#0b0304" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="60" cy="58" r="5" fill="#f1df76"/>
</svg>'''

    # The High Council: Triangular Sovereign Citadel & 3 Scepters
    svgs["icon_faction_high_council.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 116,96 4,96" fill="#261b02" stroke="#f1df76" stroke-width="4"/>
  <!-- Inner Sovereign Citadel Scepters -->
  <line x1="60" y1="26" x2="60" y2="86" stroke="#f1df76" stroke-width="4"/>
  <circle cx="60" cy="24" r="6" fill="#ef5b55" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="42" y1="46" x2="78" y2="82" stroke="#f1df76" stroke-width="3"/>
  <line x1="78" y1="46" x2="42" y2="82" stroke="#f1df76" stroke-width="3"/>
  <polygon points="60,44 76,72 44,72" fill="#594008" stroke="#38bdf8" stroke-width="2"/>
</svg>'''

    # The High Architects: Masonry Square & Hexagonal Compass
    svgs["icon_faction_architects.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 112,32 112,88 60,114 8,88 8,32" fill="#211802" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="60,20 94,78 26,78" fill="none" stroke="#f1df76" stroke-width="3.5"/>
  <circle cx="60" cy="20" r="6" fill="#f1df76"/>
  <rect x="36" y="56" width="48" height="8" rx="2" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
</svg>'''

    # The Collectors: Grasping Bird Talon & Brass Key
    svgs["icon_faction_collectors.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="#140624" stroke="#c084fc" stroke-width="4"/>
  <!-- Grasping Bird Talon -->
  <path d="M 30,30 Q 60,60 40,84 M 60,24 L 60,88 M 90,30 Q 60,60 80,84" fill="none" stroke="#f1df76" stroke-width="4" stroke-linecap="round"/>
  <!-- Ornate Key in Center -->
  <circle cx="60" cy="42" r="10" fill="#0a0212" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="60" y1="52" x2="60" y2="80" stroke="#f1df76" stroke-width="3"/>
  <line x1="60" y1="72" x2="70" y2="72" stroke="#f1df76" stroke-width="3"/>
</svg>'''

    # The Giltong Enforcers: Spiked Octagonal Badge & Heavy Truncheons
    svgs["icon_faction_giltong.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="36,4 84,4 116,36 116,84 84,116 36,116 4,84 4,36" fill="#240707" stroke="#ef4444" stroke-width="4"/>
  <!-- Crossed Heavy Truncheons -->
  <line x1="26" y1="26" x2="94" y2="94" stroke="#f1df76" stroke-width="6" stroke-linecap="round"/>
  <line x1="94" y1="26" x2="26" y2="94" stroke="#f1df76" stroke-width="6" stroke-linecap="round"/>
  <circle cx="60" cy="60" r="16" fill="#0f0202" stroke="#ef4444" stroke-width="3"/>
  <polygon points="60,48 68,60 60,72 52,60" fill="#ffffff"/>
</svg>'''

    # The SED Corps: Exploration Radar Dish & Sonar Pulses
    svgs["icon_faction_sed_corps.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 116,60 60,116 4,60" fill="#041b29" stroke="#38bdf8" stroke-width="3.5"/>
  <!-- Concentric Sonar Pulses -->
  <circle cx="60" cy="60" r="38" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 4"/>
  <circle cx="60" cy="60" r="24" fill="none" stroke="#71efaf" stroke-width="2"/>
  <circle cx="60" cy="60" r="10" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
  <line x1="60" y1="22" x2="60" y2="98" stroke="#ffffff" stroke-width="2"/>
</svg>'''

    # The UCD Strike Force: Tactical Riot Shield & Crosshairs
    svgs["icon_faction_ucd_strike.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,24 100,96 60,114 20,96 6,24" fill="#240707" stroke="#ef4444" stroke-width="3.5"/>
  <!-- Sniper Crosshairs & Reticle -->
  <circle cx="60" cy="58" r="26" fill="none" stroke="#ffffff" stroke-width="2.5"/>
  <line x1="60" y1="24" x2="60" y2="92" stroke="#ef4444" stroke-width="3"/>
  <line x1="26" y1="58" x2="94" y2="58" stroke="#ef4444" stroke-width="3"/>
  <circle cx="60" cy="58" r="6" fill="#ef4444"/>
</svg>'''

    # The Master Weavers: Clockwork Spider Loom
    svgs["icon_faction_weavers.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="#18072b" stroke="#a855f7" stroke-width="4"/>
  <!-- Articulated Spider Chassis -->
  <circle cx="60" cy="54" r="14" fill="#2e1065" stroke="#f1df76" stroke-width="2"/>
  <path d="M 46,50 L 20,30 M 46,54 L 16,54 M 46,58 L 22,78" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
  <path d="M 74,50 L 100,30 M 74,54 L 104,54 M 74,58 L 98,78" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
  <circle cx="60" cy="54" r="5" fill="#ffffff"/>
</svg>'''

    # The Bulwark Wardens: Battlement Parapet & Halberds
    svgs["icon_faction_wardens.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,26 98,96 60,116 22,96 6,26" fill="#042116" stroke="#10b981" stroke-width="3.5"/>
  <!-- Fortress Battlement Tower -->
  <polygon points="36,40 48,40 48,48 60,48 60,40 72,40 72,48 84,48 84,40 84,84 36,84" fill="#083d29" stroke="#71efaf" stroke-width="2"/>
  <line x1="60" y1="20" x2="60" y2="84" stroke="#f1df76" stroke-width="3"/>
  <polygon points="60,14 66,26 54,26" fill="#f1df76"/>
</svg>'''

    # Copy to faction synonyms
    svgs["fac_reverie_directorate.svg"] = svgs["icon_faction_reverie_directorate.svg"]
    svgs["fac_high_council.svg"] = svgs["icon_faction_high_council.svg"]
    svgs["fac_architects.svg"] = svgs["icon_faction_architects.svg"]
    svgs["fac_collectors.svg"] = svgs["icon_faction_collectors.svg"]
    svgs["fac_giltong_enforcers.svg"] = svgs["icon_faction_giltong.svg"]
    svgs["fac_sed_corps.svg"] = svgs["icon_faction_sed_corps.svg"]
    svgs["fac_ucd_strike.svg"] = svgs["icon_faction_ucd_strike.svg"]
    svgs["fac_weavers.svg"] = svgs["icon_faction_weavers.svg"]
    svgs["fac_wardens.svg"] = svgs["icon_faction_wardens.svg"]

    # ==========================================
    # 4. CITY LOCATIONS & ZONES (100% Bespoke Shapes)
    # ==========================================

    # Zone A: Core Spire Needle
    svgs["icon_zone_a_core.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 116,60 60,116 4,60" fill="#261b02" stroke="#f1df76" stroke-width="3.5"/>
  <!-- Tall Citadel Spire Needle -->
  <polygon points="60,12 68,88 52,88" fill="#f1df76" stroke="#ffffff" stroke-width="1.5"/>
  <ellipse cx="60" cy="50" rx="34" ry="12" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <ellipse cx="60" cy="70" rx="24" ry="8" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="60" cy="12" r="4" fill="#ffffff"/>
</svg>'''

    # Zone B: West Ward - Dense Alleyway Stacks
    svgs["icon_zone_b_west.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="36,4 84,4 116,36 116,84 84,116 36,116 4,84 4,36" fill="#240c02" stroke="#ea580c" stroke-width="3.5"/>
  <!-- Overlapping Slum Tenements -->
  <rect x="22" y="44" width="28" height="46" fill="#4d1c07" stroke="#f1df76" stroke-width="1.5"/>
  <rect x="44" y="28" width="32" height="62" fill="#69260a" stroke="#f1df76" stroke-width="2"/>
  <rect x="70" y="52" width="28" height="38" fill="#4d1c07" stroke="#f1df76" stroke-width="1.5"/>
  <path d="M 36,54 L 40,54 M 58,40 L 62,40 M 82,62 L 86,62" stroke="#fef08a" stroke-width="2"/>
</svg>'''

    # Zone C: Collector's Row - Open Treasure Chest & Relics
    svgs["icon_zone_c_east.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="#140624" stroke="#c084fc" stroke-width="4"/>
  <!-- Open Relic Chest -->
  <path d="M 26,44 Q 60,20 94,44 L 90,82 L 30,82 Z" fill="#2b0d4d" stroke="#f1df76" stroke-width="2.5"/>
  <ellipse cx="60" cy="44" rx="34" ry="12" fill="#0a0212" stroke="#f1df76" stroke-width="2"/>
  <!-- Glowing Relic Gemstone Floating -->
  <polygon points="60,24 72,36 60,48 48,36" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="60" cy="64" r="5" fill="#f1df76"/>
</svg>'''

    # Zone D: Han Smelters - Triple Furnace Chimneys
    svgs["icon_zone_d_flanks.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 112,32 112,88 60,114 8,88 8,32" fill="#031a10" stroke="#10b981" stroke-width="3.5"/>
  <!-- Triple Smoking Industrial Chimneys -->
  <polygon points="28,46 36,46 40,86 24,86" fill="#09452b" stroke="#71efaf" stroke-width="1.5"/>
  <polygon points="52,32 68,32 72,86 48,86" fill="#0f5c3b" stroke="#71efaf" stroke-width="2"/>
  <polygon points="84,46 92,46 96,86 80,86" fill="#09452b" stroke="#71efaf" stroke-width="1.5"/>
  <!-- Violet Exhaust Smoke Clouds -->
  <circle cx="60" cy="22" r="8" fill="#c084fc" opacity="0.8"/>
  <circle cx="32" cy="36" r="6" fill="#c084fc" opacity="0.7"/>
  <circle cx="88" cy="36" r="6" fill="#c084fc" opacity="0.7"/>
</svg>'''

    # Zone E: Perimeter Bulwark - Massive Defense Wall & Railgun Turret
    svgs["icon_zone_e_bulwark.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,24 100,94 60,114 20,94 6,24" fill="#240707" stroke="#ef4444" stroke-width="3.5"/>
  <!-- Massive High Wall -->
  <rect x="20" y="56" width="80" height="32" fill="#4d1216" stroke="#f1df76" stroke-width="2"/>
  <!-- Heavy Automated Railgun Turret -->
  <circle cx="60" cy="56" r="14" fill="#140305" stroke="#ef4444" stroke-width="2"/>
  <line x1="60" y1="56" x2="88" y2="28" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>
</svg>'''

    # General Locations
    # The Maw: Gaping Chasm Crater with Obsidian Fangs
    svgs["icon_loc_the_maw.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 116,60 60,116 4,60" fill="#051421" stroke="#38bdf8" stroke-width="3.5"/>
  <!-- Gaping Chasm Mouth -->
  <ellipse cx="60" cy="60" rx="38" ry="24" fill="#000000" stroke="#ef5b55" stroke-width="3"/>
  <!-- Jagged Rock Fangs -->
  <polygon points="34,48 42,62 50,48" fill="#ffffff"/>
  <polygon points="70,48 78,62 86,48" fill="#ffffff"/>
  <polygon points="44,72 52,58 60,72" fill="#ffffff"/>
  <polygon points="60,72 68,58 76,72" fill="#ffffff"/>
</svg>'''

    # The Desolate: Barren Desert with Dead Tree & Dust Storm
    svgs["icon_loc_the_desolate.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,26 98,96 60,116 22,96 6,26" fill="#260808" stroke="#ef4444" stroke-width="3.5"/>
  <!-- Desert Dunes -->
  <path d="M 12,80 Q 40,64 70,76 T 108,70 L 108,96 L 12,96 Z" fill="#4d1414" stroke="#f1df76" stroke-width="2"/>
  <!-- Dead Gnarled Tree -->
  <path d="M 44,78 L 48,46 L 36,34 M 48,46 L 62,32 M 48,56 L 60,50" fill="none" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
  <!-- Swirling Red Dust Storm -->
  <path d="M 68,36 Q 92,28 86,48 Q 78,60 102,52" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="3 3"/>
</svg>'''

    # The Hollow Glass: Shattered Crystal Dome
    svgs["icon_loc_the_hollow_glass.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="#041829" stroke="#38bdf8" stroke-width="4"/>
  <!-- Transparent Glass Dome -->
  <path d="M 22,76 Q 60,18 98,76 Z" fill="#0a324d" opacity="0.6" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Shattered Cracks Through Glass -->
  <path d="M 60,32 L 52,54 L 72,62 L 64,76" fill="none" stroke="#ffffff" stroke-width="2.5"/>
  <path d="M 52,54 L 34,60" fill="none" stroke="#ffffff" stroke-width="2"/>
  <path d="M 72,62 L 88,58" fill="none" stroke="#ffffff" stroke-width="2"/>
</svg>'''

    # ==========================================
    # 5. NAVIGATION & CATEGORY MASTER ICONS
    # ==========================================
    svgs["nav_entities.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,24 100,96 60,114 20,96 6,24" fill="#24070a" stroke="#ef5b55" stroke-width="3.5"/>
  <circle cx="60" cy="56" r="24" fill="#080203" stroke="#f1df76" stroke-width="2.5"/>
  <path d="M 44,54 Q 60,34 76,54 Q 60,74 44,54 Z" fill="#ef5b55" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="60" cy="54" r="5" fill="#ffffff"/>
</svg>'''

    svgs["nav_maw.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 116,60 60,116 4,60" fill="#031624" stroke="#38bdf8" stroke-width="3.5"/>
  <polygon points="60,20 84,76 60,68 36,76" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
  <line x1="60" y1="20" x2="60" y2="94" stroke="#f1df76" stroke-width="3"/>
  <circle cx="60" cy="96" r="5" fill="#ef5b55"/>
</svg>'''

    svgs["nav_departments.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="36,4 84,4 116,36 116,84 84,116 36,116 4,84 4,36" fill="#031f15" stroke="#71efaf" stroke-width="3.5"/>
  <rect x="34" y="34" width="22" height="22" fill="#0a3d2b" stroke="#f1df76" stroke-width="2"/>
  <rect x="64" y="34" width="22" height="22" fill="#0a3d2b" stroke="#f1df76" stroke-width="2"/>
  <rect x="34" y="64" width="22" height="22" fill="#0a3d2b" stroke="#f1df76" stroke-width="2"/>
  <rect x="64" y="64" width="22" height="22" fill="#0a3d2b" stroke="#f1df76" stroke-width="2"/>
</svg>'''

    svgs["nav_characters.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="#211802" stroke="#f1df76" stroke-width="4"/>
  <circle cx="60" cy="46" r="18" fill="#4d3b07" stroke="#38bdf8" stroke-width="2.5"/>
  <path d="M 32,94 C 32,74 44,70 60,70 C 76,70 88,74 88,94 Z" fill="#4d3b07" stroke="#f1df76" stroke-width="2"/>
</svg>'''

    svgs["nav_locations.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,32 114,88 60,116 6,88 6,32" fill="#1f0f04" stroke="#ea580c" stroke-width="3.5"/>
  <polygon points="60,18 90,44 76,88 44,88 30,44" fill="#4d2407" stroke="#f1df76" stroke-width="2"/>
  <circle cx="60" cy="54" r="8" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
</svg>'''

    svgs["nav_lore.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <path d="M 16,110 L 16,36 Q 60,6 104,36 L 104,110 Z" fill="#140624" stroke="#c084fc" stroke-width="3.5"/>
  <path d="M 28,46 Q 60,30 92,46 L 92,92 Q 60,78 28,92 Z" fill="#2b0d4d" stroke="#f1df76" stroke-width="2"/>
  <line x1="60" y1="36" x2="60" y2="86" stroke="#f1df76" stroke-width="2"/>
</svg>'''

    svgs["nav_mechanics.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="36,4 84,4 116,36 116,84 84,116 36,116 4,84 4,36" fill="#041a29" stroke="#38bdf8" stroke-width="3.5"/>
  <!-- Interlocking Mechanical Gears -->
  <circle cx="50" cy="50" r="22" fill="#083857" stroke="#f1df76" stroke-width="2.5" stroke-dasharray="5 3"/>
  <circle cx="50" cy="50" r="8" fill="#ffffff"/>
  <circle cx="78" cy="74" r="16" fill="#083857" stroke="#ef5b55" stroke-width="2" stroke-dasharray="4 2"/>
  <circle cx="78" cy="74" r="5" fill="#ffffff"/>
</svg>'''

    svgs["somnarak_icon.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <!-- Master Somnarak Diamond Crest -->
  <polygon points="60,4 116,60 60,116 4,60" fill="#090d16" stroke="#f1df76" stroke-width="4"/>
  <polygon points="60,14 106,60 60,106 14,60" fill="#05080f" stroke="#38bdf8" stroke-width="2"/>
  <!-- Central Weeping Core & Sovereign Crown -->
  <polygon points="60,24 74,48 60,72 46,48" fill="#ef5b55" stroke="#f1df76" stroke-width="2"/>
  <circle cx="60" cy="48" r="6" fill="#ffffff"/>
  <path d="M 60,72 L 60,98" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
</svg>'''

    # Write all bespoke SVGs to all destination directories!
    for d in target_dirs:
        for fname, svg_content in svgs.items():
            fpath = os.path.join(d, fname)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(svg_content)

    print(f"Successfully created {len(svgs)} completely bespoke, distinct-shape vector SVGs across all target asset directories!")

if __name__ == "__main__":
    generate_all_bespoke_svgs()
