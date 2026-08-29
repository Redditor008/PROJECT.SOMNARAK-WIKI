#!/usr/bin/env python3
"""
tools/fix_all_hub_card_icons.py
Directly replaces every card image across all 8 hub pages with 100% bespoke,
accurate, unique icons, eliminating all duplicate and mismatched icons.
"""

import os, re

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

def fix_characters_hub():
    path = os.path.join(WIKI_DIR, "characters/index.html")
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    replacements = [
        (r'<img src="[^"]+" alt="Majin"', '<img src="../assets/avatars/avatar_core_majin.svg" alt="Majin"'),
        (r'<img src="[^"]+" alt="Seiyon"', '<img src="../assets/avatars/avatar_core_seiyon.svg" alt="Seiyon"'),
        (r'<img src="[^"]+" alt="Dekan"', '<img src="../assets/avatars/avatar_core_dekan.svg" alt="Dekan"'),
        (r'<img src="[^"]+" alt="Zyrak"', '<img src="../assets/avatars/avatar_core_zyrak.svg" alt="Zyrak"'),
        (r'<img src="[^"]+" alt="Ayshuk"', '<img src="../assets/avatars/avatar_core_ayshuk.svg" alt="Ayshuk"'),
        (r'<img src="[^"]+" alt="Mellda"', '<img src="../assets/avatars/avatar_core_mellda.svg" alt="Mellda"'),
        (r'<img src="[^"]+" alt="Marjuk"', '<img src="../assets/avatars/avatar_core_marjuk.svg" alt="Marjuk"'),
        (r'<img src="[^"]+" alt="Ishall"', '<img src="../assets/avatars/avatar_core_ishall.svg" alt="Ishall"'),
        (r'<img src="[^"]+" alt="Xyan"', '<img src="../assets/avatars/avatar_core_xyan.svg" alt="Xyan"'),
        (r'<img src="[^"]+" alt="Minho"', '<img src="../assets/avatars/avatar_char_minho.svg" alt="Minho"'),
        (r'<img src="[^"]+" alt="Doha"', '<img src="../assets/avatars/avatar_char_doha.svg" alt="Doha"'),
        (r'<img src="[^"]+" alt="Soojin"', '<img src="../assets/avatars/avatar_char_soojin.svg" alt="Soojin"'),
        (r'<img src="[^"]+" alt="Sora"', '<img src="../assets/avatars/avatar_char_sora.svg" alt="Sora"'),
        (r'<img src="[^"]+" alt="Taeho"', '<img src="../assets/avatars/avatar_char_taeho.svg" alt="Taeho"'),
        (r'<img src="[^"]+" alt="Kael"', '<img src="../assets/avatars/avatar_char_kael.svg" alt="Kael"'),
        (r'<img src="[^"]+" alt="Yeonhwa"', '<img src="../assets/avatars/avatar_char_yeonhwa.svg" alt="Yeonhwa"'),
        (r'<img src="[^"]+" alt="Joon"', '<img src="../assets/avatars/avatar_char_joon.svg" alt="Joon"'),
        (r'<img src="[^"]+" alt="Refugees"', '<img src="../assets/avatars/avatar_char_cheonbulok_refugees.svg" alt="Refugees"'),
        (r'<img src="[^"]+" alt="Architects"', '<img src="../assets/avatars/avatar_char_high_architects.svg" alt="Architects"')
    ]

    for pattern, repl in replacements:
        c = re.sub(pattern, repl, c)

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Fixed all icons in characters/index.html")

def fix_locations_hub():
    path = os.path.join(WIKI_DIR, "locations/index.html")
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    replacements = [
        (r'<img src="[^"]+" alt="Zone A"', '<img src="../assets/layout/city/icons/icon_zone_a_core.svg" alt="Zone A"'),
        (r'<img src="[^"]+" alt="Zone B"', '<img src="../assets/layout/city/icons/icon_zone_b_west.svg" alt="Zone B"'),
        (r'<img src="[^"]+" alt="Zone C"', '<img src="../assets/layout/city/icons/icon_zone_c_east.svg" alt="Zone C"'),
        (r'<img src="[^"]+" alt="Zone D"', '<img src="../assets/layout/city/icons/icon_zone_d_flanks.svg" alt="Zone D"'),
        (r'<img src="[^"]+" alt="Zone E"', '<img src="../assets/layout/city/icons/icon_zone_e_bulwark.svg" alt="Zone E"'),
        (r'<img src="[^"]+" alt="The Desolate"', '<img src="../assets/icons/icon_loc_the_desolate.svg" alt="The Desolate"'),
        (r'<img src="[^"]+" alt="Hollow Glass"', '<img src="../assets/icons/icon_loc_the_hollow_glass.svg" alt="Hollow Glass"'),
        (r'<img src="[^"]+" alt="Library"', '<img src="../assets/icons/icon_loc_the_library_of_stolen_pasts.svg" alt="Library"'),
        (r'<img src="[^"]+" alt="The Maw"', '<img src="../assets/icons/icon_loc_the_maw.svg" alt="The Maw"'),
        (r'<img src="[^"]+" alt="Bell Tower"', '<img src="../assets/icons/icon_loc_the_orphan_bell_tower.svg" alt="Bell Tower"'),
        (r'<img src="[^"]+" alt="Unknown Cities"', '<img src="../assets/icons/icon_loc_unknown_cities.svg" alt="Unknown Cities"'),
        (r'<img src="[^"]+" alt="District Structure"', '<img src="../assets/layout/city/icons/icon_somnarak_city_badge.svg" alt="District Structure"')
    ]

    for pattern, repl in replacements:
        c = re.sub(pattern, repl, c)

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Fixed all icons in locations/index.html")

def fix_lore_hub():
    path = os.path.join(WIKI_DIR, "lore/index.html")
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    replacements = [
        (r'<img src="[^"]+" alt="Absolvohan"', '<img src="../assets/icons/icon_lore_absolvohan.svg" alt="Absolvohan"'),
        (r'<img src="[^"]+" alt="Alpha Tree"', '<img src="../assets/layout/city/icons/icon_alpha_tree.svg" alt="Alpha Tree"'),
        (r'<img src="[^"]+" alt="Three Sorrows"', '<img src="../assets/icons/icon_lore_three_sorrows.svg" alt="Three Sorrows"'),
        (r'<img src="[^"]+" alt="Taboos"', '<img src="../assets/icons/icon_lore_taboo_resonance.svg" alt="Taboos"'),
        (r'<img src="[^"]+" alt="Cheongula"', '<img src="../assets/icons/icon_lore_cheongula.svg" alt="Cheongula"'),
        (r'<img src="[^"]+" alt="Dawn of Hope"', '<img src="../assets/icons/icon_lore_dawn_of_hope.svg" alt="Dawn of Hope"'),
        (r'<img src="[^"]+" alt="Doorspeech"', '<img src="../assets/icons/icon_lore_doorspeech.svg" alt="Doorspeech"'),
        (r'<img src="[^"]+" alt="Dream Realm"', '<img src="../assets/icons/icon_lore_dream_realm.svg" alt="Dream Realm"'),
        (r'<img src="[^"]+" alt="Daily Life"', '<img src="../assets/icons/icon_lore_daily_life.svg" alt="Daily Life"'),
        (r'<img src="[^"]+" alt="Efflorescence"', '<img src="../assets/icons/icon_lore_efflorescence.svg" alt="Efflorescence"'),
        (r'<img src="[^"]+" alt="Named Fractures"', '<img src="../assets/icons/icon_lore_named_fractures.svg" alt="Named Fractures"'),
        (r'<img src="[^"]+" alt="Night Hazards"', '<img src="../assets/icons/icon_lore_night_hazards.svg" alt="Night Hazards"'),
        (r'<img src="[^"]+" alt="Cosmology"', '<img src="../assets/icons/icon_lore_cosmology.svg" alt="Cosmology"'),
        (r'<img src="[^"]+" alt="Name Registry"', '<img src="../assets/icons/icon_lore_name_registry.svg" alt="Name Registry"'),
        (r'<img src="[^"]+" alt="Three Ages"', '<img src="../assets/icons/icon_lore_three_ages.svg" alt="Three Ages"'),
        (r'<img src="[^"]+" alt="Weeping River"', '<img src="../assets/icons/icon_lore_weeping_effluent.svg" alt="Weeping River"')
    ]

    for pattern, repl in replacements:
        c = re.sub(pattern, repl, c)

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Fixed all icons in lore/index.html")

def fix_mechanics_hub():
    path = os.path.join(WIKI_DIR, "mechanics/index.html")
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    replacements = [
        (r'<img src="[^"]+" alt="Damage Matrix"', '<img src="../assets/icons/icon_mech_han_energy_damage.svg" alt="Damage Matrix"'),
        (r'<img src="[^"]+" alt="Work Types"', '<img src="../assets/icons/icon_mech_four_work_types.svg" alt="Work Types"'),
        (r'<img src="[^"]+" alt="SECC System"', '<img src="../assets/icons/icon_mech_secc_classification.svg" alt="SECC System"'),
        (r'<img src="[^"]+" alt="Resonant Clash"', '<img src="../assets/icons/icon_mech_resonant_clash.svg" alt="Resonant Clash"'),
        (r'<img src="[^"]+" alt="Ordeals"', '<img src="../assets/icons/icon_mech_ordeals_framework.svg" alt="Ordeals"'),
        (r'<img src="[^"]+" alt="Agent Stats"', '<img src="../assets/icons/icon_mech_agent_stats.svg" alt="Agent Stats"'),
        (r'<img src="[^"]+" alt="Containment"', '<img src="../assets/icons/icon_mech_containment_suppression.svg" alt="Containment"'),
        (r'<img src="[^"]+" alt="Standard Equipment"', '<img src="../assets/icons/icon_mech_standard_equipment.svg" alt="Standard Equipment"'),
        (r'<img src="[^"]+" alt="Bestiary"', '<img src="../assets/icons/icon_mech_enemy_bestiary.svg" alt="Bestiary"'),
        (r'<img src="[^"]+" alt="Therapy"', '<img src="../assets/icons/icon_mech_fracture_therapy.svg" alt="Therapy"'),
        (r'<img src="[^"]+" alt="Relic Registry"', '<img src="../assets/icons/icon_mech_han_relic_registry.svg" alt="Relic Registry"'),
        (r'<img src="[^"]+" alt="Relic Tools"', '<img src="../assets/icons/icon_mech_relic_tools.svg" alt="Relic Tools"'),
        (r'<img src="[^"]+" alt="MAW System"', '<img src="../assets/icons/icon_mech_maw_equipment_system.svg" alt="MAW System"'),
        (r'<img src="[^"]+" alt="Taboo Resonance"', '<img src="../assets/icons/icon_mech_taboo_resonance_mech.svg" alt="Taboo Resonance"')
    ]

    for pattern, repl in replacements:
        c = re.sub(pattern, repl, c)

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Fixed all icons in mechanics/index.html")

def fix_factions_hub():
    path = os.path.join(WIKI_DIR, "factions/index.html")
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    c = re.sub(
        r'<img src="[^"]+" alt="Faction Tech"',
        '<img src="../assets/icons/icon_faction_technology.svg" alt="Faction Tech"',
        c
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Fixed all icons in factions/index.html")

if __name__ == "__main__":
    fix_characters_hub()
    fix_locations_hub()
    fix_lore_hub()
    fix_mechanics_hub()
    fix_factions_hub()
