import os
import glob
import re
from bs4 import BeautifulSoup

WIKI_DIR = "/home/user/01_Somnarak_Wiki"
SRC_WORLD = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/World_Reference"

# Helper write_page
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
  <div class="utility-left">
    <button class="nav-open" type="button" aria-label="Open navigation">☰</button>
    <a class="utility-brand" href="{rel_root}/index.html">SOMNARAK.WIKI</a>
    <span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
  </div>
  <nav aria-label="Main navigation">
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
      <img src="{rel_root}/assets/layout/hand/icons/{icon_svg}" alt="">
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
    print(f"Generated: {folder}/{filename} ({len(html):,} chars)")

print("Building remaining reference documents into dedicated articles...")

# 1. SOMNARAK_ENEMY_LIST.md -> mechanics/enemy-bestiary.html
write_page(
    folder="mechanics",
    filename="enemy-bestiary.html",
    title="Somnarak Enemy &amp; Threat Bestiary",
    subtitle="Comprehensive Classification of Hostile Combatants · Feral Entities, Syndicate Enforcers & Ordeal Apparitions",
    color="#ef5b55",
    icon_svg="icon_dept_f2_maws_keep.svg",
    meta_cards=[
        ("Bestiary Scope", "City-Wide Threat Taxonomy"),
        ("Threat Categories", "Feral Entities, Underworld Frays, Ordeals, Precursor Constructs"),
        ("Governing Bureau", "Floor 2 Vanguard Command & UCD Strike Units"),
        ("Tactical Protocol", "Breach Suppression & Subdual")
    ],
    article_body="""
      <h2>Threat Taxonomy Overview</h2>
      <p>Hostile entities encountered across Somnarak, the Underworld, and the Outskirts are categorized into four major tactical threat types:</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Threat Type</th>
              <th>Origin</th>
              <th>Primary Attack Element</th>
              <th>Tactical Vulnerabilities & Countermeasures</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>Feral Sorrow Apparitions</b></td>
              <td>Subterranean Maw Runoff</td>
              <td>Lament (Blue) / Grudge (Red)</td>
              <td>Weak to Black (Weight) posture damage. Subdue before sorrow saturation reaches 100%.</td>
            </tr>
            <tr>
              <td><b>Rogue Fray Enforcers</b></td>
              <td>Underworld Black Markets</td>
              <td>Grudge (Red) / Slash Physical</td>
              <td>Equipped with bootleg M.A.W. plates; weak to Blue SP disruption and Stagger Break.</td>
            </tr>
            <tr>
              <td><b>Ordeal Constructs</b></td>
              <td>Facility Resonance Overload</td>
              <td>Varies (Dawn to Midnight)</td>
              <td>Coordinate floor-wide focus fire on primary cores before Sorrow Counters drop.</td>
            </tr>
            <tr>
              <td><b>Wasteland Behemoths</b></td>
              <td>The Desolate Ashlands</td>
              <td>Weight (Black) / Void (Pale)</td>
              <td>Requires heavy artillery from Zone E Bulwark and Ω-tier barrier anchors.</td>
            </tr>
          </tbody>
        </table>
      </div>
    """
)

# 2. SOMNARAK_CORPORATIONS.md -> factions/the-founding-corporations.html
write_page(
    folder="factions",
    filename="the-founding-corporations.html",
    title="The Founding Industrial Corporations",
    subtitle="The 5 Precursor Megacorporations of Somnarak · Metallurgy, Sap Hydro-Grids & Cartels",
    color="#e6c94d",
    icon_svg="icon_dept_f3_extraction.svg",
    meta_cards=[
        ("Faction Category", "Pre-Cataclysm Commercial & Industrial Cartels"),
        ("Key Corporations", "Han-Metallurgy Trust, Alpha-Hydro Corp, Siphon-Chem, Spire Dynamics, Veil-Glass"),
        ("Economic Influence", "Foundry Operations, Transit Rails, Residential Zoning"),
        ("Affiliation", "High Council Commercial Senate")
    ],
    article_body="""
      <h2>The Precursor Industrial Titans</h2>
      <p>Modern Somnarak was built upon the industrial foundations of five colossal commercial syndicates that financed the post-Cheongula reconstruction.</p>

      <h2>The Five Corporate Conglomerates</h2>
      <ul>
        <li><b>Han-Metallurgy Trust (한금속 트러스트):</b> Controls the Titan Foundries in Zone D; manufactures resonant granite plates and mourning steel.</li>
        <li><b>Alpha-Hydro Corporation (알파 수력):</b> Manages the civic aqueducts, municipal sap pipelines, and residential thermal grids.</li>
        <li><b>Siphon-Chem Labs (사이펀 화학):</b> Specializes in catalytic Alpha Sap distillation, medicinal salves, and neural sedatives.</li>
        <li><b>Spire Dynamics Engineering (첨탑 다이내믹스):</b> The master civil construction contractor responsible for the West Ward residential towers.</li>
        <li><b>Veil-Glass Optica (베일 광학):</b> Manufactures psychotropic observation lenses, barrier filters, and resonance microscopes.</li>
      </ul>
    """
)

# 3. SOMNARAK_HAN_RELICS.md -> mechanics/han-relic-registry.html
write_page(
    folder="mechanics",
    filename="han-relic-registry.html",
    title="Han Relic Registry (한 유물 도감)",
    subtitle="Catalog of Documented Precursor Artifacts & Resonant Relics · Grades I through V",
    color="#f1df76",
    icon_svg="icon_dept_f3_extraction.svg",
    meta_cards=[
        ("Registry Classification", "Classified Historical Relic Inventory"),
        ("Grade Scale", "Grade I (Common) to Grade V (Mythic Sovereign)"),
        ("Custodian", "Floor 6 Deep Vault & Collectors Guild"),
        ("Storage Protocol", "Sub-Zero Cryo-Sealed Vats")
    ],
    article_body="""
      <h2>The Relic Taxonomy</h2>
      <p><b>Han Relics (한 유물)</b> are physical objects from the Before-Time that absorbed extreme concentrations of emotional energy during historical cataclysms, permanently crystallizing supernatural properties.</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Relic Name</th>
              <th>Grade</th>
              <th>Resonant Property</th>
              <th>Operational Function</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>The Weeping Compass</b></td>
              <td>Grade II</td>
              <td>Lament Resonance</td>
              <td>Needle points toward the nearest uncontained sorrow source within 5 kilometers.</td>
            </tr>
            <tr>
              <td><b>The Iron Tear Vial</b></td>
              <td>Grade III</td>
              <td>Weight Resonance</td>
              <td>Absorbs up to 200 units of kinetic pressure before releasing a stabilizing shockwave.</td>
            </tr>
            <tr>
              <td><b>The Crimson Lantern of Cheonbulok</b></td>
              <td>Grade IV</td>
              <td>Grudge / Fire</td>
              <td>Emits 600°C emotional flame that burns away toxic wasteland Han miasma.</td>
            </tr>
            <tr>
              <td><b>The Sovereign Core Fragment</b></td>
              <td>Grade V</td>
              <td>Pale / Void</td>
              <td>Primordial Alpha Tree fossil capable of restoring temporal equilibrium in localized zones.</td>
            </tr>
          </tbody>
        </table>
      </div>
    """
)

# 4. SOMNARAK_TABOO_RESONANCE.md -> mechanics/taboo-resonance-mechanics.html
write_page(
    folder="mechanics",
    filename="taboo-resonance-mechanics.html",
    title="Taboo Resonance &amp; Metaphysical Backfire",
    subtitle="The Mechanics of Cosmic Retribution · Soul Calcification, Temporal Bleed & Singularity Collapse",
    color="#ef5b55",
    icon_svg="icon_dept_f6_deep_vault.svg",
    meta_cards=[
        ("System Name", "Taboo Resonance Backfire Matrix"),
        ("Governing Body", "The Giltong & Floor 4 Metaphysics Bureau"),
        ("Primary Penalties", "Soul Calcification, Memory Decay, Spatial Rupture"),
        ("Authority", "Supreme Charter of Year 3,910")
    ],
    article_body="""
      <h2>The Physics of Taboo Violations</h2>
      <p>The Seven Absolute Taboos are not merely civic laws; they are fundamental thermodynamic constraints governing human consciousness and Han energy. Violating a taboo triggers immediate <b>Metaphysical Backfire</b>:</p>

      <h2>Backfire Manifestations</h2>
      <ul>
        <li><b>Soul Calcification:</b> Direct penalty for unlicensed extraction; the perpetrator’s bone marrow and veins crystallize into solid Han stone.</li>
        <li><b>Memory Bleed:</b> Penalty for memory forgery; false memories overwrite real ones, causing permanent ego dissolution.</li>
        <li><b>Abyssal Cascade:</b> Penalty for unauthorized drilling; tears the local dimensional fabric, opening a direct conduit to the subterranean Maw.</li>
      </ul>
    """
)

# 5. SOMNARAK_NAME_REGISTRY.md -> lore/somnarak-name-registry.html
write_page(
    folder="lore",
    filename="somnarak-name-registry.html",
    title="Somnarak Name Registry (이름 보존 대장)",
    subtitle="The Sacred Archival Mandate · Preservation of Erased Lineages and Doorspeech Inscriptions",
    color="#8d2e42",
    icon_svg="icon_dept_f6_deep_vault.svg",
    meta_cards=[
        ("Archival Register", "The Master Name Ledger (이름 대장)"),
        ("Preserved Names", "Over 1.4 Million Documented Souls across 1,778 Cycles"),
        ("Keeper of Names", "Echo-Core 7 (Marjuk) · Deep Vault"),
        ("Motto", "Witness the Sorrow, Preserve the Name")
    ],
    article_body="""
      <h2>The Sacred Mandate of Remembrance</h2>
      <p>In Somnarak, a person only truly dies when their name is forgotten by the living. The <b>Name Registry</b> is the master archival database maintained by Floor 6 Deep Vault to ensure that every citizen, operative, and refugee who fell during the 1,778 Cycles remains recorded for eternity.</p>
    """
)

print("All 34 reference compendiums successfully generated.")
