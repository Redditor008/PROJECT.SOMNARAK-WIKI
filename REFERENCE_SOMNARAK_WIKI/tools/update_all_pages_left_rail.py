import os, glob, re
from bs4 import BeautifulSoup

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

def build_left_rail(prefix):
    return f'''
    <aside class="left-rail">
      <div class="site-mark">
        <a href="{prefix}index.html">
          <img src="{prefix}assets/icons/somnarak_icon.svg" alt="Somnarak Emblem">
          <b>SOMNARAK</b>
          <span>OFFICIAL WIKI ARCHIVE</span>
        </a>
      </div>
      <nav aria-label="Wiki navigation" class="left-links">
        <section>
          <h2>DATABASE HUBS</h2>
          <a href="{prefix}index.html">Main Overview</a>
          <a href="{prefix}characters/index.html">Characters Hub</a>
          <a href="{prefix}lore/index.html">Lore &amp; Cosmology</a>
          <a href="{prefix}locations/index.html">Locations &amp; Atlas</a>
          <a href="{prefix}factions/index.html">Factions &amp; Guilds</a>
          <a href="{prefix}departments/index.html">Facility Floors</a>
          <a href="{prefix}entities/index.html">Sorrow Entities</a>
          <a href="{prefix}maw/index.html">M.A.W. Equipment</a>
          <a href="{prefix}mechanics/index.html">Systems &amp; Mechanics</a>
        </section>
        <section>
          <h2>THE NINE ECHO-CORES</h2>
          <a href="{prefix}characters/the-director-majin.html">1. Director Majin</a>
          <a href="{prefix}characters/the-secretary-seiyon.html">2. Seiyon (Secretary)</a>
          <a href="{prefix}characters/the-containment-lead-dekan.html">3. Dekan (Containment)</a>
          <a href="{prefix}characters/the-extraction-lead-zyrak.html">4. Zyrak (Extraction)</a>
          <a href="{prefix}characters/the-research-lead-ayshuk.html">5. Ayshuk (Research)</a>
          <a href="{prefix}characters/the-border-lead-mellda.html">6. Mellda (Border)</a>
          <a href="{prefix}characters/the-archive-lead-marjuk.html">7. Marjuk (Archive)</a>
          <a href="{prefix}characters/the-outsider-ishall.html">8. Ishall (Outsider)</a>
          <a href="{prefix}characters/the-exile-xyan.html">9. Xyan (Exile)</a>
        </section>
        <section>
          <h2>CARTOGRAPHY &amp; SCHEMATICS</h2>
          <a href="{prefix}atlas/hand-of-change-map.html">Hand of Change Map</a>
          <a href="{prefix}atlas/somnarak-city-map.html">Somnarak City Blueprint</a>
          <a href="{prefix}project/source-map.html">Master Archive Map</a>
        </section>
      </nav>
    </aside>
    '''

# Update index.html specifically with the master L-Corp Right Rail
index_right_rail = '''
    <!-- Right Rail: Authentic L-Corp Hazard Chevron Department Buttons -->
    <aside aria-label="Hand of Change departments" class="floor-rail">
      <div class="floor-rail-header">
        <h2>/// HAND OF CHANGE ///</h2>
        <small>REVERIE DIRECTORATE FACILITY</small>
      </div>

      <!-- Floor 1: Neutral Command -->
      <a class="pm-hazard-btn" href="departments/floor-1-neutral-command.html" style="--floor-color:#ef5b55">
        <div class="pm-hazard-btn-text">
          <small>FLOOR 01 // PALM CORE</small>
          <b>NEUTRAL COMMAND</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt="">
      </a>

      <!-- Floor 2: Maw's Keep -->
      <a class="pm-hazard-btn" href="departments/floor-2-maws-keep.html" style="--floor-color:#5b75e8">
        <div class="pm-hazard-btn-text">
          <small>FLOOR 02 // WARD KEEP</small>
          <b>MAW’S KEEP</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f2_maws_keep.svg" alt="">
      </a>

      <!-- Floor 3: Extraction Hall -->
      <a class="pm-hazard-btn" href="departments/floor-3-extraction-hall.html" style="--floor-color:#e6c843">
        <div class="pm-hazard-btn-text">
          <small>FLOOR 03 // SIPHON FORGE</small>
          <b>EXTRACTION HALL</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f3_extraction.svg" alt="">
      </a>

      <!-- Floor 4: Insight Forge -->
      <a class="pm-hazard-btn" href="departments/floor-4-insight-forge.html" style="--floor-color:#47c978">
        <div class="pm-hazard-btn-text">
          <small>FLOOR 04 // RESEARCH CORE</small>
          <b>INSIGHT FORGE</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f4_insight_forge.svg" alt="">
      </a>

      <!-- Floor 5: Border Watch -->
      <a class="pm-hazard-btn" href="departments/floor-5-border-watch.html" style="--floor-color:#d4d4d8">
        <div class="pm-hazard-btn-text">
          <small>FLOOR 05 // BORDER BASTION</small>
          <b>BORDER WATCH</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f5_border_watch.svg" alt="">
      </a>

      <!-- Floor 6: Deep Vault -->
      <a class="pm-hazard-btn" href="departments/floor-6-deep-vault.html" style="--floor-color:#991b1b">
        <div class="pm-hazard-btn-text">
          <small>FLOOR 06 // CRYO ARCHIVE</small>
          <b>DEEP VAULT</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f6_deep_vault.svg" alt="">
      </a>

      <!-- Floor 7: Shadow Corps -->
      <a class="pm-hazard-btn" href="departments/floor-7-shadow-corps.html" style="--floor-color:#f472b6">
        <div class="pm-hazard-btn-text">
          <small>FLOOR 07 // VOID DIVERS</small>
          <b>SHADOW CORPS</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f7_shadow_corps.svg" alt="">
      </a>

      <!-- Floor 8: Gate Watch -->
      <a class="pm-hazard-btn" href="departments/floor-8-gate-watch.html" style="--floor-color:#fde047">
        <div class="pm-hazard-btn-text">
          <small>FLOOR 08 // TABOO GATE</small>
          <b>GATE WATCH</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f8_gate_watch.svg" alt="">
      </a>

      <!-- Action Buttons -->
      <a class="pm-action-btn" href="atlas/hand-of-change-map.html">
        FACILITY CUTAWAY MAP
        <img src="assets/layout/hand/icons/the_hand_dr_icon_styled.svg" alt="">
      </a>
      <a class="pm-action-btn" href="atlas/somnarak-city-map.html">
        CITY MASTER BLUEPRINT
        <img src="assets/layout/city/icons/somnarak_city_icon.svg" alt="">
      </a>

      <!-- Related Directories -->
      <div class="pm-related-section">
        <h3>RELATED DIRECTORIES</h3>
        <a class="pm-related-card" href="departments/index.html">
          <img src="assets/layout/hand/blueprints/THE_HAND_DR_LAYOUT.png" alt="The Hand of Change">
          <span>THE HAND OF CHANGE DIRECTORY</span>
        </a>
        <a class="pm-related-card" href="locations/index.html">
          <img src="assets/layout/city/blueprints/SOMNARAK_CITY_LAYOUT.png" alt="Somnarak City Atlas">
          <span>SOMNARAK URBAN ATLAS</span>
        </a>
      </div>
    </aside>
'''

for html_path in glob.glob(os.path.join(WIKI_DIR, "**/*.html"), recursive=True):
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    rel = os.path.relpath(html_path, WIKI_DIR)
    rel_depth = len(rel.split(os.sep)) - 1
    prefix = "../" * rel_depth

    # Replace left-rail
    new_left = build_left_rail(prefix)
    content = re.sub(r'<aside[^>]*class=[\'"][^\'"]*left-rail[^\'"]*[\'"][^>]*>.*?</aside>', new_left, content, flags=re.DOTALL)

    # If index.html, replace floor-rail
    if rel == "index.html":
        content = re.sub(r'<aside[^>]*class=[\'"][^\'"]*floor-rail[^\'"]*[\'"][^>]*>.*?</aside>', index_right_rail, content, flags=re.DOTALL)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Updated Left Rail on all 135 pages and L-Corp Right Rail on index.html.")
