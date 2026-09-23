#!/usr/bin/env python3
"""
tools/expand_absolvohan_battles_part6.py
Expands all 5 tactical Ordeal engagements in SOMNARAK-WORLD/The_Absolvohan/Part_6_Days_101_to_121.md
with full Gameplay Battle System (GBS) Reverie Directorate Style mechanics:
1. The Tired Crowd (Lament Dawn)
2. The Melting Cog (Violet Noon)
3. The Pursuing Fire (Grudge Dawn)
4. The Dawn Spark (Pale Midnight)
5. The Foundation Shard (Violet Midnight)
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

filepath = "SOMNARAK-WORLD/The_Absolvohan/Part_6_Days_101_to_121.md"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# -------------------------------------------------------------
# 1. The Tired Crowd (Lament Dawn)
# -------------------------------------------------------------
box_crowd_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (TIRED CROWD)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [CROWD-A] [CROWD-B][KANG]          [PARK]                 [DEKAN]",
    "DIST    : Kang at N03 (Band 1); Park at N05 (Band 3); Dekan at N10.",
    "---",
    "Agent Kang      : Speed 6 -> 3 AP | HP: 145/145 | SP: +30 | Heavy Maul",
    "Agent Park      : Speed 6 -> 3 AP | HP: 130/130 | SP: +30 | Sonic Bow",
    "Tired Silhouettes: Speed 4 -> 2 AP | HP: 180 each | Sleep Haze"
])

box_crowd_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Kang smashes lead silhouette; Park pierces N01; 60% Stagger 1.",
    "- Turn 03: Posture broken; direct Grudge strikes deal 2.0x direct damage.",
    "- Turn 04: Silhouettes vent heavy sleep mist; Dekan activates Bastion Ward.",
    "- Turn 05: Park executes Flerehan acoustic pulse, clearing mental fog.",
    "- Turn 06: Kang unleashes Climax Maul Cleave; entities dissolve to gray mist."
])

box_crowd_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Floor 2 transitway air circulation purged.",
    "2. Status Equilibrium : Sleep haze cleared; team SP stabilizes at +35.",
    "3. Containment Check   : All three silhouettes completely eradicated.",
    "4. OUTCOME             : ZERO CASUALTIES — +0.040 TONS BONUS HAN HARVESTED."
])

old_crowd = """Tactical Clash Telemetry:
- The three gray silhouettes drift forward, emitting a heavy cognitive mist that induces deep sleep and sluggish motor reflex.
- Range Band 1: Agent Kang lunges forward, swinging his *Heavy Maul* in a sweeping arc. The kinetic shockwave shatters the first silhouette's form (85 Grudge damage).
- Agent Park provides rear fire from Range Band 3 with the *Sonic Bow*, targeting the remaining two entities with piercing harmonic pulses.
- The specters dissolve into harmless gray vapor; zero personnel casualties.
- Elimination verified; +0.040 tons bonus Han harvested.

Shift concludes with cumulative daily harvest of **0.580 tons** (100% quota achieved)."""

new_crowd = f"""Director Majin establishes GBS tactical engagement in Floor 2's transitway:

```text
{box_crowd_hud}
```

###### Turn 01 Action Resolution Log (Floor 2 Central Transitway)
- **Step 1: Floor 2 Echo-Core Resonance (Attendant Dekan)**:
  * Dekan deploys *The Maw's Keep Bastion Ward*, raising kinetic armor across Nodes 1 to 4 and buffering against cognitive sleep effects.
- **Step 2: Movement & Action Point Spending**:
  * Agent Kang (Speed 6 -> 3 AP) spends 1 AP to advance from Node 4 to Node 3 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Heavy Maul Sweeping Cleave]`.
  * Agent Park (Speed 6 -> 3 AP) anchors Node 5 (Range Band 3). Spends 2 AP to charge `[Sonic Bow Piercing Pulse]`. Remaining 1 AP held in Guard.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * Lead Silhouette unleashes `[Cognitive Sleep Haze]` (Base 8 + 2 Coins = 12 Power).
  * Agent Kang's `[Heavy Maul Sweeping Cleave]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Kang WINS THE CLASH (15 vs 12).
    * Kang's warhammer smashes through the sleep mist, exploiting the entity's Grudge vulnerability to deal **52 Grudge damage** and inflicting +28 Stagger!
  * Park's sonic bow drives an acoustic pulse through the remaining specters from Node 5 for 36 Lament damage.

```text
{box_crowd_turns}
```

```text
{box_crowd_phase}
```

Shift concludes with cumulative daily harvest of **0.580 tons** (100% quota achieved)."""

if old_crowd in text:
    text = text.replace(old_crowd, new_crowd)
    print("Replaced Tired Crowd section successfully!")
else:
    print("Could not find Tired Crowd section!")

# -------------------------------------------------------------
# 2. The Melting Cog (Violet Noon)
# -------------------------------------------------------------
box_cog_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (MELTING COG)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [MOLTEN-COG]  [ZYRAK] [YOO]                                   [MARJUK]",
    "DIST    : Zyrak at N02 (Band 1); Yoo at N03 (Band 2); Marjuk at N10.",
    "---",
    "Extraction Lead Zyrak: Speed 6 -> 3 AP | HP: 170/170 | SP: +35 | Furnace Lance",
    "Agent Yoo            : Speed 6 -> 3 AP | HP: 145/145 | SP: +30 | Lock Maul",
    "Molten Gearwheel     : Speed 5 -> 3 AP | HP: 420/420 | Torque: High | Grav Shear"
])

box_cog_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Zyrak pierces axle; Yoo hammers teeth; Cog 60% Stagger 1.",
    "- Turn 03: Posture broken; direct Grudge blunt strikes deal 2.0x direct damage.",
    "- Turn 04: Cog charges [Thermal Super-Torque]; Marjuk deploys stasis clamp.",
    "- Turn 05: Yoo executes kinetic counter-smash, cracking central axle in half.",
    "- Turn 06: Zyrak unleashes Climax Thermal Pierce; core detonates safely."
])

box_cog_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Hydraulic transit hall thermal exhaust cleared.",
    "2. Status Equilibrium : Gravitational shear dissipates; team SP at +35.",
    "3. Containment Check   : Gear teeth and axle pulverized into inert rubble.",
    "4. OUTCOME             : ZERO CASUALTIES — +0.050 TONS BONUS EXTRACTED."
])

old_cog = """Tactical Clash Telemetry:
- The colossal gearwheel rolls down the hallway at Range Band 2, radiating white-hot heat and 2.5G gravitational shear.
- Zyrak steps into the center of the corridor, his synthetic arm locking his *Furnace Lance* forward. The thermal thrust pierces the wheel's axle!
- Agent Yoo follows up at Range Band 1, landing a devastating 150-damage kinetic strike with the *Lock Maul* that shatters the gear teeth into inert rubble.
- Elimination verified; +0.050 tons bonus Han harvested from debris.

Shift concludes with cumulative daily harvest of **0.640 tons** (100% quota achieved)."""

new_cog = f"""Director Majin establishes GBS tactical parameters in the hydraulic transit hall:

```text
{box_cog_hud}
```

###### Turn 01 Action Resolution Log (Floor 6 Hydraulic Foundry)
- **Step 1: Floor 3 & 6 Echo-Core Resonances (Zyrak & Marjuk)**:
  * Zyrak engages *M.A.W. Overcharge*, buffing allied weapon Clash Power by +3.
  * Marjuk readies *The Temporal Stasis Array* to stabilize the axle.
- **Step 2: Movement & Action Point Spending**:
  * Extraction Lead Zyrak (Speed 6 -> 3 AP) plants his boots at Node 2 (Point-Blank Range Band 1). Spends 2 AP to declare `[Furnace Lance Thermal Axle Thrust]`. Remaining 1 AP in Guard.
  * Agent Yoo (Speed 6 -> 3 AP) stands at Node 3 (Close Range Band 2). Spends 2 AP to prepare `[Lock Maul Kinetic Overdrive]`.
- **Step 3: Clash Resolution (Node 1 to 2)**:
  * Molten Gearwheel rolls forward with `[Gravitational Rolling Shear]` (Base 10 + 2 Coins = 14 Power).
  * Extraction Lead Zyrak's `[Furnace Lance Thermal Axle Thrust]` (Base 12 + 2 Coins = 16 Power).
  * **Resolution**: Zyrak WINS THE CLASH (16 vs 14).
    * Zyrak's furnace lance pierces the incandescent axle, halting the wheel's rolling momentum and dealing **54 Grudge/Thermal damage** with +28 Stagger!
  * Agent Yoo follows up with `[Lock Maul Kinetic Overdrive]`, smashing the primary gear teeth for 48 blunt damage.

```text
{box_cog_turns}
```

```text
{box_cog_phase}
```

Shift concludes with cumulative daily harvest of **0.640 tons** (100% quota achieved)."""

if old_cog in text:
    text = text.replace(old_cog, new_cog)
    print("Replaced Melting Cog section successfully!")
else:
    print("Could not find Melting Cog section!")

# -------------------------------------------------------------
# 3. The Pursuing Fire (Grudge Dawn)
# -------------------------------------------------------------
box_fire_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (PURSUING FIRE)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [STALKER-A][STALKER-B][MELLDA][CHA]           [REFUGEES]     [MAJIN]",
    "DIST    : Mellda at N03 (Band 1); Cha at N04 (Band 2); Refugees at N08.",
    "---",
    "Border Lead Mellda: Speed 6 -> 3 AP | HP: 200/200 | SP: +40 | Threshold Vow",
    "Agent Cha         : Speed 5 -> 3 AP | HP: 125/125 | SP: +30 | Forge Bracer",
    "Ash Stalkers (x4) : Speed 6 -> 3 AP | HP: 190 each | Incandescent Flame"
])

box_fire_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Mellda pins lead stalker; Cha unleashes cryo spray; 60% Stagger 1.",
    "- Turn 03: Posture broken; cryo-quench strikes deal 2.0x direct damage.",
    "- Turn 04: Stalkers attempt flank toward refugees; Mellda locks Gate 05.",
    "- Turn 05: Cha freezes remaining stalkers into brittle charcoal at Node 2.",
    "- Turn 06: Mellda executes Climax Spear Sweep; all entities shatter to ash."
])

box_fire_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Perimeter airlock thermal ventilation normalized.",
    "2. Status Equilibrium : Refugee convoy safe; team SP stabilizes at +40.",
    "3. Containment Check   : All four incandescent stalkers annihilated.",
    "4. OUTCOME             : ZERO REFUGEE LOSSES — +0.045 TONS BONUS EXTRACTED."
])

old_fire = """Tactical Clash Telemetry:
- The four glowing ash stalkers lunge toward the rear tread of the medical crawler at Range Band 1.
- Mellda manifests *Threshold Vow*, driving her golden energy spear through the lead beast's skull, pinning it to the airlock bulkhead!
- Agent Cha unleashes a high-pressure cryo-quench spray from his *Forge Bracer*, instantly solidifying the remaining three stalkers into brittle charcoal.
- Mellda sweeps her spear, shattering the frozen husks into dust. Zero refugee or personnel casualties sustained.
- Elimination verified; +0.045 tons bonus Han harvested.

Daily shift concludes with cumulative total of **0.710 tons** (100% quota achieved)."""

new_fire = f"""Director Majin establishes GBS tactical engagement at the Perimeter Airlock:

```text
{box_fire_hud}
```

###### Turn 01 Action Resolution Log (Perimeter Bulwark Airlock)
- **Step 1: Floor 5 Echo-Core Resonance (Border Lead Mellda)**:
  * Mellda activates *Blast Gate Lockdown*, sealing Node 5 to ensure zero hostile ingress toward the refugee crawler at Node 8.
- **Step 2: Movement & Action Point Spending**:
  * Border Lead Mellda (Speed 6 -> 3 AP) holds Node 3 (Point-Blank Range Band 1). Spends 2 AP to declare `[Threshold Vow Skull-Pinning Thrust]`. Remaining 1 AP in Guard.
  * Agent Cha (Speed 5 -> 3 AP) positions at Node 4 (Range Band 2). Spends 2 AP to ready `[Forge Bracer High-Pressure Cryo-Spray]`.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * Lead Ash Stalker lunges with `[Incandescent Flame Jaw]` (Base 9 + 2 Coins = 13 Power).
  * Border Lead Mellda's `[Threshold Vow Skull-Pinning Thrust]` (Base 12 + 2 Coins = 16 Power).
  * **Resolution**: Mellda WINS THE CLASH (16 vs 13).
    * Mellda drives the golden spearhead straight through the stalker's incandescent skull, pinning it to the bulkhead for **52 Grudge/Weight damage** with +26 Stagger!
  * Agent Cha unleashes the cryo spray from Node 4, chilling the remaining stalkers with 38 Lament damage.

```text
{box_fire_turns}
```

```text
{box_fire_phase}
```

Daily shift concludes with cumulative total of **0.710 tons** (100% quota achieved)."""

if old_fire in text:
    text = text.replace(old_fire, new_fire)
    print("Replaced Pursuing Fire section successfully!")
else:
    print("Could not find Pursuing Fire section!")

# -------------------------------------------------------------
# 4. The Dawn Spark (Pale Midnight)
# -------------------------------------------------------------
box_spark_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (DAWN SPARK)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [SOLAR-CORE]  [KANG]          [YOON]  [HONG]                 [AYSHUK]",
    "DIST    : Kang at N02 (Band 1); Yoon at N05 (Band 3); Hong at N06 (Band 3).",
    "---",
    "Agent Kang      : Speed 6 -> 3 AP | HP: 150/150 | SP: +35 | Heavy Maul",
    "Agent Yoon      : Speed 6 -> 3 AP | HP: 125/125 | SP: +35 | Tear Veil",
    "Agent Hong      : Speed 5 -> 3 AP | HP: 120/120 | SP: +30 | Choral Staff",
    "Dawn Solar Core : Speed 5 -> 3 AP | HP: 500/500 | Sorrow: 75% | Pale Pulse"
])

box_spark_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Yoon & Hong channel dual weeping; cool solar core; 60% Stagger 1.",
    "- Turn 03: Posture broken; all 4 damage types deal 2.0x direct damage.",
    "- Turn 04: Core charges [20% Max HP Pale Pulse]; Kang braces behind shield.",
    "- Turn 05: Ayshuk identifies thermal-psychic node; Yoon dampens vibration.",
    "- Turn 06: Kang strikes baseplate with Climax Maul; core dissolves to starlight."
])

box_spark_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Sub-Central Hall thermal radiation fully dissipated.",
    "2. Status Equilibrium : Pale sunder halted; team HP and SP restored.",
    "3. Containment Check   : Solar Core collapsed into shimmering starlight.",
    "4. OUTCOME             : HISTORIC MIDNIGHT CLEAR — +0.075 TONS BONUS EXTRACTED."
])

old_spark = """Tactical Clash Telemetry:
- The miniature cyan sun radiates omnidirectional Pale pulses, threatening to strip 20% of maximum HP per pulse.
- Range Band 4: Agent Yoon and Agent Hong coordinate from the hall's perimeter, unleashing continuous sonic lament waves with *Tear Veil* and *Choral Staff*.
- The pure sorrow harmonic lowers the core's thermal-psychic vibration.
- Range Band 1: Agent Kang rushes in with his heavy maul, striking the stabilizing baseplate and collapsing the core into shimmering starlight.
- Elimination verified; +0.075 tons bonus Han harvested.

Shift concludes with cumulative daily harvest of **0.780 tons** (100% quota achieved)."""

new_spark = f"""Director Majin establishes GBS tactical engagement in the Sub-Central Hall:

```text
{box_spark_hud}
```

###### Turn 01 Action Resolution Log (Floor 4 Sub-Central Hall)
- **Step 1: Floor 4 Echo-Core Resonance (Research Lead Ayshuk)**:
  * Ayshuk deploys *The Predictive HUD*, analyzing the miniature cyan sun's radiation harmonics and granting +3 Clash Power against its Pale pulses.
- **Step 2: Movement & Action Point Spending**:
  * Agent Yoon (Speed 6 -> 3 AP) anchors Node 5 (Range Band 3). Spends 2 AP to channel `[Tear Veil Harmonic Lament Wave]`.
  * Agent Hong (Speed 5 -> 3 AP) deploys at Node 6 (Range Band 3). Spends 2 AP to activate `[Choral Staff Sorrow Pulse]`. Remaining 1 AP held in Guard.
  * Agent Kang (Speed 6 -> 3 AP) spends 1 AP to sprint to Node 2 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Heavy Maul Kinetic Sunder]`.
- **Step 3: Clash Resolution (Node 1 to 5)**:
  * Dawn Solar Core releases `[Omnidirectional Pale Sunder]` (Base 10 + 2 Coins = 14 Power).
  * Agent Yoon & Agent Hong's `[Dual Harmonic Weeping]` (Base 12 + 2 Coins = 16 Power).
  * **Resolution**: The Agents WIN THE CLASH (16 vs 14).
    * The pure sorrow wave encapsulates the solar flare, suppressing its heat and dealing **48 Lament/Void damage** with +26 Stagger!
  * Kang strikes the stabilizing baseplate from Node 2, dealing 54 Grudge damage.

```text
{box_spark_turns}
```

```text
{box_spark_phase}
```

Shift concludes with cumulative daily harvest of **0.780 tons** (100% quota achieved)."""

if old_spark in text:
    text = text.replace(old_spark, new_spark)
    print("Replaced Dawn Spark section successfully!")
else:
    print("Could not find Dawn Spark section!")

# -------------------------------------------------------------
# 5. The Foundation Shard (Violet Midnight)
# -------------------------------------------------------------
box_shard_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (FOUNDATION SHARD)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [SHARD]       [KANG]          [COMMAND-STAFF]        [MAJIN]",
    "DIST    : Kang at N02 (Band 1); Staff at N06 (Pinned 3.5G); Majin at N09.",
    "---",
    "Agent Kang      : Speed 6 -> 3 AP | HP: 155/155 | SP: +35 | Threshold Maul",
    "Director Majin  : Speed 5 -> 3 AP | HP: 200/200 | SP: +45 | Command Eye",
    "Foundation Shard: Speed 5 -> 3 AP | HP: 520/520 | 3.5G Grav | Pre-Time Shard"
])

box_shard_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Kang smashes apex; Majin rerolls speed; Shard hits 60% Stagger 1.",
    "- Turn 03: Posture broken; direct Grudge blunt strikes deal 2.0x direct damage.",
    "- Turn 04: Shard attempts [Tectonic Reality Shear]; Majin deploys Veil Mist.",
    "- Turn 05: Kang executes kinetic surge, shattering outer crystalline lattice.",
    "- Turn 06: Kang unleashes Climax Maul Shatter; Shard crumbles to purple sand."
])

box_shard_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Command Atrium 3.5G grav field collapses to 1.0G.",
    "2. Status Equilibrium : Staff rescued from consoles; team SP at full capacity.",
    "3. Containment Check   : Pre-Time Monolith reduced to pulverized purple sand.",
    "4. OUTCOME             : HISTORIC ATRIUM DEFENSE — +0.085 TONS BONUS SECURED."
])

old_shard = """Tactical Clash Telemetry:
- The colossal violet monolith hovers above the central tactical table, radiating 3.5G of localized gravitational shear that pins command personnel to their consoles.
- Range Band 1: Agent Kang activates *Threshold Suit* grav-locks, charging directly beneath the obelisk's apex.
- Kang channels full pneumatic pressure into his *Heavy Maul*, executing a titanic upward-to-downward kinetic smash (Critical strike: 210 Grudge damage).
- The monolith's core shatters; gravitational shear dissipates instantly. The stone crumbles into inert purple sand.
- Elimination verified; +0.085 tons bonus Han secured.

Daily shift concludes with cumulative total of **0.850 tons** (100% quota achieved)."""

new_shard = f"""Director Majin establishes GBS tactical engagement in the Command Atrium:

```text
{box_shard_hud}
```

###### Turn 01 Action Resolution Log (Floor 1 Command Atrium)
- **Step 1: Floor 1 Echo-Core Resonance (Director Majin & Secretary Seiyon)**:
  * Majin deploys *The Command Eye*, rerolling Agent Kang's Speed Die to maximum, unlocking 3 Action Points under heavy gravity.
  * Seiyon engages emergency ballast compensators around the central consoles.
- **Step 2: Movement & Action Point Spending**:
  * Agent Kang (Speed 6 -> 3 AP) activates *Threshold Suit* grav-locks, spending 1 AP to sprint directly to Node 2 (Point-Blank Range Band 1) beneath the apex.
  * Kang spends 2 AP to prepare `[Threshold Maul Titanic Downward Cleave]`.
  * Director Majin (Speed 5 -> 3 AP) operates from Node 9, spending 2 AP to maintain *Administrative Clarity* team-wide. Remaining 1 AP held in Guard.
- **Step 3: Clash Resolution (Node 1 to 2)**:
  * Foundation Shard charges `[3.5G Gravitational Reality Shear]` (Base 11 + 2 Coins = 15 Power).
  * Agent Kang's `[Threshold Maul Titanic Cleave]` (Base 13 + 2 Coins = 17 Power).
  * **Resolution**: Kang WINS THE CLASH (17 vs 15).
    * Kang's warhammer crashes into the obelisk's grav-core, arresting the gravitational pulse and dealing **62 Grudge damage** with +32 Stagger!
  * The shockwave frees the pinned command staff, allowing immediate evacuation toward Node 10.

```text
{box_shard_turns}
```

```text
{box_shard_phase}
```

Daily shift concludes with cumulative total of **0.850 tons** (100% quota achieved)."""

if old_shard in text:
    text = text.replace(old_shard, new_shard)
    print("Replaced Foundation Shard section successfully!")
else:
    print("Could not find Foundation Shard section!")

check_banned(text, filepath)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
print(f"Updated {filepath} with all expanded GBS battles!")
