import os

os.makedirs("docs/game-wiki", exist_ok=True)

# 1. docs/index.html (Front Home Page Portal)
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PROJECT SOMNARAK // THE ABSOLVOHAN FRONT PORTAL</title>
  <style>
    :root {
      --bg-dark: #0a0c10;
      --bg-panel: #11151c;
      --bg-card: #161b22;
      --border-color: #30363d;
      --border-glow: #1f6feb;
      --text-main: #e6edf3;
      --text-muted: #8b949e;
      --accent-cyan: #38bdf8;
      --accent-crimson: #f43f5e;
      --accent-amber: #fbbf24;
      --accent-purple: #a855f7;
      --accent-green: #22c55e;
      --font-mono: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
      --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      padding: 0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    /* Top Ticker Bar */
    .top-bar {
      background: #0d1117;
      border-bottom: 1px solid var(--border-color);
      padding: 8px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--font-mono);
      font-size: 0.82rem;
      letter-spacing: 0.05em;
    }

    .top-bar .cycle-tag {
      color: var(--accent-cyan);
      font-weight: bold;
    }

    .top-bar .status-ticker {
      color: var(--accent-green);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .pulse-dot {
      width: 8px;
      height: 8px;
      background: var(--accent-green);
      border-radius: 50%;
      box-shadow: 0 0 8px var(--accent-green);
      animation: pulse 2s infinite;
    }

    @keyframes pulse {
      0% { opacity: 1; }
      50% { opacity: 0.3; }
      100% { opacity: 1; }
    }

    /* Header Nav */
    header {
      background: rgba(17, 21, 28, 0.95);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 16px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .logo-area {
      display: flex;
      flex-direction: column;
    }

    .logo-area h1 {
      font-family: var(--font-mono);
      font-size: 1.4rem;
      letter-spacing: 0.15em;
      color: #ffffff;
      text-transform: uppercase;
    }

    .logo-area .sub {
      font-size: 0.75rem;
      color: var(--accent-crimson);
      font-family: var(--font-mono);
      letter-spacing: 0.2em;
    }

    nav {
      display: flex;
      gap: 16px;
    }

    nav a {
      color: var(--text-muted);
      text-decoration: none;
      font-family: var(--font-mono);
      font-size: 0.85rem;
      padding: 6px 12px;
      border-radius: 4px;
      border: 1px solid transparent;
      transition: all 0.2s ease;
    }

    nav a:hover, nav a.active {
      color: var(--accent-cyan);
      border-color: var(--border-glow);
      background: rgba(56, 189, 248, 0.08);
    }

    nav a.highlight-wiki {
      color: var(--accent-amber);
      border-color: rgba(251, 191, 36, 0.4);
      background: rgba(251, 191, 36, 0.05);
    }

    nav a.highlight-wiki:hover {
      background: rgba(251, 191, 36, 0.15);
      border-color: var(--accent-amber);
    }

    /* Hero Section */
    .hero {
      padding: 64px 32px 48px;
      text-align: center;
      max-width: 1100px;
      margin: 0 auto;
    }

    .hero-badge {
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      color: var(--accent-cyan);
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 4px 14px;
      border-radius: 12px;
      margin-bottom: 20px;
      letter-spacing: 0.1em;
    }

    .hero h2 {
      font-size: 2.8rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 16px;
      background: linear-gradient(135deg, #ffffff 40%, #94a3b8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero p {
      font-size: 1.15rem;
      color: var(--text-muted);
      max-width: 820px;
      margin: 0 auto 32px;
    }

    .metrics-strip {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-top: 32px;
      text-align: left;
    }

    .metric-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      padding: 16px 20px;
      border-radius: 6px;
    }

    .metric-card .num {
      font-family: var(--font-mono);
      font-size: 1.6rem;
      font-weight: bold;
      color: var(--text-main);
    }

    .metric-card .label {
      font-size: 0.78rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Pillars Grid */
    .pillars-section {
      max-width: 1280px;
      margin: 0 auto 64px;
      padding: 0 32px;
      width: 100%;
    }

    .section-title {
      font-family: var(--font-mono);
      font-size: 1.1rem;
      text-transform: uppercase;
      letter-spacing: 0.15em;
      color: var(--accent-cyan);
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .section-title::after {
      content: '';
      flex: 1;
      height: 1px;
      background: var(--border-color);
    }

    .grid-pillars {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
      gap: 24px;
    }

    .pillar-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 28px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      transition: all 0.25s ease;
    }

    .pillar-card:hover {
      border-color: var(--accent-cyan);
      transform: translateY(-4px);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
    }

    .pillar-card.featured-wiki {
      border-color: rgba(251, 191, 36, 0.5);
      background: linear-gradient(180deg, rgba(251, 191, 36, 0.04) 0%, var(--bg-card) 100%);
    }

    .pillar-card.featured-wiki:hover {
      border-color: var(--accent-amber);
      box-shadow: 0 12px 30px rgba(251, 191, 36, 0.15);
    }

    .card-top {
      margin-bottom: 20px;
    }

    .pillar-num {
      font-family: var(--font-mono);
      font-size: 0.8rem;
      color: var(--accent-cyan);
      letter-spacing: 0.1em;
      margin-bottom: 8px;
    }

    .pillar-card.featured-wiki .pillar-num {
      color: var(--accent-amber);
    }

    .pillar-card h3 {
      font-size: 1.45rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 6px;
    }

    .pillar-card .korean-sub {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 12px;
    }

    .pillar-card p {
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.6;
    }

    .quick-tags {
      margin: 18px 0;
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .quick-tag {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      padding: 3px 8px;
      background: #0d1117;
      border: 1px solid var(--border-color);
      border-radius: 4px;
      color: var(--text-muted);
    }

    .card-bottom a {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-mono);
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--accent-cyan);
      text-decoration: none;
      padding: 10px 16px;
      background: rgba(56, 189, 248, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 4px;
      transition: all 0.2s ease;
      width: 100%;
      justify-content: center;
    }

    .pillar-card.featured-wiki .card-bottom a {
      color: var(--accent-amber);
      background: rgba(251, 191, 36, 0.08);
      border-color: rgba(251, 191, 36, 0.4);
    }

    .card-bottom a:hover {
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--accent-cyan);
    }

    .pillar-card.featured-wiki .card-bottom a:hover {
      background: rgba(251, 191, 36, 0.2);
      border-color: var(--accent-amber);
    }

    /* Footer */
    footer {
      background: #0d1117;
      border-top: 1px solid var(--border-color);
      padding: 32px;
      margin-top: auto;
      text-align: center;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      color: var(--text-muted);
    }

    footer p {
      margin-bottom: 8px;
    }

    footer .version-tag {
      color: var(--accent-cyan);
    }
  </style>
</head>
<body>

  <!-- Operational Ticker -->
  <div class="top-bar">
    <div class="cycle-tag">CYCLE 1,778 // THE ABSOLVOHAN OPERATIONAL CONTROL</div>
    <div class="status-ticker">
      <div class="pulse-dot"></div>
      <span>ATMOSPHERIC WATCH: LEVEL 1 — STABLE (292 ENTITIES SECURED)</span>
    </div>
  </div>

  <!-- Header Navigation -->
  <header>
    <div class="logo-area">
      <h1>Project Somnarak</h1>
      <span class="sub">THE ABSOLVOHAN // MASTER ARCHIVES</span>
    </div>
    <nav>
      <a href="#wiki">Wiki</a>
      <a href="#story">Story</a>
      <a href="#game">Game</a>
      <a href="game-wiki/index.html" class="highlight-wiki">Game Wiki</a>
      <a href="#collection">Collection</a>
    </nav>
  </header>

  <!-- Hero Banner -->
  <section class="hero">
    <div class="hero-badge">THE ABSOLVOHAN MASTER PORTAL // GITHUB PAGES ROOT</div>
    <h2>Contain Sorrow. Refine Han. Endure the Cycles.</h2>
    <p>
      Deep beneath Somnarak City lies The Absolvohan — a colossal subterranean containment monolith where human sorrow manifests as volatile entities. Navigate through encyclopedic archives, dramaturgical chronicles, tactical combat simulators, Project Moon style game wikis, and the complete 292 Sorrow Entity vault.
    </p>

    <!-- Audited Status Strip -->
    <div class="metrics-strip">
      <div class="metric-card">
        <div class="num" style="color: var(--accent-cyan);">292 / 292</div>
        <div class="label">Sorrow Entities Audited (100%)</div>
      </div>
      <div class="metric-card">
        <div class="num" style="color: var(--accent-green);">131 / 131</div>
        <div class="label">Two-Work-Type Rules (100%)</div>
      </div>
      <div class="metric-card">
        <div class="num" style="color: var(--accent-amber);">287+ SVG</div>
        <div class="label">M.A.W. Armory Weapons</div>
      </div>
      <div class="metric-card">
        <div class="num" style="color: var(--accent-purple);">1,778</div>
        <div class="label">Mnemonic Cycles Logged</div>
      </div>
    </div>
  </section>

  <!-- Five Pillars Section -->
  <section class="pillars-section">
    <div class="section-title">The Five Master Gateway Pillars (5대 기둥 체제)</div>

    <div class="grid-pillars">
      
      <!-- Pillar 1: WIKI -->
      <div class="pillar-card" id="wiki">
        <div class="card-top">
          <div class="pillar-num">PILLAR 01 // ENCYCLOPEDIA</div>
          <h3>WIKI HUB</h3>
          <div class="korean-sub">백과사전 포털 · Baekgwasajeon Poteol</div>
          <p>
            The comprehensive municipal knowledge base. Contains setting cosmology, SECC classification codices (Forms, Ranks I–V, Potency α–ω), the 5 Syndicates of The Raw, 10 Specialist Cadres, and the 19-section Somnarak vs. Lobotomy Corporation Comparative Guide.
          </p>
          <div class="quick-tags">
            <span class="quick-tag">SECC Codex</span>
            <span class="quick-tag">10 Cadres</span>
            <span class="quick-tag">5 Syndicates</span>
            <span class="quick-tag">System Comparison</span>
          </div>
        </div>
        <div class="card-bottom">
          <a href="../SOMNARAK-WORLD/Master_Codices/06_Integrity_Audits_and_Comparative_Studies/COMPLETE_SYSTEM_COMPARISON_SOMNARAK_VS_LOBOTOMY_CORPORATION.md">Enter Wiki Hub &rarr;</a>
        </div>
      </div>

      <!-- Pillar 2: STORY -->
      <div class="pillar-card" id="story">
        <div class="card-top">
          <div class="pillar-num">PILLAR 02 // NARRATIVE</div>
          <h3>STORY HUB</h3>
          <div class="korean-sub">서사 및 연대기 · Seosa mit Yeondaegi</div>
          <p>
            The dramaturgical narrative vault. Explore historical logs across the 1,778 Mnemonic Cycles of The Absolvohan, SED and UCD field operational campaigns, 4-phase Echo-Core Realization Wars, and the 8-scene synchronized Animatic MAD script ("Nee, Dorodoro-san").
          </p>
          <div class="quick-tags">
            <span class="quick-tag">1,778 Cycles</span>
            <span class="quick-tag">SED Arcs 1-7</span>
            <span class="quick-tag">Realization Wars</span>
            <span class="quick-tag">Animatic Script</span>
          </div>
        </div>
        <div class="card-bottom">
          <a href="../TRYOUT,SANDBOX/PROJECT.SOMNARAK-Animatic-Text.txt">Enter Story Hub &rarr;</a>
        </div>
      </div>

      <!-- Pillar 3: GAME -->
      <div class="pillar-card" id="game">
        <div class="card-top">
          <div class="pillar-num">PILLAR 03 // SIMULATOR</div>
          <h3>GAME HUB</h3>
          <div class="korean-sub">전술 시뮬레이터 · Jeonsul Simyulleisyeon</div>
          <p>
            Interactive tactical combat and containment engine. Engage with the 10-Node spatial grid battlefield, dynamic Speed-based action slots, clash calculation algorithms, containment protocols with strict Two-Work enforcement, and Grade 1–5 Workshop forging.
          </p>
          <div class="quick-tags">
            <span class="quick-tag">10-Node Grid</span>
            <span class="quick-tag">Action Slots</span>
            <span class="quick-tag">Clash Engine</span>
            <span class="quick-tag">Workshop Forging</span>
          </div>
        </div>
        <div class="card-bottom">
          <a href="#game">Launch Tactical Simulator &rarr;</a>
        </div>
      </div>

      <!-- Pillar 4: GAME WIKI (Featured Moon-Style Wiki Hub) -->
      <div class="pillar-card featured-wiki" id="game-wiki">
        <div class="card-top">
          <div class="pillar-num">PILLAR 04 // MECHANICS COMPENDIUM</div>
          <h3>GAME WIKI HUB</h3>
          <div class="korean-sub">게임 위키 포털 · P.M. Wiki.gg / Fandom Style</div>
          <p>
            Full-scale gaming mechanics database modeled directly after Project Moon wikis across <strong>wiki.gg</strong> and <strong>Fandom</strong>. Detailed game guides for <strong>Lobotomy Corporation</strong>, <strong>Library of Ruina</strong>, <strong>Limbus Company</strong>, and <strong>Project Somnarak</strong> native game systems.
          </p>
          <div class="quick-tags">
            <span class="quick-tag" style="border-color: var(--accent-amber); color: var(--accent-amber);">Lobotomy Corp</span>
            <span class="quick-tag" style="border-color: var(--accent-amber); color: var(--accent-amber);">Library of Ruina</span>
            <span class="quick-tag" style="border-color: var(--accent-amber); color: var(--accent-amber);">Limbus Company</span>
            <span class="quick-tag" style="border-color: var(--accent-amber); color: var(--accent-amber);">Somnarak Systems</span>
          </div>
        </div>
        <div class="card-bottom">
          <a href="game-wiki/index.html">Access Game Wiki &rarr;</a>
        </div>
      </div>

      <!-- Pillar 5: COLLECTION -->
      <div class="pillar-card" id="collection">
        <div class="card-top">
          <div class="pillar-num">PILLAR 05 // SPECIMENS & WEAPONS</div>
          <h3>COLLECTION HUB</h3>
          <div class="korean-sub">아카이브 및 무기고 · Akaibeu mit Mugigo</div>
          <p>
            The master specimen and equipment archive. Access all 292 individualized Sorrow Entity dossiers, 287+ SVG M.A.W. vector weapon schematics, the 131-relic Tool Abnormality catalog (Cogitopedia format), and full architectural blueprints of Somnarak City.
          </p>
          <div class="quick-tags">
            <span class="quick-tag">292 SE Vault</span>
            <span class="quick-tag">287+ SVG Weapons</span>
            <span class="quick-tag">Tool Relics</span>
            <span class="quick-tag">City Blueprints</span>
          </div>
        </div>
        <div class="card-bottom">
          <a href="../SOMNARAK-WORLD/Sorrow_Entities/">Explore Collection &rarr;</a>
        </div>
      </div>

    </div>
  </section>

  <!-- Global Footer -->
  <footer>
    <p>PROJECT SOMNARAK // THE ABSOLVOHAN MONOLITHIC ARCHIVES</p>
    <p>Branch: <span class="version-tag">arena/01a0b699-project-somnarak-wiki</span> · Canonical Cycle: 1,778 · Verified SE Total: 292</p>
    <p style="margin-top: 8px; font-size: 0.72rem; color: #484f58;">
      Compliant with SECC Standards, Two-Work-Type Containment Law & Unified Project Moon System Translation.
    </p>
  </footer>

</body>
</html>
"""

# 2. docs/game-wiki/index.html (The Dedicated P.M. Wiki.gg / Fandom Style Game Wiki Hub)
game_wiki_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GAME WIKI // PROJECT MOON & SOMNARAK MECHANICS COMPENDIUM</title>
  <style>
    :root {
      --bg-dark: #0a0c10;
      --bg-panel: #11151c;
      --bg-card: #161b22;
      --border-color: #30363d;
      --border-glow: #fbbf24;
      --text-main: #e6edf3;
      --text-muted: #8b949e;
      --accent-cyan: #38bdf8;
      --accent-crimson: #f43f5e;
      --accent-amber: #fbbf24;
      --accent-purple: #c084fc;
      --accent-green: #34d399;
      --lcorp-red: #ef4444;
      --lor-blue: #3b82f6;
      --limbus-gold: #f59e0b;
      --somnarak-cyan: #06b6d4;
      --font-mono: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
      --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      padding: 0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    /* Wiki Top Bar */
    .wiki-top-nav {
      background: #0d1117;
      border-bottom: 1px solid var(--border-color);
      padding: 10px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--font-mono);
      font-size: 0.85rem;
    }

    .wiki-breadcrumbs a {
      color: var(--accent-cyan);
      text-decoration: none;
    }

    .wiki-breadcrumbs span {
      color: var(--text-muted);
      margin: 0 8px;
    }

    .wiki-meta-badge {
      background: rgba(251, 191, 36, 0.1);
      color: var(--accent-amber);
      border: 1px solid rgba(251, 191, 36, 0.3);
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 0.75rem;
      letter-spacing: 0.05em;
    }

    /* Wiki Header */
    .wiki-header {
      background: linear-gradient(180deg, #161b22 0%, #0d1117 100%);
      border-bottom: 2px solid var(--accent-amber);
      padding: 36px 32px 28px;
    }

    .wiki-header-container {
      max-width: 1200px;
      margin: 0 auto;
    }

    .wiki-header h1 {
      font-family: var(--font-mono);
      font-size: 2.2rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
    }

    .wiki-header .sub-desc {
      color: var(--text-muted);
      font-size: 1.05rem;
      max-width: 900px;
      margin-bottom: 24px;
    }

    /* Game Navigation Tabs */
    .game-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 16px;
    }

    .game-tab {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 18px;
      border-radius: 6px;
      font-family: var(--font-mono);
      font-size: 0.9rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s ease;
      border: 1px solid var(--border-color);
      background: #11151c;
      color: var(--text-main);
    }

    .game-tab:hover {
      transform: translateY(-2px);
    }

    .game-tab.tab-lcorp { border-color: rgba(239, 68, 68, 0.4); }
    .game-tab.tab-lcorp:hover { background: rgba(239, 68, 68, 0.15); border-color: var(--lcorp-red); color: var(--lcorp-red); }

    .game-tab.tab-lor { border-color: rgba(59, 130, 246, 0.4); }
    .game-tab.tab-lor:hover { background: rgba(59, 130, 246, 0.15); border-color: var(--lor-blue); color: var(--lor-blue); }

    .game-tab.tab-limbus { border-color: rgba(245, 158, 11, 0.4); }
    .game-tab.tab-limbus:hover { background: rgba(245, 158, 11, 0.15); border-color: var(--limbus-gold); color: var(--limbus-gold); }

    .game-tab.tab-somnarak { border-color: rgba(6, 182, 212, 0.4); }
    .game-tab.tab-somnarak:hover { background: rgba(6, 182, 212, 0.15); border-color: var(--somnarak-cyan); color: var(--somnarak-cyan); }

    /* Main Wiki Content */
    .wiki-main {
      max-width: 1200px;
      margin: 40px auto 64px;
      padding: 0 32px;
      width: 100%;
    }

    .wiki-section {
      margin-bottom: 56px;
      scroll-margin-top: 20px;
    }

    .section-header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--border-color);
      margin-bottom: 24px;
    }

    .section-header-bar h2 {
      font-family: var(--font-mono);
      font-size: 1.5rem;
      letter-spacing: 0.05em;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .tag-badge {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      padding: 4px 10px;
      border-radius: 4px;
      font-weight: 600;
    }

    .badge-lcorp { background: rgba(239, 68, 68, 0.2); color: var(--lcorp-red); border: 1px solid var(--lcorp-red); }
    .badge-lor { background: rgba(59, 130, 246, 0.2); color: var(--lor-blue); border: 1px solid var(--lor-blue); }
    .badge-limbus { background: rgba(245, 158, 11, 0.2); color: var(--limbus-gold); border: 1px solid var(--limbus-gold); }
    .badge-somnarak { background: rgba(6, 182, 212, 0.2); color: var(--somnarak-cyan); border: 1px solid var(--somnarak-cyan); }

    /* Module Grid */
    .module-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
      gap: 20px;
    }

    .module-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 20px;
      transition: all 0.2s ease;
    }

    .module-card:hover {
      border-color: var(--accent-cyan);
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(0,0,0,0.3);
    }

    .module-card h3 {
      font-size: 1.15rem;
      color: #ffffff;
      margin-bottom: 8px;
    }

    .module-card p {
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 14px;
    }

    .feature-list {
      list-style: none;
      padding: 0;
      margin-bottom: 16px;
      font-size: 0.82rem;
      color: #cbd5e1;
    }

    .feature-list li {
      margin-bottom: 6px;
      position: relative;
      padding-left: 14px;
    }

    .feature-list li::before {
      content: '•';
      color: var(--accent-cyan);
      position: absolute;
      left: 0;
    }

    /* Comparison Table */
    .wiki-table {
      width: 100%;
      border-collapse: collapse;
      margin: 24px 0;
      font-size: 0.88rem;
    }

    .wiki-table th, .wiki-table td {
      border: 1px solid var(--border-color);
      padding: 12px 16px;
      text-align: left;
    }

    .wiki-table th {
      background: #0d1117;
      color: var(--accent-cyan);
      font-family: var(--font-mono);
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .wiki-table tr:nth-child(even) {
      background: rgba(22, 27, 34, 0.6);
    }

    /* Footer */
    footer {
      background: #0d1117;
      border-top: 1px solid var(--border-color);
      padding: 32px;
      margin-top: auto;
      text-align: center;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      color: var(--text-muted);
    }
  </style>
</head>
<body>

  <!-- Top Navigation & Breadcrumbs -->
  <div class="wiki-top-nav">
    <div class="wiki-breadcrumbs">
      <a href="../index.html">Portal Home</a>
      <span>/</span>
      <strong>Game Wiki (P.M. Wiki.gg & Fandom Style)</strong>
    </div>
    <div class="wiki-meta-badge">UNIFIED GAMING MECHANICS DATABASE</div>
  </div>

  <!-- Header Banner -->
  <header class="wiki-header">
    <div class="wiki-header-container">
      <h1>GAME WIKI COMPENDIUM</h1>
      <p class="sub-desc">
        Comprehensive mechanics, formulas, card databases, and containment strategies covering <strong>Lobotomy Corporation</strong>, <strong>Library of Ruina</strong>, <strong>Limbus Company</strong>, and <strong>Project Somnarak</strong> native game systems. Structured in authentic <em>wiki.gg</em> and <em>fandom</em> gaming wiki layout.
      </p>

      <!-- Fast Jump Bar -->
      <div class="game-tabs">
        <a href="#lcorp" class="game-tab tab-lcorp">Lobotomy Corporation</a>
        <a href="#lor" class="game-tab tab-lor">Library of Ruina</a>
        <a href="#limbus" class="game-tab tab-limbus">Limbus Company</a>
        <a href="#somnarak" class="game-tab tab-somnarak">Project Somnarak Engine</a>
        <a href="#cross-table" class="game-tab">Unified System Matrix</a>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <main class="wiki-main">

    <!-- SECTOR 1: LOBOTOMY CORPORATION -->
    <section class="wiki-section" id="lcorp">
      <div class="section-header-bar">
        <h2>Lobotomy Corporation Wiki Sector</h2>
        <span class="tag-badge badge-lcorp">MANAGEMENT SIMULATION</span>
      </div>
      <p style="color: var(--text-muted); margin-bottom: 20px;">
        Exhaustive reference for facility management, Abnormality work probabilities, Qliphoth meltdowns, Ordeal wave pacification, Sephirah Core Meltdowns, and E.G.O equipment scaling.
      </p>
      
      <div class="module-grid">
        <div class="module-card">
          <h3>Abnormality Work Matrix</h3>
          <p>Complete statistical odds for Fortitude (Instinct), Prudence (Insight), Temperance (Attachment), and Justice (Repression).</p>
          <ul class="feature-list">
            <li>PE-Box and NE-Box yield calculations</li>
            <li>Qliphoth Counter trigger rules & escapes</li>
            <li>Work duration, movement speed & damage ticks</li>
          </ul>
        </div>
        <div class="module-card">
          <h3>Qliphoth Meltdowns & Ordeals</h3>
          <p>Procedures for escalating containment hazards and surviving extra-dimensional incursions.</p>
          <ul class="feature-list">
            <li>Level I through X Meltdown countdowns</li>
            <li>Dawn, Noon, Dusk & Midnight Ordeals</li>
            <li>Green, Amber, Crimson, Violet pacification tactics</li>
          </ul>
        </div>
        <div class="module-card">
          <h3>Sephirah Core Meltdowns</h3>
          <p>Tactical battle manuals for Asiyah, Briah, and Atziluth floor boss suppressions.</p>
          <ul class="feature-list">
            <li>Malkuth, Yesod, Hod, Netzach debuffs</li>
            <li>Tiphereth, Gebura & Chesed lethal phases</li>
            <li>Binah, Hokma, and Keter architectural gauntlet</li>
          </ul>
        </div>
        <div class="module-card">
          <h3>E.G.O Equipment & Tools</h3>
          <p>Weapons, Suits, and Gifts cataloged across ZAYIN, TETH, HE, WAW, and ALEPH tiers.</p>
          <ul class="feature-list">
            <li>Damage types: Red, White, Black, Pale</li>
            <li>Tool Abnormalities: Continuous, Single-Use, Equippable</li>
            <li>Log & Method unlock thresholds and fatal timers</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SECTOR 2: LIBRARY OF RUINA -->
    <section class="wiki-section" id="lor">
      <div class="section-header-bar">
        <h2>Library of Ruina Wiki Sector</h2>
        <span class="tag-badge badge-lor">DECKBUILDING TACTICAL DICE BATTLE</span>
      </div>
      <p style="color: var(--text-muted); margin-bottom: 20px;">
        Complete deckbuilding, Key Page attribution, Combat Page clashing formulas, Speed Dice mechanics, and Floor Realization trauma boss walkthroughs.
      </p>

      <div class="module-grid">
        <div class="module-card">
          <h3>Key Pages & Passive Attribution</h3>
          <p>Deck slot optimization, attribute point budgets, and dice power synergies.</p>
          <ul class="feature-list">
            <li>Slash, Pierce, Blunt, Block, Evade bonuses</li>
            <li>Health & Stagger resistance thresholds</li>
            <li>Endgame attribution meta (Purple Tear, Red Mist, Xiao)</li>
          </ul>
        </div>
        <div class="module-card">
          <h3>Combat Page Deckbuilding</h3>
          <p>Light management and cost-curve stabilization for sustained receptions.</p>
          <ul class="feature-list">
            <li>0-cost to 4-cost page rotation loops</li>
            <li>On Hit, Clash Win, and Clash Lose triggers</li>
            <li>Mass Attack pages: Summation vs. Individual</li>
          </ul>
        </div>
        <div class="module-card">
          <h3>Speed Dice & Clash Calculations</h3>
          <p>Initiative rolls, target redirection, and mathematical clash resolution.</p>
          <ul class="feature-list">
            <li>Speed priority and interception mechanics</li>
            <li>Power stacking (+Power / -Power math)</li>
            <li>Stagger vulnerability multipliers (Fatal to Ineffective)</li>
          </ul>
        </div>
        <div class="module-card">
          <h3>Emotion & Floor Realizations</h3>
          <p>Emotion Level progression and multi-phase Abnormality realization encounters.</p>
          <ul class="feature-list">
            <li>Levels 0 to V: Positive vs. Negative Emotion Coins</li>
            <li>Abnormality Page drafting & E.G.O Awakening</li>
            <li>All 10 Floor Realization 4-phase & 5-phase guides</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SECTOR 3: LIMBUS COMPANY -->
    <section class="wiki-section" id="limbus">
      <div class="section-header-bar">
        <h2>Limbus Company Wiki Sector</h2>
        <span class="tag-badge badge-limbus">SIN RESONANCE STRATEGIC RPG</span>
      </div>
      <p style="color: var(--text-muted); margin-bottom: 20px;">
        Comprehensive guide to the 12 Sinners, Identity matrix, coin flip probabilities, Sanity engine, Sin affinities, and keyword status effect dynamics.
      </p>

      <div class="module-grid">
        <div class="module-card">
          <h3>12 Sinners & Identity Matrix</h3>
          <p>Base, 00, and 000 tier evaluations, Uptie I–IV costs, and Threadspinning scaling.</p>
          <ul class="feature-list">
            <li>Base Power, Coin Power, Plus & Minus Coins</li>
            <li>Skill 1, Skill 2, Skill 3, and Defense skill kits</li>
            <li>Level cap progression and stat multipliers</li>
          </ul>
        </div>
        <div class="module-card">
          <h3>Sanity (SP) & Coin Mechanics</h3>
          <p>The mathematical probability engine governing Heads flips and panic behaviors.</p>
          <ul class="feature-list">
            <li>Heads flip rate formula: 50% + SP%</li>
            <li>-45 to +45 SP scale; Panic types & Morale Boost</li>
            <li>E.G.O Corrosion mechanics and friendly fire danger</li>
          </ul>
        </div>
        <div class="module-card">
          <h3>Sin Affinities & Resonances</h3>
          <p>Wrath, Lust, Sloth, Gluttony, Gloom, Pride, Envy resource management.</p>
          <ul class="feature-list">
            <li>Sin Resonance (3+ matching skills in a chain)</li>
            <li>Absolute Resonance (consecutive chained sins)</li>
            <li>E.G.O Awakening cost checks and passive triggers</li>
          </ul>
        </div>
        <div class="module-card">
          <h3>Keyword Status Effects</h3>
          <p>Detailed mechanics for Potency, Count, triggers, and status interactions.</p>
          <ul class="feature-list">
            <li>Burn, Bleed, Rupture tick & count rules</li>
            <li>Tremor: Burst, Decay, Reverberation, Everlasting</li>
            <li>Sinking SP damage, Poise Crits, Charge thresholds</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SECTOR 4: PROJECT SOMNARAK NATIVE SYSTEMS -->
    <section class="wiki-section" id="somnarak">
      <div class="section-header-bar">
        <h2>Project Somnarak Game Engine Sector</h2>
        <span class="tag-badge badge-somnarak">NATIVE TACTICAL SYSTEMS</span>
      </div>
      <p style="color: var(--text-muted); margin-bottom: 20px;">
        Tactical game formulas, 10-Node spatial grid positioning, Speed-based action slots, Two-Work-Type containment laws, and Grade 1–5 Workshop crafting.
      </p>

      <div class="module-grid">
        <div class="module-card">
          <h3>10-Node Spatial Grid Arena</h3>
          <p>Node-based tactical movement, flanking bonuses, and knockback meters.</p>
          <ul class="feature-list">
            <li>Nodes 1 through 10 positioning and distance drag</li>
            <li>Frontline vs. Rearguard cover & interception</li>
            <li>AoE denial zones and push/pull knockback distances</li>
          </ul>
        </div>
        <div class="module-card">
          <h3>Speed & Action Slots</h3>
          <p>Turn-by-turn action slot generation and 6-battle-turn combat phases.</p>
          <ul class="feature-list">
            <li>Initiative Speed roll checks (Speed 1–8)</li>
            <li>Han Pressure (ATK) vs. Sorrow Gauge (HP) clashing</li>
            <li>Clash winning formulas and Power bonuses</li>
          </ul>
        </div>
        <div class="module-card">
          <h3>Containment Work Engine</h3>
          <p>Viderehan, Ferrehan, Flerehan, Pugnahan probability calculations.</p>
          <ul class="feature-list">
            <li>Two-Work-Type Rule: 131 Non-Subject entities strictly Viderehan/Ferrehan</li>
            <li>Flerehan & Pugnahan designated N/A on Object, Place, and Time</li>
            <li>Han-Energy yield multipliers and starting gauge thresholds</li>
          </ul>
        </div>
        <div class="module-card">
          <h3>Grade 1–5 Workshop Forging</h3>
          <p>Commissioning M.A.W. gear from Giltong, Su-Ho, and specialist bureaus.</p>
          <ul class="feature-list">
            <li>Drop rates: Grade 5 Legendary (0.5%), Grade 4 (1.0%), Grade 3 (5.0%)</li>
            <li>287+ SVG M.A.W. weapon vector database</li>
            <li>Elemental resistances: Despair, Grief, Rage, Numbness</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- UNIFIED SYSTEM TRANSLATION MATRIX -->
    <section class="wiki-section" id="cross-table">
      <div class="section-header-bar">
        <h2>Unified Cross-Game Translation Matrix</h2>
        <span class="tag-badge" style="background: rgba(255,255,255,0.1); color: #fff;">P.M. TO SOMNARAK CONVERTER</span>
      </div>
      <p style="color: var(--text-muted); margin-bottom: 16px;">
        1-to-1 operational converter bridging Lobotomy Corporation, Library of Ruina, and Limbus Company systems directly into Project Somnarak canonical mechanics:
      </p>

      <table class="wiki-table">
        <thead>
          <tr>
            <th>Concept / Mechanic</th>
            <th>Lobotomy Corporation</th>
            <th>Library of Ruina</th>
            <th>Limbus Company</th>
            <th>Project Somnarak Equivalent</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Supernatural Entity</strong></td>
            <td>Abnormality (환상체)</td>
            <td>Abnormality Book / Distortion</td>
            <td>Abnormality / Peccatulum</td>
            <td>Sorrow Entity (SE / 비탄체)</td>
          </tr>
          <tr>
            <td><strong>Extracted Gear</strong></td>
            <td>E.G.O Weapon & Suit</td>
            <td>Key Page & Combat Page</td>
            <td>Identity & E.G.O</td>
            <td>M.A.W. Armament & Attire</td>
          </tr>
          <tr>
            <td><strong>Psychic Fuel / Resource</strong></td>
            <td>Enkephalin (PE-Box)</td>
            <td>Light & Emotion Coins</td>
            <td>Sin Affinity Resources</td>
            <td>Han-Energy (한 에너지)</td>
          </tr>
          <tr>
            <td><strong>Primary Facility</strong></td>
            <td>L Corp HQ (X's Facility)</td>
            <td>The Library</td>
            <td>Mephistopheles Bus</td>
            <td>The Absolvohan Monolith</td>
          </tr>
          <tr>
            <td><strong>Departmental Bosses</strong></td>
            <td>Sephirah Core Meltdown</td>
            <td>Floor Realization</td>
            <td>Canto Climax / Railway</td>
            <td>Echo-Core Resonant Wars</td>
          </tr>
          <tr>
            <td><strong>Observation Work</strong></td>
            <td>Insight (Prudence)</td>
            <td>Observation / Analysis</td>
            <td>Sin Scan / Combat Info</td>
            <td>Viderehan (관조한 / 觀照恨)</td>
          </tr>
          <tr>
            <td><strong>Emotional Work</strong></td>
            <td>Attachment (Temperance)</td>
            <td>Emotion Resonance</td>
            <td>Sanity Recovery</td>
            <td>Flerehan (비애한 / 悲哀恨)</td>
          </tr>
          <tr>
            <td><strong>Suppression Work</strong></td>
            <td>Repression (Justice)</td>
            <td>Aggressive Clashing</td>
            <td>Physical Clash / Stagger</td>
            <td>Pugnahan (토벌한 / 討伐恨)</td>
          </tr>
          <tr>
            <td><strong>Endurance Work</strong></td>
            <td>Instinct (Fortitude)</td>
            <td>Endurance / Block Dice</td>
            <td>Defense Skill / Shield</td>
            <td>Ferrehan (인내한 / 忍耐恨)</td>
          </tr>
        </tbody>
      </table>
    </section>

  </main>

  <!-- Global Footer -->
  <footer>
    <p>PROJECT SOMNARAK // UNIFIED GAME WIKI COMPENDIUM</p>
    <p>Designed in the style of Project Moon wiki.gg and Fandom encyclopedias.</p>
    <p style="margin-top: 8px; font-size: 0.72rem; color: #484f58;">
      Covering Lobotomy Corporation · Library of Ruina · Limbus Company · Project Somnarak Engine
    </p>
  </footer>

</body>
</html>
"""

with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

with open("docs/game-wiki/index.html", "w", encoding="utf-8") as f:
    f.write(game_wiki_html)

print("Generated docs/index.html and docs/game-wiki/index.html successfully.")
