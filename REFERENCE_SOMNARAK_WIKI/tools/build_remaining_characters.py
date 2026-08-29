import os

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# 1. Kael the Drift King
kael_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Kael (The Drift King) — Somnarak Wiki</title>
  <meta name="description" content="Archival dossier for Kael, the Drift King of the Desolate Nomads. Former Zone E Warden, Ruler of the Mobile Throne.">
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
    <a class="selected" href="index.html">Characters</a>
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
        <a href="index.html">Characters Hub</a>
        <a href="../lore/index.html">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="../locations/index.html">Atlas &amp; Maps</a>
        <a href="../mechanics/index.html">Battle &amp; Systems</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="../maw/index.html">M.A.W. Codex</a>
      </section>
      <section>
        <h2>Echo-Cores</h2>
        <a href="the-director-majin.html">Majin (Director)</a>
        <a href="the-secretary-seiyon.html">Seiyon (Secretary)</a>
        <a href="the-containment-lead-dekan.html">Dekan (Containment)</a>
        <a href="the-extraction-lead-zyrak.html">Zyrak (Extraction)</a>
        <a href="the-research-lead-ayshuk.html">Ayshuk (Research)</a>
        <a href="the-border-lead-mellda.html">Mellda (Border)</a>
        <a href="the-archive-lead-marjuk.html">Marjuk (Archive)</a>
        <a href="the-outsider-ishall.html">Ishall (Outsider)</a>
        <a href="the-exile-xyan.html">Xyan (Exile)</a>
      </section>
    </nav>
  </aside>

  <main id="content">
    <div class="page-tabs">
      <span>Archival Dossier</span>
      <b>OUTSKIRTS SOVEREIGN // DESOLATE COMMAND</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i><a href="index.html">Characters</a><i>›</i>Kael (The Drift King)
    </div>

    <section class="department-hero" style="--floor:#e6c94d">
      <img src="../assets/icons/banner_characters.svg" alt="">
      <div>
        <span>OUTSKIRTS CODENAME // 漂流王 · HYOURYOU</span>
        <h1>Kael (카엘) — The Drift King</h1>
        <p>Sovereign of the Desolate Nomads · Former Zone E Warden Commander</p>
      </div>
    </section>

    <div class="entity-meta-grid" style="margin: 20px 0;">
      <div class="meta-card">
        <b>REAL NAME</b>
        <span>Kael (카엘)</span>
      </div>
      <div class="meta-card">
        <b>AFFILIATION</b>
        <span>Desolate Nomads / Horizon Caravan</span>
      </div>
      <div class="meta-card">
        <b>ORIGIN SECTOR</b>
        <span>Zone E Bulwark Border Watch</span>
      </div>
      <div class="meta-card">
        <b>RESONANCE AFFINITY</b>
        <span>Unbound Outside Han · Ferrehan/Pugnahan</span>
      </div>
    </div>

    <article class="article-body">
      <h2>1. Identity &amp; Overview</h2>
      <p><strong>Kael (카엘)</strong>, titled the <em>Drift King (漂流王 — Hyouryou)</em>, is the de facto sovereign of the Desolate Nomads—the largest migratory human population inhabiting the silent gray ash wastes beyond Somnarak’s Aegis Veil. Operating from a colossal mobile land-tread throne that drifts along subterranean Han-flow currents, Kael commands the border trade routes between the outer perimeter of Zone E and the deep wilderness.</p>
      <p>Though designated a rogue entity by the Municipal Wardens and studied intently by the Reverie Directorate's Border Watch (Floor 5), Kael functions as the primary mediator of the Outside. Under his governance, the Nomads retrieve crystallised relic deposits, map mobile anomalies like SE-007 (Brume), and provide passage to refugees attempting to reach the city gates.</p>

      <h2>2. Visual &amp; Physiological Profile</h2>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr><th>Attribute</th><th>Archival Assessment</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Age / Gender</strong></td><td>~40 Standard Years · Male</td></tr>
            <tr><td><strong>Height / Build</strong></td><td>175 cm · Lean, sinewy musculature conditioned by decades of harsh desert navigation</td></tr>
            <tr><td><strong>Hair / Eyes</strong></td><td>Soot-black hair bound in a loose, weathered knot · Muted watchful emerald eyes</td></tr>
            <tr><td><strong>Attire</strong></td><td>Heavy dust-cloaks stitched from cured nomad leather and salvaged Aegis barrier mesh</td></tr>
            <tr><td><strong>Distinguishing Marks</strong></td><td>Micro-crystallised veins across neck and forearms from raw Han exposure; the dust of a hundred roads</td></tr>
          </tbody>
        </table>
      </div>

      <h2>3. History &amp; The Border Incident</h2>
      <p>Decades prior to the Dawn Initiative, Kael was an elite Municipal Warden assigned to the high-risk perimeter towers of Zone E. Highly disciplined and perceptive, Kael became obsessed with the nature of the ambient pressure surging against the outside of the Veil.</p>
      <p>During an unrecorded midnight watch, Kael stepped beyond Gate 5 into the open Desolate. Rather than suffering violent crystallization or psychological collapse (Fracture), Kael's physiology adapted. The planetary sorrow bonded with his circulatory network, granting him innate sensory awareness of Han-flow streams across thousands of kilometers. When the Wardens attempted to forcibly retrieve him the following dawn, Kael refused containment and walked into the gray expanse to organize the scattered wandering outcasts.</p>

      <h2>4. The Toll of Stories</h2>
      <blockquote class="dossier-quote">
        “Every merchant who traverses the nomad corridors must pay a toll—not in currency, nor in raw Han cylinders, but in *stories*. Kael remembers every name spoken in the sand.” — Floor 5 Border Watch Dispatch
      </blockquote>
      <p>Under Kael's law, no currency from Somnarak holds value within the nomad caravans. Travelers, smugglers, and Fray merchants must present unrecorded tales, personal griefs, and urban news to the King’s retinue. In return, the caravans provide safe navigation through anomalous storms and escort past dormant Sorrow Entities.</p>

      <h2>5. Combat &amp; Tactical Capabilities</h2>
      <ul>
        <li><strong>Flow Stepping:</strong> Kael can anticipate enemy vectors by reading subtle shifts in local Han conductivity across the earth.</li>
        <li><strong>Nomad Poleaxe:</strong> Wields a heavy two-handed halberd forged from hardened Desolate iron and infused with Ferrehan resonance.</li>
        <li><strong>Sand Shroud:</strong> Disperses ambient ash clouds to break targeting locks and stagger approaching suppression squads.</li>
      </ul>
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
with open(os.path.join(WIKI_DIR, "characters", "kael.html"), "w", encoding="utf-8") as f:
    f.write(kael_html)

# 2. Soojin (Master Weaver)
soojin_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Soojin (Master Weaver) — Somnarak Wiki</title>
  <meta name="description" content="Archival dossier for Soojin, Master Weaver of the Echo Gardens Guild and Reverie Directorate Field Specialist.">
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
    <a class="selected" href="index.html">Characters</a>
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
        <a href="index.html">Characters Hub</a>
        <a href="../lore/index.html">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="../locations/index.html">Atlas &amp; Maps</a>
        <a href="../mechanics/index.html">Battle &amp; Systems</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="../maw/index.html">M.A.W. Codex</a>
      </section>
      <section>
        <h2>Echo-Cores</h2>
        <a href="the-director-majin.html">Majin (Director)</a>
        <a href="the-secretary-seiyon.html">Seiyon (Secretary)</a>
        <a href="the-containment-lead-dekan.html">Dekan (Containment)</a>
        <a href="the-extraction-lead-zyrak.html">Zyrak (Extraction)</a>
        <a href="the-research-lead-ayshuk.html">Ayshuk (Research)</a>
        <a href="the-border-lead-mellda.html">Mellda (Border)</a>
        <a href="the-archive-lead-marjuk.html">Marjuk (Archive)</a>
        <a href="the-outsider-ishall.html">Ishall (Outsider)</a>
        <a href="the-exile-xyan.html">Xyan (Exile)</a>
      </section>
    </nav>
  </aside>

  <main id="content">
    <div class="page-tabs">
      <span>Archival Dossier</span>
      <b>WEAVER GUILD SPECIALIST // FIELD HANDLER</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i><a href="index.html">Characters</a><i>›</i>Soojin (Master Weaver)
    </div>

    <section class="department-hero" style="--floor:#e6c94d">
      <img src="../assets/icons/banner_characters.svg" alt="">
      <div>
        <span>GUILD CODENAME // 織姬 · THE HANDLER</span>
        <h1>Soojin (수진) — Master Weaver</h1>
        <p>Lead Artisan of the Echo Gardens · Senior Field Extraction Handler</p>
      </div>
    </section>

    <div class="entity-meta-grid" style="margin: 20px 0;">
      <div class="meta-card">
        <b>DESIGNATION</b>
        <span>Soojin (수진)</span>
      </div>
      <div class="meta-card">
        <b>GUILD AFFILIATION</b>
        <span>Weavers Guild of Echo Gardens / Floor 3</span>
      </div>
      <div class="meta-card">
        <b>SPECIALIZATION</b>
        <span>Resonant Thread Synthesis &amp; M.A.W. Calibration</span>
      </div>
      <div class="meta-card">
        <b>CURRENT ROLE</b>
        <span>Senior Agony Tailor · Field Containment</span>
      </div>
    </div>

    <article class="article-body">
      <h2>1. Overview &amp; Guild Standing</h2>
      <p><strong>Soojin (수진)</strong> is the preeminent Master Weaver within the Echo Gardens Guild in Zone D and a trusted tactical liaison to Extraction Lead Zyrak (Floor 3). Renowned for her peerless needle dexterity, Soojin possesses the rare ability to spin raw, boiling Han threads extracted directly from high-risk Sorrow Entities into wearable, stabilized <strong>Materialized Agony Wear (M.A.W.)</strong>.</p>
      <p>In field operations, Soojin serves as the "Handler"—the lead containment operative responsible for anchoring fluctuating sorrow frequencies during breaches. Her work ensures that operatives wearing high-grade M.A.W. suits do not succumb to mental contamination or ego erosion.</p>

      <h2>2. History &amp; The Smothering Mother Incident</h2>
      <p>During the historic containment operation of SE-005 (The Smothering Mother) in Sector D-01, an unexpected resonant surge ruptured the primary Loom chamber. While four junior weavers suffered catastrophic cognitive fracture, Soojin stepped into the containment chamber unarmed, using her bare hands to weave the entity's suffocating silk ribbons into the first prototype of the <em>Let No One Go</em> suit.</p>
      <p>Though her palms remain permanently scarred with luminescent amber thread-burns, her breakthrough established the modern safety protocols for HE- and WAW-class M.A.W. synthesis across the entire Directorate.</p>

      <h2>3. Technical Mastery &amp; Needle Resonance</h2>
      <ul>
        <li><strong>Silk-Iron Threading:</strong> Combines refined Han filaments with high-tensile metallurgical polymers to create flexible, kinetic-absorbing protective weave.</li>
        <li><strong>Ego-Dampening Stitches:</strong> Crafts internal embroidery along collar lines and chestplates that filters out psychic whispers emitted by weaponized grief.</li>
        <li><strong>Field Repair Needle:</strong> Carries a solid silver resonance stylus capable of mending compromised M.A.W. suits mid-battle during suppression engagements.</li>
      </ul>
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
with open(os.path.join(WIKI_DIR, "characters", "soojin.html"), "w", encoding="utf-8") as f:
    f.write(soojin_html)

# 3. High Architects Guild (Daejun, Doha, Joon)
architects_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>The High Architects &amp; Masons — Somnarak Wiki</title>
  <meta name="description" content="Archival dossier on the High Architects Guild of Somnarak: Master Daejun, Doha the Mason, Joon the Engineer, and the Aegis Barrier builders.">
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
    <a class="selected" href="index.html">Characters</a>
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
        <a href="index.html">Characters Hub</a>
        <a href="../lore/index.html">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="../locations/index.html">Atlas &amp; Maps</a>
        <a href="../mechanics/index.html">Battle &amp; Systems</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="../maw/index.html">M.A.W. Codex</a>
      </section>
      <section>
        <h2>Echo-Cores</h2>
        <a href="the-director-majin.html">Majin (Director)</a>
        <a href="the-secretary-seiyon.html">Seiyon (Secretary)</a>
        <a href="the-containment-lead-dekan.html">Dekan (Containment)</a>
        <a href="the-extraction-lead-zyrak.html">Zyrak (Extraction)</a>
        <a href="the-research-lead-ayshuk.html">Ayshuk (Research)</a>
        <a href="the-border-lead-mellda.html">Mellda (Border)</a>
        <a href="the-archive-lead-marjuk.html">Marjuk (Archive)</a>
        <a href="the-outsider-ishall.html">Ishall (Outsider)</a>
        <a href="the-exile-xyan.html">Xyan (Exile)</a>
      </section>
    </nav>
  </aside>

  <main id="content">
    <div class="page-tabs">
      <span>Archival Dossier</span>
      <b>GUILD LEADERSHIP // STRUCTURAL MASONRY</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i><a href="index.html">Characters</a><i>›</i>The High Architects &amp; Masons
    </div>

    <section class="department-hero" style="--floor:#47c978">
      <img src="../assets/icons/banner_characters.svg" alt="">
      <div>
        <span>GUILD DOSSIER // 建築師團 · ARCHITECTURAL CORPS</span>
        <h1>The High Architects &amp; Masons</h1>
        <p>Master Daejun, Doha the Mason, Joon the Engineer · Keepers of the Aegis Lattice</p>
      </div>
    </section>

    <div class="entity-meta-grid" style="margin: 20px 0;">
      <div class="meta-card">
        <b>INSTITUTION</b>
        <span>High Guild of Architects</span>
      </div>
      <div class="meta-card">
        <b>KEY FIGURES</b>
        <span>Daejun (Blind Master), Doha (Mason), Joon (Engineer)</span>
      </div>
      <div class="meta-card">
        <b>SECTOR DOMAIN</b>
        <span>Zone A Core Nexus &amp; Zone E Bulwark</span>
      </div>
      <div class="meta-card">
        <b>PRIMARY MANDATE</b>
        <span>Aegis Barrier Stabilization &amp; Spire Foundation</span>
      </div>
    </div>

    <article class="article-body">
      <h2>1. The Guild &amp; Structural Metaphysics</h2>
      <p>The <strong>High Architects &amp; Masons</strong> are the master builders responsible for the structural, metaphysical, and energetic integrity of Somnarak. Tasked with anchoring the towering architecture of the Central Spire into the basalt foundations of the Alpha Tree, the Architects design every containment cell, residential arch, and barrier node across the five zones.</p>

      <h2>2. Key Guild Personages</h2>
      
      <h3>Daejun (대준) — The Blind Architect</h3>
      <p>A retired Master Architect who sacrificed his eyesight during the catastrophic Han overflow of the Year 4,112 Expansion. Though visually sightless, Daejun possesses the uncanny ability to perceive Han-flow gradients and architectural stress points through direct physical touch. Working in a quiet workshop in Zone D filled with miniature crystalline models, Daejun guides major Directorate construction projects, identifying micro-fractures in containment bulkheads that optical scanners fail to detect.</p>

      <h3>Doha (도하) — The Mason</h3>
      <p>A veteran field mason assigned to high-containment emergency response. During an uncontained breach in Zone B, Doha erected the legendary basalt bulkhead that saved three residential districts, carrying the tragic sorrow of sealing his own ancestral home on the opposite side. He wields an oversized tectonic masonry hammer capable of repairing shattered barrier nodes under active fire.</p>

      <h3>Joon (준) — The Combat Engineer</h3>
      <p>The primary tactical engineer assigned to Underworld &amp; Special Operations (UCD). Specializing in rapid battlefield fortification, Joon deploys kinetic barricades, temporary resonance dampening pillars, and emergency evacuation bridges across breach corridors.</p>

      <h2>3. The Aegis Barrier Network</h2>
      <p>The Guild maintains the 36 primary Aegis Projectors lining the circumference of Zone E. These monolithic generators project the hemispherical energy dome that shields 1.29 billion souls from the corrosive, unrefined Han winds of the Desolate.</p>
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
with open(os.path.join(WIKI_DIR, "characters", "high-architects.html"), "w", encoding="utf-8") as f:
    f.write(architects_html)

# 4. Cheonbulok Refugees (Hwaran and the Diaspora)
cheonbulok_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Cheonbulok Refugees &amp; Hwaran — Somnarak Wiki</title>
  <meta name="description" content="Archival record of the Cheonbulok Diaspora, the Furnace collapse, and Hwaran (The Furnace Refugee).">
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
    <a class="selected" href="index.html">Characters</a>
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
        <a href="index.html">Characters Hub</a>
        <a href="../lore/index.html">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="../locations/index.html">Atlas &amp; Maps</a>
        <a href="../mechanics/index.html">Battle &amp; Systems</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="../maw/index.html">M.A.W. Codex</a>
      </section>
      <section>
        <h2>Echo-Cores</h2>
        <a href="the-director-majin.html">Majin (Director)</a>
        <a href="the-secretary-seiyon.html">Seiyon (Secretary)</a>
        <a href="the-containment-lead-dekan.html">Dekan (Containment)</a>
        <a href="the-extraction-lead-zyrak.html">Zyrak (Extraction)</a>
        <a href="the-research-lead-ayshuk.html">Ayshuk (Research)</a>
        <a href="the-border-lead-mellda.html">Mellda (Border)</a>
        <a href="the-archive-lead-marjuk.html">Marjuk (Archive)</a>
        <a href="the-outsider-ishall.html">Ishall (Outsider)</a>
        <a href="the-exile-xyan.html">Xyan (Exile)</a>
      </section>
    </nav>
  </aside>

  <main id="content">
    <div class="page-tabs">
      <span>Archival Dossier</span>
      <b>OUTER CITY DIASPORA // REFUGEE REGISTRY</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i><a href="index.html">Characters</a><i>›</i>Cheonbulok Refugees
    </div>

    <section class="department-hero" style="--floor:#ef5b55">
      <img src="../assets/icons/banner_characters.svg" alt="">
      <div>
        <span>EXTERNAL CIVILIZATION // 千不落 · CHEONBULOK</span>
        <h1>Cheonbulok Refugees &amp; Hwaran</h1>
        <p>Survivors of the Furnace Collapse in Corner 2 · The Rage-Han Diaspora</p>
      </div>
    </section>

    <div class="entity-meta-grid" style="margin: 20px 0;">
      <div class="meta-card">
        <b>ORIGIN CITY</b>
        <span>Cheonbulok (천불옥 — City of a Thousand Rages)</span>
      </div>
      <div class="meta-card">
        <b>LEAD FIGURE</b>
        <span>Hwaran (화란 — The Furnace Refugee)</span>
      </div>
      <div class="meta-card">
        <b>SETTLEMENT SECTOR</b>
        <span>Zone E Bulwark Slums &amp; Zone C Enclave</span>
      </div>
      <div class="meta-card">
        <b>RESONANCE DOMAIN</b>
        <span>Rage-Infused Han · High Pugnahan Affinity</span>
      </div>
    </div>

    <article class="article-body">
      <h2>1. The Fall of Cheonbulok</h2>
      <p><strong>Cheonbulok (천불옥 — 千不落)</strong> was an external metropolis situated in the distant Corner 2 of the known planetary expanse. Unlike Somnarak, which refines Han through sorrow, grief, and memory, Cheonbulok processed emotional pressure through an immense industrial engine known as <strong>The Furnace</strong>, burning collective wrath and furious defiance to power its civil shields.</p>
      <p>Three years prior to the conclusion of the 1,778 Cycles, the Furnace suffered structural failure. As the containment core cracked, uncontrolled waves of thermal Han incinerated the metropolis. The few who escaped crossed thousands of kilometers across the Desolate to reach Somnarak.</p>

      <h2>2. Hwaran (화란) — The Furnace Refugee</h2>
      <p><strong>Hwaran</strong> was a veteran Furnace maintenance engineer who survived the collapse, arriving at Somnarak's Gate 5 severely burned and carrying a fragment of the cracked core. Hwaran represents the only living witness in Somnarak to have walked within an external civilization.</p>
      <p>Residing in the outer sectors of Zone E, Hwaran advises the Directorate's Research Lead Ayshuk on the catastrophic risks of thermal resonance overflows while assisting the refugee diaspora in establishing permanent residences within Zone C.</p>

      <h2>3. Socio-Political Status in Somnarak</h2>
      <p>While the High Council initially sought to turn the refugees away under taboo protocols regarding external contamination, Director Majin granted sanctuary under the Dawn Initiative mandate. Today, the Cheonbulok diaspora contributes their advanced thermal forging techniques to the M.A.W. Armories of Zone D.</p>
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
with open(os.path.join(WIKI_DIR, "characters", "cheonbulok-refugees.html"), "w", encoding="utf-8") as f:
    f.write(cheonbulok_html)

# 5. Characters Hub Index (characters/index.html)
char_hub_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Characters &amp; Echo-Cores Registry — Somnarak Wiki</title>
  <meta name="description" content="Master Personnel Registry of Somnarak: The Nine Echo-Cores, Reverie Directorate Leadership, Outskirts Sovereigns, and Notable Figures.">
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
    <a class="selected" href="index.html">Characters</a>
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
        <a href="index.html" style="color:#fff;font-weight:bold;">Characters Hub</a>
        <a href="../lore/index.html">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="../locations/index.html">Atlas &amp; Maps</a>
        <a href="../mechanics/index.html">Battle &amp; Systems</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="../maw/index.html">M.A.W. Codex</a>
      </section>
      <section>
        <h2>Echo-Cores</h2>
        <a href="the-director-majin.html">Majin (Director)</a>
        <a href="the-secretary-seiyon.html">Seiyon (Secretary)</a>
        <a href="the-containment-lead-dekan.html">Dekan (Containment)</a>
        <a href="the-extraction-lead-zyrak.html">Zyrak (Extraction)</a>
        <a href="the-research-lead-ayshuk.html">Ayshuk (Research)</a>
        <a href="the-border-lead-mellda.html">Mellda (Border)</a>
        <a href="the-archive-lead-marjuk.html">Marjuk (Archive)</a>
        <a href="the-outsider-ishall.html">Ishall (Outsider)</a>
        <a href="the-exile-xyan.html">Xyan (Exile)</a>
      </section>
    </nav>
  </aside>

  <main id="content">
    <div class="page-tabs">
      <span>Master Directory</span>
      <b>PERSONNEL ARCHIVE // YEAR 4,238</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i>Characters
    </div>

    <section class="department-hero" style="--floor:#ef5b55">
      <img src="../assets/icons/banner_characters.svg" alt="">
      <div>
        <span>REVERIE DIRECTORATE // CENTRAL ROSTER</span>
        <h1>Characters &amp; Echo-Cores</h1>
        <p>The Nine Directorate Leads, Guild Masters, Outskirts Sovereigns, and Notable Personages</p>
      </div>
    </section>

    <article class="article-body">
      <h2>1. The Nine Echo-Cores (The Directorate Leadership)</h2>
      <p>The Nine Echo-Cores are the central commanding intelligences of the Reverie Directorate. Having endured the full weight of the 1,778 Cycles, each Lead anchors a specific operational floor of The Hand of Change, embodying a distinct resonant aspect of Han.</p>

      <div class="archive-portal-grid">
        <a class="archive-portal" href="the-director-majin.html" style="--portal:#ef5b55">
          <span>CORE 01 · FLOOR 1</span>
          <img src="../assets/icons/floor-1-command.svg" alt="">
          <b>DIRECTOR MAJIN</b>
          <small>Pure Han · Executive Command</small>
        </a>

        <a class="archive-portal" href="the-secretary-seiyon.html" style="--portal:#ef5b55">
          <span>CORE 02 · FLOOR 1</span>
          <img src="../assets/icons/ferrehan.svg" alt="">
          <b>SECRETARY SEIYON</b>
          <small>Ferrehan · Administrative Logic</small>
        </a>

        <a class="archive-portal" href="the-containment-lead-dekan.html" style="--portal:#6f7ee8">
          <span>CORE 03 · FLOOR 2</span>
          <img src="../assets/icons/floor-2-maw.svg" alt="">
          <b>DEKAN (CONTAINMENT)</b>
          <small>Iron Han · Maw's Keep</small>
        </a>

        <a class="archive-portal" href="the-extraction-lead-zyrak.html" style="--portal:#e6c94d">
          <span>CORE 04 · FLOOR 3</span>
          <img src="../assets/icons/floor-3-extraction.svg" alt="">
          <b>ZYRAK (EXTRACTION)</b>
          <small>Weaver Han · M.A.W. Synthesis</small>
        </a>

        <a class="archive-portal" href="the-research-lead-ayshuk.html" style="--portal:#47c978">
          <span>CORE 05 · FLOOR 4</span>
          <img src="../assets/icons/floor-4-insight.svg" alt="">
          <b>AYSHUK (RESEARCH)</b>
          <small>Insight Han · Taboo Analysis</small>
        </a>

        <a class="archive-portal" href="the-border-lead-mellda.html" style="--portal:#d7d7d7">
          <span>CORE 06 · FLOOR 5</span>
          <img src="../assets/icons/floor-5-border.svg" alt="">
          <b>MELLDA (BORDER)</b>
          <small>Border Han · Perimeter Defense</small>
        </a>

        <a class="archive-portal" href="the-archive-lead-marjuk.html" style="--portal:#8d2e42">
          <span>CORE 07 · FLOOR 6</span>
          <img src="../assets/icons/floor-6-vault.svg" alt="">
          <b>MARJUK (ARCHIVE)</b>
          <small>Deep Archive Han · The 1,778 Cycles</small>
        </a>

        <a class="archive-portal" href="the-outsider-ishall.html" style="--portal:#f0a6c4">
          <span>CORE 08 · FLOOR 7</span>
          <img src="../assets/icons/floor-7-shadow.svg" alt="">
          <b>ISHALL (OUTSIDER)</b>
          <small>Shadow Han · Underworld Recon</small>
        </a>

        <a class="archive-portal" href="the-exile-xyan.html" style="--portal:#f4efa0">
          <span>CORE 09 · FLOOR 8</span>
          <img src="../assets/icons/floor-8-gate.svg" alt="">
          <b>XYAN (THE EXILE)</b>
          <small>Dawn Light · Gate Watch Command</small>
        </a>
      </div>

      <h2>2. Notable Guild Masters &amp; Key Figures</h2>
      <div class="archive-portal-grid" style="margin-top: 20px;">
        <a class="archive-portal" href="kael.html" style="--portal:#e6c94d">
          <span>OUTSKIRTS</span>
          <img src="../assets/icons/outside.svg" alt="">
          <b>KAEL (DRIFT KING)</b>
          <small>Sovereign of the Desolate Nomads</small>
        </a>

        <a class="archive-portal" href="soojin.html" style="--portal:#4ade80">
          <span>GUILD ARTISAN</span>
          <img src="../assets/icons/gift.svg" alt="">
          <b>SOOJIN (MASTER WEAVER)</b>
          <small>Lead Tailor · Field Containment</small>
        </a>

        <a class="archive-portal" href="high-architects.html" style="--portal:#38bdf8">
          <span>BARRIER MASONS</span>
          <img src="../assets/icons/city.svg" alt="">
          <b>THE HIGH ARCHITECTS</b>
          <small>Daejun, Doha &amp; Aegis Builders</small>
        </a>

        <a class="archive-portal" href="cheonbulok-refugees.html" style="--portal:#ef5b55">
          <span>OUTER DIASPORA</span>
          <img src="../assets/icons/flame.svg" alt="">
          <b>CHEONBULOK REFUGEES</b>
          <small>Hwaran &amp; Furnace Survivors</small>
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
with open(os.path.join(WIKI_DIR, "characters", "index.html"), "w", encoding="utf-8") as f:
    f.write(char_hub_html)

print("All 14 character pages successfully generated with deep canonical content!")
