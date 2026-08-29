import os

def generate_subpages():
    wiki_root = "/home/user/01_Somnarak_Wiki"

    subpages = [
        # 1. Neutral Command Sub-Protocols
        {
            "dir": "departments",
            "file": "floor-1-sub-protocols.html",
            "title": "Neutral Command Executive Protocols &amp; Override Codes",
            "category": "Facility Operations",
            "cat_url": "../departments/index.html",
            "hero_img": "../assets/layout/hand/blueprints/floor-1-neutral-blueprint.svg",
            "lead": "DIRECTOR MAJIN // SECRETARY SEIYON",
            "code": "PROTO-EXEC-01",
            "clearance": "LEVEL 5 EYES ONLY",
            "content": '''
<h2>1. Executive Summary &amp; Scope</h2>
<p>Floor 1 operates as the sovereign central nerve system of <strong>The Hand of Change (Facility 01)</strong>. Under the command of <a class="wiki-link" href="../characters/the-director-majin.html">Director Majin</a> and <a class="wiki-link" href="../characters/the-secretary-seiyon.html">Secretary Seiyon</a>, all facility-wide <a class="wiki-link" href="../mechanics/han-energy-and-damage.html">Han-Flux</a> routing, containment coherence alarms, and departmental mission authorizations are arbitrated here.</p>

<div class="wiki-callout terminal-callout">
  <div class="callout-header">FACILITY OVERRIDE DIRECTIVE 01-A</div>
  <p>In the event of simultaneous Coherence Counter failures exceeding 3 containment blocks, Executive Authority transfers automatically to Floor 1 Sovereign Core lockdown. All sub-level bulkheads lock into permanent hydraulic seal.</p>
</div>

<h2>2. The Five-Stage Alarm Escalation Hierarchy</h2>
<p>Facility 01 classifies operational threats into five distinct chromatic and conceptual tiers. When breaches or resonance anomalies occur, Floor 1 issues facility-wide acoustic and holographic alerts:</p>

<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Alert Code</th>
      <th>Threat Level</th>
      <th>Trigger Condition</th>
      <th>Executive Response</th>
      <th>Lead Authorization</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="badge badge-aether">GREEN / AETHER</span></td>
      <td>Routine (Minor)</td>
      <td>Single work failure, SP drain &lt; 20%</td>
      <td>Standard medical check, counseling</td>
      <td>Floor Lead Overseer</td>
    </tr>
    <tr>
      <td><span class="badge badge-somna">AMBER / SOMNA</span></td>
      <td>Moderate</td>
      <td>Coherence Counter drops to 1, minor breach</td>
      <td>Dispatch Floor 2 Strike Squads</td>
      <td><a class="wiki-link" href="../characters/the-containment-lead-dekan.html">Dekan</a> / <a class="wiki-link" href="../characters/the-border-lead-mellda.html">Mellda</a></td>
    </tr>
    <tr>
      <td><span class="badge badge-morphean">CRIMSON / MORPHEAN</span></td>
      <td>High Risk</td>
      <td>Multiple entities breached, corridor panic</td>
      <td>Lockdown floor elevators, authorize M.A.W. Class IV</td>
      <td><a class="wiki-link" href="../characters/the-outsider-ishall.html">Ishall</a> (Shadow Corps)</td>
    </tr>
    <tr>
      <td><span class="badge badge-phantasm">VIOLET / PHANTASM</span></td>
      <td>Catastrophic</td>
      <td>SE-002 or SE-005 full chamber rupture</td>
      <td>Authorize full lethal suppression, purge sub-corridors</td>
      <td><a class="wiki-link" href="../characters/the-director-majin.html">Director Majin</a></td>
    </tr>
    <tr>
      <td><span class="badge badge-apocrypha">BLACK / APOCRYPHA</span></td>
      <td>Existential</td>
      <td>SE-010 Event Horizon expansion / Core Meltdown</td>
      <td>Execute Absolvohan Seed Failsafe / Facility Cycle Reset</td>
      <td><a class="wiki-link" href="../characters/the-director-majin.html">Majin</a> + High Council</td>
    </tr>
  </tbody>
</table>
</div>

<h2>3. Executive Override Protocol Transcripts</h2>
<div class="terminal-callout">
  <div class="callout-header">RECORDING ARCHIVE // CYCLE 1,412 // OVERRIDE LOG 88-ALPHA</div>
  <p><strong>[SEIYON]:</strong> "Director. Floor 5 reports containment failure in Cell Block 02. The Grieving Colossus has cracked the bedrock foundation."</p>
  <p><strong>[MAJIN]:</strong> "Do not deploy local guards. Divert the Han-Flux siphons from Floor 3 directly into the acoustic dampeners on Floor 1. Give Dekan full tactical override on Maw's Keep armaments."</p>
  <p><strong>[SEIYON]:</strong> "Acknowledged. Overriding safety latches on Arsenal Vault 04. Authorizing Level IV M.A.W. Mourning Maul deployment."</p>
</div>
'''
        },

        # 2. Floor 2 Arsenal Vaults
        {
            "dir": "departments",
            "file": "floor-2-arsenal-vaults.html",
            "title": "Maw's Keep Armory &amp; M.A.W. Forging Vaults",
            "category": "Facility Operations",
            "cat_url": "../departments/index.html",
            "hero_img": "../assets/layout/hand/blueprints/floor-2-maws-keep-blueprint.svg",
            "lead": "ARMORY OVERSEERS // STRIKE FORCE LIAISONS",
            "code": "VAULT-MAW-02",
            "clearance": "LEVEL 4 CLEARANCE",
            "content": '''
<h2>1. Maw's Keep Armory Architecture</h2>
<p>Floor 2, colloquially known as <strong>Maw's Keep</strong>, houses the master fabrication chambers, crystallization forges, and secure distribution vaults for all <a class="wiki-link" href="../mechanics/maw-equipment-system.html">M.A.W. Equipment</a> extracted from Sorrow Entities.</p>

<div class="wiki-callout hazard-box">
  <div class="callout-header">HAZARD WARNING // M.A.W. RESONANCE FEEDBACK</div>
  <p>M.A.W. weaponry and armor retain cognitive fragments of the donor entity. Personnel entering Vaults 01 through 08 must wear Han-insulated earplugs to avoid phantom auditory corrosion.</p>
</div>

<h2>2. Forging &amp; Crystallization Matrix</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Vault ID</th>
      <th>Equipment Tier</th>
      <th>Donor Entity Class</th>
      <th>Temperature / Pressure</th>
      <th>Corrosion Risk</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Vault 01-03</td>
      <td>Grade I - II (Aether / Somna)</td>
      <td>SE-001, SE-007, SE-011</td>
      <td>450°C // 120 kPa Han-Vapor</td>
      <td>Low (&lt; 5%)</td>
    </tr>
    <tr>
      <td>Vault 04-06</td>
      <td>Grade III - IV (Morphean / Phantasm)</td>
      <td>SE-002, SE-003, SE-005, SE-014, SE-015</td>
      <td>1,200°C // 850 kPa Han-Vapor</td>
      <td>Moderate (15% - 30%)</td>
    </tr>
    <tr>
      <td>Vault 07-08</td>
      <td>Grade V (Apocrypha)</td>
      <td>SE-010 (The Convergence)</td>
      <td>Cryogenic Stasis // Gravitational Lock</td>
      <td>Critical (&gt; 75%)</td>
    </tr>
  </tbody>
</table>
</div>

<h2>3. Armory Maintenance Protocols</h2>
<p>Each M.A.W. suit and weapon undergoes a strict 12-hour recalibration cycle between deployments. If an agent suffers a panic breakdown during work, their assigned suit is immediately quarantined in Floor 2's Decontamination Chambers for spiritual scrubbing.</p>
'''
        },

        # 3. Extraction Protocols
        {
            "dir": "departments",
            "file": "floor-3-extraction-protocols.html",
            "title": "Extraction Hall Han-Flux Siphoning Protocols",
            "category": "Facility Operations",
            "cat_url": "../departments/index.html",
            "hero_img": "../assets/layout/hand/blueprints/floor-3-extraction-hall-blueprint.svg",
            "lead": "EXTRACTION LEAD ZYRAK",
            "code": "SIPHON-HALL-03",
            "clearance": "LEVEL 4 CLEARANCE",
            "content": '''
<h2>1. Primary Extraction Operations</h2>
<p>Overseen by <a class="wiki-link" href="../characters/the-extraction-lead-zyrak.html">Extraction Lead Zyrak</a>, Floor 3 is the industrial powerhouse of Facility 01. The Extraction Hall captures the emotional and structural resonance generated during agent work and condenses it into refined <a class="wiki-link" href="../mechanics/han-energy-and-damage.html">Han-Flux</a> energy.</p>

<h2>2. Han-Flux Condensation Yields by Work Type</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Work Type</th>
      <th>Primary Target</th>
      <th>Base Energy Yield</th>
      <th>Success Variance</th>
      <th>Critical Extraction Bonus</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Instinct</strong></td>
      <td>Physiological Needs</td>
      <td>16 - 22 Flux</td>
      <td>± 15%</td>
      <td>+8 Flux (Fortitude Rank V)</td>
    </tr>
    <tr>
      <td><strong>Insight</strong></td>
      <td>Containment Environment</td>
      <td>18 - 24 Flux</td>
      <td>± 10%</td>
      <td>+10 Flux (Prudence Rank V)</td>
    </tr>
    <tr>
      <td><strong>Attachment</strong></td>
      <td>Social &amp; Emotional Bond</td>
      <td>20 - 28 Flux</td>
      <td>± 20%</td>
      <td>+14 Flux (Temperance Rank V)</td>
    </tr>
    <tr>
      <td><strong>Repression</strong></td>
      <td>Suppression of Entity Will</td>
      <td>24 - 34 Flux</td>
      <td>± 35%</td>
      <td>+20 Flux (Justice Rank V)</td>
    </tr>
  </tbody>
</table>
</div>

<h2>3. Emergency Siphon Pressure Dump</h2>
<p>If Han vats reach 95% capacity without city grid consumption, Zyrak's automated relief valves vent excess flux into the Desolate exterior buffer via subterranean exhaust conduits.</p>
'''
        },

        # 4. Insight Observation Labs
        {
            "dir": "departments",
            "file": "floor-4-insight-observation-labs.html",
            "title": "Insight Forge Research Labs &amp; Analysis Archive",
            "category": "Facility Operations",
            "cat_url": "../departments/index.html",
            "hero_img": "../assets/layout/hand/blueprints/floor-4-insight-forge-blueprint.svg",
            "lead": "RESEARCH LEAD AYSHUK",
            "code": "LABS-FORGE-04",
            "clearance": "LEVEL 4 CLEARANCE",
            "content": '''
<h2>1. Scientific Observation Framework</h2>
<p>Directed by <a class="wiki-link" href="../characters/the-research-lead-ayshuk.html">Research Lead Ayshuk</a>, the Insight Forge decodes the psychological and physical anatomy of Sorrow Entities. High-speed spectrometers and neural resonance probes record entity emotional fluctuations in real time.</p>

<h2>2. Observation &amp; Research Stages</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Research Level</th>
      <th>Observation Requisite</th>
      <th>Unlocked Intel</th>
      <th>Work Success Bonus</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Level I (Initial)</td>
      <td>10 Work Sessions</td>
      <td>Basic Work Preferences, Damage Type</td>
      <td>+0%</td>
    </tr>
    <tr>
      <td>Level II (Anatomy)</td>
      <td>25 Work Sessions</td>
      <td>Exact Escape Counter &amp; Breach Triggers</td>
      <td>+5% Work Success</td>
    </tr>
    <tr>
      <td>Level III (Resonance)</td>
      <td>50 Work Sessions</td>
      <td>M.A.W. Extraction Recipes Unlocked</td>
      <td>+10% Work Success, -10% SP Damage</td>
    </tr>
    <tr>
      <td>Level IV (Mastery)</td>
      <td>100 Work Sessions</td>
      <td>Full Canonical Story &amp; Flavor Dossier</td>
      <td>+15% Work Success, +20% Extraction Yield</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 5. Border Watch Containment Cells
        {
            "dir": "departments",
            "file": "floor-5-border-containment-cells.html",
            "title": "Border Watch High-Security Containment Matrix",
            "category": "Facility Operations",
            "cat_url": "../departments/index.html",
            "hero_img": "../assets/layout/hand/blueprints/floor-5-border-watch-blueprint.svg",
            "lead": "BORDER LEAD MELLDA",
            "code": "BORDER-CELLS-05",
            "clearance": "LEVEL 4 CLEARANCE",
            "content": '''
<h2>1. Border Watch Defensive Grid</h2>
<p>Under <a class="wiki-link" href="../characters/the-border-lead-mellda.html">Border Lead Mellda</a>, Floor 5 houses the highest concentration of high-risk <a class="wiki-link" href="../entities/index.html">Sorrow Entities</a>. The floor utilizes reinforced triple-layered ballistic glass, hydraulic bulkheads, and neural suppression gas emitters.</p>

<h2>2. High-Risk Containment Chamber Specifications</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Cell Designation</th>
      <th>Housed Entity</th>
      <th>Wall Thickness</th>
      <th>Dampener Frequency</th>
      <th>Emergency Containment Routine</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cell 05-A</td>
      <td><a class="wiki-link" href="../entities/se-002-the-grieving-colossus.html">SE-002 (Grieving Colossus)</a></td>
      <td>4.5m Reinforced Basalt</td>
      <td>12.4 Hz Seismic Dampeners</td>
      <td>Nitrogen Quench &amp; Hydraulic Clamps</td>
    </tr>
    <tr>
      <td>Cell 05-B</td>
      <td><a class="wiki-link" href="../entities/se-005-the-smothering-mother.html">SE-005 (Smothering Mother)</a></td>
      <td>3.0m Obsidian Lattice</td>
      <td>88.2 kHz Ultrasound Cutters</td>
      <td>Thermal Arc Incineration Grid</td>
    </tr>
    <tr>
      <td>Cell 05-C</td>
      <td><a class="wiki-link" href="../entities/se-014-the-debt-eater.html">SE-014 (The Debt Eater)</a></td>
      <td>3.5m Iron-Lead Alloy</td>
      <td>Karmic Field Nullifier</td>
      <td>Molten Lead Floor Inundation</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 6. Deep Vault Records
        {
            "dir": "departments",
            "file": "floor-6-deep-vault-records.html",
            "title": "Deep Vault Classified Sub-Level Archives",
            "category": "Facility Operations",
            "cat_url": "../departments/index.html",
            "hero_img": "../assets/layout/hand/blueprints/floor-6-deep-vault-blueprint.svg",
            "lead": "CONTAINMENT LEAD DEKAN // MARJUK",
            "code": "VAULT-DEEP-06",
            "clearance": "LEVEL 5 CLEARANCE",
            "content": '''
<h2>1. Classified Sub-Level 6 Overview</h2>
<p>Floor 6 represents the deepest physical and historical stratum of The Hand of Change. Managed by <a class="wiki-link" href="../characters/the-containment-lead-dekan.html">Dekan</a> and <a class="wiki-link" href="../characters/the-archive-lead-marjuk.html">Marjuk</a>, it preserves unexpunged logs from all 1,778 previous facility cycles and sealed Sorrow Seeds.</p>

<div class="wiki-callout terminal-callout">
  <div class="callout-header">ARCHIVAL RESTRICTION // DEKAN'S SEAL</div>
  <p>Personnel below Level 5 clearance attempting to access File Register DEEP-1778 will be subject to immediate memory wipe via The Memory Washers protocol.</p>
</div>

<h2>2. Sealed Historical Artifacts</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Artifact Code</th>
      <th>Classification</th>
      <th>Historical Cycle</th>
      <th>Current Containment State</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SEED-ALPHA-01</td>
      <td>Primordial Sorrow Seed</td>
      <td>Cycle 0001 (Original)</td>
      <td>Cryogenic Chrono-Lock</td>
    </tr>
    <tr>
      <td>REVERIE-REC-44</td>
      <td>Uncut Audio of Sovereign Edicts</td>
      <td>Cycle 0418</td>
      <td>Electromagnetic Shield Box</td>
    </tr>
    <tr>
      <td>CORE-DEKAN-REMNANT</td>
      <td>Shattered Echo-Core Matrix</td>
      <td>Cycle 1205</td>
      <td>Sub-Level Vacuum Chamber</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 7. Shadow Corps Operations
        {
            "dir": "departments",
            "file": "floor-7-shadow-corps-operations.html",
            "title": "Shadow Corps Rapid Interception &amp; Suppression Units",
            "category": "Tactical Operations",
            "cat_url": "../departments/index.html",
            "hero_img": "../assets/layout/hand/blueprints/floor-7-shadow-corps-blueprint.svg",
            "lead": "THE OUTSIDER ISHALL",
            "code": "CORPS-SHADOW-07",
            "clearance": "LEVEL 4 CLEARANCE",
            "content": '''
<h2>1. Shadow Corps Tactical Doctrine</h2>
<p>Commanded by <a class="wiki-link" href="../characters/the-outsider-ishall.html">Ishall</a>, the Shadow Corps serves as the rapid-response breach interception force within Facility 01. Trained in lethal and non-lethal suppression maneuvers, they specialize in intercepting high-threat entities before breach waves reach the central lifts.</p>

<h2>2. Suppression Squad Formations</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Formation Role</th>
      <th>Recommended M.A.W.</th>
      <th>Primary Attribute</th>
      <th>Tactical Objective</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Point Vanguard</strong></td>
      <td>The Mourning Maul + Mourning Mantle</td>
      <td>Fortitude V (HP 120+)</td>
      <td>Absorb Crimson damage, hold entity aggro</td>
    </tr>
    <tr>
      <td><strong>Acoustic Breaker</strong></td>
      <td>Lament's Requiem + Lament's Shroud</td>
      <td>Prudence V (SP 110+)</td>
      <td>Inflict Stagger via Cyan resonant damage</td>
    </tr>
    <tr>
      <td><strong>Needle Skirmisher</strong></td>
      <td>The Embrace Fang + Embrace Plate</td>
      <td>Temperance V (SPD 130+)</td>
      <td>Flank breached entities, sever support tendrils</td>
    </tr>
    <tr>
      <td><strong>Singularity Scribe</strong></td>
      <td>The Absolute Maul + Absolute Mantle</td>
      <td>Justice V (ATK 125+)</td>
      <td>Execute stagger-locked targets with Pale damage</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 8. Gate Watch Perimeter
        {
            "dir": "departments",
            "file": "floor-8-gate-watch-perimeter.html",
            "title": "Gate Watch Desolate Defense Grids",
            "category": "Tactical Operations",
            "cat_url": "../departments/index.html",
            "hero_img": "../assets/layout/hand/blueprints/floor-8-gate-watch-blueprint.svg",
            "lead": "THE EXILE XYAN",
            "code": "GATE-DEFENSE-08",
            "clearance": "LEVEL 4 CLEARANCE",
            "content": '''
<h2>1. Perimeter Defense Architecture</h2>
<p>Supervised by <a class="wiki-link" href="../characters/the-exile-xyan.html">The Exile Xyan</a>, Floor 8 guards the boundary between Facility 01 and the endless, hostile expanses of <strong>The Desolate</strong>. It maintains massive long-range Han-barrier projectors that prevent wilderness entities from burrowing into the lower sub-levels.</p>

<h2>2. Desolate Anomaly Detection Parameters</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Radar Sector</th>
      <th>Monitored Threat</th>
      <th>Detection Radius</th>
      <th>Barrier Response</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Sector North-West</td>
      <td>Wilderness Tide Surges (SE-003)</td>
      <td>15.0 km</td>
      <td>Activate Thermal Barrier Grid</td>
    </tr>
    <tr>
      <td>Sector East</td>
      <td>Wound Walker Incursions</td>
      <td>8.5 km</td>
      <td>Deploy Giltong Automated Rail Cannons</td>
    </tr>
    <tr>
      <td>Sector South-Depths</td>
      <td>Subterranean Han Geysers</td>
      <td>4.2 km</td>
      <td>Engage Seismic Pressure Relievers</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 9. Facility Meltdown Procedures
        {
            "dir": "departments",
            "file": "facility-meltdown-procedures.html",
            "title": "Facility-Wide Meltdown &amp; Resonance Alarm Procedures",
            "category": "Emergency Protocols",
            "cat_url": "../departments/index.html",
            "hero_img": "../assets/diagrams/han_flux_resonance_cycle.svg",
            "lead": "FACILITY-WIDE EMERGENCY DIRECTIVE",
            "code": "MELTDOWN-ALL-00",
            "clearance": "FACILITY-WIDE BROADCAST",
            "content": '''
<h2>1. Meltdown Phase Overview</h2>
<p>A Facility Meltdown occurs when containment failures exceed operational threshold tolerances, causing Han-Flux pressure to destabilize across all 8 floors simultaneously.</p>

<div class="wiki-callout hazard-box">
  <div class="callout-header">GENERAL EVACUATION ORDER // CODE MELTDOWN</div>
  <p>When Meltdown Level IV triggers, all non-combat research staff must immediately assemble in Floor 1 Bunkers. Lifts will lock on descent.</p>
</div>

<h2>2. The Meltdown Response Timeline</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Time Elapsed</th>
      <th>System Status</th>
      <th>Automated Action</th>
      <th>Personnel Instruction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>00:00 - 02:00</td>
      <td>Coherence Cascade</td>
      <td>Chamber warning sirens sound</td>
      <td>Assign agents to immediate work to clear counters</td>
    </tr>
    <tr>
      <td>02:01 - 05:00</td>
      <td>Energy Siphon Overload</td>
      <td>Power cuts to non-essential sub-wings</td>
      <td>Deploy Floor 7 Shadow Corps to breach sectors</td>
    </tr>
    <tr>
      <td>05:01 - 10:00</td>
      <td>Multi-Chamber Rupture</td>
      <td>Sub-level bulkheads drop permanently</td>
      <td>Lethal suppression authorized with all M.A.W. gear</td>
    </tr>
    <tr>
      <td>&gt; 10:00</td>
      <td>Core Collapse Imminent</td>
      <td>Director Majin executes Absolvohan reset</td>
      <td>Brace for Cycle termination sequence</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 10. Core Suppression Guidelines
        {
            "dir": "departments",
            "file": "core-suppression-guidelines.html",
            "title": "Echo-Core Resonant Meltdown &amp; Suppression Guidelines",
            "category": "Emergency Protocols",
            "cat_url": "../departments/index.html",
            "hero_img": "../assets/banners/banner_hero_echo_cores.svg",
            "lead": "DIRECTOR MAJIN // HIGH ARCHITECTS",
            "code": "CORE-SUPPRESS-09",
            "clearance": "LEVEL 5 CLEARANCE",
            "content": '''
<h2>1. Echo-Core Meltdown Phenomenon</h2>
<p>When an <a class="wiki-link" href="../departments/index.html">Echo-Core</a> suffers overwhelming psychological trauma or ideological fracture, their resonance field erupts, transforming their assigned department into a surreal, hostile dream-construct.</p>

<h2>2. Department Debuffs During Core Meltdown</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Echo-Core</th>
      <th>Associated Department</th>
      <th>Meltdown Manifestation</th>
      <th>Department-Wide Debuff</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a class="wiki-link" href="../characters/the-director-majin.html">Majin</a></td>
      <td>Floor 1 (Neutral Command)</td>
      <td>Absolute Nihilistic Silence</td>
      <td>All Agents suffer 50% reduced Work Speed</td>
    </tr>
    <tr>
      <td><a class="wiki-link" href="../characters/the-containment-lead-dekan.html">Dekan</a></td>
      <td>Floor 6 (Deep Vault)</td>
      <td>Overlapping Memory Labyrinths</td>
      <td>Randomized corridor doors, SP drops by 5/sec</td>
    </tr>
    <tr>
      <td><a class="wiki-link" href="../characters/the-extraction-lead-zyrak.html">Zyrak</a></td>
      <td>Floor 3 (Extraction Hall)</td>
      <td>Molten Han-Flux Geysers</td>
      <td>Floors deal continuous Crimson damage to unarmored staff</td>
    </tr>
    <tr>
      <td><a class="wiki-link" href="../characters/the-border-lead-mellda.html">Mellda</a></td>
      <td>Floor 5 (Border Watch)</td>
      <td>Paranoid Razor Wire Field</td>
      <td>Movement speed reduced by 60%, bleeding on sprint</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 11. SE-001 Containment Log
        {
            "dir": "entities",
            "file": "se-001-containment-log.html",
            "title": "SE-001 The Orphaned Bell — Acoustic Containment &amp; Toll Logs",
            "category": "Sorrow Entities",
            "cat_url": "../entities/index.html",
            "hero_img": "../assets/art/entities/se-001.svg",
            "lead": "CLASSIFICATION: SE-001 // SOMNA",
            "code": "LOG-ACOUSTIC-001",
            "clearance": "LEVEL 2 CLEARANCE",
            "content": '''
<h2>1. Acoustic Containment Specifications</h2>
<p><strong>SE-001 (The Orphaned Bell)</strong> requires specialized acoustic vibration dampeners mounted inside its containment chamber. When an agent enters the cell, the chime resonance shifts dynamically based on the agent's emotional state.</p>

<div class="wiki-callout terminal-callout">
  <div class="callout-header">ACOUSTIC FREQUENCY LOG // CELL 01</div>
  <p><strong>Base Resonance:</strong> 432 Hz (Mourning Frequency)</p>
  <p><strong>Toll Breach Frequency:</strong> 1,778 Hz (Harmonic Inversion)</p>
  <p><strong>Decibel Level at Breach:</strong> 142 dB (Shatters standard eardrums)</p>
</div>

<h2>2. Work Affinity &amp; Success Probabilities</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Work Type</th>
      <th>Agent Level I</th>
      <th>Agent Level II</th>
      <th>Agent Level III</th>
      <th>Agent Level IV</th>
      <th>Agent Level V</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Instinct</strong></td>
      <td>30%</td>
      <td>35%</td>
      <td>40%</td>
      <td>45%</td>
      <td>50%</td>
    </tr>
    <tr>
      <td><strong>Insight</strong></td>
      <td>50%</td>
      <td>55%</td>
      <td>60%</td>
      <td>65%</td>
      <td>70%</td>
    </tr>
    <tr>
      <td><strong>Attachment</strong></td>
      <td><span class="badge badge-emerald">70%</span></td>
      <td><span class="badge badge-emerald">75%</span></td>
      <td><span class="badge badge-emerald">80%</span></td>
      <td><span class="badge badge-emerald">85%</span></td>
      <td><span class="badge badge-emerald">90%</span></td>
    </tr>
    <tr>
      <td><strong>Repression</strong></td>
      <td>20%</td>
      <td>25%</td>
      <td>30%</td>
      <td>35%</td>
      <td>40%</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 12. SE-002 Incident Log
        {
            "dir": "entities",
            "file": "se-002-incident-log.html",
            "title": "SE-002 The Grieving Colossus — Seismic Fissure Incident Logs",
            "category": "Sorrow Entities",
            "cat_url": "../entities/index.html",
            "hero_img": "../assets/art/entities/se-002.svg",
            "lead": "CLASSIFICATION: SE-002 // PHANTASM",
            "code": "INCIDENT-SEISMIC-002",
            "clearance": "LEVEL 4 CLEARANCE",
            "content": '''
<h2>1. Structural Seismic Impact</h2>
<p><strong>SE-002 (The Grieving Colossus)</strong> is a monolithic stone construct embodying the physical weight of Somnarak's crushed districts. When agitated, its weeping fissures release molten Crimson Han that shatters sub-level masonry.</p>

<h2>2. Recorded Breach Incident 002-C (Cycle 1,602)</h2>
<div class="terminal-callout">
  <div class="callout-header">SUPPRESSION RECORD 002-C // DURATION: 24 MINS</div>
  <p><strong>[DEKAN]:</strong> "Colossus has breached Cell 05-A. Stomp seismic waves are registering magnitude 6.2 on Floor 2."</p>
  <p><strong>[SUPPRESSION LEAD]:</strong> "Engage Vanguard formation. Mourning Maul team, strike the left knee fissure. Do not allow it to reach the central elevator shaft."</p>
  <p><strong>Casualties:</strong> 3 Fractured, 7 Incapacitated, 0 Fatalities. Colossus re-contained via Nitrogen Quench.</p>
</div>
'''
        },

        # 13. SE-003 Field Survey
        {
            "dir": "entities",
            "file": "se-003-field-survey.html",
            "title": "SE-003 The Wilderness Tide — Fluidic Incursion Survey",
            "category": "Sorrow Entities",
            "cat_url": "../entities/index.html",
            "hero_img": "../assets/art/entities/se-003.svg",
            "lead": "CLASSIFICATION: SE-003 // MORPHEAN",
            "code": "SURVEY-TIDE-003",
            "clearance": "LEVEL 3 CLEARANCE",
            "content": '''
<h2>1. Fluidic Properties of the Wilderness Tide</h2>
<p><strong>SE-003 (The Wilderness Tide)</strong> is a non-Newtonian bio-fluidic surge originating from the Desolate wilderness. It manifests as a rolling tsunami of crimson-black grief fluid containing grasping skeletal limbs.</p>

<h2>2. Damage Type &amp; Resistance Analysis</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Damage Type</th>
      <th>Resistance Multiplier</th>
      <th>Effectiveness Assessment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="badge badge-crimson">Crimson (Physical)</span></td>
      <td>0.8 (Resistant)</td>
      <td>Fluid absorbs blunt concussive kinetic force</td>
    </tr>
    <tr>
      <td><span class="badge badge-somna">Cyan (Mental)</span></td>
      <td>1.5 (Vulnerable)</td>
      <td>Acoustic resonance disrupts fluidic surface tension</td>
    </tr>
    <tr>
      <td><span class="badge badge-emerald">Emerald (Erosion)</span></td>
      <td>1.0 (Normal)</td>
      <td>Standard biological decay rate</td>
    </tr>
    <tr>
      <td><span class="badge badge-pale">Pale (Existential)</span></td>
      <td>2.0 (Fatal)</td>
      <td>Absolute existential void severs Han connection</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 14. SE-005 Suppression Guide
        {
            "dir": "entities",
            "file": "se-005-suppression-guide.html",
            "title": "SE-005 The Smothering Mother — Thread Severing Tactical Guide",
            "category": "Sorrow Entities",
            "cat_url": "../entities/index.html",
            "hero_img": "../assets/art/entities/se-005.svg",
            "lead": "CLASSIFICATION: SE-005 // PHANTASM",
            "code": "GUIDE-SEVER-005",
            "clearance": "LEVEL 4 CLEARANCE",
            "content": '''
<h2>1. Entity Threat Profile</h2>
<p><strong>SE-005 (The Smothering Mother)</strong> towers over containment chambers, weaving suffocating swaddling silk that binds and fractures agents attempting to leave her vicinity. Agents with low Justice are especially susceptible to her maternal enthrallment.</p>

<h2>2. Tactical Thread Severing Protocol</h2>
<p>1. Deploy agents equipped with high-speed slashing weapons (<a class="wiki-link" href="../maw/maw-w-005-01-the-embrace-fang.html">The Embrace Fang</a> or <a class="wiki-link" href="../maw/maw-w-001-01-the-laments-requiem.html">Lament's Requiem</a>).</p>
<p>2. Keep agent distance &gt; 5 meters to prevent the Swaddling Embrace animation.</p>
<p>3. If an agent is cocooned, apply Cyan acoustic damage to the silk bindings within 8 seconds to prevent immediate Fracturing.</p>
'''
        },

        # 15. SE-007 Observation Log
        {
            "dir": "entities",
            "file": "se-007-observation-log.html",
            "title": "SE-007 Brume — Particulate Spectral Analysis &amp; Chamber Logs",
            "category": "Sorrow Entities",
            "cat_url": "../entities/index.html",
            "hero_img": "../assets/art/entities/se-007.svg",
            "lead": "CLASSIFICATION: SE-007 // AETHER",
            "code": "OBS-BRUME-007",
            "clearance": "LEVEL 2 CLEARANCE",
            "content": '''
<h2>1. Aerosolized Grief Characteristics</h2>
<p><strong>SE-007 (Brume)</strong> manifests as an ambient pale fog suspended with microscopic weeping ocular structures. It induces serene melancholy in personnel, gradually eroding vigilance.</p>

<h2>2. Environmental Filtration Thresholds</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Exposure Duration</th>
      <th>Aerosol Density</th>
      <th>Agent Behavioral Response</th>
      <th>Required Countermeasure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0 - 15 Mins</td>
      <td>15 ppm</td>
      <td>Mild tear production, calm state</td>
      <td>Standard charcoal filter</td>
    </tr>
    <tr>
      <td>16 - 45 Mins</td>
      <td>45 ppm</td>
      <td>Auditory hallucinations of distant sobbing</td>
      <td>Insight work adjustment, oxygen purge</td>
    </tr>
    <tr>
      <td>&gt; 45 Mins</td>
      <td>120 ppm</td>
      <td>Spontaneous weeping, refusal to exit chamber</td>
      <td>Immediate evacuation &amp; SP booster injection</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 16. SE-009 Memory Extracts
        {
            "dir": "entities",
            "file": "se-009-memory-extracts.html",
            "title": "SE-009 The Memory Weaver — Filament Decryption Logs",
            "category": "Sorrow Entities",
            "cat_url": "../entities/index.html",
            "hero_img": "../assets/art/entities/se-009.svg",
            "lead": "CLASSIFICATION: SE-009 // MORPHEAN",
            "code": "EXTRACT-WEAVE-009",
            "clearance": "LEVEL 3 CLEARANCE",
            "content": '''
<h2>1. Decrypted Memory Filaments</h2>
<p><strong>SE-009 (The Memory Weaver)</strong> spins delicate clockwork threads from the forgotten memories of Somnarak citizens. In the Insight Forge, Research Lead Ayshuk successfully intercepted and decrypted several woven fragments:</p>

<div class="terminal-callout">
  <div class="callout-header">DECRYPTED WEAVE #09-44 // CYCLE 0712</div>
  <p><em>"We built the spires so high because the weeping was louder near the earth. But the sky had its own sorrow. The clouds tasted of old iron and broken vows."</em></p>
</div>

<div class="terminal-callout">
  <div class="callout-header">DECRYPTED WEAVE #09-88 // CYCLE 1104</div>
  <p><em>"Do not let the Director turn the clock again. Every cycle we forget a little more of who we were before the walls went up."</em></p>
</div>
'''
        },

        # 17. SE-010 Verdict Records
        {
            "dir": "entities",
            "file": "se-010-verdict-records.html",
            "title": "SE-010 The Convergence — Gravitational Singularity Verdicts",
            "category": "Sorrow Entities",
            "cat_url": "../entities/index.html",
            "hero_img": "../assets/art/entities/se-010.svg",
            "lead": "CLASSIFICATION: SE-010 // APOCRYPHA",
            "code": "VERDICT-SINGULARITY-010",
            "clearance": "LEVEL 5 CLEARANCE",
            "content": '''
<h2>1. Singularity Event Horizon Mechanics</h2>
<p><strong>SE-010 (The Convergence)</strong> represents the ultimate consolidation of all unresolved existential debt across Somnarak. It forms a localized gravitational singularity surrounded by shattered floating masks.</p>

<div class="wiki-callout hazard-box">
  <div class="callout-header">APOCRYPHA CLASS WARNING // DO NOT APPROACH ALONE</div>
  <p>Repression work on SE-010 is restricted to Level V Agents with Justice &gt; 130 and Pale resistance &lt; 0.5. A single failure reduces the Coherence Counter to 0, triggering instant event horizon collapse.</p>
</div>

<h2>2. Work Probability Matrix (SE-010)</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Work Type</th>
      <th>Success Rate (Level V)</th>
      <th>Damage Received</th>
      <th>Outcome on Failure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Instinct</td>
      <td>10%</td>
      <td>40 - 60 Pale Damage</td>
      <td>Agent Ingested into Singularity</td>
    </tr>
    <tr>
      <td>Insight</td>
      <td>25%</td>
      <td>35 - 50 Pale Damage</td>
      <td>Corridor Gravity Inversion</td>
    </tr>
    <tr>
      <td>Attachment</td>
      <td>15%</td>
      <td>45 - 65 Pale Damage</td>
      <td>Instant Panic (Fanatic)</td>
    </tr>
    <tr>
      <td><strong>Repression</strong></td>
      <td><span class="badge badge-apocrypha">60%</span></td>
      <td>20 - 30 Pale Damage</td>
      <td>Energy Yield: 40 Han Flux</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 18. SE-011 Acoustic Analysis
        {
            "dir": "entities",
            "file": "se-011-acoustic-analysis.html",
            "title": "SE-011 The Whispering Walls — Resonance Spectral Analysis",
            "category": "Sorrow Entities",
            "cat_url": "../entities/index.html",
            "hero_img": "../assets/art/entities/se-011.svg",
            "lead": "CLASSIFICATION: SE-011 // SOMNA",
            "code": "ACOUSTIC-WALLS-011",
            "clearance": "LEVEL 2 CLEARANCE",
            "content": '''
<h2>1. Acoustic Spectral Analysis</h2>
<p><strong>SE-011 (The Whispering Walls)</strong> consists of brutalist concrete slabs embedded with countless murmuring human relief faces. When exposed to ambient quiet, the whispers amplify into a cacophony that drains agent Sanity Points (SP).</p>

<h2>2. Noise Cancellation Thresholds</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Frequency Band</th>
      <th>Murmur Type</th>
      <th>Psychological Symptom</th>
      <th>Recommended M.A.W. Suit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>50 - 200 Hz</td>
      <td>Low Sub-Bass Moans</td>
      <td>Chest tightness, anxiety</td>
      <td><a class="wiki-link" href="../maw/maw-s-001-01-the-laments-shroud.html">Lament's Shroud</a></td>
    </tr>
    <tr>
      <td>1.2 - 3.5 kHz</td>
      <td>Vocal Accusations</td>
      <td>Guilt-induced hallucination</td>
      <td><a class="wiki-link" href="../maw/maw-s-011-01-the-listening-shroud.html">Listening Shroud</a></td>
    </tr>
    <tr>
      <td>8.0 - 15 kHz</td>
      <td>High Piercing Screams</td>
      <td>Instant ear bleeding, panic</td>
      <td><a class="wiki-link" href="../maw/maw-s-007-01-the-hope-veil.html">Hope Veil</a></td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 19. SE-014 Debt Ledger
        {
            "dir": "entities",
            "file": "se-014-debt-ledger.html",
            "title": "SE-014 The Debt Eater — Karmic Accounting &amp; Ingestion Records",
            "category": "Sorrow Entities",
            "cat_url": "../entities/index.html",
            "hero_img": "../assets/art/entities/se-014.svg",
            "lead": "CLASSIFICATION: SE-014 // PHANTASM",
            "code": "LEDGER-EATER-014",
            "clearance": "LEVEL 4 CLEARANCE",
            "content": '''
<h2>1. Karmic Accounting Overview</h2>
<p><strong>SE-014 (The Debt Eater)</strong> feeds on the physical and conceptual ledgers of unpayable civic debts accrued across the City of Somnarak. Its golden fangs and coin-scaled hide convert financial despair into raw physical violence.</p>

<h2>2. Ingestion &amp; Satiation Ledger</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Feeding Item</th>
      <th>Karmic Value</th>
      <th>Coherence Counter Delta</th>
      <th>Breach Risk Modifier</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Old Ledger Parchment</td>
      <td>50 Coins</td>
      <td>+1 Counter</td>
      <td>-10% Breach Chance</td>
    </tr>
    <tr>
      <td>Sovereign Promissory Note</td>
      <td>500 Coins</td>
      <td>+2 Counters</td>
      <td>-25% Breach Chance</td>
    </tr>
    <tr>
      <td>Forged Relic Token</td>
      <td>0 Coins (Fraud)</td>
      <td>-2 Counters (Anger)</td>
      <td>+50% Immediate Breach</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 20. SE-015 Equilibrium Trials
        {
            "dir": "entities",
            "file": "se-015-equilibrium-trials.html",
            "title": "SE-015 The Debt Scale — Moral Equilibrium Trial Records",
            "category": "Sorrow Entities",
            "cat_url": "../entities/index.html",
            "hero_img": "../assets/art/entities/se-015.svg",
            "lead": "CLASSIFICATION: SE-015 // MORPHEAN",
            "code": "TRIALS-SCALE-015",
            "clearance": "LEVEL 3 CLEARANCE",
            "content": '''
<h2>1. The Dual Pan Balance Mechanism</h2>
<p><strong>SE-015 (The Debt Scale)</strong> floats silently within its containment cell, weighing an obsidian heart of past cruelty against crystallized tears of genuine remorse. If the balance tips beyond 30 degrees in either direction, a pulse of moral dissonance floods the corridor.</p>

<h2>2. Work Calibration Results</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Work Type</th>
      <th>Scale Reaction</th>
      <th>Energy Yield</th>
      <th>Agent SP Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Instinct</td>
      <td>Tips toward Heart (+15°)</td>
      <td>14 Flux</td>
      <td>-12 HP / -5 SP</td>
    </tr>
    <tr>
      <td>Insight</td>
      <td>Stabilizes Center (0°)</td>
      <td>22 Flux</td>
      <td>+10 SP Recovery</td>
    </tr>
    <tr>
      <td>Attachment</td>
      <td>Tips toward Tears (-15°)</td>
      <td>18 Flux</td>
      <td>-8 SP</td>
    </tr>
    <tr>
      <td><strong>Repression</strong></td>
      <td>Locks Fulcrum (0°)</td>
      <td>28 Flux</td>
      <td>+15 Flux Yield</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 21. MAW Crafting & Extraction
        {
            "dir": "maw",
            "file": "maw-crafting-and-extraction.html",
            "title": "M.A.W. Extraction, Han Crystallization &amp; Forging Systems",
            "category": "M.A.W. Arsenal",
            "cat_url": "../maw/index.html",
            "hero_img": "../assets/banners/banner_hero_maw_arsenal.svg",
            "lead": "MAW'S KEEP FORGE MASTERS",
            "code": "CRAFT-MAW-SYS",
            "clearance": "LEVEL 3 CLEARANCE",
            "content": '''
<h2>1. M.A.W. Extraction Framework</h2>
<p><strong>M.A.W. (Mental Armament Weaponry)</strong> equipment is forged directly from the resonant crystallization of Sorrow Entities. Unlike mundane steel or synthetic Kevlar, M.A.W. armaments channel the emotional reality of their donor entity to deal and resist specialized Han damage.</p>

<h2>2. Crystallization Cost &amp; Extraction Requisites</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Equipment Tier</th>
      <th>Observed Research Level</th>
      <th>Required Han Flux</th>
      <th>Agent Stat Prerequisite</th>
      <th>Extraction Limit per Cycle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="badge badge-aether">Grade I (Aether)</span></td>
      <td>Research Level I</td>
      <td>20 Flux</td>
      <td>Stat Rank I</td>
      <td>5 Copies</td>
    </tr>
    <tr>
      <td><span class="badge badge-somna">Grade II (Somna)</span></td>
      <td>Research Level II</td>
      <td>45 Flux</td>
      <td>Stat Rank II</td>
      <td>3 Copies</td>
    </tr>
    <tr>
      <td><span class="badge badge-morphean">Grade III (Morphean)</span></td>
      <td>Research Level III</td>
      <td>80 Flux</td>
      <td>Stat Rank III</td>
      <td>2 Copies</td>
    </tr>
    <tr>
      <td><span class="badge badge-phantasm">Grade IV (Phantasm)</span></td>
      <td>Research Level IV</td>
      <td>140 Flux</td>
      <td>Stat Rank IV</td>
      <td>1 Copy</td>
    </tr>
    <tr>
      <td><span class="badge badge-apocrypha">Grade V (Apocrypha)</span></td>
      <td>Research Level IV (Max)</td>
      <td>250 Flux</td>
      <td>Stat Rank V (Justice 120+)</td>
      <td>1 Unique Copy</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 22. MAW Set Synergies
        {
            "dir": "maw",
            "file": "maw-set-synergies.html",
            "title": "M.A.W. Full Set Synergies &amp; Resonance Bonuses",
            "category": "M.A.W. Arsenal",
            "cat_url": "../maw/index.html",
            "hero_img": "../assets/banners/banner_hero_maw_arsenal.svg",
            "lead": "MAW'S KEEP FORGE MASTERS",
            "code": "SYNERGY-MAW-SET",
            "clearance": "LEVEL 3 CLEARANCE",
            "content": '''
<h2>1. Resonance Synergy Mechanics</h2>
<p>Equipping a complete matching M.A.W. set (Weapon + Suit + Gift) from the same Sorrow Entity unlocks powerful passive and active Resonance Synergies, granting immunity to specific breach debuffs.</p>

<h2>2. Canonical M.A.W. Set Resonance Bonuses</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Set Name</th>
      <th>Donor Entity</th>
      <th>Full Set Synergy Effect</th>
      <th>Resonance Ability</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>The Lament Set</strong></td>
      <td><a class="wiki-link" href="../entities/se-001-the-orphaned-bell.html">SE-001 (Orphaned Bell)</a></td>
      <td>+25% Cyan Damage, Immune to Deafness</td>
      <td><strong>Chime Echo:</strong> On clash win, restore 15 SP to all agents in the same room.</td>
    </tr>
    <tr>
      <td><strong>The Mourning Set</strong></td>
      <td><a class="wiki-link" href="../entities/se-002-the-grieving-colossus.html">SE-002 (Grieving Colossus)</a></td>
      <td>+30% Max HP, +20% Crimson Resist</td>
      <td><strong>Colossus Stomp:</strong> Staggers nearby minor breached entities on stagger break.</td>
    </tr>
    <tr>
      <td><strong>The Embrace Set</strong></td>
      <td><a class="wiki-link" href="../entities/se-005-the-smothering-mother.html">SE-005 (Smothering Mother)</a></td>
      <td>+20 Attack Speed, +15% Emerald Resist</td>
      <td><strong>Silk Shroud:</strong> Binds target in threads for 4 seconds, reducing attack power by 30%.</td>
    </tr>
    <tr>
      <td><strong>The Absolute Set</strong></td>
      <td><a class="wiki-link" href="../entities/se-010-the-convergence.html">SE-010 (The Convergence)</a></td>
      <td>+40% Pale Damage, All Resistances 0.5</td>
      <td><strong>Singularity Pulse:</strong> Pulls all enemies in room toward center, dealing 50 Pale damage.</td>
    </tr>
  </tbody>
</table>
</div>
'''
        },

        # 23. The First Sovereign War
        {
            "dir": "lore",
            "file": "the-first-sovereign-war.html",
            "title": "The First Sovereign War &amp; The Fall of the Old Dreamers",
            "category": "Historical Lore",
            "cat_url": "../lore/index.html",
            "hero_img": "../assets/banners/banner_hero_somnarak_city.svg",
            "lead": "THE ARCHIVES // CYCLE 0001 - 0400",
            "code": "HIST-WAR-001",
            "clearance": "PUBLIC HISTORICAL RECORD",
            "content": '''
<h2>1. Genesis of the Conflict</h2>
<p>In the First Age of Somnarak, before the establishment of the <a class="wiki-link" href="../lore/the-cycle-and-absolvohan.html">1,778 Cycles</a>, the city was ruled by the <strong>Old Dreamers</strong> — mystics who believed Han could be dispersed into pure illusion without physical consequence.</p>

<p>When the unmanaged grief pooled into massive tectonic breaches, the <strong>Founding Corporations</strong> revolted, forging the first crude M.A.W. weapons from fallen entities and seizing control of the Central Spire in what is now known as the <strong>First Sovereign War</strong>.</p>

<h2>2. The Aftermath &amp; The Nine Veiled Edicts</h2>
<p>Following the war, the High Council and the Reverie Directorate established the strict management of Han as an energy resource, dividing Somnarak into the Veiled Districts and the Raw Outskirts.</p>
'''
        },

        # 24. Panic States and Corrosion
        {
            "dir": "mechanics",
            "file": "panic-states-and-corrosion.html",
            "title": "Psychological Degradation, Panic States &amp; M.A.W. Corrosion",
            "category": "Combat &amp; Psychology",
            "cat_url": "../mechanics/index.html",
            "hero_img": "../assets/diagrams/four_work_types_matrix.svg",
            "lead": "DIRECTORATE PSYCHOLOGICAL CORPS",
            "code": "MECH-PSYCH-04",
            "clearance": "LEVEL 2 CLEARANCE",
            "content": '''
<h2>1. Sanity Points (SP) &amp; Psychological Degradation</h2>
<p>Every agent in Facility 01 possesses a Sanity Point (SP) gauge linked to their Prudence attribute. When an agent witnesses horrific entity breaches or takes White/Black Han damage, SP drains rapidly. If SP reaches 0, the agent enters a <strong>Panic State</strong>.</p>

<h2>2. The Four Panic Behaviors</h2>
<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th>Panic Behavior</th>
      <th>Primary Stat Deficiency</th>
      <th>Agent Action</th>
      <th>Remedy Protocol</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Murderous (살인)</strong></td>
      <td>Lowest Fortitude</td>
      <td>Attacks nearest allied personnel with assigned weapon</td>
      <td>Subdue with White/Cyan SP recovery weapons</td>
    </tr>
    <tr>
      <td><strong>Wandering (방황)</strong></td>
      <td>Lowest Prudence</td>
      <td>Runs aimlessly through hallways, opening containment doors</td>
      <td>Intercept with Shadow Corps, tranquilize</td>
    </tr>
    <tr>
      <td><strong>Paralyzed (마비)</strong></td>
      <td>Lowest Temperance</td>
      <td>Freezes in place, taking 2.0x damage from all sources</td>
      <td>Deploy ally to perform psychological rally</td>
    </tr>
    <tr>
      <td><strong>Fanatic (광신)</strong></td>
      <td>Lowest Justice</td>
      <td>Bow before breached Sorrow Entity, healing the entity</td>
      <td>Execute or suppress before full corrosion</td>
    </tr>
  </tbody>
</table>
</div>

<h2>3. M.A.W. Corrosion Transformation</h2>
<p>If an agent wielding a Grade IV or V M.A.W. weapon remains in a Panic State for more than 30 seconds, the entity's consciousness fully overtakes the agent's nervous system, triggering <strong>M.A.W. Corrosion</strong>. The agent morphs into a hostile mini-boss requiring full lethal suppression.</p>
'''
        }
    ]

    # Let's generate each subpage HTML file!
    left_rail_template = '''
    <aside class="left-rail">
      <div class="site-mark">
        <a href="../index.html">
          <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak Emblem">
          <b>SOMNARAK</b>
          <span>OFFICIAL WIKI ARCHIVE</span>
        </a>
      </div>
      <nav aria-label="Wiki navigation" class="left-links">
        <section>
          <h2>DATABASE HUBS</h2>
          <a href="../index.html">Main Overview</a>
          <a href="../characters/index.html">Characters Hub</a>
          <a href="../lore/index.html">Lore &amp; Cosmology</a>
          <a href="../locations/index.html">Locations &amp; Atlas</a>
          <a href="../factions/index.html">Factions &amp; Guilds</a>
          <a href="../departments/index.html">Facility Floors</a>
          <a href="../entities/index.html">Sorrow Entities</a>
          <a href="../maw/index.html">M.A.W. Equipment</a>
          <a href="../mechanics/index.html">Systems &amp; Mechanics</a>
        </section>
        <section>
          <h2>FACILITY DIRECTIVES</h2>
          <a href="../departments/facility-room-types.html">Room Types &amp; Layout</a>
          <a href="../departments/incident-reports-archive.html">Incident Reports (001-010)</a>
          <a href="../departments/facility-meltdown-procedures.html">Facility Meltdown Codes</a>
          <a href="../departments/core-suppression-guidelines.html">Core Suppression Rules</a>
          <a href="../atlas/hand-of-change-map.html">Hand of Change Map</a>
          <a href="../atlas/somnarak-city-map.html">Somnarak City Map</a>
        </section>
      </nav>
    </aside>
'''

    for sp in subpages:
        out_dir = os.path.join(wiki_root, sp["dir"])
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, sp["file"])

        html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{sp["title"]} — Somnarak Official Wiki</title>
  <link rel="stylesheet" href="../assets/css/wiki.css">
  <link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg">
  <script defer src="../assets/js/wiki.js"></script>
</head>
<body>
  <!-- Top Utility Bar -->
  <header class="utility">
    <div class="utility-left">
      <button class="nav-open" aria-label="Open navigation" type="button">☰</button>
      <a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
      <span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
    </div>
    <nav aria-label="Main navigation">
      <a href="../index.html">Main page</a>
      <a href="../characters/index.html">Characters</a>
      <a href="../lore/index.html">Lore</a>
      <a href="../locations/index.html">Atlas</a>
      <a href="../factions/index.html">Factions</a>
      <a href="../departments/index.html">Facility</a>
      <a href="../entities/index.html">Entities</a>
      <a href="../maw/index.html">M.A.W.</a>
      <a href="../mechanics/index.html">Mechanics</a>
    </nav>
    <div class="search">
      <input id="search" data-index="../data/search.json" placeholder="Search archive..." autocomplete="off">
      <div id="results"></div>
    </div>
  </header>

  <!-- Main Grid Layout -->
  <div class="wiki-shell">
    <!-- Left Rail -->
    {left_rail_template}

    <!-- Center Main Content -->
    <main class="wiki-main" id="content">
      <!-- Breadcrumb Bar -->
      <nav class="breadcrumb-bar" aria-label="Breadcrumb">
        <a href="../index.html">Home</a>
        <span class="breadcrumb-sep">&gt;</span>
        <a href="{sp['cat_url']}">{sp['category']}</a>
        <span class="breadcrumb-sep">&gt;</span>
        <span class="breadcrumb-current">{sp['title']}</span>
      </nav>

      <!-- Article Header Showcase -->
      <header class="article-header">
        <div class="hero-frame">
          <img src="{sp['hero_img']}" alt="{sp['title']}" class="hero-banner-img">
        </div>
        <div class="header-meta-wrap">
          <div class="article-badges">
            <span class="badge badge-somna">{sp['code']}</span>
            <span class="badge badge-gold">{sp['clearance']}</span>
          </div>
          <h1 class="article-title">{sp['title']}</h1>
          <p class="article-subtitle">AUTHORITY REGISTER: {sp['lead']}</p>
        </div>
      </header>

      <!-- Table of Contents Container -->
      <nav class="wiki-toc" aria-label="Table of contents">
        <div class="toc-title">DIRECTORY OF LOGS &amp; PROTOCOLS</div>
        <ol class="toc-list">
          <li><a href="#section-1">1. Primary Operational Overview</a></li>
          <li><a href="#section-2">2. Statistical Matrix &amp; Data Analysis</a></li>
          <li><a href="#section-3">3. Tactical Transcripts &amp; Incident Protocols</a></li>
        </ol>
      </nav>

      <!-- Main Body Content -->
      <article class="article-body">
        {sp['content']}
      </article>

      <!-- Page Footer -->
      <footer class="article-footer">
        <div class="footer-categories">
          <strong>Categories:</strong>
          <a href="{sp['cat_url']}">{sp['category']}</a> |
          <a href="../index.html">Somnarak Universe</a> |
          <a href="../lore/index.html">Canon Directorate Archives</a>
        </div>
        <div class="footer-disclaimer">
          Content is available under Somnarak Directorate Archival License unless otherwise noted.
        </div>
      </footer>

      <!-- Bottom Cross-Reference Directory -->
      <section class="cross-reference-section">
        <div class="cross-ref-header">CANONICAL CROSS-LINKS &amp; ATLAS CONNECTIONS</div>
        <div class="cross-ref-grid">
          <a href="../departments/index.html" class="cross-ref-card">
            <img src="../assets/layout/hand/icons/the_hand_dr_icon_styled.svg" alt="Departments">
            <div class="cross-ref-meta"><span class="cross-ref-cat">FACILITY FLOORS</span><span class="cross-ref-title">ALL 8 FLOORS</span></div>
          </a>
          <a href="../entities/index.html" class="cross-ref-card">
            <img src="../assets/art/entities/se-001.svg" alt="Entities">
            <div class="cross-ref-meta"><span class="cross-ref-cat">SORROW ENTITIES</span><span class="cross-ref-title">ENTITY CODEX</span></div>
          </a>
          <a href="../maw/index.html" class="cross-ref-card">
            <img src="../assets/art/maw/maw-w-001-01.svg" alt="MAW">
            <div class="cross-ref-meta"><span class="cross-ref-cat">ARMAMENT</span><span class="cross-ref-title">M.A.W. ARSENAL</span></div>
          </a>
          <a href="../mechanics/index.html" class="cross-ref-card">
            <img src="../assets/diagrams/han_flux_resonance_cycle.svg" alt="Mechanics">
            <div class="cross-ref-meta"><span class="cross-ref-cat">COMBAT SYSTEMS</span><span class="cross-ref-title">SYSTEMS &amp; MECHANICS</span></div>
          </a>
        </div>
      </section>
    </main>
  </div>
</body>
</html>'''
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_content)
    
    print(f"Successfully generated {len(subpages)} rich nested subpages!")

if __name__ == "__main__":
    generate_subpages()
