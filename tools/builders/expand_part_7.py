#!/usr/bin/env python3
"""
tools/expand_part_7.py
Expands Part 7 (Days 125 to 145) into an exhaustive operational chronicle:
- Full turn-by-turn combat logs for Day 125, 127, 132, 137, 141, 145 across Turns 02 to 06.
- Enforces 100% box symmetry and dual-environment typography (<= 71 chars for boxes).
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

# --- DAY 125 EXPANSION ---
def get_day_125_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 2 LOWER TRENCH PASSAGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[BEETLE-A][BEETLE-B][KANG]      [SHIN]                  [DEKAN]         ",
        "---",
        "- Node 01: Beetle A (Posture 48/120 / Thorax Fractured by Kang)",
        "- Node 02: Beetle B (Charging Mandibles / Posture 120/120)",
        "- Node 03: Agent Kang (Point-Blank Band 1 / Basalt Great-Maul Cleave)",
        "- Node 05: Agent Shin (Range Band 3 / Choral Staff Lament Firing)",
        "- Node 08: Containment Lead Dekan (Jaw Clamp Floor Traps Ready)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 140/140 | SP +35 | Posture 80/80",
        "- Agent Shin  : Spd 6 -> 3 AP | HP 120/120 | SP +35 | Posture 60/60",
        "- Dekan       : Spd 5 -> 3 AP | HP 210/210 | SP +40 | Posture 105/105",
        "- Beetle A    : Spd 3 -> 1 AP | HP 134/260 | Posture 48/120 [CRACKED]",
        "- Beetle B    : Spd 4 -> 2 AP | HP 260/260 | Posture 120/120"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER ON BEETLE A]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[GRAVEL]        [BEETLE-B][KANG][SHIN]                  [DEKAN]         ",
        "---",
        "- Node 01: Beetle A (SHATTERED & PULVERIZED / Gravel Siphoned)",
        "- Node 02: Beetle B (Exposed / Posture 68/120)",
        "- Node 03: Agent Kang (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 04: Agent Shin (Acoustic Beam Penetrating Marrow)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP [SURGE] | HP 140/140 | SP +35 | Posture 80/80",
        "- Agent Shin  : Spd 6 -> 3 AP | HP 120/120 | SP +35 | Posture 60/60",
        "- Beetle A    : HP 0/260 [DESTROYED]",
        "- Beetle B    : Spd 3 -> 1 AP | HP 168/260 | Posture 68/120 [ENGAGED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MANDIBLE CHARGE & JAW CLAMP PIN]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [BEETLE-B][KANG][SHIN]                          [DEKAN]         ",
        "---",
        "- Node 02: Beetle B (Pinned at Node 02 by Dekan's Jaw Clamp)",
        "- Node 03: Agent Kang (Spd 8 / AP 4 / Heavy Maul Sunder)",
        "- Node 04: Agent Shin (Acoustic Wave Driving into Exposed Marrow)",
        "- Node 08: Containment Lead Dekan (Hydraulic Pressure Max)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP | HP 134/140 | SP +35 | Posture 72/80",
        "- Agent Shin  : Spd 6 -> 3 AP | HP 120/120 | SP +35 | Posture 60/60",
        "- Beetle B    : Spd 2 -> 1 AP | HP 74/260  | Posture 22/120 [PINNED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER ON BEETLE B]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [BEETLE-B]                                      [DEKAN]         ",
        "                [KANG]  [SHIN]",
        "---",
        "- Node 02: Beetle B (TERMINAL STAGGER / POSTURE 0/120 / 2.0x DMG)",
        "- Node 03: Agent Kang (Cephalic Carapace Cracked)",
        "- Node 04: Agent Shin (Resonant Pulse Cleared Psychic Resistance)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 134/140 | SP +35 | Posture 72/80",
        "- Agent Shin  : Spd 6 -> 3 AP | HP 120/120 | SP +35 | Posture 60/60",
        "- Beetle B    : Spd 0 -> 0 AP | HP 18/260  | Posture 0/120 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [GRAVEL][KANG]  [SHIN]                          [DEKAN]         ",
        "---",
        "- Node 02: All Beetles (Dissolved to Amber Gravel / Siphoned)",
        "- Node 03: Agent Kang (Resting Basalt Great-Maul)",
        "- Node 04: Agent Shin (Logging Trench Acoustic Calm)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 134/140 | SP +40 | Posture 80/80",
        "- Agent Shin  : Spd 6 -> 3 AP | HP 120/120 | SP +40 | Posture 60/60",
        "- Beetles     : HP 0/260 [PURIFIED] | +0.024 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Thorax Smash & Stagger Build)
- **Vanguard Impact & Lament Focus**:
  * **Agent Kang (Speed 6 -> 3 AP)**: Smashes Beetle A's thorax with the Basalt Great-Maul at Node 03:
    * Deals **44 Grudge Damage**!
    * Inflicts +36 Posture Strain. Beetle A Posture drops to **48/120**, breaching the **60% Posture Threshold (72 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** Beetle A's amber carapace cracks wide open.
  * **Agent Shin**: Firing from Node 05 with the Choral Staff, channels a focused Lament beam into the cracked marrow for **36 Lament damage**.
  * Beetle A HP drops to **112/260**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Beetle A Annihilation & Momentum Surge)
- **Crushing Blow (1.5x Direct Damage)**:
  * Agent Kang's `Momentum Surge` activates! (+2 Speed next turn). Kang delivers an overhead execution strike:
    * Deals **68 Grudge Damage**! Beetle A HP hits **0/260**!
    * Beetle A shatters into harmless amber gravel on the trench floor.
  * Agent Shin directs her acoustic beam toward Beetle B, dealing **28 damage**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Mandible Charge & Jaw Clamp Pin)
- **Hostile Desperation Charge**:
  * Beetle B charges forward, attempting to impale Agent Shin.
  * Containment Lead Dekan activates Floor 2's *Jaw Clamp* floor traps, clamping Beetle B's mandibles at Node 02!
  * Agent Kang deploys `[Directional Guard Absorption]`, absorbing 6 chip damage (HP: 134/140).
  * Agent Shin channels an acoustic shockwave directly into Beetle B's exposed marrow, stripping 26 Posture points!
  * Beetle B Posture falls to **16/120**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger on Beetle B)
- **Marrow Cleave & Terminal Collapse**:
  * Kang lands a crushing blow on the clamped head, stripping the final 16 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/120**. Beetle B collapses onto the basalt plates.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Maul Shatter**:
  * Kang executes `[Climax Maul Shatter]`. Both beetles dissolve into amber gravel and pure Han vapor.
  * Floor 2 collection flues harvest **+0.024 tons of refined Han**!
"""

# --- DAY 127 EXPANSION ---
def get_day_127_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 4 REAGENT EXTRACTION DUCTS]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SIPHON-A][SIPHON-B][NOH][HWANG]        [KANG]                  [ISHALL]",
        "---",
        "- Node 01: Siphon A (Posture 44/120 / Feeder Tendrils Severed by Noh)",
        "- Node 02: Siphon B (Charging Bleed Deluge / Posture 120/120)",
        "- Node 03: Agent Noh (Point-Blank Band 1 / Bayonet Severing)",
        "- Node 04: Agent Hwang (Range Band 2 / Cryo-Lament Incision)",
        "- Node 06: Agent Kang (Range Band 3 / Heavy Maul Ready)",
        "- Node 10: Outsider Ishall (Shadow Ingress Ready / Band 5)",
        "---",
        "- Agent Noh   : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 60/60",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 140/140 | SP +35 | Posture 80/80",
        "- Siphon A    : Spd 3 -> 1 AP | HP 138/260 | Posture 44/120 [CRACKED]",
        "- Siphon B    : Spd 4 -> 2 AP | HP 260/260 | Posture 120/120"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER ON SIPHON A]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[ICE]   [SIPHON-B][NOH] [HWANG]         [KANG]                  [ISHALL]",
        "---",
        "- Node 01: Siphon A (FROZEN & SHATTERED / Ice Siphoned)",
        "- Node 02: Siphon B (Posture 64/120 / Internal Conduits Chilled)",
        "- Node 03: Agent Noh (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 04: Agent Hwang (Cryo Needle Driving into Main Valve)",
        "---",
        "- Agent Noh   : Spd 8 -> 4 AP [SURGE] | HP 125/125 | SP +30 | Posture 65/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 60/60",
        "- Siphon A    : HP 0/260 [DESTROYED]",
        "- Siphon B    : Spd 3 -> 1 AP | HP 164/260 | Posture 64/120 [ENGAGED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — BLEED DELUGE & SHADOW INGRESS]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [SIPHON-B][ISHALL][NOH] [HWANG] [KANG]                          ",
        "---",
        "- Node 02: Siphon B (Surging Bleed Deluge / Flanked by Ishall)",
        "- Node 03: Outsider Ishall (Shadow Ingress Infiltration to Rear)",
        "- Node 04: Agent Noh (Directional Guard Absorption Active)",
        "- Node 05: Agent Hwang (Cryo Incision Freezing Internal Conduits)",
        "- Node 06: Agent Kang (Priming Climax Maul)",
        "---",
        "- Ishall      : Spd 7 -> 4 AP | HP 165/165 | SP +40 | Posture 85/85",
        "- Agent Noh   : Spd 8 -> 4 AP | HP 118/125 | SP +30 | Posture 58/65",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 60/60",
        "- Siphon B    : Spd 2 -> 1 AP | HP 68/260  | Posture 18/120 [FROZEN]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER ON SIPHON B]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [SIPHON-B]                                                      ",
        "                [ISHALL][NOH]   [HWANG] [KANG]",
        "---",
        "- Node 02: Siphon B (TERMINAL STAGGER / POSTURE 0/120 / 2.0x DMG)",
        "- Node 03: Outsider Ishall (Severing Arterial Tube)",
        "- Node 04: Agent Noh (Pinning Valve Flange)",
        "- Node 06: Agent Kang (Priming Overhead Maul Strike)",
        "---",
        "- Siphon B    : Spd 0 -> 0 AP | HP 16/260  | Posture 0/120 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [ICE-DUST][ISHALL][NOH] [HWANG] [KANG]                          ",
        "---",
        "- Node 02: Siphons (Shattered to Crystalline Ice & Han Mist)",
        "- Node 03: Outsider Ishall (Retracting Shadow Shroud)",
        "- Node 04: Agent Noh (Reporting Ducts Clear)",
        "- Node 06: Agent Kang (Confirming Siphon Flues Active)",
        "---",
        "- Siphons     : HP 0/260 [PURIFIED] | +0.024 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Tendril Severance & Cryo Stagger)
- **Feeder Severance & Freezing Blast**:
  * Agent Noh severs the primary feeder tendrils with the clockwork bayonet at Node 03.
  * Agent Hwang channels a concentrated cryo-Lament incision into Siphon A's main valve from Node 04:
    * Deals **42 Cryo-Lament Damage**!
    * Inflicts +34 Posture Strain. Siphon A Posture drops to **44/120**, breaching the **60% Posture Threshold (72 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The fleshy siphon freezes solid.
  * Siphon A HP falls to **118/260**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Siphon A Shattered & Momentum Surge)
- **Frozen Shatter (1.5x Direct Damage)**:
  * Agent Noh's `Momentum Surge` activates! (+2 Speed next turn).
  * Agent Kang steps forward from Node 06, smashing Siphon A with the heavy maul:
    * Deals **68 Grudge Damage**! Siphon A HP hits **0/260**!
    * Siphon A shatters into thousands of frozen red ice crystals.
  * Hwang redirects cryo fire to Siphon B, dealing **32 damage**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Bleed Deluge & Shadow Ingress)
- **Hostile Desperation Deluge**:
  * Siphon B surges with `[Bleed Deluge]`, spraying pressurized crimson bile.
  * Outsider Ishall uses *Shadow Ingress* to teleport directly behind Siphon B at Node 03, severing its arterial intake!
  * Agent Noh deploys `[Directional Guard Absorption]`, taking 7 chip damage (HP: 118/125).
  * Hwang's cryo needle freezes the internal pump, stripping 26 Posture points!
  * Siphon B Posture drops to **14/120**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger on Siphon B)
- **Conduit Freeze & Terminal Collapse**:
  * Hwang delivers the final cryo incision, stripping the last 14 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/120**.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Maul Smash**:
  * Kang executes `[Climax Maul Smash]`. Siphon B shatters into sparkling ice dust and refined Han vapor.
  * Floor 4 collection flues harvest **+0.024 tons of refined Han**!
"""

# --- DAY 132 EXPANSION ---
def get_day_132_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 6 ARCHIVE RAILWAYS]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SWEEPER-A][SWEEPER-B][KANG]   [JIN]                   [MARJUK]        ",
        "---",
        "- Node 01: Sweeper A (Posture 52/130 / Scythe Blade Blocked by Kang)",
        "- Node 02: Sweeper B (Accelerating Rotary Blades / Posture 130/130)",
        "- Node 03: Agent Kang (Point-Blank Band 1 / Heavy Maul Parry Ready)",
        "- Node 05: Agent Jin (Range Band 3 / Choral Bell Sonic Pulse Aimed)",
        "- Node 08: Archive Lead Marjuk (Range Band 4 / Stasis Field Ready)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 140/140 | SP +35 | Posture 80/80",
        "- Agent Jin   : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Marjuk      : Spd 5 -> 3 AP | HP 180/180 | SP +40 | Posture 90/90",
        "- Sweeper A   : Spd 4 -> 2 AP | HP 154/280 | Posture 52/130 [CRACKED]",
        "- Sweeper B   : Spd 5 -> 3 AP | HP 280/280 | Posture 130/130"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER ON SWEEPER A]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SCRAP]         [SWEEPER-B][KANG][JIN]                  [MARJUK]        ",
        "---",
        "- Node 01: Sweeper A (SHATTERED & PULVERIZED / Scrap Siphoned)",
        "- Node 02: Sweeper B (Posture 74/130 / Drive Gear Rattling)",
        "- Node 03: Agent Kang (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 04: Agent Jin (Sonic Bell Disrupting Gear Synchronizer)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP [SURGE] | HP 140/140 | SP +35 | Posture 80/80",
        "- Agent Jin   : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Sweeper A   : HP 0/280 [DESTROYED]",
        "- Sweeper B   : Spd 4 -> 2 AP | HP 182/280 | Posture 74/130 [ENGAGED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — ROTARY SEVERANCE & STASIS INTERCEPTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [SWEEPER-B][KANG][JIN]                  [MARJUK]        [MAJIN]",
        "---",
        "- Node 02: Sweeper B (Accelerating Rotary Severance)",
        "- Node 03: Agent Kang (Directional Guard Absorption Active)",
        "- Node 04: Agent Jin (Choral Bell Resonant Sonic Pulse Firing)",
        "- Node 07: Archive Lead Marjuk (Deploying Stasis Clamp to Wheels)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP | HP 132/140 | SP +35 | Posture 70/80",
        "- Agent Jin   : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Sweeper B   : Spd 3 -> 1 AP | HP 88/280  | Posture 24/130 [STALLED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER ON SWEEPER B]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [SWEEPER-B]                                     [MARJUK]",
        "                [KANG]  [JIN]",
        "---",
        "- Node 02: Sweeper B (TERMINAL STAGGER / POSTURE 0/130 / 2.0x DMG)",
        "- Node 03: Agent Kang (Shattering Sprocket Assembly)",
        "- Node 04: Agent Jin (Disrupting Internal Escapement)",
        "---",
        "- Sweeper B   : Spd 0 -> 0 AP | HP 18/280  | Posture 0/130 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [SLAG]  [KANG]  [JIN]                   [MARJUK]        [MAJIN]",
        "---",
        "- Node 02: Sweeper B (Drive Sprockets Pulverized / Siphoned)",
        "- Node 03: Agent Kang (Clearing Steel Scraps)",
        "- Node 04: Agent Jin (Reporting Railways Clear)",
        "---",
        "- Sweepers    : HP 0/280 [PURIFIED] | +0.024 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Scythe Block & Stagger on Sweeper A)
- **Kinetic Block & Sonic Pulse**:
  * Kang blocks Sweeper A's rotary scythe with the Basalt Great-Maul at Node 03, deflecting the blade.
  * Agent Jin fires a resonant sonic wave from the Choral Bell at Node 05:
    * Deals **44 Sonic Lament Damage**!
    * Inflicts +36 Posture Strain. Sweeper A Posture drops to **46/130**, breaching the **60% Posture Threshold (78 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** Sweeper A's blade axle jams.
  * Sweeper A HP drops to **126/280**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Sweeper A Destruction & Momentum Surge)
- **Crushing Sunder (1.5x Direct Damage)**:
  * Agent Kang's `Momentum Surge` activates! (+2 Speed next turn). Kang delivers an overhead blow:
    * Deals **66 Grudge Damage**! Sweeper A HP hits **0/280**!
    * Sweeper A collapses into inert iron scrap.
  * Jin redirects sonic vibrations toward Sweeper B, dealing **32 damage**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Rotary Severance & Stasis Clamp)
- **Hostile Desperation Charge**:
  * Sweeper B activates `[Rotary Severance]`, spinning its scythe at lethal RPM.
  * Archive Lead Marjuk drops a stasis clamp onto the rail tracks, slowing the machine's advance!
  * Agent Kang deploys `[Directional Guard Absorption]`, taking 8 chip damage (HP: 132/140).
  * Jin's sonic bell disrupts the gear synchronizer, stripping 28 Posture points!
  * Sweeper B Posture falls to **16/130**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger on Sweeper B)
- **Gear Synchronization Shattered**:
  * Jin unleashes a maximum-resonance pulse, stripping the final 16 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/130**.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Maul Sweep**:
  * Kang executes `[Climax Maul Sweep]`, pulverizing the drive sprockets into smoking slag and Han mist.
  * Floor 6 collection flues harvest **+0.024 tons of refined Han**!
"""

# --- DAY 137 EXPANSION ---
def get_day_137_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 4 HIGH-GRAVITY OBSERVATION SHAFT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[WELL-A][WELL-B][KANG]  [BAE]                   [AYSHUK]        [MAJIN]",
        "---",
        "- Node 01: Gravitic Well A (Posture 56/140 / Smashed by Kang & Bae)",
        "- Node 02: Gravitic Well B (Charging Global Sanity Vortex / Posture 140/140)",
        "- Node 03: Agent Kang (Point-Blank Band 1 / Heavy Maul Sunder)",
        "- Node 04: Agent Bae (Range Band 2 / Bulwark Maul Ready)",
        "- Node 07: Research Lead Ayshuk (Predicting Gravitational Shear)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 140/140 | SP +35 | Posture 80/80",
        "- Agent Bae   : Spd 6 -> 3 AP | HP 135/135 | SP +30 | Posture 75/75",
        "- Well A      : Spd 3 -> 1 AP | HP 144/280 | Posture 56/140 [CRACKED]",
        "- Well B      : Spd 4 -> 2 AP | HP 280/280 | Posture 140/140"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER ON WELL A]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[VOID]  [WELL-B][KANG]  [BAE]                   [AYSHUK]        [MAJIN]",
        "---",
        "- Node 01: Well A (IMPLODED & DISSOLVED / Gravity Stabilized)",
        "- Node 02: Well B (Posture 72/140 / Gravitic Focal Ring Fractured)",
        "- Node 03: Agent Kang (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 04: Agent Bae (Driving Bulwark Maul into Core Ring)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP [SURGE] | HP 140/140 | SP +35 | Posture 80/80",
        "- Agent Bae   : Spd 6 -> 3 AP | HP 135/135 | SP +30 | Posture 75/75",
        "- Well A      : HP 0/280 [DESTROYED]",
        "- Well B      : Spd 3 -> 1 AP | HP 172/280 | Posture 72/140 [ENGAGED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — GLOBAL SANITY VORTEX & SHEAR NULLIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [WELL-B][KANG]  [BAE]                   [AYSHUK]        [MAJIN]",
        "---",
        "- Node 02: Well B (Recovered / Channeling Global Sanity Vortex)",
        "- Node 03: Agent Kang (Directional Guard Absorption Active)",
        "- Node 04: Agent Bae (Smashing Gravitic Focal Ring)",
        "- Node 07: Research Lead Ayshuk (Clarity Field Nullifying Vortex)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP | HP 132/140 | SP +35 | Posture 70/80",
        "- Agent Bae   : Spd 6 -> 3 AP | HP 135/135 | SP +30 | Posture 75/75",
        "- Well B      : Spd 3 -> 1 AP | HP 82/280  | Posture 22/140 [UNSTABLE]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER ON WELL B]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [WELL-B]                                [AYSHUK]        [MAJIN]",
        "                [KANG]  [BAE]",
        "---",
        "- Node 02: Well B (TERMINAL STAGGER / POSTURE 0/140 / 2.0x DMG)",
        "- Node 03: Agent Kang & Bae (Synchronized Double Sunder)",
        "---",
        "- Well B      : Spd 0 -> 0 AP | HP 16/280  | Posture 0/140 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [MIST]  [KANG]  [BAE]                   [AYSHUK]        [MAJIN]",
        "---",
        "- Node 02: Wells (Imploded into Harmless Mist / Han Siphoned)",
        "- Node 03: Agent Kang & Bae (Logging Gravitic Normalization)",
        "---",
        "- Wells       : HP 0/280 [PURIFIED] | +0.026 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Synchronized Slam & Stagger on Well A)
- **Synchronized Sunder & Focal Disruption**:
  * Kang and Bae land a synchronized double maul strike on Gravitic Well A at Node 03:
    * Deals **48 Grudge Damage**!
    * Inflicts +38 Posture Strain. Well A Posture drops to **50/140**, breaching the **60% Posture Threshold (84 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** Well A's event horizon collapses inwards.
  * Well A HP drops to **118/280**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Well A Implosion & Momentum Surge)
- **Vanguard Overload (1.5x Direct Damage)**:
  * Agent Kang's `Momentum Surge` activates! (+2 Speed next turn). Kang delivers a crushing finishing slam:
    * Deals **68 Grudge Damage**! Well A HP hits **0/280**!
    * Well A implodes harmlessly, dissipating its gravitational field.
  * Bae attacks Well B's focal ring, dealing **34 damage**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Global Sanity Vortex & Clarity Field)
- **Hostile Desperation Vortex**:
  * Well B attempts to tear the minds of all operatives with `[Global Sanity Vortex]`.
  * Research Lead Ayshuk activates Floor 4's *Clarity Field*, altering psychic frequencies to nullify the sanity drain!
  * Agent Kang deploys `[Directional Guard Absorption]`, taking 8 chip damage (HP: 132/140).
  * Agent Bae smashes the gravitic focal ring, stripping 26 Posture points!
  * Well B Posture falls to **16/140**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger on Well B)
- **Focal Ring Shatter**:
  * Bae lands a heavy blow, stripping the final 16 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/140**.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Dual Overdrive Climax Shatter**:
  * Kang and Bae execute a dual overdrive strike. Well B implodes into harmless purple mist and pure Han vapor.
  * Floor 4 collection flues harvest **+0.026 tons of refined Han**!
"""

# --- DAY 141 EXPANSION ---
def get_day_141_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 5 SUBTERRANEAN SLUICE TRENCH]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[WORM-A][WORM-B][KANG]  [CHA]                   [MELLDA]        [MAJIN]",
        "---",
        "- Node 01: Magma Worm A (Posture 54/140 / Carapace Fractured by Kang)",
        "- Node 02: Magma Worm B (Pinned by Smiths with Brass Pegs / Band 1)",
        "- Node 03: Agent Kang (Point-Blank Band 1 / Heavy Maul Cleaving)",
        "- Node 04: Agent Cha (Range Band 2 / Thermal Spike Aimed)",
        "- Node 07: Border Lead Mellda (Bulwark Shield / Sluice Gate Locked)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 140/140 | SP +35 | Posture 80/80",
        "- Agent Cha   : Spd 5 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Mellda      : Spd 6 -> 3 AP | HP 195/195 | SP +40 | Posture 95/95",
        "- Worm A      : Spd 3 -> 1 AP | HP 152/300 | Posture 54/140 [CRACKED]",
        "- Worm B      : Spd 2 -> 1 AP | HP 280/300 | Posture 110/140 [PINNED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER ON WORM A]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MOLTEN]        [WORM-B][KANG]  [CHA]           [MELLDA]        [MAJIN]",
        "---",
        "- Node 01: Worm A (SHATTERED & PULVERIZED / Molten Siphoned)",
        "- Node 02: Worm B (Posture 62/140 / Smiths Driving Brass Stakes)",
        "- Node 03: Agent Kang (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 04: Agent Cha (Driving Thermal Spike into Soft Segment)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP [SURGE] | HP 140/140 | SP +35 | Posture 80/80",
        "- Agent Cha   : Spd 5 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Worm A      : HP 0/300 [DESTROYED]",
        "- Worm B      : Spd 2 -> 1 AP | HP 184/300 | Posture 62/140 [ENGAGED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — TRENCH COLLAPSER & SLUICE LOCK]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [WORM-B][KANG]  [CHA]                   [MELLDA]        [MAJIN]",
        "---",
        "- Node 02: Worm B (Recovered / Channeling Trench Collapser)",
        "- Node 03: Agent Kang (Directional Guard Absorption Active)",
        "- Node 04: Agent Cha (Thermal Spike Superheating Ventral Core)",
        "- Node 07: Border Lead Mellda (Locking Drainage Sluice Gates)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP | HP 132/140 | SP +35 | Posture 70/80",
        "- Agent Cha   : Spd 5 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Worm B      : Spd 2 -> 1 AP | HP 82/300  | Posture 20/140 [CRITICAL]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER ON WORM B]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [WORM-B]                                [MELLDA]        [MAJIN]",
        "                [KANG]  [CHA]",
        "---",
        "- Node 02: Worm B (TERMINAL STAGGER / POSTURE 0/140 / 2.0x DMG)",
        "- Node 03: Agent Kang (Shattering Cephalic Shell)",
        "- Node 04: Agent Cha (Thermal Spike Piercing Exposed Ventral Nerve)",
        "---",
        "- Worm B      : Spd 0 -> 0 AP | HP 16/300  | Posture 0/140 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [CHITIN][KANG]  [CHA]                   [MELLDA]        [MAJIN]",
        "---",
        "- Node 02: Worm B (Decapitated / Dissolved to Molten Chitin)",
        "- Node 03: Agent Kang (Securing Sluice Perimeter)",
        "- Node 04: Agent Cha (Venting Thermal Bracer)",
        "---",
        "- Worms       : HP 0/300 [PURIFIED] | +0.026 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Brass Pin & Stagger on Worm A)
- **Trench Pincer & Thermal Focus**:
  * Cheonbulok smiths pin Worm B at Node 02 with heavy brass stakes.
  * Agent Kang smashes Worm A's anterior carapace with the heavy maul at Node 03:
    * Deals **48 Grudge Damage**!
    * Inflicts +38 Posture Strain. Worm A Posture drops to **52/140**, breaching the **60% Posture Threshold (84 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The magma worm thrash halts in a cloud of scalding steam.
  * Worm A HP drops to **124/300**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Worm A Annihilation & Momentum Surge)
- **Decapitation (1.5x Direct Damage)**:
  * Agent Kang's `Momentum Surge` activates! (+2 Speed next turn). Kang delivers a heavy downward cleave:
    * Deals **72 Grudge Damage**! Worm A HP hits **0/300**!
    * Worm A dissolves into glowing molten sediment on the trench floor.
  * Agent Cha targets Worm B's soft segment with the thermal spike, dealing **36 damage**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Trench Collapser & Sluice Lock)
- **Hostile Desperation Charge**:
  * Worm B attempts `[Trench Collapser]` to rupture the drainage gates.
  * Border Lead Mellda locks the sluice bulkheads, anchoring the channel!
  * Agent Kang deploys `[Directional Guard Absorption]`, taking 8 chip damage (HP: 132/140).
  * Agent Cha drives the thermal spike into Worm B's ventral core, stripping 26 Posture points!
  * Worm B Posture falls to **14/140**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger on Worm B)
- **Cephalic Shatter & Terminal Collapse**:
  * Cha drives the spike home, stripping the final 14 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/140**.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Dual Kinetic Decapitation**:
  * Kang and Cha execute a synchronized decapitation. The burrowers dissolve into molten chitin and pure Han vapor.
  * Floor 5 drainage flues harvest **+0.026 tons of refined Han**!
"""

# --- DAY 145 EXPANSION ---
def get_day_145_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 8 HORIZON THRESHOLD PLAZA]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[GATEWAY][KANG] [KIM]   [SEO]   [HONG]                          [MAJIN]",
        "---",
        "- Node 01: Pale Gateway (Posture 84/200 / Four Aspects Balanced)",
        "- Node 02: Agent Kang (Point-Blank Band 1 / Sunder on Left Pylon)",
        "- Node 03: Agent Kim (Point-Blank Band 1 / Grounding Right Pylon)",
        "- Node 04: Agent Seo (Range Band 2 / Void Incision on Keystone)",
        "- Node 05: Agent Hong (Range Band 3 / Choral Lament Harmonics)",
        "- Node 10: Director Majin & Seiyon Command Console (Band 5)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 140/140 | SP +35 | Posture 80/80",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 135/135 | SP +30 | Posture 75/75",
        "- Agent Seo   : Spd 5 -> 3 AP | HP 125/125 | SP +30 | Posture 65/65",
        "- Agent Hong  : Spd 6 -> 3 AP | HP 130/130 | SP +40 | Posture 70/70",
        "- Pale Gateway: Spd 5 -> 3 AP | HP 280/420 | Posture 84/200 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[GATEWAY]       [KANG]  [KIM]   [SEO]   [HONG]                  [MAJIN]",
        "---",
        "- Node 01: Pale Gateway (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 03: Agent Kang (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 04: Agent Kim (Foundation Greaves Locking Bedrock)",
        "- Node 05: Agent Seo (Void Disruption Stripping Pale Matrix)",
        "- Node 06: Agent Hong (Saint Robe Pure Lament Weeping)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP [SURGE] | HP 140/140 | SP +35 | Posture 80/80",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 135/135 | SP +30 | Posture 75/75",
        "- Gateway     : Spd 0 -> 0 AP | HP 142/420 | Posture 32/200 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — RADIANT HORIZON SHOCKWAVE REACTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[GATEWAY][KANG] [KIM]   [SEO]   [HONG]                          [MAJIN]",
        "---",
        "- Node 01: Pale Gateway (Recovered / Channeling Horizon Shockwave)",
        "- Node 02: Agent Kang (Directional Guard Absorption Active)",
        "- Node 03: Agent Kim (Grounding Shockwave into Floorplates)",
        "- Node 05: Agent Hong (Saint Robe Weeping Purging Pale Frequency)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP | HP 130/140 | SP +35 | Posture 68/80",
        "- Agent Kim   : Spd 5 -> 3 AP | HP 126/135 | SP +30 | Posture 64/75",
        "- Gateway     : Spd 4 -> 2 AP | HP 68/420  | Posture 14/200 [UNSTABLE]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[GATEWAY]                                                       [MAJIN]",
        "        [KANG]  [KIM]   [SEO]   [HONG]",
        "---",
        "- Node 01: Pale Gateway (TERMINAL STAGGER / POSTURE 0/200 / 2.0x DMG)",
        "- Node 02: Agent Kang & Kim (Shattering Left and Right Pylons)",
        "- Node 04: Agent Seo & Hong (Cleaving Keystone Keystone)",
        "---",
        "- Gateway     : Spd 0 -> 0 AP | HP 18/420  | Posture 0/200 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[GOLD-DAWN][KANG][KIM]  [SEO]   [HONG]                          [MAJIN]",
        "---",
        "- Node 01: Pale Gateway (Resolved into Golden Dawn & Radiant Han)",
        "- Node 02: Four Operatives (Reporting Absolute Mid-Year Clearance)",
        "---",
        "- Gateway     : HP 0/420 [PURIFIED] | +0.035 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Four-Aspect Strike & Stagger Build)
- **Quadruple Elemental Convergence**:
  * Agent Kang smashes the left pylon with Grudge force, Agent Kim grounds the right pylon with Weight, Agent Seo pierces the keystone with Void, and Agent Hong channels pure Lament weeping:
    * Deals **56 Multi-Affinity Damage**!
    * Inflicts +42 Posture Strain. Gateway Posture drops to **78/200**, breaching the **60% Posture Threshold (120 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The pale gateway shudders, its blinding light softening to warm gold.
  * Gateway HP drops to **224/420**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Pylon Shatter & Momentum Surge)
- **Allied Focus Fire (1.5x Direct Damage)**:
  * Agent Kang's `Momentum Surge` activates! (+2 Speed next turn). Kang delivers a crushing blow: **64 Damage**!
  * Hong and Seo discharge synchronized harmonic beams: **58 Damage**!
  * Gateway HP collapses from 224 to **102/420**! Posture drops to **24/200**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Radiant Horizon Shockwave Desperation)
- **Hostile Desperation Pulse**:
  * The Pale Gateway recovers, pulsing `[Radiant Horizon Shockwave]` across all nodes.
  * Agent Kim deploys *Foundation Greaves*, grounding the shockwave into the bedrock!
  * Agent Kang deploys `[Directional Guard Absorption]`, taking 10 chip damage (HP: 130/140).
  * Agent Hong channels pure sorrow harmonic from the Saint Robe, canceling the Pale radiation!
  * Gateway HP falls to **46/420**! Posture drops to **8/200**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Keystone Severance & Terminal Collapse**:
  * Seo and Hong slice through the keystone, stripping the final 8 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/200**.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Quadruple Overdrive Climax Strike**:
  * Kang, Kim, Seo, and Hong execute a synchronized four-element finisher.
  * The Pale Gateway dissolves into a shower of warm, radiant golden dawn and pure Han vapor.
  * Horizon collection flues harvest **+0.035 tons of refined Han**!
"""

def update_part_7():
    path = "SOMNARAK-WORLD/The_Absolvohan/Part_7_Days_125_to_145.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Day 125
    old_d125 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Kang hammers thorax; Shin focuses Lament; Beetle-A 60%   |
| Stagger 1.                                                          |
| - Turn 03: Carapace cracked; direct Grudge blunt strikes deal 2.0x  |
| direct damage.                                                      |
| - Turn 04: Beetle-B charges mandibles; Dekan locks Jaw Clamp at     |
| Node 2.                                                             |
| - Turn 05: Shin channels acoustic wave into exposed marrow;         |
| Terminal Stagger.                                                   |
| - Turn 06: Kang executes Climax Maul Shatter; beetles dissolve to   |
| amber gravel.                                                       |
+=====================================================================+
```"""
    if old_d125 in content:
        content = content.replace(old_d125, get_day_125_combat())
        print("Replaced Day 125 summary successfully!")

    # Day 127
    old_d127 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Noh severs feeder tendrils; Hwang chills main valve; 60% |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; cryo-Lament strikes deal 2.0x direct     |
| damage.                                                             |
| - Turn 04: Siphon-B surges [Bleed Deluge]; Ishall deploys Shadow    |
| Ingress.                                                            |
| - Turn 05: Hwang's cryo incision freezes internal conduits;         |
| Terminal Stagger.                                                   |
| - Turn 06: Kang executes Climax Maul Smash; frozen siphons shatter  |
| to ice.                                                             |
+=====================================================================+
```"""
    if old_d127 in content:
        content = content.replace(old_d127, get_day_127_combat())
        print("Replaced Day 127 summary successfully!")

    # Day 132
    old_d132 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Kang blocks scythe; Jin fires sonic bell; Sweeper-A 60%  |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; direct Grudge blunt strikes deal 2.0x    |
| direct damage.                                                      |
| - Turn 04: Sweeper-B accelerates [Rotary Severance]; Marjuk engages |
| stasis.                                                             |
| - Turn 05: Jin disrupts gear synchronizer; forces Terminal Stagger  |
| on both.                                                            |
| - Turn 06: Kang executes Climax Maul Sweep; drive sprockets         |
| pulverized.                                                         |
+=====================================================================+
```"""
    if old_d132 in content:
        content = content.replace(old_d132, get_day_132_combat())
        print("Replaced Day 132 summary successfully!")

    # Day 137
    old_d137 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Kang & Bae deliver synchronized slam; Well-A hits 60%    |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; direct Grudge blunt strikes deal 2.0x    |
| direct damage.                                                      |
| - Turn 04: Well-B charges [Global Sanity Vortex]; Ayshuk predicts   |
| firing arc.                                                         |
| - Turn 05: Bae smashes gravitic focal ring, forcing Terminal        |
| Stagger.                                                            |
| - Turn 06: Dual Overdrive Climax Shatter; wells implode to harmless |
| mist.                                                               |
+=====================================================================+
```"""
    if old_d137 in content:
        content = content.replace(old_d137, get_day_137_combat())
        print("Replaced Day 137 summary successfully!")

    # Day 141
    old_d141 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Smiths pin Worm-B with brass; Kang fractures Worm-A; 60% |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; direct Grudge/Thermal strikes deal 2.0x  |
| direct damage.                                                      |
| - Turn 04: Worm-A charges [Trench Collapser]; Mellda locks drainage |
| sluice.                                                             |
| - Turn 05: Cha drives thermal spike into soft segment; forces       |
| Terminal Stagger.                                                   |
| - Turn 06: Dual kinetic decapitation; burrowers dissolve to molten  |
| chitin.                                                             |
+=====================================================================+
```"""
    if old_d141 in content:
        content = content.replace(old_d141, get_day_141_combat())
        print("Replaced Day 141 summary successfully!")

    # Day 145
    old_d145 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Four-Aspect Strike lands; balances all 4 affinities; 60% |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; all 4 damage types deal 2.0x direct      |
| damage.                                                             |
| - Turn 04: Gateway pulses [Radiant Horizon Shockwave]; Kim grounds  |
| pylons.                                                             |
| - Turn 05: Hong channels pure sorrow harmonic, reducing Pale        |
| resonance.                                                          |
| - Turn 06: Quadruple Overdrive Climax Strike; Gateway resolves to   |
| golden dawn.                                                        |
+=====================================================================+
```"""
    if old_d145 in content:
        content = content.replace(old_d145, get_day_145_combat())
        print("Replaced Day 145 summary successfully!")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated Part 7 successfully!")

if __name__ == "__main__":
    update_part_7()
