import os

def rebuild_all_hub_pages():
    wiki_root = "/home/user/01_Somnarak_Wiki"

    # 1. ENTITIES HUB (entities/index.html)
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
            <a href="se-001-weeping-colossus.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-003 -->
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
            <a href="se-003-thread-of-memory.html" class="jump-btn" style="display:block; text-align:center; background:#0c4a6e; color:#bae6fd; border:1px solid #38bdf8; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-004 -->
          <div class="pm-entity-card" style="border:2px solid #c084fc; background:#0c0417; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-004.svg" alt="SE-004" style="width:64px; height:64px; border:2px solid #c084fc; border-radius:6px; background:#130421;">
              <div style="text-align:right;">
                <span class="badge badge-gold">MORPHEAN (γ)</span>
                <div style="font-size:0.75rem; color:#c084fc; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 6 // DEEP VAULT</div>
              </div>
            </div>
            <h3 style="color:#c084fc; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-004: OBSIDIAN MIRROR</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Monolithic volcanic obsidian mirror reflecting observer's deepest existential regrets. Fissures bleed void radiation that erases soul integrity.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#ffffff;">VOID (% HP)</span></span>
              <span><b>WORK:</b> INSIGHT</span>
            </div>
            <a href="se-004-obsidian-mirror.html" class="jump-btn" style="display:block; text-align:center; background:#3b0764; color:#e9d5ff; border:1px solid #c084fc; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-006 -->
          <div class="pm-entity-card" style="border:2px solid #f1df76; background:#140e02; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-006.svg" alt="SE-006" style="width:64px; height:64px; border:2px solid #f1df76; border-radius:6px; background:#1c1402;">
              <div style="text-align:right;">
                <span class="badge badge-gold">MORPHEAN (γ)</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 4 // INSIGHT FORGE</div>
              </div>
            </div>
            <h3 style="color:#f1df76; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-006: CLOCKWORK HEART</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Interlocking bronze and brass gear apparatus ticking with agonizing precision. Emits gravitational shockwaves that strain both body and mind.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#cbd5e1;">WEIGHT (DUAL)</span></span>
              <span><b>WORK:</b> REPRESSION</span>
            </div>
            <a href="se-006-clockwork-heart.html" class="jump-btn" style="display:block; text-align:center; background:#451a03; color:#fef08a; border:1px solid #f1df76; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-007 -->
          <div class="pm-entity-card" style="border:2px solid #ef5b55; background:#0c080a; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-007.svg" alt="SE-007" style="width:64px; height:64px; border:2px solid #ef5b55; border-radius:6px; background:#1f0608;">
              <div style="text-align:right;">
                <span class="badge badge-somna">SOMNA (β)</span>
                <div style="font-size:0.75rem; color:#ef5b55; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 6 // DEEP VAULT</div>
              </div>
            </div>
            <h3 style="color:#ef5b55; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-007: ASHEN SCRIBE</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Tower of charcoal-burnt manuscript codices recording fatal facility debts. Inscribes searing crimson marks onto approaching researchers.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#ef5b55;">GRUDGE (HP)</span></span>
              <span><b>WORK:</b> INSIGHT</span>
            </div>
            <a href="se-007-ashen-scribe.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-008 -->
          <div class="pm-entity-card" style="border:2px solid #71efaf; background:#04140d; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-008.svg" alt="SE-008" style="width:64px; height:64px; border:2px solid #71efaf; border-radius:6px; background:#02140d;">
              <div style="text-align:right;">
                <span class="badge badge-green" style="background:#064e3b; color:#71efaf; border:1px solid #71efaf;">AETHER (α)</span>
                <div style="font-size:0.75rem; color:#71efaf; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 1 // NEUTRAL</div>
              </div>
            </div>
            <h3 style="color:#71efaf; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-008: FORGOTTEN CRADLE</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Gilded bone rocking cradle sheltering an ethereal lullaby of infant solace. Stable containment yield with minimal breach hazards.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> ATTACHMENT</span>
            </div>
            <a href="se-008-forgotten-cradle.html" class="jump-btn" style="display:block; text-align:center; background:#064e3b; color:#a7f3d0; border:1px solid #71efaf; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-009 -->
          <div class="pm-entity-card" style="border:2px solid #38bdf8; background:#041b2c; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-009.svg" alt="SE-009" style="width:64px; height:64px; border:2px solid #38bdf8; border-radius:6px; background:#041b2c;">
              <div style="text-align:right;">
                <span class="badge badge-somna">SOMNA (β)</span>
                <div style="font-size:0.75rem; color:#38bdf8; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 5 // BORDER WATCH</div>
              </div>
            </div>
            <h3 style="color:#38bdf8; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-009: DROWNED BELL</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Verdigris-encrusted bronze church bell submerged in subterranean tears. Emits acoustic tidal resonances that induce melancholic stupor.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> REPRESSION</span>
            </div>
            <a href="se-009-drowned-bell.html" class="jump-btn" style="display:block; text-align:center; background:#0e7490; color:#cffafe; border:1px solid #38bdf8; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-011 -->
          <div class="pm-entity-card" style="border:2px solid #ef5b55; background:#1c0709; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-011.svg" alt="SE-011" style="width:64px; height:64px; border:2px solid #ef5b55; border-radius:6px; background:#1f0608;">
              <div style="text-align:right;">
                <span class="badge badge-crimson">PHANTASM (δ)</span>
                <div style="font-size:0.75rem; color:#ef5b55; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 2 // MAW'S KEEP</div>
              </div>
            </div>
            <h3 style="color:#ef5b55; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-011: IRON MAIDEN</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Spiked iron executioner sarcophagus housing a weeping bronze faceplate. Thrusts internal thorns inward when emotional resonance peaks.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#ef5b55;">GRUDGE (HP)</span></span>
              <span><b>WORK:</b> REPRESSION</span>
            </div>
            <a href="se-011-iron-maiden-of-regret.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-014 -->
          <div class="pm-entity-card" style="border:2px solid #c084fc; background:#130421; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-014.svg" alt="SE-014" style="width:64px; height:64px; border:2px solid #c084fc; border-radius:6px; background:#130421;">
              <div style="text-align:right;">
                <span class="badge" style="background:#4c1d95; color:#e9d5ff; border:1px solid #c084fc;">APOCRYPHA (ω)</span>
                <div style="font-size:0.75rem; color:#c084fc; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 7 // SHADOW CORPS</div>
              </div>
            </div>
            <h3 style="color:#c084fc; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-014: HOLLOW SINGER</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Porcelain theatrical tragedy mask singing an opera of total existential void. Bypasses physical wards to disintegrate consciousness.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#ffffff;">VOID (% HP)</span></span>
              <span><b>WORK:</b> INSIGHT</span>
            </div>
            <a href="se-014-hollow-singer.html" class="jump-btn" style="display:block; text-align:center; background:#3b0764; color:#e9d5ff; border:1px solid #c084fc; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
          </div>

          <!-- SE-015 -->
          <div class="pm-entity-card" style="border:2px solid #f1df76; background:#1c1402; padding:18px; border-radius:6px;">
            <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <img src="../assets/icons/se-015.svg" alt="SE-015" style="width:64px; height:64px; border:2px solid #f1df76; border-radius:6px; background:#1c1402;">
              <div style="text-align:right;">
                <span class="badge" style="background:#4c1d95; color:#e9d5ff; border:1px solid #c084fc;">APOCRYPHA (ω)</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 8 // GATE WATCH</div>
              </div>
            </div>
            <h3 style="color:#f1df76; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">SE-015: SOVEREIGN CROWN</h3>
            <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Jagged black iron crown encircled by a blinding golden Absolvohan halo. Catastrophic dawn core capable of total facility transformation.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:12px; display:flex; justify-content:space-between;">
              <span><b>DMG:</b> <span style="color:#fef08a;">HOPE (DAWN)</span></span>
              <span><b>WORK:</b> ATTACHMENT</span>
            </div>
            <a href="se-015-sovereign-crown.html" class="jump-btn" style="display:block; text-align:center; background:#451a03; color:#fef08a; border:1px solid #f1df76; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN FULL DOSSIER & ASSETS →</a>
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

    print("Rebuilt entities/index.html with 100% canonical cards, icons, and links!")

if __name__ == "__main__":
    rebuild_all_hub_pages()
