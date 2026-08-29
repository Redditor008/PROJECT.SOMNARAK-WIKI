import os

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

depts_data = {
    "floor-1-neutral-command.html": (
        "Floor 1: Neutral Command",
        "Majin & Seiyon",
        "#ef5b55",
        "icon_dept_f1_neutral.svg",
        "Executive Command & Central Logistics",
        """
        <h2>1. Department Mandate &amp; Architecture</h2>
        <p><strong>Floor 1: Neutral Command (중립 지휘부)</strong> is the apex operational sector of The Hand of Change, located directly beneath the Central Spire in Zone A. Jointly anchored by <strong>Director Majin (Pure Han)</strong> and <strong>Secretary Seiyon (Ferrehan)</strong>, Floor 1 coordinates all tactical communications, inter-floor resource allocations, emergency breach sirens, and citywide defense directives.</p>

        <h2>2. Key Sector Facilities</h2>
        <ul>
          <li><strong>The Command Bridge:</strong> Monolithic circular control rotunda displaying real-time bio-vital telemetry and containment status across all eight floors.</li>
          <li><strong>Central Logistical Registry:</strong> Automated records bank managed by Seiyon, processing work orders, personnel rotations, and M.A.W. requisition requests.</li>
          <li><strong>Executive Chambers:</strong> Meeting room of the Nine Echo-Cores during facility-wide crisis briefings.</li>
        </ul>

        <h2>3. Floor 1 Tactical Operations</h2>
        <p>During containment breaches, Floor 1 operators coordinate suppression squads, reroute power to isolation bulkheads, and calculate optimal work assignments to prevent entity resonance cascades.</p>
        """
    ),
    "floor-2-maws-keep.html": (
        "Floor 2: Maw's Keep",
        "Dekan (Containment Lead)",
        "#6f7ee8",
        "icon_dept_f2_maws_keep.svg",
        "Heavy Containment & Physical Restraint",
        """
        <h2>1. The Iron Bastion of Containment</h2>
        <p><strong>Floor 2: Maw's Keep (심연의 파수대)</strong> oversees the heavy containment chambers situated directly above the subterranean chasm of The Maw. Commanded by <strong>Dekan (Iron Han / Pugnahan)</strong>, the department specializes in the physical confinement, structural reinforcement, and tactical suppression of high-threat physical and kinetic Sorrow Entities.</p>

        <h2>2. Key Sector Facilities</h2>
        <ul>
          <li><strong>Heavy Containment Blocks A–D:</strong> High-density reinforced titanium-basalt isolation cells equipped with hydraulic pressure clamps.</li>
          <li><strong>Gantry Watchtowers:</strong> Fortified observation platforms suspended directly over the boiling Han reservoirs of the abyss.</li>
          <li><strong>The Iron Armory:</strong> Storage facility for heavy blunt suppression hammers, physical restraints, and Pugnahan shields.</li>
        </ul>
        """
    ),
    "floor-3-extraction-hall.html": (
        "Floor 3: Extraction Hall",
        "Zyrak (Extraction Lead)",
        "#e6c94d",
        "icon_dept_f3_extraction.svg",
        "M.A.W. Synthesis & Needle Weaving",
        """
        <h2>1. The Forge of Sorrow</h2>
        <p><strong>Floor 3: Extraction Hall (추출의 전당)</strong> is the industrial heart of The Hand of Change. Commanded by <strong>Zyrak (Weaver Han / Flerehan)</strong> in close collaboration with Master Weaver Soojin, the department siphons pure emotional resonance from stabilized entities and weaves it into wearable M.A.W. suits, weapons, and protective gifts.</p>

        <h2>2. Key Sector Facilities</h2>
        <ul>
          <li><strong>The Great Looms:</strong> Massive resonant weaving apparatuses spinning boiling Han fluids into non-conductive silk threads.</li>
          <li><strong>Crystallization Tanks:</strong> Temperature-controlled vats used to solidify liquid grief into high-density weapon blades.</li>
          <li><strong>Calibration Anvils:</strong> Fine-tuning workshops where M.A.W. gear is matched to individual operative neural frequencies.</li>
        </ul>
        """
    ),
    "floor-4-insight-forge.html": (
        "Floor 4: Insight Forge",
        "Ayshuk (Research Lead)",
        "#47c978",
        "icon_dept_f4_insight_forge.svg",
        "Cognitive Mapping & Taboo Analysis",
        """
        <h2>1. The Sanctuary of Understanding</h2>
        <p><strong>Floor 4: Insight Forge (통찰의 대장간)</strong> is the scientific, cognitive, and metaphysical laboratory of the Directorate. Commanded by <strong>Ayshuk (Insight Han / Viderehan)</strong>, the department investigates the fundamental laws of Han, conducts psychological therapy on fractured operatives, and decodes the Seven Absolute Taboos.</p>

        <h2>2. Key Sector Facilities</h2>
        <ul>
          <li><strong>Neural Telemetry Labs:</strong> Advanced observation suites monitoring brainwave coherence and panic escalation in field operatives.</li>
          <li><strong>Taboo Resonance Archive:</strong> Highly classified research vaults studying external city anomalies and illegal memory technologies.</li>
          <li><strong>The Recovery Wards:</strong> Medical sanatorium utilizing Alpha Sap resonance to heal fractured composure.</li>
        </ul>
        """
    ),
    "floor-5-border-watch.html": (
        "Floor 5: Border Watch",
        "Mellda (Border Lead)",
        "#d7d7d7",
        "icon_dept_f5_border_watch.svg",
        "Aegis Barrier Defense & Telemetry",
        """
        <h2>1. Shield of the Metropolis</h2>
        <p><strong>Floor 5: Border Watch (경계 파수대)</strong> commands the defensive energy grid protecting Somnarak. Commanded by <strong>Mellda (Border Han / Aegis Pure)</strong>, the department oversees the 36 Aegis Projectors lining Zone E, monitoring atmospheric turbulence and intercepting Desolate anomalies before they reach the perimeter.</p>

        <h2>2. Key Sector Facilities</h2>
        <ul>
          <li><strong>Barrier Telemetry Rotunda:</strong> Central array monitoring shield thickness, frequency harmonizers, and structural stress points.</li>
          <li><strong>Rapid Interception Armory:</strong> Deployment staging zone for high-mobility sentinel squads equipped with long-range kinetic rifles.</li>
          <li><strong>Desolate Seismic Arrays:</strong> Ground-penetrating sonar tracking the movements of uncontained titans across the ash wastes.</li>
        </ul>
        """
    ),
    "floor-6-deep-vault.html": (
        "Floor 6: Deep Vault",
        "Marjuk (Archive Lead)",
        "#8d2e42",
        "icon_dept_f6_deep_vault.svg",
        "The 1,778 Cycles & Memory Preservation",
        """
        <h2>1. The Keep of Unwritten History</h2>
        <p><strong>Floor 6: Deep Vault (심층 수장고)</strong> is the subterranean library preserving the complete unexpurgated history of Somnarak across all 1,778 Cycles. Commanded by <strong>Marjuk (Deep Archive Han)</strong>, the department safeguards sealed memory scrolls, pre-Cycle artifacts, and the true records of forgotten sacrifices.</p>

        <h2>2. Key Sector Facilities</h2>
        <ul>
          <li><strong>The Scroll Catacombs:</strong> Thousands of kilometers of subterranean stone shelving housing handwritten logs from every historical iteration.</li>
          <li><strong>The Void Chamber:</strong> A zero-resonance isolation chamber where dangerous psycho-active texts are preserved without radiating ambient grief.</li>
          <li><strong>The Scribe's Desk:</strong> Marjuk's personal study, where every casualty and victory of the Dawn Initiative is recorded in immutable ink.</li>
        </ul>
        """
    ),
    "floor-7-shadow-corps.html": (
        "Floor 7: Shadow Corps",
        "Ishall (The Outsider)",
        "#f0a6c4",
        "icon_dept_f7_shadow_corps.svg",
        "Underworld Infiltration & Counter-Espionage",
        """
        <h2>1. The Unseen Blade</h2>
        <p><strong>Floor 7: Shadow Corps (그림자 군단)</strong> operates in the liminal spaces between Directorate authority and the Underworld. Commanded by <strong>Ishall (Shadow Han / Void)</strong>, the department conducts covert reconnaissance, neutralizes illegal memory laundering syndicates, and infiltrates rogue Fray networks.</p>

        <h2>2. Key Sector Facilities</h2>
        <ul>
          <li><strong>Infiltration Staging Cells:</strong> Sub-level access corridors connecting directly to the black markets of Zone C.</li>
          <li><strong>Resonance Dampening Chambers:</strong> Interrogation and isolation rooms coated in sound-absorbing shadow felt.</li>
          <li><strong>The Whisper Network:</strong> Intelligence routing hub receiving clandestine reports from covert informants across the city.</li>
        </ul>
        """
    ),
    "floor-8-gate-watch.html": (
        "Floor 8: Gate Watch",
        "Xyan (The Exile)",
        "#f4efa0",
        "icon_dept_f8_gate_watch.svg",
        "Gate 5 Terminal & Returnee Protocols",
        """
        <h2>1. Gateway to the Frontier</h2>
        <p><strong>Floor 8: Gate Watch (관문 감시국)</strong> is the outermost outpost of The Hand of Change, directly commanding the fortified airlocks of Gate 5 in Zone E. Commanded by <strong>Xyan (Gate Watch Han / Dawn Light)</strong> following his physical return from the Desolate, the department manages outside expeditions, refugee quarantine, and contact with nomadic caravans.</p>

        <h2>2. Key Sector Facilities</h2>
        <ul>
          <li><strong>Gate 5 Airlock Nexus:</strong> Triple-reinforced hydraulic blast gates separating the living city from the Desolate ash wastes.</li>
          <li><strong>Dawn Quarantine Wards:</strong> Screening chambers for returnee squads and refugees to ensure zero external parasitic Han contamination.</li>
          <li><strong>Outskirts Caravan Terminal:</strong> Regulated trade platform where the Directorate conducts official exchanges with Kael the Drift King.</li>
        </ul>
        """
    )
}

hub_html = """<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>The Hand of Change (Facility Directory) — Somnarak Wiki</title>
  <meta name="description" content="Operational facility directory for The Hand of Change: Floors 1 through 8, department mandates, and Echo-Core commands.">
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
        <a href="index.html" style="color:#fff;font-weight:bold;">Hand of Change</a>
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
      <span>Facility Directory</span>
      <b>THE HAND OF CHANGE // 變化之手</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i>Hand of Change
    </div>

    <section class="department-hero" style="--floor:#4cc9f0">
      <img src="../assets/layout/hand/icons/the_hand_dr_icon_styled.svg" alt="">
      <div>
        <span>REVERIE DIRECTORATE // CENTRAL CONTAINMENT FACILITY</span>
        <h1>The Hand of Change (변화의 손)</h1>
        <p>The Eight Operational Floors Excavated into the Root Mass of the Alpha Tree</p>
      </div>
    </section>

    <article class="article-body">
      <h2>Architectural Facility Blueprint</h2>
      <div class="archive-portal-grid" style="margin-bottom: 24px;">
        <a class="archive-portal" href="../atlas/hand-of-change-map.html" style="--portal:#38bdf8">
          <span>FACILITY CUTAWAY</span>
          <img src="../assets/layout/hand/icons/the_hand_dr_icon_styled.svg" alt="">
          <b>ARCHITECTURAL MAP</b>
          <small>Interactive facility schematics</small>
        </a>
      </div>

      <h2>Operational Floors 1 through 8</h2>
      <div class="archive-portal-grid">
        <a class="archive-portal" href="floor-1-neutral-command.html" style="--portal:#ef5b55">
          <span>FLOOR 1</span>
          <img src="../assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt="">
          <b>NEUTRAL COMMAND</b>
          <small>Majin &amp; Seiyon</small>
        </a>

        <a class="archive-portal" href="floor-2-maws-keep.html" style="--portal:#6f7ee8">
          <span>FLOOR 2</span>
          <img src="../assets/layout/hand/icons/icon_dept_f2_maws_keep.svg" alt="">
          <b>MAW’S KEEP</b>
          <small>Dekan (Containment)</small>
        </a>

        <a class="archive-portal" href="floor-3-extraction-hall.html" style="--portal:#e6c94d">
          <span>FLOOR 3</span>
          <img src="../assets/layout/hand/icons/icon_dept_f3_extraction.svg" alt="">
          <b>EXTRACTION HALL</b>
          <small>Zyrak (M.A.W. Looms)</small>
        </a>

        <a class="archive-portal" href="floor-4-insight-forge.html" style="--portal:#47c978">
          <span>FLOOR 4</span>
          <img src="../assets/layout/hand/icons/icon_dept_f4_insight_forge.svg" alt="">
          <b>INSIGHT FORGE</b>
          <small>Ayshuk (Research)</small>
        </a>

        <a class="archive-portal" href="floor-5-border-watch.html" style="--portal:#d7d7d7">
          <span>FLOOR 5</span>
          <img src="../assets/layout/hand/icons/icon_dept_f5_border_watch.svg" alt="">
          <b>BORDER WATCH</b>
          <small>Mellda (Aegis Defense)</small>
        </a>

        <a class="archive-portal" href="floor-6-deep-vault.html" style="--portal:#8d2e42">
          <span>FLOOR 6</span>
          <img src="../assets/layout/hand/icons/icon_dept_f6_deep_vault.svg" alt="">
          <b>DEEP VAULT</b>
          <small>Marjuk (1,778 Cycles)</small>
        </a>

        <a class="archive-portal" href="floor-7-shadow-corps.html" style="--portal:#f0a6c4">
          <span>FLOOR 7</span>
          <img src="../assets/layout/hand/icons/icon_dept_f7_shadow_corps.svg" alt="">
          <b>SHADOW CORPS</b>
          <small>Ishall (The Outsider)</small>
        </a>

        <a class="archive-portal" href="floor-8-gate-watch.html" style="--portal:#f4efa0">
          <span>FLOOR 8</span>
          <img src="../assets/layout/hand/icons/icon_dept_f8_gate_watch.svg" alt="">
          <b>GATE WATCH</b>
          <small>Xyan (The Exile)</small>
        </a>
      </div>
    </article>
  </main>

  <aside class="floor-rail" aria-label="Hand of Change departments">
    <h2>HAND OF CHANGE</h2>
    <a class="floor-button f1" href="floor-1-neutral-command.html" style="--floor:#ef5b55"><span><small>FLOOR 1</small>NEUTRAL</span><img src="../assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt=""></a>
    <a class="floor-button f2" href="floor-2-maws-keep.html" style="--floor:#6f7ee8"><span><small>FLOOR 2</small>MAW’S KEEP</span><img src="../assets/layout/hand/icons/icon_dept_f2_maws_keep.svg" alt=""></a>
    <a class="floor-button f3" href="floor-3-extraction-hall.html" style="--floor:#e6c94d"><span><small>FLOOR 3</small>EXTRACTION HALL</span><img src="../assets/layout/hand/icons/icon_dept_f3_extraction.svg" alt=""></a>
    <a class="floor-button f4" href="floor-4-insight-forge.html" style="--floor:#47c978"><span><small>FLOOR 4</small>INSIGHT FORGE</span><img src="../assets/layout/hand/icons/icon_dept_f4_insight_forge.svg" alt=""></a>
    <a class="floor-button f5" href="floor-5-border-watch.html" style="--floor:#d7d7d7"><span><small>FLOOR 5</small>BORDER WATCH</span><img src="../assets/layout/hand/icons/icon_dept_f5_border_watch.svg" alt=""></a>
    <a class="floor-button f6" href="floor-6-deep-vault.html" style="--floor:#8d2e42"><span><small>FLOOR 6</small>DEEP VAULT</span><img src="../assets/layout/hand/icons/icon_dept_f6_deep_vault.svg" alt=""></a>
    <a class="floor-button f7" href="floor-7-shadow-corps.html" style="--floor:#f0a6c4"><span><small>FLOOR 7</small>SHADOW CORPS</span><img src="../assets/layout/hand/icons/icon_dept_f7_shadow_corps.svg" alt=""></a>
    <a class="floor-button f8" href="floor-8-gate-watch.html" style="--floor:#f4efa0"><span><small>FLOOR 8</small>GATE WATCH</span><img src="../assets/layout/hand/icons/icon_dept_f8_gate_watch.svg" alt=""></a>
    <a class="rail-action" href="index.html">OPEN FACILITY DIRECTORY</a>
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

for fname, (title, sub, color, icon, role, body) in depts_data.items():
    page_html = f"""<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title} — Somnarak Wiki</title>
  <meta name="description" content="Official operational dossier for {title} in The Hand of Change: {sub}.">
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
        <a href="index.html" style="color:#fff;font-weight:bold;">Hand of Change</a>
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
      <span>Facility Dossier</span>
      <b>DEPARTMENT RECORD // 部門紀錄</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i><a href="index.html">Hand of Change</a><i>›</i>{title}
    </div>

    <section class="department-hero" style="--floor:{color}">
      <img src="../assets/layout/hand/icons/{icon}" alt="">
      <div>
        <span>THE HAND OF CHANGE // OPERATIONAL FLOOR</span>
        <h1>{title}</h1>
        <p>Command Lead: <strong>{sub}</strong> · Mandate: {role}</p>
      </div>
    </section>

    <div class="entity-meta-grid" style="margin: 20px 0;">
      <div class="meta-card">
        <b>DEPARTMENT</b>
        <span>{title}</span>
      </div>
      <div class="meta-card">
        <b>COMMAND LEAD</b>
        <span>{sub}</span>
      </div>
      <div class="meta-card">
        <b>FACILITY MANDATE</b>
        <span>{role}</span>
      </div>
      <div class="meta-card">
        <b>CURRENT STATUS</b>
        <span>Active · Dawn Initiative</span>
      </div>
    </div>

    <article class="article-body">
      {body}
    </article>
  </main>

  <aside class="floor-rail" aria-label="Hand of Change departments">
    <h2>HAND OF CHANGE</h2>
    <a class="floor-button f1" href="floor-1-neutral-command.html" style="--floor:#ef5b55"><span><small>FLOOR 1</small>NEUTRAL</span><img src="../assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt=""></a>
    <a class="floor-button f2" href="floor-2-maws-keep.html" style="--floor:#6f7ee8"><span><small>FLOOR 2</small>MAW’S KEEP</span><img src="../assets/layout/hand/icons/icon_dept_f2_maws_keep.svg" alt=""></a>
    <a class="floor-button f3" href="floor-3-extraction-hall.html" style="--floor:#e6c94d"><span><small>FLOOR 3</small>EXTRACTION HALL</span><img src="../assets/layout/hand/icons/icon_dept_f3_extraction.svg" alt=""></a>
    <a class="floor-button f4" href="floor-4-insight-forge.html" style="--floor:#47c978"><span><small>FLOOR 4</small>INSIGHT FORGE</span><img src="../assets/layout/hand/icons/icon_dept_f4_insight_forge.svg" alt=""></a>
    <a class="floor-button f5" href="floor-5-border-watch.html" style="--floor:#d7d7d7"><span><small>FLOOR 5</small>BORDER WATCH</span><img src="../assets/layout/hand/icons/icon_dept_f5_border_watch.svg" alt=""></a>
    <a class="floor-button f6" href="floor-6-deep-vault.html" style="--floor:#8d2e42"><span><small>FLOOR 6</small>DEEP VAULT</span><img src="../assets/layout/hand/icons/icon_dept_f6_deep_vault.svg" alt=""></a>
    <a class="floor-button f7" href="floor-7-shadow-corps.html" style="--floor:#f0a6c4"><span><small>FLOOR 7</small>SHADOW CORPS</span><img src="../assets/layout/hand/icons/icon_dept_f7_shadow_corps.svg" alt=""></a>
    <a class="floor-button f8" href="floor-8-gate-watch.html" style="--floor:#f4efa0"><span><small>FLOOR 8</small>GATE WATCH</span><img src="../assets/layout/hand/icons/icon_dept_f8_gate_watch.svg" alt=""></a>
    <a class="rail-action" href="index.html">OPEN FACILITY DIRECTORY</a>
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
    with open(os.path.join(WIKI_DIR, "departments", fname), "w", encoding="utf-8") as f:
        f.write(page_html)

with open(os.path.join(WIKI_DIR, "departments", "index.html"), "w", encoding="utf-8") as f:
    f.write(hub_html)

print("All 9 Department pages successfully generated!")
