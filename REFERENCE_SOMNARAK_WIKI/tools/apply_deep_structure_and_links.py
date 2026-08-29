import os, re
from bs4 import BeautifulSoup

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# Define category fast jump datasets
FAST_JUMP_DATA = {
    "characters": [
        ("the-director-majin.html", "1. Majin"),
        ("the-secretary-seiyon.html", "2. Seiyon"),
        ("the-containment-lead-dekan.html", "3. Dekan"),
        ("the-extraction-lead-zyrak.html", "4. Zyrak"),
        ("the-research-lead-ayshuk.html", "5. Ayshuk"),
        ("the-border-lead-mellda.html", "6. Mellda"),
        ("the-archive-lead-marjuk.html", "7. Marjuk"),
        ("the-outsider-ishall.html", "8. Ishall"),
        ("the-exile-xyan.html", "9. Xyan"),
        ("minho.html", "Minho"),
        ("taeho.html", "Taeho"),
        ("soojin.html", "Soojin"),
        ("doha.html", "Doha"),
        ("index.html", "✦ Full Roster")
    ],
    "entities": [
        ("se-001-the-orphaned-bell.html", "SE-001"),
        ("se-002-the-grieving-colossus.html", "SE-002"),
        ("se-003-the-wilderness-tide.html", "SE-003"),
        ("se-005-the-smothering-mother.html", "SE-005"),
        ("se-007-brume.html", "SE-007"),
        ("se-009-the-memory-weaver.html", "SE-009"),
        ("se-010-the-convergence.html", "SE-010"),
        ("se-011-the-whispering-walls.html", "SE-011"),
        ("se-014-the-debt-eater.html", "SE-014"),
        ("se-015-the-debt-scale.html", "SE-015"),
        ("index.html", "✦ Full Codex")
    ],
    "maw": [
        ("maw-w-001-01-the-laments-requiem.html", "WPN-01"),
        ("maw-w-002-01-the-mourning-maul.html", "WPN-02"),
        ("maw-w-005-01-the-embrace-fang.html", "WPN-05"),
        ("maw-w-007-01-the-hope-lens.html", "WPN-07"),
        ("maw-w-009-01-the-forgotten-lens.html", "WPN-09"),
        ("maw-w-010-01-the-absolute-maul.html", "WPN-10"),
        ("maw-s-001-01-the-laments-shroud.html", "SUIT-01"),
        ("maw-s-002-01-the-mourning-mantle.html", "SUIT-02"),
        ("maw-s-005-01-the-embrace-plate.html", "SUIT-05"),
        ("maw-s-010-01-the-absolute-mantle.html", "SUIT-10"),
        ("maw-g-001-01-laments-edge.html", "GIFT-01"),
        ("maw-g-010-01-the-absolute-verdict.html", "GIFT-10"),
        ("index.html", "✦ Arsenal Hub")
    ],
    "departments": [
        ("floor-1-neutral-command.html", "F1: Neutral"),
        ("floor-2-maws-keep.html", "F2: Maw's Keep"),
        ("floor-3-extraction-hall.html", "F3: Extraction"),
        ("floor-4-insight-forge.html", "F4: Insight"),
        ("floor-5-border-watch.html", "F5: Border"),
        ("floor-6-deep-vault.html", "F6: Vault"),
        ("floor-7-shadow-corps.html", "F7: Shadow"),
        ("floor-8-gate-watch.html", "F8: Gate"),
        ("facility-room-types.html", "Room Types"),
        ("incident-reports-archive.html", "Incidents"),
        ("index.html", "✦ Dept Hub")
    ],
    "locations": [
        ("zone-a-core-nexus.html", "Zone A: Core"),
        ("zone-b-west-ward.html", "Zone B: West"),
        ("zone-c-collectors-row.html", "Zone C: East"),
        ("zone-d-forge-and-gardens.html", "Zone D: Flanks"),
        ("zone-e-perimeter-bulwark.html", "Zone E: Bulwark"),
        ("the-desolate.html", "The Desolate"),
        ("the-maw.html", "The Maw"),
        ("the-library-of-stolen-pasts.html", "Archive Library"),
        ("district-structure-veil-and-raw.html", "Urban Grid"),
        ("index.html", "✦ Atlas Hub")
    ],
    "factions": [
        ("the-reverie-directorate.html", "Directorate"),
        ("the-high-council.html", "High Council"),
        ("the-sed-corps.html", "SED Corps"),
        ("the-ucd-strike-force.html", "UCD Force"),
        ("the-architects.html", "Architects"),
        ("the-weavers.html", "Weavers"),
        ("the-wardens.html", "Wardens"),
        ("the-collectors.html", "Collectors"),
        ("the-horizon-caravan.html", "Caravan"),
        ("the-memory-washers.html", "Washers"),
        ("faction-technology.html", "Faction Tech"),
        ("index.html", "✦ Factions Hub")
    ],
    "lore": [
        ("the-cycle-and-absolvohan.html", "The Cycle"),
        ("the-alpha-tree.html", "Alpha Tree"),
        ("the-three-sorrows.html", "3 Sorrows"),
        ("the-seven-absolute-taboos.html", "7 Taboos"),
        ("the-cheongula-incident.html", "Cheongula"),
        ("the-dawn-of-hope.html", "Dawn of Hope"),
        ("the-dream-realm.html", "Dream Realm"),
        ("daily-life-in-somnarak.html", "Daily Life"),
        ("efflorescence-and-fracture.html", "Efflorescence"),
        ("the-three-ages-and-history.html", "3 Ages"),
        ("index.html", "✦ Lore Hub")
    ],
    "mechanics": [
        ("han-energy-and-damage.html", "Damage Matrix"),
        ("the-four-work-types.html", "Work Types"),
        ("secc-classification-system.html", "SECC Ranks"),
        ("resonant-clash-mechanics.html", "Clash Rules"),
        ("ordeals-framework.html", "Ordeals"),
        ("agent-attributes-and-stats.html", "Agent Stats"),
        ("containment-and-suppression.html", "Containment"),
        ("maw-equipment-system.html", "MAW System"),
        ("taboo-resonance-mechanics.html", "Taboo Mechanics"),
        ("index.html", "✦ Systems Hub")
    ],
    "atlas": [
        ("hand-of-change-map.html", "Facility Cutaway Map"),
        ("somnarak-city-map.html", "Somnarak City Blueprint"),
        ("../departments/index.html", "Facility Departments"),
        ("../locations/index.html", "Metropolitan Atlas")
    ]
}

def generate_fast_jump_bar(cat_name, current_file, prefix):
    items = FAST_JUMP_DATA.get(cat_name, [])
    if not items:
        return ""
    
    pills_html = []
    for href, label in items:
        # Check if active
        is_active = (href == current_file)
        active_class = " active" if is_active else ""
        link_href = f"{prefix}{cat_name}/{href}" if cat_name != "atlas" and not href.startswith("../") else f"{prefix}{cat_name}/{href}" if cat_name == "atlas" and not href.startswith("../") else f"{prefix}{href.replace('../','')}"
        
        # If in same directory
        if cat_name != "root":
            pill_href = href
        else:
            pill_href = link_href
            
        pills_html.append(f'<a href="{pill_href}" class="jump-pill{active_class}">{label}</a>')
    
    return f'''<!-- Tactical Fast-Jump Subpage Bar -->
<div class="fast-jump-nav">
  <span class="fast-jump-title">/// RAPID JUMP:</span>
  <div class="fast-jump-pills">
    {' '.join(pills_html)}
  </div>
</div>'''

def generate_directive_hud(cat_name, file_name, prefix):
    return f'''<!-- Tactical Directive Status HUD -->
<div class="tactical-directive-box">
  <div class="directive-text">
    <span class="led-dot led-green"></span> <b>STATUS:</b> ARCHIVE VERIFIED &nbsp;|&nbsp; 
    <b>CLEARANCE:</b> LEVEL-4 OVERSIGHT &nbsp;|&nbsp; 
    <b>PROTOCOL:</b> REVERIE DIRECTORATE
  </div>
  <img src="{prefix}assets/icons/hud_resonance_wave.svg" alt="Resonance Wave" class="directive-wave">
</div>'''

def generate_bottom_cross_links(cat_name, file_name, prefix):
    # Contextual high-value cross links
    cards = []
    cards.append(f'''<a href="{prefix}departments/floor-1-neutral-command.html" class="cross-ref-card">
      <img src="{prefix}assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt="Command">
      <div class="cross-ref-meta"><span class="cross-ref-cat">FACILITY COMMAND</span><span class="cross-ref-title">NEUTRAL COMMAND</span></div>
    </a>''')
    cards.append(f'''<a href="{prefix}characters/the-director-majin.html" class="cross-ref-card">
      <img src="{prefix}assets/icons/icon_core_majin.svg" alt="Majin">
      <div class="cross-ref-meta"><span class="cross-ref-cat">EXECUTIVE LEAD</span><span class="cross-ref-title">DIRECTOR MAJIN</span></div>
    </a>''')
    cards.append(f'''<a href="{prefix}lore/the-cycle-and-absolvohan.html" class="cross-ref-card">
      <img src="{prefix}assets/icons/ref_absolvohan.svg" alt="Absolvohan">
      <div class="cross-ref-meta"><span class="cross-ref-cat">PRIMARY CANON</span><span class="cross-ref-title">1,778 CYCLES</span></div>
    </a>''')
    cards.append(f'''<a href="{prefix}atlas/hand-of-change-map.html" class="cross-ref-card">
      <img src="{prefix}assets/layout/hand/icons/the_hand_dr_icon_styled.svg" alt="Facility Map">
      <div class="cross-ref-meta"><span class="cross-ref-cat">SCHEMATIC ATLAS</span><span class="cross-ref-title">HAND OF CHANGE MAP</span></div>
    </a>''')

    return f'''<!-- Bottom Cross-Reference Directory -->
<section class="cross-reference-section">
  <div class="cross-ref-header">CANONICAL CROSS-LINKS &amp; ATLAS CONNECTIONS</div>
  <div class="cross-ref-grid">
    {' '.join(cards)}
  </div>
</section>'''

# Process all HTML files
count = 0
for root, dirs, files in os.walk(WIKI_DIR):
    for f in files:
        if not f.endswith(".html"):
            continue
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, WIKI_DIR)
        
        # Determine depth & category
        parts = rel_path.split(os.sep)
        depth = len(parts) - 1
        prefix = "../" * depth if depth > 0 else "./"
        cat_name = parts[0] if depth > 0 else "root"
        file_name = parts[-1]
        
        with open(full_path, "r", encoding="utf-8") as fp:
            content = fp.read()
            
        # Don't add to 404 or already full hubs if not needed, but add to all interior articles
        if f == "404.html":
            continue
            
        # 1. Insert Fast-Jump Bar and Directive HUD if not already present
        if '<div class="fast-jump-nav">' not in content and cat_name in FAST_JUMP_DATA:
            fast_jump = generate_fast_jump_bar(cat_name, file_name, prefix)
            directive_hud = generate_directive_hud(cat_name, file_name, prefix)
            
            # Insert right after breadcrumb trail or category-hero or top of content
            if '<header class="category-hero">' in content:
                content = content.replace('</header>', f'</header>\n{fast_jump}\n{directive_hud}', 1)
            elif '<nav class="breadcrumb-trail"' in content:
                content = re.sub(r'(</nav>)', r'\1\n' + fast_jump + '\n' + directive_hud, content, count=1)
            elif '<main' in content:
                content = re.sub(r'(<main[^>]*>)', r'\1\n' + fast_jump + '\n' + directive_hud, content, count=1)
        
        # 2. Insert Bottom Cross-Reference Directory if not already present
        if '<section class="cross-reference-section">' not in content and f != "index.html" and not f.endswith("index.html"):
            bottom_links = generate_bottom_cross_links(cat_name, file_name, prefix)
            # Insert before </main> or </footer>
            if '<footer class="wiki-footer">' in content:
                content = content.replace('<footer class="wiki-footer">', f'{bottom_links}\n<footer class="wiki-footer">', 1)
            elif '</main>' in content:
                content = content.replace('</main>', f'{bottom_links}\n</main>', 1)
                
        with open(full_path, "w", encoding="utf-8") as fp:
            fp.write(content)
        count += 1

print(f"Updated {count} HTML pages with Fast-Jump Bars, Directive HUDs, and Bottom Cross-Link Directories.")
