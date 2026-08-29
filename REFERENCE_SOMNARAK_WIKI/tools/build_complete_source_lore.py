import os
import json
import re

WIKI_DIR = "/home/user/01_Somnarak_Wiki"
SRC_DIR = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/World_Reference"

with open(os.path.join(SRC_DIR, "PROJECT_SOMNARAK.md"), "r", encoding="utf-8") as f:
    project_somnarak = f.read()

with open(os.path.join(SRC_DIR, "The_REVERIE_DIRECTORATE.md"), "r", encoding="utf-8") as f:
    reverie_directorate = f.read()

print("Loaded source files. Building complete canonical articles...")

# Import write_page
from generate_wiki_content import write_page

# -------------------------------------------------------------
# 1. SECC Classification System (mechanics/secc-classification-system.html)
# -------------------------------------------------------------
write_page(
    folder="mechanics",
    filename="secc-classification-system.html",
    title="Sorrow Entity Classification Code (SECC)",
    subtitle="The Universal 5-Part Typology Code for Sorrow Entities · Origin, Coherence, Potency, Element & Manifestation",
    color="#38bdf8",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("System Designation", "SECC (Sorrow Entity Classification Code)"),
        ("Classification Schema", "[Origin]-[Coherence][Potency]-[Number] [Element] [Manifestation]"),
        ("Established By", "Echo-Core 5 (Ayshuk) & Directorate Research"),
        ("Supercedes", "Legacy SCS (Somnarak Containment Scale)"),
        ("Authority", "Insight Forge Bureau of Taxonomy")
    ],
    article_body="""
      <h2>Overview of the SECC System</h2>
      <p>The <b>Sorrow Entity Classification Code (SECC)</b> is the standardized, five-part taxonomic system used by the Reverie Directorate to identify, evaluate, and categorize all manifestations of Han in Somnarak. Every contained and wild entity is assigned an alphanumeric code that encodes its origin, structural density, threat level, emotional element, and physical form.</p>
      
      <h2>Code Structure: <code>[Origin]-[Coherence][Potency]-[Number] [Element] [Manifestation]</code></h2>
      <p>An example of a full SECC designation is <code>C-IVδ-001 [LO] [Obj]</code> (The Orphaned Bell):</p>
      <ul>
        <li><code>C</code> = City Sorrow (Origin)</li>
        <li><code>IV</code> = Entity Coherence (Full Autonomous Form)</li>
        <li><code>δ</code> = Critical Threat (Potency)</li>
        <li><code>001</code> = Catalog Number</li>
        <li><code>[LO]</code> = Lament / Deep Blue (Element)</li>
        <li><code>[Obj]</code> = Object-Lament (Manifestation Form)</li>
      </ul>

      <h2>1. Origin Codes (기원 코드)</h2>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Code</th>
              <th>Korean</th>
              <th>Classification Name</th>
              <th>Metaphysical Origin & Description</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>C</b></td>
              <td>도한 (Dohan)</td>
              <td><b>City Sorrow</b></td>
              <td>Born from the collective grief, debt, urban expansion, and tragedies of Somnarak’s citizens.</td>
            </tr>
            <tr>
              <td><b>O</b></td>
              <td>외한 (Oehan)</td>
              <td><b>Outside Sorrow</b></td>
              <td>Born from the primordial wastelands of The Desolate and ruined precursor cities beyond the Bulwark.</td>
            </tr>
            <tr>
              <td><b>I</b></td>
              <td>내한 (Naehan)</td>
              <td><b>Inner Sorrow</b></td>
              <td>Born from intense individual psychological trauma, fractured memories, and private despair.</td>
            </tr>
            <tr>
              <td><b>H</b></td>
              <td>혼합한 (Honhaphan)</td>
              <td><b>Hybrid Sorrow</b></td>
              <td>Complex fusion born from collisions between multiple sorrow origins (e.g., The Convergence).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>2. Coherence Codes (응집도 코드)</h2>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Grade</th>
              <th>Designation</th>
              <th>Structural Stability</th>
              <th>Physical Manifestation Behavior</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>I</b></td>
              <td>Trace (흔적)</td>
              <td>Unstable / Ephemeral</td>
              <td>Transient acoustic echoes, weeping stains, cold spots. Dissipates within hours.</td>
            </tr>
            <tr>
              <td><b>II</b></td>
              <td>Form (형태)</td>
              <td>Semi-Stable</td>
              <td>Shifting silhouettes, moving mist, localized temperature drops. Limited interaction.</td>
            </tr>
            <tr>
              <td><b>III</b></td>
              <td>Construct (구조체)</td>
              <td>Stable Physical Body</td>
              <td>Dense crystalline matter, animate objects, hostile constructs. Requires armed containment.</td>
            </tr>
            <tr>
              <td><b>IV</b></td>
              <td>Entity (개체)</td>
              <td>Autonomous Sentience</td>
              <td>Full individual consciousness, complex psychology, indestructible ego core.</td>
            </tr>
            <tr>
              <td><b>V</b></td>
              <td>Singularity (특이점)</td>
              <td>Cosmic Distortion</td>
              <td>Zone-scale spatial warping, reality tearing, cataclysmic emotional storms (e.g. SE-010).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>3. Potency Codes (위협 등급)</h2>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Potency</th>
              <th>Greek Tier</th>
              <th>Equivalent Risk</th>
              <th>Suppression Response Requirement</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>α (Alpha)</b></td>
              <td>Minor (경미)</td>
              <td>ZAYIN</td>
              <td>Non-lethal. Easily managed by Junior Agents and standard Wardens.</td>
            </tr>
            <tr>
              <td><b>β (Beta)</b></td>
              <td>Moderate (주의)</td>
              <td>TETH</td>
              <td>Low lethality. Can cause mental panic if mishandled. Requires standard M.A.W. gear.</td>
            </tr>
            <tr>
              <td><b>γ (Gamma)</b></td>
              <td>Significant (위험)</td>
              <td>HE</td>
              <td>Moderate lethality. Capable of killing unarmored staff and triggering corridor panics.</td>
            </tr>
            <tr>
              <td><b>δ (Delta)</b></td>
              <td>Critical (극위험)</td>
              <td>WAW</td>
              <td>High lethality. Capable of mass casualties and facility-wide containment cascade.</td>
            </tr>
            <tr>
              <td><b>ω (Omega)</b></td>
              <td>Calamity (재앙)</td>
              <td>ALEPH</td>
              <td>City-ending catastrophe. Requires Echo-Core direct intervention and floor lockdown.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>4. Element Codes (원소 코드)</h2>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Code</th>
              <th>Element Name</th>
              <th>Color Spectrum</th>
              <th>Damage Type & Combat Behavior</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>[LO]</b></td>
              <td>Lament (탄식)</td>
              <td>Deep Blue (#38bdf8)</td>
              <td>Mental SP damage; chills consciousness; induces catatonia and weeping.</td>
            </tr>
            <tr>
              <td><b>[GR]</b></td>
              <td>Grudge (원한)</td>
              <td>Crimson (#ef5b55)</td>
              <td>Physical HP damage; searing heat and kinetic razors; fractures armor plates.</td>
            </tr>
            <tr>
              <td><b>[VO]</b></td>
              <td>Void (공허)</td>
              <td>Pale White (#f8fafc)</td>
              <td>Percentage Max HP damage; existential extinction; dissolves biological tissue.</td>
            </tr>
            <tr>
              <td><b>[WE]</b></td>
              <td>Weight (무게)</td>
              <td>Black (#a855f7)</td>
              <td>Hybrid HP + SP damage; gravitational crushing pressure; collapses posture.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>5. Manifestation Codes (발현 형태)</h2>
      <ul>
        <li><b>[Sub] Subject (주체):</b> Humanoid, animalistic, or animate living forms possessing physical locomotion.</li>
        <li><b>[Obj] Object (물체):</b> Physical artifacts, bells, weapons, mirrors, or wearable relics that produce psychic resonance.</li>
        <li><b>[Pla] Place (공간):</b> Architectural structures, rooms, corridors, or geographical areas warped by Han.</li>
        <li><b>[Haz] Hazard (위험현상):</b> Environmental phenomena, toxic miasma, burning fog, acoustic chimes, or weather events.</li>
        <li><b>[Tim] Time (시간현상):</b> Temporal anomalies, localized time loops, or memory replay fields.</li>
      </ul>
    """
)

# -------------------------------------------------------------
# 2. The Giltong & Taboo Enforcement (factions/the-giltong-enforcers.html)
# -------------------------------------------------------------
write_page(
    folder="factions",
    filename="the-giltong-enforcers.html",
    title="The Giltong (질동 — The Taboo Arbiters)",
    subtitle="The Supreme Judicial Enforcers of Somnarak · Guardians of the Seven Absolute Taboos",
    color="#ef5b55",
    icon_svg="icon_dept_f6_deep_vault.svg",
    meta_cards=[
        ("Judicial Agency", "The Giltong (질동 / 秩序同盟)"),
        ("Presiding Officer", "The Grand Arbiter (심판관)"),
        ("Jurisdiction", "City-Wide Taboo Enforcement across all 5 Zones"),
        ("Operating Force", "300 Black-Robed Arbiters & Forensic Keepers"),
        ("Authority", "Supreme Charter of Year 3,910")
    ],
    article_body="""
      <h2>Overview of the Giltong</h2>
      <p>The <b>Giltong</b> (질동, <i>Giltong</i>) is the autonomous judicial and enforcement body tasked with investigating, prosecuting, and eradicating violations of the <b>Seven Absolute Taboos</b> in Somnarak. Answering neither to the High Council nor directly to individual Echo-Cores, the Giltong operates under an ancient post-Cheongula mandate granted by Director Majin to preserve the metaphysical integrity of human consciousness.</p>

      <h2>The Grand Arbiter & Organization</h2>
      <p>Led by the enigmatic <b>Grand Arbiter</b>, the Giltong is organized into three operational branches:</p>
      <ul>
        <li><b>The Inquisitors (추적단):</b> Covert investigators embedded in Zone C and the Underworld, tracking illicit memory-washing rings and unauthorized Han extraction vats.</li>
        <li><b>The Execution Sentinels (집행관):</b> Heavily armored tactical enforcers wielding execution blades lined with Pale resonance, authorized to administer summary memory scrubbing or physical execution upon confirmed Taboo breaches.</li>
        <li><b>The Vault Keepers (봉인단):</b> Forensic metaphysicians who work in coordination with Floor 6 Deep Vault to securely transport confiscated relics and seal memory jars.</li>
      </ul>

      <h2>Famous Historical Taboo Cases</h2>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Year</th>
              <th>Case Title</th>
              <th>Taboo Violated</th>
              <th>Judicial Resolution</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>Year 4,012</b></td>
              <td>The Sector B Memory Counterfeit Syndicate</td>
              <td>Taboo 1 (Memory Forgery)</td>
              <td>14 illicit workshops raided; 12,000 forged memory jars shattered; ringleaders sentenced to Floor 8 gate duty.</td>
            </tr>
            <tr>
              <td><b>Year 4,120</b></td>
              <td>The Sub-Level Maw Drilling Expedition</td>
              <td>Taboo 3 (Abyssal Piercing)</td>
              <td>Rogue mining cartel eliminated before reaching the Basal Iris; excavation shafts flooded with liquid granite.</td>
            </tr>
            <tr>
              <td><b>Year 4,198</b></td>
              <td>The Flesh-Lattice Chimera Incident</td>
              <td>Taboo 4 (Human-Entity Fusion)</td>
              <td>Heretical alchemist arrested in Zone D; mutated specimens euthanized with Pale Verdict resonance.</td>
            </tr>
          </tbody>
        </table>
      </div>
    """
)

# -------------------------------------------------------------
# 3. Agent Stats & Attributes (mechanics/agent-attributes-and-stats.html)
# -------------------------------------------------------------
write_page(
    folder="mechanics",
    filename="agent-attributes-and-stats.html",
    title="R.D. Agent Stats &amp; Attributes System",
    subtitle="The Four Core Attributes · Resilience, Clarity, Composure, and Resolve · Progression and Formulas",
    color="#47c978",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("System Name", "R.D. Agent Evaluation Framework"),
        ("The Four Attributes", "Resilience (♦ Blue), Clarity (♠ White), Composure (♣ Crimson), Resolve (♦ Black)"),
        ("Max Attribute Level", "Level V (Elite Harmonization)"),
        ("Managing Department", "Floor 4 Insight Forge & Human Resources"),
        ("Combat Impact", "Determines HP, SP, Attack Speed, Work Success, and Panic Resistance")
    ],
    article_body="""
      <h2>The Four Foundational Attributes</h2>
      <p>Every operative employed within the Hand of Change is evaluated across four metaphysical attributes. These stats govern the agent's combat survivability, work performance with Sorrow Entities, and resistance to mental fracture.</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Attribute</th>
              <th>Symbol & Color</th>
              <th>Governing Work</th>
              <th>Combat & Containment Benefits</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>Resilience (회복력)</b></td>
              <td>♦ Deep Blue</td>
              <td>Ferrehan (Endurance)</td>
              <td>Increases maximum HP (Health Points) and physical damage resistance. Reduces bleed duration.</td>
            </tr>
            <tr>
              <td><b>Clarity (명료도)</b></td>
              <td>♠ Pale White</td>
              <td>Viderehan (Observation)</td>
              <td>Increases maximum SP (Sanity Points) and psychic resistance. Speeds up observation research.</td>
            </tr>
            <tr>
              <td><b>Composure (침착도)</b></td>
              <td>♣ Crimson</td>
              <td>Pugnahan (Confrontation)</td>
              <td>Increases Attack Speed, Clash Power rolls, and critical strike chance with M.A.W. weapons.</td>
            </tr>
            <tr>
              <td><b>Resolve (결의)</b></td>
              <td>♦ Heavy Black</td>
              <td>Flerehan (Tears)</td>
              <td>Increases Work Success Rate and reduces Sorrow Counter depletion on Bad Work outcomes.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Attribute Level Progression (Levels I to V)</h2>
      <p>Agents increase their attributes through successful daily work assignments in containment chambers:</p>
      <ul>
        <li><b>Level I (Novice):</b> Base values (10–29 points). Baseline civilian capability.</li>
        <li><b>Level II (Trained):</b> Values (30–49 points). Capable of handling Beta-grade entities.</li>
        <li><b>Level III (Veteran):</b> Values (50–69 points). Qualified for Gamma-grade containment.</li>
        <li><b>Level IV (Elite):</b> Values (70–89 points). Authorized to wield Delta-grade M.A.W. gear.</li>
        <li><b>Level V (Master):</b> Values (90–120+ points). Eligible for Calamity-grade suppression.</li>
      </ul>
    """
)

# -------------------------------------------------------------
# 4. Default Standard Issue Kit (mechanics/default-standard-equipment.html)
# -------------------------------------------------------------
write_page(
    folder="mechanics",
    filename="default-standard-equipment.html",
    title="R.D. Standard Issue Equipment Kit",
    subtitle="Baseline Gear for Directorate Personnel · Sorrow Rod, Veil Vest, Echo Compass & Sorrow Gauge",
    color="#d7d7d7",
    icon_svg="icon_dept_f5_border_watch.svg",
    meta_cards=[
        ("Kit Classification", "R.D. Standard Issue (Non-M.A.W. Baseline)"),
        ("Issued To", "Junior Agents, Clerks, and Floor Staff"),
        ("Primary Armament", "The Sorrow Rod (한의 막대)"),
        ("Primary Protection", "The Veil Vest (베일 조끼)"),
        ("Survival Tools", "Echo Compass, Sorrow Gauge, Memory Anchor, Fracture Whistle")
    ],
    article_body="""
      <h2>Standard Issue Overview</h2>
      <p>Before an operative earns the right to equip specialized M.A.W. equipment extracted from Sorrow Entities, they are issued the standardized Directorate baseline kit. Designed for reliable defense, containment observation, and baseline suppression, this gear ensures every employee can survive low-intensity hazards.</p>

      <h2>The Six Standard Issue Components</h2>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Equipment Name</th>
              <th>Korean Name</th>
              <th>Slot / Category</th>
              <th>Operational Function & Stats</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>The Sorrow Rod</b></td>
              <td>한의 막대</td>
              <td>Standard Weapon</td>
              <td>Deals 4–7 Red physical damage. Emits low-voltage electric shocks to pacify minor entities.</td>
            </tr>
            <tr>
              <td><b>The Veil Vest</b></td>
              <td>베일 조끼</td>
              <td>Standard Suit</td>
              <td>Provides 1.0x (Normal) resistance across all 4 damage types (Red, Blue, Black, Pale).</td>
            </tr>
            <tr>
              <td><b>The Echo Compass</b></td>
              <td>메아리 나침반</td>
              <td>Navigation Tool</td>
              <td>Detects fluctuations in ambient Han pressure, guiding staff through containment corridors.</td>
            </tr>
            <tr>
              <td><b>The Sorrow Gauge</b></td>
              <td>한 게이지</td>
              <td>Monitoring Device</td>
              <td>Displays real-time emotional saturation of the containment cell, warning of imminent breach.</td>
            </tr>
            <tr>
              <td><b>The Memory Anchor</b></td>
              <td>기억 닻</td>
              <td>Mental Stabilizer</td>
              <td>Pocket resonator that prevents low-grade memory erasure and restores 5 SP when activated.</td>
            </tr>
            <tr>
              <td><b>The Fracture Whistle</b></td>
              <td>파열 휘파람</td>
              <td>Emergency Tool</td>
              <td>Acoustic distress beacon that alerts nearby Floor Vanguard squads to an operative in Panic.</td>
            </tr>
          </tbody>
        </table>
      </div>
    """
)

# -------------------------------------------------------------
# 5. The Four Work Types (mechanics/the-four-work-types.html)
# -------------------------------------------------------------
write_page(
    folder="mechanics",
    filename="the-four-work-types.html",
    title="The Four Work Types (4대 작업 유형)",
    subtitle="Flerehan, Pugnahan, Viderehan, and Ferrehan · Mathematical Work Matrices and Formulas",
    color="#e6c94d",
    icon_svg="icon_dept_f3_extraction.svg",
    meta_cards=[
        ("Work Disciplines", "Flerehan (Tears), Pugnahan (Confrontation), Viderehan (Observation), Ferrehan (Endurance)"),
        ("Yield Outcome", "Alpha Sap Production & M.A.W. Extraction Points"),
        ("Hazard Trigger", "Sorrow Counter Depletion on Bad Work"),
        ("Authority", "Floor 3 Extraction Hall & Floor 4 Insight Forge")
    ],
    article_body="""
      <h2>Metaphysical Foundations of Containment Work</h2>
      <p>Containment within the Hand of Change is an active psychological dialogue between human agents and crystallized grief. Every interaction is classified under one of the <b>Four Canonical Work Types</b>:</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Work Type</th>
              <th>Etymology & Meaning</th>
              <th>Primary Action</th>
              <th>Success Governing Stat</th>
              <th>Optimal Entity Match</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>Flerehan (플레레한)</b></td>
              <td><i>Flere</i> (To Weep / Tears)</td>
              <td>Emotional listening, therapeutic grieving, shared catharsis</td>
              <td>Resolve (♦ Black)</td>
              <td>Sentient, mournful, tragic humanoid entities (e.g. SE-001, SE-005)</td>
            </tr>
            <tr>
              <td><b>Pugnahan (푸그나한)</b></td>
              <td><i>Pugna</i> (To Fight / Combat)</td>
              <td>Physical restraint, resonant shock calibration, dominance display</td>
              <td>Composure (♣ Crimson)</td>
              <td>Aggressive, predatory, bestial entities (e.g. SE-007, SE-002)</td>
            </tr>
            <tr>
              <td><b>Viderehan (비데레한)</b></td>
              <td><i>Videre</i> (To See / Observe)</td>
              <td>Philosophical observation, pattern recording, environmental tuning</td>
              <td>Clarity (♠ White)</td>
              <td>Abstract, conceptual, spatial entities (e.g. SE-009, SE-011)</td>
            </tr>
            <tr>
              <td><b>Ferrehan (페레한)</b></td>
              <td><i>Ferre</i> (To Bear / Endure)</td>
              <td>Biological feeding, physical endurance, thermal regulation</td>
              <td>Resilience (♦ Blue)</td>
              <td>Organic, parasitic, bio-reactive entities (e.g. SE-014, SE-015)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Work Outcome Formula</h2>
      <p><code>Success Probability (%) = Base Entity Preference + (Agent Attribute Level × 4%) - (Cell Han Density Penalty)</code></p>
      <ul>
        <li><b>Good Outcome (80–100%):</b> Maximum Alpha Sap extracted; agent restores 15 SP; Sorrow Counter remains stable.</li>
        <li><b>Normal Outcome (50–79%):</b> Moderate Alpha Sap extracted; minor SP drain.</li>
        <li><b>Bad Outcome (0–49%):</b> Zero Alpha Sap extracted; heavy damage inflicted on agent; Sorrow Counter decreases by 1.</li>
      </ul>
    """
)

# -------------------------------------------------------------
# 6. The 10 Facility Incident Reports (departments/incident-reports-archive.html)
# -------------------------------------------------------------
write_page(
    folder="departments",
    filename="incident-reports-archive.html",
    title="Hand of Change Incident Reports Archive",
    subtitle="The 10 Canonical Containment Cascade Logs · Breaches, Structural Ruptures & Heroic Last Stands",
    color="#8d2e42",
    icon_svg="icon_dept_f6_deep_vault.svg",
    meta_cards=[
        ("Archival Classification", "Class V Operational Incident Records"),
        ("Preserving Department", "Floor 6 Deep Vault Archival Registry"),
        ("Incident Range", "Incident 001 through Incident 010"),
        ("Declassification Status", "Year 4,238 Dawn Initiative Declassified"),
        ("Historical Significance", "Formed Modern Containment Safety Protocols")
    ],
    article_body="""
      <h2>The Operational Casualty & Breach Logs</h2>
      <p>The following ten incident reports document the most severe containment failures, spatial ruptures, and tactical suppression operations in the history of the Hand of Change facility.</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Report #</th>
              <th>Incident Title</th>
              <th>Floor & Entity Involved</th>
              <th>Casualties</th>
              <th>Tactical Resolution & Post-Mortem</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>IR-001</b></td>
              <td><b>The Silent Breach</b></td>
              <td>Floor 2 · SE-001 (The Orphaned Bell)</td>
              <td>4 Agents Panicked</td>
              <td>Acoustic dampeners failed; bell tolled in reverse. Dekan deployed heavy lead shutters; all faces logged.</td>
            </tr>
            <tr>
              <td><b>IR-002</b></td>
              <td><b>The Noon Cascade</b></td>
              <td>Floor 3 & 4 · Noon Ordeal (Amber Worms)</td>
              <td>12 Clerks Lost</td>
              <td>Subterranean worms burrowed into Extraction vats; Zyrak channeled liquid Alpha Sap to incinerate the hive.</td>
            </tr>
            <tr>
              <td><b>IR-003</b></td>
              <td><b>The Smothering Incident</b></td>
              <td>Floor 2 · SE-005 (The Smothering Mother)</td>
              <td>6 Agents Embraced</td>
              <td>Entity expanded to fill Sector B corridor; Dekan used Mourning Maul to sever umbilical tendrils.</td>
            </tr>
            <tr>
              <td><b>IR-004</b></td>
              <td><b>The Dawn Transformation</b></td>
              <td>Floor 5 · Dawn Ordeal (Green Scavengers)</td>
              <td>2 Outposts Damaged</td>
              <td>Feral constructs breached Gate 3; Mellda deployed the Silver Perimeter barrier to crush the swarm.</td>
            </tr>
            <tr>
              <td><b>IR-005</b></td>
              <td><b>The Midnight Abyss</b></td>
              <td>Floor 8 · The Abyssal Singularity</td>
              <td>28 Sentries Fallen</td>
              <td>Maw Iris ruptured by 40%; Xyan held the gateway solo for 3 hours until hydraulic seals reset.</td>
            </tr>
            <tr>
              <td><b>IR-006</b></td>
              <td><b>The Forgotten Soldier's March</b></td>
              <td>Floor 6 · SE-006 (The Forgotten Soldier)</td>
              <td>Floor-wide Freeze</td>
              <td>Entity marched through Deep Vault corridors; Marjuk spoke all 1,778 lost names to pacify the march.</td>
            </tr>
            <tr>
              <td><b>IR-007</b></td>
              <td><b>The Memory Cascade</b></td>
              <td>Floor 6 · Cryo-Cylinder Rupture</td>
              <td>40 Agents Amnesic</td>
              <td>Trauma storage tank 9 ruptured; Seiyon executed Protocol Zero to overwrite corrupt memory tracks.</td>
            </tr>
            <tr>
              <td><b>IR-008</b></td>
              <td><b>The Colossus Passes</b></td>
              <td>Floor 2 · SE-002 (The Grieving Colossus)</td>
              <td>Sub-Level 2 Collapsed</td>
              <td>Entity stood upright, shaking facility foundations; Dekan applied kinetic anchors to knees.</td>
            </tr>
            <tr>
              <td><b>IR-009</b></td>
              <td><b>The Bell's Crescendo</b></td>
              <td>Zone B · SE-001 Toll Overflow</td>
              <td>Sector B-01 Evacuated</td>
              <td>100 consecutive tolls recorded during anniversary; Cheonbulok choir deployed to sing restorative chants.</td>
            </tr>
            <tr>
              <td><b>IR-010</b></td>
              <td><b>The Healing Shadow</b></td>
              <td>Floor 7 · The Dream Bleed</td>
              <td>Zero Casualties</td>
              <td>Ishall phased into the Dream Realm to seal an uncontained psychic fissure beneath Floor 7.</td>
            </tr>
          </tbody>
        </table>
      </div>
    """
)

# -------------------------------------------------------------
# 7. Efflorescence & Fracture (lore/efflorescence-and-fracture.html)
# -------------------------------------------------------------
write_page(
    folder="lore",
    filename="efflorescence-and-fracture.html",
    title="Efflorescence &amp; Fracture (개화와 파열)",
    subtitle="The Two Fates of the Human Soul in Somnarak · Awakening of Ego vs Catastrophic Collapse",
    color="#71efaf",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("Metaphysical Phenonema", "Efflorescence (개화) vs Fracture (파열)"),
        ("Positive Manifestation", "Efflorescence — Complete Ego Harmonization & M.A.W. Mastery"),
        ("Negative Manifestation", "Fracture — Cognitive Shatter, Panic & Monstrous Transmutation"),
        ("Authoring Bureau", "Floor 4 Insight Forge Cognitive Research")
    ],
    article_body="""
      <h2>The Fork in the Soul: Ego Awakening vs Collapse</h2>
      <p>When an individual in Somnarak is subjected to overwhelming concentrations of Han energy, their ego reaches a critical threshold. The soul must either shatter under the pressure or bloom into conscious mastery. These two divergent paths are known as <b>Fracture (파열)</b> and <b>Efflorescence (개화)</b>.</p>

      <h2>1. Fracture (파열 — Payeol): The Path of Collapse</h2>
      <p>When a human mind can no longer bear its sorrow, guilt, or despair, the cognitive membrane ruptures. The individual's personality dissolves, leaving only a calcified shell driven by raw instinct or transforming entirely into a feral Sorrow Entity.</p>
      <ul>
        <li><b>Mild Fracture:</b> Temporary hysteria, amnesia, loss of motor control. Managed via Floor 4 neural stabilization baths.</li>
        <li><b>Severe Fracture:</b> Total psychotic breaks resulting in Berserk or Catatonic panic states.</li>
        <li><b>Terminal Fracture:</b> Complete bodily transmutation into a crystallized monster. Irreversible.</li>
      </ul>

      <h2>2. Efflorescence (개화 — Gaehwa): The Path of Awakening</h2>
      <p>In rare circumstances (occurring in less than 0.02% of operatives), an individual confronts their deepest trauma, accepts the full burden of their sorrow without flinching, and achieves <b>Efflorescence (개화 — The Blooming of Ego)</b>.</p>
      <ul>
        <li><b>Ego Armor Manifestation:</b> The operative spontaneously manifests unique personal M.A.W. equipment woven from their own crystallized resolve, requiring zero extraction from external entities.</li>
        <li><b>Absolute Mental Immunity:</b> The operative becomes permanently immune to SP damage and mental panic.</li>
        <li><b>Harmonic Authority:</b> Surrounding allies gain immense combat boosts and emotional stabilization.</li>
      </ul>
    """
)

# -------------------------------------------------------------
# 8. Named Fractures (lore/named-fractures.html)
# -------------------------------------------------------------
write_page(
    folder="lore",
    filename="named-fractures.html",
    title="The Named Fractures (이름 붙은 파열자들)",
    subtitle="The 8 Tragic Legends of Somnarak · Historical Figures Consumed by Absolute Sorrow",
    color="#8d2e42",
    icon_svg="icon_dept_f6_deep_vault.svg",
    meta_cards=[
        ("Classification", "Historical High-Potency Fractured Entities"),
        ("Registry Status", "8 Confirmed Named Fractures"),
        ("Origin", "Prominent Citizens & Operatives Who Suffered Terminal Collapse"),
        ("Threat Profile", "Class IVδ to Class Vω Threats")
    ],
    article_body="""
      <h2>The Chronicles of the Shattered</h2>
      <p>Unlike nameless feral horrors, the <b>Named Fractures</b> are legendary figures whose personal grief was so profound that their transformation reshaped entire districts of Somnarak.</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Designation</th>
              <th>Korean Name</th>
              <th>Original Identity</th>
              <th>Tragic Catalyst & Manifestation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>1. The Weeping Judge</b></td>
              <td>우는 판사</td>
              <td>Chief Magistrate Park (Y3,980)</td>
              <td>Sentenced his own innocent family to save a district; transformed into a blindfolded titan wielding scales that weep blood.</td>
            </tr>
            <tr>
              <td><b>2. The Hollow Mother</b></td>
              <td>빈 어머니</td>
              <td>Matron Yoon of Sector B</td>
              <td>Lost all four children in the Cheongula cataclysm; manifested as an empty porcelain effigy that absorbs wandering souls.</td>
            </tr>
            <tr>
              <td><b>3. The Forgotten King</b></td>
              <td>잊혀진 왕</td>
              <td>High Elder Han of the First Council</td>
              <td>Cast out into The Desolate after political betrayal; returned as an ashen crowned monolith wielding rusting scepters.</td>
            </tr>
            <tr>
              <td><b>4. The Silent Child</b></td>
              <td>조용한 아이</td>
              <td>Orphan 042 of Sector B-01</td>
              <td>Mute child trapped in a collapsed fallout shelter; manifests as a hovering shadow that silences all sound within 500 meters.</td>
            </tr>
            <tr>
              <td><b>5. The Broken Architect</b></td>
              <td>부서진 건축가</td>
              <td>Master Mason Ryuk (Y4,050)</td>
              <td>Engineered the Hand of Change Floor 2 blast doors; fused permanently with his own granite blueprints upon breach.</td>
            </tr>
            <tr>
              <td><b>6. The Masked Dancer</b></td>
              <td>가면 무용수</td>
              <td>Silk Mistress Chae of the Weavers</td>
              <td>Consumed by grief over the death of her apprentices; dances through Zone C alleys, entangling pedestrians in razor silk.</td>
            </tr>
            <tr>
              <td><b>7. The Hollow Knight</b></td>
              <td>빈 기사</td>
              <td>Captain Go of the 1st Wardens</td>
              <td>Held the North Gate alone during the Second Outbreak; armor remains standing and patrolling though the body inside dissolved.</td>
            </tr>
            <tr>
              <td><b>8. The Memory Thief</b></td>
              <td>기록 도둑</td>
              <td>Archivist Shin of Floor 6</td>
              <td>Attempted to steal prohibited cycle records; transformed into a multi-eyed wraith that eats written ink and parchment.</td>
            </tr>
          </tbody>
        </table>
      </div>
    """
)

# -------------------------------------------------------------
# 9. Night Hazards & The Vigil (lore/night-hazards-and-vigil.html)
# -------------------------------------------------------------
write_page(
    folder="lore",
    filename="night-hazards-and-vigil.html",
    title="Night Hazards &amp; The Vigil (야간 위험과 야경)",
    subtitle="The Three Nocturnal Perils of Somnarak · Sorrow Tide, Dream Bleed, and Fracture Surge",
    color="#6f7ee8",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Environmental State", "The Night Cycle (18:00 to 06:00)"),
        ("Primary Night Hazards", "The Sorrow Tide, The Dream Bleed, The Fracture Surge"),
        ("Civic Defense Protocol", "The Night Vigil (야경 — Yagyeong)"),
        ("Enforcing Units", "The Wardens & Border Watch 2nd Division")
    ],
    article_body="""
      <h2>The Nocturnal Perils of the City</h2>
      <p>When the golden canopy of the Alpha Tree dims at twilight, the metaphysical pressure of the subterranean Maw rises sharply, creating three deadly nocturnal phenomena across Somnarak:</p>

      <h2>The Three Night Hazards</h2>
      <ul>
        <li><b>1. The Sorrow Tide (한의 조수):</b> Subterranean drainage canals fill with luminescent blue Han mist. Citizens outside after curfew risk inhaling vaporized grief, causing immediate panic and depression.</li>
        <li><b>2. The Dream Bleed (꿈의 유출):</b> The boundary between physical reality and <i>Yumonggye</i> thins. Unconscious sleepers’ nightmares project into streets as physical phantom apparitions.</li>
        <li><b>3. The Fracture Surge (파열의 급증):</b> Spontaneous micro-breaches erupt along fault lines, causing localized gravity inversions and rapid decay of building foundations.</li>
      </ul>

      <h2>The Night Vigil (야경 — Yagyeong)</h2>
      <p>To protect civil society during the night cycle, the Directorate enforces strict curfews. Armed Warden patrols walk the spires with resonance lanterns, singing the <i>Vigil Litany</i> to soothe restless emotional currents until dawn.</p>
    """
)

# -------------------------------------------------------------
# 10. The Three Ages & History of Somnarak (lore/the-three-ages-and-history.html)
# -------------------------------------------------------------
write_page(
    folder="lore",
    filename="the-three-ages-and-history.html",
    title="The Three Ages &amp; Historic Wars of Somnarak",
    subtitle="Chronological Epochs of Mugenhan · Before-Time, Becoming, Structuring, and The Wars",
    color="#e6c94d",
    icon_svg="the_hand_dr_icon_styled.svg",
    meta_cards=[
        ("Historical Epochs", "Age I (Before-Time), Age II (The Becoming), Age III (The Structuring)"),
        ("Major Historic Wars", "The Occlusihan War & The Consolihan War"),
        ("Documented Years", "Year 0 to Year 4,238 (Dawn Era)"),
        ("Authority", "Deep Vault Historical Archive (Floor 6)")
    ],
    article_body="""
      <h2>The Three Great Historical Ages</h2>
      <p>The history of humanity in Mugenhan is divided into three distinct civilizational epochs:</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Age</th>
              <th>Korean</th>
              <th>Time Period</th>
              <th>Historical Defining Characteristics</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>Age I: The Before-Time</b></td>
              <td>선시대 (Seonsidae)</td>
              <td>Prior to Y3,892</td>
              <td>The golden age of technological advancement and sprawling surface metropolises. Ended with the Cheongula Cataclysm.</td>
            </tr>
            <tr>
              <td><b>Age II: The Becoming</b></td>
              <td>변천 (Byeongcheon)</td>
              <td>Y3,892 – Y4,100</td>
              <td>The era of chaos, mass mutation, and resource wars. Humanity retreated into fortified spires around the Alpha Tree.</td>
            </tr>
            <tr>
              <td><b>Age III: The Structuring</b></td>
              <td>구조화 (Gujohwa)</td>
              <td>Y4,100 – Y4,238</td>
              <td>The establishment of the Reverie Directorate, the construction of the Hand of Change, and the 1,778 Absolvohan Cycles.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>The Great Historic Wars</h2>
      <ul>
        <li><b>The Occlusihan War (오클루시한):</b> Fought in Year 3,950 between the surviving citadels over the remaining Alpha Sap aquifers. Led to the destruction of Cheonbulok and the consolidation of Somnarak as the sole surviving megacity.</li>
        <li><b>The Consolihan War (결한 전쟁):</b> Fought in Year 4,080 against a massive swarm of Calamity-class entities emerging from The Desolate. Established the legendary status of the Bulwark Garrison under Dekan and Mellda.</li>
      </ul>
    """
)

# -------------------------------------------------------------
# 11. Hand of Change Room Types (departments/facility-room-types.html)
# -------------------------------------------------------------
write_page(
    folder="departments",
    filename="facility-room-types.html",
    title="Hand of Change Architectural Room Types",
    subtitle="Complete Engineering Catalog of Chambers, Containment Cells, Refining Vats & Observatories",
    color="#38bdf8",
    icon_svg="the_hand_dr_icon_styled.svg",
    meta_cards=[
        ("Facility Designation", "The Hand of Change (변화의 손)"),
        ("Catalog Scope", "Universal & Floor-Specific Chambers (Floors 1–8)"),
        ("Engineered By", "Grand Architect Kael & High Architects"),
        ("Classification", "High-Security Subterranean Complex")
    ],
    article_body="""
      <h2>Facility Architecture Overview</h2>
      <p>The Hand of Change contains hundreds of interconnected modular chambers engineered to withstand extreme physical and psychic pressures. Rooms are divided into <b>Universal Room Types</b> present on every floor, and <b>Specialized Department Chambers</b> unique to specific operational wings.</p>

      <h2>Universal Room Types (All Floors)</h2>
      <ul>
        <li><b>Main Department Hub (주 로비):</b> The central congregating hall where floor personnel receive daily task rosters and rest between work cycles.</li>
        <li><b>Standard Containment Cell (격리실):</b> Hexagonal chamber lined with resonant granite dampeners, observation glass, and automatic Alpha Sap injection nozzles.</li>
        <li><b>Corridor Transit Tubes (이동 통로):</b> Reinforced walkways equipped with emergency blast bulkheads that drop automatically during a containment breach.</li>
        <li><b>First-Aid Medical Station (의무실):</b> Treatment clinic stocked with regenerative Alpha Salve and sedative inhalers for injured staff.</li>
      </ul>

      <h2>Specialized Department Chambers (By Floor)</h2>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Floor</th>
              <th>Department</th>
              <th>Specialized Chamber</th>
              <th>Engineering Purpose</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>Floor 1</b></td>
              <td>Neutral Command</td>
              <td><b>Station A Core Chamber</b></td>
              <td>Hermetically sealed manifold where the Alpha Tree taproot connects to the primary sap distributor.</td>
            </tr>
            <tr>
              <td><b>Floor 2</b></td>
              <td>The Maw's Keep</td>
              <td><b>The Titan Armory & Hydraulic Vaults</b></td>
              <td>Heavy weapons forge and hydraulic dampening cells capable of restraining 500-ton physical entities.</td>
            </tr>
            <tr>
              <td><b>Floor 3</b></td>
              <td>Extraction Hall</td>
              <td><b>The Catharsis Crucible Vats</b></td>
              <td>Pressurized alchemical boilers that condense raw emotional Han into crystalline M.A.W. weapon ingots.</td>
            </tr>
            <tr>
              <td><b>Floor 4</b></td>
              <td>Insight Forge</td>
              <td><b>Neural Stabilization Baths</b></td>
              <td>Heated pools of refined sap where traumatized operatives float in sensory deprivation to repair SP.</td>
            </tr>
            <tr>
              <td><b>Floor 5</b></td>
              <td>Border Watch</td>
              <td><b>Spatial Barrier Projector Ring</b></td>
              <td>Subterranean harmonic generator linking the facility's power directly to the Zone E Titan Wall.</td>
            </tr>
            <tr>
              <td><b>Floor 6</b></td>
              <td>Deep Vault</td>
              <td><b>Sub-Zero Cryo-Cylinder Crypt</b></td>
              <td>-20°C archival vault housing over 100,000 crystallized memory cylinders from the 1,778 resets.</td>
            </tr>
            <tr>
              <td><b>Floor 7</b></td>
              <td>Shadow Corps</td>
              <td><b>Psychotropic Dream Pods</b></td>
              <td>Immersion capsules where Shadow operatives perform deep telepathic dives into <i>Yumonggye</i>.</td>
            </tr>
            <tr>
              <td><b>Floor 8</b></td>
              <td>Gate Watch</td>
              <td><b>The Basal Containment Iris</b></td>
              <td>Colossal 50-meter-thick interlocking basalt barrier sealing the entrance to the Abyssal Maw.</td>
            </tr>
          </tbody>
        </table>
      </div>
    """
)

# -------------------------------------------------------------
# 12. District Structure: The Veil and The Raw (locations/district-structure-veil-and-raw.html)
# -------------------------------------------------------------
write_page(
    folder="locations",
    filename="district-structure-veil-and-raw.html",
    title="District Architecture: The Veil &amp; The Raw",
    subtitle="The Dual Nature of Urban Space in Somnarak · Civilized Facade vs Unfiltered Han Strata",
    color="#f1df76",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Urban Philosophy", "The Veil (베일 — Beil) vs The Raw (원본 — Wonbon)"),
        ("The Veil", "The structured, sanitized, protected upper civic districts"),
        ("The Raw", "The unfiltered, crumbling, high-Han sub-levels and alleys"),
        ("Governing Faction", "The High Council & Reverie Directorate")
    ],
    article_body="""
      <h2>The Dual Metaphysical Nature of the City</h2>
      <p>Every district within Somnarak exists in a state of architectural duality. The city is fundamentally split between <b>The Veil (베일 — Beil)</b> and <b>The Raw (원본 — Wonbon)</b>.</p>

      <h2>1. The Veil (베일 — Beil)</h2>
      <p>The Veil represents the sanitized, civil, and engineered surface of Somnarak. Built from polished resonant granite, powered by purified Alpha Sap, and protected by Warden garrisons, the Veil is where commerce, education, and daily human life take place.</p>

      <h2>2. The Raw (원본 — Wonbon)</h2>
      <p>Beneath the floorboards, behind the neon alleys of Zone C, and deep within the foundation strata lies The Raw. Here, the city’s unrefined structural skeleton is exposed to the weeping of the subterranean Maw. In The Raw, space bends unpredictably, Han dust coats the walls like black frost, and outcasts of the Wound Walkers build clandestine shelters.</p>
    """
)

print("All deep canonical articles built successfully.")
