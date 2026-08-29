import re

INDEX_PATH = "/home/user/01_Somnarak_Wiki/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the count "94 article archival records" with "135 verified archival records"
content = content.replace("94 article archival records", "135 verified canonical records across all 8 facility sectors")

# Upgrade the feature grid on index.html to include direct instant-jump sub-links under every portal card!
new_feature_grid = '''<!-- 2x4 Project Moon Neon Feature Grid with Direct Instant Jump Links -->
      <div class="pm-feature-grid">
        <!-- 1. Sorrow Entities -->
        <div class="pm-card-wrapper">
          <a class="pm-card" href="entities/index.html">
            <span class="pm-card-title">— SORROW ENTITIES —</span>
            <img alt="Entities" class="pm-card-icon" src="assets/icons/banner_entities.svg"/>
            <span class="pm-card-sub">SE-001–015 Registry, Risk Ranks &amp; Containment</span>
          </a>
          <div class="card-quick-links">
            <a href="entities/se-001-the-orphaned-bell.html">SE-001</a>
            <a href="entities/se-002-the-grieving-colossus.html">SE-002</a>
            <a href="entities/se-005-the-smothering-mother.html">SE-005</a>
            <a href="entities/se-010-the-convergence.html">SE-010</a>
            <a href="entities/index.html" class="all-link">ALL 10 ENTITIES →</a>
          </div>
        </div>

        <!-- 2. M.A.W. Equipment -->
        <div class="pm-card-wrapper">
          <a class="pm-card gold" href="maw/index.html">
            <span class="pm-card-title">— M.A.W. EQUIPMENT —</span>
            <img alt="M.A.W. Equipment" class="pm-card-icon" src="assets/icons/weapon.svg"/>
            <span class="pm-card-sub">Materialized Agony Weapons, Suits &amp; Gifts</span>
          </a>
          <div class="card-quick-links">
            <a href="maw/maw-w-001-01-the-laments-requiem.html">Lament</a>
            <a href="maw/maw-w-002-01-the-mourning-maul.html">Mourning</a>
            <a href="maw/maw-w-010-01-the-absolute-maul.html">Absolute</a>
            <a href="maw/index.html#weapons-catalog">9 Weapons</a>
            <a href="maw/index.html#suits-catalog">9 Suits</a>
            <a href="maw/index.html" class="all-link">ALL 27 ARMS →</a>
          </div>
        </div>

        <!-- 3. Echo-Cores -->
        <div class="pm-card-wrapper">
          <a class="pm-card crimson" href="characters/index.html">
            <span class="pm-card-title">— ECHO-CORES &amp; CAST —</span>
            <img alt="Characters" class="pm-card-icon" src="assets/icons/banner_characters.svg"/>
            <span class="pm-card-sub">The Nine Leads, Director Majin &amp; Operatives</span>
          </a>
          <div class="card-quick-links">
            <a href="characters/the-director-majin.html">Majin</a>
            <a href="characters/the-secretary-seiyon.html">Seiyon</a>
            <a href="characters/the-containment-lead-dekan.html">Dekan</a>
            <a href="characters/the-extraction-lead-zyrak.html">Zyrak</a>
            <a href="characters/the-research-lead-ayshuk.html">Ayshuk</a>
            <a href="characters/index.html" class="all-link">ALL 19 CAST →</a>
          </div>
        </div>

        <!-- 4. Battle & Mechanics -->
        <div class="pm-card-wrapper">
          <a class="pm-card cyan" href="mechanics/index.html">
            <span class="pm-card-title">— BATTLE &amp; SYSTEMS —</span>
            <img alt="Mechanics" class="pm-card-icon" src="assets/icons/banner_mechanics.svg"/>
            <span class="pm-card-sub">Han Energy, Damage Matrix, Panic &amp; Work Types</span>
          </a>
          <div class="card-quick-links">
            <a href="mechanics/han-energy-and-damage.html">Damage Matrix</a>
            <a href="mechanics/the-four-work-types.html">Work Types</a>
            <a href="mechanics/secc-classification-system.html">SECC Ranks</a>
            <a href="mechanics/resonant-clash-mechanics.html">Clash Rules</a>
            <a href="mechanics/index.html" class="all-link">ALL 14 SYSTEMS →</a>
          </div>
        </div>

        <!-- 5. Factions & Guilds -->
        <div class="pm-card-wrapper">
          <a class="pm-card gold" href="factions/index.html">
            <span class="pm-card-title">— FACTIONS &amp; GUILDS —</span>
            <img alt="Factions" class="pm-card-icon" src="assets/icons/banner_factions.svg"/>
            <span class="pm-card-sub">The Directorate, Council of Sighs &amp; Weavers</span>
          </a>
          <div class="card-quick-links">
            <a href="factions/the-reverie-directorate.html">Directorate</a>
            <a href="factions/the-high-council.html">High Council</a>
            <a href="factions/the-sed-corps.html">SED Corps</a>
            <a href="factions/the-ucd-strike-force.html">UCD Force</a>
            <a href="factions/index.html" class="all-link">ALL 14 FACTIONS →</a>
          </div>
        </div>

        <!-- 6. Hand of Change -->
        <div class="pm-card-wrapper">
          <a class="pm-card cyan" href="departments/index.html">
            <span class="pm-card-title">— HAND OF CHANGE —</span>
            <img alt="Departments" class="pm-card-icon" src="assets/layout/hand/icons/icon_reverie_directorate_minimal.svg"/>
            <span class="pm-card-sub">Floors 1–8 Operations, Missions &amp; Protocols</span>
          </a>
          <div class="card-quick-links">
            <a href="departments/floor-1-neutral-command.html">Floor 1</a>
            <a href="departments/floor-2-maws-keep.html">Floor 2</a>
            <a href="departments/floor-3-extraction-hall.html">Floor 3</a>
            <a href="departments/floor-4-insight-forge.html">Floor 4</a>
            <a href="departments/index.html" class="all-link">ALL 8 FLOORS →</a>
          </div>
        </div>

        <!-- 7. Atlas & Maps -->
        <div class="pm-card-wrapper">
          <a class="pm-card crimson" href="locations/index.html">
            <span class="pm-card-title">— ATLAS &amp; MAPS —</span>
            <img alt="Locations" class="pm-card-icon" src="assets/icons/banner_locations.svg"/>
            <span class="pm-card-sub">Zones A–E, The Maw &amp; The Desolate Wasteland</span>
          </a>
          <div class="card-quick-links">
            <a href="locations/zone-a-core-nexus.html">Zone A</a>
            <a href="locations/zone-b-west-ward.html">Zone B</a>
            <a href="locations/the-desolate.html">The Desolate</a>
            <a href="locations/the-maw.html">The Maw</a>
            <a href="locations/index.html" class="all-link">ALL 12 ATLAS →</a>
          </div>
        </div>

        <!-- 8. Lore & Cosmology -->
        <div class="pm-card-wrapper">
          <a class="pm-card" href="lore/index.html">
            <span class="pm-card-title">— LORE &amp; COSMOLOGY —</span>
            <img alt="Lore" class="pm-card-icon" src="assets/icons/banner_lore.svg"/>
            <span class="pm-card-sub">The 1,778 Cycles, The Alpha Tree &amp; Three Sorrows</span>
          </a>
          <div class="card-quick-links">
            <a href="lore/the-cycle-and-absolvohan.html">Absolvohan</a>
            <a href="lore/the-alpha-tree.html">Alpha Tree</a>
            <a href="lore/the-three-sorrows.html">3 Sorrows</a>
            <a href="lore/the-dawn-of-hope.html">Dawn of Hope</a>
            <a href="lore/index.html" class="all-link">ALL 16 LORE →</a>
          </div>
        </div>
      </div>'''

content = re.sub(r'<div class="pm-feature-grid">.*?</div>\s*<!-- Quick Categories -->', new_feature_grid + '\n      <!-- Quick Categories -->', content, flags=re.DOTALL)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html feature grid with direct instant-jump sub-links.")
