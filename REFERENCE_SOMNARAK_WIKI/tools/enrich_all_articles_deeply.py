import os, re
from bs4 import BeautifulSoup

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# Entity triad mapping
ENTITY_TRIAD_MAP = {
    "se-001": {
        "name": "The Orphaned Bell", "slug": "the-orphaned-bell", "tier": "T-01 CAN", "risk_icon": "icon_risk_t01_can.svg", "floor": "Floor 1: Neutral Command", "floor_link": "../departments/floor-1-neutral-command.html",
        "wpn": ("maw-w-001-01-the-laments-requiem.html", "Lament's Requiem", "../assets/art/maw/maw-w-001-01.svg"),
        "suit": ("maw-s-001-01-the-laments-shroud.html", "The Lament's Shroud", "../assets/art/maw/maw-s-001-01.svg"),
        "gift": ("maw-g-001-01-laments-edge.html", "Lament's Edge", "../assets/art/maw/maw-g-001-01.svg"),
        "resists": {"red": ("1.0x", "val-normal"), "white": ("1.0x", "val-normal"), "black": ("1.5x", "val-weak"), "pale": ("2.0x", "val-weak")},
        "works": {"instinct": "Very High (70%)", "insight": "Common (50%)", "attachment": "Low (30%)", "repression": "Very Low (10%)"}
    },
    "se-002": {
        "name": "The Grieving Colossus", "slug": "the-grieving-colossus", "tier": "T-02 TETH", "risk_icon": "icon_risk_t02_teth.svg", "floor": "Floor 2: Maw's Keep", "floor_link": "../departments/floor-2-maws-keep.html",
        "wpn": ("maw-w-002-01-the-mourning-maul.html", "The Mourning Maul", "../assets/art/maw/maw-w-002-01.svg"),
        "suit": ("maw-s-002-01-the-mourning-mantle.html", "The Mourning Mantle", "../assets/art/maw/maw-s-002-01.svg"),
        "gift": ("maw-g-002-01-the-mourning-shell.html", "The Mourning Shell", "../assets/art/maw/maw-g-002-01.svg"),
        "resists": {"red": ("0.5x", "val-resist"), "white": ("1.2x", "val-weak"), "black": ("1.0x", "val-normal"), "pale": ("1.5x", "val-weak")},
        "works": {"instinct": "Low (25%)", "insight": "Common (45%)", "attachment": "Low (20%)", "repression": "High (65%)"}
    },
    "se-003": {
        "name": "The Wilderness Tide", "slug": "the-wilderness-tide", "tier": "T-02 TETH", "risk_icon": "icon_risk_t02_teth.svg", "floor": "Zone E: Outskirts", "floor_link": "../locations/zone-e-perimeter-bulwark.html",
        "wpn": ("maw-w-001-01-the-laments-requiem.html", "Resonance Wave", "../assets/icons/weapon.svg"),
        "suit": ("maw-s-001-01-the-laments-shroud.html", "Tide Shroud", "../assets/icons/suit.svg"),
        "gift": ("maw-g-001-01-laments-edge.html", "Saline Brooch", "../assets/icons/gift.svg"),
        "resists": {"red": ("1.2x", "val-weak"), "white": ("1.0x", "val-normal"), "black": ("0.6x", "val-resist"), "pale": ("1.5x", "val-weak")},
        "works": {"instinct": "Low (20%)", "insight": "Very High (70%)", "attachment": "Common (40%)", "repression": "Low (20%)"}
    },
    "se-005": {
        "name": "The Smothering Mother", "slug": "the-smothering-mother", "tier": "T-03 HE", "risk_icon": "icon_risk_t03_he.svg", "floor": "Floor 2: Maw's Keep", "floor_link": "../departments/floor-2-maws-keep.html",
        "wpn": ("maw-w-005-01-the-embrace-fang.html", "The Embrace Fang", "../assets/art/maw/maw-w-005-01.svg"),
        "suit": ("maw-s-005-01-the-embrace-plate.html", "The Embrace Plate", "../assets/art/maw/maw-s-005-01.svg"),
        "gift": ("maw-g-005-01-the-embrace.html", "The Embrace", "../assets/art/maw/maw-g-005-01.svg"),
        "resists": {"red": ("1.2x", "val-weak"), "white": ("0.6x", "val-resist"), "black": ("1.0x", "val-normal"), "pale": ("1.5x", "val-weak")},
        "works": {"instinct": "Low (20%)", "insight": "Low (25%)", "attachment": "Very High (75%)", "repression": "Fatal (0%)"}
    },
    "se-007": {
        "name": "Brume", "slug": "brume", "tier": "T-03 HE", "risk_icon": "icon_risk_t03_he.svg", "floor": "Floor 4: Insight Forge", "floor_link": "../departments/floor-4-insight-forge.html",
        "wpn": ("maw-w-007-01-the-hope-lens.html", "The Hope Lens", "../assets/art/maw/maw-w-007-01.svg"),
        "suit": ("maw-s-007-01-the-hope-veil.html", "The Hope Veil", "../assets/art/maw/maw-s-007-01.svg"),
        "gift": ("maw-g-007-01-the-hope-lantern.html", "The Hope Lantern", "../assets/art/maw/maw-g-007-01.svg"),
        "resists": {"red": ("1.5x", "val-weak"), "white": ("0.5x", "val-resist"), "black": ("0.8x", "val-resist"), "pale": ("1.2x", "val-weak")},
        "works": {"instinct": "Low (30%)", "insight": "Very High (70%)", "attachment": "Common (40%)", "repression": "Low (20%)"}
    },
    "se-009": {
        "name": "The Memory Weaver", "slug": "the-memory-weaver", "tier": "T-04 WAW", "risk_icon": "icon_risk_t04_waw.svg", "floor": "Floor 4: Insight Forge", "floor_link": "../departments/floor-4-insight-forge.html",
        "wpn": ("maw-w-009-01-the-forgotten-lens.html", "The Forgotten Lens", "../assets/art/maw/maw-w-009-01.svg"),
        "suit": ("maw-s-009-01-the-forgotten-veil.html", "The Forgotten Veil", "../assets/art/maw/maw-s-009-01.svg"),
        "gift": ("maw-g-009-01-the-forgotten-mask.html", "The Forgotten Mask", "../assets/art/maw/maw-g-009-01.svg"),
        "resists": {"red": ("1.0x", "val-normal"), "white": ("0.7x", "val-resist"), "black": ("0.5x", "val-resist"), "pale": ("1.4x", "val-weak")},
        "works": {"instinct": "Low (15%)", "insight": "High (65%)", "attachment": "Common (45%)", "repression": "Low (20%)"}
    },
    "se-010": {
        "name": "The Convergence", "slug": "the-convergence", "tier": "T-05 ALEPH", "risk_icon": "icon_risk_t05_aleph.svg", "floor": "Floor 6: Deep Vault", "floor_link": "../departments/floor-6-deep-vault.html",
        "wpn": ("maw-w-010-01-the-absolute-maul.html", "The Absolute Maul", "../assets/art/maw/maw-w-010-01.svg"),
        "suit": ("maw-s-010-01-the-absolute-mantle.html", "The Absolute Mantle", "../assets/art/maw/maw-s-010-01.svg"),
        "gift": ("maw-g-010-01-the-absolute-verdict.html", "The Absolute Verdict", "../assets/art/maw/maw-g-010-01.svg"),
        "resists": {"red": ("0.3x", "val-resist"), "white": ("0.3x", "val-resist"), "black": ("0.3x", "val-resist"), "pale": ("0.5x", "val-resist")},
        "works": {"instinct": "Very Low (10%)", "insight": "Low (20%)", "attachment": "Low (15%)", "repression": "High (55%)"}
    },
    "se-011": {
        "name": "The Whispering Walls", "slug": "the-whispering-walls", "tier": "T-03 HE", "risk_icon": "icon_risk_t03_he.svg", "floor": "Floor 5: Border Watch", "floor_link": "../departments/floor-5-border-watch.html",
        "wpn": ("maw-w-011-01-the-listening-requiem.html", "The Listening Requiem", "../assets/art/maw/maw-w-011-01.svg"),
        "suit": ("maw-s-011-01-the-listening-shroud.html", "The Listening Shroud", "../assets/art/maw/maw-s-011-01.svg"),
        "gift": ("maw-g-011-01-the-listening-stone.html", "The Listening Stone", "../assets/art/maw/maw-g-011-01.svg"),
        "resists": {"red": ("0.8x", "val-resist"), "white": ("0.5x", "val-resist"), "black": ("1.2x", "val-weak"), "pale": ("1.5x", "val-weak")},
        "works": {"instinct": "High (60%)", "insight": "Common (40%)", "attachment": "Low (20%)", "repression": "Low (20%)"}
    },
    "se-014": {
        "name": "The Debt Eater", "slug": "the-debt-eater", "tier": "T-04 WAW", "risk_icon": "icon_risk_t04_waw.svg", "floor": "Floor 7: Shadow Corps", "floor_link": "../departments/floor-7-shadow-corps.html",
        "wpn": ("maw-w-014-01-the-debt-lens.html", "The Debt Lens", "../assets/art/maw/maw-w-014-01.svg"),
        "suit": ("maw-s-014-01-the-debt-veil.html", "The Debt Veil", "../assets/art/maw/maw-s-014-01.svg"),
        "gift": ("maw-g-014-01-the-debt-scale-gift.html", "The Debt Scale Gift", "../assets/art/maw/maw-g-014-01.svg"),
        "resists": {"red": ("1.2x", "val-weak"), "white": ("1.0x", "val-normal"), "black": ("0.4x", "val-resist"), "pale": ("1.5x", "val-weak")},
        "works": {"instinct": "Low (15%)", "insight": "Low (20%)", "attachment": "Common (40%)", "repression": "High (60%)"}
    },
    "se-015": {
        "name": "The Debt Scale", "slug": "the-debt-scale", "tier": "T-04 WAW", "risk_icon": "icon_risk_t04_waw.svg", "floor": "Floor 8: Gate Watch", "floor_link": "../departments/floor-8-gate-watch.html",
        "wpn": ("maw-w-015-01-the-balance-lens.html", "The Balance Lens", "../assets/art/maw/maw-w-015-01.svg"),
        "suit": ("maw-s-015-01-the-balance-veil.html", "The Balance Veil", "../assets/art/maw/maw-s-015-01.svg"),
        "gift": ("maw-g-015-01-the-balance-pendant.html", "The Balance Pendant", "../assets/art/maw/maw-g-015-01.svg"),
        "resists": {"red": ("1.0x", "val-normal"), "white": ("0.8x", "val-resist"), "black": ("0.8x", "val-resist"), "pale": ("0.4x", "val-resist")},
        "works": {"instinct": "Low (20%)", "insight": "Common (45%)", "attachment": "High (65%)", "repression": "Low (25%)"}
    }
}

# 1. Update Sorrow Entity pages
entity_files = [f for f in os.listdir(os.path.join(WIKI_DIR, "entities")) if f.startswith("se-") and f.endswith(".html")]
for ef in entity_files:
    m = re.search(r'se-(\d+)', ef)
    if not m:
        continue
    num = int(m.group(1))
    normalized_code = f"se-{num:03d}"
    
    triad_data = ENTITY_TRIAD_MAP.get(normalized_code)
    if not triad_data:
        continue
        
    file_path = os.path.join(WIKI_DIR, "entities", ef)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    res = triad_data["resists"]
    wks = triad_data["works"]
    
    tactical_boxes = f'''
    <!-- Tactical Damage Resistance Matrix -->
    <div class="wiki-section">
      <div class="section-banner">
        <h2>/// TACTICAL DEFENSE &amp; DAMAGE MULTIPLIERS</h2>
        <span class="section-tag">SECC COMBAT RADAR</span>
      </div>
      <div class="tactical-resist-grid">
        <div class="resist-cell">
          <img src="../assets/icons/icon_damage_physical_red.svg" alt="Physical">
          <div class="resist-meta"><span class="resist-name" style="color:#ef4444;">PHYSICAL (RED)</span><span class="resist-val {res['red'][1]}">{res['red'][0]} MULTIPLIER</span></div>
        </div>
        <div class="resist-cell">
          <img src="../assets/icons/icon_damage_mental_white.svg" alt="Mental">
          <div class="resist-meta"><span class="resist-name" style="color:#38bdf8;">MENTAL (WHITE)</span><span class="resist-val {res['white'][1]}">{res['white'][0]} MULTIPLIER</span></div>
        </div>
        <div class="resist-cell">
          <img src="../assets/icons/icon_damage_corrosive_black.svg" alt="Corrosive">
          <div class="resist-meta"><span class="resist-name" style="color:#a855f7;">CORROSIVE (BLACK)</span><span class="resist-val {res['black'][1]}">{res['black'][0]} MULTIPLIER</span></div>
        </div>
        <div class="resist-cell">
          <img src="../assets/icons/icon_damage_pale_cyan.svg" alt="Pale">
          <div class="resist-meta"><span class="resist-name" style="color:#f1df76;">PALE (EXTINCTION)</span><span class="resist-val {res['pale'][1]}">{res['pale'][0]} MULTIPLIER</span></div>
        </div>
      </div>
    </div>

    <!-- Work Type Success Rates -->
    <div class="wiki-section">
      <div class="section-banner">
        <h2>/// CONTAINMENT WORK AFFINITY MATRIX</h2>
        <span class="section-tag">THE 4 HARVEST METHODS</span>
      </div>
      <div class="work-affinity-grid">
        <div class="work-affinity-cell">
          <img src="../assets/icons/icon_work_instinct_red.svg" alt="Instinct">
          <div class="work-meta"><span class="work-name">INSTINCT (FERREHAN)</span><span class="work-rate">{wks['instinct']}</span></div>
        </div>
        <div class="work-affinity-cell">
          <img src="../assets/icons/icon_work_insight_white.svg" alt="Insight">
          <div class="work-meta"><span class="work-name">INSIGHT (VIDEREHAN)</span><span class="work-rate">{wks['insight']}</span></div>
        </div>
        <div class="work-affinity-cell">
          <img src="../assets/icons/icon_work_attachment_black.svg" alt="Attachment">
          <div class="work-meta"><span class="work-name">ATTACHMENT (FLEREHAN)</span><span class="work-rate">{wks['attachment']}</span></div>
        </div>
        <div class="work-affinity-cell">
          <img src="../assets/icons/icon_work_repression_cyan.svg" alt="Repression">
          <div class="work-meta"><span class="work-name">REPRESSION (PUGNAHAN)</span><span class="work-rate">{wks['repression']}</span></div>
        </div>
      </div>
    </div>

    <!-- Extracted M.A.W. Equipment Triad -->
    <div class="maw-triad-box">
      <div class="maw-triad-header">EXTRACTABLE M.A.W. ARMAMENT TRIAD ({triad_data['name'].upper()})</div>
      <div class="maw-triad-grid">
        <a href="../maw/{triad_data['wpn'][0]}" class="triad-card">
          <img src="{triad_data['wpn'][2]}" alt="Weapon">
          <div class="triad-meta"><span class="triad-type">M.A.W. WEAPON</span><span class="triad-name">{triad_data['wpn'][1]}</span></div>
        </a>
        <a href="../maw/{triad_data['suit'][0]}" class="triad-card">
          <img src="{triad_data['suit'][2]}" alt="Suit">
          <div class="triad-meta"><span class="triad-type">M.A.W. SUIT</span><span class="triad-name">{triad_data['suit'][1]}</span></div>
        </a>
        <a href="../maw/{triad_data['gift'][0]}" class="triad-card">
          <img src="{triad_data['gift'][2]}" alt="Gift">
          <div class="triad-meta"><span class="triad-type">M.A.W. GIFT</span><span class="triad-name">{triad_data['gift'][1]}</span></div>
        </a>
      </div>
    </div>
    '''
    
    if 'TACTICAL DEFENSE &amp; DAMAGE MULTIPLIERS' not in content:
        if '<section class="cross-reference-section">' in content:
            content = content.replace('<section class="cross-reference-section">', f'{tactical_boxes}\n<section class="cross-reference-section">', 1)
        elif '<footer class="wiki-footer">' in content:
            content = content.replace('<footer class="wiki-footer">', f'{tactical_boxes}\n<footer class="wiki-footer">', 1)
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Enriched all Sorrow Entity articles with Damage Matrices and Triad Gear boxes.")

# 2. Update MAW Equipment subpages with Triad boxes
maw_files = [f for f in os.listdir(os.path.join(WIKI_DIR, "maw")) if f.startswith("maw-") and f.endswith(".html")]
for mf in maw_files:
    m = re.search(r'maw-[wsg]-(\d+)', mf)
    if not m:
        continue
    num = int(m.group(1))
    normalized_code = f"se-{num:03d}"
    
    triad_data = ENTITY_TRIAD_MAP.get(normalized_code)
    if not triad_data:
        continue
        
    file_path = os.path.join(WIKI_DIR, "maw", mf)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    entity_file_name = f"se-{num:03d}-{triad_data['slug']}.html"
    maw_triad = f'''
    <!-- M.A.W. Set Synergy Triad -->
    <div class="maw-triad-box">
      <div class="maw-triad-header">M.A.W. TRIAD SET SYNERGY &amp; SOURCE ENTITY</div>
      <div class="maw-triad-grid">
        <a href="../entities/{entity_file_name}" class="triad-card" style="border-color:#f1df76;">
          <img src="../assets/art/entities/se-{num:03d}.svg" alt="Entity">
          <div class="triad-meta"><span class="triad-type">SOURCE ENTITY ({triad_data['tier']})</span><span class="triad-name">{triad_data['name']}</span></div>
        </a>
        <a href="{triad_data['wpn'][0]}" class="triad-card">
          <img src="{triad_data['wpn'][2]}" alt="Weapon">
          <div class="triad-meta"><span class="triad-type">SET WEAPON</span><span class="triad-name">{triad_data['wpn'][1]}</span></div>
        </a>
        <a href="{triad_data['suit'][0]}" class="triad-card">
          <img src="{triad_data['suit'][2]}" alt="Suit">
          <div class="triad-meta"><span class="triad-type">SET SUIT</span><span class="triad-name">{triad_data['suit'][1]}</span></div>
        </a>
      </div>
    </div>
    '''
    
    if 'M.A.W. TRIAD SET SYNERGY' not in content:
        if '<section class="cross-reference-section">' in content:
            content = content.replace('<section class="cross-reference-section">', f'{maw_triad}\n<section class="cross-reference-section">', 1)
        elif '<footer class="wiki-footer">' in content:
            content = content.replace('<footer class="wiki-footer">', f'{maw_triad}\n<footer class="wiki-footer">', 1)
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Enriched all M.A.W. Equipment articles with Set Synergy Triad boxes.")
