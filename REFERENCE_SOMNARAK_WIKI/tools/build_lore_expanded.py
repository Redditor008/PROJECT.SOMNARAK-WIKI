import os

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# 1. Somnarak Cosmology
cosmology_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Somnarak Cosmology &amp; The Veil — Somnarak Wiki</title>
  <meta name="description" content="Compendium on Somnarak Cosmology: The Aegis Veil, The Weeping, The 1,778 Cycles, and the Metaphysics of Han.">
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
    <a class="selected" href="index.html">Lore</a>
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
        <a href="index.html" style="color:#fff;font-weight:bold;">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="../locations/index.html">Atlas &amp; Maps</a>
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
      <span>Archival Compendium</span>
      <b>COSMOLOGY &amp; METAPHYSICS // YEAR 4,238</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i><a href="index.html">Lore</a><i>›</i>Somnarak Cosmology
    </div>

    <section class="department-hero" style="--floor:#38bdf8">
      <img src="../assets/icons/banner_lore.svg" alt="">
      <div>
        <span>COSMOLOGICAL ARCHIVE // 夢淵宇宙論</span>
        <h1>Somnarak Cosmology</h1>
        <p>The Physics of Han, The Aegis Barrier, The Weeping Confluence, and the Spire Lattice</p>
      </div>
    </section>

    <div class="entity-meta-grid" style="margin: 20px 0;">
      <div class="meta-card">
        <b>CANONICAL ERA</b>
        <span>Year 4,238 · Dawn Initiative</span>
      </div>
      <div class="meta-card">
        <b>CORE METAPHYSICAL FORCE</b>
        <span>Han (한 — Unresolved Emotional Mass)</span>
      </div>
      <div class="meta-card">
        <b>CONTAINED POPULATION</b>
        <span>1.29 Billion Registered Citizens</span>
      </div>
      <div class="meta-card">
        <b>CENTRAL FOUNDATION</b>
        <span>The Alpha Tree &amp; The Weeping River</span>
      </div>
    </div>

    <article class="article-body">
      <h2>1. The Foundation of Somnarak</h2>
      <p><strong>Somnarak (솜나락)</strong>—known formally in pre-Cycle annals as the <em>City of Unresolved Sorrow</em>—is a monolithic enclosed metropolis situated at the convergence of planetary emotional currents. Built directly around the golden monolithic trunk of the <strong>Alpha Tree</strong> and anchored over the subterranean abyss of the <strong>Weeping</strong>, Somnarak exists as an oasis of structured civilization surrounded by the infinite silent ash expanse of the <strong>Desolate</strong>.</p>
      <p>The city's existence is governed by the physical laws of <strong>Han (한)</strong>—a metaphysical form of energy generated by human suffering, grief, unavenged injustice, and intense emotional memory. Unlike ordinary thermal or kinetic energy, Han permeates matter, altering the density of buildings, crystallizing in water tables, and condensing into sentient or semi-sentient manifestations known as <strong>Sorrow Entities</strong>.</p>

      <h2>2. The Aegis Veil &amp; The Outer Frontier</h2>
      <p>The city is completely encapsulated by the <strong>Aegis Veil (수호막)</strong>—a hemispherical resonance barrier projected by 36 massive generator spires along the Zone E Bulwark. The Veil serves two vital purposes:</p>
      <ul>
        <li><strong>Inward Containment:</strong> Prevents the city's internal ambient Han from dispersing uncontrollably, allowing the Reverie Directorate to harvest and refine the energy for civil power, lighting, and defensive armament.</li>
        <li><strong>Outward Shielding:</strong> Deflects the corrosive, unrefined Han winds of the Desolate, which would otherwise induce instant crystallization or catastrophic psychological Fracture in unprotected citizens.</li>
      </ul>

      <h2>3. The River Weeping &amp; Subterranean Abyssal Hydrology</h2>
      <p>Flowing thousands of meters beneath the foundations of Zone A is <strong>The Weeping (흐느낌의 강)</strong>—a subterranean river comprised of liquid emotional sediment. It is fed by the collective tears, memory runoff, and dissolved physical remains of the city's dead across 1,778 historical Cycles. The Weeping is channeled into Floor 2 (Maw's Keep) and Floor 3 (Extraction Hall), where specialized filtration turbines separate raw sorrow into usable power cells and weave-grade filaments.</p>

      <h2>4. The Spire &amp; Urban Zonal Hierarchy</h2>
      <p>Somnarak is organized into five concentric zones, with authority and defensive density radiating outward from the Central Spire in Zone A to the perimeter bastions of Zone E:</p>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr><th>Zone</th><th>Sector Name</th><th>Primary Function &amp; Metaphysical Balance</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Zone A</strong></td><td>Core Nexus</td><td>Executive seat of the Reverie Directorate, High Council Senate, Central Command.</td></tr>
            <tr><td><strong>Zone B</strong></td><td>West Ward</td><td>High-density residential towers, historic Old Lament district, civil education.</td></tr>
            <tr><td><strong>Zone C</strong></td><td>Collector's Row</td><td>Commercial bazaars, Scavenger Enclaves, debt arbitration courts, artisan markets.</td></tr>
            <tr><td><strong>Zone D</strong></td><td>Forge &amp; Gardens</td><td>Alpha Tree arboretums, M.A.W. armories, Insight Forge research facilities.</td></tr>
            <tr><td><strong>Zone E</strong></td><td>Perimeter Bulwark</td><td>Aegis Barrier projectors, heavy artillery bastions, Gate Watch security garrisons.</td></tr>
          </tbody>
        </table>
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
with open(os.path.join(WIKI_DIR, "lore", "somnarak-cosmology.html"), "w", encoding="utf-8") as f:
    f.write(cosmology_html)

# 2. The Three Sorrows
three_sorrows_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>The Three Sorrows (Lament, Grudge, Weight) — Somnarak Wiki</title>
  <meta name="description" content="Treatise on the Metaphysical Triad of Han: Lament (슬픔), Grudge (한), and Weight (무게).">
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
    <a class="selected" href="index.html">Lore</a>
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
        <a href="index.html" style="color:#fff;font-weight:bold;">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="../locations/index.html">Atlas &amp; Maps</a>
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
      <span>Archival Compendium</span>
      <b>METAPHYSICAL TRIAD // 三大悲哀</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i><a href="index.html">Lore</a><i>›</i>The Three Sorrows
    </div>

    <section class="department-hero" style="--floor:#ef5b55">
      <img src="../assets/icons/banner_lament.svg" alt="">
      <div>
        <span>THEORETICAL HAN PHYSICS // 悲·恨·重</span>
        <h1>The Three Sorrows</h1>
        <p>Lament (슬픔), Grudge (한), and Weight (무게) — The Metaphysical Trinity of Somnarak</p>
      </div>
    </section>

    <div class="entity-meta-grid" style="margin: 20px 0;">
      <div class="meta-card">
        <b>PRIMARY TRIAD</b>
        <span>Lament (슬픔) · Grudge (한) · Weight (무게)</span>
      </div>
      <div class="meta-card">
        <b>DAMAGE CORRELATIONS</b>
        <span>Ferrehan (Mental) · Pugnahan (Physical) · Viderehan (True)</span>
      </div>
      <div class="meta-card">
        <b>HARMONIC STATE</b>
        <span>Absolvohan (Resolution of the Triad)</span>
      </div>
      <div class="meta-card">
        <b>RESEARCH SECTOR</b>
        <span>Floor 4: Insight Forge (Lead: Ayshuk)</span>
      </div>
    </div>

    <article class="article-body">
      <h2>1. The Metaphysical Trinity</h2>
      <p>All psychic, metaphysical, and kinetic phenomena in the universe of Somnarak originate from the <strong>Three Primary Sorrows (三大悲哀 — Samdae Biae)</strong>. Identified during the earliest recorded observations of the Alpha Tree, this triad represents the fundamental spectrum of human grief when exposed to the high-density emotional pressure of the world.</p>

      <h2>2. Detailed Breakdown of the Three Pillars</h2>

      <h3>I. Lament (슬픔 — Seulpeum) · The Sorrow of Loss</h3>
      <p><strong>Definition:</strong> The passive, resonant sorrow produced by separation, bereavement, fading memories, and the quiet acceptance of death. Lament is fluid and pervasive, moving like water through urban drainage channels and infiltrating living minds as melancholy or apathy.</p>
      <ul>
        <li><strong>Color Alignment:</strong> Deep Cyan &amp; Azure (`#38bdf8` / `#4a90d9`)</li>
        <li><strong>Associated Damage Type:</strong> <strong>Ferrehan (Mental / Coherence Drain)</strong></li>
        <li><strong>Representative Manifestations:</strong> SE-001 (The Orphaned Bell), SE-005 (The Smothering Mother), SE-011 (The Whispering Walls).</li>
      </ul>

      <h3>II. Grudge (한 — Han) · The Sorrow of Injustice</h3>
      <p><strong>Definition:</strong> The active, volatile sorrow born of unavenged betrayal, systemic oppression, violent denial, and burning spite. Unlike Lament, Grudge does not weep; it ignites, fracturing physical matter, generating kinetic shockwaves, and driving victims into berserk frenzy.</p>
      <ul>
        <li><strong>Color Alignment:</strong> Crimson &amp; Rust Red (`#ef5b55` / `#8d2e42`)</li>
        <li><strong>Associated Damage Type:</strong> <strong>Pugnahan (Physical Trauma / Bleed &amp; Rupture)</strong></li>
        <li><strong>Representative Manifestations:</strong> SE-003 (The Wilderness Tide), SE-009 (The Memory Weaver), SE-014 (The Debt Eater).</li>
      </ul>

      <h3>III. Weight (무게 — Muge) · The Sorrow of History</h3>
      <p><strong>Definition:</strong> The accumulated, immovable mass of unatoned historical sin, endless debt, societal burden, and the crushing momentum of the 1,778 Cycles. Weight exerts literal gravitational and compressive force upon physical bodies and architecture.</p>
      <ul>
        <li><strong>Color Alignment:</strong> Heavy Amber &amp; Obsidian (`#e6c94d` / `#181e2b`)</li>
        <li><strong>Associated Damage Type:</strong> <strong>Flerehan &amp; Viderehan (Composite Break / Absolute Structural Crush)</strong></li>
        <li><strong>Representative Manifestations:</strong> SE-002 (The Grieving Colossus), SE-010 (The Convergence), SE-015 (The Debt Scale).</li>
      </ul>

      <h2>3. The Triad in Tactical Combat</h2>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr><th>Sorrow Type</th><th>Affinity Advantage</th><th>Vulnerability</th><th>Resonance Effect</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Lament</strong></td><td>Eats Mental Composure; bypasses physical armor</td><td>Vulnerable to high-impact Grudge strikes</td><td>Induces Apathy &amp; Panic</td></tr>
            <tr><td><strong>Grudge</strong></td><td>Shatters physical barricades &amp; shields</td><td>Vulnerable to gravitational Weight suppression</td><td>Induces Bleed &amp; Berserk</td></tr>
            <tr><td><strong>Weight</strong></td><td>Staggers and immobilizes enemy squads</td><td>Vulnerable to piercing Lament resonance</td><td>Induces Stagger &amp; Absolute Crush</td></tr>
          </tbody>
        </table>
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
with open(os.path.join(WIKI_DIR, "lore", "the-three-sorrows.html"), "w", encoding="utf-8") as f:
    f.write(three_sorrows_html)

# 3. The Cycle and Absolvohan
cycle_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>The 1,778 Cycles &amp; Absolvohan — Somnarak Wiki</title>
  <meta name="description" content="Comprehensive chronicle of the 1,778 Historical Loops of Somnarak, the Absolvohan Revelation, and the Dawn Initiative.">
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
    <a class="selected" href="index.html">Lore</a>
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
        <a href="index.html" style="color:#fff;font-weight:bold;">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="../locations/index.html">Atlas &amp; Maps</a>
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
      <span>Archival Compendium</span>
      <b>TEMPORAL RECURRENCE // 循環與解恨</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i><a href="index.html">Lore</a><i>›</i>The 1,778 Cycles &amp; Absolvohan
    </div>

    <section class="department-hero" style="--floor:#8d2e42">
      <img src="../assets/icons/banner_timeline.svg" alt="">
      <div>
        <span>HISTORICAL RECURRENCE RECORD // 1,778 循環</span>
        <h1>The 1,778 Cycles &amp; Absolvohan</h1>
        <p>The Temporal Loop of Agony, The Nine Sacrifices, and the Dawn Initiative Breakthrough</p>
      </div>
    </section>

    <div class="entity-meta-grid" style="margin: 20px 0;">
      <div class="meta-card">
        <b>TOTAL RECORDED LOOPS</b>
        <span>1,778 Complete Recurrences</span>
      </div>
      <div class="meta-card">
        <b>FINAL RITUAL</b>
        <span>Absolvohan (해한 — Unraveling of the Knot)</span>
      </div>
      <div class="meta-card">
        <b>CURRENT STATUS</b>
        <span>Cycle Broken · Linear Time Restored</span>
      </div>
      <div class="meta-card">
        <b>PRESENT ERA</b>
        <span>Year 4,238 · Dawn Initiative</span>
      </div>
    </div>

    <article class="article-body">
      <h2>1. The Architecture of the 1,778 Cycles</h2>
      <p>For millennia, Somnarak was trapped within a self-contained metaphysical loop known as <strong>The Cycle (循環 — Sungwhan)</strong>. Spanning exactly fifty standard calendar days per iteration, each Cycle concluded with the catastrophic overflow of the city's accumulative Han, triggering a complete wipe of urban memory, the resurrection and recalibration of the Nine Echo-Cores, and the resetting of the city's 1.29 billion inhabitants.</p>
      <p>A total of <strong>1,778 Cycles</strong> were executed under the supervision of Director Majin and Archive Lead Marjuk (Floor 6). While ordinary citizens woke with their memories wiped clean by ambient Ferrehan discharges, the Nine Leads accumulated micro-resonant scars across each reset, gradually piecing together the cryptographic solution required to shatter the loop.</p>

      <h2>2. The Absolvohan Revelation (Parts 1–9)</h2>
      <p><strong>Absolvohan (해한 — 解恨)</strong> represents the supreme metaphysical doctrine formulated across the final nine Cycles. Rather than seeking to suppress, incinerate, or escape human sorrow, Absolvohan dictates that <em>Han can only be resolved through absolute recognition, bearing witness, and preservation of the unavenged name</em>.</p>
      <p>Across the nine canonical trials of Absolvohan, each Echo-Core Lead confronted their primordial trauma within the Root Chamber of the Alpha Tree:</p>
      <ul>
        <li><strong>Part 1 (Dekan):</strong> Forged the Iron Will of Maw's Keep by acknowledging that physical restraint without compassion is mere brutality.</li>
        <li><strong>Part 2 (Zyrak):</strong> Synthesized the true Needle Resonance, accepting that weaving sorrow is an act of preservation, not exploitation.</li>
        <li><strong>Part 3 (Ayshuk):</strong> Unlocked the Insight of Taboos, establishing that forbidden knowledge must be understood to prevent future catastrophe.</li>
        <li><strong>Part 4 (Mellda):</strong> Anchored the Border Aegis, recognizing that true defense protects the wanderer as well as the citizen.</li>
        <li><strong>Part 5 (Marjuk):</strong> Unsealed the Unwritten Scrolls of Floor 6, guaranteeing that no sacrifice across the 1,778 loops would be forgotten.</li>
        <li><strong>Part 6 (Ishall):</strong> Emerged from the Underworld Shadows, bridging the rift between the Frays and Directorate authority.</li>
        <li><strong>Part 7 (Xyan):</strong> Commanded the Gate Watch, returning physically from the Desolate to reclaim his rightful place among the Leads.</li>
        <li><strong>Part 8 (Seiyon):</strong> Discharged the Administrative Grief of Floor 1, reconciling the bureaucratic machinery with living empathy.</li>
        <li><strong>Part 9 (Majin):</strong> Executed the Final Unknotting, dissolving the temporal loop and initiating the Dawn of Year 4,238.</li>
      </ul>

      <h2>3. The Dawn Initiative Mandate</h2>
      <p>With the Cycle historically concluded, Somnarak now operates under linear time. The Reverie Directorate has pivoted from endless repetition to active forward progress: containment is now protection, extraction is a solemn craft, research is empathy, and every route outward is incomplete without a route home.</p>
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
with open(os.path.join(WIKI_DIR, "lore", "the-cycle-and-absolvohan.html"), "w", encoding="utf-8") as f:
    f.write(cycle_html)

# 4. The Alpha Tree
tree_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>The Alpha Tree (Root Core of Somnarak) — Somnarak Wiki</title>
  <meta name="description" content="Archival treatise on the Alpha Tree: The crystalline biological monument anchoring Somnarak, its mycelium root network, and Han conduction.">
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
    <a class="selected" href="index.html">Lore</a>
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
        <a href="index.html" style="color:#fff;font-weight:bold;">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="../locations/index.html">Atlas &amp; Maps</a>
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
      <span>Archival Compendium</span>
      <b>BIOLOGICAL MONUMENT // 根源巨木</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i><a href="index.html">Lore</a><i>›</i>The Alpha Tree
    </div>

    <section class="department-hero" style="--floor:#e6c94d">
      <img src="../assets/icons/banner_hope.svg" alt="">
      <div>
        <span>CENTRAL MONUMENT // 알파 나무 · THE ROOT CORE</span>
        <h1>The Alpha Tree (알파 나무)</h1>
        <p>The Monolithic Golden Tree, Subterranean Han Conduction, and the Mycelium of Zone D</p>
      </div>
    </section>

    <div class="entity-meta-grid" style="margin: 20px 0;">
      <div class="meta-card">
        <b>LOCATION</b>
        <span>Zone A / Subterranean Nexus</span>
      </div>
      <div class="meta-card">
        <b>CANOPY HEIGHT</b>
        <span>1,850 Meters (Pierces Spire Vault)</span>
      </div>
      <div class="meta-card">
        <b>ROOT SPREAD</b>
        <span>Encompasses all Zones A through E</span>
      </div>
      <div class="meta-card">
        <b>PRIMARY RESOURCE</b>
        <span>Alpha Sap · Refined Dawn Resonance</span>
      </div>
    </div>

    <article class="article-body">
      <h2>1. Biological &amp; Energetic Core</h2>
      <p>The <strong>Alpha Tree (알파 나무)</strong> is the titanic bio-crystalline organism around which the entirety of Somnarak is constructed. Rising from the subterranean abyss of the Weeping to pierce the upper cloud vault of the Central Spire, the Tree functions as the primary metaphysical conduit of the city, absorbing raw, unstable Han from the earth and transmuting it into stabilized golden sap.</p>

      <h2>2. The Root Lattice &amp; Subterranean Mycelium</h2>
      <p>The Tree's root network extends outward in a vast web beneath all five urban zones. In Zone D (Forge &amp; Gardens), these roots breach the surface in bioluminescent arboretums maintained by the Weavers Guild. The roots act as living lightning rods, absorbing sudden surges of emotional pressure from the population and preventing spontaneous sorrow eruptions.</p>

      <h2>3. The Alpha Sap &amp; Dawn Resonance</h2>
      <p>Refined by Extraction Hall (Floor 3), the luminous resin secreted by the Tree's canopy is utilized to forge highest-grade WAW and ALEPH M.A.W. armors. In the Dawn Initiative, Alpha Sap forms the core catalyst for the Shield of Dawn network, providing permanent stabilization against Desolate encroachment.</p>
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
with open(os.path.join(WIKI_DIR, "lore", "the-alpha-tree.html"), "w", encoding="utf-8") as f:
    f.write(tree_html)

# 5. The Cheongula Incident
cheongula_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>The Cheongula Incident (Year 3,892) — Somnarak Wiki</title>
  <meta name="description" content="Historical catastrophe report on the Cheongula Incident: The Sector B Veil Rupture, Three Birds breach, and modern containment reforms.">
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
    <a class="selected" href="index.html">Lore</a>
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
        <a href="index.html" style="color:#fff;font-weight:bold;">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="../locations/index.html">Atlas &amp; Maps</a>
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
      <span>Historical Incident Report</span>
      <b>CATASTROPHIC BREACH // 靑窟事變</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i><a href="index.html">Lore</a><i>›</i>The Cheongula Incident
    </div>

    <section class="department-hero" style="--floor:#ef5b55">
      <img src="../assets/icons/banner_grudge.svg" alt="">
      <div>
        <span>YEAR 3,892 CATASTROPHE // 靑窟 · CHEONGULA</span>
        <h1>The Cheongula Incident</h1>
        <p>The Sector B Barrier Collapse, Emergence of The Convergence, and the Modern Work Type Protocol</p>
      </div>
    </section>

    <div class="entity-meta-grid" style="margin: 20px 0;">
      <div class="meta-card">
        <b>DATE OF INCIDENT</b>
        <span>Year 3,892 · Cycle 1,440</span>
      </div>
      <div class="meta-card">
        <b>LOCATION</b>
        <span>Zone B / Sector B-02 Library Corridor</span>
      </div>
      <div class="meta-card">
        <b>CASUALTIES</b>
        <span>14,200 Citizens Fractured · 8 Squads Lost</span>
      </div>
      <div class="meta-card">
        <b>OUTCOME</b>
        <span>Establishment of the Four Work Types</span>
      </div>
    </div>

    <article class="article-body">
      <h2>1. The Breach at Sector B</h2>
      <p>In Year 3,892, during the 1,440th Cycle, an unprecedented resonance harmonic destabilized the secondary Aegis generator in Zone B. Termed <strong>The Cheongula Incident (靑窟事變)</strong>, the event opened a catastrophic sub-spatial fracture directly into the underground caverns beneath the Library of Stolen Pasts.</p>
      <p>Raw, unrefined Han flooded the residential avenues, triggering simultaneous breaches of three high-risk Sorrow Entities: SE-001 (The Orphaned Bell), SE-009 (The Memory Weaver), and the dormant core of SE-010 (The Convergence).</p>

      <h2>2. The Three Birds &amp; The Convergence</h2>
      <p>As the grief of thousands merged within the breach zone, the three entities fused into the apocalyptic ALEPH manifestation known as <em>The Convergence</em>. Emitting absolute Weight and Lament resonance, the entity collapsed twelve city blocks into pure crystal ash within twenty minutes.</p>
      <p>Director Majin, Containment Lead Dekan, and Archive Lead Marjuk executed emergency containment protocol 'Iron Shroud', manually severing the district's power grid and personally holding the line until the High Architects could seal the breach with high-density basalt barricades.</p>

      <h2>3. The Legacy: Modern Containment Doctrine</h2>
      <p>The lessons of the Cheongula catastrophe completely restructured the Reverie Directorate. The obsolete "Brute Suppression" model was permanently abolished, replaced by the scientific <strong>Four Work Types</strong> (Instinct, Insight, Attachment, Repression) and the establishment of dedicated psychological therapy units across all facility floors.</p>
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
with open(os.path.join(WIKI_DIR, "lore", "the-cheongula-incident.html"), "w", encoding="utf-8") as f:
    f.write(cheongula_html)

# 6. Lore Hub Index (lore/index.html)
lore_hub_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Lore &amp; Cosmology Compendium — Somnarak Wiki</title>
  <meta name="description" content="Master Compendium of Somnarak World Lore: Cosmology, The Three Sorrows, The 1,778 Cycles, The Alpha Tree, and Historic Incidents.">
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
    <a class="selected" href="index.html">Lore</a>
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
        <a href="index.html" style="color:#fff;font-weight:bold;">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="../locations/index.html">Atlas &amp; Maps</a>
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
      <span>Master Compendium</span>
      <b>COSMOLOGY &amp; HISTORY // YEAR 4,238</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i>Lore
    </div>

    <section class="department-hero" style="--floor:#38bdf8">
      <img src="../assets/icons/banner_lore.svg" alt="">
      <div>
        <span>REVERIE DIRECTORATE // CENTRAL ARCHIVES</span>
        <h1>Lore &amp; Cosmology</h1>
        <p>Cosmological Structure, The Three Sorrows, The 1,778 Cycles, and Historical Incidents</p>
      </div>
    </section>

    <article class="article-body">
      <h2>Canonical Archival Treatises</h2>
      <p>Explore the primary treatises governing the metaphysics, history, and physics of Somnarak:</p>

      <div class="archive-portal-grid">
        <a class="archive-portal" href="somnarak-cosmology.html" style="--portal:#38bdf8">
          <span>WORLD SYSTEM</span>
          <img src="../assets/icons/city.svg" alt="">
          <b>SOMNARAK COSMOLOGY</b>
          <small>The Spire, The Veil, &amp; The Weeping</small>
        </a>

        <a class="archive-portal" href="the-three-sorrows.html" style="--portal:#ef5b55">
          <span>METAPHYSICAL TRIAD</span>
          <img src="../assets/icons/banner_lament.svg" alt="">
          <b>THE THREE SORROWS</b>
          <small>Lament, Grudge, and Weight</small>
        </a>

        <a class="archive-portal" href="the-cycle-and-absolvohan.html" style="--portal:#8d2e42">
          <span>TEMPORAL LOOP</span>
          <img src="../assets/icons/banner_timeline.svg" alt="">
          <b>1,778 CYCLES &amp; ABSOLVOHAN</b>
          <small>The Loop &amp; Dawn Initiative</small>
        </a>

        <a class="archive-portal" href="the-alpha-tree.html" style="--portal:#e6c94d">
          <span>ROOT MONUMENT</span>
          <img src="../assets/icons/banner_hope.svg" alt="">
          <b>THE ALPHA TREE</b>
          <small>Core Conduit &amp; Zone D Mycelium</small>
        </a>

        <a class="archive-portal" href="the-cheongula-incident.html" style="--portal:#f4efa0">
          <span>HISTORICAL DISASTER</span>
          <img src="../assets/icons/banner_grudge.svg" alt="">
          <b>CHEONGULA INCIDENT</b>
          <small>Year 3,892 Breach &amp; Reforms</small>
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
with open(os.path.join(WIKI_DIR, "lore", "index.html"), "w", encoding="utf-8") as f:
    f.write(lore_hub_html)

print("All 6 Lore compendiums successfully generated!")
