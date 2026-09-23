#!/usr/bin/env python3
"""
tools/expand_absolvohan_battles_part3_all.py
Expands ALL Ordeal and combat encounters in SOMNARAK-WORLD/The_Absolvohan/Part_3_Days_29_to_49.md
with full Gameplay Battle System (GBS) Reverie Directorate Style mechanics:
1. Sanguine Larvae (Crimson Noon)
2. The Gilded Drowners (Violet Dusk)
3. Pugnahan Combat Work on SE-055 (The Iron Statue)
4. The Churning Hive (Amber Dusk)
5. The Midnight Herald (Sovereign Watch)
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

filepath = "SOMNARAK-WORLD/The_Absolvohan/Part_3_Days_29_to_49.md"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# -------------------------------------------------------------
# 1. Sanguine Larvae (Crimson Noon)
# -------------------------------------------------------------
box_larvae_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (CRIMSON NOON)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [POD-1]   [POD-2] [HWANG]         [SONG]         [MAJIN]",
    "DIST    : Hwang at N03 (Band 1); Song at N05 (Band 3); Majin at N09.",
    "---",
    "Agent Hwang : Speed 6 -> 3 AP | HP: 115/115 | SP: +25 | Observing Scepter",
    "Agent Song  : Speed 5 -> 3 AP | HP: 110/110 | SP: +20 | Kinetic Cleaver",
    "Sanguine Pod: Speed 4 -> 2 AP | HP: 160/160 | Sorrow: 50% | Acid Brood"
])

box_larvae_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Hwang pierces Pod 1; triggers 60% Stagger 1; Song flanks N04.",
    "- Turn 03: All allied attacks deal 2.0x direct damage; Pod 1 destroyed.",
    "- Turn 04: Pod 2 spawns brood cluster; Dekan engages Bastion Ward.",
    "- Turn 05: Song sweeps Node 2 with kinetic arc; forces Terminal Stagger.",
    "- Turn 06: Hwang executes Climax Siphon; all larvae vaporize into red ash."
])

box_larvae_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Corridor drainage pumps clear biological bile.",
    "2. Status Equilibrium : Bleed counters purge; team SP rises to +32.",
    "3. Containment Check   : Zero breaches across Chambers 031, 032, 033.",
    "4. OUTCOME             : 100% SUPPRESSION — ZERO CASUALTIES, +15 RHR."
])

target_larvae_start = "##### Ordeal Manifestation: Crimson Noon Ordeal — The Sanguine Larvae"
target_larvae_end = "- **Ordeal Suppressed with 0 cell breaches and 0 agent casualties!** +15 RHR reagents secured."

new_larvae_full = f"""##### Ordeal Manifestation: Crimson Noon Ordeal — The Sanguine Larvae
At 0.125 tons harvested, the floor vents rupture. Four crimson flesh pods erupt across Floor 2 and Floor 3, spawning scuttling Sorrow Larvae that seek out containment doors to cause instant breaches!

```text
+==============================================+
| TACTICAL DOSSIER: CRIMSON NOON ORDEAL        |
| DESIGNATION : SANGUINE LARVAE                |
| CLASSIFICATION : RED (GRUDGE/WEIGHT) NOON    |
| INTRUSION POINT : FLOOR 2 & 3 CORRIDORS      |
| HOSTILE PARAMETERS:                          |
| - Entities: 4x Rapid Flesh Pods & Broods     |
| - Attack Affinity: Grudge Bleed Hemorrhage   |
| - Weakness Affinity: Void / Pierce           |
| TACTICAL DEPLOYMENT: SPLIT TEAMS INTERCEPT   |
+==============================================+
```

Director Majin establishes split-team GBS sector commands:
- **Team A (Agent Hwang & Agent Song)** intercepts Pod 1 & 2 outside Chamber 033 on Floor 2.
- **Team B (Agent Kim & Agent Park)** locks down Pod 3 & 4 at the main vertical stairwell.

```text
{box_larvae_hud}
```

###### Turn 01 Action Resolution Log (Team A — Floor 2 Sector)
- **Step 1: Floor 2 Echo-Core Resonance (Containment Lead Dekan)**:
  * Dekan anchors *The Maw's Keep Bastion Ward*, raising physical barrier resistance across Nodes 1 to 4 and nullifying the larvae's acid bleed coating.
- **Step 2: Movement & Action Point Spending**:
  * Agent Hwang (Speed 6 -> 3 AP) spends 1 AP to advance from Node 3 to Node 2 (Point-Blank Range Band 1 with Flesh Pod 1).
  * Hwang spends 2 AP to declare `[Observing Scepter Void Thrust]`.
  * Agent Song (Speed 5 -> 3 AP) advances to Node 4 (Range Band 2). Spends 2 AP to ready `[Kinetic Cleaver Pincer Sweep]`. Remaining 1 AP held in Guard.
- **Step 3: Clash Resolution (Node 2)**:
  * Flesh Pod 1 declares `[Acid Bile Burst]` on Node 2 (Base 7 + 2 Coins = 11 Power).
  * Hwang's `[Observing Scepter Void Thrust]` (Base 9 + 2 Coins = 13 Power).
  * **Resolution**: Hwang WINS THE CLASH (13 vs 11).
    * Hwang's scepter pierces the pod's central valve, dealing 34 Void damage and inflicting +18 Stagger.
  * Agent Song cleaves incoming larvae at Node 4, dealing 28 kinetic damage and preventing encirclement.

```text
{box_larvae_turns}
```

```text
{box_larvae_phase}
```

- **Ordeal Suppressed with 0 cell breaches and 0 agent casualties!** +15 RHR reagents secured."""

if target_larvae_start in text and target_larvae_end in text:
    idx1 = text.find(target_larvae_start)
    idx2 = text.find(target_larvae_end) + len(target_larvae_end)
    text = text[:idx1] + new_larvae_full + text[idx2:]
    print("Replaced Larvae section with full GBS!")
else:
    print("Could not find Larvae section!")

# -------------------------------------------------------------
# 2. The Gilded Drowners (Violet Dusk)
# -------------------------------------------------------------
box_drowners_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (VIOLET DUSK)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [DROWNER]     [PARK]  [HWANG]         [KIM]          [MAJIN]",
    "DIST    : Park at N03 (Band 2); Hwang at N04 (Band 3); Kim at N06.",
    "---",
    "Agent Park    : Speed 6 -> 3 AP | HP: 120/120 | SP: +25 | Lament Requiem",
    "Agent Hwang   : Speed 5 -> 3 AP | HP: 110/110 | SP: +20 | Guardian Shield",
    "Agent Kim     : Speed 5 -> 3 AP | HP: 105/105 | SP: +20 | Kinetic Carbine",
    "Gilded Drowner: Speed 4 -> 2 AP | HP: 280/280 | Sorrow: 60% | Void Beam"
])

box_drowners_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Park charges N02; delivers 42 Lament damage; Drowner 60% Stagger 1.",
    "- Turn 03: Defense breaks to 0; all attacks deal 2.0x direct damage; HP at 110.",
    "- Turn 04: Drowner recovers; charges corridor laser [Oblivion Torrent].",
    "- Turn 05: Hwang deploys Guardian Aegis at N03, completely blocking beam.",
    "- Turn 06: Kim & Park coordinate dual clash; Terminal Stagger shatters monument."
])

box_drowners_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Violet laser conduits overload and power down.",
    "2. Status Equilibrium : Void radiation drains; team SP stabilizes at +30.",
    "3. Containment Check   : All three monuments neutralized across floors.",
    "4. OUTCOME             : ZERO AGENT CASUALTIES, +22 REFINED RHR."
])

target_drowners_start = "##### Ordeal Manifestation: Third Watch (Dusk) Ordeal — The Gilded Drowners"
target_drowners_end = "- **All 3 monuments shatter within 38 seconds of arrival! Zero agent casualties!** +22 RHR harvested."

new_drowners_full = f"""##### Ordeal Manifestation: Third Watch (Dusk) Ordeal — The Gilded Drowners
At 0.145 tons harvested, the facility's emergency sirens shift from amber to violet. A Dusk Ordeal has arrived:

```text
+==============================================+
| TACTICAL DOSSIER: THIRD WATCH (DUSK) ORDEAL  |
| DESIGNATION : THE GILDED DROWNERS            |
| CLASSIFICATION : VIOLET (VOID/DECAY) DUSK    |
| INTRUSION POINT : FLOORS 1, 3, AND 5         |
| HOSTILE PARAMETERS:                          |
| - Entities: 3x Colossal Gilded Monoliths     |
| - Attack Affinity: Piercing Void Lasers      |
| - Weakness Affinity: Lament / Weight         |
| TACTICAL DEPLOYMENT: TRI-SECTOR INTERCEPT    |
+==============================================+
```

Three colossal gilded monuments materialize simultaneously across the facility spine, channeling high-yield Void laser arrays across entire corridors!

Director Majin coordinates tri-sector suppression on the 10-node grid:
- **Floor 1 Primary Sector**: Agent Park, Agent Hwang, and Agent Kim engage Monument Alpha.
- **Floor 3 Sector**: Extraction Lead Zyrak activates terminal dampeners.
- **Floor 5 Sector**: Border Lead Mellda locks down the blast sluices.

```text
{box_drowners_hud}
```

###### Turn 01 Action Resolution Log (Floor 1 Main Corridor)
- **Step 1: Floor 1 Echo-Core Resonance (Director Majin & Secretary Seiyon)**:
  * Majin deploys *The Command Eye*, rerolling Agent Park's Speed Die from 4 to 6, granting 3 Action Points.
  * Secretary Seiyon broadcasts *Administrative Clarity*, preparing +15 SP restoration on first clash victory.
- **Step 2: Movement & Action Point Spending**:
  * Agent Park (Speed 6 -> 3 AP) spends 1 AP to advance from Node 4 to Node 3 (Close Range Band 2).
  * Park spends 2 AP to prepare `[Lament Requiem Heavy Smite]`.
  * Agent Hwang (Speed 5 -> 3 AP) advances to Node 3 beside Park, spending 2 AP to deploy `[Guardian Shield Reflection Mantlet]`.
  * Agent Kim (Speed 5 -> 3 AP) holds Node 6, aiming concentrated rifle fire at the monument's optical lens.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * The Gilded Drowner charges `[Void Prismatic Ray]` targeting Node 3 (Base 8 + 2 Coins = 12 Power).
  * Agent Park's `[Lament Requiem Heavy Smite]` (Base 9 + 2 Coins = 14 Power).
  * **Resolution**: Park WINS THE CLASH (14 vs 12).
    * Park's warhammer smashes into the focusing crystal, disrupting the beam charge and dealing 42 Lament damage with +24 Stagger!
  * Hwang's shield absorbs the stray refractive discharge, taking 0 damage.

```text
{box_drowners_turns}
```

```text
{box_drowners_phase}
```

- **All 3 monuments shatter within 38 seconds of arrival! Zero agent casualties!** +22 RHR harvested."""

if target_drowners_start in text and target_drowners_end in text:
    idx1 = text.find(target_drowners_start)
    idx2 = text.find(target_drowners_end) + len(target_drowners_end)
    text = text[:idx1] + new_drowners_full + text[idx2:]
    print("Replaced Gilded Drowners section with full GBS!")
else:
    print("Could not find Gilded Drowners section!")

# -------------------------------------------------------------
# 3. SE-055 (The Iron Statue) Combat Work
# -------------------------------------------------------------
box_statue_hud = make_box("COMBAT WORK HUD: PHASE 01 — BATTLE TURN 01 (SE-055 PUGNAHAN)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [STATUE]      [BAE]           [HWANG]         [CONSOLE]",
    "DIST    : Bae at N02 (Band 1); Hwang at N04 (Band 2); Console at N05.",
    "---",
    "Agent Bae   : Speed 6 -> 3 AP | HP: 130/130 | SP: +25 | Bulwark Maul",
    "Agent Hwang : Speed 5 -> 3 AP | HP: 115/115 | SP: +25 | Guardian Aegis",
    "The Iron Statue : Speed 3 -> 2 AP | HP: 300/300 | Sorrow: 75% | Iron Fist"
])

box_statue_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Bae parries iron strike; Hwang scans posture; Statue 60% Stagger 1.",
    "- Turn 03: Bae executes non-lethal Pugnahan lock; entity Speed reduced by -4.",
    "- Turn 04: Statue attempts berserk hammer; Bae absorbs impact behind shield.",
    "- Turn 05: Hwang completes cognitive dampening; Sorrow Gauge drops to 20%.",
    "- Turn 06: Final Pugnahan clamp locks armature; entity enters stable stasis."
])

box_statue_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Chamber 055 containment integrity stabilizes at 98%.",
    "2. Status Equilibrium : Physical strain vents; Bae gains +5 Resilience.",
    "3. Containment Check   : 10/10 Positive Han crystals secured (+0.018t).",
    "4. OUTCOME             : PERFECT PUGNAHAN CONTAINMENT — ZERO VESSEL DAMAGE."
])

target_statue_start = "##### Work Session 1: Pugnahan Combat Work on SE-055 (The Iron Statue)"
target_statue_end = "- Work concludes with **10/10 Positive Han crystals extracted!** Energy counter hits `0.165 / 0.170 tons`."

new_statue_full = f"""##### Work Session 1: Pugnahan Combat Work on SE-055 (The Iron Statue)
Majin issues heavy combat dispatch:
- `[DISPATCH ORDER: Agent Bae -> Sector 5, Chamber 055 (The Iron Statue)]`
- `[ASSIGNED PROTOCOL: Pugnahan Confrontation]`
- `[OBJECTIVE: Engage meteoric entity in direct physical clash testing endurance]`

```text
+==============================================+
| TACTICAL DOSSIER: COMBAT WORK (SE-055)       |
| ENTITY CODE : SE-C-IIIβ-055 (THE IRON STATUE)|
| CLASSIFICATION : CLASS III (HE-TIER) METEORIC|
| CHAMBER LOCATION : FLOOR 5 SECTOR B          |
| BEHAVIORAL PARAMETERS:                       |
| - High physical armor; crushing downward fist|
| - Retaliates violently against weak attacks  |
| - Requires strict kinetic dampening clamps   |
| TACTICAL DISPATCH: AGENT BAE & AGENT HWANG   |
+==============================================+
```

Agent Bae enters the containment chamber, wielding the heavy *Bulwark Maul*. The air inside Chamber 055 smells of scorched metallic ozone. At Node 1, the colossal iron idol rises from its stone pedestal, curling its massive pneumatic fist!

Director Majin establishes the 10-node chamber grid:

```text
{box_statue_hud}
```

###### Turn 01 Action Resolution Log (Chamber 055)
- **Step 1: Floor 2 Echo-Core Resonance (Dekan)**:
  * Dekan's *Bastion Ward* reinforces Agent Bae's armor plating, granting +40% kinetic damage absorption.
- **Step 2: Movement & Action Point Spending**:
  * Agent Bae (Speed 6 -> 3 AP) advances to Node 2 (Point-Blank Range Band 1).
  * Bae spends 2 AP to declare `[Pugnahan Kinetic Suppression Strike]`.
  * Agent Hwang (Speed 5 -> 3 AP) holds Node 4 behind the acoustic baffle, spending 2 AP to operate the `[Acoustic Resonance Clamping Console]`.
- **Step 3: Clash Standoff (Node 2)**:
  * The Iron Statue declares `[Meteorite Heavy Fist]` (Base 9 + 2 Coins = 13 Power).
  * Agent Bae's `[Pugnahan Suppression Strike]` (Base 10 + 2 Coins = 15 Power).
  * **Resolution**: Bae WINS THE CLASH (15 vs 13).
    * Bae's maul collides directly with the descending iron knuckles. The kinetic shockwave rings like a cathedral bell, canceling the statue's strike and inflicting +22 Stagger buildup!
  * Hwang triggers the acoustic clamps, sapping the entity's kinetic momentum and reducing its Sorrow Gauge by 20%.

```text
{box_statue_turns}
```

```text
{box_statue_phase}
```

- Work concludes with **10/10 Positive Han crystals extracted!** Energy counter hits `0.165 / 0.170 tons`."""

if target_statue_start in text and target_statue_end in text:
    idx1 = text.find(target_statue_start)
    idx2 = text.find(target_statue_end) + len(target_statue_end)
    text = text[:idx1] + new_statue_full + text[idx2:]
    print("Replaced SE-055 Statue section with full GBS!")
else:
    print("Could not find SE-055 Statue section!")

# -------------------------------------------------------------
# 4. The Churning Hive (Amber Dusk)
# -------------------------------------------------------------
box_hive_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (AMBER DUSK ORDEAL)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [HIVE-MAW]    [MELLDA][BAE]           [KANG]         [MAJIN]",
    "DIST    : Mellda at N03 (Band 1); Bae at N04 (Band 2); Kang at N06.",
    "---",
    "Border Lead Mellda: Speed 5 -> 3 AP | HP: 190/190 | SP: +30 | Threshold Vow",
    "Agent Bae         : Speed 6 -> 3 AP | HP: 135/135 | SP: +25 | Bulwark Maul",
    "Agent Kang        : Speed 6 -> 3 AP | HP: 125/125 | SP: +25 | Fury Greatsword",
    "The Churning Hive : Speed 4 -> 2 AP | HP: 360/360 | Sorrow: 65% | Sub-Maw"
])

box_hive_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Mellda anchors Gate 5; Bae smashes jaw; Hive hits 60% Stagger 1.",
    "- Turn 03: Posture broken; all attacks deal 2.0x direct damage; HP at 140.",
    "- Turn 04: Hive attempts deep burrow; Dekan activates Jaw Clamp pin.",
    "- Turn 05: Kang delivers Fury Cleave, severing primary mandibles at N02.",
    "- Turn 06: Mellda executes Threshold Execution; Terminal Stagger shatters Hive."
])

box_hive_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Sector 5 floorplates sealed and secured.",
    "2. Status Equilibrium : Tectonic vibrations cease; team SP at +35.",
    "3. Containment Check   : The Churning Hive collapsed into dry amber husk.",
    "4. OUTCOME             : ZERO CASUALTIES — +28 REFINED RHR SECURED."
])

target_hive_start = "##### Ordeal Manifestation: Amber Dusk Ordeal — The Churning Hive"
target_hive_end = "- Hive collapses into dry amber dust! **Zero agent casualties!** +28 RHR secured."

new_hive_full = f"""##### Ordeal Manifestation: Amber Dusk Ordeal — The Churning Hive
At 0.165 tons collected, the subterranean bedrock shudders. Colossal segmented centipedes burst through the flagstones of Floor 5 and Floor 6:

```text
+==============================================+
| TACTICAL DOSSIER: AMBER DUSK ORDEAL          |
| DESIGNATION : THE CHURNING HIVE              |
| CLASSIFICATION : AMBER (WEIGHT/GRUDGE) DUSK  |
| INTRUSION POINT : FLOOR 5 GATEWAY SLUICE     |
| HOSTILE PARAMETERS:                          |
| - Entity: 1x Colossal Segmented Burrower     |
| - Attack Affinity: Crushing Weight Shock     |
| - Weakness Affinity: Physical Slash / Cleave |
| TACTICAL DEPLOYMENT: MELLDA, BAE & KANG      |
+==============================================+
```

A massive, armored subterranean centipede erupts through the reinforced masonry at Node 1, gnashing four pairs of serrated diamond mandibles!

Director Majin establishes GBS tactical positioning:

```text
{box_hive_hud}
```

###### Turn 01 Action Resolution Log (Floor 5 Gateway Sluice)
- **Step 1: Floor 5 Echo-Core Resonance (Border Lead Mellda)**:
  * Mellda engages *Blast Gate Lockdown*, dropping heavy steel portcullises at Node 4 to isolate Nodes 1–3 and trap the beast in the gateway vestibule.
- **Step 2: Movement & Action Point Spending**:
  * Border Lead Mellda (Speed 5 -> 3 AP) stands firm at Node 3 (Range Band 1). Spends 2 AP to prepare `[Threshold Vow Bulwark Stance]`.
  * Agent Bae (Speed 6 -> 3 AP) steps up to Node 3 beside Mellda, spending 2 AP to ready `[Bulwark Maul Impact Strike]`. Remaining 1 AP in Guard.
  * Agent Kang (Speed 6 -> 3 AP) holds Node 6 with his two-handed greatsword, spending 1 AP to sprint to Node 4 and 2 AP to wind up `[Fury Cleave]`.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * The Churning Hive declares `[Tectonic Mandible Crush]` on Node 3 (Base 9 + 2 Coins = 13 Power).
  * Mellda's `[Threshold Vow Bulwark Stance]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Mellda WINS THE CLASH (15 vs 13).
    * Mellda's golden arm-blade locks the centipede's primary mandibles. The jarring counter-force reverberates through the beast's chitinous segments, dealing 36 Grudge damage and inflicting +24 Stagger!
  * Agent Bae slams his maul into the exposed ventral plate, dealing 34 Weight damage.

```text
{box_hive_turns}
```

```text
{box_hive_phase}
```

- Hive collapses into dry amber dust! **Zero agent casualties!** +28 RHR secured."""

if target_hive_start in text and target_hive_end in text:
    idx1 = text.find(target_hive_start)
    idx2 = text.find(target_hive_end) + len(target_hive_end)
    text = text[:idx1] + new_hive_full + text[idx2:]
    print("Replaced Churning Hive section with full GBS!")
else:
    print("Could not find Churning Hive section!")

check_banned(text, filepath)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
print(f"Updated {filepath} with all expanded GBS battles!")
