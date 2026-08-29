import os, sys, re, html

def get_base_template(title, category_label, category_href, rel_prefix, content_html, toc_items=None):
    toc_html = ""
    if toc_items:
        toc_links = "".join([f'<li><a href="#{item_id}">{item_title}</a></li>' for item_id, item_title in toc_items])
        toc_html = f'''
        <div class="toc" id="toc">
          <div class="toc-title">Contents</div>
          <ol>
            {toc_links}
          </ol>
        </div>
        '''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Somnarak Official Wiki</title>
  <link rel="stylesheet" href="{rel_prefix}assets/css/wiki.css">
  <link rel="icon" href="{rel_prefix}assets/icons/somnarak_icon.svg" type="image/svg+xml">
  <script defer src="{rel_prefix}assets/js/wiki.js"></script>
</head>
<body>
  <!-- Top Utility Bar -->
  <header class="utility">
    <div class="utility-left">
      <button aria-label="Open navigation" class="nav-open" type="button">☰</button>
      <a href="{rel_prefix}index.html" class="utility-brand">SOMNARAK.WIKI</a>
      <span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
    </div>
    <nav aria-label="Main navigation">
      <a href="{rel_prefix}index.html">Main page</a>
      <a href="{rel_prefix}characters/index.html">Characters</a>
      <a href="{rel_prefix}lore/index.html">Lore</a>
      <a href="{rel_prefix}locations/index.html">Atlas</a>
      <a href="{rel_prefix}factions/index.html">Factions</a>
      <a href="{rel_prefix}departments/index.html">Facility</a>
      <a href="{rel_prefix}entities/index.html">Entities</a>
      <a href="{rel_prefix}maw/index.html">M.A.W.</a>
      <a href="{rel_prefix}mechanics/index.html">Mechanics</a>
    </nav>
    <div class="search">
      <input autocomplete="off" id="search-input" placeholder="Search archive..." type="search">
      <div id="results"></div>
    </div>
  </header>

  <!-- Main Grid Layout -->
  <div class="wiki-shell">
    <!-- Left Rail -->
    <aside class="left-rail">
      <div class="site-mark">
        <a href="{rel_prefix}index.html">
          <img src="{rel_prefix}assets/icons/somnarak_icon.svg" alt="Somnarak Emblem">
          <b>SOMNARAK</b>
          <span>WIKI ARCHIVE</span>
        </a>
      </div>
      <nav aria-label="Wiki navigation" class="left-links">
        <section>
          <h2>Core Archive</h2>
          <a href="{rel_prefix}index.html">Main Overview</a>
          <a href="{rel_prefix}characters/index.html">Characters Hub</a>
          <a href="{rel_prefix}lore/index.html">Lore &amp; Cosmology</a>
          <a href="{rel_prefix}locations/index.html">Atlas &amp; Locations</a>
          <a href="{rel_prefix}factions/index.html">Factions &amp; Guilds</a>
          <a href="{rel_prefix}departments/index.html">Facility Floors</a>
          <a href="{rel_prefix}entities/index.html">Sorrow Entities</a>
          <a href="{rel_prefix}maw/index.html">M.A.W. Equipment</a>
          <a href="{rel_prefix}mechanics/index.html">Systems &amp; Mechanics</a>
        </section>
        <section>
          <h2>Facility Schematics</h2>
          <a href="{rel_prefix}atlas/hand-of-change-map.html">Hand of Change Map</a>
          <a href="{rel_prefix}atlas/somnarak-city-map.html">Somnarak City Blueprint</a>
          <a href="{rel_prefix}project/source-map.html">Master Archive Map</a>
        </section>
      </nav>
    </aside>

    <!-- Main Content Body -->
    <main id="content">
      <!-- Page Tabs -->
      <div class="page-tabs">
        <span>ARTICLE</span>
        <span>DISCUSSION</span>
        <span>SOURCE</span>
        <span>HISTORY</span>
        <b>YEAR 4,238 · DAWN OF HOPE</b>
      </div>

      <!-- Breadcrumbs -->
      <div class="breadcrumbs">
        <a href="{rel_prefix}index.html">Somnarak</a> <i>/</i>
        <a href="{rel_prefix}{category_href}">{category_label}</a> <i>/</i>
        <span>{title}</span>
      </div>

      <!-- Article Header -->
      <div class="article-header">
        <div class="article-eyebrow">{category_label.upper()} RECORD</div>
        <h1 class="article-title">{title}</h1>
        <div class="article-subbar">
          <span class="badge badge-canon">CANONICAL ARTIFACT</span>
          <span class="badge badge-source">SOURCE VERIFIED</span>
          <div class="article-actions">
            <span class="action-btn">History</span>
            <span class="action-btn">View Source</span>
          </div>
        </div>
      </div>

      {toc_html}

      {content_html}

      <!-- Page Footer -->
      <footer class="article-footer">
        <div class="footer-categories">
          <strong>Categories:</strong>
          <a href="{rel_prefix}{category_href}">{category_label}</a> |
          <a href="{rel_prefix}index.html">Somnarak Universe</a> |
          <a href="{rel_prefix}lore/index.html">Canon Lore</a>
        </div>
        <div class="footer-disclaimer">
          Content is available under Somnarak Directorate Archival License unless otherwise noted.
        </div>
      </footer>
    </main>
  </div>
</body>
</html>'''

print("Updated template loaded.")
