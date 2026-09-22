#!/usr/bin/env python3
"""
Generator script for SOMNARAK-WORLD/Master_Codices/SOMNARAK_BATTLE_SYSTEM_STYLES.md
and updater for SOMNARAK-WORLD/Master_Codices/SOMNARAK_BATTLE_SYSTEM.md.

Enforces:
- 4-Branch Architecture:
  1. Generic P.S. Core Foundation (Universal Engine)
  2. Reverie Directorate (R.D.) Style (Facility Oversight & Containment)
  3. Underworld Cleanup Descend (UCD) Style (Urban CQB & Interdiction Warfare)
  4. Somnarak Exploration Decree (SED) Style (Subterranean Abyssal Descents)
- Exact symmetrical ASCII boxes (71 columns).
- Zero banned terms / zero external verse borrowings.
- Authoritative V.1.0 standard with zero file-embedded confessions.
"""

import sys
import re

banned_patterns = [
    r"\bego\b", r"\be\.g\.o\b", r"\babnormality\b", r"\babnormalities\b",
    r"\bdistortion\b", r"\bdistortions\b", r"\bpeccatula\b", r"\bfixer\b",
    r"\bfixers\b", r"\bassociation\b", r"\bassociations\b", r"\bfingers\b",
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

# Master text for SOMNARAK_BATTLE_SYSTEM_STYLES.md
styles_content = """# Project Somnarak — Battle System Styles (전투 체계 양식록)
## The Four Canonical Tactical Branches of Combat & Tactical Physics
### Authorized by the Reverie Directorate, SED Frontier Command, and UCD High Command

> *"A warden defending a high-security containment cell does not fight like a riot breacher clearing a sunken drug foundry, and an abyssal explorer suspended over a three-kilometer chasm does not fight like either. The sorrow of this world is infinite, but the methods we forge to withstand it are precise, disciplined, and uniquely adapted to where we stand."*  
> — Supreme Tactical Doctrine, Reverie Directorate General Staff

---

## I. Executive Architectural Overview

The combat physics of Project Somnarak are unified by a single foundational engine—**The Generic P.S. Combat Core**—while branching into three highly specialized operational styles corresponding to the three major institutions of the city:

```text
+=====================================================================+
|               PROJECT SOMNARAK: QUAD-STYLE BATTLE SYSTEM            |
+=====================================================================+
| 1. GENERIC P.S. CORE FOUNDATION (Universal Combat Engine)           |
|    - Dual-Resource Pool : Sorrow Gauge (0-100%) and Composure (SP). |
|    - Clash Resolution   : Speed Dice, Atk/Def power, Clash Wins.    |
|    - Stagger Mechanics  : Dual-Threshold (Stagger 1 and Terminal 2).|
|    - Armament System    : M.A.W. Quadripartite (Weapon, Suit, Cloak)|
|    - Four Affinities    : Grudge, Lament, Void, Weight.             |
+---------------------------------------------------------------------+
| 2. REVERIE DIRECTORATE (R.D.) STYLE — Facility Oversight & Contain  |
|    - Operational Domain : Subterranean Facility 01 (Hand of Change).|
|    - Core Mechanic      : Echo-Core Floor Resonance (Floors 1 to 8).|
|    - Tactical Focus     : In-combat Work Cycles, Meltdown Timers,   |
|                           Multi-color Ordeal outbreak suppression.  |
+---------------------------------------------------------------------+
| 3. UNDERWORLD CLEANUP DESCEND (UCD) STYLE — Urban CQB & Interdict   |
|    - Operational Domain : Dense undercity slums, vaults, and kilns. |
|    - Core Mechanic      : Targeted Part Dismantling & Sapping.      |
|    - Tactical Focus     : Room-to-room breach grids, forensic hacks,|
|                           non-lethal hostage and foundation shields.|
+---------------------------------------------------------------------+
| 4. SOMNARAK EXPLORATION DECREE (SED) STYLE — Abyssal Descents       |
|    - Operational Domain : Unmapped karst caverns (-50m to -3,500m). |
|    - Core Mechanic      : Strata Depth Atmospheric Pressure.        |
|    - Tactical Focus     : Acoustic stealth/sonar, oxygen attrition, |
|                           seismic pitons, pre-cataclysm relic digs. |
+=====================================================================+
```

---

## II. Branch 1: Generic P.S. Combat Core (The Universal Engine)

The Universal Engine defines the fundamental mathematics, initiative flow, and damage calculations shared across all operational branches.

### 2.1 Dual-Resource Architecture

Every combatant operates under two interconnected emotional gauges:

1. **Sorrow Gauge (0% to 100%)**:
   - Represents the accumulation of ambient and internal grief.
   - For personnel: Reaching 100% triggers **Fracture** (catastrophic cognitive collapse or permanent sorrow transformation).
   - For entities and bosses: Reaching 100% triggers **Berserk Overdrive**, unlocking lethal area-of-effect skills and changing attack patterns.
2. **Mental Composure / Sanity Points (SP: -45 to +45)**:
   - Measures emotional clarity, moral grounding, and operational discipline.
   - High SP (+15 to +45): Increases Clash coin flip success rates, granting bonus offensive power.
   - Low SP (-15 to -44): Causes panic, misses, and erratic combat actions.
   - Terminal SP (-45): Forces the combatant into **Panic State** or temporary paralysis.

### 2.2 Turn Flow & Clash Mechanics

```text
+=====================================================================+
|                     GENERIC P.S. TURN RESOLUTION                    |
+=====================================================================+
| STEP 1 : Speed Dice Roll -> Determines turn initiative order.       |
| STEP 2 : Target Slot Allocation -> Lines of engagement assigned.    |
| STEP 3 : Clash Comparison -> (Base Power + Coin Modifiers) weighed. |
| STEP 4 : Clash Winner strikes opponent; loser action is cancelled.  |
| STEP 5 : Damage calculated through Elemental Affinity multipliers.  |
| STEP 6 : Sorrow Gauge and Composure (SP) adjusted based on outcome. |
+=====================================================================+
```

### 2.3 The Dual-Threshold Stagger Engine

Every target possesses two hard break points within their maximum vitality:

- **Stagger Threshold 1 (60% Max HP)**:
  * When health drops below 60%, the target's posture breaks.
  * Duration: 1 complete turn.
  * Penalties: Defense drops to 0; takes **2.0× direct damage**; all queued actions cancelled.
- **Terminal Stagger Threshold 2 (25% Max HP)**:
  * Triggered when health falls below 25%.
  * Duration: 1 complete turn.
  * Penalties: Complete immobility; takes **2.5× direct damage**; all defensive passives extinguished. Allows tactical execution of Overdrive Climax finishers.

### 2.4 The Four Elemental Affinities

| Element | Color Spectrum | Damage Focus | Defensive Counter | Strategic Role |
|---|---|---|---|---|
| **Grudge** | Crimson (원한) | Physical / Structural / Hemorrhage | Resilience | Heavy kinetic cleaves, part fractures, bleeding |
| **Lament** | Deep Blue (비탄) | Composure Drain / Psychic Erosion | Clarity | SP destruction, panic inducement, weeping slows |
| **Void** | Pale White (공허) | Soul Disruption / Amnesia / Erasure | Composure | Absolute percentage damage, skill silencing |
| **Weight** | Black (비중) | Gravitational Crush / Impact Stun | Resolve | Heavy stagger buildup, armor shattering, knockback |

---

## III. Branch 2: Reverie Directorate (R.D.) Style

**Operational Domain**: Subterranean Facility 01 (*The Hand of Change*), containment cells, and extraction vaults.  
**Doctrine**: Methodical containment, psychological stabilization, and structured energy harvest.

```text
+=====================================================================+
|               REVERIE DIRECTORATE TACTICAL HUD LAYOUT               |
+=====================================================================+
| [FLOOR RESONANCE] : Active Lead Resonance Bonus (Floors 1 to 8)     |
| [CONTAINMENT GAUGE] : Sector Meltdown Alarm Timer (Turn Counter)    |
| [WORK COMMAND]    : Mid-Combat Work Cycle (Ferre/Flere/Pugna/Videre)|
| [ORDEAL RADAR]    : Secondary Sector Defense Status (Color Watch)   |
+=====================================================================+
```

### 3.1 Echo-Core Floor Resonance System

In R.D. combat encounters, the deploying unit coordinates directly with the assigned Echo-Core department lead, gaining massive passive and active battlefield commands:

- **Floor 1 (Majin & Seiyon — Central Command)**:
  * *The Director's Eye*: Once per battle, reroll all allied Speed Dice.
  * *Administrative Clarity*: Restores +15 SP team-wide upon successful Clash.
- **Floor 2 (Dekan — The Maw's Keep / Containment)**:
  * *Bastion of the Keep*: Allied shields absorb +40% kinetic impact.
  * *Scaled Maw Grasp*: Melee strikes inflict bonus Weight damage, pinning breached entities.
- **Floor 3 (Zyrak — The Extraction Hall)**:
  * *Energy Multiplier*: Successful work actions generate double Han-Energy.
  * *M.A.W. Overcharge*: Spend 20 Han-Energy to grant an ally's weapon a temporary Grade-Ω damage boost.
- **Floor 4 (Ayshuk — Insight Forge / Research)**:
  * *Predictive Analysis*: Reveals all enemy attack slots and target weaknesses 1 turn in advance.
  * *Resonance Attunement*: Increases elemental weakness damage from 1.5× to 2.2×.
- **Floor 5 (Mellda — Border Watch / Bulwark)**:
  * *Sacred Perimeter*: Deploys deployable blast barriers that absorb incoming area-of-effect attacks.
  * *Threshold Lockdown*: Closes emergency sector gates, preventing entity escape.
- **Floor 6 (Marjuk — Deep Vault / Archive)**:
  * *Mnemonic Recovery*: Prevents permanent death; fallen agents are placed in stasis for post-battle memory restoration.
  * *Stasis Field*: Freezes a breached entity's action slot for 1 turn.
- **Floor 7 (Ishall — Shadow Corps / Covert Operations)**:
  * *Unanswered Strike*: Remote relic strikes deal direct Void damage, bypassing enemy armor shields.
  * *Phantom Ingress*: Grants allied agents stealth and guaranteed critical strikes on opening turns.
- **Floor 8 (Xyan — The Final Gate / Wellhead)**:
  * *Dimensional Singularity*: Anchors gravitational field, nullifying all entity displacement abilities.

### 3.2 Mid-Combat Work Cycle Execution

Unlike military engagements, R.D. wardens can sacrifice attack slots to execute official **Work Types** mid-battle:
- **Flerehan (공감작업)**: Plays weeping resonance to soothe an entity's sorrow, reducing its Sorrow Gauge by 20% on Clash Win.
- **Pugnahan (억제작업)**: Deploys acoustic clamps to stun the target and prevent phase transformation.
- **Ferrehan (인내작업)**: Bolsters allied physical armor ratings while absorbing direct kinetic blows.
- **Viderehan (관찰작업)**: Scans structural weak points to reveal hidden stagger thresholds.

---

## IV. Branch 3: Underworld Cleanup Descend (UCD) Style

**Operational Domain**: Subterranean slums (*The Raw*), drainage foundries, usury vaults, and basalt arenas (-5m to -350m).  
**Doctrine**: Urban CQB, room-by-room clearing, targeted part dismantling, and civilian collateral shielding.

```text
+=====================================================================+
|                  UCD TACTICAL INTERDICTION HUD                      |
+=====================================================================+
| [BREACH TOPOLOGY] : Node 1 through Node 7 Ingress Clearance Grid    |
| [PART TARGETING]  : Exoskeleton / Weapon Manifold / Entity Core HP  |
| [FORENSIC HACK]   : Yuna Cipher Progress (%) & Terminal Override    |
| [CIVILIAN CORDON] : Hostage Berth Integrity & Foundation Shield HP  |
+=====================================================================+
```

### 4.1 Targeted Part Dismantling Engine (Part-Breaking)

UCD bosses possess multiple distinct structural and biological modules. Rather than depleting a generic health bar, UCD strike teams dismantle enemy capabilities part by part:

- **Exoskeleton Chassis**: Provides high physical armor and kinetic resistance. Smashing the chassis reduces target defense to 0 and exposes the pilot.
- **Weapon Manifolds & Conduits**: Powers high-damage offensive skills (e.g., Sura's chemical sprayer, Boknam's steam winch, Man-sik's golden cudgel). Severing the manifold permanently deletes the associated boss skill.
- **Contraband Entity Cores**: Powers the boss's elemental Overdrive. Soojin's leaded containment traps isolate the core, preventing catastrophic environmental leaks.

### 4.2 In-Combat Forensic Decryption (Auditor Yuna)

While vanguard officers hold the clash line, UCD auditors execute mid-combat digital forensics:
- **Ledger Seizure**: Each turn, Yuna decrypts enemy financial registers, progressively disabling boss buffs and uncovering corrupt patron networks.
- **Frequency Jams**: Transmits counter-frequencies to scramble syndicate radios, disorienting enemy enforcer squads and canceling their support fire.

### 4.3 Civilian & Foundation Shielding (Commander Taeho)

In UCD operations, victory requires zero civilian casualties and preserving civic infrastructure:
- **Phalanx Bastion Deployment**: Commander Taeho anchors his Obsidian shield between enemy AoE attacks and civilian holding pens.
- **Collateral Gauge**: If stray bullets or explosions damage the municipal foundations, the Collateral Gauge rises. Exceeding 100% causes cavern collapse and operational failure.

---

## V. Branch 4: Somnarak Exploration Decree (SED) Style

**Operational Domain**: Lightless geological karst caverns, boiling aquifers, and the Mugenhan Ocean (-50m to -3,500m).  
**Doctrine**: Strata depth survival, acoustic decibel management, long-range reconnaissance, and relic excavation.

```text
+=====================================================================+
|                   SED ABYSSAL EXPEDITION HUD                        |
+=====================================================================+
| [DEPTH PRESSURE]  : Hydrostatic/Tectonic Bar Pressure (-50m to Core)|
| [ACOUSTIC SONAR]  : Decibel Noise Meter (dB) & Behemoth Sleep Level |
| [SURVIVAL TIMERS] : Oxygen Reserves, Lantern Fuel, Thermal Heatsinks|
| [SEISMIC ANCHORS] : Tectonic Pitons & Cable Suspension Integrity    |
+=====================================================================+
```

### 5.1 Strata Atmospheric Depth Pressure Engine

As SED specialists descend deeper into the planetary mantle, the crushing physical and metaphysical weight of subterranean sorrow imposes severe operational penalties:

| Stratum & Depth Band | Atmospheric Pressure | Environmental Composure Drain | Operational Combat Penalties |
|---|---|---|---|
| **Stratum 1 (0m to -150m)** | 1.0 to 1.5 Bar | -2 SP per 3 turns | Standard combat; minor footing penalties |
| **Stratum 2 (-150m to -500m)** | 1.5 to 3.0 Bar | -4 SP per 3 turns | Movement speed reduced by 15%; thermal wear |
| **Stratum 3 (-500m to -1,200m)** | 3.0 to 6.5 Bar | -6 SP per 3 turns | Toxic runoff; chemical suit integrity checks |
| **Stratum 4 (-1,200m to -2,000m)** | 6.5 to 9.0 Bar | -8 SP per 2 turns | Crushing gravity; speed reduced by 30% |
| **Stratum 5 (-2,000m to -2,600m)** | 9.0 to 11.5 Bar | -10 SP per 2 turns | Tectonic tremors; required seismic anchoring |
| **Stratum 6 (-2,600m to -2,800m)** | 11.5 to 13.5 Bar| -12 SP per turn | Supercritical Han currents; acoustic interference |
| **Stratum 7 (-2,800m to Core)** | 13.5 to 15.0+ Bar| -15 SP per turn | Primordial Nadir; Singularity diving rigs required |

### 5.2 Acoustic Stealth & Sonar Decibel Meter

Subterranean karst strata are inhabited by ancient, dormant Sorrow Beasts and colossal slumbering entities:
- **Decibel Accumulation**: High-noise kinetic weapons (shotguns, heavy demolition charges) generate noise spikes (+20 to +40 dB).
- **The Awakening Threshold**: If the squad's cumulative noise exceeds the sector's ambient acoustic threshold (typically 100 dB), slumbering behemoths awaken and join the battle as third-party hostiles.
- **Stealth Takedowns**: Encourages suppressed weapons, silenced stilettos, and acoustic dampening fields to resolve skirmishes silently.

### 5.3 Survival Resource Timers

Every SED combat round tracks essential survival consumables:
- **Oxygen Supply**: Depleted every turn; puncturing an environmental suit imposes a rapid 3-turn suffocation timer.
- **Lantern Burn**: Han-lanterns ward off the supernatural darkness of the abyss. If fuel runs out, all agents suffer absolute blindness and panic.
- **Tectonic Pitons**: Specialists fire heavy steel pitons into cavern walls to maintain elevated sniper perches and avoid falling into bottomless abyssal fissures.

---

## VI. Comparative Style Synthesis Matrix

| Tactical Dimension | Generic P.S. Core | Reverie Directorate (R.D.) | Underworld Cleanup (UCD) | Exploration Decree (SED) |
|---|---|---|---|---|
| **Primary Environment** | Universal Baseline | High-Security Vaults | Urban Slums & Basements | Abyssal Karst Caverns |
| **Operational Goal** | Universal Clash Victory | Containment & Work Cycles | Demolition & Arrests | Survival & Excavation |
| **Signature System** | Dual Stagger & Clashes | Echo-Core Floor Resonance | Targeted Part-Dismantling | Depth Pressure & Sonar |
| **Unique Resource** | SP (-45 to +45) & Han Gauge | Han-Energy & Meltdown Clock | Forensic Decryption % | Oxygen & Decibel Meter |
| **Equipment Focus** | Quadripartite M.A.W. | Floor-Attuned M.A.W. | Armored Shields & Rams | Deep-Diving Singularity Rigs|
| **Boss Structure** | Single Health & Stagger | Meltdown Multi-Phase | Multi-Part Modular Chassis | Environmental Colossi |
| **Allied Casualties** | Defeat on Team Wipe | Stasis / Vault Recovery | Permanent Loss / Trial | Lost in the Endless Abyss |
| **Collateral Metric** | None | Facility Structural Meltdown | Civilian & Foundation Gauge | Cavern Collapse / Awakening |

---

### Master Archive Status

- **Codex Designation**: `SOMNARAK-TAC-04-A`
- **Compiler**: General Staff Coalition (R.D. / UCD / SED)
- **Authority**: High Council Supreme Tactical Directive
- **Baseline Standard**: 100% Authoritative V.1.0 Standard
"""

check_banned(styles_content, "SOMNARAK_BATTLE_SYSTEM_STYLES.md")

# Write SOMNARAK_BATTLE_SYSTEM_STYLES.md
out_path = "SOMNARAK-WORLD/Master_Codices/SOMNARAK_BATTLE_SYSTEM_STYLES.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(styles_content)
print(f"Generated {out_path} ({len(styles_content)} chars)")

# Now read existing SOMNARAK_BATTLE_SYSTEM.md and integrate the Four Styles overview
with open("SOMNARAK-WORLD/Master_Codices/SOMNARAK_BATTLE_SYSTEM.md", "r", encoding="utf-8") as f:
    bat_text = f.read()

# Add Section VII to SOMNARAK_BATTLE_SYSTEM.md
section_vii = """
---

## VII. The Four Operational Combat Styles (사대 전투 양식)

Combat doctrine across Somnarak is codified into four distinct operational branches, formally detailed in `SOMNARAK_BATTLE_SYSTEM_STYLES.md`:

1. **Generic P.S. Combat Core (The Universal Engine)**: Universal mechanics of Speed Dice, Clash resolution, SP Composure (-45 to +45), Sorrow Gauges (0–100%), Dual-Threshold Stagger (60% and 25%), and Quadripartite M.A.W. armaments.
2. **Reverie Directorate (R.D.) Style**: Facility containment operations governed by the **Nine Echo-Cores** (Floors 1 to 8), mid-combat Work Cycle execution (Ferrehan, Flerehan, Pugnahan, Viderehan), emergency sector lockdown gates, and multi-color Ordeal suppression.
3. **Underworld Cleanup Descend (UCD) Style**: Urban CQB across The Raw, featuring **Targeted Part Dismantling** (shattering enemy exoskeletons and weapon manifolds), in-combat forensic auditing by Yuna, and non-lethal hostage/foundation preservation behind Taeho's Obsidian Bastion.
4. **Somnarak Exploration Decree (SED) Style**: Subterranean abyssal descents governed by **Strata Depth Atmospheric Pressure** (-50m to -3,500m), acoustic sonar decibel stealth to prevent awakening dormant behemoths, oxygen/fuel burn timers, and seismic piton anchoring.

*(For full mathematical formulas, HUD wireframes, and turn flowcharts, refer to the authoritative master codex: `SOMNARAK_BATTLE_SYSTEM_STYLES.md`).*
"""

if "## VII. The Four Operational Combat Styles" not in bat_text:
    bat_text = bat_text.rstrip() + "\n" + section_vii

check_banned(bat_text, "SOMNARAK_BATTLE_SYSTEM.md")

with open("SOMNARAK-WORLD/Master_Codices/SOMNARAK_BATTLE_SYSTEM.md", "w", encoding="utf-8") as f:
    f.write(bat_text)
print("Updated SOMNARAK-WORLD/Master_Codices/SOMNARAK_BATTLE_SYSTEM.md")
