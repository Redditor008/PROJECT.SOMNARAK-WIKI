#!/usr/bin/env python3
"""
tools/expand_absolvohan_battles_part4.py
Expands all 5 Ordeal encounters in SOMNARAK-WORLD/The_Absolvohan/Part_4_Days_53_to_73.md
with full Gameplay Battle System (GBS) Reverie Directorate Style mechanics:
1. Green Dusk Ordeal — The Siphon Spires
2. Crimson Dusk Ordeal — The Blood-Tide Shrouds
3. Amber Dusk Ordeal — The Tremor Spiders
4. Violet Dusk Ordeal — The Floating Spires
5. The Midnight Herald — Sovereign Echo of the Deep Vaults
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

filepath = "SOMNARAK-WORLD/The_Absolvohan/Part_4_Days_53_to_73.md"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# -------------------------------------------------------------
# 1. Green Dusk Ordeal — The Siphon Spires
# -------------------------------------------------------------
box_spires_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (GREEN DUSK)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [SPIRE-A]     [PARK]  [KIM]           [HWANG]        [DEKAN]",
    "DIST    : Park at N03 (Band 1); Kim at N04 (Band 2); Hwang at N06.",
    "---",
    "Agent Park        : Speed 6 -> 3 AP | HP: 130/130 | SP: +30 | Judgment Maul",
    "Agent Kim         : Speed 5 -> 3 AP | HP: 120/120 | SP: +25 | Kinetic Carbine",
    "Agent Hwang       : Speed 6 -> 3 AP | HP: 125/125 | SP: +30 | Observing Bow",
    "Siphon Spire (x2) : Speed 4 -> 2 AP | HP: 360 each | Energy Drain"
])

box_spires_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Park smashes Spire-A base; Kim covers flank; Spire 60% Stagger 1.",
    "- Turn 03: Posture broken; direct Grudge damage deals 2.0x; Spire-A shattered.",
    "- Turn 04: Spire-B spawns scuttlers; Hwang uses 2 AP for suppressing arrow.",
    "- Turn 05: Dekan activates Jaw Clamp, pinning scuttlers at Node 2.",
    "- Turn 06: Park & Kim coordinate Climax Smash; Spire-B collapses to slag."
])

box_spires_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Escapement energy feedback vents without damage.",
    "2. Status Equilibrium : Facility quota preserved; team SP stabilizes at +35.",
    "3. Containment Check   : Both Siphon Spires reduced to pulverized brass.",
    "4. OUTCOME             : ZERO CELL BREACHES — +26 REFINED RHR SECURED."
])

old_spires = """Squad Alpha (Park & Kim) hammers the Floor 2 Spire with *Judgment Maul* strikes, smashing the central escapement in 20 seconds. Squad Beta (Hwang & Song) snipes the Floor 4 Spire with Void and Lament rounds, preventing a single scuttler from reaching containment cells! +26 RHR reagents collected!"""

new_spires = f"""Director Majin establishes split-squad GBS tactical coordinates:
- **Squad Alpha (Park & Kim)** suppresses the Floor 2 Spire at Point-Blank range.
- **Squad Beta (Hwang & Song)** locks down the Floor 4 Spire with long-range fire.

```text
{box_spires_hud}
```

###### Turn 01 Action Resolution Log (Floor 2 Main Vestibule)
- **Step 1: Floor 2 Echo-Core Resonance (Dekan)**:
  * Dekan deploys *The Maw's Keep Bastion Ward*, shielding Nodes 1 to 4 with +50% kinetic armor against escaping gear teeth.
- **Step 2: Movement & Action Point Spending**:
  * Agent Park (Speed 6 -> 3 AP) spends 1 AP to advance from Node 4 to Node 3 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Judgment Maul Escapement Crusher]`.
  * Agent Kim (Speed 5 -> 3 AP) positions at Node 4 (Range Band 2). Spends 2 AP to ready concentrated carbine suppressive fire. Remaining 1 AP held in Guard.
  * Agent Hwang (Speed 6 -> 3 AP) operates from Node 6 (Range Band 3), aiming an armor-piercing Void arrow at the spire's energy conduit.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * Siphon Spire A attempts `[High-Torque Escapement Sweep]` (Base 8 + 2 Coins = 12 Power).
  * Agent Park's `[Judgment Maul Escapement Crusher]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Park WINS THE CLASH (15 vs 12).
    * Park's heavy maul shatters the main clockwork axle, halting energy siphonage and dealing **46 Grudge damage** with +28 Stagger!
  * Hwang and Kim fire coordinated bursts from Nodes 4 and 6, cutting down emerging gear scuttlers.

```text
{box_spires_turns}
```

```text
{box_spires_phase}
```

Squad Beta executes synchronized suppression on Floor 4, preventing a single scuttler from reaching containment cells! +26 RHR reagents collected!"""

if old_spires in text:
    text = text.replace(old_spires, new_spires)
    print("Replaced Siphon Spires section successfully!")
else:
    print("Could not find Siphon Spires section!")

# -------------------------------------------------------------
# 2. Crimson Dusk Ordeal — The Blood-Tide Shrouds
# -------------------------------------------------------------
box_shrouds_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (CRIMSON DUSK)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [SHROUD-A]    [ISHALL][PARK]          [SONG]         [MAJIN]",
    "DIST    : Ishall at N02 (Band 1); Park at N03 (Band 2); Song at N06.",
    "---",
    "Shadow Lead Ishall: Speed 7 -> 4 AP | HP: 190/190 | SP: +35 | Unanswered Talon",
    "Agent Park        : Speed 6 -> 3 AP | HP: 135/135 | SP: +30 | Judgment Scale",
    "Agent Song        : Speed 5 -> 3 AP | HP: 115/115 | SP: +25 | Cherub Bow",
    "Blood-Tide Shroud : Speed 5 -> 3 AP | HP: 380 each | Crimson Lash"
])

box_shrouds_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Ishall teleports to N01 rear; Park tanks lash; Shroud 60% Stagger 1.",
    "- Turn 03: Posture broken; all allied attacks deal 2.0x direct damage; HP at 140.",
    "- Turn 04: Shroud charges [Sanguine Deluge]; Song fires piercing bolt.",
    "- Turn 05: Ishall executes Void Talons, dissecting shroud mantle from behind.",
    "- Turn 06: Park unleashes Judgment Climax; Terminal Stagger dissolves shroud."
])

box_shrouds_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Crimson seepage drained by subterranean pumps.",
    "2. Status Equilibrium : Bleed counters expire; team SP rises to +35.",
    "3. Containment Check   : All three Shrouds dissolved into inert mist.",
    "4. OUTCOME             : ZERO AGENT CASUALTIES, +28 REFINED RHR SECURED."
])

old_shrouds = """Ishall and Agent Park engage the central shroud in close combat, absorbing the physical Grudge lashes with *Judgment Scale* armor. Agent Song snipes from the rear with *Cherub's Bow*, shattering the spectral weave in 24 seconds! +28 RHR reagents collected!"""

new_shrouds = f"""Director Majin establishes GBS tactical deployment at Floor 7's outer bulkhead:

```text
{box_shrouds_hud}
```

###### Turn 01 Action Resolution Log (Floor 7 Outer Wall)
- **Step 1: Floor 7 Echo-Core Resonance (Shadow Lead Ishall)**:
  * Ishall activates *Shadow Ingress*, allowing rapid phase-shifting between Node 8 and Node 2 without provoking opportunity attacks.
  * Majin deploys `Veil Mist Dampener`, reducing Crimson bleed splatter by 40%.
- **Step 2: Movement & Action Point Spending**:
  * Shadow Lead Ishall (Speed 7 -> 4 AP) spends 1 AP to shift directly to Node 2 behind Shroud Alpha. Spends 2 AP to declare `[Unanswered Talon Void Dissection]`. Remaining 1 AP held in Evade.
  * Agent Park (Speed 6 -> 3 AP) anchors Node 3 in Point-Blank Range Band 1. Spends 2 AP to brace *Judgment Scale* in a kinetic absorb stance.
  * Agent Song (Speed 5 -> 3 AP) positions at Node 6 (Range Band 3). Spends 2 AP to ready `[Cherub's Bow Resonant Arrow]`.
- **Step 3: Clash Resolution (Node 1 to 2)**:
  * Blood-Tide Shroud declares `[Sanguine Lash Volley]` (Base 9 + 2 Coins = 13 Power).
  * Shadow Lead Ishall's `[Unanswered Talon]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Ishall WINS THE CLASH (15 vs 13).
    * Ishall's floating relic digits slice cleanly through the shroud's ectoplasmic core, dealing **44 Void damage** and inflicting +26 Stagger!
  * Park absorbs the deflected crimson spray behind *Judgment Scale*, suffering 0 damage.
  * Song releases a resonant arrow from Node 6, tearing open the shroud's spectral mantle.

```text
{box_shrouds_turns}
```

```text
{box_shrouds_phase}
```

All three spectral weaves shatter in 24 seconds! Zero casualties, +28 RHR reagents collected!"""

if old_shrouds in text:
    text = text.replace(old_shrouds, new_shrouds)
    print("Replaced Blood-Tide Shrouds section successfully!")
else:
    print("Could not find Blood-Tide Shrouds section!")

# -------------------------------------------------------------
# 3. Amber Dusk Ordeal — The Tremor Spiders
# -------------------------------------------------------------
box_spiders_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (AMBER SPIDERS)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [ALPHA-SPIDER] [PARK]  [KIM]           [HWANG]        [MELLDA]",
    "DIST    : Park at N03 (Band 1); Kim at N04 (Band 2); Hwang at N06.",
    "---",
    "Agent Park          : Speed 6 -> 3 AP | HP: 135/135 | SP: +30 | Judgment Maul",
    "Agent Kim           : Speed 5 -> 3 AP | HP: 125/125 | SP: +25 | Kinetic Carbine",
    "Agent Hwang         : Speed 6 -> 3 AP | HP: 120/120 | SP: +25 | Wellspring Lens",
    "Alpha Tremor Spider : Speed 5 -> 3 AP | HP: 400/400 | Acid Web Shock"
])

box_spiders_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Park hammers thorax; Mellda locks Node 4; Spider 60% Stagger 1.",
    "- Turn 03: Posture broken; direct Weight/Void strikes deal 2.0x direct damage.",
    "- Turn 04: Alpha attempts tectonic web burst; Kim burns threads with carbine.",
    "- Turn 05: Hwang fires Wellspring beam into eye cluster; forces Terminal Stagger.",
    "- Turn 06: Park executes Climax Smite; Spider dissolves into amber crystals."
])

box_spiders_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Stairwell web snares dissolved and neutralized.",
    "2. Status Equilibrium : Acid pools drained; team SP stabilizes at +35.",
    "3. Containment Check   : Alpha and brood thoroughly eradicated.",
    "4. OUTCOME             : PERFECT SUPPRESSION — 22.0s CLEAR, +30 RHR."
])

old_spiders = """Park and Kim pin the alpha spider with crushing hammer blows while Hwang unleashes rapid Void piercing strikes from his *Wellspring Lens*. The alpha collapses in 22 seconds, dissolving into +30 RHR reagents!"""

new_spiders = f"""Director Majin establishes GBS tactical coordinates at Floor 5's stairwell:

```text
{box_spiders_hud}
```

###### Turn 01 Action Resolution Log (Floor 5 Main Stairwell)
- **Step 1: Floor 5 Echo-Core Resonance (Border Lead Mellda)**:
  * Mellda drops *The Bulwark Perimeter* across Node 4, preventing web lines from trapping the rear ranks.
- **Step 2: Movement & Action Point Spending**:
  * Agent Park (Speed 6 -> 3 AP) spends 1 AP to advance to Node 3 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Judgment Maul Thorax Impact]`.
  * Agent Kim (Speed 5 -> 3 AP) takes Node 4 (Range Band 2). Spends 2 AP to prepare incendiary carbine rounds to burn acid webs. Remaining 1 AP held in Guard.
  * Agent Hwang (Speed 6 -> 3 AP) stands at Node 6 (Range Band 3). Spends 2 AP to charge `[Wellspring Lens Void Lance]`.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * Alpha Tremor Spider strikes with `[Acid Mandible Pincer]` (Base 9 + 2 Coins = 13 Power).
  * Agent Park's `[Judgment Maul Thorax Impact]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Park WINS THE CLASH (15 vs 13).
    * Park's warhammer shatters the spider's front armored leg, driving it back to Node 1 and dealing **48 Weight damage** with +26 Stagger!
  * Hwang's Void lance strikes the spider's exposed carapace from Node 6 for 36 piercing damage.

```text
{box_spiders_turns}
```

```text
{box_spiders_phase}
```

The alpha collapses in 22 seconds, dissolving into +30 RHR reagents!"""

if old_spiders in text:
    text = text.replace(old_spiders, new_spiders)
    print("Replaced Tremor Spiders section successfully!")
else:
    print("Could not find Tremor Spiders section!")

# -------------------------------------------------------------
# 4. Violet Dusk Ordeal — The Floating Spires
# -------------------------------------------------------------
box_floating_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (FLOATING SPIRES)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [SPIRE-A]             [SONG]  [HWANG]         [KIM]  [AYSHUK]",
    "DIST    : Spire at N01; Song at N05 (Band 3); Hwang at N06; Kim at N08.",
    "---",
    "Agent Song          : Speed 6 -> 3 AP | HP: 120/120 | SP: +30 | Cherub Bow",
    "Agent Hwang         : Speed 6 -> 3 AP | HP: 125/125 | SP: +30 | Wellspring Lens",
    "Agent Kim           : Speed 5 -> 3 AP | HP: 125/125 | SP: +25 | Kinetic Carbine",
    "Levitating Spire(x3): Speed 4 -> 2 AP | HP: 350 each | Void Death-Ray"
])

box_floating_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Song & Hwang snipe Spire-A core; Ayshuk predicts firing angles.",
    "- Turn 03: Spire-A hits 60% Stagger 1; synchronized arrows shatter it to slag.",
    "- Turn 04: Spires B & C charge cross-floor beam; Kim activates stasis shield.",
    "- Turn 05: Hwang unleashes Overdrive Void Lance, fracturing Spire-B core.",
    "- Turn 06: Song executes Climax Volley; Spire-C disintegrates into ash."
])

box_floating_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Cross-floor laser channels clear and power down.",
    "2. Status Equilibrium : Clerk areas shielded; team SP rises to +35.",
    "3. Containment Check   : All three levitating monoliths eradicated.",
    "4. OUTCOME             : ZERO CASUALTIES — +32 REFINED RHR SECURED."
])

old_floating = """Agent Song and Agent Hwang form a sniper battery, firing synchronized Lament and Void piercing bolts from Range Band 3, shattering all three spires before a single clerk is harmed! +32 RHR reagents collected!"""

new_floating = f"""Director Majin establishes sniper battery coordinates across the central plaza:

```text
{box_floating_hud}
```

###### Turn 01 Action Resolution Log (Floor 4 Research Plaza)
- **Step 1: Floor 4 Echo-Core Resonance (Research Lead Ayshuk)**:
  * Ayshuk activates *The Predictive HUD*, projecting the spires' cross-floor laser firing arcs onto the agents' reticles and granting +3 Clash Power against ranged skills.
- **Step 2: Movement & Action Point Spending**:
  * Agent Song (Speed 6 -> 3 AP) anchors Node 5 (Range Band 3). Spends 2 AP to ready `[Cherub's Bow Synchronized Resonant Bolt]`. Remaining 1 AP held in Guard.
  * Agent Hwang (Speed 6 -> 3 AP) stands at Node 6 (Range Band 3). Spends 2 AP to charge `[Wellspring Lens Void Piercer]`.
  * Agent Kim (Speed 5 -> 3 AP) deploys at Node 8 (Range Band 4), spending 2 AP to prime suppressive stasis rounds.
- **Step 3: Clash Resolution (Node 1 to 5)**:
  * Levitating Spire A declares `[Corridor Annihilation Beam]` on Node 5 (Base 9 + 2 Coins = 13 Power).
  * Agent Song's `[Synchronized Resonant Bolt]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Song WINS THE CLASH (15 vs 13).
    * Song's acoustic arrow threads directly down the aperture of the charging death-ray, detonating inside the spire's core and dealing **46 Lament damage** with +28 Stagger!
  * Hwang follows with a precision Void beam, fracturing the spire's levitation gyros.

```text
{box_floating_turns}
```

```text
{box_floating_phase}
```

All three spires shatter before a single clerk is harmed! +32 RHR reagents collected!"""

if old_floating in text:
    text = text.replace(old_floating, new_floating)
    print("Replaced Floating Spires section successfully!")
else:
    print("Could not find Floating Spires section!")

# -------------------------------------------------------------
# 5. Sovereign Echo of the Deep Vaults (Midnight Herald)
# -------------------------------------------------------------
box_deep_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (DEEP VAULT ECHO)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [VAULT-ECHO]  [ISHALL][MELLDA][DEKAN]                 [MAJIN]",
    "DIST    : Ishall at N02; Mellda at N03; Dekan at N04 (Wall of Molybdenum).",
    "---",
    "Shadow Lead Ishall: Speed 7 -> 4 AP | HP: 195/195 | SP: +40 | Unanswered Void",
    "Border Lead Mellda: Speed 6 -> 3 AP | HP: 200/200 | SP: +40 | Threshold Vow",
    "Attendant Dekan   : Speed 5 -> 3 AP | HP: 210/210 | SP: +45 | Maw's Aegis",
    "Deep Vault Echo   : Speed 5 -> 3 AP | HP: 550/550 | Sorrow: 80% | Deep Pulse"
])

box_deep_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Mellda & Dekan absorb wave; Ishall attacks rear; Echo 60% Stagger 1.",
    "- Turn 03: Defense broken; direct multi-affinity strikes deal 2.0x direct damage.",
    "- Turn 04: Echo releases [Ancient Ballast Quake]; Dekan locks Jaw Clamp.",
    "- Turn 05: Ishall executes Unanswered Talon, severing the harmonic nexus.",
    "- Turn 06: Tri-Lead Climax Strike forces Terminal Stagger; Echo dissolves."
])

box_deep_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Deep Vault foundation locks withstand the harmonic toll.",
    "2. Status Equilibrium : Pale shockwave dissolves; team SP at full capacity.",
    "3. Containment Check   : Deep Vault Echo returned to inert subterranean salt.",
    "4. OUTCOME             : HISTORIC DEFENSE VICTORY — +35 REFINED RHR SECURED."
])

old_deep = """The three floor leads form an unbreakable wall of lead and molybdenum, absorbing the harmonic shockwave until it dissolves back into the deep salt flats! +35 RHR reagents secured!"""

new_deep = f"""The three floor leads form an unbreakable wall of lead and molybdenum across the 10-node boundary:

```text
{box_deep_hud}
```

###### Turn 01 Action Resolution Log (Perimeter Corridors)
- **Step 1: Floor 2 & 5 Echo-Core Resonances (Dekan & Mellda)**:
  * Dekan and Mellda unite their defensive fields, creating *The Bulwark of Molybdenum* across Nodes 2 to 4, absorbing +60% physical and pale trauma.
- **Step 2: Movement & Action Point Spending**:
  * Attendant Dekan (Speed 5 -> 3 AP) stands at Node 4, spending 2 AP to maintain *Maw's Aegis*.
  * Border Lead Mellda (Speed 6 -> 3 AP) locks Node 3 with *Threshold Vow*, spending 2 AP to brace for impact.
  * Shadow Lead Ishall (Speed 7 -> 4 AP) shifts to Node 2 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Unanswered Void Strike]`. Remaining 1 AP in Guard.
- **Step 3: Clash Resolution (Node 1 to 2)**:
  * Deep Vault Echo unloads `[Harmonic Shockwave of the Before-Time]` (Base 11 + 2 Coins = 15 Power).
  * Mellda & Dekan's `[Bulwark of Molybdenum]` (Base 12 + 2 Coins = 16 Power).
  * **Resolution**: The Floor Leads WIN THE CLASH (16 vs 15).
    * The golden and dark-steel shields hold fast against the pale tide. The kinetic backlash jars the Echo's dimensional matrix, dealing **48 Weight/Pale damage** with +30 Stagger!
  * Ishall's floating digits pierce the fracture line, unraveling its harmonic core.

```text
{box_deep_turns}
```

```text
{box_deep_phase}
```

The harmonic shockwave dissolves back into the deep salt flats! +35 RHR reagents secured!"""

if old_deep in text:
    text = text.replace(old_deep, new_deep)
    print("Replaced Deep Vault Echo section successfully!")
else:
    print("Could not find Deep Vault Echo section!")

check_banned(text, filepath)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
print(f"Updated {filepath} with all expanded GBS battles!")
