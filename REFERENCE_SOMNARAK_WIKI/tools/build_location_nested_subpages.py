import os

def generate_location_subpages():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    loc_dir = os.path.join(wiki_root, "locations")
    os.makedirs(loc_dir, exist_ok=True)

    zones = [
        {
            "file": "zone-a-central-spire.html",
            "title": "Zone A Central Spire &amp; High Council Bastion",
            "code": "ZONE-A-CITADEL",
            "clearance": "HIGH COUNCIL RESTRICTED",
            "hero_img": "../assets/layout/city/blueprints/zone-a-blueprint.svg",
            "lead": "THE HIGH COUNCIL // ARCHITECT EMBASSY",
            "content": '''
<h2>1. Zone A Geographic &amp; Civic Overview</h2>
<p>Rising at the geometric center of Somnarak, the <strong>Central Spire</strong> is the supreme administrative and ideological peak of the city. Enclosed within the pristine <strong>Sovereign Veil</strong>, Zone A suffers almost zero ambient weeping, as structural grief is siphoned downward into the lower outer wards.</p>

<h2>2. Demographics &amp; Infrastructure</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Demographic Metric</th>
      <th>Statistic</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Permanent Population</td>
      <td>142,000 Citizens</td>
      <td>High Council Executives, Chief Researchers, Directorate Liaisons</td>
    </tr>
    <tr>
      <td>Ambient Han Flux</td>
      <td>0.02 ppm (Negligible)</td>
      <td>Active triple-filter atmospheric scrubbers</td>
    </tr>
    <tr>
      <td>Security Density</td>
      <td>1 Giltong Warden per 12 Citizens</td>
      <td>Automated biometric surveillance turrets</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },
        {
            "file": "zone-b-giltong-slums.html",
            "title": "Zone B West Ward &amp; Giltong Iron Alleys",
            "code": "ZONE-B-WEST",
            "clearance": "LEVEL 2 CIVILIAN ACCESS",
            "hero_img": "../assets/layout/city/blueprints/zone-b-blueprint.svg",
            "lead": "GILTONG ENFORCERS // LOCAL CHIEFS",
            "content": '''
<h2>1. The Iron Alleys Overview</h2>
<p>The <strong>West Ward</strong> of Somnarak is a dense, labyrinthine network of rusty iron tenement stacks, narrow catwalks, and crowded subterranean markets. Governed by the ruthless <strong>Giltong Enforcers</strong>, the district operates under strict martial law and nocturnal curfews.</p>

<h2>2. Hazard &amp; Containment Levels</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Sub-District</th>
      <th>Primary Industry</th>
      <th>Taboo Violation Rate</th>
      <th>Security Response</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Upper Iron Row</td>
      <td>M.A.W. Scrap Refinement</td>
      <td>Low (5%)</td>
      <td>Standard Giltong Patrols</td>
    </tr>
    <tr>
      <td>The Weeping Gutters</td>
      <td>Raw Han Siphoning</td>
      <td>High (38%)</td>
      <td>Lethal Cleansing Raids</td>
    </tr>
    <tr>
      <td>Deep Pipe Labyrinth</td>
      <td>Illicit Memory Exchanges</td>
      <td>Severe (65%)</td>
      <td>Memory Washers Dispatched</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },
        {
            "file": "zone-c-auction-houses.html",
            "title": "Zone C Collector's Row &amp; Relic Black Markets",
            "code": "ZONE-C-MARKET",
            "clearance": "BLACK MARKET PERMIT REQUIRED",
            "hero_img": "../assets/layout/city/blueprints/zone-c-blueprint.svg",
            "lead": "THE COLLECTORS // HORIZON CARAVAN",
            "content": '''
<h2>1. Collector's Row Market Structure</h2>
<p><strong>Collector's Row</strong> serves as the premier underground emporium for forbidden Sorrow Relics, salvaged M.A.W. weaponry, and unregistered Han batteries smuggled from the Desolate. Under the protection of <a class="wiki-link" href="../characters/joon.html">Joon</a> and <a class="wiki-link" href="../factions/the-collectors.html">The Collectors</a>, high-stakes auctions dictate the underground economy.</p>

<h2>2. Black Market Trade Registry</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Contraband Category</th>
      <th>Average Auction Value</th>
      <th>Risk Rating</th>
      <th>Giltong Seizure Policy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Extracted Sorrow Seeds</td>
      <td>250,000 Han Coins</td>
      <td><span class="badge badge-apocrypha">EXTREME</span></td>
      <td>Immediate Execution of Possessor</td>
    </tr>
    <tr>
      <td>Grade III M.A.W. Weapons</td>
      <td>45,000 Han Coins</td>
      <td><span class="badge badge-morphean">HIGH</span></td>
      <td>Confiscation &amp; Fine</td>
    </tr>
    <tr>
      <td>Preserved Memory Vials</td>
      <td>12,000 Han Coins</td>
      <td><span class="badge badge-somna">MODERATE</span></td>
      <td>Memory Erasure of Buyer</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },
        {
            "file": "zone-d-han-refineries.html",
            "title": "Zone D Forge &amp; Gardens Industrial Smelters",
            "code": "ZONE-D-FORGE",
            "clearance": "LEVEL 3 INDUSTRIAL CLEARANCE",
            "hero_img": "../assets/layout/city/blueprints/zone-d-blueprint.svg",
            "lead": "SMELTER GUILD // EXTRACTION ENGINEERS",
            "content": '''
<h2>1. Industrial Smelter Infrastructure</h2>
<p>Zone D houses the colossal thermal smelters and Han crystallization towers that power Somnarak's electrical grid and public infrastructure. Massive exhaust stacks emit iridescent violet smoke day and night as raw grief fluid is boiled into stable solid fuel blocks.</p>

<h2>2. Refining Metrics &amp; Smelter Yields</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Smelter Complex</th>
      <th>Daily Inflow</th>
      <th>Refined Output</th>
      <th>Thermal Operating Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Smelter Tower Alpha</td>
      <td>50,000 Liters Raw Han</td>
      <td>12,000 Solid Fuel Blocks</td>
      <td>1,450°C</td>
    </tr>
    <tr>
      <td>Smelter Tower Beta</td>
      <td>85,000 Liters Raw Han</td>
      <td>22,500 Solid Fuel Blocks</td>
      <td>1,620°C</td>
    </tr>
    <tr>
      <td>The Crystal Garden Vats</td>
      <td>20,000 Liters Pure Grief</td>
      <td>500 M.A.W. Ingot Cores</td>
      <td>2,100°C</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },
        {
            "file": "zone-e-frontier-ramparts.html",
            "title": "Zone E Perimeter Bulwark &amp; Desolate Ramparts",
            "code": "ZONE-E-BULWARK",
            "clearance": "MILITARY LEVEL 4 CLEARANCE",
            "hero_img": "../assets/layout/city/blueprints/zone-e-blueprint.svg",
            "lead": "THE WARDENS // BORDER GARRISON",
            "content": '''
<h2>1. The Outer Perimeter Bulwark</h2>
<p>Zone E marks the edge of human civilization in Somnarak. The 80-meter-high concrete and Han-steel ramparts repel continuous waves of wilderness anomalies from The Desolate, supported by <a class="wiki-link" href="../factions/the-wardens.html">The Wardens</a> and heavy automated rail batteries.</p>

<h2>2. Frontier Defense Statistics</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Defense Bastion</th>
      <th>Artillery Battery</th>
      <th>Monthly Incursion Count</th>
      <th>Breach Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bastion North-Gate</td>
      <td>Twin 400mm Han Railguns</td>
      <td>48 Incursions</td>
      <td>100% Repelled</td>
    </tr>
    <tr>
      <td>Bastion Iron-Crag</td>
      <td>Acoustic Shockwave Mortars</td>
      <td>92 Incursions</td>
      <td>1 Minor Breach (Repaired)</td>
    </tr>
    <tr>
      <td>Bastion Desolate-Watch</td>
      <td>Thermal Plasma Projectors</td>
      <td>114 Incursions</td>
      <td>100% Repelled</td>
    </tr>
  </tbody>
</table>
</div>
'''
        }
    ]

    left_rail_template = '''
    <aside class="left-rail">
      <div class="site-mark">
        <a href="../index.html">
          <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak Emblem">
          <b>SOMNARAK</b>
          <span>OFFICIAL WIKI ARCHIVE</span>
        </a>
      </div>
      <nav aria-label="Wiki navigation" class="left-links">
        <section>
          <h2>DATABASE HUBS</h2>
          <a href="../index.html">Main Overview</a>
          <a href="../characters/index.html">Characters Hub</a>
          <a href="../lore/index.html">Lore &amp; Cosmology</a>
          <a href="../locations/index.html">Locations &amp; Atlas</a>
          <a href="../factions/index.html">Factions &amp; Guilds</a>
          <a href="../departments/index.html">Facility Floors</a>
          <a href="../entities/index.html">Sorrow Entities</a>
          <a href="../maw/index.html">M.A.W. Equipment</a>
          <a href="../mechanics/index.html">Systems &amp; Mechanics</a>
        </section>
        <section>
          <h2>ATLAS &amp; ZONES</h2>
          <a href="../locations/zone-a-central-spire.html">Zone A Central Spire</a>
          <a href="../locations/zone-b-giltong-slums.html">Zone B West Ward</a>
          <a href="../locations/zone-c-auction-houses.html">Zone C Collector's Row</a>
          <a href="../locations/zone-d-han-refineries.html">Zone D Smelters</a>
          <a href="../locations/zone-e-frontier-ramparts.html">Zone E Frontier Bulwark</a>
          <a href="../atlas/somnarak-city-map.html">Somnarak City Map</a>
          <a href="../atlas/hand-of-change-map.html">Hand of Change Map</a>
        </section>
      </nav>
    </aside>
'''

    for z in zones:
        out_path = os.path.join(loc_dir, z["file"])
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{z["title"]} — Somnarak Official Wiki</title>
  <link rel="stylesheet" href="../assets/css/wiki.css">
  <link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg">
  <script defer src="../assets/js/wiki.js"></script>
</head>
<body>
  <!-- Top Utility Bar -->
  <header class="utility">
    <div class="utility-left">
      <button class="nav-open" aria-label="Open navigation" type="button">☰</button>
      <a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
      <span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
    </div>
    <nav aria-label="Main navigation">
      <a href="../index.html">Main page</a>
      <a href="../characters/index.html">Characters</a>
      <a href="../lore/index.html">Lore</a>
      <a href="../locations/index.html">Atlas</a>
      <a href="../factions/index.html">Factions</a>
      <a href="../departments/index.html">Facility</a>
      <a href="../entities/index.html">Entities</a>
      <a href="../maw/index.html">M.A.W.</a>
      <a href="../mechanics/index.html">Mechanics</a>
    </nav>
    <div class="search">
      <input id="search" data-index="../data/search.json" placeholder="Search archive..." autocomplete="off">
      <div id="results"></div>
    </div>
  </header>

  <!-- Main Grid Layout -->
  <div class="wiki-shell">
    {left_rail_template}

    <main class="wiki-main" id="content">
      <nav class="breadcrumb-bar" aria-label="Breadcrumb">
        <a href="../index.html">Home</a>
        <span class="breadcrumb-sep">&gt;</span>
        <a href="../locations/index.html">Atlas &amp; Locations</a>
        <span class="breadcrumb-sep">&gt;</span>
        <span class="breadcrumb-current">{z['title']}</span>
      </nav>

      <header class="article-header">
        <div class="hero-frame">
          <img src="{z['hero_img']}" alt="{z['title']}" class="hero-banner-img">
        </div>
        <div class="header-meta-wrap">
          <div class="article-badges">
            <span class="badge badge-gold">{z['code']}</span>
            <span class="badge badge-somna">{z['clearance']}</span>
          </div>
          <h1 class="article-title">{z['title']}</h1>
          <p class="article-subtitle">GOVERNING AUTHORITY: {z['lead']}</p>
        </div>
      </header>

      <nav class="wiki-toc" aria-label="Table of contents">
        <div class="toc-title">SECTOR ATLAS CONTENTS</div>
        <ol class="toc-list">
          <li><a href="#section-1">1. Geographic &amp; Infrastructure Overview</a></li>
          <li><a href="#section-2">2. Sector Demographics &amp; Tactical Statistics</a></li>
        </ol>
      </nav>

      <article class="article-body">
        {z['content']}
      </article>

      <footer class="article-footer">
        <div class="footer-categories">
          <strong>Categories:</strong>
          <a href="../locations/index.html">Somnarak Atlas</a> |
          <a href="../index.html">Somnarak Universe</a> |
          <a href="../lore/index.html">Urban Districts</a>
        </div>
        <div class="footer-disclaimer">
          Content is available under Somnarak Directorate Archival License unless otherwise noted.
        </div>
      </footer>

      <section class="cross-reference-section">
        <div class="cross-ref-header">CANONICAL CROSS-LINKS &amp; ATLAS CONNECTIONS</div>
        <div class="cross-ref-grid">
          <a href="../locations/index.html" class="cross-ref-card">
            <img src="../assets/layout/city/icons/somnarak_city_icon_styled.svg" alt="City Atlas">
            <div class="cross-ref-meta"><span class="cross-ref-cat">SOMNARAK ATLAS</span><span class="cross-ref-title">ALL 5 ZONES</span></div>
          </a>
          <a href="../atlas/somnarak-city-map.html" class="cross-ref-card">
            <img src="../assets/layout/city/blueprints/zone-a-blueprint.svg" alt="City Map">
            <div class="cross-ref-meta"><span class="cross-ref-cat">URBAN MAP</span><span class="cross-ref-title">FULL CITY BLUEPRINT</span></div>
          </a>
          <a href="../factions/index.html" class="cross-ref-card">
            <img src="../assets/banners/banner_hero_factions_council.svg" alt="Factions">
            <div class="cross-ref-meta"><span class="cross-ref-cat">POWER STRUCTURE</span><span class="cross-ref-title">FACTIONS &amp; GUILDS</span></div>
          </a>
          <a href="../lore/the-cycle-and-absolvohan.html" class="cross-ref-card">
            <img src="../assets/icons/ref_absolvohan.svg" alt="Absolvohan">
            <div class="cross-ref-meta"><span class="cross-ref-cat">CANON LORE</span><span class="cross-ref-title">1,778 CYCLES</span></div>
          </a>
        </div>
      </section>
    </main>
  </div>
</body>
</html>'''
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
    print(f"Successfully generated {len(zones)} location nested subpages!")

if __name__ == "__main__":
    generate_location_subpages()
