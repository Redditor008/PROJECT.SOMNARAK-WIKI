import os
import re

def master_upgrade():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    assets_dir = os.path.join(wiki_root, "assets")
    icons_dir = os.path.join(assets_dir, "icons")
    banners_dir = os.path.join(assets_dir, "banners")
    avatars_dir = os.path.join(assets_dir, "avatars")
    entity_art_dir = os.path.join(assets_dir, "art/entities")
    hand_icons_dir = os.path.join(assets_dir, "layout/hand/icons")
    city_icons_dir = os.path.join(assets_dir, "layout/city/icons")
    user_icons_dir = "/home/user/icons"

    os.makedirs(icons_dir, exist_ok=True)
    os.makedirs(banners_dir, exist_ok=True)
    os.makedirs(avatars_dir, exist_ok=True)
    os.makedirs(entity_art_dir, exist_ok=True)
    os.makedirs(hand_icons_dir, exist_ok=True)
    os.makedirs(city_icons_dir, exist_ok=True)
    os.makedirs(user_icons_dir, exist_ok=True)

    print("--- 1. GENERATING RICH FACTION HERALDIC SEALS ---")
    factions = {
        "fac_rd": {
            "name": "REVERIE DIRECTORATE",
            "col": "#71efaf",
            "bg": "#02140d",
            "sub": "EXECUTIVE COMMAND",
            "svg": '''<polygon points="60,20 88,40 80,78 60,92 40,78 32,40" fill="#064e3b" stroke="#71efaf" stroke-width="2.5"/>
<polygon points="60,32 76,64 44,64" fill="#022c22" stroke="#f1df76" stroke-width="1.8"/>
<circle cx="60" cy="52" r="6" fill="#f1df76" stroke="#ffffff" stroke-width="1.2"/>
<line x1="24" y1="56" x2="96" y2="56" stroke="#71efaf" stroke-width="1.5" stroke-dasharray="4 2"/>'''
        },
        "fac_council": {
            "name": "HIGH COUNCIL",
            "col": "#f1df76",
            "bg": "#1c1402",
            "sub": "METROPOLITAN SENATE",
            "svg": '''<rect x="30" y="32" width="12" height="46" rx="1" fill="#451a03" stroke="#f1df76" stroke-width="1.5"/>
<rect x="54" y="24" width="12" height="54" rx="1" fill="#451a03" stroke="#f1df76" stroke-width="1.5"/>
<rect x="78" y="32" width="12" height="46" rx="1" fill="#451a03" stroke="#f1df76" stroke-width="1.5"/>
<polygon points="24,32 60,14 96,32" fill="#f1df76" stroke="#ffffff" stroke-width="1.2"/>
<rect x="22" y="78" width="76" height="8" rx="1" fill="#f1df76"/>'''
        },
        "fac_keepers": {
            "name": "KEEPERS OF SORROW",
            "col": "#ef5b55",
            "bg": "#1f0608",
            "sub": "ZEALOT CULT",
            "svg": '''<circle cx="60" cy="54" r="26" fill="none" stroke="#ef5b55" stroke-width="2" stroke-dasharray="6 3"/>
<path d="M 60,24 C 60,24 82,48 82,64 C 82,78 72,86 60,86 C 48,86 38,78 38,64 C 38,48 60,24 60,24 Z" fill="#450a0a" stroke="#ef5b55" stroke-width="2"/>
<line x1="32" y1="84" x2="88" y2="24" stroke="#ffffff" stroke-width="3"/>
<circle cx="60" cy="66" r="4" fill="#f1df76"/>'''
        },
        "fac_architects": {
            "name": "HIGH ARCHITECTS",
            "col": "#f1df76",
            "bg": "#1c1402",
            "sub": "URBAN BUILDERS",
            "svg": '''<polygon points="56,20 64,20 88,82 78,82" fill="#f1df76" stroke="#ffffff" stroke-width="1"/>
<polygon points="56,20 64,20 42,82 32,82" fill="#f1df76" stroke="#ffffff" stroke-width="1"/>
<circle cx="60" cy="22" r="6" fill="#ca8a04" stroke="#ffffff" stroke-width="1.5"/>
<path d="M 40,60 Q 60,72 80,60" fill="none" stroke="#71efaf" stroke-width="2" stroke-dasharray="3 3"/>'''
        },
        "fac_weavers": {
            "name": "WEAVERS OF SORROW",
            "col": "#38bdf8",
            "bg": "#031526",
            "sub": "MEMORY GUILD",
            "svg": '''<polygon points="60,20 86,54 60,88 34,54" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2.5"/>
<line x1="28" y1="36" x2="92" y2="72" stroke="#ffffff" stroke-width="1.8"/>
<line x1="92" y1="36" x2="28" y2="72" stroke="#ffffff" stroke-width="1.8"/>
<circle cx="60" cy="54" r="7" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>'''
        },
        "fac_underworld": {
            "name": "UNDERWORLD SYNDICATES",
            "col": "#ef5b55",
            "bg": "#140205",
            "sub": "BLACK MARKET GUILD",
            "svg": '''<circle cx="60" cy="54" r="26" fill="#334155" stroke="#f1df76" stroke-width="2.5"/>
<line x1="60" y1="28" x2="60" y2="80" stroke="#ef5b55" stroke-width="3"/>
<line x1="42" y1="42" x2="78" y2="66" stroke="#ef5b55" stroke-width="3"/>
<line x1="78" y1="42" x2="42" y2="66" stroke="#ef5b55" stroke-width="3"/>
<circle cx="60" cy="54" r="8" fill="#1e293b" stroke="#ffffff" stroke-width="1.5"/>'''
        },
        "fac_sed_corps": {
            "name": "SED CORPS",
            "col": "#ef5b55",
            "bg": "#1c0709",
            "sub": "SUPPRESSION CORPS",
            "svg": '''<polygon points="34,24 86,24 80,80 60,92 40,80" fill="#450a0a" stroke="#ef5b55" stroke-width="2.5"/>
<line x1="30" y1="84" x2="90" y2="24" stroke="#ffffff" stroke-width="3"/>
<line x1="90" y1="84" x2="30" y2="24" stroke="#ffffff" stroke-width="3"/>
<circle cx="60" cy="54" r="6" fill="#f1df76"/>'''
        },
        "fac_wardens": {
            "name": "CONTAINMENT WARDENS",
            "col": "#ef5b55",
            "bg": "#1c0709",
            "sub": "FACILITY SECURITY",
            "svg": '''<polygon points="34,24 86,24 80,80 60,92 40,80" fill="#450a0a" stroke="#ef5b55" stroke-width="2.5"/>
<rect x="42" y="44" width="36" height="6" rx="2" fill="#f1df76"/>
<circle cx="60" cy="64" r="6" fill="#ef5b55" stroke="#ffffff" stroke-width="1.2"/>'''
        },
        "fac_ucd_strike": {
            "name": "UCD STRIKE FORCE",
            "col": "#38bdf8",
            "bg": "#031526",
            "sub": "URBAN CRISIS DEFENSE",
            "svg": '''<circle cx="60" cy="54" r="28" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 2"/>
<polygon points="60,22 74,48 94,54 78,66 82,90 60,78 38,90 42,66 26,54 46,48" fill="#082f49" stroke="#38bdf8" stroke-width="1.8"/>
<circle cx="60" cy="56" r="5" fill="#f1df76"/>'''
        },
        "fac_giltong_enforcers": {
            "name": "GILTONG ENFORCERS",
            "col": "#f1df76",
            "bg": "#1c1402",
            "sub": "DISTRICT POLICE",
            "svg": '''<rect x="36" y="30" width="48" height="50" rx="4" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
<line x1="36" y1="55" x2="84" y2="55" stroke="#ffffff" stroke-width="2"/>
<circle cx="60" cy="42" r="6" fill="#ef5b55"/>
<circle cx="60" cy="68" r="6" fill="#f1df76"/>'''
        },
        "fac_memory_washers": {
            "name": "MEMORY WASHERS",
            "col": "#c084fc",
            "bg": "#130421",
            "sub": "COGNITIVE PURGERS",
            "svg": '''<circle cx="60" cy="54" r="26" fill="none" stroke="#c084fc" stroke-width="2" stroke-dasharray="6 3"/>
<ellipse cx="60" cy="54" rx="22" ry="12" fill="#3b0764" stroke="#38bdf8" stroke-width="1.8"/>
<line x1="38" y1="54" x2="82" y2="54" stroke="#ffffff" stroke-width="2.5"/>
<circle cx="60" cy="54" r="4" fill="#f1df76"/>'''
        },
        "fac_horizon_caravan": {
            "name": "HORIZON CARAVAN",
            "col": "#f1df76",
            "bg": "#1c1402",
            "sub": "NOMADIC TRADERS",
            "svg": '''<circle cx="60" cy="54" r="26" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
<polygon points="60,26 66,46 86,46 70,58 76,78 60,66 44,78 50,58 34,46 54,46" fill="#fef08a" stroke="#ffffff" stroke-width="1"/>
<circle cx="60" cy="54" r="4" fill="#ef5b55"/>'''
        },
        "fac_founding_corps": {
            "name": "FOUNDING CORPS",
            "col": "#71efaf",
            "bg": "#02140d",
            "sub": "ORIGIN BUILDERS",
            "svg": '''<polygon points="60,20 88,40 80,80 60,92 40,80 32,40" fill="#064e3b" stroke="#71efaf" stroke-width="2"/>
<line x1="60" y1="20" x2="60" y2="92" stroke="#f1df76" stroke-width="2"/>
<circle cx="60" cy="54" r="8" fill="#f1df76" stroke="#ffffff" stroke-width="1.5"/>'''
        }
    }

    for k, data in factions.items():
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="{data['bg']}" stroke="{data['col']}" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="none" stroke="{data['col']}" stroke-width="1.2" stroke-dasharray="6 3"/>
  {data['svg']}
  <text x="60" y="98" fill="{data['col']}" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="bold" text-anchor="middle">{data['name']}</text>
  <text x="60" y="108" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="5.5" font-weight="bold" text-anchor="middle">{data['sub']}</text>
</svg>'''
        # Write to all faction aliases
        for prefix in ["", "icon_faction_", "icon_"]:
            fn = f"{k}.svg" if not prefix else f"{prefix}{k.replace('fac_', '')}.svg"
            for d in [icons_dir, avatars_dir, hand_icons_dir, city_icons_dir, user_icons_dir]:
                with open(os.path.join(d, fn), "w", encoding="utf-8") as f:
                    f.write(svg)

    print("--- 2. GENERATING RICH DISTRICT & LOCATION BADGES ---")
    locations = {
        "icon_zone_a_core": ("ZONE A // SOVEREIGN CORE", "#71efaf", "#02140d", "SPIRE CENTER"),
        "icon_zone_b_rings": ("ZONE B // GILDED RINGS", "#f1df76", "#1c1402", "COMMERCIAL DISTRICT"),
        "icon_zone_c_foundry": ("ZONE C // THE FOUNDRY", "#ef5b55", "#1f0608", "EXTRACTION DISTRICT"),
        "icon_zone_d_outskirts": ("ZONE D // SUNKEN RESIDENTIAL", "#38bdf8", "#031526", "LOWER CITY"),
        "icon_zone_e_bulwark": ("ZONE E // FRONTIER BULWARK", "#ef5b55", "#1c0709", "PERIMETER WALL"),
        "icon_loc_the_maw": ("THE MAW // DEEP CHASM", "#c084fc", "#130421", "ABYSSAL TRENCH"),
        "icon_loc_hollow_glass": ("HOLLOW GLASS DISTRICT", "#38bdf8", "#041b2c", "PRISMATIC ARCHIVE"),
        "icon_loc_desolate_outskirts": ("DESOLATE OUTSKIRTS", "#cbd5e1", "#111827", "WASTELAND PERIMETER")
    }

    for k, (name, col, bg, sub) in locations.items():
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="{bg}" stroke="{col}" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="none" stroke="{col}" stroke-width="1.2" stroke-dasharray="6 3"/>
  <polygon points="60,22 88,40 88,72 60,88 32,72 32,40" fill="#0b1320" stroke="{col}" stroke-width="2"/>
  <circle cx="60" cy="54" r="8" fill="{col}"/>
  <line x1="60" y1="22" x2="60" y2="88" stroke="#ffffff" stroke-width="1.2" stroke-dasharray="3 3"/>
  <line x1="32" y1="54" x2="88" y2="54" stroke="#ffffff" stroke-width="1.2" stroke-dasharray="3 3"/>
  <text x="60" y="98" fill="{col}" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="bold" text-anchor="middle">{name}</text>
  <text x="60" y="108" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="5.5" font-weight="bold" text-anchor="middle">{sub}</text>
</svg>'''
        for d in [icons_dir, avatars_dir, hand_icons_dir, city_icons_dir, user_icons_dir]:
            with open(os.path.join(d, f"{k}.svg"), "w", encoding="utf-8") as f:
                f.write(svg)

    print("--- 3. GENERATING RICH WORK METHODS & HUD WIDGETS ---")
    work_types = {
        "wt_pugnahan": ("PUGNAHAN // COMBAT", "#ef5b55", "#1f0608", "STABILIZATION WORK"),
        "wt_flerehan": ("FLEREHAN // WEEPING", "#38bdf8", "#031526", "RESONANCE WORK"),
        "wt_ferrehan": ("FERREHAN // IRON", "#f1df76", "#1c1402", "REPRESSION WORK"),
        "wt_viderehan": ("VIDEREHAN // FORESIGHT", "#71efaf", "#02140d", "INSIGHT WORK"),
        "icon_sorrow_dohan_city": ("DOHAN // CITY SORROW", "#f1df76", "#1c1402", "METROPOLITAN ORIGIN"),
        "icon_sorrow_naehan_inner": ("NAEHAN // INNER SORROW", "#71efaf", "#02140d", "PSYCHE ORIGIN"),
        "icon_sorrow_oehan_outside": ("OEHAN // OUTSIDE SORROW", "#c084fc", "#130421", "ABYSSAL ORIGIN")
    }

    for k, (name, col, bg, sub) in work_types.items():
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="{bg}" stroke="{col}" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="none" stroke="{col}" stroke-width="1.2" stroke-dasharray="6 3"/>
  <circle cx="60" cy="52" r="22" fill="#040914" stroke="{col}" stroke-width="2"/>
  <polygon points="60,34 76,64 44,64" fill="{col}"/>
  <circle cx="60" cy="52" r="4" fill="#ffffff"/>
  <text x="60" y="98" fill="{col}" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="bold" text-anchor="middle">{name}</text>
  <text x="60" y="108" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="5.5" font-weight="bold" text-anchor="middle">{sub}</text>
</svg>'''
        for d in [icons_dir, user_icons_dir]:
            with open(os.path.join(d, f"{k}.svg"), "w", encoding="utf-8") as f:
                f.write(svg)
            # Aliases
            short_k = k.replace("wt_", "").replace("icon_sorrow_", "") + ".svg"
            with open(os.path.join(d, short_k), "w", encoding="utf-8") as f:
                f.write(svg)

    # Rich HUD Widgets
    hud_widgets = {
        "hud_resonance_wave.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="6" fill="#031526" stroke="#38bdf8" stroke-width="2.5"/>
  <path d="M 12,60 Q 30,20 48,60 T 84,60 T 108,60" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <line x1="12" y1="60" x2="108" y2="60" stroke="#f1df76" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="60" y="96" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">RESONANCE OSCILLATOR</text>
</svg>''',

        "hud_han_gauge.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="6" fill="#031526" stroke="#38bdf8" stroke-width="2.5"/>
  <path d="M 24,76 A 40 40 0 0 1 96,76" fill="none" stroke="#0c4a6e" stroke-width="10"/>
  <path d="M 24,76 A 40 40 0 0 1 84,40" fill="none" stroke="#38bdf8" stroke-width="10"/>
  <line x1="60" y1="76" x2="76" y2="44" stroke="#ef5b55" stroke-width="3" stroke-linecap="round"/>
  <circle cx="60" cy="76" r="6" fill="#f1df76"/>
  <text x="60" y="98" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">HAN FLUX // 98.4%</text>
</svg>''',

        "hud_containment_lock.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="6" fill="#1f0608" stroke="#ef5b55" stroke-width="2.5"/>
  <rect x="36" y="48" width="48" height="40" rx="4" fill="#450a0a" stroke="#ef5b55" stroke-width="2"/>
  <path d="M 44,48 L 44,34 Q 60,18 76,34 L 76,48" fill="none" stroke="#f1df76" stroke-width="4"/>
  <circle cx="60" cy="68" r="5" fill="#f1df76"/>
  <line x1="60" y1="68" x2="60" y2="78" stroke="#f1df76" stroke-width="2"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">CONTAINMENT LOCKED</text>
</svg>'''
    }

    for fname, code in hud_widgets.items():
        for d in [icons_dir, user_icons_dir]:
            with open(os.path.join(d, fname), "w", encoding="utf-8") as f:
                f.write(code)

    print("--- 4. UPGRADING ALL CATEGORY HERO BANNERS ---")
    category_banners = {
        "banner_entities.svg": ("SORROW ENTITIES REGISTRY", "SE-001 THROUGH SE-015 CLASSIFICATIONS", "#ef5b55", "#200609"),
        "banner_maw.svg": ("M.A.W. ARMAMENTS & SUITS", "MANIFESTED AGONY WEAPONS & WARDS", "#f1df76", "#1c1402"),
        "banner_characters.svg": ("PERSONNEL & ECHO-CORES", "DIRECTOR MAJIN & OPERATIONAL LEADS", "#38bdf8", "#031526"),
        "banner_departments.svg": ("FACILITY 01 // HAND OF CHANGE", "8 FLOORS & SUB-SECTOR BLUEPRINTS", "#71efaf", "#02140d"),
        "banner_factions.svg": ("FACTIONS & CITY GUILDS", "THE DIRECTORATE, HIGH COUNCIL & SYNDICATES", "#ef5b55", "#1c0709"),
        "banner_locations.svg": ("ATLAS & SOMNARAK METROPOLITAN", "ZONES A–E & DESOLATE PERIMETER", "#c084fc", "#130421"),
        "banner_lore.svg": ("LORE & THE 1,778 CYCLES", "ABSOLVOHAN SEED & COSMIC SORROWS", "#f1df76", "#1c1402"),
        "banner_mechanics.svg": ("BATTLE SYSTEMS & MECHANICS", "HAN FLUX, DAMAGE MATRIX & WORK PROTOCOLS", "#38bdf8", "#031526")
    }

    for fname, (title, sub, col, bg) in category_banners.items():
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad_{fname}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg}"/>
      <stop offset="60%" stop-color="#060912"/>
      <stop offset="100%" stop-color="#020408"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#bgGrad_{fname})"/>
  <!-- Blueprint Grid -->
  <line x1="40" y1="40" x2="1160" y2="40" stroke="{col}" stroke-width="1" stroke-dasharray="10 5" opacity="0.4"/>
  <line x1="40" y1="360" x2="1160" y2="360" stroke="{col}" stroke-width="1" stroke-dasharray="10 5" opacity="0.4"/>
  <line x1="100" y1="40" x2="100" y2="360" stroke="{col}" stroke-width="1" stroke-dasharray="10 5" opacity="0.4"/>
  <line x1="1100" y1="40" x2="1100" y2="360" stroke="{col}" stroke-width="1" stroke-dasharray="10 5" opacity="0.4"/>
  
  <!-- Outer Cybernetic Border -->
  <polygon points="20,20 1180,20 1180,380 20,380" fill="none" stroke="{col}" stroke-width="3"/>
  <polygon points="20,40 40,20 1160,20 1180,40 1180,360 1160,380 40,380 20,360" fill="none" stroke="#f1df76" stroke-width="1.2" stroke-dasharray="12 6"/>
  
  <!-- Left Thematic Emblem -->
  <g transform="translate(140, 110)">
    <polygon points="90,10 170,40 170,140 90,170 10,140 10,40" fill="#0b1320" stroke="{col}" stroke-width="4"/>
    <circle cx="90" cy="90" r="40" fill="none" stroke="{col}" stroke-width="3" stroke-dasharray="8 4"/>
    <polygon points="90,56 120,116 60,116" fill="{col}"/>
    <circle cx="90" cy="90" r="10" fill="#ffffff"/>
  </g>

  <!-- Typography & Meta -->
  <text x="360" y="150" fill="{col}" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="bold" letter-spacing="4">[ ARCHIVAL DATABASE DIRECTORY ]</text>
  <text x="360" y="210" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="44" font-weight="bold" letter-spacing="2">{title}</text>
  <text x="360" y="260" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="18" font-weight="bold" letter-spacing="1">{sub}</text>
  
  <!-- Bottom Status Bar -->
  <rect x="360" y="290" width="700" height="12" rx="2" fill="#0b1320" stroke="{col}" stroke-width="1"/>
  <rect x="362" y="292" width="580" height="8" rx="1" fill="{col}"/>
  <text x="1080" y="302" fill="{col}" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold">ONLINE</text>
</svg>'''
        with open(os.path.join(banners_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg)
        with open(os.path.join(icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg)
        # Hero banner variant
        hero_fname = f"banner_hero_{fname.replace('banner_', '')}"
        with open(os.path.join(banners_dir, hero_fname), "w", encoding="utf-8") as f:
            f.write(svg)

    print("--- 5. UPDATING DAMAGE TABLES & CSS LAYOUT TO PREVENT HORIZONTAL SCROLL ---")
    # Clean 4-Column Responsive Damage Table HTML
    clean_damage_table_html = '''        <div class="pm-table-wrapper" style="width:100%; max-width:100%; overflow-x:visible; margin:1rem 0;">
          <table class="pm-table" style="width:100%; max-width:100%; table-layout:fixed; border-collapse:collapse; border:2px solid #38bdf8;">
            <colgroup>
              <col style="width: 25%;">
              <col style="width: 18%;">
              <col style="width: 32%;">
              <col style="width: 25%;">
            </colgroup>
            <thead>
              <tr style="background:#081c2e; border-bottom:2px solid #38bdf8;">
                <th style="padding:10px; text-align:left; color:#38bdf8; font-family:'JetBrains Mono', monospace; font-size:0.85rem;">ELEMENT & SEAL</th>
                <th style="padding:10px; text-align:left; color:#38bdf8; font-family:'JetBrains Mono', monospace; font-size:0.85rem;">TARGET POOL</th>
                <th style="padding:10px; text-align:left; color:#38bdf8; font-family:'JetBrains Mono', monospace; font-size:0.85rem;">COMBAT TRAUMA & PHENOMENON</th>
                <th style="padding:10px; text-align:left; color:#38bdf8; font-family:'JetBrains Mono', monospace; font-size:0.85rem;">MITIGATION PROTOCOL</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #1e293b; background:#0c0f17;">
                <td style="padding:10px; vertical-align:middle;">
                  <div style="display:flex; align-items:center; gap:10px;">
                    <img src="assets/icons/damage_grudge.svg" alt="Grudge" style="width:44px; height:44px; flex-shrink:0; border:1.5px solid #ef4444; border-radius:6px; background:#180407;">
                    <div>
                      <strong style="color:#ef4444; font-size:0.95rem; display:block;">Grudge (원한)</strong>
                      <span class="badge badge-crimson" style="font-size:0.7rem; padding:2px 6px; background:#450a0a; color:#fca5a5; border:1px solid #ef4444;">Crimson</span>
                    </div>
                  </div>
                </td>
                <td style="padding:10px; vertical-align:middle;">
                  <strong style="color:#fca5a5; font-size:0.9rem;">Health Points (HP)</strong>
                </td>
                <td style="padding:10px; vertical-align:middle; font-size:0.82rem; color:#cbd5e1; line-height:1.4;">
                  Direct physical blunt force, deep lacerations, thermal searing, and severe bone fracturing.
                </td>
                <td style="padding:10px; vertical-align:middle; font-size:0.82rem; color:#94a3b8; line-height:1.4;">
                  Heavy M.A.W. Suits (<span style="color:#ef4444;">Resolve</span> affinity &le; 0.5 res).
                </td>
              </tr>
              <tr style="border-bottom:1px solid #1e293b; background:#070d18;">
                <td style="padding:10px; vertical-align:middle;">
                  <div style="display:flex; align-items:center; gap:10px;">
                    <img src="assets/icons/damage_lament.svg" alt="Lament" style="width:44px; height:44px; flex-shrink:0; border:1.5px solid #38bdf8; border-radius:6px; background:#031526;">
                    <div>
                      <strong style="color:#38bdf8; font-size:0.95rem; display:block;">Lament (비탄)</strong>
                      <span class="badge badge-somna" style="font-size:0.7rem; padding:2px 6px; background:#0c4a6e; color:#bae6fd; border:1px solid #38bdf8;">Deep Blue</span>
                    </div>
                  </div>
                </td>
                <td style="padding:10px; vertical-align:middle;">
                  <strong style="color:#38bdf8; font-size:0.9rem;">Sanity Points (SP)</strong>
                </td>
                <td style="padding:10px; vertical-align:middle; font-size:0.82rem; color:#cbd5e1; line-height:1.4;">
                  Cognitive acoustic hallucinations, deep grief paralysis, mental panic erosion, and self-harm.
                </td>
                <td style="padding:10px; vertical-align:middle; font-size:0.82rem; color:#94a3b8; line-height:1.4;">
                  Psychological M.A.W. Veils (<span style="color:#38bdf8;">Resilience</span> affinity) &amp; Insight routines.
                </td>
              </tr>
              <tr style="border-bottom:1px solid #1e293b; background:#0a0e14;">
                <td style="padding:10px; vertical-align:middle;">
                  <div style="display:flex; align-items:center; gap:10px;">
                    <img src="assets/icons/damage_void.svg" alt="Void" style="width:44px; height:44px; flex-shrink:0; border:1.5px solid #ffffff; border-radius:6px; background:#1e293b;">
                    <div>
                      <strong style="color:#ffffff; font-size:0.95rem; display:block;">Void (공허)</strong>
                      <span class="badge badge-pale" style="font-size:0.7rem; padding:2px 6px; background:#1e293b; color:#ffffff; border:1px solid #ffffff;">Pale White</span>
                    </div>
                  </div>
                </td>
                <td style="padding:10px; vertical-align:middle;">
                  <strong style="color:#ffffff; font-size:0.9rem;">Max HP % Dissolution</strong>
                </td>
                <td style="padding:10px; vertical-align:middle; font-size:0.82rem; color:#cbd5e1; line-height:1.4;">
                  Existential soul dissolution and memory erasure bypassing conventional physical defense.
                </td>
                <td style="padding:10px; vertical-align:middle; font-size:0.82rem; color:#94a3b8; line-height:1.4;">
                  Tier V &omega;-grade M.A.W. Suits (<span style="color:#ffffff;">Clarity</span> affinity required).
                </td>
              </tr>
              <tr style="border-bottom:1px solid #1e293b; background:#07080d;">
                <td style="padding:10px; vertical-align:middle;">
                  <div style="display:flex; align-items:center; gap:10px;">
                    <img src="assets/icons/damage_weight.svg" alt="Weight" style="width:44px; height:44px; flex-shrink:0; border:1.5px solid #94a3b8; border-radius:6px; background:#090d16;">
                    <div>
                      <strong style="color:#cbd5e1; font-size:0.95rem; display:block;">Weight (중압)</strong>
                      <span class="badge badge-dark" style="font-size:0.7rem; padding:2px 6px; background:#000000; color:#a1a1aa; border:1px solid #71717a;">Black</span>
                    </div>
                  </div>
                </td>
                <td style="padding:10px; vertical-align:middle;">
                  <strong style="color:#f1df76; font-size:0.9rem;">Dual HP &amp; SP Decay</strong>
                </td>
                <td style="padding:10px; vertical-align:middle; font-size:0.82rem; color:#cbd5e1; line-height:1.4;">
                  Simultaneous gravitic compression and dual corrosive decay crushing both body and sanity.
                </td>
                <td style="padding:10px; vertical-align:middle; font-size:0.82rem; color:#94a3b8; line-height:1.4;">
                  Balanced composite M.A.W. Plate (<span style="color:#f1df76;">Composure</span> affinity).
                </td>
              </tr>
              <tr style="border-bottom:1px solid #1e293b; background:#0b0a14;">
                <td style="padding:10px; vertical-align:middle;">
                  <div style="display:flex; align-items:center; gap:10px;">
                    <img src="assets/icons/damage_mixed.svg" alt="Mixed" style="width:44px; height:44px; flex-shrink:0; border:1.5px solid #c084fc; border-radius:6px; background:#090d16;">
                    <div>
                      <strong style="color:#c084fc; font-size:0.95rem; display:block;">Mixed (혼합)</strong>
                      <span class="badge" style="font-size:0.7rem; padding:2px 6px; background:linear-gradient(90deg, #ef4444, #f59e0b, #10b981, #38bdf8); color:#ffffff; font-weight:bold;">Rainbow</span>
                    </div>
                  </div>
                </td>
                <td style="padding:10px; vertical-align:middle;">
                  <strong style="color:#c084fc; font-size:0.9rem;">Multi-Spectral</strong>
                </td>
                <td style="padding:10px; vertical-align:middle; font-size:0.82rem; color:#cbd5e1; line-height:1.4;">
                  Chaotic sorrow resonance shifting dynamically between all elemental frequencies.
                </td>
                <td style="padding:10px; vertical-align:middle; font-size:0.82rem; color:#94a3b8; line-height:1.4;">
                  Adaptive multi-layer shielding &amp; rapid squad rotation.
                </td>
              </tr>
              <tr style="background:#140e02;">
                <td style="padding:10px; vertical-align:middle;">
                  <div style="display:flex; align-items:center; gap:10px;">
                    <img src="assets/icons/damage_hope.svg" alt="Hope" style="width:44px; height:44px; flex-shrink:0; border:1.5px solid #f1df76; border-radius:6px; background:#1c1202;">
                    <div>
                      <strong style="color:#f1df76; font-size:0.95rem; display:block;">Hope (희망)</strong>
                      <span class="badge badge-gold" style="font-size:0.7rem; padding:2px 6px; background:#451a03; color:#fef08a; border:1px solid #f1df76;">Golden</span>
                    </div>
                  </div>
                </td>
                <td style="padding:10px; vertical-align:middle;">
                  <strong style="color:#fef08a; font-size:0.9rem;">Cathartic Dawn / Soul</strong>
                </td>
                <td style="padding:10px; vertical-align:middle; font-size:0.82rem; color:#cbd5e1; line-height:1.4;">
                  Sovereign dawn resonance restoring corrupted psyches and stabilizing fractured Han-flux.
                </td>
                <td style="padding:10px; vertical-align:middle; font-size:0.82rem; color:#94a3b8; line-height:1.4;">
                  Absolvohan Core restoration protocols (Restorative).
                </td>
              </tr>
            </tbody>
          </table>
        </div>'''

    # Update index.html with the clean 4-column damage table
    index_path = os.path.join(wiki_root, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        index_html = f.read()

    # Replace the old damage table section in index.html
    old_table_pattern = re.compile(r'<div class="pm-table-wrapper">.*?</table>\s*</div>', re.DOTALL)
    if old_table_pattern.search(index_html):
        index_html = old_table_pattern.sub(clean_damage_table_html, index_html, count=1)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_html)
        print("Updated damage table in index.html to 100% responsive 4-column layout!")

    # CSS Enhancements in wiki.css to prevent horizontal scrolling on all tables
    css_path = os.path.join(assets_dir, "css/wiki.css")
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()

    css_patch = '''
/* --- GLOBAL ZERO HORIZONTAL SCROLL TABLE OPTIMIZATIONS --- */
.wiki-shell {
  max-width: 100% !important;
  box-sizing: border-box !important;
}

.wiki-content {
  min-width: 0 !important;
  max-width: 100% !important;
  overflow-x: hidden !important;
  box-sizing: border-box !important;
}

.pm-table-wrapper, .table-container, .table-wrap {
  width: 100% !important;
  max-width: 100% !important;
  overflow-x: auto !important;
  box-sizing: border-box !important;
  margin: 1.2rem 0 !important;
}

.pm-table, .wiki-table, .data-table {
  width: 100% !important;
  max-width: 100% !important;
  border-collapse: collapse !important;
  box-sizing: border-box !important;
  word-wrap: break-word !important;
  overflow-wrap: break-word !important;
}

.pm-table th, .pm-table td, .wiki-table th, .wiki-table td {
  padding: 8px 10px !important;
  font-size: 0.85rem !important;
  line-height: 1.4 !important;
  word-wrap: break-word !important;
  overflow-wrap: break-word !important;
  box-sizing: border-box !important;
}
'''
    if "GLOBAL ZERO HORIZONTAL SCROLL TABLE OPTIMIZATIONS" not in css_content:
        with open(css_path, "a", encoding="utf-8") as f:
            f.write(css_patch)
        print("Appended global zero horizontal scroll rules to wiki.css!")

if __name__ == "__main__":
    master_upgrade()
