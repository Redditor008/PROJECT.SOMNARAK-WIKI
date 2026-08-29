import re

new_hubs_html = """      <!-- 8 Portal Navigation Hubs -->
      <section class="pm-section-block">
        <div class="section-title-bar">
          <h2>/// MASTER ENCYCLOPEDIC ARCHIVES</h2>
          <span class="title-sub">EXPLORE ALL 8 FACILITY & METROPOLITAN CODEXES</span>
        </div>
        <div class="master-hub-grid">
          <!-- 1. Sorrow Entities -->
          <div class="master-hub-card hub-entities">
            <div class="hub-card-header">
              <span class="hub-card-badge">REGISTER SE-001–015</span>
              <span class="hub-card-counter">10 ENTITIES</span>
            </div>
            <div class="hub-card-body">
              <img src="assets/icons/icon_hub_entities.svg" alt="Sorrow Entities" class="hub-card-icon" width="76" height="76">
              <div class="hub-card-info">
                <h3 class="hub-card-title"><a href="entities/index.html">SORROW ENTITIES</a></h3>
                <span class="hub-card-sub">Containment &amp; Extraction Registry</span>
                <p class="hub-card-desc">SECC Threat Ranks (CAN to APOCRYPHA), Coherence decay formulas, work responses &amp; M.A.W. yield stats.</p>
              </div>
            </div>
            <div class="hub-card-footer">
              <a href="entities/index.html" class="hub-enter-btn">EXPLORE ENTITY CODEX →</a>
              <div class="hub-card-links">
                <a href="entities/se-001-the-orphaned-bell.html">SE-001</a>
                <a href="entities/se-002-the-grieving-colossus.html">SE-002</a>
                <a href="entities/se-005-the-smothering-mother.html">SE-005</a>
                <a href="entities/se-010-the-convergence.html">SE-010</a>
              </div>
            </div>
          </div>

          <!-- 2. M.A.W. Equipment -->
          <div class="master-hub-card hub-maw">
            <div class="hub-card-header">
              <span class="hub-card-badge">ARSENAL MATRIX</span>
              <span class="hub-card-counter">27 GEAR CODEXES</span>
            </div>
            <div class="hub-card-body">
              <img src="assets/icons/icon_hub_maw.svg" alt="M.A.W. Equipment" class="hub-card-icon" width="76" height="76">
              <div class="hub-card-info">
                <h3 class="hub-card-title"><a href="maw/index.html">M.A.W. EQUIPMENT</a></h3>
                <span class="hub-card-sub">Materialized Agony Armory</span>
                <p class="hub-card-desc">Weapons, containment suits, and extraction gifts categorized by the 4 Han damage types &amp; resonance tiers.</p>
              </div>
            </div>
            <div class="hub-card-footer">
              <a href="maw/index.html" class="hub-enter-btn">BROWSE ARSENAL →</a>
              <div class="hub-card-links">
                <a href="maw/maw-w-001-01-the-laments-requiem.html">Lament Requiem</a>
                <a href="maw/maw-w-010-01-the-absolute-maul.html">Absolute Maul</a>
                <a href="maw/maw-s-001-01-the-laments-shroud.html">Lament Shroud</a>
              </div>
            </div>
          </div>

          <!-- 3. Echo-Cores & Personnel -->
          <div class="master-hub-card hub-characters">
            <div class="hub-card-header">
              <span class="hub-card-badge">PERSONNEL DOSSIERS</span>
              <span class="hub-card-counter">19 PROFILES</span>
            </div>
            <div class="hub-card-body">
              <img src="assets/icons/icon_hub_characters.svg" alt="Characters" class="hub-card-icon" width="76" height="76">
              <div class="hub-card-info">
                <h3 class="hub-card-title"><a href="characters/index.html">ECHO-CORES &amp; CAST</a></h3>
                <span class="hub-card-sub">The Nine Leads &amp; Directorate</span>
                <p class="hub-card-desc">Department head biographies, symbolic regalia artifacts, behavioral profiles, and facility directives.</p>
              </div>
            </div>
            <div class="hub-card-footer">
              <a href="characters/index.html" class="hub-enter-btn">VIEW PERSONNEL FILES →</a>
              <div class="hub-card-links">
                <a href="characters/the-director-majin.html">Majin</a>
                <a href="characters/the-secretary-seiyon.html">Seiyon</a>
                <a href="characters/the-containment-lead-dekan.html">Dekan</a>
                <a href="characters/the-border-lead-mellda.html">Mellda</a>
              </div>
            </div>
          </div>

          <!-- 4. Combat Systems & Mechanics -->
          <div class="master-hub-card hub-mechanics">
            <div class="hub-card-header">
              <span class="hub-card-badge">COMBAT ENGINE</span>
              <span class="hub-card-counter">13 PROTOCOLS</span>
            </div>
            <div class="hub-card-body">
              <img src="assets/icons/icon_hub_mechanics.svg" alt="Mechanics" class="hub-card-icon" width="76" height="76">
              <div class="hub-card-info">
                <h3 class="hub-card-title"><a href="mechanics/index.html">BATTLE &amp; SYSTEMS</a></h3>
                <span class="hub-card-sub">Han Energy, Panic &amp; Work Types</span>
                <p class="hub-card-desc">The 4-way Han damage rules (Grudge, Lament, Void, Weight), agent panic states, and containment suppression.</p>
              </div>
            </div>
            <div class="hub-card-footer">
              <a href="mechanics/index.html" class="hub-enter-btn">MASTER SYSTEMS →</a>
              <div class="hub-card-links">
                <a href="mechanics/han-energy-and-damage.html">Damage Matrix</a>
                <a href="mechanics/the-four-work-types.html">4 Work Types</a>
                <a href="mechanics/panic-states-and-corrosion.html">Panic States</a>
              </div>
            </div>
          </div>

          <!-- 5. Factions & Metropolitan Guilds -->
          <div class="master-hub-card hub-factions">
            <div class="hub-card-header">
              <span class="hub-card-badge">POLITICAL CODEX</span>
              <span class="hub-card-counter">12 FACTIONS</span>
            </div>
            <div class="hub-card-body">
              <img src="assets/icons/icon_hub_factions.svg" alt="Factions" class="hub-card-icon" width="76" height="76">
              <div class="hub-card-info">
                <h3 class="hub-card-title"><a href="factions/index.html">FACTIONS &amp; GUILDS</a></h3>
                <span class="hub-card-sub">Directorate, Council &amp; Syndicates</span>
                <p class="hub-card-desc">Geopolitical records on the Reverie Directorate, High Council, Iron Guild, Siphon Cults, and Underground rings.</p>
              </div>
            </div>
            <div class="hub-card-footer">
              <a href="factions/index.html" class="hub-enter-btn">INSPECT FACTIONS →</a>
              <div class="hub-card-links">
                <a href="factions/the-reverie-directorate.html">Directorate</a>
                <a href="factions/the-high-council.html">High Council</a>
                <a href="factions/the-weavers.html">Weavers</a>
              </div>
            </div>
          </div>

          <!-- 6. Hand of Change (Facility 01) -->
          <div class="master-hub-card hub-departments">
            <div class="hub-card-header">
              <span class="hub-card-badge">FACILITY MONOLITH</span>
              <span class="hub-card-counter">8 FLOORS</span>
            </div>
            <div class="hub-card-body">
              <img src="assets/icons/icon_hub_departments.svg" alt="Hand of Change" class="hub-card-icon" width="76" height="76">
              <div class="hub-card-info">
                <h3 class="hub-card-title"><a href="departments/index.html">HAND OF CHANGE</a></h3>
                <span class="hub-card-sub">Floors 1–8 Operations &amp; Blueprints</span>
                <p class="hub-card-desc">Departmental Han passives, containment grid blueprints, emergency lockdown triggers, and incident archives.</p>
              </div>
            </div>
            <div class="hub-card-footer">
              <a href="departments/index.html" class="hub-enter-btn">ENTER FACILITY →</a>
              <div class="hub-card-links">
                <a href="departments/floor-1-neutral-command.html">Floor 1 Neutral</a>
                <a href="departments/floor-2-maws-keep.html">Floor 2 Maw</a>
                <a href="departments/floor-8-gate-watch.html">Floor 8 Gate</a>
              </div>
            </div>
          </div>

          <!-- 7. Metropolitan Atlas & Geography -->
          <div class="master-hub-card hub-locations">
            <div class="hub-card-header">
              <span class="hub-card-badge">SPATIAL SECTORS</span>
              <span class="hub-card-counter">10 LOCATIONS</span>
            </div>
            <div class="hub-card-body">
              <img src="assets/icons/icon_hub_locations.svg" alt="Atlas" class="hub-card-icon" width="76" height="76">
              <div class="hub-card-info">
                <h3 class="hub-card-title"><a href="locations/index.html">ATLAS &amp; GEOGRAPHY</a></h3>
                <span class="hub-card-sub">Zones A–E, The Maw &amp; Outskirts</span>
                <p class="hub-card-desc">Topographical schematics of the 5 Metropolitan Zones, Hollow Glass, Subterranean Maw, and Desolate Outskirts.</p>
              </div>
            </div>
            <div class="hub-card-footer">
              <a href="locations/index.html" class="hub-enter-btn">SURVEY ATLAS →</a>
              <div class="hub-card-links">
                <a href="locations/zone-a-core-nexus.html">Zone A Core</a>
                <a href="locations/the-maw.html">The Maw</a>
                <a href="locations/the-desolate.html">The Desolate</a>
              </div>
            </div>
          </div>

          <!-- 8. Lore Chronicles & Cosmology -->
          <div class="master-hub-card hub-lore">
            <div class="hub-card-header">
              <span class="hub-card-badge">CHRONOLOGY MATRIX</span>
              <span class="hub-card-counter">24 CHRONICLES</span>
            </div>
            <div class="hub-card-body">
              <img src="assets/icons/icon_hub_lore.svg" alt="Lore" class="hub-card-icon" width="76" height="76">
              <div class="hub-card-info">
                <h3 class="hub-card-title"><a href="lore/index.html">LORE &amp; COSMOLOGY</a></h3>
                <span class="hub-card-sub">The 1,778 Cycles &amp; Alpha Tree</span>
                <p class="hub-card-desc">The primordial Alpha Tree, the Three Sorrows, the Seven Absolute Taboos, and the historic Dawn of Hope in Year 4,238.</p>
              </div>
            </div>
            <div class="hub-card-footer">
              <a href="lore/index.html" class="hub-enter-btn">READ CHRONICLES →</a>
              <div class="hub-card-links">
                <a href="lore/the-cycle-and-absolvohan.html">1,778 Cycles</a>
                <a href="lore/the-alpha-tree.html">Alpha Tree</a>
                <a href="lore/the-seven-absolute-taboos.html">Seven Taboos</a>
              </div>
            </div>
          </div>
        </div>
      </section>"""

with open('/home/user/01_Somnarak_Wiki/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_section_regex = r'<!-- 8 Portal Navigation Hubs -->[\s\S]*?<\/section>'
match = re.search(old_section_regex, content)
if match:
    new_content = content[:match.start()] + new_hubs_html + content[match.end():]
    with open('/home/user/01_Somnarak_Wiki/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('SUCCESS: Updated index.html with validated links!')
else:
    print('ERROR: Could not find section in index.html')
