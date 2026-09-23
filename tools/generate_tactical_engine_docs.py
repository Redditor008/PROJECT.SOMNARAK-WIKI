#!/usr/bin/env python3
"""
Generate SOMNARAK-WORLD/Tactical_Combat_Engine/README.md and
SOMNARAK-WORLD/Tactical_Combat_Engine/WHAT_CAN_BE_DONE.md
with 100% text box symmetry (71 cols), zero HTML tags, and zero dollar signs.
"""

import os

def make_box(width, title, lines):
    inner_width = width - 4
    out = []
    top_border = "+" + "-" * (width - 2) + "+"
    out.append(top_border)
    if title:
        t_pad = title.center(inner_width)
        out.append(f"| {t_pad} |")
        out.append("+" + "-" * (width - 2) + "+")
    for l in lines:
        if len(l) > inner_width:
            raise ValueError(f"Line too long ({len(l)} > {inner_width}): {l}")
        l_pad = l.ljust(inner_width)
        out.append(f"| {l_pad} |")
    out.append("+" + "-" * (width - 2) + "+")
    return "```text\n" + "\n".join(out) + "\n```\n\n"

def build_engine_readme():
    box1 = make_box(71, "TACTICAL COMBAT ENGINE - SPATIAL GRID & RESOLUTION ARCHITECTURE", [
        "System Name       : Somnarak Grid Battle System (GBS Core Engine)",
        "Spatial Field     : 10-Node Linear Engagement Grid ([N01] to [N10])",
        "Action Economy    : Speed-Scaled Action Points (AP 2 to 5 per Turn)",
        "Engagement Bands  : Range Bands 1 through 5 (Point-Blank to Siege)",
        "Stagger Mechanics : Dual-Threshold (60% Part Rupture / 0% Meltdown)",
        "Combat Phases     : 6 Battle Turns = 1 Macro Environmental Phase",
        "Framework Standard: Four P-Framework (Passive, Panic, Parry, Poise)"
    ])

    box2 = make_box(71, "SPATIAL GRID NODE TOPOGRAPHY - 10-NODE ENGAGEMENT LINE", [
        "[N01] [N02] [N03] [N04] [N05] [N06] [N07] [N08] [N09] [N10]",
        "Vanguard Bastion [N01-03] | Center [N04-06] | Abyssal Rift [N07-10]",
        "Point-Blank Band 1        : Distance = 0 Nodes (Adjacent Melee)",
        "Short-Range Band 2        : Distance = 1 to 2 Nodes (Polearms/Shot)",
        "Medium-Range Band 3       : Distance = 3 to 4 Nodes (Rifles/Bows)",
        "Long-Range Band 4         : Distance = 5 to 6 Nodes (Artillery)",
        "Global Artillery Band 5   : Distance = 7+ Nodes (Siege Resonance)"
    ])

    box3 = make_box(71, "THE FOUR P-FRAMEWORK CORE ARCHITECTURE - CANONICAL PILLARS", [
        "P1: Passives   - Innate biological, mental, and M.A.W. traits",
        "P2: Panic      - Acoustic Composure gauge, Meltdown thresholds",
        "P3: Parry      - Dynamic clash resolution, deflection, shield",
        "P4: Posture    - Physical balance, knockback resistance, stagger"
    ])

    content = f"""# Tactical Combat Engine — Grid Battle System (GBS)
## Spatial Physics, Action Economies, and Engagement Protocols

---

{box1}
## 1. Engine Overview & Design Tenets

The Somnarak Tactical Combat Engine represents the operational simulation framework governing all hostile engagements across Facility 01, subterranean descent operations (SED), underworld pacification sweeps (UCD), and overland caravan expeditions.

Unlike abstract card-battlers or static turn-based systems, the Somnarak engine combines **spatial positioning across a discrete 10-Node Grid**, **speed-scaled dynamic action economies**, **dual-threshold modular part damage**, and the holistic **Four P-Framework (Passives, Panic, Parry, Posture)**.

The primary design tenets are:
1. **Physical Spatial Value:** Movement and positioning directly dictate combat effectiveness. Every meter on the grid matters.
2. **Speed as Operational Bandwidth:** Speed does not simply decide who strikes first; higher speed awards more Action Points (AP), allowing complex multi-skill sequences and evasive maneuvers.
3. **Dual-Threshold Stagger:** Enemies cannot be defeated by simple hit-point attrition. Dismantling modular body parts triggers tactical Staggers (60% threshold), while draining psychic Composure triggers terminal Meltdown (0% threshold).
4. **Macro-Phase Rhythms:** Engagements are structured into 6-Turn Combat Phases. At Phase-End, environmental tides, atmospheric Han saturation, and boss transformations resolve.

---

## 2. Spatial Grid Mechanics: The 10-Node Engagement Line

{box2}
All combat occurs along a standardized linear corridor consisting of ten discrete nodes: `[N01]` through `[N10]`.

### 2.1 Node Allocation & Starting Deployment
- **Allied Operatives (Vanguard Bastion):** Typically deploy within `[N01]` to `[N03]`.
- **Neutral / Transit Zone (Center Field):** Spans `[N04]` to `[N06]`. Contains barricades, hydraulic pipes, and destructible cover.
- **Hostile Entities (Abyssal Rift):** Typically manifest within `[N07]` to `[N10]`.

### 2.2 Movement Points & Grid Repositioning
- Operatives spend **1 Action Point (AP)** to shift 1 node along the line, unless modified by equipment weight or agility passives.
- **Collision & Interception:** An operative cannot move past an active hostile occupying a node without passing a Posture clash. Attempting to bypass a hostile triggers an automatic Opportunity Strike.
- **Flanking & Pincer Mechanics:** If allied units occupy nodes on both sides of a target (e.g., Ally A at `[N04]`, Enemy at `[N05]`, Ally B at `[N06]`), all subsequent attacks deal +25% bonus kinetic damage.

### 2.3 The Five Range Bands
Every weapon, skill, and Sorrow manifestation is calibrated to a specific Range Band:
- **Band 1 (Point-Blank / Melee):** Effective at 0 node distance (same or directly adjacent node). Maximum kinetic impact; vulnerable to parry.
- **Band 2 (Short-Range):** Effective at 1 to 2 nodes. Polearms, short shotguns, and close-quarters acoustic emitters.
- **Band 3 (Medium-Range):** Effective at 3 to 4 nodes. Pneumatic rifles, longbows, and directional Han projectors.
- **Band 4 (Long-Range):** Effective at 5 to 6 nodes. Heavy sniper rifles, mortar canisters, and boundary harpoons.
- **Band 5 (Global Artillery / Siege):** Effective at 7+ nodes. Sector-wide acoustic cannons and sovereign tide waves.

---

## 3. Action Economy & Speed Scaling

The core resource governing every combat turn is the **Action Point (AP)**.

### 3.1 Speed-to-AP Conversion Formula
At the beginning of each Battle Turn, an operative's initiative is calculated using their base Speed stat, modified by equipment weight class:
- **Base Speed 1–2 (Heavy / Fortress):** Generates 2 AP per turn.
- **Base Speed 3–4 (Medium):** Generates 3 AP per turn.
- **Base Speed 5–6 (Light):** Generates 4 AP per turn.
- **Base Speed 7+ (Ultra-Light / Agility Vanguard):** Generates 5 AP per turn.

### 3.2 Action Slot Dispatching
Action Points are allocated across discrete Action Slots:
- **Movement:** 1 AP per node advance or retreat.
- **Basic Strike / Skill:** 1 to 2 AP depending on skill complexity.
- **Defensive Guard / Parry Stance:** 1 AP (primes active counter-dice).
- **Special M.A.W. Activation:** 2 to 3 AP plus Sorrow Echo expenditure.

---

## 4. The Four P-Framework

{box3}

### 4.1 Pillar 1: Passives (P1)
Every operative and entity possesses innate passives derived from their biological background, departmental training, and equipped M.A.W. gear. Passives trigger automatically upon condition fulfillment (e.g., bonus damage against targets below 30% HP, or automatic composure recovery when standing adjacent to an ally).

### 4.2 Pillar 2: Panic / Composure (P2)
- **Composure Pool (0 to 100):** Represents neurological and psychological resilience against acoustic Han frequencies.
- Taking Lament or Void damage drains Composure directly.
- **Panic Threshold (Composure <= 25):** Operative suffers accuracy penalties, speed reductions, and cannot execute advanced skills.
- **Composure Meltdown (Composure = 0):** The operative suffers complete cognitive breakdown. They are incapacitated for 1 turn, drop all defensive stances, and take 100% vulnerability to all damage types.

### 4.3 Pillar 3: Parry / Protection (P3)
- When two opposing units target each other within mutual range, a **Clash Resolution** occurs.
- The units roll their respective Skill Dice. The higher roll deflects the incoming attack entirely, inflicting the roll difference as direct Posture strain onto the loser.
- **Active Cover:** Operatives behind environmental sandbags or industrial bulkheads gain +30% protection against ranged projectile damage.

### 4.4 Pillar 4: Posture / Poise (P4)
- **Posture Pool (0 to 100):** Measures physical balance and skeletal integrity against kinetic shockwaves and Weight pressure.
- Taking heavy blunt or kinetic strikes drains Posture.
- **Posture Break (Posture = 0):** The target is knocked back by 1 node, loses their remaining AP for the current turn, and enters a Stagger state.

---

## 5. Dual-Threshold Stagger Engine

Hostile entities—especially Rank IV Entities and Rank V Sovereigns—possess modular body parts (Head, Torso, Limbs, Core, Wings). Combat resolution tracks two distinct stagger triggers:

| Stagger Trigger | Threshold Condition | Mechanical Consequence | Duration |
|---|---|---|---|
| **Part Rupture (Tactical Stagger)** | Specific Part HP drops below 60% | That part's associated skills are disabled; defensive resistance on that part drops from 0.7 to 1.5. | 1 Turn |
| **Composure Meltdown (Terminal Stagger)** | Total Composure drops to 0 | Entity collapses; cannot act; loses all Action Slots; all parts receive maximum critical damage. | Full Combat Phase |

---

## 6. Macro-Phase Structure (6-Turn Combat Cycle)

A full combat engagement is structured around **Macro Combat Phases**, where exactly **6 Battle Turns constitute 1 Combat Phase**:
- **Turns 01 to 05:** Tactical skirmishing, node maneuvering, part dismantling, and composure attrition.
- **Turn 06 (Phase Climax):** High-stakes clash turn; major elite skills charge; environmental alarms trigger.
- **Phase-End Resolution:** After Turn 06 finishes, the engine executes global environmental updates:
  * **Sorrow Tide Check:** Ambient Han saturation increases by +10%.
  * **Status Ticks:** Bleed, corrosion, and resonance ticks resolve.
  * **Boss Stance Transition:** Sovereigns enter evolved behavioral stances if HP thresholds were crossed.

---

## 7. Canonical Battle Demonstration (Turns 01 to 06 Summary)

The engine's complete operation is demonstrated in the canonical engagement between Strike Team Alpha (Operatives Taeho, Seol-A, Min-Jae, Ha-Eun) and Sovereign Entity `SE-C-Vδ-002 The Grieving Colossus`:
- **Turn 01:** Vanguard advances from `[N02]` to `[N04]`; sniper occupies high-ground cover at `[N01]`.
- **Turn 02:** Boss unleashes tectonic shockwave at `[N05]`; Min-Jae absorbs with Fortress Shield, preserving squad posture.
- **Turn 03:** Concentrated fire focuses on the Colossus's Left Knee, breaching the 60% threshold and triggering Part Rupture.
- **Turn 04:** The Colossus is immobilized; Seol-A delivers an acoustic puncture, draining 35 Composure points.
- **Turn 05:** Composure reaches zero; Terminal Meltdown activates, collapsing the colossus across nodes `[N06]` to `[N08]`.
- **Turn 06:** All four operatives execute synchronized execution strikes, shattering the vessel into 650 kg of pure Han dust.

---

**Engine Specification Code:** `SOMNARAK-ENGINE-GBS-001`  
**Standard Authority:** Reverie Directorate Tactical Simulation Division  
**Classification:** Definitive Combat Architecture Standard
"""
    return content

def build_what_can_be_done():
    box1 = make_box(71, "PLAYABLE IMPLEMENTATION ROADMAP - WHAT CAN BE DONE", [
        "Project Goal      : Playable Implementation of Somnarak GBS",
        "Target Milestones : CLI Simulator -> Web Prototype -> Engine Port",
        "Architecture Model: Decoupled State Machine & Event Dispatcher",
        "Engine Tech Stack : TypeScript / Python Core -> Canvas / Godot 4",
        "Data Standard     : Pure JSON Schemas for Operatives and Gears",
        "Validation Status : Verified Math Formulas & State Transition Maps"
    ])

    box2 = make_box(71, "PHASED DEVELOPMENT MILESTONES - EXECUTION PIPELINE", [
        "Milestone 01: Pure CLI Terminal Combat Simulator (Logic Core)",
        "Milestone 02: Interactive Browser Canvas / Web UI Prototype",
        "Milestone 03: Full Data-Driven Scenario Builder & Encounter Tool",
        "Milestone 04: Godot 4 / WebAssembly Executable Game Build",
        "Milestone 05: Complete Wiki Integration with Interactive Logs"
    ])

    content = f"""# Tactical Combat Engine — Playable Implementation Roadmap
## What Can Be Done: Architecture, Data Schemas, Formulas, and Milestones

---

{box1}
## 1. Executive Summary & Implementation Vision

The foundational design of the Somnarak Grid Battle System (GBS) has been fully codified in `SOMNARAK_BATTLE_SYSTEM.md` and `SOMNARAK_BATTLE_SYSTEM_STYLES.md`. This document establishes the concrete, actionable engineering roadmap for transforming those mathematical and spatial rules into a **fully playable, executable tactical combat game**.

The core philosophy of this implementation is **strict decoupling between the simulation logic and the presentation layer**. The combat engine will exist as an autonomous, deterministic state machine that can be executed as a command-line simulator, embedded inside a web-based interactive wiki page, or linked into a high-performance 2D/3D game engine such as Godot 4.

---

## 2. Core Engine Architecture

The playable system is organized into five decoupled architectural modules:

```text
+-------------------------------------------------------------------+
|                        PRESENTATION LAYER                         |
|   (CLI Terminal / Web Canvas / Vue.js UI / Godot Engine Views)    |
+-------------------------------------------------------------------+
                                 ^
                                 |  Event Stream (Turns, Hits, Meltdowns)
                                 v
+-------------------------------------------------------------------+
|                     COMBAT ENGINE DISPATCHER                      |
|  - Phase Manager (6-Turn Macro Cycle & Phase-End Ticks)           |
|  - Turn Dispatcher (AP Allocation, Initiative Sorting)            |
|  - Action Queue & Clash Evaluator                                 |
+-------------------------------------------------------------------+
                                 ^
                                 |  Reads & Modifies State
                                 v
+-------------------------------------------------------------------+
|                   SPATIAL & DAMAGE STATE MACHINE                  |
|  - 10-Node Grid Coordinator ([N01] to [N10] Occupancy & Range)    |
|  - Four P-Framework Evaluator (Passives, Panic, Parry, Posture)   |
|  - Dual-Threshold Stagger Engine (60% Part Rupture / 0% Meltdown) |
+-------------------------------------------------------------------+
                                 ^
                                 |  Data Injection
                                 v
+-------------------------------------------------------------------+
|                        CANONICAL DATA REPO                        |
|  - Operative Database (Base Stats, Speed Dice, M.A.W. Wear)       |
|  - 287 Sorrow Entities (Modular Parts, AI Intention Decks)        |
|  - 198 Quadripartite M.A.W. Sets (Weapons, Suits, Gifts)          |
+-------------------------------------------------------------------+
```

---

## 3. Mathematical Formulas & Combat Resolution

All numerical resolutions within the engine rely on clean, deterministic arithmetic without complex floating-point ambiguities.

### 3.1 Damage Calculation Formula
When a skill strikes a target without being completely parried:

```text
Effective Damage = Base Weapon Damage * Skill Multiplier * Elemental Affinity Multiplier * Stagger Multiplier
```

Where:
- **Base Weapon Damage:** Rolled from weapon range (e.g., Grade γ poleaxe rolls 8–15).
- **Elemental Affinity Multiplier:**
  * Resistant (0.3 to 0.5)
  * Endured (0.7 to 0.8)
  * Normal (1.0)
  * Weak / Vulnerable (1.2 to 1.5)
  * Fatal / Cleaved (2.0)
- **Stagger Multiplier:**
  * Normal Stance: 1.0
  * Part Rupture Active (Threshold <= 60%): 1.5 on targeted ruptured part
  * Composure Meltdown Active (Composure = 0): 2.0 across all parts

### 3.2 Clash & Parry Resolution Formula
When two opposing skills target each other in mutual range:

```text
Clash Value = (Speed Roll + Base Skill Power + Active Passive Modifiers)
Margin of Victory = Ally Clash Value - Hostile Clash Value
```

- If `Margin > 0`: The ally wins the clash. The enemy's attack is cancelled; the enemy suffers `Margin * 2` direct Posture damage.
- If `Margin < 0`: The enemy wins the clash. The ally's attack is cancelled; the ally takes `|Margin| * 2` Posture damage.
- If `Margin == 0`: Mutual deflection (Tied Clash). Both combatants take 5 Posture recoil, and both skills fail to inflict health damage.

### 3.3 Node-Distance & Range Formula
Between Source Node `N_src` and Target Node `N_tgt`:

```text
Distance = |N_src - N_tgt|
```

A skill can only be queued if `Distance` falls within the weapon's calibrated Range Band:
- **Band 1:** Distance == 0
- **Band 2:** Distance >= 1 and Distance <= 2
- **Band 3:** Distance >= 3 and Distance <= 4
- **Band 4:** Distance >= 5 and Distance <= 6
- **Band 5:** Distance >= 7

---

## 4. Concrete Data Schemas (JSON Specification)

### 4.1 Operative Profile Schema (`operative.json`)
```json
{{
  "id": "OP-001",
  "name": "Taeho",
  "callsign": "The Architect",
  "assigned_wing": "Reverie Directorate",
  "base_stats": {{
    "health_max": 180,
    "health_current": 180,
    "composure_max": 100,
    "composure_current": 100,
    "posture_max": 100,
    "posture_current": 100,
    "base_speed": 4,
    "current_grid_node": 2
  }},
  "equipped_maw": {{
    "weapon": "MAW-W-002-01",
    "suit": "MAW-S-002-01",
    "gift": "MAW-G-002-01"
  }},
  "passives": ["P1-MANTLE-ENDURANCE", "P1-STEADY-PACE"],
  "action_slots": []
}}
```

### 4.2 Modular Sorrow Entity Schema (`entity.json`)
```json
{{
  "secc_code": "SE-C-Vδ-002",
  "name_en": "The Grieving Colossus",
  "name_ko": "슬픔의 거인",
  "coherence_rank": "V",
  "potency_grade": "δ",
  "occupying_nodes": [7, 8],
  "composure_pool": {{
    "max": 300,
    "current": 300,
    "meltdown_threshold": 0
  }},
  "modular_parts": [
    {{
      "part_name": "Stone Head",
      "hp_max": 800,
      "hp_current": 800,
      "rupture_threshold": 480,
      "is_ruptured": false,
      "resistances": {{ "lament": 0.5, "grudge": 1.0, "void": 1.2, "weight": 0.4 }}
    }},
    {{
      "part_name": "Left Knee Pillar",
      "hp_max": 600,
      "hp_current": 600,
      "rupture_threshold": 360,
      "is_ruptured": false,
      "resistances": {{ "lament": 0.7, "grudge": 0.8, "void": 1.0, "weight": 0.3 }}
    }}
  ],
  "ai_intent_deck": [
    {{
      "skill_id": "SKILL-COLOSSUS-STOMP",
      "target_part": "Left Knee Pillar",
      "target_range": [0, 2],
      "ap_cost": 2,
      "damage_type": "weight",
      "damage_dice": [14, 26]
    }}
  ]
}}
```

---

## 5. Phased Execution Pipeline: What Can Be Done

{box2}

### Milestone 01: Pure CLI Terminal Combat Simulator (Logic Core)
- **Scope:** A lightweight Python/TypeScript terminal engine.
- **Features:**
  * Implements the 10-node array with visual ASCII battle line.
  * Turn loop: Initiative calculation -> AP allocation -> Clash roll -> Stagger check.
  * Runs automated headless combat simulations (e.g., 1,000 battles) to mathematically verify balance between M.A.W. Wear Grades and Entity Ranks.
- **Deliverable:** `tools/combat_simulator.py` or `engine/cli_combat.ts`.

### Milestone 02: Interactive Browser Canvas / Web UI Prototype
- **Scope:** Client-side HTML5 Canvas or Vue.js / React micro-app embedded in the documentation.
- **Features:**
  * Visual 10-node grid where players drag operative tokens along the track.
  * AP allocation bar, Skill Clash preview dials, and interactive Composure meters.
  * Real-time generation of the canonical 6-turn combat log format.
- **Deliverable:** Standalone single-file HTML/JS playable prototype in `docs/interactive_combat/`.

### Milestone 03: Full Data-Driven Scenario Builder
- **Scope:** Web interface allowing writers and designers to construct custom combat encounters.
- **Features:**
  * Select from the 287 canonical Sorrow Entities and configure environmental hazards.
  * Equip custom 4-person squad configurations across all 198 complete M.A.W. sets.
  * Export verified combat encounters directly as markdown narrative battle logs for story codices.

### Milestone 04: Godot 4 / WebAssembly Executable Game Build
- **Scope:** Full-fledged standalone tactical RPG build.
- **Features:**
  * 2D pixel-art or stylized vector sprites on the 10-node battlefield.
  * Dynamic camera zooms during high-stakes clashes and Part Ruptures.
  * Sound design featuring 432 Hz mantle hums and authentic Han acoustic effects.
  * Cross-platform release: WebAssembly (browser), Windows, Linux, and macOS.

### Milestone 05: Wiki & Encyclopedia Synchronization
- **Scope:** Direct deep linking between game data and the public web wiki.
- **Features:**
  * Clicking an entity in the combat interface opens its canonical side codex and observation logs.
  * Dynamic equipment tooltips displaying real-time M.A.W. wear stats.

---

## 6. Actionable Next Steps

To immediately commence the playable implementation:
1. **Initialize Engine Core Package:** Create pure state-machine logic in `SOMNARAK-WORLD/Tactical_Combat_Engine/src/`.
2. **Implement CLI Test Suite:** Write deterministic unit tests asserting clash formulas, knockback resolution, and dual-threshold staggers.
3. **Connect Canonical Schemas:** Ingest the completed M.A.W. sets and Sorrow Entities into structured JSON bundles.

---

**Roadmap ID:** `SOMNARAK-ROADMAP-TCE-001`  
**Author Authority:** Core Tactical Combat Simulation Group  
**Classification:** Definitive Engineering Implementation Blueprint
"""
    return content

if __name__ == "__main__":
    target_dir = "SOMNARAK-WORLD/Tactical_Combat_Engine"
    os.makedirs(target_dir, exist_ok=True)

    r_text = build_engine_readme()
    with open(os.path.join(target_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(r_text)
    print("Successfully wrote SOMNARAK-WORLD/Tactical_Combat_Engine/README.md")

    w_text = build_what_can_be_done()
    with open(os.path.join(target_dir, "WHAT_CAN_BE_DONE.md"), "w", encoding="utf-8") as f:
        f.write(w_text)
    print("Successfully wrote SOMNARAK-WORLD/Tactical_Combat_Engine/WHAT_CAN_BE_DONE.md")
