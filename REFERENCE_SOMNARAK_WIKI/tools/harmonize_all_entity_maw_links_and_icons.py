import os
import re

def harmonize():
    wiki_root = "/home/user/01_Somnarak_Wiki"

    # 1. Update entities/index.html with exact existing files and canonical names
    entities_hub_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sorrow Entities Codex - Somnarak Official Wiki</title>
  <link rel="stylesheet" href="../assets/css/wiki.css">
  <link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg">
  <script defer src="../assets/js/wiki.js"></script>
</head>
<body class="wiki-body">
  <!-- Top Utility Navigation Bar -->
  <header class="utility">
    <div class="utility-left">
      <button aria-label="Open navigation" class="nav-open" type="button">☰</button>
      <a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
      <span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
    </div>
    <nav aria-label="Main navigation">
      <a href="../index.html">Main page</a>
      <a href="../characters/index.html">Characters</a>
      <a href="../lore/index.html">Lore</a>
      <a href="../locations/index.html">Locations</a>
      <a href="../factions/index.html">Factions</a>
      <a href="../departments/index.html">Departments</a>
      <a href="../entities/index.html" class="selected">Sorrow Entities</a>
      <a href="../maw/index.html">M.A.W.</a>
      <a href="../mechanics/index.html">Mechanics</a>
    </nav>
    <div class="search">
      <input aria-label="Search" data-index="../data/search.json" id="search" placeholder="Search archive..." autocomplete="off"/>
      <div id="results"></div>
    </div>
  </header>

  <div class="wiki-shell">
    <!-- Left Navigation Rail -->
    <aside aria-label="Main navigation" class="left-rail">
      <div class="branding">
        <a class="brand-link" href="../index.html">
          <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak Seal" class="brand-logo" width="96" height="96">
          <span class="brand-title">SOMNARAK</span>
          <span class="brand-subtitle">REVERIE DIRECTORATE ARCHIVE</span>
        </a>
      </div>
      
      <div class="rail-group">
        <div class="rail-header">DATABASE HUBS</div>
        <ul class="rail-list">
          <li><a href="../index.html">Main Terminal</a></li>
          <li><a href="../characters/index.html">Characters & Echo-Cores</a></li>
          <li><a href="../lore/index.html">Lore & Cosmology</a></li>
          <li><a href="../locations/index.html">Atlas & Locations</a></li>
          <li><a href="../factions/index.html">Factions & Guilds</a></li>
          <li><a href="../departments/index.html">Facility Departments</a></li>
          <li><a href="../entities/index.html" style="color:#f1df76; font-weight:bold;">Sorrow Entities</a></li>
          <li><a href="../maw/index.html">M.A.W. Armaments</a></li>
          <li><a href="../mechanics/index.html">Systems & Mechanics</a></li>
        </ul>
      </div>

      <div class="rail-group">
        <div class="rail-header">THE NINE ECHO-CORES</div>
        <ul class="rail-list">
          <li><a href="../characters/the-director-majin.html">Director Majin</a></li>
          <li><a href="../characters/the-secretary-seiyon.html">Secretary Seiyon</a></li>
          <li><a href="../characters/the-containment-lead-dekan.html">Containment: Dekan</a></li>
          <li><a href="../characters/the-extraction-lead-zyrak.html">Extraction: Zyrak</a></li>
          <li><a href="../characters/the-research-lead-ayshuk.html">Research: Ayshuk</a></li>
          <li><a href="../characters/the-border-lead-mellda.html">Border: Mellda</a></li>
          <li><a href="../characters/the-archive-lead-marjuk.html">Archive: Marjuk</a></li>
          <li><a href="../characters/the-outsider-ishall.html">Outsider: Ishall</a></li>
          <li><a href="../characters/the-exile-xyan.html">Exile: Xyan</a></li>
        </ul>
      </div>

      <div class="rail-group">
        <div class="rail-header">CARTOGRAPHY & SCHEMATICS</div>
        <ul class="rail-list">
          <li><a href="../atlas/hand-of-change-map.html">Facility Cutaway Map</a></li>
          <li><a href="../atlas/somnarak-city-map.html">City Master Blueprint</a></li>
        </ul>
      </div>
    </aside>

    <!-- Main Content Area -->
    <main id="content" class="wiki-content">
      <!-- Tactical Top Status HUD -->
      <div class="tactical-hud-bar">
        <div class="hud-item"><span class="led-dot led-green"></span> ARCHIVE ONLINE</div>
        <div class="hud-item"><span class="hud-label">CLEARANCE:</span> LEVEL 5 RESTRICTED</div>
        <div class="hud-item"><span class="hud-label">DIRECTORY:</span> ENTITIES</div>
        <div class="hud-item"><span class="hud-label">STABILITY:</span> 99.4% NOMINAL</div>
      </div>

      <!-- Breadcrumbs -->
      <nav class="breadcrumb-trail" aria-label="Breadcrumb">
        <a href="../index.html">SOMNARAK ARCHIVE</a> &gt; <span>SORROW ENTITIES</span>
      </nav>

      <!-- Panoramic Hero Banner -->
      <div class="category-panoramic-banner">
        <img src="../assets/banners/banner_hero_entities.svg" alt="SORROW ENTITIES CODEX" class="panoramic-banner-img">
      </div>

      <!-- Fast Jump Bar -->
      <div class="fast-jump-nav">
        <span class="fast-jump-title">/// DIRECT ACCESS:</span>
        <div class="fast-jump-pills">
          <a href="../entities/index.html" class="jump-pill active">Entities Codex</a>
          <a href="../maw/index.html" class="jump-pill">M.A.W. Arsenal</a>
          <a href="../characters/index.html" class="jump-pill">Echo-Cores &amp; Cast</a>
          <a href="../departments/index.html" class="jump-pill">Facility Floors</a>
          <a href="../lore/index.html" class="jump-pill">Lore Chronicles</a>
          <a href="../locations/index.html" class="jump-pill">Metropolitan Atlas</a>
          <a href="../factions/index.html" class="jump-pill">Factions &amp; Guilds</a>
          <a href="../mechanics/index.html" class="jump-pill">Combat Systems</a>
        </div>
      </div>

      <div class="wiki-section">
        <div class="section-banner">
          <h2>/// CANONICAL SORROW ENTITY CONTAINMENT DIRECTORY</h2>
          <span class="section-tag">ALL 10 CANONICAL PHENOMENA & REGISTRIES</span>
        </div>
        <p class="section-desc">
          Sorrow Entities (슬픔의 존재) are metaphysical manifestations born of human grief, regret, and Han energy. Each entity is secured in dedicated containment sectors within Facility 01 (The Hand of Change) under strict SECC protocols.
        </p>

        <div class="hub-grid-3" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px; margin-top:1.5rem;">
          
          <!-- SE-001 -->
          <div class="pm-entity-card" style="border:2px solid #ef5b55; background:#0c080a; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-001.svg" alt="SE-001" style="width:64px; height:64px; border:2px solid #ef5b55; border-radius:6px; background:#180407;">
              <div style="text-align:right;">
                <span class="badge badge-crimson">PHANTASM (δ)</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 2 // MAW'S KEEP</div>
              </div>
            </div>
            <h3 style="color:#ef5b55; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-001: WEEPING COLOSSUS</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Colossal black iron titan weeping molten silver tears through a cracked basalt mask. Bleeds crimson Han channels into subterranean vaults.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#ef5b55;">GRUDGE (HP)</span></span>
              <span><b>WORK:</b> ATTACHMENT</span>
            </div>
            <a href="se-001-the-orphaned-bell.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-002 / Grieving Colossus -->
          <div class="pm-entity-card" style="border:2px solid #ef5b55; background:#0c080a; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-001.svg" alt="SE-002" style="width:64px; height:64px; border:2px solid #ef5b55; border-radius:6px; background:#180407;">
              <div style="text-align:right;">
                <span class="badge badge-crimson">PHANTASM (δ)</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 2 // MAW'S KEEP</div>
              </div>
            </div>
            <h3 style="color:#ef5b55; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-002: GRIEVING COLOSSUS</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Subterranean titan manifestation of physical sorrow. High kinetic impact resistance and heavy containment threshold.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#ef5b55;">GRUDGE (HP)</span></span>
              <span><b>WORK:</b> REPRESSION</span>
            </div>
            <a href="se-002-the-grieving-colossus.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-003 / Wilderness Tide -->
          <div class="pm-entity-card" style="border:2px solid #38bdf8; background:#040e18; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-003.svg" alt="SE-003" style="width:64px; height:64px; border:2px solid #38bdf8; border-radius:6px; background:#031526;">
              <div style="text-align:right;">
                <span class="badge badge-somna">SOMNA (β)</span>
                <div style="font-size:0.75rem; color:#38bdf8; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 3 // EXTRACTION</div>
              </div>
            </div>
            <h3 style="color:#38bdf8; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-003: THREAD OF MEMORY</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Pale silver spider-silk loom weaving forgotten memories of dead cycles. Discharges psychic needle vibrations affecting employee sanity.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> INSIGHT</span>
            </div>
            <a href="se-003-the-wilderness-tide.html" class="jump-btn" style="display:block; text-align:center; background:#0c4a6e; color:#bae6fd; border:1px solid #38bdf8; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-005 / Smothering Mother -->
          <div class="pm-entity-card" style="border:2px solid #71efaf; background:#04140d; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-008.svg" alt="SE-005" style="width:64px; height:64px; border:2px solid #71efaf; border-radius:6px; background:#02140d;">
              <div style="text-align:right;">
                <span class="badge badge-green" style="background:#064e3b; color:#71efaf; border:1px solid #71efaf;">AETHER (α)</span>
                <div style="font-size:0.75rem; color:#71efaf; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 1 // NEUTRAL</div>
              </div>
            </div>
            <h3 style="color:#71efaf; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-005: SMOTHERING CRADLE</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Gilded cradle sheltering an ethereal lullaby of maternal solace. High harmonic extraction stability under basic supervision.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> ATTACHMENT</span>
            </div>
            <a href="se-005-the-smothering-mother.html" class="jump-btn" style="display:block; text-align:center; background:#064e3b; color:#a7f3d0; border:1px solid #71efaf; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-007 / Brume -->
          <div class="pm-entity-card" style="border:2px solid #ef5b55; background:#0c080a; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-007.svg" alt="SE-007" style="width:64px; height:64px; border:2px solid #ef5b55; border-radius:6px; background:#1f0608;">
              <div style="text-align:right;">
                <span class="badge badge-somna">SOMNA (β)</span>
                <div style="font-size:0.75rem; color:#ef5b55; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 6 // DEEP VAULT</div>
              </div>
            </div>
            <h3 style="color:#ef5b55; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-007: ASHEN SCRIBE (BRUME)</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Tower of charcoal-burnt manuscript codices recording fatal facility debts. Inscribes searing crimson marks onto approaching researchers.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#ef5b55;">GRUDGE (HP)</span></span>
              <span><b>WORK:</b> INSIGHT</span>
            </div>
            <a href="se-007-brume.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-009 / Memory Weaver -->
          <div class="pm-entity-card" style="border:2px solid #38bdf8; background:#041b2c; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-009.svg" alt="SE-009" style="width:64px; height:64px; border:2px solid #38bdf8; border-radius:6px; background:#041b2c;">
              <div style="text-align:right;">
                <span class="badge badge-somna">SOMNA (β)</span>
                <div style="font-size:0.75rem; color:#38bdf8; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 5 // BORDER WATCH</div>
              </div>
            </div>
            <h3 style="color:#38bdf8; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-009: DROWNED BELL (WEAVER)</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Verdigris bronze church bell submerged in subterranean tears. Emits acoustic tidal resonances that induce melancholic stupor.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> REPRESSION</span>
            </div>
            <a href="se-009-the-memory-weaver.html" class="jump-btn" style="display:block; text-align:center; background:#0e7490; color:#cffafe; border:1px solid #38bdf8; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-010 / Convergence -->
          <div class="pm-entity-card" style="border:2px solid #c084fc; background:#130421; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-014.svg" alt="SE-010" style="width:64px; height:64px; border:2px solid #c084fc; border-radius:6px; background:#130421;">
              <div style="text-align:right;">
                <span class="badge" style="background:#4c1d95; color:#e9d5ff; border:1px solid #c084fc;">APOCRYPHA (ω)</span>
                <div style="font-size:0.75rem; color:#c084fc; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 8 // GATE WATCH</div>
              </div>
            </div>
            <h3 style="color:#c084fc; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-010: THE CONVERGENCE</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Pulsating abyssal singularity of all 1,778 cycle resets capable of unraveling structural reality across the entire facility.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#ffffff;">VOID (% HP)</span></span>
              <span><b>WORK:</b> INSIGHT</span>
            </div>
            <a href="se-010-the-convergence.html" class="jump-btn" style="display:block; text-align:center; background:#3b0764; color:#e9d5ff; border:1px solid #c084fc; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-011 / Whispering Walls -->
          <div class="pm-entity-card" style="border:2px solid #ef5b55; background:#1c0709; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-011.svg" alt="SE-011" style="width:64px; height:64px; border:2px solid #ef5b55; border-radius:6px; background:#1f0608;">
              <div style="text-align:right;">
                <span class="badge badge-crimson">PHANTASM (δ)</span>
                <div style="font-size:0.75rem; color:#ef5b55; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 2 // MAW'S KEEP</div>
              </div>
            </div>
            <h3 style="color:#ef5b55; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-011: WHISPERING IRON MAIDEN</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Spiked iron executioner sarcophagus housing a weeping bronze faceplate. Thrusts internal thorns inward when emotional resonance peaks.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#ef5b55;">GRUDGE (HP)</span></span>
              <span><b>WORK:</b> REPRESSION</span>
            </div>
            <a href="se-011-the-whispering-walls.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-014 / Debt Eater -->
          <div class="pm-entity-card" style="border:2px solid #c084fc; background:#130421; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-014.svg" alt="SE-014" style="width:64px; height:64px; border:2px solid #c084fc; border-radius:6px; background:#130421;">
              <div style="text-align:right;">
                <span class="badge" style="background:#4c1d95; color:#e9d5ff; border:1px solid #c084fc;">APOCRYPHA (ω)</span>
                <div style="font-size:0.75rem; color:#c084fc; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 7 // SHADOW CORPS</div>
              </div>
            </div>
            <h3 style="color:#c084fc; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-014: HOLLOW DEBT EATER</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Porcelain tragedy mask singing an opera of total existential void. Bypasses physical wards to disintegrate consciousness.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#ffffff;">VOID (% HP)</span></span>
              <span><b>WORK:</b> INSIGHT</span>
            </div>
            <a href="se-014-the-debt-eater.html" class="jump-btn" style="display:block; text-align:center; background:#3b0764; color:#e9d5ff; border:1px solid #c084fc; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-015 / Debt Scale / Sovereign Crown -->
          <div class="pm-entity-card" style="border:2px solid #f1df76; background:#1c1402; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-015.svg" alt="SE-015" style="width:64px; height:64px; border:2px solid #f1df76; border-radius:6px; background:#1c1402;">
              <div style="text-align:right;">
                <span class="badge" style="background:#4c1d95; color:#e9d5ff; border:1px solid #c084fc;">APOCRYPHA (ω)</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 8 // GATE WATCH</div>
              </div>
            </div>
            <h3 style="color:#f1df76; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-015: SOVEREIGN DEBT SCALE</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Jagged black iron crown encircled by a golden Absolvohan halo. Catastrophic dawn core capable of total facility transformation.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#fef08a;">HOPE (DAWN)</span></span>
              <span><b>WORK:</b> ATTACHMENT</span>
            </div>
            <a href="se-015-the-debt-scale.html" class="jump-btn" style="display:block; text-align:center; background:#451a03; color:#fef08a; border:1px solid #f1df76; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>
        </div>
      </div>

      <!-- Master Footer Navigation -->
      <footer class="wiki-footer">
        <div class="footer-grid">
          <div>
            <b>SOMNARAK ARCHIVAL INITIATIVE</b>
            <p>Comprehensive encyclopedia of the 1,778 Cycles. Maintained by the Reverie Directorate.</p>
          </div>
          <div style="text-align: right;">
            <b>FACILITY 01</b> · THE HAND OF CHANGE<br>
            <span>CYCLE 1,778 ACTIVE</span>
          </div>
        </div>
      </footer>
    </main>
  </div>
</body>
</html>'''

    with open(os.path.join(wiki_root, "entities/index.html"), "w", encoding="utf-8") as f:
        f.write(entities_hub_content)

    # 2. Update homepage categorized directory with the exact matching HTML filenames
    homepage_directory_html = '''      <!-- Complete Encyclopedic Directory -->
      <section class="pm-section-block">
        <div class="section-title-bar">
          <h2>/// COMPREHENSIVE ARTICLE DIRECTORY</h2>
          <span class="title-sub">INDEX OF 166 CANONICAL ARTICLES ACROSS ALL NAMESPACES</span>
        </div>
        <div class="portal-category-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(340px, 1fr)); gap:20px; margin-top:1.5rem;">
          
          <!-- Box 1: Sorrow Entities -->
          <div class="portal-cat-box" style="background:#090e17; border:1.5px solid #ef5b55; border-radius:6px; padding:18px;">
            <h4 style="display:flex; align-items:center; gap:10px; color:#ef5b55; font-family:'JetBrains Mono', monospace; font-size:1.1rem; margin:0 0 14px; border-bottom:1px solid rgba(239,91,85,0.3); padding-bottom:8px;">
              <img src="assets/icons/nav_entities.svg" alt="" style="width:28px; height:28px; vertical-align:middle;"> 
              Sorrow Entities (SE-xxx)
            </h4>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px;">
              <li><a href="entities/se-001-the-orphaned-bell.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-001.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #ef5b55;"> <span style="color:#ef5b55; font-weight:bold;">SE-001</span> Weeping Colossus <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">PHANTASM</span></a></li>
              <li><a href="entities/se-002-the-grieving-colossus.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-001.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #ef5b55;"> <span style="color:#ef5b55; font-weight:bold;">SE-002</span> Grieving Colossus <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">PHANTASM</span></a></li>
              <li><a href="entities/se-003-the-wilderness-tide.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-003.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #38bdf8;"> <span style="color:#38bdf8; font-weight:bold;">SE-003</span> Thread of Memory <span class="badge badge-somna" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">SOMNA</span></a></li>
              <li><a href="entities/se-005-the-smothering-mother.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-008.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #71efaf;"> <span style="color:#71efaf; font-weight:bold;">SE-005</span> Smothering Cradle <span class="badge badge-green" style="font-size:0.65rem; margin-left:auto; padding:2px 6px; background:#064e3b; color:#71efaf; border:1px solid #71efaf;">AETHER</span></a></li>
              <li><a href="entities/se-007-brume.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-007.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #38bdf8;"> <span style="color:#38bdf8; font-weight:bold;">SE-007</span> Ashen Scribe <span class="badge badge-somna" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">SOMNA</span></a></li>
              <li><a href="entities/se-009-the-memory-weaver.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-009.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #38bdf8;"> <span style="color:#38bdf8; font-weight:bold;">SE-009</span> Drowned Bell <span class="badge badge-somna" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">SOMNA</span></a></li>
              <li><a href="entities/se-010-the-convergence.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-014.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #c084fc;"> <span style="color:#c084fc; font-weight:bold;">SE-010</span> The Convergence <span class="badge" style="font-size:0.65rem; margin-left:auto; padding:2px 6px; background:#4c1d95; color:#e9d5ff; border:1px solid #c084fc;">APOCRYPHA</span></a></li>
              <li><a href="entities/se-011-the-whispering-walls.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-011.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #ef5b55;"> <span style="color:#ef5b55; font-weight:bold;">SE-011</span> Whispering Iron Maiden <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">PHANTASM</span></a></li>
              <li><a href="entities/se-014-the-debt-eater.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-014.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #c084fc;"> <span style="color:#c084fc; font-weight:bold;">SE-014</span> Hollow Debt Eater <span class="badge" style="font-size:0.65rem; margin-left:auto; padding:2px 6px; background:#4c1d95; color:#e9d5ff; border:1px solid #c084fc;">APOCRYPHA</span></a></li>
              <li><a href="entities/se-015-the-debt-scale.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-015.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #f1df76;"> <span style="color:#f1df76; font-weight:bold;">SE-015</span> Sovereign Debt Scale <span class="badge" style="font-size:0.65rem; margin-left:auto; padding:2px 6px; background:#4c1d95; color:#e9d5ff; border:1px solid #c084fc;">APOCRYPHA</span></a></li>
            </ul>
          </div>

          <!-- Box 2: M.A.W. Equipment -->
          <div class="portal-cat-box" style="background:#090e17; border:1.5px solid #f1df76; border-radius:6px; padding:18px;">
            <h4 style="display:flex; align-items:center; gap:10px; color:#f1df76; font-family:'JetBrains Mono', monospace; font-size:1.1rem; margin:0 0 14px; border-bottom:1px solid rgba(241,223,118,0.3); padding-bottom:8px;">
              <img src="assets/icons/tool.svg" alt="" style="width:28px; height:28px; vertical-align:middle;"> 
              M.A.W. Equipment Armory
            </h4>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px;">
              <li><a href="maw/maw-w-001-01-the-laments-requiem.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/tool.svg" alt="" style="width:20px; height:20px;"> Lament's Requiem <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">WEAPON</span></a></li>
              <li><a href="maw/maw-w-002-01-the-mourning-maul.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/tool.svg" alt="" style="width:20px; height:20px;"> Mourning Maul <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">WEAPON</span></a></li>
              <li><a href="maw/maw-w-010-01-the-absolute-maul.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/tool.svg" alt="" style="width:20px; height:20px;"> Absolute Maul <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">WEAPON</span></a></li>
              <li><a href="maw/maw-s-001-01-the-laments-shroud.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/suit.svg" alt="" style="width:20px; height:20px;"> Lament Shroud <span class="badge badge-somna" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">SUIT</span></a></li>
              <li><a href="maw/maw-s-002-01-the-mourning-mantle.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/suit.svg" alt="" style="width:20px; height:20px;"> Mourning Mantle <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">SUIT</span></a></li>
              <li><a href="maw/maw-s-010-01-the-absolute-mantle.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/suit.svg" alt="" style="width:20px; height:20px;"> Absolute Mantle <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">SUIT</span></a></li>
              <li><a href="maw/maw-g-001-01-laments-edge.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/gift.svg" alt="" style="width:20px; height:20px;"> Lament's Edge <span class="badge" style="font-size:0.65rem; margin-left:auto; padding:2px 6px; background:#3b0764; color:#c084fc; border:1px solid #c084fc;">GIFT</span></a></li>
              <li><a href="maw/maw-g-010-01-the-absolute-verdict.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/gift.svg" alt="" style="width:20px; height:20px;"> Absolute Verdict <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">GIFT</span></a></li>
              <li style="margin-top:6px; border-top:1px dashed rgba(241,223,118,0.2); padding-top:6px;"><a href="maw/index.html" style="color:#f1df76; font-size:0.85rem; font-weight:bold; text-decoration:none;">View All 27 M.A.W. Weapon/Suit/Gift Codexes →</a></li>
            </ul>
          </div>

          <!-- Box 3: Key Personnel & Echo-Cores -->
          <div class="portal-cat-box" style="background:#090e17; border:1.5px solid #38bdf8; border-radius:6px; padding:18px;">
            <h4 style="display:flex; align-items:center; gap:10px; color:#38bdf8; font-family:'JetBrains Mono', monospace; font-size:1.1rem; margin:0 0 14px; border-bottom:1px solid rgba(56,189,248,0.3); padding-bottom:8px;">
              <img src="assets/icons/nav_characters.svg" alt="" style="width:28px; height:28px; vertical-align:middle;"> 
              Personnel & Echo-Cores
            </h4>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px;">
              <li><a href="characters/the-director-majin.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_majin.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #f1df76;"> Director Majin <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">DIRECTOR</span></a></li>
              <li><a href="characters/the-containment-lead-dekan.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_dekan.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #ef5b55;"> Lead Dekan <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">CONTAIN</span></a></li>
              <li><a href="characters/the-extraction-lead-zyrak.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_zyrak.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #38bdf8;"> Lead Zyrak <span class="badge badge-somna" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">EXTRACT</span></a></li>
              <li><a href="characters/the-research-lead-ayshuk.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_ayshuk.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #f1df76;"> Lead Ayshuk <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">RESEARCH</span></a></li>
              <li><a href="characters/the-border-lead-mellda.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_mellda.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #ef5b55;"> Lead Mellda <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">BORDER</span></a></li>
              <li><a href="characters/the-archive-lead-marjuk.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_marjuk.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #c084fc;"> Lead Marjuk <span class="badge" style="font-size:0.65rem; margin-left:auto; padding:2px 6px; background:#4c1d95; color:#e9d5ff; border:1px solid #c084fc;">ARCHIVE</span></a></li>
              <li><a href="characters/the-outsider-ishall.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_ishall.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #ef5b55;"> Lead Ishall <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">STRIKE</span></a></li>
              <li><a href="characters/the-exile-xyan.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_xyan.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #f1df76;"> Lead Xyan <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">GATE</span></a></li>
              <li style="margin-top:6px; border-top:1px dashed rgba(56,189,248,0.2); padding-top:6px;"><a href="characters/index.html" style="color:#38bdf8; font-size:0.85rem; font-weight:bold; text-decoration:none;">View All 19 Personnel & Operative Files →</a></li>
            </ul>
          </div>

          <!-- Box 4: Lore & Cosmology -->
          <div class="portal-cat-box" style="background:#090e17; border:1.5px solid #71efaf; border-radius:6px; padding:18px;">
            <h4 style="display:flex; align-items:center; gap:10px; color:#71efaf; font-family:'JetBrains Mono', monospace; font-size:1.1rem; margin:0 0 14px; border-bottom:1px solid rgba(113,239,175,0.3); padding-bottom:8px;">
              <img src="assets/icons/nav_lore.svg" alt="" style="width:28px; height:28px; vertical-align:middle;"> 
              Lore & Chronicles
            </h4>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px;">
              <li><a href="lore/the-alpha-tree.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/icon_zone_a_core.svg" alt="" style="width:20px; height:20px;"> The Alpha Tree & Metropolitan Axis</a></li>
              <li><a href="lore/the-three-sorrows.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/damage_mixed.svg" alt="" style="width:20px; height:20px;"> The Three Sorrows (Dohan, Oehan, Naehan)</a></li>
              <li><a href="lore/the-cycle-and-absolvohan.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/damage_hope.svg" alt="" style="width:20px; height:20px;"> The Absolvohan Seed of Dawn</a></li>
              <li><a href="lore/the-seven-absolute-taboos.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/taboo.svg" alt="" style="width:20px; height:20px;"> The Seven Absolute Taboos of Somnarak</a></li>
              <li><a href="lore/the-cheongula-incident.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/fracture.svg" alt="" style="width:20px; height:20px;"> The Cheongula Collapse Incident</a></li>
              <li><a href="lore/the-doorspeech.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/hud_resonance_wave.svg" alt="" style="width:20px; height:20px;"> The Doorspeech Frequency Phenomenon</a></li>
              <li><a href="lore/efflorescence-and-fracture.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/resonance.svg" alt="" style="width:20px; height:20px;"> Efflorescence & Han Petrification</a></li>
              <li style="margin-top:6px; border-top:1px dashed rgba(113,239,175,0.2); padding-top:6px;"><a href="lore/index.html" style="color:#71efaf; font-size:0.85rem; font-weight:bold; text-decoration:none;">View All 24 Lore Chronicles & Codexes →</a></li>
            </ul>
          </div>
        </div>
      </section>'''

    index_path = os.path.join(wiki_root, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        index_html = f.read()

    dir_pattern = re.compile(r'<section class="pm-section-block">\s*<div class="section-title-bar">\s*<h2>/// COMPREHENSIVE ARTICLE DIRECTORY</h2>.*?</div>\s*</section>', re.DOTALL)
    if dir_pattern.search(index_html):
        index_html = dir_pattern.sub(homepage_directory_html, index_html, count=1)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_html)
        print("Updated index.html directory with exact matching files!")

if __name__ == "__main__":
    harmonize()
