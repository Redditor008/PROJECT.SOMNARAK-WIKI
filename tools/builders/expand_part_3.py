#!/usr/bin/env python3
"""
tools/expand_part_3.py
Expands Part 3 (Days 29 to 49) into an exhaustive operational chronicle:
- Replaces Turns 02-06 summaries on Day 29, Day 31, Day 36, Day 41, and Day 49 with full turn-by-turn combat logs.
- Inserts Day 45 (Avian Triad Calibration & Violet Second Watch Ordeal).
- Enforces 100% box symmetry and dual-environment typography.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

# --- DAY 29 TURNS 02-06 ---
def get_day_29_expanded():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 2 PRIMARY JUNCTION CORRIDOR]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MONOLITH][MELLDA]      [PARK]          [KIM]                   [DEKAN]",
        "---",
        "- Node 01: Grieving Monolith (Compressive Basalt Core / Posture 112/160)",
        "- Node 02: Border Lead Mellda (Point-Blank Band 1 / Mantlet Locked)",
        "- Node 04: Agent Park (Range Band 2 / Resonant Requiem Firing)",
        "- Node 06: Agent Kim (Range Band 3 / Concentrated Carbine Aimed)",
        "- Node 10: Containment Lead Dekan (Observation Catwalk / Band 5)",
        "---",
        "- Mellda   : Spd 5 -> 3 AP | HP 180/180 | SP +30 | Posture 85/85",
        "- Agent Park: Spd 6 -> 3 AP | HP 110/110 | SP +25 | Posture 55/55",
        "- Agent Kim : Spd 5 -> 3 AP | HP 105/105 | SP +20 | Posture 65/65",
        "- Monolith : Spd 3 -> 2 AP | HP 258/320  | Posture 112/160 (Stagger 1: 96)"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MONOLITH]      [PARK]                  [KIM]                   [DEKAN]",
        "        [MELLDA]",
        "---",
        "- Node 01: Grieving Monolith (STAGGER LEVEL 1 ACTIVE / 1.5x DAMAGE)",
        "- Node 02: Border Lead Mellda (Golden Arm-Blade Driving into Core)",
        "- Node 03: Agent Park (Advancing with Momentum Surge / +2 Speed)",
        "- Node 06: Agent Kim (Coordinating Stasis Harpoon Arc)",
        "---",
        "- Mellda   : Spd 5 -> 3 AP | HP 180/180 | SP +30 | Posture 85/85",
        "- Agent Park: Spd 8 -> 4 AP [SURGE] | HP 110/110 | SP +25 | Posture 55/55",
        "- Agent Kim : Spd 5 -> 3 AP | HP 105/105 | SP +20 | Posture 65/65",
        "- Monolith : Spd 0 -> 0 AP | HP 148/320  | Posture 48/160 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — TECTONIC TOLL DESPERATION RESURGENCE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MONOLITH][MELLDA][PARK]                [KIM]                   [DEKAN]",
        "---",
        "- Node 01: Grieving Monolith (Recovered / Channeling Tectonic Toll)",
        "- Node 02: Border Lead Mellda (Directional Guard Absorption Active)",
        "- Node 03: Agent Park (Sheltered behind Mellda's Mantlet)",
        "- Node 06: Agent Kim (Locking Stasis Disruption Beam)",
        "---",
        "- Mellda   : Spd 5 -> 3 AP | HP 168/180 | SP +28 | Posture 62/85",
        "- Agent Park: Spd 6 -> 3 AP | HP 110/110 | SP +25 | Posture 55/55",
        "- Agent Kim : Spd 5 -> 3 AP | HP 105/105 | SP +20 | Posture 65/65",
        "- Monolith : Spd 3 -> 2 AP | HP 102/320  | Posture 28/160 [FRACTURED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MONOLITH][MELLDA][PARK]                [KIM]                   [DEKAN]",
        "---",
        "- Node 01: Grieving Monolith (TERMINAL STAGGER / POSTURE 0/160 / 2.0x DMG)",
        "- Node 02: Border Lead Mellda (Severing Basalt Anchors)",
        "- Node 03: Agent Park (Priming Requiem Climax Resonance)",
        "- Node 06: Agent Kim (Discharging Piercing Void Bolt)",
        "---",
        "- Mellda   : Spd 5 -> 3 AP | HP 168/180 | SP +28 | Posture 62/85",
        "- Agent Park: Spd 6 -> 3 AP | HP 110/110 | SP +25 | Posture 55/55",
        "- Agent Kim : Spd 5 -> 3 AP | HP 105/105 | SP +20 | Posture 65/65",
        "- Monolith : Spd 0 -> 0 AP | HP 38/320   | Posture 0/160 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SILT]  [MELLDA][PARK]                 [KIM]                   [DEKAN]",
        "---",
        "- Node 01: Grieving Monolith (Pulverized into River Silt / Purified)",
        "- Node 02: Border Lead Mellda (Retracting Threshold Vow Blade)",
        "- Node 03: Agent Park (Channeling Positive Han into Conduits)",
        "- Node 06: Agent Kim (Lowering Carbine / Confirming Zero Casualties)",
        "---",
        "- Mellda   : Spd 5 -> 3 AP | HP 168/180 | SP +35 | Posture 75/85",
        "- Agent Park: Spd 6 -> 3 AP | HP 110/110 | SP +30 | Posture 55/55",
        "- Agent Kim : Spd 5 -> 3 AP | HP 105/105 | SP +25 | Posture 65/65",
        "- Monolith : HP 0/320 [PURIFIED] | +0.020 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Range Advantage & Stagger Build)
- **Coordinated Tripartite Fire**:
  * **Border Lead Mellda (Speed 5 -> 3 AP)**: Holds Node 02 in Point-Blank Band 1. Spends 2 AP to execute `[Threshold Vow Kinetic Parry]`, anchoring her shield mantlet against the stone slab.
  * The Monolith channels `[Basalt Fissure Crash]` directed at Node 02 (Base 8 + 2 Coins = 12 Power). Mellda wins clash (14 vs 12), turning the blow aside!
  * **Agent Park (Speed 6 -> 3 AP)**: Firing from Node 04 (Range Band 2):
    * Spends 2 AP to channel `[Lament Requiem Resonant Smash]`. Range Band advantage (+15%) and Lament vulnerability trigger: deals **38 Pure Lament Damage**!
  * **Agent Kim (Speed 5 -> 3 AP)**: From Node 06 (Range Band 3), delivers a 3-round piercing burst for **24 Void damage**.
  * Monolith HP drops from 294 to **232/320**!
  * Combined Posture strain inflicts +38 points. Posture drops from 112 to **74/160**, breaching the **60% Posture Threshold (96 Points)**!
  * **STAGGER LEVEL 1 TRIGGERED!** The basalt slab cracks down its center axis; all incoming attacks will deal 1.5x direct damage in Turn 03!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Vanguard Overload (1.5x Direct Damage)**:
  * With the monolith staggered, its action dice are canceled for Turn 03.
  * **Agent Park**: Passive `Momentum Surge` activates upon witnessing the stagger! Gains +2 Speed and +15% Critical Chance. Spends 1 AP to sprint to Node 03 and 2 AP to unleash `[Critical Lament Overload]`:
    * Deals **54 Direct Lament Damage**!
  * **Border Lead Mellda**: Spends 2 AP to drive *Threshold Vow* deep into the central fissure, dealing **30 Grudge damage**!
  * Monolith HP plummets from 232 to **148/320**!
  * Posture collapses to **28/160**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Desperation Tectonic Toll)
- **Hostile Recovery & Desperation Counter-Surge**:
  * The Monolith recovers from Stagger Level 1, vibrating with a deep sub-bass roar: `[Tectonic Toll]` (a 3-node compressive seismic wave hitting Nodes 01, 02, and 03).
  * **Border Lead Mellda**: Deploys `[Directional Guard Absorption]`, locking her golden arm-blade into the floorplates to form an impenetrable kinetic wall. She absorbs 28 points of physical shock, taking only 12 chip damage (HP: 168/180) and completely shielding Park behind her!
  * **Agent Kim (Speed 5 -> 3 AP)**: From Range Band 3, spends 2 AP to fire `[Stasis Disruption Harpoon]`, piercing the monolith's resonance core and disrupting the vibration!
  * Monolith HP falls to **102/320**! Posture drops to **14/160**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Pincer Lockdown**:
  * Border Lead Mellda executes `[Threshold Severance Strike]`, stripping the final 14 points of Posture!
  * **TERMINAL STAGGER LEVEL 2 TRIGGERED!** Monolith Posture hits **0/160**. The massive basalt slab splits into two unaligned halves, collapsing helpless onto the deckplates (2.0x direct damage active)!
  * Agent Kim fires a suppressive void round into the cleft, dealing **32 Void damage** (HP: 38/320).

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Siphon)
- **Synchronized Subdual Execution**:
  * Agent Park steps onto the fractured pedestal, raising the Lament Requiem high: `[Requiem Climax: Choral Absolution]`.
  * The acoustic hammer strikes the exposed core crystal with blinding resonance. The entire stone slab pulverizes into inert river silt and shimmering Han mist!
  * Floor 2's drainage flues siphon the harvest: **+0.020 tons of refined Han secured**!
"""

# --- DAY 45 GENERATOR ---
def generate_day_45():
    t_box = make_box("REVERIE DIRECTORATE — CENTRAL COMMAND TERMINAL", [
        "FACILITY MANAGEMENT INTERFACE: DAY 45 SHIFT",
        "ENERGY HARVEST QUOTA  : 0.160 TONS // CURRENT HARVEST: 0.000 TONS",
        "COVERT BALLAST RESERVE : 49.100 TONS [HYDRAULIC CRYO-VAULTS]",
        "ACTIVE CONTAINMENT    : SE-001, 005, 014, 025, 031, 032, 033",
        "TRIAD INTEGRATION     : THE THREE BIRDS OF THE BLACK FOREST ACTIVE"
    ])

    roster_box = make_box("DEPLOYED ROSTER: DAY 45 TRIAD SYNCHRONIZATION", [
        "AGENT & RATING        | STATS, GEAR & FOUR P-FRAMEWORK SPEC",
        "----------------------+-----------------------------------------------",
        "Agent Park (Grade V)  | HP 68 | SP 75 | Work 62 | Speed 6 (3 AP + 1 Move)",
        "Senior Skirmisher     | M.A.W.-W: Lament Requiem (Medium / 1 AP)",
        "Floor 5 Assigned      | Suit: Lament Shroud (Light / Spd +1) | Halo Gift",
        "                      | Posture: 65/65 | Parry: 16 Power | Pass: Momentum Surge",
        "                      | Panic Typology: Despair (SP <= -35)",
        "----------------------+-----------------------------------------------",
        "Border Lead Mellda    | HP 190| SP 80 | Work 65 | Speed 6 (3 AP + 1 Move)",
        "Floor 5 Decision Core | M.A.W.-W: Threshold Vow (Sacred Blade / 2 AP)",
        "Bulwark Commander     | Suit: Threshold Coat (Heavy / Spd 0 under Aura)",
        "                      | Posture: 95/95 | Guard: 22 Absorb | Pass: Iron Perimeter",
        "                      | Panic Typology: Berserk (SP <= -40)",
        "----------------------+-----------------------------------------------",
        "Agent Hwang (Grade V) | HP 58 | SP 70 | Work 64 | Speed 6 (3 AP)",
        "Senior Scribe         | M.A.W.-W: Blessed Scalpel (Void / Light / 1 AP)",
        "Floor 4 Assigned      | Suit: White Scribe Robe (Light / Spd +1)",
        "                      | Posture: 55/55 | Parry: 15 Power | Pass: Scribe Focus",
        "                      | Panic Typology: Wandering (SP <= -30)"
    ])

    ordeal_box = make_box("TACTICAL DOSSIER: VIOLET NOON ORDEAL SUPPRESSION", [
        "DESIGNATION           : THE PIERCING HAND (VIOLET NOON)",
        "CLASSIFICATION        : VIOLET (ALL-AFFINITY) SECOND WATCH ENTITY",
        "INTRUSION POINT       : FLOOR 5 BORDER OBSERVATION GATE (NODE 02)",
        "HOSTILE PARAMETERS    : HP 240/240 | Posture 120/120 | Speed 5 (3 AP)",
        "ATTACK AFFINITY       : Violet (Pure Disruption / Prismatic Decay)",
        "AFFINITY VULNERABILITY: Void (Pierce: 1.5x) & Lament (White: 1.25x)",
        "SPECIAL THREAT        : Dimensional reach allows attacks across 4 nodes",
        "TACTICAL ORDERS       : ANCHOR AT NODE 02; BREAK FINGERS WITH SCALPEL"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 5 BORDER OBSERVATION GATE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [HAND]  [MELLDA][PARK]  [HWANG]                         [MAJIN]",
        "---",
        "SPATIAL RANGES & POSITIONS:",
        "- Node 02: Piercing Hand (Dimensional Rift Ingress Epicenter)",
        "- Node 03: Border Lead Mellda (Frontline Bulwark / Range Band 1)",
        "- Node 04: Agent Park (Vanguard Skirmisher / Range Band 2)",
        "- Node 05: Agent Hwang (Void Scribe / Range Band 3)",
        "- Node 10: Director Majin & Seiyon Command Terminal (Band 5)",
        "---",
        "OPERATIVE STATUS & RESOURCE POOLS:",
        "- Mellda      : Spd 6 -> 3 AP | HP 190/190 | SP 80/80 | Posture 95/95",
        "- Agent Park  : Spd 6 -> 3 AP | HP 68/68   | SP 75/75 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 58/58   | SP 70/70 | Posture 55/55",
        "- Piercing Hand: Spd 5 -> 3 AP | HP 240/240 | Posture 120/120"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — SHATTERING THE CRYSTALLINE DIGITS]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [HAND]  [MELLDA][PARK]  [HWANG]                         [MAJIN]",
        "---",
        "- Node 02: Piercing Hand (Posture 78/120 / Thumb Joint Severed)",
        "- Node 03: Border Lead Mellda (Parrying Prismatic Beam)",
        "- Node 04: Agent Park (Lament Requiem Resonant Wave Firing)",
        "- Node 05: Agent Hwang (Blessed Scalpel Precision Incision)",
        "---",
        "- Mellda      : Spd 6 -> 3 AP | HP 182/190 | SP 80/80 | Posture 82/95",
        "- Agent Park  : Spd 6 -> 3 AP | HP 68/68   | SP 75/75 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 58/58   | SP 70/70 | Posture 55/55",
        "- Piercing Hand: Spd 4 -> 2 AP | HP 178/240 | Posture 78/120 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [HAND]          [PARK]                                  [MAJIN]",
        "        [MELLDA][HWANG]",
        "---",
        "- Node 02: Piercing Hand (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 02: Border Lead Mellda (Cleaving Palm Joint)",
        "- Node 03: Agent Hwang (Driving Scalpel into Rift Tendon)",
        "- Node 04: Agent Park (Momentum Surge Primed / +2 Speed Next Turn)",
        "---",
        "- Mellda      : Spd 6 -> 3 AP | HP 182/190 | SP 80/80 | Posture 82/95",
        "- Agent Park  : Spd 6 -> 3 AP | HP 68/68   | SP 75/75 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 58/58   | SP 70/70 | Posture 55/55",
        "- Piercing Hand: Spd 0 -> 0 AP | HP 98/240  | Posture 32/120 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — PRISMATIC RIFT REACTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [HAND]  [MELLDA][PARK]  [HWANG]                         [MAJIN]",
        "---",
        "- Node 02: Piercing Hand (Recovered / Channeling Prismatic Spire)",
        "- Node 03: Border Lead Mellda (Directional Guard Absorption)",
        "- Node 04: Agent Park (Spd 8 / AP 4 / Rapid Choral Pulse)",
        "- Node 05: Agent Hwang (Void Harpoon Readied)",
        "---",
        "- Mellda      : Spd 6 -> 3 AP | HP 174/190 | SP 76/80 | Posture 68/95",
        "- Agent Park  : Spd 8 -> 4 AP [SURGE] | HP 68/68 | SP 75/75 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 58/58   | SP 70/70 | Posture 55/55",
        "- Piercing Hand: Spd 5 -> 3 AP | HP 48/240  | Posture 16/120 [UNSTABLE]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [HAND]                                                  [MAJIN]",
        "        [MELLDA][PARK]  [HWANG]",
        "---",
        "- Node 02: Piercing Hand (TERMINAL STAGGER / POSTURE 0/120 / 2.0x DMG)",
        "- Node 02: Border Lead Mellda (Pinning Wrist Plate to Bedrock)",
        "- Node 03: Agent Park (Driving Lament Hammer into Knuckles)",
        "- Node 04: Agent Hwang (Executing Void Suture Strike)",
        "---",
        "- Mellda      : Spd 6 -> 3 AP | HP 174/190 | SP 76/80 | Posture 68/95",
        "- Agent Park  : Spd 6 -> 3 AP | HP 68/68   | SP 75/75 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 58/58   | SP 70/70 | Posture 55/55",
        "- Piercing Hand: Spd 0 -> 0 AP | HP 12/240  | Posture 0/120 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [MIST]  [MELLDA][PARK]  [HWANG]                         [MAJIN]",
        "---",
        "- Node 02: Piercing Hand (Dissolved into Prismatic Violet Fog)",
        "- Node 03: Border Lead Mellda (Checking Border Perimeter Seals)",
        "- Node 04: Agent Park (Collecting Pure Refined Reagents)",
        "- Node 05: Agent Hwang (Sealing Dimensional Rift Fissure)",
        "---",
        "- Mellda      : Spd 6 -> 3 AP | HP 174/190 | SP 80/80 | Posture 80/95",
        "- Agent Park  : Spd 6 -> 3 AP | HP 68/68   | SP 75/75 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 58/58   | SP 70/70 | Posture 55/55",
        "- Piercing Hand: HP 0/240 [PURIFIED] | +0.018 TONS REFINED HAN HARVESTED"
    ])

    eval_box = make_box("END-OF-DAY PERFORMANCE EVALUATION: DAY 45", [
        "METRIC                 | TARGET QUOTA   | REALIZED PERFORMANCE",
        "-----------------------+----------------+---------------------",
        "Han Energy Harvested   | 0.160 Tons     | 0.168 Tons [MET]",
        "Containment Breaches   | 0 Breaches Max | 0 Breaches [CLEARED]",
        "Personnel Casualties   | 0 Fatalities   | 0 Fatalities [PERFECT]",
        "Violet Noon Suppressed | 1/1 Suppressed | 100% Rate [RESOLVED]",
        "Triad Resonance Sync   | 100% Stable    | HARMONIC BALANCED",
        "-----------------------+----------------+---------------------",
        "SHIFT PERFORMANCE GRADE: GRADE S (TRIAD HARMONIC MASTER)",
        "REAGENTS ACCUMULATED   : +32 RHR (REFINED HAN REAGENTS)",
        "OPERATIVE ADVANCEMENT  :",
        "- Agent Park  : +4 Clarity, +3 Resolve (Senior Vanguard)",
        "- Agent Hwang : +5 Composure, +3 Clarity (Senior Archivist)",
        "- Border Lead Mellda: +5 Resilience (Bulwark Commander)"
    ])

    extract_box = make_box("EXTRACTION WELL ARCHIVE: SELECT NEXT COMPANION", [
        "CHOICE ALPHA [SE-C-IIIg-081]:",
        "'A hollow saint weeping liquid gold into an iron chalice, praying",
        "for a congregation that never arrived.'",
        "---",
        "CHOICE BETA  [SE-C-IIIg-140]:",
        "'A weeping willow whose branches droop beneath the weight of",
        "unspoken farewells.'",
        "---",
        "CHOICE GAMMA [SE-C-Ia-008]:",
        "'The dark abyss where the thousand martyrs speak in unison",
        "beneath the black tar.'"
    ])

    forge_box = make_box("M.A.W. SYNTHESIS FORGING LOG — DAY 45", [
        "FORGE SPECIFICATION    | SLOT / PROPERTIES / PARAMETERS",
        "-----------------------+----------------------------------------------",
        "Whispering Needle      | Weapon: 5-8 Void (Light / Speed Delta +1)",
        "                       | Range Band 2-3 | 1 AP | Pierces +25% Armor",
        "Needle Veil Shroud     | Suit: Light Armor (Speed Delta +1)",
        "                       | Resist: 0.8 Grudge / 0.6 Lament / 0.6 Void",
        "Avian Eye Gift         | Eye Slot: +6 SP, +8% Critical Clash Power",
        "-----------------------+----------------------------------------------",
        "EQUIPMENT ALLOCATION   | BESTOWED UPON AGENT HWANG (VOID SPECIALIST)"
    ])

    content = f"""
### Day 45

### Story — Dialogue

> **Ayshuk:** _"Director. The three birds have begun to breathe together."_

> **Majin:** _"Telemetry?"_

> **Ayshuk:** _"Chambers 031, 032, and 033 are locked in tripartite harmonic resonance. When The Guarding Bird stretches its wings on Floor 2, The Weighting Bird tilts its scale on Floor 4, and The Whispering Bird flutters its small bronze beak on Floor 3. The acoustic bleed is zero. They are balancing each other's sorrow."_

> **Mellda:** _"They may be calm inside their chambers, Director, but the perimeter is trembling. A Violet Second Watch Ordeal is tearing through Floor 5's border gate. A dimensional hand—five meters across, forged of faceted crystal—is reaching into our transit corridor."_

> **Majin:** _"Deploy Park, Mellda, and Hwang to Gate 05. The birds have shown us how balance works. Show that rift what Directorate discipline means."_

---

### Gameplay — Day 45: Central Command Tactical Interface

```text
{t_box}
```

Shift parameters engaged for Day 45. Target energy quota rises to **0.160 tons** of pure refined Han. Covert hydraulic reserves beneath Floor 6 confirm **49.100 tons**—passing the critical ninety-eight percent mark toward our mid-cycle operational threshold.

Operational priorities for Day 45:
1. Maintain tripartite stabilization across Chambers 031, 032, and 033.
2. Intercept and suppress the Violet Second Watch Ordeal along Floor 5's outer gate.
3. Advance senior operative proficiencies using the Four P-Framework.

#### 1. Pre-Shift Tactical Deployment & Operative Profiles

```text
{roster_box}
```

Director Majin engages the Floor 5 border relays: **[DAY 45 OPERATIONAL SHIFT COMMENCED]**.

---

#### 2. Granular Work Type Management: Chamber 031 (The Whispering Bird)

Agent Hwang enters Chamber 031 for Viderehan observation:
- `[DISPATCH: Agent Hwang -> Floor 3, Chamber 031]`
- `[PROTOCOL: Viderehan Observation (Acoustic Calibration / Void Affinity)]`

```text
> Chamber Telemetry: "The small bird hops onto Hwang's shoulder, whispering old secrets..."
> Fear Check: Level V Senior Agent vs Class III Entity -> RESULT: ABSOLUTE CALM.
```

- **Work Tick 01–05:** 5 Successes. The small bronze bird pecks gently at Hwang's collar.
- **Work Tick 06:** Failure! A sudden sharp chirp deals 4 White (Lament) damage (SP: 66/70).
- **Work Tick 07–10:** 4 Successes.
- **Work Result:** **9/10 Positive Han Crystals (EXCELLENT WORK RESULT)!**
- Yield: **+0.028 tons** of refined Han lubricant extracted.

Energy meter climbs to `0.092 / 0.160 tons`.

---

#### 3. Ordeal Manifestation: Second Watch (Violet Noon) Suppression

At 14:40, the space outside Gate 05 shatters like crystalline glass:

```text
{ordeal_box}
```

A colossal, five-fingered arm composed of iridescent violet crystal protrudes from an open spatial fissure at Node 02, sweeping through the air with piercing dimensional decay!

```text
{hud_t01}
```

##### Turn 01 Action Resolution Log (Spatial Ingress & Bulwark Anchor)
- **Operative Movement & Clash Standoff**:
  * **Border Lead Mellda (Speed 6 -> 3 AP)**: Spends 1 AP to advance to Node 03, planting *Threshold Vow* in front of the rift. Declares `[Threshold Vow Kinetic Parry]` (Costs 2 AP).
  * The Piercing Hand declares `[Prismatic Sweep]` on Node 03 (Base 9 + 2 Coins = 13 Power).
  * Mellda's Roll:
    * *Passive Trigger:* `Iron Perimeter` (+2 Base Clash Power).
    * Mellda Roll: Base 11 + 2 Coins = **15 Power**!
  * **Clash Result**: **Mellda WINS THE CLASH (15 vs 13)!**
    * The arm-blade deflects the crystalline fingers, dealing 32 Grudge damage (HP: 208/240) and inflicting +22 Posture Strain (Posture: 98/120).
  * **Agent Hwang (Speed 6 -> 3 AP)**: From Node 05 (Range Band 3), strikes with `[Blessed Scalpel Void Beam]`, exploiting the entity's Void vulnerability: **36 Direct Void Damage**!
  * **Agent Park**: Firing from Node 04, adds 18 Lament damage. Hostile HP drops to **154/240**!

---

```text
{hud_t02}
```

##### Turn 02 Action Resolution Log (Joint Severing & Stagger Build)
- **Joint Severing Assault**:
  * Agent Hwang targets the thumb joint with a precision void incision: **28 Void Damage**!
  * Agent Park discharges `[Lament Requiem Pure Echo]`: **24 Damage**!
  * Hostile HP drops to **102/240**!
  * Combined Posture strain strips another 36 points: Posture drops to **42/120**, crossing the **60% Posture Threshold (72 Points)**!
  * **STAGGER LEVEL 1 TRIGGERED!** The crystalline fingers droop, and the rift wavers!

---

```text
{hud_t03}
```

##### Turn 03 Action Resolution Log (Stagger Level 1 Exploitation)
- **Vanguard Overload (1.5x Direct Damage)**:
  * Agent Park's `Momentum Surge` activates! (+2 Speed next turn). Park unleashes a point-blank smash for **42 Damage**!
  * Border Lead Mellda executes `[Threshold Cleave]` at the wrist joint: **38 Damage**!
  * Hostile HP plummets to **22/240**! Posture collapses to **10/120**!

---

```text
{hud_t04}
```

##### Turn 04 Action Resolution Log (Prismatic Desperation Burst)
- **Hostile Recovery & Desperation Counter-Surge**:
  * The Piercing Hand flares with blinding violet radiance: `[Prismatic Spire]`.
  * Mellda deploys `[Directional Guard Absorption]`, taking 8 chip damage (HP: 174/190) and anchoring the team against the dimensional back-pressure.
  * Park and Hwang coordinate counter-fire, reducing HP to **10/240**!

---

```text
{hud_t05}
```

##### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Wrist Pin & Terminal Collapse**:
  * Mellda drives *Threshold Vow* through the main wrist joint, pinning the hand against the floorplates.
  * Posture hits **0/120**! **TERMINAL STAGGER TRIGGERED!** The construct shatters into non-functional crystal chunks.

---

```text
{hud_t06}
```

##### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Rift Closure & Purification**:
  * Agent Hwang executes `[Void Suture]`, sealing the spatial fissure while Mellda and Park pulverize the remaining crystal fingers into harmless violet mist.
  * Floor 5 collection manifolds harvest **+0.018 tons of pure refined Han**!

Total daily harvest reaches **0.168 / 0.160 tons**! Quota surpassed!

---

#### 4. Shift Evaluation Index & Daily RHR Allocation

```text
{eval_box}
```

---

#### 5. Well Extraction Protocol (Containment Authorization)

```text
{extract_box}
```

##### Director Majin's Assessment & Authorization
- *Choice Beta* is *The Weeping Willow* (SE-C-IIIγ-140)—a serene entity, but low energy output.
- *Choice Gamma* is *The Maw* (SE-C-Iα-008)—already anchored in our foundation.
- *Choice Alpha* is **The Hollow Saint** (SE-C-IIIγ-081)—a high-tier Lament/White entity capable of providing top-tier sanity regeneration gear (*Saint Robes*).

AUTHORIZATION LOCKED: **Choice Alpha: SE-C-IIIγ-081 (*The Hollow Saint*)**.

---

#### 6. M.A.W. Synthesis & Armament Forging

```text
{forge_box}
```

Agent Hwang equips the *Whispering Needle*, granting Floor 4 unmatched armor-piercing void precision.

---

#### 7. Nocturnal Sub-Vault Telemetry & Director's Vigil

At 02:45, Majin inspects Floor 5's reinforced observation gallery. The border rift is completely sealed. Outside, the Desolate winds howl against the outer Veil, but inside, the facility is tranquil.

Deep within Floor 6, the hydraulic ballast meters register **49.100 tons** of stored sorrow.

Seiyon's holographic form materializes beside him: *"Forty-nine point one tons, Majin. We are less than one ton away from Day 160."*

Majin gazes into the dark dunes beyond Gate 05: *"Four days until the Pale Dusk. Alert Marjuk on Floor 6. When the shadow falls, we hold the line."*
"""
    return content

def update_part_3():
    path = "SOMNARAK-WORLD/The_Absolvohan/Part_3_Days_29_to_49.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Expand Day 29 Turn 02-06
    old_d29_summary = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Mellda holds N02; Park deals 38 Lament damage; Monolith  |
| 60% Stagger.                                                        |
| - Turn 03: Posture broken; all attacks deal 2.0x direct damage; HP  |
| falls to 125.                                                       |
| - Turn 04: Monolith recovers; charges massive shockwave [Tectonic   |
| Toll].                                                              |
| - Turn 05: Kim at N06 uses 2 AP to fire Stasis Disruption,          |
| canceling skill.                                                    |
| - Turn 06: Park unleashes Requiem Climax; Terminal Stagger shatters |
| monolith.                                                           |
+=====================================================================+
```"""

    if old_d29_summary in content:
        content = content.replace(old_d29_summary, get_day_29_expanded())
        print("Day 29 Turns 02-06 replaced successfully!")
    else:
        print("Warning: Day 29 summary not matched directly.")

    # 2. Insert Day 45 before Day 49
    day_45_text = generate_day_45()
    day_49_marker = "### Day 49"
    if day_49_marker in content:
        content = content.replace(day_49_marker, day_45_text + "\n" + day_49_marker)
        print("Day 45 inserted successfully before Day 49!")
    else:
        print("Warning: Day 49 marker not found.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated Part 3 successfully!")

if __name__ == "__main__":
    update_part_3()
