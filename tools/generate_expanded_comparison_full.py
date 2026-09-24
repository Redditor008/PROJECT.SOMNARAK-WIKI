#!/usr/bin/env python3
"""
tools/generate_expanded_comparison_full.py
Generates the comprehensive, story-ready COMPLETE SYSTEM COMPARISON: SOMNARAK vs. Lobotomy Corporation.
Enriches narrative vocabulary, worldbuilding, and comparative systems while strictly maintaining
74-column text box formatting, Korean two-space buffers, zero raw HTML, and zero LaTeX dollar signs.
"""

import sys
import re

sys.path.insert(0, ".")
from tools.box_formatter import make_box

def create_box(title, rows, width=74):
    box = make_box(title, rows, width=width)
    for line in box.split("\n"):
        assert len(line) == width, f"Box line length error ({len(line)} != {width}):\n{line}"
    return f"```text\n{box}\n```\n"

header_box = create_box("COMPLETE SYSTEM COMPARISON // EXPANDED STORY EDITION", [
    "DOCUMENT: COMPLETE SYSTEM COMPARISON - SOMNARAK VS LOBOTOMY CORP",
    "EDITION : EXPANDED STORY & NARRATIVE LEXICON // CANONICAL AUDIT",
    "PURPOSE : COMPREHENSIVE 1-TO-1 MECHANICS, WORLD & STORY TRANSLATION",
    "---",
    "ROADMAP : 1,778 CYCLES // 5 WORKSHOPS // 5 SYNDICATES // 10 CADRES",
    "CALIB   : 10,000 HP REWORK // TWO-WORK LAW // REALIZATION WARS"
])

summary_box = create_box("SYSTEM COMPARISON AT A GLANCE // CORE METRICS", [
    "FEATURE                | LOBOTOMY CORPORATION | PROJECT SOMNARAK",
    "-----------------------+----------------------+--------------------",
    "Operating Agency       | Lobotomy Corporation | Reverie Directorate",
    "Primary Energy Source  | Enkephalin (PE/NE)   | Han-Energy",
    "Entity Classification  | Abnormalities        | Sorrow Entities",
    "Threat Hierarchy       | ZAYIN to ALEPH       | Ranks I-V / a to w",
    "Containment Discipline | 4 Works (All Units)  | Absolvohan (2 or 4)",
    "Inanimate Restriction  | Unrestricted         | 2 Works (Vid/Fer)",
    "Damage Spectrum        | RED/WHITE/BLACK/PALE | Grudge/Lam/Wgt/Void",
    "Crisis Mechanics       | Qliphoth Meltdowns   | Four Watches",
    "Breach Dynamics        | Standard Corridor    | Place Metamorphosis",
    "Equipment Extraction   | E.G.O (Weapon/Suit)  | M.A.W. (3 Pieces)",
    "Tool Entity Framework  | Tool Abnormalities   | Relic-Entities",
    "Department Awakening   | Core Suppressions    | Realization Wars",
    "External Guilds        | Fixer Associations   | Ten Cadres",
    "Underworld Factions    | The Five Fingers     | Five Raw Syndicates",
    "Equipment Tuning       | Fixer Workshops      | Five-Grade Forges"
])

factions_box = create_box("GEOPOLITICAL & FACTION EQUIVALENCE // MATRIX", [
    "LOBOTOMY CORP / THE CITY             | PROJECT SOMNARAK / THE RAW",
    "-------------------------------------+---------------------------------",
    "The Head / Wings of the City         | Council of Sighs / Directorate",
    "The Five Fingers (Syndicates)        | Five Syndicates of The Raw",
    "Fixer Associations (Hana, Zwei, etc) | Ten Specialist Cadres",
    "Fixer Workshops (Zelkova, Mook, etc) | Five Artisan Workshop Grades",
    "Backstreets & Outskirts              | The Raw & The Desolate",
    "The Well / Human Unconscious         | 1,778 Mnemonic Cycle Engrams"
])

realization_box = create_box("REALIZATION WARS & DEPARTMENT CRISIS // PHASES", [
    "PHASE | THEMATIC TRIAL      | COMBAT & PSYCHIC MANIFESTATION",
    "------+---------------------+-----------------------------------------",
    "I     | Awakening of Lament | Composure drain; auditory resonance spike",
    "II    | Grudge Surge        | Spatial displacement; kinetic shockwaves",
    "III   | Weight of Memory    | Gravitational debt; ancestral memories",
    "IV    | Void Integration    | Sovereign realization; permanent awakening"
])

compliance_box = create_box("DIRECTORATE SYSTEM COMPARISON VERIFICATION", [
    "DOCUMENT CLASS   : COMPLETE SYSTEM COMPARISON (EXPANDED STORY EDITION)",
    "VOCABULARY AUDIT : FULL 1-TO-1 CANONICAL & NARRATIVE LEXICON EXPANSION",
    "ROADMAP SYSTEMS  : 1,778 CYCLES / 5 WORKSHOPS / 5 SYNDICATES / 10 CADRES",
    "10,000 HP REWORK : STANDARD (150-1000 HP) / SOVEREIGN (10,000+ HP)",
    "TWO-WORK LAW     : STRICTLY ENFORCED ACROSS ALL INANIMATE TYPES",
    "STATUS           : FULLY RATIFIED & SYNCHRONIZED ACROSS ARCHIVE"
])

doc = f"""# COMPLETE SYSTEM COMPARISON: SOMNARAK vs. Lobotomy Corporation
## Direct 1-to-1 Universe, Mechanics & Narrative Reference
### Expanded Story Edition

{header_box}

> *"This document provides a comprehensive, 1-to-1 narrative and systems comparison between **Lobotomy Corporation** (Project Moon) and **Project Somnarak**. It serves both as a precise operational reference and as an enriched story bible for authors, game masters, and chroniclers. It preserves the authentic comparative format while fully detailing native vocabulary, cosmological lore, geopolitical underpinnings, containment mechanics, tactical calibrations, and narrative protocols across both universes."*

---

## 1. Executive Summary & Core Comparison Matrix

{summary_box}

---

## 2. Metaphysical Origins & Narrative Cosmology

The underlying mythos of both worlds drives their operational and narrative tone. In **Lobotomy Corporation**, horror arises from the commodification of the collective human unconscious, corporate exploitation, and the struggle for individual self-actualization. In **Project Somnarak**, horror stems from ancestral grief, accumulated historical injustice, communal mourning, and the heavy physical residue of saline tears accumulating over millennia.

| Cosmological Realm | Lobotomy Corporation (Project Moon) | Project Somnarak (Reverie Directorate) | Narrative & Story Synthesis |
|---|---|---|---|
| **Primary Metaphysical Force** | **Cogito / Human Unconscious** — Liquid extraction of human archetypes, fears, and suppressed desires. | **Han (  한   )** — Collective, unspoken historical sorrow, grief, and unavenged grief accumulated across 1,778 historical cycles. | Cogito manifests individual psyche into monsters; Han crystallizes communal grief into Sorrow Entities. |
| **Origin Reservoir** | **The Well / The River** — The subterranean reservoir of all human memory tapped by Carmen and Ayin. | **The Ancient Salt Sediment & 1,778 Mnemonic Engrams** (1,778  주기 기억 각인  ) — The fossilized stratum of ancestral tears beneath the bedrock. | The Well yields primordial mental archetypes; the Salt Sediment yields historical grief engrams. |
| **Philosophical Goal** | **The Seed of Light** — To break the City's disease of the mind, instilling genuine ego and emotional sincerity. | **The Great Pacification (  대안식   )** — To console the ancestral dead, resolve inherited debt, and maintain warmth in the Desolate. | Self-actualization and personal ego vs collective catharsis and communal survival. |
| **The Inhabited World** | **The City** — 26 colossal districts ruled by megacorporate Wings, encircled by Backstreets and the Outskirts. | **Somnarak City** — A fortified subterranean metropolis encircled by **The Raw (  생경   )** and **The Desolate (  황무지   )**. | Urban capitalist dystopia vs somber subterranean sanctuary surrounded by brine wastes. |
| **Cyclical Structure** | **The 50-Day Loop / The Script** — Thousands of simulated facility iterations orchestrated by Angela and Ayin. | **1,778 Mnemonic Cycles** — Historical civilizational resets recorded in the Directorate Mnemonic Archive. | Repeating temporal cycles designed to refine consciousness vs preserved historical grief records. |

---

## 3. Facility Architecture & Bureaucratic Hierarchy

Both settings feature a strict vertical bureaucracy governing subterranean containment chambers.

| Operational Feature | Lobotomy Corporation | Project Somnarak (Reverie Directorate) | Narrative & Story Register |
|---|---|---|---|
| **Managing Authority** | **Lobotomy Corporation** (Wing L of the City) | **The Reverie Directorate (  몽환국   )** governed by the **Council of Sighs (  위령원   )** | Corporate energy conglomerate vs solemn municipal civic trust and grief ministry. |
| **Facility Environment** | Subterranean bunker facility (District 12) divided into 10 Sephirah Departments. | Subterranean containment stratum: **The Absolvohan (  해원한   )**, constructed above the abyssal weeping vents. | Modern sterile industrial laboratories vs brutalist slate vaults lined with acoustic dampeners and incense grates. |
| **Primary Executive** | **The Manager (X)** advised by AI Coordinator **Angela**. | **The Dekan (  데칸   )** advised by Floor Secretaries (  서기관   ) and High Wardens. | Distant corporate overseer and synthetic guide vs ordained grief magistrate and monastic archivists. |
| **Department Structure** | Control, Information, Training, Security, Central Command, Welfare, Disciplinary, Extraction, Records, Architecture. | Departmental Floors: Floor 01 (Foundation), Floor 02 (Dekan Archive), Floor 03 (Thermal Hearth), Floor 04 (Acoustic Buffer), Floor 05 to Floor 10. | Departments supervise specific containment wings and provide facility buffs and defensive wards. |
| **Operative Personnel** | **Agents** (armed containment workers) and **Clerks** (office staff providing morale). | **Absolvers (  해원사   )** (containment operatives) and **Salt-Scrubbers (  염초공   )** (sanitation personnel). | Sacrificial corporate employees vs solemn sworn liturgical containment wardens. |
| **Tactical Rapid Response** | **Rabbit Team** (R Corp 4th Pack mercenaries) summoned for total sector cleansing. | **Cadre Sim-Pan (  심판   / Arbiters)** and **Cadre Gyeo-Tu (  격투   / Duelists)** mobilized for kinetic execution. | Hired private military shock troopers vs dedicated Directorate inquisitors and frontline champions. |

---

## 4. Energy Extraction & Production Systems

| Metric | Lobotomy Corporation | Project Somnarak | Mechanics & Story Lore |
|---|---|---|---|
| **Energy Medium** | **Enkephalin** — Green fluid extracted from Abnormalities; refined into electrical power. | **Han-Energy (  한 에너지   )** — Acoustic-metaphysical resonance harvested from pacified Sorrow Entities. | Enkephalin powers the City's technological infrastructure; Han-Energy powers Somnarak's thermal hearths and barrier wards. |
| **Work Output** | **PE-Boxes** (Positive Enkephalin) and **NE-Boxes** (Negative Enkephalin). | **Han-Energy Yield** per work cycle (08 to 40+ Han units). | PE-Boxes fill the facility's daily quota; Han-Energy fills municipal capacitors to stave off the freezing dark. |
| **Daily Quota** | Daily quota threshold (e.g., 200–1,200 PE) required to conclude the work day. | Daily Han-Quota required to maintain the Absolvohan's containment barriers and prevent citywide blackout. | Failure to meet daily quota triggers emergency overtime, panic, and structural containment instability. |
| **Sanitation / Byproducts** | Minor Enkephalin gas fumes; cleansers scrub residue. | **Han-Brine (  염간수   / *Yeomgansu*)** — Caustic saline fluid that crystallizes into corrosive salt if left unburned. | Somnarak incorporates physical brine build-up that erodes floorboards, requiring Haz-scorchers (  화용반   ) to burn it off. |

---

## 5. Entity Classification & Threat Tiers

Lobotomy Corporation ranks Abnormalities through a five-tier Hebrew risk scale. Project Somnarak uses the **SECC (Sorrow Entity Classification Code)** combining Coherence Ranks (I to V) and Potency Grades (α to ω):

| Threat Level | Lobotomy Corp Risk Tier | Somnarak Coherence Rank | Somnarak Potency Grade | Threat Scope & Containment Profile |
|---|---|---|---|---|
| **Lowest** | **ZAYIN** | **Rank I (Residue /   잔여  )** | **Grade α (Minor)** | Minimal danger; routine procedure; incapable of facility breach. |
| **Low-Mid** | **TETH** | **Rank II (Echo /   메아리  )** | **Grade β (Moderate)** | Manageable with standard precautions; minor mental or physical hazards. |
| **Mid-High**| **HE** | **Rank III (Fragment /   파편  )**| **Grade γ (Major)** | Demands specialized staff; capable of breaching and killing employees. |
| **High** | **WAW** | **Rank IV (Entity /   개체  )** | **Grade δ (Critical)** | Highly dangerous; facility-threatening breach risk; complex escape conditions. |
| **Apex** | **ALEPH** | **Rank V (Sovereign /   군주  )**| **Grade ω (Catastrophic)**| Catastrophic; city-threatening; requires total departmental mobilization. |

### 5.1 Entity Structural Types & Special Transform Breaches
- **Subject `[S]`:** Autonomous animate entities with biological or spiritual agency (e.g. humanoids, beasts, specters).
- **Object `[O]`:** Inanimate items, artifacts, relics, or tools.
- **Place `[P]`:** Structural chambers, cursed rooms, territorial environments, or localized spatial rifts.
- **Time `[T]`:** Temporal anomalies, looped moments, or chronometric disturbances.
- **Hazard `[H]`:** Environmental phenomena, toxic brine miasmas, or pervasive acoustic curses.

**Special Transform Breach (Place-to-Subject Metamorphosis):**
In Lobotomy Corporation, breached entities exit containment and roam corridors while maintaining their physical form. In Project Somnarak, specific apex Place entities undergo structural metamorphosis upon containment failure:
- Example: *The Maw* (`C-IVω-001 [GP]`), normally a stationary subterranean containment chamber, tears itself free from the surrounding rock stratum during breach, transforming into the mobile walking titan `C-IVω-001-B [GS]`.

---

## 6. Health Pools (HP) & Durability Scaling (The 10,000 HP Update)

In legacy development notes ("Old P.S."), Sorrow Entities were occasionally assigned uncapped 10,000 HP pools. This comparison updates that metric to its canonical balance:

| Category | Lobotomy Corporation HP | Project Somnarak Sorrow Gauge [HP] | Updated Balance Rationale |
|---|---|---|---|
| **ZAYIN / Rank I (α)** | 50 – 200 HP | **150 – 300 HP** | Novice training entities; low physical mass. |
| **TETH / Rank II (β)** | 200 – 500 HP | **300 – 500 HP** | Standard working entities; moderate durability. |
| **HE / Rank III (γ)** | 400 – 1,000 HP | **500 – 750 HP** | Armed combatants; requires coordinated suppression squads. |
| **WAW / Rank IV (δ)** | 800 – 2,500 HP | **750 – 1,000 HP** | Apex tactical entities; balanced for 10-node spatial combat. |
| **ALEPH / Rank V (ω)** | 2,000 – 10,000 HP (e.g. WhiteNight: 6,666 HP)| **1,000 – 12,000 HP** (e.g. Dawn of Mourning: 12,000 HP) | Multi-phase Sovereign Calamities and departmental Realizations. |
| **Planetary Geography** | N/A | **N/A (Invulnerable / Unfightable)** | Natural oceans, continental landmasses, and polar tundra are Geography, not combatants. |

---

## 7. Containment Disciplines & The Two-Work-Type Rule

Lobotomy Corporation uses four standardized work types. Somnarak formalizes containment through **The Absolvohan** (  해원한   / *Haewonhan*):

### 7.1 Direct Work Type Translation

| Lobotomy Corp Work | Somnarak Absolvohan Work | Meaning & Method | Tested Employee / Operative Stat |
|---|---|---|---|
| **Instinct** (Physical care) | **Viderehan (  관조한   / *Gwanjohan*)** | **Observation** — Monitoring acoustic frequencies and resonance from safety. | Fortitude (LC) / **Resilience** & **Clarity** (PS) |
| **Insight** (Environment care) | **Ferrehan (  인내한   / *Innaehan*)** | **Endurance** — Entering the unit to physically endure ambient pressure and cold. | Prudence (LC) / **Resilience** & **Composure** (PS) |
| **Attachment** (Social interaction)| **Flerehan (  통곡한   / *Tonggokhan*)** | **Weeping / Catharsis** — Empathetic emotional dialogue and reciprocal crying. | Temperance (LC) / **Composure** (PS) |
| **Repression** (Suppression) | **Pugnahan (  격투한   / *Gyeoktuhan*)** | **Confrontation / Wrath** — Kinetic suppression strikes to beat back growth. | Justice (LC) / **Resolve** (PS) |

### 7.2 The Inviolable Two-Work-Type Rule (Non-Subject Entities)
- **In Lobotomy Corporation:** Employees perform all four work types on almost all Abnormalities.
- **In Project Somnarak:** All **Object (`[O]`)**, **Place (`[P]`)**, **Time (`[T]`)**, and **Hazard (`[H]`)** entities can **ONLY** be worked with **Viderehan and Ferrehan**.
- **Flerehan and Pugnahan are strictly `N/A`:**
  * Inanimate objects, rooms, and temporal phenomena have no emotional consciousness to comfort (invalidating Flerehan).
  * Inanimate relics and districts have no biological body or anatomical center to strike (invalidating Pugnahan).
  * Performing Flerehan or Pugnahan on an inanimate SE causes automatic work failure, severe psychic backfire, and an immediate Sorrow Gauge surge.

---

## 8. Elemental Damage Spectrum & Psychological Rupture

Both systems utilize a four-element damage and defense architecture:

| LC Damage Type | Target Attribute | PS Han Element | Color | Target Attribute | Mechanical Identity in Combat |
|---|---|---|---|---|---|
| **RED** | Physical HP | **Grudge (  원한   )** | Crimson | Body (Physical HP) | Direct kinetic trauma; lacerations; breaks armor. |
| **WHITE** | Sanity (SP) | **Lament (  탄식   )** | Deep Blue | Composure (Sanity) | Acoustic weeping; Composure drain; induces panic. |
| **BLACK** | Dual HP & SP | **Weight (  무게   )** | Black | Body & Composure | Gravitational debt; crushes both physical HP and mental sanity. |
| **PALE** | % Max HP | **Void (  공허   )** | Pale White | Existential Core (% HP) | True percentage damage; existential erasure; ignores physical armor. |

### 8.1 Psychological Rupture & Panic States in Narrative
When an operative's mental fortitude collapses, their behavior breaks down according to the setting's psychological nature:

- **Lobotomy Corporation (Sanity Collapse / Panic):**
  * *Murderous Frenzy (High Fortitude):* The employee attacks nearby colleagues with equipped weapons.
  * *Wandering (High Prudence):* The employee enters a daze, roaming corridors and opening containment doors.
  * *Panic Suicide (High Temperance):* The employee takes their own life using their E.G.O weapon.
  * *Catatonia (High Justice):* The employee freezes in terror, unable to act or flee.
- **Project Somnarak (Composure Rupture /   침착 붕괴  ):**
  * *Mournful Hysteria (Resilience Rupture):* The operative breaks into uncontrollable wailing, emitting Lament shockwaves that drain nearby allies' Composure.
  * *Salt Paralysis (Clarity Rupture):* The operative's extremities calcify into brittle salt crust, reducing movement speed to zero and making them vulnerable to kinetic shatter.
  * *Echo-Possession (Composure Rupture):* The operative's vocal cords mimic the acoustic frequency of the Sorrow Entity, turning them into a thrall.
  * *Berserk Wrath (Resolve Rupture):* The operative lashes out in blind Grudge strikes, attacking friend and foe alike until subdued.

---

## 9. Breach Dynamics & Crisis Escalation

| Crisis Metric | Lobotomy Corporation | Project Somnarak | Updated Canonical Mechanics |
|---|---|---|---|
| **Facility Emergency** | **Qliphoth Meltdown** — Red alert sirens; countdown timers on random containment cells. | **Atmospheric Watches (  사경   )** — Barometric Han surges (First, Second, Third, Tide Watch). | Shifts in subterranean Han tides elevate facility-wide pressure and breach agitation. |
| **Breach Trigger** | **Qliphoth Counter** drops to 0. | **Sorrow Gauge** reaches 100% (or activation threshold). | When the counter drops / gauge fills, containment fails. |
| **Standard Breach** | Entity breaks door, enters hallway, and attacks employees. | Breaching Subject roams corridors along Range Bands. | Requires tactical suppression squads to intercept and pacify on the 10-node spatial grid. |
| **Special Transform Breach** | Not present (breached entities keep same code/form). | **Place-to-Subject Metamorphosis** (e.g. *The Maw* `C-IVω-001 [GP]` → `C-IVω-001-B [GS]`). | District/Place entities detach from the bedrock, transforming into mobile breaching colossi. |

### 9.1 The Four Atmospheric Watches of Somnarak
Unlike random Qliphoth meltdowns, Somnarak experiences cyclical atmospheric shifts driven by subterranean tides:
1. **First Watch (  일경   / *Ilgyeong*):** Ambient temperature drops; thin salt frost forms on iron bulkheads. Operative Composure drain increased by 10%.
2. **Second Watch (  이경   / *Igyeong*):** Acoustic resonance hums through floor grates; Han-Energy yield increased by 20%, but failure damage is doubled.
3. **Third Watch (  삼경   / *Samgyeong*):** Han-brine begins seeping through drainage pipes; random containment cells enter High Agitation (+25% starting gauge).
4. **Tide Watch (  해일경   / *Hae-ilgyeong*):** Total subterranean inundation; all Sorrow Entities gain +1 Speed slot and +20% Han Pressure [ATK]. Uncontained brine crystallizes corridors.

---

## 10. Equipment Extraction: E.G.O vs. M.A.W. Wear

| Equipment Domain | Lobotomy Corporation (E.G.O) | Project Somnarak (M.A.W. Wear) | Updated Synthesis |
|---|---|---|---|
| **Full Name** | **Extermination of Geas / Manifestation of Ego** | **Materialized Agony Wear (M.A.W.)** | Equipment crystallized from extracted entity matter. |
| **Equipment Triad** | **Weapon**, **Suit**, and **Gift**. | **Weapon**, **Suit**, and **Gift**. | Standard extraction yields a 3-piece set for operatives. |
| **Material Taxonomy** | Categorized primarily by Risk Grade (ZAYIN–ALEPH). | Categorized by **Five Material Weight Classes**: Primal Marrow, Tempered Brass, Resonant Alloy, Woven Thread, Void Glass. | Somnarak adds physical material weight and mobility modifiers. |
| **Mental Risk** | **E.G.O Corrosion** — Employee transforms into a feral puppet of the weapon upon panic. | **M.A.W. Meltdown** — Gear fuses into the nervous system under Composure Load, turning operative into an Echo. | Overuse or sanity collapse results in irreversible entity fusion. |

---

## 11. Tool Entities: Tool Abnormalities vs. Relic-Entities

| Feature | Lobotomy Corporation Tool Abnormalities | Project Somnarak Relic-Entities |
|---|---|---|
| **Sub-Types** | Single-Use, Equippable, Channeled / Continuous. | **A-Relics** (Consumable), **O-Relics** (Wearable), **I-Relics** (Stationary). |
| **Capability Badges** | `[Can Benefit Facility]`, `[Capable of Alteration]`, `[Capable of Instadeath]`. | Retains identical capability badges in all 82 Relic-Entity dossiers. |
| **Work Rule** | Used directly without work types. | **Strictly locked to Viderehan and Ferrehan only.** Pugnahan and Flerehan strictly N/A. |
| **Documentation** | Tiered log entries unlocked by usage count or duration. | **Progressive 4-Tier Log & Method Tables** (Tier I: Appearance → Tier IV: Origin Tale). |

---

## 12. Employee / Operative Core Attributes

| Lobotomy Corporation Attribute | Governed Metric | Project Somnarak Attribute | Governed Metric |
|---|---|---|---|
| **Fortitude** | Max HP (Physical Durability) | **Resilience (  회복력   )** | Max HP, physical wound recovery, armor carry capacity. |
| **Prudence** | Max SP (Mental Durability) | **Clarity (  명징성   )** | Max Composure, acoustic frequency detection, observation precision. |
| **Temperance** | Work Success Rate & Work Speed | **Composure (  침착성   )** | Emotional stability, resistance to Lament/Weight drain, Flerehan stability. |
| **Justice** | Attack Speed & Movement Speed | **Resolve (  결의   )** | Speed-scaled Action Points (AP), Pugnahan clash power, parry chance. |

---

## 13. Story Expansion: Outer World Governance & Subterranean Geopolitics

{factions_box}

For narrative fiction and worldbuilding, both universes feature intricate geopolitical power structures operating beyond facility walls:

### 13.1 The City vs. Somnarak City & The Raw
- **The City (Project Moon):** Governed by **The Head** (A Corp, B Corp, C Corp) with absolute taboos enforced by Arbiters and Claws. The 26 Wings exploit their Singularities, while the **Five Fingers** (Thumb, Index, Middle, Ring, Pinky) govern the underworld Backstreets through brutal syndicates.
- **Somnarak City & The Raw (Project Somnarak):** Somnarak City is an engineered cavern stronghold governed by the **Council of Sighs (  위령원   )** and the **Reverie Directorate (  몽환국   )**. Outside the thermal wards lies **The Raw (  생경   )**, a lawless undercity built in the salt-encrusted ruins of previous cycles, and beyond that lies **The Desolate (  황무지   )**, the frozen exterior surface.

### 13.2 The Five Syndicates of The Raw
In the underworld of The Raw, five criminal organizations control illicit trades, contraband mourning gear, and unrefined sorrow:
1. **The Menders (  수선공   / *Suseongong*):** Flesh-weavers and surgical embalmers who suture dying operatives back together using thread spun from Sorrow Entity hair.
2. **The Rust Frays (  녹슨 올   / *Nokseun Ol*):** Heavy scrappers and demolition scavengers who harvest decommissioned containment plating, hydraulic pistons, and seismic drilling rigs.
3. **The Veil Merchants (  면사포 상단   / *Myeonsapo Sangdan*):** Smugglers and black-market dealers in mourning veils, acoustic dampening silks, and contraband Grade β Relics.
4. **The Memory Washers (  기억 세탁관   / *Gieok Setakkwan*):** Illicit psycho-surgeons who scrub traumatizing containment memories from deserters and traumatized citizens for exorbitant fees.
5. **The Debt Concourse (  부채 회랑   / *Buchae Hoirang*):** Ruthless usurers who trade in ancestral grievances, blood contracts, and karmic debts, enforcing repayment through ritualistic salt-branding.

---

## 14. Story Expansion: Specialist Cadres & Contractor Bureaus

While Lobotomy Corporation hires independent Fixers and Associations (Hana, Zwei, Shi, Dieci, Liu, Seven) through the Charles Office and Hana Association, the Reverie Directorate contracts **The Ten Specialist Cadres (  십대 전문직 결사   / *Sipdae Jeonmunjik Gyeolsa*)**:

| Specialist Cadre | Korean Title | Functional Role & Expertise | Lobotomy / PM Fixer Equivalent |
|---|---|---|---|
| **Cadre Giltong** |   길통   (*Giltong*) | **Spatial Navigators & Cartographers** — Chart shifting labyrinthine corridors, Range Bands, and spatial warps. | Seven Association / Charles Office scouts |
| **Cadre Su-Ho** |   수호   (*Suho*) | **Bulwark Sentinels & Heavy Wardens** — Deploy portable acoustic shields and blast barriers during breaches. | Zwei Association (Protection & defense) |
| **Cadre Tam-Sa** |   탐사   (*Tamsa*) | **Abyssal Inquisitors & Sounders** — Venture into unmapped salt strata to locate dormant Sorrow Entities. | Tres Association / Deep exploratory Fixers |
| **Cadre Sim-Pan** |   심판   (*Simpan*) | **Directorate Arbiters & Executioners** — Enforce containment laws, eliminate mutineers, and execute breaching entities. | The Head's Arbiters / Shi Association |
| **Cadre Il-Gwang** |   일광   (*Ilgwang*) | **Thermal Engineers & Sun-Prism Operators** — Focus intense thermal light to burn away corrosive Han-brine. | Dawn Office / Cinq Association |
| **Cadre Hwa-Yong** |   화용   (*Hwayong*) | **Pyre-Alchemists & Salt-Incinerators** — Deploy chemical flamethrowers to incinerate crystallized salt crusts. | Liu Association (Flames and incineration) |
| **Cadre Jeong-Bo** |   정보   (*Jeongbo*) | **Acoustic Cryptographers & Archive Wardens** — Decode entity resonance frequencies and catalog tales. | Hana Association / Seven Association analysts |
| **Cadre Un-Song** |   운송   (*Unsong*) | **Heavy Logistics Draymen** — Transport pressurized Han-Energy capacitors and volatile Relic-Entities. | Devyat Association (Courier and transport) |
| **Cadre Ui-Ryo** |   의료   (*Uiryo*) | **Saline Psych-Surgeons** — Treat Composure Rupture, extract crystallized salt from lungs, and realign nerves. | Doctor Fixers / Biotechnical clinics |
| **Cadre Gyeo-Tu** |   격투   (*Gyeotu*) | **Vanguard Duelists & Suppression Champions** — Master kinetic melee combat on the 10-node spatial grid. | Shi Association / Special strike Fixers |

---

## 15. Story Expansion: Equipment Tuning & Artisan Workshops

In Project Moon lore, Fixers purchase specialized weapons and clothing crafted by high-end Workshops (Zelkova, Old Boys, Atelier Logic, Mook, Wheels Industry). In Project Somnarak, containment gear is manufactured and refined through **The Five Workshop Grades (  공방 체계   / *Gongbang Chegye*)**:

| Workshop Grade | Workshop Tier | Access & Procurement | Drop Probability | Legendary Stat Rationale |
|---|---|---|---|---|
| **Grade 1 Forge** | Apprentice Workshop | Open purchase at all Absolvohan armories; basic field-issue gear. | Common (100%) | Standard baseline parameters; no special abilities. |
| **Grade 2 Forge** | Journeyman Workshop | Directorate contract required; reinforced alloys and dampening weave. | High (50.0%) | +10% Resistance to chosen Han damage element. |
| **Grade 3 Forge** | Master Artisan Atelier | Requires Tier 3 clearance; custom resonant tuning for specific Cadres. | **5.0% Drop** | Grants unique combat passive (e.g. Acoustic Parry). |
| **Grade 4 Forge** | Grand Foundry Guild | Restricted to Floor Secretaries and high-ranking Absolver squads. | **1.0% Drop** | Active ability; spatial manipulation on the 10-node grid. |
| **Grade 5 Forge** | Sovereign Master Forge | **Attains Legendary Stat; requires active contracted employment.** | **0.5% Drop** | **Legendary Stat:** Unlocks ultimate signature trait and sovereign damage multiplier. |

### 15.1 The Legendary Stat & Employment Covenant
To wield Grade 5 Workshop equipment, an operative cannot simply purchase or loot the gear. They must swear a formal **Employment Covenant (  고용 서약   )** with the master artisan guild. If the operative breaks service or falls into Composure Rupture, the equipment's resonant matrix seals itself, preventing misuse by unauthorized parties.

---

## 16. Story Expansion: Departmental Awakenings & Realization Wars

{realization_box}

In Lobotomy Corporation, the Manager must face **Sephirah Meltdowns (Core Suppressions)** from Malkuth to Keter, resolving each Sephirah's personal trauma to awaken the facility's full potential and complete the Seed of Light.

In Project Somnarak, the Dekan must guide each Floor Secretary through **Echo-Core Resonant Realization Wars (  잔향핵 공명 각성전   / *Janhyanghaek Gongmyeong Gakseongjeon*)**:
- **Narrative Premise:** Each departmental floor is anchored by an Echo-Core containing the accumulated grief of past cycles. To achieve complete harmonic synchronization, the Floor Secretary must descend into the core's psychological crucible and wage a 4-phase trauma battle:
  1. **Phase I — Awakening of Lament:** The floor is flooded with acoustic weeping. Operatives suffer continuous Lament pressure and must maintain Composure thresholds while decoding resonance nodes.
  2. **Phase II — Grudge Surge:** Physical shockwaves shatter the containment floor. Breaching phantoms test the squad's clash power on the 10-node spatial grid.
  3. **Phase III — Weight of Memory:** Ancestral memories from the 1,778 historical cycles manifest as crushing gravitational burdens. Operatives must manage Weight damage and coordinate tactical positioning.
  4. **Phase IV — Void Integration:** The Secretary confronts their personal despair, integrating the floor's ancestral grief into an enlightened state of harmonic mastery.
- **Permanent Facility Buff:** Surviving a Realization War grants permanent departmental passives, immunity to specific Atmospheric Watch penalties, and unlocks Grade 5 Workshop commissioning for that floor.

---

## 17. Comprehensive Narrative Lexicon (1-to-1 Story Dictionary)

This lexicon serves authors and creators adapting scenarios, dialogue, or lore between the two settings:

| Lobotomy Corporation / Project Moon | Project Somnarak (Reverie Directorate) | Narrative Meaning & In-Universe Application |
|---|---|---|
| **Abnormality** | **Sorrow Entity (  비탄의 개체   )** | The supernatural phenomena contained within the facility. |
| **E.G.O (Equipment)** | **M.A.W. Wear (  물질화 고뇌복   )** | Weapons and protective suits extracted from contained entities. |
| **E.G.O Corrosion** | **M.A.W. Meltdown (  고뇌복 용해   )** | Catastrophic fusion between equipment and operative's nervous system. |
| **Enkephalin** | **Han-Energy (  한 에너지   )** | Refined energy extracted from entities to power the civilization. |
| **PE-Box / NE-Box** | **Han Yield (  한 생산량   )** | The measure of positive extraction vs volatile waste per cycle. |
| **Qliphoth Meltdown** | **Atmospheric Watch (  사경   )** | Facility-wide crisis timer triggering increased entity aggression. |
| **Qliphoth Counter** | **Sorrow Gauge (  비탄 척도   )** | Containment integrity threshold; reaching zero (or 100%) triggers breach. |
| **Instinct Work** | **Viderehan (  관조한   / *Gwanjohan*)** | Containment via remote acoustic observation and frequency monitoring. |
| **Insight Work** | **Ferrehan (  인내한   / *Innaehan*)** | Containment via direct physical endurance inside the chamber. |
| **Attachment Work** | **Flerehan (  통곡한   / *Tonggokhan*)** | Containment via reciprocal empathetic weeping and emotional dialogue. |
| **Repression Work** | **Pugnahan (  격투한   / *Gyeoktuhan*)** | Containment via wrathful kinetic strikes to suppress entity growth. |
| **Sanity (SP)** | **Composure (  침착성   )** | Mental equilibrium; when depleted, operative suffers Composure Rupture. |
| **HP (Health Points)** | **Sorrow Gauge / Physical Durability** | Structural or biological integrity of entities and operatives. |
| **The Manager (X)** | **The Dekan (  데칸   )** | The supreme tactical commander and overseer of containment operations. |
| **Angela (AI Coordinator)** | **Floor Secretary (  서기관   )** | The protocol archivist and tactical liaison guiding operatives. |
| **Agent** | **Absolver (  해원사   )** | Sworn elite field operative entering containment cells. |
| **Clerk** | **Salt-Scrubber (  염초공   )** | Auxiliary personnel maintaining sanitation, brine drainage, and grates. |
| **Tool Abnormality** | **Relic-Entity (  유물 개체   )** | Inanimate or stationary entities operated under strict Two-Work rules. |
| **Core Suppression** | **Realization War (  각성전   )** | Departmental psychological boss battle resolving ancestral trauma. |
| **The City** | **Somnarak City (  솜나락 도성   )** | The main human metropolitan stronghold. |
| **Backstreets** | **The Raw (  생경   )** | The unpatrolled, violent undercity surrounding the facility. |
| **Outskirts** | **The Desolate (  황무지   )** | The frozen, uninhabitable planetary badlands beyond the perimeter. |
| **The Fingers (Syndicates)** | **Five Syndicates of The Raw** | Major criminal syndicates governing the underworld outside Directorate law. |
| **Fixers & Associations** | **Ten Specialist Cadres** | Specialized contractor guilds providing mercenary and tactical services. |
| **Fixer Workshops** | **Artisan Workshops (Grades 1–5)** | Specialized guilds forging high-tier containment weapons and armor. |
| **The Well / Cogito** | **1,778 Mnemonic Engrams** | The ancient repository of collective subconscious memory and grief. |
| **Seed of Light** | **The Great Pacification (  대안식   )** | The ultimate philosophical goal of resolving all accumulated human grief. |

---

## 18. Story Protocol & Dialogue Vignettes

To illustrate the contrasting atmosphere, narrative tone, and operational jargon, the following parallel scenes depict a routine containment dispatch:

### 18.1 Lobotomy Corporation Dispatch Protocol
> **[P.A. Announcement — Control Team Chime]**  
> *"Attention, Agent Justin. You are scheduled for Attachment Work with O-01-04 (The Lady Facing the Wall). Equip your WhiteNight Suit and ensure your mental stabilizer injectors are primed. Maintain eye contact, recite the designated reassurance script, and do not acknowledge the acoustic frequencies echoing behind the plaster. Complete the cycle within forty seconds to preserve PE-Box purity. Lobotomy Corporation appreciates your devotion."*

### 18.2 Reverie Directorate Dispatch Protocol
> **[P.A. Announcement — Resonance Bell Chime]**  
> *"Attention, Absolver Min-Seo. The Dekan has inscribed your ledger for Flerehan (  통곡한   ) with Entity C-IIIγ-019 (The Weeping Weaver). Fasten your Resonant Alloy mantle and burn three sticks of sandalwood incense at the air-dam sill. When you cross the acoustic threshold, open your heart to the entity's grief, but anchor your Composure to the Directorate hearth. Weep with the entity until the salt brine flows clear, but do not drink the tears. Bear the weight of our ancestors, and return unbroken."*

---

## 19. Verification & Canonical Compliance Seal

{compliance_box}
"""

target_path = "SOMNARAK-WORLD/Master_Codices/06_Integrity_Audits_and_Comparative_Studies/COMPLETE_SYSTEM_COMPARISON_SOMNARAK_VS_LOBOTOMY_CORPORATION.md"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(doc)

root_path = "COMPLETE_SYSTEM_COMPARISON_SOMNARAK_VS_LOBOTOMY_CORPORATION.md"
with open(root_path, "w", encoding="utf-8") as f:
    f.write(doc)

print("Both expanded comparative files written successfully!")
