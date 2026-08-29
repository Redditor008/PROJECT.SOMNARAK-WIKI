import os

def generate_canonical_assets():
    icons_dir = "/home/user/01_Somnarak_Wiki/assets/icons"
    avatars_dir = "/home/user/01_Somnarak_Wiki/assets/avatars"
    entities_art_dir = "/home/user/01_Somnarak_Wiki/assets/art/entities"
    banners_dir = "/home/user/01_Somnarak_Wiki/assets/banners"
    user_icons_dir = "/home/user/icons"

    for p in [icons_dir, avatars_dir, entities_art_dir, banners_dir, user_icons_dir]:
        os.makedirs(p, exist_ok=True)

    # =========================================================================
    # 1. CANONICAL DAMAGE TYPE & ELEMENT ICONS
    # Grudge = Crimson, Lament = Deep Blue, Void = Pale White, Weight = Black, Mixed = Rainbow, Hope = Golden
    # =========================================================================
    damage_svgs = {}

    # Grudge (Crimson) - Physical Trauma / Blades & Flames
    damage_svgs["damage_red.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="grudgeGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.95"/>
      <stop offset="60%" stop-color="#991b1b" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#350606" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <!-- Crimson Jagged War-Shield -->
  <polygon points="60,4 116,24 100,96 60,116 20,96 4,24" fill="url(#grudgeGlow)" stroke="#ef4444" stroke-width="4"/>
  <polygon points="60,14 102,30 90,88 60,104 30,88 18,30" fill="#140303" stroke="#fca5a5" stroke-width="2"/>
  
  <!-- Massive Flaming Cleaver & Crimson Rage Spikes -->
  <polygon points="60,18 76,46 70,82 60,94 50,82 44,46" fill="#ffffff" stroke="#ef4444" stroke-width="3"/>
  <polygon points="60,28 68,48 64,76 60,84 56,76 52,48" fill="#ef4444"/>
  <rect x="40" y="78" width="40" height="8" rx="2" fill="#fca5a5" stroke="#7f1d1d" stroke-width="1.5"/>
  <circle cx="60" cy="100" r="5" fill="#ffffff" stroke="#ef4444" stroke-width="2"/>
</svg>'''

    # Lament (Deep Blue) - Mental Anguish / Weeping Acoustic Crystal Eye
    damage_svgs["damage_white.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="lamentGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2563eb" stop-opacity="0.95"/>
      <stop offset="60%" stop-color="#1e3a8a" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#081026" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <!-- Deep Blue Diamond Shield Frame -->
  <polygon points="60,4 116,60 60,116 4,60" fill="url(#lamentGlow)" stroke="#3b82f6" stroke-width="4"/>
  <polygon points="60,16 102,60 60,102 18,60" fill="#030b1e" stroke="#93c5fd" stroke-width="2"/>

  <!-- Weeping Acoustic Eye & Deep Blue Harmonic Crystal -->
  <path d="M 28,60 Q 60,24 92,60 Q 60,96 28,60 Z" fill="#1e40af" stroke="#60a5fa" stroke-width="3"/>
  <circle cx="60" cy="60" r="18" fill="#1d4ed8" stroke="#ffffff" stroke-width="2.5"/>
  <polygon points="60,46 70,60 60,74 50,60" fill="#ffffff"/>
  <path d="M 60,74 L 60,98" stroke="#60a5fa" stroke-width="4" stroke-linecap="round"/>
</svg>'''

    # Void (Pale White) - Soul Dissolution / 8-Pointed Sovereign Stigmata Star
    damage_svgs["damage_pale.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="voidGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
      <stop offset="50%" stop-color="#e2e8f0" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0.95"/>
    </radialGradient>
  </defs>
  <!-- Pale White Hexagonal Frame -->
  <polygon points="60,4 112,32 112,88 60,116 8,88 8,32" fill="url(#voidGlow)" stroke="#ffffff" stroke-width="4"/>
  <polygon points="60,14 102,38 102,82 60,106 18,82 18,38" fill="#090d16" stroke="#e2e8f0" stroke-width="2"/>

  <!-- 8-Pointed Existential Void Star -->
  <polygon points="60,18 66,46 94,52 70,68 76,96 60,78 44,96 50,68 26,52 54,46" fill="#ffffff" stroke="#94a3b8" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="12" fill="#0f172a" stroke="#ffffff" stroke-width="3"/>
  <circle cx="60" cy="60" r="4" fill="#ffffff"/>
</svg>'''

    # Weight (Black) - Gravitational Corrosive Grief / Black Vortex Core
    damage_svgs["damage_black.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="weightGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#27272a" stop-opacity="0.95"/>
      <stop offset="70%" stop-color="#18181b" stop-opacity="0.98"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <!-- Heavy Black Octagonal Bulwark Frame -->
  <polygon points="38,4 82,4 116,38 116,82 82,116 38,116 4,82 4,38" fill="url(#weightGlow)" stroke="#71717a" stroke-width="4"/>
  <polygon points="40,12 80,12 108,40 108,80 80,108 40,108 12,80 12,40" fill="#050505" stroke="#52525b" stroke-width="2"/>

  <!-- Crushing Gravitational Obsidian Monolith & Dual Decay Ring -->
  <circle cx="60" cy="60" r="32" fill="#09090b" stroke="#3f3f46" stroke-width="3"/>
  <polygon points="60,26 84,52 84,76 60,94 36,76 36,52" fill="#000000" stroke="#a1a1aa" stroke-width="2.5"/>
  <line x1="60" y1="26" x2="60" y2="94" stroke="#71717a" stroke-width="3"/>
  <line x1="36" y1="60" x2="84" y2="60" stroke="#71717a" stroke-width="3"/>
  <circle cx="60" cy="60" r="6" fill="#ffffff"/>
</svg>'''

    # Mixed (Rainbow) - Multi-Spectral Resonance
    damage_svgs["damage_mixed.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="rainbowGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="25%" stop-color="#f59e0b"/>
      <stop offset="50%" stop-color="#10b981"/>
      <stop offset="75%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#8b5cf6"/>
    </linearGradient>
  </defs>
  <polygon points="60,4 116,60 60,116 4,60" fill="#0a0a14" stroke="url(#rainbowGrad)" stroke-width="4"/>
  <!-- Concentric Rainbow Rings -->
  <circle cx="60" cy="60" r="36" fill="none" stroke="#ef4444" stroke-width="3"/>
  <circle cx="60" cy="60" r="28" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <circle cx="60" cy="60" r="20" fill="none" stroke="#10b981" stroke-width="3"/>
  <circle cx="60" cy="60" r="12" fill="none" stroke="#3b82f6" stroke-width="3"/>
  <circle cx="60" cy="60" r="5" fill="#8b5cf6"/>
</svg>'''

    # Hope (Golden) - Absolvohan Restoration & Dawn
    damage_svgs["hope_gold.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="hopeGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="1"/>
      <stop offset="60%" stop-color="#eab308" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#713f12" stop-opacity="0.95"/>
    </radialGradient>
  </defs>
  <polygon points="60,4 114,24 114,84 60,116 6,84 6,24" fill="url(#hopeGlow)" stroke="#f1df76" stroke-width="4"/>
  <polygon points="60,14 104,28 104,78 60,104 16,78 16,28" fill="#1c1303" stroke="#fef08a" stroke-width="2"/>
  <!-- Radiant Dawn Sun & Crown of Absolvohan -->
  <circle cx="60" cy="60" r="22" fill="#eab308" stroke="#ffffff" stroke-width="3"/>
  <polygon points="60,20 64,34 78,34 66,44 70,58 60,50 50,58 54,44 42,34 56,34" fill="#ffffff"/>
  <circle cx="60" cy="60" r="8" fill="#ffffff"/>
</svg>'''

    # Synonyms
    damage_svgs["icon_damage_grudge.svg"] = damage_svgs["damage_red.svg"]
    damage_svgs["icon_damage_lament.svg"] = damage_svgs["damage_white.svg"]
    damage_svgs["icon_damage_void.svg"] = damage_svgs["damage_pale.svg"]
    damage_svgs["icon_damage_weight.svg"] = damage_svgs["damage_black.svg"]
    damage_svgs["el_mixed.svg"] = damage_svgs["damage_mixed.svg"]
    damage_svgs["el_hope.svg"] = damage_svgs["hope_gold.svg"]

    for fname, svg_c in damage_svgs.items():
        for d in [icons_dir, user_icons_dir]:
            with open(os.path.join(d, fname), "w", encoding="utf-8") as f:
                f.write(svg_c)

    print("Generated all canonical Damage Type & Element SVGs!")

    # =========================================================================
    # 2. SPECIALIZED CHARACTER & ECHO-CORE EMBLEM ICONS (NO PROFILE HEADS!)
    # Bespoke Signature Artifact / Weapon / Heraldry Icons
    # =========================================================================
    char_emblems = {
        # Majin (Director): Golden Hourglass with Sovereign Scepters & Crown Antennas
        "avatar_core_majin.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,84 60,116 6,84 6,24" fill="#1a0407" stroke="#f1df76" stroke-width="3.5"/>
  <!-- Sovereign Scepters Crossed Behind Hourglass -->
  <line x1="26" y1="26" x2="94" y2="94" stroke="#f1df76" stroke-width="4"/>
  <circle cx="26" cy="26" r="6" fill="#ef5b55"/>
  <line x1="94" y1="26" x2="26" y2="94" stroke="#f1df76" stroke-width="4"/>
  <circle cx="94" cy="26" r="6" fill="#ef5b55"/>
  <!-- Sovereign Golden Hourglass Core -->
  <polygon points="40,36 80,36 44,84 76,84" fill="#ef5b55" stroke="#f1df76" stroke-width="3"/>
  <circle cx="60" cy="60" r="7" fill="#ffffff" stroke="#f1df76" stroke-width="2"/>
  <!-- Crown Finial -->
  <polygon points="48,22 60,12 72,22 60,28" fill="#f1df76"/>
</svg>''',

        # Seiyon (Secretary): Prismatic Holographic Slate Terminal & Cybernetic Stylus
        "avatar_core_seiyon.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 116,60 60,116 4,60" fill="#041524" stroke="#38bdf8" stroke-width="3.5"/>
  <!-- Holographic Terminal Slate -->
  <rect x="30" y="32" width="60" height="56" rx="6" fill="#082845" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Glowing Cyan Data Waves & Stylus -->
  <line x1="38" y1="46" x2="82" y2="46" stroke="#ffffff" stroke-width="2.5"/>
  <line x1="38" y1="58" x2="72" y2="58" stroke="#38bdf8" stroke-width="2.5"/>
  <line x1="38" y1="70" x2="82" y2="70" stroke="#f1df76" stroke-width="2"/>
  <polygon points="76,20 96,40 90,46 70,26" fill="#ffffff" stroke="#38bdf8" stroke-width="1.5"/>
</svg>''',

        # Dekan (Containment Lead): Basalt Fortress Gate & Triple Hydraulic Clamps
        "avatar_core_dekan.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,24 100,96 60,114 20,96 6,24" fill="#21080b" stroke="#ef5b55" stroke-width="3.5"/>
  <!-- Heavy Basalt Vault Gate Slabs -->
  <rect x="28" y="32" width="30" height="56" fill="#421217" stroke="#ef5b55" stroke-width="2"/>
  <rect x="62" y="32" width="30" height="56" fill="#421217" stroke="#ef5b55" stroke-width="2"/>
  <!-- Triple Hydraulic Locking Clamps -->
  <rect x="24" y="40" width="72" height="8" rx="2" fill="#f1df76" stroke="#991b1b" stroke-width="1.5"/>
  <rect x="24" y="56" width="72" height="8" rx="2" fill="#f1df76" stroke="#991b1b" stroke-width="1.5"/>
  <rect x="24" y="72" width="72" height="8" rx="2" fill="#f1df76" stroke="#991b1b" stroke-width="1.5"/>
</svg>''',

        # Zyrak (Extraction Lead): Alchemical Siphon Crucible with Twin Pressurized Han Coils
        "avatar_core_zyrak.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="36,4 84,4 116,36 116,84 84,116 36,116 4,84 4,36" fill="#1f1402" stroke="#f1df76" stroke-width="3.5"/>
  <!-- Han Crucible Body -->
  <path d="M 38,36 L 82,36 L 76,84 Q 60,98 44,84 Z" fill="#4a2e05" stroke="#f1df76" stroke-width="2.5"/>
  <!-- Bubbling Molten Core & Siphon Coils -->
  <circle cx="60" cy="62" r="14" fill="#ef5b55" stroke="#ffffff" stroke-width="2"/>
  <path d="M 28,42 Q 60,20 92,42" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <line x1="60" y1="20" x2="60" y2="44" stroke="#ffffff" stroke-width="3"/>
</svg>''',

        # Ayshuk (Research Lead): Triple Microscope Lens Array & Neural Mandala
        "avatar_core_ayshuk.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 112,32 112,88 60,116 8,88 8,32" fill="#031f18" stroke="#71efaf" stroke-width="3.5"/>
  <!-- Hexagonal Microscope Array -->
  <polygon points="60,22 88,38 88,70 60,86 32,70 32,38" fill="#094537" stroke="#71efaf" stroke-width="2"/>
  <circle cx="46" cy="46" r="10" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
  <circle cx="74" cy="46" r="10" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
  <circle cx="60" cy="68" r="12" fill="#f1df76" stroke="#ffffff" stroke-width="2"/>
  <circle cx="60" cy="68" r="4" fill="#000000"/>
</svg>''',

        # Mellda (Border Lead): Barbed Trench Shield & Razor-Wire Crown
        "avatar_core_mellda.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,24 100,94 60,114 20,94 6,24" fill="#24070a" stroke="#ef5b55" stroke-width="3.5"/>
  <!-- Razor-Wire Spikes Crown -->
  <path d="M 26,30 L 38,40 L 50,26 L 60,42 L 70,26 L 82,40 L 94,30" fill="none" stroke="#f1df76" stroke-width="3"/>
  <!-- Heavy Fortress Pavise -->
  <polygon points="34,44 86,44 80,86 60,98 40,86" fill="#4d1218" stroke="#ef5b55" stroke-width="2.5"/>
  <line x1="60" y1="44" x2="60" y2="98" stroke="#ffffff" stroke-width="3"/>
  <line x1="40" y1="66" x2="80" y2="66" stroke="#ffffff" stroke-width="3"/>
</svg>''',

        # Marjuk (Archive Lead): Antique Clockwork Chronometer & Rolled Scroll
        "avatar_core_marjuk.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="#140624" stroke="#c084fc" stroke-width="4"/>
  <!-- Chronometer Cog & Gear Ring -->
  <circle cx="60" cy="54" r="30" fill="#2b0d4d" stroke="#f1df76" stroke-width="2.5" stroke-dasharray="6 4"/>
  <!-- Floating Glowing Quill & Rolled Parchment -->
  <path d="M 76,24 Q 92,16 88,38 Q 80,34 72,40 Z" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
  <rect x="36" y="86" width="48" height="16" rx="4" fill="#fef08a" stroke="#7e22ce" stroke-width="2"/>
  <line x1="44" y1="94" x2="76" y2="94" stroke="#3b0764" stroke-width="2"/>
</svg>''',

        # Ishall (The Outsider): Inverted Crescent & Crossed Obsidian Daggers
        "avatar_core_ishall.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,20 100,70 114,114 60,98 6,114 20,70 6,20" fill="#0d0414" stroke="#ef5b55" stroke-width="3.5"/>
  <!-- Crossed Inverted Stiletto Blades -->
  <line x1="26" y1="26" x2="94" y2="94" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <polygon points="94,94 82,92 92,82" fill="#ef5b55"/>
  <line x1="94" y1="26" x2="26" y2="94" stroke="#e2e8f0" stroke-width="5" stroke-linecap="round"/>
  <polygon points="26,94 38,92 28,82" fill="#ef5b55"/>
  <!-- Inverted Shadow Crescent Core -->
  <path d="M 40,40 Q 60,70 80,40 Q 60,86 40,40 Z" fill="#ef5b55" stroke="#ffffff" stroke-width="2"/>
</svg>''',

        # Xyan (The Exile): Desolate Sun Sextant Compass & Barbed Chain
        "avatar_core_xyan.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 76,26 106,14 100,44 118,66 92,78 94,110 64,98 44,116 34,88 6,86 16,56 4,28 34,32" fill="#211802" stroke="#f1df76" stroke-width="3.5"/>
  <!-- Desolate Navigator Sextant -->
  <circle cx="60" cy="60" r="28" fill="#453106" stroke="#f1df76" stroke-width="2.5"/>
  <polygon points="60,36 68,56 88,60 68,64 60,84 52,64 32,60 52,56" fill="#f1df76" stroke="#ef5b55" stroke-width="1.5"/>
  <circle cx="60" cy="60" r="6" fill="#ffffff"/>
</svg>'''
    }

    # Supporting Characters Symbolic Artifacts
    char_emblems["avatar_char_minho.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 110,24 110,84 60,114 10,84 10,24" fill="#081729" stroke="#38bdf8" stroke-width="3.5"/>
  <!-- Tactical Radio Comm & Crossed M.A.W. Blades -->
  <line x1="28" y1="36" x2="92" y2="84" stroke="#f1df76" stroke-width="4"/>
  <line x1="92" y1="36" x2="28" y2="84" stroke="#f1df76" stroke-width="4"/>
  <circle cx="60" cy="60" r="16" fill="#0284c7" stroke="#ffffff" stroke-width="2.5"/>
  <line x1="88" y1="20" x2="104" y2="4" stroke="#38bdf8" stroke-width="3"/>
</svg>'''

    char_emblems["avatar_char_doha.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="#261704" stroke="#f1df76" stroke-width="4"/>
  <!-- Golden Scale of Antiquity Balancing Coin & Ingot -->
  <line x1="30" y1="44" x2="90" y2="44" stroke="#f1df76" stroke-width="4"/>
  <line x1="60" y1="24" x2="60" y2="84" stroke="#f1df76" stroke-width="3.5"/>
  <circle cx="40" cy="66" r="10" fill="#eab308" stroke="#ffffff" stroke-width="1.5"/>
  <rect x="70" y="58" width="18" height="14" rx="2" fill="#ef4444" stroke="#f1df76" stroke-width="1.5"/>
</svg>'''

    char_emblems["avatar_char_soojin.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,60 60,114 6,60" fill="#042022" stroke="#06b6d4" stroke-width="3.5"/>
  <!-- Crossed Glowing Alchemical Vials -->
  <line x1="36" y1="36" x2="84" y2="84" stroke="#06b6d4" stroke-width="7" stroke-linecap="round"/>
  <line x1="84" y1="36" x2="36" y2="84" stroke="#ef4444" stroke-width="7" stroke-linecap="round"/>
  <circle cx="60" cy="60" r="14" fill="#ffffff" stroke="#083344" stroke-width="3"/>
</svg>'''

    char_emblems["avatar_char_sora.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 110,32 110,88 60,116 10,88 10,32" fill="#1f1404" stroke="#f59e0b" stroke-width="3.5"/>
  <!-- Weeping Crystal Tear Locket -->
  <path d="M 60,32 C 44,52 38,72 60,94 C 82,72 76,52 60,32 Z" fill="#38bdf8" stroke="#ffffff" stroke-width="3"/>
  <circle cx="60" cy="68" r="8" fill="#fef08a" stroke="#d97706" stroke-width="2"/>
</svg>'''

    char_emblems["avatar_char_taeho.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,24 100,94 60,114 20,94 6,24" fill="#240707" stroke="#ef4444" stroke-width="3.5"/>
  <!-- Heavy Riot Shield & Crossed Heavy Batons -->
  <line x1="26" y1="24" x2="94" y2="92" stroke="#f1df76" stroke-width="6" stroke-linecap="round"/>
  <line x1="94" y1="24" x2="26" y2="92" stroke="#f1df76" stroke-width="6" stroke-linecap="round"/>
  <rect x="36" y="44" width="48" height="32" rx="4" fill="#120404" stroke="#ef4444" stroke-width="2.5"/>
</svg>'''

    char_emblems["avatar_char_kael.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="40,4 80,4 116,40 116,80 80,116 40,116 4,80 4,40" fill="#241503" stroke="#d97706" stroke-width="3.5"/>
  <!-- Star Navigator Compass Rose & Golden Lantern -->
  <circle cx="60" cy="60" r="28" fill="#4d3007" stroke="#f1df76" stroke-width="2.5"/>
  <polygon points="60,26 66,54 94,60 66,66 60,94 54,66 26,60 54,54" fill="#f1df76"/>
  <circle cx="60" cy="60" r="6" fill="#ef4444"/>
</svg>'''

    char_emblems["avatar_char_yeonhwa.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="#18072b" stroke="#a855f7" stroke-width="4"/>
  <!-- Clockwork Spindle Loom with 8 Radial Silk Strands -->
  <circle cx="60" cy="60" r="16" fill="#3b0764" stroke="#f1df76" stroke-width="3"/>
  <line x1="60" y1="16" x2="60" y2="104" stroke="#38bdf8" stroke-width="2.5"/>
  <line x1="16" y1="60" x2="104" y2="60" stroke="#38bdf8" stroke-width="2.5"/>
  <line x1="28" y1="28" x2="92" y2="92" stroke="#38bdf8" stroke-width="2.5"/>
  <line x1="92" y1="28" x2="28" y2="92" stroke="#38bdf8" stroke-width="2.5"/>
</svg>'''

    char_emblems["avatar_char_joon.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,32 114,88 60,114 6,88 6,32" fill="#260f04" stroke="#ea580c" stroke-width="3.5"/>
  <!-- Smelter Furnace Crucible with Forging Tongs -->
  <path d="M 36,36 Q 60,68 84,36" fill="none" stroke="#f1df76" stroke-width="5"/>
  <circle cx="60" cy="62" r="18" fill="#f97316" stroke="#ffffff" stroke-width="3"/>
  <circle cx="60" cy="62" r="8" fill="#ffffff"/>
</svg>'''

    char_emblems["avatar_char_high_architects.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 116,60 60,116 4,60" fill="#1a1402" stroke="#f1df76" stroke-width="4"/>
  <!-- Master Masonry Compass & Plumb-Bob -->
  <polygon points="60,20 92,76 28,76" fill="none" stroke="#f1df76" stroke-width="4"/>
  <line x1="60" y1="20" x2="60" y2="96" stroke="#38bdf8" stroke-width="3.5"/>
  <circle cx="60" cy="98" r="7" fill="#ef5b55" stroke="#ffffff" stroke-width="2"/>
</svg>'''

    char_emblems["avatar_char_cheonbulok_refugees.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 112,32 112,88 60,114 8,88 8,32" fill="#0f1926" stroke="#38bdf8" stroke-width="3.5"/>
  <!-- Hearth Hope Lantern with Reaching Protective Hands -->
  <polygon points="60,22 100,72 20,72" fill="#1b2a3d" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="52" y="48" width="16" height="26" rx="4" fill="#f1df76" stroke="#ffffff" stroke-width="2"/>
  <circle cx="60" cy="60" r="4" fill="#ef5b55"/>
</svg>'''

    for fname, svg_c in char_emblems.items():
        # Copy to avatars and icons
        with open(os.path.join(avatars_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg_c)
        with open(os.path.join(icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg_c)
        with open(os.path.join(user_icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg_c)
        # Also copy to icon_core_*
        alt_name = fname.replace("avatar_", "icon_")
        with open(os.path.join(icons_dir, alt_name), "w", encoding="utf-8") as f:
            f.write(svg_c)

    print(f"Generated {len(char_emblems)} specialized symbolic character artifact icons (no human profile heads)!")

    # =========================================================================
    # 3. THREE DISTINCT ASSET TYPES FOR EVERY SORROW ENTITY:
    # A) ICON (Heraldic Seal - 120x120)
    # B) BANNER (Tactical Containment Scene - 1200x400)
    # C) PROFILE (500x500 Master Physical Showcase Illustration)
    # =========================================================================
    entities_data = {
        "se-001": {
            "name": "The Orphaned Bell",
            "tier": "SOMNA (C-IVδ-001 [LO])",
            "color": "#38bdf8",
            "accent": "#f1df76",
            "icon": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 116,60 60,116 4,60" fill="#081424" stroke="#38bdf8" stroke-width="4"/>
  <!-- Bell Heraldic Emblem -->
  <path d="M 44,32 Q 60,18 76,32 L 86,76 Q 90,86 60,86 Q 30,86 34,76 Z" fill="#132740" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="60" cy="86" r="8" fill="#ef5b55" stroke="#ffffff" stroke-width="1.5"/>
  <path d="M 60,44 L 54,60 L 66,70" fill="none" stroke="#38bdf8" stroke-width="2"/>
</svg>''',
            "banner": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="b1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b172a"/>
      <stop offset="60%" stop-color="#040914"/>
      <stop offset="100%" stop-color="#020408"/>
    </linearGradient>
    <radialGradient id="b1Glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="0" y="0" width="1200" height="400" fill="url(#b1Grad)"/>
  <circle cx="600" cy="200" r="300" fill="url(#b1Glow)"/>
  <!-- Outer Chamber Frame -->
  <rect x="15" y="15" width="1170" height="370" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="25" y="25" width="1150" height="350" fill="none" stroke="#f1df76" stroke-width="1" stroke-dasharray="8 4" opacity="0.4"/>
  <!-- Acoustic Wave Decals -->
  <path d="M 100,200 Q 350,80 600,200 T 1100,200" fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.6"/>
  <path d="M 100,240 Q 350,120 600,240 T 1100,240" fill="none" stroke="#f1df76" stroke-width="1.5" opacity="0.5"/>
  <!-- Hanging Giant Bronze Bell in Center -->
  <rect x="585" y="30" width="30" height="50" fill="#1e293b" stroke="#f1df76" stroke-width="2"/>
  <path d="M 520,80 Q 600,40 680,80 L 730,260 Q 750,290 600,290 Q 450,290 470,260 Z" fill="#132338" stroke="#f1df76" stroke-width="4"/>
  <circle cx="600" cy="290" r="24" fill="#ef5b55" stroke="#ffffff" stroke-width="3"/>
  <!-- HUD Text Overlay -->
  <text x="50" y="80" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-001 // THE ORPHANED BELL</text>
  <text x="50" y="115" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="16">ACOUSTIC CONTAINMENT SECTOR 01 // SOMNA RISK</text>
</svg>'''
        },
        "se-002": {
            "name": "The Grieving Colossus",
            "tier": "PHANTASM (C-Vδ-002 [WS])",
            "color": "#ef5b55",
            "accent": "#f1df76",
            "icon": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,24 100,94 60,114 20,94 6,24" fill="#24070a" stroke="#ef5b55" stroke-width="4"/>
  <!-- Crag Fist / Broken Monolith Spire -->
  <polygon points="34,38 60,20 86,38 80,84 40,84" fill="#4d1218" stroke="#ef5b55" stroke-width="2.5"/>
  <line x1="60" y1="20" x2="60" y2="84" stroke="#f1df76" stroke-width="3"/>
  <circle cx="60" cy="52" r="6" fill="#ffffff"/>
</svg>''',
            "banner": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="b2Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2a0a0f"/>
      <stop offset="60%" stop-color="#140306"/>
      <stop offset="100%" stop-color="#050001"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="1200" height="400" fill="url(#b2Grad)"/>
  <rect x="15" y="15" width="1170" height="370" fill="none" stroke="#ef5b55" stroke-width="2.5"/>
  <!-- Colossus Silhouette Rising in Chamber -->
  <polygon points="450,380 480,180 540,120 600,160 660,120 720,180 750,380" fill="#170609" stroke="#ef5b55" stroke-width="4"/>
  <!-- Glowing Crimson Fissure Eyes -->
  <circle cx="570" cy="190" r="12" fill="#ef5b55"/>
  <circle cx="630" cy="190" r="12" fill="#ef5b55"/>
  <path d="M 600,210 L 600,380" stroke="#f1df76" stroke-width="3.5"/>
  <!-- HUD Text Overlay -->
  <text x="50" y="80" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-002 // THE GRIEVING COLOSSUS</text>
  <text x="50" y="115" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16">SEISMIC CONTAINMENT SECTOR 02 // PHANTASM RISK</text>
</svg>'''
        },
        "se-003": {
            "name": "The Wilderness Tide",
            "tier": "MORPHEAN (O-Vγ-003 [WP])",
            "color": "#71efaf",
            "accent": "#38bdf8",
            "icon": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 116,60 60,116 4,60" fill="#031f18" stroke="#71efaf" stroke-width="4"/>
  <!-- Bioluminescent Wave Crest -->
  <path d="M 24,76 Q 50,32 76,52 T 96,44" fill="none" stroke="#71efaf" stroke-width="4"/>
  <circle cx="76" cy="52" r="6" fill="#38bdf8"/>
</svg>''',
            "banner": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect x="0" y="0" width="1200" height="400" fill="#031410"/>
  <rect x="15" y="15" width="1170" height="370" fill="none" stroke="#71efaf" stroke-width="2.5"/>
  <!-- Surging Tsunami Bio-Waves -->
  <path d="M 0,380 Q 300,180 600,260 T 1200,200 L 1200,400 L 0,400 Z" fill="#06382a" stroke="#71efaf" stroke-width="3"/>
  <text x="50" y="80" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-003 // THE WILDERNESS TIDE</text>
  <text x="50" y="115" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="16">FLUIDIC INVASION SECTOR 03 // MORPHEAN RISK</text>
</svg>'''
        },
        "se-005": {
            "name": "The Smothering Mother",
            "tier": "PHANTASM (N-IVδ-005 [GS])",
            "color": "#c084fc",
            "accent": "#ef5b55",
            "icon": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 110,32 110,88 60,116 10,88 10,32" fill="#140624" stroke="#c084fc" stroke-width="4"/>
  <!-- Shrouded Maternal Veil & Stigmata -->
  <path d="M 36,36 Q 60,18 84,36 L 90,92 L 30,92 Z" fill="#2b0d4d" stroke="#c084fc" stroke-width="2.5"/>
  <circle cx="60" cy="54" r="6" fill="#ef5b55" stroke="#ffffff" stroke-width="1.5"/>
</svg>''',
            "banner": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect x="0" y="0" width="1200" height="400" fill="#10041c"/>
  <rect x="15" y="15" width="1170" height="370" fill="none" stroke="#c084fc" stroke-width="2.5"/>
  <path d="M 500,400 Q 600,100 700,400 Z" fill="#200738" stroke="#c084fc" stroke-width="3"/>
  <text x="50" y="80" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-005 // THE SMOTHERING MOTHER</text>
  <text x="50" y="115" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="16">MATERNAL SHROUD SECTOR 05 // PHANTASM RISK</text>
</svg>'''
        },
        "se-007": {
            "name": "Brume",
            "tier": "AETHER (O-IIγ-007 [VP])",
            "color": "#38bdf8",
            "accent": "#71efaf",
            "icon": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,60 60,114 6,60" fill="#041a29" stroke="#38bdf8" stroke-width="4"/>
  <!-- Particulate Cloud Swirls -->
  <circle cx="48" cy="54" r="14" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="72" cy="54" r="14" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="60" cy="68" r="16" fill="#0284c7" stroke="#71efaf" stroke-width="2"/>
</svg>''',
            "banner": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect x="0" y="0" width="1200" height="400" fill="#031521"/>
  <rect x="15" y="15" width="1170" height="370" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="50" y="80" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-007 // BRUME</text>
  <text x="50" y="115" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="16">AEROSOL CHAMBER 07 // AETHER RISK</text>
</svg>'''
        },
        "se-009": {
            "name": "The Memory Weaver",
            "tier": "MORPHEAN (C-IVγ-009 [VS])",
            "color": "#38bdf8",
            "accent": "#c084fc",
            "icon": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="#100824" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="60" cy="60" r="18" fill="#2b0d4d" stroke="#c084fc" stroke-width="2.5"/>
  <line x1="24" y1="24" x2="96" y2="96" stroke="#38bdf8" stroke-width="2"/>
  <line x1="96" y1="24" x2="24" y2="96" stroke="#38bdf8" stroke-width="2"/>
</svg>''',
            "banner": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect x="0" y="0" width="1200" height="400" fill="#0d041a"/>
  <rect x="15" y="15" width="1170" height="370" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="50" y="80" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-009 // THE MEMORY WEAVER</text>
  <text x="50" y="115" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="16">CLOCKWORK LOOM SECTOR 09 // MORPHEAN RISK</text>
</svg>'''
        },
        "se-010": {
            "name": "The Convergence",
            "tier": "APOCRYPHA (C-IVω-001 [GP])",
            "color": "#c084fc",
            "accent": "#ef5b55",
            "icon": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 116,60 60,116 4,60" fill="#140224" stroke="#c084fc" stroke-width="4"/>
  <!-- Orbiting Singularity Rings -->
  <ellipse cx="60" cy="60" rx="34" ry="12" fill="none" stroke="#ef5b55" stroke-width="2.5" transform="rotate(-30 60 60)"/>
  <circle cx="60" cy="60" r="14" fill="#000000" stroke="#c084fc" stroke-width="2"/>
</svg>''',
            "banner": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect x="0" y="0" width="1200" height="400" fill="#080010"/>
  <rect x="15" y="15" width="1170" height="370" fill="none" stroke="#c084fc" stroke-width="2.5"/>
  <circle cx="600" cy="200" r="80" fill="#000000" stroke="#ef5b55" stroke-width="4"/>
  <text x="50" y="80" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-010 // THE CONVERGENCE</text>
  <text x="50" y="115" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="16">GRAVITATIONAL EVENT HORIZON // APOCRYPHA RISK</text>
</svg>'''
        },
        "se-011": {
            "name": "The Whispering Walls",
            "tier": "SOMNA (C-IIIγ-021 [LS])",
            "color": "#38bdf8",
            "accent": "#f1df76",
            "icon": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="36,4 84,4 116,36 116,84 84,116 36,116 4,84 4,36" fill="#06121f" stroke="#38bdf8" stroke-width="3.5"/>
  <rect x="36" y="28" width="48" height="64" fill="#132740" stroke="#f1df76" stroke-width="2"/>
  <circle cx="60" cy="48" r="8" fill="#38bdf8"/>
  <ellipse cx="60" cy="70" rx="6" ry="10" fill="#000000" stroke="#38bdf8"/>
</svg>''',
            "banner": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect x="0" y="0" width="1200" height="400" fill="#050e18"/>
  <rect x="15" y="15" width="1170" height="370" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="50" y="80" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-011 // THE WHISPERING WALLS</text>
  <text x="50" y="115" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="16">ACOUSTIC SLAB SECTOR 11 // SOMNA RISK</text>
</svg>'''
        },
        "se-014": {
            "name": "The Debt Eater",
            "tier": "PHANTASM (C-IIIβ-014 [VS])",
            "color": "#f1df76",
            "accent": "#ef5b55",
            "icon": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,6 114,24 100,94 60,114 20,94 6,24" fill="#261704" stroke="#f1df76" stroke-width="4"/>
  <path d="M 36,44 Q 60,20 84,44 L 80,78 Q 60,94 40,78 Z" fill="#4d2f07" stroke="#ef5b55" stroke-width="2.5"/>
  <circle cx="60" cy="62" r="8" fill="#f1df76"/>
</svg>''',
            "banner": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect x="0" y="0" width="1200" height="400" fill="#140b02"/>
  <rect x="15" y="15" width="1170" height="370" fill="none" stroke="#f1df76" stroke-width="2.5"/>
  <text x="50" y="80" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-014 // THE DEBT EATER</text>
  <text x="50" y="115" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="16">KARMIC LEDGER VAULT 14 // PHANTASM RISK</text>
</svg>'''
        },
        "se-015": {
            "name": "The Debt Scale",
            "tier": "MORPHEAN (C-IIIγ-015 [LS])",
            "color": "#f1df76",
            "accent": "#38bdf8",
            "icon": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="54" fill="#171203" stroke="#f1df76" stroke-width="4"/>
  <line x1="30" y1="46" x2="90" y2="46" stroke="#f1df76" stroke-width="4"/>
  <line x1="60" y1="26" x2="60" y2="86" stroke="#f1df76" stroke-width="3"/>
  <circle cx="40" cy="66" r="8" fill="#ef5b55"/>
  <circle cx="80" cy="66" r="8" fill="#38bdf8"/>
</svg>''',
            "banner": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <rect x="0" y="0" width="1200" height="400" fill="#0d0a02"/>
  <rect x="15" y="15" width="1170" height="370" fill="none" stroke="#f1df76" stroke-width="2.5"/>
  <text x="50" y="80" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="bold">SE-015 // THE DEBT SCALE</text>
  <text x="50" y="115" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="16">EQUILIBRIUM CHAMBER 15 // MORPHEAN RISK</text>
</svg>'''
        }
    }

    for se_id, se_info in entities_data.items():
        # A) Write ICON
        icon_path = os.path.join(entities_art_dir, f"{se_id}-icon.svg")
        with open(icon_path, "w", encoding="utf-8") as f:
            f.write(se_info["icon"])
        with open(os.path.join(icons_dir, f"{se_id}.svg"), "w", encoding="utf-8") as f:
            f.write(se_info["icon"])

        # B) Write BANNER
        banner_path = os.path.join(entities_art_dir, f"{se_id}-banner.svg")
        with open(banner_path, "w", encoding="utf-8") as f:
            f.write(se_info["banner"])
        with open(os.path.join(banners_dir, f"{se_id}-banner.svg"), "w", encoding="utf-8") as f:
            f.write(se_info["banner"])

        # C) PROFILE (already exists as se-xxx.svg in assets/art/entities/ from earlier script; copy to se-xxx-profile.svg)
        prof_src = os.path.join(entities_art_dir, f"{se_id}.svg")
        prof_dest = os.path.join(entities_art_dir, f"{se_id}-profile.svg")
        if os.path.exists(prof_src):
            with open(prof_src, "r", encoding="utf-8") as f:
                c = f.read()
            with open(prof_dest, "w", encoding="utf-8") as f:
                f.write(c)

    print("Generated 3 DISTINCT asset types (Icon, Banner, Profile) for all 10 Sorrow Entities!")

if __name__ == "__main__":
    generate_canonical_assets()
