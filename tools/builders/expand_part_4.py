#!/usr/bin/env python3
"""
tools/expand_part_4.py
Expands Part 4 (Days 53 to 73) into an exhaustive operational chronicle:
- Full turn-by-turn combat logs for Day 53, 55, 60, 65, 73 across Turns 02 to 06.
- Inserts Day 69 (Deep Bedrock Tremors & Amber Dusk Magma Tunneler Suppression).
- Enforces 100% box symmetry and dual-environment typography (<= 71 chars for boxes).
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

# --- DAY 53 EXPANSION ---
def get_day_53_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 3 HYDRAULIC EXTRACTION HALL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SPIRE-A][PARK]  [SPIRE-B][HWANG]       [KIM]                   [ZYRAK]",
        "---",
        "- Node 01: Clockwork Spire A (Posture 56/120 / Base Drive Fractured)",
        "- Node 02: Agent Park (Point-Blank Band 1 / Heavy Maul Cleaving)",
        "- Node 03: Clockwork Spire B (Charging Kinetic Piston / Posture 120/120)",
        "- Node 04: Agent Hwang (Range Band 2 / Blessed Scalpel Firing)",
        "- Node 06: Agent Kim (Range Band 3 / Covering Flank with Carbine)",
        "---",
        "- Agent Park  : Spd 6 -> 3 AP | HP 120/120 | SP +25 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 110/110 | SP +20 | Posture 70/70",
        "- Spire A     : Spd 3 -> 1 AP | HP 164/260 | Posture 56/120 [CRACKED]",
        "- Spire B     : Spd 4 -> 2 AP | HP 260/260 | Posture 120/120"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1 ON SPIRE A]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SCRAP]         [SPIRE-B][HWANG]        [KIM]                   [ZYRAK]",
        "        [PARK]",
        "---",
        "- Node 01: Spire A (SHATTERED & PULVERIZED / Scrap Siphoned)",
        "- Node 02: Agent Park (Momentum Surge Primed / Repositioning to Node 03)",
        "- Node 03: Spire B (Exposed / Posture 84/120)",
        "- Node 04: Agent Hwang (Void Disruption Firing)",
        "- Node 06: Agent Kim (Suppressing Emerging Gear Scuttlers)",
        "---",
        "- Agent Park  : Spd 8 -> 4 AP [SURGE] | HP 120/120 | SP +25 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +28 | Posture 55/55",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 110/110 | SP +25 | Posture 70/70",
        "- Spire A     : HP 0/260 [DESTROYED]",
        "- Spire B     : Spd 4 -> 2 AP | HP 212/260 | Posture 84/120 [ENGAGED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — SCUTTLER SWARM & JAW CLAMP PIN]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [PARK]  [SPIRE-B][HWANG]        [KIM]                   [ZYRAK]",
        "---",
        "- Node 02: Agent Park (Spd 8 / AP 4 / Heavy Maul Overhead Strike)",
        "- Node 03: Clockwork Spire B (Posture 40/120 / Piston Damaged)",
        "- Node 04: Agent Hwang (Slicing Gear Teeth with Scalpel)",
        "- Node 06: Agent Kim (Pinning Scuttlers at Node 03 with Jaw Clamp)",
        "---",
        "- Agent Park  : Spd 8 -> 4 AP [SURGE] | HP 120/120 | SP +25 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +28 | Posture 55/55",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 106/110 | SP +25 | Posture 62/70",
        "- Spire B     : Spd 3 -> 1 AP | HP 136/260 | Posture 40/120 [CRITICAL]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                [SPIRE-B]                                       [ZYRAK]",
        "        [PARK]  [HWANG]         [KIM]",
        "---",
        "- Node 02: Agent Park (Two-Handed Maul Sunder Landed)",
        "- Node 03: Spire B (TERMINAL STAGGER / POSTURE 0/120 / 2.0x DMG)",
        "- Node 03: Agent Hwang (Severing Central Flywheel)",
        "- Node 04: Agent Kim (Breaching Hydraulic Fuel Tank)",
        "---",
        "- Agent Park  : Spd 6 -> 3 AP | HP 120/120 | SP +25 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +28 | Posture 55/55",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 106/110 | SP +25 | Posture 62/70",
        "- Spire B     : Spd 0 -> 0 AP | HP 42/260  | Posture 0/120 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [SLAG]  [PARK]  [HWANG]         [KIM]                   [ZYRAK]",
        "---",
        "- Node 02: Clockwork Spires (Reduced to Slag & Pure Han Vapor)",
        "- Node 03: Agent Park (Venting Heated Steam)",
        "- Node 04: Agent Hwang (Sheathing Scalpel / Sanitizing Core)",
        "- Node 06: Agent Kim (Reporting Sector Clear)",
        "---",
        "- Agent Park  : Spd 6 -> 3 AP | HP 120/120 | SP +30 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +32 | Posture 55/55",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 106/110 | SP +30 | Posture 70/70",
        "- Spires      : HP 0/260 [DESTROYED] | +0.020 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Stagger Level 1 on Spire A)
- **Coordinated Breaching Strike**:
  * **Agent Park (Speed 6 -> 3 AP)**: Stands at Node 02 in Point-Blank Band 1. Spends 2 AP to execute `[Heavy Maul Sunder]` targeting Spire A's primary axle.
    * Grudge Base 18 * Grudge Vulnerability (1.5x) = **27 Direct Damage**!
    * Inflicts +28 Posture Strain. Spire A Posture drops to **44/120**, breaching the **60% Posture Threshold (72 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** Spire A's gears lock up in sparks.
  * **Agent Hwang (Speed 6 -> 3 AP)**: From Node 04 (Range Band 2), fires `[Blessed Scalpel Void Beam]` into Spire B for **24 Void damage**.
  * **Agent Kim (Speed 5 -> 3 AP)**: Firing from Node 06, cuts down four emerging gear scuttlers.
  * Spire A HP drops to **118/260**; Spire B HP drops to **212/260**.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Spire A Destruction & Momentum Surge)
- **Stagger Exploitation & Execution**:
  * With Spire A immobilized in Stagger Level 1, all incoming strikes deal 1.5x direct damage!
  * **Agent Park**: Passive `Momentum Surge` triggers! Gains +2 Speed for next turn. Park unleashes an overhead maul smash:
    * Deals **56 Grudge Damage**!
    * Spire A HP reaches **0/260**! The entire brass structure shatters into heaps of inert scrap metal.
  * **Agent Kim**: Steps up to Node 04, channeling suppressive carbine rounds into Spire B.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Scuttler Swarm & Jaw Clamp Pin)
- **Hostile Counter-Surge & Extraction Control**:
  * Spire B releases a swarm of razor-toothed brass scuttlers to encircle Park.
  * Containment Lead Dekan activates Floor 2's *Jaw Clamp* hydraulic traps through the floorplates, pinning the scuttler swarm in place!
  * **Agent Kim**: Uses `[Directional Guard Absorption]`, absorbing 12 kinetic damage (HP: 106/110) while covering Hwang.
  * **Agent Park (Speed 8 under Surge -> 4 AP)**: Swings his maul in a wide 360-degree arc, pulverizing the pinned scuttlers and smashing Spire B's main flywheel for **38 damage**!
  * Spire B Posture falls to **28/120**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Piston Severance & Terminal Collapse**:
  * Agent Hwang drives the Blessed Scalpel into Spire B's primary steam valve, stripping the final 28 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/120**. Spire B ceases all rotation, venting black oil onto the deckplates.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Purification)
- **Final Subdual**:
  * Agent Park and Agent Kim coordinate a synchronized double-impact smash. Spire B collapses into smoking slag and pure refined Han aerosol.
  * Floor 3 pneumatic collection flues siphon the harvest: **+0.020 tons of refined Han secured**!
"""

# --- DAY 55 EXPANSION ---
def get_day_55_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 7 SHADOW CORPS TRANSIT VAULT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SHROUD][ISHALL]        [PARK]                  [SONG]          [MAJIN]",
        "---",
        "- Node 01: Sanguine Shroud (Posture 68/140 / Spectral Mantle Pierced)",
        "- Node 02: Outsider Ishall (Rear Infiltration / Void Talons Readied)",
        "- Node 04: Agent Park (Line Anchor / Judgment Scale Raised / Band 2)",
        "- Node 07: Agent Song (Ranged Support / Fountain Siphon Bow Aimed)",
        "- Node 10: Director Majin & Seiyon Command Console (Band 5)",
        "---",
        "- Ishall      : Spd 7 -> 4 AP | HP 160/160 | SP +35 | Posture 80/80",
        "- Agent Park  : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 70/70",
        "- Agent Song  : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Sanguine Shroud: Spd 5 -> 3 AP | HP 210/300 | Posture 68/140 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SHROUD][ISHALL]        [PARK]                  [SONG]          [MAJIN]",
        "---",
        "- Node 01: Sanguine Shroud (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 02: Outsider Ishall (Executing Unanswered Void Flurry)",
        "- Node 04: Agent Park (Advancing with Momentum Surge / +2 Speed)",
        "- Node 07: Agent Song (Releasing Triple Resonant Lament Volley)",
        "---",
        "- Ishall      : Spd 7 -> 4 AP | HP 160/160 | SP +35 | Posture 80/80",
        "- Agent Park  : Spd 8 -> 4 AP [SURGE] | HP 125/125 | SP +30 | Posture 70/70",
        "- Agent Song  : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Shroud      : Spd 0 -> 0 AP | HP 112/300 | Posture 25/140 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — SANGUINE DELUGE REACTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SHROUD][ISHALL][PARK]                          [SONG]          [MAJIN]",
        "---",
        "- Node 01: Sanguine Shroud (Recovered / Channeling Sanguine Deluge)",
        "- Node 02: Outsider Ishall (Directional Guard Absorption Active)",
        "- Node 03: Agent Park (Interposing Judgment Scale Shield)",
        "- Node 07: Agent Song (Piercing Channeling Eye with Siphon Bow)",
        "---",
        "- Ishall      : Spd 7 -> 4 AP | HP 152/160 | SP +35 | Posture 70/80",
        "- Agent Park  : Spd 8 -> 4 AP | HP 125/125 | SP +30 | Posture 70/70",
        "- Agent Song  : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Shroud      : Spd 4 -> 2 AP | HP 64/300  | Posture 12/140 [UNSTABLE]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SHROUD]                                        [SONG]          [MAJIN]",
        "        [ISHALL][PARK]",
        "---",
        "- Node 01: Sanguine Shroud (TERMINAL STAGGER / POSTURE 0/140 / 2.0x DMG)",
        "- Node 02: Outsider Ishall (Dissecting Heart Core with Relic Digits)",
        "- Node 03: Agent Park (Priming Judgment Climax Smash)",
        "- Node 07: Agent Song (Harmonic Resonant Chorus Aimed)",
        "---",
        "- Ishall      : Spd 7 -> 4 AP | HP 152/160 | SP +35 | Posture 70/80",
        "- Agent Park  : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 70/70",
        "- Agent Song  : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Shroud      : Spd 0 -> 0 AP | HP 18/300  | Posture 0/140 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MIST]  [ISHALL][PARK]                          [SONG]          [MAJIN]",
        "---",
        "- Node 01: Sanguine Shroud (Dissolved into Crimson Vapor / Siphoned)",
        "- Node 02: Outsider Ishall (Retracting Mineral Digits)",
        "- Node 03: Agent Park (Resting Scale / Securing RHR)",
        "- Node 07: Agent Song (Lowering Bow / Confirming Clean Floor)",
        "---",
        "- Ishall      : Spd 7 -> 4 AP | HP 152/160 | SP +40 | Posture 80/80",
        "- Agent Park  : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 70/70",
        "- Agent Song  : Spd 6 -> 3 AP | HP 115/115 | SP +30 | Posture 55/55",
        "- Shroud      : HP 0/300 [PURIFIED] | +0.022 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Rear Infiltration & Stagger Build)
- **Infiltration & Flanking Strike**:
  * **Outsider Ishall (Speed 7 -> 4 AP)**: Utilizes *Shadow Ingress* to teleport from Node 08 directly to Node 02 behind the Sanguine Shroud!
    * Spends 2 AP to execute `[Unanswered Void Talons]` on the rear emotional nexus:
      * Deals **42 Direct Void Damage**!
      * Inflicts +32 Posture Strain. Shroud Posture drops to **52/140**, crossing the **60% Posture Threshold (84 Points)**!
      * **STAGGER LEVEL 1 TRIGGERED!** The crimson shroud tears along its spectral hem.
  * **Agent Park**: Anchoring Node 04 behind the *Judgment Scale*, parries the deflected lash with zero damage sustained.
  * **Agent Song**: Firing from Node 07 with the Fountain Siphon Bow, hits for **28 Lament damage**.
  * Shroud HP drops to **140/300**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Allied Focus Fire (1.5x Direct Damage)**:
  * Agent Park's `Momentum Surge` activates! (+2 Speed next turn). Park advances to Node 03, delivering a heavy downward smash: **48 Weight Damage**!
  * Outsider Ishall executes a continuous four-strike void tear: **46 Damage**!
  * Shroud HP falls from 140 to **72/300**! Posture drops to **18/140**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Sanguine Deluge Desperation)
- **Hostile Recovery & Desperation Counter-Surge**:
  * The Sanguine Shroud recovers, attempting to inundate the corridor with `[Sanguine Deluge]`.
  * Outsider Ishall deploys `[Directional Guard Absorption]`, taking 8 chip damage (HP: 152/160) and deflecting the blood tide away from the squad!
  * Agent Song fires a piercing arrow directly into the entity's central eye, canceling the torrential deluge!
  * Shroud HP drops to **34/300**! Posture falls to **6/140**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Heart Dissection & Terminal Collapse**:
  * Ishall's floating relic digits slice through the core tendons, stripping the final 6 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/140**. The shroud falls flat against the deckplates like discarded red silk.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Judgment Climax**:
  * Agent Park executes `[Judgment Climax: Scale of Atonement]`. The entity dissolves into a cloud of crimson vapor and refined Han crystals.
  * Floor 7 collection flues harvest **+0.022 tons of refined Han**!
"""

# --- DAY 60 EXPANSION ---
def get_day_60_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 5 CHITINOUS BREEDING TRENCH]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SPIDER][PARK]          [MELLDA]        [KIM]   [HWANG]         [MAJIN]",
        "---",
        "- Node 01: Chitinous Queen (Posture 72/160 / Thorax Fractured)",
        "- Node 02: Agent Park (Point-Blank Band 1 / Warhammer Cleave Landed)",
        "- Node 04: Border Lead Mellda (Bulwark Shield / Threshold Vow Ready)",
        "- Node 06: Agent Kim (Range Band 3 / Incendiary Carbine Firing)",
        "- Node 07: Agent Hwang (Range Band 4 / Void Lance Aimed)",
        "---",
        "- Agent Park  : Spd 6 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Mellda      : Spd 5 -> 3 AP | HP 190/190 | SP +35 | Posture 95/95",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 115/115 | SP +25 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Chitin Queen: Spd 4 -> 2 AP | HP 215/340 | Posture 72/160 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SPIDER]        [MELLDA]                [KIM]   [HWANG]         [MAJIN]",
        "        [PARK]",
        "---",
        "- Node 01: Chitinous Queen (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 02: Agent Park (Advancing with Momentum Surge / +2 Speed)",
        "- Node 03: Border Lead Mellda (Driving Arm-Blade into Ventral Shell)",
        "- Node 07: Agent Hwang (Discharging Focused Void Ray)",
        "---",
        "- Agent Park  : Spd 8 -> 4 AP [SURGE] | HP 130/130 | SP +30 | Posture 70/70",
        "- Mellda      : Spd 5 -> 3 AP | HP 190/190 | SP +35 | Posture 95/95",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 115/115 | SP +25 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Queen       : Spd 0 -> 0 AP | HP 118/340 | Posture 28/160 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — TECTONIC WEB BURST COUNTER-SURGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SPIDER][PARK]  [MELLDA]                [KIM]   [HWANG]         [MAJIN]",
        "---",
        "- Node 01: Chitinous Queen (Recovered / Channeling Tectonic Web)",
        "- Node 02: Agent Park (Shielding Face with Warhammer Mantlet)",
        "- Node 03: Border Lead Mellda (Directional Guard Absorption)",
        "- Node 06: Agent Kim (Burning Web Filaments with Carbine)",
        "---",
        "- Agent Park  : Spd 8 -> 4 AP | HP 124/130 | SP +30 | Posture 60/70",
        "- Mellda      : Spd 5 -> 3 AP | HP 184/190 | SP +35 | Posture 85/95",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 115/115 | SP +25 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Queen       : Spd 4 -> 2 AP | HP 62/340  | Posture 14/160 [WEAKENED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SPIDER]                                                        [MAJIN]",
        "        [PARK]  [MELLDA]        [KIM]   [HWANG]",
        "---",
        "- Node 01: Chitinous Queen (TERMINAL STAGGER / POSTURE 0/160 / 2.0x DMG)",
        "- Node 02: Agent Park (Crushing Cephalic Nerve)",
        "- Node 03: Border Lead Mellda (Pinning Dorsal Carapace)",
        "- Node 07: Agent Hwang (Firing Wellspring Beam into Eye Cluster)",
        "---",
        "- Agent Park  : Spd 6 -> 3 AP | HP 124/130 | SP +30 | Posture 60/70",
        "- Mellda      : Spd 5 -> 3 AP | HP 184/190 | SP +35 | Posture 85/95",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 115/115 | SP +25 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Queen       : Spd 0 -> 0 AP | HP 16/340  | Posture 0/160 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRYSTAL][PARK] [MELLDA]                [KIM]   [HWANG]         [MAJIN]",
        "---",
        "- Node 01: Chitinous Queen (Dissolved into Amber Crystals / Siphoned)",
        "- Node 02: Agent Park (Resting Hammer / Securing Carapace Shards)",
        "- Node 03: Border Lead Mellda (Confirming Perimeter Lockdown)",
        "- Node 06: Agent Kim (Venting Gas Purge)",
        "---",
        "- Agent Park  : Spd 6 -> 3 AP | HP 124/130 | SP +35 | Posture 70/70",
        "- Mellda      : Spd 5 -> 3 AP | HP 184/190 | SP +40 | Posture 95/95",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 115/115 | SP +30 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +30 | Posture 55/55",
        "- Queen       : HP 0/340 [PURIFIED] | +0.024 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Thorax Fracture & Stagger Build)
- **Frontline Hammer Impact**:
  * **Agent Park (Speed 6 -> 3 AP)**: Smashes the spider's front armored leg with his heavy warhammer:
    * Deals **48 Weight Damage**!
    * Inflicts +36 Posture Strain. Queen Posture drops to **60/160**, breaching the **60% Posture Threshold (96 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The arachnid's legs tremble, and its carapace fissures along the dorsal midline.
  * **Border Lead Mellda**: Locks Node 04 with her Bulwark Shield, intercepting rogue web strands.
  * **Agent Hwang**: From Node 07 (Range Band 4), drives a Void beam through the fissure for **36 Void damage**.
  * Queen HP drops to **176/340**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Allied Focus Fire (1.5x Direct Damage)**:
  * Agent Park's `Momentum Surge` activates! (+2 Speed next turn). Park unleashes a direct crushing blow to the cephalothorax: **54 Weight Damage**!
  * Border Lead Mellda drives *Threshold Vow* into the exposed nerve cluster: **42 Grudge Damage**!
  * Queen HP falls from 176 to **80/340**! Posture collapses to **18/160**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Tectonic Web Burst Desperation)
- **Hostile Recovery & Desperation Web Burst**:
  * The Chitinous Queen recovers, releasing an explosive burst of electrified tectonic silk across Nodes 01, 02, and 03.
  * Mellda deploys `[Directional Guard Absorption]`, taking 6 chip damage (HP: 184/190) and shielding Park.
  * Agent Kim fires incendiary rounds from his carbine at Node 06, incinerating the web filaments before they can trap the vanguard!
  * Queen HP drops to **42/340**! Posture drops to **6/160**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Eye Cluster Pin & Terminal Collapse**:
  * Agent Hwang channels a high-intensity Wellspring beam into the central eye cluster, stripping the last 6 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/160**. The massive spider collapses motionless across Node 01.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Smite**:
  * Agent Park raises the heavy warhammer, delivering the finishing smite. The Chitinous Queen dissolves into thousands of gleaming amber crystals and refined Han mist.
  * Floor 5 collection flues harvest **+0.024 tons of refined Han**!
"""

# --- DAY 65 EXPANSION ---
def get_day_65_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 4 LEVITATION VOID ARENA]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SPIRE-A][SPIRE-B][SPIRE-C][AYSHUK]     [KIM]   [HWANG] [SONG]  [MAJIN]",
        "---",
        "- Node 01: Spire A (Posture 42/100 / Optical Focal Aperture Severed)",
        "- Node 02: Spire B (Charging Void Beam / Posture 100/100)",
        "- Node 03: Spire C (Charging Prismatic Lance / Posture 100/100)",
        "- Node 04: Research Lead Ayshuk (Predicting Refraction Angles / Band 2)",
        "- Node 06: Agent Kim (Stasis Shield Primed / Band 3)",
        "- Node 07: Agent Hwang (Void Lance Aimed / Band 4)",
        "- Node 08: Agent Song (Fountain Siphon Bow Locked / Band 4)",
        "---",
        "- Spire A : Spd 3 -> 1 AP | HP 142/240 | Posture 42/100 [CRACKED]",
        "- Spire B : Spd 4 -> 2 AP | HP 240/240 | Posture 100/100",
        "- Spire C : Spd 4 -> 2 AP | HP 240/240 | Posture 100/100"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — SPIRE A SHATTERED & CROSS-FIRE FOCUS]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SLAG]  [SPIRE-B][SPIRE-C][AYSHUK]     [KIM]   [HWANG] [SONG]  [MAJIN]",
        "---",
        "- Node 01: Spire A (SHATTERED & PULVERIZED / Slag Siphoned)",
        "- Node 02: Spire B (Posture 60/100 / Core Fractured)",
        "- Node 03: Spire C (Charging Prismatic Lance / Posture 85/100)",
        "- Node 07: Agent Hwang (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 08: Agent Song (Synchronized Volley Firing)",
        "---",
        "- Spire A : HP 0/240 [DESTROYED]",
        "- Spire B : Spd 4 -> 2 AP | HP 156/240 | Posture 60/100 [STAGGER 1]",
        "- Spire C : Spd 4 -> 2 AP | HP 210/240 | Posture 85/100"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — CROSS-FLOOR BEAM & STASIS SHIELD]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [SPIRE-B][SPIRE-C][AYSHUK][KIM]         [HWANG] [SONG]  [MAJIN]",
        "---",
        "- Node 02: Spire B (Recovered / Firing Cross-Floor Beam)",
        "- Node 03: Spire C (Coordinating Prismatic Surge)",
        "- Node 04: Research Lead Ayshuk (Clarity Field Deployed)",
        "- Node 05: Agent Kim (Directional Guard Absorption Active)",
        "- Node 07: Agent Hwang (Spd 8 / AP 4 / Overdrive Void Lance)",
        "---",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 108/115 | SP +25 | Posture 58/65",
        "- Agent Hwang : Spd 8 -> 4 AP [SURGE] | HP 115/115 | SP +25 | Posture 55/55",
        "- Agent Song  : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Spire B     : Spd 3 -> 1 AP | HP 82/240  | Posture 24/100 [CRITICAL]",
        "- Spire C     : Spd 4 -> 2 AP | HP 165/240 | Posture 54/100"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER ON SPIRE B & C]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [SPIRE-B][SPIRE-C]                                      [MAJIN]",
        "                [AYSHUK][KIM]   [HWANG] [SONG]",
        "---",
        "- Node 02: Spire B (TERMINAL STAGGER / POSTURE 0/100 / 2.0x DMG)",
        "- Node 03: Spire C (TERMINAL STAGGER / POSTURE 0/100 / 2.0x DMG)",
        "- Node 07: Agent Hwang (Overdrive Beam Fractured Spire B Core)",
        "- Node 08: Agent Song (Dual Acoustic Volley Grounded Spire C)",
        "---",
        "- Spire B     : Spd 0 -> 0 AP | HP 18/240  | Posture 0/100 [COLLAPSED]",
        "- Spire C     : Spd 0 -> 0 AP | HP 32/240  | Posture 0/100 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [ASH]   [ASH]   [AYSHUK][KIM]   [HWANG] [SONG]          [MAJIN]",
        "---",
        "- Node 02-03: Spires B & C (Disintegrated into White Ash / Siphoned)",
        "- Node 04: Research Lead Ayshuk (Calibrating Optical Arrays)",
        "- Node 05: Agent Kim (Lowering Stasis Shield)",
        "- Node 07: Agent Hwang (Venting Capacitor Heat)",
        "- Node 08: Agent Song (Reporting Tripartite Void Purge Complete)",
        "---",
        "- Spires B & C: HP 0/240 [DESTROYED] | +0.026 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Sniper Focus & Spire A Stagger)
- **Long-Range Volley**:
  * **Agent Song (Speed 6 -> 3 AP)**: Operating from Range Band 4 (Node 08), releases a high-tension acoustic arrow from the Fountain Siphon Bow:
    * The projectile threads straight through the aperture of Spire A's charging beam!
    * Deals **46 Pure Lament Damage**!
    * Inflicts +28 Posture Strain. Spire A Posture drops to **42/100**, breaching the **60% Posture Threshold (60 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** Spire A's optical disc dims, its charging sequence aborted.
  * **Agent Hwang**: Fires a precision Void beam into Spire A's levitation gyros for **32 Void damage**.
  * Spire A HP drops to **118/240**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Spire A Annihilation & Momentum Surge)
- **Synchronized Execution (1.5x Direct Damage)**:
  * Agent Hwang's `Momentum Surge` activates! (+2 Speed next turn). Hwang discharges a full-power beam directly into Spire A's exposed core:
    * Deals **58 Void Damage**! Spire A HP hits **0/240**!
    * Spire A shatters into harmless slag and dissolves into white vapor!
  * Agent Song redirects her fire to Spire B, dealing **34 damage** and inflicting +24 Posture strain.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Cross-Floor Beam & Stasis Shield)
- **Hostile Desperation Counter-Surge**:
  * Spires B and C coordinate their prismatic emitters, firing a lethal cross-floor laser convergence down Node 04 and 05.
  * Research Lead Ayshuk activates the floor's *Clarity Field*, altering the atmospheric refraction index.
  * **Agent Kim**: Deploys `[Directional Guard Absorption]`, taking 7 chip damage (HP: 108/115) while grounding the laser burst!
  * **Agent Hwang (Speed 8 under Surge -> 4 AP)**: Unleashes `[Overdrive Void Lance]`, driving the beam through Spire B's gyro housing for **48 damage**!
  * Spire B Posture falls to **24/100**; Spire C Posture falls to **54/100**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger on Spires B & C)
- **Dual Gyro Collapse**:
  * Agent Song fires a double arrow volley into Spire C's base, while Agent Hwang pierces Spire B's power cell.
  * **TERMINAL STAGGER TRIGGERED ON BOTH SPIRES!** Posture hits **0/100** for both constructs. The spires lose levitation, crashing hard onto the deckplates!

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Volley**:
  * Agent Song executes `[Climax Volley: Rain of Siphon Petals]`. Spires B and C disintegrate into fine white ash and radiant Han mist.
  * Floor 4 collection flues harvest **+0.026 tons of refined Han**!
"""

# --- DAY 73 EXPANSION ---
def get_day_73_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 8 BOUNDARY GATE 05]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[ECHO]  [ISHALL]        [MELLDA][DEKAN]         [XYAN]                  [MAJIN]",
        "---",
        "- Node 01: Pallid Echo (Posture 84/180 / Dimensional Matrix Fractured)",
        "- Node 02: Outsider Ishall (Rear Flank Ingress / Unanswered Talons)",
        "- Node 04: Border Lead Mellda (Point-Blank Band 1 / Bulwark Shield)",
        "- Node 05: Containment Lead Dekan (Jaw Clamp Anchor / Heavy Plate)",
        "- Node 07: Boundary Vanguard Xyan (Desolate Transit Flues Firing)",
        "---",
        "- Ishall  : Spd 7 -> 4 AP | HP 165/165 | SP +35 | Posture 85/85",
        "- Mellda  : Spd 6 -> 3 AP | HP 195/195 | SP +35 | Posture 95/95",
        "- Dekan   : Spd 5 -> 3 AP | HP 205/205 | SP +35 | Posture 100/100",
        "- Xyan    : Spd 6 -> 3 AP | HP 170/170 | SP +30 | Posture 85/85",
        "- Pallid Echo : Spd 5 -> 3 AP | HP 260/380 | Posture 84/180 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[ECHO]  [ISHALL]        [MELLDA][DEKAN]         [XYAN]                  [MAJIN]",
        "---",
        "- Node 01: Pallid Echo (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 02: Outsider Ishall (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 04: Border Lead Mellda (Threshold Severance Slice Landed)",
        "- Node 05: Containment Lead Dekan (Hydraulic Hammer Shock)",
        "- Node 07: Boundary Vanguard Xyan (Desolate Siphon Beam)",
        "---",
        "- Ishall  : Spd 9 -> 5 AP [SURGE] | HP 165/165 | SP +35 | Posture 85/85",
        "- Mellda  : Spd 6 -> 3 AP | HP 195/195 | SP +35 | Posture 95/95",
        "- Dekan   : Spd 5 -> 3 AP | HP 205/205 | SP +35 | Posture 100/100",
        "- Echo    : Spd 0 -> 0 AP | HP 136/380 | Posture 32/180 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — ANCIENT BALLAST QUAKE REACTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[ECHO]  [ISHALL][MELLDA][DEKAN]                 [XYAN]                  [MAJIN]",
        "---",
        "- Node 01: Pallid Echo (Recovered / Channeling Ancient Ballast Quake)",
        "- Node 02: Outsider Ishall (Spd 9 / AP 5 / Severing Harmonic Nexus)",
        "- Node 03: Border Lead Mellda (Directional Guard Absorption)",
        "- Node 04: Containment Lead Dekan (Jaw Clamp Pin Engaged)",
        "- Node 07: Boundary Vanguard Xyan (Grounding Tectonic Shockwave)",
        "---",
        "- Ishall  : Spd 9 -> 5 AP | HP 165/165 | SP +35 | Posture 85/85",
        "- Mellda  : Spd 6 -> 3 AP | HP 185/195 | SP +32 | Posture 80/95",
        "- Dekan   : Spd 5 -> 3 AP | HP 195/205 | SP +32 | Posture 85/100",
        "- Echo    : Spd 4 -> 2 AP | HP 68/380  | Posture 14/180 [UNSTABLE]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[ECHO]                                          [XYAN]                  [MAJIN]",
        "        [ISHALL][MELLDA][DEKAN]",
        "---",
        "- Node 01: Pallid Echo (TERMINAL STAGGER / POSTURE 0/180 / 2.0x DMG)",
        "- Node 02: Outsider Ishall (Unanswered Talon Severance Strike)",
        "- Node 03: Border Lead Mellda (Threshold Blade Locked into Core)",
        "- Node 04: Containment Lead Dekan (Hydraulic Pressure Clamp Engaged)",
        "---",
        "- Ishall  : Spd 7 -> 4 AP | HP 165/165 | SP +40 | Posture 85/85",
        "- Mellda  : Spd 6 -> 3 AP | HP 185/195 | SP +35 | Posture 80/95",
        "- Dekan   : Spd 5 -> 3 AP | HP 195/205 | SP +35 | Posture 85/100",
        "- Echo    : Spd 0 -> 0 AP | HP 16/380  | Posture 0/180 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[WHITE] [ISHALL][MELLDA][DEKAN]                 [XYAN]                  [MAJIN]",
        "---",
        "- Node 01: Pallid Echo (Dissolved into Radiant White Light / Siphoned)",
        "- Node 02: Outsider Ishall (Logging Terminal Boundary Telemetry)",
        "- Node 03: Border Lead Mellda (Sheathing Arm-Blade)",
        "- Node 04: Containment Lead Dekan (Venting Hydraulic Clamps)",
        "- Node 07: Boundary Vanguard Xyan (Securing Desolate Outpost)",
        "---",
        "- Echo    : HP 0/380 [PURIFIED] | +0.030 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Tri-Lead Absorption & Stagger Build)
- **Frontline Anchor & Flanking Severance**:
  * Mellda and Dekan hold Nodes 04 and 05, their overlapping shields absorbing the entity's pale tidal wave with zero damage to the rear lines.
  * **Outsider Ishall**: Operates from Node 02 behind the Echo. Spends 2 AP to unleash `[Unanswered Void Talons]`:
    * Deals **48 Multi-Affinity Damage**!
    * Inflicts +38 Posture Strain. Echo Posture drops to **62/180**, breaching the **60% Posture Threshold (108 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The entity's pale shroud unravels, exposing its crystalline harmonic core.
  * Boundary Vanguard Xyan fires from Node 07 with the Desolate transit flue, hitting for **34 Weight damage**.
  * Echo HP drops to **186/380**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Tri-Lead Focus Fire (1.5x Direct Damage)**:
  * Outsider Ishall's `Momentum Surge` activates! (+2 Speed next turn). Ishall executes a continuous void frenzy: **56 Damage**!
  * Border Lead Mellda delivers a devastating Threshold severance strike: **44 Grudge Damage**!
  * Dekan slams his hydraulic hammer into the floorplates, sending shockwaves through the core: **36 Weight Damage**!
  * Echo HP collapses from 186 to **50/380**! Posture drops to **16/180**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Ancient Ballast Quake Desperation)
- **Hostile Recovery & Desperation Quake**:
  * The Pallid Echo recovers, releasing an earth-shaking shockwave: `[Ancient Ballast Quake]`.
  * Containment Lead Dekan activates Floor 2's *Jaw Clamp* foundation locks, absorbing the kinetic shock into the bedrock!
  * Mellda deploys `[Directional Guard Absorption]`, taking 10 chip damage (HP: 185/195) and anchoring the squad.
  * Outsider Ishall slices through the harmonic nexus from Node 02, stripping another 12 points of Posture!
  * Echo HP drops to **24/380**! Posture falls to **4/180**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Harmonic Severance & Terminal Collapse**:
  * Ishall's floating relic digits pierce the nexus core, stripping the final 4 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/180**. The Pallid Echo's dimensional anchor shatters completely.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Purification)
- **Tri-Lead Climax Strike**:
  * Ishall, Mellda, and Dekan execute a synchronized triple-lead discharge.
  * The Pallid Echo dissolves into blinding, warm white light that purges all sorrow residue from Floor 8's boundary gates.
  * Gate collection manifolds harvest **+0.030 tons of refined Han**!
"""

# --- DAY 69 GENERATOR ---
def generate_day_69():
    t_box = make_box("REVERIE DIRECTORATE — CENTRAL COMMAND TERMINAL", [
        "FACILITY MANAGEMENT INTERFACE: DAY 69 SHIFT",
        "ENERGY HARVEST QUOTA  : 0.200 TONS // CURRENT HARVEST: 0.000 TONS",
        "COVERT BALLAST RESERVE : 51.250 TONS [HYDRAULIC CRYO-VAULTS]",
        "ACTIVE CONTAINMENT    : SE-001, 005, 014, 025, 031, 032, 033, 102",
        "TECTONIC ALERT        : MAW FAULT LINE RESONANCE SPIKE DETECTED"
    ])

    roster_box = make_box("DEPLOYED ROSTER: DAY 69 DEEP-BEDROCK TACTICAL SQUAD", [
        "AGENT & RATING        | STATS, GEAR & FOUR P-FRAMEWORK SPEC",
        "----------------------+-----------------------------------------------",
        "Outsider Ishall       | HP 165| SP 80 | Work 65 | Speed 7 (4 AP Base)",
        "Shadow Corps Decision | M.A.W.-W: Unanswered (Void / Light / 1 AP)",
        "Floor 7 Lead          | Suit: Shadow Shroud (Speed Delta +1 / Posture 85)",
        "                      | Parry: 18 Power | Pass: Shadow Ingress (Teleport)",
        "                      | Panic Typology: Despair (SP <= -40)",
        "----------------------+-----------------------------------------------",
        "Boundary Vanguard Xyan| HP 175| SP 75 | Work 68 | Speed 6 (3 AP + 1 Move)",
        "Gate Watch Decision   | M.A.W.-W: Desolate Flue (Weight / Heavy / 2 AP)",
        "Floor 8 Lead          | Suit: Sand-Worn Mail (Heavy / Spd 0 under Aura)",
        "                      | Posture: 90/90 | Guard: 20 Absorb | Pass: Bedrock Anchor",
        "                      | Panic Typology: Berserk (SP <= -35)",
        "----------------------+-----------------------------------------------",
        "Agent Park (Grade V)  | HP 72 | SP 78 | Work 65 | Speed 6 (3 AP + 1 Move)",
        "Senior Skirmisher     | M.A.W.-W: Judgment Scale (Weight / Medium / 1 AP)",
        "Floor 7 Assigned      | Suit: Lament Shroud (Light / Spd +1) | Halo Gift",
        "                      | Posture: 70/70 | Parry: 16 Power | Pass: Momentum Surge",
        "                      | Panic Typology: Despair (SP <= -35)"
    ])

    ordeal_box = make_box("TACTICAL DOSSIER: AMBER DUSK ORDEAL SUPPRESSION", [
        "DESIGNATION           : THE MAGMA TUNNELER (AMBER DUSK)",
        "CLASSIFICATION        : AMBER (WEIGHT/GRUDGE) THIRD WATCH LEVIATHAN",
        "INTRUSION POINT       : FLOOR 7 SUBTERRANEAN VENT CORE (NODE 02)",
        "HOSTILE PARAMETERS    : HP 360/360 | Posture 180/180 | Speed 4 (2 AP)",
        "ATTACK AFFINITY       : Weight / Tremor (High Kinetic Ground Shock)",
        "AFFINITY VULNERABILITY: Void (Pierce: 1.5x) & Lament (White: 1.25x)",
        "SPECIAL THREAT        : Burrowing sub-floor charge disrupts all nodes",
        "TACTICAL ORDERS       : INTERCEPT AT NODE 02; EXPLOIT VOID VULNERABILITY"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 7 SUBTERRANEAN VENT CORE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [TUNNEL][ISHALL][XYAN]  [PARK]                          [MAJIN]",
        "---",
        "SPATIAL RANGES & POSITIONS:",
        "- Node 02: Magma Tunneler (Burrowing Eruption Epicenter)",
        "- Node 03: Outsider Ishall (Rear Void Flanker / Range Band 1)",
        "- Node 04: Boundary Vanguard Xyan (Bedrock Bulwark / Range Band 2)",
        "- Node 05: Agent Park (Weighting Skirmisher / Range Band 3)",
        "- Node 10: Director Majin & Seiyon Command Console (Band 5)",
        "---",
        "OPERATIVE STATUS & RESOURCE POOLS:",
        "- Ishall      : Spd 7 -> 4 AP | HP 165/165 | SP 80/80 | Posture 85/85",
        "- Xyan        : Spd 6 -> 3 AP | HP 175/175 | SP 75/75 | Posture 90/90",
        "- Agent Park  : Spd 6 -> 3 AP | HP 72/72   | SP 78/78 | Posture 70/70",
        "- Tunneler    : Spd 4 -> 2 AP | HP 360/360 | Posture 180/180"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — CRACKING THE BASALT PLATING]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [TUNNEL][ISHALL][XYAN]  [PARK]                          [MAJIN]",
        "---",
        "- Node 02: Magma Tunneler (Posture 114/180 / Anterior Shell Fissured)",
        "- Node 03: Outsider Ishall (Void Talons Cleaving Nerve Cord)",
        "- Node 04: Boundary Vanguard Xyan (Desolate Flue Anchor Strike)",
        "- Node 05: Agent Park (Judgment Scale Weight Smash)",
        "---",
        "- Ishall      : Spd 7 -> 4 AP | HP 165/165 | SP 80/80 | Posture 85/85",
        "- Xyan        : Spd 6 -> 3 AP | HP 175/175 | SP 75/75 | Posture 90/90",
        "- Agent Park  : Spd 6 -> 3 AP | HP 72/72   | SP 78/78 | Posture 70/70",
        "- Tunneler    : Spd 3 -> 1 AP | HP 272/360 | Posture 114/180 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [TUNNEL]        [XYAN]  [PARK]                          [MAJIN]",
        "        [ISHALL]",
        "---",
        "- Node 02: Magma Tunneler (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 02: Outsider Ishall (Executing Unanswered Ingress Tear)",
        "- Node 04: Boundary Vanguard Xyan (Driving Heavy Maul into Core)",
        "- Node 05: Agent Park (Momentum Surge Primed / +2 Speed Next Turn)",
        "---",
        "- Ishall      : Spd 7 -> 4 AP | HP 165/165 | SP 80/80 | Posture 85/85",
        "- Xyan        : Spd 6 -> 3 AP | HP 175/175 | SP 75/75 | Posture 90/90",
        "- Agent Park  : Spd 8 -> 4 AP [SURGE] | HP 72/72 | SP 78/78 | Posture 70/70",
        "- Tunneler    : Spd 0 -> 0 AP | HP 148/360 | Posture 42/180 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAGMA SURGE & BEDROCK ANCHOR]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [TUNNEL][ISHALL][XYAN]  [PARK]                          [MAJIN]",
        "---",
        "- Node 02: Magma Tunneler (Recovered / Channeling Magma Surge)",
        "- Node 03: Outsider Ishall (Dissecting Vent Pipes)",
        "- Node 04: Boundary Vanguard Xyan (Directional Guard Absorption)",
        "- Node 05: Agent Park (Lament Requiem Resonant Shield)",
        "---",
        "- Ishall      : Spd 7 -> 4 AP | HP 165/165 | SP 80/80 | Posture 85/85",
        "- Xyan        : Spd 6 -> 3 AP | HP 162/175 | SP 75/75 | Posture 74/90",
        "- Agent Park  : Spd 8 -> 4 AP | HP 72/72   | SP 78/78 | Posture 70/70",
        "- Tunneler    : Spd 4 -> 2 AP | HP 76/360  | Posture 18/180 [UNSTABLE]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [TUNNEL]                                                [MAJIN]",
        "        [ISHALL][XYAN]  [PARK]",
        "---",
        "- Node 02: Magma Tunneler (TERMINAL STAGGER / POSTURE 0/180 / 2.0x DMG)",
        "- Node 02: Outsider Ishall (Severing Magma Sac)",
        "- Node 03: Boundary Vanguard Xyan (Pinning Mandibles to Bedrock)",
        "- Node 04: Agent Park (Priming Judgment Climax)",
        "---",
        "- Ishall      : Spd 7 -> 4 AP | HP 165/165 | SP 80/80 | Posture 85/85",
        "- Xyan        : Spd 6 -> 3 AP | HP 162/175 | SP 75/75 | Posture 74/90",
        "- Agent Park  : Spd 6 -> 3 AP | HP 72/72   | SP 78/78 | Posture 70/70",
        "- Tunneler    : Spd 0 -> 0 AP | HP 18/360  | Posture 0/180 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [GLASS] [ISHALL][XYAN]  [PARK]                          [MAJIN]",
        "---",
        "- Node 02: Magma Tunneler (Cooled into Inert Obsidian Glass / Siphoned)",
        "- Node 03: Outsider Ishall (Cleaning Relic Digits)",
        "- Node 04: Boundary Vanguard Xyan (Securing Bedrock Anchors)",
        "- Node 05: Agent Park (Siphoning Superheated Han Liquid)",
        "---",
        "- Ishall      : Spd 7 -> 4 AP | HP 165/165 | SP 80/80 | Posture 85/85",
        "- Xyan        : Spd 6 -> 3 AP | HP 162/175 | SP 75/75 | Posture 85/90",
        "- Agent Park  : Spd 6 -> 3 AP | HP 72/72   | SP 78/78 | Posture 70/70",
        "- Tunneler    : HP 0/360 [PURIFIED] | +0.025 TONS REFINED HAN HARVESTED"
    ])

    eval_box = make_box("END-OF-DAY PERFORMANCE EVALUATION: DAY 69", [
        "METRIC                 | TARGET QUOTA   | REALIZED PERFORMANCE",
        "-----------------------+----------------+---------------------",
        "Han Energy Harvested   | 0.200 Tons     | 0.210 Tons [SURPASSED]",
        "Containment Breaches   | 0 Breaches Max | 0 Breaches [CLEARED]",
        "Personnel Casualties   | 0 Fatalities   | 0 Fatalities [PERFECT]",
        "Amber Dusk Suppressed  | 1/1 Suppressed | 100% Rate [RESOLVED]",
        "Tectonic Stabilized    | 100% Locked    | SECURED TO BEDROCK",
        "-----------------------+----------------+---------------------",
        "SHIFT PERFORMANCE GRADE: GRADE S (BEDROCK DEFENDER)",
        "REAGENTS ACCUMULATED   : +35 RHR (REFINED HAN REAGENTS)",
        "OPERATIVE ADVANCEMENT  :",
        "- Outsider Ishall     : +5 Clarity, +3 Resolve (Master Infiltrator)",
        "- Vanguard Xyan       : +5 Resilience, +2 Composure (Bedrock Anchor)",
        "- Agent Park          : +4 Clarity, +3 Resilience (Senior Vanguard)"
    ])

    forge_box = make_box("M.A.W. SYNTHESIS FORGING LOG — DAY 69", [
        "FORGE SPECIFICATION    | SLOT / PROPERTIES / PARAMETERS",
        "-----------------------+----------------------------------------------",
        "Chained Anchor Blade   | Weapon: 8-12 Weight (Heavy / Speed Delta -1)",
        "                       | Range Band 1 | 2 AP | Inflicts Seismic Pin",
        "Vent Mantlet Shroud    | Suit: Heavy Armor (Speed Delta -1)",
        "                       | Resist: 0.5 Grudge / 0.8 Lament / 0.5 Weight",
        "Molten Crest Gift      | Head Slot: +10 HP, +10% Tremor Resistance",
        "-----------------------+----------------------------------------------",
        "EQUIPMENT ALLOCATION   | BESTOWED UPON VANGUARD XYAN (GATE WATCH LEAD)"
    ])

    content = f"""
### Day 69

### Story — Dialogue

> **Ishall:** _"Tremors on Floor 7, Director. The ventilation shafts beneath the Shadow Corps are bubbling with superheated liquid tar."_

> **Xyan:** _"It is not ordinary tar, Majin. The Maw is pushing upward against Floor 8's foundation gates. An Amber Dusk entity—a Magma Tunneler—has breached the cooling ducts at Node 02."_

> **Majin:** _"Casualties?"_

> **Ishall:** _"None. I relocated the maintenance personnel into the shadow corridors before the blast gates buckled. But the heat is rising. If we don't freeze the core, the hydraulic ballast tanks will boil."_

> **Majin:** _"Deploy Ishall, Xyan, and Park. Xyan, anchor the bedrock with your Desolate flues. Ishall, strike from the shadows. Put the beast to sleep."_

---

### Gameplay — Day 69: Central Command Tactical Interface

```text
{t_box}
```

Shift parameters engaged for Day 69. Daily collection quota increases to **0.200 tons** of pure refined Han. Secret ballast reserves confirm **51.250 tons** stored safely within the cryogenic sub-vaults—advancing beyond the fifty-one ton mark as Cycle 1,778 surges forward.

Operational priorities for Day 69:
1. Conduct safe containment on **SE-C-IIIγ-102** (*The Dancing Chains*).
2. Suppress the Amber Third Watch Ordeal along Floor 7's subterranean vent core.
3. Lock the bedrock foundation to prevent Maw seepage.

#### 1. Pre-Shift Tactical Deployment & Operative Profiles

```text
{roster_box}
```

Director Majin engages the Floor 7 emergency dispatch: **[DAY 69 OPERATIONAL SHIFT COMMENCED]**.

---

#### 2. Granular Work Type Management: Chamber 102 (The Dancing Chains)

Agent Park enters Chamber 102 for Ferrehan containment:
- `[DISPATCH: Agent Park -> Floor 4, Chamber 102]`
- `[PROTOCOL: Ferrehan Endurance (Rhythmic Containment / Weight Affinity)]`

```text
> Chamber Telemetry: "The iron chains sway to the rhythm of human pulse rates..."
> Fear Check: Level V Senior Agent vs Class III Entity -> RESULT: ABSOLUTE CALM.
```

- **Work Tick 01–06:** 6 Successes. Park matches his breathing to the swinging chains.
- **Work Tick 07:** Failure! An iron link whips across Park's shoulder; 5 Red (Grudge) damage sustained (HP: 67/72).
- **Work Tick 08–10:** 3 Successes.
- **Work Result:** **9/10 Positive Han Crystals (EXCELLENT WORK RESULT)!**
- Yield: **+0.032 tons** of refined Han lubricant extracted.

Energy meter climbs to `0.124 / 0.200 tons`.

---

#### 3. Ordeal Manifestation: Third Watch (Amber Dusk) Suppression

At 15:50, the vent floorplates of Floor 7 rupture in a geyser of magma:

```text
{ordeal_box}
```

A colossal, segmented insectoid leviathan plated in superheated basalt chitin erupts at Node 02, spraying molten rock across the corridor!

```text
{hud_t01}
```

##### Turn 01 Action Resolution Log (Spatial Ingress & Bedrock Clash)
- **Operative Movement & Clash Standoff**:
  * **Boundary Vanguard Xyan (Speed 6 -> 3 AP)**: Steps up to Node 04, planting his Desolate flue into the bedrock. Declares `[Bedrock Bulwark Anchor]` (Costs 2 AP).
  * The Magma Tunneler unleashes `[Subterranean Magma Charge]` against Node 04 (Base 10 + 2 Coins = 14 Power).
  * Xyan's Roll:
    * *Passive Trigger:* `Bedrock Anchor` (+2 Base Clash Power).
    * Xyan Roll: Base 11 + 2 Coins = **15 Power**!
  * **Clash Result**: **Xyan WINS THE CLASH (15 vs 14)!**
    * Xyan's heavy mail absorbs the crushing charge, redirecting the kinetic force into the floorplates!
    * Deals 32 Weight damage (HP: 328/360) and inflicts +28 Posture Strain (Posture: 152/180).
  * **Outsider Ishall (Speed 7 -> 4 AP)**: Uses *Shadow Ingress* to teleport to Node 03, driving *Unanswered* into the exposed neck joint: **44 Void Damage**!
  * Tunneler HP drops to **284/360**!

---

```text
{hud_t02}
```

##### Turn 02 Action Resolution Log (Basalt Fracture & Stagger Build)
- **Coordinated Pincer Assault**:
  * Ishall tears open a seam in the basalt plating from behind: **38 Void Damage**!
  * Agent Park hammers the fissure with *Judgment Scale*: **34 Weight Damage**!
  * Tunneler HP falls to **212/360**!
  * Combined Posture strain inflicts +38 points. Posture drops to **76/180**, breaching the **60% Posture Threshold (108 Points)**!
  * **STAGGER LEVEL 1 TRIGGERED!** The magma glow within the beast's carapace dims, and its charging dice are wiped out!

---

```text
{hud_t03}
```

##### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Vanguard Overload (1.5x Direct Damage)**:
  * Agent Park's `Momentum Surge` activates! (+2 Speed next turn). Park executes an overhead smash: **52 Weight Damage**!
  * Outsider Ishall unleashes a relentless void frenzy: **58 Void Damage**!
  * Tunneler HP collapses from 212 to **102/360**! Posture drops to **22/180**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Magma Surge Desperation)
- **Hostile Recovery & Desperation Counter-Surge**:
  * The Magma Tunneler recovers, releasing an explosive burst of molten rock: `[Magma Surge]`.
  * Vanguard Xyan deploys `[Directional Guard Absorption]`, taking 13 chip damage (HP: 162/175) and shielding Park and Ishall completely!
  * Ishall strikes the central magma valve, canceling the secondary explosion!
  * Tunneler HP falls to **46/360**! Posture drops to **6/180**!

---

```text
{hud_t05}
```

##### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Mandible Pin & Terminal Collapse**:
  * Xyan locks the tunneler's mandibles against the bedrock with his heavy flue, stripping the final 6 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/180**. The molten beast collapses motionless, its magma cooling into black glass.

---

```text
{hud_t06}
```

##### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Obsidian Purification**:
  * Agent Park and Outsider Ishall deliver the final synchronized blow. The beast shatters into thousands of smooth obsidian tiles and refined Han vapor.
  * Floor 7 collection flues harvest **+0.025 tons of refined Han**!

Total daily harvest reaches **0.210 / 0.200 tons**! Quota surpassed!

---

#### 4. Shift Evaluation Index & Daily RHR Allocation

```text
{eval_box}
```

---

#### 5. M.A.W. Synthesis & Armament Forging

```text
{forge_box}
```

Boundary Vanguard Xyan equips the *Chained Anchor Blade*, cementing Floor 8's absolute physical perimeter.

---

#### 6. Nocturnal Sub-Vault Telemetry & Director's Vigil

At 02:30, Majin joins Ishall and Xyan in Floor 7's observation nexus. The cooling conduits hum smoothly, all magma drained into the sub-zero cryo-sinks.

Beneath Floor 6, the hydraulic ballast meters verify **51.250 tons** of stored sorrow.

Xyan places a heavy hand on the conduit pipe: *"The bedrock held, brother. Four more days until the White Dusk."*

Majin nods quietly: *"And when the White Dusk comes, we will show them that human sorrow does not surrender."*
"""
    return content

def update_part_4():
    path = "SOMNARAK-WORLD/The_Absolvohan/Part_4_Days_53_to_73.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace Day 53 summary
    old_d53 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Park smashes Spire-A base; Kim covers flank; Spire 60%   |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; direct Grudge damage deals 2.0x; Spire-A |
| shattered.                                                          |
| - Turn 04: Spire-B spawns scuttlers; Hwang uses 2 AP for            |
| suppressing arrow.                                                  |
| - Turn 05: Dekan activates Jaw Clamp, pinning scuttlers at Node 2.  |
| - Turn 06: Park & Kim coordinate Climax Smash; Spire-B collapses to |
| slag.                                                               |
+=====================================================================+
```"""
    if old_d53 in content:
        content = content.replace(old_d53, get_day_53_combat())
        print("Replaced Day 53 summary successfully!")
    else:
        print("Warning: Day 53 summary not found.")

    # Replace Day 55 summary
    old_d55 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Ishall teleports to N01 rear; Park tanks lash; Shroud    |
| 60% Stagger 1.                                                      |
| - Turn 03: Posture broken; all allied attacks deal 2.0x direct      |
| damage; HP at 140.                                                  |
| - Turn 04: Shroud charges [Sanguine Deluge]; Song fires piercing    |
| bolt.                                                               |
| - Turn 05: Ishall executes Void Talons, dissecting shroud mantle    |
| from behind.                                                        |
| - Turn 06: Park unleashes Judgment Climax; Terminal Stagger         |
| dissolves shroud.                                                   |
+=====================================================================+
```"""
    if old_d55 in content:
        content = content.replace(old_d55, get_day_55_combat())
        print("Replaced Day 55 summary successfully!")
    else:
        print("Warning: Day 55 summary not found.")

    # Replace Day 60 summary
    old_d60 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Park hammers thorax; Mellda locks Node 4; Spider 60%     |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; direct Weight/Void strikes deal 2.0x     |
| direct damage.                                                      |
| - Turn 04: Alpha attempts tectonic web burst; Kim burns threads     |
| with carbine.                                                       |
| - Turn 05: Hwang fires Wellspring beam into eye cluster; forces     |
| Terminal Stagger.                                                   |
| - Turn 06: Park executes Climax Smite; Spider dissolves into amber  |
| crystals.                                                           |
+=====================================================================+
```"""
    if old_d60 in content:
        content = content.replace(old_d60, get_day_60_combat())
        print("Replaced Day 60 summary successfully!")
    else:
        print("Warning: Day 60 summary not found.")

    # Replace Day 65 summary
    old_d65 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Song & Hwang snipe Spire-A core; Ayshuk predicts firing  |
| angles.                                                             |
| - Turn 03: Spire-A hits 60% Stagger 1; synchronized arrows shatter  |
| it to slag.                                                         |
| - Turn 04: Spires B & C charge cross-floor beam; Kim activates      |
| stasis shield.                                                      |
| - Turn 05: Hwang unleashes Overdrive Void Lance, fracturing Spire-B |
| core.                                                               |
| - Turn 06: Song executes Climax Volley; Spire-C disintegrates into  |
| ash.                                                                |
+=====================================================================+
```"""
    if old_d65 in content:
        content = content.replace(old_d65, get_day_65_combat())
        print("Replaced Day 65 summary successfully!")
    else:
        print("Warning: Day 65 summary not found.")

    # Insert Day 69 before Day 73
    day_69_text = generate_day_69()
    day_73_marker = "### Day 73"
    if day_73_marker in content:
        content = content.replace(day_73_marker, day_69_text + "\n" + day_73_marker)
        print("Inserted Day 69 successfully before Day 73!")
    else:
        print("Warning: Day 73 marker not found.")

    # Replace Day 73 summary
    old_d73 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Mellda & Dekan absorb wave; Ishall attacks rear; Echo    |
| 60% Stagger 1.                                                      |
| - Turn 03: Defense broken; direct multi-affinity strikes deal 2.0x  |
| direct damage.                                                      |
| - Turn 04: Echo releases [Ancient Ballast Quake]; Dekan locks Jaw   |
| Clamp.                                                              |
| - Turn 05: Ishall executes Unanswered Talon, severing the harmonic  |
| nexus.                                                              |
| - Turn 06: Tri-Lead Climax Strike forces Terminal Stagger; Echo     |
| dissolves.                                                          |
+=====================================================================+
```"""
    if old_d73 in content:
        content = content.replace(old_d73, get_day_73_combat())
        print("Replaced Day 73 summary successfully!")
    else:
        print("Warning: Day 73 summary not found.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated Part 4 successfully!")

if __name__ == "__main__":
    update_part_4()
