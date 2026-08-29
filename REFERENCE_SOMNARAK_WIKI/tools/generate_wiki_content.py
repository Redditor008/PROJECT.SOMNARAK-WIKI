import os
import json
import re

WIKI_DIR = "/home/user/01_Somnarak_Wiki"
SRC_CHAR = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/Character_Wiki"
SRC_ABSOL = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/Absolvohan"
SRC_WORLD = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/World_Reference"

def read_src(folder, filename):
    p = os.path.join(folder, filename)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def write_page(folder, filename, title, subtitle, color, icon_svg, meta_cards, article_body):
    rel_root = ".."
    meta_cards_html = "".join([f"""<div class="meta-card"><b>{k}</b><span>{v}</span></div>""" for k, v in meta_cards])
    
    html = f"""<!doctype html>
<html lang="en" data-article-status="article">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title} — Somnarak Wiki</title>
  <meta name="description" content="{subtitle}">
  <link rel="icon" type="image/svg+xml" href="{rel_root}/assets/icons/somnarak_icon.svg">
  <link rel="stylesheet" href="{rel_root}/assets/css/wiki.css">
  <script defer src="{rel_root}/assets/js/wiki.js"></script>
</head>
<body>
<header class="utility">
  <button class="nav-open" type="button" aria-label="Open navigation">☰</button>
  <a class="utility-brand" href="{rel_root}/index.html">SOMNARAK.WIKI</a>
  <span>YEAR 4,238 · DAWN INITIATIVE</span>
  <nav>
    <a href="{rel_root}/index.html">Main page</a>
    <a href="{rel_root}/characters/index.html">Characters</a>
    <a href="{rel_root}/lore/index.html">Lore</a>
    <a href="{rel_root}/factions/index.html">Factions</a>
    <a href="{rel_root}/departments/index.html">Departments</a>
    <a href="{rel_root}/locations/index.html">Locations</a>
    <a href="{rel_root}/mechanics/index.html">Mechanics</a>
    <a href="{rel_root}/entities/index.html">Sorrow Entities</a>
    <a href="{rel_root}/maw/index.html">M.A.W.</a>
  </nav>
  <div class="search">
    <input id="search" data-index="{rel_root}/data/search.json" aria-label="Search" placeholder="Search Somnarak Wiki">
    <div id="results"></div>
  </div>
</header>

<div class="wiki-shell">
  <aside class="left-rail">
    <div class="site-mark">
      <a href="{rel_root}/index.html">
        <img src="{rel_root}/assets/icons/somnarak_icon.svg" alt="Somnarak">
        <b>SOMNARAK</b>
        <span>WIKI ARCHIVE</span>
      </a>
    </div>
    <nav class="left-links" aria-label="Wiki navigation">
      <section>
        <h2>Archive</h2>
        <a href="{rel_root}/index.html">Main page</a>
        <a href="{rel_root}/characters/index.html">Characters Hub</a>
        <a href="{rel_root}/lore/index.html">Lore &amp; Cosmology</a>
        <a href="{rel_root}/factions/index.html">Factions &amp; Guilds</a>
        <a href="{rel_root}/departments/index.html">Hand of Change</a>
        <a href="{rel_root}/locations/index.html">Atlas &amp; Maps</a>
        <a href="{rel_root}/mechanics/index.html">Battle &amp; Systems</a>
        <a href="{rel_root}/entities/index.html">Sorrow Entities</a>
        <a href="{rel_root}/maw/index.html">M.A.W. Codex</a>
      </section>
      <section>
        <h2>Echo-Cores</h2>
        <a href="{rel_root}/characters/the-director-majin.html">Majin (Director)</a>
        <a href="{rel_root}/characters/the-secretary-seiyon.html">Seiyon (Secretary)</a>
        <a href="{rel_root}/characters/the-containment-lead-dekan.html">Dekan (Containment)</a>
        <a href="{rel_root}/characters/the-extraction-lead-zyrak.html">Zyrak (Extraction)</a>
        <a href="{rel_root}/characters/the-research-lead-ayshuk.html">Ayshuk (Research)</a>
        <a href="{rel_root}/characters/the-border-lead-mellda.html">Mellda (Border)</a>
        <a href="{rel_root}/characters/the-archive-lead-marjuk.html">Marjuk (Archive)</a>
        <a href="{rel_root}/characters/the-outsider-ishall.html">Ishall (Outsider)</a>
        <a href="{rel_root}/characters/the-exile-xyan.html">Xyan (Exile)</a>
      </section>
      <section>
        <h2>The Palm</h2>
        <a href="{rel_root}/departments/floor-1-neutral-command.html">Neutral Command</a>
        <a href="{rel_root}/departments/floor-2-maws-keep.html">The Maw’s Keep</a>
        <a href="{rel_root}/departments/floor-3-extraction-hall.html">Extraction Hall</a>
      </section>
      <section>
        <h2>Fingers &amp; Wing</h2>
        <a href="{rel_root}/departments/floor-4-insight-forge.html">Insight Forge</a>
        <a href="{rel_root}/departments/floor-5-border-watch.html">Border Watch</a>
        <a href="{rel_root}/departments/floor-6-deep-vault.html">Deep Vault</a>
        <a href="{rel_root}/departments/floor-7-shadow-corps.html">Shadow Corps</a>
        <a href="{rel_root}/departments/floor-8-gate-watch.html">Gate Watch</a>
      </section>
    </nav>
  </aside>

  <main id="content">
    <div class="page-tabs">
      <span>Article</span>
      <b>{folder.upper()} // ARCHIVE</b>
    </div>
    <div class="breadcrumbs">
      <a href="{rel_root}/index.html">Main page</a><i>›</i><a href="index.html">{folder.capitalize()}</a><i>›</i>{title}
    </div>

    <section class="department-hero" style="--floor:{color}">
      <img src="{rel_root}/assets/icons/{icon_svg}" alt="">
      <div>
        <span>{folder.upper()} // CANONICAL ARCHIVE</span>
        <h1>{title}</h1>
        <p>{subtitle}</p>
      </div>
    </section>

    <div class="entity-meta-grid">
      {meta_cards_html}
    </div>

    <article class="article-body">
      {article_body}
    </article>
  </main>

  <aside class="floor-rail" aria-label="Hand of Change departments">
    <h2>HAND OF CHANGE</h2>
    <a class="pm-hazard-btn" href="{rel_root}/departments/floor-1-neutral-command.html" style="--floor-color:#ef5b55"><div class="pm-hazard-btn-text"><small>FLOOR 1</small><b>NEUTRAL COMMAND</b></div><img src="{rel_root}/assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt=""></a>
    <a class="pm-hazard-btn" href="{rel_root}/departments/floor-2-maws-keep.html" style="--floor-color:#6f7ee8"><div class="pm-hazard-btn-text"><small>FLOOR 2</small><b>MAW’S KEEP</b></div><img src="{rel_root}/assets/layout/hand/icons/icon_dept_f2_maws_keep.svg" alt=""></a>
    <a class="pm-hazard-btn" href="{rel_root}/departments/floor-3-extraction-hall.html" style="--floor-color:#e6c94d"><div class="pm-hazard-btn-text"><small>FLOOR 3</small><b>EXTRACTION HALL</b></div><img src="{rel_root}/assets/layout/hand/icons/icon_dept_f3_extraction.svg" alt=""></a>
    <a class="pm-hazard-btn" href="{rel_root}/departments/floor-4-insight-forge.html" style="--floor-color:#47c978"><div class="pm-hazard-btn-text"><small>FLOOR 4</small><b>INSIGHT FORGE</b></div><img src="{rel_root}/assets/layout/hand/icons/icon_dept_f4_insight_forge.svg" alt=""></a>
    <a class="pm-hazard-btn" href="{rel_root}/departments/floor-5-border-watch.html" style="--floor-color:#d7d7d7"><div class="pm-hazard-btn-text"><small>FLOOR 5</small><b>BORDER WATCH</b></div><img src="{rel_root}/assets/layout/hand/icons/icon_dept_f5_border_watch.svg" alt=""></a>
    <a class="pm-hazard-btn" href="{rel_root}/departments/floor-6-deep-vault.html" style="--floor-color:#8d2e42"><div class="pm-hazard-btn-text"><small>FLOOR 6</small><b>DEEP VAULT</b></div><img src="{rel_root}/assets/layout/hand/icons/icon_dept_f6_deep_vault.svg" alt=""></a>
    <a class="pm-hazard-btn" href="{rel_root}/departments/floor-7-shadow-corps.html" style="--floor-color:#f0a6c4"><div class="pm-hazard-btn-text"><small>FLOOR 7</small><b>SHADOW CORPS</b></div><img src="{rel_root}/assets/layout/hand/icons/icon_dept_f7_shadow_corps.svg" alt=""></a>
    <a class="pm-hazard-btn" href="{rel_root}/departments/floor-8-gate-watch.html" style="--floor-color:#f4efa0"><div class="pm-hazard-btn-text"><small>FLOOR 8</small><b>GATE WATCH</b></div><img src="{rel_root}/assets/layout/hand/icons/icon_dept_f8_gate_watch.svg" alt=""></a>
    <a class="pm-action-btn" href="{rel_root}/atlas/hand-of-change-map.html">FACILITY CUTAWAY MAP<img src="{rel_root}/assets/layout/hand/icons/the_hand_dr_icon_styled.svg" alt=""></a>
    <a class="pm-action-btn" href="{rel_root}/atlas/somnarak-city-map.html">CITY MASTER BLUEPRINT<img src="{rel_root}/assets/layout/city/icons/somnarak_city_icon.svg" alt=""></a>
  </aside>
</div>

<footer>
  <div>
    <b>SOMNARAK WIKI</b> · Encyclopedia of Somnarak<br>
    Content is available under the Somnarak Archival Documentation License · Year 4,238 Dawn Initiative
  </div>
  <div>
    The 1,778 Cycles have ended.<br>
    Xyan commands Gate Watch. Hope has not removed sorrow; it has changed what the city believes can be done with it.
  </div>
</footer>
</body>
</html>
"""
    dest_path = os.path.join(WIKI_DIR, folder, filename)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Written: {folder}/{filename} ({len(html)} chars)")

print("Helper functions compiled.")
