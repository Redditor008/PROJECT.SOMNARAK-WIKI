#!/usr/bin/env python3
"""
tools/expand_part_2.py
Expands Part 2 (Days 1 to 25) into an exhaustive operational chronicle:
- Full turn-by-turn combat logs for Day 1, 5, 7, 12, 17 across Turns 02 to 06.
- Enforces 100% box symmetry and dual-environment typography (<= 71 chars for boxes).
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

# --- DAY 1 EXPANSION ---
def get_day_1_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — CORRIDOR EAST FUNGAL INTERCEPT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SPORE-A][KIM]   [SPORE-B][PARK]  [LEE]                   [CLERK]         ",
        "---",
        "- Node 01: Spore Carrier A (Posture 38/100 / Locked by Kim's Fang)",
        "- Node 02: Agent Kim (Point-Blank Band 1 / Embrace Fang Vicious Guard)",
        "- Node 03: Spore Carrier B (Venting Spores / Posture 100/100)",
        "- Node 04: Agent Park (Range Band 2 / Lament Requiem Harmonic Blast)",
        "- Node 05: Agent Lee (Range Band 3 / Activating Air Scrubbers)",
        "- Node 08: Clerk Dormitory Entrance (Protected)",
        "---",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 115/115 | SP +30 | Posture 65/65",
        "- Agent Park  : Spd 6 -> 3 AP | HP 110/110 | SP +35 | Posture 60/60",
        "- Agent Lee   : Spd 4 -> 2 AP | HP 105/105 | SP +25 | Posture 55/55",
        "- Spore A     : Spd 3 -> 1 AP | HP 98/180  | Posture 38/100 [CRACKED]",
        "- Spore B     : Spd 3 -> 1 AP | HP 180/180 | Posture 100/100"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER ON SPORE A]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[ASH]    [KIM]   [SPORE-B][PARK]  [LEE]                   [CLERK]         ",
        "---",
        "- Node 01: Spore Carrier A (SPORES DISSOLVED / Ash Siphoned)",
        "- Node 02: Agent Kim (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 03: Spore Carrier B (Exposed / Posture 54/100)",
        "- Node 04: Agent Park (Lament Beam Piercing Fungal Core)",
        "---",
        "- Agent Kim   : Spd 7 -> 4 AP [SURGE] | HP 115/115 | SP +30 | Posture 65/65",
        "- Agent Park  : Spd 6 -> 3 AP | HP 110/110 | SP +35 | Posture 60/60",
        "- Spore A     : HP 0/180 [DESTROYED]",
        "- Spore B     : Spd 2 -> 1 AP | HP 122/180 | Posture 54/100 [ENGAGED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — TOXIC CLOUD VENTING & AIR SCRUBBER LOCK]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [KIM]   [SPORE-B][PARK]  [LEE]                   [CLERK]         ",
        "---",
        "- Node 03: Spore Carrier B (Venting Toxic Cloud / Blinded by Scrubbers)",
        "- Node 02: Agent Kim (Directional Guard Absorption Active)",
        "- Node 04: Agent Park (Harmonic Choral Wave Charging)",
        "- Node 05: Agent Lee (Air Scrubber System at 100% Suction)",
        "---",
        "- Agent Kim   : Spd 7 -> 4 AP | HP 110/115 | SP +30 | Posture 58/65",
        "- Agent Park  : Spd 6 -> 3 AP | HP 110/110 | SP +35 | Posture 60/60",
        "- Spore B     : Spd 2 -> 1 AP | HP 64/180  | Posture 16/100 [POISONED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER ON SPORE B]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                [SPORE-B]                                [CLERK]         ",
        "                [KIM]    [PARK]  [LEE]",
        "---",
        "- Node 03: Spore Carrier B (TERMINAL STAGGER / POSTURE 0/100 / 2.0x DMG)",
        "- Node 03: Agent Kim (Fang Blade Penetrating Main Stem)",
        "- Node 04: Agent Park (Acoustic Resonance Disintegrating Hyphae)",
        "---",
        "- Spore B     : Spd 0 -> 0 AP | HP 14/180  | Posture 0/100 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                [PURIFIED][KIM]  [PARK]  [LEE]           [CLERK]         ",
        "---",
        "- Node 03: Spores (Completely Dissolved to Ash / Purged by Scrubbers)",
        "- Node 04: Corridor East (Acoustic and Atmospheric Purity Confirmed)",
        "---",
        "- Spores      : HP 0/180 [PURIFIED] | +0.015 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Node Lock & Stagger on Spore A)
- **Node Lock & Acoustic Sunder**:
  * Agent Kim maintains the grapple at Node 02 with `[Embrace Fang Vicious Guard]`, anchoring Spore Carrier A.
  * Agent Park discharges a concentrated Lament acoustic pulse from Node 04:
    * Deals **44 Lament Damage**!
    * Inflicts +34 Posture Strain. Spore A Posture drops to **38/100**, breaching the **60% Posture Threshold (60 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The carrier's fungal exoskeleton fissures wide open.
  * Spore Carrier A HP falls to **54/180**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Spore A Annihilation & Momentum Surge)
- **Posture Shatter Execution (1.5x Direct Damage)**:
  * Agent Kim's `Momentum Surge` activates! (+2 Speed next turn). Kim delivers a brutal finishing bite:
    * Deals **58 Grudge Damage**! Spore A HP hits **0/180**!
    * Spore Carrier A collapses into dry organic ash.
  * Park redirects the acoustic beam to Spore Carrier B, dealing **32 damage**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Toxic Cloud & Air Scrubber Siphon)
- **Hostile Desperation Spore Burst**:
  * Spore Carrier B vents a thick green toxic cloud across Nodes 2 and 3.
  * Agent Lee activates Floor 1's auxiliary air scrubbers at Node 05, reversing ventilation and filtering the toxic spore cloud!
  * Agent Kim deploys `[Directional Guard Absorption]`, taking 5 chip damage (HP: 110/115).
  * Park's Flerehan acoustic resonance strips 38 Posture points!
  * Spore B Posture drops to **16/100**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger on Spore B)
- **Acoustic Hyphae Disintegration**:
  * Park channels an overcharged acoustic frequency, stripping the final 16 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/100**. Spore Carrier B sinks to the floor plates.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Fang Execution**:
  * Agent Kim executes `[Climax Fang]`, biting clean through the main fungal stem.
  * All spore carriers dissolve into inert ash and pure Han mist, collected by the scrubbers.
  * Floor 1 collection flues harvest **+0.015 tons of refined Han**!
"""

# --- DAY 5 EXPANSION ---
def get_day_5_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 2 SUB-LEVEL GRAVITATIONAL ROTUNDA]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[OBELISK]       [KANG]          [KIM]                   [DEKAN]         ",
        "---",
        "- Node 01: Heavy Pendulum Obelisk (Posture 48/120 / Suspension Ring Split)",
        "- Node 03: Agent Kang (Point-Blank Band 1 / Basalt Shield Raised)",
        "- Node 05: Agent Kim (Range Band 3 / Kinetic Carbine Aimed)",
        "- Node 08: Attendant Dekan (Maw Bastion Barrier Maintaining)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 70/70",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 115/115 | SP +30 | Posture 65/65",
        "- Dekan       : Spd 5 -> 3 AP | HP 210/210 | SP +40 | Posture 105/105",
        "- Obelisk     : Spd 3 -> 1 AP | HP 136/220 | Posture 48/120 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER & DIRECT DAMAGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[OBELISK]       [KANG]          [KIM]                   [DEKAN]         ",
        "---",
        "- Node 01: Obelisk (STAGGER LEVEL 1 / 1.5x DAMAGE / Posture 22/120)",
        "- Node 03: Agent Kang (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 05: Agent Kim (Piercing Void Round Primed in Chamber)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP [SURGE] | HP 125/125 | SP +35 | Posture 70/70",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 115/115 | SP +30 | Posture 65/65",
        "- Obelisk     : Spd 0 -> 0 AP | HP 74/220  | Posture 22/120 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — 3.2G GRAVITATIONAL RUPTURE & VOID SHOT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[OBELISK]       [KANG]          [KIM]                   [DEKAN]         ",
        "---",
        "- Node 01: Obelisk (Recovered / Channeling 3.2G Gravitational Rupture)",
        "- Node 03: Agent Kang (Directional Guard Absorption Active)",
        "- Node 05: Agent Kim (Firing High-Penetration Void Disruptor)",
        "- Node 08: Attendant Dekan (Anchoring Floor Pylons Against G-Shear)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP | HP 118/125 | SP +35 | Posture 62/70",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 115/115 | SP +30 | Posture 65/65",
        "- Obelisk     : Spd 2 -> 1 AP | HP 38/220  | Posture 12/120 [UNSTABLE]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER ON GRAVITIC CORE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[OBELISK]                                               [DEKAN]         ",
        "        [KANG]  [KIM]",
        "---",
        "- Node 01: Obelisk (TERMINAL STAGGER / POSTURE 0/120 / CORE FRACTURED)",
        "- Node 02: Agent Kang (Fury Blade Thrust into Suspension Hub)",
        "- Node 03: Agent Kim (Void Beam Collapsing Gravitic Lens)",
        "---",
        "- Obelisk     : Spd 0 -> 0 AP | HP 12/220  | Posture 0/120 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & STONE SHATTER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[GRAVEL]        [KANG]  [KIM]                           [DEKAN]         ",
        "---",
        "- Node 01: Obelisk (Shattered to Crystalline Gravel / Gravity Restored)",
        "- Node 03: Agent Kang (Logging Sub-Level Rotunda Normalized)",
        "---",
        "- Obelisk     : HP 0/220 [PURIFIED] | +0.018 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Shield Stand & Obelisk Stagger)
- **Vanguard Anchor & Sunder**:
  * Agent Kang holds Node 03 firmly behind the basalt shield, absorbing gravitational turbulence.
  * Kang executes a heavy sunder against the lower pylon, dealing **46 Grudge damage**:
    * Inflicts +36 Posture Strain. Obelisk Posture drops to **48/120**, breaching the **60% Posture Threshold (72 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The obelisk tilts precariously on its gravitic axis.
  * Agent Kim fires three armor-piercing kinetic rounds from Node 05, chipping away another 16 HP.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Direct Damage Sunder & Momentum Surge)
- **Crushing Sunder (1.5x Direct Damage)**:
  * Agent Kang's `Momentum Surge` activates! (+2 Speed next turn). Kang delivers an overcharged greatsword cleave:
    * Deals **62 Grudge Damage**! Obelisk HP drops to **74/220**!
    * Massive fissures spiderweb across the violet stone monolith.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Gravitational Rupture & Piercing Void Shot)
- **Hostile Desperation Pulse**:
  * The obelisk recovers and attempts to channel `[3.2G Gravitational Rupture]`.
  * Agent Kim at Node 05 fires a high-penetration Void round straight into the charging core!
  * The Void disruption cancels the gravitational blast midway!
  * Agent Kang deploys `[Directional Guard Absorption]`, taking 7 chip damage (HP: 118/125).
  * Obelisk Posture drops to **12/120**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger on Obelisk)
- **Suspension Hub Cleave**:
  * Kang drives the blade into the central suspension hub, stripping the final 12 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/120**. The gravitational field collapses entirely.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Pierce**:
  * Kang executes `[Climax Pierce]`, sundering the obelisk into harmless violet stone gravel and pure Han vapor.
  * Floor 2 collection flues harvest **+0.018 tons of refined Han**!
"""

# --- DAY 7 EXPANSION ---
def get_day_7_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — GATE 03 PERIMETER DOCK]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[STALKER-A][STALKER-B][MELLDA][MOON]                                   ",
        "---",
        "- Node 01: Tempest Stalker A (Posture 46/120 / Pierced by Mellda's Spear)",
        "- Node 02: Tempest Stalker B (Charging Void Cyclone / Posture 120/120)",
        "- Node 03: Border Lead Mellda (Point-Blank Band 1 / Threshold Vow)",
        "- Node 04: Agent Moon (Range Band 2 / Lead Maul Heavy Downswing)",
        "---",
        "- Mellda      : Spd 6 -> 3 AP | HP 195/195 | SP +40 | Posture 95/95",
        "- Agent Moon  : Spd 5 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Stalker A   : Spd 3 -> 1 AP | HP 128/240 | Posture 46/120 [CRACKED]",
        "- Stalker B   : Spd 4 -> 2 AP | HP 240/240 | Posture 120/120"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER ON STALKER A]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SALT]   [STALKER-B][MELLDA][MOON]                                      ",
        "---",
        "- Node 01: Stalker A (SHATTERED & PULVERIZED / Salt Siphoned)",
        "- Node 02: Stalker B (Posture 66/120 / Mist Pinned by Golden Aura)",
        "- Node 03: Border Lead Mellda (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 04: Agent Moon (Pugnahan Heavy Slam Primed)",
        "---",
        "- Mellda      : Spd 8 -> 4 AP [SURGE] | HP 195/195 | SP +40 | Posture 95/95",
        "- Agent Moon  : Spd 5 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Stalker A   : HP 0/240 [DESTROYED]",
        "- Stalker B   : Spd 3 -> 1 AP | HP 164/240 | Posture 66/120 [ENGAGED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — VOID CYCLONE & SPEAR AURA PIN]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [STALKER-B][MELLDA][MOON]                                       ",
        "---",
        "- Node 02: Stalker B (Swirling into Void Cyclone / Grounded by Mellda)",
        "- Node 03: Border Lead Mellda (Directional Guard Absorption Active)",
        "- Node 04: Agent Moon (Lead Maul Driving into Grounded Nucleus)",
        "---",
        "- Mellda      : Spd 8 -> 4 AP | HP 188/195 | SP +40 | Posture 88/95",
        "- Agent Moon  : Spd 5 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Stalker B   : Spd 2 -> 1 AP | HP 78/240  | Posture 20/120 [GROUNDED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER ON STALKER B]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [STALKER-B]                                                     ",
        "                [MELLDA][MOON]",
        "---",
        "- Node 02: Stalker B (TERMINAL STAGGER / POSTURE 0/120 / 2.0x DMG)",
        "- Node 03: Border Lead Mellda (Impaling Core Nexus)",
        "- Node 04: Agent Moon (Pugnahan Overhead Sunder)",
        "---",
        "- Stalker B   : Spd 0 -> 0 AP | HP 16/240  | Posture 0/120 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [SALT]  [MELLDA][MOON]                                          ",
        "---",
        "- Node 02: Stalkers (Shattered into Gray Salt & Dissipated)",
        "- Node 03: Border Lead Mellda (Reporting Gate 03 Perimeter Secure)",
        "---",
        "- Stalkers    : HP 0/240 [PURIFIED] | +0.020 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Gate Anchor & Stagger on Stalker A)
- **Gate Anchor & Weight Impact**:
  * Mellda pins Stalker A's mist body at Node 03 using *Threshold Vow*.
  * Agent Moon swings the Lead Maul from Node 04, slamming the entity's core:
    * Deals **48 Weight Damage**!
    * Inflicts +38 Posture Strain. Stalker A Posture drops to **46/120**, breaching the **60% Posture Threshold (72 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The tempest vapor condenses into brittle crystalline needles.
  * Stalker A HP falls to **80/240**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stalker A Destruction & Momentum Surge)
- **Direct Weight Sunder (1.5x Direct Damage)**:
  * Mellda's `Momentum Surge` activates! (+2 Speed next turn).
  * Agent Moon delivers a crushing downward strike:
    * Deals **80 Weight Damage**! Stalker A HP hits **0/240**!
    * Stalker A shatters into a pile of dry gray salt.
  * Mellda directs her golden spear toward Stalker B, dealing **34 damage**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Void Cyclone & Golden Spear Pin)
- **Hostile Desperation Cyclone**:
  * Stalker B accelerates into a razor-sharp `[Void Cyclone]`.
  * Mellda unleashes a golden spear aura, pinning the cyclone's eye to the stone plates!
  * Mellda deploys `[Directional Guard Absorption]`, taking 7 chip damage (HP: 188/195).
  * Agent Moon's heavy blow strips 28 Posture points!
  * Stalker B Posture drops to **18/120**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger on Stalker B)
- **Pugnahan Heavy Slam**:
  * Moon executes a full overhead Pugnahan slam, stripping the final 18 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/120**. The mist entity collapses into solid salt crust.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Impale**:
  * Mellda executes `[Climax Impale]`, driving *Threshold Vow* through the salt crust. Both stalkers dissolve into gray salt and pure Han vapor.
  * Gate 03 collection flues harvest **+0.020 tons of refined Han**!
"""

# --- DAY 12 EXPANSION ---
def get_day_12_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 3 DATA CORRIDOR]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CENOTAPH-A][CENOTAPH-B][SIM]   [KWON]  [SEO]                   [ZYRAK] ",
        "---",
        "- Node 01: Cenotaph A (Posture 44/130 / Base Fractured by Sim's Maul)",
        "- Node 02: Cenotaph B (Channeling 90dB Wail / Posture 130/130)",
        "- Node 03: Agent Sim (Point-Blank Band 1 / Lead Maul Ready)",
        "- Node 04: Agent Kwon (Range Band 2 / Calibrated Stun Baton)",
        "- Node 05: Agent Seo (Range Band 3 / Choral Sonic Burst Aimed)",
        "- Node 08: Extraction Lead Zyrak (Extraction Siphon Ready)",
        "---",
        "- Agent Sim   : Spd 6 -> 3 AP | HP 135/135 | SP +35 | Posture 75/75",
        "- Agent Kwon  : Spd 5 -> 3 AP | HP 120/120 | SP +30 | Posture 65/65",
        "- Agent Seo   : Spd 5 -> 3 AP | HP 120/120 | SP +35 | Posture 60/60",
        "- Cenotaph A  : Spd 3 -> 1 AP | HP 134/260 | Posture 44/130 [CRACKED]",
        "- Cenotaph B  : Spd 4 -> 2 AP | HP 260/260 | Posture 130/130"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER ON CENOTAPH A]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[DUST]  [CENOTAPH-B][SIM]       [KWON]  [SEO]                   [ZYRAK] ",
        "---",
        "- Node 01: Cenotaph A (PULVERIZED TO DUST / Han Siphoned)",
        "- Node 02: Cenotaph B (Posture 68/130 / Stone Crown Vibrating)",
        "- Node 03: Agent Sim (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 05: Agent Seo (Focusing High-Frequency Sonic Beam)",
        "---",
        "- Agent Sim   : Spd 8 -> 4 AP [SURGE] | HP 135/135 | SP +35 | Posture 75/75",
        "- Cenotaph A  : HP 0/260 [DESTROYED]",
        "- Cenotaph B  : Spd 3 -> 1 AP | HP 176/260 | Posture 68/130 [ENGAGED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — 90dB WAIL & EXTRACTION SIPHON LOCK]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [CENOTAPH-B][SIM]       [KWON]  [SEO]                   [ZYRAK] ",
        "---",
        "- Node 02: Cenotaph B (Unleashing 90dB Cognitive Wail / Siphoned)",
        "- Node 03: Agent Sim (Directional Guard Absorption Active)",
        "- Node 05: Agent Seo (High-Frequency Burst Cracking Stone Crown)",
        "- Node 08: Extraction Lead Zyrak (Siphoning Excess Screech into Reserve)",
        "---",
        "- Agent Sim   : Spd 8 -> 4 AP | HP 128/135 | SP +35 | Posture 67/75",
        "- Cenotaph B  : Spd 2 -> 1 AP | HP 84/260  | Posture 22/130 [CRACKED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER ON CENOTAPH B]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [CENOTAPH-B]                                            [ZYRAK] ",
        "                [SIM]   [KWON]  [SEO]",
        "---",
        "- Node 02: Cenotaph B (TERMINAL STAGGER / POSTURE 0/130 / 2.0x DMG)",
        "- Node 03: Agent Sim (Heavy Maul Strike Aimed at Monolith Base)",
        "- Node 05: Agent Seo (Acoustic Cleave Severing Inscriptions)",
        "---",
        "- Cenotaph B  : Spd 0 -> 0 AP | HP 18/260  | Posture 0/130 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [GRAVEL][SIM]   [KWON]  [SEO]                           [ZYRAK] ",
        "---",
        "- Node 02: Cenotaphs (Collapsed to Harmless Gravel / Han Siphoned)",
        "- Node 03: Agent Sim (Clearing Corridor East)",
        "---",
        "- Cenotaphs   : HP 0/260 [PURIFIED] | +0.022 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Base Fracture & Stagger on Cenotaph A)
- **Monolith Sunder & Sonic Focus**:
  * Agent Sim pulverizes the base of Cenotaph A at Node 03, exploiting its Grudge vulnerability:
    * Deals **46 Grudge Damage**!
    * Inflicts +36 Posture Strain. Cenotaph A Posture drops to **44/130**, breaching the **60% Posture Threshold (78 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The stone stele splits along its central inscription line.
  * Agent Seo fires a sonic beam from Node 05, chipping 18 damage off Cenotaph B.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Cenotaph A Annihilation & Momentum Surge)
- **Direct Grudge Sunder (1.5x Direct Damage)**:
  * Agent Sim's `Momentum Surge` activates! (+2 Speed next turn). Sim delivers a massive overhead maul strike:
    * Deals **70 Grudge Damage**! Cenotaph A HP hits **0/260**!
    * Cenotaph A disintegrates into fine stone dust.
  * Seo concentrates sonic vibrations on Cenotaph B, dealing **34 damage**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (90dB Wail & Extraction Siphon)
- **Hostile Desperation Screech**:
  * Cenotaph B unleashes a 90dB cognitive screech across the corridor.
  * Extraction Lead Zyrak engages the *Extraction Siphon*, redirecting 40% of the acoustic energy into floor storage cells!
  * Agent Sim deploys `[Directional Guard Absorption]`, taking 7 chip damage (HP: 128/135).
  * Agent Seo fires a high-frequency burst into the stone crown, stripping 28 Posture points!
  * Cenotaph B Posture drops to **16/130**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger on Cenotaph B)
- **Crown Shatter & Terminal Collapse**:
  * Seo discharges the maximum frequency tone, stripping the final 16 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/130**. The monolith wobbles and cracks.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Maul Strike**:
  * Sim executes `[Climax Maul Strike]`, shattering Cenotaph B into harmless gravel and pure Han vapor.
  * Floor 3 collection flues harvest **+0.022 tons of refined Han**!
"""

# --- DAY 17 EXPANSION ---
def get_day_17_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 6 CENTRAL VENT CORE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[LEVIATHAN]     [TAK]   [ZYRAK]         [HONG]  [JO]    [MARJUK]        ",
        "---",
        "- Node 01: Ash Leviathan (Posture 76/200 / Scales Pierced by Tak & Zyrak)",
        "- Node 03: Agent Tak (Point-Blank Band 1 / Molten Blade Driving)",
        "- Node 04: Extraction Lead Zyrak (Range Band 2 / Extraction Lance Siphoning)",
        "- Node 06: Agent Hong & Jo (Range Band 3 / Choral Lament & Thermal Rays)",
        "- Node 08: Archive Lead Marjuk (Temporal Stasis Array Active)",
        "---",
        "- Agent Tak   : Spd 6 -> 3 AP | HP 140/140 | SP +35 | Posture 80/80",
        "- Zyrak       : Spd 5 -> 3 AP | HP 180/180 | SP +40 | Posture 90/90",
        "- Agent Hong  : Spd 5 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Leviathan   : Spd 4 -> 2 AP | HP 260/420 | Posture 76/200 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[LEVIATHAN]             [TAK]   [ZYRAK] [HONG]  [JO]    [MARJUK]        ",
        "---",
        "- Node 01: Leviathan (STAGGER LEVEL 1 / 1.5x DAMAGE / Posture 34/200)",
        "- Node 03: Agent Tak (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 04: Extraction Lead Zyrak (Siphoning Molten Core)",
        "- Node 06: Hong & Jo (Synchronized Four-Spectral Beam)",
        "---",
        "- Agent Tak   : Spd 8 -> 4 AP [SURGE] | HP 140/140 | SP +35 | Posture 80/80",
        "- Zyrak       : Spd 5 -> 3 AP | HP 180/180 | SP +40 | Posture 90/90",
        "- Leviathan   : Spd 0 -> 0 AP | HP 142/420 | Posture 34/200 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MIDNIGHT TIDAL WAVE & STASIS LOCK]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[LEVIATHAN]     [TAK]   [ZYRAK]         [HONG]  [JO]    [MARJUK]        ",
        "---",
        "- Node 01: Leviathan (Recovered / Channeling Midnight Tidal Wave)",
        "- Node 03: Agent Tak (Directional Guard Absorption Active)",
        "- Node 04: Extraction Lead Zyrak (Grounding Lance into Ash Surge)",
        "- Node 06: Agent Jo (Prismatic Beam Burning off Thermal Crest)",
        "- Node 08: Archive Lead Marjuk (Locking Stasis Field at 0.1x Speed)",
        "---",
        "- Agent Tak   : Spd 8 -> 4 AP | HP 130/140 | SP +35 | Posture 68/80",
        "- Leviathan   : Spd 3 -> 1 AP | HP 74/420  | Posture 16/200 [BURNING]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER ON ASH LEVIATHAN]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[LEVIATHAN]                                             [MARJUK]        ",
        "        [TAK]   [ZYRAK] [HONG]  [JO]",
        "---",
        "- Node 01: Leviathan (TERMINAL STAGGER / POSTURE 0/200 / 2.0x DMG)",
        "- Node 02: Agent Tak & Zyrak (Driving Dual Piercers into Spinal Vent)",
        "- Node 03: Hong & Jo (Disrupting Residual Thermal Flow)",
        "---",
        "- Leviathan   : Spd 0 -> 0 AP | HP 22/420  | Posture 0/200 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[ASH-MIST]      [TAK]   [ZYRAK] [HONG]  [JO]            [MARJUK]        ",
        "---",
        "- Node 01: Leviathan (Shattered into Inert Volcanic Ash & Pure Han)",
        "- Node 02: Strike Team (Reporting Central Vent Core Fully Pacified)",
        "---",
        "- Leviathan   : HP 0/420 [PURIFIED] | +0.032 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Scale Pierce & Stagger Build)
- **Multi-Operative Sunder & Lament Focus**:
  * Agent Tak drives the molten blade into the leviathan's ash mantle at Node 03, while Zyrak thrusts the Extraction Lance at Node 04:
    * Deals **52 Combined Grudge/Kinetic Damage**!
    * Inflicts +42 Posture Strain. Leviathan Posture drops to **76/200**, breaching the **60% Posture Threshold (120 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The volcanic scales crack open, exposing glowing magma flesh.
  * Hong discharges a pure Lament beam from Node 06, stripping 28 HP!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Magma Sunder & Momentum Surge)
- **Coordinated Focus (1.5x Direct Damage)**:
  * Agent Tak's `Momentum Surge` activates! (+2 Speed next turn). Tak delivers a sweeping fire slash:
    * Deals **68 Damage**!
  * Hong and Jo unleash synchronized elemental beams: **50 Damage**!
  * Leviathan HP falls to **142/420**! Posture drops to **34/200**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Midnight Tidal Wave & Stasis Lock)
- **Hostile Desperation Tidal Wave**:
  * The leviathan attempts to unleash `[Midnight Tidal Wave]`, flooding Floor 6 with boiling ash.
  * Archive Lead Marjuk engages the *Temporal Stasis Array*, slowing the ash wave to 0.1x velocity!
  * Agent Jo focuses the prismatic beam, incinerating the entity's thermal crest!
  * Agent Tak deploys `[Directional Guard Absorption]`, taking 10 chip damage (HP: 130/140).
  * Leviathan Posture falls to **16/200**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger on Ash Leviathan)
- **Spinal Vent Sunder**:
  * Tak and Zyrak drive their weapons simultaneously into the exposed spinal vent, stripping the final 16 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/200**. The leviathan crashes against the floor plates.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Overdrive Climax Cleave**:
  * Tak executes `[Overdrive Climax Cleave]`. The beast shatters into smoking volcanic ash and dense Han mist.
  * Floor 6 collection flues harvest **+0.032 tons of refined Han**!
"""

def update_part_2():
    path = "SOMNARAK-WORLD/The_Absolvohan/Part_2_Days_1_to_25.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Day 1
    old_d1 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Kim locks N02; Park unleashes Lament pulse; Spore-A 60%  |
| Stagger.                                                            |
| - Turn 03: Posture broken; all allied strikes deal 2.0x damage;     |
| Spore-A dead.                                                       |
| - Turn 04: Spore-B & C vent toxic cloud; Lee activates air scrubber |
| at N05.                                                             |
| - Turn 05: Park executes Flerehan acoustic resonance; Spores lose   |
| momentum.                                                           |
| - Turn 06: Kim executes Climax Fang; Terminal Stagger shatters      |
| carriers.                                                           |
+=====================================================================+
```"""
    if old_d1 in content:
        content = content.replace(old_d1, get_day_1_combat())
        print("Replaced Day 1 summary successfully!")

    # Day 5
    old_d5 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Kang holds N02 behind shield; Obelisk hits 60% Stagger   |
| 1.                                                                  |
| - Turn 03: All allied attacks deal 2.0x direct damage; HP falls to  |
| 98.                                                                 |
| - Turn 04: Obelisk recovers; charges 3.2G pulse [Gravitational      |
| Rupture].                                                           |
| - Turn 05: Kim at N05 fires piercing Void shot, canceling charging  |
| core.                                                               |
| - Turn 06: Kang executes Climax Pierce; Terminal Stagger shatters   |
| stone.                                                              |
+=====================================================================+
```"""
    if old_d5 in content:
        content = content.replace(old_d5, get_day_5_combat())
        print("Replaced Day 5 summary successfully!")

    # Day 7
    old_d7 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Mellda anchors Gate 03; Moon smashes Stalker-A; 60%      |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; direct Weight damage deals 2.0x;         |
| Stalker-A dead.                                                     |
| - Turn 04: Stalker-B swirls into Void cyclone; Mellda pins with     |
| spear aura.                                                         |
| - Turn 05: Moon executes Pugnahan heavy slam; forces Terminal       |
| Stagger.                                                            |
| - Turn 06: Mellda executes Climax Impale; Stalker shatters into     |
| gray salt.                                                          |
+=====================================================================+
```"""
    if old_d7 in content:
        content = content.replace(old_d7, get_day_7_combat())
        print("Replaced Day 7 summary successfully!")

    # Day 12
    old_d12 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Sim pulverizes Cenotaph-A base; exploits Grudge; 60%     |
| Stagger 1.                                                          |
| - Turn 03: Posture shattered; 2.0x direct damage breaks Cenotaph-A  |
| into dust.                                                          |
| - Turn 04: Cenotaph-B unleashes 90dB wail; Zyrak engages Extraction |
| Siphon.                                                             |
| - Turn 05: Seo fires high-frequency sonic burst, cracking the stone |
| crown.                                                              |
| - Turn 06: Sim executes Climax Maul Strike; Cenotaph-B collapses to |
| gravel.                                                             |
+=====================================================================+
```"""
    if old_d12 in content:
        content = content.replace(old_d12, get_day_12_combat())
        print("Replaced Day 12 summary successfully!")

    # Day 17
    old_d17 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Tak & Zyrak pierce scales; Hong beams Lament; 60%        |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; balanced 4-affinity attacks deal 2.0x    |
| direct damage.                                                      |
| - Turn 04: Leviathan charges [Midnight Tidal Wave]; Marjuk          |
| activates Stasis.                                                   |
| - Turn 05: Jo focuses prismatic beam; burns off leviathan thermal   |
| crest.                                                              |
| - Turn 06: Tak executes Overdrive Climax Cleave; Terminal Stagger   |
| shatters beast.                                                     |
+=====================================================================+
```"""
    if old_d17 in content:
        content = content.replace(old_d17, get_day_17_combat())
        print("Replaced Day 17 summary successfully!")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated Part 2 successfully!")

if __name__ == "__main__":
    update_part_2()
