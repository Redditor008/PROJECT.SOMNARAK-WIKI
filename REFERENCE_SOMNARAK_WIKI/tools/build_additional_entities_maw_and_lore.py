import os

def wrap_article(title, breadcrumb_category, breadcrumb_link, content, rel_depth='..'):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Somnarak Official Wiki</title>
  <link rel="stylesheet" href="{rel_depth}/assets/css/wiki.css">
  <script defer src="{rel_depth}/assets/js/wiki.js"></script>
</head>
<body class="wiki-body">
<header class="utility">
  <div class="utility-left">
    <button aria-label="Open navigation" class="nav-open" type="button">☰</button>
    <a class="utility-brand" href="{rel_depth}/index.html">SOMNARAK.WIKI</a>
    <span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
  </div>
  <nav aria-label="Main navigation">
    <a href="{rel_depth}/index.html">Main page</a>
    <a href="{rel_depth}/characters/index.html">Characters</a>
    <a href="{rel_depth}/lore/index.html">Lore</a>
    <a href="{rel_depth}/locations/index.html">Locations</a>
    <a href="{rel_depth}/factions/index.html">Factions</a>
    <a href="{rel_depth}/departments/index.html">Departments</a>
    <a href="{rel_depth}/entities/index.html">Sorrow Entities</a>
    <a href="{rel_depth}/maw/index.html">M.A.W.</a>
    <a href="{rel_depth}/mechanics/index.html">Mechanics</a>
  </nav>
  <div class="search">
    <input aria-label="Search" data-index="{rel_depth}/data/search.json" id="search" placeholder="Search archive..." autocomplete="off"/>
    <div id="results"></div>
  </div>
</header>

  <div class="wiki-shell">
    <aside aria-label="Main navigation" class="left-rail">
      <div class="branding">
        <a class="brand-link" href="{rel_depth}/index.html">
          <img src="{rel_depth}/assets/layout/hand/icons/icon_reverie_directorate_badge.svg" alt="Reverie Directorate Crest" class="brand-logo" width="110" height="110">
          <span class="brand-title">SOMNARAK</span>
          <span class="brand-subtitle">REVERIE DIRECTORATE ARCHIVE</span>
        </a>
      </div>
      
      <div class="rail-group">
        <div class="rail-header">DATABASE HUBS</div>
        <ul class="rail-list">
          <li><a href="{rel_depth}/index.html">Main Terminal</a></li>
          <li><a href="{rel_depth}/characters/index.html">Characters &amp; Echo-Cores</a></li>
          <li><a href="{rel_depth}/lore/index.html">Lore &amp; Cosmology</a></li>
          <li><a href="{rel_depth}/locations/index.html">Atlas &amp; Locations</a></li>
          <li><a href="{rel_depth}/factions/index.html">Factions &amp; Guilds</a></li>
          <li><a href="{rel_depth}/departments/index.html">Facility Departments</a></li>
          <li><a href="{rel_depth}/entities/index.html">Sorrow Entities</a></li>
          <li><a href="{rel_depth}/maw/index.html">M.A.W. Armaments</a></li>
          <li><a href="{rel_depth}/mechanics/index.html">Systems &amp; Mechanics</a></li>
        </ul>
      </div>

      <div class="rail-group">
        <div class="rail-header">THE NINE ECHO-CORES</div>
        <ul class="rail-list">
          <li><a href="{rel_depth}/characters/the-director-majin.html">Director Majin</a></li>
          <li><a href="{rel_depth}/characters/the-secretary-seiyon.html">Secretary Seiyon</a></li>
          <li><a href="{rel_depth}/characters/the-containment-lead-dekan.html">Containment: Dekan</a></li>
          <li><a href="{rel_depth}/characters/the-extraction-lead-zyrak.html">Extraction: Zyrak</a></li>
          <li><a href="{rel_depth}/characters/the-research-lead-ayshuk.html">Research: Ayshuk</a></li>
          <li><a href="{rel_depth}/characters/the-border-lead-mellda.html">Border: Mellda</a></li>
          <li><a href="{rel_depth}/characters/the-archive-lead-marjuk.html">Archive: Marjuk</a></li>
          <li><a href="{rel_depth}/characters/the-outsider-ishall.html">Outsider: Ishall</a></li>
          <li><a href="{rel_depth}/characters/the-exile-xyan.html">Exile: Xyan</a></li>
        </ul>
      </div>
    </aside>

    <main id="content" class="wiki-content">
      <div class="tactical-hud-bar">
        <div class="hud-item"><span class="led-dot led-green"></span> ARCHIVE ONLINE</div>
        <div class="hud-item"><span class="hud-label">CLEARANCE:</span> LEVEL 5 RESTRICTED</div>
        <div class="hud-item"><span class="hud-label">RECORD:</span> CANONICAL</div>
        <div class="hud-item"><span class="hud-label">STABILITY:</span> 99.4% NOMINAL</div>
      </div>

      <nav class="breadcrumb-trail" aria-label="Breadcrumb">
        <a href="{rel_depth}/index.html">SOMNARAK ARCHIVE</a> &gt; 
        <a href="{breadcrumb_link}">{breadcrumb_category}</a> &gt; 
        <span>{title}</span>
      </nav>

      <div class="page-action-row" style="display:flex; justify-content:space-between; align-items:center; margin:1rem 0; padding-bottom:0.8rem; border-bottom:1px solid #1e293b;">
        <h1 style="margin:0; font-family:Impact, 'Arial Narrow Bold', sans-serif; font-size:1.8rem; color:#f1df76; letter-spacing:0.08em;">{title.upper()}</h1>
        <div style="display:flex; gap:8px;">
          <button type="button" class="action-btn" data-action="history">History</button>
          <button type="button" class="action-btn" data-action="view-source">View Source</button>
        </div>
      </div>

      {content}

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

# Define articles to generate
articles = {}

# 1. SE-004
articles['entities/se-004-the-rust-bleeding-sentry.html'] = {
    'title': 'SE-004 — The Rust-Bleeding Sentry',
    'cat': 'SORROW ENTITIES',
    'cat_link': 'index.html',
    'content': """
<div class="infobox-wrapper" style="float:right; width:340px; margin:0 0 1.5rem 1.5rem;">
  <div class="infobox" style="border:2px solid #f97316; background:#0e0805; padding:14px; border-radius:6px;">
    <div style="text-align:center; padding-bottom:8px; border-bottom:1.5px solid #f97316;">
      <h3 style="margin:0; font-family:'JetBrains Mono', monospace; color:#f97316; font-size:1.15rem;">SE-004</h3>
      <b style="color:#ffffff; font-size:0.95rem;">THE RUST-BLEEDING SENTRY</b>
      <div style="font-size:0.75rem; color:#94a3b8; font-family:'Courier New', monospace;">녹혈의 보초 (Nokhyeol-ui Bocho)</div>
    </div>
    <div style="text-align:center; margin:12px 0;">
      <img src="../assets/art/entities/se-004-profile.svg" alt="SE-004 Profile" style="width:200px; height:200px; border:1.5px solid #f97316; border-radius:6px; background:#040201; padding:4px;">
    </div>
    <table class="pm-table condensed" style="width:100%;">
      <tr><th>SECC Risk</th><td><span class="risk-badge risk-MORPHEAN">γ (MORPHEAN)</span></td></tr>
      <tr><th>Damage Type</th><td><span class="damage-badge dmg-red">GRUDGE (Physical)</span></td></tr>
      <tr><th>Damage Value</th><td>14 – 20 Grudge</td></tr>
      <tr><th>Coherence Base</th><td>04 Threshold Points</td></tr>
      <tr><th>Han Yield</th><td>22 PE / Cycle</td></tr>
      <tr><th>Location</th><td>Floor 5 (Border Watch)</td></tr>
    </table>
  </div>
</div>

<div class="toc" id="toc">
  <div class="toc-title">Contents</div>
  <ol>
    <li><a href="#overview">Overview &amp; Manifestation</a></li>
    <li><a href="#containment-procedures">Containment &amp; Work Protocols</a></li>
    <li><a href="#breach-behavior">Breach Dynamics &amp; Suppression</a></li>
    <li><a href="#maw-extraction">Extracted M.A.W. Armory</a></li>
  </ol>
</div>

<h2 id="overview">/// 1. OVERVIEW &amp; MANIFESTATION</h2>
<p>
  <strong>SE-004 (The Rust-Bleeding Sentry)</strong> is an ancient clockwork sentinel embodying the unavenged deaths of perimeter border guards during the Great Breach of Year 3,892. Encased in oxidized iron plating, its ocular visor continuously weeps corrosive rust sludge that dissolves protective alloy barriers upon contact.
</p>

<h2 id="containment-procedures">/// 2. CONTAINMENT &amp; WORK PROTOCOLS</h2>
<p>
  Operatives assigned to SE-004 must wear high-density kinetic M.A.W. suits to withstand high-frequency halberd clashing. Subjugation work is the most stabilizing protocol, relieving the entity's phantom combat reflexes.
</p>
<div class="pm-table-wrapper">
  <table class="pm-table">
    <thead>
      <tr><th>Work Protocol</th><th>Korean Name</th><th>Success Rate</th><th>Coherence Response</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Communion</strong></td><td>Docerehan (교감)</td><td>35%</td><td>Neutral (+0)</td></tr>
      <tr><td><strong>Dissection</strong></td><td>Discernerehan (분해)</td><td>45%</td><td>Neutral (+0)</td></tr>
      <tr><td><strong>Siphon</strong></td><td>Hausuhan (추출)</td><td>50%</td><td>Coherence +1</td></tr>
      <tr><td><strong>Subjugation</strong></td><td>Ferrehan (제압)</td><td><strong style="color:#71efaf;">65% (Optimal)</strong></td><td>Coherence +2</td></tr>
    </tbody>
  </table>
</div>

<h2 id="breach-behavior">/// 3. BREACH DYNAMICS &amp; SUPPRESSION</h2>
<p>
  Upon Coherence collapse, SE-004 shatters containment bulkheads and patrols surrounding hallways with wide halberd cleaves, inflicting heavy <strong>Grudge damage</strong> and reducing operative defense ratings through rust corrosion.
</p>

<h2 id="maw-extraction">/// 4. EXTRACTED M.A.W. ARMORY</h2>
<div class="hub-grid-3">
  <div class="pm-entity-card" style="border:1.5px solid #ef5b55;">
    <h4 style="margin:0 0 6px; color:#ef5b55;">RUST HALBERD (WEAPON)</h4>
    <p style="font-size:0.8rem; color:#cbd5e1;">Heavy poleaxe inflicting 14–20 Grudge damage with 15% armor reduction on target hit.</p>
    <a href="../maw/maw-w-004-01-rust-halberd.html" class="jump-btn">VIEW WEAPON DATA →</a>
  </div>
  <div class="pm-entity-card" style="border:1.5px solid #f97316;">
    <h4 style="margin:0 0 6px; color:#f97316;">SENTRY'S IRON PLATE (SUIT)</h4>
    <p style="font-size:0.8rem; color:#cbd5e1;">Heavy plate armor providing 0.5 Grudge resistance and 0.7 Lament resistance.</p>
    <a href="../maw/maw-s-004-01-sentrys-iron-plate.html" class="jump-btn">VIEW SUIT DATA →</a>
  </div>
  <div class="pm-entity-card" style="border:1.5px solid #f1df76;">
    <h4 style="margin:0 0 6px; color:#f1df76;">CORROSION VISOR (GIFT)</h4>
    <p style="font-size:0.8rem; color:#cbd5e1;">Ocular augment granting +4 Max HP and +3 Grudge Defense.</p>
    <a href="../maw/maw-g-004-01-corrosion-visor.html" class="jump-btn">VIEW GIFT DATA →</a>
  </div>
</div>
"""
}

# 2. SE-006
articles['entities/se-006-the-siphon-leech.html'] = {
    'title': 'SE-006 — The Siphon Leech',
    'cat': 'SORROW ENTITIES',
    'cat_link': 'index.html',
    'content': """
<div class="infobox-wrapper" style="float:right; width:340px; margin:0 0 1.5rem 1.5rem;">
  <div class="infobox" style="border:2px solid #10b981; background:#041510; padding:14px; border-radius:6px;">
    <div style="text-align:center; padding-bottom:8px; border-bottom:1.5px solid #10b981;">
      <h3 style="margin:0; font-family:'JetBrains Mono', monospace; color:#10b981; font-size:1.15rem;">SE-006</h3>
      <b style="color:#ffffff; font-size:0.95rem;">THE SIPHON LEECH</b>
      <div style="font-size:0.75rem; color:#94a3b8; font-family:'Courier New', monospace;">흡관 거머리 (Heupgwan Geomeori)</div>
    </div>
    <div style="text-align:center; margin:12px 0;">
      <img src="../assets/art/entities/se-006-profile.svg" alt="SE-006 Profile" style="width:200px; height:200px; border:1.5px solid #10b981; border-radius:6px; background:#010a08; padding:4px;">
    </div>
    <table class="pm-table condensed" style="width:100%;">
      <tr><th>SECC Risk</th><td><span class="risk-badge risk-SOMNA">β (SOMNA)</span></td></tr>
      <tr><th>Damage Type</th><td><span class="damage-badge dmg-black">WEIGHT (Dual HP+SP)</span></td></tr>
      <tr><th>Damage Value</th><td>10 – 16 Weight</td></tr>
      <tr><th>Coherence Base</th><td>03 Threshold Points</td></tr>
      <tr><th>Han Yield</th><td>20 PE / Cycle</td></tr>
      <tr><th>Location</th><td>Floor 3 (Extraction Hall)</td></tr>
    </table>
  </div>
</div>

<div class="toc" id="toc">
  <div class="toc-title">Contents</div>
  <ol>
    <li><a href="#overview">Overview &amp; Manifestation</a></li>
    <li><a href="#containment-procedures">Containment &amp; Work Protocols</a></li>
    <li><a href="#maw-extraction">Extracted M.A.W. Armory</a></li>
  </ol>
</div>

<h2 id="overview">/// 1. OVERVIEW &amp; MANIFESTATION</h2>
<p>
  <strong>SE-006 (The Siphon Leech)</strong> is an iridescent subterranean parasite native to the raw effluent canals beneath Facility 01. Possessing a concentric razor-toothed siphon maw, it feeds directly on unrefined Han flux, simultaneously draining physical vitality and psychological cohesion (<strong>Weight Damage</strong>).
</p>

<h2 id="containment-procedures">/// 2. CONTAINMENT &amp; WORK PROTOCOLS</h2>
<p>
  Extraction work yields maximum stability as it aligns with the entity's metabolic desire to channel fluid Han streams.
</p>
<div class="pm-table-wrapper">
  <table class="pm-table">
    <thead>
      <tr><th>Work Protocol</th><th>Korean Name</th><th>Success Rate</th><th>Coherence Response</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Communion</strong></td><td>Docerehan (교감)</td><td>40%</td><td>Neutral (+0)</td></tr>
      <tr><td><strong>Dissection</strong></td><td>Discernerehan (분해)</td><td>50%</td><td>Neutral (+0)</td></tr>
      <tr><td><strong>Siphon</strong></td><td>Hausuhan (추출)</td><td><strong style="color:#71efaf;">70% (Optimal)</strong></td><td>Coherence +2</td></tr>
      <tr><td><strong>Subjugation</strong></td><td>Ferrehan (제압)</td><td>45%</td><td>Coherence -1</td></tr>
    </tbody>
  </table>
</div>

<h2 id="maw-extraction">/// 3. EXTRACTED M.A.W. ARMORY</h2>
<div class="hub-grid-3">
  <div class="pm-entity-card" style="border:1.5px solid #10b981;">
    <h4 style="margin:0 0 6px; color:#10b981;">SIPHON CANNULA (WEAPON)</h4>
    <p style="font-size:0.8rem; color:#cbd5e1;">Dual-drain lance dealing 10–16 Weight damage and siphoning 10% damage dealt as agent HP.</p>
    <a href="../maw/maw-w-006-01-siphon-cannula.html" class="jump-btn">VIEW WEAPON DATA →</a>
  </div>
  <div class="pm-entity-card" style="border:1.5px solid #38bdf8;">
    <h4 style="margin:0 0 6px; color:#38bdf8;">LEECH MEMBRANE SUIT (SUIT)</h4>
    <p style="font-size:0.8rem; color:#cbd5e1;">Flexible bio-membrane suit granting 0.6 Weight resistance and 0.8 Grudge resistance.</p>
    <a href="../maw/maw-s-006-01-leech-membrane-suit.html" class="jump-btn">VIEW SUIT DATA →</a>
  </div>
  <div class="pm-entity-card" style="border:1.5px solid #71efaf;">
    <h4 style="margin:0 0 6px; color:#71efaf;">EFFLUENT GLAND (GIFT)</h4>
    <p style="font-size:0.8rem; color:#cbd5e1;">Symbiotic gland adding +5 Max HP and +5 Max SP.</p>
    <a href="../maw/maw-g-006-01-effluent-gland.html" class="jump-btn">VIEW GIFT DATA →</a>
  </div>
</div>
"""
}

# 3. SE-008
articles['entities/se-008-the-iron-maiden-of-regret.html'] = {
    'title': 'SE-008 — The Iron Maiden of Regret',
    'cat': 'SORROW ENTITIES',
    'cat_link': 'index.html',
    'content': """
<div class="infobox-wrapper" style="float:right; width:340px; margin:0 0 1.5rem 1.5rem;">
  <div class="infobox" style="border:2px solid #ef4444; background:#140407; padding:14px; border-radius:6px;">
    <div style="text-align:center; padding-bottom:8px; border-bottom:1.5px solid #ef4444;">
      <h3 style="margin:0; font-family:'JetBrains Mono', monospace; color:#ef4444; font-size:1.15rem;">SE-008</h3>
      <b style="color:#ffffff; font-size:0.95rem;">THE IRON MAIDEN OF REGRET</b>
      <div style="font-size:0.75rem; color:#94a3b8; font-family:'Courier New', monospace;">후회의 철처녀 (Huhoe-ui Cheolcheonyeo)</div>
    </div>
    <div style="text-align:center; margin:12px 0;">
      <img src="../assets/art/entities/se-008-profile.svg" alt="SE-008 Profile" style="width:200px; height:200px; border:1.5px solid #ef4444; border-radius:6px; background:#050102; padding:4px;">
    </div>
    <table class="pm-table condensed" style="width:100%;">
      <tr><th>SECC Risk</th><td><span class="risk-badge risk-PHANTASM">δ (PHANTASM)</span></td></tr>
      <tr><th>Damage Type</th><td><span class="damage-badge dmg-red">GRUDGE / LAMENT</span></td></tr>
      <tr><th>Damage Value</th><td>20 – 26 Dual</td></tr>
      <tr><th>Coherence Base</th><td>03 Threshold Points</td></tr>
      <tr><th>Han Yield</th><td>32 PE / Cycle</td></tr>
      <tr><th>Location</th><td>Floor 6 (Deep Vault)</td></tr>
    </table>
  </div>
</div>

<div class="toc" id="toc">
  <div class="toc-title">Contents</div>
  <ol>
    <li><a href="#overview">Overview &amp; Manifestation</a></li>
    <li><a href="#containment-procedures">Containment &amp; Work Protocols</a></li>
    <li><a href="#maw-extraction">Extracted M.A.W. Armory</a></li>
  </ol>
</div>

<h2 id="overview">/// 1. OVERVIEW &amp; MANIFESTATION</h2>
<p>
  <strong>SE-008 (The Iron Maiden of Regret)</strong> is a monumental sarcophagus forged from weeping black iron and thorns. If an operative panics while inside the containment chamber, the maiden snaps shut, trapping the agent within internal thorn spines that extract concentrated agony Han flux.
</p>

<h2 id="containment-procedures">/// 2. CONTAINMENT &amp; WORK PROTOCOLS</h2>
<div class="pm-table-wrapper">
  <table class="pm-table">
    <thead>
      <tr><th>Work Protocol</th><th>Korean Name</th><th>Success Rate</th><th>Coherence Response</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Communion</strong></td><td>Docerehan (교감)</td><td>25%</td><td>Coherence -1</td></tr>
      <tr><td><strong>Dissection</strong></td><td>Discernerehan (분해)</td><td>50%</td><td>Neutral (+0)</td></tr>
      <tr><td><strong>Siphon</strong></td><td>Hausuhan (추출)</td><td>55%</td><td>Coherence +1</td></tr>
      <tr><td><strong>Subjugation</strong></td><td>Ferrehan (제압)</td><td><strong style="color:#71efaf;">65% (Optimal)</strong></td><td>Coherence +2</td></tr>
    </tbody>
  </table>
</div>

<h2 id="maw-extraction">/// 3. EXTRACTED M.A.W. ARMORY</h2>
<div class="hub-grid-3">
  <div class="pm-entity-card" style="border:1.5px solid #ef4444;">
    <h4 style="margin:0 0 6px; color:#ef4444;">THORN IMPALER (WEAPON)</h4>
    <p style="font-size:0.8rem; color:#cbd5e1;">Spiked iron war-pike inflicting 20–26 mixed Grudge and Lament damage.</p>
    <a href="../maw/maw-w-008-01-thorn-impaler.html" class="jump-btn">VIEW WEAPON DATA →</a>
  </div>
  <div class="pm-entity-card" style="border:1.5px solid #f1df76;">
    <h4 style="margin:0 0 6px; color:#f1df76;">SARCOPHAGUS SHROUD (SUIT)</h4>
    <p style="font-size:0.8rem; color:#cbd5e1;">Reinforced iron armor providing 0.4 Grudge Res and 0.4 Lament Res.</p>
    <a href="../maw/maw-s-008-01-sarcophagus-shroud.html" class="jump-btn">VIEW SUIT DATA →</a>
  </div>
  <div class="pm-entity-card" style="border:1.5px solid #c084fc;">
    <h4 style="margin:0 0 6px; color:#c084fc;">SPIKE CROWN (GIFT)</h4>
    <p style="font-size:0.8rem; color:#cbd5e1;">Thorn halo augment granting +8 Max SP and +5 Physical Attack Power.</p>
    <a href="../maw/maw-g-008-01-spike-crown.html" class="jump-btn">VIEW GIFT DATA →</a>
  </div>
</div>
"""
}

# 4. Ordeals Mechanics Page
articles['mechanics/the-four-ordeals.html'] = {
    'title': 'The Four Ordeals of Facility 01',
    'cat': 'SYSTEMS & MECHANICS',
    'cat_link': 'index.html',
    'content': """
<div class="toc" id="toc">
  <div class="toc-title">Contents</div>
  <ol>
    <li><a href="#overview">Overview of Facility Ordeals</a></li>
    <li><a href="#the-whisper">Tier I: The Whisper (Dawn Ordeal)</a></li>
    <li><a href="#the-surge">Tier II: The Surge (Noon Ordeal)</a></li>
    <li><a href="#the-breach">Tier III: The Breach (Dusk Ordeal)</a></li>
    <li><a href="#the-abyss">Tier IV: The Abyss (Midnight Ordeal)</a></li>
  </ol>
</div>

<h2 id="overview">/// 1. OVERVIEW OF FACILITY ORDEALS</h2>
<p>
  As daily Han extraction quotas are met throughout a shift, metaphysical pressure within the subterranean bedrock escalates. When Han saturation reaches critical thresholds, spontaneous resonance waves known as <strong>Ordeals (시련 — Siryeon)</strong> manifest throughout Facility 01 corridors.
</p>

<h2 id="the-whisper">/// 2. TIER I: THE WHISPER (DAWN ORDEAL)</h2>
<p>
  Minor auditory hallucinations and crawling sorrow larvae manifesting in peripheral hallways. Easily suppressed by Grade 1–2 operatives wielding basic Grudge/Lament weaponry.
</p>

<h2 id="the-surge">/// 3. TIER II: THE SURGE (NOON ORDEAL)</h2>
<p>
  Effluent geysers erupting from drainage grates across Floors 3–5. Inflicts passive Weight damage on non-shielded personnel and reduces chamber Coherence counters by 1 if left uncontained.
</p>

<h2 id="the-breach">/// 4. TIER III: THE BREACH (DUSK ORDEAL)</h2>
<p>
  Crystalline monolithic pillars piercing multiple sector bulkheads simultaneously. Spawns hostile Night Aberrations capable of engaging multiple SED strike teams.
</p>

<h2 id="the-abyss">/// 5. TIER IV: THE ABYSS (MIDNIGHT ORDEAL)</h2>
<p>
  Catastrophic existential rupture unsealing Floor 8 Gate Watch boundaries. Inflicts global facility-wide Void decay (% Max HP). Demands immediate deployment of Echo-Core Leads and APOCRYPHA-grade M.A.W. armament squads.
</p>
"""
}

# 5. Facility Incident Reports Page
articles['lore/facility-incident-reports.html'] = {
    'title': 'Directorate Facility Incident Reports (001–010)',
    'cat': 'LORE & COSMOLOGY',
    'cat_link': 'index.html',
    'content': """
<div class="toc" id="toc">
  <div class="toc-title">Contents</div>
  <ol>
    <li><a href="#incident-001">Incident 001: The Silent Breach</a></li>
    <li><a href="#incident-002">Incident 002: The Noon Cascade</a></li>
    <li><a href="#incident-008">Incident 008: The Colossus Passes</a></li>
    <li><a href="#incident-009">Incident 009: The Bell's Crescendo</a></li>
    <li><a href="#incident-010">Incident 010: The Healing Shadow</a></li>
  </ol>
</div>

<h2 id="incident-001">/// INCIDENT 001: THE SILENT BREACH</h2>
<p>
  <strong>Cycle 0412 // Floor 6 Deep Vault</strong>: Complete acoustic baffle failure during observation of SE-007. 14 personnel experienced total retrograde amnesia before containment was restored by Lead Marjuk.
</p>

<h2 id="incident-002">/// INCIDENT 002: THE NOON CASCADE</h2>
<p>
  <strong>Cycle 0884 // Floor 3 Extraction Hall</strong>: Effluent surge in primary refining conduit. Over-pressurization resulted in spontaneous manifestation of 6 Siphon Leeches across Sector B corridors.
</p>

<h2 id="incident-008">/// INCIDENT 008: THE COLOSSUS PASSES</h2>
<p>
  <strong>Cycle 1,420 // Floor 2 Maw's Keep</strong>: Seismic breach of SE-002. Kinetic tremors compromised structural integrity of central elevator shaft. Suppressed through coordinated Ferrehan work by Lead Dekan.
</p>

<h2 id="incident-009">/// INCIDENT 009: THE BELL'S CRESCENDO</h2>
<p>
  <strong>Cycle 1,605 // Floor 2 Maw's Keep</strong>: Coherence threshold depleted during shift change. Resonance shockwaves shattered all glass monitoring panels in Sector MK-01. Fatalities: 8; Restored via emergency acoustic dampers.
</p>

<h2 id="incident-010">/// INCIDENT 010: THE HEALING SHADOW</h2>
<p>
  <strong>Cycle 1,778 (Dawn Initiative)</strong>: Final cycle breakthrough. Absolvohan resonance seed catalyzed by Director Majin and Secretary Seiyon, bringing an end to the 1,778 temporal resets.
</p>
"""
}

# Generate M.A.W. equipment files for SE-004, SE-006, SE-008
maw_items = {
    'maw/maw-w-004-01-rust-halberd.html': ('M.A.W. Weapon: Rust Halberd', 'SE-004', 'Weapon', 'Grudge', '14–20', 'Floor 5 Border Watch'),
    'maw/maw-s-004-01-sentrys-iron-plate.html': ('M.A.W. Suit: Sentry\'s Iron Plate', 'SE-004', 'Suit', 'Grudge 0.5 Res', 'Heavy Plate', 'Floor 5 Border Watch'),
    'maw/maw-g-004-01-corrosion-visor.html': ('M.A.W. Gift: Corrosion Visor', 'SE-004', 'Special Gift', '+4 HP, +3 Res', 'Ocular Augment', 'Floor 5 Border Watch'),
    'maw/maw-w-006-01-siphon-cannula.html': ('M.A.W. Weapon: Siphon Cannula', 'SE-006', 'Weapon', 'Weight (Dual)', '10–16', 'Floor 3 Extraction Hall'),
    'maw/maw-s-006-01-leech-membrane-suit.html': ('M.A.W. Suit: Leech Membrane Suit', 'SE-006', 'Suit', 'Weight 0.6 Res', 'Bio-Membrane', 'Floor 3 Extraction Hall'),
    'maw/maw-g-006-01-effluent-gland.html': ('M.A.W. Gift: Effluent Gland', 'SE-006', 'Special Gift', '+5 HP, +5 SP', 'Symbiotic Gland', 'Floor 3 Extraction Hall'),
    'maw/maw-w-008-01-thorn-impaler.html': ('M.A.W. Weapon: Thorn Impaler', 'SE-008', 'Weapon', 'Grudge/Lament', '20–26', 'Floor 6 Deep Vault'),
    'maw/maw-s-008-01-sarcophagus-shroud.html': ('M.A.W. Suit: Sarcophagus Shroud', 'SE-008', 'Suit', 'Grudge 0.4 Res', 'Iron Sarcophagus', 'Floor 6 Deep Vault'),
    'maw/maw-g-008-01-spike-crown.html': ('M.A.W. Gift: Spike Crown', 'SE-008', 'Special Gift', '+8 SP, +5 Atk', 'Thorn Halo', 'Floor 6 Deep Vault'),
}

for path, (title, origin, gear_type, stat, sub_desc, dept) in maw_items.items():
    articles[path] = {
        'title': title,
        'cat': 'M.A.W. ARMORY',
        'cat_link': 'index.html',
        'content': f"""
<div class="infobox-wrapper" style="float:right; width:340px; margin:0 0 1.5rem 1.5rem;">
  <div class="infobox" style="border:2px solid #f1df76; background:#0c101a; padding:14px; border-radius:6px;">
    <div style="text-align:center; padding-bottom:8px; border-bottom:1.5px solid #f1df76;">
      <h3 style="margin:0; font-family:'JetBrains Mono', monospace; color:#f1df76; font-size:1.1rem;">{title.upper()}</h3>
      <b style="color:#ffffff; font-size:0.85rem;">EXTRACTED M.A.W. ARTIFACT</b>
    </div>
    <table class="pm-table condensed" style="width:100%; margin-top:10px;">
      <tr><th>Origin Entity</th><td>{origin}</td></tr>
      <tr><th>Gear Type</th><td>{gear_type}</td></tr>
      <tr><th>Combat Stat</th><td>{stat}</td></tr>
      <tr><th>Classification</th><td>{sub_desc}</td></tr>
      <tr><th>Department</th><td>{dept}</td></tr>
    </table>
  </div>
</div>

<h2 id="overview">/// 1. SPECIFICATION &amp; COMBAT PROPERTIES</h2>
<p>
  <strong>{title}</strong> is materialized directly from the psychic resonance of <strong>{origin}</strong>. Engineered by Echo-Core Lead Ayshuk in Floor 4 (Insight Forge), it channels stabilized Han flux into active combat multipliers.
</p>
<h2 id="combat-mechanics">/// 2. COMBAT &amp; RESONANCE MULTIPLIERS</h2>
<p>
  Provides superior defensive and offensive capabilities when wielded by operatives with matching psychic fortitude. Prevents catastrophic cognitive rupture during high-threat containment breaches.
</p>
"""
    }

wiki_root = '/home/user/01_Somnarak_Wiki'
for rel_path, data in articles.items():
    full_path = os.path.join(wiki_root, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    depth = '..' if '/' in rel_path else '.'
    html = wrap_article(data['title'], data['cat'], data['cat_link'], data['content'], depth)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Wrote {full_path}')

print('SUCCESS: Created all additional canonical entities, M.A.W. armaments, ordeals, and incident files!')
