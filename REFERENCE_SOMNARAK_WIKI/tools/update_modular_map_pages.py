import os

HAND_MAP_PATH = "/home/user/01_Somnarak_Wiki/atlas/hand-of-change-map.html"
CITY_MAP_PATH = "/home/user/01_Somnarak_Wiki/atlas/somnarak-city-map.html"

# 1. Update Hand of Change Map Page
hand_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Hand of Change: Facility 01 Blueprint - Somnarak Official Wiki</title>
  <link rel="stylesheet" href="../assets/css/wiki.css">
</head>
<body class="wiki-body map-viewer-page">
  <div class="wiki-shell map-shell">
    <!-- Left Navigation Rail -->
    <aside aria-label="Main navigation" class="left-rail">
      <div class="branding">
        <a class="brand-link" href="../index.html">
          <img src="../assets/layout/hand/icons/icon_reverie_directorate_badge.svg" alt="Reverie Directorate Crest" class="brand-logo" width="110" height="110">
          <span class="brand-title">SOMNARAK</span>
          <span class="brand-subtitle">REVERIE DIRECTORATE ARCHIVE</span>
        </a>
      </div>
      <div class="rail-group">
        <div class="rail-header">DATABASE HUBS</div>
        <ul class="rail-list">
          <li><a href="../index.html">Main Terminal</a></li>
          <li><a href="../departments/index.html">Facility Departments</a></li>
          <li><a href="../locations/index.html">Atlas &amp; Locations</a></li>
          <li><a href="../entities/index.html">Sorrow Entities</a></li>
          <li><a href="../maw/index.html">M.A.W. Armaments</a></li>
          <li><a href="../lore/index.html">Lore &amp; Cosmology</a></li>
        </ul>
      </div>
      <div class="rail-group">
        <div class="rail-header">CARTOGRAPHY &amp; BLUEPRINTS</div>
        <ul class="rail-list">
          <li><a href="hand-of-change-map.html" style="color:#f1df76; font-weight:bold;">Facility Cutaway Map</a></li>
          <li><a href="somnarak-city-map.html">City Master Blueprint</a></li>
        </ul>
      </div>
    </aside>

    <!-- Map Main Content -->
    <main class="wiki-content">
      <!-- Tactical Top Status HUD -->
      <div class="tactical-hud-bar">
        <div class="hud-item"><span class="led-dot led-green"></span> SCHEMATIC VIEWER ONLINE</div>
        <div class="hud-item"><span class="hud-label">FACILITY:</span> 01 THE HAND OF CHANGE</div>
        <div class="hud-item"><span class="hud-label">SECURITY:</span> LEVEL-5 OVERSIGHT</div>
        <div class="hud-item"><span class="hud-label">CONTAINMENT:</span> 8 SECTORS ACTIVE</div>
      </div>

      <!-- Breadcrumbs -->
      <nav class="breadcrumb-trail" aria-label="Breadcrumb">
        <a href="../index.html">SOMNARAK ARCHIVE</a> &gt; 
        <a href="../departments/index.html">DEPARTMENTS</a> &gt; 
        <span>FACILITY 01 BLUEPRINT</span>
      </nav>

      <!-- Panoramic Banner -->
      <div class="category-panoramic-banner">
        <img src="../assets/banners/banner_hero_hand_of_change.svg" alt="Hand of Change" class="panoramic-banner-img">
      </div>

      <!-- Interactive Cutaway Sector Switcher -->
      <div class="map-sector-tabs">
        <button class="sector-tab-btn active" data-target="master">MASTER BLUEPRINT</button>
        <button class="sector-tab-btn" data-target="cut1">CUT 1: UPPER COMMAND (F1 &amp; F2)</button>
        <button class="sector-tab-btn" data-target="cut2">CUT 2: SIPHON FORGE (F3 &amp; F4)</button>
        <button class="sector-tab-btn" data-target="cut3">CUT 3: DEEP VAULT (F5 &amp; F6)</button>
        <button class="sector-tab-btn" data-target="cut4">CUT 4: TABOO GATE (F7 &amp; F8)</button>
      </div>

      <!-- Interactive Map Viewer Canvas -->
      <div class="map-viewer" data-map-width="2400">
        <div class="map-controls">
          <strong>FACILITY CUTAWAY SCHEMATIC:</strong>
          <button data-map-action="in" type="button">ZOOM IN (+)</button>
          <button data-map-action="out" type="button">ZOOM OUT (−)</button>
          <button data-map-action="fit" type="button">FIT SCREEN</button>
          <button data-map-action="native" type="button">100% SCALE</button>
          <output>100%</output>
          <a class="jump-pill" href="../assets/layout/hand/blueprints/THE_HAND_DR_LAYOUT.svg" download style="margin-left:auto;">DOWNLOAD SVG</a>
        </div>
        <div class="map-canvas">
          <img id="facility-map-img" src="../assets/layout/hand/blueprints/THE_HAND_DR_LAYOUT.svg" alt="The Hand of Change Master Blueprint">
        </div>
      </div>

      <!-- Sector Information Card -->
      <div id="sector-info-box" class="wiki-section" style="margin-top:2rem;">
        <div class="section-banner">
          <h2 id="sector-info-title">/// SECTOR BLUEPRINT SPECIFICATIONS</h2>
          <span id="sector-info-tag" class="section-tag">SUBTERRANEAN MATRIX</span>
        </div>
        <p id="sector-info-desc" class="section-desc">
          Facility 01 "The Hand of Change" descends 800 meters into the subterranean crust below Zone A. It houses eight specialized containment and processing floors connected via the central Adamantine elevator column.
        </p>
      </div>

      <!-- Department Directory Links Grid -->
      <div class="hub-grid-3" style="margin-top:2rem;">
        <a href="../departments/floor-1-neutral-command.html" class="pm-entity-card" style="--card-border:#ef5b55;">
          <h3 class="entity-card-name">FLOOR 1: NEUTRAL COMMAND</h3>
          <p class="entity-card-desc">Directorate Spire // Lead: Director Majin</p>
          <span class="jump-btn">ENTER FLOOR 1 →</span>
        </a>
        <a href="../departments/floor-2-maws-keep.html" class="pm-entity-card" style="--card-border:#5b75e8;">
          <h3 class="entity-card-name">FLOOR 2: MAW'S KEEP</h3>
          <p class="entity-card-desc">Heavy Containment Ward // Lead: Dekan</p>
          <span class="jump-btn">ENTER FLOOR 2 →</span>
        </a>
        <a href="../departments/floor-3-extraction-hall.html" class="pm-entity-card" style="--card-border:#e6c843;">
          <h3 class="entity-card-name">FLOOR 3: EXTRACTION HALL</h3>
          <p class="entity-card-desc">M.A.W. Agony Siphons // Lead: Zyrak</p>
          <span class="jump-btn">ENTER FLOOR 3 →</span>
        </a>
        <a href="../departments/floor-4-insight-forge.html" class="pm-entity-card" style="--card-border:#47c978;">
          <h3 class="entity-card-name">FLOOR 4: INSIGHT FORGE</h3>
          <p class="entity-card-desc">Research Laboratories // Lead: Ayshuk</p>
          <span class="jump-btn">ENTER FLOOR 4 →</span>
        </a>
        <a href="../departments/floor-5-border-watch.html" class="pm-entity-card" style="--card-border:#d4d4d8;">
          <h3 class="entity-card-name">FLOOR 5: BORDER WATCH</h3>
          <p class="entity-card-desc">Subterranean Fortress // Lead: Mellda</p>
          <span class="jump-btn">ENTER FLOOR 5 →</span>
        </a>
        <a href="../departments/floor-6-deep-vault.html" class="pm-entity-card" style="--card-border:#be123c;">
          <h3 class="entity-card-name">FLOOR 6: DEEP VAULT</h3>
          <p class="entity-card-desc">Cryogenic Archives &amp; SE-010 // Lead: Marjuk</p>
          <span class="jump-btn">ENTER FLOOR 6 →</span>
        </a>
        <a href="../departments/floor-7-shadow-corps.html" class="pm-entity-card" style="--card-border:#f43f5e;">
          <h3 class="entity-card-name">FLOOR 7: SHADOW CORPS</h3>
          <p class="entity-card-desc">Abyssal Void Docks // Lead: Ishall</p>
          <span class="jump-btn">ENTER FLOOR 7 →</span>
        </a>
        <a href="../departments/floor-8-gate-watch.html" class="pm-entity-card" style="--card-border:#fbbf24;">
          <h3 class="entity-card-name">FLOOR 8: GATE WATCH</h3>
          <p class="entity-card-desc">The Absolute Taboo Gate // Lead: Xyan</p>
          <span class="jump-btn">ENTER FLOOR 8 →</span>
        </a>
      </div>
    </main>
  </div>

  <script src="../assets/js/wiki.js"></script>
  <script>
    // Modular Sector Cut Switcher
    const cuts = {
      master: { src: '../assets/layout/hand/blueprints/THE_HAND_DR_LAYOUT.svg', title: '/// MASTER CUTAWAY SCHEMATIC (ALL 8 FLOORS)', tag: 'CONSOLIDATED FACILITY', desc: 'The complete 8-floor subterranean facility layout descending from the surface Palm Core down to Floor 8 Taboo Gate.' },
      cut1: { src: '../assets/layout/hand/blueprints/the_hand_cut_1_upper_command.svg', title: '/// SECTOR CUT 01: UPPER COMMAND & CONTAINMENT WARD', tag: 'FLOORS 1 & 2', desc: 'Directorate Headquarters, Reset Terminals, Main Observation Deck, and Heavy Kinetic Containment Chambers (SE-001 The Orphaned Bell, SE-002 The Grieving Colossus, SE-005 The Smothering Mother).' },
      cut2: { src: '../assets/layout/hand/blueprints/the_hand_cut_2_industrial_core.svg', title: '/// SECTOR CUT 02: EXTRACTION HALL & INSIGHT FORGE', tag: 'FLOORS 3 & 4', desc: 'M.A.W. Agony Smelting Crucibles, Weapon Anvils, Synaptic Suit Looms, Han Chemical Synthesis Laboratories, and Containment for SE-007 Brume & SE-009 The Memory Weaver.' },
      cut3: { src: '../assets/layout/hand/blueprints/the_hand_cut_3_defense_vault.svg', title: '/// SECTOR CUT 03: BORDER DEFENSE & DEEP CRYO VAULT', tag: 'FLOORS 5 & 6', desc: 'Subterranean Perimeter Fortress, Auto-Turret Batteries, SE-011 Whispering Walls, Cryogenic Archival Vaults, and the Critical Stasis Matrix for SE-010 The Convergence (T-05 ALEPH).' },
      cut4: { src: '../assets/layout/hand/blueprints/the_hand_cut_4_abyss_gate.svg', title: '/// SECTOR CUT 04: VOID DIVING DOCKS & THE TABOO GATE', tag: 'FLOORS 7 & 8', desc: 'Sub-Abyss Submarine Docks, Neural Diver Anchors, SE-014 The Debt Eater, SE-015 The Debt Scale, and the Absolute Taboo Threshold Gate leading beyond Somnarak.' }
    };

    document.querySelectorAll('.sector-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.sector-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const cutKey = btn.dataset.target;
        const cut = cuts[cutKey];
        if (cut) {
          const img = document.getElementById('facility-map-img');
          img.src = cut.src;
          document.getElementById('sector-info-title').textContent = cut.title;
          document.getElementById('sector-info-tag').textContent = cut.tag;
          document.getElementById('sector-info-desc').textContent = cut.desc;
        }
      });
    });
  </script>
</body>
</html>'''

with open(HAND_MAP_PATH, "w", encoding="utf-8") as f:
    f.write(hand_html)

# 2. Update City Map Page
city_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Somnarak City Master Cartography & Blueprint - Somnarak Official Wiki</title>
  <link rel="stylesheet" href="../assets/css/wiki.css">
</head>
<body class="wiki-body map-viewer-page">
  <div class="wiki-shell map-shell">
    <!-- Left Navigation Rail -->
    <aside aria-label="Main navigation" class="left-rail">
      <div class="branding">
        <a class="brand-link" href="../index.html">
          <img src="../assets/layout/hand/icons/icon_reverie_directorate_badge.svg" alt="Reverie Directorate Crest" class="brand-logo" width="110" height="110">
          <span class="brand-title">SOMNARAK</span>
          <span class="brand-subtitle">REVERIE DIRECTORATE ARCHIVE</span>
        </a>
      </div>
      <div class="rail-group">
        <div class="rail-header">DATABASE HUBS</div>
        <ul class="rail-list">
          <li><a href="../index.html">Main Terminal</a></li>
          <li><a href="../locations/index.html">Atlas &amp; Locations</a></li>
          <li><a href="../departments/index.html">Facility Departments</a></li>
          <li><a href="../factions/index.html">Factions &amp; Guilds</a></li>
          <li><a href="../lore/index.html">Lore &amp; Cosmology</a></li>
        </ul>
      </div>
      <div class="rail-group">
        <div class="rail-header">CARTOGRAPHY &amp; BLUEPRINTS</div>
        <ul class="rail-list">
          <li><a href="hand-of-change-map.html">Facility Cutaway Map</a></li>
          <li><a href="somnarak-city-map.html" style="color:#f1df76; font-weight:bold;">City Master Blueprint</a></li>
        </ul>
      </div>
    </aside>

    <!-- Map Main Content -->
    <main class="wiki-content">
      <!-- Tactical Top Status HUD -->
      <div class="tactical-hud-bar">
        <div class="hud-item"><span class="led-dot led-green"></span> URBAN CARTOGRAPHY ONLINE</div>
        <div class="hud-item"><span class="hud-label">METROPOLIS:</span> SOMNARAK ZONES A–E</div>
        <div class="hud-item"><span class="hud-label">ATMOSPHERIC VEIL:</span> 99.4% STABLE</div>
        <div class="hud-item"><span class="hud-label">PERIMETER:</span> 400M BULWARK ACTIVE</div>
      </div>

      <!-- Breadcrumbs -->
      <nav class="breadcrumb-trail" aria-label="Breadcrumb">
        <a href="../index.html">SOMNARAK ARCHIVE</a> &gt; 
        <a href="../locations/index.html">LOCATIONS</a> &gt; 
        <span>CITY MASTER BLUEPRINT</span>
      </nav>

      <!-- Panoramic Banner -->
      <div class="category-panoramic-banner">
        <img src="../assets/banners/banner_hero_somnarak_city.svg" alt="Somnarak City" class="panoramic-banner-img">
      </div>

      <!-- Interactive Cutaway District Switcher -->
      <div class="map-sector-tabs">
        <button class="sector-tab-btn active" data-target="master">MASTER BLUEPRINT</button>
        <button class="sector-tab-btn" data-target="cut1">CUT 1: CORE &amp; WEST WARD (ZONE A &amp; B)</button>
        <button class="sector-tab-btn" data-target="cut2">CUT 2: INDUSTRIAL EAST (ZONE C &amp; D)</button>
        <button class="sector-tab-btn" data-target="cut3">CUT 3: PERIMETER &amp; WASTELAND (ZONE E)</button>
        <button class="sector-tab-btn" data-target="cut4">CUT 4: THE WEEPING CANALS</button>
      </div>

      <!-- Interactive Map Viewer Canvas -->
      <div class="map-viewer city" data-map-width="2400">
        <div class="map-controls">
          <strong>METROPOLITAN MASTER BLUEPRINT:</strong>
          <button data-map-action="in" type="button">ZOOM IN (+)</button>
          <button data-map-action="out" type="button">ZOOM OUT (−)</button>
          <button data-map-action="fit" type="button">FIT SCREEN</button>
          <button data-map-action="native" type="button">100% SCALE</button>
          <output>100%</output>
          <a class="jump-pill" href="../assets/layout/city/blueprints/SOMNARAK_CITY_LAYOUT.svg" download style="margin-left:auto;">DOWNLOAD SVG</a>
        </div>
        <div class="map-canvas">
          <img id="city-map-img" src="../assets/layout/city/blueprints/SOMNARAK_CITY_LAYOUT.svg" alt="Somnarak City Master Blueprint">
        </div>
      </div>

      <!-- District Information Card -->
      <div id="district-info-box" class="wiki-section" style="margin-top:2rem;">
        <div class="section-banner">
          <h2 id="district-info-title">/// METROPOLITAN CARTOGRAPHY SPECIFICATIONS</h2>
          <span id="district-info-tag" class="section-tag">ZONING ARCHITECTURE</span>
        </div>
        <p id="district-info-desc" class="section-desc">
          Somnarak is structured into five concentric metropolitan zones enclosed by the 400-meter Perimeter Bulwark, centered upon the Directorate Spire and the subterranean roots of the Alpha Tree.
        </p>
      </div>

      <!-- Zone Atlas Directory Cards -->
      <div class="hub-grid-3" style="margin-top:2rem;">
        <a href="../locations/zone-a-core-nexus.html" class="pm-entity-card" style="--card-border:#ef5b55;">
          <h3 class="entity-card-name">ZONE A: CORE NEXUS</h3>
          <p class="entity-card-desc">Directorate Spire // Alpha Tree Root Wells</p>
          <span class="jump-btn">EXPLORE ZONE A →</span>
        </a>
        <a href="../locations/zone-b-west-ward.html" class="pm-entity-card" style="--card-border:#38bdf8;">
          <h3 class="entity-card-name">ZONE B: WEST WARD</h3>
          <p class="entity-card-desc">Residential Mega-Blocks // Veil Filtration Dome</p>
          <span class="jump-btn">EXPLORE ZONE B →</span>
        </a>
        <a href="../locations/zone-c-collectors-row.html" class="pm-entity-card" style="--card-border:#10b981;">
          <h3 class="entity-card-name">ZONE C: COLLECTOR'S ROW</h3>
          <p class="entity-card-desc">Pre-Cataclysm Relic Bazaars // Scrap Foundries</p>
          <span class="jump-btn">EXPLORE ZONE C →</span>
        </a>
        <a href="../locations/zone-d-forge-and-gardens.html" class="pm-entity-card" style="--card-border:#47c978;">
          <h3 class="entity-card-name">ZONE D: FORGE &amp; GARDENS</h3>
          <p class="entity-card-desc">Bio-Synthetic Greenhouses // Han Flora Cultivation</p>
          <span class="jump-btn">EXPLORE ZONE D →</span>
        </a>
        <a href="../locations/zone-e-perimeter-bulwark.html" class="pm-entity-card" style="--card-border:#f59e0b;">
          <h3 class="entity-card-name">ZONE E: PERIMETER BULWARK</h3>
          <p class="entity-card-desc">400m Titanium Curtain Wall // Frontier Gates</p>
          <span class="jump-btn">EXPLORE ZONE E →</span>
        </a>
        <a href="../locations/the-desolate.html" class="pm-entity-card" style="--card-border:#ef4444;">
          <h3 class="entity-card-name">THE DESOLATE (황무지)</h3>
          <p class="entity-card-desc">Radioactive Crystalline Wasteland // Distortions</p>
          <span class="jump-btn">EXPLORE WASTELAND →</span>
        </a>
      </div>
    </main>
  </div>

  <script src="../assets/js/wiki.js"></script>
  <script>
    // Modular City District Cut Switcher
    const cityCuts = {
      master: { src: '../assets/layout/city/blueprints/SOMNARAK_CITY_LAYOUT.svg', title: '/// MASTER CITY BLUEPRINT (ALL 5 ZONES)', tag: 'CONSOLIDATED METROPOLIS', desc: 'Master urban blueprint covering Zones A through E, the Alpha Tree Spire, and the outer radioactive Desolate frontier.' },
      cut1: { src: '../assets/layout/city/blueprints/city_cut_1_core_and_west.svg', title: '/// CUT 01: METROPOLITAN CORE & WEST WARD', tag: 'ZONE A & ZONE B', desc: 'Central Directorate Command Spire, Alpha Tree Rootwells, and West Ward Residential Mega-Blocks beneath the atmospheric Veil dome.' },
      cut2: { src: '../assets/layout/city/blueprints/city_cut_2_industrial_east.svg', title: '/// CUT 02: COLLECTOR\'S ROW & FORGE GARDENS', tag: 'ZONE C & ZONE D', desc: 'Pre-Cataclysm Relic Bazaars, Doha\'s underground Han refineries, Bio-Synthetic Botanical Domes, and Han Flora research foundries.' },
      cut3: { src: '../assets/layout/city/blueprints/city_cut_3_perimeter_frontier.svg', title: '/// CUT 03: PERIMETER BULWARK & THE DESOLATE', tag: 'ZONE E & WASTELAND', desc: '400-Meter Titanium Battlements, Watchtower 01, Gate of Sighs, Horizon Caravan Departure Trail, and Hollow Glass vitrified plain.' },
      cut4: { src: '../assets/layout/city/blueprints/city_cut_4_subterranean_canals.svg', title: '/// CUT 04: THE WEEPING & SUB-RAIL GRID', tag: 'HYDROLOGY & UNDER-RAIL', desc: 'Subterranean effluent waterway network channeling liquefied Han remorse from Siphon Stations A-1, B-4, and C-8 into Facility 01.' }
    };

    document.querySelectorAll('.sector-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.sector-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const cutKey = btn.dataset.target;
        const cut = cityCuts[cutKey];
        if (cut) {
          const img = document.getElementById('city-map-img');
          img.src = cut.src;
          document.getElementById('district-info-title').textContent = cut.title;
          document.getElementById('district-info-tag').textContent = cut.tag;
          document.getElementById('district-info-desc').textContent = cut.desc;
        }
      });
    });
  </script>
</body>
</html>'''

with open(CITY_MAP_PATH, "w", encoding="utf-8") as f:
    f.write(city_html)

print("Updated both Map pages with Interactive Modular SVG Cutaway Viewers.")
