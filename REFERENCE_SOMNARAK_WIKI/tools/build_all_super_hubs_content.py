import os

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

def wrap_page(rel_path, page_title, category_name, hero_title, hero_subtitle, hero_banner_svg, breadcrumb_label, content_html):
    depth = rel_path.count('/')
    prefix = '../' * depth if depth > 0 else './'
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title} - Somnarak Official Wiki</title>
  <link rel="stylesheet" href="{prefix}assets/css/wiki.css">
</head>
<body class="wiki-body">
  <div class="wiki-shell">
    <!-- Left Navigation Rail -->
    <aside aria-label="Main navigation" class="left-rail">
      <div class="branding">
        <a class="brand-link" href="{prefix}index.html">
          <img src="{prefix}assets/layout/hand/icons/icon_reverie_directorate_badge.svg" alt="Reverie Directorate Crest" class="brand-logo" width="110" height="110">
          <span class="brand-title">SOMNARAK</span>
          <span class="brand-subtitle">REVERIE DIRECTORATE ARCHIVE</span>
        </a>
      </div>
      
      <div class="rail-group">
        <div class="rail-header">DATABASE HUBS</div>
        <ul class="rail-list">
          <li><a href="{prefix}index.html">Main Terminal</a></li>
          <li><a href="{prefix}characters/index.html">Characters & Echo-Cores</a></li>
          <li><a href="{prefix}lore/index.html">Lore & Cosmology</a></li>
          <li><a href="{prefix}locations/index.html">Atlas & Locations</a></li>
          <li><a href="{prefix}factions/index.html">Factions & Guilds</a></li>
          <li><a href="{prefix}departments/index.html">Facility Departments</a></li>
          <li><a href="{prefix}entities/index.html">Sorrow Entities</a></li>
          <li><a href="{prefix}maw/index.html">M.A.W. Armaments</a></li>
          <li><a href="{prefix}mechanics/index.html">Systems & Mechanics</a></li>
        </ul>
      </div>

      <div class="rail-group">
        <div class="rail-header">THE NINE ECHO-CORES</div>
        <ul class="rail-list">
          <li><a href="{prefix}characters/the-director-majin.html">Director Majin</a></li>
          <li><a href="{prefix}characters/the-secretary-seiyon.html">Secretary Seiyon</a></li>
          <li><a href="{prefix}characters/the-containment-lead-dekan.html">Containment: Dekan</a></li>
          <li><a href="{prefix}characters/the-extraction-lead-zyrak.html">Extraction: Zyrak</a></li>
          <li><a href="{prefix}characters/the-research-lead-ayshuk.html">Research: Ayshuk</a></li>
          <li><a href="{prefix}characters/the-border-lead-mellda.html">Border: Mellda</a></li>
          <li><a href="{prefix}characters/the-archive-lead-marjuk.html">Archive: Marjuk</a></li>
          <li><a href="{prefix}characters/the-outsider-ishall.html">Outsider: Ishall</a></li>
          <li><a href="{prefix}characters/the-exile-xyan.html">Exile: Xyan</a></li>
        </ul>
      </div>

      <div class="rail-group">
        <div class="rail-header">CARTOGRAPHY & SCHEMATICS</div>
        <ul class="rail-list">
          <li><a href="{prefix}atlas/hand-of-change-map.html">Facility Cutaway Map</a></li>
          <li><a href="{prefix}atlas/somnarak-city-map.html">City Master Blueprint</a></li>
        </ul>
      </div>
    </aside>

    <!-- Main Content Area -->
    <main class="wiki-content">
      <!-- Tactical Top Status HUD -->
      <div class="tactical-hud-bar">
        <div class="hud-item"><span class="led-dot led-green"></span> ARCHIVE ONLINE</div>
        <div class="hud-item"><span class="hud-label">CLEARANCE:</span> LEVEL 5 RESTRICTED</div>
        <div class="hud-item"><span class="hud-label">DIRECTORY:</span> {category_name.upper()}</div>
        <div class="hud-item"><span class="hud-label">STABILITY:</span> 99.4% NOMINAL</div>
      </div>

      <!-- Breadcrumbs -->
      <nav class="breadcrumb-trail" aria-label="Breadcrumb">
        <a href="{prefix}index.html">SOMNARAK ARCHIVE</a> &gt; 
        <span>{breadcrumb_label}</span>
      </nav>

      <!-- Panoramic Hero Banner -->
      <div class="category-panoramic-banner">
        <img src="{prefix}{hero_banner_svg}" alt="{hero_title}" class="panoramic-banner-img">
      </div>

      <!-- Fast Jump Bar -->
      <div class="fast-jump-nav">
        <span class="fast-jump-title">/// DIRECT ACCESS:</span>
        <div class="fast-jump-pills">
          <a href="{prefix}entities/index.html" class="jump-pill">Entities Codex</a>
          <a href="{prefix}maw/index.html" class="jump-pill">M.A.W. Arsenal</a>
          <a href="{prefix}characters/index.html" class="jump-pill">Echo-Cores &amp; Cast</a>
          <a href="{prefix}departments/index.html" class="jump-pill">Facility Floors</a>
          <a href="{prefix}lore/index.html" class="jump-pill">Lore Chronicles</a>
          <a href="{prefix}locations/index.html" class="jump-pill">Metropolitan Atlas</a>
          <a href="{prefix}factions/index.html" class="jump-pill">Factions &amp; Guilds</a>
          <a href="{prefix}mechanics/index.html" class="jump-pill">Combat Systems</a>
        </div>
      </div>

      {content_html}

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
</html>'''
    full_path = os.path.join(WIKI_DIR, rel_path)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Hub with Panoramic SVG Banner: {rel_path}")

# =========================================================================
# 1. ENTITIES HUB (entities/index.html)
# =========================================================================
entities_html = '''
<div class="wiki-section">
  <div class="section-banner">
    <h2>/// SORROW ENTITY CONTAINMENT DIRECTORY</h2>
    <span class="section-tag">ALL 10 CANONICAL ABNORMAL PHENOMENA</span>
  </div>
  <p class="section-desc">
    Sorrow Entities (슬픔의 존재) are metaphysical crystallizations of collective human anguish, regret, and Han energy manifested from the Alpha Tree and the Subterranean Veil. Each entity is contained within dedicated isolation chambers in the Hand of Change facility under strict SECC protocols.
  </p>

  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#10b981;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-001.svg" alt="SE-001" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-can">T-01 CAN</span><span class="sector-tag">FLOOR 1 // NEUTRAL</span></div>
      </div>
      <h3 class="entity-card-name">SE-001: THE ORPHANED BELL</h3>
      <p class="entity-card-desc">A bronze tolling bell forged from the resonance of abandoned settlements. Tolls at dawn, emitting low-frequency acoustic vibrations that steady human heartbeat.</p>
      <div class="entity-card-stats"><span><b>Work:</b> Instinct (70%)</span><span><b>Damage:</b> Physical (RED)</span></div>
      <a href="se-001-the-orphaned-bell.html" class="jump-btn">OPEN FULL DOSSIER →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#38bdf8;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-002-profile.svg" alt="SE-002" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-teth">T-02 TETH</span><span class="sector-tag">FLOOR 2 // MAW'S KEEP</span></div>
      </div>
      <h3 class="entity-card-name">SE-002: THE GRIEVING COLOSSUS</h3>
      <p class="entity-card-desc">A towering sentinel composed of solidified tear-stone and basalt monoliths. Carries the monolithic weight of lost frontline fortresses, weeping mineral residue.</p>
      <div class="entity-card-stats"><span><b>Work:</b> Repression (65%)</span><span><b>Damage:</b> Physical (RED)</span></div>
      <a href="se-002-the-grieving-colossus.html" class="jump-btn">OPEN FULL DOSSIER →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#38bdf8;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-003.svg" alt="SE-003" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-teth">T-02 TETH</span><span class="sector-tag">ZONE E // OUTSKIRTS</span></div>
      </div>
      <h3 class="entity-card-name">SE-003: THE WILDERNESS TIDE</h3>
      <p class="entity-card-desc">An undulating biomechanical swarm of saline aquatic tendrils that mimic the lost coastal tides of pre-Cataclysm Somnarak. Dissolves biological barriers.</p>
      <div class="entity-card-stats"><span><b>Work:</b> Insight (70%)</span><span><b>Damage:</b> Corrosive (BLACK)</span></div>
      <a href="se-003-the-wilderness-tide.html" class="jump-btn">OPEN FULL DOSSIER →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#f1df76;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-005-profile.svg" alt="SE-005" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-he">T-03 HE</span><span class="sector-tag">FLOOR 2 // MAW'S KEEP</span></div>
      </div>
      <h3 class="entity-card-name">SE-005: THE SMOTHERING MOTHER</h3>
      <p class="entity-card-desc">A maternal silhouette draped in heavy mourning silk. Envelops agents in suffocating fabric cocoons, soothing psychological pain at the expense of vital respiration.</p>
      <div class="entity-card-stats"><span><b>Work:</b> Attachment (75%)</span><span><b>Damage:</b> Mental (WHITE)</span></div>
      <a href="se-005-the-smothering-mother.html" class="jump-btn">OPEN FULL DOSSIER →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#f1df76;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-007.svg" alt="SE-007" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-he">T-03 HE</span><span class="sector-tag">FLOOR 4 // INSIGHT FORGE</span></div>
      </div>
      <h3 class="entity-card-name">SE-007: BRUME</h3>
      <p class="entity-card-desc">A dense vaporous atmospheric entity that suspends frozen memories and spectral apparitions. Exposure induces auditory hallucinations of deceased relatives.</p>
      <div class="entity-card-stats"><span><b>Work:</b> Insight (70%)</span><span><b>Damage:</b> Mental (WHITE)</span></div>
      <a href="se-007-brume.html" class="jump-btn">OPEN FULL DOSSIER →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#a855f7;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-009.svg" alt="SE-009" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-waw">T-04 WAW</span><span class="sector-tag">FLOOR 4 // INSIGHT FORGE</span></div>
      </div>
      <h3 class="entity-card-name">SE-009: THE MEMORY WEAVER</h3>
      <p class="entity-card-desc">An arachnid loom construct with crystalline spinnerets that harvest neurological recollections, spinning them into luminescent synaptic tapestries.</p>
      <div class="entity-card-stats"><span><b>Work:</b> Insight (65%)</span><span><b>Damage:</b> Corrosive (BLACK)</span></div>
      <a href="se-009-the-memory-weaver.html" class="jump-btn">OPEN FULL DOSSIER →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#ef4444;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-010-profile.svg" alt="SE-010" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-aleph">T-05 ALEPH</span><span class="sector-tag">FLOOR 6 // DEEP VAULT</span></div>
      </div>
      <h3 class="entity-card-name">SE-010: THE CONVERGENCE</h3>
      <p class="entity-card-desc">The supreme cataclysmic entity residing in the lowest abyss. A pulsating nexus of all 1,778 cycle resets capable of unraveling structural reality across the entire facility.</p>
      <div class="entity-card-stats"><span><b>Work:</b> Repression (55%)</span><span><b>Damage:</b> Pale (PALE)</span></div>
      <a href="se-010-the-convergence.html" class="jump-btn">OPEN FULL DOSSIER →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#f1df76;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-011.svg" alt="SE-011" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-he">T-03 HE</span><span class="sector-tag">FLOOR 5 // BORDER WATCH</span></div>
      </div>
      <h3 class="entity-card-name">SE-011: THE WHISPERING WALLS</h3>
      <p class="entity-card-desc">Living architectural barricades embedded with hundreds of calcified vocal cords. Chants forgotten names and protective perimeter hymns.</p>
      <div class="entity-card-stats"><span><b>Work:</b> Instinct (60%)</span><span><b>Damage:</b> Mental (WHITE)</span></div>
      <a href="se-011-the-whispering-walls.html" class="jump-btn">OPEN FULL DOSSIER →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#a855f7;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-014.svg" alt="SE-014" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-waw">T-04 WAW</span><span class="sector-tag">FLOOR 7 // SHADOW CORPS</span></div>
      </div>
      <h3 class="entity-card-name">SE-014: THE DEBT EATER</h3>
      <p class="entity-card-desc">A grotesque porcelain furnace entity that consumes signed contracts, ledgers, and mortal debts in exchange for high-density Han fuel rods.</p>
      <div class="entity-card-stats"><span><b>Work:</b> Repression (60%)</span><span><b>Damage:</b> Corrosive (BLACK)</span></div>
      <a href="se-014-the-debt-eater.html" class="jump-btn">OPEN FULL DOSSIER →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#a855f7;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-015.svg" alt="SE-015" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-waw">T-04 WAW</span><span class="sector-tag">FLOOR 8 // GATE WATCH</span></div>
      </div>
      <h3 class="entity-card-name">SE-015: THE DEBT SCALE</h3>
      <p class="entity-card-desc">A colossal golden balance suspended above the taboo boundary. Weighs the spiritual sins and existential transgressions of fallen Directorate operatives.</p>
      <div class="entity-card-stats"><span><b>Work:</b> Attachment (65%)</span><span><b>Damage:</b> Pale (PALE)</span></div>
      <a href="se-015-the-debt-scale.html" class="jump-btn">OPEN FULL DOSSIER →</a>
    </div>
  </div>
</div>
'''
wrap_page("entities/index.html", "Sorrow Entities Codex", "entities", "SORROW ENTITIES CODEX", "Master Registry of Canonical Abnormalities, Risk Classifications, and Containment Protocols", "assets/banners/banner_hero_sorrow_entities.svg", "SORROW ENTITIES", entities_html)

# =========================================================================
# 2. MAW HUB (maw/index.html)
# =========================================================================
maw_html = '''
<div class="wiki-section">
  <div class="section-banner">
    <h2>/// M.A.W. ARMAMENT ARSENAL (MATERIALIZED AGONY WEAPONRY)</h2>
    <span class="section-tag">ALL 27 CANONICAL WEAPONS, SUITS & GIFTS</span>
  </div>
  <p class="section-desc">
    M.A.W. Equipment represents weaponized resonance gear extracted directly from Sorrow Entities by Floor 3 Extraction Hall under Zyrak. Agents equip Triad Sets (Weapon, Suit, and Gift) to channel entity damage types while safeguarding sanity.
  </p>

  <div class="toc-box" style="margin-bottom: 2rem;">
    <div class="toc-title">RAPID ARSENAL CLASSIFICATION JUMP:</div>
    <div class="toc-grid">
      <a href="#weapons-catalog">✦ M.A.W. WEAPONS (9 ARMS)</a>
      <a href="#suits-catalog">✦ M.A.W. SUITS (9 ARMORS)</a>
      <a href="#gifts-catalog">✦ M.A.W. GIFTS (9 RELICS)</a>
      <a href="../mechanics/maw-equipment-system.html">✦ EXTRACTION MECHANICS</a>
    </div>
  </div>

  <h2 id="weapons-catalog" class="sub-category-header">/// 1. M.A.W. WEAPONS ARSENAL (9 OFFENSIVE IMPLEMENTS)</h2>
  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#ef4444;"><div class="entity-card-top"><img src="../assets/art/maw/maw-w-001-01.svg" alt="Lament Requiem" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-can">CAN</span><span class="sector-tag">SE-001</span></div></div><h3 class="entity-card-name">LAMENT'S REQUIEM</h3><p class="entity-card-desc">Tuning-fork blade delivering concussive acoustic shockwaves on impact.</p><a href="maw-w-001-01-the-laments-requiem.html" class="jump-btn">VIEW WEAPON SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#ef4444;"><div class="entity-card-top"><img src="../assets/art/maw/maw-w-002-01.svg" alt="Mourning Maul" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-teth">TETH</span><span class="sector-tag">SE-002</span></div></div><h3 class="entity-card-name">THE MOURNING MAUL</h3><p class="entity-card-desc">Massive tear-stone warhammer that sunders armor plating with tectonic force.</p><a href="maw-w-002-01-the-mourning-maul.html" class="jump-btn">VIEW WEAPON SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#38bdf8;"><div class="entity-card-top"><img src="../assets/art/maw/maw-w-005-01.svg" alt="Embrace Fang" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">HE</span><span class="sector-tag">SE-005</span></div></div><h3 class="entity-card-name">THE EMBRACE FANG</h3><p class="entity-card-desc">Silk-bound stiletto inflicting psychological terror and sensory deprivation.</p><a href="maw-w-005-01-the-embrace-fang.html" class="jump-btn">VIEW WEAPON SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#38bdf8;"><div class="entity-card-top"><img src="../assets/art/maw/maw-w-007-01.svg" alt="Hope Lens" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">HE</span><span class="sector-tag">SE-007</span></div></div><h3 class="entity-card-name">THE HOPE LENS</h3><p class="entity-card-desc">Refractive crystal emitter focusing atmospheric vapor into radiant beams.</p><a href="maw-w-007-01-the-hope-lens.html" class="jump-btn">VIEW WEAPON SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#a855f7;"><div class="entity-card-top"><img src="../assets/art/maw/maw-w-009-01.svg" alt="Forgotten Lens" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">WAW</span><span class="sector-tag">SE-009</span></div></div><h3 class="entity-card-name">THE FORGOTTEN LENS</h3><p class="entity-card-desc">Prismatic weaver prism that unravels target neurological connections.</p><a href="maw-w-009-01-the-forgotten-lens.html" class="jump-btn">VIEW WEAPON SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#ef4444;"><div class="entity-card-top"><img src="../assets/art/maw/maw-w-010-01.svg" alt="Absolute Maul" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">ALEPH</span><span class="sector-tag">SE-010</span></div></div><h3 class="entity-card-name">THE ABSOLUTE MAUL</h3><p class="entity-card-desc">Singularity hammer crushing existential timelines and physical matter.</p><a href="maw-w-010-01-the-absolute-maul.html" class="jump-btn">VIEW WEAPON SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#ef4444;"><div class="entity-card-top"><img src="../assets/art/maw/maw-w-011-01.svg" alt="Listening Requiem" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">HE</span><span class="sector-tag">SE-011</span></div></div><h3 class="entity-card-name">THE LISTENING REQUIEM</h3><p class="entity-card-desc">Resonant tuning pole channeling perimeter hymns that disrupt cognitive cohesion.</p><a href="maw-w-011-01-the-listening-requiem.html" class="jump-btn">VIEW WEAPON SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#a855f7;"><div class="entity-card-top"><img src="../assets/art/maw/maw-w-014-01.svg" alt="Debt Lens" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">WAW</span><span class="sector-tag">SE-014</span></div></div><h3 class="entity-card-name">THE DEBT LENS</h3><p class="entity-card-desc">Incinerating ledger-focus that burns monetary and biological debts.</p><a href="maw-w-014-01-the-debt-lens.html" class="jump-btn">VIEW WEAPON SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#f1df76;"><div class="entity-card-top"><img src="../assets/art/maw/maw-w-015-01.svg" alt="Balance Lens" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">WAW</span><span class="sector-tag">SE-015</span></div></div><h3 class="entity-card-name">THE BALANCE LENS</h3><p class="entity-card-desc">Dual-aperture beam weapon balancing damage output based on agent sanity.</p><a href="maw-w-015-01-the-balance-lens.html" class="jump-btn">VIEW WEAPON SPECS →</a></div>
  </div>

  <h2 id="suits-catalog" class="sub-category-header" style="margin-top: 3rem;">/// 2. M.A.W. SUITS ARSENAL (9 PROTECTIVE CASINGS)</h2>
  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#10b981;"><div class="entity-card-top"><img src="../assets/art/maw/maw-s-001-01.svg" alt="Lament Shroud" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-can">CAN</span><span class="sector-tag">SE-001</span></div></div><h3 class="entity-card-name">THE LAMENT'S SHROUD</h3><p class="entity-card-desc">Reinforced ballistic tunic providing high kinetic absorption.</p><a href="maw-s-001-01-the-laments-shroud.html" class="jump-btn">VIEW SUIT SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#38bdf8;"><div class="entity-card-top"><img src="../assets/art/maw/maw-s-002-01.svg" alt="Mourning Mantle" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-teth">TETH</span><span class="sector-tag">SE-002</span></div></div><h3 class="entity-card-name">THE MOURNING MANTLE</h3><p class="entity-card-desc">Heavy basalt-infused battlecoat resistant to physical crush.</p><a href="maw-s-002-01-the-mourning-mantle.html" class="jump-btn">VIEW SUIT SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#f1df76;"><div class="entity-card-top"><img src="../assets/art/maw/maw-s-005-01.svg" alt="Embrace Plate" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">HE</span><span class="sector-tag">SE-005</span></div></div><h3 class="entity-card-name">THE EMBRACE PLATE</h3><p class="entity-card-desc">Silk-lined carapace offering superb mental protection.</p><a href="maw-s-005-01-the-embrace-plate.html" class="jump-btn">VIEW SUIT SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#f1df76;"><div class="entity-card-top"><img src="../assets/art/maw/maw-s-007-01.svg" alt="Hope Veil" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">HE</span><span class="sector-tag">SE-007</span></div></div><h3 class="entity-card-name">THE HOPE VEIL</h3><p class="entity-card-desc">Vaporous thermal coat shielding against psychic hallucinations.</p><a href="maw-s-007-01-the-hope-veil.html" class="jump-btn">VIEW SUIT SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#a855f7;"><div class="entity-card-top"><img src="../assets/art/maw/maw-s-009-01.svg" alt="Forgotten Veil" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">WAW</span><span class="sector-tag">SE-009</span></div></div><h3 class="entity-card-name">THE FORGOTTEN VEIL</h3><p class="entity-card-desc">Woven memory armor neutralizing chemical and corrosive rot.</p><a href="maw-s-009-01-the-forgotten-veil.html" class="jump-btn">VIEW SUIT SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#ef4444;"><div class="entity-card-top"><img src="../assets/art/maw/maw-s-010-01.svg" alt="Absolute Mantle" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">ALEPH</span><span class="sector-tag">SE-010</span></div></div><h3 class="entity-card-name">THE ABSOLUTE MANTLE</h3><p class="entity-card-desc">Singularity cuirass with universal resistance against all damage.</p><a href="maw-s-010-01-the-absolute-mantle.html" class="jump-btn">VIEW SUIT SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#f1df76;"><div class="entity-card-top"><img src="../assets/art/maw/maw-s-011-01.svg" alt="Listening Shroud" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">HE</span><span class="sector-tag">SE-011</span></div></div><h3 class="entity-card-name">THE LISTENING SHROUD</h3><p class="entity-card-desc">Perimeter-shielded uniform dampening mental shockwaves.</p><a href="maw-s-011-01-the-listening-shroud.html" class="jump-btn">VIEW SUIT SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#a855f7;"><div class="entity-card-top"><img src="../assets/art/maw/maw-s-014-01.svg" alt="Debt Veil" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">WAW</span><span class="sector-tag">SE-014</span></div></div><h3 class="entity-card-name">THE DEBT VEIL</h3><p class="entity-card-desc">Thermal-resistant leather coat forged from debt certificates.</p><a href="maw-s-014-01-the-debt-veil.html" class="jump-btn">VIEW SUIT SPECS →</a></div>
    <div class="pm-entity-card" style="--card-border:#f1df76;"><div class="entity-card-top"><img src="../assets/art/maw/maw-s-015-01.svg" alt="Balance Veil" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">WAW</span><span class="sector-tag">SE-015</span></div></div><h3 class="entity-card-name">THE BALANCE VEIL</h3><p class="entity-card-desc">Harmonized golden vestment offering extreme Pale resistance.</p><a href="maw-s-015-01-the-balance-veil.html" class="jump-btn">VIEW SUIT SPECS →</a></div>
  </div>

  <h2 id="gifts-catalog" class="sub-category-header" style="margin-top: 3rem;">/// 3. M.A.W. GIFTS ARSENAL (9 RESONANCE RELICS)</h2>
  <div class="hub-grid-3">
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/art/maw/maw-g-001-01.svg" alt="Lament's Edge" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-can">CAN</span><span class="sector-tag">SE-001</span></div></div><h3 class="entity-card-name">LAMENT'S EDGE</h3><p class="entity-card-desc">Brooch granting +3 Max SP and +2 Attack Speed.</p><a href="maw-g-001-01-laments-edge.html" class="jump-btn">VIEW GIFT SPECS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/art/maw/maw-g-002-01.svg" alt="Mourning Shell" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-teth">TETH</span><span class="sector-tag">SE-002</span></div></div><h3 class="entity-card-name">THE MOURNING SHELL</h3><p class="entity-card-desc">Stone pauldron boosting Physical Defense by +15%.</p><a href="maw-g-002-01-the-mourning-shell.html" class="jump-btn">VIEW GIFT SPECS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/art/maw/maw-g-005-01.svg" alt="The Embrace" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">HE</span><span class="sector-tag">SE-005</span></div></div><h3 class="entity-card-name">THE EMBRACE</h3><p class="entity-card-desc">Silk choker recovering 5% SP upon successful work.</p><a href="maw-g-005-01-the-embrace.html" class="jump-btn">VIEW GIFT SPECS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/art/maw/maw-g-007-01.svg" alt="Hope Lantern" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">HE</span><span class="sector-tag">SE-007</span></div></div><h3 class="entity-card-name">THE HOPE LANTERN</h3><p class="entity-card-desc">Floating orb revealing cloaked entities in sectors.</p><a href="maw-g-007-01-the-hope-lantern.html" class="jump-btn">VIEW GIFT SPECS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/art/maw/maw-g-009-01.svg" alt="Forgotten Mask" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">WAW</span><span class="sector-tag">SE-009</span></div></div><h3 class="entity-card-name">THE FORGOTTEN MASK</h3><p class="entity-card-desc">Porcelain visor granting immunity to amnesia hazing.</p><a href="maw-g-009-01-the-forgotten-mask.html" class="jump-btn">VIEW GIFT SPECS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/art/maw/maw-g-010-01.svg" alt="Absolute Verdict" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">ALEPH</span><span class="sector-tag">SE-010</span></div></div><h3 class="entity-card-name">THE ABSOLUTE VERDICT</h3><p class="entity-card-desc">Singularity ring multiplying final clash power by 1.5x.</p><a href="maw-g-010-01-the-absolute-verdict.html" class="jump-btn">VIEW GIFT SPECS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/art/maw/maw-g-011-01.svg" alt="Listening Stone" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">HE</span><span class="sector-tag">SE-011</span></div></div><h3 class="entity-card-name">THE LISTENING STONE</h3><p class="entity-card-desc">Acoustic amulet reflecting 10% of incoming mental damage.</p><a href="maw-g-011-01-the-listening-stone.html" class="jump-btn">VIEW GIFT SPECS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/art/maw/maw-g-014-01.svg" alt="Debt Scale Gift" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">WAW</span><span class="sector-tag">SE-014</span></div></div><h3 class="entity-card-name">THE DEBT SCALE GIFT</h3><p class="entity-card-desc">Gold seal converting damage dealt into Han fuel units.</p><a href="maw-g-014-01-the-debt-scale-gift.html" class="jump-btn">VIEW GIFT SPECS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/art/maw/maw-g-015-01.svg" alt="Balance Pendant" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">WAW</span><span class="sector-tag">SE-015</span></div></div><h3 class="entity-card-name">THE BALANCE PENDANT</h3><p class="entity-card-desc">Harmonic relic preventing instant death from Pale damage once per day.</p><a href="maw-g-015-01-the-balance-pendant.html" class="jump-btn">VIEW GIFT SPECS →</a></div>
  </div>
</div>
'''
wrap_page("maw/index.html", "M.A.W. Equipment Arsenal", "maw", "M.A.W. ARSENAL DIRECTORY", "Complete Compendium of Materialized Agony Weaponry, Extraction Protocols, and Sync Gears", "assets/banners/banner_hero_maw_arsenal.svg", "M.A.W. EQUIPMENT", maw_html)

# =========================================================================
# 3. LORE HUB (lore/index.html)
# =========================================================================
lore_html = '''
<div class="wiki-section">
  <div class="section-banner">
    <h2>/// SOMNARAK LORE, COSMOLOGY & HISTORICAL CHRONICLES</h2>
    <span class="section-tag">ALL 16 CORE CANONICAL ARCHIVES</span>
  </div>
  <p class="section-desc">
    The historical and metaphysical framework of Somnarak spans 1,778 temporal resets, the primordial Alpha Tree, the catastrophic Three Sorrows, and the eventual Dawn of Hope in Year 4,238.
  </p>

  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#f1df76;"><div class="entity-card-top"><img src="../assets/icons/ref_absolvohan.svg" alt="Absolvohan" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">PRIMARY CANON</span></div></div><h3 class="entity-card-name">THE CYCLE & ABSOLVOHAN</h3><p class="entity-card-desc">The 1,778 loops of facility reset from Day 0 to Day 365 leading to the final transcendence.</p><a href="the-cycle-and-absolvohan.html" class="jump-btn">READ 9-PART CHRONICLE →</a></div>
    <div class="pm-entity-card" style="--card-border:#38bdf8;"><div class="entity-card-top"><img src="../assets/layout/city/icons/icon_alpha_tree.svg" alt="Alpha Tree" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">SOURCE OF HAN</span></div></div><h3 class="entity-card-name">THE ALPHA TREE</h3><p class="entity-card-desc">The subterranean arboreal organism whose sap channels infinite emotional Han fuel.</p><a href="the-alpha-tree.html" class="jump-btn">VIEW ARBOREAL DOSSIER →</a></div>
    <div class="pm-entity-card" style="--card-border:#ef4444;"><div class="entity-card-top"><img src="../assets/icons/banner_grudge.svg" alt="Three Sorrows" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">METAPHYSICS</span></div></div><h3 class="entity-card-name">THE THREE SORROWS</h3><p class="entity-card-desc">The primordial metaphysical cataclysms: Grief, Oblivion, and the Final Void.</p><a href="the-three-sorrows.html" class="jump-btn">VIEW METAPHYSICAL MATRIX →</a></div>
    <div class="pm-entity-card" style="--card-border:#ef5b55;"><div class="entity-card-top"><img src="../assets/icons/taboo.svg" alt="Taboos" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">CITY LAW</span></div></div><h3 class="entity-card-name">THE SEVEN ABSOLUTE TABOOS</h3><p class="entity-card-desc">The immutable legal codex enforced across Somnarak City on pain of instant execution.</p><a href="the-seven-absolute-taboos.html" class="jump-btn">EXAMINE LAW CODES →</a></div>
    <div class="pm-entity-card" style="--card-border:#ef4444;"><div class="entity-card-top"><img src="../assets/icons/ref_cheongula.svg" alt="Cheongula" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">DISASTER LOG</span></div></div><h3 class="entity-card-name">THE CHEONGULA INCIDENT</h3><p class="entity-card-desc">The cataclysmic breach of Year 3,892 that ruptured the southern district walls.</p><a href="the-cheongula-incident.html" class="jump-btn">VIEW DISASTER LOGS →</a></div>
    <div class="pm-entity-card" style="--card-border:#10b981;"><div class="entity-card-top"><img src="../assets/icons/art_dawn.svg" alt="Dawn of Hope" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-can">YEAR 4,238</span></div></div><h3 class="entity-card-name">THE DAWN OF HOPE</h3><p class="entity-card-desc">The historic culmination of the 1,778th cycle and the liberation of human consciousness.</p><a href="the-dawn-of-hope.html" class="jump-btn">READ LIBERATION TEXT →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_dream_realm.svg" alt="Doorspeech" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">LINGUISTICS</span></div></div><h3 class="entity-card-name">THE DOORSPEECH</h3><p class="entity-card-desc">Sub-vocal dialect used to communicate through sealed containment barriers.</p><a href="the-doorspeech.html" class="jump-btn">READ LINGUISTIC STUDY →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_dream_realm.svg" alt="Dream Realm" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">DIMENSION</span></div></div><h3 class="entity-card-name">THE DREAM REALM</h3><p class="entity-card-desc">The collective subconscious realm from which Sorrow Entities crystallize.</p><a href="the-dream-realm.html" class="jump-btn">VIEW REALM TOPOLOGY →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_daily_life.svg" alt="Daily Life" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-can">SOCIOLOGY</span></div></div><h3 class="entity-card-name">DAILY LIFE IN SOMNARAK</h3><p class="entity-card-desc">Civilian routines, Veil ration cards, memory filtration, and urban lifestyle.</p><a href="daily-life-in-somnarak.html" class="jump-btn">VIEW CIVILIAN DOSSIER →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/fracture.svg" alt="Efflorescence" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">PSYCHOLOGY</span></div></div><h3 class="entity-card-name">EFFLORESCENCE & FRACTURE</h3><p class="entity-card-desc">The psychological manifestation of E.G.O. weapons vs Distortion collapse.</p><a href="efflorescence-and-fracture.html" class="jump-btn">EXAMINE PSYCH-METRICS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_named_fractures.svg" alt="Named Fractures" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">INCIDENT ARCHIVE</span></div></div><h3 class="entity-card-name">NAMED FRACTURES</h3><p class="entity-card-desc">The twelve catastrophic Han breaches that permanently altered the city geography.</p><a href="named-fractures.html" class="jump-btn">VIEW FRACTURE LOGS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/banner_weight.svg" alt="Night Hazards" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">SURVIVAL</span></div></div><h3 class="entity-card-name">NIGHT HAZARDS & VIGIL</h3><p class="entity-card-desc">Curfew protocols and nocturnal entities active between 22:00 and 06:00.</p><a href="night-hazards-and-vigil.html" class="jump-btn">EXAMINE VIGIL RULES →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/banner_lore.svg" alt="Cosmology" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">COSMOLOGY</span></div></div><h3 class="entity-card-name">SOMNARAK COSMOLOGY</h3><p class="entity-card-desc">The five ontological layers of reality separating the Upper City from the Abyss.</p><a href="somnarak-cosmology.html" class="jump-btn">EXPLORE 5 LAYERS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_name_registry.svg" alt="Name Registry" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-can">REGISTRY</span></div></div><h3 class="entity-card-name">SOMNARAK NAME REGISTRY</h3><p class="entity-card-desc">Official onomasticon and phonetic naming conventions of the Directorate.</p><a href="somnarak-name-registry.html" class="jump-btn">VIEW NAME ROSTER →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_project_somnarak.svg" alt="Three Ages" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">TIMELINE</span></div></div><h3 class="entity-card-name">THE THREE AGES & HISTORY</h3><p class="entity-card-desc">The complete 4,000-year chronology: Age of Dawn, Age of Iron, Age of Sorrow.</p><a href="the-three-ages-and-history.html" class="jump-btn">READ COMPLETE TIMELINE →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_the_weeping.svg" alt="Weeping River" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-teth">HYDROLOGY</span></div></div><h3 class="entity-card-name">THE WEEPING RIVER</h3><p class="entity-card-desc">Subterranean effluent waterways channeling liquefied remorse through the city.</p><a href="the-weeping-river.html" class="jump-btn">VIEW WATERWAY ATLAS →</a></div>
  </div>
</div>
'''
wrap_page("lore/index.html", "Lore & Cosmology Compendium", "lore", "LORE & COSMOLOGY CHRONICLES", "Canonical History, Metaphysical Axioms, The 1,778 Cycles, and Directorate Historical Records", "assets/banners/banner_hero_lore_absolvohan.svg", "LORE & COSMOLOGY", lore_html)

# =========================================================================
# 4. MECHANICS HUB (mechanics/index.html)
# =========================================================================
mechanics_html = '''
<div class="wiki-section">
  <div class="section-banner">
    <h2>/// SYSTEMS, COMBAT RULES & CONTAINMENT MECHANICS</h2>
    <span class="section-tag">ALL 14 CORE OPERATIONAL FRAMEWORKS</span>
  </div>
  <p class="section-desc">
    Facility management and tactical field operations in Somnarak adhere to strict mathematical formulas, damage types, work affinities, and resonance clash rules.
  </p>

  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#ef4444;"><div class="entity-card-top"><img src="../assets/icons/damage_red.svg" alt="Damage Matrix" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">CORE COMBAT</span></div></div><h3 class="entity-card-name">HAN ENERGY & DAMAGE</h3><p class="entity-card-desc">The 4 Damage Types: Physical (RED), Mental (WHITE), Corrosive (BLACK), and Pale (PALE).</p><a href="han-energy-and-damage.html" class="jump-btn">VIEW DAMAGE MATRIX →</a></div>
    <div class="pm-entity-card" style="--card-border:#f1df76;"><div class="entity-card-top"><img src="../assets/icons/work_extraction.svg" alt="Work Types" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">CONTAINMENT</span></div></div><h3 class="entity-card-name">THE FOUR WORK TYPES</h3><p class="entity-card-desc">Instinct (Ferrehan), Insight (Viderehan), Attachment (Flerehan), Repression (Pugnahan).</p><a href="the-four-work-types.html" class="jump-btn">VIEW WORK FORMULAS →</a></div>
    <div class="pm-entity-card" style="--card-border:#38bdf8;"><div class="entity-card-top"><img src="../assets/icons/risk_aleph.svg" alt="SECC System" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">CLASSIFICATION</span></div></div><h3 class="entity-card-name">SECC CLASSIFICATION</h3><p class="entity-card-desc">Threat rating hierarchy from T-01 CAN up to catastrophic T-05 ALEPH breach tiers.</p><a href="secc-classification-system.html" class="jump-btn">VIEW RISK TIERS →</a></div>
    <div class="pm-entity-card" style="--card-border:#ef5b55;"><div class="entity-card-top"><img src="../assets/icons/ref_battle_system.svg" alt="Resonant Clash" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">CLASH SYSTEM</span></div></div><h3 class="entity-card-name">RESONANT CLASH RULES</h3><p class="entity-card-desc">Dice clash formulas, speed priority, coin flips, and stagger threshold calculation.</p><a href="resonant-clash-mechanics.html" class="jump-btn">VIEW CLASH RULES →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/banner_ordeals.svg" alt="Ordeals" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">FACILITY THREAT</span></div></div><h3 class="entity-card-name">ORDEALS FRAMEWORK</h3><p class="entity-card-desc">Dawn, Noon, Dusk, and Midnight timed incursions invading facility floors.</p><a href="ordeals-framework.html" class="jump-btn">VIEW ORDEAL WAVES →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_full_cast.svg" alt="Agent Stats" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-can">AGENT STATS</span></div></div><h3 class="entity-card-name">AGENT ATTRIBUTES & STATS</h3><p class="entity-card-desc">Fortitude (HP), Prudence (SP), Temperance (Success/Speed), and Justice (Attack/Evade).</p><a href="agent-attributes-and-stats.html" class="jump-btn">VIEW STAT CHARTS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/man_hazard.svg" alt="Containment" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">FACILITY OPS</span></div></div><h3 class="entity-card-name">CONTAINMENT & SUPPRESSION</h3><p class="entity-card-desc">Qliphoth counters, escape conditions, chamber meltdown timers, and suppression squads.</p><a href="containment-and-suppression.html" class="jump-btn">VIEW OPS PROTOCOL →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/weapon.svg" alt="Standard Equipment" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-can">STANDARD GEAR</span></div></div><h3 class="entity-card-name">DEFAULT STANDARD EQUIPMENT</h3><p class="entity-card-desc">Standard Directorate issue batons, tactical suits, and shock protection kits.</p><a href="default-standard-equipment.html" class="jump-btn">VIEW STANDARD ISSUE →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_enemy_list.svg" alt="Bestiary" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">BESTIARY</span></div></div><h3 class="entity-card-name">ENEMY BESTIARY</h3><p class="entity-card-desc">Tactical profiles of Outskirt Distortions, Rogue Operatives, and Wound Walkers.</p><a href="enemy-bestiary.html" class="jump-btn">VIEW BESTIARY ROSTER →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/fracture.svg" alt="Therapy" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">PSYCH RECOVERY</span></div></div><h3 class="entity-card-name">FRACTURE & THERAPY</h3><p class="entity-card-desc">Panic states (Murder, Suicide, Wander, Shutdown) and psychological rehabilitation.</p><a href="fracture-and-therapy.html" class="jump-btn">VIEW THERAPY PROTOCOLS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_han_relics.svg" alt="Relic Registry" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">RELIC CODEX</span></div></div><h3 class="entity-card-name">HAN RELIC REGISTRY</h3><p class="entity-card-desc">Master catalog of recovered pre-Cataclysm Han artifacts and anomalous tools.</p><a href="han-relic-registry.html" class="jump-btn">VIEW RELIC CATALOG →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/tool.svg" alt="Relic Tools" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">OPERATIONAL GEAR</span></div></div><h3 class="entity-card-name">HAN RELICS & TOOLS</h3><p class="entity-card-desc">Deployable field relics providing passive facility buffs and extraction boosts.</p><a href="han-relics-and-tools.html" class="jump-btn">VIEW TOOL MECHANICS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/banner_maw.svg" alt="MAW System" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">EXTRACTION</span></div></div><h3 class="entity-card-name">M.A.W. EQUIPMENT SYSTEM</h3><p class="entity-card-desc">Extraction formulas, Sync Ratios, equipment loss penalties, and resonance tuning.</p><a href="maw-equipment-system.html" class="jump-btn">VIEW SYSTEM RULES →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_taboo_resonance.svg" alt="Taboo Resonance" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">TABOO SYSTEM</span></div></div><h3 class="entity-card-name">TABOO RESONANCE MECHANICS</h3><p class="entity-card-desc">Sanction build-up meters, retribution waves, and Giltong enforcement triggers.</p><a href="taboo-resonance-mechanics.html" class="jump-btn">VIEW TABOO RULES →</a></div>
  </div>
</div>
'''
wrap_page("mechanics/index.html", "Systems & Mechanics Guide", "mechanics", "SYSTEMS & COMBAT MECHANICS", "Operational Rules, Containment Procedures, Damage Matrices, and Tactical Clash Calculations", "assets/banners/banner_hero_combat_mechanics.svg", "SYSTEMS & MECHANICS", mechanics_html)

# =========================================================================
# 5. FACTIONS HUB (factions/index.html)
# =========================================================================
factions_html = '''
<div class="wiki-section">
  <div class="section-banner">
    <h2>/// FACTIONS, GOVERNING BODIES & SYNDICATES</h2>
    <span class="section-tag">ALL 14 CANONICAL ORGANIZATIONS</span>
  </div>
  <p class="section-desc">
    Power in Somnarak is divided between the authoritarian Reverie Directorate, the Supreme High Council, the four great artisan guilds, outskirt nomadic cartels, and underworld syndicates.
  </p>

  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#ef5b55;"><div class="entity-card-top"><img src="../assets/icons/icon_faction_reverie_directorate.svg" alt="Directorate" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">SUPREME RULER</span></div></div><h3 class="entity-card-name">THE REVERIE DIRECTORATE</h3><p class="entity-card-desc">The supreme metropolitan authority governing all 8 districts and Hand of Change operations.</p><a href="the-reverie-directorate.html" class="jump-btn">VIEW MASTER DOSSIER →</a></div>
    <div class="pm-entity-card" style="--card-border:#f1df76;"><div class="entity-card-top"><img src="../assets/icons/icon_faction_high_council.svg" alt="High Council" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">COUNCIL OF SIGHS</span></div></div><h3 class="entity-card-name">THE HIGH COUNCIL</h3><p class="entity-card-desc">The executive board of corporate magnates directing city-wide Veil energy rationing.</p><a href="the-high-council.html" class="jump-btn">VIEW COUNCIL REGISTER →</a></div>
    <div class="pm-entity-card" style="--card-border:#38bdf8;"><div class="entity-card-top"><img src="../assets/icons/icon_faction_sed_corps.svg" alt="SED" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">OUTSKIRT EXPEDITION</span></div></div><h3 class="entity-card-name">SORROW EXPLORATION DIVISION</h3><p class="entity-card-desc">Elite diver corps venturing into The Desolate to map uncharted ruins and retrieve relics.</p><a href="the-sed-corps.html" class="jump-btn">VIEW EXPEDITION LOGS →</a></div>
    <div class="pm-entity-card" style="--card-border:#ef5b55;"><div class="entity-card-top"><img src="../assets/icons/icon_faction_ucd_strike.svg" alt="UCD" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">TACTICAL RESPONSE</span></div></div><h3 class="entity-card-name">UNDERWORLD CONTAINMENT (UCD)</h3><p class="entity-card-desc">Heavily armed rapid breach suppression units deploying to neutralize urban outbreaks.</p><a href="the-ucd-strike-force.html" class="jump-btn">VIEW TACTICAL RAIDS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_architects.svg" alt="Architects" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">MASTER GUILD</span></div></div><h3 class="entity-card-name">THE ARCHITECTS</h3><p class="entity-card-desc">Master builders responsible for kinetic containment vaults and structural resonance integrity.</p><a href="the-architects.html" class="jump-btn">VIEW GUILD DOSSIER →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_weavers.svg" alt="Weavers" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">MASTER GUILD</span></div></div><h3 class="entity-card-name">THE WEAVERS</h3><p class="entity-card-desc">Artisans weaving protective Veil fabrics, synaptic tapestries, and M.A.W. suit linings.</p><a href="the-weavers.html" class="jump-btn">VIEW GUILD DOSSIER →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_wardens.svg" alt="Wardens" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">MASTER GUILD</span></div></div><h3 class="entity-card-name">THE WARDENS</h3><p class="entity-card-desc">Garrison legion manning the Perimeter Bulwark against wasteland horde incursions.</p><a href="the-wardens.html" class="jump-btn">VIEW GUILD DOSSIER →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_collectors.svg" alt="Collectors" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">MASTER GUILD</span></div></div><h3 class="entity-card-name">THE COLLECTORS</h3><p class="entity-card-desc">Scavenger cartel operating in Zone C, trading salvaged pre-Cataclysm microchips and Han scrap.</p><a href="the-collectors.html" class="jump-btn">VIEW GUILD DOSSIER →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_horizon_caravan.svg" alt="Caravan" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">NOMAD CARTEL</span></div></div><h3 class="entity-card-name">THE HORIZON CARAVAN</h3><p class="entity-card-desc">Armored wasteland trading convoys crossing the Desolate between distant citadels.</p><a href="the-horizon-caravan.html" class="jump-btn">VIEW CARAVAN LOGS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_memory_washers.svg" alt="Washers" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">PSYCH POLICE</span></div></div><h3 class="entity-card-name">THE MEMORY WASHERS</h3><p class="entity-card-desc">Covert amnesia operatives erasing traumatic incident memories from civilian survivors.</p><a href="the-memory-washers.html" class="jump-btn">VIEW WASHING LOGS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_giltong_enforcers.svg" alt="Giltong" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">SECURITY</span></div></div><h3 class="entity-card-name">THE GILTONG ENFORCERS</h3><p class="entity-card-desc">Zone security militia enforcing Taboo compliance with lethal automatic suppression.</p><a href="the-giltong-enforcers.html" class="jump-btn">VIEW ENFORCER CODE →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_founding_corps.svg" alt="Founding Corps" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">INDUSTRY</span></div></div><h3 class="entity-card-name">FOUNDING CORPORATIONS</h3><p class="entity-card-desc">The 8 original corporate conglomerates that financed the construction of the Hand.</p><a href="the-founding-corporations.html" class="jump-btn">VIEW CORP ARCHIVES →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_underworld.svg" alt="Underworld" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">SYNDICATE</span></div></div><h3 class="entity-card-name">UNDERWORLD & WOUND WALKERS</h3><p class="entity-card-desc">Illicit black-market syndicates trading in unrefined Han extract and smuggled relics.</p><a href="the-underworld-and-wound-walkers.html" class="jump-btn">VIEW SYNDICATE LOGS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_faction_tech.svg" alt="Faction Tech" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">TECH ARSENAL</span></div></div><h3 class="entity-card-name">FACTION TECHNOLOGY</h3><p class="entity-card-desc">Comparative technical catalog of energy weaponry, veil stabilizers, and barrier shields.</p><a href="faction-technology.html" class="jump-btn">VIEW TECH MATRIX →</a></div>
  </div>
</div>
'''
wrap_page("factions/index.html", "Factions & Organizations Hub", "factions", "FACTIONS & GUILDS DIRECTORY", "Political Powers, Industrial Conglomerates, Master Guilds, and Underworld Syndicates", "assets/banners/banner_hero_factions_council.svg", "FACTIONS & GUILDS", factions_html)

# =========================================================================
# 6. LOCATIONS HUB (locations/index.html)
# =========================================================================
locations_html = '''
<div class="wiki-section">
  <div class="section-banner">
    <h2>/// METROPOLITAN ZONES, CARTOGRAPHY & WASTELANDS</h2>
    <span class="section-tag">ALL 12 CANONICAL URBAN & WASTELAND SECTORS</span>
  </div>
  <p class="section-desc">
    The urban geography of Somnarak is centered around the Directorate Spire in Zone A, extending through industrial sectors to the outer Perimeter Bulwark and the lethal radioactive Desolate.
  </p>

  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#ef5b55;"><div class="entity-card-top"><img src="../assets/layout/city/icons/icon_zone_a_core.svg" alt="Zone A" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">SECTOR A</span></div></div><h3 class="entity-card-name">ZONE A: CORE NEXUS</h3><p class="entity-card-desc">The central governmental spire housing the Alpha Tree root complex and Directorate Command.</p><a href="zone-a-core-nexus.html" class="jump-btn">ENTER CORE NEXUS →</a></div>
    <div class="pm-entity-card" style="--card-border:#38bdf8;"><div class="entity-card-top"><img src="../assets/layout/city/icons/icon_zone_b_west.svg" alt="Zone B" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-can">SECTOR B</span></div></div><h3 class="entity-card-name">ZONE B: WEST WARD</h3><p class="entity-card-desc">Densely populated residential mega-blocks sheltered beneath atmospheric filtration domes.</p><a href="zone-b-west-ward.html" class="jump-btn">ENTER WEST WARD →</a></div>
    <div class="pm-entity-card" style="--card-border:#10b981;"><div class="entity-card-top"><img src="../assets/layout/city/icons/icon_zone_c_east.svg" alt="Zone C" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">SECTOR C</span></div></div><h3 class="entity-card-name">ZONE C: COLLECTOR'S ROW</h3><p class="entity-card-desc">Sprawling industrial scrap-yards, relic bazaars, and illicit modification workshops.</p><a href="zone-c-collectors-row.html" class="jump-btn">ENTER COLLECTOR'S ROW →</a></div>
    <div class="pm-entity-card" style="--card-border:#47c978;"><div class="entity-card-top"><img src="../assets/layout/city/icons/icon_zone_d_flanks.svg" alt="Zone D" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">SECTOR D</span></div></div><h3 class="entity-card-name">ZONE D: FORGE & GARDENS</h3><p class="entity-card-desc">High-tech R&D foundries and bio-synthetic botanical gardens cultivating Han flora.</p><a href="zone-d-forge-and-gardens.html" class="jump-btn">ENTER FORGE & GARDENS →</a></div>
    <div class="pm-entity-card" style="--card-border:#f59e0b;"><div class="entity-card-top"><img src="../assets/layout/city/icons/icon_zone_e_bulwark.svg" alt="Zone E" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">SECTOR E</span></div></div><h3 class="entity-card-name">ZONE E: PERIMETER BULWARK</h3><p class="entity-card-desc">Massive 400-meter outer perimeter battlements guarding against the outer wasteland.</p><a href="zone-e-perimeter-bulwark.html" class="jump-btn">ENTER PERIMETER BULWARK →</a></div>
    <div class="pm-entity-card" style="--card-border:#ef4444;"><div class="entity-card-top"><img src="../assets/icons/ref_the_desolate.svg" alt="The Desolate" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">OUTSKIRTS</span></div></div><h3 class="entity-card-name">THE DESOLATE (황무지)</h3><p class="entity-card-desc">Radioactive crystalline wasteland populated by rogue Distortions and wandering scavengers.</p><a href="the-desolate.html" class="jump-btn">VIEW WASTELAND ATLAS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/banner_locations.svg" alt="Hollow Glass" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">ANOMALY ZONE</span></div></div><h3 class="entity-card-name">THE HOLLOW GLASS</h3><p class="entity-card-desc">Vitrified desert plain where sound and memories freeze into solid crystalline pillars.</p><a href="the-hollow-glass.html" class="jump-btn">VIEW HOLLOW GLASS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_memory_archive.svg" alt="Library" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">ARCHIVE VAULT</span></div></div><h3 class="entity-card-name">LIBRARY OF STOLEN PASTS</h3><p class="entity-card-desc">Subterranean memory vault storing erased historical scrolls and forbidden records.</p><a href="the-library-of-stolen-pasts.html" class="jump-btn">ENTER THE LIBRARY →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/maw.svg" alt="The Maw" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">EXTRACTION PIT</span></div></div><h3 class="entity-card-name">THE MAW</h3><p class="entity-card-desc">The abyssal containment pit where raw Sorrow Entities are harvested for energy extraction.</p><a href="the-maw.html" class="jump-btn">ENTER THE MAW →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/art_bell.svg" alt="Bell Tower" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">MONUMENT</span></div></div><h3 class="entity-card-name">ORPHAN BELL TOWER</h3><p class="entity-card-desc">Historic clockwork monument housing the resonant bell that signals morning curfew lift.</p><a href="the-orphan-bell-tower.html" class="jump-btn">VIEW BELL TOWER →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_unknown_cities.svg" alt="Unknown Cities" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">PRECURSOR RUINS</span></div></div><h3 class="entity-card-name">UNKNOWN CITIES & RUINS</h3><p class="entity-card-desc">Submerged precursor metropolises lost beneath the radioactive dust of the deep wasteland.</p><a href="unknown-cities.html" class="jump-btn">EXPLORE RUIN ATLAS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/layout/city/icons/icon_somnarak_city_badge.svg" alt="District Structure" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-can">ZONING CODE</span></div></div><h3 class="entity-card-name">DISTRICT STRUCTURE & VEIL</h3><p class="entity-card-desc">Urban architectural blueprints detailing the 8 districts, Veil boundaries, and rail routes.</p><a href="district-structure-veil-and-raw.html" class="jump-btn">VIEW URBAN SCHEMATIC →</a></div>
  </div>
</div>
'''
wrap_page("locations/index.html", "Atlas & Cartography Hub", "locations", "SOMNARAK URBAN & WASTELAND ATLAS", "City Sectors, Metropolitan Zones, Outskirt Bastions, and Uncharted Precursor Citadels", "assets/banners/banner_hero_somnarak_city.svg", "ATLAS & LOCATIONS", locations_html)

# =========================================================================
# 7. CHARACTERS HUB (characters/index.html)
# =========================================================================
characters_html = '''
<div class="wiki-section">
  <div class="section-banner">
    <h2>/// THE NINE ECHO-CORES & OPERATIONAL PERSONNEL</h2>
    <span class="section-tag">ALL 19 PRIMARY & SECONDARY ROSTER PROFILES</span>
  </div>
  <p class="section-desc">
    The facility is overseen by nine immortal Echo-Core leads who retain memories across resets, supported by frontline field commanders, tactical operatives, and civilian guild representatives.
  </p>

  <h2 class="sub-category-header">/// 1. THE NINE ECHO-CORES (EXECUTIVE COMMAND)</h2>
  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#ef5b55;"><div class="entity-card-top"><img src="../assets/avatars/avatar_core_majin.svg" alt="Majin" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">THE DIRECTOR</span><span class="sector-tag">CORE 01</span></div></div><h3 class="entity-card-name">DIRECTOR MAJIN</h3><p class="entity-card-desc">Mastermind behind Project Somnarak, bearing the crushing burden of 1,778 resets.</p><a href="the-director-majin.html" class="jump-btn">VIEW EXECUTIVE DOSSIER →</a></div>
    <div class="pm-entity-card" style="--card-border:#5b75e8;"><div class="entity-card-top"><img src="../assets/avatars/avatar_core_seiyon.svg" alt="Seiyon" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">THE SECRETARY</span><span class="sector-tag">CORE 02</span></div></div><h3 class="entity-card-name">SECRETARY SEIYON</h3><p class="entity-card-desc">Facility administrator managing administrative routines, supply logistics, and resets.</p><a href="the-secretary-seiyon.html" class="jump-btn">VIEW EXECUTIVE DOSSIER →</a></div>
    <div class="pm-entity-card" style="--card-border:#38bdf8;"><div class="entity-card-top"><img src="../assets/avatars/avatar_core_dekan.svg" alt="Dekan" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">CONTAINMENT LEAD</span><span class="sector-tag">CORE 03</span></div></div><h3 class="entity-card-name">LEAD DEKAN</h3><p class="entity-card-desc">Commander of Maw's Keep, specialized in direct physical containment and kinetic seals.</p><a href="the-containment-lead-dekan.html" class="jump-btn">VIEW EXECUTIVE DOSSIER →</a></div>
    <div class="pm-entity-card" style="--card-border:#e6c843;"><div class="entity-card-top"><img src="../assets/avatars/avatar_core_zyrak.svg" alt="Zyrak" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">EXTRACTION LEAD</span><span class="sector-tag">CORE 04</span></div></div><h3 class="entity-card-name">LEAD ZYRAK</h3><p class="entity-card-desc">Master of Floor 3 Extraction Hall, forging raw entity agony into high-grade M.A.W. gear.</p><a href="the-extraction-lead-zyrak.html" class="jump-btn">VIEW EXECUTIVE DOSSIER →</a></div>
    <div class="pm-entity-card" style="--card-border:#47c978;"><div class="entity-card-top"><img src="../assets/avatars/avatar_core_ayshuk.svg" alt="Ayshuk" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">RESEARCH LEAD</span><span class="sector-tag">CORE 05</span></div></div><h3 class="entity-card-name">LEAD AYSHUK</h3><p class="entity-card-desc">Director of Insight Forge, unlocking metaphysical mysteries and Han chemical synthesis.</p><a href="the-research-lead-ayshuk.html" class="jump-btn">VIEW EXECUTIVE DOSSIER →</a></div>
    <div class="pm-entity-card" style="--card-border:#d4d4d8;"><div class="entity-card-top"><img src="../assets/avatars/avatar_core_mellda.svg" alt="Mellda" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">BORDER LEAD</span><span class="sector-tag">CORE 06</span></div></div><h3 class="entity-card-name">LEAD MELLDA</h3><p class="entity-card-desc">Commander of Border Watch, defending the facility perimeter against wasteland hordes.</p><a href="the-border-lead-mellda.html" class="jump-btn">VIEW EXECUTIVE DOSSIER →</a></div>
    <div class="pm-entity-card" style="--card-border:#be123c;"><div class="entity-card-top"><img src="../assets/avatars/avatar_core_marjuk.svg" alt="Marjuk" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">ARCHIVE LEAD</span><span class="sector-tag">CORE 07</span></div></div><h3 class="entity-card-name">LEAD MARJUK</h3><p class="entity-card-desc">Keeper of Deep Vault archives, guarding forgotten truths, ledgers, and cycle logs.</p><a href="the-archive-lead-marjuk.html" class="jump-btn">VIEW EXECUTIVE DOSSIER →</a></div>
    <div class="pm-entity-card" style="--card-border:#f43f5e;"><div class="entity-card-top"><img src="../assets/avatars/avatar_core_ishall.svg" alt="Ishall" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">THE OUTSIDER</span><span class="sector-tag">CORE 08</span></div></div><h3 class="entity-card-name">LEAD ISHALL</h3><p class="entity-card-desc">Commander of Shadow Corps void divers navigating uncharted abyssal currents.</p><a href="the-outsider-ishall.html" class="jump-btn">VIEW EXECUTIVE DOSSIER →</a></div>
    <div class="pm-entity-card" style="--card-border:#fbbf24;"><div class="entity-card-top"><img src="../assets/avatars/avatar_core_xyan.svg" alt="Xyan" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">THE EXILE</span><span class="sector-tag">CORE 09</span></div></div><h3 class="entity-card-name">LEAD XYAN</h3><p class="entity-card-desc">Sentinel of Gate Watch, guarding the forbidden portal leading beyond Somnarak.</p><a href="the-exile-xyan.html" class="jump-btn">VIEW EXECUTIVE DOSSIER →</a></div>
  </div>

  <h2 class="sub-category-header" style="margin-top: 3rem;">/// 2. SECONDARY OPERATIVES & CIVILIANS (10 PROFILES)</h2>
  <div class="hub-grid-3">
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_full_cast.svg" alt="Minho" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">FIELD AGENT</span></div></div><h3 class="entity-card-name">MINHO</h3><p class="entity-card-desc">Veteran SED scout surviving 40+ deep wasteland excursions.</p><a href="minho.html" class="jump-btn">VIEW PROFILE →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_full_cast.svg" alt="Doha" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-can">MERCHANT</span></div></div><h3 class="entity-card-name">DOHA</h3><p class="entity-card-desc">Collector guildmaster trading illegal Han injectors in Zone C.</p><a href="doha.html" class="jump-btn">VIEW PROFILE →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_full_cast.svg" alt="Soojin" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">RESEARCHER</span></div></div><h3 class="entity-card-name">SOOJIN</h3><p class="entity-card-desc">Senior Insight Forge alchemist decoding synaptic frequencies.</p><a href="soojin.html" class="jump-btn">VIEW PROFILE →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_full_cast.svg" alt="Sora" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-can">CIVILIAN</span></div></div><h3 class="entity-card-name">SORA</h3><p class="entity-card-desc">Underground ballad singer chronicling the pre-Cataclysm city.</p><a href="sora.html" class="jump-btn">VIEW PROFILE →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_full_cast.svg" alt="Taeho" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">STRIKE CAPTAIN</span></div></div><h3 class="entity-card-name">TAEHO</h3><p class="entity-card-desc">UCD strike commander leading urban breach containment raids.</p><a href="taeho.html" class="jump-btn">VIEW PROFILE →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_full_cast.svg" alt="Kael" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">CARAVAN MASTER</span></div></div><h3 class="entity-card-name">KAEL</h3><p class="entity-card-desc">Horizon Caravan driver traversing uncharted wasteland routes.</p><a href="kael.html" class="jump-btn">VIEW PROFILE →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_full_cast.svg" alt="Yeonhwa" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">WEAVER ARTISAN</span></div></div><h3 class="entity-card-name">YEONHWA</h3><p class="entity-card-desc">Master weaver tailoring high-grade M.A.W. suit linings.</p><a href="yeonhwa.html" class="jump-btn">VIEW PROFILE →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_full_cast.svg" alt="Joon" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-can">ENGINEER</span></div></div><h3 class="entity-card-name">JOON</h3><p class="entity-card-desc">Floor 3 siphon technician maintaining Han extraction pumps.</p><a href="joon.html" class="jump-btn">VIEW PROFILE →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/ref_full_cast.svg" alt="Refugees" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">SURVIVORS</span></div></div><h3 class="entity-card-name">CHEONBULOK REFUGEES</h3><p class="entity-card-desc">Survivors of the destroyed southern citadel seeking shelter.</p><a href="cheonbulok-refugees.html" class="jump-btn">VIEW DOSSIER →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/fac_architects.svg" alt="Architects" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">GUILD COUNCIL</span></div></div><h3 class="entity-card-name">HIGH ARCHITECTS</h3><p class="entity-card-desc">Founding engineers who drafted the 8-floor facility blue-prints.</p><a href="high-architects.html" class="jump-btn">VIEW DOSSIER →</a></div>
  </div>
</div>
'''
wrap_page("characters/index.html", "Personnel & Echo-Cores Hub", "characters", "CHARACTERS & PERSONNEL ROSTER", "The Nine Immortal Echo-Cores, Field Operatives, Guild Masters, and Civilian Survivors", "assets/banners/banner_hero_echo_cores.svg", "CHARACTERS & PERSONNEL", characters_html)

# =========================================================================
# 8. DEPARTMENTS HUB (departments/index.html)
# =========================================================================
departments_html = '''
<div class="wiki-section">
  <div class="section-banner">
    <h2>/// THE EIGHT FACILITY FLOORS & TECHNICAL ARCHIVES</h2>
    <span class="section-tag">ALL 10 SECTOR PROFILES & TECHNICAL SCHEMATICS</span>
  </div>
  <p class="section-desc">
    Facility 01 "The Hand of Change" is structured across eight subterranean sectors descending from the surface Palm Core down to the Taboo Gate, each overseen by a dedicated Echo-Core department lead.
  </p>

  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#ef5b55;"><div class="entity-card-top"><img src="../assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt="Floor 1" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">FLOOR 01</span><span class="sector-tag">PALM CORE</span></div></div><h3 class="entity-card-name">NEUTRAL COMMAND</h3><p class="entity-card-desc">Directorate headquarters overseeing central power distribution, alerts, and personnel assignments.</p><div class="entity-card-stats"><span><b>Lead:</b> Director Majin</span><span><b>Role:</b> Administration</span></div><a href="floor-1-neutral-command.html" class="jump-btn">ENTER FLOOR 1 →</a></div>
    <div class="pm-entity-card" style="--card-border:#5b75e8;"><div class="entity-card-top"><img src="../assets/layout/hand/icons/icon_dept_f2_maws_keep.svg" alt="Floor 2" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">FLOOR 02</span><span class="sector-tag">WARD KEEP</span></div></div><h3 class="entity-card-name">MAW'S KEEP</h3><p class="entity-card-desc">Heavy physical containment sectors housing high-mass Sorrow Entities with kinetic dampeners.</p><div class="entity-card-stats"><span><b>Lead:</b> Dekan</span><span><b>Role:</b> Containment</span></div><a href="floor-2-maws-keep.html" class="jump-btn">ENTER FLOOR 2 →</a></div>
    <div class="pm-entity-card" style="--card-border:#e6c843;"><div class="entity-card-top"><img src="../assets/layout/hand/icons/icon_dept_f3_extraction.svg" alt="Floor 3" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">FLOOR 03</span><span class="sector-tag">SIPHON FORGE</span></div></div><h3 class="entity-card-name">EXTRACTION HALL</h3><p class="entity-card-desc">M.A.W. manufacturing foundries forging weapons and armor from entity agony resonances.</p><div class="entity-card-stats"><span><b>Lead:</b> Zyrak</span><span><b>Role:</b> Extraction & Forging</span></div><a href="floor-3-extraction-hall.html" class="jump-btn">ENTER FLOOR 3 →</a></div>
    <div class="pm-entity-card" style="--card-border:#47c978;"><div class="entity-card-top"><img src="../assets/layout/hand/icons/icon_dept_f4_insight_forge.svg" alt="Floor 4" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">FLOOR 04</span><span class="sector-tag">RESEARCH CORE</span></div></div><h3 class="entity-card-name">INSIGHT FORGE</h3><p class="entity-card-desc">Metaphysical laboratories conducting cognitive experiments, Han analysis, and psychic mapping.</p><div class="entity-card-stats"><span><b>Lead:</b> Ayshuk</span><span><b>Role:</b> R&D & Alchemy</span></div><a href="floor-4-insight-forge.html" class="jump-btn">ENTER FLOOR 4 →</a></div>
    <div class="pm-entity-card" style="--card-border:#d4d4d8;"><div class="entity-card-top"><img src="../assets/layout/hand/icons/icon_dept_f5_border_watch.svg" alt="Floor 5" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-waw">FLOOR 05</span><span class="sector-tag">BORDER BASTION</span></div></div><h3 class="entity-card-name">BORDER WATCH</h3><p class="entity-card-desc">Subterranean perimeter fortress defending the facility's foundations against burrowing horrors.</p><div class="entity-card-stats"><span><b>Lead:</b> Mellda</span><span><b>Role:</b> Perimeter Defense</span></div><a href="floor-5-border-watch.html" class="jump-btn">ENTER FLOOR 5 →</a></div>
    <div class="pm-entity-card" style="--card-border:#be123c;"><div class="entity-card-top"><img src="../assets/layout/hand/icons/icon_dept_f6_deep_vault.svg" alt="Floor 6" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">FLOOR 06</span><span class="sector-tag">CRYO ARCHIVE</span></div></div><h3 class="entity-card-name">DEEP VAULT</h3><p class="entity-card-desc">Cryogenic archive vaults sealing catastrophic T-05 entities and pre-Cataclysm records.</p><div class="entity-card-stats"><span><b>Lead:</b> Marjuk</span><span><b>Role:</b> Archival & Sealing</span></div><a href="floor-6-deep-vault.html" class="jump-btn">ENTER FLOOR 6 →</a></div>
    <div class="pm-entity-card" style="--card-border:#f43f5e;"><div class="entity-card-top"><img src="../assets/layout/hand/icons/icon_dept_f7_shadow_corps.svg" alt="Floor 7" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">FLOOR 07</span><span class="sector-tag">VOID DIVERS</span></div></div><h3 class="entity-card-name">SHADOW CORPS</h3><p class="entity-card-desc">Void diving staging docks exploring the abyssal currents below the facility foundation.</p><div class="entity-card-stats"><span><b>Lead:</b> Ishall</span><span><b>Role:</b> Void Navigation</span></div><a href="floor-7-shadow-corps.html" class="jump-btn">ENTER FLOOR 7 →</a></div>
    <div class="pm-entity-card" style="--card-border:#fbbf24;"><div class="entity-card-top"><img src="../assets/layout/hand/icons/icon_dept_f8_gate_watch.svg" alt="Floor 8" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">FLOOR 08</span><span class="sector-tag">TABOO GATE</span></div></div><h3 class="entity-card-name">GATE WATCH</h3><p class="entity-card-desc">The final threshold containing the cosmic taboo boundary leading outside Somnarak.</p><div class="entity-card-stats"><span><b>Lead:</b> Xyan</span><span><b>Role:</b> Gate Vigil</span></div><a href="floor-8-gate-watch.html" class="jump-btn">ENTER FLOOR 8 →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/layout/hand/icons/the_hand_dr_icon_styled.svg" alt="Room Types" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">SCHEMATICS</span></div></div><h3 class="entity-card-name">FACILITY ROOM TYPES</h3><p class="entity-card-desc">Architectural classification of containment cells, corridors, elevators, and airlocks.</p><a href="facility-room-types.html" class="jump-btn">VIEW ROOM SCHEMATICS →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/man_hazard.svg" alt="Incident Reports" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-aleph">INCIDENTS</span></div></div><h3 class="entity-card-name">INCIDENT REPORTS ARCHIVE</h3><p class="entity-card-desc">Chronological repository of all facility meltdowns, breaches, and mass casualties.</p><a href="incident-reports-archive.html" class="jump-btn">VIEW INCIDENT LOGS →</a></div>
  </div>
</div>
'''
wrap_page("departments/index.html", "Facility Departments & Floors Hub", "departments", "THE HAND OF CHANGE DEPARTMENTS", "Subterranean Facility 01 Architecture, Sector Commands, and Technical Blueprints", "assets/banners/banner_hero_hand_of_change.svg", "FACILITY DEPARTMENTS", departments_html)

print("Super Hubs updated with Panoramic SVG Hero Banners.")
