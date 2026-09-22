#!/usr/bin/env python3
"""
tools/expand_part_5.py
Replaces the compressed Turns 02-06 summaries on Day 77, Day 82, Day 87, Day 92, and Day 97
with exhaustive, turn-by-turn tactical combat logs utilizing the 10-node spatial engine,
Four P-framework (Passives, Panic, Parry, Posture), Speed/AP, and M.A.W.-W modifiers.
"""

def make_box(title, rows, width=71):
    top = "+" + "=" * (width - 2) + "+"
    bottom = "+" + "=" * (width - 2) + "+"
    sep = "+" + "-" * (width - 2) + "+"
    
    out = [top]
    if title:
        title_str = f" {title} "
        out.append(f"|{title_str.center(width - 2)}|")
        out.append(sep)
    
    for r in rows:
        if r == "---":
            out.append(sep)
        elif r.startswith("==="):
            out.append(top)
        else:
            text = r[:width - 4]
            out.append(f"| {text.ljust(width - 4)} |")
    out.append(bottom)
    return "\n".join(out)

# --- DAY 77 EXPANSION ---
def get_day_77_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 6 ARCHIVE DEEP SUB-VAULT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[FOSSIL][YOO]           [MARJUK]                [MAJIN]                 ",
        "---",
        "- Node 01: Fossilized Titan (Posture 72/150 / Rib Cage Fractured)",
        "- Node 02: Agent Yoo (Point-Blank Band 1 / Heavy Maul Cleaving)",
        "- Node 05: Archive Lead Marjuk (Range Band 3 / Easing Stasis Field)",
        "- Node 08: Director Majin & Seiyon Command Console (Band 4)",
        "---",
        "- Agent Yoo    : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 70/70",
        "- Marjuk       : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 90/90",
        "- Fossil Titan : Spd 3 -> 1 AP | HP 198/320 | Posture 72/150 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[FOSSIL]        [YOO]   [MARJUK]                [MAJIN]                 ",
        "---",
        "- Node 01: Fossil Titan (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 03: Agent Yoo (Advancing with Momentum Surge / +2 Speed)",
        "- Node 04: Archive Lead Marjuk (Applying Chronological Seal)",
        "---",
        "- Agent Yoo    : Spd 8 -> 4 AP [SURGE] | HP 125/125 | SP +30 | Posture 70/70",
        "- Marjuk       : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 90/90",
        "- Fossil Titan : Spd 0 -> 0 AP | HP 102/320 | Posture 24/150 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — GRAVITATIONAL SINGULARITY COUNTER-SURGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[FOSSIL][YOO]           [MARJUK]                [MAJIN]                 ",
        "---",
        "- Node 01: Fossil Titan (Recovered / Channeling Singularity Pulse)",
        "- Node 02: Agent Yoo (Directional Guard Absorption Active)",
        "- Node 05: Archive Lead Marjuk (Freezing Vertebrae with Stasis Field)",
        "---",
        "- Agent Yoo    : Spd 8 -> 4 AP | HP 118/125 | SP +30 | Posture 62/70",
        "- Marjuk       : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 90/90",
        "- Fossil Titan : Spd 3 -> 1 AP | HP 54/320  | Posture 10/150 [UNSTABLE]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[FOSSIL]                                        [MAJIN]                 ",
        "        [YOO]   [MARJUK]",
        "---",
        "- Node 01: Fossil Titan (TERMINAL STAGGER / POSTURE 0/150 / 2.0x DMG)",
        "- Node 02: Agent Yoo (Crushing Pelvic Pivot)",
        "- Node 03: Archive Lead Marjuk (Locking Stasis Field over Skull)",
        "---",
        "- Agent Yoo    : Spd 6 -> 3 AP | HP 118/125 | SP +30 | Posture 62/70",
        "- Marjuk       : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 90/90",
        "- Fossil Titan : Spd 0 -> 0 AP | HP 16/320  | Posture 0/150 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[GRAVEL][YOO]           [MARJUK]                [MAJIN]                 ",
        "---",
        "- Node 01: Fossil Titan (Disintegrated to Gravel / Han Siphoned)",
        "- Node 02: Agent Yoo (Resting Maul / Wiping Bone Dust)",
        "- Node 05: Archive Lead Marjuk (Deactivating Stasis Cannons)",
        "---",
        "- Agent Yoo    : Spd 6 -> 3 AP | HP 118/125 | SP +35 | Posture 70/70",
        "- Marjuk       : Spd 5 -> 3 AP | HP 180/180 | SP +40 | Posture 90/90",
        "- Fossil Titan : HP 0/320 [PURIFIED] | +0.022 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Rib Cage Fracture & Stagger Build)
- **Heavy Breacher Assault**:
  * **Agent Yoo (Speed 6 -> 3 AP)**: Stands at Node 02 in Point-Blank Band 1. Spends 2 AP to execute `[Heavy Maul Rib Sunder]`:
    * Grudge Base 20 * Grudge Vulnerability (1.5x) = **30 Direct Damage**!
    * Inflicts +32 Posture Strain. Titan Posture drops to **58/150**, breaching the **60% Posture Threshold (90 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The petrified rib cage shatters, spraying calcified rock shards across Node 01.
  * **Archive Lead Marjuk**: From Node 05 (Range Band 3), pulses the stasis cannons to lock the titan's hips in amber: **24 Void damage**.
  * Titan HP drops to **158/320**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Vanguard Overload (1.5x Direct Damage)**:
  * Agent Yoo's `Momentum Surge` activates! (+2 Speed next turn). Yoo unleashes an overhead maul smash into the exposed spinal column: **56 Grudge Damage**!
  * Marjuk freezes the lumbar vertebrae, dealing **32 Damage**!
  * Titan HP collapses from 158 to **70/320**! Posture drops to **18/150**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Gravitational Singularity Desperation)
- **Hostile Recovery & Desperation Singularity**:
  * The Fossilized Titan recovers, opening its rib cage to draw all adjacent matter into a gravitational singularity: `[Gravitational Pull]`.
  * Agent Yoo deploys `[Directional Guard Absorption]`, grounding his heavy maul into the floorplates to resist displacement; absorbs 7 damage (HP: 118/125).
  * Marjuk aims the stasis emitters directly into the vortex, neutralizing the gravitational pull!
  * Titan HP falls to **34/320**! Posture drops to **4/150**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Pelvic Sunder & Terminal Collapse**:
  * Agent Yoo strikes the pelvic pivot, stripping the remaining 4 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/150**. The skeleton buckles under its own petrified weight.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Pulverize**:
  * Agent Yoo executes `[Climax Pulverize: Sunder of Ages]`. The entire fossilized titan disintegrates into harmless gravel and refined Han vapor.
  * Floor 6 pneumatic flues harvest **+0.022 tons of refined Han**!
"""

# --- DAY 82 EXPANSION ---
def get_day_82_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 5 OUTER DRAINAGE SLUICE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[WORM-A][WORM-B][KANG]  [NOH]                   [MELLDA]        [MAJIN]",
        "---",
        "- Node 01: Chitinous Worm A (Posture 48/120 / Mandible Severed)",
        "- Node 02: Chitinous Worm B (Charging Subterranean Sunder / Posture 120/120)",
        "- Node 03: Agent Kang (Point-Blank Band 1 / Cleaving Segment Joints)",
        "- Node 04: Agent Noh (Range Band 2 / Clockwork Bayonet Piercing)",
        "- Node 07: Border Lead Mellda (Bulwark Shield / Sluice Gate Locked)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Agent Noh   : Spd 6 -> 3 AP | HP 120/120 | SP +25 | Posture 60/60",
        "- Mellda      : Spd 6 -> 3 AP | HP 195/195 | SP +35 | Posture 95/95",
        "- Worm A      : Spd 3 -> 1 AP | HP 142/260 | Posture 48/120 [CRACKED]",
        "- Worm B      : Spd 4 -> 2 AP | HP 260/260 | Posture 120/120"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1 ON WORM A]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SEDIMENT][WORM-B][KANG][NOH]                   [MELLDA]        [MAJIN]",
        "---",
        "- Node 01: Worm A (SHATTERED & PULVERIZED / Sediment Siphoned)",
        "- Node 02: Worm B (Posture 72/120 / Segment Joints Exposed)",
        "- Node 03: Agent Kang (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 04: Agent Noh (Bayonet Thrust Landed)",
        "- Node 07: Border Lead Mellda (Holding Sluice)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP [SURGE] | HP 130/130 | SP +30 | Posture 70/70",
        "- Agent Noh   : Spd 6 -> 3 AP | HP 120/120 | SP +25 | Posture 60/60",
        "- Worm A      : HP 0/260 [DESTROYED]",
        "- Worm B      : Spd 3 -> 1 AP | HP 168/260 | Posture 72/120 [ENGAGED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — TRENCH COLLAPSER COUNTER-SURGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [WORM-B][KANG]  [NOH]                   [MELLDA]        [MAJIN]",
        "---",
        "- Node 02: Worm B (Recovered / Channeling Trench Collapser)",
        "- Node 03: Agent Kang (Spd 8 / AP 4 / Heavy Maul Cross-Slash)",
        "- Node 04: Agent Noh (Directional Guard Absorption Active)",
        "- Node 07: Border Lead Mellda (Locking Drainage Sluice Gates)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Agent Noh   : Spd 6 -> 3 AP | HP 114/120 | SP +25 | Posture 52/60",
        "- Mellda      : Spd 6 -> 3 AP | HP 195/195 | SP +35 | Posture 95/95",
        "- Worm B      : Spd 3 -> 1 AP | HP 82/260  | Posture 24/120 [CRITICAL]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER ON WORM B]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [WORM-B]                                [MELLDA]        [MAJIN]",
        "                [KANG]  [NOH]",
        "---",
        "- Node 02: Worm B (TERMINAL STAGGER / POSTURE 0/120 / 2.0x DMG)",
        "- Node 03: Agent Kang (Severing Cephalic Nerve)",
        "- Node 04: Agent Noh (Driving Bayonet into Heart Segment)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Agent Noh   : Spd 6 -> 3 AP | HP 114/120 | SP +25 | Posture 52/60",
        "- Worm B      : Spd 0 -> 0 AP | HP 18/260  | Posture 0/120 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — DUAL DECAPITATION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [ASH]   [KANG]  [NOH]                   [MELLDA]        [MAJIN]",
        "---",
        "- Node 02: Worm B (Decapitated / Dissolved into Amber Sediment)",
        "- Node 03: Agent Kang (Sheathing Blade / Securing RHR)",
        "- Node 04: Agent Noh (Reporting Sluice Clear)",
        "- Node 07: Border Lead Mellda (Opening Transit Gates)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 130/130 | SP +35 | Posture 70/70",
        "- Agent Noh   : Spd 6 -> 3 AP | HP 114/120 | SP +30 | Posture 60/60",
        "- Mellda      : Spd 6 -> 3 AP | HP 195/195 | SP +40 | Posture 95/95",
        "- Worms       : HP 0/260 [PURIFIED] | +0.024 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Jaw Severance & Stagger on Worm A)
- **Synchronized Vanguard Strike**:
  * **Agent Kang (Speed 6 -> 3 AP)**: Smashes Worm A's primary mandible with the heavy maul:
    * Deals **36 Grudge Damage**!
    * Inflicts +28 Posture Strain. Worm A Posture drops to **44/120**, breaching the **60% Posture Threshold (72 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** Worm A recoils, its burrowing jaws paralyzed.
  * **Agent Noh (Speed 6 -> 3 AP)**: Operating from Node 04 (Range Band 2), drives a precision bayonet thrust into Worm B's segment joint for **28 piercing damage**.
  * Worm A HP drops to **112/260**; Worm B HP drops to **204/260**.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Worm A Annihilation & Momentum Surge)
- **Stagger Exploitation & Execution (1.5x Direct Damage)**:
  * Agent Kang's `Momentum Surge` activates! (+2 Speed next turn). Kang delivers a crushing downward execution blow:
    * Deals **58 Grudge Damage**! Worm A HP hits **0/260**!
    * Worm A shatters into harmless amber sediment and dissolves into Han mist!
  * Agent Noh targets Worm B's exposed ventral nerve, dealing **32 damage**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Trench Collapser Desperation)
- **Hostile Desperation Counter-Surge**:
  * Worm B recovers, thrashing wildly to trigger `[Trench Collapser]`—attempting to cave in the sluice walls.
  * Border Lead Mellda engages the sluice locks, anchoring the foundation plates!
  * Agent Noh deploys `[Directional Guard Absorption]`, taking 6 chip damage (HP: 114/120) while covering Kang.
  * Agent Kang (Speed 8 under Surge -> 4 AP) executes a double maul strike into Worm B's neck, dealing **44 damage**!
  * Worm B Posture falls to **16/120**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger on Worm B)
- **Nerve Severance & Terminal Collapse**:
  * Agent Noh drives the clockwork bayonet deep into the central nerve cluster, stripping the final 16 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/120**. Worm B collapses motionless onto the drainage grates.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Dual Decapitation**:
  * Kang and Noh execute a synchronized cross-decapitation. Worm B dissolves into fine amber sediment and refined Han vapor.
  * Floor 5 drainage flues harvest **+0.024 tons of refined Han**!
"""

# --- DAY 87 EXPANSION ---
def get_day_87_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 2 CORRIDOR EAST]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[HUSK-1][NOH]   [HUSK-2][SHIN]  [KANG]                  [DEKAN]         ",
        "---",
        "- Node 01: Sanguine Husk 1 (Posture 36/90 / Pinned by Noh)",
        "- Node 02: Agent Noh (Point-Blank Band 1 / Bayonet Locked)",
        "- Node 03: Sanguine Husk 2 (Preparing Pincer Charge / Posture 90/90)",
        "- Node 04: Agent Shin (Range Band 2 / Choral Staff Lament Firing)",
        "- Node 05: Agent Kang (Range Band 3 / Heavy Maul Ready to Intercept)",
        "- Node 08: Containment Lead Dekan (Observation Post / Band 4)",
        "---",
        "- Agent Noh   : Spd 6 -> 3 AP | HP 120/120 | SP +25 | Posture 60/60",
        "- Agent Shin  : Spd 6 -> 3 AP | HP 115/115 | SP +30 | Posture 55/55",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Husk 1      : Spd 3 -> 1 AP | HP 82/180  | Posture 36/90 [CRACKED]",
        "- Husk 2      : Spd 4 -> 2 AP | HP 180/180 | Posture 90/90"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER ON HUSK 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SLUDGE]        [HUSK-2][SHIN]  [KANG]                  [DEKAN]         ",
        "        [NOH]",
        "---",
        "- Node 01: Husk 1 (CRUSHED & PULVERIZED / Sludge Siphoned)",
        "- Node 02: Agent Noh (Momentum Surge Primed / +2 Speed Next Turn)",
        "- Node 03: Husk 2 (Exposed / Posture 54/90)",
        "- Node 04: Agent Shin (Choral Lament Pulse Continuing)",
        "- Node 05: Agent Kang (Advancing with Heavy Maul)",
        "---",
        "- Agent Noh   : Spd 8 -> 4 AP [SURGE] | HP 120/120 | SP +25 | Posture 60/60",
        "- Agent Shin  : Spd 6 -> 3 AP | HP 115/115 | SP +30 | Posture 55/55",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Husk 1      : HP 0/180 [ELIMINATED]",
        "- Husk 2      : Spd 4 -> 2 AP | HP 128/180 | Posture 54/90 [ENGAGED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — PINCER CHARGE & JAW CLAMP PIN]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [NOH]   [HUSK-2][SHIN]  [KANG]                  [DEKAN]         ",
        "---",
        "- Node 02: Agent Noh (Spd 8 / AP 4 / Rapid Bayonet Incisions)",
        "- Node 03: Husk 2 (Pinned by Dekan's Jaw Clamp / Posture 24/90)",
        "- Node 04: Agent Shin (Wide-Angle Acoustic Wave Firing)",
        "- Node 05: Agent Kang (Directional Guard Absorption Active)",
        "---",
        "- Agent Noh   : Spd 8 -> 4 AP | HP 120/120 | SP +25 | Posture 60/60",
        "- Agent Shin  : Spd 6 -> 3 AP | HP 115/115 | SP +30 | Posture 55/55",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 124/130 | SP +30 | Posture 62/70",
        "- Husk 2      : Spd 2 -> 1 AP | HP 64/180  | Posture 24/90 [PINNED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER ON HUSK 2]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                [HUSK-2]                                [DEKAN]         ",
        "        [NOH]   [SHIN]  [KANG]",
        "---",
        "- Node 03: Husk 2 (TERMINAL STAGGER / POSTURE 0/90 / 2.0x DMG)",
        "- Node 02: Agent Noh (Pinning Right Arm)",
        "- Node 03: Agent Shin (Choral Pulse Shattered Psychic Cohesion)",
        "- Node 04: Agent Kang (Priming Climax Sweep)",
        "---",
        "- Agent Noh   : Spd 6 -> 3 AP | HP 120/120 | SP +25 | Posture 60/60",
        "- Agent Shin  : Spd 6 -> 3 AP | HP 115/115 | SP +30 | Posture 55/55",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 124/130 | SP +30 | Posture 62/70",
        "- Husk 2      : Spd 0 -> 0 AP | HP 16/180  | Posture 0/90 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [SLUDGE][NOH]   [SHIN]  [KANG]                  [DEKAN]         ",
        "---",
        "- Node 01-03: All Husks (Pulverized to Sludge / Siphoned)",
        "- Node 02: Agent Noh (Retracting Bayonet)",
        "- Node 03: Agent Shin (Lowering Choral Staff)",
        "- Node 04: Agent Kang (Reporting Sector 2 Clear)",
        "---",
        "- Agent Noh   : Spd 6 -> 3 AP | HP 120/120 | SP +30 | Posture 60/60",
        "- Agent Shin  : Spd 6 -> 3 AP | HP 115/115 | SP +35 | Posture 55/55",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 124/130 | SP +35 | Posture 70/70",
        "- Husks       : HP 0/180 [DESTROYED] | +0.022 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Lead Husk Stagger)
- **Pin & Lament Focus**:
  * **Agent Noh**: Holds Husk 1 pinned with the clockwork bayonet at Node 02.
  * **Agent Shin**: Firing from Node 04, channels a high-frequency Lament wave from the Choral Staff:
    * Deals **38 Pure Lament Damage**!
    * Inflicts +26 Posture Strain. Husk 1 Posture drops to **34/90**, breaching the **60% Posture Threshold (54 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** Husk 1's bloody shroud slackens.
  * Husk 1 HP drops to **64/180**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Husk 1 Crushed & Momentum Surge)
- **Crushing Blow (1.5x Direct Damage)**:
  * Agent Noh's `Momentum Surge` activates! (+2 Speed next turn).
  * Agent Kang steps forward from Node 05, swinging the heavy maul down onto Husk 1's head:
    * Deals **64 Grudge Damage**! Husk 1 HP hits **0/180**!
    * Husk 1 dissolves into smoking crimson sludge on the deckplates.
  * Agent Shin directs her acoustic beam toward Husk 2, dealing **26 damage**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Pincer Charge & Jaw Clamp Pin)
- **Hostile Desperation Charge**:
  * Husk 2 attempts a desperate lunging charge to impale Agent Shin.
  * Containment Lead Dekan deploys Floor 2's *Jaw Clamp* floor traps, clamping Husk 2's ankles in heavy steel teeth!
  * Agent Kang deploys `[Directional Guard Absorption]`, absorbing 6 chip damage (HP: 124/130) while halting the charge!
  * Agent Noh (Speed 8 under Surge -> 4 AP) executes four rapid bayonet strikes, dealing **42 piercing damage**!
  * Husk 2 Posture falls to **18/90**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger on Husk 2)
- **Psychic Cohesion Shattered**:
  * Agent Shin unleashes a wide-angle harmonic blast, completely shattering the husk's psychic cohesion.
  * Posture hits **0/90**! **TERMINAL STAGGER TRIGGERED!** Husk 2 collapses helpless against the hydraulic clamps.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Sweep**:
  * Kang and Noh execute a coordinated sweeping finisher. Husk 2 dissolves into harmless red sludge and pure Han vapor.
  * Floor 2 drainage flues harvest **+0.022 tons of refined Han**!
"""

# --- DAY 92 EXPANSION ---
def get_day_92_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 3 EXTRACTION FORGE PLAZA]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[TITAN] [JIN]   [YOO]                   [MARJUK]                [MAJIN]",
        "---",
        "- Node 01: Clockwork Titan (Posture 76/160 / Boiler Exhaust Jammed)",
        "- Node 02: Agent Jin (Point-Blank Band 1 / Jamming Exhaust Pipe)",
        "- Node 03: Agent Yoo (Range Band 2 / Smashing Heavy Axle)",
        "- Node 06: Archive Lead Marjuk (Range Band 3 / Pre-Charging Stasis)",
        "- Node 09: Director Majin & Seiyon Command Console (Band 5)",
        "---",
        "- Agent Jin   : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 65/65",
        "- Agent Yoo   : Spd 6 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Marjuk      : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 90/90",
        "- Clock Titan : Spd 4 -> 2 AP | HP 245/360 | Posture 76/160 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[TITAN] [JIN]           [YOO]           [MARJUK]                [MAJIN]",
        "---",
        "- Node 01: Clockwork Titan (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 02: Agent Jin (Executing Steam Release Pin)",
        "- Node 04: Agent Yoo (Advancing with Momentum Surge / +2 Speed)",
        "- Node 06: Archive Lead Marjuk (Applying Stasis Field)",
        "---",
        "- Agent Jin   : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 65/65",
        "- Agent Yoo   : Spd 8 -> 4 AP [SURGE] | HP 130/130 | SP +30 | Posture 70/70",
        "- Marjuk      : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 90/90",
        "- Clock Titan : Spd 0 -> 0 AP | HP 122/360 | Posture 28/160 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — SELF-DESTRUCT SEQUENCE INITIATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[TITAN] [JIN]   [YOO]                   [MARJUK]                [MAJIN]",
        "---",
        "- Node 01: Clockwork Titan (Initiating Overheat Self-Destruct)",
        "- Node 02: Agent Jin (Severing Emergency Release Lever)",
        "- Node 03: Agent Yoo (Slamming Maul onto Main Relief Valve)",
        "- Node 06: Archive Lead Marjuk (Locking Stasis Barrier)",
        "---",
        "- Agent Jin   : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 65/65",
        "- Agent Yoo   : Spd 8 -> 4 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Marjuk      : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 90/90",
        "- Clock Titan : Spd 3 -> 1 AP | HP 58/360  | Posture 8/160 [OVERHEATING]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — CRITICAL VALVE SHUTDOWN & RETREAT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[TITAN]                                                 [ALL-AGENTS]    ",
        "---",
        "- Node 01: Clockwork Titan (TERMINAL STAGGER / POSTURE 0/160 / 2.0x DMG)",
        "- Node 08: All Operatives (Safely Evacuated behind Blast Bulkhead)",
        "- Node 08: Archive Lead Marjuk (Engaging Stasis Quarantine)",
        "---",
        "- Agent Jin   : Spd 6 -> 3 AP | HP 125/125 | SP +30 | Posture 65/65",
        "- Agent Yoo   : Spd 6 -> 3 AP | HP 130/130 | SP +30 | Posture 70/70",
        "- Marjuk      : Spd 5 -> 3 AP | HP 180/180 | SP +35 | Posture 90/90",
        "- Clock Titan : Spd 0 -> 0 AP | HP 12/360  | Posture 0/160 [MELTING]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CONTAINED DETONATION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SLAG]                                                  [ALL-AGENTS]    ",
        "---",
        "- Node 01: Clockwork Titan (Detonated inside Stasis Vault / 0 Casualties)",
        "- Node 08: Floor 3 Team (Venting Pressurized Steam / Siphoning RHR)",
        "- Node 08: Archive Lead Marjuk (Confirming Zero Structural Damage)",
        "---",
        "- All Agents  : ZERO DAMAGE SUSTAINED | +0.026 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Boiler Exhaust Jammed & Stagger Build)
- **Mechanical Sabotage**:
  * **Agent Jin**: Plants his spear directly down the titan's primary boiler exhaust pipe at Node 02, blocking the steam vent.
  * **Agent Yoo**: Delivers a crushing maul strike to the left drive axle:
    * Deals **42 Grudge Damage**!
    * Inflicts +34 Posture Strain. Titan Posture drops to **62/160**, breaching the **60% Posture Threshold (96 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** High-pressure steam erupts from failed gasket joints, stalling the titan's pistons.
  * Titan HP drops to **186/360**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Vanguard Overload (1.5x Direct Damage)**:
  * Agent Yoo's `Momentum Surge` activates! (+2 Speed next turn). Yoo delivers a massive two-handed swing into the exposed boiler shell: **64 Grudge Damage**!
  * Marjuk stabilizes the stasis barrier, dealing **28 damage**.
  * Titan HP collapses to **94/360**! Posture drops to **16/160**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Self-Destruct Initiation & Stasis Shield)
- **Hostile Overheat Counter-Surge**:
  * The Clockwork Titan enters a terminal thermal runaway: `[Self-Destruct Sequence]`, its boiler glowing cherry-red.
  * Agent Jin severs the emergency release lever, trapping the explosion inside the internal firebox!
  * Agent Yoo delivers a heavy blow to the relief valve, stripping another 10 Posture points!
  * Titan HP falls to **42/360**! Posture drops to **2/160**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger & Safe Evacuation)
- **Terminal Collapse & Tactical Fallback**:
  * Yoo delivers a final blow to the central valve, stripping the last 2 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/160**.
  * On Director Majin's order, all operatives sprint to Node 08 behind the reinforced titanium blast bulkhead!

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Contained Detonation & Purification)
- **Hermetic Containment**:
  * The Clockwork Titan detonates inside the sealed blast chamber. The stasis field and bulkheads absorb 100% of the explosive force with zero injuries to personnel!
  * Floor 3 filtration systems condense the vaporized bronze and refined Han: **+0.026 tons harvested**!
"""

# --- DAY 97 EXPANSION ---
def get_day_97_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 4 VOID OBSERVATION DOME]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MONOLITH][KANG] [HWANG]                 [AYSHUK]                [MAJIN]",
        "---",
        "- Node 01: Void Monolith (Posture 78/170 / Pedestal Cracked)",
        "- Node 02: Agent Kang (Point-Blank Band 1 / Smashing Crystalline Base)",
        "- Node 03: Agent Hwang (Range Band 2 / Blessed Scalpel Optical Strike)",
        "- Node 06: Research Lead Ayshuk (Predicting Death-Ray Trajectory)",
        "- Node 09: Director Majin & Seiyon Command Console (Band 5)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 135/135 | SP +30 | Posture 75/75",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 120/120 | SP +30 | Posture 60/60",
        "- Ayshuk      : Spd 6 -> 3 AP | HP 165/165 | SP +40 | Posture 85/85",
        "- Void Monolith: Spd 4 -> 2 AP | HP 260/380 | Posture 78/170 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MONOLITH]      [KANG]  [HWANG]         [AYSHUK]                [MAJIN]",
        "---",
        "- Node 01: Void Monolith (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 03: Agent Kang (Advancing with Momentum Surge / +2 Speed)",
        "- Node 04: Agent Hwang (Driving Scalpel into Focal Core)",
        "- Node 06: Research Lead Ayshuk (Discharging Optical Interference)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP [SURGE] | HP 135/135 | SP +30 | Posture 75/75",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 120/120 | SP +30 | Posture 60/60",
        "- Ayshuk      : Spd 6 -> 3 AP | HP 165/165 | SP +40 | Posture 85/85",
        "- Monolith    : Spd 0 -> 0 AP | HP 130/380 | Posture 32/170 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — GLOBAL VOID DEATH-RAY REACTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MONOLITH][KANG] [HWANG]                 [AYSHUK]                [MAJIN]",
        "---",
        "- Node 01: Void Monolith (Recovered / Charging Global Void Death-Ray)",
        "- Node 02: Agent Kang (Directional Guard Absorption Active)",
        "- Node 03: Agent Hwang (Focusing Scalpel on Central Optic Nerve)",
        "- Node 06: Research Lead Ayshuk (Clarity Field Deflecting Beam)",
        "---",
        "- Agent Kang  : Spd 8 -> 4 AP | HP 126/135 | SP +30 | Posture 65/75",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 120/120 | SP +30 | Posture 60/60",
        "- Ayshuk      : Spd 6 -> 3 AP | HP 165/165 | SP +40 | Posture 85/85",
        "- Monolith    : Spd 4 -> 2 AP | HP 62/380  | Posture 12/170 [FRACTURED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER LEVEL 2 INDUCTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[MONOLITH]                                              [MAJIN]",
        "        [KANG]  [HWANG]                 [AYSHUK]",
        "---",
        "- Node 01: Void Monolith (TERMINAL STAGGER / POSTURE 0/170 / 2.0x DMG)",
        "- Node 02: Agent Kang (Shattering Foundation Support)",
        "- Node 03: Agent Hwang (Severing Central Optic Nerve)",
        "- Node 06: Research Lead Ayshuk (Siphoning Radiance)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 126/135 | SP +30 | Posture 65/75",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 120/120 | SP +30 | Posture 60/60",
        "- Ayshuk      : Spd 6 -> 3 AP | HP 165/165 | SP +40 | Posture 85/85",
        "- Monolith    : Spd 0 -> 0 AP | HP 14/380  | Posture 0/170 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[GLASS] [KANG]  [HWANG]                 [AYSHUK]                [MAJIN]",
        "---",
        "- Node 01: Void Monolith (Shattered into Prismatic Glass & Han Mist)",
        "- Node 02: Agent Kang (Resting Maul / Logging Victory)",
        "- Node 03: Agent Hwang (Sheathing Blessed Scalpel)",
        "- Node 06: Research Lead Ayshuk (Archiving Spectral Wavelengths)",
        "---",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 126/135 | SP +35 | Posture 75/75",
        "- Agent Hwang : Spd 6 -> 3 AP | HP 120/120 | SP +35 | Posture 60/60",
        "- Ayshuk      : Spd 6 -> 3 AP | HP 165/165 | SP +45 | Posture 85/85",
        "- Monolith    : HP 0/380 [PURIFIED] | +0.028 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Pedestal Sunder & Stagger Build)
- **Pedestal Impact & Optic Focus**:
  * **Agent Kang**: Smashes the crystalline pedestal with the heavy maul at Node 02:
    * Deals **44 Grudge Damage**!
    * Inflicts +36 Posture Strain. Monolith Posture drops to **66/170**, breaching the **60% Posture Threshold (102 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The crystalline prism fissures, its charging laser deflecting into the ceiling.
  * **Agent Hwang**: Firing from Node 03 with the Blessed Scalpel, strikes the primary optical nerve for **36 Void damage**.
  * Monolith HP drops to **186/380**!

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Stagger Exploitation & Momentum Surge)
- **Vanguard Overload (1.5x Direct Damage)**:
  * Agent Kang's `Momentum Surge` activates! (+2 Speed next turn). Kang delivers a crushing downward smite: **58 Grudge Damage**!
  * Agent Hwang drives the scalpel into the central prism core: **46 Void Damage**!
  * Monolith HP collapses to **82/380**! Posture drops to **18/170**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Global Void Death-Ray Desperation)
- **Hostile Desperation Counter-Surge**:
  * The Void Monolith recovers, opening its aperture to charge `[Global Void Death-Ray]`.
  * Research Lead Ayshuk activates Floor 4's *Clarity Field*, altering the atmospheric refraction index to scatter the beam!
  * Agent Kang deploys `[Directional Guard Absorption]`, taking 9 chip damage (HP: 126/135) while shielding Hwang.
  * Agent Hwang strikes the exposed optic nerve, canceling the death-ray follow-up!
  * Monolith HP falls to **36/380**! Posture drops to **4/170**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger Level 2 Induction)
- **Optic Severance & Terminal Collapse**:
  * Hwang slices through the central optic nerve, stripping the final 4 Posture points!
  * **TERMINAL STAGGER TRIGGERED!** Posture hits **0/170**. The crystalline monolith shatters along all internal lattice planes.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Climax Obliteration**:
  * Agent Kang executes `[Climax Obliteration]`. The monolith shatters into a glittering blizzard of prismatic glass and pure Han vapor.
  * Floor 4 collection flues harvest **+0.028 tons of refined Han**!
"""

def update_part_5():
    path = "SOMNARAK-WORLD/The_Absolvohan/Part_5_Days_77_to_97.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Day 77 summary
    old_d77 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Yoo hammers ribs; Marjuk eases stasis at N05; Fossil 60% |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; direct Grudge damage deals 2.0x; HP      |
| falls to 130.                                                       |
| - Turn 04: Fossil attempts [Gravitational Singularity]; Yoo blocks  |
| behind maul.                                                        |
| - Turn 05: Marjuk freezes vertebrae with stasis field; forces       |
| Terminal Stagger.                                                   |
| - Turn 06: Yoo executes Climax Pulverize; Fossil disintegrates to   |
| gravel.                                                             |
+=====================================================================+
```"""
    if old_d77 in content:
        content = content.replace(old_d77, get_day_77_combat())
        print("Replaced Day 77 summary successfully!")
    else:
        print("Warning: Day 77 summary not found.")

    # Day 82 summary
    old_d82 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Kang severs Worm-A jaw; Noh targets segment joints; 60%  |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; high-velocity pierce deals 2.0x direct   |
| damage.                                                             |
| - Turn 04: Worm-B charges [Trench Collapser]; Mellda locks drainage |
| sluice.                                                             |
| - Turn 05: Kang & Noh coordinate cross-slash, forcing Terminal      |
| Stagger on both.                                                    |
| - Turn 06: Dual decapitation executed; worms dissolve into amber    |
| sediment.                                                           |
+=====================================================================+
```"""
    if old_d82 in content:
        content = content.replace(old_d82, get_day_82_combat())
        print("Replaced Day 82 summary successfully!")
    else:
        print("Warning: Day 82 summary not found.")

    # Day 87 summary
    old_d87 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Noh pins lead husk; Shin unleashes Lament wave; Husk-1   |
| 60% Stagger 1.                                                      |
| - Turn 03: Kang crushes Husk-1 with 2.0x direct damage; Husk-1      |
| eliminated.                                                         |
| - Turn 04: Husks 2 & 3 attempt pincer charge; Dekan activates Jaw   |
| Clamp.                                                              |
| - Turn 05: Shin's wide-angle pulse shatters psychic cohesion;       |
| Terminal Stagger.                                                   |
| - Turn 06: Kang & Noh execute Climax Sweep; all husks pulverized to |
| sludge.                                                             |
+=====================================================================+
```"""
    if old_d87 in content:
        content = content.replace(old_d87, get_day_87_combat())
        print("Replaced Day 87 summary successfully!")
    else:
        print("Warning: Day 87 summary not found.")

    # Day 92 summary
    old_d92 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Jin jams boiler exhaust; Yoo smashes axle; Titan 60%     |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; direct Grudge strikes deal 2.0x direct   |
| damage.                                                             |
| - Turn 04: Titan initiates [Self-Destruct Sequence]; Marjuk         |
| prepares stasis.                                                    |
| - Turn 05: Yoo lands crushing blow on valve; all agents retreat to  |
| Node 8.                                                             |
| - Turn 06: Titan detonates inside sealed blast doors; 0 damage      |
| taken.                                                              |
+=====================================================================+
```"""
    if old_d92 in content:
        content = content.replace(old_d92, get_day_92_combat())
        print("Replaced Day 92 summary successfully!")
    else:
        print("Warning: Day 92 summary not found.")

    # Day 97 summary
    old_d97 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Kang smashes pedestal; Hwang strikes eye; Monolith 60%   |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; direct Grudge/Void strikes deal 2.0x     |
| direct damage.                                                      |
| - Turn 04: Monolith attempts [Global Void Death-Ray]; Ayshuk        |
| predicts firing.                                                    |
| - Turn 05: Hwang severs central optic nerve; forces Terminal        |
| Stagger.                                                            |
| - Turn 06: Kang executes Climax Obliteration; Monolith shatters to  |
| glass.                                                              |
+=====================================================================+
```"""
    if old_d97 in content:
        content = content.replace(old_d97, get_day_97_combat())
        print("Replaced Day 97 summary successfully!")
    else:
        print("Warning: Day 97 summary not found.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated Part 5 successfully!")

if __name__ == "__main__":
    update_part_5()
