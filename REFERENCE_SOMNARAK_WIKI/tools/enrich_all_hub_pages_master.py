#!/usr/bin/env python3
"""
tools/enrich_all_hub_pages_master.py
Enriches characters/index.html, locations/index.html, lore/index.html,
mechanics/index.html, departments/index.html, and factions/index.html
with comprehensive encyclopedic overviews, master comparison tables,
operational lore, and deep data matrices.
"""

import os, re

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# =========================================================================
# 1. ENRICH CHARACTERS HUB (characters/index.html)
# =========================================================================
def enrich_characters_hub():
    path = os.path.join(WIKI_DIR, "characters/index.html")
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    # Find where the cards end (before footer)
    insert_point = c.rfind("</div>\n</div>\n\n\n      <!-- Master Footer Navigation -->")
    if insert_point == -1:
        insert_point = c.rfind("<!-- Master Footer Navigation -->")

    encyclopedia_content = """
<!-- Master Encyclopedic Sections for Characters Hub -->
<section class="pm-section-block">
  <div class="section-title-bar">
    <h2>/// EXECUTIVE COMMAND & SYNTHETIC ECHO-CORE REBIRTH</h2>
    <span class="title-sub">THE ARCHITECTURE OF IMMORTAL LEADERSHIP</span>
  </div>
  <p class="section-lead-text">
    The command structure of the <a href="../factions/the-reverie-directorate.html" class="wiki-link">Reverie Directorate</a> is anchored upon nine synthetic humanoids known as the <strong>Echo-Core Leads</strong>. Originally high-ranking mortal researchers and commanders during the First Age of Founding, each lead underwent voluntary cranial core extraction to anchor a specific sector of Facility 01. Encased in reinforced bio-mechanical chassis infused with purified Han flux, they are impervious to natural aging, disease, and standard physical trauma.
  </p>
  <p class="section-lead-text">
    However, this immortality carries a catastrophic psychological cost: across 1,778 recorded facility resets, each Echo-Core lead retains fragmented traumatic memories of every containment failure, operative death, and apocalyptic breach. Maintaining their psychological stability—or preventing their "Resonance Corrosion"—is the primary duty of <a href="the-secretary-seiyon.html" class="wiki-link">Secretary Seiyon</a> and <a href="the-director-majin.html" class="wiki-link">Director Majin</a>.
  </p>
</section>

<section class="pm-section-block">
  <div class="section-title-bar">
    <h2>/// MASTER PERSONNEL ROSTER & OPERATIONAL DIRECTORY</h2>
    <span class="title-sub">COMPLETE 19-MEMBER ARCHIVAL MATRIX</span>
  </div>
  <div class="pm-table-wrapper">
    <table class="pm-table">
      <thead>
        <tr>
          <th>Personnel / Designation</th>
          <th>Rank / Title</th>
          <th>Sector Assignment</th>
          <th>Primary Specialization</th>
          <th>Han Resonance</th>
          <th>Archival Dossier</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:#ef5b55;"><img src="../assets/avatars/avatar_core_majin.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Director Majin</strong></td>
          <td>Supreme Arch-Architect</td>
          <td>Floor 1 (Neutral Core)</td>
          <td>Executive Command, Cycle Memory Preservation, System Architecture</td>
          <td><span class="risk-badge risk-aleph">ALEPH (100%)</span></td>
          <td><a href="the-director-majin.html" class="wiki-link">View Dossier →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#6366f1;"><img src="../assets/avatars/avatar_core_seiyon.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Secretary Seiyon</strong></td>
          <td>Executive Administrator</td>
          <td>Floor 1 (Neutral Core)</td>
          <td>Resource Logistics, Mental Stability Diagnostics, Cycle Reset Cadence</td>
          <td><span class="risk-badge risk-waw">WAW (92%)</span></td>
          <td><a href="the-secretary-seiyon.html" class="wiki-link">View Dossier →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#38bdf8;"><img src="../assets/avatars/avatar_core_dekan.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Dekan</strong></td>
          <td>Containment Marshal</td>
          <td>Floor 2 (Maw's Keep)</td>
          <td>Heavy Kinetic Suppression, Airlock Integrity, High-Mass Entity Restraint</td>
          <td><span class="risk-badge risk-waw">WAW (88%)</span></td>
          <td><a href="the-containment-lead-dekan.html" class="wiki-link">View Dossier →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#f59e0b;"><img src="../assets/avatars/avatar_core_zyrak.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Zyrak</strong></td>
          <td>Extraction Overseer</td>
          <td>Floor 3 (Extraction Hall)</td>
          <td>Han-Flux Refining, Thermal Purification, Energy Grid Regulation</td>
          <td><span class="risk-badge risk-waw">WAW (85%)</span></td>
          <td><a href="the-extraction-lead-zyrak.html" class="wiki-link">View Dossier →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#10b981;"><img src="../assets/avatars/avatar_core_ayshuk.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Ayshuk</strong></td>
          <td>Chief Scholar</td>
          <td>Floor 4 (Insight Forge)</td>
          <td>M.A.W. Equipment Forging, Neurological Scanning, Psychological Profiling</td>
          <td><span class="risk-badge risk-he">HE (79%)</span></td>
          <td><a href="the-research-lead-ayshuk.html" class="wiki-link">View Dossier →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#e2e8f0;"><img src="../assets/avatars/avatar_core_mellda.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Mellda</strong></td>
          <td>Perimeter Warden</td>
          <td>Floor 5 (Border Watch)</td>
          <td>Subterranean Border Patrol, Effluent Flood Barriers, Night Infiltration Defense</td>
          <td><span class="risk-badge risk-waw">WAW (86%)</span></td>
          <td><a href="the-border-lead-mellda.html" class="wiki-link">View Dossier →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#be123c;"><img src="../assets/avatars/avatar_core_marjuk.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Marjuk</strong></td>
          <td>Grand Archivist</td>
          <td>Floor 6 (Deep Vault)</td>
          <td>Lost Cycle Stele Translation, Taboo Curation, Memory Reclamation</td>
          <td><span class="risk-badge risk-aleph">ALEPH (95%)</span></td>
          <td><a href="the-archive-lead-marjuk.html" class="wiki-link">View Dossier →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#a855f7;"><img src="../assets/avatars/avatar_core_ishall.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Ishall</strong></td>
          <td>Covert Commander</td>
          <td>Floor 7 (Shadow Corps)</td>
          <td>Breach Infiltration, Rogue Aberration Elimination, Covert Execution</td>
          <td><span class="risk-badge risk-aleph">ALEPH (96%)</span></td>
          <td><a href="the-shadow-lead-ishall.html" class="wiki-link">View Dossier →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#fbbf24;"><img src="../assets/avatars/avatar_core_xyan.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Lead Xyan</strong></td>
          <td>Gate Sentinel</td>
          <td>Floor 8 (Gate Watch)</td>
          <td>Cheongula Seal Enforcement, Sub-Basement Defense, Void Resonance Barriers</td>
          <td><span class="risk-badge risk-aleph">ALEPH (98%)</span></td>
          <td><a href="the-exile-lead-xyan.html" class="wiki-link">View Dossier →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#38bdf8;"><img src="../assets/avatars/avatar_char_minho.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Agent Minho</strong></td>
          <td>Senior Recon Operative</td>
          <td>SED Field Division</td>
          <td>Frontline Sorrow Entity Observation, Scout Infiltration, Kinetic Extraction</td>
          <td><span class="risk-badge risk-he">HE (72%)</span></td>
          <td><a href="agent-minho.html" class="wiki-link">View Profile →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#f1df76;"><img src="../assets/avatars/avatar_char_doha.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Merchant Doha</strong></td>
          <td>Master Appraiser</td>
          <td>The Maw Bazaar (District 3)</td>
          <td>Black-Market Han Vials, Relic Trading, Smuggled M.A.W. Components</td>
          <td><span class="risk-badge risk-can">CAN (45%)</span></td>
          <td><a href="merchant-doha.html" class="wiki-link">View Profile →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#06b6d4;"><img src="../assets/avatars/avatar_char_soojin.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Researcher Soojin</strong></td>
          <td>Subterranean Biologist</td>
          <td>Alpha Root Labs (Zone A)</td>
          <td>Alpha Tree Effluent Ecology, Bio-Resonance Culture, Crystal Growth</td>
          <td><span class="risk-badge risk-waw">WAW (81%)</span></td>
          <td><a href="researcher-soojin.html" class="wiki-link">View Profile →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#f59e0b;"><img src="../assets/avatars/avatar_char_sora.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Civilian Sora</strong></td>
          <td>Memory Custodian</td>
          <td>District 4 Flanks</td>
          <td>Preservation of Lost Folk Songs, Cheonbulok Relic Care, Civilian Morale</td>
          <td><span class="risk-badge risk-can">CAN (30%)</span></td>
          <td><a href="sora-civilian.html" class="wiki-link">View Profile →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#ef4444;"><img src="../assets/avatars/avatar_char_taeho.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Captain Taeho</strong></td>
          <td>Breach Strike Commander</td>
          <td>UCD Division (Zone E)</td>
          <td>Tactical Breaching, Rapid Suppressive Force, District Perimeter Defense</td>
          <td><span class="risk-badge risk-waw">WAW (87%)</span></td>
          <td><a href="captain-taeho.html" class="wiki-link">View Profile →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#d97706;"><img src="../assets/avatars/avatar_char_kael.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Caravan Master Kael</strong></td>
          <td>Expedition Leader</td>
          <td>The Desolate Wasteland</td>
          <td>Wasteland Navigation, Forgotten City Relic Salvage, Sand Crawler Transit</td>
          <td><span class="risk-badge risk-he">HE (76%)</span></td>
          <td><a href="kael-caravan-master.html" class="wiki-link">View Profile →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#a855f7;"><img src="../assets/avatars/avatar_char_yeonhwa.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Weaver Yeonhwa</strong></td>
          <td>Grand Loom Artisan</td>
          <td>Weavers Guild (District 2)</td>
          <td>Han-Silk Spinning, M.A.W. Suit Weaving, Protective Veil Crafting</td>
          <td><span class="risk-badge risk-he">HE (78%)</span></td>
          <td><a href="yeonhwa-weaver.html" class="wiki-link">View Profile →</a></td>
        </tr>
        <tr>
          <td><strong style="color:#ea580c;"><img src="../assets/avatars/avatar_char_joon.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Engineer Joon</strong></td>
          <td>Heavy Systems Chief</td>
          <td>Facility Maintenance Corps</td>
          <td>Hydraulic Pressure Regulation, Airlock Welding, Emergency Power Generators</td>
          <td><span class="risk-badge risk-can">CAN (52%)</span></td>
          <td><a href="engineer-joon.html" class="wiki-link">View Profile →</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="pm-section-block">
  <div class="section-title-bar">
    <h2>/// INTER-LEAD DYNAMICS & PROCEDURAL FRICTION</h2>
    <span class="title-sub">CONFLICTS AND COOPERATION IN FACILITY 01</span>
  </div>
  <p class="section-lead-text">
    The operational survival of Facility 01 depends on fragile psychological alliances among the Leads:
  </p>
  <ul>
    <li><strong>Dekan vs. Zyrak (Containment vs. Yield)</strong>: Containment Lead Dekan prioritizes operative safety and kinetic restraint, frequently clashing with Extraction Lead Zyrak, who demands prolonged entity stimulation to maximize pure Han-flux energy quotas.</li>
    <li><strong>Ayshuk vs. Marjuk (Innovation vs. Taboo)</strong>: Research Lead Ayshuk continually attempts to reverse-engineer forbidden cognitive patterns from Aleph-class entities, repeatedly triggering official archival vetoes and seal enforcement from Grand Archivist Marjuk.</li>
    <li><strong>Mellda vs. Ishall (Frontline Watch vs. Shadow Intervention)</strong>: Border Lead Mellda maintains formal defensive barricades along the effluent canals, often finding her command compromised by unannounced assassinations conducted by Lead Ishall's Shadow Corps.</li>
  </ul>
</section>
"""

    if "/// EXECUTIVE COMMAND & SYNTHETIC ECHO-CORE REBIRTH" not in c:
        # replace the end of cards with cards + encyclopedia
        c = c[:insert_point] + encyclopedia_content + c[insert_point:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(c)
        print("Enriched characters/index.html with master encyclopedia sections!")

# =========================================================================
# 2. ENRICH LOCATIONS HUB (locations/index.html)
# =========================================================================
def enrich_locations_hub():
    path = os.path.join(WIKI_DIR, "locations/index.html")
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    insert_point = c.rfind("<!-- Master Footer Navigation -->")

    encyclopedia_content = """
<!-- Master Encyclopedic Sections for Locations Hub -->
<section class="pm-section-block">
  <div class="section-title-bar">
    <h2>/// CARTOGRAPHIC OVERVIEW: THE METROPOLITAN CONCENTRIC RINGS</h2>
    <span class="title-sub">URBAN ZONING & SUBTERRANEAN DEPTH METRICS</span>
  </div>
  <p class="section-lead-text">
    The city of <strong>Somnarak</strong> is structured as five concentric urban zones encircling the colossal <a href="../lore/the-alpha-tree.html" class="wiki-link">Alpha Tree</a>. Beneath this surface sprawl lies the subterranean chasm known as <a href="the-maw.html" class="wiki-link">The Maw</a>, through which the toxic, bioluminescent waters of the Weeping river carve into the dark bedrock. Beyond the outermost defensive bulwark lies <a href="the-desolate.html" class="wiki-link">The Desolate</a>—thousands of square kilometers of scorched wasteland littered with petrified ruins of pre-Cycle civilizations.
  </p>
</section>

<section class="pm-section-block">
  <div class="section-title-bar">
    <h2>/// MASTER METROPOLITAN DISTRICT & GEOGRAPHIC MATRIX</h2>
    <span class="title-sub">POPULATION, HAZARDS, AND MILITARY GARRISONS</span>
  </div>
  <div class="pm-table-wrapper">
    <table class="pm-table">
      <thead>
        <tr>
          <th>District / Landmark</th>
          <th>Zone / Location</th>
          <th>Han Density</th>
          <th>Civilian Population</th>
          <th>Primary Environmental Hazard</th>
          <th>Defensive Garrison</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:#f1df76;"><img src="../assets/layout/city/icons/icon_zone_a_core.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Zone A: Core Spire</strong></td>
          <td>Metropolitan Center</td>
          <td>Extremely High (Pure Flux)</td>
          <td>~45,000 (Directorate Staff)</td>
          <td>Resonant cognitive saturation, spatial warp anomalies</td>
          <td>Directorate Elite Honor Guard & Automated Spires</td>
        </tr>
        <tr>
          <td><strong style="color:#f97316;"><img src="../assets/layout/city/icons/icon_zone_b_west.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Zone B: West Ward</strong></td>
          <td>Western Quadrant</td>
          <td>High (Combustion Vapor)</td>
          <td>~280,000 (Refinery Workers)</td>
          <td>Thermal exhaust bursts, toxic particulate clouds</td>
          <td>SED Industrial Suppression Corps</td>
        </tr>
        <tr>
          <td><strong style="color:#38bdf8;"><img src="../assets/layout/city/icons/icon_zone_c_east.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Zone C: East Arcology</strong></td>
          <td>Eastern Quadrant</td>
          <td>Moderate (Refracted Wave)</td>
          <td>~420,000 (Commercial/Guilds)</td>
          <td>Corporate espionage, memory theft, data corruption</td>
          <td>High Council Private Enforcers & Giltong Units</td>
        </tr>
        <tr>
          <td><strong style="color:#10b981;"><img src="../assets/layout/city/icons/icon_zone_d_flanks.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Zone D: The Flanks</strong></td>
          <td>Southern & Northern Flanks</td>
          <td>Low to Moderate</td>
          <td>~650,000 (Tenements/Citizens)</td>
          <td>Effluent seepage, black-market violence, structural decay</td>
          <td>Urban Containment Division (UCD) Regulars</td>
        </tr>
        <tr>
          <td><strong style="color:#ef4444;"><img src="../assets/layout/city/icons/icon_zone_e_bulwark.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Zone E: Outer Bulwark</strong></td>
          <td>Perimeter Ring Wall</td>
          <td>Variable (Wasteland Spill)</td>
          <td>~90,000 (Border Wardens)</td>
          <td>Night Aberration assaults, howling radiation dust</td>
          <td>Bulwark Heavy Bastion Artillery & Border Wardens</td>
        </tr>
        <tr>
          <td><strong style="color:#38bdf8;"><img src="../assets/icons/icon_loc_the_maw.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">The Maw</strong></td>
          <td>Subterranean Chasm</td>
          <td>Critical (Unrefined Abyss)</td>
          <td>~15,000 (Salvagers/Miners)</td>
          <td>Abyssal vortex suction, Coherence loss, drowning</td>
          <td>Floor 2 Keep Sentinels & Hydraulic Gates</td>
        </tr>
        <tr>
          <td><strong style="color:#ef4444;"><img src="../assets/icons/icon_loc_the_desolate.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">The Desolate</strong></td>
          <td>Outer Wastelands</td>
          <td>Corrosive Void Flux</td>
          <td>Nomadic (Caravans Only)</td>
          <td>Perpetual dust storms, petrified entity corpses</td>
          <td>Horizon Armored Crawler convoys</td>
        </tr>
        <tr>
          <td><strong style="color:#38bdf8;"><img src="../assets/icons/icon_loc_the_hollow_glass.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">The Hollow Glass</strong></td>
          <td>Northern Desert Anomaly</td>
          <td>Prismatic Refraction</td>
          <td>Uninhabited</td>
          <td>Psychic hallucinations, chronological echo loops</td>
          <td>Restricted Exclusion Zone (Automated Beacons)</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
"""

    if "/// CARTOGRAPHIC OVERVIEW: THE METROPOLITAN CONCENTRIC RINGS" not in c:
        c = c[:insert_point] + encyclopedia_content + c[insert_point:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(c)
        print("Enriched locations/index.html with master encyclopedia sections!")

# =========================================================================
# 3. ENRICH LORE HUB (lore/index.html)
# =========================================================================
def enrich_lore_hub():
    path = os.path.join(WIKI_DIR, "lore/index.html")
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    insert_point = c.rfind("<!-- Master Footer Navigation -->")

    encyclopedia_content = """
<!-- Master Encyclopedic Sections for Lore Hub -->
<section class="pm-section-block">
  <div class="section-title-bar">
    <h2>/// THE METAPHYSICS OF HAN & COSMOLOGICAL STRUCTURE</h2>
    <span class="title-sub">THE EMOTIONAL PRESSURE THAT SHAPES REALITY</span>
  </div>
  <p class="section-lead-text">
    In the cosmology of Somnarak, <strong>Han (한)</strong> is not mere emotion, but a fundamental metaphysical law of conservation. Whenever human grief, righteous indignation, unavenged death, or profound sacrifice is denied resolution or forced into silence, the psychic resonance accumulates as physical pressure within the bedrock of the world. 
  </p>
  <p class="section-lead-text">
    Drawing this subterranean effluent upward, the <a href="the-alpha-tree.html" class="wiki-link">Alpha Tree</a> converts raw Han into the radiant energy that illuminates and powers the metropolitan sectors. However, when unrefined Han reaches critical saturation thresholds, it manifests spontaneously as monstrous, sentient entities known as <strong>Sorrow Entities</strong>.
  </p>
</section>

<section class="pm-section-block">
  <div class="section-title-bar">
    <h2>/// THE 1,778 CYCLES CHRONOLOGY & ERA BREAKDOWN</h2>
    <span class="title-sub">THE HISTORICAL CHRONOLOGY OF THE METROPOLIS</span>
  </div>
  <div class="pm-table-wrapper">
    <table class="pm-table">
      <thead>
        <tr>
          <th>Historical Era</th>
          <th>Cycle Range</th>
          <th>Key Historical Epochs</th>
          <th>Technological & Societal Breakthroughs</th>
          <th>Major Cataclysms</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:#f1df76;">The First Age (Founding)</strong></td>
          <td>Cycles 001 – 210</td>
          <td>Discovery of the Alpha Tree seedling and the subterranean Weeping by Director Majin.</td>
          <td>Construction of Facility 01; voluntary synthesis of the First Generation Echo-Core Leads.</td>
          <td>The First Great Collapse; emergence of SE-001 (The Weeping Colossus).</td>
        </tr>
        <tr>
          <td><strong style="color:#38bdf8;">The Second Age (Containment)</strong></td>
          <td>Cycles 211 – 1,140</td>
          <td>Establishment of the 4 Work Types (Observation, Extraction, Insight, Restraint).</td>
          <td>Invention of M.A.W. equipment materialization by Lead Ayshuk; expansion of Zones B and C.</td>
          <td>The Cheongula Deep Vault Breach; sealing of Floor 8 by Lead Xyan.</td>
        </tr>
        <tr>
          <td><strong style="color:#ef4444;">The Third Age (Silence & Resets)</strong></td>
          <td>Cycles 1,141 – 1,777</td>
          <td>Implementation of the Cycle Reset Protocol by Secretary Seiyon and Director Majin.</td>
          <td>Memory wiping technologies, creation of the Amnestic Corps, synthesis of Aleph-grade gear.</td>
          <td>1,777 complete facility resets to prevent global Efflorescence and total urban crystallization.</td>
        </tr>
        <tr>
          <td><strong style="color:#71efaf;">The Present Cycle (Cycle 1,778)</strong></td>
          <td>Cycle 1,778 (Active)</td>
          <td>The Dawn Initiative; ongoing operations under Code Amber alert status.</td>
          <td>Deployment of tactical radar networks, stabilization of all 8 facility sectors.</td>
          <td>Current status: 137 verified canonical records actively maintained.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="pm-section-block">
  <div class="section-title-bar">
    <h2>/// THE SEVEN ABSOLUTE TABOOS OF SOMNARAK</h2>
    <span class="title-sub">SACRED PROHIBITIONS ENFORCED BY THE DIRECTORATE</span>
  </div>
  <div class="pm-table-wrapper">
    <table class="pm-table">
      <thead>
        <tr>
          <th>Taboo Number</th>
          <th>Prohibition Mandate</th>
          <th>Metaphysical Rationale</th>
          <th>Enforcement Division</th>
          <th>Penalty for Infraction</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Taboo I</strong></td>
          <td><strong>Denial of the Name (이름의 부정)</strong></td>
          <td>Erasing or refusing to speak the true name of a fallen operative causes immediate Han crystallization.</td>
          <td>Grand Archivist Marjuk</td>
          <td>Permanent extraction to Floor 6 Memorial Stele.</td>
        </tr>
        <tr>
          <td><strong>Taboo II</strong></td>
          <td><strong>Unfiltered Doorspeech (비정제 문언)</strong></td>
          <td>Speaking directly to high-threat entities without acoustic frequency baffles induces irreversible cognitive rupture.</td>
          <td>Lead Dekan (Maw's Keep)</td>
          <td>Mandatory vocal chord neural dampening.</td>
        </tr>
        <tr>
          <td><strong>Taboo III</strong></td>
          <td><strong>Unauthorized Effluent Consumption</strong></td>
          <td>Drinking raw liquid from the Weeping causes violent physical mutation into a Night Aberration.</td>
          <td>Border Watch Mellda</td>
          <td>Immediate kinetic liquidation by SED Strike Units.</td>
        </tr>
        <tr>
          <td><strong>Taboo IV</strong></td>
          <td><strong>Artificial Memory Duplication</strong></td>
          <td>Cloning conscious memories across resets corrupts the Alpha Tree root resonance frequency.</td>
          <td>Secretary Seiyon</td>
          <td>Complete core memory scrubbing via Amnestic Slate.</td>
        </tr>
        <tr>
          <td><strong>Taboo V</strong></td>
          <td><strong>Unsealed Cheongula Descent</strong></td>
          <td>Breaching Floor 8's subterranean iron gates risks unsealing the primordial Void chasm.</td>
          <td>Gate Sentinel Xyan</td>
          <td>Terminal exile into The Desolate wasteland.</td>
        </tr>
        <tr>
          <td><strong>Taboo VI</strong></td>
          <td><strong>Desecration of M.A.W. Relics</strong></td>
          <td>Selling or altering extracted weapons without Directorate appraisal causes catastrophic M.A.W. corrosion.</td>
          <td>UCD Commander Taeho</td>
          <td>Asset confiscation and labor reassignment.</td>
        </tr>
        <tr>
          <td><strong>Taboo VII</strong></td>
          <td><strong>Rejection of the Cycle Reset</strong></td>
          <td>Attempting to sabotage the facility reset protocol dooms the city to total Efflorescence petrification.</td>
          <td>Director Majin</td>
          <td>Permanent cranial core extraction and isolation.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
"""

    if "/// THE METAPHYSICS OF HAN & COSMOLOGICAL STRUCTURE" not in c:
        c = c[:insert_point] + encyclopedia_content + c[insert_point:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(c)
        print("Enriched lore/index.html with master encyclopedia sections!")

# =========================================================================
# 4. ENRICH MECHANICS HUB (mechanics/index.html)
# =========================================================================
def enrich_mechanics_hub():
    path = os.path.join(WIKI_DIR, "mechanics/index.html")
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    insert_point = c.rfind("<!-- Master Footer Navigation -->")

    encyclopedia_content = """
<!-- Master Encyclopedic Sections for Mechanics Hub -->
<section class="pm-section-block">
  <div class="section-title-bar">
    <h2>/// THE FOUR WORK TYPES & PSYCHOLOGICAL RESPONSE DYNAMICS</h2>
    <span class="title-sub">OPERATIVE WORK PROCEDURES & RISK CALCULATION</span>
  </div>
  <p class="section-lead-text">
    When containing a Sorrow Entity, agents perform one of four standardized work routines to harvest Han-flux while maintaining the entity's Coherence Counter. Each work type interacts with specific agent attributes:
  </p>
  <div class="pm-table-wrapper">
    <table class="pm-table">
      <thead>
        <tr>
          <th>Work Routine</th>
          <th>Han Protocol Name</th>
          <th>Primary Scaling Stat</th>
          <th>Operative Procedure</th>
          <th>Failure Consequence</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:#ef4444;"><img src="../assets/icons/work_instinct.svg" alt="" style="width:18px;vertical-align:middle;margin-right:6px;">Observation</strong></td>
          <td><em>Pugnahan (투쟁한)</em></td>
          <td><strong>Fortitude (체력/HP)</strong></td>
          <td>Direct sensory monitoring, physical threat deterrence, and bio-metric vital recording.</td>
          <td>Physical trauma and Grudge damage backlashes against the operative.</td>
        </tr>
        <tr>
          <td><strong style="color:#38bdf8;"><img src="../assets/icons/work_extraction.svg" alt="" style="width:18px;vertical-align:middle;margin-right:6px;">Extraction</strong></td>
          <td><em>Ferrehan (수렴한)</em></td>
          <td><strong>Prudence (정신력/SP)</strong></td>
          <td>Attaching hydraulic needles to draw liquefied Han flux into facility storage batteries.</td>
          <td>Lament damage; severe mental exhaustion and auditory hallucinations.</td>
        </tr>
        <tr>
          <td><strong style="color:#10b981;"><img src="../assets/icons/work_insight.svg" alt="" style="width:18px;vertical-align:middle;margin-right:6px;">Insight</strong></td>
          <td><em>Viderehan (통찰한)</em></td>
          <td><strong>Temperance (숙련도)</strong></td>
          <td>Environmental conditioning, chamber optimization, and cognitive communion.</td>
          <td>Void damage; reduction in work efficiency and potential chamber contamination.</td>
        </tr>
        <tr>
          <td><strong style="color:#f1df76;"><img src="../assets/icons/work_repression.svg" alt="" style="width:18px;vertical-align:middle;margin-right:6px;">Restraint</strong></td>
          <td><em>Flerehan (억제한)</em></td>
          <td><strong>Justice (정의/속도)</strong></td>
          <td>Imposing magnetic suppression fields, sensory deprivation, and acoustic dampening.</td>
          <td>Coherence Counter reduction; triggers immediate breach alerts if zeroed.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="pm-section-block">
  <div class="section-title-bar">
    <h2>/// THE ORDEALS FRAMEWORK: 24-HOUR BREACH ESCALATIONS</h2>
    <span class="title-sub">SYSTEMIC FACILITY EMERGENCIES THROUGHOUT THE CYCLE</span>
  </div>
  <p class="section-lead-text">
    As the daily energy quota increases, unrefined Han seepage precipitates systemic crises known as <strong>Ordeals</strong> at specific time milestones:
  </p>
  <div class="pm-table-wrapper">
    <table class="pm-table">
      <thead>
        <tr>
          <th>Ordeal Phase</th>
          <th>Color Spectrum</th>
          <th>Trigger Threshold</th>
          <th>Manifestation Form</th>
          <th>Recommended Suppression Strategy</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:#10b981;">Dawn (새벽)</strong></td>
          <td>Green / Amber / Crimson</td>
          <td>25% Daily Quota</td>
          <td>Small swarms of crystalline parasites and malfunctioning maintenance drones.</td>
          <td>Fast level I-II operatives with standard kinetic sidearms.</td>
        </tr>
        <tr>
          <td><strong style="color:#38bdf8;">Noon (정오)</strong></td>
          <td>Cyan / Violet</td>
          <td>50% Daily Quota</td>
          <td>Heavily armored Han seep golems and sensory disruption pillars.</td>
          <td>Dedicated strike teams equipped with Lament & Grudge M.A.W. gear.</td>
        </tr>
        <tr>
          <td><strong style="color:#ef4444;">Dusk (황혼)</strong></td>
          <td>Crimson / Blood Gold</td>
          <td>75% Daily Quota</td>
          <td>Colossal mobile obelisks that drain surrounding containment counters.</td>
          <td>Full department mobilization; prioritize destroying obelisk cores immediately.</td>
        </tr>
        <tr>
          <td><strong style="color:#a855f7;">Midnight (자정)</strong></td>
          <td>Obsidian / Pure Pale</td>
          <td>100% Daily Quota</td>
          <td>Catastrophic apocalyptic manifestations capable of facility-wide wipes.</td>
          <td>Deployment of Aleph-grade M.A.W. specialists and Echo-Core direct intervention.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
"""

    if "/// THE FOUR WORK TYPES & PSYCHOLOGICAL RESPONSE DYNAMICS" not in c:
        c = c[:insert_point] + encyclopedia_content + c[insert_point:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(c)
        print("Enriched mechanics/index.html with master encyclopedia sections!")

# =========================================================================
# 5. ENRICH DEPARTMENTS HUB (departments/index.html)
# =========================================================================
def enrich_departments_hub():
    path = os.path.join(WIKI_DIR, "departments/index.html")
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    insert_point = c.rfind("<!-- Master Footer Navigation -->")

    encyclopedia_content = """
<!-- Master Encyclopedic Sections for Departments Hub -->
<section class="pm-section-block">
  <div class="section-title-bar">
    <h2>/// FACILITY 01 STRUCTURAL BLUEPRINT & SUBTERRANEAN HIERARCHY</h2>
    <span class="title-sub">THE 8 TIERS OF THE HAND OF CHANGE</span>
  </div>
  <p class="section-lead-text">
    The <a href="../atlas/hand-of-change-map.html" class="wiki-link">Hand of Change (Facility 01)</a> is an inverted brutalist ziggurat descending hundreds of meters beneath the urban bedrock. Divided into upper, middle, and lower strata, its 8 floors operate with strict compartmentalization to prevent cascaded containment breaches from reaching the surface districts.
  </p>
  <div class="pm-table-wrapper">
    <table class="pm-table">
      <thead>
        <tr>
          <th>Tier / Layer</th>
          <th>Included Floors</th>
          <th>Sector Leads</th>
          <th>Operational Focus</th>
          <th>Emergency Lockdown Protocol</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Upper Strata (Command & Keep)</strong></td>
          <td>Floor 1 (Neutral Core)<br>Floor 2 (Maw's Keep)</td>
          <td>Director Majin<br>Lead Dekan</td>
          <td>Facility administration, logistics, and high-mass containment.</td>
          <td>Primary hydraulic blast gates isolate elevators to surface.</td>
        </tr>
        <tr>
          <td><strong>Middle Strata (Refining & Research)</strong></td>
          <td>Floor 3 (Extraction Hall)<br>Floor 4 (Insight Forge)<br>Floor 5 (Border Watch)</td>
          <td>Lead Zyrak<br>Lead Ayshuk<br>Lead Mellda</td>
          <td>Energy refining, M.A.W. weapon synthesis, and effluent perimeter watch.</td>
          <td>Thermal vent purging and localized laser containment grids.</td>
        </tr>
        <tr>
          <td><strong>Lower Strata (Deep Vault & Threshold)</strong></td>
          <td>Floor 6 (Deep Vault)<br>Floor 7 (Shadow Corps)<br>Floor 8 (Gate Watch)</td>
          <td>Lead Marjuk<br>Lead Ishall<br>Lead Xyan</td>
          <td>Classified taboos, covert strike operations, and Cheongula gate defense.</td>
          <td>Complete subterranean bulkhead seal; total isolation from grid.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
"""

    if "/// FACILITY 01 STRUCTURAL BLUEPRINT & SUBTERRANEAN HIERARCHY" not in c:
        c = c[:insert_point] + encyclopedia_content + c[insert_point:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(c)
        print("Enriched departments/index.html with master encyclopedia sections!")

# =========================================================================
# 6. ENRICH FACTIONS HUB (factions/index.html)
# =========================================================================
def enrich_factions_hub():
    path = os.path.join(WIKI_DIR, "factions/index.html")
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    insert_point = c.rfind("<!-- Master Footer Navigation -->")

    encyclopedia_content = """
<!-- Master Encyclopedic Sections for Factions Hub -->
<section class="pm-section-block">
  <div class="section-title-bar">
    <h2>/// THE SOCIO-POLITICAL POWER STRUCTURE OF SOMNARAK</h2>
    <span class="title-sub">GOVERNING BODIES, GUILDS, AND THE BALANCE OF FORCE</span>
  </div>
  <p class="section-lead-text">
    Governance in Somnarak is divided between the totalitarian technological mandate of the <strong>Reverie Directorate</strong>, the commercial influence of the <strong>High Council of Sights</strong>, and specialized craft guilds such as the <strong>High Architects</strong> and <strong>Master Weavers</strong>.
  </p>
  <div class="pm-table-wrapper">
    <table class="pm-table">
      <thead>
        <tr>
          <th>Faction / Guild</th>
          <th>Governance Role</th>
          <th>Key Leadership</th>
          <th>Primary Technology</th>
          <th>Relationship to Directorate</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:#ef5b55;"><img src="../assets/icons/icon_faction_reverie_directorate.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Reverie Directorate</strong></td>
          <td>Supreme Metropolitan Authority</td>
          <td>Director Majin</td>
          <td>Facility 01, Han Energy Extraction, Echo-Cores</td>
          <td>Ruler / Central Government</td>
        </tr>
        <tr>
          <td><strong style="color:#f1df76;"><img src="../assets/icons/icon_faction_high_council.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">High Council of Sights</strong></td>
          <td>Commercial & Guild Oligarchy</td>
          <td>The Seven Sights</td>
          <td>Zone C Arcology Markets, Transit Networks</td>
          <td>Uneasy Alliance / Energy Beneficiary</td>
        </tr>
        <tr>
          <td><strong style="color:#38bdf8;"><img src="../assets/icons/icon_faction_sed_corps.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">SED Exploration Corps</strong></td>
          <td>External Resource Gathering</td>
          <td>Field Agent Minho</td>
          <td>Reconnaissance Rigs, Kinetic Sidearms</td>
          <td>Direct Military Sub-Branch</td>
        </tr>
        <tr>
          <td><strong style="color:#ef4444;"><img src="../assets/icons/icon_faction_ucd_strike.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">UCD Urban Containment</strong></td>
          <td>Metropolitan Crisis Suppression</td>
          <td>Captain Taeho</td>
          <td>Heavy Breaching Cleavers, Tactical Armor</td>
          <td>Internal Security Enforcement</td>
        </tr>
        <tr>
          <td><strong style="color:#f1df76;"><img src="../assets/icons/icon_faction_architects.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">High Architects Guild</strong></td>
          <td>Urban Infrastructure & Fortifications</td>
          <td>Council of Architects</td>
          <td>Hexagonal Blueprints, Kinetic Spire Design</td>
          <td>Founding Partners of Facility 01</td>
        </tr>
        <tr>
          <td><strong style="color:#a855f7;"><img src="../assets/icons/icon_faction_weavers.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Master Weavers</strong></td>
          <td>M.A.W. Suit Synthesis & Apparel</td>
          <td>Weaver Yeonhwa</td>
          <td>Han-Silk Looms, Protective Veils</td>
          <td>Official Directorate Supplier</td>
        </tr>
        <tr>
          <td><strong style="color:#10b981;"><img src="../assets/icons/icon_faction_wardens.svg" alt="" style="width:20px;vertical-align:middle;margin-right:6px;">Bulwark Wardens</strong></td>
          <td>Outer Wall Defense</td>
          <td>Perimeter Marshals</td>
          <td>Heavy Bastion Artillery, Searchlight Beacons</td>
          <td>Frontline Perimeter Defense</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
"""

    if "/// THE SOCIO-POLITICAL POWER STRUCTURE OF SOMNARAK" not in c:
        c = c[:insert_point] + encyclopedia_content + c[insert_point:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(c)
        print("Enriched factions/index.html with master encyclopedia sections!")

if __name__ == "__main__":
    enrich_characters_hub()
    enrich_locations_hub()
    enrich_lore_hub()
    enrich_mechanics_hub()
    enrich_departments_hub()
    enrich_factions_hub()
