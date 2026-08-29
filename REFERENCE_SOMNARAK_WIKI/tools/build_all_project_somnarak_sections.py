import os, sys, re, html
sys.path.insert(0, '/home/user')
from tools.build_deep_canon_wiki import get_base_template
from tools.convert_echo_cores import parse_markdown_to_wiki_sections, format_lines_to_html

SOURCE_DIR = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/World_Reference"
WIKI_DIR = "/home/user/01_Somnarak_Wiki"

with open(os.path.join(SOURCE_DIR, "PROJECT_SOMNARAK.md"), 'r', encoding='utf-8') as f:
    ps_raw = f.read()

quote_ps, auth_ps, ps_sections = parse_markdown_to_wiki_sections(ps_raw)

targets = [
    # Lore
    ("lore/somnarak-cosmology.html", "Somnarak Cosmology & The Five Layers", "Lore & World", "lore/index.html", ["cosmology", "five layers", "veil", "raw", "weeping", "alpha tree"]),
    ("lore/the-alpha-tree.html", "The Alpha Tree (알파 나무 — Alpha Namu)", "Lore & World", "lore/index.html", ["alpha tree", "sap", "canopy", "roots", "chlorophyll"]),
    ("lore/the-three-sorrows.html", "The Three Sorrows (Sorrow, Grieving, Lament)", "Lore & World", "lore/index.html", ["three sorrows", "lament", "grief", "han", "manifestation"]),
    ("lore/the-three-ages-and-history.html", "The Three Ages & Historic Wars of Somnarak", "Lore & World", "lore/index.html", ["three ages", "history", "foundation", "siphoning", "cycle"]),
    ("lore/the-seven-absolute-taboos.html", "The Seven Absolute Taboos of Somnarak", "Lore & World", "lore/index.html", ["taboo", "seven absolute", "giltong", "enforcement", "calcification"]),
    ("lore/efflorescence-and-fracture.html", "Efflorescence (Gaehwa) & Mental Fracture", "Lore & World", "lore/index.html", ["efflorescence", "gaehwa", "fracture", "psychological", "calcification"]),
    ("lore/night-hazards-and-vigil.html", "Night Hazards & Evening Vigil Protocols", "Lore & World", "lore/index.html", ["night hazards", "evening", "vigil", "curfew", "mist"]),
    
    # Locations
    ("locations/district-structure-veil-and-raw.html", "District Structure: The Veil and The Raw", "Locations & Atlas", "locations/index.html", ["district", "veil", "raw", "architecture", "spire"]),
    ("locations/the-maw.html", "The Maw (M.A.W. Siphoning Core)", "Locations & Atlas", "locations/index.html", ["the maw", "siphoning core", "extraction", "furnace", "maw"]),
    ("locations/the-hollow-glass.html", "The Hollow Glass (District 4 Memorial)", "Locations & Atlas", "locations/index.html", ["hollow glass", "memorial", "glass", "district 4"]),
    ("locations/the-library-of-stolen-pasts.html", "The Library of Stolen Pasts", "Locations & Atlas", "locations/index.html", ["library", "stolen pasts", "archive", "subterranean"]),
    ("locations/the-orphan-bell-tower.html", "The Orphan Bell Tower (Sector 7)", "Locations & Atlas", "locations/index.html", ["orphan bell", "bell tower", "acoustic", "sector 7"]),
    ("locations/zone-a-core-nexus.html", "Zone A: Core Nexus & High Spire", "Locations & Atlas", "locations/index.html", ["zone a", "core nexus", "high spire", "central"]),
    ("locations/zone-b-west-ward.html", "Zone B: West Ward & Residential Rings", "Locations & Atlas", "locations/index.html", ["zone b", "west ward", "residential", "living"]),
    ("locations/zone-c-collectors-row.html", "Zone C: Collector's Row & Scrap Markets", "Locations & Atlas", "locations/index.html", ["zone c", "collectors", "row", "market", "salvage"]),
    ("locations/zone-d-forge-and-gardens.html", "Zone D: Insight Forge & Hydro Gardens", "Locations & Atlas", "locations/index.html", ["zone d", "forge", "hydro", "gardens", "industrial"]),
    ("locations/zone-e-perimeter-bulwark.html", "Zone E: Perimeter Bulwark & Outer Gate", "Locations & Atlas", "locations/index.html", ["zone e", "perimeter", "bulwark", "outer gate", "wall"]),

    # Factions
    ("factions/the-high-council.html", "The High Council (Council of Sighs)", "Factions & Guilds", "factions/index.html", ["high council", "council of sighs", "governance", "five heads"]),
    ("factions/the-architects.html", "The Architects (Geonchukga Guild)", "Factions & Guilds", "factions/index.html", ["architect", "geonchukga", "building", "spire", "masonry"]),
    ("factions/the-weavers.html", "The Weavers (Jikjo-gwan Guild)", "Factions & Guilds", "factions/index.html", ["weaver", "jikjo", "silk", "memory fabric", "thread"]),
    ("factions/the-wardens.html", "The Wardens (Gyeongbi Guild)", "Factions & Guilds", "factions/index.html", ["warden", "gyeongbi", "guard", "security", "bulwark"]),
    ("factions/the-collectors.html", "The Collectors (Sujipga Cartel)", "Factions & Guilds", "factions/index.html", ["collector", "sujipga", "scrap", "salvage", "relic"]),
    ("factions/the-giltong-enforcers.html", "The Giltong Enforcers (질동 — Taboo Hunters)", "Factions & Guilds", "factions/index.html", ["giltong", "enforcer", "taboo hunter", "executioner"]),
    ("factions/the-memory-washers.html", "The Memory Washers (기억 세척자 — Girok Secheokja)", "Factions & Guilds", "factions/index.html", ["memory washer", "secheokja", "amnesia", "erasure"]),

    # Mechanics
    ("mechanics/agent-attributes-and-stats.html", "Agent Attributes & Cognitive Stats", "Systems & Mechanics", "mechanics/index.html", ["agent stats", "attributes", "fortitude", "prudence", "temperance", "justice"]),
    ("mechanics/containment-and-suppression.html", "Containment Procedures & Breach Suppression", "Systems & Mechanics", "mechanics/index.html", ["containment", "suppression", "breach", "qliphoth", "sorrow gauge"]),
    ("mechanics/default-standard-equipment.html", "Default Standard Equipment & Uniforms", "Systems & Mechanics", "mechanics/index.html", ["default equipment", "standard issue", "uniform", "baton", "vest"]),
    ("mechanics/fracture-and-therapy.html", "Mental Fracture & Cognitive Therapy", "Systems & Mechanics", "mechanics/index.html", ["fracture", "therapy", "calcification", "psychological", "panic"]),
    ("mechanics/han-energy-and-damage.html", "Han Energy Physics & Four Damage Types", "Systems & Mechanics", "mechanics/index.html", ["han energy", "damage types", "red", "white", "black", "pale"]),
    ("mechanics/han-relics-and-tools.html", "Han Relics & Utility Extraction Tools", "Systems & Mechanics", "mechanics/index.html", ["han relics", "tools", "utility", "compass", "lantern"]),
    ("mechanics/maw-equipment-system.html", "M.A.W. Equipment Architecture & Synthesis", "Systems & Mechanics", "mechanics/index.html", ["maw equipment", "weapon", "suit", "gift", "corrosion"]),
    ("mechanics/secc-classification-system.html", "SECC Classification System (ZAYIN to ALEPH)", "Systems & Mechanics", "mechanics/index.html", ["secc", "classification", "zayin", "teth", "he", "waw", "aleph"]),
    ("mechanics/the-four-work-types.html", "The Four Work Types (Insight, Attachment, Repression, Extraction)", "Systems & Mechanics", "mechanics/index.html", ["work types", "insight", "attachment", "repression", "extraction"]),
]

for dst_rel, title, cat_label, cat_href, keywords in targets:
    matched_sections = []
    for st, slines in ps_sections:
        full_sec_text = (st + " " + "\n".join(slines)).lower()
        if any(kw in full_sec_text for kw in keywords):
            matched_sections.append((st, slines))
            
    if not matched_sections:
        matched_sections = ps_sections[:2]
        
    toc = [(re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec', t) for t, _ in matched_sections]
    body_parts = []
    
    body_parts.append(f'''
    <div class="wiki-callout">
      <p><strong>CANONICAL RECORD:</strong> Sourced directly from the official <em>Project Somnarak Worldbuilding Codex</em>.</p>
    </div>
    ''')
    
    for t, lines in matched_sections:
        sid = re.sub(r'[^a-zA-Z0-9]+', '-', t.lower()).strip('-') or 'sec'
        body_parts.append(f'<section class="wiki-section" id="{sid}"><h2 class="section-title">{t}</h2>{format_lines_to_html(lines)}</section>')
        
    html_page = get_base_template(
        title=title,
        category_label=cat_label,
        category_href=cat_href,
        rel_prefix="../",
        content_html='\n'.join(body_parts),
        toc_items=toc
    )
    
    dst_path = os.path.join(WIKI_DIR, dst_rel)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(html_page)
    print(f"Built deep lore/mechanics page: {dst_rel} ({len(html_page)} chars, {len(matched_sections)} sections)")

print("All PROJECT_SOMNARAK sections fully compiled.")
