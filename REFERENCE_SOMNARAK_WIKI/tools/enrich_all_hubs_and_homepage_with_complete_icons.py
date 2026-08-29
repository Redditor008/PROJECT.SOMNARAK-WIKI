import os
import re

def enrich_homepage_and_all_hubs():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    assets_dir = os.path.join(wiki_root, "assets")

    # =========================================================================
    # 1. UPGRADE HOMEPAGE CATEGORIZED DIRECTORY WITH ICONS & CANONICAL NAMES
    # =========================================================================
    homepage_directory_html = '''      <!-- Complete Encyclopedic Directory -->
      <section class="pm-section-block">
        <div class="section-title-bar">
          <h2>/// COMPREHENSIVE ARTICLE DIRECTORY</h2>
          <span class="title-sub">INDEX OF 166 CANONICAL ARTICLES ACROSS ALL NAMESPACES</span>
        </div>
        <div class="portal-category-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(340px, 1fr)); gap:20px; margin-top:1.5rem;">
          
          <!-- Box 1: Sorrow Entities -->
          <div class="portal-cat-box" style="background:#090e17; border:1.5px solid #ef5b55; border-radius:6px; padding:18px;">
            <h4 style="display:flex; align-items:center; gap:10px; color:#ef5b55; font-family:'JetBrains Mono', monospace; font-size:1.1rem; margin:0 0 14px; border-bottom:1px solid rgba(239,91,85,0.3); padding-bottom:8px;">
              <img src="assets/icons/nav_entities.svg" alt="" style="width:28px; height:28px; vertical-align:middle;"> 
              Sorrow Entities (SE-xxx)
            </h4>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px;">
              <li><a href="entities/se-001-weeping-colossus.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-001.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #ef5b55;"> <span style="color:#ef5b55; font-weight:bold;">SE-001</span> Weeping Colossus <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">PHANTASM</span></a></li>
              <li><a href="entities/se-003-thread-of-memory.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-003.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #38bdf8;"> <span style="color:#38bdf8; font-weight:bold;">SE-003</span> Thread of Memory <span class="badge badge-somna" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">SOMNA</span></a></li>
              <li><a href="entities/se-004-obsidian-mirror.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-004.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #f1df76;"> <span style="color:#f1df76; font-weight:bold;">SE-004</span> Obsidian Mirror <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">MORPHEAN</span></a></li>
              <li><a href="entities/se-006-clockwork-heart.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-006.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #f1df76;"> <span style="color:#f1df76; font-weight:bold;">SE-006</span> Clockwork Heart <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">MORPHEAN</span></a></li>
              <li><a href="entities/se-007-ashen-scribe.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-007.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #38bdf8;"> <span style="color:#38bdf8; font-weight:bold;">SE-007</span> Ashen Scribe <span class="badge badge-somna" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">SOMNA</span></a></li>
              <li><a href="entities/se-008-forgotten-cradle.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-008.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #71efaf;"> <span style="color:#71efaf; font-weight:bold;">SE-008</span> Forgotten Cradle <span class="badge badge-green" style="font-size:0.65rem; margin-left:auto; padding:2px 6px; background:#064e3b; color:#71efaf; border:1px solid #71efaf;">AETHER</span></a></li>
              <li><a href="entities/se-009-drowned-bell.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-009.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #38bdf8;"> <span style="color:#38bdf8; font-weight:bold;">SE-009</span> Drowned Bell <span class="badge badge-somna" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">SOMNA</span></a></li>
              <li><a href="entities/se-011-iron-maiden-of-regret.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-011.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #ef5b55;"> <span style="color:#ef5b55; font-weight:bold;">SE-011</span> Iron Maiden <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">PHANTASM</span></a></li>
              <li><a href="entities/se-014-hollow-singer.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-014.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #c084fc;"> <span style="color:#c084fc; font-weight:bold;">SE-014</span> Hollow Singer <span class="badge" style="font-size:0.65rem; margin-left:auto; padding:2px 6px; background:#4c1d95; color:#e9d5ff; border:1px solid #c084fc;">APOCRYPHA</span></a></li>
              <li><a href="entities/se-015-sovereign-crown.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/se-015.svg" alt="" style="width:22px; height:22px; border-radius:3px; border:1px solid #f1df76;"> <span style="color:#f1df76; font-weight:bold;">SE-015</span> Sovereign Crown <span class="badge" style="font-size:0.65rem; margin-left:auto; padding:2px 6px; background:#4c1d95; color:#e9d5ff; border:1px solid #c084fc;">APOCRYPHA</span></a></li>
            </ul>
          </div>

          <!-- Box 2: M.A.W. Equipment -->
          <div class="portal-cat-box" style="background:#090e17; border:1.5px solid #f1df76; border-radius:6px; padding:18px;">
            <h4 style="display:flex; align-items:center; gap:10px; color:#f1df76; font-family:'JetBrains Mono', monospace; font-size:1.1rem; margin:0 0 14px; border-bottom:1px solid rgba(241,223,118,0.3); padding-bottom:8px;">
              <img src="assets/icons/tool.svg" alt="" style="width:28px; height:28px; vertical-align:middle;"> 
              M.A.W. Equipment Armory
            </h4>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px;">
              <li><a href="maw/maw-w-001-weeping-cleaver.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/tool.svg" alt="" style="width:20px; height:20px;"> Weeping Cleaver <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">WEAPON</span></a></li>
              <li><a href="maw/maw-w-003-thread-spindle.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/tool.svg" alt="" style="width:20px; height:20px;"> Memory Spindle <span class="badge badge-somna" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">WEAPON</span></a></li>
              <li><a href="maw/maw-w-015-sovereign-scepter.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/tool.svg" alt="" style="width:20px; height:20px;"> Sovereign Scepter <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">WEAPON</span></a></li>
              <li><a href="maw/maw-s-001-weeping-plate.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/suit.svg" alt="" style="width:20px; height:20px;"> Weeping Plate <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">SUIT</span></a></li>
              <li><a href="maw/maw-s-003-memory-veil.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/suit.svg" alt="" style="width:20px; height:20px;"> Memory Shroud <span class="badge badge-somna" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">SUIT</span></a></li>
              <li><a href="maw/maw-s-015-sovereign-regalia.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/suit.svg" alt="" style="width:20px; height:20px;"> Sovereign Regalia <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">SUIT</span></a></li>
              <li><a href="maw/maw-g-001-weeping-tear.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/gift.svg" alt="" style="width:20px; height:20px;"> Colossus Tear <span class="badge" style="font-size:0.65rem; margin-left:auto; padding:2px 6px; background:#3b0764; color:#c084fc; border:1px solid #c084fc;">GIFT</span></a></li>
              <li><a href="maw/maw-g-015-sovereign-halo.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/gift.svg" alt="" style="width:20px; height:20px;"> Sovereign Halo <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">GIFT</span></a></li>
              <li style="margin-top:6px; border-top:1px dashed rgba(241,223,118,0.2); padding-top:6px;"><a href="maw/index.html" style="color:#f1df76; font-size:0.85rem; font-weight:bold; text-decoration:none;">View All 27 M.A.W. Equipment Dossiers →</a></li>
            </ul>
          </div>

          <!-- Box 3: Key Personnel & Echo-Cores -->
          <div class="portal-cat-box" style="background:#090e17; border:1.5px solid #38bdf8; border-radius:6px; padding:18px;">
            <h4 style="display:flex; align-items:center; gap:10px; color:#38bdf8; font-family:'JetBrains Mono', monospace; font-size:1.1rem; margin:0 0 14px; border-bottom:1px solid rgba(56,189,248,0.3); padding-bottom:8px;">
              <img src="assets/icons/nav_characters.svg" alt="" style="width:28px; height:28px; vertical-align:middle;"> 
              Personnel & Echo-Cores
            </h4>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px;">
              <li><a href="characters/the-director-majin.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_majin.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #f1df76;"> Director Majin <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">DIRECTOR</span></a></li>
              <li><a href="characters/the-containment-lead-dekan.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_dekan.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #ef5b55;"> Lead Dekan <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">CONTAIN</span></a></li>
              <li><a href="characters/the-extraction-lead-zyrak.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_zyrak.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #38bdf8;"> Lead Zyrak <span class="badge badge-somna" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">EXTRACT</span></a></li>
              <li><a href="characters/the-research-lead-ayshuk.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_ayshuk.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #f1df76;"> Lead Ayshuk <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">RESEARCH</span></a></li>
              <li><a href="characters/the-border-lead-mellda.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_mellda.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #ef5b55;"> Lead Mellda <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">BORDER</span></a></li>
              <li><a href="characters/the-archive-lead-marjuk.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_marjuk.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #c084fc;"> Lead Marjuk <span class="badge" style="font-size:0.65rem; margin-left:auto; padding:2px 6px; background:#4c1d95; color:#e9d5ff; border:1px solid #c084fc;">ARCHIVE</span></a></li>
              <li><a href="characters/the-outsider-ishall.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_ishall.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #ef5b55;"> Lead Ishall <span class="badge badge-crimson" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">STRIKE</span></a></li>
              <li><a href="characters/the-exile-xyan.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/avatars/avatar_core_xyan.svg" alt="" style="width:22px; height:22px; border-radius:50%; border:1px solid #f1df76;"> Lead Xyan <span class="badge badge-gold" style="font-size:0.65rem; margin-left:auto; padding:2px 6px;">GATE</span></a></li>
              <li style="margin-top:6px; border-top:1px dashed rgba(56,189,248,0.2); padding-top:6px;"><a href="characters/index.html" style="color:#38bdf8; font-size:0.85rem; font-weight:bold; text-decoration:none;">View All 19 Personnel & Operative Files →</a></li>
            </ul>
          </div>

          <!-- Box 4: Lore & Cosmology -->
          <div class="portal-cat-box" style="background:#090e17; border:1.5px solid #71efaf; border-radius:6px; padding:18px;">
            <h4 style="display:flex; align-items:center; gap:10px; color:#71efaf; font-family:'JetBrains Mono', monospace; font-size:1.1rem; margin:0 0 14px; border-bottom:1px solid rgba(113,239,175,0.3); padding-bottom:8px;">
              <img src="assets/icons/nav_lore.svg" alt="" style="width:28px; height:28px; vertical-align:middle;"> 
              Lore & Chronicles
            </h4>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px;">
              <li><a href="lore/the-alpha-tree.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/icon_zone_a_core.svg" alt="" style="width:20px; height:20px;"> The Alpha Tree & Metropolitan Axis</a></li>
              <li><a href="lore/the-three-sorrows.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/damage_mixed.svg" alt="" style="width:20px; height:20px;"> The Three Sorrows (Dohan, Oehan, Naehan)</a></li>
              <li><a href="lore/the-cycle-and-absolvohan.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/damage_hope.svg" alt="" style="width:20px; height:20px;"> The Absolvohan Seed of Dawn</a></li>
              <li><a href="lore/the-seven-absolute-taboos.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/taboo.svg" alt="" style="width:20px; height:20px;"> The Seven Absolute Taboos of Somnarak</a></li>
              <li><a href="lore/the-cheongula-incident.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/fracture.svg" alt="" style="width:20px; height:20px;"> The Cheongula Collapse Incident</a></li>
              <li><a href="lore/the-doorspeech.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/hud_resonance_wave.svg" alt="" style="width:20px; height:20px;"> The Doorspeech Frequency Phenomenon</a></li>
              <li><a href="lore/efflorescence-and-fracture.html" style="display:flex; align-items:center; gap:8px; color:#cbd5e1; text-decoration:none; font-size:0.88rem;"><img src="assets/icons/resonance.svg" alt="" style="width:20px; height:20px;"> Efflorescence & Han Petrification</a></li>
              <li style="margin-top:6px; border-top:1px dashed rgba(113,239,175,0.2); padding-top:6px;"><a href="lore/index.html" style="color:#71efaf; font-size:0.85rem; font-weight:bold; text-decoration:none;">View All 24 Lore Chronicles & Codexes →</a></li>
            </ul>
          </div>
        </div>
      </section>'''

    index_path = os.path.join(wiki_root, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        index_html = f.read()

    # Replace the Directory section
    dir_pattern = re.compile(r'<section class="pm-section-block">\s*<div class="section-title-bar">\s*<h2>/// COMPREHENSIVE ARTICLE DIRECTORY</h2>.*?</div>\s*</section>', re.DOTALL)
    if dir_pattern.search(index_html):
        index_html = dir_pattern.sub(homepage_directory_html, index_html, count=1)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_html)
        print("Updated homepage categorized directory with rich icons and canonical links!")

    # =========================================================================
    # 2. ENRICH ALL 8 HUB INDEX PAGES WITH RICH ICON-ENRICHED CARDS
    # =========================================================================
    
    # 2A. ENTITIES HUB (entities/index.html)
    canonical_entities_grid = '''<div class="hub-grid-3" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px; margin-top:1.5rem;">
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
      <a href="se-001-weeping-colossus.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN DOSSIER & ASSETS →</a>
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
      <a href="se-003-thread-of-memory.html" class="jump-btn" style="display:block; text-align:center; background:#0c4a6e; color:#bae6fd; border:1px solid #38bdf8; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN DOSSIER & ASSETS →</a>
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
      <a href="se-004-obsidian-mirror.html" class="jump-btn" style="display:block; text-align:center; background:#3b0764; color:#e9d5ff; border:1px solid #c084fc; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN DOSSIER & ASSETS →</a>
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
      <a href="se-006-clockwork-heart.html" class="jump-btn" style="display:block; text-align:center; background:#451a03; color:#fef08a; border:1px solid #f1df76; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN DOSSIER & ASSETS →</a>
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
      <a href="se-007-ashen-scribe.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN DOSSIER & ASSETS →</a>
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
      <a href="se-008-forgotten-cradle.html" class="jump-btn" style="display:block; text-align:center; background:#064e3b; color:#a7f3d0; border:1px solid #71efaf; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN DOSSIER & ASSETS →</a>
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
      <a href="se-009-drowned-bell.html" class="jump-btn" style="display:block; text-align:center; background:#0e7490; color:#cffafe; border:1px solid #38bdf8; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN DOSSIER & ASSETS →</a>
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
      <a href="se-011-iron-maiden-of-regret.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN DOSSIER & ASSETS →</a>
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
      <a href="se-014-hollow-singer.html" class="jump-btn" style="display:block; text-align:center; background:#3b0764; color:#e9d5ff; border:1px solid #c084fc; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN DOSSIER & ASSETS →</a>
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
      <a href="se-015-sovereign-crown.html" class="jump-btn" style="display:block; text-align:center; background:#451a03; color:#fef08a; border:1px solid #f1df76; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">OPEN DOSSIER & ASSETS →</a>
    </div>
  </div>'''

    entities_index_path = os.path.join(wiki_root, "entities/index.html")
    with open(entities_index_path, "r", encoding="utf-8") as f:
        ent_html = f.read()

    ent_grid_pattern = re.compile(r'<div class="hub-grid-3">.*?</div>\s*</div>\s*</main>', re.DOTALL)
    if ent_grid_pattern.search(ent_html):
        ent_html = ent_grid_pattern.sub(f'{canonical_entities_grid}\n</div>\n</main>', ent_html, count=1)
        with open(entities_index_path, "w", encoding="utf-8") as f:
            f.write(ent_html)
        print("Updated entities/index.html with all 10 canonical Sorrow Entities!")

    # 2B. FACTIONS HUB (factions/index.html)
    factions_grid_html = '''<div class="hub-grid-3" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px; margin-top:1.5rem;">
    <!-- Reverie Directorate -->
    <div class="pm-entity-card" style="border:2px solid #71efaf; background:#04140d; padding:18px; border-radius:6px;">
      <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <img src="../assets/icons/fac_rd.svg" alt="Directorate" style="width:64px; height:64px; border:2px solid #71efaf; border-radius:6px; background:#02140d;">
        <span class="badge" style="background:#064e3b; color:#71efaf; border:1px solid #71efaf;">OVERSEER</span>
      </div>
      <h3 style="color:#71efaf; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">REVERIE DIRECTORATE</h3>
      <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">The sovereign administration governing Facility 01 (The Hand of Change) and coordinating all 8 subterranean floors under Director Majin.</p>
      <a href="the-reverie-directorate.html" class="jump-btn" style="display:block; text-align:center; background:#064e3b; color:#a7f3d0; border:1px solid #71efaf; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">VIEW FACTION DOSSIER →</a>
    </div>

    <!-- High Council -->
    <div class="pm-entity-card" style="border:2px solid #f1df76; background:#1c1402; padding:18px; border-radius:6px;">
      <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <img src="../assets/icons/fac_council.svg" alt="Council" style="width:64px; height:64px; border:2px solid #f1df76; border-radius:6px; background:#1c1402;">
        <span class="badge badge-gold">GOVERNANCE</span>
      </div>
      <h3 style="color:#f1df76; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">HIGH COUNCIL OF SOMNARAK</h3>
      <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">The metropolitan legislative body managing civil law, Han-energy tariffs, and social order across Zones A through E.</p>
      <a href="the-city-council.html" class="jump-btn" style="display:block; text-align:center; background:#451a03; color:#fef08a; border:1px solid #f1df76; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">VIEW FACTION DOSSIER →</a>
    </div>

    <!-- Keepers of Sorrow -->
    <div class="pm-entity-card" style="border:2px solid #ef5b55; background:#1f0608; padding:18px; border-radius:6px;">
      <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <img src="../assets/icons/fac_keepers.svg" alt="Keepers" style="width:64px; height:64px; border:2px solid #ef5b55; border-radius:6px; background:#1f0608;">
        <span class="badge badge-crimson">ZEALOT GUILD</span>
      </div>
      <h3 style="color:#ef5b55; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">KEEPERS OF SORROW</h3>
      <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Fanatical religious order revering the Weeping as divine transformation, resisting facility extraction in the outer zones.</p>
      <a href="the-keepers-of-sorrow.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">VIEW FACTION DOSSIER →</a>
    </div>

    <!-- High Architects -->
    <div class="pm-entity-card" style="border:2px solid #f1df76; background:#1c1402; padding:18px; border-radius:6px;">
      <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <img src="../assets/icons/fac_architects.svg" alt="Architects" style="width:64px; height:64px; border:2px solid #f1df76; border-radius:6px; background:#1c1402;">
        <span class="badge badge-gold">INNER RING</span>
      </div>
      <h3 style="color:#f1df76; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">HIGH ARCHITECTS</h3>
      <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Master builders and urban planners constructing the Han-stabilized foundations and monumental spires of Zone A.</p>
      <a href="the-high-architects.html" class="jump-btn" style="display:block; text-align:center; background:#451a03; color:#fef08a; border:1px solid #f1df76; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">VIEW FACTION DOSSIER →</a>
    </div>

    <!-- Weavers of Sorrow -->
    <div class="pm-entity-card" style="border:2px solid #38bdf8; background:#031526; padding:18px; border-radius:6px;">
      <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <img src="../assets/icons/fac_weavers.svg" alt="Weavers" style="width:64px; height:64px; border:2px solid #38bdf8; border-radius:6px; background:#031526;">
        <span class="badge badge-somna">ARTISAN GUILD</span>
      </div>
      <h3 style="color:#38bdf8; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">WEAVERS OF SORROW</h3>
      <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Artisan guild spinning Han-flux into psychically reinforced memory fabric and protective M.A.W. suit linings.</p>
      <a href="the-weavers-of-sorrow.html" class="jump-btn" style="display:block; text-align:center; background:#0c4a6e; color:#bae6fd; border:1px solid #38bdf8; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">VIEW FACTION DOSSIER →</a>
    </div>

    <!-- Underworld Syndicates -->
    <div class="pm-entity-card" style="border:2px solid #ef5b55; background:#140205; padding:18px; border-radius:6px;">
      <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <img src="../assets/icons/fac_underworld.svg" alt="Syndicates" style="width:64px; height:64px; border:2px solid #ef5b55; border-radius:6px; background:#140205;">
        <span class="badge badge-crimson">BLACK MARKET</span>
      </div>
      <h3 style="color:#ef5b55; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">UNDERWORLD SYNDICATES</h3>
      <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Covert criminal syndicates trafficking contraband Han-flux, unrefined sorrow crystals, and black-market M.A.W. gifts in Zone D.</p>
      <a href="the-underworld-syndicates.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">VIEW FACTION DOSSIER →</a>
    </div>
  </div>'''

    factions_index_path = os.path.join(wiki_root, "factions/index.html")
    with open(factions_index_path, "r", encoding="utf-8") as f:
        fac_html = f.read()

    fac_grid_pattern = re.compile(r'<div class="hub-grid-3">.*?</div>\s*</div>\s*</main>', re.DOTALL)
    if fac_grid_pattern.search(fac_html):
        fac_html = fac_grid_pattern.sub(f'{factions_grid_html}\n</div>\n</main>', fac_html, count=1)
        with open(factions_index_path, "w", encoding="utf-8") as f:
            f.write(fac_html)
        print("Updated factions/index.html with rich heraldic cards!")

    # 2C. LOCATIONS HUB (locations/index.html)
    locations_grid_html = '''<div class="hub-grid-3" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px; margin-top:1.5rem;">
    <!-- Zone A -->
    <div class="pm-entity-card" style="border:2px solid #71efaf; background:#04140d; padding:18px; border-radius:6px;">
      <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <img src="../assets/icons/icon_zone_a_core.svg" alt="Zone A" style="width:64px; height:64px; border:2px solid #71efaf; border-radius:6px; background:#02140d;">
        <span class="badge" style="background:#064e3b; color:#71efaf; border:1px solid #71efaf;">METROPOLITAN AXIS</span>
      </div>
      <h3 style="color:#71efaf; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">ZONE A // SOVEREIGN CORE</h3>
      <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">The central pinnacle district housing the Alpha Tree Spire, Reverie Directorate Headquarters, and High Council Chambers.</p>
      <a href="zone-a-core-nexus.html" class="jump-btn" style="display:block; text-align:center; background:#064e3b; color:#a7f3d0; border:1px solid #71efaf; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">VIEW ATLAS ENTRY →</a>
    </div>

    <!-- Zone B -->
    <div class="pm-entity-card" style="border:2px solid #f1df76; background:#1c1402; padding:18px; border-radius:6px;">
      <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <img src="../assets/icons/icon_zone_b_rings.svg" alt="Zone B" style="width:64px; height:64px; border:2px solid #f1df76; border-radius:6px; background:#1c1402;">
        <span class="badge badge-gold">COMMERCIAL</span>
      </div>
      <h3 style="color:#f1df76; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">ZONE B // GILDED RINGS</h3>
      <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Concentric rings of brass avenues, merchant houses, trading guilds, and the civil bureaucracy of Somnarak.</p>
      <a href="zone-b-west-ward.html" class="jump-btn" style="display:block; text-align:center; background:#451a03; color:#fef08a; border:1px solid #f1df76; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">VIEW ATLAS ENTRY →</a>
    </div>

    <!-- Zone C -->
    <div class="pm-entity-card" style="border:2px solid #ef5b55; background:#1f0608; padding:18px; border-radius:6px;">
      <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <img src="../assets/icons/icon_zone_c_foundry.svg" alt="Zone C" style="width:64px; height:64px; border:2px solid #ef5b55; border-radius:6px; background:#1f0608;">
        <span class="badge badge-crimson">HEAVY FOUNDRY</span>
      </div>
      <h3 style="color:#ef5b55; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">ZONE C // THE FOUNDRY</h3>
      <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Industrial refinery sector processing raw Han effluents into crystal power batteries and structural materials.</p>
      <a href="zone-c-east-foundry.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">VIEW ATLAS ENTRY →</a>
    </div>

    <!-- Zone D -->
    <div class="pm-entity-card" style="border:2px solid #38bdf8; background:#031526; padding:18px; border-radius:6px;">
      <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <img src="../assets/icons/icon_zone_d_outskirts.svg" alt="Zone D" style="width:64px; height:64px; border:2px solid #38bdf8; border-radius:6px; background:#031526;">
        <span class="badge badge-somna">SUNKEN DISTRICT</span>
      </div>
      <h3 style="color:#38bdf8; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">ZONE D // SUNKEN RESIDENTIAL</h3>
      <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Flooded residential warrens and subterranean markets bordering the Weeping drainage canal systems.</p>
      <a href="zone-d-south-canals.html" class="jump-btn" style="display:block; text-align:center; background:#0c4a6e; color:#bae6fd; border:1px solid #38bdf8; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">VIEW ATLAS ENTRY →</a>
    </div>

    <!-- Zone E -->
    <div class="pm-entity-card" style="border:2px solid #ef5b55; background:#1c0709; padding:18px; border-radius:6px;">
      <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <img src="../assets/icons/icon_zone_e_bulwark.svg" alt="Zone E" style="width:64px; height:64px; border:2px solid #ef5b55; border-radius:6px; background:#1c0709;">
        <span class="badge badge-crimson">PERIMETER BASTION</span>
      </div>
      <h3 style="color:#ef5b55; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">ZONE E // FRONTIER BULWARK</h3>
      <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">Heavy perimeter defensive walls, searchlight watchtowers, and sentry batteries holding back the Desolate.</p>
      <a href="zone-e-frontier-bulwark.html" class="jump-btn" style="display:block; text-align:center; background:#450a0a; color:#fca5a5; border:1px solid #ef5b55; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">VIEW ATLAS ENTRY →</a>
    </div>

    <!-- The Maw -->
    <div class="pm-entity-card" style="border:2px solid #c084fc; background:#130421; padding:18px; border-radius:6px;">
      <div class="entity-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <img src="../assets/icons/icon_loc_the_maw.svg" alt="The Maw" style="width:64px; height:64px; border:2px solid #c084fc; border-radius:6px; background:#130421;">
        <span class="badge" style="background:#4c1d95; color:#e9d5ff; border:1px solid #c084fc;">ABYSSAL CHASM</span>
      </div>
      <h3 style="color:#c084fc; font-family:'JetBrains Mono', monospace; font-size:1.2rem; margin:6px 0;">THE MAW // DEEP CHASM</h3>
      <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.4; margin:6px 0 12px;">The cyclopean abyss dropping directly into the subterranean veil and the Cheongula tomb where raw Han flows wild.</p>
      <a href="the-maw.html" class="jump-btn" style="display:block; text-align:center; background:#3b0764; color:#e9d5ff; border:1px solid #c084fc; padding:8px 0; font-weight:bold; text-decoration:none; border-radius:3px;">VIEW ATLAS ENTRY →</a>
    </div>
  </div>'''

    loc_index_path = os.path.join(wiki_root, "locations/index.html")
    with open(loc_index_path, "r", encoding="utf-8") as f:
        loc_html = f.read()

    loc_grid_pattern = re.compile(r'<div class="hub-grid-3">.*?</div>\s*</div>\s*</main>', re.DOTALL)
    if loc_grid_pattern.search(loc_html):
        loc_html = loc_grid_pattern.sub(f'{locations_grid_html}\n</div>\n</main>', loc_html, count=1)
        with open(loc_index_path, "w", encoding="utf-8") as f:
            f.write(loc_html)
        print("Updated locations/index.html with rich district and location badges!")

if __name__ == "__main__":
    enrich_homepage_and_all_hubs()
