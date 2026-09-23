# Tactical Combat Engine — Playable Implementation Roadmap
## What Can Be Done: Architecture, Data Schemas, Formulas, and Milestones

---

```text
+---------------------------------------------------------------------+
|          PLAYABLE IMPLEMENTATION ROADMAP - WHAT CAN BE DONE         |
+---------------------------------------------------------------------+
| Project Goal      : Playable Implementation of Somnarak GBS         |
| Target Milestones : CLI Simulator -> Web Prototype -> Engine Port   |
| Architecture Model: Decoupled State Machine & Event Dispatcher      |
| Engine Tech Stack : TypeScript / Python Core -> Canvas / Godot 4    |
| Data Standard     : Pure JSON Schemas for Operatives and Gears      |
| Validation Status : Verified Math Formulas & State Transition Maps  |
+---------------------------------------------------------------------+
```


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
{
  "id": "OP-001",
  "name": "Taeho",
  "callsign": "The Architect",
  "assigned_wing": "Reverie Directorate",
  "base_stats": {
    "health_max": 180,
    "health_current": 180,
    "composure_max": 100,
    "composure_current": 100,
    "posture_max": 100,
    "posture_current": 100,
    "base_speed": 4,
    "current_grid_node": 2
  },
  "equipped_maw": {
    "weapon": "MAW-W-002-01",
    "suit": "MAW-S-002-01",
    "gift": "MAW-G-002-01"
  },
  "passives": ["P1-MANTLE-ENDURANCE", "P1-STEADY-PACE"],
  "action_slots": []
}
```

### 4.2 Modular Sorrow Entity Schema (`entity.json`)
```json
{
  "secc_code": "SE-C-Vδ-002",
  "name_en": "The Grieving Colossus",
  "name_ko": "슬픔의 거인",
  "coherence_rank": "V",
  "potency_grade": "δ",
  "occupying_nodes": [7, 8],
  "composure_pool": {
    "max": 300,
    "current": 300,
    "meltdown_threshold": 0
  },
  "modular_parts": [
    {
      "part_name": "Stone Head",
      "hp_max": 800,
      "hp_current": 800,
      "rupture_threshold": 480,
      "is_ruptured": false,
      "resistances": { "lament": 0.5, "grudge": 1.0, "void": 1.2, "weight": 0.4 }
    },
    {
      "part_name": "Left Knee Pillar",
      "hp_max": 600,
      "hp_current": 600,
      "rupture_threshold": 360,
      "is_ruptured": false,
      "resistances": { "lament": 0.7, "grudge": 0.8, "void": 1.0, "weight": 0.3 }
    }
  ],
  "ai_intent_deck": [
    {
      "skill_id": "SKILL-COLOSSUS-STOMP",
      "target_part": "Left Knee Pillar",
      "target_range": [0, 2],
      "ap_cost": 2,
      "damage_type": "weight",
      "damage_dice": [14, 26]
    }
  ]
}
```

---

## 5. Phased Execution Pipeline: What Can Be Done

```text
+---------------------------------------------------------------------+
|          PHASED DEVELOPMENT MILESTONES - EXECUTION PIPELINE         |
+---------------------------------------------------------------------+
| Milestone 01: Pure CLI Terminal Combat Simulator (Logic Core)       |
| Milestone 02: Interactive Browser Canvas / Web UI Prototype         |
| Milestone 03: Full Data-Driven Scenario Builder & Encounter Tool    |
| Milestone 04: Godot 4 / WebAssembly Executable Game Build           |
| Milestone 05: Complete Wiki Integration with Interactive Logs       |
+---------------------------------------------------------------------+
```



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
