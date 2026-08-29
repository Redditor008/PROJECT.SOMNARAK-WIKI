import os

def build_all_ultra_maw_svgs():
    maw_art_dir = "/home/user/01_Somnarak_Wiki/assets/art/maw"
    os.makedirs(maw_art_dir, exist_ok=True)

    # 10 Weapons, 10 Suits, 10 Gifts
    maw_items = {
        # WEAPONS (maw-w-xxx-01.svg)
        "maw-w-001-01.svg": {
            "title": "LAMENT'S REQUIEM",
            "type": "WEAPON // HEAVY CLEAVER",
            "color": "#38bdf8",
            "accent": "#f1df76",
            "body": '''<!-- Heavy Resonant Cleaver Blade -->
  <path d="M 120 340 L 145 365 L 210 300 L 290 120 L 320 80 L 260 70 L 190 230 Z" fill="#182333" stroke="#38bdf8" stroke-width="3"/>
  <path d="M 290 120 L 250 140 L 190 230" fill="none" stroke="#f1df76" stroke-width="2.5"/>
  <!-- Bell Chime Resonance Holes along Blade -->
  <circle cx="240" cy="160" r="8" fill="#090d16" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="215" cy="205" r="6" fill="#090d16" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="190" cy="250" r="5" fill="#090d16" stroke="#38bdf8" stroke-width="2"/>
  <!-- Hilt & Grip -->
  <line x1="120" y1="340" x2="80" y2="380" stroke="#f1df76" stroke-width="8" stroke-linecap="round"/>
  <circle cx="75" cy="385" r="8" fill="#ef5b55"/>'''
        },
        "maw-w-002-01.svg": {
            "title": "THE MOURNING MAUL",
            "type": "WEAPON // CRAG MAUL",
            "color": "#ef5b55",
            "accent": "#f1df76",
            "body": '''<!-- Massive Crag Stone Maul Head -->
  <polygon points="170,90 310,70 330,190 190,210" fill="#1e181c" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="200,105 280,95 295,175 215,185" fill="#2d2228" stroke="#f1df76" stroke-width="2"/>
  <!-- Glowing Crimson Fissure Conduits -->
  <path d="M 210 115 L 240 145 L 230 175 L 270 165" fill="none" stroke="#ef5b55" stroke-width="3"/>
  <!-- Reinforced Steel Haft -->
  <line x1="250" y1="140" x2="90" y2="360" stroke="#475569" stroke-width="9" stroke-linecap="round"/>
  <line x1="250" y1="140" x2="90" y2="360" stroke="#f1df76" stroke-width="2" stroke-dasharray="8 4"/>
  <circle cx="85" cy="365" r="12" fill="#0f172a" stroke="#ef5b55" stroke-width="3"/>'''
        },
        "maw-w-005-01.svg": {
            "title": "THE EMBRACE FANG",
            "type": "WEAPON // OBSIDIAN NEEDLE RAPIER",
            "color": "#c084fc",
            "accent": "#ef5b55",
            "body": '''<!-- Needle-Thin Obsidian Stiletto Blade -->
  <path d="M 90 350 L 140 300 L 320 80 L 310 70 L 130 290 Z" fill="#110e1e" stroke="#c084fc" stroke-width="2.5"/>
  <line x1="320" y1="80" x2="135" y2="295" stroke="#ef5b55" stroke-width="2"/>
  <!-- Shroud Cradle Crossguard -->
  <ellipse cx="140" cy="300" rx="35" ry="18" fill="#1e1430" stroke="#f1df76" stroke-width="2.5" transform="rotate(-45 140 300)"/>
  <!-- Grip and Thread Pommel -->
  <line x1="125" y1="315" x2="70" y2="370" stroke="#c084fc" stroke-width="6"/>
  <circle cx="65" cy="375" r="10" fill="#ef5b55" stroke="#f1df76" stroke-width="2"/>'''
        },
        "maw-w-007-01.svg": {
            "title": "THE HOPE LENS",
            "type": "WEAPON // AEROSOL EMITTER",
            "color": "#38bdf8",
            "accent": "#71efaf",
            "body": '''<!-- Aerosol Emitter Barrel & Prism Lens -->
  <rect x="130" y="160" width="160" height="60" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5" transform="rotate(-25 210 190)"/>
  <!-- Glass Vapor Chamber -->
  <ellipse cx="180" cy="200" rx="30" ry="20" fill="#0284c7" opacity="0.4" stroke="#71efaf" stroke-width="2"/>
  <!-- Prismatic Focus Ring -->
  <circle cx="280" cy="155" r="28" fill="#082f49" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="280" cy="155" r="14" fill="#71efaf" opacity="0.8"/>
  <!-- Stock and Trigger Grip -->
  <path d="M 140 225 L 110 300 L 80 320" fill="none" stroke="#f1df76" stroke-width="6" stroke-linecap="round"/>'''
        },
        "maw-w-009-01.svg": {
            "title": "THE FORGOTTEN LENS",
            "type": "WEAPON // WEAVER'S SCYTHE",
            "color": "#38bdf8",
            "accent": "#c084fc",
            "body": '''<!-- Curved Clockwork Loom Scythe Blade -->
  <path d="M 120 180 C 120 70, 220 50, 310 70 C 260 110, 220 160, 180 190 Z" fill="#131028" stroke="#38bdf8" stroke-width="3"/>
  <!-- Azure Filament Wire along Blade Edge -->
  <path d="M 310 70 Q 200 120 130 180" fill="none" stroke="#c084fc" stroke-width="2.5"/>
  <!-- Long Mechanical Shaft -->
  <line x1="180" y1="190" x2="100" y2="370" stroke="#475569" stroke-width="7" stroke-linecap="round"/>
  <!-- Clockwork Gear Housing at Joint -->
  <circle cx="180" cy="190" r="18" fill="#1e1b4b" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="180" cy="190" r="7" fill="#38bdf8"/>'''
        },
        "maw-w-010-01.svg": {
            "title": "THE ABSOLUTE MAUL",
            "type": "WEAPON // SINGULARITY SCEPTER",
            "color": "#c084fc",
            "accent": "#ef5b55",
            "body": '''<!-- Singularity Orb Head -->
  <circle cx="280" cy="120" r="45" fill="#090014" stroke="#c084fc" stroke-width="3"/>
  <circle cx="280" cy="120" r="28" fill="#1e1b4b" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="280" cy="120" r="12" fill="#f1df76"/>
  <!-- Orbital Rings Orbiting Head -->
  <ellipse cx="280" cy="120" rx="60" ry="20" fill="none" stroke="#c084fc" stroke-width="2" transform="rotate(-30 280 120)"/>
  <ellipse cx="280" cy="120" rx="55" ry="18" fill="none" stroke="#ef5b55" stroke-width="1.8" transform="rotate(45 280 120)"/>
  <!-- Staff Shaft -->
  <line x1="250" y1="150" x2="90" y2="360" stroke="#f1df76" stroke-width="7" stroke-linecap="round"/>
  <circle cx="85" cy="365" r="10" fill="#c084fc" stroke="#ef5b55" stroke-width="2"/>'''
        },
        "maw-w-011-01.svg": {
            "title": "THE LISTENING REQUIEM",
            "type": "WEAPON // ACOUSTIC TUNING BLADE",
            "color": "#38bdf8",
            "accent": "#f1df76",
            "body": '''<!-- Dual Tuning Fork Blade -->
  <path d="M 180 230 L 240 100 L 260 100 L 210 230 Z" fill="#182333" stroke="#38bdf8" stroke-width="2.5"/>
  <path d="M 210 230 L 290 80 L 310 80 L 240 230 Z" fill="#182333" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Acoustic Bridge Base -->
  <polygon points="170,230 250,230 230,280 190,280" fill="#0f172a" stroke="#f1df76" stroke-width="2.5"/>
  <!-- Acoustic Wave Ring Between Prongs -->
  <path d="M 250 110 Q 275 130 285 100" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3 3"/>
  <!-- Grip -->
  <line x1="210" y1="280" x2="140" y2="370" stroke="#f1df76" stroke-width="7" stroke-linecap="round"/>
  <circle cx="135" cy="375" r="9" fill="#38bdf8" stroke="#1e293b" stroke-width="2"/>'''
        },
        "maw-w-014-01.svg": {
            "title": "THE DEBT LENS",
            "type": "WEAPON // LEDGER GLAIVE",
            "color": "#f1df76",
            "accent": "#ef5b55",
            "body": '''<!-- Gold-Toothed Ledger Blade -->
  <path d="M 150 210 L 270 70 L 310 85 L 210 250 Z" fill="#2d1c08" stroke="#f1df76" stroke-width="3"/>
  <!-- Serrated Coin Teeth Edge -->
  <polygon points="280,80 295,95 275,100" fill="#f1df76"/>
  <polygon points="260,105 275,120 255,125" fill="#f1df76"/>
  <polygon points="240,130 255,145 235,150" fill="#f1df76"/>
  <!-- Molten Core Ingot in Guard -->
  <circle cx="180" cy="230" r="16" fill="#ef5b55" stroke="#f1df76" stroke-width="2.5"/>
  <!-- Long Pole Haft -->
  <line x1="170" y1="245" x2="90" y2="365" stroke="#78350f" stroke-width="7" stroke-linecap="round"/>'''
        },
        "maw-w-015-01.svg": {
            "title": "THE BALANCE LENS",
            "type": "WEAPON // EQUILIBRIUM STAVE",
            "color": "#f1df76",
            "accent": "#38bdf8",
            "body": '''<!-- Dual-Balance Stave Head -->
  <line x1="180" y1="130" x2="320" y2="100" stroke="#f1df76" stroke-width="4"/>
  <!-- Left Weight: Obsidian Heart -->
  <circle cx="180" cy="150" r="14" fill="#0f172a" stroke="#ef5b55" stroke-width="2"/>
  <line x1="180" y1="130" x2="180" y2="150" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Right Weight: Crystalline Prism -->
  <polygon points="320,135 330,150 320,165 310,150" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="320" y1="100" x2="320" y2="135" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Center Pivot Ring & Staff -->
  <circle cx="250" cy="115" r="16" fill="#1e293b" stroke="#f1df76" stroke-width="3"/>
  <line x1="250" y1="131" x2="120" y2="370" stroke="#38bdf8" stroke-width="7" stroke-linecap="round"/>'''
        },

        # SUITS (maw-s-xxx-01.svg)
        "maw-s-001-01.svg": {
            "title": "THE LAMENT'S SHROUD",
            "type": "SUIT // TACTICAL TUNIC",
            "color": "#38bdf8",
            "accent": "#f1df76",
            "body": '''<!-- Bell Shroud Armor Carapace -->
  <path d="M 130 110 L 200 90 L 270 110 L 300 230 L 200 270 L 100 230 Z" fill="#121d2d" stroke="#38bdf8" stroke-width="3"/>
  <!-- Reinforced Gold Plating Trim -->
  <path d="M 160 110 L 200 95 L 240 110 L 250 200 L 200 220 L 150 200 Z" fill="#1a283e" stroke="#f1df76" stroke-width="2"/>
  <!-- Hanging Bronze Clapper Guards & Mantle Straps -->
  <path d="M 100 230 L 70 330 L 140 310 L 160 260" fill="#0a101b" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 300 230 L 330 330 L 260 310 L 240 260" fill="#0a101b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Central Weeping Sigil -->
  <circle cx="200" cy="160" r="12" fill="#ef5b55" stroke="#f1df76" stroke-width="2"/>'''
        },
        "maw-s-002-01.svg": {
            "title": "THE MOURNING MANTLE",
            "type": "SUIT // HEAVY CRAG PLATES",
            "color": "#ef5b55",
            "accent": "#f1df76",
            "body": '''<!-- Heavy Crag Stone Pauldrons and Breastplate -->
  <polygon points="90,110 160,90 190,150 110,180" fill="#2d2228" stroke="#ef5b55" stroke-width="3"/>
  <polygon points="310,110 240,90 210,150 290,180" fill="#2d2228" stroke="#ef5b55" stroke-width="3"/>
  <!-- Central Obsidian Chestplate -->
  <polygon points="150,140 250,140 270,290 200,340 130,290" fill="#1a1418" stroke="#f1df76" stroke-width="2.5"/>
  <!-- Magma Fissure Conduits Running Down Center -->
  <path d="M 200 140 L 195 200 L 210 260 L 200 330" fill="none" stroke="#ef5b55" stroke-width="3"/>'''
        },
        "maw-s-005-01.svg": {
            "title": "THE EMBRACE PLATE",
            "type": "SUIT // SILKEN NEEDLE COAT",
            "color": "#c084fc",
            "accent": "#ef5b55",
            "body": '''<!-- Flowing Maternal Longcoat Silhouette -->
  <path d="M 140 100 L 200 80 L 260 100 L 290 350 L 200 320 L 110 350 Z" fill="#140f24" stroke="#c084fc" stroke-width="3"/>
  <!-- Crossed Obsidian Ribbons -->
  <path d="M 140 100 L 240 220 L 130 330" fill="none" stroke="#ef5b55" stroke-width="2.5"/>
  <path d="M 260 100 L 160 220 L 270 330" fill="none" stroke="#ef5b55" stroke-width="2.5"/>
  <!-- High Indigo Collar -->
  <path d="M 160 90 L 200 60 L 240 90 L 200 120 Z" fill="#231a3d" stroke="#f1df76" stroke-width="2"/>'''
        },
        "maw-s-007-01.svg": {
            "title": "THE HOPE VEIL",
            "type": "SUIT // FILTRATION HAZMAT MANTLE",
            "color": "#38bdf8",
            "accent": "#71efaf",
            "body": '''<!-- Sealed Tactical Environmental Mantle -->
  <path d="M 130 110 L 200 90 L 270 110 L 290 320 L 200 350 L 110 320 Z" fill="#0e1f33" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Gas Filter Cartridge Vests -->
  <rect x="140" y="140" width="45" height="70" rx="8" fill="#132e4d" stroke="#71efaf" stroke-width="2"/>
  <rect x="215" y="140" width="45" height="70" rx="8" fill="#132e4d" stroke="#71efaf" stroke-width="2"/>
  <!-- Han Purifier Tubing -->
  <path d="M 160 210 Q 200 240 240 210" fill="none" stroke="#38bdf8" stroke-width="3"/>'''
        },
        "maw-s-009-01.svg": {
            "title": "THE FORGOTTEN VEIL",
            "type": "SUIT // CLOCKWORK WEFT COAT",
            "color": "#38bdf8",
            "accent": "#c084fc",
            "body": '''<!-- Weft Coat with Clockwork Strands -->
  <path d="M 130 100 L 200 80 L 270 100 L 310 330 L 200 360 L 90 330 Z" fill="#110d24" stroke="#38bdf8" stroke-width="3"/>
  <!-- Filament Weave Webbing Across Chest -->
  <line x1="130" y1="130" x2="270" y2="230" stroke="#c084fc" stroke-width="2"/>
  <line x1="270" y1="130" x2="130" y2="230" stroke="#c084fc" stroke-width="2"/>
  <circle cx="200" cy="180" r="14" fill="#0c0919" stroke="#f1df76" stroke-width="2"/>'''
        },
        "maw-s-010-01.svg": {
            "title": "THE ABSOLUTE MANTLE",
            "type": "SUIT // GRAVITATIONAL EXOSUITE",
            "color": "#c084fc",
            "accent": "#ef5b55",
            "body": '''<!-- Cosmic Singularity Armored Robe -->
  <path d="M 120 100 L 200 70 L 280 100 L 320 340 L 200 370 L 80 340 Z" fill="#0c0214" stroke="#c084fc" stroke-width="3"/>
  <!-- Central Gravitational Core Breastplate -->
  <circle cx="200" cy="190" r="40" fill="#1b072b" stroke="#ef5b55" stroke-width="2.5"/>
  <circle cx="200" cy="190" r="20" fill="#000000" stroke="#f1df76" stroke-width="2"/>
  <!-- Radiating Orbit Lines -->
  <ellipse cx="200" cy="190" rx="60" ry="15" fill="none" stroke="#c084fc" stroke-width="1.8" transform="rotate(-20 200 190)"/>'''
        },
        "maw-s-011-01.svg": {
            "title": "THE LISTENING SHROUD",
            "type": "SUIT // ACOUSTIC INSULATION CARAPACE",
            "color": "#38bdf8",
            "accent": "#f1df76",
            "body": '''<!-- Acoustic Foam & Concrete Slabs Suit -->
  <rect x="130" y="110" width="140" height="210" rx="12" fill="#141e2e" stroke="#38bdf8" stroke-width="3"/>
  <!-- Baffled Sound Dampener Ribs -->
  <line x1="145" y1="150" x2="255" y2="150" stroke="#f1df76" stroke-width="2"/>
  <line x1="145" y1="190" x2="255" y2="190" stroke="#f1df76" stroke-width="2"/>
  <line x1="145" y1="230" x2="255" y2="230" stroke="#f1df76" stroke-width="2"/>
  <line x1="145" y1="270" x2="255" y2="270" stroke="#f1df76" stroke-width="2"/>'''
        },
        "maw-s-014-01.svg": {
            "title": "THE DEBT VEIL",
            "type": "SUIT // COIN-SCALED BRIGANDINE",
            "color": "#f1df76",
            "accent": "#ef5b55",
            "body": '''<!-- Overlapping Gold Coin Scales Brigandine -->
  <path d="M 120 110 L 200 90 L 280 110 L 300 330 L 200 350 L 100 330 Z" fill="#1f1406" stroke="#f1df76" stroke-width="3"/>
  <!-- Gold Coins Pattern -->
  <circle cx="160" cy="160" r="14" fill="#3a2505" stroke="#f1df76" stroke-width="2"/>
  <circle cx="200" cy="160" r="14" fill="#3a2505" stroke="#f1df76" stroke-width="2"/>
  <circle cx="240" cy="160" r="14" fill="#3a2505" stroke="#f1df76" stroke-width="2"/>
  <circle cx="180" cy="210" r="14" fill="#3a2505" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="220" cy="210" r="14" fill="#3a2505" stroke="#ef5b55" stroke-width="2"/>'''
        },
        "maw-s-015-01.svg": {
            "title": "THE BALANCE VEIL",
            "type": "SUIT // EQUILIBRIUM ROBE",
            "color": "#f1df76",
            "accent": "#38bdf8",
            "body": '''<!-- Split Gold/Blue Equilibrium Vestment -->
  <path d="M 120 100 L 200 80 L 200 350 L 100 330 Z" fill="#1f1b0a" stroke="#f1df76" stroke-width="2.5"/>
  <path d="M 200 80 L 280 100 L 300 330 L 200 350 Z" fill="#0d1b2a" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Center Balance Seam -->
  <line x1="200" y1="80" x2="200" y2="350" stroke="#f8fafc" stroke-width="2"/>'''
        },

        # GIFTS (maw-g-xxx-01.svg)
        "maw-g-001-01.svg": {
            "title": "LAMENT'S EDGE",
            "type": "GIFT // BRONZE CHIME PENDANT",
            "color": "#38bdf8",
            "accent": "#f1df76",
            "body": '''<!-- Small Hanging Weeping Chime Pendant -->
  <circle cx="200" cy="100" r="12" fill="#0f172a" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="200" y1="112" x2="200" y2="180" stroke="#38bdf8" stroke-width="3"/>
  <path d="M 160 210 Q 200 170 240 210 L 250 260 L 150 260 Z" fill="#162338" stroke="#38bdf8" stroke-width="2.5"/>
  <circle cx="200" cy="275" r="10" fill="#ef5b55" stroke="#f1df76" stroke-width="2"/>'''
        },
        "maw-g-002-01.svg": {
            "title": "THE MOURNING SHELL",
            "type": "GIFT // CRAG VISOR",
            "color": "#ef5b55",
            "accent": "#f1df76",
            "body": '''<!-- Crag Obsidian Eye Visor -->
  <polygon points="100,170 300,170 270,230 130,230" fill="#1b1216" stroke="#ef5b55" stroke-width="3"/>
  <!-- Crimson Eye Slit Fissure -->
  <line x1="120" y1="200" x2="280" y2="200" stroke="#ef5b55" stroke-width="4"/>
  <circle cx="160" cy="200" r="5" fill="#f1df76"/>
  <circle cx="240" cy="200" r="5" fill="#f1df76"/>'''
        },
        "maw-g-005-01.svg": {
            "title": "THE EMBRACE",
            "type": "GIFT // INDIGO SHROUD BROOCH",
            "color": "#c084fc",
            "accent": "#ef5b55",
            "body": '''<!-- Swaddled Silk Brooch -->
  <circle cx="200" cy="200" r="60" fill="#150f28" stroke="#c084fc" stroke-width="3"/>
  <ellipse cx="200" cy="200" rx="30" ry="45" fill="#251b47" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="200" cy="180" r="10" fill="#ef5b55"/>'''
        },
        "maw-g-007-01.svg": {
            "title": "THE HOPE LANTERN",
            "type": "GIFT // VAPOR OCULAR LENS",
            "color": "#38bdf8",
            "accent": "#71efaf",
            "body": '''<!-- Monocle with Aerosol Gas Ring -->
  <circle cx="200" cy="200" r="55" fill="#082f49" stroke="#38bdf8" stroke-width="3.5"/>
  <circle cx="200" cy="200" r="40" fill="#0e4b75" opacity="0.6"/>
  <circle cx="200" cy="200" r="16" fill="#71efaf"/>'''
        },
        "maw-g-009-01.svg": {
            "title": "THE FORGOTTEN MASK",
            "type": "GIFT // WEAVER'S VISOR",
            "color": "#38bdf8",
            "accent": "#c084fc",
            "body": '''<!-- Spider-Eyed Clockwork Goggles -->
  <rect x="110" y="170" width="180" height="60" rx="14" fill="#0f0c22" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="150" cy="200" r="16" fill="#38bdf8"/>
  <circle cx="200" cy="200" r="10" fill="#c084fc"/>
  <circle cx="250" cy="200" r="16" fill="#38bdf8"/>'''
        },
        "maw-g-010-01.svg": {
            "title": "THE ABSOLUTE VERDICT",
            "type": "GIFT // SINGULARITY CORONA",
            "color": "#c084fc",
            "accent": "#ef5b55",
            "body": '''<!-- Floating Gravitational Halo -->
  <ellipse cx="200" cy="170" rx="80" ry="25" fill="none" stroke="#c084fc" stroke-width="3.5"/>
  <circle cx="200" cy="170" r="12" fill="#ef5b55"/>'''
        },
        "maw-g-011-01.svg": {
            "title": "THE LISTENING STONE",
            "type": "GIFT // ACOUSTIC EARPIECE",
            "color": "#38bdf8",
            "accent": "#f1df76",
            "body": '''<!-- Tuning Fork Earpiece -->
  <path d="M 180 140 Q 220 140 220 200 L 220 260" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="180" cy="140" r="8" fill="#f1df76"/>
  <circle cx="220" cy="260" r="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5"/>'''
        },
        "maw-g-014-01.svg": {
            "title": "THE DEBT SCALE GIFT",
            "type": "GIFT // GOLD COIN TALISMAN",
            "color": "#f1df76",
            "accent": "#ef5b55",
            "body": '''<!-- Pierced Gold Coin Talisman -->
  <circle cx="200" cy="200" r="55" fill="#2d1c08" stroke="#f1df76" stroke-width="3.5"/>
  <rect x="180" y="180" width="40" height="40" fill="#090d16" stroke="#ef5b55" stroke-width="2.5"/>'''
        },
        "maw-g-015-01.svg": {
            "title": "THE BALANCE PENDANT",
            "type": "GIFT // DUAL-EQUILIBRIUM BROOCH",
            "color": "#f1df76",
            "accent": "#38bdf8",
            "body": '''<!-- Yin-Yang Style Balance Brooch -->
  <circle cx="200" cy="200" r="55" fill="#0d1522" stroke="#f1df76" stroke-width="3"/>
  <path d="M 200 145 C 170 145 170 200 200 200 C 230 200 230 255 200 255 A 55 55 0 0 1 200 145" fill="#38bdf8"/>
  <circle cx="200" cy="172" r="6" fill="#f1df76"/>
  <circle cx="200" cy="228" r="6" fill="#0d1522"/>'''
        }
    }

    for fname, data in maw_items.items():
        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="mawBg_{fname[:8]}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#111827" stop-opacity="0.95"/>
      <stop offset="70%" stop-color="#090d16" stop-opacity="0.98"/>
      <stop offset="100%" stop-color="#030712" stop-opacity="1"/>
    </radialGradient>
    <radialGradient id="mawGlow_{fname[:8]}" cx="50%" cy="50%" r="45%">
      <stop offset="0%" stop-color="{data['color']}" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect x="6" y="6" width="388" height="388" rx="16" fill="url(#mawBg_{fname[:8]})" stroke="{data['color']}" stroke-width="2"/>
  <rect x="12" y="12" width="376" height="376" rx="12" fill="none" stroke="{data['accent']}" stroke-width="1" stroke-dasharray="6 3" opacity="0.35"/>
  <circle cx="200" cy="200" r="140" fill="url(#mawGlow_{fname[:8]})"/>

  {data['body']}

  <!-- Header Category Badge -->
  <rect x="20" y="20" width="220" height="26" rx="4" fill="#090d16" stroke="{data['color']}" stroke-width="1.2"/>
  <text x="30" y="37" fill="{data['color']}" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold">{data['type']}</text>

  <!-- Bottom Name Label -->
  <rect x="20" y="355" width="360" height="26" rx="4" fill="#090d16" stroke="{data['accent']}" stroke-width="1.2"/>
  <text x="200" y="372" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">{data['title']}</text>
</svg>'''
        with open(os.path.join(maw_art_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg_content)
    print(f"Generated {len(maw_items)} ultra-HD M.A.W. bespoke vector SVGs!")

if __name__ == "__main__":
    build_all_ultra_maw_svgs()
