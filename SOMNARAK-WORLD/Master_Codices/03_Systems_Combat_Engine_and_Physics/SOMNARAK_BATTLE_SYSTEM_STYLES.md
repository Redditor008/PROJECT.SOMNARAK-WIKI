# Project Somnarak — Battle System Styles (전투 체계 양식록)
## The Four Canonical Tactical Branches of Combat & Tactical Physics
### Authorized by the Reverie Directorate, SED Frontier Command, and UCD High Command

> *"A warden defending a high-security containment cell does not fight like a riot breacher clearing a sunken drug foundry, and an abyssal explorer suspended over a three-kilometer chasm does not fight like either. The sorrow of this world is infinite, but the methods we forge to withstand it are precise, disciplined, and uniquely adapted to where we stand."*  
> — Supreme Tactical Doctrine, Reverie Directorate General Staff

---

## I. Executive Architectural Overview

The combat physics of Project Somnarak are unified by a single foundational engine—**The Generic P.S. Combat Core**—while branching into three highly specialized operational styles corresponding to the three major institutions of the city:

```text
+=====================================================================+
|       PROJECT SOMNARAK: QUAD-STYLE BATTLE SYSTEM ARCHITECTURE       |
+---------------------------------------------------------------------+
| 1. GENERIC P.S. CORE FOUNDATION (Universal Combat Engine)           |
|    - 10-Node Room Stage Grid (Node 1 to Node 10 spatial positions). |
|    - Speed-to-AP Action Economy (Initiative, Movement, Clashes).    |
|    - Macro Phase Structure (6 Battle Turns = 1 Combat Phase).       |
|    - Dual-Resource Pool: Sorrow Gauge (0-100%) and Composure (SP).  |
| - Dual-Threshold Stagger Engine (Stagger 1 at 60%, Terminal 25%).   |
|    - M.A.W. Quadripartite Armaments & 4 Sorrow Elements.            |
+---------------------------------------------------------------------+
| 2. REVERIE DIRECTORATE (R.D.) STYLE — Facility Oversight & Contain  |
| - Operational Domain : Subterranean Facility 01 (Hand of Change).   |
|    - Spatial Topology   : 10-Node Containment Vault & Console Grid. |
| - Core Mechanic : Echo-Core Floor Resonance (Floors 1 to 8).        |
|    - Tactical Focus     : Mid-combat Work Cycles (Flere/Pugna/etc), |
| containment meltdowns, and colored Ordeals.                         |
+---------------------------------------------------------------------+
| 3. UNDERWORLD CLEANUP DESCEND (UCD) STYLE — Urban CQB & Interdict   |
|    - Operational Domain : Undercity slums, drainage kilns, vaults.  |
|    - Spatial Topology   : 10-Node Ingress Grid (Cordon to Sanctum). |
| - Core Mechanic : Targeted Part Dismantling (Modular Parts).        |
| - Tactical Focus : In-combat forensic hacking, civilian cover,      |
| and municipal collateral threshold defense.                         |
+---------------------------------------------------------------------+
| 4. SOMNARAK EXPLORATION DECREE (SED) STYLE — Abyssal Descents       |
|    - Operational Domain : Unmapped karst caverns (-50m to -3,500m). |
|    - Spatial Topology   : 10-Node Vertical Karst & Chasm Grid.      |
| - Core Mechanic : Strata Depth Atmospheric Pressure per Phase.      |
| - Tactical Focus : Acoustic stealth / decibel sonar management,     |
| survival attrition timers, seismic pitons,                          |
|                           and pre-cataclysm relic field excavation. |
+=====================================================================+
```

Every battle encounter across the narrative passages and operational sweeps adheres to three universal structural pillars:
1. **The 10-Node Room Stage Grid**: Precise physical spatial positioning that makes Speed, Range, and Line of Sight literal tactical mechanics.
2. **Speed-Driven Battle Turn Action Economy**: Speed determines not just initiative order, but the exact Action Points (AP) an operative commands per turn.
3. **Macro Phase Combat Structure**: Every 6 Battle Turns compose 1 Combat Phase, culminating in systemic Phase-End Environmental Hazard and Equilibrium checks.

---

## II. The Universal 10-Node Room Stage Engine (Spatial Combat Grid)

To eradicate abstract positioning and give Range, Speed, and Movement concrete tactical meaning, all combat chambers in Somnarak are mapped onto a standard linear and depth track: **Nodes 1 through 10**.

```text
+=====================================================================+
|              THE UNIVERSAL 10-NODE ROOM STAGE TOPOLOGY              |
+---------------------------------------------------------------------+
| [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]         |
| |--VANGUARD---| |--SKIRMISH---| |--MID-FIELD--| |--REAR LINE--|     |
+---------------------------------------------------------------------+
| Node 01-02 : Vanguard / Point Blank (Melee, Shields, Breaches)      |
| Node 03-04 : Close Skirmish / CQB (Shotguns, SMGs, Daggers)         |
| Node 05-06 : Mid-Field Convergence (Assault Rifles, Work Terminals) |
| Node 07-08 : Rear Line Overwatch (Sniper Rifles, Piton Winches)     |
| Node 09-10 : Extreme Artillery / Sanctuary (Mortars, Hostage        |
| Berths)                                                             |
+=====================================================================+
```

### 2.1 The Five Tactical Node Sectors

1. **Vanguard & Breach Zone (Nodes 1–2 / 0 to 5 meters)**:
   - The violent frontline. Dedicated to melee weapon clashes, heavy riot shields, hydraulic rams, and physical grapples.
   - Operatives here physically intercept advancing hostiles, preventing them from pushing toward rear support units.
2. **Close Skirmish / CQB Band (Nodes 3–4 / 6 to 15 meters)**:
   - The close-quarters skirmish corridor. Optimal for shotguns, submachine guns, cleavers, and directional defensive barriers.
   - Serves as the primary defensive screen for the mid-field.
3. **Mid-Field Convergence Band (Nodes 5–6 / 16 to 30 meters)**:
   - The tactician and support staging ground. Optimal for assault rifles, medium-range energy lances, and specialized institutional consoles (containment work terminals, mobile field hospitals).
4. **Rear Line Overwatch Band (Nodes 7–8 / 31 to 50 meters)**:
   - The heavy marksman and command perimeter. High-caliber anti-materiel rifles, acoustic decryption antennas, and structural piton anchors operate here with full visual clearance.
5. **Extreme Artillery & Sanctuary Band (Nodes 9–10 / 51+ meters)**:
   - The absolute rear. Shelters wounded personnel, non-combatant civilian berths, long-range heavy mortars, facility stasis projectors, and ascent cables.

---

### 2.2 Range Bands & Distance Mechanics

Distance between combatants is calculated by absolute node difference:  
$$\text{Distance (Nodes)} = |\text{Node}_{\text{Attacker}} - \text{Node}_{\text{Target}}|$$

| Range Band | Node Distance | Real Distance | Optimal Weaponry | Damage & Accuracy Modifiers |
|---|---|---|---|---|
| **Band 1 (Point Blank)** | 0 to 1 Node | 0 – 5 meters | Fists, daggers, cleavers, shields | **100% Melee Power**; Ranged incurs -20% accuracy & -2 Clash Power |
| **Band 2 (Close CQB)** | 2 to 3 Nodes | 6 – 15 meters | Shotguns, SMGs, short polearms | **100% CQB Power**; Melee requires 1 AP Dash to engage |
| **Band 3 (Mid-Range)** | 4 to 5 Nodes | 16 – 30 meters | Assault rifles, energy conduits | **100% Rifle Power**; Shotguns suffer 70% falloff; Melee cannot reach |
| **Band 4 (Long-Range)** | 6 to 7 Nodes | 31 – 50 meters | Precision sniper rifles, relic bows | **100% Sniper Power**; Mid rifles suffer 50% falloff; CQB cannot reach |
| **Band 5 (Extreme)** | 8 to 9 Nodes | 51+ meters | Heavy siege mortars, Singularity beams | **100% Heavy Artillery**; All standard small arms deal 0% damage |

---

### 2.3 Movement, Positioning & Interception

Combatants do not stand stationary. Operatives utilize their Speed-allocated Action Points to dynamically navigate the 10-node grid:

- **Node Movement Cost**: Moving 1 Node forward or backward costs **1 Action Point (AP)**.
- **Sprint / Dash**: Spending 2 AP enables a high-speed dash across 2 to 3 Nodes simultaneously, bypassing light ground hazards.
- **Node Capacity & Cover**:
  * Each standard Node can hold up to 3 medium combatants or 1 massive boss module.
  * **Light Cover** (Debris, pillars): Grants +15% Evasion and +1 Clash Power against incoming ranged fire.
  * **Heavy Cover** (Reinforced blast plates, steel bulkheads): Grants +30% Armor Defense and absorbs direct projectile pierce.
- **The Interception Law (Zone of Control)**:
  * Attempting to move past an enemy occupied node without eliminating them triggers an immediate **Interception Clash**.
  * If the mover loses the clash, their movement is halted on that node and they suffer immediate kinetic stagger buildup.

---

## III. Speed-Driven Battle Turn Structure & Action Economy

In Project Somnarak, **Speed is not merely turn order—it is your operational action budget**. High-speed operatives act earlier *and* accomplish substantially more actions per turn than encumbered or panicked combatants.

```text
+=====================================================================+
|            SPEED-TO-ACTION POINT (AP) CONVERSION ENGINE             |
+---------------------------------------------------------------------+
| Speed Roll   | Action Points (AP) | Tactical Capabilities Per Turn  |
| -------------+--------------------+-------------------------------- |
| Speed 1 - 2  | 1 Action Point     | 1 Basic Strike OR 1 Node Shift  |
| Speed 3 - 4  | 2 Action Points    | 1 Move + 1 Attack OR 1 Guard    |
| Speed 5 - 6  | 3 Action Points    | Move + Resonance Skill + Guard  |
| Speed 7 - 8  | 4 Action Points    | Multi-Combo + Rapid Sprint      |
| Speed 9 - 10+| 5 Action Points    | Overdrive Blitz + Spatial Flank |
+=====================================================================+
```

### 3.1 Speed Roll & Action Point (AP) Allocation

At the beginning of every Battle Turn, each participant rolls their Speed Die:
$$\text{Speed} = \text{Base Speed Attribute} + \text{Composure Modifier} + \text{Die Roll (1d6 or 1d10)}$$

The rolled Speed directly unlocks **Action Points (AP)** for that turn:
- **Speed 1–2**: 1 AP (Severely crippled or suppressed; single basic action only).
- **Speed 3–4**: 2 AP (Standard baseline combatant; move + attack, or brace + strike).
- **Speed 5–6**: 3 AP (Veteran operative; move + tactical skill + defensive guard).
- **Speed 7–8**: 4 AP (High-speed specialist; multi-target combos, rapid sprint + double clash).
- **Speed 9–10+**: 5 AP (Elite overdrive state; spatial blink, quad-clash barrage, team support).

### 3.2 Action Point Spending Menu

During their Battle Turn, an operative can spend their AP across five tactical categories:

1. **Maneuver (1 AP per Node)**: Reposition along the 10-node grid to achieve optimal Range Band.
2. **Basic Strike (1 AP)**: Perform a standard melee swing or ranged burst within weapon range.
3. **Resonance Skill (2 AP)**: Unleash an advanced M.A.W. combat art (elemental infusal, armor pierce, multi-coin strike).
4. **Defensive Stance (1 AP)**:
   - *Guard*: Deploys a barrier absorbing incoming damage equal to (Base Defense + Resolve).
   - *Evade*: Sets an evasion coin; completely nullifies damage on winning dodge rolls.
   - *Counter*: Prepares a reactionary strike triggered when struck by an incoming melee clash.
5. **Institutional Action (1 to 2 AP)**:
   - *R.D. Work Cycle* (2 AP): Perform Flerehan, Pugnahan, Ferrehan, or Viderehan at an entity terminal.
   - *UCD Forensic Hack* (2 AP): Auditor slices syndicate ledgers or jams communication frequencies.
   - *SED Seismic Anchor* (1 AP): Specialist fires a heavy piton into unstable cavern basalt.

---

## IV. The Macro Phase Combat Structure (6 Battle Turns = 1 Phase)

Combat progresses through a strictly regulated temporal hierarchy:
1. **Action**: A single resolution (strike, step, guard, hack).
2. **Battle Turn**: The full cycle where all combatants spend their rolled AP.
3. **Combat Phase**: A macro-cycle consisting of **exactly six (6) Battle Turns**.

```text
+=====================================================================+
|                  MACRO PHASE COMBAT TIME STRUCTURE                  |
+---------------------------------------------------------------------+
| ONE COMBAT PHASE = SIX (6) SEQUENTIAL BATTLE TURNS                  |
+---------------------------------------------------------------------+
| Turn 1 : Roll Speed -> Determine AP -> Resolve movement & clashes.  |
| Turn 2 : Repositioning along nodes, second exchange of fire.        |
| Turn 3 : Focus fire, part-dismantling strikes, defensive guards.    |
| Turn 4 : Department specials, forensic decrypts, work cycles.       |
| Turn 5 : Stagger exploitation, emergency healing, shield bracing.   |
| Turn 6 : Climax finishers, final clash line of the phase cycle.     |
+---------------------------------------------------------------------+
| [PHASE-END EQUILIBRIUM & HAZARD TICK]                               |
| 1. Environmental Check : Meltdown timer / Collateral / Depth        |
| Strain.                                                             |
| 2. Status Decay        : Bleed / Weep damage; SP drifts toward 0.   |
| 3. Stagger Recovery : Stagger 1 resets; Terminal Stagger checked.   |
| 4. Boss Phase Shift    : Stance change / Ordeal Ingress / Waves.    |
+=====================================================================+
```

### 4.1 The Phase-End Equilibrium & Environmental Hazard Tick

When Battle Turn 6 concludes, the battlefield enters the **Phase-End Resolution Window** before Battle Turn 1 of the next phase begins. During this window, systemic world physics activate:

1. **Environmental Threat Advancement**:
   - *Reverie Directorate*: The Facility Meltdown Clock advances by 1 tier. If containment was neglected, secondary sector sirens sound and Ordeal entities breach.
   - *Underworld Cleanup*: Municipal Collateral is audited. If structural integrity fell below safety thresholds, ceiling girders collapse, turning random nodes into hazard zones.
   - *Exploration Decree*: The Strata Depth Atmospheric Pressure ticks, inflicting severe SP erosion and testing suit oxygen seals.
2. **Status Decay & Elemental Equilibrium**:
   - Bleed / Hemorrhage counters halve after dealing direct physical damage per stack.
   - Composure (SP) drifts naturally by +3 toward 0 if negative, representing adrenaline stabilization.
   - Sorrow Gauges vent or condense depending on active resonant frequencies.
3. **Dual-Threshold Stagger Duration Check**:
   - Operatives who suffered Stagger 1 during Turns 1–5 recover their posture and regain defensive stats.
   - Operatives who suffered Terminal Stagger 2 remain broken until the entire encounter ends or an ally spends 3 AP to administer emergency stimulants.
4. **Boss Phase Alteration & Ordeal Ingress**:
   - Bosses evaluate their remaining vitality. Crossing phase thresholds causes bosses to discard broken parts, draw secondary heavy weapons, deploy invincible shields, or summon backup waves.

---

## V. Branch 1: Generic P.S. Combat Core (The Universal Engine)

The Universal Engine governs all basic combat mathematics, clash comparisons, and elemental relationships.

### 5.1 Dual-Resource Equilibrium: Sorrow vs Composure

Every combatant in Somnarak balances two internal psychological gauges:

1. **Sorrow Gauge (0% to 100%)**:
   - Represents the accumulation of ambient and manifested Han-sorrow.
   - *For Agents*: Reaching 100% causes **Cognitive Fracture**—the agent succumbs to overwhelming grief, mutating or attacking allies indiscriminately.
   - *For Sorrow Entities*: Reaching 100% triggers **Berserk Overdrive**, unlocking lethal multi-target attacks and stripping all stagger vulnerabilities.
2. **Mental Composure / Sanity Points (SP: -45 to +45)**:
   - Measures operational clarity and emotional grounding.
   - High SP (+15 to +45): Greatly improves Clash coin flip odds (up to 95% heads rate).
   - Low SP (-15 to -44): Causes panic, misses, and erratic target redirection.
   - Terminal SP (-45): Forces the combatant into **Paralyzing Panic** for 1 full turn.

### 5.2 Clash Resolution Mechanics

When two combatants target each other within viable Range Bands, a **Clash** occurs:
$$\text{Total Clash Power} = \text{Base Skill Power} + \sum (\text{Heads Coins} \times \text{Coin Modifier})$$

- **Winner**: Lands their strike, dealing full damage and inflicting associated status effects.
- **Loser**: Their attack is completely nullified; they take direct damage and suffer +15 Stagger buildup.
- **One-Sided Attack**: If a target has no remaining AP or actions to contest an incoming attack, the attacker strikes unopposed with a +20% damage bonus.

### 5.3 The Dual-Threshold Stagger Engine

Health bars feature two distinct break thresholds:
- **Stagger 1 (60% Max HP)**:
  * Posture breaks. Defense drops to 0. Takes **2.0× direct damage** for 1 turn. Action slots for that turn are wiped.
- **Terminal Stagger 2 (25% Max HP)**:
  * Complete skeletal and nervous collapse. Takes **2.5× direct damage**. Enables allies to execute **Overdrive Climax Finishers** (3 AP execution skills dealing lethal true damage).

### 5.4 The Four Elemental Affinities

| Element | Color | Damage Paradigm | Defensive Ward | Combat Dynamic |
|---|---|---|---|---|
| **Grudge** | Crimson (원한) | Physical / Hemorrhage / Rupture | Resilience | Cleaving flesh, breaking mechanical parts, stacking bleeding |
| **Lament** | Deep Blue (비탄) | SP Erosion / Composure Drain | Clarity | Rapidly reducing enemy SP to force panic and clash failure |
| **Void** | Pale White (공허) | Soul Disruption / Memory Erasure | Composure | Absolute percentage damage, silencing high-tier skills |
| **Weight** | Black (비중) | Gravitational Crush / Impact | Resolve | Enormous stagger buildup, smashing shields, knocking targets back |

---

## VI. Branch 2: Reverie Directorate (R.D.) Style

**Operational Focus**: Facility 01 (*The Hand of Change*), 8 subterranean containment floors, extraction vaults.  
**Tactical Philosophy**: Containment over slaughter; methodical psychological stabilization and continuous Han-Energy harvest.

```text
+=====================================================================+
|          REVERIE DIRECTORATE (R.D.) CONTAINMENT VAULT GRID          |
+---------------------------------------------------------------------+
| [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]         |
| |--ENTITY CORE--| |--BLAST GATE---| |--WORK BAFFLES-|               |
| |--TERMINAL--|                                                      |
+---------------------------------------------------------------------+
| N01-N02 : Entity Core (Sorrow Radiation, Melee Engagement Zone)     |
| N03-N04 : Heavy Blast Gates (Kinetic Interception, Warden Phalanx)  |
| N05-N06 : Work Console Array (Flerehan, Pugnahan, Ferrehan, Videre) |
| N07-N08 : Quarantine Overwatch (Stasis Cannons, Sedative Conduits)  |
| N09-N10 : Echo-Core Terminal (Direct Resonance to Floors 1 to 8)    |
+=====================================================================+
```

### 6.1 Spatial 10-Node Containment Topology

In Reverie Directorate operations, battlefields are high-security containment sectors:
- **Nodes 1–2 (Chamber Core)**: Where the breached entity or Ordeal manifests. Highly hazardous; saturated with ambient Sorrow radiation.
- **Nodes 3–4 (Inner Blast Sluice)**: Reinforced kinetic airlocks. Heavy containment wardens hold the line here with blast mantlets to prevent the entity from breaking into corridor spaces.
- **Nodes 5–6 (Work Console Array)**: Contains specialized pneumatic terminals wired to the facility's emotion baffles. Operatives can spend 2 AP here to execute non-lethal Work Types directly on the entity.
- **Nodes 7–8 (Quarantine Perimeter)**: Where reserve agents and snipers monitor containment gauge levels and fire sedative harpoons.
- **Nodes 9–10 (Echo-Core Terminal)**: The direct energetic uplink to the assigned Department Floor Lead.

---

### 6.2 Echo-Core Floor Resonance on the 10-Node Grid

When deploying under a specific department, the Echo-Core lead projects tactical auras across designated nodes:

1. **Floor 1 (Majin & Seiyon — Central Command)**:
   - *Command Eye*: Can spend 1 AP to reroll the Speed Die of any allied agent across Nodes 1 to 10.
   - *Department Clarity*: Team-wide +15 SP restoration whenever a clash is won at Node 5 or 6.
2. **Floor 2 (Dekan — The Maw's Keep / Containment)**:
   - *Bastion Ward*: Grants +50% Shield Armor to all allies standing on Nodes 1 through 4.
   - *Jaw Clamp*: Any melee clash won at Node 1 or 2 pins the entity, preventing it from moving past Node 2 for 2 turns.
3. **Floor 3 (Zyrak — The Extraction Hall)**:
   - *Energy Siphon*: Executing a Work Cycle on Nodes 5–6 extracts double Han-Energy into the facility battery.
   - *M.A.W. Overcharge*: Consumes 20 Han-Energy to grant an ally's weapon +5 Clash Power and elemental true damage.
4. **Floor 4 (Ayshuk — Insight Forge / Research)**:
   - *Predictive HUD*: Reveals the entity's exact target nodes and dice rolls 1 full Battle Turn in advance.
   - *Weakness Attunement*: Increases elemental damage multipliers from 1.5× to 2.2× across all nodes.
5. **Floor 5 (Mellda — Border Watch / Bulwark)**:
   - *Blast Gate Lockdown*: Mellda raises emergency steel bulkheads at Node 4, isolating Nodes 1–3 and blocking all ranged entity beams.
   - *Martial Rebuke*: Retaliatory counter-attack when an enemy breaches past Node 4.
6. **Floor 6 (Marjuk — Deep Vault / Archive)**:
   - *Stasis Field*: Freezes a target on Node 1 or 2 in temporal amber for 1 full Battle Turn, canceling all its queued AP.
   - *Mnemonic Recovery*: If an agent falls in battle, their cognitive pattern is locked in stasis, guaranteeing post-operation revival.
7. **Floor 7 (Ishall — Shadow Corps / Covert Relics)**:
   - *Unanswered Strike*: Remote relic strike utilizing the floating mineral digits. Dispatches Void damage from Node 10 directly to Node 1 with 0% range falloff and armor bypass.
   - *Shadow Ingress*: Allows allied infiltrators to teleport from Node 8 directly behind the entity at Node 1.
8. **Floor 8 (Xyan — The Final Gate / Wellhead)**:
   - *Singularity Well*: Creates a gravitational vortex at Node 1 that pulls all roaming hostiles into melee range and suppresses displacement abilities.

---

### 6.3 Mid-Combat Work Cycle Execution

Unlike military annihilation, R.D. teams often achieve victory by completing **Work Cycles** mid-battle:
- An agent moves to Nodes 5–6 (Console) or Nodes 1–2 (Direct Contact) and spends 2 AP:
  * **Flerehan (공감작업)**: Plays harmonic weeping frequencies. Wins a psychological clash to lower the entity's Sorrow Gauge by 25%.
  * **Pugnahan (억제작업)**: Deploys kinetic dampeners. Wins a physical clash to reduce entity Speed by -4 and lock its high-tier skills.
  * **Ferrehan (인내작업)**: Reinforces containment seals while absorbing direct kinetic blows; boosts allied defense by +40%.
  * **Viderehan (관찰작업)**: Analyzes cognitive resonance, instantly exposing hidden Stagger thresholds and lowering enemy clash defense.

---

### 6.4 Facility Meltdown Clock & Ordeal Waves per Phase

- At the end of every Phase (every 6 Battle Turns), the **Meltdown Clock** ticks:
  * **Phase 1 End**: Level 1 Meltdown. 2 peripheral containment cells enter warning state.
  * **Phase 2 End**: Level 2 Meltdown. Green or Amber Dawn Ordeal units spawn at Node 10, flanking the squad.
  * **Phase 3 End**: Level 3 Meltdown. Violet Noon fissures open on Nodes 3 and 7, dealing passive Void damage each turn.
  * **Phase 4+ End**: Level 4+ Meltdown. Dusk or Midnight catastrophic entities mobilize unless the primary target is contained.

---

## VII. Branch 3: Underworld Cleanup Descend (UCD) Style

**Operational Focus**: Dense municipal undercity slums (*The Raw*), subterranean drainage foundries, usury vaults (-5m to -350m).  
**Tactical Philosophy**: Urban CQB, room-to-room breach clearance, targeted structural dismantling, and civilian collateral preservation.

```text
+=====================================================================+
|           UNDERWORLD CLEANUP DESCEND (UCD) URBAN CQB GRID           |
+---------------------------------------------------------------------+
| [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]         |
| |--BREACH CORDON| |--SLUICE ALLEY-| |--FOUNDRY FLOOR|               |
| |--SANCTUM---|                                                      |
+---------------------------------------------------------------------+
| N01 : Breach Cordon (Entry Ram, Smoke Mortars, Breacher Shields)    |
| N02-N03 : Tight Corridors (Shotgun Sweeps, Melee Alley Brawls)      |
| N04-N05 : Foundry / Usury Floor (Syndicate Enforcers, Boss Parts)   |
| N06-N07 : Server Vault (Auditor Yuna Forensic Hacking Hub)          |
| N08-N09 : Hostage Holding Berths (Civilians, Taeho Obsidian         |
| Bastion)                                                            |
| N10     : Syndicate Boss Dais / Contraband Vault / Escape Pod       |
+=====================================================================+
```

### 7.1 Spatial 10-Node Urban CQB Grid

UCD operations unfold through claustrophobic architectural choke points:
- **Node 1 (Breach Cordon)**: The heavy reinforced entrance. Breachers deploy shaped kinetic charges and ballistic riot shields.
- **Nodes 2–3 (Tenement Alley / Sluice)**: Confined urban corridors. Shotgun spreads and shield bashes dominate here; ranged weapons suffer severe line-of-sight penalties.
- **Nodes 4–5 (Foundry Main Floor / Usury Vault)**: Large industrial chambers. Where syndicate lieutenants, heavy machinery, and modular boss components are stationed.
- **Nodes 6–7 (Server Vault & Hacking Hub)**: Syndicate communications switchboards and encrypted financial ledgers. Auditor Yuna plugs in here to dismantle criminal networks.
- **Nodes 8–9 (Hostage Berths & Structural Pillars)**: Cages holding kidnapped civilians alongside critical building load-bearing columns. Must be shielded from stray bullets.
- **Node 10 (Syndicate Command Dais / Escape Pod)**: Where the syndicate chief commands or attempts extraction.

---

### 7.2 Targeted Part Dismantling Engine (Part-Breaking)

UCD bosses do not fight as monolithic HP pools. They are assembled from distinct mechanical, chemical, and biological modules spanning multiple nodes:

```text
+=====================================================================+
|                UCD TARGETED PART BREAKING INTERFACE                 |
+---------------------------------------------------------------------+
| [MODULE 1: EXOSKELETON CHASSIS]      HP: [100/100] DEF: 45 (ARMD)   |
| - Function: Grants boss +30% Kinetic Armor across Nodes 3 to 5.     |
| - Broken  : Armor reduced to 0; pilot exposed to direct Stagger.    |
+---------------------------------------------------------------------+
| [MODULE 2: CHEMICAL SPRAY CONDUIT]   HP: [ 60/ 60] RANGE: Band 2    |
| - Function: Blasts Nodes 1-4 with corrosive acid every 2 turns.     |
| - Broken  : Acid attack permanently disabled; spills on boss.       |
+---------------------------------------------------------------------+
| [MODULE 3: HYDRAULIC WINCH ARM]      HP: [ 40/ 40] RANGE: Band 3    |
| - Function: Pulls operatives from Node 6 forward into Node 2 melee. |
| - Broken  : Winch snaps; boss loses grab and takes 25 Stagger.      |
+=====================================================================+
```

- **Targeting a Part**: Operatives at appropriate Range Bands spend AP to direct strikes at specific modules rather than the central boss core.
- **Sapping & Severing**: Depleting a part's HP breaks the module, permanently deleting associated boss skills, triggering an immediate Stagger check, and changing the boss's attack pattern.

---

### 7.3 In-Combat Forensic Decryption (Auditor Yuna)

While vanguard breachers pin syndicate enforcers on Nodes 1–4, Auditor Yuna advances to the Server Vault at Nodes 6–7:
- **Decryption Progress (0% to 100%)**:
  * Yuna spends 2 AP per turn interfacing with the terminal. Each turn of uninterrupted hacking adds +25% Decryption.
  * **25% Decryption**: Uncovers syndicate radio frequencies, disabling enemy support fire.
  * **50% Decryption**: Freezes syndicate automated defense turrets across Nodes 3–6.
  * **75% Decryption**: Cuts power to the boss's hydraulic armaments, reducing boss Speed by -3.
  * **100% Decryption (Full Audit)**: Seizes illicit bank accounts, permanently breaking boss morale and inflicting team-wide -30 SP Panic on remaining syndicate thugs.

---

### 7.4 Civic Collateral & Hostage Shielding (Commander Taeho)

In UCD doctrine, achieving a military victory while slaughtering civilians or collapsing the city block is rated an **Operational Failure**:
- **The Collateral Gauge (0% to 100%)**:
  * Explosive and high-caliber misses near Nodes 8–9 increase the Collateral Gauge (+10% per stray heavy projectile).
  * If the gauge hits 100%, the ceiling collapses, causing total mission failure.
- **Taeho's Obsidian Bastion**:
  * Commander Taeho positions at Node 7, deploying his heavy obsidian mantlet.
  * *Shield Redirection*: Any stray bullet or enemy area-of-effect aimed at Nodes 8–9 is automatically intercepted by Taeho's shield, preserving hostage lives and structural integrity.

---

## VIII. Branch 4: Somnarak Exploration Decree (SED) Style

**Operational Focus**: Unmapped geological karst caverns, boiling underground aquifers, and the -3,500m Mugenhan Ocean.  
**Tactical Philosophy**: Extreme environmental survival, acoustic stealth, long-range reconnaissance, and relic excavation.

```text
+=====================================================================+
|           SOMNARAK EXPLORATION DECREE (SED) ABYSSAL GRID            |
+---------------------------------------------------------------------+
| [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]         |
| |--CHASM BRINK--| |--KARST SCREE--| |--SURVEY BASE--| |--ASCENT     |
| RIG-|                                                               |
+---------------------------------------------------------------------+
| N01     : The Chasm Brink (-1,500m to -3,500m Void, Supercritical)  |
| N02-N03 : Treacherous Karst Scree (Double Move Cost, Piton Target)  |
| N04-N05 : Expedition Base Camp (Oxygen Refills, Lantern Fuel)       |
| N06-N07 : Primordial Ruin Shelf (Before-Time Relic Dig Sites)       |
| N08-N09 : High Stalactite Shelf (Long-Range Overwatch, Sonar Radar) |
| N10     : Surface Ascent Cable & Pressurized Evacuation Cradle      |
+=====================================================================+
```

### 8.1 Spatial 10-Node Abyssal Cavern Topology

SED descents take place across vertically staggered cavern shelves and abyssal crevices:
- **Node 1 (The Chasm Brink)**: A bottomless sheer drop into the lightless planetary mantle. Saturated with superheated steam and supercritical Han currents.
- **Nodes 2–3 (Treacherous Karst Scree)**: Fractured, unstable stone. Moving through costs **2 AP per Node** unless stabilized by seismic pitons.
- **Nodes 4–5 (Expedition Base Camp)**: Secured heavy anchor platform holding oxygen replenishment compressors and lantern fuel canisters.
- **Nodes 6–7 (Primordial Ruin Shelf)**: Ancient stone terraces containing half-buried Before-Time relics and fossilized strata.
- **Nodes 8–9 (Elevated Stalactite Perch)**: Natural high ground providing perfect line-of-sight across Nodes 1 through 7 for marksmen.
- **Node 10 (Ascent Cable & Evacuation Cradle)**: High-tensile steel winches leading back to the upper frontier outpost.

---

### 8.2 Strata Depth Atmospheric Pressure Engine

The deeper the expedition descends, the greater the physical and cognitive weight of the earth:

$$\text{Pressure Penalty} = f(\text{Depth Stratum}) \quad \text{evaluated at each Phase-End}$$

| Stratum & Depth Band | Atmospheric Pressure | Phase-End Environmental SP Drain | Combat Penalties & Hazard Level |
|---|---|---|---|
| **Stratum 1 (0m to -150m)** | 1.0 to 1.5 Bar | -2 SP per Phase | Baseline subterranean conditions; minor footing hazards |
| **Stratum 2 (-150m to -500m)** | 1.5 to 3.0 Bar | -4 SP per Phase | Movement costs +1 AP on rough nodes; thermal suit wear |
| **Stratum 3 (-500m to -1,200m)** | 3.0 to 6.5 Bar | -6 SP per Phase | Toxic gas clouds; failure of gas masks deals Grudge bleed |
| **Stratum 4 (-1,200m to -2,000m)** | 6.5 to 9.0 Bar | -8 SP per Phase | Crushing rock weight; all maximum Speed rolls reduced by -2 |
| **Stratum 5 (-2,000m to -2,600m)** | 9.0 to 11.5 Bar | -10 SP per Phase | Tectonic tremors; unanchored agents risk falling into Node 1 |
| **Stratum 6 (-2,600m to -2,800m)** | 11.5 to 13.5 Bar| -12 SP per Phase | Supercritical Han vapors; acoustic and sensory interference |
| **Stratum 7 (-2,800m to Core)** | 13.5 to 15.0+ Bar| -15 SP per Phase | Primordial Nadir; Singularity diving rigs strictly mandatory |

---

### 8.3 Acoustic Stealth & Sonar Decibel System

Deep subterranean caverns echo with lethal precision. Giant slumbering Sorrow Beasts nest inside hollow stone walls:
- **The Decibel Meter (0 to 120 dB)**:
  * Silenced stilettos, bows, and Work actions generate **0 to 5 dB**.
  * Medium caliber bursts generate **+15 dB**.
  * Heavy shotguns and demolition charges generate **+35 dB**.
  * Sound dissipates by -10 dB at the end of each Phase.
- **The Awakening Threshold (100 dB)**:
  * If the cumulative decibel meter exceeds 100 dB, the cavern ceiling shatters. A dormant Tier-3 or Tier-4 subterranean behemoth awakens and drops onto Node 1, entering the fight as a hostile third party attacking both sides.

---

### 8.4 Seismic Anchoring & In-Combat Relic Excavation

SED specialists deploy unique expedition tools on the grid:
- **Tectonic Piton Anchoring (1 AP)**:
  * An engineer fires a heavy titanium piton into an unstable node (Nodes 2–3).
  * The node becomes **Anchored**: movement cost drops back to standard 1 AP, and all occupants become immune to tectonic tremor knockbacks.
- **In-Combat Relic Excavation (2 AP)**:
  * A field scholar standing on Nodes 6–7 spends 2 AP per turn using sonic picks to unearth ancient Before-Time relics.
  * Excavating a relic grants powerful one-shot primordial field effects (e.g., *Aura of Ancient Solitude*, granting team-wide invulnerability to Void damage for 1 Phase).

---

## IX. Complete Combat Visualization Template & Step-by-Step Scenario

Below is the definitive, canonical combat visualization template designed for direct adaptation into narrative story chapters.

### Scenario: Warden Strike Team vs Breached Entity "The Weeping Bell" (Tier HE)
- **Location**: Facility 01, Floor 4 (Insight Forge Sector).
- **Roster**: Warden Captain Jin (Vanguard / Melee), Agent Min (Mid-Field / Console Specialist), Agent Ray (Rear Sniper).
- **Enemy**: The Weeping Bell (Occupies Node 2).

```text
+=====================================================================+
|                COMBAT HUD: PHASE 01 — BATTLE TURN 01                |
+---------------------------------------------------------------------+
| [STAGE] :                                                           |
| [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]         |
| POS     :        [BELL] [JIN]           [MIN]           [RAY]       |
| DIST    : Jin at N03 (Band 1); Min at N05 (Console); Ray at N07.    |
+---------------------------------------------------------------------+
| Jin : Speed 6 -> 3 AP | SP: +20 | Sorrow:  5% | Dekan Cleaver (B1)  |
| Min : Speed 4 -> 2 AP | SP: +15 | Sorrow: 10% | Insight Lens        |
| (Console)                                                           |
| Ray : Speed 7 -> 4 AP | SP: +25 | Sorrow:  0% | Stasis Carbine (B4) |
| Bell: Speed 5 -> 3 AP | Sorrow: 40% | Resonant Clang, Wail (AoE)    |
+=====================================================================+
```

#### Turn 01 Action Resolution Log
- **Step 1: Movement & AP Allocation**:
  * Warden Jin spends 1 AP to shift from Node 3 to Node 2 (closing to Point Blank with The Bell). Remaining AP: 2.
  * Agent Min holds Node 5 (Work Console). Spends 2 AP to initiate `[Flerehan Work Cycle]`.
  * Agent Ray holds Node 7 (Overwatch). Spends 2 AP to aim `[Aimed Void Shot]` at Bell's clapper module. Remaining AP: 2.
- **Step 2: Clash Engagement (Node 2)**:
  * The Weeping Bell declares `[Resonant Clang]` against Warden Jin (Base 8 + 2 Coins = 12 Power).
  * Warden Jin declares `[Heavy Cleaver Parry]` (Base 9 + 2 Coins = 14 Power).
  * **Resolution**: Jin WINS THE CLASH (14 vs 12). Bell's attack is cancelled. Jin deals 32 Weight damage, inflicting +18 Stagger. Jin SP rises from +20 to +25.
- **Step 3: Ranged & Work Resolution**:
  * Agent Ray fires `[Aimed Void Shot]` from Node 7 to Node 2 (Distance: 5 Nodes / Band 3). Unopposed strike deals 28 Void damage to Bell's clapper.
  * Agent Min completes `[Flerehan Console Transmission]` from Node 5. Emotional harmonics reduce Entity Sorrow Gauge from 40% to 20%.

```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Jin holds N02 behind shield; Bell hits 60% Stagger 1.    |
| - Turn 03: All allied attacks deal 2.0x damage; Bell HP drops to    |
| 45%.                                                                |
| - Turn 04: Bell recovers; charges lethal area skill [Deafening      |
| Toll].                                                              |
| - Turn 05: Ray at N07 uses 2 AP to fire Stasis Bolt, canceling      |
| skill.                                                              |
| - Turn 06: Min completes second Work Cycle; Bell Sorrow drops to    |
| 0%.                                                                 |
+=====================================================================+
```

```text
+=====================================================================+
|                PHASE 01 RESOLUTION (PHASE-END TICK)                 |
+---------------------------------------------------------------------+
| 1. Environmental Check : Meltdown Clock advances to Level 1.        |
| 2. Status Equilibrium : Bleed ticks on Bell (-12 HP); Jin SP at     |
| +30.                                                                |
| 3. Containment Check   : Entity Sorrow Gauge reaches 0%.            |
| 4. OUTCOME : CLEAN CONTAINMENT — ZERO ALLIED CASUALTIES.            |
+=====================================================================+
```

---

## X. Story Combat Adaptation Guidelines

When writing or revising battle sequences across canonical chronicles (`SOMNARAK_SED_PASSAGES.md`, `SOMNARAK_UCD_PACIFICATION.md`, and `The_Absolvohan`):

1. **Always Establish Spatial Nodes**: Explicitly state where combatants begin and how they maneuver across Nodes 1 through 10.
2. **Translate Speed into Tangible Actions**: Describe high-speed combatants executing multiple actions (striking, dashing, parrying) within a single turn, reflecting their higher AP budget.
3. **Respect Range Band Falloff**: A shotgun blast fired from Node 7 must visibly scatter with heavy damage penalty; a sniper shot from Node 8 into Node 1 must carry devastating kinetic power.
4. **Structure Long Battles in 6-Turn Phases**: Group escalating narrative tension into distinct 6-turn phases, concluding with systemic Phase-End environmental checks (meltdowns, collateral collapses, depth pressure ticks).
5. **Enforce Branch Mechanics**:
   - Reverie Directorate battles must feature Echo-Core leads, mid-combat Work Cycles, and containment aims.
   - UCD battles must feature room breaching, targeted module breaking, Yuna's forensic hacking, and Taeho's civilian protection.
   - SED battles must feature atmospheric pressure strain, acoustic stealth management, seismic pitons, and primordial relic excavations.

---

### Master Archive Status

- **Codex Designation**: `SOMNARAK-TAC-04-A (Expanded Edition)`
- **Compiler**: General Staff Coalition (R.D. / UCD / SED)
- **Authority**: High Council Supreme Tactical Directive
- **Baseline Standard**: 100% Authoritative V.1.0 Standard (Zero file-embedded confessions)
