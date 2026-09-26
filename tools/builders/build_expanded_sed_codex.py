#!/usr/bin/env python3
"""
tools/build_expanded_sed_codex.py
Builds the massive, encyclopedic Master Codex for The Somnarak Exploration Decree (탐사 집행국)
in SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_SOMNARAK_EXPLORATION_DECREE.md.
"""

import os
import sys

# Ensure tools directory is in sys.path
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def wrap_box(b):
    return "```text\n" + b + "\n```\n\n"

def build_sed_codex():
    sections = []

    # Title & Header
    header = """# Master Codex: The Somnarak Exploration Decree (탐사 집행국 — Tamsa Jiphaengguk)
## Frontier Reconnaissance, Subterranean Engineering & Deep Strata Doctrine
### Subterranean Wing Codex 02 — High Council Mandate 042 (Post-Consolihan Edition)

"""
    sections.append(header)

    # Master Dossier Box
    dossier_box = make_box("THE SOMNARAK EXPLORATION DECREE — MASTER DOSSIER", [
        "CORPORATE CODE     : SED-CORP-M042",
        "KOREAN AUTHORITY   : Tamsa Jiphaengguk (Exploration Executive Bureau)",
        "EXECUTIVE MANDATE  : High Council of Sighs Mandate 042",
        "OPERATIONAL DOMAIN : Negative 50 Meters to Primordial Nadir (-3,000m+)",
        "HEADQUARTERS       : The Chthonic Citadel (Zone B / Eastern Maw Rim)",
        "HIGH COMMISSIONER  : Baek Seung-Hyun (Supreme Exploration Commander)",
        "ACTIVE PERSONNEL   : 1,460 Sworn Expeditionary & Engineering Members",
        "PRIMARY SQUAD      : The Seven Vanguard Specialists (Katabagil Descent)",
        "BORE FLEET ASSETS  : 1 Dreadnought, 4 Heavy Dredgers, 12 Mole Skimmers",
        "ASSOCIATED SUITE   : SOMNARAK-WORLD/Katabagil/ (Passages 1 to 7)"
    ])
    sections.append(wrap_box(dossier_box))

    quote = """> *"The city is forty-two centuries old. We have mapped every street, numbered every building, and taxed every doorway. Yet we walk upon a hollow crust, terrified of the silence beneath our boots. The exploration of the underworld is not an ambition; it is an existential necessity. If we do not chart the sorrow gathering in the deep strata, the ground will swallow us whole."*  
> — High Commissioner Baek Seung-Hyun, Address to the Council of Sighs, Year 4,180

---

## Section I: Foundational Charter & Four-Thousand-Year History

### 1.1 Executive Summary & Foundational Purpose
The **Somnarak Exploration Decree (SED / 탐사 집행국 — Tamsa Jiphaengguk)** is the sovereign municipal expeditionary and subterranean engineering corporation of Somnarak. Established under the High Council of Sighs through **Council Mandate 042**, the SED possesses absolute jurisdictional, exploratory, and salvage authority over all subterranean territories extending beneath the municipal bedrock, beginning strictly at the negative fifty-meter (-50m) civil demarcation threshold.

While the surface footprint of Somnarak encompasses eighty-six square kilometers of paved avenues, high-density residential wards, and fortified perimeter walls, the true mass of the city extends vertically downward into thousands of meters of unmapped geological, tectonic, and metaphysical strata. Millions of citizens walk upon roads that sit precariously atop ancient catacombs, drowned pre-cataclysm wards, pressurized aquifers of liquid sorrow, and cyclopean structures predating recorded human civilization.

The SED serves as the vanguard against the darkness beneath. It is not a passive research guild or an archival library; it is an active, industrialized expeditionary force equipped with heavy subterranean drilling crawlers, pneumatic ballast stabilizers, pressurized diving suits, and acoustic resonance theodolites. Its personnel—ranging from weathered miners and structural architects to psychic weavers and elite frontier wardens—venture daily into the suffocating depths to chart shifting fault lines, secure hazardous pre-collapse technologies, and ensure that the primordial sorrow pooling in the planetary abyss does not breach the surface world.

---

### 1.2 Institutional Contrast: The Three Corporate Powers

To understand the operational doctrine of the SED, one must distinguish its mission from the other two supreme corporate entities operating within Somnarak:

| Institution | Primary Focus | Operational Domain | Key Leadership |
|---|---|---|---|
| **Reverie Directorate (R.D.)** | Static Containment & Energetic Extraction | Facility 01 (0m to -2,000m beneath Alpha Tree) | Director Majin & Secretary Seiyon |
| **Underworld Cleanup Descend (UCD)** | Urban Anti-Fray Pacification & Police Interdiction | Zones B, C, D (0m to -50m subterranean slums) | Commander Taeho & Auditor Yuna |
| **Somnarak Exploration Decree (SED)** | Sub-Strata Cartography & Abyssal Frontier Descents | Planetary Bedrock (-50m to Primordial Nadir) | High Commissioner & Vanguard Specialists |

---

## Section II: The Six Operational Divisions

The Somnarak Exploration Decree executes its municipal mandate through six specialized divisions:

### 1. Division I: Cartography & Topology (지형 측량국)
- **Role:** Deep acoustic cartography, tectonic fault tracking, and three-dimensional holographic mapping.
- **Equipment:** Resonant acoustic theodolites, quantum gravity gradient meters, and seismic transceivers.
- **Head:** Lead Cartographer Yeonhwa (연화).

### 2. Division II: Engineering & Bore Fleet (천공 함대국)
- **Role:** Construction, operation, and maintenance of the subterranean crawler fleet, pneumatic drilling rigs, and structural ballast shoring.
- **Equipment:** Diamond-tipped rotary cutters, hydraulic arch supports, and high-pressure steam boilers.
- **Head:** Master Mason Doha (도하).

### 3. Division III: Relic Recovery & Archaeology (유물 회수국)
- **Role:** Excavation, preservation, and cataloging of pre-Calamity technologies, architectural fragments, and ancient municipal archives.
- **Equipment:** Hermetic stasis caskets, ultrasonic cleaning vats, and forensic carbon spectrometers.
- **Head:** Senior Archivist Minjae (민재).

### 4. Division IV: Chthonic Containment & Safety (심층 방호국)
- **Role:** Vanguard defense against feral subterranean entities, tunnel collapse shoring, and hazardous gas mitigation.
- **Equipment:** Class III Heavy M.A.W. Kinetic Bulwarks, pressurized hyperbaric suits, and chemical scrubbers.
- **Head:** Sentinel Commander Harin (하린).

### 5. Division V: Vanguard Scouts & Special Operations (선봉 수색국)
- **Role:** Point-reconnaissance into unmapped strata, first-contact protocols, and high-risk extraction sorties.
- **Equipment:** High-speed Mole-class skimmers, acoustic cloaking cowls, and diamond grappling lines.
- **Head:** Scout Leader Sora the Dreamer (소라).

### 6. Division VI: Subterranean Intelligence & Sonar Logistics (음향 정보국)
- **Role:** Fleet-wide communication relay management, life-support ballast auditing, and inter-agency treaty enforcement.
- **Equipment:** Deep-earth optical transceivers, acoustic decryptors, and actuarial ledger matrices.
- **Head:** Chief Auditor Jisoo (지수).

---

## Section III: Headquarters Architecture — The Chthonic Citadel

"""
    sections.append(quote)

    citadel_box = make_box("THE CHTHONIC CITADEL STRUCTURAL PROFILE (ZONE B RIM)", [
        "LOCATION            : Zone B Maw Rim (Tectonic Fault Ingress)",
        "VERTICAL ELEVATION  : Surface (+150m Spire) to Deep Vaults (-1,200m)",
        "STRUCTURAL SKELETON : Reinforced Ferro-Concrete & Vitrified Basalt",
        "POPULATION CAPACITY : 2,400 Expedition Personnel & Engineering Staff",
        "---------------------------------------------------------------------",
        "TIER 01 (+150m to 0m) : The Zenith Needle & Atmospheric Sonar Spire",
        "TIER 02 (0m to -200m) : Central Administrative Hub & Dry Docks",
        "TIER 03 (-200m to -600m): Heavy Machine Shops & Pressure Simulators",
        "TIER 04 (-600m to -1,200m): Base Camp Alpha (The Abyssal Overlook)"
    ])
    sections.append(wrap_box(citadel_box))

    citadel_text = """### 3.1 The Zenith Needle & Sonar Spire (+150m to 0m)
Rising one hundred and fifty meters above the rim of the Eastern Maw, the Zenith Needle serves as the communications and early-warning hub of the SED:
- **The Grand Cartography Planetarium:** A thirty-meter hemispherical projection dome displaying a real-time three-dimensional holographic model of Somnarak's subterranean crust. Shifting fault lines, sorrow flow currents, and active crawler locations are tracked with pinpoint precision.
- **High Council Liaison Chambers:** The diplomatic offices where High Commissioner Baek Seung-Hyun meets with municipal delegates and corporate ambassadors to negotiate resource allocations.

### 3.2 Level -200m: The Heavy Sub-Docks & Engineering Dry Docks
Directly beneath the Maw rim lies the staging area for the Bore Fleet:
- **Crawler Departure Gantries:** Massive hydraulic berths where heavy chthonic dredgers undergo engine overhauls, drill bit replacements, and armor refits.
- **The Ballast Vaults:** Enormous holding tanks storing millions of metric tons of liquefied lead-water ballast used to counterbalance shifting tectonic pressures during deep drilling operations.

### 3.3 Level -1,200m: Base Camp Alpha (The Abyssal Overlook)
Anchored into the volcanic basalt cliff face overlooking the abyss, Base Camp Alpha is the final permanent outpost of human civilization before the unknown:
- **The Abyssal Overlook:** A heavily fortified bunker featuring five-meter-thick lead-crystal observation viewports looking out over the cyclopean chasm of the Weeping's lower aquifers.
- **Frontier Garrison Barracks:** Self-contained living quarters, hydroponic meal stations, and medical trauma bays housing sixty sworn vanguard wardens who maintain the perimeter against entity breaches.
- **The Bore Launch Apron:** The departure platform where exploration crawlers decouple their umbilical cables and descend into the virgin darkness of the unmapped depths.

---

## Section IV: Employee Hierarchy, Ranks & Workforce Census

The rank structure of the Somnarak Exploration Decree reflects its dual nature as an industrialized scientific institution and an expeditionary military force:

| Rank Grade | Korean Title | Minimum Tenure | Core Responsibilities | Attribute Minimums |
|---|---|---|---|---|
| **Rank 1: Surface Apprentice** | 지상 수습원 | Induction | Surface logistics, tool maintenance, sonar data entry | Resilience 25+, Agility 20+ |
| **Rank 2: Field Scout** | 현장 수색원 | 2 Years | Strata 1–2 drilling, acoustic markers, basic vehicle repairs | Resilience 40+, Agility 35+ |
| **Rank 3: Senior Cartographer** | 선임 측량사 | 5 Years | Strata 3–4 sonar interpretation, squad defense, abort authority | Resilience 55+, Instinct 50+ |
| **Rank 4: Bore Captain** | 천공 함장 | 10 Years | Heavy crawler command, deep multi-week sorties, combat clearance | Resilience 70+, Fortitude 65+ |
| **Rank 5: Expedition Marshal** | 원정 제독 | 15 Years | Sector fleet command, Base Camp Alpha direction, inter-agency policy| Resilience 85+, Wisdom 75+ |
| **Executive: High Commissioner**| 탐사 총감 | Council Seat | Corporate supreme leadership, Council Mandate 042 enforcement | Executive Council Mandate |

---

## Section V: The Bore Fleet & Field Technology

"""
    sections.append(citadel_text)

    fleet_box = make_box("THE SED BORE FLEET CANONICAL ASSET REGISTRY", [
        "FLAGSHIP: 'THE CHTHONIC DREADNOUGHT' (CLASS V HEAVY BORE CRUISER)",
        "- Length: 94.0m | Mass: 8,200 Tons | Main Drill: 12m Diamond Rotary Head",
        "- Crew: 45 Specialists | Power: Geothermal High-Pressure Steam Reactor",
        "---------------------------------------------------------------------",
        "HEAVY MINER: 'BORE-VII GOLEM' (CLASS IV INDUSTRIAL DREDGER)",
        "- Length: 48.0m | Mass: 3,400 Tons | Role: Shaft Excavation & Ballast",
        "- Crew: 18 Engineers | Armament: Dual Pneumatic Rock-Splitters",
        "---------------------------------------------------------------------",
        "RECONNAISSANCE: 'MOLE-IV SKIMMER' (CLASS II RAPID SCOUT RIG)",
        "- Length: 12.5m | Mass: 42 Tons | Velocity: 65 km/h across cavern rock",
        "- Crew: 3 Scouts | Role: Point mapping, acoustic sensor deployment",
        "---------------------------------------------------------------------",
        "RESEARCH TENDER: 'SONAR-I ECHO' (CLASS III ACOUSTIC LAB TENDER)",
        "- Length: 36.0m | Mass: 1,800 Tons | Role: Real-time seismic analysis"
    ])
    sections.append(wrap_box(fleet_box))

    fleet_text = """### 5.1 The Chthonic Dreadnought (지하 전함 — Jiha Jeonham)
The flagship of the SED Bore Fleet is a marvel of subterranean engineering:
- **The Diamond Rotary Head:** A twelve-meter-diameter rotating cutter face composed of four hundred interlocking diamond-matrix carbide teeth. Capable of grinding solid granite and basalt into fine gravel at a rate of fifteen linear meters per hour.
- **Continuous Shoring Injector:** As the drill advances, automated trailing arms spray quick-curing hydraulic silicate foam along the tunnel walls, instantly creating a reinforced casing capable of withstanding two thousand atmospheres of tectonic pressure.
- **Internal Atmospheric Scrubbers:** Closed-loop oxygen recyclers and carbon scrubbers allow the vessel to operate submerged in toxic sorrow aquifers or vacuum pockets for up to six consecutive months.

---

## Section VI: Sub-Strata Topography (The Seven Geological Layers)

The underworld of Somnarak is categorized into seven distinct geological and metaphysical strata, each presenting unique structural, chemical, and psychic hazards:
"""
    sections.append(fleet_text)

    strata_box = make_box("THE SEVEN SUBTERRANEAN STRATA OF SOMNARAK", [
        "STRATA 1: THE DROWNED NECROPOLIS (CRYPTASU / 0m to -150m)",
        "- Composition: Ferro-concrete ruins, flooded subway vaults, black silt.",
        "- Primary Hazard: Supercritical sorrow brine aquifers, rusted rebar.",
        "---------------------------------------------------------------------",
        "STRATA 2: THE CALCIFIED BASTIONS (PETROBYEOK / -150m to -450m)",
        "- Composition: Pre-Calamity adamantine foundations, calcified basalt.",
        "- Primary Hazard: Instantaneous petrifying vapors, structural collapse.",
        "---------------------------------------------------------------------",
        "STRATA 3: THE SEVERED ARTERIES (FURTUGIL / -450m to -900m)",
        "- Composition: Tectonic fault corridors, abandoned smuggling flumes.",
        "- Primary Hazard: Rogue Fray weapon caches, unstable gravity pockets.",
        "---------------------------------------------------------------------",
        "STRATA 4: THE ECHO-ROOT GARDENS (RADIKKUM / -900m to -1,500m)",
        "- Composition: Petrified roots of Alpha Tree, bioluminescent fungal forests.",
        "- Primary Hazard: Spore-induced cognitive hallucinations, psychic drift.",
        "---------------------------------------------------------------------",
        "STRATA 5: THE PERIMETER FOOTINGS (LIMESTEUM / -1,500m to -2,100m)",
        "- Composition: Vitrified outside Han-stone, pressurized tectonic plates.",
        "- Primary Hazard: Outside Sorrow seepage, extreme thermal heat vents.",
        "---------------------------------------------------------------------",
        "STRATA 6: THE OCCLUSIHAN RIFT (TRAUMAGOL / -2,100m to -2,800m)",
        "- Composition: Non-reflective black obsidian glass, non-Euclidean voids.",
        "- Primary Hazard: Acoustic erasure, spatial dislocation, Scar Walkers.",
        "---------------------------------------------------------------------",
        "STRATA 7: THE PRIMORDIAL WELLSPRING (FONTISAEM / -2,800m to Nadir)",
        "- Composition: Liquid Mugenhan crystal core, pure uncompressed sorrow.",
        "- Primary Hazard: Absolute psychic dissolution, ontological reality collapse."
    ])
    sections.append(wrap_box(strata_box))

    specialists_intro = """---

## Section VII: The Core Vanguard Specialists (Complete Personnel Profiles)

The vanguard of the SED consists of seven sworn specialists who spearhead the historic **Katabagil Descent**:

### 7.1 Cartographer Yeonhwa (연화 / 蓮花)
- **Specialization:** Acoustic Sonic Cartography & Vanguard Direction.
- **Combat Style:** Wields the **Theodolite Sonar Stave**, scanning enemy armor seams and broadcasting targeting telemetry to allies across Range Bands 3 and 4.
- **Key Passive:** `[Acoustic Mapping]` — Allies attacking target nodes designated by Yeonhwa gain +25% Stagger Damage.

### 7.2 Master Mason Doha (도하 / 渡河)
- **Specialization:** Subterranean Architecture & Sapper Demolitions.
- **Combat Style:** Wields the **Hydraulic Tectonic Wedge**, cracking subterranean bedrock to expose enemy modular appendages and destabilize footing.
- **Key Passive:** `[Structural Fracture]` — Doha's attacks ignore 30% of target physical protection.

### 7.3 Sentinel Commander Harin (하린 / 霞璘)
- **Specialization:** Heavy Kinetic Bulwark & Phalanx Defense.
- **Combat Style:** Wields the **Adamantine Tower Shield *Bulwark-IV***, intercepting incoming melee and artillery strikes directed at backline specialists.
- **Key Passive:** `[Iron Sentry]` — Absorbs 100% of single-target damage directed at adjacent allies in Range Band 1.

### 7.4 Dreamer Sora (소라 / 昭羅)
- **Specialization:** Psychic Weaver & Mnemonic Sanity Repose.
- **Combat Style:** Wields the **528 Hz Resonant Damping Cowl**, emitting harmonic soundwaves that restore operative Composure and quench feral entity rage.
- **Key Passive:** `[Acoustic Repose]` — Winning a clash restores +15 Composure (SP) to the entire squad.

### 7.5 Senior Archivist Minjae (민재 / 珉載)
- **Specialization:** Forensic Epigraphy & Relic Decryption.
- **Combat Style:** Wields the **Crystalline Lancets**, slicing through metaphysical sorrow barriers with precision strikes targeting historical emotional trauma.
- **Key Passive:** `[Historical Record]` — Crits inflict permanent -2 Clash Power on the target.

### 7.6 Chief Actuary Jisoo (지수 / 智秀)
- **Specialization:** Cryogenic Ballast & Life-Support Management.
- **Combat Style:** Wields the **Pneumatic Cryo-Harpoon**, firing liquid-nitrogen-tipped cables that freeze enemy limbs and anchor massive behemoths in place.
- **Key Passive:** `[Cryo Lock]` — Hits inflict 2 turns of immobilized status on enemy appendages.

### 7.7 High Commissioner Baek Seung-Hyun (백승현 / 白承鉉)
- **Specialization:** Supreme Tactical Command & Sovereign Authority.
- **Combat Style:** Wields the **Chthonic Command Saber**, directing multi-target kinetic bombardments and coordinating flawless team clashes.
- **Key Passive:** `[Council Mandate]` — Squad-wide Speed increased by +2; immune to first panic check.

---

## Section VIII: Subterranean Survival Physics & Abyssal Combat Engine

"""
    sections.append(specialists_intro)

    grid_box = make_box("SED UNIVERSAL 10-NODE VERTICAL ABYSS COMBAT GRID", [
        "[STAGE NODES 01 TO 10 — UPPER RIG INGRESS TO PRIMORDIAL CORE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]    ",
        "|--BOREHOLE RIG-| |--FLOODED LEDGE-| |--CENTRAL DAIS---| |--CORE RELIC-|",
        "---------------------------------------------------------------------",
        "- Node 01: Borehole Rig Staging ('The Iron Mole' Anchor / Heavy Lift)",
        "- Node 02-03: Bedrock Causeways & Trenches (Harin & Doha Vanguard)",
        "- Node 04: Sluice Conduits & Spore Clearings (Sora Mnemonic Repose)",
        "- Node 05: Central Altar / Strata Dais (Apex Boss Sovereign Core)",
        "- Node 06-07: High Spire Catwalks & Arches (Yeonhwa Sonar / Minjae Scribe)",
        "- Node 08: Forensic Balconies & Ballast Gauges (Jisoo Cryo Harpoon)",
        "- Node 09: Sub-Dais Abyssal Chasm (Tectonic Pressure Buffer)",
        "- Node 10: Strata Descent Sluice / Sovereign Reliquary (The Silent One)",
        "---------------------------------------------------------------------",
        "RANGE BANDS (1 TO 5):",
        "- Band 1 (Nodes 01-02): Heavy Tower Shields, Pneumatic Rams, Cleavers",
        "- Band 2 (Nodes 03-04): Sapper Drills, Incendiary Wedges, Shock Pikes",
        "- Band 3 (Nodes 05-06): Sonar Theodolites, Silver Cowls, Carbines",
        "- Band 4 (Nodes 07-08): Forensic Scribe Tablets, Archaeological Lancets",
        "- Band 5 (Nodes 09-10): Hydraulic Winches, Cryo Harpoons, Anchor Cables"
    ])
    sections.append(wrap_box(grid_box))

    four_p_box = make_box("THE FOUR P-FRAMEWORK IN ABYSSAL EXPEDITIONS", [
        "P1: PASSIVES (MOMENTUM SURGE & SONAR TARGET LOCK)",
        "- Momentum Surge: Winning clashes awards +2 Speed on the next turn.",
        "- Sonar Target Lock: Yeonhwa tags part seams, giving +25% Stagger Dmg.",
        "- Adamantine Bastion: Harin's armor ignores light stagger pushback.",
        "---------------------------------------------------------------------",
        "P2: PANIC / COMPOSURE (DEPTH CLAUSTROPHOBIA & SANITY ANCHORS)",
        "- Composure Gauge (0-50 SP): Measures sanity against depth terror.",
        "- Depth Claustrophobia (< 15 SP): Operative suffers panic, -2 Clash.",
        "- Harmonic Repose: Sora's 528 Hz cowl restores +15 SP squad-wide.",
        "---------------------------------------------------------------------",
        "P3: PARRY / PROTECTION (KINETIC BULWARK & HARMONIC REPOSE)",
        "- Bastion Kinetic Lock: Harin reflects physical impact back as tremor.",
        "- Sapper Counter-Lever: Doha absorbs kinetic force to pop armor seams.",
        "- Leaded Damping Dome: Sora vacuum sphere captures rogue sorrow waves.",
        "---------------------------------------------------------------------",
        "P4: POSTURE / POISE (MODULAR STAGGER & TERMINAL PACIFICATION)",
        "- Modular Part Posture: Boss weapons/cores possess discrete pools.",
        "- Stagger 1 Proc (60% Strain): Destroys modular weapon components.",
        "- Stagger 2 Proc (0% Collapse): Terminal Stagger; communion pacification."
    ])
    sections.append(wrap_box(four_p_box))

    combat_text = """### 8.1 Tactical Decibel Sonar Management
Operating kilometers beneath the bedrock requires strict acoustic discipline:
- **The Decibel Threshold (90 dB):** High-impact kinetic detonations exceeding ninety decibels risk triggering secondary cavern collapses or alerting dormant abyssal swarms.
- **Acoustic Damping Fields:** Dreamer Sora and Cartographer Yeonhwa deploy acoustic null-fields to muffle heavy drill impacts, keeping combat noise below seventy decibels during tactical engagements.

### 8.2 Dual-Threshold Stagger Engine in Strata Warfare
- **Tier 1 Stagger (60% Posture Strain / Modular Part Dismantling):** Targeting primary entity appendages (e.g., Siphon Arms, Adamantine Claws, Magma Cleavers) breaks that part's posture. When it hits 60% strain, the part fractures, cancelling channeled special attacks and increasing incoming damage to that zone by +50% for 1 turn.
- **Tier 2 Stagger (0% Posture Collapse / Terminal Pacification):** When the central core posture collapses to 0/0, the entity enters complete catatonia, enabling peaceful communion, engram extraction, or lethal execution.

---

### 8.3 Canonical Turn-Based Expedition Demonstration: The Drowned Gatekeeper (Passage 1)
Below is the turn-by-turn operational battle log demonstrating the 10-node vertical abyss combat engine during the Vanguard's descent into Strata 1 against the SECC Rank IV Entity *The Drowned Municipal Gatekeeper*.

"""
    sections.append(combat_text)

    turn1_hud = make_box("TURN 01 SPATIAL HUD — THE SUBWAY INGRESS (STRATA 1)", [
        "[STAGE NODES 01 TO 10 — FLOODED SUBWAY INGRESS (-120M)]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]    ",
        "[RIG-01] [HARIN]  [DOHA]   [SORA]   [GATEKP] [YEONH]  [JISOO]  [CHASM]       [CORE]  ",
        "---------------------------------------------------------------------",
        "- Node 02: Sentinel Harin (Speed 6 -> 3 AP | HP 3,800/3,800 | SP 50/50)",
        "- Node 03: Master Mason Doha (Speed 7 -> 4 AP | HP 3,400/3,400 | SP 50/50)",
        "- Node 05: The Drowned Gatekeeper (Speed 5 -> 3 AP | HP 6,400/6,400 | Posture 400/400)",
        "  * Corroded Rail Scepter: 1,500/1,500 HP | Posture 250/250 [Target Lock N02]",
        "  * Submerged Turnstile Shield: 1,800/1,800 HP | Posture 300/300 [Active Guard]",
        "  * Drowned Municipal Core: 3,100/3,100 HP | Posture 400/400 [Immune]"
    ])
    sections.append(wrap_box(turn1_hud))

    turn1_log = """###### Turn 01 Action Resolution Log:
- **Phase Step 1 (Passives & AP Allocation):**
  * Harin rolls Speed 6 (3 AP). Doha rolls Speed 7 (4 AP).
  * Gatekeeper rolls Speed 5 (3 AP). Ambient flooded brine inflicts 1 AP movement penalty without Diving Boots.
- **Phase Step 2 (Spatial Maneuvers & Targeting):**
  * Harin plants the Bulwark at Node 02, locking defensive stance.
  * Gatekeeper plays `[Crushing Rail Swing]` targeting Node 02 (Band 1-2 Cleave, Power 15-20, Weight).
- **Phase Step 3 (Clash Resolution):**
  * Harin plays `[Kinetic Lock Bulwark]` (Power 17-22).
  * Clash Roll: Harin 19 vs Gatekeeper 16. **Clash Won!**
  * The massive corroded rail scepter clangs harmlessly against Harin's adamantine shield, reflecting 65 Posture Strain back onto the weapon!
- **Phase Step 4 (Turn-End Status):**
  * Rail Scepter Posture: 185/250. Harin SP: 50/50.

"""
    sections.append(turn1_log)

    turn3_hud = make_box("TURN 03 SPATIAL HUD — RAIL SCEPTER SHATTERS (STRATA 1)", [
        "[STAGE NODES 01 TO 10 — FLOODED SUBWAY PLATFORM]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]    ",
        "[RIG-01]          [HARIN]  [DOHA]   [GATEKP] [YEONH]  [JISOO]  [CHASM]       [CORE]  ",
        "---------------------------------------------------------------------",
        "- Node 03: Harin (Speed 7 -> 4 AP | HP 3,750/3,800 | SP 48/50)",
        "- Node 04: Doha (Speed 8 -> 4 AP | HP 3,380/3,400 | SP 50/50)",
        "- Node 05: The Drowned Gatekeeper (Speed 4 -> 2 AP | HP 5,100/6,400 | Posture 260/400)",
        "  * Corroded Rail Scepter: 520/1,500 HP | Posture 90/250 [CRITICAL FRACTURE]",
        "  * Submerged Turnstile Shield: 1,600/1,800 HP | Posture 260/300",
        "  * Drowned Municipal Core: 2,980/3,100 HP | Posture 400/400"
    ])
    sections.append(wrap_box(turn3_hud))

    turn3_log = """###### Turn 03 Action Resolution Log:
- **Phase Step 1 (Clash & Sapper Strike):**
  * Doha commits 3 AP to play `[Hydraulic Tectonic Wedge]` targeting the fractured Rail Scepter.
  * Attack connects with 260 kinetic impact!
  * **TIER 1 STAGGER PROC!** The Rail Scepter drops to 90/250 Posture (< 60% threshold).
- **Phase Step 2 (Part Dismantling Effects):**
  * The rusted steel rail snaps in half, splashing into the flooded silt!
  * Gatekeeper's channeled skill `[Subway Deluge]` is instantly cancelled!
  * Gatekeeper enters Tier 1 Stagger; incoming damage amplified by +50% for 1 turn.

"""
    sections.append(turn3_log)

    turn6_hud = make_box("TURN 06 SPATIAL HUD — CORE PACIFICATION (STRATA 1)", [
        "[STAGE NODES 01 TO 10 — SUBTERRANEAN STATION VAULT]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]    ",
        "[RIG-01]                   [HARIN]  [GATEKP] [DOHA]   [SORA]   [CHASM]       [CORE]  ",
        "---------------------------------------------------------------------",
        "- Node 04: Harin (Speed 8 -> 4 AP | HP 3,750/3,800 | SP 50/50)",
        "- Node 05: The Drowned Gatekeeper (Speed 0 -> 0 AP | HP 340/6,400 | Posture 0/400)",
        "  * Corroded Rail Scepter: DESTROYED (0 HP / 0 Posture)",
        "  * Submerged Turnstile Shield: CRACKED (0 HP / 0 Posture)",
        "  * Drowned Municipal Core: 340/3,100 HP | Posture 0/400 [TERMINAL STAGGER]"
    ])
    sections.append(wrap_box(turn6_hud))

    turn6_log = """###### Turn 06 Action Resolution Log (Terminal Pacification Achieved):
- **Step 1 (Terminal Collapse):**
  * Gatekeeper Core Posture collapses to **0/400 [TERMINAL STAGGER]**.
- **Step 2 (The Acoustic Communion):**
  * Dreamer Sora steps forward to Node 05, placing her silver damping cowl over the Gatekeeper's weeping mask.
  * She speaks the Year Zero municipal transit authorization: *"Ticket validated, Stationmaster. The train has departed. You may close the gates."*
  * The entity sighs softly; its brine dissolves into clear, harmless mineral water.
- **Step 3 (Operational Extraction & Sluice Opened):**
  * Minjae extracts the **Year Zero Municipal Transit Ledger** (Grade Beta Relic).
  * At the rear of the station, the floodgates open, exposing the dry descent shaft to **Strata 2: Petrobyeok**.

---

## Section IX: Operational Context: The Katabagil Descent

The complete operational execution of the Katabagil descent is chronicled in the dedicated narrative suite:

| Katabagil Arc | Subterranean Target Domain | Geological Stratum | Strategic Exploration Objective | Companion File Reference |
|---|---|---|---|---|
| **Arc 1: Cryptasu** | Drowned Pre-Cataclysm City | Strata 1 (-120m) | Recover Year Zero municipal diaries & breach gate | `Passage_1_Cryptasu.md` |
| **Arc 2: Petrobyeok** | Calcified Bastion Wall | Strata 2 (-380m) | Breach Doha's ancient wall & evaluate survivors | `Passage_2_Petrobyeok.md` |
| **Arc 3: Furtugil** | Smuggler Conduits & Faults | Strata 3 (-650m) | Reclaim severed arteries & clear Fray transit | `Passage_3_Furtugil.md` |
| **Arc 4: Radikkum** | Deep Roots of Echo Gardens | Strata 4 (-950m) | Map Dream Realm seepage & pacify floral entity | `Passage_4_Radikkum.md` |
| **Arc 5: Limesteum** | Sub-Bulwark Perimeter Footing| Strata 5 (-1,400m)| Shore outer perimeter & seal Outside Sorrow seep | `Passage_5_Limesteum.md` |
| **Arc 6: Traumagol** | Occlusihan Rift Open Fracture | Strata 6 (-1,900m)| Traverse obsidian rift & defeat Scar Walker | `Passage_6_Traumagol.md` |
| **Arc 7: Fontisaem** | Primordial Wellspring of Han | Strata 7 (-2,300m)| Reach planetary nadir & discover Mugenhan truth | `Passage_7_Fontisaem.md` |

- **Suite Directory:** `SOMNARAK-WORLD/Katabagil/`
- **Field Guidebook:** `SOMNARAK-WORLD/Katabagil/KATABAGIL_OVERVIEW.md`

---

## Section X: Inter-Corporate Treaties & Demarcation Protocols

"""
    sections.append(turn6_log)

    treaties_box = make_box("SED INTER-CORPORATE TREATY MATRIX", [
        "TREATY 01: THE -50 METER DEMARCATION ACCORD (WITH UCD)",
        "- Jurisdictional boundary at exactly -50m depth beneath street grid.",
        "- Hot pursuit transfers to SED; joint sweeps authorized under Protocol 09.",
        "---------------------------------------------------------------------",
        "TREATY 02: THE RAW ENTITY CUSTODY TREATY (WITH REVERIE DIRECTORATE)",
        "- Mandatory 24-hour transfer of captured entities to R.D. Floor 2.",
        "- R.D. reimburses SED with Class III MAW defensive suits & power cells.",
        "---------------------------------------------------------------------",
        "TREATY 03: THE ACOUSTIC TOPOLOGY ACCORD (WITH R.D. FLOOR 4 / AYSHUK)",
        "- Real-time optical sonar telemetry feeds directly into Insight Forge.",
        "- Floor 4 provides predictive early warning for deep sorrow tides.",
        "---------------------------------------------------------------------",
        "TREATY 04: THE PLANETARY HORIZON COMPACT (WITH HORIZON CARAVAN)",
        "- Joint salvage protocols where deep sinkholes breach the Desolate.",
        "- Sovereign boundary recognized; subterranean guidance beacons shared."
    ])
    sections.append(wrap_box(treaties_box))

    catastrophes_intro = """---

## Section XI: The Three Great Subterranean Catastrophes (Historical Disaster Logs)

"""
    sections.append(catastrophes_intro)

    disaster_box = make_box("THE THREE GREAT HISTORICAL DISASTERS OF THE SED", [
        "DISASTER 01 (YEAR 2,412) : THE DROWNED DRILL (EXPEDITION 17)",
        "- Location: -420m (Karst Aquifer) | Catalyst: Supercritical sorrow brine.",
        "- Casualties: 14 Crew drowned; Ultrasonic pre-drilling mandated.",
        "---------------------------------------------------------------------",
        "DISASTER 02 (YEAR 3,105) : THE CALCIFIED BRIGADE (EXPEDITION 44)",
        "- Location: -750m (Severed Arteries) | Catalyst: Petrifying vapor vent.",
        "- Casualties: 80 Miners petrified; Hall of Silent Watchers created.",
        "---------------------------------------------------------------------",
        "DISASTER 03 (YEAR 3,988) : THE ABYSSAL SILENCE (EXPEDITION 89)",
        "- Location: -1,800m (Occlusihan Rift) | Catalyst: Cyclopean glass ruin.",
        "- Casualties: Crawler 'Endeavor-IV' lost; Level 5 Rift clearance enacted."
    ])
    sections.append(wrap_box(disaster_box))

    disaster_detail = """### 11.1 The Drowned Drill of Expedition 17 (Year 2,412)
While attempting to bore a primary drainage aqueduct beneath the Old Lament at a depth of negative four hundred and twenty meters, the steam crawler *Bore-V* punctured a pressurized subterranean aquifer containing supercritical liquid sorrow. Within ninety seconds, millions of liters of freezing, corrosive brine surged through the drill head under eighty atmospheres of pressure.
- The liquid completely dissolved the crawler's reinforced copper seals and instantly drowned all fourteen crew members.
- The hyper-saturated emotional resonance of their sudden death bonded with the surrounding limestone caverns, creating a permanent acoustic anomaly known today as the Resonant Echo Sump.
- Ever since this disaster, SED doctrine mandates the use of ultrasonic pre-drilling sonic probes before any rotary drill bit penetrates unmapped rock faces.

### 11.2 The Calcified Brigade of Expedition 44 (Year 3,105)
During a major stabilization operation in the Severed Artery Network at negative seven hundred and fifty meters, an eighty-man engineering battalion deployed to erect seismic support pillars encountered a sudden tectonic outgassing of high-density petrifying vapor. The vapor, a rare gaseous manifestation of calcified Grudge and Weight, interacted violently with the moisture in the miners' respirators and skin.
- Within less than three minutes, the entire battalion underwent instantaneous biological petrification. Their organic tissue was converted into solid basalt while retaining their exact physical forms, postures, and facial expressions of shock.
- Today, the sector remains preserved as the Hall of the Silent Watchers, where the eighty stone statues of the miners still serve as structural load-bearing pillars supporting the cavern ceiling.

### 11.3 The Abyssal Silence of Expedition 89 (Year 3,988)
Expedition 89 represents the deepest reconnaissance sortie ever attempted by a conventional SED exploration fleet. Operating the experimental heavy chthonic crawler *Endeavor-IV*, an elite twelve-member team commanded by Captain Jin Min-Gyu successfully crossed the negative eighteen hundred-meter barrier into the upper reaches of the Occlusihan Rift.
- For twelve days, the expedition transmitted continuous acoustic and barometric telemetry back to headquarters, documenting vast cyclopean megaliths constructed from non-reflective black glass that displayed no architectural resemblance to any human civilization.
- On the thirteenth day at 03:42 hours, the crawler's audio transceiver broadcast a single, unhurried transmission from Captain Jin: *"The stone is breathing, and it knows our names."*
- Immediately following this sentence, all seismic, thermal, and radio telemetry flatlined simultaneously. A rescue operation launched six days later discovered the borehole intact, but found no trace of the crawler, its crew, or their equipment. To this day, Expedition 89 is classified as an Active Hazard Zone, and entry into the Rift requires Level 5 Executive clearance.

---

## Section XII: Chronological Timeline & The Nadir Horizon (Year 0001 to 4,247)

"""
    sections.append(disaster_detail)

    timeline_box = make_box("THE SOMNARAK EXPLORATION DECREE CHRONOLOGY", [
        "YEAR 0001   : Consolihan founded; early miners chart -50m bedrock.",
        "YEAR 1,840  : High Council Mandate 042 formalizes the SED as sovereign arm.",
        "YEAR 2,412  : Disaster 01 (The Drowned Drill); ultrasonic probes invented.",
        "YEAR 3,105  : Disaster 02 (The Calcified Brigade); Hall of Watchers sealed.",
        "YEAR 3,988  : Disaster 03 (The Abyssal Silence); Rift clearance enacted.",
        "YEAR 4,180  : Baek Seung-Hyun appointed High Commissioner of Exploration.",
        "YEAR 4,232  : Absolvohan activates; tectonic sorrow pressure drops 15%.",
        "YEAR 4,233  : The Katabagil Descent executed; Seven Passages completed.",
        "YEAR 4,247  : Dawn Initiative reaches 45% Transmutation; Nadir charted."
    ])
    sections.append(wrap_box(timeline_box))

    epilogue = """### 12.1 The Primordial Wellspring & Future Mandate
The completion of the Katabagil Descent by the Seven Vanguard Specialists proved that the abyss beneath Somnarak is not an infinite pit of despair, but a traversable frontier of human courage:
- **Tectonic Stabilization:** By anchoring geothermal release valves in Strata 5 and 6, the SED reduced catastrophic municipal earthquakes by eighty percent, safeguarding the city's surface spires for generations to come.
- **The Fontisaem Wellspring:** At -2,800 meters, the discovery of the true wellspring of Mugenhan revealed that the planet's weeping is not a curse of destruction, but an unexpressed cry for communion. As the Dawn Initiative continues, the SED prepares for its next era: transforming subterranean boreholes into permanent geothermal highways of light.

> *"We were sent into the dark to die. We remained in the dark to build. And when humanity is ready to look beneath its feet without fear, they will find that we have already lit the path."*  
> — High Commissioner Baek Seung-Hyun, Address to the Bore Fleet, Base Camp Alpha

---

*Master Codex Authorization: High Commissioner Baek Seung-Hyun, Board of Survey, The Chthonic Citadel (Level -200m). Classified under High Council Mandate 042.*
"""
    sections.append(epilogue)

    return "".join(sections)

def main():
    dest_path = "SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_SOMNARAK_EXPLORATION_DECREE.md"
    content = build_sed_codex()
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {dest_path} successfully ({len(content.splitlines())} lines)!")

if __name__ == "__main__":
    main()
