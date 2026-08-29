import os
import re

def upgrade_all_entity_pages():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    ent_dir = os.path.join(wiki_root, "entities")

    entities = [
        ("se-001", "se-001-the-orphaned-bell.html", "The Orphaned Bell", "Lament — Deep Blue", "Object-Lament", "C-IVδ-001 [LO]", "#38bdf8"),
        ("se-002", "se-002-the-grieving-colossus.html", "The Grieving Colossus", "Weight — Black", "Subject-Body", "C-Vδ-002 [WS]", "#ef5b55"),
        ("se-003", "se-003-the-wilderness-tide.html", "The Wilderness Tide", "Weight — Black", "Place-Body", "O-Vγ-003 [WP]", "#71efaf"),
        ("se-005", "se-005-the-smothering-mother.html", "The Smothering Mother", "Grudge — Crimson", "Subject-Body", "N-IVδ-005 [GS]", "#c084fc"),
        ("se-007", "se-007-brume.html", "Brume", "Void — Pale White", "Place-Phantasmal", "O-IIγ-007 [VP]", "#38bdf8"),
        ("se-009", "se-009-the-memory-weaver.html", "The Memory Weaver", "Void — Pale White", "Subject-Dream", "C-IVγ-009 [VS]", "#38bdf8"),
        ("se-010", "se-010-the-convergence.html", "The Convergence", "Grudge — Crimson", "Place-Tale", "C-IVω-001 [GP]", "#c084fc"),
        ("se-011", "se-011-the-whispering-walls.html", "The Whispering Walls", "Lament — Deep Blue", "Subject-Spirit", "C-IIIγ-021 [LS]", "#38bdf8"),
        ("se-014", "se-014-the-debt-eater.html", "The Debt Eater", "Void — Pale White", "Subject-Body", "C-IIIβ-014 [VS]", "#f1df76"),
        ("se-015", "se-015-the-debt-scale.html", "The Debt Scale", "Lament — Deep Blue", "Object-Weight", "C-IIIγ-015 [LS]", "#f1df76")
    ]

    for se_id, fname, name, elem, manif, code, col in entities:
        fpath = os.path.join(ent_dir, fname)
        if not os.path.exists(fpath):
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        # 1. Ensure Tactical Header Banner is displayed right above the article or in entity hero
        banner_tag = f'''
      <!-- Tactical Cinematic Header Banner (Asset Type 2: BANNER) -->
      <div class="entity-tactical-banner" style="margin-bottom: 2rem; border: 2.5px solid {col}; border-radius: 8px; overflow: hidden; box-shadow: 0 8px 30px rgba(0,0,0,0.85);">
        <img src="../assets/art/entities/{se_id}-banner.svg" alt="{name} Tactical Banner" style="width: 100%; height: auto; display: block;">
      </div>
'''
        # Replace or inject banner before entity-hero
        if "class=\"entity-tactical-banner\"" in html:
            html = re.sub(r'<div class="entity-tactical-banner".*?</div>', banner_tag.strip(), html, flags=re.DOTALL)
        else:
            html = html.replace('<section class="entity-hero', banner_tag + '\n<section class="entity-hero')

        # 2. Ensure Entity Portrait in Hero uses Asset Type 3: PROFILE
        html = re.sub(
            r'<img alt="[^"]*"\s+class="entity-portrait"\s+src="[^"]*"/>',
            f'<img alt="Operational Profile of {name}" class="entity-portrait" src="../assets/art/entities/{se_id}-profile.svg"/>',
            html
        )

        # 3. Ensure Emblem Seal (Asset Type 1: ICON) is placed in entity symbols header
        icon_symbol = f'<span><img alt="Seal" src="../assets/art/entities/{se_id}-icon.svg" style="width:36px;height:36px;vertical-align:middle;margin-right:6px;display:inline-block;border-radius:4px;border:1px solid {col};padding:2px;background:#050a12;"/>SECC Seal</span>'
        if f"{se_id}-icon.svg" not in html:
            html = html.replace('<div class="entity-symbols">', '<div class="entity-symbols">' + icon_symbol)

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)

    print("Updated all 10 Sorrow Entity articles with distinct ICON, BANNER, and PROFILE asset placements!")

if __name__ == "__main__":
    upgrade_all_entity_pages()
