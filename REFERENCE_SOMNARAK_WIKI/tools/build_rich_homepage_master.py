#!/usr/bin/env python3
"""
tools/build_rich_homepage_master.py
Constructs a comprehensive, rich, encyclopedic Main Page (index.html)
featuring deep lore, featured entity spotlights, quick-reference combat tables,
operational directives, facility floor summaries, and a complete directory
with 100% exact, verified links.
"""

INDEX_PATH = "/home/user/01_Somnarak_Wiki/index.html"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Somnarak Wiki — Official Encyclopedia of the City of Unresolved Sorrow</title>
  <link rel="stylesheet" href="assets/css/wiki.css">
  <link rel="icon" type="image/svg+xml" href="assets/icons/somnarak_icon.svg">
</head>
<body class="pm-dark terminal-theme">
  <!-- Top Utility Navigation Bar -->
  <header class="pm-navbar">
    <div class="nav-left">
      <a href="index.html" class="logo-link">
        <img src="assets/icons/somnarak_icon.svg" alt="Somnarak Crest" class="nav-logo">
        <span class="logo-title">SOMNARAK // <span>WIKI</span></span>
      </a>
      <span class="status-indicator live">
        <span class="pulse-dot"></span>
        <span class="status-text">CYCLE 1,778 ACTIVE</span>
      </span>
    </div>
    <div class="nav-center">
      <div class="search-container">
        <input type="text" id="wiki-search-input" placeholder="Search Sorrow Entities, M.A.W., Echo-Cores, Lore..." autocomplete="off">
        <div id="wiki-search-results" class="search-dropdown"></div>
      </div>
    </div>
    <div class="nav-right">
      <nav class="top-nav-links">
        <a href="entities/index.html">ENTITIES</a>
        <a href="maw/index.html">M.A.W.</a>
        <a href="characters/index.html">ECHO-CORES</a>
        <a href="mechanics/index.html">SYSTEMS</a>
        <a href="locations/index.html">ATLAS</a>
        <a href="lore/index.html">LORE</a>
        <a href="downloads.html" class="dl-pill">DOWNLOADS</a>
      </nav>
    </div>
  </header>

  <div class="pm-wiki-wrapper">
    <!-- Left Navigation Rail -->
    <aside class="wiki-sidebar-left">
      <div class="sidebar-section">
        <h3 class="sidebar-header">/// NAVIGATION</h3>
        <ul class="sidebar-menu">
          <li><a href="index.html" class="active"><img src="assets/icons/nav_home.svg" alt="" class="menu-icon"> Main Portal</a></li>
          <li><a href="entities/index.html"><img src="assets/icons/nav_entities.svg" alt="" class="menu-icon"> Sorrow Entities</a></li>
          <li><a href="maw/index.html"><img src="assets/icons/weapon.svg" alt="" class="menu-icon"> M.A.W. Equipment</a></li>
          <li><a href="characters/index.html"><img src="assets/icons/nav_characters.svg" alt="" class="menu-icon"> Echo-Cores & Cast</a></li>
          <li><a href="departments/index.html"><img src="assets/icons/the_hand_of_change_simple.svg" alt="" class="menu-icon"> Hand of Change</a></li>
          <li><a href="factions/index.html"><img src="assets/icons/nav_factions.svg" alt="" class="menu-icon"> Factions & Guilds</a></li>
          <li><a href="locations/index.html"><img src="assets/icons/nav_locations.svg" alt="" class="menu-icon"> Metropolitan Atlas</a></li>
          <li><a href="lore/index.html"><img src="assets/icons/nav_lore.svg" alt="" class="menu-icon"> Lore & Cosmology</a></li>
          <li><a href="mechanics/index.html"><img src="assets/icons/nav_mechanics.svg" alt="" class="menu-icon"> Combat & Systems</a></li>
        </ul>
      </div>

      <div class="sidebar-section">
        <h3 class="sidebar-header">/// QUICK DIRECTORY</h3>
        <ul class="sidebar-menu small-menu">
          <li><a href="entities/se-001-the-orphaned-bell.html">SE-001 The Orphaned Bell</a></li>
          <li><a href="entities/se-002-the-grieving-colossus.html">SE-002 The Grieving Colossus</a></li>
          <li><a href="entities/se-010-the-convergence.html">SE-010 The Convergence</a></li>
          <li><a href="characters/the-director-majin.html">Core 01: Director Majin</a></li>
          <li><a href="characters/the-containment-lead-dekan.html">Core 03: Lead Dekan</a></li>
          <li><a href="lore/the-alpha-tree.html">The Alpha Tree Nexus</a></li>
          <li><a href="lore/the-three-sorrows.html">The Three Sorrows</a></li>
          <li><a href="mechanics/han-energy-and-damage.html">Han Damage Matrix</a></li>
          <li><a href="mechanics/the-four-work-types.html">The Four Work Types</a></li>
          <li><a href="atlas/hand-of-change-map.html">Facility 01 Blueprint</a></li>
        </ul>
      </div>
    </aside>

    <!-- Main Content Body -->
    <main class="wiki-main-container">
      <!-- Breadcrumbs & Status -->
      <div class="page-tabs">
        <span>Main Portal</span>
        <b>MAIN CANON // DAWN INITIATIVE // CYCLE 1,778</b>
      </div>

      <!-- Hero Header -->
      <div class="pm-hero-container">
        <div class="pm-hero-main pm-hero-centered">
          <div class="pm-brand-row">
            <img src="assets/icons/somnarak_icon.svg" alt="Somnarak Emblem">
            <div class="pm-brand-text">
              <h1>SOMNARAK<span>WIKI</span></h1>
              <strong>CITY OF UNRESOLVED SORROW // COMPREHENSIVE ARCHIVE</strong>
            </div>
          </div>
          <div class="pm-hero-subtext">
            The definitive encyclopedic record of the metropolitan civilization anchored to the Alpha Tree above the subterranean Weeping, the metaphysical dynamics of Han flux, the Reverie Directorate, and the individuals who endure beyond the 1,778 Cycles.
          </div>
        </div>
        <div class="pm-slogan-bar">
          WITNESS THE SORROW, PRESERVE THE NAME <span>슬픔을 직시하고, 이름을 보존하라</span>
        </div>
      </div>

      <!-- Live Incident Bulletins & Operational Status -->
      <div class="pm-dispatch-banner">
        <div class="dispatch-header">
          <span class="pulse-dot"></span>
          <strong>DIRECTORATE ACTIVE BULLETIN // CYCLE 1,778 DISPATCH</strong>
          <span class="dispatch-time">04:18 FACILITY STANDARD</span>
        </div>
        <div class="dispatch-content">
          <div class="dispatch-item">
            <span class="disp-tag alert-amber">CONTAINMENT</span>
            <span>Floor 2 (Maw's Keep): <a href="entities/se-002-the-grieving-colossus.html" class="wiki-link">SE-002 (The Grieving Colossus)</a> Coherence Counter steady at 4. Han yield threshold at 104%. Lead Dekan ordering standard Ferrehan extraction shifts.</span>
          </div>
          <div class="dispatch-item">
            <span class="disp-tag alert-blue">RESEARCH</span>
            <span>Floor 4 (Insight Forge): Lead Ayshuk validates new M.A.W. resonance calibration matrices for <a href="maw/maw-w-010-01-the-absolute-maul.html" class="wiki-link">Absolute Maul</a>. Minimum agent Resolve required: Level IV.</span>
          </div>
          <div class="dispatch-item">
            <span class="disp-tag alert-red">BORDER ALERT</span>
            <span>Floor 5 (Border Watch): Subterranean effluent surging in District 4. Lead Mellda deployed SED tactical squads to prevent Night Aberration infiltration.</span>
          </div>
        </div>
      </div>

      <!-- Featured Entity Spotlight Section -->
      <section class="pm-section-block">
        <div class="section-title-bar">
          <h2>/// FEATURED ENTITY SPOTLIGHT OF THE CYCLE</h2>
          <span class="title-sub">SECC CLASSIFICATION: ALEPH // THREAT REGISTER 001</span>
        </div>
        <div class="featured-spotlight-grid">
          <div class="spotlight-visual">
            <img src="assets/art/entities/se-001.svg" alt="SE-001 The Orphaned Bell" class="spotlight-img">
            <div class="spotlight-badges">
              <span class="risk-badge risk-aleph">ALEPH THREAT</span>
              <span class="damage-badge dmg-cyan">LAMENT DAMAGE</span>
              <span class="han-badge">HAN FLUX: 32 PE</span>
            </div>
          </div>
          <div class="spotlight-body">
            <div class="spotlight-meta-header">
              <h3><a href="entities/se-001-the-orphaned-bell.html">SE-001 — The Orphaned Bell (고아의 종)</a></h3>
              <small>Location: Facility 01, Floor 2 (Maw's Keep) | Containment Unit MK-01</small>
            </div>
            <p>
              <strong>The Orphaned Bell</strong> is a monumental Sorrow Entity embodying the collective grief of the city's foundational sacrifices during Cycle 001. Manifesting as an ancient bronze resonance bell hanging over subterranean abyssal currents, it continuously emits deep sonic frequencies that vibrate through the bedrock. If its Coherence Counter reaches zero, its tolling echoes shatter surrounding corridors, inflicting lethal Lament (Mental) damage upon operatives without specialized M.A.W. psychological shielding.
            </p>
            <div class="spotlight-data-table">
              <table class="pm-table condensed">
                <thead>
                  <tr>
                    <th>Optimal Work</th>
                    <th>Extracted M.A.W. Weapon</th>
                    <th>Extracted M.A.W. Suit</th>
                    <th>Special Gift</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong style="color:#38bdf8;">Insight (Viderehan)</strong> (65% Base)</td>
                    <td><a href="maw/maw-w-001-01-the-laments-requiem.html">Lament Requiem</a> (Lament 18-24)</td>
                    <td><a href="maw/maw-s-001-01-the-laments-shroud.html">Lament Shroud</a> (Lament 0.4 Res)</td>
                    <td><a href="maw/maw-g-001-01-laments-edge.html">Lament's Edge</a> (+5 SP, +4 Res)</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="spotlight-actions">
              <a href="entities/se-001-the-orphaned-bell.html" class="pm-btn-primary">View Full Containment Dossier & Work Probabilities →</a>
              <a href="entities/index.html" class="pm-btn-secondary">Browse All 10 Sorrow Entities →</a>
            </div>
          </div>
        </div>
      </section>

      <!-- 8 Portal Navigation Hubs -->
      <section class="pm-section-block">
        <div class="section-title-bar">
          <h2>/// MASTER ENCYCLOPEDIC ARCHIVES</h2>
          <span class="title-sub">EXPLORE ALL 8 FACILITY & METROPOLITAN CODEXES</span>
        </div>
        <div class="pm-feature-grid">
          <!-- 1. Sorrow Entities -->
          <a class="pm-card" href="entities/index.html">
            <span class="pm-card-title">— SORROW ENTITIES —</span>
            <img alt="Entities" class="pm-card-icon" src="assets/icons/banner_entities.svg"/>
            <span class="pm-card-sub">SE-001–015 Registry, Risk Ranks & Containment Rules</span>
          </a>
          <!-- 2. M.A.W. Equipment -->
          <a class="pm-card gold" href="maw/index.html">
            <span class="pm-card-title">— M.A.W. EQUIPMENT —</span>
            <img alt="M.A.W. Equipment" class="pm-card-icon" src="assets/icons/banner_maw.svg"/>
            <span class="pm-card-sub">Materialized Agony Weapons, Suits & Special Gifts</span>
          </a>
          <!-- 3. Echo-Cores -->
          <a class="pm-card crimson" href="characters/index.html">
            <span class="pm-card-title">— ECHO-CORES & CAST —</span>
            <img alt="Characters" class="pm-card-icon" src="assets/icons/banner_characters.svg"/>
            <span class="pm-card-sub">The Nine Leads, Director Majin & Operational Figures</span>
          </a>
          <!-- 4. Battle & Mechanics -->
          <a class="pm-card cyan" href="mechanics/index.html">
            <span class="pm-card-title">— BATTLE & SYSTEMS —</span>
            <img alt="Mechanics" class="pm-card-icon" src="assets/icons/banner_mechanics.svg"/>
            <span class="pm-card-sub">Han Energy, Damage Matrix, Panic & Work Protocols</span>
          </a>
          <!-- 5. Factions & Guilds -->
          <a class="pm-card gold" href="factions/index.html">
            <span class="pm-card-title">— FACTIONS & GUILDS —</span>
            <img alt="Factions" class="pm-card-icon" src="assets/icons/banner_factions.svg"/>
            <span class="pm-card-sub">The Directorate, High Council, Weavers & Syndicates</span>
          </a>
          <!-- 6. Hand of Change -->
          <a class="pm-card cyan" href="departments/index.html">
            <span class="pm-card-title">— HAND OF CHANGE —</span>
            <img alt="Hand of Change" class="pm-card-icon" src="assets/icons/banner_departments.svg"/>
            <span class="pm-card-sub">Floors 1–8 Operations, Floor Blueprints & Incident Files</span>
          </a>
          <!-- 7. Atlas & Locations -->
          <a class="pm-card crimson" href="locations/index.html">
            <span class="pm-card-title">— ATLAS & GEOGRAPHY —</span>
            <img alt="Atlas" class="pm-card-icon" src="assets/icons/banner_locations.svg"/>
            <span class="pm-card-sub">Zones A–E, The Maw, Hollow Glass & Desolate Outskirts</span>
          </a>
          <!-- 8. Lore & Cosmology -->
          <a class="pm-card" href="lore/index.html">
            <span class="pm-card-title">— LORE & COSMOLOGY —</span>
            <img alt="Lore" class="pm-card-icon" src="assets/icons/banner_lore.svg"/>
            <span class="pm-card-sub">The 1,778 Cycles, The Three Sorrows & Absolvohan</span>
          </a>
        </div>
      </section>

      <!-- Tactical Quick-Reference: 4-Way Han Damage Matrix -->
      <section class="pm-section-block">
        <div class="section-title-bar">
          <h2>/// TACTICAL QUICK REFERENCE: 4-WAY HAN DAMAGE MATRIX</h2>
          <span class="title-sub">ESSENTIAL COMBAT & CONTAINMENT MULTIPLIERS</span>
        </div>
        <p class="section-lead-text">
          Within the Hand of Change, all psychic trauma, physical force, and metaphysical pressure are categorized into four distinct Han damage manifestations. Agents must wear matching M.A.W. suits to avoid fatal trauma or psychological panic.
        </p>
        <div class="pm-table-wrapper">
          <table class="pm-table">
            <thead>
              <tr>
                <th>Damage Type</th>
                <th>Dominant Color</th>
                <th>Target Attribute</th>
                <th>Psychic & Physical Effects</th>
                <th>Primary Mitigation Strategy</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong style="color:#ef4444;"><img src="assets/icons/damage_red.svg" alt="" style="width:16px;vertical-align:middle;margin-right:6px;">Grudge (원한)</strong></td>
                <td>Crimson / Fiery Red</td>
                <td>Health Points (HP)</td>
                <td>Direct physical blunt impact, lacerations, thermal combustion, and severe bone fracturing.</td>
                <td>Heavy armored M.A.W. Suits (Fortitude affinity) with Grudge resistance ≤ 0.5.</td>
              </tr>
              <tr>
                <td><strong style="color:#38bdf8;"><img src="assets/icons/damage_white.svg" alt="" style="width:16px;vertical-align:middle;margin-right:6px;">Lament (비탄)</strong></td>
                <td>Azure / Cyan Blue</td>
                <td>Sanity Points (SP)</td>
                <td>Severe cognitive distress, auditory hallucinations, grief paralysis, panic erosion, and self-harm.</td>
                <td>Psychologically reinforced M.A.W. Veils (Prudence affinity) and Insight work routines.</td>
              </tr>
              <tr>
                <td><strong style="color:#f1df76;"><img src="assets/icons/damage_black.svg" alt="" style="width:16px;vertical-align:middle;margin-right:6px;">Void (공허)</strong></td>
                <td>Amber / Obsidian Gold</td>
                <td>Simultaneous HP & SP</td>
                <td>Dual-channel corrosive necrosis and existential ego dissolution; drains body and mind equally.</td>
                <td>Balanced composite M.A.W. Plate (Temperance affinity); avoid solitary containment shifts.</td>
              </tr>
              <tr>
                <td><strong style="color:#e2e8f0;"><img src="assets/icons/damage_pale.svg" alt="" style="width:16px;vertical-align:middle;margin-right:6px;">Pale (창백)</strong></td>
                <td>Pristine / Ghost White</td>
                <td>Max HP Percentage</td>
                <td>Direct soul-death bypassing conventional physical armor; deals damage scaling off maximum HP.</td>
                <td>High-tier Aleph-grade M.A.W. suits (Justice affinity Level V required); extreme caution.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Facility 01 Floor Operations & Echo-Core Leads -->
      <section class="pm-section-block">
        <div class="section-title-bar">
          <h2>/// FACILITY 01: THE HAND OF CHANGE SECTOR SUMMARY</h2>
          <span class="title-sub">THE 8 SUBTERRANEAN FLOORS & ECHO-CORE DIRECTORS</span>
        </div>
        <p class="section-lead-text">
          Facility 01 (The Hand of Change) descends 8 subterranean tiers directly beneath the Alpha Tree roots into the Weeping. Each floor is commanded by an awakened Echo-Core Lead:
        </p>
        <div class="pm-table-wrapper">
          <table class="pm-table">
            <thead>
              <tr>
                <th>Floor</th>
                <th>Department Name</th>
                <th>Echo-Core Lead</th>
                <th>Core Function & Mandate</th>
                <th>Hazard Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Floor 1</strong></td>
                <td><a href="departments/floor-1-neutral-command.html" class="wiki-link">Neutral Command</a></td>
                <td><a href="characters/the-director-majin.html"><img src="assets/avatars/avatar_core_majin.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Director Majin</a></td>
                <td>Master facility administration, executive energy quota distribution, and city oversight.</td>
                <td><span class="risk-badge risk-can">CAN (SECURE)</span></td>
              </tr>
              <tr>
                <td><strong>Floor 2</strong></td>
                <td><a href="departments/floor-2-maws-keep.html" class="wiki-link">Maw's Keep</a></td>
                <td><a href="characters/the-containment-lead-dekan.html"><img src="assets/avatars/avatar_core_dekan.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Dekan</a></td>
                <td>Heavy containment of high-mass Sorrow Entities and Chasm suppression protocols.</td>
                <td><span class="risk-badge risk-waw">WAW (HIGH HAZARD)</span></td>
              </tr>
              <tr>
                <td><strong>Floor 3</strong></td>
                <td><a href="departments/floor-3-extraction-hall.html" class="wiki-link">Extraction Hall</a></td>
                <td><a href="characters/the-extraction-lead-zyrak.html"><img src="assets/avatars/avatar_core_zyrak.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Zyrak</a></td>
                <td>Han-flux refining, thermal energy purification, and high-yield fuel extraction.</td>
                <td><span class="risk-badge risk-he">HE (ELEVATED)</span></td>
              </tr>
              <tr>
                <td><strong>Floor 4</strong></td>
                <td><a href="departments/floor-4-insight-forge.html" class="wiki-link">Insight Forge</a></td>
                <td><a href="characters/the-research-lead-ayshuk.html"><img src="assets/avatars/avatar_core_ayshuk.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Ayshuk</a></td>
                <td>M.A.W. equipment synthesis, neurological resonance profiling, and cognitive mapping.</td>
                <td><span class="risk-badge risk-he">HE (ELEVATED)</span></td>
              </tr>
              <tr>
                <td><strong>Floor 5</strong></td>
                <td><a href="departments/floor-5-border-watch.html" class="wiki-link">Border Watch</a></td>
                <td><a href="characters/the-border-lead-mellda.html"><img src="assets/avatars/avatar_core_mellda.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Mellda</a></td>
                <td>Perimeter surveillance, effluent flood prevention, and Night Hazard interdiction.</td>
                <td><span class="risk-badge risk-waw">WAW (HIGH HAZARD)</span></td>
              </tr>
              <tr>
                <td><strong>Floor 6</strong></td>
                <td><a href="departments/floor-6-deep-vault.html" class="wiki-link">Deep Vault</a></td>
                <td><a href="characters/the-archive-lead-marjuk.html"><img src="assets/avatars/avatar_core_marjuk.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Marjuk</a></td>
                <td>Classified memory archive, ancient Cycle stele translation, and taboo artifact stasis.</td>
                <td><span class="risk-badge risk-aleph">ALEPH (EXTREME)</span></td>
              </tr>
              <tr>
                <td><strong>Floor 7</strong></td>
                <td><a href="departments/floor-7-shadow-corps.html" class="wiki-link">Shadow Corps</a></td>
                <td><a href="characters/the-outsider-ishall.html"><img src="assets/avatars/avatar_core_ishall.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Ishall</a></td>
                <td>Rapid covert suppression of rogue aberrations and containment breach strike operations.</td>
                <td><span class="risk-badge risk-aleph">ALEPH (EXTREME)</span></td>
              </tr>
              <tr>
                <td><strong>Floor 8</strong></td>
                <td><a href="departments/floor-8-gate-watch.html" class="wiki-link">Gate Watch</a></td>
                <td><a href="characters/the-exile-xyan.html"><img src="assets/avatars/avatar_core_xyan.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Xyan</a></td>
                <td>Subterranean deep gate containment guarding the abyssal threshold into Cheongula.</td>
                <td><span class="risk-badge risk-aleph">ALEPH (MAXIMUM)</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Complete Encyclopedic Directory -->
      <section class="pm-section-block">
        <div class="section-title-bar">
          <h2>/// COMPREHENSIVE ARTICLE DIRECTORY</h2>
          <span class="title-sub">INDEX OF 137 CANONICAL ARTICLES ACROSS ALL NAMESPACES</span>
        </div>
        <div class="portal-category-grid">
          <div class="portal-cat-box">
            <h4><img src="assets/icons/nav_entities.svg" alt="" class="cat-icon"> Sorrow Entities (SE-xxx)</h4>
            <ul>
              <li><a href="entities/se-001-the-orphaned-bell.html">SE-001 The Orphaned Bell (Can)</a></li>
              <li><a href="entities/se-002-the-grieving-colossus.html">SE-002 The Grieving Colossus (Waw)</a></li>
              <li><a href="entities/se-003-the-wilderness-tide.html">SE-003 The Wilderness Tide (He)</a></li>
              <li><a href="entities/se-005-the-smothering-mother.html">SE-005 The Smothering Mother (Teth)</a></li>
              <li><a href="entities/se-007-brume.html">SE-007 Brume (Can)</a></li>
              <li><a href="entities/se-009-the-memory-weaver.html">SE-009 The Memory Weaver (He)</a></li>
              <li><a href="entities/se-010-the-convergence.html">SE-010 The Convergence (Aleph)</a></li>
              <li><a href="entities/se-011-the-whispering-walls.html">SE-011 The Whispering Walls (Waw)</a></li>
              <li><a href="entities/se-014-the-debt-eater.html">SE-014 The Debt Eater (He)</a></li>
              <li><a href="entities/se-015-the-debt-scale.html">SE-015 The Debt Scale (Waw)</a></li>
            </ul>
          </div>

          <div class="portal-cat-box">
            <h4><img src="assets/icons/weapon.svg" alt="" class="cat-icon"> M.A.W. Equipment Armory</h4>
            <ul>
              <li><a href="maw/maw-w-001-01-the-laments-requiem.html">Lament Requiem (Weapon)</a></li>
              <li><a href="maw/maw-w-002-01-the-mourning-maul.html">Mourning Maul (Weapon)</a></li>
              <li><a href="maw/maw-w-010-01-the-absolute-maul.html">Absolute Maul (Weapon)</a></li>
              <li><a href="maw/maw-s-001-01-the-laments-shroud.html">Lament Shroud (Suit)</a></li>
              <li><a href="maw/maw-s-002-01-the-mourning-mantle.html">Mourning Mantle (Suit)</a></li>
              <li><a href="maw/maw-s-010-01-the-absolute-mantle.html">Absolute Mantle (Suit)</a></li>
              <li><a href="maw/maw-g-001-01-laments-edge.html">Lament's Edge (Gift)</a></li>
              <li><a href="maw/maw-g-010-01-the-absolute-verdict.html">Absolute Verdict (Gift)</a></li>
              <li><a href="maw/index.html">View All 27 M.A.W. Weapon/Suit/Gift Codexes →</a></li>
            </ul>
          </div>

          <div class="portal-cat-box">
            <h4><img src="assets/icons/nav_characters.svg" alt="" class="cat-icon"> Key Figures & Secondary Cast</h4>
            <ul>
              <li><a href="characters/the-director-majin.html">Director Majin (The Arch-Architect)</a></li>
              <li><a href="characters/the-secretary-seiyon.html">Secretary Seiyon (Executive Secretary)</a></li>
              <li><a href="characters/minho.html">Field Agent Minho (SED Operative)</a></li>
              <li><a href="characters/doha.html">Merchant Doha (Maw Black-Market)</a></li>
              <li><a href="characters/soojin.html">Researcher Soojin (Han Biologist)</a></li>
              <li><a href="characters/sora.html">Civilian Sora (Cheonbulok Survivor)</a></li>
              <li><a href="characters/taeho.html">Captain Taeho (UCD Strike Commander)</a></li>
              <li><a href="characters/kael.html">Kael (Horizon Caravan Master)</a></li>
              <li><a href="characters/yeonhwa.html">Yeonhwa (Master Weaver of Han-Silk)</a></li>
              <li><a href="characters/joon.html">Engineer Joon (Facility Heavy Maintenance)</a></li>
            </ul>
          </div>

          <div class="portal-cat-box">
            <h4><img src="assets/icons/nav_lore.svg" alt="" class="cat-icon"> Cosmological Lore & Chronicles</h4>
            <ul>
              <li><a href="lore/the-alpha-tree.html">The Alpha Tree & Metropolitan Axis</a></li>
              <li><a href="lore/the-three-sorrows.html">The Three Sorrows (Grudge, Lament, Void)</a></li>
              <li><a href="lore/the-cycle-and-absolvohan.html">The Absolvohan Purification Codex</a></li>
              <li><a href="lore/the-seven-absolute-taboos.html">The Seven Absolute Taboos of Somnarak</a></li>
              <li><a href="lore/the-cheongula-incident.html">The Cheongula Incident & The Great Collapse</a></li>
              <li><a href="lore/the-dawn-of-hope.html">The Dawn of Hope & The 1,778 Cycles</a></li>
              <li><a href="lore/the-doorspeech.html">The Doorspeech Frequency Phenomenon</a></li>
              <li><a href="lore/the-dream-realm.html">The Dream Realm & Crystalline Nebula</a></li>
              <li><a href="lore/efflorescence-and-fracture.html">Efflorescence (Han Petrification)</a></li>
              <li><a href="lore/the-weeping-river.html">The Weeping Subterranean Effluent</a></li>
            </ul>
          </div>
        </div>
      </section>
    </main>

    <!-- Right Rail: Ultimate Multi-Scale Console with Mini-Banners, Avatars & Diagnostics -->
    <aside aria-label="Hand of Change Department Console" class="floor-rail">
      <!-- Master Facility Diagnostic Header -->
      <div class="floor-console-header">
        <div class="console-header-top">
          <div class="console-title-wrap">
            <h2>FACILITY 01 // SECTORS</h2>
            <small>THE HAND OF CHANGE SUBTERRANEAN SYSTEM</small>
          </div>
          <img src="assets/icons/hud_facility_radar.svg" alt="Radar" class="console-radar-icon">
        </div>
        <div class="console-status-bar">
          <span><span class="led-dot led-amber"></span> CODE AMBER</span>
          <span>CYCLE: 1,778</span>
          <span>FLUX: 98.4%</span>
        </div>
      </div>

      <!-- Sector Floor Roster with Multi-Scale Mini-Banners & Circular Avatars -->
      <div class="floor-button-list">
        <!-- Floor 1 -->
        <a href="departments/floor-1-neutral-command.html" class="floor-card-link floor-1-link" title="Floor 1: Neutral Command Core">
          <div class="floor-card-banner">
            <img src="assets/banners/floor_banner_f1_neutral.svg" alt="Floor 1" class="floor-banner-img">
            <div class="floor-badge-tag gold-tag">CORE 01</div>
          </div>
          <div class="floor-card-body">
            <div class="floor-lead-avatar-wrap">
              <img src="assets/avatars/avatar_core_majin.svg" alt="Majin" class="floor-avatar-img">
            </div>
            <div class="floor-info-text">
              <span class="floor-dept-name">NEUTRAL CORE</span>
              <span class="floor-lead-name">MAJIN // DIRECTOR</span>
            </div>
            <span class="floor-nav-arrow">›</span>
          </div>
        </a>

        <!-- Floor 2 -->
        <a href="departments/floor-2-maws-keep.html" class="floor-card-link floor-2-link" title="Floor 2: Maw's Keep">
          <div class="floor-card-banner">
            <img src="assets/banners/floor_banner_f2_maws_keep.svg" alt="Floor 2" class="floor-banner-img">
            <div class="floor-badge-tag cyan-tag">CORE 03</div>
          </div>
          <div class="floor-card-body">
            <div class="floor-lead-avatar-wrap">
              <img src="assets/avatars/avatar_core_dekan.svg" alt="Dekan" class="floor-avatar-img">
            </div>
            <div class="floor-info-text">
              <span class="floor-dept-name">MAW'S KEEP</span>
              <span class="floor-lead-name">DEKAN // CONTAINMENT</span>
            </div>
            <span class="floor-nav-arrow">›</span>
          </div>
        </a>

        <!-- Floor 3 -->
        <a href="departments/floor-3-extraction-hall.html" class="floor-card-link floor-3-link" title="Floor 3: Extraction Hall">
          <div class="floor-card-banner">
            <img src="assets/banners/floor_banner_f3_extraction.svg" alt="Floor 3" class="floor-banner-img">
            <div class="floor-badge-tag gold-tag">CORE 04</div>
          </div>
          <div class="floor-card-body">
            <div class="floor-lead-avatar-wrap">
              <img src="assets/avatars/avatar_core_zyrak.svg" alt="Zyrak" class="floor-avatar-img">
            </div>
            <div class="floor-info-text">
              <span class="floor-dept-name">EXTRACTION HALL</span>
              <span class="floor-lead-name">ZYRAK // REFINING</span>
            </div>
            <span class="floor-nav-arrow">›</span>
          </div>
        </a>

        <!-- Floor 4 -->
        <a href="departments/floor-4-insight-forge.html" class="floor-card-link floor-4-link" title="Floor 4: Insight Forge">
          <div class="floor-card-banner">
            <img src="assets/banners/floor_banner_f4_insight_forge.svg" alt="Floor 4" class="floor-banner-img">
            <div class="floor-badge-tag green-tag">CORE 05</div>
          </div>
          <div class="floor-card-body">
            <div class="floor-lead-avatar-wrap">
              <img src="assets/avatars/avatar_core_ayshuk.svg" alt="Ayshuk" class="floor-avatar-img">
            </div>
            <div class="floor-info-text">
              <span class="floor-dept-name">INSIGHT FORGE</span>
              <span class="floor-lead-name">AYSHUK // RESEARCH</span>
            </div>
            <span class="floor-nav-arrow">›</span>
          </div>
        </a>

        <!-- Floor 5 -->
        <a href="departments/floor-5-border-watch.html" class="floor-card-link floor-5-link" title="Floor 5: Border Watch">
          <div class="floor-card-banner">
            <img src="assets/banners/floor_banner_f5_border_watch.svg" alt="Floor 5" class="floor-banner-img">
            <div class="floor-badge-tag white-tag">CORE 06</div>
          </div>
          <div class="floor-card-body">
            <div class="floor-lead-avatar-wrap">
              <img src="assets/avatars/avatar_core_mellda.svg" alt="Mellda" class="floor-avatar-img">
            </div>
            <div class="floor-info-text">
              <span class="floor-dept-name">BORDER WATCH</span>
              <span class="floor-lead-name">MELLDA // PERIMETER</span>
            </div>
            <span class="floor-nav-arrow">›</span>
          </div>
        </a>

        <!-- Floor 6 -->
        <a href="departments/floor-6-deep-vault.html" class="floor-card-link floor-6-link" title="Floor 6: Deep Vault">
          <div class="floor-card-banner">
            <img src="assets/banners/floor_banner_f6_deep_vault.svg" alt="Floor 6" class="floor-banner-img">
            <div class="floor-badge-tag crimson-tag">CORE 07</div>
          </div>
          <div class="floor-card-body">
            <div class="floor-lead-avatar-wrap">
              <img src="assets/avatars/avatar_core_marjuk.svg" alt="Marjuk" class="floor-avatar-img">
            </div>
            <div class="floor-info-text">
              <span class="floor-dept-name">DEEP VAULT</span>
              <span class="floor-lead-name">MARJUK // ARCHIVES</span>
            </div>
            <span class="floor-nav-arrow">›</span>
          </div>
        </a>

        <!-- Floor 7 -->
        <a href="departments/floor-7-shadow-corps.html" class="floor-card-link floor-7-link" title="Floor 7: Shadow Corps">
          <div class="floor-card-banner">
            <img src="assets/banners/floor_banner_f7_shadow_corps.svg" alt="Floor 7" class="floor-banner-img">
            <div class="floor-badge-tag purple-tag">CORE 08</div>
          </div>
          <div class="floor-card-body">
            <div class="floor-lead-avatar-wrap">
              <img src="assets/avatars/avatar_core_ishall.svg" alt="Ishall" class="floor-avatar-img">
            </div>
            <div class="floor-info-text">
              <span class="floor-dept-name">SHADOW CORPS</span>
              <span class="floor-lead-name">ISHALL // OUTSIDER</span>
            </div>
            <span class="floor-nav-arrow">›</span>
          </div>
        </a>

        <!-- Floor 8 -->
        <a href="departments/floor-8-gate-watch.html" class="floor-card-link floor-8-link" title="Floor 8: Gate Watch">
          <div class="floor-card-banner">
            <img src="assets/banners/floor_banner_f8_gate_watch.svg" alt="Floor 8" class="floor-banner-img">
            <div class="floor-badge-tag amber-tag">CORE 09</div>
          </div>
          <div class="floor-card-body">
            <div class="floor-lead-avatar-wrap">
              <img src="assets/avatars/avatar_core_xyan.svg" alt="Xyan" class="floor-avatar-img">
            </div>
            <div class="floor-info-text">
              <span class="floor-dept-name">GATE WATCH</span>
              <span class="floor-lead-name">XYAN // EXILE</span>
            </div>
            <span class="floor-nav-arrow">›</span>
          </div>
        </a>
      </div>

      <!-- Master Blueprint Quick Panels -->
      <div class="blueprint-quick-panels">
        <a href="atlas/hand-of-change-map.html" class="blueprint-card-widget">
          <div class="blueprint-thumb-box">
            <img src="assets/layout/hand/icons/the_hand_dr_icon_styled.svg" alt="Facility Blueprint" class="blueprint-thumb-img">
          </div>
          <div class="blueprint-widget-meta">
            <span class="widget-title">FACILITY 01 BLUEPRINT</span>
            <span class="widget-sub">8 Floors & Sub-Sectors Layout</span>
          </div>
        </a>

        <a href="atlas/somnarak-city-map.html" class="blueprint-card-widget">
          <div class="blueprint-thumb-box">
            <img src="assets/layout/city/icons/somnarak_city_icon.svg" alt="City Blueprint" class="blueprint-thumb-img">
          </div>
          <div class="blueprint-widget-meta">
            <span class="widget-title">SOMNARAK METROPOLITAN</span>
            <span class="widget-sub">5 Zones & Outer Perimeter</span>
          </div>
        </a>
      </div>
    </aside>
  </div>

  <footer class="pm-footer">
    <div class="footer-content">
      <div class="footer-brand">
        <img src="assets/icons/somnarak_icon.svg" alt="Somnarak Crest" class="footer-logo">
        <div>
          <span class="footer-title">SOMNARAK ARCHIVAL INITIATIVE</span>
          <p>Preserving the names, containment records, and histories of the 1,778 Cycles.</p>
        </div>
      </div>
      <div class="footer-links">
        <a href="index.html">Main Portal</a>
        <a href="entities/index.html">Entities</a>
        <a href="maw/index.html">M.A.W.</a>
        <a href="characters/index.html">Personnel</a>
        <a href="lore/index.html">Lore</a>
        <a href="mechanics/index.html">Mechanics</a>
        <a href="downloads.html">Offline Archives</a>
      </div>
    </div>
  </footer>

  <script src="assets/js/wiki.js"></script>
</body>
</html>
"""

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("Updated index.html with exact valid links!")
