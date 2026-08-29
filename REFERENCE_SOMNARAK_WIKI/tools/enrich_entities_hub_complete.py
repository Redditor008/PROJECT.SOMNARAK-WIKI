import os

# Update entities/index.html
entities_hub_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sorrow Entities Codex - Somnarak Official Wiki</title>
  <link rel="stylesheet" href="../assets/css/wiki.css">
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
    <a href="../entities/index.html" class="active">Sorrow Entities</a>
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
          <img src="../assets/layout/hand/icons/icon_reverie_directorate_badge.svg" alt="Reverie Directorate Crest" class="brand-logo" width="110" height="110">
          <span class="brand-title">SOMNARAK</span>
          <span class="brand-subtitle">REVERIE DIRECTORATE ARCHIVE</span>
        </a>
      </div>
      
      <div class="rail-group">
        <div class="rail-header">DATABASE HUBS</div>
        <ul class="rail-list">
          <li><a href="../index.html">Main Terminal</a></li>
          <li><a href="../characters/index.html">Characters &amp; Echo-Cores</a></li>
          <li><a href="../lore/index.html">Lore &amp; Cosmology</a></li>
          <li><a href="../locations/index.html">Atlas &amp; Locations</a></li>
          <li><a href="../factions/index.html">Factions &amp; Guilds</a></li>
          <li><a href="../departments/index.html">Facility Departments</a></li>
          <li><a href="../entities/index.html" class="active">Sorrow Entities</a></li>
          <li><a href="../maw/index.html">M.A.W. Armaments</a></li>
          <li><a href="../mechanics/index.html">Systems &amp; Mechanics</a></li>
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
        <div class="rail-header">CARTOGRAPHY &amp; SCHEMATICS</div>
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
          <span class="section-tag">ALL 10 CANONICAL PHENOMENA &amp; REGISTRIES</span>
        </div>
        <p class="section-desc">
          Sorrow Entities (슬픔의 존재) are metaphysical manifestations born of human grief, regret, and Han energy. Each entity is secured in dedicated containment sectors within Facility 01 (The Hand of Change) under strict SECC protocols.
        </p>

        <div class="hub-grid-3">
          
          <!-- SE-001 -->
          <div class="pm-entity-card" style="border:2px solid #38bdf8; background:#040d18;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-001-icon.svg" alt="SE-001" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-PHANTASM">δ (PHANTASM)</span>
                <span class="damage-badge dmg-cyan">LAMENT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 2 // MAW'S KEEP</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#38bdf8;">SE-001: THE ORPHANED BELL</h3>
            <p class="entity-card-desc">Ancient bronze resonance bell weeping liquid cyan Han tears. Emits cognitive shockwaves upon Coherence depletion.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> INSIGHT (65%)</span>
            </div>
            <a href="se-001-the-orphaned-bell.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-002 -->
          <div class="pm-entity-card" style="border:2px solid #ef5b55; background:#0c080a;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-002-icon.svg" alt="SE-002" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-PHANTASM">δ (PHANTASM)</span>
                <span class="damage-badge dmg-red">GRUDGE DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 2 // MAW'S KEEP</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#ef5b55;">SE-002: GRIEVING COLOSSUS</h3>
            <p class="entity-card-desc">Subterranean basalt titan weeping crimson sludge through cracked mask. Massive kinetic shockwave hazard.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#ef5b55;">GRUDGE (HP)</span></span>
              <span><b>WORK:</b> SUBJUGATION (60%)</span>
            </div>
            <a href="se-002-the-grieving-colossus.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-003 -->
          <div class="pm-entity-card" style="border:2px solid #38bdf8; background:#060e1f;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-003-icon.svg" alt="SE-003" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-SOMNA">β (SOMNA)</span>
                <span class="damage-badge dmg-cyan">LAMENT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 3 // EXTRACTION</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#38bdf8;">SE-003: THREAD OF MEMORY</h3>
            <p class="entity-card-desc">Ethereal azure loom piercing human consciousness with memory-weaving needles. Induces selective amnesia.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> COMMUNION (70%)</span>
            </div>
            <a href="se-003-the-wilderness-tide.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-004 -->
          <div class="pm-entity-card" style="border:2px solid #f97316; background:#120804;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-004-icon.svg" alt="SE-004" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-MORPHEAN">γ (MORPHEAN)</span>
                <span class="damage-badge dmg-red">GRUDGE DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 5 // BORDER WATCH</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#f97316;">SE-004: RUST-BLEEDING SENTRY</h3>
            <p class="entity-card-desc">Automaton sentinel weeping corrosive rust from ocular slits. High armor-penetration halberd attacks.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#ef5b55;">GRUDGE (HP)</span></span>
              <span><b>WORK:</b> SUBJUGATION (65%)</span>
            </div>
            <a href="se-004-the-rust-bleeding-sentry.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-005 -->
          <div class="pm-entity-card" style="border:2px solid #f1df76; background:#141004;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-005-icon.svg" alt="SE-005" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-AETHER">α (AETHER)</span>
                <span class="damage-badge dmg-cyan">LAMENT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 1 // NEUTRAL CORE</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#f1df76;">SE-005: SMOTHERING CRADLE</h3>
            <p class="entity-card-desc">Golden porcelain maternal effigy entwined in suffocating dark shrouds. Low base threat but induces passive despair aura.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> COMMUNION (80%)</span>
            </div>
            <a href="se-005-the-smothering-mother.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-006 -->
          <div class="pm-entity-card" style="border:2px solid #10b981; background:#041510;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-006-icon.svg" alt="SE-006" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-SOMNA">β (SOMNA)</span>
                <span class="damage-badge dmg-black">WEIGHT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 3 // EXTRACTION</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#10b981;">SE-006: SIPHON LEECH</h3>
            <p class="entity-card-desc">Predatory annelid siphon organism drinking subterranean effluent. Drains agent HP and SP concurrently.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#94a3b8;">WEIGHT (HP+SP)</span></span>
              <span><b>WORK:</b> EXTRACTION (70%)</span>
            </div>
            <a href="se-006-the-siphon-leech.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-007 -->
          <div class="pm-entity-card" style="border:2px solid #94a3b8; background:#080c14;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-007-icon.svg" alt="SE-007" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-SOMNA">β (SOMNA)</span>
                <span class="damage-badge dmg-cyan">LAMENT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 6 // DEEP VAULT</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#cbd5e1;">SE-007: ASHEN SCRIBE</h3>
            <p class="entity-card-desc">Spectral cloaked recorder engraving forgotten names upon basalt slates. Demands high mental fortitude.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> INSIGHT (70%)</span>
            </div>
            <a href="se-007-brume.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-009 -->
          <div class="pm-entity-card" style="border:2px solid #0284c7; background:#04101e;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-009-icon.svg" alt="SE-009" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-SOMNA">β (SOMNA)</span>
                <span class="damage-badge dmg-cyan">LAMENT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 4 // INSIGHT FORGE</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#38bdf8;">SE-009: DROWNED BELL</h3>
            <p class="entity-card-desc">Aquatic bronze bell submerged in subterranean tears. Tolling underwater pulses erode agent SP.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> COMMUNION (70%)</span>
            </div>
            <a href="se-009-the-memory-weaver.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-010 -->
          <div class="pm-entity-card" style="border:2px solid #f8fafc; background:#100c24;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-010-icon.svg" alt="SE-010" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-APOCRYPHA">ε (APOCRYPHA)</span>
                <span class="damage-badge dmg-white">VOID DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 8 // GATE WATCH</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#f8fafc;">SE-010: THE CONVERGENCE</h3>
            <p class="entity-card-desc">Apocalyptic sphere of interwoven crowns and existential void eye. Breaching initiates facility-wide Efflorescence.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#ffffff;">VOID (% MAX HP)</span></span>
              <span><b>WORK:</b> RESTRAINT (30%)</span>
            </div>
            <a href="se-010-the-convergence.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-011 -->
          <div class="pm-entity-card" style="border:2px solid #ef4444; background:#140407;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-011-icon.svg" alt="SE-011" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-PHANTASM">δ (PHANTASM)</span>
                <span class="damage-badge dmg-cyan">LAMENT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 7 // SHADOW CORPS</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#ef4444;">SE-011: WHISPERING WALLS</h3>
            <p class="entity-card-desc">Living labyrinth bulkhead embedded with screaming faces and acoustic resonance baffles.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> INSIGHT (60%)</span>
            </div>
            <a href="se-011-the-whispering-walls.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

        </div>
      </div>

      <!-- Master Footer Navigation -->
      <footer class="wiki-footer">
        <div class="footer-grid">
          <div>
            <b>SOMNARAK ARCHIVAL DIRECTORY</b>
            <p>Reverie Directorate Subterranean Complex // Facility 01 Hand of Change</p>
          </div>
          <div style="text-align: right;">
            <b>AUTHORIZATION:</b> OVERSIGHT CLEARANCE TIER-5<br>
            <span>CONFIDENTIAL ARCHIVAL SYSTEM</span>
          </div>
        </div>
      </footer>
    </main>
  </div>
</body>
</html>"""

with open('/home/user/01_Somnarak_Wiki/entities/index.html', 'w', encoding='utf-8') as f:
    f.write(entities_hub_content)

print('SUCCESS: Rebuilt entities/index.html with large 112px icons and generous badge padding!')
