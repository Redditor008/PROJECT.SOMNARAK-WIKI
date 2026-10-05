#!/usr/bin/env python3
"""
tools/generate_scenario_05.py
Generates GAME_BATTLE/SCENARIO_05_HORIZON_CARAVAN_LEVIATHAN_SIEGE.md with 100% strict 71-column ASCII text box symmetry.
Uses wrap_box for every single text box to guarantee exact mathematical alignment.
"""

from box_formatter import make_box

def wrap_box(title, rows, width=71):
    box = make_box(title, rows, width)
    return "```text\n" + box + "\n```\n\n"

def build_scenario():
    content = []
    
    # Title Header
    content.append("# SCENARIO 05 — The Horizon Caravan: Leviathan Siege on the Glass Sands\n")
    content.append("## Tactical Engagement Record: Defense of the Drift Throne & Subjugation of the Glass Burrower\n")
    content.append("### Canonical Tactical Scenario — SOP-GB-SCENARIO-005\n\n")
    
    # Header Box
    b0 = wrap_box("TACTICAL ENGAGEMENT RECORD: BATTLE-005-LEVIATHAN-SIEGE", [
        "OPERATIONAL CAMPAIGN: The Horizon Caravan (Arc 2: Sea of Glass)",
        "DEPLOYING FLAGSHIP  : The Drift Throne (142.5m Mobile Heavy Cruiser)",
        "THEATER LOCATION    : Waystations 04-07 (The Vitrified Expanse, Km 720)",
        "TARGET ADVERSARY    : The Titanic Glass Burrower (SECC-088 Leviathan)",
        "COMMAND CADRE       : Commander Kael, Wright Gwan, Hwaran, Sora",
        "PRIMARY OBJECTIVE   : Mandible Rupture, Meltdown, & Crawler Defense"
    ])
    content.append(b0)
    
    content.append("""---

## 1. Tactical Overview & Operational Parameters

- **Topological Coordinate:** The Sea of Vitrified Glass, Overland Waystation 05 Transit Trench (Kilometer 720).
- **Ambient Han Saturation:** 40% Desolate Sorrow Dust (Microscopic volcanic glass storm at 55°C).
- **Environmental Hazard Modifiers:**
  * **Singing Glass Sandstorm:** High-velocity volcanic glass particles deal 10 kinetic abrasive strain per turn to unshielded units on Nodes `[N05]` to `[N10]`.
  * **Drift Cruiser Speed Advantage:** While the Drift Throne maintains crawler momentum, allied units gain +1 Speed Band when moving toward the rear hull nodes (`[N01]` to `[N04]`).
  * **Trench Collapse Risk:** If the Leviathan breaches past Node `[N04]`, crawler starboard tracks suffer critical damage, reducing caravan transit speed by 50%.
- **Mission Briefing:**
  While traversing the shimmering expanse of the Sea of Vitrified Glass, the 142.5-meter mobile flagship *The Drift Throne* intercepted seismic pulses from an apex subterranean megafauna: **The Titanic Glass Burrower (SECC-088)**. Attracted by the crawler's engine harmonics, the 60-meter leviathan breached the dunes directly off the starboard beam. Supreme Commander Kael and Master Wright Gwan have scrambled the starboard defense crew. The crew must sever the creature's crushing vitreous mandibles, crack its heat-baked basalt carapace, and induce a Composure Meltdown to hook the beast onto the industrial recovery sleds before it shears through the starboard crawler bogies.

---

## 2. Combatant Rosters & Technical Profiles

### 2.1 Allied Horizon Caravan Starboard Defense Crew

| Operative Callsign | Role | Base Spd | Max HP | Composure | Posture | Equipped M.A.W. Set | Range Band |
|---|---|---|---|---|---|---|---|
| **Commander Kael** | Drift Vanguard | 5 | 220 | 110 | 140 | The Sovereign Cleaver (Gr 4) | Band 1 (Melee) |
| **Master Wright Gwan**| Engine Breaker | 3 | 195 | 100 | 155 | Heavy Hydraulic Piston Maul | Band 1-2 (Mid) |
| **Gunner Hwaran** | Ballista Artillery| 4 | 140 | 105 | 90 | Pneumatic Starboard Harpoon | Band 3-4 (Long) |
| **Ley-Seer Sora** | Sonar Navigator | 5 | 120 | 125 | 80 | Chim-Mok Acoustic Siphon | Band 4 (Long) |

### 2.2 Hostile Entity: The Titanic Glass Burrower (`SECC-088`)
- **Coherence Rank & Potency:** Rank V Sovereign (Wilderness Megafauna) • Grade Delta Potency
- **Total Composure Pool:** 360 Points • Meltdown Threshold: 0 Points
- **Base Speed:** 4 (Generates 4 Action Points per turn)
- **Modular Body Part Anatomy:**

| Modular Part Name | Part Max HP | Rupture Threshold (60%) | Lament Def | Grudge Def | Void Def | Weight Def |
|---|---|---|---|---|---|---|
| **Vitreous Mandibles** | 1,400 HP | 840 HP | 0.5x | 1.2x | 0.8x | 2.0x (Fatal)|
| **Vitrified Carapace** | 1,800 HP | 1,080 HP | 0.5x | 1.0x | 0.5x | 1.5x |
| **Siphon Resonance Heart**| 2,200 HP | 1,320 HP | 1.4x | 1.5x | 2.0x (Fatal)| 1.0x |

- **Hostile Intention Deck:**
  * **Vitreous Shearing Snap:** 2 AP • Range Band 1-2 • Weight • Base 24. Deals 45 crushing damage and destroys tactical cover.
  * **Singing Dune Breath:** 1 AP • Range Band 1-4 Area • Void • Base 18. Bathes nodes in supersonic glass dust; drains 25 Composure.
  * **Subterranean Trench Dive:** 2 AP • Range Band 1-5 • Kinetic • Base 26. Dives into the glass sand and breaches under target node.

---

## 3. Initial 10-Node Grid Topography Map

""")

    # Grid Topography Box
    b_grid = wrap_box("INITIAL 10-NODE GRID TOPOGRAPHY — STARBOARD APRON", [
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]    ",
        "[SORA]  [HWARAN] [GWAN]   [KAEL]  [SKIRT] [DUNE]  [LEVIATHAN BODY][SAND]",
        "Bridge Deck [N01-02] | Catwalk [N03-05] | Dunes [N06-08] | Deep Sea [N09-10]"
    ])
    content.append(b_grid)

    content.append("""- **Allied Starting Coordinates:** Ley-Seer Sora at `[N01]`, Gunner Hwaran at `[N02]`, Wright Gwan at `[N03]`, Commander Kael at `[N04]`.
- **Destructible Tactical Cover:** Heavy Ballast Skirting located at `[N05]` (absorbs 180 kinetic impact before shearing).
- **Terrain Elevation:** Singing Dune Crest Ridge located at `[N06]`.
- **Target Position:** The Titanic Glass Burrower occupies Nodes `[N07]` and `[N08]`.
- **Subterranean Trench:** Nodes `[N09]` and `[N10]` descend into the open, vitrified glass sea.

---

## 4. Turn-by-Turn Operational Chronicle

### Battle Turn 01: Dune Emergence & Heavy Ballista Harpoon

#### 1. Initiative & Action Point Allocation
- **Commander Kael:** Rolled Speed 6 -> 4 Action Points (AP).
- **Master Wright Gwan:** Rolled Speed 3 -> 2 Action Points (AP).
- **Gunner Hwaran:** Rolled Speed 4 -> 3 Action Points (AP).
- **Ley-Seer Sora:** Rolled Speed 5 -> 4 Action Points (AP).
- **The Glass Burrower:** Rolled Speed 4 -> 4 Action Points (AP) (Queues *Vitreous Shearing Snap* targeting `[N04]`).

#### 2. Node Maneuvers & Tactical Positioning
- Commander Kael advances from `[N04]` to `[N05]`, taking position behind the crawler's heavy ballast skirting (1 AP spent, 3 AP remaining).
- Wright Gwan advances from `[N03]` to `[N04]`, readying the pneumatic torque winch (1 AP spent, 1 AP remaining).
- Gunner Hwaran elevates the starboard pneumatic harpoon ballista at `[N02]`.
- Ley-Seer Sora monitors acoustic pulse telemetry from `[N01]`.

#### 3. Clash & Parry Resolutions
- **Clash 01 (Kael vs Vitreous Shearing Snap):**
  * Kael queues *The Drift King's Aegis* (2 AP).
  * Kael Roll: Speed 6 + Blade Deflect Power 21 = 27.
  * Burrower Roll: Speed 4 + Snap Attack Power 22 = 26.
  * Result: **Kael Deflects (Margin +1)**. Kael's massive two-handed cleaver wedges between the snapping mandibles, sparking blinding vitrified flint sparks. The blow is diverted away from the track skirts. Beast suffers 6 Posture strain.

#### 4. Modular Part Damage & Composure Tracking
- Gunner Hwaran fires a high-tensile steel harpoon from `[N02]` targeting the Vitreous Mandibles at `[N07]` (Distance = 5, Band 4 valid):
  * Base Damage: 80 * Weight Multiplier (2.0x Fatal!) = 160 Massive Damage!
  * Vitreous Mandibles HP: 1,400 -> 1,240 / 1,400 (Rupture Threshold: 840 HP).
  * Cable Anchor Attached: Leviathan is physically tethered to the Drift Throne's starboard winch!
- Ley-Seer Sora channels an acoustic sensor scan:
  * Reveals acoustic vibration stress in the left mandible hinge.
- Burrower Composure: 360 / 360. Posture: 94 / 100.

---

### Battle Turn 02: Mandible Thrash & Pneumatic Winch Tension

#### 1. Initiative & Action Point Allocation
- **Commander Kael:** Rolled Speed 5 -> 4 AP.
- **Master Wright Gwan:** Rolled Speed 4 -> 3 AP.
- **Gunner Hwaran:** Rolled Speed 5 -> 4 AP.
- **Ley-Seer Sora:** Rolled Speed 5 -> 4 AP.
- **The Glass Burrower:** Rolled Speed 4 -> 4 AP (Queues *Singing Dune Breath* across Nodes 03-06 and *Subterranean Trench Dive*).

#### 2. Node Maneuvers & Hazard Crisis
- The Leviathan thrashes violently against the attached harpoon cable, attempting to dive beneath the sand at `[N08]`!
- Wright Gwan expends 2 AP to lock the hydraulic winch drums at `[N04]`, holding the beast at the surface through sheer steam-driven torque.
- Kael holds at `[N05]`, bracing against the incoming supersonic glass breath.
- Hwaran loads a barbed pneumatic canister at `[N02]`.

#### 3. Clash & Armor Damage
- **Clash 02 (Gwan Torque Lock vs Trench Dive):**
  * Gwan Roll: Speed 4 + Winch Power 24 = 28.
  * Burrower Roll: Speed 4 + Dive Power 24 = 28.
  * Result: **Stalemate!** The cable groans under 400 tons of tension; the beast is halted from submerging, remaining trapped at Node `[N07]`.
- **Targeted Mandible Assault:**
  * Kael executes *Sovereign Cleaver Sunder* (2 AP) against the left mandible hinge:
    - Base Damage: 95 * Weight (2.0x Fatal!) = 190 Damage!
  * Hwaran fires secondary explosive harpoon (2 AP):
    - Base Damage: 85 * Weight (2.0x Fatal!) = 170 Damage!
  * Vitreous Mandibles HP: 1,240 -> 880 / 1,400 (Rupture Threshold: 840 HP).

#### 4. Posture & Composure Tracking
- Singing dune breath grazes Kael and Gwan, dealing 15 abrasion damage (Kael HP: 220 -> 205; Gwan HP: 195 -> 180).
- Burrower Composure: 360 -> 310 / 360. Posture: 94 -> 58 / 100.

---

### Battle Turn 03: Part Rupture Threshold Breach (Mandibles Shattered)

#### 1. Initiative & Action Point Allocation
- **Commander Kael:** Rolled Speed 6 -> 4 AP.
- **Master Wright Gwan:** Rolled Speed 4 -> 3 AP.
- **Gunner Hwaran:** Rolled Speed 5 -> 4 AP.
- **Ley-Seer Sora:** Rolled Speed 6 -> 4 AP.
- **The Glass Burrower:** Rolled Speed 3 -> 3 AP (Queues *Vitreous Shearing Snap*).

#### 2. Synchronized Heavy Kinetic Strike
- Master Wright Gwan surges forward to Node `[N05]`, activating the pneumatic pile-bunker on his industrial maul (2 AP):
  * Target: Left Vitreous Mandible at `[N07]`.
  * Base Damage: 110 * Weight Multiplier (2.0x) = 220 Massive Kinetic Damage!
  * Vitreous Mandibles HP: 880 -> 660 / 1,400 -> **RUPTURE THRESHOLD (840 HP) SHATTERED!**

#### 3. Part Rupture Trigger & Effect
- **PART RUPTURE CONFIRMED:** The leviathan's left vitreous mandible shatters into a thousand crystalline fragments with a deafening sonic crack!
- **Mechanical Penalties Inflicted on Megafauna:**
  * All Vitreous Shearing Snap attacks permanently disabled!
  * Queued snap attack cancelled!
  * Beast suffers **Tactical Stagger**; all incoming damage multiplied by **1.5x** for 1 turn!
  * Posture collapses to 10 / 100; Composure drops: 310 -> 210 / 360.

---

### Battle Turn 04: Tactical Stagger Exploitation & Carapace Shattered

#### 1. Initiative & Action Point Allocation
- **Commander Kael:** Rolled Speed 6 -> 4 AP.
- **Master Wright Gwan:** Rolled Speed 4 -> 3 AP.
- **Gunner Hwaran:** Rolled Speed 5 -> 4 AP.
- **Ley-Seer Sora:** Rolled Speed 6 -> 4 AP.
- **The Glass Burrower:** Staggered! (0 AP, Defense dice disabled).

#### 2. Concentrated Assault on Vitrified Carapace
- With the leviathan paralyzed on the dune ridge at `[N07]`, the crew unleashes full offensive firepower:
- **Commander Kael (Node 05):** Spends 3 AP on *Sand-Cleaver Execution*:
  * Base Damage: 125 * Weight (1.5x) * Stagger Multiplier (1.5x) = 281 Damage!
  * Vitrified Carapace HP: 1,800 -> 1,519 / 1,800.
- **Master Wright Gwan (Node 05):** Drives heavy pile-bunker into the central dorsal plate (2 AP):
  * Base Damage: 100 * Weight (1.5x) * Stagger (1.5x) = 225 Damage!
  * Vitrified Carapace HP: 1,519 -> 1,294 / 1,800.
- **Gunner Hwaran (Node 02):** Fires dual armor-cracking kinetic spikes (3 AP):
  * Base Damage: 115 * Weight (1.5x) * Stagger (1.5x) = 258 Damage!
  * Vitrified Carapace HP: 1,294 -> 1,036 / 1,800 -> **CARAPACE RUPTURED (Threshold: 1,080 HP)!**
- The thick glass armor plates shatter, exposing the pulsing, deep-violet **Siphon Resonance Heart** beneath!
- Burrower Composure: 210 -> 110 / 360.

---

### Battle Turn 05: Siphon Resonance Heart Meltdown (Terminal Collapse)

#### 1. Initiative & Action Point Allocation
- **Commander Kael:** Rolled Speed 5 -> 4 AP.
- **Master Wright Gwan:** Rolled Speed 4 -> 3 AP.
- **Gunner Hwaran:** Rolled Speed 5 -> 4 AP.
- **Ley-Seer Sora:** Rolled Speed 6 -> 4 AP.
- **The Glass Burrower:** Recovers from Stagger, rolls Speed 2 -> 2 AP (Fires desperate *Singing Dune Breath*).

#### 2. The Final Acoustic Resonance Shock
- Kael steps forward with his heavy basalt surcoat, shielding Gwan from the supersonic glass spray.
- Ley-Seer Sora taps into the embedded steel harpoon cables, using them as massive conductive acoustic conduits (3 AP):
  * Sora channels *Ley-Line Inversion Pulse* directly into the pulsing Siphon Heart:
  * Void Resonance Multiplier: **2.0x Fatal!**
  * Siphon Heart Damage: 120 * 2.0x = 240 True Void Damage!
  * Siphon Heart HP: 2,200 -> 1,960 / 2,200.
  * Direct Composure Drain: -140 Composure Points!
  * **COMPOSURE POOL HIT: 110 - 140 = 0 POINTS!**

#### 3. Terminal Meltdown Trigger
- **TERMINAL MELTDOWN ACTIVE:** The Titanic Glass Burrower lets out a mournful, bell-like chord that echoes across fifty kilometers of dunes.
- The creature's inner resonance collapses; its massive body goes completely limp across Nodes `[N07-08]`.
- All defenses collapse to **2.0x Fatal vulnerability**!

---

### Battle Turn 06: Synchronized Winch Haul & Caravan Triumph

#### 1. Beast Subjugation & Recovery Operation
- **Master Wright Gwan & Gunner Hwaran:** Engage the flagship's twin 500-horsepower steam winches:
  * Four additional heavy steel hawser cables are fired through the creature's dorsal ridges, anchoring its 60-meter bulk to the crawler's reinforced recovery sled.
- **Commander Kael (Node 05):** Signals the engine room to resume full forward crawl:
  * The Drift Throne surges forward through the singing dunes, dragging the subdued leviathan onto the traveling processing gantry.
- **Ley-Seer Sora:** Verifies surrounding seismic sensors: no other megafauna are in pursuit. The crossing across the Sea of Vitrified Glass proceeds without further delay.

---

## 5. Macro Phase-End Resolution Block (Phase 01 Complete)

""")

    # Phase-End Box
    b_phase = wrap_box("MACRO PHASE-END RESOLUTION SUMMARY — BATTLE 05", [
        "COMPLETED PHASE  : Combat Phase 01 (Battle Turns 01 to 06)",
        "BEAST STATUS     : Mandibles Shattered (660 HP) • Carapace Shattered",
        "SIPHON HEART     : Subdued & Resonant-Locked (1,960 / 2,200 HP)",
        "COMPOSURE POOL   : 0 / 360 (Terminal Meltdown Confirmed)",
        "FLAGSHIP INTEGRITY: Drift Throne Hull 100% • Starboard Skirt Minor Abrasion",
        "SQUAD CASUALTIES : 0 Fatalities • Kael (15 HP) • Gwan (15 HP Abrasion)"
    ])
    content.append(b_phase)

    content.append("""---

## 6. After-Action Report & Expedition Manifest

""")

    # After-Action Box
    b_aar = wrap_box("AFTER-ACTION TACTICAL REPORT & EXPEDITION MANIFEST", [
        "ENGAGEMENT RESULT: Decisive Overland Victory • Megafauna Subdued",
        "FLAGSHIP STATUS  : Transit Resumed at 22 Knots • Starboard Apron Intact",
        "SPECIMEN HARVEST : 8.5 Tons Vitrified Chitin • 1,200 Liters Sorrow Oil",
        "M.A.W. EXTRACTION: 1x Grade-Delta Leviathan Core (SECC-088 Chitin)",
        "EXPEDITION ORDER : Caravan cleared for Waystation 06 Approach",
        "TACTICAL CITATION: Master Wright Gwan & Gunner Hwaran for Cable Lock"
    ])
    content.append(b_aar)

    content.append("""---
*End of Canonical Tactical Scenario SOP-GB-SCENARIO-005.*
""")
    
    return "".join(content)

if __name__ == "__main__":
    scenario_text = build_scenario()
    target_path = "GAME_BATTLE/SCENARIO_05_HORIZON_CARAVAN_LEVIATHAN_SIEGE.md"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(scenario_text)
    print(f"Successfully wrote {len(scenario_text)} bytes to {target_path}")
