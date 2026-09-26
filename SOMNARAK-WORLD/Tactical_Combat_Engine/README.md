# Tactical Combat Engine — Grid Battle System (GBS)
## Spatial Physics, Action Economies, and Engagement Protocols

---

```text
+---------------------------------------------------------------------+
|   TACTICAL COMBAT ENGINE - SPATIAL GRID & RESOLUTION ARCHITECTURE   |
+---------------------------------------------------------------------+
| System Name       : Somnarak Grid Battle System (GBS Core Engine)   |
| Spatial Field     : 10-Node Linear Engagement Grid ([N01] to [N10]) |
| Action Economy    : Speed-Scaled Action Points (AP 2 to 5 per Turn) |
| Engagement Bands  : Range Bands 1 through 5 (Point-Blank to Siege)  |
| Stagger Mechanics : Dual-Threshold (60% Part Rupture / 0% Meltdown) |
| Combat Phases     : 6 Battle Turns = 1 Macro Environmental Phase    |
| Framework Standard: Four P-Framework (Passive, Panic, Parry, Poise) |
+---------------------------------------------------------------------+
```


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

```text
+---------------------------------------------------------------------+
|        SPATIAL GRID NODE TOPOGRAPHY - 10-NODE ENGAGEMENT LINE       |
+---------------------------------------------------------------------+
| [N01] [N02] [N03] [N04] [N05] [N06] [N07] [N08] [N09] [N10]         |
| Vanguard Bastion [N01-03] | Center [N04-06] | Abyssal Rift [N07-10] |
| Point-Blank Band 1        : Distance = 0 Nodes (Adjacent Melee)     |
| Short-Range Band 2        : Distance = 1 to 2 Nodes (Polearms/Shot) |
| Medium-Range Band 3       : Distance = 3 to 4 Nodes (Rifles/Bows)   |
| Long-Range Band 4         : Distance = 5 to 6 Nodes (Artillery)     |
| Global Artillery Band 5   : Distance = 7+ Nodes (Siege Resonance)   |
+---------------------------------------------------------------------+
```


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

```text
+---------------------------------------------------------------------+
|      THE FOUR P-FRAMEWORK CORE ARCHITECTURE - CANONICAL PILLARS     |
+---------------------------------------------------------------------+
| P1: Passives   - Innate biological, mental, and M.A.W. traits       |
| P2: Panic      - Acoustic Composure gauge, Meltdown thresholds      |
| P3: Parry      - Dynamic clash resolution, deflection, shield       |
| P4: Posture    - Physical balance, knockback resistance, stagger    |
+---------------------------------------------------------------------+
```



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
