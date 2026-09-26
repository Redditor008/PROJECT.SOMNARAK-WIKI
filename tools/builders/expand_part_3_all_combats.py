#!/usr/bin/env python3
"""
tools/expand_part_3_all_combats.py
Replaces the compressed Turns 02-06 summaries on Day 31, Day 36, Day 41, and Day 49
with exhaustive, turn-by-turn tactical combat logs utilizing the 10-node spatial engine,
Four P-framework (Passives, Panic, Parry, Posture), Speed/AP, and M.A.W.-W modifiers.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

# --- DAY 31 EXPANSION ---
def get_day_31_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 2 CORRIDOR SECTOR A]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[POD-1] [HWANG] [POD-2] [SONG]                                  [DEKAN]",
        "---",
        "- Node 01: Sanguine Pod 1 (Posture 38/80 / Central Valve Pierced)",
        "- Node 02: Agent Hwang (Point-Blank Band 1 / Blessed Scalpel Aimed)",
        "- Node 03: Sanguine Pod 2 (Brood Cluster Spawning / Posture 80/80)",
        "- Node 04: Agent Song (Mid-Field Sweeper / Kinetic Cleaver Readied)",
        "- Node 10: Containment Lead Dekan (Bastion Ward Anchor / Band 5)",
        "---",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Agent Song  : Spd 5 -> 3 AP | HP 110/110 | SP +20 | Posture 60/60",
        "- Pod 1       : Spd 3 -> 1 AP | HP 98/160  | Posture 38/80 [STAGGER 1: 48]",
        "- Pod 2       : Spd 4 -> 2 AP | HP 160/160 | Posture 80/80"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[BILE]  [HWANG] [POD-2] [SONG]                                  [DEKAN]",
        "---",
        "- Node 01: Sanguine Pod 1 (RUPTURED & DESTROYED / Siphoned)",
        "- Node 02: Agent Hwang (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 03: Sanguine Pod 2 (Acid Sac Charging / Posture 80/80)",
        "- Node 04: Agent Song (Cleaving Brood Larvae at Node 03-04)",
        "---",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +28 | Posture 55/55",
        "- Agent Song  : Spd 5 -> 3 AP | HP 110/110 | SP +22 | Posture 60/60",
        "- Pod 1       : HP 0/160 [ELIMINATED]",
        "- Pod 2       : Spd 4 -> 2 AP | HP 160/160 | Posture 80/80"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — BROOD ERUPTION & BASTION WARD]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [HWANG] [POD-2] [SONG]                                  [DEKAN]",
        "---",
        "- Node 02: Agent Hwang (Spd 8 / AP 4 / Rapid Suture Thrust)",
        "- Node 03: Sanguine Pod 2 (Posture 42/80 / Carapace Fissuring)",
        "- Node 04: Agent Song (Directional Guard Absorption Active)",
        "---",
        "- Agent Hwang : Spd 8 -> 4 AP [SURGE] | HP 115/115 | SP +28 | Posture 55/55",
        "- Agent Song  : Spd 5 -> 3 AP | HP 106/110 | SP +22 | Posture 52/60",
        "- Pod 2       : Spd 3 -> 1 AP | HP 102/160 | Posture 42/80 [CRACKED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [HWANG] [POD-2]                                         [DEKAN]",
        "                [SONG]",
        "---",
        "- Node 02: Agent Hwang (Pinning Sanguine Conduit / Void Siphon)",
        "- Node 03: Sanguine Pod 2 (TERMINAL STAGGER / POSTURE 0/80 / 2.0x DMG)",
        "- Node 03: Agent Song (Driving Cleaver into Ventral Valve)",
        "---",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +28 | Posture 55/55",
        "- Agent Song  : Spd 5 -> 3 AP | HP 106/110 | SP +22 | Posture 52/60",
        "- Pod 2       : Spd 0 -> 0 AP | HP 28/160  | Posture 0/80 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [HWANG] [ASH]   [SONG]                                  [DEKAN]",
        "---",
        "- Node 02: Agent Hwang (Sheathing Scalpel / Sanitizing Core)",
        "- Node 03: Pod 2 (Vaporized into Red Ash / Han Harvested)",
        "- Node 04: Agent Song (Clearing Sanguine Sludge from Deck)",
        "---",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +35 | Posture 55/55",
        "- Agent Song  : Spd 5 -> 3 AP | HP 106/110 | SP +30 | Posture 60/60",
        "- Pod 2       : HP 0/160 [DESTROYED] | +0.015 TONS REFINED HAN SIPHONED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Stagger Level 1 on Pod 1)
- **Coordinated Pincer Strike**:
  * **Agent Hwang (Speed 6 -> 3 AP)**: Stands at Node 02. Spends 2 AP to execute `[Blessed Scalpel Void Dissection]` targeting Pod 1's ruptured valve.
    * Base Damage 18 * Void Vulnerability (1.5x) = **27 Direct Void Damage**!
    * Inflicts +20 Posture Strain. Pod 1 Posture drops to **18/80**, breaching the **60% Posture Threshold (48 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** Pod 1 ceases pulsing, its acid secretion lines freezing.
  * **Agent Song (Speed 5 -> 3 AP)**: Flanks at Node 04. Spends 2 AP to execute `[Kinetic Cleaver Pincer Sweep]`, cleaving through three emerging larvae broods at Node 03 and dealing **26 kinetic damage** to Pod 2!
  * Pod 1 HP drops from 126 to **71/160**; Pod 2 HP drops to **134/160**.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Pod 1 Destruction & Momentum Surge)
- **Stagger Exploitation & Execution**:
  * With Pod 1 immobilized in Stagger Level 1, all allied attacks deal 1.5x direct damage!
  * **Agent Hwang**: Passive `Momentum Surge` activates upon triggering the stagger! Gains +2 Speed for next turn. Hwang spends 2 AP to deliver a surgical thrust into Pod 1's nucleus:
    * Deals **48 Pure Void Damage**!
    * Pod 1 HP hits **0/160**! The biological sac ruptures with a muffled hiss, disintegrating into inert crimson bile!
  * **Agent Song**: Steps forward to Node 03, swinging the heavy cleaver into Pod 2's flank for **24 Grudge damage**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Brood Eruption & Bastion Guard)
- **Hostile Desperation Counter-Surge**:
  * Pod 2 shakes violently, initiating `[Brood Eruption]`—spraying an acidic bio-blast across Nodes 02, 03, and 04.
  * Containment Lead Dekan channels *The Maw's Keep Bastion Ward* from the observation balcony, absorbing 50% of the acoustic bile.
  * **Agent Song**: Deploys `[Directional Guard Absorption]`, taking only 4 chip damage (HP: 106/110) while shielding Hwang behind her broadsword!
  * **Agent Hwang (Speed 8 under Surge -> 4 AP)**: Strikes twice in rapid succession from Node 02 with the Blessed Scalpel, stripping 38 points of Posture!
  * Pod 2 Posture drops to **42/80**, crossing the Stagger threshold!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Ventral Severance & Terminal Collapse**:
  * Agent Song steps in close to Node 03, delivering a crushing downward cleave to Pod 2's primary anchor root.
  * Posture drops to **0/80**! **TERMINAL STAGGER TRIGGERED!** Pod 2 deflates, completely paralyzed on the deckplates (2.0x direct damage active).
  * Agent Hwang prepares the final siphoning lance.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Purification)
- **Siphon Discharge**:
  * Agent Hwang drives the extraction siphon through the core valve while Agent Song severs the feeder conduits.
  * Pod 2 implodes, all residual larvae dissolving into sparkling red ash and refined Han aerosol!
  * Sector 2 drainage conduits harvest **+0.015 tons of refined Han**!
"""

# --- DAY 36 EXPANSION ---
def get_day_36_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 5 BULWARK GATEWAY]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MONUMENT][MELLDA][PARK]                [HWANG]                 [MAJIN]",
        "---",
        "- Node 01: Gilded Monument (Posture 120/180 / Pedestal Cracked)",
        "- Node 02: Border Lead Mellda (Point-Blank Band 1 / Mantlet Locked)",
        "- Node 03: Agent Park (Range Band 2 / Resonant Requiem Firing)",
        "- Node 06: Agent Hwang (Range Band 3 / Blessed Scalpel Optical Aim)",
        "---",
        "- Mellda      : Spd 5 -> 3 AP | HP 190/190 | SP +30 | Posture 90/90",
        "- Agent Park  : Spd 6 -> 3 AP | HP 120/120 | SP +25 | Posture 60/60",
        "- Agent Hwang : Spd 5 -> 3 AP | HP 110/110 | SP +20 | Posture 55/55",
        "- Monument    : Spd 4 -> 2 AP | HP 260/340 | Posture 120/180 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MONUMENT]      [PARK]                  [HWANG]                 [MAJIN]",
        "        [MELLDA]",
        "---",
        "- Node 01: Gilded Monument (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 02: Border Lead Mellda (Golden Arm-Blade Pincer Sunder)",
        "- Node 03: Agent Park (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 06: Agent Hwang (Discharging High-Density Void Ray)",
        "---",
        "- Mellda      : Spd 5 -> 3 AP | HP 190/190 | SP +30 | Posture 90/90",
        "- Agent Park  : Spd 8 -> 4 AP [SURGE] | HP 120/120 | SP +25 | Posture 60/60",
        "- Agent Hwang : Spd 5 -> 3 AP | HP 110/110 | SP +20 | Posture 55/55",
        "- Monument    : Spd 0 -> 0 AP | HP 130/340 | Posture 45/180 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — OBLIVION TORRENT REACTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MONUMENT][MELLDA][PARK]                [HWANG]                 [MAJIN]",
        "---",
        "- Node 01: Gilded Monument (Recovered / Charging Oblivion Torrent)",
        "- Node 02: Border Lead Mellda (Reflective Bulwark Shield Raised)",
        "- Node 03: Agent Park (Lament Requiem Resonant Shield)",
        "- Node 06: Agent Hwang (Focusing Scalpel on Optical Focal Lens)",
        "---",
        "- Mellda      : Spd 5 -> 3 AP | HP 176/190 | SP +28 | Posture 72/90",
        "- Agent Park  : Spd 6 -> 3 AP | HP 120/120 | SP +25 | Posture 60/60",
        "- Agent Hwang : Spd 5 -> 3 AP | HP 110/110 | SP +20 | Posture 55/55",
        "- Monument    : Spd 4 -> 2 AP | HP 82/340  | Posture 22/180 [FRACTURED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MONUMENT][MELLDA][PARK]                [HWANG]                 [MAJIN]",
        "---",
        "- Node 01: Gilded Monument (TERMINAL STAGGER / POSTURE 0/180 / 2.0x DMG)",
        "- Node 02: Border Lead Mellda (Pinning Pedestal Joint)",
        "- Node 03: Agent Park (Priming Climax Smite)",
        "- Node 06: Agent Hwang (Shattering Optical Crown)",
        "---",
        "- Mellda      : Spd 5 -> 3 AP | HP 176/190 | SP +28 | Posture 72/90",
        "- Agent Park  : Spd 6 -> 3 AP | HP 120/120 | SP +25 | Posture 60/60",
        "- Agent Hwang : Spd 5 -> 3 AP | HP 110/110 | SP +20 | Posture 55/55",
        "- Monument    : Spd 0 -> 0 AP | HP 24/340  | Posture 0/180 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[GOLD-DUST][MELLDA][PARK]               [HWANG]                 [MAJIN]",
        "---",
        "- Node 01: Gilded Monument (Pulverized into Gold Dust & Han Vapor)",
        "- Node 02: Border Lead Mellda (Retracting Shield)",
        "- Node 03: Agent Park (Harvesting Refined Reagents)",
        "- Node 06: Agent Hwang (Logging Archive Telemetry)",
        "---",
        "- Mellda      : Spd 5 -> 3 AP | HP 176/190 | SP +35 | Posture 85/90",
        "- Agent Park  : Spd 6 -> 3 AP | HP 120/120 | SP +30 | Posture 60/60",
        "- Agent Hwang : Spd 5 -> 3 AP | HP 110/110 | SP +25 | Posture 55/55",
        "- Monument    : HP 0/340 [PURIFIED] | +0.022 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Stagger Level 1 on Monument)
- **Tripartite Pressure**:
  * **Border Lead Mellda**: Holds Node 02 in Point-Blank Band 1. Braces *Threshold Vow* against the monument's base, executing `[Threshold Kinetic Anchor]`.
  * **Agent Park**: Firing from Node 03 (Range Band 2), channels `[Lament Requiem Resonant Crush]`:
    * Deals **44 Pure Lament Damage** directly through the structural crack opened in Turn 01!
  * **Agent Hwang**: Targets the optical lens from Node 06 with a focused Void beam for **28 Void damage**.
  * Gilded Monument HP drops to **188/340**!
  * Posture drops to **68/180**, breaching the **60% Posture Threshold (108 Points)**!
  * **STAGGER LEVEL 1 TRIGGERED!** The monument's prismatic crown dims, and its charging dice are wiped out for Turn 03!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Allied Focus Fire (1.5x Direct Damage)**:
  * Agent Park's `Momentum Surge` triggers! Gains +2 Speed for next turn. Park drives the acoustic hammer deep into the monument's core: **58 Lament Damage**!
  * Border Lead Mellda delivers a sweeping two-handed cleave: **34 Grudge Damage**!
  * Monument HP collapses from 188 to **96/340**! Posture drops to **24/180**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Oblivion Torrent Desperation Blast)
- **Hostile Recovery & Desperation Counter-Surge**:
  * The Gilded Monument recovers, unleashing its maximum-aperture area laser: `[Oblivion Torrent]` sweeping down the central corridor.
  * Mellda deploys `[Directional Guard Absorption]`, taking 14 chip damage (HP: 176/190) and absorbing 75% of the laser energy to protect Park and Hwang behind her!
  * Agent Hwang targets the glowing lens from Range Band 3, firing `[Blessed Scalpel Void Incision]`: the beam pierces the crystal optic, shattering the lens and canceling the high-yield follow-up!
  * Monument HP drops to **42/340**! Posture falls to **10/180**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Optical Shatter & Terminal Collapse**:
  * Mellda drives *Threshold Vow* through the foundation pedestal, stripping the remaining 10 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/180**. The monument's golden plating peels away, its stone core crumbling onto the deckplates.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Purification)
- **Final Subdual**:
  * Agent Park executes `[Requiem Climax: Smite of Absolution]`. The acoustic hammer shatters the monument into a shower of shimmering golden dust and refined Han vapor!
  * Floor 5 collection flues siphon the harvest: **+0.022 tons of refined Han secured**!
"""

# --- DAY 41 EXPANSION ---
def get_day_41_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 5 GATEWAY SLUICE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[HIVE]          [MELLDA][HWANG]         [BAE]                   [MAJIN]",
        "---",
        "- Node 01-02: Churning Trench Hive (Posture 130/200 / Mandible Locked)",
        "- Node 03: Border Lead Mellda (Bulwark Stance / Threshold Vow Ready)",
        "- Node 04: Agent Hwang (Void Scalpel Precision / Range Band 2)",
        "- Node 06: Agent Bae (Bulwark Great-Maul Primed / Range Band 3)",
        "---",
        "- Mellda      : Spd 5 -> 3 AP | HP 190/190 | SP +30 | Posture 95/95",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Agent Bae   : Spd 5 -> 3 AP | HP 125/125 | SP +20 | Posture 70/70",
        "- Trench Hive : Spd 4 -> 2 AP | HP 302/380 | Posture 130/200 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[HIVE]  [HWANG] [MELLDA]                [BAE]                   [MAJIN]",
        "---",
        "- Node 01-02: Trench Hive (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 02: Agent Hwang (Driving Scalpel into Exposed Ventral Nerve)",
        "- Node 03: Border Lead Mellda (Holding Primary Mandibles)",
        "- Node 05: Agent Bae (Advancing with Great-Maul / Momentum Surge)",
        "---",
        "- Mellda      : Spd 5 -> 3 AP | HP 190/190 | SP +30 | Posture 95/95",
        "- Agent Hwang : Spd 8 -> 4 AP [SURGE] | HP 115/115 | SP +25 | Posture 55/55",
        "- Agent Bae   : Spd 5 -> 3 AP | HP 125/125 | SP +20 | Posture 70/70",
        "- Trench Hive : Spd 0 -> 0 AP | HP 168/380 | Posture 52/200 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — TECTONIC BURROW ATTEMPT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[HIVE]  [HWANG] [MELLDA][BAE]                                   [MAJIN]",
        "---",
        "- Node 01-02: Trench Hive (Recovered / Channeling Tectonic Burrow)",
        "- Node 02: Agent Hwang (Slicing Chitinous Leg Joints)",
        "- Node 03: Border Lead Mellda (Jaw Clamp Pin Engaged)",
        "- Node 04: Agent Bae (Executing Bulwark Maul Ground Breaker)",
        "---",
        "- Mellda      : Spd 5 -> 3 AP | HP 182/190 | SP +28 | Posture 80/95",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Agent Bae   : Spd 5 -> 3 AP | HP 125/125 | SP +20 | Posture 70/70",
        "- Trench Hive : Spd 3 -> 1 AP | HP 112/380 | Posture 24/200 [TRAPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[HIVE]  [HWANG] [MELLDA][BAE]                                   [MAJIN]",
        "---",
        "- Node 01-02: Trench Hive (TERMINAL STAGGER / POSTURE 0/200 / 2.0x DMG)",
        "- Node 02: Agent Hwang (Severing Central Nerve Cord)",
        "- Node 03: Border Lead Mellda (Executing Threshold Execution Slice)",
        "- Node 04: Agent Bae (Grounding Kinetic Shockwave)",
        "---",
        "- Mellda      : Spd 5 -> 3 AP | HP 182/190 | SP +28 | Posture 80/95",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +25 | Posture 55/55",
        "- Agent Bae   : Spd 5 -> 3 AP | HP 125/125 | SP +20 | Posture 70/70",
        "- Trench Hive : Spd 0 -> 0 AP | HP 34/380  | Posture 0/200 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[AMBER-DUST]    [MELLDA][HWANG] [BAE]                           [MAJIN]",
        "---",
        "- Node 01-02: Trench Hive (Dissolved into Inert Amber Dust)",
        "- Node 03: Border Lead Mellda (Locking Gateway Portcullis)",
        "- Node 04: Agent Hwang (Disinfecting Corridor Conduits)",
        "- Node 05: Agent Bae (Siphoning Refined Reagents)",
        "---",
        "- Mellda      : Spd 5 -> 3 AP | HP 182/190 | SP +35 | Posture 90/95",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 115/115 | SP +30 | Posture 55/55",
        "- Agent Bae   : Spd 5 -> 3 AP | HP 125/125 | SP +25 | Posture 70/70",
        "- Trench Hive : HP 0/380 [PURIFIED] | +0.025 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Carapace Crack & Stagger Build)
- **Trench Lockdown & Flanking Strike**:
  * Mellda holds Gate 05 closed, locking the centipede's anterior armor plates with *Threshold Vow*.
  * Agent Hwang maneuvers to Node 02 behind the centipede's flank, driving the Blessed Scalpel into the ventral joint: **38 Void Damage**!
  * Agent Bae winds up the Bulwark Great-Maul from Node 06, delivering a ground-shaking kinetic slam: **32 Weight Damage**!
  * Trench Hive HP drops to **232/380**!
  * Posture drops to **78/200**, breaching the **60% Posture Threshold (120 Points)**!
  * **STAGGER LEVEL 1 TRIGGERED!** The centipede's hundreds of legs tremble, and its burrowing drill stalls!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Allied Focus Fire (1.5x Direct Damage)**:
  * Agent Hwang's `Momentum Surge` activates! (+2 Speed next turn). Hwang delivers three consecutive scalpel incisions into the central nerve cluster: **64 Void Damage**!
  * Mellda cleaves through two armored dorsal segments: **38 Grudge Damage**!
  * Hive HP plummets from 232 to **130/380**! Posture drops to **24/200**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Tectonic Burrow Desperation)
- **Hostile Recovery & Desperation Burrow**:
  * The Trench Hive recovers, attempting to drill through the bedrock with `[Tectonic Burrow]` to bypass the blast gates.
  * Containment Lead Dekan deploys Floor 2's *Jaw Clamp* hydraulic clamps through the grates, pinning the centipede's thorax!
  * Mellda deploys `[Directional Guard Absorption]`, taking 8 chip damage (HP: 182/190) and preventing the beast from submerging!
  * Agent Bae smashes the exposed dorsal nerve for **34 Weight damage**!
  * Hive HP falls to **62/380**! Posture drops to **8/200**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Ventral Nerve Severance & Terminal Collapse**:
  * Mellda and Bae land a synchronized heavy blow, shattering the creature's cephalic plate!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/200**. The beast collapses motionless across Nodes 01 and 02.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Threshold Execution**:
  * Mellda executes `[Threshold Severance: Edge of Dawn]`. The massive centipede dissolves into glowing amber dust and pure Han vapor.
  * Gateway drainage flues harvest **+0.025 tons of refined Han**!
"""

# --- DAY 49 EXPANSION ---
def get_day_49_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — LOWER ARCHIVE ELEVATOR SHAFT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SHADOW][MARJUK]        [HWANG] [PARK]                          [MAJIN]",
        "---",
        "- Node 01: Weeping Shadow (Posture 115/170 / Stasis Fog Frozen)",
        "- Node 02: Archive Lead Marjuk (Point-Blank Band 1 / Stasis Seal)",
        "- Node 04: Agent Hwang (Void Scalpel / Range Band 2)",
        "- Node 05: Agent Park (Lament Requiem Resonant Beam / Range Band 3)",
        "---",
        "- Marjuk      : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 90/90",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 120/120 | SP +25 | Posture 60/60",
        "- Agent Park  : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 65/65",
        "- Weeping Shadow: Spd 4 -> 2 AP | HP 280/360 | Posture 115/170 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SHADOW][MARJUK]        [HWANG] [PARK]                          [MAJIN]",
        "---",
        "- Node 01: Weeping Shadow (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 02: Archive Lead Marjuk (Applying Chronological Seal)",
        "- Node 04: Agent Hwang (Executing Void Disruption)",
        "- Node 05: Agent Park (Momentum Surge Primed / +2 Speed Next Turn)",
        "---",
        "- Marjuk      : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 90/90",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 120/120 | SP +25 | Posture 60/60",
        "- Agent Park  : Spd 8 -> 4 AP [SURGE] | HP 125/125 | SP +30 | Posture 65/65",
        "- Shadow      : Spd 0 -> 0 AP | HP 142/360 | Posture 40/170 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — SHATTERED MEMORY SURGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SHADOW][MARJUK][HWANG]         [PARK]                          [MAJIN]",
        "---",
        "- Node 01: Weeping Shadow (Recovered / Chanting Shattered Memory Surge)",
        "- Node 02: Archive Lead Marjuk (Deploying Chrono-Shield)",
        "- Node 03: Agent Hwang (Slicing Acoustic Echo Cord)",
        "- Node 05: Agent Park (Lament Firing Line)",
        "---",
        "- Marjuk      : Spd 5 -> 3 AP | HP 172/180 | SP +32 | Posture 76/90",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 120/120 | SP +25 | Posture 60/60",
        "- Agent Park  : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 65/65",
        "- Shadow      : Spd 4 -> 2 AP | HP 84/360  | Posture 18/170 [UNSTABLE]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SHADOW][MARJUK][HWANG] [PARK]                                  [MAJIN]",
        "---",
        "- Node 01: Weeping Shadow (TERMINAL STAGGER / POSTURE 0/170 / 2.0x DMG)",
        "- Node 02: Archive Lead Marjuk (Locking Temporal Stasis Box)",
        "- Node 03: Agent Hwang (Void Disruption Climax)",
        "- Node 04: Agent Park (Acoustic Resonance Climax)",
        "---",
        "- Marjuk      : Spd 5 -> 3 AP | HP 172/180 | SP +32 | Posture 76/90",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 120/120 | SP +25 | Posture 60/60",
        "- Agent Park  : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 65/65",
        "- Shadow      : Spd 0 -> 0 AP | HP 20/360  | Posture 0/170 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MIST]  [MARJUK][HWANG] [PARK]                                  [MAJIN]",
        "---",
        "- Node 01: Weeping Shadow (Dissolved into Pale Mnemonic Mist)",
        "- Node 02: Archive Lead Marjuk (Storing Crystallized Memory)",
        "- Node 03: Agent Hwang (Recording Historical Ledger)",
        "- Node 04: Agent Park (Harvesting Refined Reagents)",
        "---",
        "- Marjuk      : Spd 5 -> 3 AP | HP 172/180 | SP +40 | Posture 85/90",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 120/120 | SP +30 | Posture 60/60",
        "- Agent Park  : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Shadow      : HP 0/360 [PURIFIED] | +0.028 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Stasis Lock & Stagger Build)
- **Tripartite Resonance Strike**:
  * **Archive Lead Marjuk**: Holds Node 02 in Point-Blank Band 1. Spends 2 AP to maintain *The Temporal Stasis Array*, freezing the lower elevator shaft in chronological amber.
  * The Weeping Shadow attempts `[Chrono-Lament Wail]`, but Marjuk's stasis array turns the pulse back into the projection!
  * **Agent Hwang**: From Node 04 (Range Band 2), discharges `[Whispering Needle Piercing Void]`: **36 Void Damage**!
  * **Agent Park**: From Node 05 (Range Band 3), unleashes a resonant Lament beam: **32 Damage**!
  * Weeping Shadow HP drops to **212/360**!
  * Posture drops to **68/170**, crossing the **60% Posture Threshold (102 Points)**!
  * **STAGGER LEVEL 1 TRIGGERED!** The shadow's projection wavers and flickers out of phase!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Allied Focus Fire (1.5x Direct Damage)**:
  * Agent Park's `Momentum Surge` activates! (+2 Speed next turn). Park unleashes a direct point-blank acoustic smash: **54 Lament Damage**!
  * Agent Hwang targets the projection's harmonic heart: **44 Void Damage**!
  * Shadow HP collapses from 212 to **114/360**! Posture drops to **22/170**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Shattered Memory Surge)
- **Hostile Desperation Surge**:
  * The Weeping Shadow recovers, radiating a high-frequency mnemonic scream: `[Shattered Memory Surge]`.
  * Marjuk deploys `[Directional Guard Absorption]`, taking 8 chip damage (HP: 172/180) and shielding Hwang and Park from psychological feedback!
  * Hwang and Park coordinate counter-fire, stripping another 14 points of Posture and driving HP down to **52/360**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Temporal Box Lock & Terminal Collapse**:
  * Marjuk slams the stasis casing shut around the projection's focal core, stripping the final 8 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/170**. The shadow dissolves into slow-motion crystalline tears.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Purification)
- **Mnemonic Purification**:
  * Agent Park, Agent Hwang, and Archive Lead Marjuk execute a synchronized three-way purge.
  * The Weeping Shadow dissolves into pure, sweet-smelling mnemonic mist and glittering Han crystals.
  * Floor 6 pneumatic flues harvest **+0.028 tons of refined Han**!
"""

def update_all_part_3():
    path = "SOMNARAK-WORLD/The_Absolvohan/Part_3_Days_29_to_49.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Day 31 summary replacement
    old_d31 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Hwang pierces Pod 1; triggers 60% Stagger 1; Song flanks |
| N04.                                                                |
| - Turn 03: All allied attacks deal 2.0x direct damage; Pod 1        |
| destroyed.                                                          |
| - Turn 04: Pod 2 spawns brood cluster; Dekan engages Bastion Ward.  |
| - Turn 05: Song sweeps Node 2 with kinetic arc; forces Terminal     |
| Stagger.                                                            |
| - Turn 06: Hwang executes Climax Siphon; all larvae vaporize into   |
| red ash.                                                            |
+=====================================================================+
```"""
    if old_d31 in content:
        content = content.replace(old_d31, get_day_31_combat())
        print("Replaced Day 31 summary successfully!")
    else:
        print("Warning: Day 31 summary not found.")

    # Day 36 summary replacement
    old_d36 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Mellda locks N02; Park delivers 44 Lament; Monument 60%  |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; all allied attacks deal 2.0x direct      |
| damage; HP at 130.                                                  |
| - Turn 04: Monument charges corridor laser [Oblivion Torrent];      |
| Mellda shields.                                                     |
| - Turn 05: Hwang pierces Void focal lens from N06, canceling        |
| high-yield blast.                                                   |
| - Turn 06: Park unleashes Climax Smite; Terminal Stagger shatters   |
| monument.                                                           |
+=====================================================================+
```"""
    if old_d36 in content:
        content = content.replace(old_d36, get_day_36_combat())
        print("Replaced Day 36 summary successfully!")
    else:
        print("Warning: Day 36 summary not found.")

    # Day 41 summary replacement
    old_d41 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Mellda locks Gate 5; Hwang flanks N02; Hive hits 60%     |
| Stagger 1.                                                          |
| - Turn 03: Carapace cracked; all attacks deal 2.0x direct damage;   |
| HP at 150.                                                          |
| - Turn 04: Hive attempts tectonic burrow; Dekan engages Jaw Clamp   |
| pin.                                                                |
| - Turn 05: Bae lands heavy maul strike on ventral nerve; forces     |
| Terminal Stagger.                                                   |
| - Turn 06: Mellda executes Threshold Execution; Hive dissolves to   |
| amber dust.                                                         |
+=====================================================================+
```"""
    if old_d41 in content:
        content = content.replace(old_d41, get_day_41_combat())
        print("Replaced Day 41 summary successfully!")
    else:
        print("Warning: Day 41 summary not found.")

    # Day 49 summary replacement
    old_d49 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Marjuk freezes Node 1; Hwang & Park strike; Echo 60%     |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; all 4-affinity strikes deal 2.0x direct  |
| damage.                                                             |
| - Turn 04: Echo attempts dimensional toll; Xyan deploys Singularity |
| Well.                                                               |
| - Turn 05: Park executes Flerehan resonance, purging the sorrow     |
| harmonic.                                                           |
| - Turn 06: Marjuk & Xyan coordinate terminal lockdown; Echo         |
| dissolves.                                                          |
+=====================================================================+
```"""
    if old_d49 in content:
        content = content.replace(old_d49, get_day_49_combat())
        print("Replaced Day 49 summary successfully!")
    else:
        print("Warning: Day 49 summary not found.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated Part 3 with all combat expansions successfully!")

if __name__ == "__main__":
    update_all_part_3()
