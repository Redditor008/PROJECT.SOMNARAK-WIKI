import os, glob, re

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

nav_map = {
    "assets/images/emblem.svg": "assets/icons/somnarak_icon.svg",
    "assets/images/icons/characters.svg": "assets/icons/nav_characters.svg",
    "assets/images/icons/lore.svg": "assets/icons/nav_lore.svg",
    "assets/images/icons/locations.svg": "assets/icons/nav_locations.svg",
    "assets/images/icons/factions.svg": "assets/icons/nav_factions.svg",
    "assets/images/icons/departments.svg": "assets/icons/floor-1-command.svg",
    "assets/images/icons/entities.svg": "assets/icons/nav_entities.svg",
    "assets/images/icons/maw.svg": "assets/icons/nav_maw.svg",
    "assets/images/icons/mechanics.svg": "assets/icons/nav_mechanics.svg",
    "assets/images/icons/map-facility.svg": "assets/layout/hand/icons/the_hand_dr_icon_styled.svg",
    "assets/images/icons/map-city.svg": "assets/layout/city/icons/somnarak_city_icon.svg",
    "assets/images/icons/archive.svg": "assets/icons/ref_project_somnarak.svg",
}

for html_path in glob.glob(os.path.join(WIKI_DIR, '**/*.html'), recursive=True):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    rel_depth = len(os.path.relpath(html_path, WIKI_DIR).split(os.sep)) - 1
    prefix = "../" * rel_depth

    for fake_p, real_p in nav_map.items():
        content = content.replace(f'{prefix}{fake_p}', f'{prefix}{real_p}')
        content = content.replace(fake_p, f'{prefix}{real_p}')

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Nav rail and icon references fixed.")
