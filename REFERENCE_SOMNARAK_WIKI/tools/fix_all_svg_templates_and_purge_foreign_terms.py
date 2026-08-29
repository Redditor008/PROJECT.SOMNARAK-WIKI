import os
import re

def fix_all_svgs_and_purge():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    banners_dir = os.path.join(wiki_root, "assets/banners")
    icons_dir = os.path.join(wiki_root, "assets/icons")
    blueprints_dir = os.path.join(wiki_root, "assets/layout/hand/blueprints")
    user_icons_dir = "/home/user/icons"

    # 1. COMPLETELY BESPOKE FLOOR MINI-BANNERS FOR RIGHT SIDEBAR (340x85 viewBox, unique shapes)
    floor_banners = {
        "floor_banner_f1_neutral.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <rect x="2" y="2" width="336" height="81" rx="6" fill="#04140d" stroke="#71efaf" stroke-width="2"/>
  <!-- Bespoke Pyramid Spire & Holographic Command Beacon -->
  <polygon points="44,14 66,68 22,68" fill="#0a3827" stroke="#71efaf" stroke-width="2"/>
  <circle cx="44" cy="36" r="6" fill="#f1df76" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="32" y1="52" x2="56" y2="52" stroke="#f1df76" stroke-width="1.5"/>
  <!-- Typography & Meta -->
  <text x="80" y="24" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">[F1 // SOVEREIGN PALM]</text>
  <text x="80" y="46" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">NEUTRAL COMMAND</text>
  <text x="80" y="66" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9.5">LEAD: <tspan fill="#f1df76">MAJIN</tspan> | SECTOR: <tspan fill="#71efaf">PALM CORE</tspan></text>
  <!-- Chevron -->
  <polygon points="318,42 308,32 312,28 326,42 312,56 308,52" fill="#71efaf"/>
</svg>''',

        "floor_banner_f2_maws_keep.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <rect x="2" y="2" width="336" height="81" rx="6" fill="#1f0709" stroke="#ef5b55" stroke-width="2"/>
  <!-- Bespoke Forging Anvil & Crushing Sledgehammer -->
  <path d="M 22,46 L 66,46 L 60,56 L 52,56 L 56,70 L 64,74 L 24,74 L 32,70 L 36,56 L 28,56 Z" fill="#4d1217" stroke="#ef5b55" stroke-width="1.5"/>
  <rect x="36" y="22" width="16" height="10" rx="2" fill="#f1df76"/>
  <line x1="44" y1="16" x2="44" y2="38" stroke="#ffffff" stroke-width="2"/>
  <!-- Typography & Meta -->
  <text x="80" y="24" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">[F2 // KINETIC FORGE]</text>
  <text x="80" y="46" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">MAW'S KEEP</text>
  <text x="80" y="66" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9.5">LEAD: <tspan fill="#f1df76">DEKAN</tspan> | SECTOR: <tspan fill="#ef5b55">WARD KEEP</tspan></text>
  <polygon points="318,42 308,32 312,28 326,42 312,56 308,52" fill="#ef5b55"/>
</svg>''',

        "floor_banner_f3_extraction.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <rect x="2" y="2" width="336" height="81" rx="6" fill="#041624" stroke="#38bdf8" stroke-width="2"/>
  <!-- Bespoke Distillation Retort & Han Pressure Coil -->
  <path d="M 38,20 L 50,20 L 50,38 L 62,64 C 66,74 56,78 44,78 C 32,78 22,74 26,64 L 38,38 Z" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.8"/>
  <circle cx="44" cy="62" r="7" fill="#f1df76"/>
  <!-- Typography & Meta -->
  <text x="80" y="24" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">[F3 // FLUX SIPHON]</text>
  <text x="80" y="46" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">EXTRACTION HALL</text>
  <text x="80" y="66" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9.5">LEAD: <tspan fill="#f1df76">ZYRAK</tspan> | SECTOR: <tspan fill="#38bdf8">SIPHON FORGE</tspan></text>
  <polygon points="318,42 308,32 312,28 326,42 312,56 308,52" fill="#38bdf8"/>
</svg>''',

        "floor_banner_f4_insight_forge.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <rect x="2" y="2" width="336" height="81" rx="6" fill="#1c1402" stroke="#f1df76" stroke-width="2"/>
  <!-- Bespoke Prismatic Compass Star & Lens Array -->
  <polygon points="44,16 52,34 70,36 56,48 62,66 44,56 26,66 32,48 18,36 36,34" fill="#4d3b07" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="44" cy="42" r="8" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
  <!-- Typography & Meta -->
  <text x="80" y="24" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">[F4 // NEURAL MATRIX]</text>
  <text x="80" y="46" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">INSIGHT FORGE</text>
  <text x="80" y="66" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9.5">LEAD: <tspan fill="#71efaf">AYSHUK</tspan> | SECTOR: <tspan fill="#f1df76">RESEARCH LABS</tspan></text>
  <polygon points="318,42 308,32 312,28 326,42 312,56 308,52" fill="#f1df76"/>
</svg>''',

        "floor_banner_f5_border_watch.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <rect x="2" y="2" width="336" height="81" rx="6" fill="#1c0709" stroke="#ef5b55" stroke-width="2"/>
  <!-- Bespoke Fortress Rampart Wall & Searchlight -->
  <polygon points="22,34 32,34 32,42 42,42 42,34 56,34 56,42 66,42 66,34 66,72 22,72" fill="#4a1219" stroke="#ef5b55" stroke-width="1.5"/>
  <circle cx="44" cy="54" r="5" fill="#f1df76"/>
  <!-- Typography & Meta -->
  <text x="80" y="24" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">[F5 // BULWARK GRID]</text>
  <text x="80" y="46" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">BORDER WATCH</text>
  <text x="80" y="66" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9.5">LEAD: <tspan fill="#f1df76">MELLDA</tspan> | SECTOR: <tspan fill="#ef5b55">FRONTIER BASTION</tspan></text>
  <polygon points="318,42 308,32 312,28 326,42 312,56 308,52" fill="#ef5b55"/>
</svg>''',

        "floor_banner_f6_deep_vault.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <rect x="2" y="2" width="336" height="81" rx="6" fill="#120420" stroke="#c084fc" stroke-width="2"/>
  <!-- Bespoke Bank Vault Gear & Triple Lock Tumbler -->
  <circle cx="44" cy="44" r="26" fill="#2b0d4d" stroke="#f1df76" stroke-width="1.8" stroke-dasharray="5 3"/>
  <circle cx="44" cy="44" r="14" fill="#090212" stroke="#38bdf8" stroke-width="1.5"/>
  <circle cx="44" cy="40" r="4" fill="#f1df76"/>
  <!-- Typography & Meta -->
  <text x="80" y="24" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">[F6 // CRYO ARCHIVE]</text>
  <text x="80" y="46" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">DEEP VAULT</text>
  <text x="80" y="66" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9.5">LEAD: <tspan fill="#38bdf8">MARJUK</tspan> | SECTOR: <tspan fill="#c084fc">CLASSIFIED VAULTS</tspan></text>
  <polygon points="318,42 308,32 312,28 326,42 312,56 308,52" fill="#c084fc"/>
</svg>''',

        "floor_banner_f7_shadow_corps.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <rect x="2" y="2" width="336" height="81" rx="6" fill="#0f0204" stroke="#ef5b55" stroke-width="2"/>
  <!-- Bespoke Crescent Scythes & Shadow Dagger -->
  <path d="M 22,26 Q 44,42 22,66 Q 38,50 22,26 Z" fill="#ef5b55" stroke="#ffffff" stroke-width="1"/>
  <path d="M 66,26 Q 44,42 66,66 Q 50,50 66,26 Z" fill="#ef5b55" stroke="#ffffff" stroke-width="1"/>
  <polygon points="44,18 48,54 44,68 40,54" fill="#f1df76"/>
  <!-- Typography & Meta -->
  <text x="80" y="24" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">[F7 // SHADOW CORPS]</text>
  <text x="80" y="46" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">SHADOW CORPS</text>
  <text x="80" y="66" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9.5">LEAD: <tspan fill="#ffffff">ISHALL</tspan> | SECTOR: <tspan fill="#ef5b55">RAPID STRIKE</tspan></text>
  <polygon points="318,42 308,32 312,28 326,42 312,56 308,52" fill="#ef5b55"/>
</svg>''',

        "floor_banner_f8_gate_watch.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 85" width="100%" height="100%">
  <rect x="2" y="2" width="336" height="81" rx="6" fill="#1a1202" stroke="#f1df76" stroke-width="2"/>
  <!-- Bespoke Stone Gateway Arch & Portcullis Grate -->
  <path d="M 22,72 L 22,36 Q 44,16 66,36 L 66,72 L 56,72 L 56,44 Q 44,30 32,44 L 32,72 Z" fill="#4d3707" stroke="#f1df76" stroke-width="1.8"/>
  <line x1="38" y1="38" x2="38" y2="72" stroke="#ef5b55" stroke-width="1.5"/>
  <line x1="44" y1="32" x2="44" y2="72" stroke="#ef5b55" stroke-width="1.5"/>
  <line x1="50" y1="38" x2="50" y2="72" stroke="#ef5b55" stroke-width="1.5"/>
  <!-- Typography & Meta -->
  <text x="80" y="24" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">[F8 // ABYSSAL GATE]</text>
  <text x="80" y="46" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">GATE WATCH</text>
  <text x="80" y="66" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9.5">LEAD: <tspan fill="#c084fc">XYAN</tspan> | SECTOR: <tspan fill="#f1df76">DESOLATE GATE</tspan></text>
  <polygon points="318,42 308,32 312,28 326,42 312,56 308,52" fill="#f1df76"/>
</svg>'''
    }

    for fname, svg_str in floor_banners.items():
        with open(os.path.join(banners_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg_str)

    print("Redesigned all 8 floor mini-banners with 100% bespoke vector shapes!")

    # 2. REGENERATE SECC RISK ICONS (Pure Canonical SECC Tiers)
    secc_risks = {
        "icon_risk_t01_aether.svg": ("AETHER", "α", "#71efaf", "#064e3b"),
        "icon_risk_t02_somna.svg": ("SOMNA", "β", "#38bdf8", "#0369a1"),
        "icon_risk_t03_morphean.svg": ("MORPHEAN", "γ", "#f1df76", "#a16207"),
        "icon_risk_t04_phantasm.svg": ("PHANTASM", "δ", "#ef5b55", "#b91c1c"),
        "icon_risk_t05_apocrypha.svg": ("APOCRYPHA", "ω", "#c084fc", "#6b21a8")
    }

    for fname, (name, greek, col, bg) in secc_risks.items():
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <polygon points="50,4 96,50 50,96 4,50" fill="{bg}" stroke="{col}" stroke-width="4"/>
  <text x="50" y="44" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">{greek}</text>
  <text x="50" y="62" fill="{col}" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" text-anchor="middle">{name}</text>
</svg>'''
        with open(os.path.join(icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg)
        with open(os.path.join(user_icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg)

    # Replace legacy risk icon files
    legacy_map = {
        "icon_risk_t01_can.svg": "icon_risk_t01_aether.svg",
        "icon_risk_t02_teth.svg": "icon_risk_t02_somna.svg",
        "icon_risk_t03_he.svg": "icon_risk_t03_morphean.svg",
        "icon_risk_t04_waw.svg": "icon_risk_t04_phantasm.svg",
        "icon_risk_t05_aleph.svg": "icon_risk_t05_apocrypha.svg",
        "risk_zayin.svg": "icon_risk_t01_aether.svg",
        "risk_teth.svg": "icon_risk_t02_somna.svg",
        "risk_he.svg": "icon_risk_t03_morphean.svg",
        "risk_waw.svg": "icon_risk_t04_phantasm.svg",
        "risk_aleph.svg": "icon_risk_t05_apocrypha.svg"
    }

    for leg, targ in legacy_map.items():
        targ_path = os.path.join(icons_dir, targ)
        if os.path.exists(targ_path):
            with open(targ_path, "r", encoding="utf-8") as f:
                c = f.read()
            with open(os.path.join(icons_dir, leg), "w", encoding="utf-8") as f:
                f.write(c)
            with open(os.path.join(user_icons_dir, leg), "w", encoding="utf-8") as f:
                f.write(c)

    # 3. PURGE ALL L-CORP VOCABULARY IN ALL FILES (.html, .svg)
    search_dirs = [wiki_root, user_icons_dir, "/home/user/diagrams"]
    term_replacements = [
        # Risk Tiers
        (re.compile(r'\bALEPH\b', re.IGNORECASE), "APOCRYPHA"),
        (re.compile(r'\bWAW\b', re.IGNORECASE), "PHANTASM"),
        (re.compile(r'\bHE\b(?!\s*=\s*|\s*>\s*|\s*<\s*)'), "MORPHEAN"),
        (re.compile(r'\bTETH\b', re.IGNORECASE), "SOMNA"),
        (re.compile(r'\bZAYIN\b', re.IGNORECASE), "AETHER"),
        (re.compile(r'\bT-05 ALEPH\b', re.IGNORECASE), "T-05 APOCRYPHA"),
        (re.compile(r'\bT-04 WAW\b', re.IGNORECASE), "T-04 PHANTASM"),
        (re.compile(r'\bT-03 HE\b', re.IGNORECASE), "T-03 MORPHEAN"),
        (re.compile(r'\bT-02 TETH\b', re.IGNORECASE), "T-02 SOMNA"),
        (re.compile(r'\bT-01 ZAYIN\b', re.IGNORECASE), "T-01 AETHER"),
        (re.compile(r'\bT-01 CAN\b', re.IGNORECASE), "T-01 AETHER"),
        # Foreign Terms
        (re.compile(r'Qliphoth\s+Counter', re.IGNORECASE), "Coherence Counter"),
        (re.compile(r'Qliphoth', re.IGNORECASE), "Coherence"),
        (re.compile(r'Sephirah', re.IGNORECASE), "Echo-Core Lead"),
        (re.compile(r'Sephirot', re.IGNORECASE), "Echo-Cores"),
        (re.compile(r'Abnormality', re.IGNORECASE), "Sorrow Entity"),
        (re.compile(r'Abnormalities', re.IGNORECASE), "Sorrow Entities"),
        (re.compile(r'Enkephalin', re.IGNORECASE), "Han-Flux"),
        (re.compile(r'E\.G\.O', re.IGNORECASE), "M.A.W."),
        (re.compile(r'Lobotomy\s+Corporation', re.IGNORECASE), "The Reverie Directorate"),
        (re.compile(r'Lobotomy', re.IGNORECASE), "Somnarak")
    ]

    for s_dir in search_dirs:
        for root, dirs, files in os.walk(s_dir):
            for file in files:
                if file.endswith(('.html', '.svg', '.json', '.md')):
                    # Skip research archives
                    if "01_Comparative_Wiki_Research" in root:
                        continue
                    fpath = os.path.join(root, file)
                    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                        text = f.read()

                    orig_text = text
                    for pattern, repl in term_replacements:
                        text = pattern.sub(repl, text)

                    if text != orig_text:
                        with open(fpath, "w", encoding="utf-8") as f:
                            f.write(text)

    print("Purged all foreign vocabulary across all SVG and HTML files!")

if __name__ == "__main__":
    fix_all_svgs_and_purge()
