import os, glob, re

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# Terms with exact relative paths
terms_map = {
    "Director Majin": ("characters/the-director-majin.html", "assets/icons/somnarak_icon.svg"),
    "Seiyon": ("characters/the-secretary-seiyon.html", "assets/icons/floor-2-maw.svg"),
    "Dekan": ("characters/the-containment-lead-dekan.html", "assets/icons/shield_hope.svg"),
    "Zyrak": ("characters/the-extraction-lead-zyrak.html", "assets/icons/weapon.svg"),
    "Ayshuk": ("characters/the-research-lead-ayshuk.html", "assets/icons/clarity.svg"),
    "Mellda": ("characters/the-border-lead-mellda.html", "assets/icons/veil.svg"),
    "Marjuk": ("characters/the-archive-lead-marjuk.html", "assets/icons/floor-6-vault.svg"),
    "Ishall": ("characters/the-outsider-ishall.html", "assets/icons/floor-7-shadow.svg"),
    "Xyan": ("characters/the-exile-xyan.html", "assets/icons/floor-8-gate.svg"),
    "Alpha Tree": ("lore/the-alpha-tree.html", "assets/icons/art_dawn.svg"),
    "The Desolate": ("locations/the-desolate.html", "assets/icons/outside.svg"),
    "The Weeping": ("lore/the-weeping-river.html", "assets/icons/lament.svg"),
    "The Maw": ("locations/the-maw.html", "assets/icons/art_maw.svg"),
    "Hand of Change": ("atlas/hand-of-change-map.html", "assets/layout/hand/icons/the_hand_dr_icon_styled.svg"),
    "Reverie Directorate": ("factions/the-reverie-directorate.html", "assets/icons/fac_rd.svg"),
    "Absolvohan": ("lore/the-cycle-and-absolvohan.html", "assets/icons/ref_absolvohan.svg"),
}

for html_path in glob.glob(os.path.join(WIKI_DIR, '**/*.html'), recursive=True):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    rel_depth = len(os.path.relpath(html_path, WIKI_DIR).split(os.sep)) - 1
    prefix = "../" * rel_depth

    # Quick cleanup of any stale icon references
    content = content.replace(f'{prefix}assets/icons/the_hand_dr_facility_cutaway_clean.svg', f'{prefix}assets/layout/hand/icons/the_hand_dr_icon_styled.svg')
    content = content.replace(f'assets/icons/the_hand_dr_facility_cutaway_clean.svg', f'{prefix}assets/layout/hand/icons/the_hand_dr_icon_styled.svg')
    content = content.replace(f'{prefix}assets/icons/somnarak_city_icon.svg', f'{prefix}assets/layout/city/icons/somnarak_city_icon.svg')
    content = content.replace(f'assets/icons/somnarak_city_icon.svg', f'{prefix}assets/layout/city/icons/somnarak_city_icon.svg')
    content = content.replace(f'{prefix}assets/icons/icon_dept_f', f'{prefix}assets/layout/hand/icons/icon_dept_f')
    content = content.replace(f'assets/icons/icon_dept_f', f'{prefix}assets/layout/hand/icons/icon_dept_f')

    def replace_in_p(match):
        p_content = match.group(1)
        for term, (target_rel, icon_path) in terms_map.items():
            if term in p_content and f'>{term}</a>' not in p_content:
                icon_tag = f'<img src="{prefix}{icon_path}" class="wiki-icon" alt="">'
                link_tag = f'<a href="{prefix}{target_rel}" class="wiki-link">{icon_tag} {term}</a>'
                pattern = rf'(?<!["\'>/])\b{re.escape(term)}\b(?!["\'<])'
                p_content = re.sub(pattern, link_tag, p_content, count=2)
        return f'<p>{p_content}</p>'

    new_content = re.sub(r'<p>(.*?)</p>', replace_in_p, content, flags=re.DOTALL)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Wiki links and icon paths sanitized.")
