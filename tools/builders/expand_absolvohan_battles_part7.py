#!/usr/bin/env python3
"""
tools/expand_absolvohan_battles_part7.py
Expands all 6 tactical Ordeal engagements in SOMNARAK-WORLD/The_Absolvohan/Part_7_Days_125_to_145.md
with full Gameplay Battle System (GBS) Reverie Directorate Style mechanics:
1. The Gluttonous Chitin (Amber Noon)
2. The Crimson Siphon (Crimson Dusk)
3. The Clockwork Sweeper (Green Noon)
4. The Void Siphon (Violet Dusk)
5. The Subterranean Burrower (Amber Dusk)
6. The Horizon of Hope (Pale Midnight)
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

filepath = "SOMNARAK-WORLD/The_Absolvohan/Part_7_Days_125_to_145.md"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# -------------------------------------------------------------
# 1. The Gluttonous Chitin (Amber Noon)
# -------------------------------------------------------------
box_chitin_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (AMBER CHITIN)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [BEETLE-A][BEETLE-B][KANG]         [SHIN]                 [DEKAN]",
    "DIST    : Kang at N03 (Band 1); Shin at N05 (Band 3); Dekan at N10.",
    "---",
    "Agent Kang      : Speed 6 -> 3 AP | HP: 155/155 | SP: +35 | Lock Maul",
    "Agent Shin      : Speed 5 -> 3 AP | HP: 125/125 | SP: +30 | Choral Staff",
    "Chitin Beetles(x2): Speed 4 -> 2 AP | HP: 380 each | Crushing Crunch"
])

box_chitin_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Kang hammers thorax; Shin focuses Lament; Beetle-A 60% Stagger 1.",
    "- Turn 03: Carapace cracked; direct Grudge blunt strikes deal 2.0x direct damage.",
    "- Turn 04: Beetle-B charges mandibles; Dekan locks Jaw Clamp at Node 2.",
    "- Turn 05: Shin channels acoustic wave into exposed marrow; Terminal Stagger.",
    "- Turn 06: Kang executes Climax Maul Shatter; beetles dissolve to amber gravel."
])

box_chitin_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Sub-flooring integrity restored across Floor 2.",
    "2. Status Equilibrium : Mandible tremors cease; team SP stabilizes at +40.",
    "3. Containment Check   : Both Armored Burrowers completely pulverized.",
    "4. OUTCOME             : ZERO FATALITIES — +0.060 TONS BONUS HAN HARVESTED."
])

old_chitin = """Tactical Clash Telemetry:
- The two colossal beetles breach through the floor plating, gnashing mandibles with crushing Weight damage (18 damage -> mitigated to 9 by *Soldier Coat*).
- Range Band 1: Agent Kang plants his heavy maul into the lead beetle's thorax, cracking its thick chitin shell (Critical strike: 160 Grudge damage).
- Agent Shin channels the *Choral Staff*, directing a focused cobalt Lament wave into the exposed marrow.
- Both entities dissolve into inert amber gravel; zero personnel fatalities.
- Elimination verified; +0.060 tons bonus Han harvested.

Shift concludes with cumulative daily harvest of **0.920 tons** (100% quota achieved)."""

new_chitin = f"""Director Majin establishes GBS tactical engagement in Floor 2's corridor:

```text
{box_chitin_hud}
```

###### Turn 01 Action Resolution Log (Floor 2 Central Corridor)
- **Step 1: Floor 2 Echo-Core Resonance (Attendant Dekan)**:
  * Dekan activates *The Maw's Keep Bastion Ward*, raising physical hardness over Nodes 1 to 4 and cutting mandible crunch trauma by 50%.
- **Step 2: Movement & Action Point Spending**:
  * Agent Kang (Speed 6 -> 3 AP) spends 1 AP to advance from Node 4 to Node 3 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Lock Maul Thorax Breaker]`.
  * Agent Shin (Speed 5 -> 3 AP) deploys at Node 5 (Range Band 3). Spends 2 AP to channel `[Choral Staff Cobalt Lament Wave]`. Remaining 1 AP held in Guard.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * Lead Chitin Beetle lunges with `[Crushing Mandible Shear]` (Base 9 + 2 Coins = 13 Power).
  * Agent Kang's `[Lock Maul Thorax Breaker]` (Base 12 + 2 Coins = 16 Power).
  * **Resolution**: Kang WINS THE CLASH (16 vs 13).
    * Kang drives the heavy maul straight into the beetle's central dorsal plate, shattering the outer shell for **54 Grudge damage** and inflicting +28 Stagger!
  * Shin channels acoustic energy directly into the rupture, dealing 40 Lament damage.

```text
{box_chitin_turns}
```

```text
{box_chitin_phase}
```

Shift concludes with cumulative daily harvest of **0.920 tons** (100% quota achieved)."""

if old_chitin in text:
    text = text.replace(old_chitin, new_chitin)
    print("Replaced Chitin section successfully!")
else:
    print("Could not find Chitin section!")

# -------------------------------------------------------------
# 2. The Crimson Siphon (Crimson Dusk)
# -------------------------------------------------------------
box_siphon_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (CRIMSON SIPHON)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [SIPHON-A]    [KANG]  [HWANG]         [NOH]                  [ISHALL]",
    "DIST    : Kang at N02 (Band 1); Hwang at N03 (Band 2); Noh at N05 (Band 3).",
    "---",
    "Agent Kang      : Speed 6 -> 3 AP | HP: 155/155 | SP: +35 | Heavy Maul",
    "Agent Hwang     : Speed 6 -> 3 AP | HP: 135/135 | SP: +30 | Apostle Scalpel",
    "Agent Noh       : Speed 5 -> 3 AP | HP: 130/130 | SP: +25 | Clockwork Bayonet",
    "Crimson Siphon(x2): Speed 4 -> 2 AP | HP: 420 each | Bleed Drain"
])

box_siphon_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Noh severs feeder tendrils; Hwang chills main valve; 60% Stagger 1.",
    "- Turn 03: Posture broken; cryo-Lament strikes deal 2.0x direct damage.",
    "- Turn 04: Siphon-B surges [Bleed Deluge]; Ishall deploys Shadow Ingress.",
    "- Turn 05: Hwang's cryo incision freezes internal conduits; Terminal Stagger.",
    "- Turn 06: Kang executes Climax Maul Smash; frozen siphons shatter to ice."
])

box_siphon_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Coolant trunk line hydraulic fluid stabilized.",
    "2. Status Equilibrium : Bleed lacerations purged; team SP rises to +40.",
    "3. Containment Check   : Both Crimson Siphons completely frozen and shattered.",
    "4. OUTCOME             : ZERO CASUALTIES — +0.070 TONS BONUS HAN SECURED."
])

old_siphon = """Tactical Clash Telemetry:
- The two pulsing crimson siphons wrap around the coolant trunk lines, draining hydraulic fluid to feed bleed tentacles.
- Range Band 3: Agent Noh unleashes continuous Grudge spikes from the *Clockwork Bayonet*, severing the exterior feeder tendrils.
- Range Band 2: Agent Hwang steps forward, channeling concentrated Lament frost with the consecrated scalpel. The cryogenic wave freezes the siphons' main valves.
- Agent Kang delivers the finishing blow at Range Band 1 with his heavy maul, shattering the frozen siphons into crimson ice shards.
- Elimination verified; +0.070 tons bonus Han secured.

Daily shift concludes with cumulative total of **0.980 tons** (100% quota achieved)."""

new_siphon = f"""Director Majin establishes GBS tactical engagement in Floor 7's Atrium:

```text
{box_siphon_hud}
```

###### Turn 01 Action Resolution Log (Floor 7 Main Atrium)
- **Step 1: Floor 7 Echo-Core Resonance (Shadow Lead Ishall)**:
  * Ishall deploys *Shadow Ingress*, allowing rapid flanking strikes without provoking bleed tentacle opportunity attacks.
- **Step 2: Movement & Action Point Spending**:
  * Agent Noh (Speed 5 -> 3 AP) deploys at Node 5 (Range Band 3). Spends 2 AP to ready `[Clockwork Bayonet Tendril Severing Burst]`. Remaining 1 AP in Guard.
  * Agent Hwang (Speed 6 -> 3 AP) advances to Node 3 (Close Range Band 2). Spends 2 AP to charge `[Apostle Scalpel Cryo-Lament Incision]`.
  * Agent Kang (Speed 6 -> 3 AP) spends 1 AP to sprint to Node 2 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Heavy Maul Frost Shatter]`.
- **Step 3: Clash Resolution (Node 1 to 3)**:
  * Crimson Siphon A attempts `[Sanguine Hydraulic Siphon]` (Base 9 + 2 Coins = 13 Power).
  * Agent Hwang's `[Apostle Scalpel Cryo-Lament Incision]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Hwang WINS THE CLASH (15 vs 13).
    * Hwang carves through the main arterial valve with frozen precision, freezing its circulation and dealing **46 Lament damage** with +26 Stagger!
  * Noh's bayonet fires concentrated spikes from Node 5, severing external feeder tendrils.

```text
{box_siphon_turns}
```

```text
{box_siphon_phase}
```

Daily shift concludes with cumulative total of **0.980 tons** (100% quota achieved)."""

if old_siphon in text:
    text = text.replace(old_siphon, new_siphon)
    print("Replaced Crimson Siphon section successfully!")
else:
    print("Could not find Crimson Siphon section!")

# -------------------------------------------------------------
# 3. The Clockwork Sweeper (Green Noon)
# -------------------------------------------------------------
box_sweeper_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (CLOCKWORK SWEEPER)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [SWEEPER-A][SWEEPER-B][KANG]       [JIN]                  [MARJUK]",
    "DIST    : Kang at N03 (Band 1); Jin at N05 (Band 3); Marjuk at N10.",
    "---",
    "Agent Kang      : Speed 6 -> 3 AP | HP: 155/155 | SP: +35 | Heavy Maul",
    "Agent Jin       : Speed 6 -> 3 AP | HP: 130/130 | SP: +30 | Choral Bell",
    "Clockwork Sweeper(x2): Speed 6 -> 3 AP | HP: 360 each | Rotary Blade"
])

box_sweeper_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Kang blocks scythe; Jin fires sonic bell; Sweeper-A 60% Stagger 1.",
    "- Turn 03: Posture broken; direct Grudge blunt strikes deal 2.0x direct damage.",
    "- Turn 04: Sweeper-B accelerates [Rotary Severance]; Marjuk engages stasis.",
    "- Turn 05: Jin disrupts gear synchronizer; forces Terminal Stagger on both.",
    "- Turn 06: Kang executes Climax Maul Sweep; drive sprockets pulverized."
])

box_sweeper_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Hydraulic plaza cleared of spinning shrapnel.",
    "2. Status Equilibrium : Rotary wind calm; team SP stabilizes at +40.",
    "3. Containment Check   : Both Sweeper frames completely crushed.",
    "4. OUTCOME             : ZERO CASUALTIES — +0.065 TONS BONUS HARVESTED."
])

old_sweeper = """Tactical Clash Telemetry:
- The sweepers sprint through the corridor, spinning rotary scythe blades with lethal cutting speed.
- Range Band 1: Agent Kang plants his heavy maul into the ground, locking his *Feather Mantle* to absorb the kinetic blade clash (mitigated to 8 damage).
- Agent Jin unleashes a piercing sonic wave from Range Band 3 with the *Choral Bell*, disrupting the sweepers' internal gear synchronization.
- Kang follows up with a crushing horizontal swing, shattering the drive sprockets of both automatons simultaneously.
- Elimination verified; +0.065 tons bonus Han harvested.

Shift concludes with cumulative daily harvest of **1.050 tons** (100% quota achieved)."""

new_sweeper = f"""Director Majin establishes GBS tactical engagement in the Hydraulic Plaza:

```text
{box_sweeper_hud}
```

###### Turn 01 Action Resolution Log (Floor 6 Hydraulic Plaza)
- **Step 1: Floor 6 Echo-Core Resonance (Archive Lead Marjuk)**:
  * Marjuk deploys *The Temporal Stasis Array*, reducing the sweepers' rotary attack speed by 30% across Nodes 1 to 3.
- **Step 2: Movement & Action Point Spending**:
  * Agent Kang (Speed 6 -> 3 AP) plants his boots at Node 3 (Point-Blank Range Band 1). Spends 2 AP to declare `[Heavy Maul Kinetic Blade-Lock]`. Remaining 1 AP in Guard.
  * Agent Jin (Speed 6 -> 3 AP) positions at Node 5 (Range Band 3). Spends 2 AP to ready `[Choral Bell Resonant Sonic Pulse]`.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * Clockwork Sweeper A charges with `[High-Speed Rotary Scythe Slash]` (Base 10 + 2 Coins = 14 Power).
  * Agent Kang's `[Heavy Maul Kinetic Blade-Lock]` (Base 12 + 2 Coins = 16 Power).
  * **Resolution**: Kang WINS THE CLASH (16 vs 14).
    * Kang locks his maul head against the whirling scythe, grinding its drive teeth to a dead halt and dealing **52 Grudge damage** with +28 Stagger!
  * Jin unleashes the *Choral Bell* from Node 5, sending acoustic shockwaves that disrupt Sweeper B's internal escapement.

```text
{box_sweeper_turns}
```

```text
{box_sweeper_phase}
```

Shift concludes with cumulative daily harvest of **1.050 tons** (100% quota achieved)."""

if old_sweeper in text:
    text = text.replace(old_sweeper, new_sweeper)
    print("Replaced Clockwork Sweeper section successfully!")
else:
    print("Could not find Clockwork Sweeper section!")

# -------------------------------------------------------------
# 4. The Void Siphon (Violet Dusk)
# -------------------------------------------------------------
box_voidsiphon_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (VOID SIPHON)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [WELL-A]  [WELL-B] [KANG]  [BAE]                              [AYSHUK]",
    "DIST    : Kang at N03 (Band 1); Bae at N04 (Band 1); Ayshuk at N10.",
    "---",
    "Agent Kang      : Speed 6 -> 3 AP | HP: 160/160 | SP: +40 | Heavy Maul",
    "Agent Bae       : Speed 6 -> 3 AP | HP: 145/145 | SP: +35 | Bulwark Maul",
    "Floating Wells(x2): Speed 4 -> 2 AP | HP: 440 each | Psychic Hum"
])

box_voidsiphon_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Kang & Bae deliver synchronized slam; Well-A hits 60% Stagger 1.",
    "- Turn 03: Posture broken; direct Grudge blunt strikes deal 2.0x direct damage.",
    "- Turn 04: Well-B charges [Global Sanity Vortex]; Ayshuk predicts firing arc.",
    "- Turn 05: Bae smashes gravitic focal ring, forcing Terminal Stagger.",
    "- Turn 06: Dual Overdrive Climax Shatter; wells implode to harmless mist."
])

box_voidsiphon_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Sub-Vault Gallery psychic pressure returns to zero.",
    "2. Status Equilibrium : Team SP stabilized; no sanity drain sustained.",
    "3. Containment Check   : Both Void Wells completely imploded.",
    "4. OUTCOME             : PERFECT DUAL SLAM — +0.075 TONS BONUS HARVESTED."
])

old_voidsiphon = """Tactical Clash Telemetry:
- The two floating violet wells emit an intense psychic drain that leaches sanity across the corridor.
- Range Band 1: Agent Kang and Agent Bae sprint through the gravitic disruption, raising their heavy mauls in perfect sync.
- Synchronized slam! Both mauls strike the vortex focal points simultaneously, shattering the gravitic cohesion (Combined damage: 290 Grudge).
- The dual wells collapse into harmless purple mist; zero casualties sustained.
- Elimination verified; +0.075 tons bonus Han harvested.

Shift concludes with cumulative daily harvest of **1.120 tons** (100% quota achieved)."""

new_voidsiphon = f"""Director Majin establishes GBS tactical engagement in the Sub-Vault Gallery:

```text
{box_voidsiphon_hud}
```

###### Turn 01 Action Resolution Log (Floor 4 Sub-Vault Gallery)
- **Step 1: Floor 4 Echo-Core Resonance (Research Lead Ayshuk)**:
  * Ayshuk engages *The Predictive HUD*, projecting the wells' psychic resonance nodes onto the operatives' visors and granting +3 Clash Power.
- **Step 2: Movement & Action Point Spending**:
  * Agent Kang (Speed 6 -> 3 AP) spends 1 AP to sprint to Node 3 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Heavy Maul Grav-Shatter]`.
  * Agent Bae (Speed 6 -> 3 AP) advances to Node 4 (Point-Blank Range Band 1). Spends 2 AP to ready `[Bulwark Maul Synchronized Slam]`. Remaining 1 AP held in Guard.
- **Step 3: Clash Resolution (Node 1 to 3)**:
  * Floating Well A emits `[Intense Sanity Leeching Vortex]` (Base 10 + 2 Coins = 14 Power).
  * Agent Kang & Agent Bae's `[Synchronized Dual Maul Slam]` (Base 13 + 2 Coins = 17 Power).
  * **Resolution**: The Agents WIN THE CLASH (17 vs 14).
    * Both heavy mauls strike the vortex core simultaneously, breaking its gravitic cohesion and dealing **68 Grudge damage** with +34 Stagger!
  * The psychic drain collapses instantly, shielding the floor's personnel.

```text
{box_voidsiphon_turns}
```

```text
{box_voidsiphon_phase}
```

Shift concludes with cumulative daily harvest of **1.120 tons** (100% quota achieved)."""

if old_voidsiphon in text:
    text = text.replace(old_voidsiphon, new_voidsiphon)
    print("Replaced Void Siphon section successfully!")
else:
    print("Could not find Void Siphon section!")

# -------------------------------------------------------------
# 5. The Subterranean Burrower (Amber Dusk)
# -------------------------------------------------------------
box_burrower_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (SUBTERRANEAN WORM)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [WORM-A]  [WORM-B] [KANG]  [CHA]           [REFUGEE-SMITHS][MELLDA]",
    "DIST    : Kang at N03 (Band 1); Cha at N04 (Band 2); Smiths at N06 (Band 3).",
    "---",
    "Agent Kang      : Speed 6 -> 3 AP | HP: 160/160 | SP: +40 | Heavy Maul",
    "Agent Cha       : Speed 5 -> 3 AP | HP: 130/130 | SP: +30 | Forge Bracer",
    "Refugee Smiths  : Speed 5 -> 3 AP | Molten Brass Barrier | Cheonbulok Ally",
    "Trench Worms(x2): Speed 4 -> 2 AP | HP: 440 each | Chitin Crush"
])

box_burrower_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Smiths pin Worm-B with brass; Kang fractures Worm-A; 60% Stagger 1.",
    "- Turn 03: Posture broken; direct Grudge/Thermal strikes deal 2.0x direct damage.",
    "- Turn 04: Worm-A charges [Trench Collapser]; Mellda locks drainage sluice.",
    "- Turn 05: Cha drives thermal spike into soft segment; forces Terminal Stagger.",
    "- Turn 06: Dual kinetic decapitation; burrowers dissolve to molten chitin."
])

box_burrower_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Drainage sub-plaza forge line reinforced.",
    "2. Status Equilibrium : Bedrock vibrations calm; team SP at full capacity.",
    "3. Containment Check   : Both trench worms eradicated; forge protected.",
    "4. OUTCOME             : ZERO ALLIED CASUALTIES — +0.080 TONS BONUS HARVESTED."
])

old_burrower = """Tactical Clash Telemetry:
- The two armored worms breach the stone floorplates directly beneath the forge line.
- The Cheonbulok refugee smiths drop a wall of molten brass, pinning the second worm's burrowing tracks!
- Range Band 1: Agent Kang charges with the *Heavy Maul*, fracturing the lead worm's mandible with a downward blow (185 Grudge damage).
- Agent Cha follows up with the *Forge Bracer*, driving a high-heat thermal spike into the soft segment joints, decapitating the beast.
- The secondary worm is dissolved under continuous brass fire; zero casualties.
- Elimination verified; +0.080 tons bonus Han harvested.

Shift concludes with cumulative daily harvest of **1.180 tons** (100% quota achieved)."""

new_burrower = f"""Director Majin establishes GBS tactical engagement at Floor 5's drainage sub-plaza:

```text
{box_burrower_hud}
```

###### Turn 01 Action Resolution Log (Floor 5 Drainage Sub-Plaza)
- **Step 1: Floor 5 Echo-Core Resonance (Border Lead Mellda)**:
  * Mellda activates *The Bulwark Perimeter*, locking Node 5 to prevent subterranean tremors from destabilizing the refugee forge line.
- **Step 2: Movement & Action Point Spending**:
  * Refugee Smiths (Cheonbulok Allies) deploy molten brass barriers across Node 4 to pin Worm B's burrowing tracks.
  * Agent Kang (Speed 6 -> 3 AP) spends 1 AP to sprint to Node 3 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Heavy Maul Downward Mandible Smash]`.
  * Agent Cha (Speed 5 -> 3 AP) stands at Node 4 (Range Band 2). Spends 2 AP to ready `[Forge Bracer High-Heat Thermal Spike]`. Remaining 1 AP in Guard.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * Lead Trench Worm launches `[Crushing Segment Charge]` (Base 10 + 2 Coins = 14 Power).
  * Agent Kang's `[Heavy Maul Mandible Smash]` (Base 12 + 2 Coins = 16 Power).
  * **Resolution**: Kang WINS THE CLASH (16 vs 14).
    * Kang's warhammer crashes directly onto the beast's mandibles, splintering the diamond edge and dealing **58 Grudge damage** with +28 Stagger!
  * Cha follows up with a thermal thrust into the exposed marrow for 44 thermal damage.

```text
{box_burrower_turns}
```

```text
{box_burrower_phase}
```

Shift concludes with cumulative daily harvest of **1.180 tons** (100% quota achieved)."""

if old_burrower in text:
    text = text.replace(old_burrower, new_burrower)
    print("Replaced Subterranean Burrower section successfully!")
else:
    print("Could not find Subterranean Burrower section!")

# -------------------------------------------------------------
# 6. The Horizon of Hope (Pale Midnight)
# -------------------------------------------------------------
box_hope_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (HORIZON OF HOPE)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [GATEWAY]     [KANG]  [KIM]   [SEO]   [HONG]                 [ZYRAK]",
    "DIST    : Kang & Kim at N02-N03; Seo at N04 (Band 2); Hong at N05 (Band 3).",
    "---",
    "Agent Kang      : Speed 6 -> 3 AP | HP: 165/165 | SP: +45 | Lock Maul (Grudge)",
    "Agent Hong      : Speed 6 -> 3 AP | HP: 130/130 | SP: +40 | Saint Robe (Lament)",
    "Agent Seo       : Speed 5 -> 3 AP | HP: 125/125 | SP: +35 | Apostle Scalpel (Void)",
    "Agent Kim       : Speed 5 -> 3 AP | HP: 140/140 | SP: +35 | Greaves (Weight)",
    "Horizon Gateway : Speed 5 -> 4 AP | HP: 600/600 | 25% Pale | Sovereign Gate"
])

box_hope_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Four-Aspect Strike lands; balances all 4 affinities; 60% Stagger 1.",
    "- Turn 03: Posture broken; all 4 damage types deal 2.0x direct damage.",
    "- Turn 04: Gateway pulses [Radiant Horizon Shockwave]; Kim grounds pylons.",
    "- Turn 05: Hong channels pure sorrow harmonic, reducing Pale resonance.",
    "- Turn 06: Quadruple Overdrive Climax Strike; Gateway resolves to golden dawn."
])

box_hope_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Archive Rotunda dimensional pressure stabilizes.",
    "2. Status Equilibrium : Pale sunder clears; team HP and SP at full capacity.",
    "3. Containment Check   : Sovereign Gateway resolved into gentle starlight.",
    "4. OUTCOME             : HISTORIC TRANSCENDENCE — +0.090 TONS BONUS SECURED."
])

old_hope = """Tactical Clash Telemetry:
- The colossal gateway radiates pulsing Pale waves that threaten to strip 25% of maximum HP per harmonic pulse.
- Four-Aspect Strike deployed!
  * Range Band 1: Agent Kang strikes the gateway's left pylon with heavy Grudge impact (*Lock Maul*).
  * Range Band 3: Agent Hong channels pure weeping Lament through the *Saint Robe*.
  * Range Band 2: Agent Seo carves the right pylon with Void incisions (*Apostle Scalpel*).
  * Range Band 1: Agent Kim grounds the foundation with Weight anchoring (*Foundation Greaves*).
- The four frequencies achieve perfect harmonic equilibrium; the Pale anomaly dissolves into gentle, golden starlight.
- Elimination verified; +0.090 tons bonus Han secured.

Daily shift concludes with cumulative total of **1.250 tons** (100% quota achieved)."""

new_hope = f"""Director Majin coordinates the Four-Aspect Strike across the 10-node grid:

```text
{box_hope_hud}
```

###### Turn 01 Action Resolution Log (Floor 3 Archive Rotunda)
- **Step 1: Floor 3 Echo-Core Resonance (Extraction Lead Zyrak)**:
  * Zyrak activates *The Energy Siphon*, recycling surplus harmonic frequencies into the facility containment grid.
- **Step 2: Movement & Action Point Spending**:
  * Agent Kang (Speed 6 -> 3 AP) takes Node 2 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Lock Maul Grudge Sunder]` on the left pylon.
  * Agent Kim (Speed 5 -> 3 AP) stands at Node 3 (Point-Blank Range Band 1). Spends 2 AP to execute `[Foundation Greaves Weight Grounding]`.
  * Agent Seo (Speed 5 -> 3 AP) takes Node 4 (Close Range Band 2). Spends 2 AP to ready `[Apostle Scalpel Void Incision]` on the right pylon.
  * Agent Hong (Speed 6 -> 3 AP) anchors Node 5 (Range Band 3). Spends 2 AP to channel `[Saint Robe Pure Lament Weeping]`.
- **Step 3: Clash Resolution (The Four-Aspect Equilibrium)**:
  * Horizon Gateway unleashes `[Radiant Horizon Pale Wave]` (Base 12 + 2 Coins = 16 Power).
  * Allied Quadruple Standoff (Base 14 + 2 Coins = 18 Power).
  * **Resolution**: The Four Operatives WIN THE CLASH (18 vs 16).
    * Kang strikes Grudge, Kim grounds Weight, Seo carves Void, and Hong channels Lament! The four elemental frequencies achieve perfect resonance, canceling the Pale pulse and dealing **74 True Elemental damage** with +36 Stagger!

```text
{box_hope_turns}
```

```text
{box_hope_phase}
```

Daily shift concludes with cumulative total of **1.250 tons** (100% quota achieved)."""

if old_hope in text:
    text = text.replace(old_hope, new_hope)
    print("Replaced Horizon of Hope section successfully!")
else:
    print("Could not find Horizon of Hope section!")

check_banned(text, filepath)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
print(f"Updated {filepath} with all expanded GBS battles!")
