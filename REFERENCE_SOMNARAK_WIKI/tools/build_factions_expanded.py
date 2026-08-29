import os

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

factions_data = {
    "the-reverie-directorate.html": (
        "The Reverie Directorate",
        "Executive Authority of Somnarak",
        "#ef5b55",
        "fac_rd.svg",
        "Zone A Central Spire & The Hand of Change",
        """
        <h2>1. Executive Mandate &amp; Sovereignty</h2>
        <p>The <strong>Reverie Directorate (몽환국 — 夢幻局)</strong> is the supreme executive, scientific, and containment authority governing the City of Somnarak. Established during the First Cycle to study the volatile emotional physics of the Alpha Tree and the Weeping, the Directorate coordinates the containment of Sorrow Entities, the refinement of Han energy, and the defense of 1.29 billion human lives.</p>
        <p>Operating from <strong>The Hand of Change</strong>—a monolithic underground facility excavated directly into the root mass of the Alpha Tree—the Directorate exercises absolute jurisdiction over all anomaly research, M.A.W. synthesis, and emergency breach suppression.</p>

        <h2>2. Institutional Command Hierarchy</h2>
        <div class="table-wrap">
          <table class="data-table">
            <thead>
              <tr><th>Command Tier</th><th>Designation</th><th>Operational Domain</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Tier 0: Supreme Director</strong></td><td>Director Majin (마진)</td><td>Executive authority, strategic containment, Absolvohan mandate.</td></tr>
              <tr><td><strong>Tier 1: Secretary General</strong></td><td>Secretary Seiyon (세이연)</td><td>Administrative logistics, inter-floor coordination, civic resources.</td></tr>
              <tr><td><strong>Tier 2: The Echo-Cores</strong></td><td>Floors 2 through 8 Leads</td><td>Containment, extraction, research, border defense, vault archives, shadow ops, gate watch.</td></tr>
              <tr><td><strong>Tier 3: Senior Handlers</strong></td><td>Weaver &amp; Containment Masters</td><td>Direct entity observation, work order execution, field suppression.</td></tr>
            </tbody>
          </table>
        </div>

        <h2>3. The Four Work Types</h2>
        <p>To safely harvest energy from Sorrow Entities without provoking catastrophic fractures or breaches, the Directorate developed the <strong>Four Standardized Work Types</strong>:</p>
        <ul>
          <li><strong>Instinct Work (본능):</strong> Tending to the physical, ambient, or material requirements of the entity. Satisfies basic stability.</li>
          <li><strong>Insight Work (통찰):</strong> Environmental calibration, chamber cleansing, and structural analysis. Maintains spatial containment.</li>
          <li><strong>Attachment Work (애착):</strong> Emotional resonance matching and psychic dialogue. Calms active grief and prevents rage accumulation.</li>
          <li><strong>Repression Work (억압):</strong> Active suppression of anomalous emanations via dampening resonance fields. Constrains hostile expansion.</li>
        </ul>
        """
    ),
    "the-high-council.html": (
        "The High Council (Council of Sights)",
        "The Senate of Somnarak",
        "#f1df76",
        "fac_council.svg",
        "Zone A Senate Citadel",
        """
        <h2>1. Legislative Governance</h2>
        <p>The <strong>High Council (최고 평의회)</strong>—known colloquially as the <em>Council of Sights (시선의 평의회)</em>—is the parliamentary senate of Somnarak. Composed of twelve Grand Senators representing the political, industrial, and social factions across Zones A through E, the Council enacts civil legislation, sets municipal tax rates, regulates the Scavenger Guilds, and adjudicates the <strong>Seven Absolute Taboos</strong>.</p>

        <h2>2. Political Tension with the Directorate</h2>
        <p>While the Reverie Directorate maintains executive control over containment, defense, and M.A.W. armaments, the High Council manages civil infrastructure, food distribution, and municipal law. Historically, bitter tensions have existed between the Council’s conservative preservationists and the Directorate's progressive Dawn Initiative, particularly regarding the rights of external refugees and the deregulation of outer-zone commerce.</p>

        <h2>3. The Seven Absolute Taboos</h2>
        <div class="table-wrap">
          <table class="data-table">
            <thead>
              <tr><th>Taboo ID</th><th>Classification</th><th>Enforcement Protocol</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Taboo I</strong></td><td>Unlicensed Extraction of Raw Han</td><td>Immediate seizure by Municipal Wardens; trial in Sector C Debt Court.</td></tr>
              <tr><td><strong>Taboo II</strong></td><td>Breaching the Aegis Barrier without Gate Authorization</td><td>Lethal suppression authorized by Floor 8 Gate Watch.</td></tr>
              <tr><td><strong>Taboo III</strong></td><td>Memory Washing &amp; Identity Theft</td><td>Permanent consignment to the Deep Vault (Floor 6).</td></tr>
              <tr><td><strong>Taboo IV</strong></td><td>Possession of Unbound ALEPH Relics</td><td>Directorate emergency containment intervention.</td></tr>
              <tr><td><strong>Taboo V</strong></td><td>Intentional Provocation of Sorrow Fractures</td><td>Summary execution or forced induction into Maw labor squads.</td></tr>
              <tr><td><strong>Taboo VI</strong></td><td>Falsification of Archival Cycle Records</td><td>Direct adjudication under Director Majin’s seal.</td></tr>
              <tr><td><strong>Taboo VII</strong></td><td>Conspiracy with Uncontained Anomalies</td><td>Total civic erasure.</td></tr>
            </tbody>
          </table>
        </div>
        """
    ),
    "the-architects.html": (
        "The High Guild of Architects",
        "The Masons of Aegis",
        "#47c978",
        "fac_architects.svg",
        "Zone A Core Spire & Zone D Masonry Yards",
        """
        <h2>1. Masters of the Built World</h2>
        <p>The <strong>High Guild of Architects (건축가 길드)</strong> is the ancient masonry and engineering fraternity tasked with designing, constructing, and fortifying Somnarak. From the colossal subterranean pylons supporting the Central Spire to the hexagonal blast doors of The Hand of Change, the Architects master the unique art of <em>Resonant Architecture</em>—shaping stone and metal to absorb and channel ambient Han without fracturing.</p>

        <h2>2. Guardians of the Aegis Lattice</h2>
        <p>The Guild is directly responsible for the operational maintenance of the 36 Aegis Projectors lining Zone E. In coordination with Master Daejun (The Blind Architect) and Chief Engineer Joon, the Architects conduct daily structural audits of the perimeter barrier, repairing micro-fractures caused by abrasive sandstorms and anomalous seismic pulses from the Desolate.</p>
        """
    ),
    "the-weavers.html": (
        "The Weavers Guild of Echo Gardens",
        "Artisans of Materialized Agony",
        "#e6c94d",
        "fac_weavers.svg",
        "Zone D Echo Arboretums & Floor 3 Looms",
        """
        <h2>1. The Art of Needle Resonance</h2>
        <p>The <strong>Weavers Guild (직조사 길드)</strong> operates from the bioluminescent botanical arboretums of Zone D and the industrial looms of Floor 3 (Extraction Hall). Their sacred duty is the transformation of extracted sorrow into wearable armor, weapons, and protective gifts—a discipline known as <strong>M.A.W. Synthesis</strong>.</p>

        <h2>2. The Three Weaving Doctrines</h2>
        <ul>
          <li><strong>Filament Spinning:</strong> Channelling boiling Han liquids from containment cells into fine, non-conductive silk threads.</li>
          <li><strong>Ego-Embroidery:</strong> Stitching protective geometric glyphs into the inner linings of combat suits to insulate operatives against psychic contagion.</li>
          <li><strong>Needle Attunement:</strong> Calibrating weapons to harmonize with an operative's individual emotional frequency, maximizing clash potency.</li>
        </ul>
        """
    ),
    "the-wardens.html": (
        "The Municipal Wardens",
        "Civil Enforcement & Perimeter Sentinels",
        "#d7d7d7",
        "fac_wardens.svg",
        "Zone B Headquarters & All Sector Precincts",
        """
        <h2>1. Law Enforcement in the City of Sorrow</h2>
        <p>The <strong>Municipal Wardens (도시 경비대)</strong> are the primary civil peacekeepers of Somnarak. Stationed across all five zones, the Wardens maintain civil order, enforce citywide curfews, patrol the perimeter bastions of Zone E, and provide auxiliary security during low-level containment breaches.</p>

        <h2>2. Tactical Armament &amp; Riot Suppression</h2>
        <p>Equipped with standardized TETH- and HE-grade kinetic riot shields, shock batons, and Ferrehan gas canisters, Warden strike teams are trained to subdue panicked mobs and suppress minor rogue anomalies before full Directorate intervention is required.</p>
        """
    ),
    "the-collectors.html": (
        "The Scavenger & Collector Guilds",
        "Relic Salvagers of Zone C",
        "#a78bfa",
        "fac_collectors.svg",
        "Zone C Collector's Row & Debt Court",
        """
        <h2>1. Salvage, Pawn, and Debt</h2>
        <p>The <strong>Collectors (수집가 길드)</strong> dominate the commercial underbelly of Zone C. Specializing in the retrieval, appraisal, and trade of historical relics, dormant crystal nodes, and outside artifacts salvaged from the fringe of the Desolate, the Collectors operate the city's private debt courts and pawn emporiums.</p>

        <h2>2. Relationship with SE-014 &amp; SE-015</h2>
        <p>The Collectors maintain close metaphysical ties to SE-014 (The Debt Eater) and SE-015 (The Debt Scale). Through legally binding debt contracts inscribed on Han-parchment, Collector magistrates utilize these entities to enforce financial contracts and extract collateral from defaulters.</p>
        """
    ),
    "the-underworld-and-wound-walkers.html": (
        "The Underworld &amp; Wound Walkers",
        "Nomads of the Desolate &amp; The Frays",
        "#8d2e42",
        "fac_keepers.svg",
        "Zone C Sub-levels & Outer Sand Wastes",
        """
        <h2>1. The Frays of the Sub-Levels</h2>
        <p>Beneath the regulated districts of Zone C lies the sprawling labyrinth of the <strong>Underworld Frays (암흑가)</strong>. Comprising rogue fixers, illegal Han refiners, and memory syndicates like the <em>Memory Washers</em>, the Frays operate beyond the High Council’s reach, trading illicit outside goods and stolen identities.</p>

        <h2>2. The Wound Walkers of the Desolate</h2>
        <p>Beyond the Aegis Veil wander the <strong>Wound Walkers (상처를 걷는 자들)</strong>—hardened nomads and ascetics who traverse the gray ash wastes without barrier protection. Guided by Kael the Drift King, these outcasts have adapted their physiology to withstand raw Han, living in mobile tread-settlements that follow planetary emotional ley lines.</p>
        """
    )
}

# Hub Page HTML for factions/index.html
hub_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Factions &amp; Guilds of Somnarak — Somnarak Wiki</title>
  <meta name="description" content="Master Directory of Factions, Governance, and Guilds in Somnarak: Reverie Directorate, High Council, Architects, Weavers, and Underworld.">
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
    <a class="selected" href="index.html">Factions</a>
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
        <a href="index.html" style="color:#fff;font-weight:bold;">Factions &amp; Guilds</a>
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
      <span>Master Directory</span>
      <b>INSTITUTIONAL DIRECTORY // 勢力目錄</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i>Factions
    </div>

    <section class="department-hero" style="--floor:#f1df76">
      <img src="../assets/icons/banner_factions.svg" alt="">
      <div>
        <span>SOMNARAK HIERARCHY // 統治與組織</span>
        <h1>Factions &amp; Guilds</h1>
        <p>Executive Governance, Legislative Senate, Artisan Guilds, and Outskirts Nomads</p>
      </div>
    </section>

    <article class="article-body">
      <h2>Institutional Portals</h2>
      <div class="archive-portal-grid">
        <a class="archive-portal" href="the-reverie-directorate.html" style="--portal:#ef5b55">
          <span>EXECUTIVE AUTHORITY</span>
          <img src="../assets/icons/fac_rd.svg" alt="">
          <b>REVERIE DIRECTORATE</b>
          <small>Central Spire &amp; The Hand</small>
        </a>

        <a class="archive-portal" href="the-high-council.html" style="--portal:#f1df76">
          <span>SENATE</span>
          <img src="../assets/icons/fac_council.svg" alt="">
          <b>THE HIGH COUNCIL</b>
          <small>Council of Sights &amp; Taboos</small>
        </a>

        <a class="archive-portal" href="the-architects.html" style="--portal:#47c978">
          <span>MASONRY GUILD</span>
          <img src="../assets/icons/fac_architects.svg" alt="">
          <b>THE ARCHITECTS</b>
          <small>Aegis Builders &amp; Masons</small>
        </a>

        <a class="archive-portal" href="the-weavers.html" style="--portal:#e6c94d">
          <span>M.A.W. ARTISANS</span>
          <img src="../assets/icons/fac_weavers.svg" alt="">
          <b>THE WEAVERS</b>
          <small>Echo Gardens &amp; Needles</small>
        </a>

        <a class="archive-portal" href="the-wardens.html" style="--portal:#d7d7d7">
          <span>CIVIC DEFENSE</span>
          <img src="../assets/icons/fac_wardens.svg" alt="">
          <b>THE WARDENS</b>
          <small>Municipal Sentinels</small>
        </a>

        <a class="archive-portal" href="the-collectors.html" style="--portal:#a78bfa">
          <span>COMMERCE &amp; DEBT</span>
          <img src="../assets/icons/fac_collectors.svg" alt="">
          <b>THE COLLECTORS</b>
          <small>Scavengers &amp; Debt Court</small>
        </a>

        <a class="archive-portal" href="the-underworld-and-wound-walkers.html" style="--portal:#8d2e42">
          <span>OUTSKIRTS &amp; FRAYS</span>
          <img src="../assets/icons/fac_keepers.svg" alt="">
          <b>WOUND WALKERS</b>
          <small>Desolate Nomads &amp; Frays</small>
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

for fname, (title, sub, color, icon, domain, body) in factions_data.items():
    page_html = f"""<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title} — Somnarak Wiki</title>
  <meta name="description" content="Official archival record on {title}: {sub}.">
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
    <a class="selected" href="index.html">Factions</a>
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
        <a href="index.html" style="color:#fff;font-weight:bold;">Factions &amp; Guilds</a>
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
      <span>Institutional Dossier</span>
      <b>FACTION RECORD // YEAR 4,238</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i><a href="index.html">Factions</a><i>›</i>{title}
    </div>

    <section class="department-hero" style="--floor:{color}">
      <img src="../assets/icons/{icon}" alt="">
      <div>
        <span>INSTITUTIONAL REGISTRY // 組織紀錄</span>
        <h1>{title}</h1>
        <p>{sub} · Jurisdiction: <strong>{domain}</strong></p>
      </div>
    </section>

    <div class="entity-meta-grid" style="margin: 20px 0;">
      <div class="meta-card">
        <b>ORGANIZATION</b>
        <span>{title}</span>
      </div>
      <div class="meta-card">
        <b>HEADQUARTERS</b>
        <span>{domain}</span>
      </div>
      <div class="meta-card">
        <b>AUTHORITY CLASS</b>
        <span>{sub}</span>
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
    with open(os.path.join(WIKI_DIR, "factions", fname), "w", encoding="utf-8") as f:
        f.write(page_html)

with open(os.path.join(WIKI_DIR, "factions", "index.html"), "w", encoding="utf-8") as f:
    f.write(hub_html)

print("All 8 Faction compendiums successfully generated!")
