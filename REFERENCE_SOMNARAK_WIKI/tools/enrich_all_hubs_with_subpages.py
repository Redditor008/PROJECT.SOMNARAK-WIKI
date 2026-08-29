import os
import re

def enrich_hubs():
    base_dir = "/home/user/01_Somnarak_Wiki"

    # 1. ENRICH DEPARTMENTS INDEX
    dept_index = os.path.join(base_dir, "departments/index.html")
    if os.path.exists(dept_index):
        with open(dept_index, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Add a new section for Floor Sub-Protocols & Emergency Directives before the footer
        subpage_section = '''
  <h2 class="section-title" id="sub-protocols" style="margin-top: 3rem;">DEPARTMENT OPERATIONAL SUB-PROTOCOLS &amp; EMERGENCY DIRECTIVES</h2>
  <p class="section-desc">
    Classified executive override protocols, specialized chamber schematics, and facility-wide meltdown containment directives for all 8 sectors.
  </p>

  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#71efaf;">
      <div class="entity-card-top">
        <img src="../assets/layout/hand/blueprints/floor-1-neutral-blueprint.svg" alt="Floor 1 Sub-Protocols" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-aleph">PROTO-01</span><span class="sector-tag">EXECUTIVE</span></div>
      </div>
      <h3 class="entity-card-name">NEUTRAL COMMAND OVERRIDES</h3>
      <p class="entity-card-desc">Director Majin's emergency authority, 5-stage alarm escalation rules, and sovereign core lockdown procedures.</p>
      <a href="floor-1-sub-protocols.html" class="jump-btn">ACCESS SUB-PROTOCOLS →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#ef5b55;">
      <div class="entity-card-top">
        <img src="../assets/layout/hand/blueprints/floor-2-maws-keep-blueprint.svg" alt="Floor 2 Armory" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-waw">VAULT-02</span><span class="sector-tag">FORGE</span></div>
      </div>
      <h3 class="entity-card-name">MAW'S KEEP FORGING VAULTS</h3>
      <p class="entity-card-desc">M.A.W. crystallization forges, temperature parameters, and armory maintenance schedules.</p>
      <a href="floor-2-arsenal-vaults.html" class="jump-btn">ACCESS ARSENAL VAULTS →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#38bdf8;">
      <div class="entity-card-top">
        <img src="../assets/layout/hand/blueprints/floor-3-extraction-hall-blueprint.svg" alt="Floor 3 Siphons" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-waw">SIPHON-03</span><span class="sector-tag">ENERGY</span></div>
      </div>
      <h3 class="entity-card-name">EXTRACTION HALL SIPHONS</h3>
      <p class="entity-card-desc">Extraction Lead Zyrak's Han-Flux siphoning vats, yield variance tables, and pressure dump valves.</p>
      <a href="floor-3-extraction-protocols.html" class="jump-btn">ACCESS EXTRACTION LOGS →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#f1df76;">
      <div class="entity-card-top">
        <img src="../assets/layout/hand/blueprints/floor-4-insight-forge-blueprint.svg" alt="Floor 4 Labs" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-he">LABS-04</span><span class="sector-tag">R&amp;D</span></div>
      </div>
      <h3 class="entity-card-name">INSIGHT FORGE RESEARCH LABS</h3>
      <p class="entity-card-desc">Cognitive resonance spectrometers, observation stages, and unredacted entity psychology dossiers.</p>
      <a href="floor-4-insight-observation-labs.html" class="jump-btn">ACCESS LAB DOSSIERS →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#ef5b55;">
      <div class="entity-card-top">
        <img src="../assets/layout/hand/blueprints/floor-5-border-watch-blueprint.svg" alt="Floor 5 Containment" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-waw">CELLS-05</span><span class="sector-tag">DEFENSE</span></div>
      </div>
      <h3 class="entity-card-name">BORDER WATCH HIGH CONTAINMENT</h3>
      <p class="entity-card-desc">Mellda's reinforced ballistic chambers, seismic dampeners, and anti-breach hydraulic bulkheads.</p>
      <a href="floor-5-border-containment-cells.html" class="jump-btn">ACCESS HIGH CONTAINMENT →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#c084fc;">
      <div class="entity-card-top">
        <img src="../assets/layout/hand/blueprints/floor-6-deep-vault-blueprint.svg" alt="Floor 6 Archives" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-aleph">VAULT-06</span><span class="sector-tag">CLASSIFIED</span></div>
      </div>
      <h3 class="entity-card-name">DEEP VAULT CLASSIFIED ARCHIVES</h3>
      <p class="entity-card-desc">Sealed historical Sorrow Seeds, unexpunged cycle logs, and Dekan's level 5 lockdown records.</p>
      <a href="floor-6-deep-vault-records.html" class="jump-btn">ACCESS DEEP ARCHIVES →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#ef5b55;">
      <div class="entity-card-top">
        <img src="../assets/layout/hand/blueprints/floor-7-shadow-corps-blueprint.svg" alt="Floor 7 Shadow Corps" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-aleph">SHADOW-07</span><span class="sector-tag">TACTICAL</span></div>
      </div>
      <h3 class="entity-card-name">SHADOW CORPS RAPID SUPPRESSION</h3>
      <p class="entity-card-desc">The Outsider Ishall's strike doctrine, 4-man vanguard formations, and lethal suppression rules.</p>
      <a href="floor-7-shadow-corps-operations.html" class="jump-btn">ACCESS STRIKE PROTOCOLS →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#f1df76;">
      <div class="entity-card-top">
        <img src="../assets/layout/hand/blueprints/floor-8-gate-watch-blueprint.svg" alt="Floor 8 Gate Watch" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-waw">GATE-08</span><span class="sector-tag">DESOLATE</span></div>
      </div>
      <h3 class="entity-card-name">GATE WATCH DESOLATE GRIDS</h3>
      <p class="entity-card-desc">The Exile Xyan's frontier barrier cannons, Desolate anomaly radars, and perimeter bulwarks.</p>
      <a href="floor-8-gate-watch-perimeter.html" class="jump-btn">ACCESS GATE DEFENSE →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#c084fc;">
      <div class="entity-card-top">
        <img src="../assets/diagrams/han_flux_resonance_cycle.svg" alt="Emergency Directives" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-aleph">ALL-FLOORS</span><span class="sector-tag">EMERGENCY</span></div>
      </div>
      <h3 class="entity-card-name">FACILITY MELTDOWN PROCEDURES</h3>
      <p class="entity-card-desc">Step-by-step cascade meltdown response timeline, evacuation orders, and Absolvohan failsafe.</p>
      <a href="facility-meltdown-procedures.html" class="jump-btn">ACCESS MELTDOWN CODES →</a>
    </div>
  </div>
'''
        if "id=\"sub-protocols\"" not in content:
            content = content.replace("<!-- Page Footer -->", subpage_section + "\n<!-- Page Footer -->")
            with open(dept_index, "w", encoding="utf-8") as f:
                f.write(content)
            print("Enriched departments/index.html with sub-protocols section!")

    # 2. ENRICH ENTITIES INDEX
    ent_index = os.path.join(base_dir, "entities/index.html")
    if os.path.exists(ent_index):
        with open(ent_index, "r", encoding="utf-8") as f:
            content = f.read()

        ent_subpage_section = '''
  <h2 class="section-title" id="containment-logs" style="margin-top: 3rem;">CONTAINMENT DOSSIERS &amp; FIELD SURVEY ARCHIVES</h2>
  <p class="section-desc">
    Deep-dive containment logs, acoustic spectrograms, seismic breach histories, and tactical suppression guides for recorded Sorrow Entities.
  </p>

  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#38bdf8;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-001.svg" alt="SE-001 Log" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-somna">SE-001</span><span class="sector-tag">ACOUSTIC</span></div>
      </div>
      <h3 class="entity-card-name">SE-001 TOLL &amp; ACOUSTIC LOGS</h3>
      <p class="entity-card-desc">Detailed decibel spectrograms, Cheongula harmonic resonance curves, and work success probabilities.</p>
      <a href="se-001-containment-log.html" class="jump-btn">ACCESS ACOUSTIC LOGS →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#ef5b55;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-002.svg" alt="SE-002 Log" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-waw">SE-002</span><span class="sector-tag">SEISMIC</span></div>
      </div>
      <h3 class="entity-card-name">SE-002 SEISMIC INCIDENT DOSSIER</h3>
      <p class="entity-card-desc">Fissure magma pressure readings, bedrock structural integrity analysis, and suppression battle 002-C.</p>
      <a href="se-002-incident-log.html" class="jump-btn">ACCESS SEISMIC DOSSIER →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#71efaf;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-003.svg" alt="SE-003 Log" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-he">SE-003</span><span class="sector-tag">SURVEY</span></div>
      </div>
      <h3 class="entity-card-name">SE-003 WILDERNESS TIDE SURVEY</h3>
      <p class="entity-card-desc">Fluidic chemical analysis of the Desolate bio-surge, skeletal limb density, and damage multipliers.</p>
      <a href="se-003-field-survey.html" class="jump-btn">ACCESS TIDE SURVEY →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#c084fc;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-005.svg" alt="SE-005 Guide" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-waw">SE-005</span><span class="sector-tag">TACTICAL</span></div>
      </div>
      <h3 class="entity-card-name">SE-005 THREAD SEVERING GUIDE</h3>
      <p class="entity-card-desc">Tactical manual for severing maternal silk bindings, managing agent obsession, and avoiding cocoon traps.</p>
      <a href="se-005-suppression-guide.html" class="jump-btn">ACCESS SEVERING GUIDE →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#38bdf8;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-007.svg" alt="SE-007 Log" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-zayin">SE-007</span><span class="sector-tag">AEROSOL</span></div>
      </div>
      <h3 class="entity-card-name">SE-007 BRUME OBSERVATION LOG</h3>
      <p class="entity-card-desc">Aerosol density thresholds, gas mask filter degradation timelines, and Agent Sora's sensory test logs.</p>
      <a href="se-007-observation-log.html" class="jump-btn">ACCESS BRUME LOGS →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#38bdf8;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-009.svg" alt="SE-009 Extracts" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-he">SE-009</span><span class="sector-tag">DECRYPTION</span></div>
      </div>
      <h3 class="entity-card-name">SE-009 MEMORY WEAVE EXTRACTS</h3>
      <p class="entity-card-desc">Decrypted historical memory tapestries, Old Somnarak civilian transcripts, and weaver spider mechanics.</p>
      <a href="se-009-memory-extracts.html" class="jump-btn">ACCESS MEMORY EXTRACTS →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#c084fc;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-010.svg" alt="SE-010 Verdicts" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-aleph">SE-010</span><span class="sector-tag">SINGULARITY</span></div>
      </div>
      <h3 class="entity-card-name">SE-010 THE CONVERGENCE VERDICTS</h3>
      <p class="entity-card-desc">Gravitational event horizon metrics, erased agents' final words, and Apocrypha Repression work rules.</p>
      <a href="se-010-verdict-records.html" class="jump-btn">ACCESS VERDICT RECORDS →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#38bdf8;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-011.svg" alt="SE-011 Analysis" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-somna">SE-011</span><span class="sector-tag">ACOUSTIC</span></div>
      </div>
      <h3 class="entity-card-name">SE-011 ACOUSTIC WALL ANALYSIS</h3>
      <p class="entity-card-desc">Concrete absorption curves, voice decomposition spectrograms, and Insight psychological isolation.</p>
      <a href="se-011-acoustic-analysis.html" class="jump-btn">ACCESS ACOUSTIC DOSSIER →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#f1df76;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-014.svg" alt="SE-014 Ledger" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-waw">SE-014</span><span class="sector-tag">LEDGER</span></div>
      </div>
      <h3 class="entity-card-name">SE-014 KARMIC DEBT LEDGERS</h3>
      <p class="entity-card-desc">Ingested debt ledger records, currency-to-Han conversion rates, and Instinct feeding schedules.</p>
      <a href="se-014-debt-ledger.html" class="jump-btn">ACCESS DEBT LEDGER →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#f1df76;">
      <div class="entity-card-top">
        <img src="../assets/art/entities/se-015.svg" alt="SE-015 Trials" class="entity-card-icon">
        <div class="entity-card-meta"><span class="risk-badge risk-he">SE-015</span><span class="sector-tag">EQUILIBRIUM</span></div>
      </div>
      <h3 class="entity-card-name">SE-015 MORAL EQUILIBRIUM TRIALS</h3>
      <p class="entity-card-desc">Dual pan calibration logs, heart-vs-tear mass discrepancy records, and Repression stabilization.</p>
      <a href="se-015-equilibrium-trials.html" class="jump-btn">ACCESS TRIAL RECORDS →</a>
    </div>
  </div>
'''
        if "id=\"containment-logs\"" not in content:
            content = content.replace("<!-- Page Footer -->", ent_subpage_section + "\n<!-- Page Footer -->")
            with open(ent_index, "w", encoding="utf-8") as f:
                f.write(content)
            print("Enriched entities/index.html with containment dossiers section!")

    # 3. ENRICH MAW INDEX
    maw_index = os.path.join(base_dir, "maw/index.html")
    if os.path.exists(maw_index):
        with open(maw_index, "r", encoding="utf-8") as f:
            content = f.read()

        maw_subpage_section = '''
  <h2 class="section-title" id="maw-crafting" style="margin-top: 3rem;">M.A.W. FORGING SYSTEMS &amp; SET SYNERGIES</h2>
  <p class="section-desc">
    Complete crystallization equations, extraction prerequisites, and matching set resonance synergy bonuses.
  </p>

  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#f1df76;">
      <div class="entity-card-top">
        <img src="../assets/banners/banner_hero_maw_arsenal.svg" alt="M.A.W. Crafting" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-waw">FORGE</span><span class="sector-tag">EXTRACTION</span></div>
      </div>
      <h3 class="entity-card-name">M.A.W. CRAFTING &amp; EXTRACTION</h3>
      <p class="entity-card-desc">Detailed Han-Flux crystallization costs, agent stat prerequisites, and maintenance protocols.</p>
      <a href="maw-crafting-and-extraction.html" class="jump-btn">ACCESS CRAFTING MATRIX →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#38bdf8;">
      <div class="entity-card-top">
        <img src="../assets/banners/banner_hero_maw_arsenal.svg" alt="M.A.W. Synergies" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-aleph">RESONANCE</span><span class="sector-tag">SYNERGY</span></div>
      </div>
      <h3 class="entity-card-name">M.A.W. FULL SET SYNERGIES</h3>
      <p class="entity-card-desc">Resonance bonuses unlocked by equipping matching Weapon + Suit + Gift sets from the same entity.</p>
      <a href="maw-set-synergies.html" class="jump-btn">ACCESS SET BONUSES →</a>
    </div>
  </div>
'''
        if "id=\"maw-crafting\"" not in content:
            content = content.replace("<!-- Page Footer -->", maw_subpage_section + "\n<!-- Page Footer -->")
            with open(maw_index, "w", encoding="utf-8") as f:
                f.write(content)
            print("Enriched maw/index.html with crafting and synergy sections!")

    # 4. ENRICH LOCATIONS INDEX
    loc_index = os.path.join(base_dir, "locations/index.html")
    if os.path.exists(loc_index):
        with open(loc_index, "r", encoding="utf-8") as f:
            content = f.read()

        loc_subpage_section = '''
  <h2 class="section-title" id="zone-blueprints" style="margin-top: 3rem;">SOMNARAK URBAN ZONE ARCHITECTURAL BLUEPRINTS</h2>
  <p class="section-desc">
    Tactical cartographic schematics, demographic data, and security profiles for all 5 primary civic zones.
  </p>

  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#f1df76;">
      <div class="entity-card-top">
        <img src="../assets/layout/city/blueprints/zone-a-blueprint.svg" alt="Zone A" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-aleph">ZONE A</span><span class="sector-tag">CITADEL</span></div>
      </div>
      <h3 class="entity-card-name">ZONE A: CENTRAL SPIRE</h3>
      <p class="entity-card-desc">High Council administrative bastion, Sovereign Veil filtration grids, and elite residency towers.</p>
      <a href="zone-a-central-spire.html" class="jump-btn">ACCESS ZONE A →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#ef5b55;">
      <div class="entity-card-top">
        <img src="../assets/layout/city/blueprints/zone-b-blueprint.svg" alt="Zone B" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-waw">ZONE B</span><span class="sector-tag">WEST WARD</span></div>
      </div>
      <h3 class="entity-card-name">ZONE B: GILTONG SLUMS</h3>
      <p class="entity-card-desc">Iron alleyways, enforcer patrol routes, weeping gutters, and subterranean market stacks.</p>
      <a href="zone-b-giltong-slums.html" class="jump-btn">ACCESS ZONE B →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#c084fc;">
      <div class="entity-card-top">
        <img src="../assets/layout/city/blueprints/zone-c-blueprint.svg" alt="Zone C" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-waw">ZONE C</span><span class="sector-tag">BAZAAR</span></div>
      </div>
      <h3 class="entity-card-name">ZONE C: COLLECTOR'S ROW</h3>
      <p class="entity-card-desc">Black market relic auctions, contraband Sorrow Seeds, and illegal memory trading posts.</p>
      <a href="zone-c-auction-houses.html" class="jump-btn">ACCESS ZONE C →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#71efaf;">
      <div class="entity-card-top">
        <img src="../assets/layout/city/blueprints/zone-d-blueprint.svg" alt="Zone D" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-he">ZONE D</span><span class="sector-tag">SMELTERS</span></div>
      </div>
      <h3 class="entity-card-name">ZONE D: HAN SMELTERS</h3>
      <p class="entity-card-desc">Colossal thermal refining towers converting raw grief into crystallized power blocks.</p>
      <a href="zone-d-han-refineries.html" class="jump-btn">ACCESS ZONE D →</a>
    </div>

    <div class="pm-entity-card" style="--card-border:#38bdf8;">
      <div class="entity-card-top">
        <img src="../assets/layout/city/blueprints/zone-e-blueprint.svg" alt="Zone E" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-aleph">ZONE E</span><span class="sector-tag">BULWARK</span></div>
      </div>
      <h3 class="entity-card-name">ZONE E: FRONTIER BULWARK</h3>
      <p class="entity-card-desc">80-meter perimeter ramparts, heavy automated railguns, and Desolate repulsion outposts.</p>
      <a href="zone-e-frontier-ramparts.html" class="jump-btn">ACCESS ZONE E →</a>
    </div>
  </div>
'''
        if "id=\"zone-blueprints\"" not in content:
            content = content.replace("<!-- Page Footer -->", loc_subpage_section + "\n<!-- Page Footer -->")
            with open(loc_index, "w", encoding="utf-8") as f:
                f.write(content)
            print("Enriched locations/index.html with zone blueprints section!")

    # 5. ENRICH LORE INDEX
    lore_index = os.path.join(base_dir, "lore/index.html")
    if os.path.exists(lore_index):
        with open(lore_index, "r", encoding="utf-8") as f:
            content = f.read()

        lore_subpage_section = '''
  <h2 class="section-title" id="historical-archives" style="margin-top: 3rem;">CHRONICLES &amp; HISTORICAL ARCHIVES</h2>
  <p class="section-desc">
    Unabridged chronicles of the early sovereign wars, the formation of the Han economy, and the origin of the Veil protocols.
  </p>

  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#f1df76;">
      <div class="entity-card-top">
        <img src="../assets/banners/banner_hero_somnarak_city.svg" alt="Sovereign War" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-aleph">WAR-01</span><span class="sector-tag">CHRONICLE</span></div>
      </div>
      <h3 class="entity-card-name">THE FIRST SOVEREIGN WAR</h3>
      <p class="entity-card-desc">The cataclysmic uprising against the Old Dreamers and the founding of the modern corporate city state.</p>
      <a href="the-first-sovereign-war.html" class="jump-btn">ACCESS CHRONICLE →</a>
    </div>
  </div>
'''
        if "id=\"historical-archives\"" not in content:
            content = content.replace("<!-- Page Footer -->", lore_subpage_section + "\n<!-- Page Footer -->")
            with open(lore_index, "w", encoding="utf-8") as f:
                f.write(content)
            print("Enriched lore/index.html with historical archives section!")

    # 6. ENRICH MECHANICS INDEX
    mech_index = os.path.join(base_dir, "mechanics/index.html")
    if os.path.exists(mech_index):
        with open(mech_index, "r", encoding="utf-8") as f:
            content = f.read()

        mech_subpage_section = '''
  <h2 class="section-title" id="combat-psychology" style="margin-top: 3rem;">COMBAT PSYCHOLOGY &amp; CORROSION GUIDELINES</h2>
  <p class="section-desc">
    Technical breakdowns of Sanity Point degradation, the 4 Panic behaviors, and M.A.W. Corrosion triggers.
  </p>

  <div class="hub-grid-3">
    <div class="pm-entity-card" style="--card-border:#ef5b55;">
      <div class="entity-card-top">
        <img src="../assets/diagrams/four_work_types_matrix.svg" alt="Panic &amp; Corrosion" class="entity-card-icon" style="border-radius:4px;">
        <div class="entity-card-meta"><span class="risk-badge risk-aleph">PSYCH-04</span><span class="sector-tag">TACTICAL</span></div>
      </div>
      <h3 class="entity-card-name">PANIC STATES &amp; M.A.W. CORROSION</h3>
      <p class="entity-card-desc">Murderous, Wandering, Paralyzed, and Fanatic behaviors, SP restoration, and weapon corrosion overrides.</p>
      <a href="panic-states-and-corrosion.html" class="jump-btn">ACCESS PSYCH MANUAL →</a>
    </div>
  </div>
'''
        if "id=\"combat-psychology\"" not in content:
            content = content.replace("<!-- Page Footer -->", mech_subpage_section + "\n<!-- Page Footer -->")
            with open(mech_index, "w", encoding="utf-8") as f:
                f.write(content)
            print("Enriched mechanics/index.html with combat psychology section!")

if __name__ == "__main__":
    enrich_hubs()
