import os, sys
sys.path.insert(0, '/home/user')
from tools.build_deep_canon_wiki import get_base_template

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# ==============================================================================
# 1. CHARACTERS HUB (characters/index.html)
# ==============================================================================
char_hub_html = '''
<div class="wiki-callout" style="border-left: 5px solid #f1df76; background: linear-gradient(135deg, #0d121c 0%, #06080d 100%);">
  <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
    <div>
      <span class="badge badge-canon" style="margin-bottom: 6px;">PERSONNEL CODEX</span>
      <h2 style="margin: 0; color: #f1df76; font-size: 1.6rem; font-family: Impact, sans-serif;">SOMNARAK CENTRAL PERSONNEL REGISTRY</h2>
      <p style="margin: 4px 0 0; color: #94a3b8; font-size: 0.88rem;">Official Directorate Personnel Roster · Hand of Change Operational Heads · Field Commanders</p>
    </div>
    <div style="display: flex; gap: 8px;">
      <span class="badge badge-source">9 ECHO-CORES</span>
      <span class="badge badge-source">6 FIELD LEADS</span>
      <span class="badge badge-source">53 NAMED CAST</span>
    </div>
  </div>
</div>

<section class="wiki-section" id="executive-echo-cores">
  <h2 class="section-title">The Nine Echo-Cores (에코 코어 — Eko Koeo)</h2>
  <p>The <strong>Nine Echo-Cores</strong> constitute the supreme governing and operational executive tier of the <a href="../factions/the-reverie-directorate.html" class="wiki-link">Reverie Directorate</a>. Stationed within the <a href="../atlas/hand-of-change-map.html" class="wiki-link">Hand of Change</a> beneath the <a href="../lore/the-alpha-tree.html" class="wiki-link">Alpha Tree</a>, each Echo-Core oversees a dedicated operational floor, anchoring reality against abyssal collapse across the 1,778 iterations of <a href="../lore/the-cycle-and-absolvohan.html" class="wiki-link">Absolvohan</a>.</p>
  
  <div class="table-wrap">
    <table class="wiki-table">
      <thead>
        <tr>
          <th>Core #</th>
          <th>Designation &amp; Name</th>
          <th>Korean / Hanja</th>
          <th>Assigned Floor</th>
          <th>Primary Mandate</th>
          <th>Signature M.A.W.</th>
          <th>Resonance Type</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Core 1</strong></td>
          <td><a href="the-director-majin.html" class="wiki-link"><img src="../assets/icons/somnarak_icon.svg" class="wiki-icon" alt=""> Director Majin</a></td>
          <td>마진 (魔鎭)</td>
          <td><a href="../departments/floor-1-neutral-command.html" class="wiki-link">Floor 1: Neutral Command</a></td>
          <td>Supreme Directorate Oversight &amp; Siphon Architecture</td>
          <td>Ω-Grade Fusion Matrix</td>
          <td><span class="badge badge-source">PALE / ABSOLUTE</span></td>
        </tr>
        <tr>
          <td><strong>Core 2</strong></td>
          <td><a href="the-secretary-seiyon.html" class="wiki-link"><img src="../assets/icons/floor-2-maw.svg" class="wiki-icon" alt=""> Seiyon</a></td>
          <td>세이연 (世理淵)</td>
          <td><a href="../departments/floor-2-maws-keep.html" class="wiki-link">Floor 2: Maw's Keep</a></td>
          <td>Central Archive Index &amp; Memory Preservation</td>
          <td>The Memory Shroud</td>
          <td><span class="badge badge-source">WHITE / MENTAL</span></td>
        </tr>
        <tr>
          <td><strong>Core 3</strong></td>
          <td><a href="the-containment-lead-dekan.html" class="wiki-link"><img src="../assets/icons/shield_hope.svg" class="wiki-icon" alt=""> Dekan</a></td>
          <td>데칸 (大關)</td>
          <td><a href="../departments/floor-2-maws-keep.html" class="wiki-link">Floor 2: Maw's Keep</a></td>
          <td>Sorrow Containment &amp; High-Density Ward</td>
          <td>The Bastion Aegis</td>
          <td><span class="badge badge-source">BLACK / HYBRID</span></td>
        </tr>
        <tr>
          <td><strong>Core 4</strong></td>
          <td><a href="the-extraction-lead-zyrak.html" class="wiki-link"><img src="../assets/icons/weapon.svg" class="wiki-icon" alt=""> Zyrak</a></td>
          <td>자이락 (紫鍛)</td>
          <td><a href="../departments/floor-3-extraction-hall.html" class="wiki-link">Floor 3: Extraction Hall</a></td>
          <td>M.A.W. Siphoning, Forge Master &amp; Armaments</td>
          <td>The Siphon Forge Hammer</td>
          <td><span class="badge badge-source">RED / PHYSICAL</span></td>
        </tr>
        <tr>
          <td><strong>Core 5</strong></td>
          <td><a href="the-research-lead-ayshuk.html" class="wiki-link"><img src="../assets/icons/clarity.svg" class="wiki-icon" alt=""> Ayshuk</a></td>
          <td>아이샥 (眼識)</td>
          <td><a href="../departments/floor-4-insight-forge.html" class="wiki-link">Floor 4: Insight Forge</a></td>
          <td>Han Kinetics, Anomaly Research &amp; Particle Physics</td>
          <td>The Insight Lens Array</td>
          <td><span class="badge badge-source">WHITE / COGNITIVE</span></td>
        </tr>
        <tr>
          <td><strong>Core 6</strong></td>
          <td><a href="the-border-lead-mellda.html" class="wiki-link"><img src="../assets/icons/veil.svg" class="wiki-icon" alt=""> Mellda</a></td>
          <td>멜다 (壁羅)</td>
          <td><a href="../departments/floor-5-border-watch.html" class="wiki-link">Floor 5: Border Watch</a></td>
          <td>Perimeter Acoustic Bastion &amp; Defense Grid</td>
          <td>The Acoustic Greatshield</td>
          <td><span class="badge badge-source">BLACK / EROSION</span></td>
        </tr>
        <tr>
          <td><strong>Core 7</strong></td>
          <td><a href="the-archive-lead-marjuk.html" class="wiki-link"><img src="../assets/icons/floor-6-vault.svg" class="wiki-icon" alt=""> Marjuk</a></td>
          <td>마르죽 (冥錄)</td>
          <td><a href="../departments/floor-6-deep-vault.html" class="wiki-link">Floor 6: Deep Vault</a></td>
          <td>Deep Vault, Cryo-Names &amp; Precursor Records</td>
          <td>The Ledger of 1.4 Million</td>
          <td><span class="badge badge-source">PALE / SOUL</span></td>
        </tr>
        <tr>
          <td><strong>Core 8</strong></td>
          <td><a href="the-outsider-ishall.html" class="wiki-link"><img src="../assets/icons/floor-7-shadow.svg" class="wiki-icon" alt=""> Ishall</a></td>
          <td>이샬 (異界)</td>
          <td><a href="../departments/floor-7-shadow-corps.html" class="wiki-link">Floor 7: Shadow Corps</a></td>
          <td>Desolate Reconnaissance &amp; Void Diving</td>
          <td>The Desolate Cloak</td>
          <td><span class="badge badge-source">BLACK / VOID</span></td>
        </tr>
        <tr>
          <td><strong>Core 9</strong></td>
          <td><a href="the-exile-xyan.html" class="wiki-link"><img src="../assets/icons/floor-8-gate.svg" class="wiki-icon" alt=""> Xyan</a></td>
          <td>시안 (始禁)</td>
          <td><a href="../departments/floor-8-gate-watch.html" class="wiki-link">Floor 8: Gate Watch</a></td>
          <td>The Forbidden Gate &amp; Taboo Resonance Seal</td>
          <td>The Key of Absolute Taboo</td>
          <td><span class="badge badge-source">PALE / PRIMORDIAL</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="wiki-section" id="field-operatives">
  <h2 class="section-title">Field Commanders &amp; Tactical Operatives</h2>
  <div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 16px; margin-top: 1rem;">
    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
        <img src="../assets/icons/nav_characters.svg" style="width: 44px; height: 44px;" alt="">
        <div>
          <a href="kael.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none;">KAEL (THE WANDERER)</a>
          <div style="font-size: 0.72rem; color: #38bdf8;">Resonant Pilgrim · Outskirts Survivor</div>
        </div>
      </div>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Survivor of the Cheongula quarantine who unlocked self-directed Han resonance without Directorate equipment. Wields raw kinetic vibration.</p>
      <a href="kael.html" class="action-btn" style="display: inline-block;">View Full Dossier →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
        <img src="../assets/icons/nav_characters.svg" style="width: 44px; height: 44px;" alt="">
        <div>
          <a href="soojin.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none;">SOOJIN (THE APPRENTICE)</a>
          <div style="font-size: 0.72rem; color: #38bdf8;">Fray Weaver · Memory Transcriber</div>
        </div>
      </div>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Former apprentice archivist turned independent stitcher of memory fabrics. Possesses unique immunity to psychic memory bleeds.</p>
      <a href="soojin.html" class="action-btn" style="display: inline-block;">View Full Dossier →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
        <img src="../assets/icons/ref_sed.svg" style="width: 44px; height: 44px;" alt="">
        <div>
          <a href="yeonhwa.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none;">LEAD YEONHWA</a>
          <div style="font-size: 0.72rem; color: #38bdf8;">SED Chief Field Cartographer</div>
        </div>
      </div>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Commander of 14 successful deep-range expeditions into The Desolate. Master of acoustic navigation and wasteland topography.</p>
      <a href="yeonhwa.html" class="action-btn" style="display: inline-block;">View Full Dossier →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
        <img src="../assets/icons/ref_ucd.svg" style="width: 44px; height: 44px;" alt="">
        <div>
          <a href="taeho.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none;">COMMANDER TAEHO</a>
          <div style="font-size: 0.72rem; color: #38bdf8;">UCD Strike Force Tactical Lead</div>
        </div>
      </div>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Veteran strike leader executing subterranean breach suppression against illegal entity trade syndicates across the Underworld.</p>
      <a href="taeho.html" class="action-btn" style="display: inline-block;">View Full Dossier →</a>
    </div>
  </div>
</section>

<section class="wiki-section" id="guild-leaders-refugees">
  <h2 class="section-title">Guild Masters &amp; Civilian Factions</h2>
  <div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 16px; margin-top: 1rem;">
    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="high-architects.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">THE HIGH ARCHITECTS</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">The master masonry guild responsible for designing the Spire towers, acoustic resonance chambers, and barrier foundations.</p>
      <a href="high-architects.html" class="action-btn">Read Guild Dossier →</a>
    </div>
    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="cheonbulok-refugees.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">CHEONBULOK REFUGEES</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">The survivor collective displaced by the ancient drowning of the precursor citadel, keeping alive oral histories and forgotten rituals.</p>
      <a href="cheonbulok-refugees.html" class="action-btn">Read Collective Dossier →</a>
    </div>
  </div>
</section>
'''

toc_char = [
    ("executive-echo-cores", "The Nine Echo-Cores (Executive Tier)"),
    ("field-operatives", "Field Commanders & Tactical Operatives"),
    ("guild-leaders-refugees", "Guild Masters & Civilian Factions")
]

p_char = get_base_template("Personnel & Characters Directory", "Characters", "characters/index.html", "../", char_hub_html, toc_char)
with open(os.path.join(WIKI_DIR, "characters/index.html"), 'w', encoding='utf-8') as f:
    f.write(p_char)
print("Built Super Hub: characters/index.html")

# ==============================================================================
# 2. LORE & WORLD HUB (lore/index.html)
# ==============================================================================
lore_hub_html = '''
<div class="wiki-callout" style="border-left: 5px solid #38bdf8; background: linear-gradient(135deg, #0d121c 0%, #06080d 100%);">
  <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
    <div>
      <span class="badge badge-canon" style="margin-bottom: 6px;">COSMOLOGY &amp; CHRONOLOGY</span>
      <h2 style="margin: 0; color: #38bdf8; font-size: 1.6rem; font-family: Impact, sans-serif;">SOMNARAK MASTER WORLD CODEX</h2>
      <p style="margin: 4px 0 0; color: #94a3b8; font-size: 0.88rem;">The Five Layers of Reality · Absolvohan Singularity · Han Physics &amp; Absolute Taboos</p>
    </div>
    <div style="display: flex; gap: 8px;">
      <span class="badge badge-source">1,778 CYCLES</span>
      <span class="badge badge-source">5 LAYERS</span>
      <span class="badge badge-source">7 TABOOS</span>
    </div>
  </div>
</div>

<section class="wiki-section" id="cosmological-foundations">
  <h2 class="section-title">Cosmological Framework &amp; The Five Layers</h2>
  <p>The universe of Somnarak operates under non-Euclidean metaphysical physics where human grief, regret, and sorrow (*Han* — 한) exert physical mass and crystalline pressure. Reality is partitioned into five distinct vertical strata:</p>
  
  <div class="table-wrap">
    <table class="wiki-table">
      <thead>
        <tr>
          <th>Layer Stratum</th>
          <th>Domain Name</th>
          <th>Physical &amp; Metaphysical Properties</th>
          <th>Primary Manifestations</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Layer 1</strong></td>
          <td><strong>The Celestial Canopy (Alpha Crown)</strong></td>
          <td>The towering upper branches of the Alpha Tree that filter primordial cosmic radiation.</td>
          <td>Living Sap, Chlorophyll filters, Upper Atmosphere Gates</td>
        </tr>
        <tr>
          <td><strong>Layer 2</strong></td>
          <td><strong>The Spire City (The Veil)</strong></td>
          <td>The inhabited metropolitan zones shielded from toxic sorrow by architectural glass and acoustic mantles.</td>
          <td>Zones A to E, Residential Rings, Directorate Headquarters</td>
        </tr>
        <tr>
          <td><strong>Layer 3</strong></td>
          <td><strong>The Surface Barrens (The Raw / Desolate)</strong></td>
          <td>The toxic wasteland (*Hwangmuji*) where unshielded sorrow crystallizes into razor dunes and feral storms.</td>
          <td>Wandering Titans, Precursor Ruins, Toxic Han Storms</td>
        </tr>
        <tr>
          <td><strong>Layer 4</strong></td>
          <td><strong>The Underworld &amp; Hand Complex</strong></td>
          <td>The subterranean labyrinth housing the 8 floors of the Hand of Change and black-market dens.</td>
          <td>Containment Cells, M.A.W. Forges, Cryo-Vaults, Menders</td>
        </tr>
        <tr>
          <td><strong>Layer 5</strong></td>
          <td><strong>The Abyssal Deep (The Weeping River)</strong></td>
          <td>The subterranean ocean of pure liquefied grief from which all Sorrow Entities continuously coalesce.</td>
          <td>The Forbidden Gate, Singularity Conduit, The Primordial Weeping</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="wiki-section" id="core-lore-compendium">
  <h2 class="section-title">Core Lore Compendium &amp; Historical Chronicles</h2>
  <div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 16px; margin-top: 1rem;">
    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="the-cycle-and-absolvohan.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">THE CYCLE &amp; ABSOLVOHAN</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">The complete day-by-day facility chronicle across 1,778 resets. Details the Day 0 awakening through the terminal Day 365 Singularity convergence.</p>
      <a href="the-cycle-and-absolvohan.html" class="action-btn">Read 9-Part Chronicle →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="the-alpha-tree.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">THE ALPHA TREE (알파 나무)</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">The colossal biological singularity whose Sap sustains the city's power grid. Explores canopy ecology, root networks, and extraction limits.</p>
      <a href="the-alpha-tree.html" class="action-btn">View Arboreal Dossier →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="the-three-sorrows.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">THE THREE SORROWS</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">The foundational triad of sorrow manifestation: *Sorrow* (active grief), *Grieving* (decaying mourning), and *Lament* (petrified regret).</p>
      <a href="the-three-sorrows.html" class="action-btn">View Metaphysical Matrix →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="the-seven-absolute-taboos.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">THE SEVEN ABSOLUTE TABOOS</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Civic and existential prohibitions enforced by the Giltong hunters. Explores soul calcification, forbidden research, and memory breaches.</p>
      <a href="the-seven-absolute-taboos.html" class="action-btn">Examine Law Codes →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="the-cheongula-incident.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">THE CHEONGULA INCIDENT (3,892)</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Hour-by-hour timeline of the catastrophic reactor breach that claimed 142,000 lives and led to the creation of the sealed quarantine wall.</p>
      <a href="the-cheongula-incident.html" class="action-btn">View Disaster Logs →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="the-dawn-of-hope.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">THE DAWN OF HOPE (YEAR 4,238)</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">The post-cycle reconstruction era following the release of the Alpha Sap, chronicling the emergence of Outskirts settlements and fracture healing.</p>
      <a href="the-dawn-of-hope.html" class="action-btn">Explore 8 Epilogue Arcs →</a>
    </div>
  </div>
</section>
'''

toc_lore = [
    ("cosmological-foundations", "Cosmological Framework & The Five Layers"),
    ("core-lore-compendium", "Core Lore Compendium & Historical Chronicles")
]

p_lore = get_base_template("Lore & Cosmology Master Directory", "Lore & World", "lore/index.html", "../", lore_hub_html, toc_lore)
with open(os.path.join(WIKI_DIR, "lore/index.html"), 'w', encoding='utf-8') as f:
    f.write(p_lore)
print("Built Super Hub: lore/index.html")

# ==============================================================================
# 3. LOCATIONS & ATLAS HUB (locations/index.html)
# ==============================================================================
loc_hub_html = '''
<div class="wiki-callout" style="border-left: 5px solid #22c55e; background: linear-gradient(135deg, #0d121c 0%, #06080d 100%);">
  <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
    <div>
      <span class="badge badge-canon" style="margin-bottom: 6px;">CARTOGRAPHY &amp; ATLAS</span>
      <h2 style="margin: 0; color: #4ade80; font-size: 1.6rem; font-family: Impact, sans-serif;">SOMNARAK GEOGRAPHICAL &amp; URBAN ATLAS</h2>
      <p style="margin: 4px 0 0; color: #94a3b8; font-size: 0.88rem;">Zones A to E · Hand of Change Subterranean Layout · The Desolate &amp; Lost Cities</p>
    </div>
    <div style="display: flex; gap: 8px;">
      <span class="badge badge-source">5 ZONES</span>
      <span class="badge badge-source">8 FLOORS</span>
      <span class="badge badge-source">4 UNKNOWN CITIES</span>
    </div>
  </div>
</div>

<section class="wiki-section" id="city-zones-structure">
  <h2 class="section-title">The Five Metropolitan Zones (구역 구조)</h2>
  <p>The city of Somnarak is constructed in concentric architectural rings radiating outward from the <a href="zone-a-core-nexus.html" class="wiki-link">Core Nexus</a> at the base of the <a href="../lore/the-alpha-tree.html" class="wiki-link">Alpha Tree</a>:</p>
  
  <div class="table-wrap">
    <table class="wiki-table">
      <thead>
        <tr>
          <th>Zone Code</th>
          <th>District Name</th>
          <th>Urban Function</th>
          <th>Primary Landmarks</th>
          <th>Atmospheric Shield Tier</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Zone A</strong></td>
          <td><a href="zone-a-core-nexus.html" class="wiki-link">Core Nexus</a></td>
          <td>Governance, Siphon Pylons, Council Chambers</td>
          <td>The High Spire, Directorate Monolith, Sap Conduits</td>
          <td><span class="badge badge-source">GRADE I VEIL (100% PURIFIED)</span></td>
        </tr>
        <tr>
          <td><strong>Zone B</strong></td>
          <td><a href="zone-b-west-ward.html" class="wiki-link">West Ward</a></td>
          <td>Civilian Habitation, Commerce, Culture</td>
          <td>Orphan Bell Tower, Residential Spires, Tea Gardens</td>
          <td><span class="badge badge-source">GRADE II VEIL (95% FILTERED)</span></td>
        </tr>
        <tr>
          <td><strong>Zone C</strong></td>
          <td><a href="zone-c-collectors-row.html" class="wiki-link">Collector's Row</a></td>
          <td>Scrap Salvage, Pawn Conduits, Relic Trade</td>
          <td>Black Market Conduits, Exchange Dens, Pawn Spire</td>
          <td><span class="badge badge-source">GRADE III VEIL (80% FILTERED)</span></td>
        </tr>
        <tr>
          <td><strong>Zone D</strong></td>
          <td><a href="zone-d-forge-and-gardens.html" class="wiki-link">Insight Forge &amp; Gardens</a></td>
          <td>Heavy Industry, Hydroponics, Power Relays</td>
          <td>Hydroponic Glasshouses, Siphon Refineries, Smelters</td>
          <td><span class="badge badge-source">GRADE IV VEIL (60% FILTERED)</span></td>
        </tr>
        <tr>
          <td><strong>Zone E</strong></td>
          <td><a href="zone-e-perimeter-bulwark.html" class="wiki-link">Perimeter Bulwark</a></td>
          <td>Border Defense, Acoustic Shields, Outpost Gate</td>
          <td>Outer Titanium Wall, Soundwave Pylons, Outskirts Gate</td>
          <td><span class="badge badge-source">GRADE V REINFORCED BASTION</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="wiki-section" id="outer-realms-ruins">
  <h2 class="section-title">The Desolate &amp; Precursor Ruins</h2>
  <div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 16px; margin-top: 1rem;">
    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="the-desolate.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">THE DESOLATE (황무지)</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">The toxic barrens surrounding Somnarak. Features razor dunes of crystallized grief, wandering sorrow colossi, and lethal Han storm scales.</p>
      <a href="the-desolate.html" class="action-btn">View Wasteland Atlas →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="unknown-cities.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">UNKNOWN CITIES &amp; CITADELS</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Catalog of lost precursor settlements: the Sunken Citadel of Cheonbulok, Old Cheongula Basin, Port Haerim, and Spire Namsan.</p>
      <a href="unknown-cities.html" class="action-btn">Explore Ruin Registers →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="the-maw.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">THE MAW (추출의 용광로)</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">The subterranean extraction furnace deep within Floor 3, where pure sorrow resonance is harvested and forged into M.A.W. equipment.</p>
      <a href="the-maw.html" class="action-btn">Examine Siphoning Core →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="../atlas/hand-of-change-map.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">HAND OF CHANGE BLUEPRINT</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Interactive high-resolution architectural cutaway schematic detailing all 8 containment and operational floors of the Directorate.</p>
      <a href="../atlas/hand-of-change-map.html" class="action-btn">Open Interactive Map →</a>
    </div>
  </div>
</section>
'''

toc_loc = [
    ("city-zones-structure", "The Five Metropolitan Zones"),
    ("outer-realms-ruins", "The Desolate & Precursor Ruins")
]

p_loc = get_base_template("Atlas & Locations Directory", "Locations & Atlas", "locations/index.html", "../", loc_hub_html, toc_loc)
with open(os.path.join(WIKI_DIR, "locations/index.html"), 'w', encoding='utf-8') as f:
    f.write(p_loc)
print("Built Super Hub: locations/index.html")

# ==============================================================================
# 4. FACTIONS & GUILDS HUB (factions/index.html)
# ==============================================================================
fac_hub_html = '''
<div class="wiki-callout" style="border-left: 5px solid #ef5b55; background: linear-gradient(135deg, #0d121c 0%, #06080d 100%);">
  <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
    <div>
      <span class="badge badge-canon" style="margin-bottom: 6px;">POLITICAL &amp; GUILD MATRIX</span>
      <h2 style="margin: 0; color: #ef5b55; font-size: 1.6rem; font-family: Impact, sans-serif;">SOMNARAK FACTIONS &amp; GUILDS REGISTRY</h2>
      <p style="margin: 4px 0 0; color: #94a3b8; font-size: 0.88rem;">The Reverie Directorate · The Council of Sighs · The Four Master Guilds · The Underworld</p>
    </div>
    <div style="display: flex; gap: 8px;">
      <span class="badge badge-source">1 DIRECTORATE</span>
      <span class="badge badge-source">4 MASTER GUILDS</span>
      <span class="badge badge-source">2 TACTICAL DIVISIONS</span>
    </div>
  </div>
</div>

<section class="wiki-section" id="governing-authorities">
  <h2 class="section-title">Governing Powers &amp; Tactical Divisions</h2>
  <div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 16px; margin-top: 1rem;">
    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="the-reverie-directorate.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">THE REVERIE DIRECTORATE</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">The supreme containment authority commanding the Hand of Change. Features 12 specialized bureaus, 8 floors, and 9 Echo-Core leaders.</p>
      <a href="the-reverie-directorate.html" class="action-btn">View Master Dossier →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="the-high-council.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">THE HIGH COUNCIL (COUNCIL OF SIGHS)</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">The Five Heads (*Osu*) governing civic administration, food synthesis rationing, Echo-Token currency, and Spire residential permits.</p>
      <a href="the-high-council.html" class="action-btn">View Council Register →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="the-sed-corps.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">SORROW EXPLORATION DIVISION (SED)</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Deep-range wasteland survey division led by Cartographer Yeonhwa. Complete logs of 7 campaigns, 43 chapters, and wasteland compass mechanics.</p>
      <a href="the-sed-corps.html" class="action-btn">View Expedition Logs →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="the-ucd-strike-force.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">UNDERWORLD CONTAINMENT DIVISION (UCD)</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Subterranean tactical strike force led by Commander Taeho. Chronicles 6 campaigns combating black-market entity traders and memory washers.</p>
      <a href="the-ucd-strike-force.html" class="action-btn">View Tactical Raids →</a>
    </div>
  </div>
</section>

<section class="wiki-section" id="four-master-guilds">
  <h2 class="section-title">The Four Master Guilds of Somnarak</h2>
  <div class="table-wrap">
    <table class="wiki-table">
      <thead>
        <tr>
          <th>Guild Name</th>
          <th>Korean Name</th>
          <th>Primary Specialization</th>
          <th>Primary Technology Base</th>
          <th>Zone Presence</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><a href="the-architects.html" class="wiki-link">The Architects</a></td>
          <td>건축가 (Geonchukga)</td>
          <td>Spire masonry, acoustic resonance chambers, titanium foundations</td>
          <td>Masonry &amp; Resonance Conduits</td>
          <td>Zone A &amp; Zone B</td>
        </tr>
        <tr>
          <td><a href="the-weavers.html" class="wiki-link">The Weavers</a></td>
          <td>직조관 (Jikjo-gwan)</td>
          <td>Sorrow silk harvesting, memory fabric tailoring, protective mantles</td>
          <td>Silk Siphoning &amp; Loom Weaving</td>
          <td>Zone B &amp; Zone C</td>
        </tr>
        <tr>
          <td><a href="the-wardens.html" class="wiki-link">The Wardens</a></td>
          <td>경비대 (Gyeongbidae)</td>
          <td>Perimeter wall defense, gate security, acoustic blast shields</td>
          <td>Kinetic Dampening &amp; Armor Plating</td>
          <td>Zone E Bulwark</td>
        </tr>
        <tr>
          <td><a href="the-collectors.html" class="wiki-link">The Collectors</a></td>
          <td>수집가 (Sujipga)</td>
          <td>Precursor relic prospectors, scrap brokers, salvage markets</td>
          <td>Scrap Engineering &amp; Relic Adapters</td>
          <td>Zone C &amp; The Desolate</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
'''

toc_fac = [
    ("governing-authorities", "Governing Powers & Tactical Divisions"),
    ("four-master-guilds", "The Four Master Guilds of Somnarak")
]

p_fac = get_base_template("Factions & Guilds Directory", "Factions & Guilds", "factions/index.html", "../", fac_hub_html, toc_fac)
with open(os.path.join(WIKI_DIR, "factions/index.html"), 'w', encoding='utf-8') as f:
    f.write(p_fac)
print("Built Super Hub: factions/index.html")

# ==============================================================================
# 5. SYSTEMS & MECHANICS HUB (mechanics/index.html)
# ==============================================================================
mech_hub_html = '''
<div class="wiki-callout" style="border-left: 5px solid #c084fc; background: linear-gradient(135deg, #0d121c 0%, #06080d 100%);">
  <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
    <div>
      <span class="badge badge-canon" style="margin-bottom: 6px;">SYSTEMS &amp; COMBAT MECHANICS</span>
      <h2 style="margin: 0; color: #c084fc; font-size: 1.6rem; font-family: Impact, sans-serif;">SOMNARAK OPERATIONAL SYSTEMS MANUAL</h2>
      <p style="margin: 4px 0 0; color: #94a3b8; font-size: 0.88rem;">SECC Threat Classification · Resonant Clash Mechanics · Four Damage Types · Ordeals Schedule</p>
    </div>
    <div style="display: flex; gap: 8px;">
      <span class="badge badge-source">4 DAMAGE TYPES</span>
      <span class="badge badge-source">5 SECC TIERS</span>
      <span class="badge badge-source">4 WORK TYPES</span>
    </div>
  </div>
</div>

<section class="wiki-section" id="damage-matrix">
  <h2 class="section-title">The Four Damage &amp; Resonance Types</h2>
  <div class="table-wrap">
    <table class="wiki-table">
      <thead>
        <tr>
          <th>Damage Type</th>
          <th>Color Spectrum</th>
          <th>Target Attribute</th>
          <th>Resonance Effect</th>
          <th>Therapy / Countermeasure</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>RED (Physical)</strong></td>
          <td><span class="badge" style="background: #ef4444; color: #fff;">RED</span></td>
          <td>Physical HP / Flesh</td>
          <td>Lacerations, crushing bone impact, blood crystallization</td>
          <td>Physical Trauma Suture / Medical Bandages</td>
        </tr>
        <tr>
          <td><strong>WHITE (Mental)</strong></td>
          <td><span class="badge" style="background: #38bdf8; color: #000;">WHITE</span></td>
          <td>Sanity (SP) / Rationality</td>
          <td>Psychic panic, auditory hallucinations, amnesia bleed</td>
          <td>Insight Therapy / Cognitive Anchors</td>
        </tr>
        <tr>
          <td><strong>BLACK (Hybrid)</strong></td>
          <td><span class="badge" style="background: #a855f7; color: #fff;">BLACK</span></td>
          <td>HP &amp; SP Simultaneously</td>
          <td>Erosive decay, necrotic flesh rot, despair corrosion</td>
          <td>Dual Stabilizers / M.A.W. Shroud Reinforcement</td>
        </tr>
        <tr>
          <td><strong>PALE (Soul)</strong></td>
          <td><span class="badge" style="background: #f8fafc; color: #000;">PALE</span></td>
          <td>Max HP Percentage (Absolute)</td>
          <td>Direct soul calcification, erasure of self-identity</td>
          <td>Absolute Resonance Purge / Singularity Shield</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="wiki-section" id="work-types-secc">
  <h2 class="section-title">The Four Work Types &amp; SECC Risk Tiers</h2>
  <div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 16px; margin-top: 1rem;">
    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="the-four-work-types.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">THE FOUR WORK TYPES</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Insight (environmental maintenance), Attachment (social interaction), Repression (instinct containment), and Extraction (M.A.W. harvesting).</p>
      <a href="the-four-work-types.html" class="action-btn">View Work Formulas →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="secc-classification-system.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">SECC THREAT HIERARCHY</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Standardized threat taxonomy: ZAYIN (trivial), TETH (moderate), HE (dangerous), WAW (catastrophic), and ALEPH (existential annihilation).</p>
      <a href="secc-classification-system.html" class="action-btn">View Risk Tiers →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="resonant-clash-mechanics.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">RESONANT CLASH COMBAT</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Speed dice initiative, Clash Power calculations, coin flip mechanics, and Stagger Break vulnerability (2.0x damage multiplier).</p>
      <a href="resonant-clash-mechanics.html" class="action-btn">View Combat Rules →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="ordeals-framework.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">ORDEALS INCURSIONS</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Dawn (First Watch), Noon (Second Watch), Dusk (Third Watch), and Midnight (Tide Watch) incursion waves across 7 color resonances.</p>
      <a href="ordeals-framework.html" class="action-btn">View Ordeal Waves →</a>
    </div>
  </div>
</section>
'''

toc_mech = [
    ("damage-matrix", "The Four Damage & Resonance Types"),
    ("work-types-secc", "The Four Work Types & SECC Risk Tiers")
]

p_mech = get_base_template("Systems & Mechanics Manual", "Systems & Mechanics", "mechanics/index.html", "../", mech_hub_html, toc_mech)
with open(os.path.join(WIKI_DIR, "mechanics/index.html"), 'w', encoding='utf-8') as f:
    f.write(p_mech)
print("Built Super Hub: mechanics/index.html")

