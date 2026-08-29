import os

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# Helper to wrap hub pages in standard master wiki shell
def generate_hub_page(rel_path, page_title, category_name, hero_title, hero_subtitle, hero_icon, breadcrumb_label, content_html):
    # Calculate depth
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

      <!-- Category Hero Banner -->
      <header class="category-hero">
        <div class="hero-left-art">
          <img src="{prefix}{hero_icon}" alt="{hero_title}" class="hero-icon-large">
        </div>
        <div class="hero-center-meta">
          <div class="hero-tag">[ CLASSIFIED DIRECTORATE DATABASE // PRIMARY INDEX ]</div>
          <h1 class="hero-title">{hero_title}</h1>
          <p class="hero-subtitle">{hero_subtitle}</p>
        </div>
      </header>

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
    print(f"Built Super Hub: {rel_path}")

print("Master Super Hub builder loaded.")
