#!/usr/bin/env python3
"""
tools/expand_part_6.py
Expands Part 6 (Days 101 to 121) into an exhaustive operational chronicle:
- Full turn-by-turn combat logs for Day 101, 103, 108, 113, 121 across Turns 02 to 06.
- Inserts Day 117 (Maw Resonance & Amber Dusk Sediment Behemoth Suppression).
- Enforces 100% box symmetry and dual-environment typography (<= 71 chars for boxes).
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

# --- DAY 101 EXPANSION ---
def get_day_101_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 1 WEST DORMITORY CORRIDOR]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SILHOUETTE][KANG]       [PARK]                  [SEIYON]        [MAJIN]",
        "---",
        "- Node 01: Lead Silhouette (Posture 54/120 / Dream Lattice Pierced)",
        "- Node 02: Agent Kang (Point-Blank Band 1 / Heavy Maul Cleaving)",
        "- Node 04: Agent Park (Range Band 2 / Resonant Requiem Firing)",
        "- Node 08: Secretary Seiyon (Sync Directive / Band 4)",
        "- Node 10: Director Majin Command Terminal (Band 5)",
        "---",
        "- Agent Kang   : Spd 6 -> 3 AP | HP 135/135 | SP +30 | Posture 75/75",
        "- Agent Park   : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Silhouette   : Spd 4 -> 2 AP | HP 184/280 | Posture 54/120 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SILHOUETTE]    [KANG]  [PARK]                  [SEIYON]        [MAJIN]",
        "---",
        "- Node 01: Lead Silhouette (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 03: Agent Kang (Advancing with Momentum Surge / +2 Speed)",
        "- Node 04: Agent Park (Channeling Pure Lament Wave)",
        "---",
        "- Agent Kang   : Spd 8 -> 4 AP [SURGE] | HP 135/135 | SP +30 | Posture 75/75",
        "- Agent Park   : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Silhouette   : Spd 0 -> 0 AP | HP 96/280  | Posture 20/120 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — SLEEP MIST VENTING & BASTION WARD]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SILHOUETTE][KANG]       [PARK]                  [SEIYON]        [MAJIN]",
        "---",
        "- Node 01: Silhouette (Recovered / Venting Heavy Somnolent Mist)",
        "- Node 02: Agent Kang (Directional Guard Absorption Active)",
        "- Node 04: Agent Park (Flerehan Acoustic Pulse Purging Fog)",
        "---",
        "- Agent Kang   : Spd 8 -> 4 AP | HP 128/135 | SP +30 | Posture 66/75",
        "- Agent Park   : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Silhouette   : Spd 3 -> 1 AP | HP 48/280  | Posture 8/120 [WEAKENED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SILHOUETTE]                                    [SEIYON]        [MAJIN]",
        "        [KANG]  [PARK]",
        "---",
        "- Node 01: Silhouette (TERMINAL STAGGER / POSTURE 0/120 / 2.0x DMG)",
        "- Node 02: Agent Kang (Pinning Spectral Throat)",
        "- Node 03: Agent Park (Priming Resonant Requiem Siphon)",
        "---",
        "- Agent Kang   : Spd 6 -> 3 AP | HP 128/135 | SP +30 | Posture 66/75",
        "- Agent Park   : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Silhouette   : Spd 0 -> 0 AP | HP 14/280  | Posture 0/120 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MIST]  [KANG]  [PARK]                          [SEIYON]        [MAJIN]",
        "---",
        "- Node 01: Lead Silhouette (Dissolved to Gray Mist / Siphoned)",
        "- Node 02: Agent Kang (Resting Maul / Checking Corridor Air)",
        "- Node 03: Agent Park (Confirming Dormitory Personnel Safe)",
        "---",
        "- Agent Kang   : Spd 6 -> 3 AP | HP 128/135 | SP +35 | Posture 75/75",
        "- Agent Park   : Spd 6 -> 3 AP | HP 125/125 | SP +40 | Posture 65/65",
        "- Silhouette   : HP 0/280 [PURIFIED] | +0.024 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Silhouette Stagger Build)
- **Vanguard Impact & Flerehan Pulse**:
  * **Agent Kang (Speed 6 -> 3 AP)**: Smashes the lead silhouette's dream lattice at Node 02:
    * Deals **42 Grudge Damage**!
    * Inflicts +34 Posture Strain. Silhouette Posture drops to **54/120**, breaching the **60% Posture Threshold (72 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The phantom's somnolent aura fractures.
  * **Agent Park**: Firing from Node 04 with the Lament Requiem, deals **36 direct Lament damage**.
  * Silhouette HP falls to **154/280**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Allied Focus Fire (1.5x Direct Damage)**:
  * Agent Kang's `Momentum Surge` activates! (+2 Speed next turn). Kang delivers a crushing downward smite: **58 Grudge Damage**!
  * Agent Park channels a high-frequency harmonic beam: **44 Damage**!
  * Silhouette HP collapses from 154 to **52/280**! Posture drops to **14/120**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Sleep Mist Venting & Bastion Ward)
- **Hostile Desperation Counter-Surge**:
  * The Silhouette recovers, venting heavy somnolent mist to put all nearby personnel into a coma: `[Somnolent Fog]`.
  * Containment Lead Dekan activates Floor 2's *Bastion Ward* relays, neutralizing the chemical toxin!
  * Agent Kang deploys `[Directional Guard Absorption]`, absorbing 7 chip damage (HP: 128/135) while holding the frontline!
  * Agent Park executes a non-lethal acoustic wave, completely dispersing the mental fog!
  * Silhouette Posture drops to **6/120**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Throat Pin & Terminal Collapse**:
  * Kang locks the phantom's spectral throat with the maul haft, stripping the remaining 6 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/120**. The entity dissolves into slow-motion gray vapor.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Maul Cleave**:
  * Kang executes `[Climax Maul Cleave]`. The lead silhouette shatters into harmless gray fog and pure Han crystals.
  * Floor 1 collection flues harvest **+0.024 tons of refined Han**!
"""

# --- DAY 103 EXPANSION ---
def get_day_103_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 3 REFINERY CONDUIT CORE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[COG]   [ZYRAK] [YOO]                   [MARJUK]                [MAJIN]",
        "---",
        "- Node 01: Ancient Cog (Posture 52/130 / Drive Axle Pierced)",
        "- Node 02: Extraction Lead Zyrak (Thermal Lance Thrust Landed)",
        "- Node 03: Agent Yoo (Range Band 2 / Lock Maul Kinetic Cleave)",
        "- Node 06: Archive Lead Marjuk (Range Band 3 / Pre-Charging Stasis)",
        "---",
        "- Zyrak       : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 85/85",
        "- Agent Yoo   : Spd 6 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Marjuk      : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 90/90",
        "- Ancient Cog : Spd 3 -> 1 AP | HP 182/280 | Posture 52/130 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[COG]   [ZYRAK]         [YOO]           [MARJUK]                [MAJIN]",
        "---",
        "- Node 01: Ancient Cog (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 02: Extraction Lead Zyrak (Overheating Axle Bearings)",
        "- Node 04: Agent Yoo (Advancing with Momentum Surge / +2 Speed)",
        "- Node 06: Archive Lead Marjuk (Deploying Stasis Clamp)",
        "---",
        "- Zyrak       : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 85/85",
        "- Agent Yoo   : Spd 8 -> 4 AP [SURGE] | HP 130/130 | SP +30 | Posture 70/70",
        "- Marjuk      : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 90/90",
        "- Cog         : Spd 0 -> 0 AP | HP 98/280  | Posture 20/130 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — THERMAL SUPER-TORQUE COUNTER-SURGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[COG]   [ZYRAK] [YOO]                   [MARJUK]                [MAJIN]",
        "---",
        "- Node 01: Ancient Cog (Recovered / Channeling Thermal Super-Torque)",
        "- Node 02: Extraction Lead Zyrak (Directional Guard Absorption)",
        "- Node 03: Agent Yoo (Kinetic Counter-Smash Cracking Axle)",
        "- Node 06: Archive Lead Marjuk (Applying Stasis Clamp to Flywheel)",
        "---",
        "- Zyrak       : Spd 5 -> 3 AP | HP 172/180 | SP +35 | Posture 75/85",
        "- Agent Yoo   : Spd 8 -> 4 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Cog         : Spd 4 -> 2 AP | HP 44/280  | Posture 8/130 [CRITICAL]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[COG]                                                           [MAJIN]",
        "        [ZYRAK] [YOO]                   [MARJUK]",
        "---",
        "- Node 01: Ancient Cog (TERMINAL STAGGER / POSTURE 0/130 / 2.0x DMG)",
        "- Node 02: Extraction Lead Zyrak (Priming Climax Thermal Lance)",
        "- Node 03: Agent Yoo (Cracking Central Drive Shaft)",
        "---",
        "- Zyrak       : Spd 5 -> 3 AP | HP 172/180 | SP +35 | Posture 75/85",
        "- Agent Yoo   : Spd 6 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Cog         : Spd 0 -> 0 AP | HP 12/280  | Posture 0/130 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SLAG]  [ZYRAK] [YOO]                   [MARJUK]                [MAJIN]",
        "---",
        "- Node 01: Ancient Cog (Detonated Safely / Slag Siphoned into Flues)",
        "- Node 02: Extraction Lead Zyrak (Venting Lance Heat)",
        "- Node 03: Agent Yoo (Logging Kinetic Impact)",
        "---",
        "- Zyrak       : Spd 5 -> 3 AP | HP 172/180 | SP +40 | Posture 85/85",
        "- Agent Yoo   : Spd 6 -> 3 AP | HP 130/130 | SP +35 | Posture 70/70",
        "- Cog         : HP 0/280 [PURIFIED] | +0.024 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Axle Pierce & Stagger Build)
- **Thermal Sunder & Axle Smash**:
  * **Extraction Lead Zyrak**: Drives the high-heat thermal lance directly through the cog's central drive axle at Node 02:
    * Deals **44 Grudge Damage**!
    * Inflicts +36 Posture Strain. Cog Posture drops to **52/130**, breaching the **60% Posture Threshold (78 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The spinning gear teeth seize in a shower of white sparks.
  * **Agent Yoo**: Smashes the peripheral gear train with the heavy maul for **34 kinetic damage**.
  * Cog HP falls to **152/280**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Vanguard Overload (1.5x Direct Damage)**:
  * Agent Yoo's `Momentum Surge` activates! (+2 Speed next turn). Yoo delivers an overhead smash directly onto the jammed gear teeth: **58 Damage**!
  * Zyrak melts the internal bearings with thermal spray: **46 Damage**!
  * Cog HP drops to **48/280**! Posture drops to **14/130**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Thermal Super-Torque Desperation)
- **Hostile Desperation Counter-Surge**:
  * The Ancient Cog attempts to break free with `[Thermal Super-Torque]`, spinning its gear teeth at blinding velocity.
  * Zyrak deploys `[Directional Guard Absorption]`, taking 8 chip damage (HP: 172/180) while shielding Yoo.
  * Marjuk locks the stasis clamp over the outer rim, slowing rotation!
  * Yoo lands a crushing blow, cracking the drive axle in half!
  * Cog HP falls to **16/280**! Posture drops to **2/130**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Shaft Shatter & Terminal Collapse**:
  * Yoo delivers a final blow, stripping the last 2 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/130**. The gear splits down its diameter, collapsing onto the deckplates.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Thermal Pierce**:
  * Zyrak executes `[Climax Thermal Pierce]`. The core detonates inside the stasis field, dissolving into melted slag and refined Han vapor.
  * Floor 3 collection flues harvest **+0.024 tons of refined Han**!
"""

# --- DAY 108 EXPANSION ---
def get_day_108_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 5 TRANSIT GATE 05]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[STALKER][MELLDA][CHA]                   [PARK]                  [MAJIN]",
        "---",
        "- Node 01: Lead Stalker (Posture 48/120 / Pinned by Mellda)",
        "- Node 02: Border Lead Mellda (Point-Blank Band 1 / Bulwark Locked)",
        "- Node 03: Agent Cha (Range Band 2 / Cryo-Quench Spray Firing)",
        "- Node 06: Agent Park (Range Band 3 / Lament Requiem Aimed)",
        "---",
        "- Mellda      : Spd 6 -> 3 AP | HP 195/195 | SP +35 | Posture 95/95",
        "- Agent Cha   : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 65/65",
        "- Agent Park  : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Stalker     : Spd 4 -> 2 AP | HP 182/280 | Posture 48/120 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[STALKER]        [MELLDA][CHA]           [PARK]                  [MAJIN]",
        "---",
        "- Node 01: Lead Stalker (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 03: Border Lead Mellda (Momentum Surge Primed / +2 Speed)",
        "- Node 04: Agent Cha (Cryo-Quench Shell Freezing Chitin)",
        "- Node 06: Agent Park (Lament Requiem Resonant Smash Fired)",
        "---",
        "- Mellda      : Spd 8 -> 4 AP [SURGE] | HP 195/195 | SP +35 | Posture 95/95",
        "- Agent Cha   : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 65/65",
        "- Agent Park  : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Stalker     : Spd 0 -> 0 AP | HP 88/280  | Posture 18/120 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — REFUGEE FLANK ATTEMPT & GATE LOCK]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[STALKER][MELLDA][CHA]                   [PARK]                  [MAJIN]",
        "---",
        "- Node 01: Stalker (Recovered / Attempting Flank toward Gate 05)",
        "- Node 02: Border Lead Mellda (Locking Transit Portcullis)",
        "- Node 03: Agent Cha (Directional Guard Absorption / Freezing Nodes)",
        "- Node 06: Agent Park (Piercing Acoustic Volley Firing)",
        "---",
        "- Mellda      : Spd 8 -> 4 AP | HP 188/195 | SP +35 | Posture 85/95",
        "- Agent Cha   : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 65/65",
        "- Agent Park  : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Stalker     : Spd 3 -> 1 AP | HP 38/280  | Posture 6/120 [TRAPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[STALKER]                                                        [MAJIN]",
        "        [MELLDA][CHA]                   [PARK]",
        "---",
        "- Node 01: Stalker (TERMINAL STAGGER / POSTURE 0/120 / 2.0x DMG)",
        "- Node 02: Border Lead Mellda (Threshold Blade Locked into Throat)",
        "- Node 03: Agent Cha (Cryo Freeze Complete / Charcoal Shell)",
        "---",
        "- Mellda      : Spd 6 -> 3 AP | HP 188/195 | SP +35 | Posture 85/95",
        "- Agent Cha   : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 65/65",
        "- Stalker     : Spd 0 -> 0 AP | HP 10/280  | Posture 0/120 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[ASH]   [MELLDA][CHA]                   [PARK]                  [MAJIN]",
        "---",
        "- Node 01: Stalkers (Shattered to Ash / Siphoned into Flues)",
        "- Node 02: Border Lead Mellda (Checking Refugee Seals)",
        "- Node 03: Agent Cha (Clearing Ice Shards)",
        "---",
        "- Mellda      : Spd 6 -> 3 AP | HP 188/195 | SP +40 | Posture 95/95",
        "- Agent Cha   : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Stalkers    : HP 0/280 [PURIFIED] | +0.024 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Stalker Pin & Cryo Stagger Build)
- **Pin & Cryo Quench**:
  * Mellda pins the lead stalker against Gate 05's reinforced bulkheads at Node 02.
  * Agent Cha unleashes high-pressure cryo spray from the Forge Bracer:
    * Deals **38 Thermal/Cryo Damage**!
    * Inflicts +32 Posture Strain. Stalker Posture drops to **46/120**, breaching the **60% Posture Threshold (72 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The stalker's exoskeleton freezes into brittle charcoal.
  * Stalker HP drops to **142/280**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Cryo-Quench Focus (1.5x Direct Damage)**:
  * Mellda's `Momentum Surge` activates! (+2 Speed next turn). Mellda drives the golden arm-blade through the frozen thorax: **56 Grudge Damage**!
  * Agent Park delivers a resonant Lament smash: **44 Damage**!
  * Stalker HP collapses from 142 to **42/280**! Posture drops to **12/120**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Refugee Flank Attempt & Gate Lock)
- **Hostile Desperation Flank**:
  * Secondary stalkers attempt to scramble past Node 02 toward the Cheonbulok refugee shelter.
  * Mellda slams the portcullis shut, blocking the corridor!
  * Agent Cha deploys `[Directional Guard Absorption]`, taking 7 chip damage (HP: 188/195) while freezing all remaining stalkers at Node 02 into brittle charcoal!
  * Stalker HP falls to **14/280**! Posture drops to **2/120**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Throat Pin & Terminal Collapse**:
  * Mellda locks the lead stalker's throat with *Threshold Vow*, stripping the final 2 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/120**.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Spear Sweep**:
  * Mellda executes `[Climax Spear Sweep]`. The frozen stalkers shatter into harmless charcoal dust and refined Han vapor.
  * Gate collection flues harvest **+0.024 tons of refined Han**!
"""

# --- DAY 113 EXPANSION ---
def get_day_113_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 4 CENTRAL RESEARCH FORGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CORE]  [KANG]          [YOON]  [HONG]                  [AYSHUK]        ",
        "---",
        "- Node 01: Solar Core (Posture 56/140 / Cooled by Dual Weeping)",
        "- Node 02: Agent Kang (Point-Blank Band 1 / Shield Mantlet Raised)",
        "- Node 04: Agent Yoon (Range Band 2 / Harmonic Lament Wave Firing)",
        "- Node 05: Agent Hong (Range Band 3 / Choral Staff Echo Firing)",
        "- Node 08: Research Lead Ayshuk (Predicting Thermal-Psychic Nodes)",
        "---",
        "- Agent Kang   : Spd 6 -> 3 AP | HP 135/135 | SP +30 | Posture 75/75",
        "- Agent Yoon   : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Agent Hong   : Spd 5 -> 3 AP | HP 120/120 | SP +35 | Posture 60/60",
        "- Solar Core   : Spd 4 -> 2 AP | HP 210/320 | Posture 56/140 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CORE]          [KANG]  [YOON]  [HONG]                  [AYSHUK]        ",
        "---",
        "- Node 01: Solar Core (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 03: Agent Kang (Advancing with Momentum Surge / +2 Speed)",
        "- Node 04: Agent Yoon (Discharging High-Frequency Lament Beam)",
        "- Node 05: Agent Hong (Dual Choral Pulses Converging)",
        "---",
        "- Agent Kang   : Spd 8 -> 4 AP [SURGE] | HP 135/135 | SP +30 | Posture 75/75",
        "- Agent Yoon   : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Agent Hong   : Spd 5 -> 3 AP | HP 120/120 | SP +35 | Posture 60/60",
        "- Core         : Spd 0 -> 0 AP | HP 112/320 | Posture 22/140 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — PALE PULSE COUNTER-SURGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CORE]  [KANG]          [YOON]  [HONG]                  [AYSHUK]        ",
        "---",
        "- Node 01: Solar Core (Recovered / Channeling 20% Max HP Pale Pulse)",
        "- Node 02: Agent Kang (Directional Guard Absorption Active)",
        "- Node 04: Agent Yoon (Dampening Vibration with Tear Veil)",
        "- Node 08: Research Lead Ayshuk (Identifying Thermal-Psychic Node)",
        "---",
        "- Agent Kang   : Spd 8 -> 4 AP | HP 122/135 | SP +30 | Posture 62/75",
        "- Agent Yoon   : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Core         : Spd 3 -> 1 AP | HP 48/320  | Posture 8/140 [UNSTABLE]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CORE]                                                  [AYSHUK]        ",
        "        [KANG]          [YOON]  [HONG]",
        "---",
        "- Node 01: Solar Core (TERMINAL STAGGER / POSTURE 0/140 / 2.0x DMG)",
        "- Node 02: Agent Kang (Locking Baseplate Clamp)",
        "- Node 04: Agent Yoon (Thermal Damping Complete)",
        "---",
        "- Agent Kang   : Spd 6 -> 3 AP | HP 122/135 | SP +30 | Posture 62/75",
        "- Core         : Spd 0 -> 0 AP | HP 12/320  | Posture 0/140 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[STAR]  [KANG]          [YOON]  [HONG]                  [AYSHUK]        ",
        "---",
        "- Node 01: Solar Core (Dissolved to Starlight & Han Vapor / Siphoned)",
        "- Node 02: Agent Kang (Resting Climax Maul)",
        "- Node 04: Agent Yoon (Logging Thermal Equilibrium)",
        "---",
        "- Agent Kang   : Spd 6 -> 3 AP | HP 122/135 | SP +35 | Posture 75/75",
        "- Core         : HP 0/320 [PURIFIED] | +0.026 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Dual Weeping & Solar Core Stagger)
- **Cooling Volley & Stagger Build**:
  * Agent Yoon and Agent Hong channel dual Lament weeping from Nodes 04 and 05, cooling the solar core's thermal corona:
    * Deals **44 Pure Lament Damage**!
    * Inflicts +36 Posture Strain. Core Posture drops to **52/140**, breaching the **60% Posture Threshold (84 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The miniature sun dims from blinding white to cool indigo.
  * Core HP drops to **166/320**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Vanguard Overload (1.5x Direct Damage)**:
  * Agent Kang's `Momentum Surge` activates! (+2 Speed next turn). Kang delivers a crushing downward smite into the containment ring: **56 Damage**!
  * Yoon and Hong discharge synchronized beams: **48 Damage**!
  * Core HP collapses from 166 to **62/320**! Posture drops to **14/140**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Pale Pulse Desperation)
- **Hostile Desperation Counter-Surge**:
  * The Solar Core recovers, pulsing a 20% Max HP Pale shockwave across all nodes.
  * Agent Kang deploys `[Directional Guard Absorption]`, taking 13 chip damage (HP: 122/135) and grounding the pulse!
  * Research Lead Ayshuk identifies the thermal-psychic node, allowing Yoon to dampen the acoustic resonance.
  * Core Posture drops to **4/140**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Baseplate Lock & Terminal Collapse**:
  * Kang locks the baseplate clamp, stripping the final 4 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/140**.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Maul Finisher**:
  * Kang strikes the baseplate with the Climax Maul. The solar core dissolves into glittering starlight and pure refined Han vapor.
  * Floor 4 collection flues harvest **+0.026 tons of refined Han**!
"""

# --- DAY 121 EXPANSION ---
def get_day_121_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 1 CENTRAL SPIRE SANCTUARY]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SHARD] [KANG]                                          [SEIYON][MAJIN]",
        "---",
        "- Node 01: Reality Shard (Posture 72/160 / Apex Smashed by Kang)",
        "- Node 02: Agent Kang (Point-Blank Band 1 / Heavy Maul Cleaving)",
        "- Node 09: Secretary Seiyon (Sync Directive Active / Band 5)",
        "- Node 10: Director Majin (Tactical Command Rerolls Engaged)",
        "---",
        "- Agent Kang   : Spd 6 -> 3 AP | HP 140/140 | SP +35 | Posture 80/80",
        "- Shard        : Spd 4 -> 2 AP | HP 220/340 | Posture 72/160 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SHARD]         [KANG]                                  [SEIYON][MAJIN]",
        "---",
        "- Node 01: Reality Shard (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 03: Agent Kang (Advancing with Momentum Surge / +2 Speed)",
        "- Node 10: Director Majin (Coordinating Siphon Array)",
        "---",
        "- Agent Kang   : Spd 8 -> 4 AP [SURGE] | HP 140/140 | SP +35 | Posture 80/80",
        "- Shard        : Spd 0 -> 0 AP | HP 116/340 | Posture 24/160 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — TECTONIC REALITY SHEAR COUNTER-SURGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SHARD] [KANG]                                          [SEIYON][MAJIN]",
        "---",
        "- Node 01: Reality Shard (Recovered / Channeling Reality Shear)",
        "- Node 02: Agent Kang (Directional Guard Absorption Active)",
        "- Node 10: Director Majin (Deploying Veil Mist Dampener)",
        "---",
        "- Agent Kang   : Spd 8 -> 4 AP | HP 132/140 | SP +35 | Posture 70/80",
        "- Shard        : Spd 3 -> 1 AP | HP 48/340  | Posture 8/160 [FRACTURED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SHARD]                                                 [SEIYON][MAJIN]",
        "        [KANG]",
        "---",
        "- Node 01: Reality Shard (TERMINAL STAGGER / POSTURE 0/160 / 2.0x DMG)",
        "- Node 02: Agent Kang (Shattering Outer Crystalline Lattice)",
        "---",
        "- Agent Kang   : Spd 6 -> 3 AP | HP 132/140 | SP +35 | Posture 70/80",
        "- Shard        : Spd 0 -> 0 AP | HP 12/340  | Posture 0/160 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SAND]  [KANG]                                          [SEIYON][MAJIN]",
        "---",
        "- Node 01: Reality Shard (Crumbled to Purple Sand / Siphoned)",
        "- Node 02: Agent Kang (Resting Climax Maul / Sector Clear)",
        "---",
        "- Agent Kang   : Spd 6 -> 3 AP | HP 132/140 | SP +40 | Posture 80/80",
        "- Shard        : HP 0/340 [PURIFIED] | +0.028 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Apex Smash & Stagger Build)
- **Direct Kinetic Sunder**:
  * Agent Kang smashes the shard's crystalline apex with the heavy maul at Node 02:
    * Deals **48 Grudge Damage**!
    * Inflicts +38 Posture Strain. Shard Posture drops to **58/160**, breaching the **60% Posture Threshold (96 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The geometric distortion wavers and fractures.
  * Director Majin uses tactical command to reroll speed dice for optimal positioning.
  * Shard HP drops to **172/340**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Vanguard Overload (1.5x Direct Damage)**:
  * Agent Kang's `Momentum Surge` activates! (+2 Speed next turn). Kang delivers an overhead smash: **68 Grudge Damage**!
  * Shard HP collapses from 172 to **56/340**! Posture drops to **16/160**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Tectonic Reality Shear Desperation)
- **Hostile Desperation Counter-Surge**:
  * The Reality Shard recovers, attempting `[Tectonic Reality Shear]` to warp the central command floorplates.
  * Director Majin deploys the *Veil Mist Dampener*, stabilizing local physics!
  * Agent Kang deploys `[Directional Guard Absorption]`, taking 8 chip damage (HP: 132/140).
  * Kang executes a kinetic counter-strike, shattering the outer lattice!
  * Shard HP drops to **16/340**! Posture drops to **2/160**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Lattice Collapse & Terminal Stagger**:
  * Kang delivers a sweeping blow, stripping the final 2 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/160**.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Maul Shatter**:
  * Kang unleashes `[Climax Maul Shatter]`. The Reality Shard crumbles into shimmering purple sand and pure Han vapor.
  * Central command flues harvest **+0.028 tons of refined Han**!
"""

# --- DAY 117 GENERATOR ---
def generate_day_117():
    t_box = make_box("REVERIE DIRECTORATE — CENTRAL COMMAND TERMINAL", [
        "FACILITY MANAGEMENT INTERFACE: DAY 117 SHIFT",
        "ENERGY HARVEST QUOTA  : 0.280 TONS // CURRENT HARVEST: 0.000 TONS",
        "COVERT BALLAST RESERVE : 53.850 TONS [HYDRAULIC CRYO-VAULTS]",
        "ACTIVE CONTAINMENT    : SE-001, 005, 008 (MAW SIPHON), 033, 102",
        "MAW TELEMETRY         : WHISPERS OF CHEONBULOK MARTYRS ACCELERATING"
    ])

    roster_box = make_box("DEPLOYED ROSTER: DAY 117 MAW PACIFICATION SQUAD", [
        "AGENT & RATING        | STATS, GEAR & FOUR P-FRAMEWORK SPEC",
        "----------------------+-----------------------------------------------",
        "Containment Lead Dekan| HP 210| SP 80 | Work 70 | Speed 5 (3 AP Base)",
        "Floor 2 Decision Core | M.A.W.-W: Basalt Siphon (Weight / Heavy / 2 AP)",
        "Ward of the Maw       | Suit: Maw Trench Mail (Heavy / Spd 0 under Aura)",
        "                      | Posture: 105/105 | Guard: 24 Absorb | Pass: Maw Ward",
        "                      | Panic Typology: Berserk (SP <= -40)",
        "----------------------+-----------------------------------------------",
        "Extraction Lead Zyrak | HP 185| SP 78 | Work 68 | Speed 6 (3 AP + 1 Move)",
        "Floor 3 Decision Core | M.A.W.-W: Thermal Lance (Grudge / Medium / 1 AP)",
        "Forge Commander       | Suit: Crucible Mail (Medium / Spd +1 under Aura)",
        "                      | Posture: 90/90 | Parry: 18 Power | Pass: Forge Heat",
        "                      | Panic Typology: Despair (SP <= -35)",
        "----------------------+-----------------------------------------------",
        "Agent Kang (Grade V)  | HP 140| SP 78 | Work 66 | Speed 6 (3 AP + 1 Move)",
        "Senior Breacher       | M.A.W.-W: Climax Maul (Grudge / Heavy / 2 AP)",
        "Floor 2 Assigned      | Suit: Chitin Carapace Mail (Heavy / Spd +1)",
        "                      | Posture: 80/80 | Guard: 18 Absorb | Pass: Momentum Surge",
        "                      | Panic Typology: Berserk (SP <= -35)"
    ])

    ordeal_box = make_box("TACTICAL DOSSIER: AMBER DUSK ORDEAL SUPPRESSION", [
        "DESIGNATION           : THE SEDIMENT BEHEMOTH (AMBER DUSK)",
        "CLASSIFICATION        : AMBER (WEIGHT/GRUDGE) THIRD WATCH HOSTILE",
        "INTRUSION POINT       : FLOOR 2 BASALT SIPHON VAULT (NODE 02)",
        "HOSTILE PARAMETERS    : HP 400/400 | Posture 200/200 | Speed 4 (2 AP)",
        "ATTACK AFFINITY       : Weight / Tremor (Compressive Silt Shock)",
        "AFFINITY VULNERABILITY: Grudge (Physical: 1.5x) & Lament (White: 1.25x)",
        "SPECIAL THREAT        : Mudslide eruption drags operatives 2 nodes",
        "TACTICAL ORDERS       : ANCHOR AT NODE 02; CRUSH SEDIMENT CARAPACE"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 2 BASALT SIPHON VAULT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [BEHEM] [DEKAN] [ZYRAK] [KANG]                          [MAJIN]",
        "---",
        "SPATIAL RANGES & POSITIONS:",
        "- Node 02: Sediment Behemoth (Basalt Mudslide Eruption Epicenter)",
        "- Node 03: Containment Lead Dekan (Frontline Anchor / Band 1)",
        "- Node 04: Extraction Lead Zyrak (Thermal Mid-Field / Band 2)",
        "- Node 05: Agent Kang (Senior Breacher / Heavy Maul / Band 3)",
        "- Node 10: Director Majin & Seiyon Command Console (Band 5)",
        "---",
        "OPERATIVE STATUS & RESOURCE POOLS:",
        "- Dekan       : Spd 5 -> 3 AP | HP 210/210 | SP 80/80 | Posture 105/105",
        "- Zyrak       : Spd 6 -> 3 AP | HP 185/185 | SP 78/78 | Posture 90/90",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 140/140 | SP 78/78 | Posture 80/80",
        "- Behemoth    : Spd 4 -> 2 AP | HP 400/400 | Posture 200/200"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — CRACKING THE SEDIMENT CARAPACE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [BEHEM] [DEKAN] [ZYRAK] [KANG]                          [MAJIN]",
        "---",
        "- Node 02: Sediment Behemoth (Posture 124/200 / Anterior Shell Cracked)",
        "- Node 03: Containment Lead Dekan (Basalt Siphon Parry Executed)",
        "- Node 04: Extraction Lead Zyrak (Thermal Spray Melting Silt)",
        "- Node 05: Agent Kang (Climax Maul Sunder Landed)",
        "---",
        "- Dekan       : Spd 5 -> 3 AP | HP 210/210 | SP 80/80 | Posture 105/105",
        "- Zyrak       : Spd 6 -> 3 AP | HP 185/185 | SP 78/78 | Posture 90/90",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 140/140 | SP 78/78 | Posture 80/80",
        "- Behemoth    : Spd 3 -> 1 AP | HP 302/400 | Posture 124/200 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [BEHEM]         [ZYRAK] [KANG]                          [MAJIN]",
        "        [DEKAN]",
        "---",
        "- Node 02: Sediment Behemoth (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 02: Containment Lead Dekan (Driving Siphon into Heart Core)",
        "- Node 04: Extraction Lead Zyrak (Overheating Mud Armor)",
        "- Node 05: Agent Kang (Momentum Surge Primed / +2 Speed Next Turn)",
        "---",
        "- Dekan       : Spd 5 -> 3 AP | HP 210/210 | SP 80/80 | Posture 105/105",
        "- Zyrak       : Spd 6 -> 3 AP | HP 185/185 | SP 78/78 | Posture 90/90",
        "- Agent Kang  : Spd 8 -> 4 AP [SURGE] | HP 140/140 | SP 78/78 | Posture 80/80",
        "- Behemoth    : Spd 0 -> 0 AP | HP 168/400 | Posture 46/200 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MUDSLIDE ERUPTION COUNTER-SURGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [BEHEM] [DEKAN] [ZYRAK] [KANG]                          [MAJIN]",
        "---",
        "- Node 02: Sediment Behemoth (Recovered / Channeling Mudslide Eruption)",
        "- Node 03: Containment Lead Dekan (Directional Guard Absorption Active)",
        "- Node 04: Extraction Lead Zyrak (Thermal Blast Evaporating Mud)",
        "- Node 05: Agent Kang (Spd 8 / AP 4 / Heavy Maul Sunder)",
        "---",
        "- Dekan       : Spd 5 -> 3 AP | HP 198/210 | SP 76/80 | Posture 90/105",
        "- Zyrak       : Spd 6 -> 3 AP | HP 185/185 | SP 78/78 | Posture 90/90",
        "- Agent Kang  : Spd 8 -> 4 AP | HP 140/140 | SP 78/78 | Posture 80/80",
        "- Behemoth    : Spd 4 -> 2 AP | HP 84/400  | Posture 20/200 [UNSTABLE]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [BEHEM]                                                 [MAJIN]",
        "        [DEKAN] [ZYRAK] [KANG]",
        "---",
        "- Node 02: Sediment Behemoth (TERMINAL STAGGER / POSTURE 0/200 / 2.0x DMG)",
        "- Node 02: Containment Lead Dekan (Jaw Clamp Pinning Anterior Tusk)",
        "- Node 03: Extraction Lead Zyrak (Thermal Lance Overdrive)",
        "- Node 04: Agent Kang (Priming Climax Execution)",
        "---",
        "- Dekan       : Spd 5 -> 3 AP | HP 198/210 | SP 76/80 | Posture 90/105",
        "- Zyrak       : Spd 6 -> 3 AP | HP 185/185 | SP 78/78 | Posture 90/90",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 140/140 | SP 78/78 | Posture 80/80",
        "- Behemoth    : Spd 0 -> 0 AP | HP 20/400  | Posture 0/200 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [SILT]  [DEKAN] [ZYRAK] [KANG]                          [MAJIN]",
        "---",
        "- Node 02: Sediment Behemoth (Dissolved into River Silt / Siphoned)",
        "- Node 03: Containment Lead Dekan (Venting Basalt Siphon)",
        "- Node 04: Extraction Lead Zyrak (Securing RHR Reagents)",
        "- Node 05: Agent Kang (Reporting Siphon Vault Clear)",
        "---",
        "- Dekan       : Spd 5 -> 3 AP | HP 198/210 | SP 80/80 | Posture 100/105",
        "- Zyrak       : Spd 6 -> 3 AP | HP 185/185 | SP +40 | Posture 90/90",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 140/140 | SP +40 | Posture 80/80",
        "- Behemoth    : HP 0/400 [PURIFIED] | +0.030 TONS REFINED HAN HARVESTED"
    ])

    eval_box = make_box("END-OF-DAY PERFORMANCE EVALUATION: DAY 117", [
        "METRIC                 | TARGET QUOTA   | REALIZED PERFORMANCE",
        "-----------------------+----------------+---------------------",
        "Han Energy Harvested   | 0.280 Tons     | 0.292 Tons [SURPASSED]",
        "Containment Breaches   | 0 Breaches Max | 0 Breaches [CLEARED]",
        "Personnel Casualties   | 0 Fatalities   | 0 Fatalities [PERFECT]",
        "Amber Dusk Suppressed  | 1/1 Suppressed | 100% Rate [RESOLVED]",
        "Maw Siphon Synchronized| 100% Stable    | TAR BACK-PRESSURE ZERO",
        "-----------------------+----------------+---------------------",
        "SHIFT PERFORMANCE GRADE: GRADE S (MAW DEFENDER MASTER)",
        "REAGENTS ACCUMULATED   : +38 RHR (REFINED HAN REAGENTS)",
        "OPERATIVE ADVANCEMENT  :",
        "- Containment Dekan   : +5 Resilience, +3 Composure (Maw Guardian)",
        "- Extraction Zyrak    : +5 Composure, +3 Resolve (Forge Master)",
        "- Agent Kang          : +4 Resilience, +3 Clarity (Senior Bulwark)"
    ])

    forge_box = make_box("M.A.W. SYNTHESIS FORGING LOG — DAY 117", [
        "FORGE SPECIFICATION    | SLOT / PROPERTIES / PARAMETERS",
        "-----------------------+----------------------------------------------",
        "Basalt Great-Maul      | Weapon: 9-14 Weight (Heavy / Speed Delta -1)",
        "                       | Range Band 1 | 2 AP | Inflicts +30% Posture",
        "Siphon Basin Mail      | Suit: Heavy Armor (Speed Delta -1)",
        "                       | Resist: 0.5 Grudge / 0.7 Lament / 0.5 Weight",
        "Maw Tusk Brooch        | Chest Slot: +12 HP, +10% Tremor Nullification",
        "-----------------------+----------------------------------------------",
        "EQUIPMENT ALLOCATION   | BESTOWED UPON AGENT KANG (SENIOR BREACHER)"
    ])

    content = f"""
### Day 117

### Story — Dialogue

> **Dekan:** _"The Maw has begun to sing the old names, Director. Not whispers anymore. A chorus."_

> **Majin:** _"Which names?"_

> **Dekan:** _"The miners of the Fourth Sub-Vault. The children who starved in Sector 9 before the Before-Time ended. And beneath them... an Amber Dusk behemoth has risen through the basalt siphon pipes on Floor 2."_

> **Zyrak:** _"It brought three hundred tons of river silt with it. If that mud clogs our extraction turbines, the entire floor will overheat."_

> **Majin:** _"Take Dekan and Kang. Zyrak, boil the silt with your thermal lances. Dekan, lock the creature's tusks with your basalt siphon. Kang will deliver the hammer."_

---

### Gameplay — Day 117: Central Command Tactical Interface

```text
{t_box}
```

Shift parameters engaged for Day 117. Daily harvest quota climbs to **0.280 tons** of pure refined Han. Secret ballast reserves confirm **53.850 tons** stored safely within the cryogenic sub-vaults—advancing past the fifty-three ton threshold as the facility nears the mid-cycle crisis.

Operational priorities for Day 117:
1. Maintain safe siphoning on **SE-C-Iα-008** (*The Maw*).
2. Suppress the Amber Third Watch Ordeal along Floor 2's basalt siphon vault.
3. Advance veteran operative proficiencies using the Four P-Framework.

#### 1. Pre-Shift Tactical Deployment & Operative Profiles

```text
{roster_box}
```

Director Majin engages the Floor 2 emergency valves: **[DAY 117 OPERATIONAL SHIFT COMMENCED]**.

---

#### 2. Granular Work Type Management: Chamber 008 (The Maw's Siphon Core)

Containment Lead Dekan conducts Pugnahan calibration at the Maw's edge:
- `[DISPATCH: Dekan -> Floor 2, Chamber 008]`
- `[PROTOCOL: Pugnahan Calibration (Combat Siphon / Weight Affinity)]`

```text
> Chamber Telemetry: "The black tar churns violently, roaring the names of the dead..."
> Fear Check: Level V Echo-Core Lead vs Sovereign Entity -> RESULT: ABSOLUTE CALM.
```

- **Work Tick 01–06:** 6 Successes. Dekan drives the basalt siphon into the tar.
- **Work Tick 07:** Failure! A tar tendril lashes his chest; 6 Black (Weight) damage sustained (SP: 74/80).
- **Work Tick 08–10:** 3 Successes.
- **Work Result:** **9/10 Positive Han Crystals (EXCELLENT WORK RESULT)!**
- Yield: **+0.038 tons** of refined Han lubricant extracted.

Energy meter climbs to `0.178 / 0.280 tons`.

---

#### 3. Ordeal Manifestation: Third Watch (Amber Dusk) Suppression

At 16:10, boiling river silt floods the Floor 2 siphon vault:

```text
{ordeal_box}
```

A towering, quad-tusked behemoth plated in fossilized basalt silt crashes through the vault grates at Node 02, spraying boiling mud across the corridor!

```text
{hud_t01}
```

##### Turn 01 Action Resolution Log (Spatial Ingress & Bulwark Clash)
- **Operative Movement & Clash Standoff**:
  * **Containment Lead Dekan (Speed 5 -> 3 AP)**: Steps up to Node 03, planting his basalt siphon into the floorplates. Declares `[Basalt Siphon Parry]` (Costs 2 AP).
  * The Sediment Behemoth unleashes `[Tectonic Mudslide Charge]` against Node 03 (Base 10 + 2 Coins = 14 Power).
  * Dekan's Roll:
    * *Passive Trigger:* `Maw Ward` (+2 Base Clash Power).
    * Dekan Roll: Base 12 + 2 Coins = **16 Power**!
  * **Clash Result**: **Dekan WINS THE CLASH (16 vs 14)!**
    * The basalt siphon locks the creature's primary tusk, diverting the mudslide into the drainage flues!
    * Deals 36 Weight damage (HP: 364/400) and inflicts +32 Posture Strain (Posture: 168/200).
  * **Extraction Lead Zyrak (Speed 6 -> 3 AP)**: From Node 04, fires `[Thermal Spray]`, boiling the mud armor: **42 Grudge Damage**!
  * **Agent Kang**: Smashes with *Climax Maul* for **34 damage**. Behemoth HP drops to **288/400**!

---

```text
{hud_t02}
```

##### Turn 02 Action Resolution Log (Shell Fissure & Stagger Build)
- **Coordinated Vanguard Strike**:
  * Zyrak melts the anterior silt plating: **38 Grudge Damage**!
  * Agent Kang drives the heavy maul into the softened shell: **46 Damage**!
  * Behemoth HP drops to **204/400**!
  * Combined Posture strain inflicts +44 points. Posture drops to **80/200**, breaching the **60% Posture Threshold (120 Points)**!
  * **STAGGER LEVEL 1 TRIGGERED!** The behemoth's tusks droop, its mud armor cracking open!

---

```text
{hud_t03}
```

##### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Vanguard Overload (1.5x Direct Damage)**:
  * Agent Kang's `Momentum Surge` activates! (+2 Speed next turn). Kang delivers a crushing downward smite: **64 Grudge Damage**!
  * Dekan drives the basalt siphon deep into the exposed heart core: **56 Damage**!
  * Behemoth HP collapses from 204 to **84/400**! Posture drops to **20/200**!

---

```text
{hud_t04}
```

##### Turn 04 Action Resolution Log (Mudslide Eruption Desperation)
- **Hostile Desperation Counter-Surge**:
  * The Sediment Behemoth recovers, unleashing `[Mudslide Eruption]` to drown the vault.
  * Dekan deploys `[Directional Guard Absorption]`, taking 12 chip damage (HP: 198/210) while anchoring Zyrak and Kang!
  * Zyrak superheats the mud with thermal blast, evaporating the mudslide before it can reach the turbines!
  * Behemoth HP drops to **36/400**! Posture falls to **6/200**!

---

```text
{hud_t05}
```

##### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Tusk Pin & Terminal Collapse**:
  * Dekan clamps the creature's anterior tusk in Floor 2's hydraulic locks, stripping the final 6 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/200**. The beast collapses onto the silt-covered grates.

---

```text
{hud_t06}
```

##### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Final Subdual**:
  * Kang and Dekan execute a synchronized execution blow. The behemoth crumbles into smooth river silt and refined Han vapor.
  * Floor 2 drainage flues harvest **+0.030 tons of refined Han**!

Total daily harvest reaches **0.292 / 0.280 tons**! Quota surpassed!

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

Agent Kang equips the *Basalt Great-Maul*, establishing himself as Floor 2's supreme physical frontline breacher.

---

#### 6. Nocturnal Sub-Vault Telemetry & Director's Vigil

At 02:15, Majin walks along the observation catwalk overlooking the Maw's basin with Dekan. The black tar has calmed, its surface glossy like dark obsidian.

Beneath Floor 6, the hydraulic ballast meters verify **53.850 tons** of stored sorrow.

Dekan speaks quietly: *"Four days until Day 121, Majin. The reality shards are beginning to gather around Floor 1."*

Majin places his hand upon the iron railing: *"Let them gather. In cycle 1,778, reality does not fracture us. We rewrite it."*
"""
    return content

def update_part_6():
    path = "SOMNARAK-WORLD/The_Absolvohan/Part_6_Days_101_to_121.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Day 101 summary
    old_d101 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Kang smashes lead silhouette; Park pierces N01; 60%      |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; direct Grudge strikes deal 2.0x direct   |
| damage.                                                             |
| - Turn 04: Silhouettes vent heavy sleep mist; Dekan activates       |
| Bastion Ward.                                                       |
| - Turn 05: Park executes Flerehan acoustic pulse, clearing mental   |
| fog.                                                                |
| - Turn 06: Kang unleashes Climax Maul Cleave; entities dissolve to  |
| gray mist.                                                          |
+=====================================================================+
```"""
    if old_d101 in content:
        content = content.replace(old_d101, get_day_101_combat())
        print("Replaced Day 101 summary successfully!")
    else:
        print("Warning: Day 101 summary not found.")

    # Day 103 summary
    old_d103 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Zyrak pierces axle; Yoo hammers teeth; Cog 60% Stagger   |
| 1.                                                                  |
| - Turn 03: Posture broken; direct Grudge blunt strikes deal 2.0x    |
| direct damage.                                                      |
| - Turn 04: Cog charges [Thermal Super-Torque]; Marjuk deploys       |
| stasis clamp.                                                       |
| - Turn 05: Yoo executes kinetic counter-smash, cracking central     |
| axle in half.                                                       |
| - Turn 06: Zyrak unleashes Climax Thermal Pierce; core detonates    |
| safely.                                                             |
+=====================================================================+
```"""
    if old_d103 in content:
        content = content.replace(old_d103, get_day_103_combat())
        print("Replaced Day 103 summary successfully!")
    else:
        print("Warning: Day 103 summary not found.")

    # Day 108 summary
    old_d108 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Mellda pins lead stalker; Cha unleashes cryo spray; 60%  |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; cryo-quench strikes deal 2.0x direct     |
| damage.                                                             |
| - Turn 04: Stalkers attempt flank toward refugees; Mellda locks     |
| Gate 05.                                                            |
| - Turn 05: Cha freezes remaining stalkers into brittle charcoal at  |
| Node 2.                                                             |
| - Turn 06: Mellda executes Climax Spear Sweep; all entities shatter |
| to ash.                                                             |
+=====================================================================+
```"""
    if old_d108 in content:
        content = content.replace(old_d108, get_day_108_combat())
        print("Replaced Day 108 summary successfully!")
    else:
        print("Warning: Day 108 summary not found.")

    # Day 113 summary
    old_d113 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Yoon & Hong channel dual weeping; cool solar core; 60%   |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; all 4 damage types deal 2.0x direct      |
| damage.                                                             |
| - Turn 04: Core charges [20% Max HP Pale Pulse]; Kang braces behind |
| shield.                                                             |
| - Turn 05: Ayshuk identifies thermal-psychic node; Yoon dampens     |
| vibration.                                                          |
| - Turn 06: Kang strikes baseplate with Climax Maul; core dissolves  |
| to starlight.                                                       |
+=====================================================================+
```"""
    if old_d113 in content:
        content = content.replace(old_d113, get_day_113_combat())
        print("Replaced Day 113 summary successfully!")
    else:
        print("Warning: Day 113 summary not found.")

    # Insert Day 117 before Day 121
    day_117_text = generate_day_117()
    day_121_marker = "### Day 121"
    if day_121_marker in content:
        content = content.replace(day_121_marker, day_117_text + "\n" + day_121_marker)
        print("Inserted Day 117 successfully before Day 121!")
    else:
        print("Warning: Day 121 marker not found.")

    # Day 121 summary
    old_d121 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Kang smashes apex; Majin rerolls speed; Shard hits 60%   |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; direct Grudge blunt strikes deal 2.0x    |
| direct damage.                                                      |
| - Turn 04: Shard attempts [Tectonic Reality Shear]; Majin deploys   |
| Veil Mist.                                                          |
| - Turn 05: Kang executes kinetic surge, shattering outer            |
| crystalline lattice.                                                |
| - Turn 06: Kang unleashes Climax Maul Shatter; Shard crumbles to    |
| purple sand.                                                        |
+=====================================================================+
```"""
    if old_d121 in content:
        content = content.replace(old_d121, get_day_121_combat())
        print("Replaced Day 121 summary successfully!")
    else:
        print("Warning: Day 121 summary not found.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated Part 6 successfully!")

if __name__ == "__main__":
    update_part_6()
