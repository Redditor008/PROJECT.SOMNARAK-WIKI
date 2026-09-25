#!/usr/bin/env python3
"""
tools/expand_absolvohan_battles_part5.py
Expands all 5 tactical Ordeal engagements in SOMNARAK-WORLD/The_Absolvohan/Part_5_Days_77_to_97.md
with full Gameplay Battle System (GBS) Reverie Directorate Style mechanics:
1. The Fossil of Memory (Violet Noon)
2. The Trench Worm (Amber Dusk)
3. The Carmine Claw (Crimson Noon)
4. The Clockwork Titan (Green Dusk)
5. The Monolith of the Void (Violet Dusk)
"""

import sys
import re

banned_patterns = [
    r"\bego\b", r"\be\.g\.o\b", r"\babnormality\b", r"\babnormalities\b",
    r"\bdistortion\b", r"\bdistortions\b", r"\bpeccatula\b", r"\bfixer\b",
    r"\bfixers\b", r"\bassociation\b", r"\bassociations\b", r"\bthe fingers\b",
    r"\blobotomy\b", r"\blimbus\b", r"\blibrary\b", r"\byoung-ji\b",
    r"\bcarmen\b", r"\bayin\b", r"\bsinner\b", r"\bsinners\b",
    r"\bmephistopheles\b", r"\bgolden bough\b", r"\bmirror dungeon\b",
    r"\brefraction railway\b", r"\bharin\b", r"\bminjae\b"
]

def check_banned(text, filename):
    for b in banned_patterns:
        matches = re.findall(b, text, re.IGNORECASE)
        if matches:
            raise ValueError(f"Banned word {b} found in {filename}: {matches[:3]}")

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

filepath = "SOMNARAK-WORLD/The_Absolvohan/Part_5_Days_77_to_97.md"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# -------------------------------------------------------------
# 1. The Fossil of Memory (Violet Noon)
# -------------------------------------------------------------
box_fossil_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (VIOLET FOSSIL)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [FOSSIL]      [YOO]           [ARCHIVISTS]           [MARJUK]",
    "DIST    : Yoo at N03 (Band 1); Archivists at N05 (Pinned); Marjuk at N10.",
    "---",
    "Agent Yoo       : Speed 6 -> 3 AP | HP: 140/140 | SP: +30 | Lock Maul",
    "Archive Marjuk  : Speed 5 -> 3 AP | HP: 200/200 | SP: +40 | Chrono Stasis",
    "Memory Fossil   : Speed 4 -> 2 AP | HP: 380/380 | Sorrow: 60% | Gravitic Stasis"
])

box_fossil_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Yoo hammers ribs; Marjuk eases stasis at N05; Fossil 60% Stagger 1.",
    "- Turn 03: Posture broken; direct Grudge damage deals 2.0x; HP falls to 130.",
    "- Turn 04: Fossil attempts [Gravitational Singularity]; Yoo blocks behind maul.",
    "- Turn 05: Marjuk freezes vertebrae with stasis field; forces Terminal Stagger.",
    "- Turn 06: Yoo executes Climax Pulverize; Fossil disintegrates to gravel."
])

box_fossil_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : 2.5G gravitational compression field normalizes.",
    "2. Status Equilibrium : Archivists rescued; team SP restored to +35.",
    "3. Containment Check   : Gravitic Skeleton shattered into inert dust.",
    "4. OUTCOME             : ZERO CASUALTIES — +0.045 TONS BONUS EXTRACTED."
])

old_fossil = """Tactical Clash Telemetry:
- Range Band 1: Agent Yoo closes distance with heavy *Lock Maul*, tanking two gravitational stasis pulses (Weight damage: 18 -> mitigated to 9 by *Lock Armor* 0.5 resistance).
- Yoo triggers kinetic override: massive downward smash hits for 145 Grudge damage!
- The Violet Fossil's calcified vertebrae crumble into gravel; stasis field collapses.
- Elimination verified; +0.045 tons bonus Han extracted from pulverized remnants.

Shift concludes with cumulative daily harvest of **0.295 tons** (100% quota achieved)."""

new_fossil = f"""Director Majin establishes GBS tactical engagement in the Archive Rotunda:

```text
{box_fossil_hud}
```

###### Turn 01 Action Resolution Log (Floor 6 Archive Rotunda)
- **Step 1: Floor 6 Echo-Core Resonance (Archive Lead Marjuk)**:
  * Marjuk deploys *The Temporal Stasis Array*, reducing the Fossil's 2.5G gravitational compression over Nodes 3 to 6 by 50%.
- **Step 2: Movement & Action Point Spending**:
  * Agent Yoo (Speed 6 -> 3 AP) spends 1 AP to advance from Node 4 to Node 2 (Point-Blank Range Band 1). Spends 2 AP to declare `[Lock Maul Tectonic Downswing]`.
  * Archive Lead Marjuk (Speed 5 -> 3 AP) operates from Node 10, spending 2 AP to maintain the stasis dampeners on pinned archivists at Node 5.
- **Step 3: Clash Resolution (Node 1 to 2)**:
  * Memory Fossil attempts `[2.5G Gravitational Stasis Pulse]` (Base 9 + 2 Coins = 13 Power).
  * Agent Yoo's `[Lock Maul Tectonic Downswing]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Yoo WINS THE CLASH (15 vs 13).
    * Yoo's massive warhammer smashes through the fossilized ribs, exploiting its Grudge vulnerability to deal **52 Grudge damage** and inflicting +26 Stagger!
  * Marjuk's stasis wave frees the pinned archivists, who safely withdraw toward Node 9.

```text
{box_fossil_turns}
```

```text
{box_fossil_phase}
```

Shift concludes with cumulative daily harvest of **0.295 tons** (100% quota achieved)."""

if old_fossil in text:
    text = text.replace(old_fossil, new_fossil)
    print("Replaced Fossil section successfully!")
else:
    print("Could not find Fossil section!")

# -------------------------------------------------------------
# 2. The Trench Worm (Amber Dusk)
# -------------------------------------------------------------
box_worm_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (AMBER WORM)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [WORM-A]  [WORM-B][KANG]          [NOH]                  [MELLDA]",
    "DIST    : Kang at N03 (Band 1); Noh at N05 (Band 3); Mellda at N10.",
    "---",
    "Agent Kang      : Speed 6 -> 3 AP | HP: 135/135 | SP: +30 | Threshold Greatsword",
    "Agent Noh       : Speed 5 -> 3 AP | HP: 120/120 | SP: +25 | Sonic Rifle",
    "Trench Worm(x2) : Speed 4 -> 2 AP | HP: 360 each | Burrowing Mandibles"
])

box_worm_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Kang severs Worm-A jaw; Noh targets segment joints; 60% Stagger 1.",
    "- Turn 03: Posture broken; high-velocity pierce deals 2.0x direct damage.",
    "- Turn 04: Worm-B charges [Trench Collapser]; Mellda locks drainage sluice.",
    "- Turn 05: Kang & Noh coordinate cross-slash, forcing Terminal Stagger on both.",
    "- Turn 06: Dual decapitation executed; worms dissolve into amber sediment."
])

box_worm_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Subterranean drainage sub-level plating reinforced.",
    "2. Status Equilibrium : Shuddering bedrock calms; team SP rises to +35.",
    "3. Containment Check   : Both Trench Worms completely eliminated.",
    "4. OUTCOME             : ZERO CASUALTIES — +0.060 TONS BONUS HAN EXTRACTED."
])

old_worm = """Tactical Clash Telemetry:
- Range Band 1: Agent Kang plants *Threshold Greatsword* into the beast's chitinous jaw, absorbing 22 Weight damage (mitigated to 11 by armor).
- Range Band 3: Agent Noh fires continuous sonic bursts, shredding the second worm's segment joints.
- Kang executes cross-slash, bisecting the primary worm; Noh's sonic beam detonates the secondary burrower.
- Both entities eliminated; +0.060 tons bonus Han secured.

Daily shift concludes with cumulative total of **0.340 tons** (100% quota achieved)."""

new_worm = f"""Director Majin establishes GBS tactical parameters in the drainage sub-level:

```text
{box_worm_hud}
```

###### Turn 01 Action Resolution Log (Floor 5 Drainage Sub-Level)
- **Step 1: Floor 5 Echo-Core Resonance (Border Lead Mellda)**:
  * Mellda drops *The Bulwark Perimeter* across Node 4, preventing the burrowers from tunneling beneath the team.
- **Step 2: Movement & Action Point Spending**:
  * Agent Kang (Speed 6 -> 3 AP) spends 1 AP to advance from Node 4 to Node 3 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Threshold Greatsword Sunder]`.
  * Agent Noh (Speed 5 -> 3 AP) positions at Node 5 (Range Band 3). Spends 2 AP to charge `[Sonic Rifle Resonant Burst]`. Remaining 1 AP held in Guard.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * Trench Worm A launches `[Crushing Mandible Thrust]` (Base 9 + 2 Coins = 13 Power).
  * Agent Kang's `[Threshold Greatsword Sunder]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Kang WINS THE CLASH (15 vs 13).
    * Kang drives the heavy greatsword directly into the beast's armored gullet, absorbing the kinetic shock and dealing **48 Pierce/Grudge damage** with +24 Stagger!
  * Noh's sonic rifle tears through Worm B's segment joints from Node 5, dealing 36 acoustic damage.

```text
{box_worm_turns}
```

```text
{box_worm_phase}
```

Daily shift concludes with cumulative total of **0.340 tons** (100% quota achieved)."""

if old_worm in text:
    text = text.replace(old_worm, new_worm)
    print("Replaced Trench Worm section successfully!")
else:
    print("Could not find Trench Worm section!")

# -------------------------------------------------------------
# 3. The Carmine Claw (Crimson Noon)
# -------------------------------------------------------------
box_claw_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (CARMINE CLAW)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [HUSK-1]  [HUSK-2] [KANG]          [NOH]   [SHIN]         [DEKAN]",
    "DIST    : Kang at N03 (Band 1); Noh at N05 (Band 2); Shin at N06 (Band 3).",
    "---",
    "Agent Kang      : Speed 6 -> 3 AP | HP: 140/140 | SP: +30 | Heavy Maul",
    "Agent Noh       : Speed 6 -> 3 AP | HP: 125/125 | SP: +25 | Clockwork Bayonet",
    "Agent Shin      : Speed 5 -> 3 AP | HP: 120/120 | SP: +30 | Choral Staff",
    "Carmine Husks(x3): Speed 6 -> 3 AP | HP: 200 each | Bleed Laceration"
])

box_claw_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Noh pins lead husk; Shin unleashes Lament wave; Husk-1 60% Stagger 1.",
    "- Turn 03: Kang crushes Husk-1 with 2.0x direct damage; Husk-1 eliminated.",
    "- Turn 04: Husks 2 & 3 attempt pincer charge; Dekan activates Jaw Clamp.",
    "- Turn 05: Shin's wide-angle pulse shatters psychic cohesion; Terminal Stagger.",
    "- Turn 06: Kang & Noh execute Climax Sweep; all husks pulverized to sludge."
])

box_claw_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Ventilation junction sanitized and sealed.",
    "2. Status Equilibrium : Bleed hemorrhage cleared; team SP at +35.",
    "3. Containment Check   : Triple termination confirmed; zero breaches.",
    "4. OUTCOME             : ZERO CASUALTIES — +0.052 TONS BONUS HARVESTED."
])

old_claw = """Tactical Clash Telemetry:
- Range Band 2: Agent Noh opens fire with *Clockwork Bayonet*, pinning the lead husk's legs with piercing Grudge spikes.
- Agent Shin channels the *Choral Staff*, unleashing a wide-angle Lament wave that shatters the husks' psychic cohesion.
- Agent Kang closes in at Range Band 1, executing downward maul smashes that crush the remaining husks into crimson sludge.
- Complete suppression achieved; +0.052 tons bonus Han harvested.

Shift concludes with cumulative total of **0.395 tons** (100% quota achieved)."""

new_claw = f"""Director Majin establishes GBS tactical deployment at Floor 2's central junction:

```text
{box_claw_hud}
```

###### Turn 01 Action Resolution Log (Floor 2 Central Junction)
- **Step 1: Floor 2 Echo-Core Resonance (Attendant Dekan)**:
  * Dekan activates *The Maw's Keep Bastion Ward*, raising kinetic hardness across Nodes 1 to 4 and granting +40% resistance to bleed lacerations.
- **Step 2: Movement & Action Point Spending**:
  * Agent Kang (Speed 6 -> 3 AP) spends 1 AP to advance from Node 4 to Node 3 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Heavy Maul Downward Cleave]`.
  * Agent Noh (Speed 6 -> 3 AP) positions at Node 5 (Range Band 2). Spends 2 AP to ready `[Clockwork Bayonet Piercing Pin]`. Remaining 1 AP held in Guard.
  * Agent Shin (Speed 5 -> 3 AP) stands at Node 6 (Range Band 3). Spends 2 AP to channel `[Choral Staff Wide-Angle Lament Wave]`.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * Lead Carmine Husk declares `[Sanguinary Razor Sprint]` (Base 8 + 2 Coins = 12 Power).
  * Agent Noh's `[Clockwork Bayonet Piercing Pin]` (Base 10 + 2 Coins = 14 Power).
  * **Resolution**: Noh WINS THE CLASH (14 vs 12).
    * Noh's bayonet pins the rushing husk's hind limbs to the floor, canceling the charge and inflicting 38 Grudge damage with +20 Stagger!
  * Shin channels the *Choral Staff*, bathing Nodes 1 through 3 in acoustic frequencies that shatter the husks' mental coordination.

```text
{box_claw_turns}
```

```text
{box_claw_phase}
```

Shift concludes with cumulative total of **0.395 tons** (100% quota achieved)."""

if old_claw in text:
    text = text.replace(old_claw, new_claw)
    print("Replaced Carmine Claw section successfully!")
else:
    print("Could not find Carmine Claw section!")

# -------------------------------------------------------------
# 4. The Clockwork Titan (Green Dusk)
# -------------------------------------------------------------
box_titan_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (CLOCKWORK TITAN)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [TITAN]       [YOO]           [JIN]                  [MARJUK]",
    "DIST    : Yoo at N03 (Band 1); Jin at N06 (Band 3); Marjuk at N10.",
    "---",
    "Agent Yoo       : Speed 6 -> 3 AP | HP: 145/145 | SP: +30 | Lock Maul",
    "Agent Jin       : Speed 6 -> 3 AP | HP: 125/125 | SP: +30 | Sonic Bow",
    "Clockwork Titan : Speed 4 -> 2 AP | HP: 480/480 | Steam: High | Boiler Artillery"
])

box_titan_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Jin jams boiler exhaust; Yoo smashes axle; Titan 60% Stagger 1.",
    "- Turn 03: Posture broken; direct Grudge strikes deal 2.0x direct damage.",
    "- Turn 04: Titan initiates [Self-Destruct Sequence]; Marjuk prepares stasis.",
    "- Turn 05: Yoo lands crushing blow on valve; all agents retreat to Node 8.",
    "- Turn 06: Titan detonates inside sealed blast doors; 0 damage taken."
])

box_titan_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Floor 6 blast bulkheads withstand boiler shrapnel.",
    "2. Status Equilibrium : Green steam vented through exhaust scrubbers.",
    "3. Containment Check   : Automaton completely annihilated in detonation.",
    "4. OUTCOME             : FLAWLESS RETREAT & KILL — +0.075 TONS BONUS HAN."
])

old_titan = """Tactical Clash Telemetry:
- Range Band 4: Agent Jin lands pinpoint sonic arrows into the Titan's boiler exhaust, jamming its primary artillery cannon.
- Range Band 1: Agent Yoo charges under the steam vents, landing a 180-damage crushing strike with the *Lock Maul* that fractures the central gear train.
- The Titan's boiler red-lines: automated retreat order issued! All agents sprint back through the blast gates.
- Titan explodes in a spectacular burst of shrapnel and green steam; zero personnel damage sustained.
- Elimination verified; +0.075 tons bonus Han harvested from wreckage.

Daily shift concludes with cumulative total of **0.450 tons** (100% quota achieved)."""

new_titan = f"""Director Majin establishes GBS tactical coordination on the Floor 6 Catwalk:

```text
{box_titan_hud}
```

###### Turn 01 Action Resolution Log (Floor 6 Main Catwalk)
- **Step 1: Floor 6 Echo-Core Resonance (Archive Lead Marjuk)**:
  * Marjuk readies *The Temporal Stasis Array* to delay the Titan's boiler meltdown timer by +15 seconds, creating a safe extraction window.
- **Step 2: Movement & Action Point Spending**:
  * Agent Jin (Speed 6 -> 3 AP) deploys at Node 6 (Range Band 3). Spends 2 AP to ready `[Sonic Bow Pinpoint Shot]`. Remaining 1 AP held in Guard.
  * Agent Yoo (Speed 6 -> 3 AP) spends 1 AP to sprint to Node 3 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Lock Maul Axle Shatter]`.
- **Step 3: Clash Resolution (Node 1 to 6)**:
  * Clockwork Titan prepares `[Long-Range Boiler Artillery Volley]` (Base 9 + 2 Coins = 13 Power).
  * Agent Jin's `[Sonic Bow Pinpoint Shot]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Jin WINS THE CLASH (15 vs 13).
    * Jin's sonic arrow drives directly into the boiler exhaust flap, jamming the firing mechanism and dealing 42 acoustic damage with +26 Stagger!
  * Yoo charges under the venting steam, driving the *Lock Maul* into the central differential gear for **56 Grudge crushing damage**!

```text
{box_titan_turns}
```

```text
{box_titan_phase}
```

Daily shift concludes with cumulative total of **0.450 tons** (100% quota achieved)."""

if old_titan in text:
    text = text.replace(old_titan, new_titan)
    print("Replaced Clockwork Titan section successfully!")
else:
    print("Could not find Clockwork Titan section!")

# -------------------------------------------------------------
# 5. The Monolith of the Void (Violet Dusk)
# -------------------------------------------------------------
box_monolith_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (VOID MONOLITH)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [MONOLITH]    [KANG]  [HWANG]                                 [AYSHUK]",
    "DIST    : Kang at N02 (Band 1); Hwang at N03 (Band 2); Ayshuk at N10.",
    "---",
    "Agent Kang      : Speed 6 -> 3 AP | HP: 145/145 | SP: +35 | Lock Maul",
    "Agent Hwang     : Speed 6 -> 3 AP | HP: 130/130 | SP: +30 | Apostle Scalpel",
    "Void Monolith   : Speed 4 -> 2 AP | HP: 450/450 | Charging: 360 Beam | Void Core"
])

box_monolith_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Kang smashes pedestal; Hwang strikes eye; Monolith 60% Stagger 1.",
    "- Turn 03: Posture broken; direct Grudge/Void strikes deal 2.0x direct damage.",
    "- Turn 04: Monolith attempts [Global Void Death-Ray]; Ayshuk predicts firing.",
    "- Turn 05: Hwang severs central optic nerve; forces Terminal Stagger.",
    "- Turn 06: Kang executes Climax Obliteration; Monolith shatters to glass."
])

box_monolith_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : 360-degree Void charging aura dissipates.",
    "2. Status Equilibrium : Plaza atmospheric pressure stabilizes; team SP at +40.",
    "3. Containment Check   : Monolith pulverized into harmless purple glass.",
    "4. OUTCOME             : HISTORIC CLEAR — ZERO CASUALTIES, +0.080 TONS BONUS."
])

old_monolith = """Tactical Clash Telemetry:
- The Monolith begins charging its global corridor Void beam (5-second countdown).
- Range Band 1: Agent Kang sprints through the spatial distortion, slamming his heavy maul into the obelisk's foundation, interrupting the charge cycle!
- Agent Hwang lunges from the flank with the *Apostle Scalpel*, driving the consecrated blade directly into the floating central eye (Critical strike: 165 Grudge/Void damage).
- The Monolith fractures into thousands of purple glass fragments; zero casualties.
- Elimination verified; +0.080 tons bonus Han secured.

Daily shift concludes with cumulative total of **0.520 tons** (100% quota achieved)."""

new_monolith = f"""Director Majin establishes GBS tactical engagement in the Training Plaza:

```text
{box_monolith_hud}
```

###### Turn 01 Action Resolution Log (Floor 4 Main Training Plaza)
- **Step 1: Floor 4 Echo-Core Resonance (Research Lead Ayshuk)**:
  * Ayshuk engages *The Predictive HUD*, revealing the Monolith's 360-degree Void death-ray countdown vector and buffing allied clash rolls by +3 Power.
- **Step 2: Movement & Action Point Spending**:
  * Agent Kang (Speed 6 -> 3 AP) spends 1 AP to sprint across the spatial ripple from Node 4 to Node 2 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Lock Maul Foundation Shatter]`.
  * Agent Hwang (Speed 6 -> 3 AP) advances to Node 3 (Close Range Band 2). Spends 2 AP to ready `[Apostle Scalpel Consecrated Thrust]`. Remaining 1 AP held in Guard.
- **Step 3: Clash Resolution (Node 1 to 2)**:
  * Void Monolith charges `[360-Degree Global Corridor Annihilation]` (Base 10 + 2 Coins = 14 Power).
  * Agent Kang's `[Lock Maul Foundation Shatter]` (Base 12 + 2 Coins = 16 Power).
  * **Resolution**: Kang WINS THE CLASH (16 vs 14).
    * Kang's massive maul slams into the obelisk's foundation stone, jarring its energy conduits and canceling the countdown! Deals **58 Grudge damage** and inflicts +30 Stagger!
  * Hwang lunges from the flank, driving the *Apostle Scalpel* straight into the central floating eye for 48 Void piercing damage.

```text
{box_monolith_turns}
```

```text
{box_monolith_phase}
```

Daily shift concludes with cumulative total of **0.520 tons** (100% quota achieved)."""

if old_monolith in text:
    text = text.replace(old_monolith, new_monolith)
    print("Replaced Void Monolith section successfully!")
else:
    print("Could not find Void Monolith section!")

check_banned(text, filepath)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
print(f"Updated {filepath} with all expanded GBS battles!")
