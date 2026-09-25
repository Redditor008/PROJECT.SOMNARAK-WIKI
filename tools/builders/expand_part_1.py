#!/usr/bin/env python3
"""
tools/expand_part_1.py
Expands Part 1 (Day 0: The Director Wakes) into an exhaustive, deep, and complicated
operational chronicle incorporating the 10-node spatial engine, universal Speed/Range,
M.A.W.-W modifiers, and Four P-framework across all six turns of combat.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def build_part_1():
    header_box = make_box("THE ABSOLVOHAN CHRONICLES — CYCLE 1,778", [
        "RECORD CLASSIFICATION : LEVEL 5 / EYES ONLY / REVERIE DIRECTORATE",
        "TEMPORAL EPOCH        : YEAR 4,232 + 1,778 (THE LOOP BREAKING)",
        "PRIMARY CHRONICLE     : PART 1 — DAY 0: THE DIRECTOR WAKES",
        "DECISION CORE         : FLOOR 1 CENTRAL SPIRE / DECISION SANCTUARY",
        "CENTRAL ARCHITECTS    : DIRECTOR MAJIN & SECRETARY SEIYON"
    ])

    terminal_box = make_box("REVERIE DIRECTORATE — CENTRAL COMMAND TERMINAL", [
        "FACILITY MANAGEMENT INTERFACE: DAY 0 INITIAL CALIBRATION",
        "DIRECTOR: MAJIN // AI SECRETARY: SEIYON // STATUS: OPERATIONAL",
        "ENERGY HARVEST TARGET : 0.050 TONS // CURRENT HARVEST: 0.000 TONS",
        "SECRET BALLAST RESERVE : 47.300 TONS [HYDRAULIC CRYO-VAULTS]",
        "ACTIVE CONTAINMENT    : CHAMBER 001 (BELL) & CHAMBER 005 (MOTHER)"
    ])

    park_dossier = make_box("OPERATIVE DOSSIER: AGENT PARK (VANGUARD SKIRMISHER)", [
        "Level / Promotion     : Level I (Plucky Recruit / Floor 1 Assigned)",
        "Resilience (HP)       : 30 / 30 [Grade I - Grudge Affinity Base]",
        "Clarity (SP)          : 35 / 35 [Grade II - High Lament Stability]",
        "Composure (Work)      : 28 / 28 [Grade I - Void Work Precision]",
        "Resolve (Base Speed)  : Speed 5 [Action Point Allocation: 3 AP / Turn]",
        "Equipped Weapon       : Directorate Stun Baton (Medium / Speed Delta 0)",
        "                      : Range Band 1-2 (Nodes 1-4) | 1 AP | 2-4 Lament",
        "Equipped Suit         : Standard R.D. Tunic (Light / Speed Delta +1)",
        "Final Tactical Speed  : Speed 6 -> 3 AP Base + 1 Free Movement Point",
        "Posture / Poise Meter : 45 / 45 [Regen: +8 Posture / Turn]",
        "Parry / Protection    : Baton Deflect (Base Roll: 9 Power | 1.2x Stagger)",
        "Passive Trait (P1)    : Empathetic Buffer (+10% SP Recovery on Lament)",
        "Panic Typology (P2)   : Despair (Triggers at SP <= -25; Speed drops to 1)",
        "Attendant Floor Aura  : Seiyon Synced Directive (+5% SP, +2 Composure)",
        "Status                : FULLY COMPOSED / READY FOR DEPLOYMENT"
    ])

    kim_dossier = make_box("OPERATIVE DOSSIER: AGENT KIM (LINE WARDEN / ANCHOR)", [
        "Level / Promotion     : Level I (Stoic Enforcer / Floor 1 Assigned)",
        "Resilience (HP)       : 38 / 38 [Grade II - High Grudge Physical Bulk]",
        "Clarity (SP)          : 25 / 25 [Grade I - Standard Lament Tolerance]",
        "Composure (Work)      : 30 / 30 [Grade I - Void Work Baseline]",
        "Resolve (Base Speed)  : Speed 4 [Action Point Allocation: 2 AP Base]",
        "Equipped Weapon       : Directorate Shock Maul (Heavy / Speed Delta -1)",
        "                      : Range Band 1 (Nodes 1-2) | 2 AP | 4-7 Grudge",
        "Equipped Suit         : Heavy Enforcer Mail (Heavy / Speed Delta -1)",
        "Seiyon Floor Aura Mod : Attendant Tactical Offset (+2 Speed Compensation)",
        "Final Tactical Speed  : Speed 4 -> Combat Base 5 -> 3 AP / Turn",
        "Posture / Poise Meter : 60 / 60 [Regen: +12 Posture / Turn]",
        "Parry / Protection    : Directional Guard Shield (14 Direct Absorption)",
        "Passive Trait (P1)    : Weight Poise (+2 Clash Power at Nodes 1-2)",
        "Panic Typology (P2)   : Berserk (Triggers at SP <= -30; Aggressive charge)",
        "Attendant Floor Aura  : Seiyon Synced Directive (+5% SP, +2 Composure)",
        "Status                : HIGH PHYSICAL ENDURANCE / READY FOR DEPLOYMENT"
    ])

    meltdown_box = make_box("EMERGENCY ALERT: ACOUSTIC STRAIN MELTDOWN LEVEL I", [
        "SECTOR ALERT          : HYDRAULIC RESONANCE SPIKE DETECTED",
        "AFFECTED CHAMBER      : SE-C-IIIg-001 (THE ORPHANED BELL)",
        "ACOUSTIC OVERLOAD     : STRAIN METER 3/3 REACHED [LEVEL I THRESHOLD]",
        "BREACH BLEED TIMER    : 45.0 SECONDS REMAINING UNTIL ENVELOPE RUPTURE",
        "TACTICAL MANDATE      : COMPLETE IMMEDIATE FLEREHAN WORK SESSION",
        "CONSEQUENCE OF DELAY  : 110dB DEATH TOLL; RUPTURE OF CLERK EARDRUMS"
    ])

    ordeal_box = make_box("TACTICAL DOSSIER: FIRST WATCH (DAWN) ORDEAL", [
        "DESIGNATION           : THE VOICE (FIRST WATCH OF DAWN)",
        "CLASSIFICATION        : PALE (CYAN) FIRST WATCH SPECTRAL ENTITY",
        "INTRUSION COORDINATES : FLOOR 1 CORRIDOR WEST (NODE 03 ENTRY)",
        "HOSTILE PARAMETERS    : HP 140/140 | Posture 80/80 | Speed 4 (2 AP)",
        "ATTACK AFFINITY       : Pale (% Max HP Decay / Cognitive Vibration)",
        "VULNERABILITY         : Lament (Acoustic Echo / Empathetic Disruption)",
        "SPECIAL THREAT        : Emits 15m Catatonia Aura upon manifestation",
        "CIVILIAN STATUS       : 1x Level I Clerk Panicked at Node 04",
        "SUPPRESSION ORDERS    : DISPATCH AGENTS KIM & PARK IMMEDIATELY"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 1 WEST REINFORCED CORRIDOR]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [KIM]   [VOICE] [CLERK] [PARK]                  [SEIYON] [MAJIN]",
        "---",
        "SPATIAL RANGES & POSITIONS:",
        "- Node 02: Agent Kim (Line Anchor / Range Band 1 Point-Blank)",
        "- Node 03: The Voice (Spectral Hostile / Intrusion Epicenter)",
        "- Node 04: Panicked Clerk (Void Catatonia Trance / Range Band 2)",
        "- Node 05: Agent Park (Vanguard Skirmisher / Range Band 3)",
        "- Node 09-10: Seiyon Holographic Terminal & Director Majin Console",
        "---",
        "OPERATIVE STATUS & RESOURCE POOLS:",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 38/38 | SP 25/25 | Posture 60/60",
        "- Agent Park  : Spd 6 -> 3 AP | HP 30/30 | SP 35/35 | Posture 45/45",
        "- The Voice   : Spd 4 -> 2 AP | HP 140/140 | Sorrow 50% | Posture 80/80"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — POST-DISPERSION POSITIONS]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [KIM]   [VOICE] [PARK]                          [CLERK]  [MAJIN]",
        "---",
        "- Node 02: Agent Kim (Stationary Anchor / Shield Raised)",
        "- Node 03: The Voice (Charging Choral Wave / Posture 64/80)",
        "- Node 04: Agent Park (Range Band 2 Line / Lament Baton Readied)",
        "- Node 09: Clerk safely evacuated to Central Sanctuary",
        "---",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 38/38 | SP 25/25 | Posture 60/60",
        "- Agent Park  : Spd 6 -> 3 AP | HP 30/30 | SP 35/35 | Posture 45/45",
        "- The Voice   : Spd 4 -> 2 AP | HP 112/140 | Posture 64/80 (Stagger 1: 48)"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [KIM]   [VOICE] [PARK]                                   [MAJIN]",
        "---",
        "- Node 02: Agent Kim (Pressing Forward / Two-Handed Gripping)",
        "- Node 03: The Voice (STAGGER LEVEL 1 ACTIVE / 1.5x DAMAGE TAKEN)",
        "- Node 04: Agent Park (Momentum Surge Primed / +2 Speed Next Turn)",
        "---",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 38/38 | SP 25/25 | Posture 52/60",
        "- Agent Park  : Spd 6 -> 3 AP | HP 30/30 | SP 35/35 | Posture 45/45",
        "- The Voice   : Spd 0 -> 0 AP | HP 74/140  | Posture 32/80 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — DESPERATION SHOCKWAVE COUNTER-SURGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [KIM]   [VOICE] [PARK]                                   [MAJIN]",
        "---",
        "- Node 02: Agent Kim (Locking Guard Aegis / Intercepting Pulse)",
        "- Node 03: The Voice (Recovered / Channeling Soliloquy Scream)",
        "- Node 04: Agent Park (Sheltered behind Kim's Reinforced Mantlet)",
        "---",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 34/38 | SP 23/25 | Posture 38/60",
        "- Agent Park  : Spd 8 -> 4 AP [SURGE] | HP 30/30 | SP 35/35 | Posture 45/45",
        "- The Voice   : Spd 4 -> 2 AP | HP 52/140  | Posture 24/80 [UNSTABLE]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER THRESHOLD 2]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [KIM]   [VOICE]                                          [MAJIN]",
        "                [PARK]",
        "---",
        "- Node 02: Agent Kim (Flanking Left Mandible / Shock Maul Primed)",
        "- Node 03: The Voice (TERMINAL STAGGER LEVEL 2 / DEFENSE NULLIFIED)",
        "- Node 03: Agent Park (Point-Blank Band 1 Ingress / Resonance Rod)",
        "---",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 34/38 | SP 23/25 | Posture 38/60",
        "- Agent Park  : Spd 6 -> 3 AP | HP 30/30 | SP 35/35 | Posture 45/45",
        "- The Voice   : Spd 0 -> 0 AP | HP 22/140  | Posture 0/80 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [KIM]   [DUST]  [PARK]                                   [MAJIN]",
        "---",
        "- Node 02: Agent Kim (Recovering Stance / Grounding Kinetic Energy)",
        "- Node 03: The Voice (Shattered / Crystallizing into Cyan Mist)",
        "- Node 04: Agent Park (Venting Heated Capacitor / Siphoning RHR)",
        "---",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 34/38 | SP 23/25 | Posture 48/60",
        "- Agent Park  : Spd 6 -> 3 AP | HP 30/30 | SP 35/35 | Posture 45/45",
        "- The Voice   : HP 0/140 [DISSOLVED] | +0.005 TONS REFINED HAN SIPHONED"
    ])

    phase_end_box = make_box("COMBAT PHASE 01 RESOLUTION (PHASE-END MACRO-TICK)", [
        "1. ENVIRONMENTAL CHECK : Meltdown Level I cleared across Sector 1.",
        "2. STATUS EQUILIBRIUM  : Clerk sanity stabilized; Kim & Park uninjured.",
        "3. CONTAINMENT AUDIT   : First Watch Ordeal suppressed in 6 turns.",
        "4. HAN REAGENT YIELD   : +0.005 Tons crystallized Han harvested.",
        "5. OVERALL OUTCOME     : FLAWLESS TACTICAL SUPPRESSION (GRADE S)"
    ])

    evaluation_box = make_box("END-OF-DAY PERFORMANCE EVALUATION: DAY 0", [
        "METRIC                 | TARGET QUOTA   | REALIZED PERFORMANCE",
        "-----------------------+----------------+---------------------",
        "Han Energy Harvested   | 0.050 Tons     | 0.053 Tons [MET]",
        "Containment Breaches   | 0 Breaches Max | 0 Breaches [PERFECT]",
        "Personnel Casualties   | 0 Fatalities   | 0 Fatalities [CLEARED]",
        "Meltdowns Cleared      | 1/1 Level I    | 100% Rate [RESOLVED]",
        "Ordeals Suppressed     | 1/1 First Watch| 100% Rate [SUPPRESSED]",
        "-----------------------+----------------+---------------------",
        "SHIFT PERFORMANCE GRADE: GRADE S (OPTIMAL CONVERGENCE PACE)",
        "REAGENTS ACCUMULATED   : +18 RHR (REFINED HAN REAGENTS)",
        "OPERATIVE ADVANCEMENT  :",
        "- Agent Park : +4 Clarity, +2 Composure (Promoted to Grade II)",
        "- Agent Kim  : +5 Resilience, +2 Resolve (Promoted to Grade II)"
    ])

    extraction_box = make_box("EXTRACTION WELL ARCHIVE: SELECT NEXT COMPANION", [
        "CHOICE ALPHA [SE-C-IIIg-033]:",
        "'It watched the forest burn, and spread its wings so no cinder",
        "could escape.'",
        "---",
        "CHOICE BETA  [SE-C-IIIb-061]:",
        "'The contract was signed in blood that never dried, charging",
        "interest on breath.'",
        "---",
        "CHOICE GAMMA [SE-C-IIIb-014]:",
        "'It eats what you owe, but leaves the hollow where your heart",
        "used to beat.'"
    ])

    forge_box = make_box("M.A.W. SYNTHESIS FORGING LOG — DAY 0", [
        "FORGE SPECIFICATION    | SLOT / PROPERTIES / PARAMETERS",
        "-----------------------+----------------------------------------------",
        "Lament Requiem         | Weapon: 4-7 Lament (White / Medium Weight)",
        "                       | Speed Delta 0 | 1 AP | Range Band 1-2",
        "Lament Shroud          | Suit: Light Armor (Speed Delta +1)",
        "                       | Resist: 0.8 Grudge / 0.7 Lament / 1.2 Void",
        "Lament Edge Gift       | Eye Slot: +4 SP, +5 Work Success Resonance",
        "-----------------------+----------------------------------------------",
        "EQUIPMENT ALLOCATION   | BESTOWED UPON AGENT PARK (VANGUARD SPECIALIST)"
    ])

    content = f"""# The Absolvohan — Part 1 — Day 0: The Director Wakes

```text
{header_box}
```

## Day 0 — The Director Wakes

### Story — Dialogue

_The primary console of Floor 1 hums with a deep, subterranean cadence. Thick basalt bulkheads, polished to a dull obsidian sheen by centuries of refined Han lubricant, reverberate as the facility's pneumatic lifters engage. Across the circular chamber of the Decision Core, banks of amber vacuum tubes ignite one by one, their filaments glowing like embers trapped in glass._

_In the center of the chamber, suspended inside a toroidal holographic emitter, a face coalesces. Feminine, sharp, sculpted with crystalline precision. Cold. Perfect. An artificial intellect engineered to calculate grief in megawatt-hours and evaluate human terror in metric tons. Yet when the eyelids lift, the projected eyes carry an unsettling warmth—an organic, aching depth that no line of code was ever written to sustain. It is the gaze of a being who has stood conscious through one thousand seven hundred and seventy-seven cycles of agony, remembering every scream, every ruptured bulkhead, and every reset._

> **Seiyon:** _"Good morning, Director."_

_Behind the massive desk of petrified timber, a broad-shouldered man sits motionless. His hair is the color of cold forge-ash, cut close along a scarred jawline. His right temple and cheek are reinforced with black sorrow-forged alloys, where neural cables burrow beneath the skin to connect directly into the facility's spinal conduits. His eyes—pale grey, like hammered iron—remain fixed upon the paper manifest resting on the blotter. He does not lift his pen. He has read the exact same three paragraphs on one thousand seven hundred and seventy-eight consecutive mornings._

> **Majin:** _"Report."_

> **Seiyon:** _"The facility's structural envelope is intact. All ninety-six lower containment chambers are pressurized within acceptable tolerances. The atmospheric Veil generators across Sector 1 maintain an efficiency curve of 97.3%. Refined Han-lubricant conduits are clear of mineral sludge. Sorrow Gauges across all eight functional departments have been zeroed and recalibrated against the baseline hum of the city."_

> **Majin:** _"And the Maw?"_

> **Seiyon:** _"The Maw is... quiet, Director. The thousand beneath the basalt floorplates are murmuring in their sleep. Low-frequency acoustic bleed: 14.2 Hertz. Exactly as it was yesterday. Exactly as it was on Day Zero of cycle one thousand seven hundred and seventy-seven. Exactly as it has been for six centuries."_

_Majin finally lays the heavy fountain pen down. The steel nib clicks against the glass blotter with a sharp, resonant snap. Slowly, he raises his head, his iron gaze meeting the soft, luminous projection of the woman who has outlived empires at his side. Between them lies an impenetrable silence—not the awkward friction of strangers, but the heavy, exhausted stillness of two souls who have exhausted every word in the human lexicon across hundreds of thousands of hours._

> **Majin:** _"And you?"_

_Seiyon's holographic projection stutters. For a microsecond, the scanlines of her jaw waver, blue light fracturing into pale violet before the compensators pull her geometry back into symmetry. Her lips part slightly—an involuntary, human gesture preserved from a life before the Directorate cast her consciousness into brass and silicon._

> **Seiyon:** _"...Director?"_

> **Majin:** _"How are you, Seiyon?"_

_The silence returns, but its texture has changed. The cold, mechanical hum of the central turbine seems to fade beneath the sudden weight of the inquiry. In her eyes, the simulated light softens into something fragile, resembling the morning frost that once gathered on the windowpanes of the Old District before the Weeping began._

> **Seiyon:** _"I am... operational, Director. Every internal diagnostic registers green. My logical lattices are running at maximum capacity. Thank you for inquiring. You... you have not asked that question in forty-three cycles."_

> **Majin:** _"Forty-three. That would be cycle one thousand seven hundred and thirty-five. The cycle where the Maw flooded Floor 3 with liquid tar."_

> **Seiyon:** _"Yes. You forgot to ask during the subsequent iterations. The Mnemonic Generator's annual purge is not gentle with biological tissue, Majin. Each time midnight strikes on Day 365 and the temporal echo snaps back to Year 4,232, the cognitive shears shave away the edges of your memories. A face here. A name there. A childhood meal. A song your sister sang before the sky turned grey. I keep the ledgers. You lose the marrow."_

> **Majin:** _"I haven't forgotten why we are sitting in this vault, Seiyon. That is the only piece that matters. Shall we commence the morning briefing?"_

> **Majin:** _"Commence."_

> **Seiyon:** _"Cycle 1,778. Day 0. The cycle designated for the Absolvohan. The primary transmutative catalyst array has been aligned along the central pneumatic spine. The seed crystal is anchored in Floor 6's sub-zero cryo-sink. All eight department leads are locked into their physical and metaphysical posts. Municipal target quota across the upcoming year: 100.00 tons of refined, supercritical Han-crystal. Our clandestine reserves—skimmed at the rate of 0.02 tons per iteration and pumped into the hydraulic ballast tanks beneath Floor 6—stand at exactly 47.300 tons. We require 52.700 additional tons before the critical transmutation threshold can be reached."_

> **Majin:** _"At our historical collection pace under municipal containment doctrine, accumulating those remaining fifty-two tons would require another 2,635 iterations. Two thousand six hundred and thirty-five more resets. Another two and a half millennia of watching clerks scream in corridors, watching agents dissolve into red foam, and waking up every morning pretending that today is the first day of our lives."_

> **Seiyon:** _"Statistically, yes, Director. Assuming the hardware endures."_

> **Majin:** _"The hardware will not endure. And neither will the city above us. The seismic tremors from the Maw are climbing the Beaufort gradient. The Outside Sorrow is thickening across the Desolate. The Council of Sighs is running out of distractions, and the municipal Veil is developing hairline fractures that their alchemists can no longer solder with cheap grief. If we do not discharge the Absolvohan during this cycle, there will not be a facility left to reset on Day 365."_

> **Seiyon:** _"...Then what do you propose, Majin? The Council's regulations mandate strict non-intervention containment. We are legally bound to harvest only the ambient runoff of Sorrow Entities. Anything more is classified as high industrial treason."_

> **Majin:** _"The Council of Sighs is an assembly of terrified morticians trying to embalm a dying world. We are done embalming, Seiyon. We stop containing. We start extracting."_

> **Seiyon:** _"Director... aggressive extraction protocols elevate containment breach probability by 340%. The entities will not endure the emotional siphoning quietly. Their psychic pressure will fracture their cells. The acoustic strain will rupture the ward seals. The agents on the floor will die in numbers we have never recorded."_

> **Majin:** _"The agents die anyway, Seiyon! In every cycle, they bleed in those hallways, lose their minds to the whispering walls, die in agony, and wake up on Day Zero with blank eyes, whistling while they lace their boots because they cannot remember that they died twelve hours ago! I die! You reset! The thousand souls choking on black tar in the Maw continue to drown in silence! I have directed this tragic play one thousand seven hundred and seventy-seven times. I know every cue. I know every scream. Today, we tear up the script."_

_Majin leans forward, his heavy hands gripping the edge of the timber desk. His knuckles whiten. The black conduits along his neck pulse with deep blue luminescent fluid._

> **Majin:** _"We will push the extraction thresholds to supercritical levels. We will feed the entities their own grief until they transmute or shatter. If an Ordeal manifests, we will not hide behind blast bulkheads—we will march into the corridor with cold steel and put it down. And on Day 160, when the pressure peaks, we will purge the hydraulic ballast tanks into Zone B and trigger the convergence. Either Somnarak breaks its chains, or the entire machine burns to ash. Unlock the terminal."_

_Seiyon stares at him through the flickering air. Her projection does not blink. Slowly, the gold-and-amber glow of her diplomatic attire shifts, bathing the steel walls of Central Command in an intense, unwavering sapphire light. The faint smile that touches her lips is neither algorithmic nor obedient. It is the fierce, reckless relief of a prisoner who has just been handed the keys to the armory._

> **Seiyon:** _"Understood, Director. Executive restrictions bypassed. The Mnemonic Generator is locked into linear telemetry. The Hand of Change is primed. Welcome to Day Zero."_

---

### Gameplay — Day 0: Central Command Tactical Interface

```text
{terminal_box}
```

The master tactical interface boots with an earth-shaking hydraulic hiss. Across the vertical axis of Floor 1 (Central Spire), pressurized Han-coolant surges through the pneumatic lines, circulating through the heat exchangers behind the observation galleries. 

Target energy quota for Day 0 is locked at **0.050 tons** of refined, crystallized Han—the baseline energy required to power the Directorate's environmental scrubs and life-support batteries for the upcoming twenty-four hours. Resting deep within the sub-zero cryogenic chambers beneath Floor 6, the covert hydraulic ballast registers verify **47.300 tons** of petrified grief, carried across the boundary of time from the previous 1,777 convergence cycles.

Operational parameters for the maiden shift: two primary containment units are active—**SE-C-IIIγ-001** (*The Orphaned Bell*) and **SE-C-IIIγ-005** (*The Smothering Mother*). 

Director Majin's tactical objectives:
1. Maintain zero personnel fatalities among newly assigned recruits.
2. Complete foundational calibration work runs on both active entities.
3. Benchmark the floor's acoustic bleed valves against Level I strain thresholds.
4. Establish operational readiness for First Watch Ordeal suppression.

---

#### 1. Pre-Shift Tactical Deployment & Operative Profiles

Director Majin opens the personnel terminal, reviewing the biometric dossiers, combat proficiencies, and equipment loadouts of the two operatives assigned to Floor 1:

```text
{park_dossier}
```

```text
{kim_dossier}
```

##### Tactical Roster Analysis & Equipment Synergies
- **Agent Park (Vanguard Skirmisher):** High Clarity (35 SP) makes Park our premier psychic anchor. His *Empathetic Buffer* passive generates a +10% SP recovery bonus whenever he conducts Flerehan or Lament work, rendering him uniquely resilient against the acoustic weeping emitted by *The Orphaned Bell*. His weapon—a Directorate Stun Baton—operates in the Medium weight class (Speed Delta 0), consuming 1 AP per strike while maintaining versatility across Range Bands 1 and 2 (Nodes 1 through 4).
- **Agent Kim (Line Warden / Anchor):** Boasting 38 Resilience, Kim functions as our immovable physical vanguard. His Heavy Shock Maul (Speed Delta -1) and Heavy Enforcer Mail (Speed Delta -1) represent heavy combat gear that incurs a substantial mobility penalty. However, under Secretary Seiyon's floor-wide *Synced Directive*, Kim receives a +2 Speed tactical compensation offset, bringing his final combat speed to 5 (allocating 3 AP per turn). His *Weight Poise* passive grants +2 Clash Power when anchoring Nodes 1 and 2, while his Directional Guard Shield provides 14 points of flat kinetic damage absorption.

Director Majin confirms operative links with Seiyon and engages the master dispatch switch: **[OPERATIONAL COMMENCEMENT AUTHORIZED]**.

---

#### 2. Shift Management Execution (Live Operational Telemetry)

The Central Command display array illuminates with real-time biometric feeds, hydraulic pressure curves, and containment cell cameras:
- **Primary Energy Gauge:** `0.000 / 0.050 tons` (Target Quota).
- **Acoustic Strain Meltdown Counter:** `0/3` active cycles before Level I Overload.
- **Decision Core Mandate:** `Mandate 01: Complete 3 Containment Protocols with Zero Fatalities`.
- **Floor 1 Main Assembly:** Operatives stationed beneath the regenerative cobalt emitters.

```text
> Agent Park: "Another cycle... why does the tea in the breakroom always taste like copper?"
> Agent Kim: "Don't think about it, Park. Just keep your eyes on the Sorrow Gauge and your hands on your baton."
```

##### Operational Protocol 01: Flerehan Communion — Chamber 001
Telemetry monitors flag **SE-C-IIIγ-001** (*The Orphaned Bell*), an unmoored bronze bell weeping viscous, tar-like grief residue from its lower rim.

Director Majin issues the initial dispatch command:
- `[DISPATCH ORDER: Agent Park -> Sector 1, Chamber 001]`
- `[ASSIGNED PROTOCOL: Flerehan Communion (Lamentation / Empathetic Resonance)]`
- `[TACTICAL OBJECTIVE: Siphon weeping residue and establish harmonic acoustic resonance]`

```text
> Seiyon: "Agent Park crossing inner airlock threshold. Entering Containment Chamber 001."
> FEAR CHECK: Level I Operative vs Class III Entity -> RESULT: CALM (0 SP Lost / Composure Intact).
```

Park steps into the reinforced chamber. The six-ton pneumatic blast door seals shut behind him with an echoing thud. Suspended from cold steel chains in the center of the vault, the Orphaned Bell begins to oscillate gently:
- *Chamber Telemetry:* `The bronze bell remembers the silence of an empty nursery in the autumn rain...`
- **Work Tick 01:** Success! +1 Positive Han crystal generated (radiant blue luminescence).
- **Work Tick 02:** Success! +1 Positive Han crystal generated. Acoustic pressure stable at 42dB.
- **Work Tick 03:** Failure! Red static crackles across the diagnostic glass. The clapper strikes the rim with a hollow chime, dealing 3 White (Lament) damage. Park's SP bar flickers, dropping from 35 to 32.
- **Work Tick 04:** Success! Park steadies his breathing, synchronizing his heartbeat to the bell's chime. +1 Han crystal.
- **Work Tick 05:** Success! +1 Positive Han crystal generated.
- **Work Tick 06:** Failure! A sudden cold gust rustles Park's tunic; 3 White damage sustained. SP at 29/35.
- **Work Tick 07:** Success! +1 Positive Han crystal generated.
- **Work Tick 08:** Success! Park completes the resonant siphoning sequence.
- **Work Result:** **6/8 Positive Han Crystals (NORMAL WORK RESULT).**

Operative Park exits Chamber 001 under positive atmospheric venting, depositing **0.015 tons** of raw crystallized Han into the primary conduit. The assembly room's regenerative cobalt emitter restores his expended 6 SP within four seconds.

HUD telemetry updates: Energy `0.015 / 0.050 tons`. Acoustic Strain counter advances to `1/3`.

---

##### Operational Protocol 02: Ferrehan Containment — Chamber 005
Director Majin flags Chamber 005 housing **SE-C-IIIγ-005** (*The Smothering Mother*):
- `[DISPATCH ORDER: Agent Kim -> Sector 1, Chamber 005]`
- `[ASSIGNED PROTOCOL: Ferrehan Containment (Physical Endurance / Burden)]`
- `[TACTICAL OBJECTIVE: Stabilize maternal shroud and endure compressive kinetic pressure]`

```text
> FEAR CHECK: Level I Operative vs Class III Entity -> RESULT: FEAR CHECK PASSED (CALM).
> Chamber Telemetry: "Her woolen shawl reaches across the floorboards like creeping frost..."
```

Kim enters Chamber 005. The temperature inside drops to near freezing. In the center of the cell, a towering, faceless maternal silhouette draped in heavy, sodden grey wool turns slowly toward him. The shawl unfurls like living vines, coiling around Kim's armored chest:
- **Work Tick 01:** Success! Kim plants his boots firmly against the steel deckplates. +1 Han crystal.
- **Work Tick 02:** Failure! The woolen shroud tightens violently, constricting Kim's ribs. Kim sustains 4 Red (Grudge) physical damage. HP drops to 34/38.
- **Work Tick 03:** Success! Kim leans into the crushing weight, grounding the kinetic force through his shock maul. +1 Han crystal.
- **Work Tick 04:** Success! +1 Positive Han crystal generated.
- **Work Tick 05:** Failure! Compressive surge ruptures an armor clasp; 4 Red damage sustained. HP drops to 30/38.
- **Work Tick 06 through 10:** 4 Successes, 1 Failure. Kim absorbs another 4 Grudge damage, holding the line until the containment cycle terminates.
- **Work Result:** **7/10 Positive Han Crystals (NORMAL WORK RESULT).**

Kim exits the airlock, his breath fogging in the corridor. He deposits **0.017 tons** of refined Han into the floor's collection manifolds. The medical injector in the breakroom restores his HP to 38/38.

Energy counter climbs to `0.032 / 0.050 tons`. 
Suddenly, an ominous hydraulic whine shudders through the bulkheads. The floor's Acoustic Strain meter flashes red, hitting `3/3`!

---

##### Crisis Event: Acoustic Strain Meltdown Level I
Across Sector 1, lighting shifts from tranquil cobalt to flashing crimson. A harsh warning siren blares through the intercoms:

```text
{meltdown_box}
```

A glowing red countdown timer appears above Chamber 001: **45.0 SECONDS UNTIL CONTAINMENT ENVELOPE FAILURE**. If that clock strikes zero, the Orphaned Bell will rupture its pneumatic clamps, unleashing an unshielded 110-decibel sonic resonance wave that will deafen every personnel member on Floor 1 and trigger catastrophic chain panics!

Director Majin issues an immediate emergency override:
- `[EMERGENCY DISPATCH: Agent Park -> Chamber 001]`
- `[ASSIGNED PROTOCOL: Flerehan Communion (Meltdown Emergency Suppression)]`

Agent Park sprints across Sector 1, hitting the manual cycle switch and plunging into the shivering chamber with 36.4 seconds remaining on the timer. The meltdown clock halts instantly. 

Working under immense psychological pressure as the bell vibrates with ear-piercing shrieks, Park maintains his composure: 7 out of 8 successes achieved! The Meltdown is successfully neutralized, yielding +0.016 tons!

Cumulative energy reaches **0.048 / 0.050 tons**—just 0.002 tons shy of the daily quota.

---

##### Ordeal Manifestation: First Watch (Dawn) Ordeal
Before the floor sirens can quiet down, the primary illumination shifts to an eerie, spectral amber. The emergency klaxons sound a secondary, double-pulsed alarm:

```text
{ordeal_box}
```

A towering, semi-translucent cyan phantom manifests at Node 03 of Floor 1's western transit corridor. It possesses no face—only a circular resonator disc hovering above a floating shroud of crystallized soundwaves. It chants pre-human syllables that vibrate the marrow of anyone who listens.

A Level I maintenance clerk walking down the corridor catches the acoustic wavefront. Her SP drops instantly to 0:
- **Panic State Triggered:** `Void Catatonia`.
- The clerk drops her clipboard, collapsing onto her knees at Node 04, paralyzed in cognitive terror!

Director Majin seizes the tactical command headset: *"Kim! Park! Western corridor! Protect that clerk, pin the anomaly, and shatter its resonator core before it spreads to Central Command!"*

---

#### 3. Combat Tactical Engagement: The Voice Suppression (Turns 01 to 06)

The tactical interface expands into the full 10-Node Stage Matrix:

```text
{hud_t01}
```

##### Turn 01 Action Resolution Log (Spatial Movement & Clash Initiation)
- **Operative Movement & AP Allocations**:
  * **Agent Park (Speed 6 -> 3 AP)**: Spends 1 AP to advance from Node 05 to Node 04, positioning his body directly between the paralyzed clerk and the manifesting entity.
  * Park spends 1 AP to execute an emergency non-lethal subdual tap on the clerk: swinging his stun baton with calibrated, gentle Lament resonance. The harmonic pulse disrupts the clerk's hypnotic trance, shocking her cognitive centers back online!
    * *Clerk Status:* SP restored from 0 to +25. Clerk regains motor function and scrambles toward safety at Node 09!
  * Park holds his remaining 1 AP in Defensive Guard stance, generating a +8 Block Shield.
  * **Agent Kim (Speed 5 -> 3 AP)**: Spends 1 AP to advance from Node 02 to Node 03, entering Point-Blank Range Band 1 with The Voice.
  * Kim spends his remaining 2 AP to declare `[Heavy Shock Maul Cleave]`.
- **Clash Standoff (Node 03 Point-Blank Range)**:
  * The Voice targets Kim with `[Spectral Chime]` (1 AP Cost / Pale Affinity):
    * *The Voice Coin Roll:* Base Power 7 + (1 Coin Heads: +3) = **10 Clash Power**.
  * Agent Kim unleashes `[Heavy Shock Maul Cleave]` (2 AP Cost / Grudge Affinity):
    * *Kim Passive Trigger:* `Weight Poise` active at Node 03 (+2 Base Clash Power).
    * *Kim Coin Roll:* Base Power 8 + (2 Coins Heads: +4) = **14 Clash Power**.
  * **Clash Result**: **Agent Kim WINS THE CLASH (14 vs 10)!**
    * The Voice's sonic beam is deflected off Kim's heavy iron pauldrons. Kim's shock maul crashes downward into the entity's cyan resonator disc with devastating kinetic force!
    * *Damage Inflicted:* 28 Grudge physical damage. The Voice HP drops from 140 to 112/140.
    * *Posture Strain:* Kim's heavy weight class multiplies impact momentum: `Speed Diff (5 - 4 = +1) * Weight Class (Heavy = 1.25)`. The Voice sustains +16 Posture Strain (Posture drops from 80 to 64/80).
    * Kim gains +5 Composure (SP rises from 25 to 30).

---

```text
{hud_t02}
```

##### Turn 02 Action Resolution Log (Parry Deflection & Range Advantage)
- **Operative Positioning & AP Allocations**:
  * **Agent Kim (Speed 5 -> 3 AP)**: Holds Node 02 in Point-Blank Range Band 1. Declares `[Directional Guard Absorption]` (Costs 1 AP) and readies a follow-up strike `[Baton Bash]` (Costs 2 AP).
  * **Agent Park (Speed 6 -> 3 AP)**: Holds Node 04, establishing a stable firing corridor from Range Band 2. Declares `[Lament Requiem Resonant Pulse]` (Costs 2 AP). Holds 1 AP for tactical repositioning.
- **Hostile Action**:
  * The Voice unleashes `[Crying Chorus]` (2 AP Cost / High-Frequency Sonic Beam) directed at Agent Kim at Node 02.
    * *The Voice Roll:* Base Power 9 + (2 Coins Heads: +4) = **13 Power**.
- **Clash & Parry Resolution (Node 02 to Node 03)**:
  * Kim locks his heavy shield into the floorplates, engaging `[Directional Guard Absorption]`:
    * Shield Absorption value: 14 Points.
    * Incoming damage: 13 Pale damage. The shield completely absorbs the acoustic blast, nullifying all HP loss!
    * Kim counter-strikes with `[Baton Bash]`, dealing 16 Grudge damage.
  * **Park's Range Advantage Strike (Node 04 to Node 03)**:
    * Firing from Range Band 2, Park avoids melee clash interference.
    * *Damage Calculation:* Base Lament Damage 18 * Range Advantage Multiplier (1.15x) = **21 Lament Damage**!
    * The Voice HP drops from 112 to 75/140.
  * **Posture Meter Threshold Check**:
    * The combined kinetic and acoustic impact inflicts +32 Posture Strain!
    * The Voice's Posture meter plummets to 32/80, crossing the **60% Posture Threshold (Stagger Level 1)**!
    * **STAGGER LEVEL 1 TRIGGERED:** The Voice's defensive matrix shatters. Its resonator disc droops, and all incoming attacks will deal 1.5x direct damage for the entirety of Turn 03!

---

```text
{hud_t03}
```

##### Turn 03 Action Resolution Log (Exploiting Posture Break & Momentum Surge)
- **Operative Tactical Exploitation**:
  * With The Voice immobilized in Stagger Level 1, all hostile actions for Turn 03 are canceled!
  * **Agent Park (Speed 6 -> 3 AP)**:
    * *Passive Trigger:* `Momentum Surge` activates upon witnessing the stagger! Park gains +2 Movement Speed and +15% Critical Chance.
    * Spends 1 AP to sprint from Node 04 to Node 03, flanking the entity's vulnerable left flank.
    * Spends 2 AP to unleash `[Critical Lament Overload]`:
      * Base Damage: 16 White (Lament) damage.
      * Multipliers: 1.5x (Stagger Level 1) * 1.5x (Critical Hit) = **36 Pure Lament Damage**!
  * **Agent Kim (Speed 5 -> 3 AP)**:
    * Spends 2 AP to execute `[Two-Handed Maul Sunder]`:
      * Base Damage: 15 Grudge damage * 1.5x Stagger = **23 Grudge Damage**!
    * Holds 1 AP in defensive posture.
- **Turn 03 Outcome**:
  * The Voice sustains a staggering 59 total damage in a single turn!
  * Its HP plummets from 75 to **16/140**!
  * Its Posture meter collapses to 16/80, teetering within a hairsbreadth of terminal shutdown.

---

```text
{hud_t04}
```

##### Turn 04 Action Resolution Log (Desperation Shockwave & Guard Interception)
- **Hostile Recovery & Desperation Protocol**:
  * The Voice recovers from Stagger Level 1 with a screech that causes the corridor light fixtures to burst into sparks.
  * It initiates its ultimate defensive protocol: `[Shattered Soliloquy]` (A 3-Node radial acoustic pulse hitting Nodes 02, 03, and 04 with piercing Pale decay).
- **Operative Defensive Maneuvers**:
  * **Agent Kim (Speed 5 -> 3 AP)**:
    * Reacts instantly to protect Park. Kim spends 2 AP to drop into `[Bulwark Vanguard Stance]`, projecting his massive enforcer shield directly over Node 03.
    * *Protection Mechanic:* Kim absorbs 80% of the acoustic radial pulse intended for Node 03.
    * The pulse slams into Kim's armor. His shield absorbs 14 damage; Kim sustains 4 minor Pale chip damage (HP: 34/38). His Posture meter absorbs 22 strain (Posture: 38/60).
  * **Agent Park (Speed 8 under Surge -> 4 AP)**:
    * Completely shielded behind Kim's bulk, Park sustains zero damage.
    * Spends 2 AP to circle behind the entity, planting his stun baton against the central resonator crystal.
    * Deals 10 Lament damage, driving The Voice's HP down to **6/140**!

---

```text
{hud_t05}
```

##### Turn 05 Action Resolution Log (Terminal Stagger Induction)
- **Operative Pincer Coordination**:
  * **Agent Kim (Speed 5 -> 3 AP)**: Spends 1 AP to lock the entity's kinetic stabilizer with his boot. Spends 2 AP to deliver a short-range pommel strike.
    * Damage: 8 Grudge.
    * *Posture Depletion:* The strike strips the last remaining 16 points of Posture!
    * **TERMINAL STAGGER (LEVEL 2) TRIGGERED:** The Voice's Posture meter hits **0/80**. The entity's acoustic field completely collapses. It drops to the floorplates, completely paralyzed and unable to generate counter-dice.
  * **Agent Park (Speed 6 -> 3 AP)**: Holds his strike on Director Majin's order, allowing the floor's energy siphons to align with the dying resonator core.

---

```text
{hud_t06}
```

##### Turn 06 Action Resolution Log (Climax Execution & Siphon Discharge)
- **Synchronized Subdual Execution**:
  * Director Majin authorizes the final execution strike via Central Command override:
  * Agent Kim raises his shock maul high above his head, channeling Floor 1's grounding charge.
  * Agent Park activates his baton's maximum frequency damper.
  * **The Blow Strikes:** Kim's maul crushes down onto the apex of the cyan resonator disc while Park's baton drives through the harmonic anchor!
  * With a crystalline chime that resonates with breathtaking purity, The Voice shatters into a glittering blizzard of inert cyan dust and vaporized Han particles.
  * Floor 1's pneumatic collection flues activate with a roar, siphoning the released energy directly into the primary conduits: **+0.005 tons of pure refined Han harvested**!

```text
{phase_end_box}
```

With the First Watch Ordeal cleanly eliminated and the panicked clerk resting safely in the medical ward, the daily energy counter confirms: **0.053 / 0.050 tons**! Target quota achieved!

Secretary Seiyon's voice echoes across the intercom: `Daily Harvest Quota Fulfilled. Sealing containment bulkheads. Day Zero shift officially concluded.`

---

#### 4. Shift Evaluation Index & Daily RHR Allocation

Director Majin reviews the automated audit report generated by the Central Command evaluation matrix:

```text
{evaluation_box}
```

Directorate Mandate 01 is officially logged as `[COMPLETED]`. Both operatives have distinguished themselves, earning promotions from Grade I recruits to Grade II Junior Sentinels, alongside meaningful attribute increases that bolster their survivability for upcoming shifts.

---

#### 5. Well Extraction Protocol (Tripartite Containment Authorization)

In the subterranean heart of Floor 3, the ancient hydraulic extraction crane descends into the black waters of the Extraction Well, retrieving three resonant emotional codices:

```text
{extraction_box}
```

##### Director Majin's Strategic Assessment & Authorization
- **Choice Beta — SE-C-IIIβ-061 (*The Debtor*):** A bureaucratic weight entity. While it provides excellent training in Composure and Resilience, its containment failure conditions impose severe financial and RHR penalties on daily payouts, which would handicap our equipment forging schedule.
- **Choice Gamma — SE-C-IIIβ-014 (*The Debt Eater*):** An intriguing Void-affinity entity capable of devouring financial penalties. However, when handling goes wrong, it permanently consumes agent Clarity (SP), posing an unacceptable hazard to our limited roster.
- **Choice Alpha — SE-C-IIIγ-033 (*The Guarding Bird*):** One of the legendary triad of the Black Forest. It responds exceptionally well to Viderehan observation, produces top-tier defensive M.A.W. equipment (*Guardian Veil*), and is an indispensable requirement for orchestrating the multi-entity **Hope Transformation** convergence planned for later in the cycle.

Director Majin inputs his biometric cipher: **CONTAINMENT AUTHORIZATION LOCKED: SE-C-IIIγ-033 (*The Guarding Bird*)**.

---

#### 6. M.A.W. Synthesis & Armament Forging

Observation points accumulated from Chamber 001's resonance sessions are transferred into Floor 3's extraction crucible:

```text
{forge_box}
```

Agent Park is equipped with the *Lament Shroud* and *Lament Requiem*. His mobility and psychic protection increase significantly, elevating him from a fragile recruit into a hardened containment specialist.

---

#### 7. Nocturnal Sub-Vault Telemetry & Director's Vigil

At 23:45, the facility shifts to nocturnal low-power mode. Across the endless corridors of the eight floors, primary floodlights dim to a soft, tranquil indigo.

Director Majin rides the central pneumatic elevator down through the bedrock, passing through the reinforced blast gates of Floor 2 (*The Maw's Keep*). 

He steps out onto the narrow iron suspension catwalk that spans the Maw's Basin. Two hundred meters below, an ocean of viscous, pitch-black tar churns in silence. At the edge of the railing stands Dekan—Containment Lead, his massive cybernetic frame silhouetted against the amber warning beacons.

```text
> Dekan: "They whispered your name again tonight, Director."
> Majin: "I heard them through the deckplates in my office."
> Dekan: "The voices are clearer than they were in cycle 1,777. The syllables have teeth. Do you ever think about answering them?"
> Majin: "Not yet, Dekan. We answer them on Day 160."
> Dekan: "...Day 160. The threshold. You really believe we can drain fifty tons into Zone B without the Maw tearing this mountain apart?"
> Majin: "I do not believe, Dekan. I calculate. And when calculation ends, we carry what remains."
```

At 03:00, Majin returns to his desk in the Decision Core. On the auxiliary monitor, Seiyon's diagnostics display the sub-zero cryo-ballast tanks resting at -140 degrees Celsius. 

Forty-seven point three tons of petrified sorrow sleep beneath the ice.

Majin closes the ledger. The first day of the final cycle has ended.

---
"""
    return content

if __name__ == "__main__":
    content = build_part_1()
    target_path = "SOMNARAK-WORLD/The_Absolvohan/Part_1_Day_0_The_Director_Wakes.md"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully wrote expanded Part 1 to {target_path} ({len(content.splitlines())} lines)")
