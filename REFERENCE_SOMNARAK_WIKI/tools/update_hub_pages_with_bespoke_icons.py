#!/usr/bin/env python3
"""
tools/update_hub_pages_with_bespoke_icons.py
Updates all Hub landing pages to use 100% bespoke, individual, non-repeated icons
for every single card, eliminating all mismatched styles and generic duplicates.
"""

import os, re

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

def update_characters_hub():
    path = os.path.join(WIKI_DIR, "characters/index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace repeated icons on secondary characters
    char_replacements = [
        ("doha.html", "avatar_char_doha.svg"),
        ("joon.html", "avatar_char_joon.svg"),
        ("yeonhwa.html", "avatar_char_yeonhwa.svg"),
        ("taeho.html", "avatar_char_taeho.svg"),
        ("kael.html", "avatar_char_kael.svg"),
        ("minho.html", "avatar_char_minho.svg"),
        ("sora.html", "avatar_char_sora.svg"),
        ("soojin.html", "avatar_char_soojin.svg"),
        ("cheonbulok-refugees.html", "avatar_char_cheonbulok_refugees.svg"),
        ("high-architects.html", "avatar_char_high_architects.svg")
    ]

    for page, icon in char_replacements:
        # Pattern to replace img src in the card containing page link
        pattern = r'(<div class="pm-entity-card"[^>]*>.*?<img src=")[^"]+(" alt="[^"]*" class="entity-card-icon">.*?<a href="' + re.escape(page) + r'")'
        replacement = r'\g<1>../assets/avatars/' + icon + r'\2'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated characters/index.html with bespoke avatars!")

def update_locations_hub():
    path = os.path.join(WIKI_DIR, "locations/index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    loc_replacements = [
        ("the-maw.html", "icon_loc_the_maw.svg"),
        ("the-desolate.html", "icon_loc_the_desolate.svg"),
        ("the-hollow-glass.html", "icon_loc_the_hollow_glass.svg"),
        ("the-library-of-stolen-pasts.html", "icon_loc_the_library_of_stolen_pasts.svg"),
        ("the-orphan-bell-tower.html", "icon_loc_the_orphan_bell_tower.svg"),
        ("unknown-cities-and-unclaimed-frontier.html", "icon_loc_unknown_cities.svg")
    ]

    for page, icon in loc_replacements:
        pattern = r'(<div class="pm-entity-card"[^>]*>.*?<img src=")[^"]+(" alt="[^"]*" class="entity-card-icon">.*?<a href="' + re.escape(page) + r'")'
        replacement = r'\g<1>../assets/icons/' + icon + r'\2'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated locations/index.html with bespoke location icons!")

def update_lore_hub():
    path = os.path.join(WIKI_DIR, "lore/index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    lore_replacements = [
        ("the-three-ages-and-history.html", "icon_lore_three_ages.svg"),
        ("the-cycle-and-absolvohan.html", "icon_lore_absolvohan.svg"),
        ("the-doorspeech.html", "icon_lore_doorspeech.svg"),
        ("the-dawn-of-hope.html", "icon_lore_dawn_of_hope.svg"),
        ("taboo-resonance-and-penalties.html", "icon_lore_taboo_resonance.svg"),
        ("cheongula-the-living-city.html", "icon_lore_cheongula.svg"),
        ("night-hazards-and-vigil.html", "icon_lore_night_hazards.svg"),
        ("named-fractures.html", "icon_lore_named_fractures.svg"),
        ("the-dream-realm.html", "icon_lore_dream_realm.svg"),
        ("the-weeping-effluent-and-conduits.html", "icon_lore_weeping_effluent.svg"),
        ("daily-life-in-somnarak.html", "icon_lore_daily_life.svg"),
        ("somnarak-name-registry.html", "icon_lore_name_registry.svg")
    ]

    for page, icon in lore_replacements:
        pattern = r'(<div class="pm-entity-card"[^>]*>.*?<img src=")[^"]+(" alt="[^"]*" class="entity-card-icon">.*?<a href="' + re.escape(page) + r'")'
        replacement = r'\g<1>../assets/icons/' + icon + r'\2'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated lore/index.html with bespoke lore icons!")

def update_mechanics_hub():
    path = os.path.join(WIKI_DIR, "mechanics/index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    mech_replacements = [
        ("the-four-work-types.html", "icon_mech_four_work_types.svg"),
        ("han-energy-and-damage.html", "icon_mech_han_energy_damage.svg"),
        ("resonant-clash-mechanics.html", "icon_mech_resonant_clash.svg"),
        ("fracture-and-therapy.html", "icon_mech_fracture_therapy.svg"),
        ("containment-and-suppression.html", "icon_mech_containment_suppression.svg"),
        ("secc-classification-system.html", "icon_mech_secc_classification.svg"),
        ("ordeals-framework.html", "icon_mech_ordeals_framework.svg"),
        ("maw-equipment-system.html", "icon_mech_maw_equipment_system.svg"),
        ("agent-attributes-and-stats.html", "icon_mech_agent_stats.svg"),
        ("enemy-bestiary.html", "icon_mech_enemy_bestiary.svg"),
        ("han-relic-registry.html", "icon_mech_han_relic_registry.svg"),
        ("default-standard-equipment.html", "icon_mech_standard_equipment.svg"),
        ("taboo-resonance-mechanics.html", "icon_mech_taboo_resonance_mech.svg")
    ]

    for page, icon in mech_replacements:
        pattern = r'(<div class="pm-entity-card"[^>]*>.*?<img src=")[^"]+(" alt="[^"]*" class="entity-card-icon">.*?<a href="' + re.escape(page) + r'")'
        replacement = r'\g<1>../assets/icons/' + icon + r'\2'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated mechanics/index.html with bespoke tactical icons!")

def update_departments_and_factions_hub():
    # Departments
    dept_path = os.path.join(WIKI_DIR, "departments/index.html")
    with open(dept_path, "r", encoding="utf-8") as f:
        c = f.read()
    c = c.replace(
        '<img src="../assets/layout/hand/icons/the_hand_of_change_simple.svg" alt="Facility Schematics"',
        '<img src="../assets/layout/hand/icons/icon_dept_room_types.svg" alt="Facility Schematics"'
    )
    c = c.replace(
        '<img src="../assets/icons/man_hazard.svg" alt="Incident Reports"',
        '<img src="../assets/layout/hand/icons/icon_dept_incident_archive.svg" alt="Incident Reports"'
    )
    with open(dept_path, "w", encoding="utf-8") as f:
        f.write(c)

    # Factions
    fac_path = os.path.join(WIKI_DIR, "factions/index.html")
    with open(fac_path, "r", encoding="utf-8") as f:
        fc = f.read()
    fc = fc.replace(
        '<img src="../assets/icons/ref_faction_tech.svg" alt="Faction Technology"',
        '<img src="../assets/icons/icon_faction_technology.svg" alt="Faction Technology"'
    )
    with open(fac_path, "w", encoding="utf-8") as f:
        f.write(fc)

    print("Updated departments/index.html and factions/index.html!")

if __name__ == "__main__":
    update_characters_hub()
    update_locations_hub()
    update_lore_hub()
    update_mechanics_hub()
    update_departments_and_factions_hub()
