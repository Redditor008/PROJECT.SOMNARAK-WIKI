import os, sys
sys.path.insert(0, '/home/user')
from tools.build_deep_canon_wiki import get_base_template

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# 1. Characters Index
char_cards = [
    ("the-director-majin.html", "Echo-Core 1: Director Majin", "Supreme Directorate Authority & Hand Commander", "assets/icons/somnarak_icon.svg"),
    ("the-secretary-seiyon.html", "Echo-Core 2: Seiyon", "Central Archives & Preserved Memory Index", "assets/icons/floor-2-maw.svg"),
    ("the-containment-lead-dekan.html", "Echo-Core 3: Dekan", "Sorrow Containment & High-Density Ward", "assets/icons/shield_hope.svg"),
    ("the-extraction-lead-zyrak.html", "Echo-Core 4: Zyrak", "M.A.W. Siphoning & Forge Master", "assets/icons/weapon.svg"),
    ("the-research-lead-ayshuk.html", "Echo-Core 5: Ayshuk", "Han Kinetics & Anomaly Analysis", "assets/icons/clarity.svg"),
    ("the-border-lead-mellda.html", "Echo-Core 6: Mellda", "Outer Bulwark & Acoustic Bastion", "assets/icons/veil.svg"),
    ("the-archive-lead-marjuk.html", "Echo-Core 7: Marjuk", "Deep Vault & Cryogenic Record Keeper", "assets/icons/floor-6-vault.svg"),
    ("the-outsider-ishall.html", "Echo-Core 8: Ishall", "Desolate Reconnaissance & Void Diver", "assets/icons/floor-7-shadow.svg"),
    ("the-exile-xyan.html", "Echo-Core 9: Xyan", "The Forbidden Gate & Taboo Resonance", "assets/icons/floor-8-gate.svg"),
    ("kael.html", "Kael (The Wanderer)", "Resonant Pilgrim & Outskirts Survivor", "assets/icons/nav_characters.svg"),
    ("soojin.html", "Soojin (Archivist's Apprentice)", "Fray Weaver & Memory Transcriber", "assets/icons/nav_characters.svg"),
    ("yeonhwa.html", "Lead Yeonhwa (Cartographer)", "SED Field Expedition Commander", "assets/icons/ref_sed.svg"),
    ("taeho.html", "Commander Taeho (Strike Lead)", "UCD Tactical Suppression Commander", "assets/icons/ref_ucd.svg"),
    ("high-architects.html", "The High Architects", "Precursor Masonry & Spire Engineers", "assets/icons/fac_architects.svg"),
    ("cheonbulok-refugees.html", "Cheonbulok Refugee Collective", "Displaced Subterranean Citizens", "assets/icons/outside.svg")
]

char_html = '''
<div class="wiki-callout">
  <p><strong>PERSONNEL ARCHIVE:</strong> Complete registry of Echo-Cores, tactical commanders, guild leaders, and notable figures across Somnarak.</p>
</div>
<div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 14px; margin-top: 1.5rem;">
'''
for href, title, desc, icon in char_cards:
    char_html += f'''
    <a href="{href}" class="archive-portal" style="border: 1px solid #334155; padding: 16px; text-decoration: none; display: flex; flex-direction: column; align-items: center; text-align: center; background: #070a10; border-radius: 4px;">
      <img src="../{icon}" style="width: 48px; height: 48px; margin-bottom: 8px;" alt="">
      <b style="color: #f1df76; font-size: 1rem; margin-bottom: 4px;">{title}</b>
      <small style="color: #94a3b8; font-size: 0.78rem;">{desc}</small>
    </a>
    '''
char_html += '</div>'

html_char_page = get_base_template("Characters Directory", "Characters", "characters/index.html", "../", char_html)
with open(os.path.join(WIKI_DIR, "characters/index.html"), 'w', encoding='utf-8') as f:
    f.write(html_char_page)

# 2. Lore Index
lore_cards = [
    ("somnarak-cosmology.html", "Somnarak Cosmology", "The Five Layers of Reality, The Veil, and The Raw", "assets/icons/nav_lore.svg"),
    ("the-cycle-and-absolvohan.html", "The Cycle & Absolvohan", "The 1,778 resets and Day 0 to 365 chronicle", "assets/icons/ref_absolvohan.svg"),
    ("the-alpha-tree.html", "The Alpha Tree", "Living Singularity, canopy ecology, and Sap extraction", "assets/icons/art_dawn.svg"),
    ("the-three-sorrows.html", "The Three Sorrows", "Sorrow, Grieving, Lament and their physical forms", "assets/icons/lament.svg"),
    ("the-three-ages-and-history.html", "The Three Ages & Wars", "Foundation, Siphoning Wars, and the Directorate Era", "assets/icons/banner_timeline.svg"),
    ("the-seven-absolute-taboos.html", "The Seven Absolute Taboos", "Civic laws, Giltong enforcement, and calcification", "assets/icons/taboo.svg"),
    ("the-cheongula-incident.html", "The Cheongula Incident", "Year 3,892 disaster, reactor breach, and quarantine", "assets/icons/ref_cheongula.svg"),
    ("the-dawn-of-hope.html", "The Dawn of Hope", "Year 4,238 post-cycle reconstruction and Outskirts", "assets/icons/banner_hope.svg"),
    ("daily-life-in-somnarak.html", "Daily Life in Somnarak", "Echo-Token economy, Spire life, and Evening Return", "assets/icons/ref_daily_life.svg"),
    ("the-doorspeech.html", "The Doorspeech (Mun-eon)", "Acoustic grammar, voice mantles, and encryption", "assets/icons/clarity.svg"),
    ("the-weeping-river.html", "The Weeping River", "Abyssal hydrology and sorrow crystallization", "assets/icons/ref_the_weeping.svg"),
    ("the-dream-realm.html", "The Dream Realm (Yumonggye)", "Subconscious ocean and dream diving protocols", "assets/icons/ref_dream_realm.svg"),
    ("somnarak-name-registry.html", "Name Registry & Cryo-Vault", "1.4M preserved identities and memory recovery", "assets/icons/ref_name_registry.svg"),
    ("named-fractures.html", "The Eight Named Fractures", "Legendary entities born from catastrophic sorrow", "assets/icons/ref_named_fractures.svg"),
    ("efflorescence-and-fracture.html", "Efflorescence & Fracture", "Psychological resonance, Gaehwa, and mental strain", "assets/icons/fracture.svg"),
    ("night-hazards-and-vigil.html", "Night Hazards & Evening Vigil", "Curfew protocols and nocturnal entity activity", "assets/icons/man_hazard.svg")
]

lore_html = '''
<div class="wiki-callout">
  <p><strong>COSMOLOGICAL &amp; HISTORICAL ARCHIVE:</strong> Comprehensive collection of records on the universe, the Alpha Tree, historical eras, taboos, and metaphysical principles of Somnarak.</p>
</div>
<div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 14px; margin-top: 1.5rem;">
'''
for href, title, desc, icon in lore_cards:
    lore_html += f'''
    <a href="{href}" class="archive-portal" style="border: 1px solid #334155; padding: 16px; text-decoration: none; display: flex; flex-direction: column; align-items: center; text-align: center; background: #070a10; border-radius: 4px;">
      <img src="../{icon}" style="width: 48px; height: 48px; margin-bottom: 8px;" alt="">
      <b style="color: #f1df76; font-size: 1rem; margin-bottom: 4px;">{title}</b>
      <small style="color: #94a3b8; font-size: 0.78rem;">{desc}</small>
    </a>
    '''
lore_html += '</div>'

html_lore_page = get_base_template("Lore & Cosmology Directory", "Lore & World", "lore/index.html", "../", lore_html)
with open(os.path.join(WIKI_DIR, "lore/index.html"), 'w', encoding='utf-8') as f:
    f.write(html_lore_page)

# 3. Locations Index
loc_cards = [
    ("zone-a-core-nexus.html", "Zone A: Core Nexus", "High Spire, Council Chamber, and Alpha Siphon Pylons", "assets/layout/city/icons/icon_zone_a_core.svg"),
    ("zone-b-west-ward.html", "Zone B: West Ward", "Residential rings, civilian districts, and Bell Tower", "assets/layout/city/icons/icon_zone_b_west.svg"),
    ("zone-c-collectors-row.html", "Zone C: Collector's Row", "Scrap markets, salvage yards, and pawn conduits", "assets/layout/city/icons/icon_zone_c_east.svg"),
    ("zone-d-forge-and-gardens.html", "Zone D: Insight Forge & Gardens", "Industrial workshops, hydroponic chambers, and labs", "assets/layout/city/icons/icon_zone_d_flanks.svg"),
    ("zone-e-perimeter-bulwark.html", "Zone E: Perimeter Bulwark", "The Outer Wall, acoustic barriers, and defense gates", "assets/layout/city/icons/icon_zone_e_bulwark.svg"),
    ("district-structure-veil-and-raw.html", "District Structure: Veil & Raw", "Urban architectural zoning and atmospheric filters", "assets/icons/veil.svg"),
    ("the-maw.html", "The Maw (Siphoning Core)", "The industrial extraction furnace beneath the facility", "assets/icons/art_maw.svg"),
    ("the-desolate.html", "The Desolate (Hwangmuji)", "The toxic wasteland barrens surrounding the city", "assets/icons/outside.svg"),
    ("unknown-cities.html", "Unknown Cities & Ruins", "Cheonbulok Citadel, Port Haerim, and Spire Namsan", "assets/icons/ref_unknown_cities.svg"),
    ("the-hollow-glass.html", "The Hollow Glass", "District 4 Memorial for the lost souls", "assets/icons/place.svg"),
    ("the-library-of-stolen-pasts.html", "Library of Stolen Pasts", "Subterranean knowledge vault of precursor texts", "assets/icons/ref_project_somnarak.svg"),
    ("the-orphan-bell-tower.html", "Orphan Bell Tower", "Sector 7 acoustic resonance landmark", "assets/icons/art_bell.svg")
]

loc_html = '''
<div class="wiki-callout">
  <p><strong>CARTOGRAPHIC ATLAS:</strong> City zones, landmark structures, subterranean vaults, and uncharted wasteland ruins.</p>
</div>
<div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 14px; margin-top: 1.5rem;">
'''
for href, title, desc, icon in loc_cards:
    loc_html += f'''
    <a href="{href}" class="archive-portal" style="border: 1px solid #334155; padding: 16px; text-decoration: none; display: flex; flex-direction: column; align-items: center; text-align: center; background: #070a10; border-radius: 4px;">
      <img src="../{icon}" style="width: 48px; height: 48px; margin-bottom: 8px;" alt="">
      <b style="color: #f1df76; font-size: 1rem; margin-bottom: 4px;">{title}</b>
      <small style="color: #94a3b8; font-size: 0.78rem;">{desc}</small>
    </a>
    '''
loc_html += '</div>'

html_loc_page = get_base_template("Atlas & Locations Directory", "Locations & Atlas", "locations/index.html", "../", loc_html)
with open(os.path.join(WIKI_DIR, "locations/index.html"), 'w', encoding='utf-8') as f:
    f.write(html_loc_page)

# 4. Factions Index
fac_cards = [
    ("the-reverie-directorate.html", "The Reverie Directorate", "The governing containment authority of the Hand of Change", "assets/icons/fac_rd.svg"),
    ("the-high-council.html", "The High Council", "The Council of Sighs and civic rulers of Somnarak", "assets/icons/fac_council.svg"),
    ("the-sed-corps.html", "Sorrow Exploration Division (SED)", "Deep-range survey corps and cartographers of The Desolate", "assets/icons/ref_sed.svg"),
    ("the-ucd-strike-force.html", "Underworld Containment Division (UCD)", "Subterranean strike force combating black-market entity rings", "assets/icons/ref_ucd.svg"),
    ("the-architects.html", "The Architects Guild", "Master builders, Spire masons, and structural engineers", "assets/icons/fac_architects.svg"),
    ("the-weavers.html", "The Weavers Guild", "Harvesters of sorrow silk and memory fabric tailors", "assets/icons/fac_weavers.svg"),
    ("the-wardens.html", "The Wardens Guild", "City perimeter defense, gatekeepers, and wall guards", "assets/icons/fac_wardens.svg"),
    ("the-collectors.html", "The Collectors Cartel", "Scrap prospectors, relic dealers, and salvage brokers", "assets/icons/fac_collectors.svg"),
    ("the-horizon-caravan.html", "The Horizon Caravan", "Nomadic land-crawler fleet crossing the toxic barrens", "assets/icons/ref_horizon_caravan.svg"),
    ("the-underworld-and-wound-walkers.html", "The Underworld & Wound Walkers", "Subterranean survivors adhering to the Philosophy of Scars", "assets/icons/ref_wound_walkers.svg"),
    ("the-founding-corporations.html", "Founding Corporations", "Precursor industrial syndicates that created the city", "assets/icons/ref_corporations.svg"),
    ("the-giltong-enforcers.html", "The Giltong Enforcers", "Ruthless hunters enforcing the Seven Absolute Taboos", "assets/icons/taboo.svg"),
    ("the-memory-washers.html", "The Memory Washers", "Black market operators erasing civilian traumatic memories", "assets/icons/ref_memory_archive.svg"),
    ("faction-technology.html", "Faction Technology Matrix", "Comparative engineering matrix across all guilds", "assets/icons/ref_faction_tech.svg")
]

fac_html = '''
<div class="wiki-callout">
  <p><strong>FACTIONS &amp; GUILDS REGISTRY:</strong> Comprehensive dossiers on all governmental authorities, specialized divisions, commercial cartels, and subterranean factions.</p>
</div>
<div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 14px; margin-top: 1.5rem;">
'''
for href, title, desc, icon in fac_cards:
    fac_html += f'''
    <a href="{href}" class="archive-portal" style="border: 1px solid #334155; padding: 16px; text-decoration: none; display: flex; flex-direction: column; align-items: center; text-align: center; background: #070a10; border-radius: 4px;">
      <img src="../{icon}" style="width: 48px; height: 48px; margin-bottom: 8px;" alt="">
      <b style="color: #f1df76; font-size: 1rem; margin-bottom: 4px;">{title}</b>
      <small style="color: #94a3b8; font-size: 0.78rem;">{desc}</small>
    </a>
    '''
fac_html += '</div>'

html_fac_page = get_base_template("Factions & Guilds Directory", "Factions & Guilds", "factions/index.html", "../", fac_html)
with open(os.path.join(WIKI_DIR, "factions/index.html"), 'w', encoding='utf-8') as f:
    f.write(html_fac_page)

# 5. Mechanics Index
mech_cards = [
    ("secc-classification-system.html", "SECC Classification System", "ZAYIN, TETH, HE, WAW, and ALEPH risk ratings", "assets/icons/risk_aleph.svg"),
    ("the-four-work-types.html", "The Four Work Types", "Insight, Attachment, Repression, and Extraction protocols", "assets/icons/ref_project_somnarak.svg"),
    ("containment-and-suppression.html", "Containment & Suppression", "Qliphoth counters, sorrow gauge, and breach suppression", "assets/icons/sorrow_gauge.svg"),
    ("han-energy-and-damage.html", "Han Energy & Damage Types", "RED, WHITE, BLACK, and PALE damage calculations", "assets/icons/element.svg"),
    ("maw-equipment-system.html", "M.A.W. Equipment System", "Weapon, Suit, and Gift extraction and resonance sync", "assets/icons/maw.svg"),
    ("resonant-clash-mechanics.html", "Resonant Clash Combat", "Speed dice, Clash Power, and Stagger Break formulas", "assets/icons/ref_battle_system.svg"),
    ("ordeals-framework.html", "Ordeals Framework", "Dawn, Noon, Dusk, and Midnight incursion waves", "assets/icons/ref_ordeals_framework.svg"),
    ("enemy-bestiary.html", "Enemy Bestiary", "Catalog of feral sorrow entities and rogue combatants", "assets/icons/ref_enemy_list.svg"),
    ("agent-attributes-and-stats.html", "Agent Stats & Attributes", "Fortitude, Prudence, Temperance, and Justice progression", "assets/icons/resolve.svg"),
    ("fracture-and-therapy.html", "Fracture & Cognitive Therapy", "Panic behaviors, trauma reversal, and mental stability", "assets/icons/fracture.svg"),
    ("taboo-resonance-mechanics.html", "Taboo Resonance Mechanics", "Soul calcification stages and abyssal cascade risks", "assets/icons/ref_taboo_resonance.svg"),
    ("han-relic-registry.html", "Han Relic Registry", "Grade I through V Relics, properties, and multipliers", "assets/icons/ref_han_relics.svg"),
    ("han-relics-and-tools.html", "Han Tools & Instruments", "Standard issue extraction gauges and field gear", "assets/icons/tool.svg"),
    ("default-standard-equipment.html", "Default Standard Equipment", "Uniforms, shock batons, and baseline agent gear", "assets/icons/suit.svg")
]

mech_html = '''
<div class="wiki-callout">
  <p><strong>SYSTEMS &amp; MECHANICS MANUAL:</strong> Comprehensive technical documentation on combat calculations, risk classifications, work types, M.A.W. synthesis, and Ordeal incursions.</p>
</div>
<div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 14px; margin-top: 1.5rem;">
'''
for href, title, desc, icon in mech_cards:
    mech_html += f'''
    <a href="{href}" class="archive-portal" style="border: 1px solid #334155; padding: 16px; text-decoration: none; display: flex; flex-direction: column; align-items: center; text-align: center; background: #070a10; border-radius: 4px;">
      <img src="../{icon}" style="width: 48px; height: 48px; margin-bottom: 8px;" alt="">
      <b style="color: #f1df76; font-size: 1rem; margin-bottom: 4px;">{title}</b>
      <small style="color: #94a3b8; font-size: 0.78rem;">{desc}</small>
    </a>
    '''
mech_html += '</div>'

html_mech_page = get_base_template("Systems & Mechanics Directory", "Systems & Mechanics", "mechanics/index.html", "../", mech_html)
with open(os.path.join(WIKI_DIR, "mechanics/index.html"), 'w', encoding='utf-8') as f:
    f.write(html_mech_page)

print("All 5 hub index pages refreshed cleanly.")
