import os

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

locations_data = {
    "zone-a-core-nexus.html": (
        "Zone A — Core Nexus",
        "The Central Spire & Reverie Directorate Executive HQ",
        "#ef5b55",
        "banner_zonemap.svg",
        """
        <h2>1. Topological &amp; Political Overview</h2>
        <p><strong>Zone A (Core Nexus — 核心樞紐)</strong> is the innermost territorial sector of Somnarak, encircling the base of the monumental Central Spire and the upper trunk of the Alpha Tree. Zone A houses the supreme governing bodies of the city: the Executive Command of the Reverie Directorate, the Senate Citadel of the High Council, and the central planetary telemetry stations.</p>

        <h2>2. Key Sector Infrastructure</h2>
        <ul>
          <li><strong>The Central Spire (중앙 첨탑):</strong> A 2,400-meter crystalline titanium monolith anchoring the upper barrier matrix and housing Directorate command.</li>
          <li><strong>The Grand Senate Hall:</strong> Meeting chambers of the twelve Council of Sights senators.</li>
          <li><strong>The Palm Sub-Structure:</strong> The primary surface entrance and heavy freight elevators descending directly into The Hand of Change facility.</li>
        </ul>
        """
    ),
    "zone-b-west-ward.html": (
        "Zone B — West Ward",
        "High-Density Residential Sector & Old Lament District",
        "#38bdf8",
        "banner_lament.svg",
        """
        <h2>1. Residential Spires &amp; Cultural Heritage</h2>
        <p><strong>Zone B (West Ward — 西部管區)</strong> is the most populous residential district in Somnarak, housing over 450 million registered citizens within interconnected hexagonal tenement spires. Characterized by cool cyan lighting and tranquil canals fed by purified surface runoff, Zone B represents the cultural heart of the city.</p>

        <h2>2. The Historic Old Lament Sector</h2>
        <p>In the oldest quarter of Zone B stands the <em>Old Lament District</em>—a preserved historical sector of pre-Cycle basalt stone architecture. Here sits the sealed bell tower of SE-001 (The Orphaned Bell) and the sprawling archives of the Library of Stolen Pasts.</p>
        """
    ),
    "zone-c-collectors-row.html": (
        "Zone C — Collector's Row",
        "Commercial Bazaar, Scavenger Enclaves & Debt Courts",
        "#a78bfa",
        "banner_factions.svg",
        """
        <h2>1. The Commercial Capital</h2>
        <p><strong>Zone C (Collector's Row — 收集者街區)</strong> is the bustling financial, merchant, and trade epicenter of Somnarak. Lined with thousands of open-air neon bazaars, pawn emporiums, and relic exchange halls, Zone C processes the flow of raw crystal, outside scrap, and luxury textiles between the inner spires and outer bastions.</p>

        <h2>2. The Debt Court &amp; Sub-Level Frays</h2>
        <p>Zone C is overseen by the Scavenger Guilds and the Collector Magistrates. Within the subterranean levels of Sector C-01 lies the Debt Court, where financial disputes are adjudicated under the binding metaphysical authority of SE-014 (The Debt Eater) and SE-015 (The Debt Scale).</p>
        """
    ),
    "zone-d-forge-and-gardens.html": (
        "Zone D — Forge & Gardens",
        "Alpha Arboretums, M.A.W. Industrial Looms & Migration Flank",
        "#47c978",
        "banner_hope.svg",
        """
        <h2>1. Botanical Synthesis &amp; Heavy Industry</h2>
        <p><strong>Zone D (Forge &amp; Gardens — 鍛造與庭園)</strong> is a vast sector dedicated to heavy M.A.W. manufacturing, bio-botanical research, and energy agriculture. Here, the roots of the Alpha Tree breach the surface in bioluminescent groves known as the <em>Echo Arboretums</em>, cultivated by the Weavers Guild.</p>

        <h2>2. The Colossus Migration Corridor</h2>
        <p>Cutting through the western plains of Zone D is the reinforced migration trench traversed by SE-002 (The Grieving Colossus). The sector is reinforced with seismic dampening pylons designed by Master Daejun to prevent citywide tremors during the titan's periodic movements.</p>
        """
    ),
    "zone-e-perimeter-bulwark.html": (
        "Zone E — Perimeter Bulwark",
        "The Great Aegis Barrier Wall & Gates 1 through 5",
        "#d7d7d7",
        "banner_locations.svg",
        """
        <h2>1. The Outer Bastion</h2>
        <p><strong>Zone E (Perimeter Bulwark — 外圍要塞)</strong> is the outermost ring of Somnarak. Encircling the city along a 280-kilometer perimeter, Zone E consists of reinforced composite-armor bulwark walls standing 180 meters tall, crowned with heavy kinetic batteries, resonance projectors, and sentinel garrisons.</p>

        <h2>2. The Five Great Gates</h2>
        <p>Access beyond the Aegis Veil is restricted to five heavily fortified airlocks. <strong>Gate 5 (The Exile's Gate)</strong> is the most critical terminal, commanded by Xyan and Floor 8 Gate Watch, providing monitored entry to nomad caravans and outside reconnaissance squads.</p>
        """
    ),
    "the-desolate.html": (
        "The Desolate (황량 — Hwangryang)",
        "The Silent Gray Ash Wastes Beyond the Aegis Veil",
        "#f8fafc",
        "banner_void.svg",
        """
        <h2>1. The Planetary Wilderness</h2>
        <p><strong>The Desolate (황량 — 荒涼)</strong> is the infinite, silent expanse of pale gray sand, mineral ash, and howling sorrow-winds extending across the entire planet outside Somnarak. Devoid of organic vegetation, the Desolate is saturated with unrefined ambient Han that crystallizes exposed matter within hours.</p>

        <h2>2. Anomalies &amp; Mobile Horizons</h2>
        <p>Roaming the dunes are wandering anomalies such as SE-007 (Brume), the remnants of extinct civilizations like Cheonbulok, and the mobile tread-citadels of Kael the Drift King and the Wound Walkers.</p>
        """
    ),
    "the-maw.html": (
        "The Maw (심연의 아가리 — The Abyss)",
        "The Subterranean Han Basin & Abyssal Extraction Pit",
        "#8d2e42",
        "floor-2-maw.svg",
        """
        <h2>1. The Deepest Chasm</h2>
        <p><strong>The Maw (아가리)</strong> is the colossal subterranean abyss located directly beneath the Central Spire, plunging over four thousand meters into the bedrock beneath the roots of the Alpha Tree. It represents the confluence point where the river Weeping pools into a boiling sea of liquid Han.</p>

        <h2>2. Maw's Keep &amp; Deep Extraction</h2>
        <p>Overlooking the abyss is Floor 2 of The Hand of Change (Maw's Keep), commanded by Dekan. Heavy extraction gantries continuously siphon raw grief from the depths, powering the city above while maintaining containment over the deepest primeval Sorrow Entities.</p>
        """
    )
}

hub_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Somnarak Cartographic Atlas — Somnarak Wiki</title>
  <meta name="description" content="Master Cartographic Atlas of Somnarak: Urban Zones A through E, The Desolate Wilderness, and The Maw.">
  <link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg">
  <link rel="stylesheet" href="../assets/css/wiki.css">
  <script defer src="../assets/js/wiki.js"></script>
</head>
<body>
<header class="utility">
  <button class="nav-open" type="button" aria-label="Open navigation">☰</button>
  <a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
  <span>YEAR 4,238 · DAWN INITIATIVE</span>
  <nav>
    <a href="../index.html">Main page</a>
    <a href="../characters/index.html">Characters</a>
    <a href="../lore/index.html">Lore</a>
    <a href="../factions/index.html">Factions</a>
    <a href="../entities/index.html">Sorrow Entities</a>
    <a href="../maw/index.html">M.A.W.</a>
  </nav>
  <div class="search">
    <input id="search" data-index="../data/search.json" aria-label="Search" placeholder="Search Somnarak Wiki">
    <div id="results"></div>
  </div>
</header>

<div class="wiki-shell">
  <aside class="left-rail">
    <div class="site-mark">
      <a href="../index.html">
        <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak">
        <b>SOMNARAK</b>
        <span>WIKI ARCHIVE</span>
      </a>
    </div>
    <nav class="left-links" aria-label="Wiki navigation">
      <section>
        <h2>Archive</h2>
        <a href="../index.html">Main page</a>
        <a href="../characters/index.html">Characters Hub</a>
        <a href="../lore/index.html">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="index.html" style="color:#fff;font-weight:bold;">Atlas &amp; Maps</a>
        <a href="../mechanics/index.html">Battle &amp; Systems</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="../maw/index.html">M.A.W. Codex</a>
      </section>
      <section>
        <h2>Echo-Cores</h2>
        <a href="../characters/the-director-majin.html">Majin (Director)</a>
        <a href="../characters/the-secretary-seiyon.html">Seiyon (Secretary)</a>
        <a href="../characters/the-containment-lead-dekan.html">Dekan (Containment)</a>
        <a href="../characters/the-extraction-lead-zyrak.html">Zyrak (Extraction)</a>
        <a href="../characters/the-research-lead-ayshuk.html">Ayshuk (Research)</a>
        <a href="../characters/the-border-lead-mellda.html">Mellda (Border)</a>
        <a href="../characters/the-archive-lead-marjuk.html">Marjuk (Archive)</a>
        <a href="../characters/the-outsider-ishall.html">Ishall (Outsider)</a>
        <a href="../characters/the-exile-xyan.html">Xyan (Exile)</a>
      </section>
    </nav>
  </aside>

  <main id="content">
    <div class="page-tabs">
      <span>Master Atlas</span>
      <b>CARTOGRAPHY &amp; ZONES // 地圖指南</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i>Locations
    </div>

    <section class="department-hero" style="--floor:#a78bfa">
      <img src="../assets/icons/banner_locations.svg" alt="">
      <div>
        <span>REVERIE DIRECTORATE // MASTER ATLAS</span>
        <h1>Somnarak Cartographic Atlas</h1>
        <p>Urban Zones A through E, The Subterranean Maw, and The Desolate Frontier</p>
      </div>
    </section>

    <article class="article-body">
      <h2>Architectural Vector Blueprints</h2>
      <div class="archive-portal-grid" style="margin-bottom: 24px;">
        <a class="archive-portal" href="../atlas/somnarak-city-map.html" style="--portal:#f1df76">
          <span>CITY BLUEPRINT</span>
          <img src="../assets/layout/city/icons/somnarak_city_icon.svg" alt="">
          <b>MASTER CITY MAP</b>
          <small>Interactive vector blueprint</small>
        </a>
        <a class="archive-portal" href="../atlas/hand-of-change-map.html" style="--portal:#38bdf8">
          <span>FACILITY BLUEPRINT</span>
          <img src="../assets/layout/hand/icons/the_hand_dr_icon_styled.svg" alt="">
          <b>HAND OF CHANGE MAP</b>
          <small>Architectural facility cutaway</small>
        </a>
      </div>

      <h2>Zonal &amp; Frontier Sectors</h2>
      <div class="archive-portal-grid">
        <a class="archive-portal" href="zone-a-core-nexus.html" style="--portal:#ef5b55">
          <span>ZONE A</span>
          <img src="../assets/icons/banner_zonemap.svg" alt="">
          <b>CORE NEXUS</b>
          <small>Central Spire &amp; Directorate</small>
        </a>

        <a class="archive-portal" href="zone-b-west-ward.html" style="--portal:#38bdf8">
          <span>ZONE B</span>
          <img src="../assets/icons/banner_lament.svg" alt="">
          <b>WEST WARD</b>
          <small>Residential &amp; Old Lament</small>
        </a>

        <a class="archive-portal" href="zone-c-collectors-row.html" style="--portal:#a78bfa">
          <span>ZONE C</span>
          <img src="../assets/icons/banner_factions.svg" alt="">
          <b>COLLECTOR'S ROW</b>
          <small>Bazaars &amp; Debt Courts</small>
        </a>

        <a class="archive-portal" href="zone-d-forge-and-gardens.html" style="--portal:#47c978">
          <span>ZONE D</span>
          <img src="../assets/icons/banner_hope.svg" alt="">
          <b>FORGE &amp; GARDENS</b>
          <small>Arboretums &amp; M.A.W. Looms</small>
        </a>

        <a class="archive-portal" href="zone-e-perimeter-bulwark.html" style="--portal:#d7d7d7">
          <span>ZONE E</span>
          <img src="../assets/icons/banner_locations.svg" alt="">
          <b>PERIMETER BULWARK</b>
          <small>Aegis Wall &amp; Gates 1–5</small>
        </a>

        <a class="archive-portal" href="the-desolate.html" style="--portal:#f8fafc">
          <span>OUTSKIRTS</span>
          <img src="../assets/icons/banner_void.svg" alt="">
          <b>THE DESOLATE</b>
          <small>Silent Ash Wastes Beyond Veil</small>
        </a>

        <a class="archive-portal" href="the-maw.html" style="--portal:#8d2e42">
          <span>ABYSS</span>
          <img src="../assets/icons/floor-2-maw.svg" alt="">
          <b>THE MAW</b>
          <small>Subterranean Han Confluence</small>
        </a>
      </div>
    </article>
  </main>

  <aside class="floor-rail" aria-label="Hand of Change departments">
    <h2>HAND OF CHANGE</h2>
    <a class="floor-button f1" href="../departments/floor-1-neutral-command.html" style="--floor:#ef5b55"><span><small>FLOOR 1</small>NEUTRAL</span><img src="../assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt=""></a>
    <a class="floor-button f2" href="../departments/floor-2-maws-keep.html" style="--floor:#6f7ee8"><span><small>FLOOR 2</small>MAW’S KEEP</span><img src="../assets/layout/hand/icons/icon_dept_f2_maws_keep.svg" alt=""></a>
    <a class="floor-button f3" href="../departments/floor-3-extraction-hall.html" style="--floor:#e6c94d"><span><small>FLOOR 3</small>EXTRACTION HALL</span><img src="../assets/layout/hand/icons/icon_dept_f3_extraction.svg" alt=""></a>
    <a class="floor-button f4" href="../departments/floor-4-insight-forge.html" style="--floor:#47c978"><span><small>FLOOR 4</small>INSIGHT FORGE</span><img src="../assets/layout/hand/icons/icon_dept_f4_insight_forge.svg" alt=""></a>
    <a class="floor-button f5" href="../departments/floor-5-border-watch.html" style="--floor:#d7d7d7"><span><small>FLOOR 5</small>BORDER WATCH</span><img src="../assets/layout/hand/icons/icon_dept_f5_border_watch.svg" alt=""></a>
    <a class="floor-button f6" href="../departments/floor-6-deep-vault.html" style="--floor:#8d2e42"><span><small>FLOOR 6</small>DEEP VAULT</span><img src="../assets/layout/hand/icons/icon_dept_f6_deep_vault.svg" alt=""></a>
    <a class="floor-button f7" href="../departments/floor-7-shadow-corps.html" style="--floor:#f0a6c4"><span><small>FLOOR 7</small>SHADOW CORPS</span><img src="../assets/layout/hand/icons/icon_dept_f7_shadow_corps.svg" alt=""></a>
    <a class="floor-button f8" href="../departments/floor-8-gate-watch.html" style="--floor:#f4efa0"><span><small>FLOOR 8</small>GATE WATCH</span><img src="../assets/layout/hand/icons/icon_dept_f8_gate_watch.svg" alt=""></a>
    <a class="rail-action" href="../departments/index.html">OPEN FACILITY DIRECTORY</a>
  </aside>
</div>

<footer>
  <div><b>SOMNARAK WIKI</b><br>Encyclopedia of the City of Unresolved Sorrow</div>
  <div>Current record: Year 4,238 · Dawn Initiative</div>
  <div>The Cycle has ended.<br>Xyan is home and commands Gate Watch.</div>
</footer>
</body>
</html>
"""

for fname, (title, sub, color, icon, body) in locations_data.items():
    page_html = f"""<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title} — Somnarak Wiki</title>
  <meta name="description" content="Official geographical and architectural dossier for {title}: {sub}.">
  <link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg">
  <link rel="stylesheet" href="../assets/css/wiki.css">
  <script defer src="../assets/js/wiki.js"></script>
</head>
<body>
<header class="utility">
  <button class="nav-open" type="button" aria-label="Open navigation">☰</button>
  <a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
  <span>YEAR 4,238 · DAWN INITIATIVE</span>
  <nav>
    <a href="../index.html">Main page</a>
    <a href="../characters/index.html">Characters</a>
    <a href="../lore/index.html">Lore</a>
    <a href="../factions/index.html">Factions</a>
    <a href="../entities/index.html">Sorrow Entities</a>
    <a href="../maw/index.html">M.A.W.</a>
  </nav>
  <div class="search">
    <input id="search" data-index="../data/search.json" aria-label="Search" placeholder="Search Somnarak Wiki">
    <div id="results"></div>
  </div>
</header>

<div class="wiki-shell">
  <aside class="left-rail">
    <div class="site-mark">
      <a href="../index.html">
        <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak">
        <b>SOMNARAK</b>
        <span>WIKI ARCHIVE</span>
      </a>
    </div>
    <nav class="left-links" aria-label="Wiki navigation">
      <section>
        <h2>Archive</h2>
        <a href="../index.html">Main page</a>
        <a href="../characters/index.html">Characters Hub</a>
        <a href="../lore/index.html">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="index.html" style="color:#fff;font-weight:bold;">Atlas &amp; Maps</a>
        <a href="../mechanics/index.html">Battle &amp; Systems</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="../maw/index.html">M.A.W. Codex</a>
      </section>
      <section>
        <h2>Echo-Cores</h2>
        <a href="../characters/the-director-majin.html">Majin (Director)</a>
        <a href="../characters/the-secretary-seiyon.html">Seiyon (Secretary)</a>
        <a href="../characters/the-containment-lead-dekan.html">Dekan (Containment)</a>
        <a href="../characters/the-extraction-lead-zyrak.html">Zyrak (Extraction)</a>
        <a href="../characters/the-research-lead-ayshuk.html">Ayshuk (Research)</a>
        <a href="../characters/the-border-lead-mellda.html">Mellda (Border)</a>
        <a href="../characters/the-archive-lead-marjuk.html">Marjuk (Archive)</a>
        <a href="../characters/the-outsider-ishall.html">Ishall (Outsider)</a>
        <a href="../characters/the-exile-xyan.html">Xyan (Exile)</a>
      </section>
    </nav>
  </aside>

  <main id="content">
    <div class="page-tabs">
      <span>Cartographic Dossier</span>
      <b>ATLAS RECORD // 地理紀錄</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i><a href="index.html">Locations</a><i>›</i>{title}
    </div>

    <section class="department-hero" style="--floor:{color}">
      <img src="../assets/icons/{icon}" alt="">
      <div>
        <span>REVERIE DIRECTORATE // CARTOGRAPHIC DOSSIER</span>
        <h1>{title}</h1>
        <p>{sub}</p>
      </div>
    </section>

    <div class="entity-meta-grid" style="margin: 20px 0;">
      <div class="meta-card">
        <b>SECTOR</b>
        <span>{title}</span>
      </div>
      <div class="meta-card">
        <b>GEOGRAPHICAL ROLE</b>
        <span>{sub}</span>
      </div>
      <div class="meta-card">
        <b>DEFENSIVE GRADE</b>
        <span>Aegis Monitored Zone</span>
      </div>
      <div class="meta-card">
        <b>ERA STATUS</b>
        <span>Active · Dawn Initiative</span>
      </div>
    </div>

    <article class="article-body">
      {body}
    </article>
  </main>

  <aside class="floor-rail" aria-label="Hand of Change departments">
    <h2>HAND OF CHANGE</h2>
    <a class="floor-button f1" href="../departments/floor-1-neutral-command.html" style="--floor:#ef5b55"><span><small>FLOOR 1</small>NEUTRAL</span><img src="../assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt=""></a>
    <a class="floor-button f2" href="../departments/floor-2-maws-keep.html" style="--floor:#6f7ee8"><span><small>FLOOR 2</small>MAW’S KEEP</span><img src="../assets/layout/hand/icons/icon_dept_f2_maws_keep.svg" alt=""></a>
    <a class="floor-button f3" href="../departments/floor-3-extraction-hall.html" style="--floor:#e6c94d"><span><small>FLOOR 3</small>EXTRACTION HALL</span><img src="../assets/layout/hand/icons/icon_dept_f3_extraction.svg" alt=""></a>
    <a class="floor-button f4" href="../departments/floor-4-insight-forge.html" style="--floor:#47c978"><span><small>FLOOR 4</small>INSIGHT FORGE</span><img src="../assets/layout/hand/icons/icon_dept_f4_insight_forge.svg" alt=""></a>
    <a class="floor-button f5" href="../departments/floor-5-border-watch.html" style="--floor:#d7d7d7"><span><small>FLOOR 5</small>BORDER WATCH</span><img src="../assets/layout/hand/icons/icon_dept_f5_border_watch.svg" alt=""></a>
    <a class="floor-button f6" href="../departments/floor-6-deep-vault.html" style="--floor:#8d2e42"><span><small>FLOOR 6</small>DEEP VAULT</span><img src="../assets/layout/hand/icons/icon_dept_f6_deep_vault.svg" alt=""></a>
    <a class="floor-button f7" href="../departments/floor-7-shadow-corps.html" style="--floor:#f0a6c4"><span><small>FLOOR 7</small>SHADOW CORPS</span><img src="../assets/layout/hand/icons/icon_dept_f7_shadow_corps.svg" alt=""></a>
    <a class="floor-button f8" href="../departments/floor-8-gate-watch.html" style="--floor:#f4efa0"><span><small>FLOOR 8</small>GATE WATCH</span><img src="../assets/layout/hand/icons/icon_dept_f8_gate_watch.svg" alt=""></a>
    <a class="rail-action" href="../departments/index.html">OPEN FACILITY DIRECTORY</a>
  </aside>
</div>

<footer>
  <div><b>SOMNARAK WIKI</b><br>Encyclopedia of the City of Unresolved Sorrow</div>
  <div>Current record: Year 4,238 · Dawn Initiative</div>
  <div>The Cycle has ended.<br>Xyan is home and commands Gate Watch.</div>
</footer>
</body>
</html>
"""
    with open(os.path.join(WIKI_DIR, "locations", fname), "w", encoding="utf-8") as f:
        f.write(page_html)

with open(os.path.join(WIKI_DIR, "locations", "index.html"), "w", encoding="utf-8") as f:
    f.write(hub_html)

print("All 8 Location & Atlas pages successfully generated!")
