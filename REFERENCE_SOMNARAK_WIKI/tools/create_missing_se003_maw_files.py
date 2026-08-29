import os

wiki_root = '/home/user/01_Somnarak_Wiki'

# 1. Create SE-003 MAW files
w_html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>MAW-W-003-01: Memory Blade — Somnarak Directorate Wiki</title>
  <meta name="description" content="M.A.W. Weapon extracted from SE-003 (The Thread of Memory). Inflicts Lament damage.">
  <link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg">
  <link rel="stylesheet" href="../assets/css/wiki.css">
  <script defer src="../assets/js/wiki.js"></script>
</head>
<body>
  <header class="utility">
    <div class="utility-left">
      <button class="nav-open" type="button" aria-label="Open navigation">☰</button>
      <a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
      <span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
    </div>
    <nav aria-label="Main navigation">
      <a href="../index.html">Main page</a>
      <a href="../characters/index.html">Characters</a>
      <a href="../lore/index.html">Lore</a>
      <a href="../factions/index.html">Factions</a>
      <a href="../departments/index.html">Departments</a>
      <a href="../locations/index.html">Locations</a>
      <a href="../mechanics/index.html">Mechanics</a>
      <a href="../entities/index.html">Sorrow Entities</a>
      <a href="index.html" class="active">M.A.W.</a>
    </nav>
    <div class="search">
      <input id="search" data-index="../data/search.json" aria-label="Search" placeholder="Search Somnarak Wiki">
      <div id="results"></div>
    </div>
  </header>

  <div class="layout">
    <aside class="rail" aria-label="Site navigation">
      <div class="brand">
        <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak Crest" class="brand-logo" width="36" height="36">
        <div>
          <div class="brand-title">SOMNARAK</div>
          <div class="brand-sub">DIRECTORATE CODEX</div>
        </div>
      </div>
      <div class="nav-section">
        <div class="nav-section-title">CODEX DIRECTORY</div>
        <a href="../index.html">Main Portal</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="index.html" class="active">M.A.W. Armory</a>
        <a href="../departments/index.html">Facility 01 Floors</a>
        <a href="../characters/index.html">Echo-Cores &amp; Leads</a>
        <a href="../lore/index.html">Lore &amp; Cosmology</a>
        <a href="../locations/index.html">Metropolitan Atlas</a>
        <a href="../mechanics/index.html">Battle Mechanics</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
      </div>
    </aside>

    <main class="content">
      <div class="hero-banner" style="background: linear-gradient(135deg, rgba(8, 14, 26, 0.95), rgba(15, 23, 42, 0.9)), url('../assets/icons/banner_maw.svg') center/cover;">
        <div class="hero-badge">ARMAMENT CODEX // WEAPON MAW-W-003-01</div>
        <h1 class="hero-title" style="font-size:2.2rem; color:#f8fafc; font-family:'Cinzel', serif;">MAW-W-003-01: MEMORY BLADE</h1>
        <p class="hero-subtitle" style="color:#94a3b8; max-width:850px;">
          Filament rapier forged from azure memory threads of SE-003. Inflicts piercing Lament mental damage.
        </p>
      </div>

      <div class="article-body">
        <div class="table-wrap">
          <table class="data-table">
            <thead>
              <tr>
                <th>ATTRIBUTE</th>
                <th>SPECIFICATION</th>
              </tr>
            </thead>
            <tbody>
              <tr><td><b>DESIGNATION</b></td><td><code>MAW-W-003-01</code></td></tr>
              <tr><td><b>EQUIPMENT TYPE</b></td><td>M.A.W. Weapon (Filament Rapier)</td></tr>
              <tr><td><b>SOURCE ENTITY</b></td><td><a href="../entities/se-003-the-wilderness-tide.html" style="color:#38bdf8;">SE-003: The Thread of Memory</a></td></tr>
              <tr><td><b>DAMAGE TYPE</b></td><td><span class="damage-badge" style="color:#38bdf8; border-color:#38bdf8;">LAMENT (비탄)</span></td></tr>
              <tr><td><b>BASE DAMAGE</b></td><td>10 – 15 Mental Damage (Target: SP)</td></tr>
              <tr><td><b>ATTACK SPEED</b></td><td>Fast (1.2s per strike)</td></tr>
              <tr><td><b>SPECIAL EFFECT</b></td><td>Memory Sever: 15% chance to confuse the target for 3 seconds.</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <footer class="footer">
        <div class="footer-bottom">
          <span>PROJECT SOMNARAK ENCYCLOPEDIA · CANONICAL CODEX</span>
          <span>CYCLE 1,778 · YEAR 4,238</span>
        </div>
      </footer>
    </main>
  </div>
</body>
</html>
"""

s_html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>MAW-S-003-01: Tide Cloak — Somnarak Directorate Wiki</title>
  <meta name="description" content="M.A.W. Suit extracted from SE-003 (The Thread of Memory). High Lament resistance.">
  <link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg">
  <link rel="stylesheet" href="../assets/css/wiki.css">
  <script defer src="../assets/js/wiki.js"></script>
</head>
<body>
  <header class="utility">
    <div class="utility-left">
      <button class="nav-open" type="button" aria-label="Open navigation">☰</button>
      <a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
      <span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
    </div>
    <nav aria-label="Main navigation">
      <a href="../index.html">Main page</a>
      <a href="../characters/index.html">Characters</a>
      <a href="../lore/index.html">Lore</a>
      <a href="../factions/index.html">Factions</a>
      <a href="../departments/index.html">Departments</a>
      <a href="../locations/index.html">Locations</a>
      <a href="../mechanics/index.html">Mechanics</a>
      <a href="../entities/index.html">Sorrow Entities</a>
      <a href="index.html" class="active">M.A.W.</a>
    </nav>
    <div class="search">
      <input id="search" data-index="../data/search.json" aria-label="Search" placeholder="Search Somnarak Wiki">
      <div id="results"></div>
    </div>
  </header>

  <div class="layout">
    <aside class="rail" aria-label="Site navigation">
      <div class="brand">
        <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak Crest" class="brand-logo" width="36" height="36">
        <div>
          <div class="brand-title">SOMNARAK</div>
          <div class="brand-sub">DIRECTORATE CODEX</div>
        </div>
      </div>
      <div class="nav-section">
        <div class="nav-section-title">CODEX DIRECTORY</div>
        <a href="../index.html">Main Portal</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="index.html" class="active">M.A.W. Armory</a>
        <a href="../departments/index.html">Facility 01 Floors</a>
        <a href="../characters/index.html">Echo-Cores &amp; Leads</a>
        <a href="../lore/index.html">Lore &amp; Cosmology</a>
        <a href="../locations/index.html">Metropolitan Atlas</a>
        <a href="../mechanics/index.html">Battle Mechanics</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
      </div>
    </aside>

    <main class="content">
      <div class="hero-banner" style="background: linear-gradient(135deg, rgba(8, 14, 26, 0.95), rgba(15, 23, 42, 0.9)), url('../assets/icons/banner_maw.svg') center/cover;">
        <div class="hero-badge">ARMAMENT CODEX // SUIT MAW-S-003-01</div>
        <h1 class="hero-title" style="font-size:2.2rem; color:#f8fafc; font-family:'Cinzel', serif;">MAW-S-003-01: TIDE CLOAK</h1>
        <p class="hero-subtitle" style="color:#94a3b8; max-width:850px;">
          Woven silk cloak crafted from the nostalgic threads of SE-003. Deflects psychic trauma.
        </p>
      </div>

      <div class="article-body">
        <div class="table-wrap">
          <table class="data-table">
            <thead>
              <tr>
                <th>ATTRIBUTE</th>
                <th>SPECIFICATION</th>
              </tr>
            </thead>
            <tbody>
              <tr><td><b>DESIGNATION</b></td><td><code>MAW-S-003-01</code></td></tr>
              <tr><td><b>EQUIPMENT TYPE</b></td><td>M.A.W. Suit (Woven Silk Cloak)</td></tr>
              <tr><td><b>SOURCE ENTITY</b></td><td><a href="../entities/se-003-the-wilderness-tide.html" style="color:#38bdf8;">SE-003: The Thread of Memory</a></td></tr>
              <tr><td><b>RESISTANCE PROFILE</b></td><td>Grudge: 1.0 · Lament: <b>0.7</b> · Void: <b>0.8</b> · Weight: 1.2</td></tr>
              <tr><td><b>REQUIREMENTS</b></td><td>Prudence Level II, Temperance Level I</td></tr>
              <tr><td><b>SPECIAL EFFECT</b></td><td>Amnestic Barrier: Reduces SP damage from all psychic screams by 20%.</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <footer class="footer">
        <div class="footer-bottom">
          <span>PROJECT SOMNARAK ENCYCLOPEDIA · CANONICAL CODEX</span>
          <span>CYCLE 1,778 · YEAR 4,238</span>
        </div>
      </footer>
    </main>
  </div>
</body>
</html>
"""

g_html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>MAW-G-003-01: Memory Thread Needle — Somnarak Directorate Wiki</title>
  <meta name="description" content="M.A.W. Gift bestowed by SE-003 (The Thread of Memory).">
  <link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg">
  <link rel="stylesheet" href="../assets/css/wiki.css">
  <script defer src="../assets/js/wiki.js"></script>
</head>
<body>
  <header class="utility">
    <div class="utility-left">
      <button class="nav-open" type="button" aria-label="Open navigation">☰</button>
      <a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
      <span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
    </div>
    <nav aria-label="Main navigation">
      <a href="../index.html">Main page</a>
      <a href="../characters/index.html">Characters</a>
      <a href="../lore/index.html">Lore</a>
      <a href="../factions/index.html">Factions</a>
      <a href="../departments/index.html">Departments</a>
      <a href="../locations/index.html">Locations</a>
      <a href="../mechanics/index.html">Mechanics</a>
      <a href="../entities/index.html">Sorrow Entities</a>
      <a href="index.html" class="active">M.A.W.</a>
    </nav>
    <div class="search">
      <input id="search" data-index="../data/search.json" aria-label="Search" placeholder="Search Somnarak Wiki">
      <div id="results"></div>
    </div>
  </header>

  <div class="layout">
    <aside class="rail" aria-label="Site navigation">
      <div class="brand">
        <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak Crest" class="brand-logo" width="36" height="36">
        <div>
          <div class="brand-title">SOMNARAK</div>
          <div class="brand-sub">DIRECTORATE CODEX</div>
        </div>
      </div>
      <div class="nav-section">
        <div class="nav-section-title">CODEX DIRECTORY</div>
        <a href="../index.html">Main Portal</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="index.html" class="active">M.A.W. Armory</a>
        <a href="../departments/index.html">Facility 01 Floors</a>
        <a href="../characters/index.html">Echo-Cores &amp; Leads</a>
        <a href="../lore/index.html">Lore &amp; Cosmology</a>
        <a href="../locations/index.html">Metropolitan Atlas</a>
        <a href="../mechanics/index.html">Battle Mechanics</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
      </div>
    </aside>

    <main class="content">
      <div class="hero-banner" style="background: linear-gradient(135deg, rgba(8, 14, 26, 0.95), rgba(15, 23, 42, 0.9)), url('../assets/icons/banner_maw.svg') center/cover;">
        <div class="hero-badge">ARMAMENT CODEX // GIFT MAW-G-003-01</div>
        <h1 class="hero-title" style="font-size:2.2rem; color:#f8fafc; font-family:'Cinzel', serif;">MAW-G-003-01: MEMORY THREAD NEEDLE</h1>
        <p class="hero-subtitle" style="color:#94a3b8; max-width:850px;">
          Gilded hair needle manifested from continuous communion with SE-003. Accelerates work efficiency.
        </p>
      </div>

      <div class="article-body">
        <div class="table-wrap">
          <table class="data-table">
            <thead>
              <tr>
                <th>ATTRIBUTE</th>
                <th>SPECIFICATION</th>
              </tr>
            </thead>
            <tbody>
              <tr><td><b>DESIGNATION</b></td><td><code>MAW-G-003-01</code></td></tr>
              <tr><td><b>EQUIPMENT TYPE</b></td><td>M.A.W. Gift (Hair Accessory / Needle)</td></tr>
              <tr><td><b>SOURCE ENTITY</b></td><td><a href="../entities/se-003-the-wilderness-tide.html" style="color:#38bdf8;">SE-003: The Thread of Memory</a></td></tr>
              <tr><td><b>EQUIP SLOT</b></td><td>Head / Hair</td></tr>
              <tr><td><b>STAT BONUSES</b></td><td>+4 Max SP, +5% Work Speed</td></tr>
              <tr><td><b>SPECIAL EFFECT</b></td><td>Nostalgic Focus: +5% success rate on Insight Work.</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <footer class="footer">
        <div class="footer-bottom">
          <span>PROJECT SOMNARAK ENCYCLOPEDIA · CANONICAL CODEX</span>
          <span>CYCLE 1,778 · YEAR 4,238</span>
        </div>
      </footer>
    </main>
  </div>
</body>
</html>
"""

with open(f'{wiki_root}/maw/maw-w-003-01-memory-blade.html', 'w', encoding='utf-8') as f:
    f.write(w_html)
with open(f'{wiki_root}/maw/maw-s-003-01-tide-cloak.html', 'w', encoding='utf-8') as f:
    f.write(s_html)
with open(f'{wiki_root}/maw/maw-g-003-01-memory-thread-needle.html', 'w', encoding='utf-8') as f:
    f.write(g_html)

print("Created SE-003 MAW files!")

# Fix rail links in entity-tales.html
with open(f'{wiki_root}/lore/entity-tales.html', 'r', encoding='utf-8') as f:
    t_html = f.read()

t_html = t_html.replace('timeline-1778-cycles.html', 'the-three-ages-and-history.html')
t_html = t_html.replace('the-seven-taboos.html', 'the-seven-absolute-taboos.html')

with open(f'{wiki_root}/lore/entity-tales.html', 'w', encoding='utf-8') as f:
    f.write(t_html)

print("Fixed rail links in entity-tales.html!")
