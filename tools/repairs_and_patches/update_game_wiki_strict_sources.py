with open("docs/game-wiki/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add direct repository links in the top navigation bar of game-wiki
old_nav = """    <div class="wiki-breadcrumbs">
      <a href="../index.html">Portal Home</a>
      <span>/</span>
      <strong>Game Wiki (P.M. Wiki.gg & Fandom Style)</strong>
    </div>"""

new_nav = """    <div class="wiki-breadcrumbs">
      <a href="../index.html">Portal Home</a>
      <span>/</span>
      <a href="../../SOMNARAK-WORLD/">SOMNARAK-WORLD</a>
      <span>/</span>
      <a href="../../GAME_BATTLE/">GAME_BATTLE</a>
      <span>/</span>
      <strong>Game Wiki (P.M. Wiki.gg & Fandom Style)</strong>
    </div>"""

assert old_nav in html, "Could not find old nav in docs/game-wiki/index.html"
html = html.replace(old_nav, new_nav)

# In the Sector 4 (Project Somnarak Game Engine Sector) add direct links to GAME_BATTLE
old_sec4 = """    <!-- SECTOR 4: PROJECT SOMNARAK NATIVE SYSTEMS -->
    <section class="wiki-section" id="somnarak">
      <div class="section-header-bar">
        <h2>Project Somnarak Game Engine Sector</h2>
        <span class="tag-badge badge-somnarak">NATIVE TACTICAL SYSTEMS</span>
      </div>
      <p style="color: var(--text-muted); margin-bottom: 20px;">
        Tactical game formulas, 10-Node spatial grid positioning, Speed-based action slots, Two-Work-Type containment laws, and Grade 1–5 Workshop crafting.
      </p>"""

new_sec4 = """    <!-- SECTOR 4: PROJECT SOMNARAK NATIVE SYSTEMS -->
    <section class="wiki-section" id="somnarak">
      <div class="section-header-bar">
        <h2>Project Somnarak Game Engine Sector</h2>
        <span class="tag-badge badge-somnarak">NATIVE TACTICAL SYSTEMS (GAME_BATTLE)</span>
      </div>
      <p style="color: var(--text-muted); margin-bottom: 20px;">
        Tactical game formulas, 10-Node spatial grid positioning, Speed-based action slots, Two-Work-Type containment laws, and Grade 1–5 Workshop crafting derived strictly from <a href="../../GAME_BATTLE/" style="color: var(--somnarak-cyan); font-weight: bold;">GAME_BATTLE</a> and <a href="../../SOMNARAK-WORLD/" style="color: var(--somnarak-cyan); font-weight: bold;">SOMNARAK-WORLD</a>.
      </p>"""

assert old_sec4 in html, "Could not find old sec4 in docs/game-wiki/index.html"
html = html.replace(old_sec4, new_sec4)

with open("docs/game-wiki/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated docs/game-wiki/index.html successfully.")
