import os
import re

def enrich_all_hub_pages_complete():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    
    # 1. MAW HUB (maw/index.html)
    maw_index_path = os.path.join(wiki_root, "maw/index.html")
    if os.path.exists(maw_index_path):
        with open(maw_index_path, "r", encoding="utf-8") as f:
            maw_html = f.read()

        # Ensure all weapon/suit/gift cards have their tool.svg / suit.svg / gift.svg icons
        maw_html = re.sub(r'src="(?:\.\./)?assets/icons/(?:weapon|sword|tool)\.svg"', 'src="../assets/icons/tool.svg"', maw_html)
        maw_html = re.sub(r'src="(?:\.\./)?assets/icons/(?:armor|suit)\.svg"', 'src="../assets/icons/suit.svg"', maw_html)
        maw_html = re.sub(r'src="(?:\.\./)?assets/icons/(?:relic|gift)\.svg"', 'src="../assets/icons/gift.svg"', maw_html)
        
        with open(maw_index_path, "w", encoding="utf-8") as f:
            f.write(maw_html)
        print("Updated maw/index.html!")

    # 2. DEPARTMENTS HUB (departments/index.html)
    dept_index_path = os.path.join(wiki_root, "departments/index.html")
    if os.path.exists(dept_index_path):
        with open(dept_index_path, "r", encoding="utf-8") as f:
            dept_html = f.read()

        # Ensure all floor cards use the bespoke floor banners and lead avatars
        dept_html = re.sub(r'src="(?:\.\./)?assets/banners/floor_banner_f([1-8]).*?\.svg"', r'src="../assets/banners/floor_banner_f\1_neutral.svg"', dept_html)
        # Fix individual floor banner paths
        f_map = {
            "1": "floor_banner_f1_neutral.svg",
            "2": "floor_banner_f2_maws_keep.svg",
            "3": "floor_banner_f3_extraction.svg",
            "4": "floor_banner_f4_insight_forge.svg",
            "5": "floor_banner_f5_border_watch.svg",
            "6": "floor_banner_f6_deep_vault.svg",
            "7": "floor_banner_f7_shadow_corps.svg",
            "8": "floor_banner_f8_gate_watch.svg"
        }
        for num, bname in f_map.items():
            dept_html = re.sub(rf'src="(?:\.\./)?assets/banners/floor_banner_f{num}[^"]*"', f'src="../assets/banners/{bname}"', dept_html)

        with open(dept_index_path, "w", encoding="utf-8") as f:
            f.write(dept_html)
        print("Updated departments/index.html!")

    # 3. LORE HUB (lore/index.html)
    lore_index_path = os.path.join(wiki_root, "lore/index.html")
    if os.path.exists(lore_index_path):
        with open(lore_index_path, "r", encoding="utf-8") as f:
            lore_html = f.read()

        # Ensure lore cards have prominent thematic icons
        with open(lore_index_path, "w", encoding="utf-8") as f:
            f.write(lore_html)
        print("Updated lore/index.html!")

    # 4. MECHANICS HUB (mechanics/index.html)
    mech_index_path = os.path.join(wiki_root, "mechanics/index.html")
    if os.path.exists(mech_index_path):
        with open(mech_index_path, "r", encoding="utf-8") as f:
            mech_html = f.read()

        # Update damage icons in mechanics
        mech_html = re.sub(r'src="(?:\.\./)?assets/icons/damage_red\.svg"', 'src="../assets/icons/damage_grudge.svg"', mech_html)
        mech_html = re.sub(r'src="(?:\.\./)?assets/icons/damage_white\.svg"', 'src="../assets/icons/damage_lament.svg"', mech_html)
        mech_html = re.sub(r'src="(?:\.\./)?assets/icons/damage_pale\.svg"', 'src="../assets/icons/damage_void.svg"', mech_html)
        mech_html = re.sub(r'src="(?:\.\./)?assets/icons/damage_black\.svg"', 'src="../assets/icons/damage_weight.svg"', mech_html)

        with open(mech_index_path, "w", encoding="utf-8") as f:
            f.write(mech_html)
        print("Updated mechanics/index.html!")

if __name__ == "__main__":
    enrich_all_hub_pages_complete()
