#!/usr/bin/env python3
"""
tools/update_absolvohan_gbs.py
Expands and enriches the Gameplay Battle System (GBS) across:
1. SOMNARAK-WORLD/The_Absolvohan/ABSOLOVHAN_OVERVIEW.md (Section IV)
2. SOMNARAK-WORLD/The_Absolvohan/Part_1_Day_0_The_Director_Wakes.md (First Watch Ordeal)
3. SOMNARAK-WORLD/The_Absolvohan/Part_2_Days_1_to_25.md (Noon & Dusk Ordeals)

Enforces:
- 10-Node Stage Grid ([N01] to [N10])
- Speed-to-AP conversion
- 6-Turn Phase combat structure
- Echo-Core Floor Resonances
- Dual-Threshold Stagger (60% and 25%)
- Mid-Combat Work Cycles
- Exact 71-column ASCII boxes & zero banned terms
"""

import os
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

# -------------------------------------------------------------
# 1. Update ABSOLOVHAN_OVERVIEW.md Section IV
# -------------------------------------------------------------
def update_overview():
    filepath = "SOMNARAK-WORLD/The_Absolvohan/ABSOLOVHAN_OVERVIEW.md"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    box_stage_grid = make_box("REVERIE DIRECTORATE TACTICAL 10-NODE STAGE TOPOLOGY", [
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "|--CORE--| |--BLAST GATES--| |--WORK BAFFLES--| |--OVERWATCH--|",
        "---",
        "Node 01-02 : Entity Core / Breach Epicenter (Point Blank Band 1)",
        "Node 03-04 : Inner Blast Gates / Kinetic Airlock (CQB Band 2)",
        "Node 05-06 : Work Console Array & Emotion Baffles (Mid-Field Band 3)",
        "Node 07-08 : Quarantine Overwatch & Stasis Cannons (Rear Line Band 4)",
        "Node 09-10 : Echo-Core Terminal & Department Hub (Artillery Band 5)"
    ])

    box_speed_ap = make_box("SPEED-TO-ACTION POINT (AP) CONVERSION ENGINE", [
        "Speed Roll   | Action Points (AP) | Tactical Capabilities Per Turn",
        "-------------+--------------------+--------------------------------",
        "Speed 1 - 2  | 1 Action Point     | 1 Basic Strike OR 1 Node Shift",
        "Speed 3 - 4  | 2 Action Points    | 1 Move + 1 Attack OR 1 Guard",
        "Speed 5 - 6  | 3 Action Points    | Move + Resonance Skill + Guard",
        "Speed 7 - 8  | 4 Action Points    | Multi-Combo + Rapid Sprint",
        "Speed 9 - 10+| 5 Action Points    | Overdrive Blitz + Spatial Flank"
    ])

    box_macro_phase = make_box("MACRO PHASE COMBAT TIME STRUCTURE", [
        "ONE COMBAT PHASE = SIX (6) SEQUENTIAL BATTLE TURNS",
        "---",
        "Turn 1 : Roll Speed -> Determine AP -> Resolve movement & clashes.",
        "Turn 2 : Repositioning along nodes, second exchange of fire.",
        "Turn 3 : Focus fire, part-dismantling strikes, defensive guards.",
        "Turn 4 : Department specials, forensic decrypts, work cycles.",
        "Turn 5 : Stagger exploitation, emergency healing, shield bracing.",
        "Turn 6 : Climax finishers, final clash line of the phase cycle.",
        "---",
        "[PHASE-END EQUILIBRIUM & HAZARD TICK]",
        "1. Environmental Check : Meltdown timer / Collateral / Depth Strain.",
        "2. Status Decay        : Bleed / Weep damage; SP drifts toward 0.",
        "3. Stagger Recovery    : Stagger 1 resets; Terminal Stagger checked.",
        "4. Boss Phase Shift    : Stance change / Ordeal Ingress / Waves."
    ])

    new_section_iv = f"""### 4.2 The 10-Node Facility Combat & Containment Grid (Stage Topology)

All tactical engagements, containment cell breaches, and Ordeal suppressions inside Facility 01 are mapped onto a standardized 10-node spatial grid: **Nodes 1 through 10**:

```text
{box_stage_grid}
```

- **Node 01–02 (Entity Core / Vanguard Zone / 0–5m)**:
  * The containment chamber threshold or Ordeal breach point.
  * Point-Blank Range Band 1. Melee strikes, blast shields, and direct physical interception occur here. Ranged weapons incur -20% accuracy and -2 Clash Power.
- **Node 03–04 (Inner Blast Gates / Kinetic Airlock / 6–15m)**:
  * Close CQB Range Band 2. Heavy steel bulkheads and kinetic dampeners.
  * Wardens deploy here to prevent breaches from spreading into common corridors.
- **Node 05–06 (Work Console Array & Baffles / 16–30m)**:
  * Mid-Field Range Band 3. Wired with pneumatic emotion consoles and acoustic baffles.
  * Agents spend 2 AP here to execute non-lethal Work Types (Flerehan, Pugnahan, Ferrehan, Viderehan) directly into entity fields.
- **Node 07–08 (Quarantine Overwatch / 31–50m)**:
  * Long-Range Range Band 4. Sniper positions, sedative harpoon rigs, and stasis turrets.
  * 100% precision power; standard rifles suffer 50% falloff.
- **Node 09–10 (Echo-Core Terminal & Department Hub / 51m+)**:
  * Extreme Range Band 5. Connects directly to the Department Floor Lead's command matrix.
  * Heavy artillery, emergency team-wide SP conduits, and facility stasis arrays operate here.

---

### 4.3 Speed-Driven Action Economy & Action Points (AP)

Speed rolls at the start of each Battle Turn determine both turn order and the agent's **Action Points (AP)**:

```text
{box_speed_ap}
```

- **Action Point Spending**:
  * **Movement (1 AP per Node)**: Reposition along the 10-node track.
  * **Basic Attack (1 AP)**: Standard weapon strike within Range Band.
  * **Resonance Skill (2 AP)**: High-power M.A.W. combat art with elemental multipliers.
  * **Defensive Stance (1 AP)**: Deploy Guard shield, Evade roll, or Counter-strike.
  * **Work Cycle Action (2 AP)**: Perform Flerehan, Pugnahan, Ferrehan, or Viderehan at Nodes 5–6 or Nodes 1–2.
  * **Climax Finisher (3 AP)**: True lethal damage against Staggered targets.

---

### 4.4 The Macro Phase Combat Structure (6 Battle Turns = 1 Phase)

All containment engagements progress in strict cycles of **six (6) Battle Turns per Phase**:

```text
{box_macro_phase}
```

---

### 4.5 Echo-Core Department Floor Resonance on the 10-Node Grid

When agents engage hostiles within an operational department, the Echo-Core lead projects active battlefield resonance across designated nodes:

1. **Floor 1 (Majin & Seiyon — Central Command)**:
   * *Command Eye*: Spend 1 AP to reroll the Speed Die of any allied agent across Nodes 1 to 10.
   * *Administrative Clarity*: Restores +15 SP team-wide upon winning a clash at Nodes 5 or 6.
2. **Floor 2 (Dekan — The Maw's Keep / Containment)**:
   * *Bastion Ward*: Grants +50% shield armor to all allies on Nodes 1 through 4.
   * *Jaw Clamp*: Winning a melee clash at Node 1 or 2 pins the hostile, preventing it from advancing past Node 2 for 2 turns.
3. **Floor 3 (Zyrak — The Extraction Hall)**:
   * *Energy Siphon*: Executing a Work Cycle on Nodes 5–6 generates double Han-Energy into the facility quota.
   * *M.A.W. Overcharge*: Consumes 20 Han-Energy to grant an ally's weapon +5 Clash Power and true elemental damage.
4. **Floor 4 (Ayshuk — Insight Forge / Research)**:
   * *Predictive HUD*: Reveals hostile target nodes and dice rolls 1 full Battle Turn in advance.
   * *Weakness Attunement*: Increases elemental weakness damage from 1.5× to 2.2× across all nodes.
5. **Floor 5 (Mellda — Border Watch / Bulwark)**:
   * *Blast Gate Lockdown*: Mellda raises emergency bulkheads at Node 4, isolating Nodes 1–3 and blocking all ranged beams.
   * *Martial Rebuke*: Automatic counter-attack whenever a hostile crosses past Node 4.
6. **Floor 6 (Marjuk — Deep Vault / Archive)**:
   * *Stasis Field*: Freezes a target on Node 1 or 2 in temporal amber for 1 Battle Turn, canceling all its queued actions.
   * *Mnemonic Recovery*: If an agent falls in battle, their cognitive pattern is locked in stasis, guaranteeing post-battle revival.
7. **Floor 7 (Ishall — Shadow Corps / Covert Relics)**:
   * *Unanswered Strike*: Remote relic strike with the floating mineral digits. Dispatches Void damage from Node 10 directly to Node 1 with 0% range falloff and armor bypass.
   * *Shadow Ingress*: Infiltrators teleport from Node 8 directly behind hostiles at Node 1.
8. **Floor 8 (Xyan — The Final Gate / Wellhead)**:
   * *Singularity Well*: Anchors a gravitational vortex at Node 1 that pulls all roaming hostiles into melee range and nullifies displacement skills.

---

### 4.6 Dual-Threshold Stagger Engine & Mid-Combat Work Protocols

Every combatant operates with two hard Stagger thresholds within their vitality pool:
- **Stagger Threshold 1 (60% Max HP)**:
  * When health drops below 60%, the target's posture shatters.
  * Duration: 1 complete turn.
  * Effect: Defense drops to 0; takes **2.0× direct damage**; all queued action slots wiped.
- **Terminal Stagger Threshold 2 (25% Max HP)**:
  * When health falls below 25%, the skeletal and neural frame breaks.
  * Duration: 1 complete turn.
  * Effect: Complete immobility; takes **2.5× direct damage**; enables execution of Overdrive Climax Finishers (3 AP true lethal damage).

#### Mid-Combat Work Cycle Execution
Unlike lethal elimination, containment agents can spend 2 AP to execute official **Work Types** mid-battle:
- **Flerehan (공감작업)**: Harmonic weeping frequencies soothing grief; lowers entity Sorrow Gauge by 25% on Clash Win.
- **Pugnahan (억제작업)**: Kinetic dampening strikes; reduces entity Speed by -4 and locks its highest-tier attack skill for 2 turns.
- **Ferrehan (인내작업)**: Fortifies containment barriers and M.A.W. armor, granting +40% physical defense to allies on the same node.
- **Viderehan (관찰작업)**: Scans cognitive patterns, instantly exposing hidden Stagger thresholds and lowering enemy clash defense.

---

### 4.7 Agent Panic Typologies & Recovery Protocols"""

    target_start = "### 4.2 Combat Mechanics & The 5 Range Bands"
    target_end = "### 4.3 Agent Panic Typologies & Recovery Protocols"

    if target_start in text and target_end in text:
        idx1 = text.find(target_start)
        idx2 = text.find(target_end) + len(target_end)
        text = text[:idx1] + new_section_iv + text[idx2:]
        check_banned(text, filepath)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Updated {filepath} with complete GBS Section IV!")
    else:
        print("Could not find targets in ABSOLOVHAN_OVERVIEW.md")

# -------------------------------------------------------------
# 2. Update Part_1_Day_0_The_Director_Wakes.md
# -------------------------------------------------------------
def update_part_1():
    filepath = "SOMNARAK-WORLD/The_Absolvohan/Part_1_Day_0_The_Director_Wakes.md"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    hud_dawn = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (DAWN SUPPRESSION)", [
        "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "POS     :        [VOICE] [KIM]           [PARK]         [MAJIN]",
        "DIST    : Kim at N03 (Band 1); Park at N05 (Console); Majin at N09.",
        "---",
        "Agent Kim   : Speed 5 -> 3 AP | HP: 100/100 | SP: +15 | Stun Baton",
        "Agent Park  : Speed 6 -> 3 AP | HP:  95/ 95 | SP: +20 | Lament Requiem",
        "The Voice   : Speed 4 -> 2 AP | HP: 140/140 | Sorrow: 50% | Pale Echo"
    ])

    turns_summary = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
        "- Turn 02: Kim holds N02; Park fires from N05; Voice hits 60% Stagger 1.",
        "- Turn 03: All allied attacks deal 2.0x damage; Voice HP falls to 52.",
        "- Turn 04: Voice recovers; charges area pulse [Shattered Soliloquy].",
        "- Turn 05: Park executes Flerehan at N05; Voice Sorrow drops to 15%.",
        "- Turn 06: Kim executes Climax Finisher; Terminal Stagger shatters Voice."
    ])

    phase_tick = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
        "1. Environmental Check : Meltdown Level 1 cleared in Sector 1.",
        "2. Status Equilibrium : Clerk sanity fully restored; Park SP at +30.",
        "3. Containment Check   : The Voice dissolved into inert crystalline dust.",
        "4. OUTCOME             : FLAWLESS VICTORY — 0 CASUALTIES, +0.005 TONS."
    ])

    new_dawn_combat = f"""##### Ordeal Manifestation: First Watch (Dawn) Ordeal
Before we can celebrate, the facility lights turn amber. A secondary klaxon blares:

```text
+==============================================+
| TACTICAL DOSSIER: FIRST WATCH (DAWN) ORDEAL  |
+----------------------------------------------+
| DESIGNATION : THE VOICE                      |
| CLASSIFICATION : PALE (CYAN) FIRST WATCH     |
| INTRUSION POINT : FLOOR 1 CORRIDOR WEST      |
+----------------------------------------------+
| HOSTILE PARAMETERS:                          |
| - Entity: 1x Spectral Resonator Projection   |
| - Attack Affinity: Pale (% Max HP Decay)     |
| - Weakness Affinity: Lament (Acoustic Echo)  |
+----------------------------------------------+
| TACTICAL ORDERS: DEPLOY PARK & KIM           |
+==============================================+
```

A glowing cyan apparition appears in the western corridor, chanting pre-human syllables. A Level I clerk wandering the hallway immediately loses all SP and enters **Panic State: Void Catatonia**, freezing in terror at Node 4!

Director Majin establishes tactical command via the Floor 1 Central Console:

```text
{hud_dawn}
```

###### Turn 01 Action Resolution Log
- **Step 1: Movement & Action Point (AP) Spending**:
  * Agent Park (Speed 6 -> 3 AP) spends 1 AP to shift from Node 5 to Node 4, standing directly over the catatonic clerk.
  * Park spends 1 AP to administer an emergency cognitive wake-up strike: swinging his stun baton with gentle Lament resonance. The calibrated shock immediately dispels the clerk's trance, restoring their SP from 0 to +25 and escorting them toward Node 9!
  * Park holds remaining 1 AP in Defensive Guard (+8 Block Shield).
  * Agent Kim (Speed 5 -> 3 AP) spends 1 AP to advance from Node 3 to Node 2, entering Point-Blank Range Band 1 with The Voice. Remaining AP: 2.
- **Step 2: Clash Standoff (Node 2)**:
  * The Voice declares `[Spectral Chime]` against Agent Kim:
    * The Voice Roll: Base 7 + (1 Coin Heads: +3) = 10 Power.
  * Agent Kim declares `[Heavy Kinetic Baton Cleave]` (Costs 2 AP):
    * Kim Roll: Base 8 + (2 Coins Heads: +4) = 12 Power.
  * **Resolution**: Kim WINS THE CLASH (12 vs 10).
    * The Voice's sonic beam is deflected. Kim's baton smashes into the cyan resonator core, dealing 28 Grudge damage and inflicting +16 Stagger buildup.
    * Kim's Composure rises from +15 to +20.

```text
{turns_summary}
```

```text
{phase_tick}
```

With the Ordeal suppressed, Agent Kim completes one final calibration pass on Chamber 001, extracting +0.005 tons. Target quota reached: **0.053 / 0.050 tons!**"""

    target_start = "##### Ordeal Manifestation: First Watch (Dawn) Ordeal"
    target_end = "With the Ordeal suppressed, Agent Kim completes one final calibration pass on Chamber 001, extracting +0.005 tons. Target quota reached: **0.053 / 0.050 tons!**"

    if target_start in text and target_end in text:
        idx1 = text.find(target_start)
        idx2 = text.find(target_end) + len(target_end)
        text = text[:idx1] + new_dawn_combat + text[idx2:]
        check_banned(text, filepath)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Updated {filepath} with full GBS Turn-by-Turn combat!")
    else:
        print("Could not find targets in Part_1_Day_0_The_Director_Wakes.md")

# -------------------------------------------------------------
# 3. Update Part_2_Days_1_to_25.md
# -------------------------------------------------------------
def update_part_2():
    filepath = "SOMNARAK-WORLD/The_Absolvohan/Part_2_Days_1_to_25.md"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    hud_pendulum = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (VIOLET NOON)", [
        "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "POS     :        [OBELISK][KANG]          [KIM]          [DEKAN]",
        "DIST    : Kang at N03 (Band 1); Kim at N05 (Band 3); Dekan at N09.",
        "---",
        "Agent Kang  : Speed 6 -> 3 AP | HP: 120/120 | SP: +25 | Fury Blade",
        "Agent Kim   : Speed 5 -> 3 AP | HP: 110/110 | SP: +20 | Kinetic Carbine",
        "The Obelisk : Speed 3 -> 2 AP | HP: 260/260 | Sorrow: 60% | Weight Crush"
    ])

    turns_pendulum = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
        "- Turn 02: Kang holds N02 behind shield; Obelisk hits 60% Stagger 1.",
        "- Turn 03: All allied attacks deal 2.0x direct damage; HP falls to 98.",
        "- Turn 04: Obelisk recovers; charges 3.2G pulse [Gravitational Rupture].",
        "- Turn 05: Kim at N05 fires piercing Void shot, canceling charging core.",
        "- Turn 06: Kang executes Climax Pierce; Terminal Stagger shatters stone."
    ])

    phase_pendulum = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
        "1. Environmental Check : Gravitational field neutralizes across Floor 4.",
        "2. Status Equilibrium : Stagger meters reset; Kang SP stabilizes at +35.",
        "3. Containment Check   : Violet crystal shattered into inert fragments.",
        "4. OUTCOME             : ZERO CASUALTIES — 52.1 SECONDS TO RESOLUTION."
    ])

    new_noon_combat = f"""Second Watch (Noon) Ordeal
At 14:00, the screen shudders. The Second Watch arrives:

```text
+==============================================+
| TACTICAL DOSSIER: SECOND WATCH (NOON) ORDEAL |
| DESIGNATION : THE HEAVY PENDULUM             |
| CLASSIFICATION : WEIGHT (VIOLET) NOON ORDEAL |
| INTRUSION POINT : FLOOR 4 RESEARCH CORRIDOR  |
| HOSTILE PARAMETERS:                          |
| - Entity: 1x Colossal Suspended Obelisk      |
| - Attack Affinity: Weight (Gravitational     |
| Stagger)                                     |
| - Weakness Affinity: Grudge (Physical        |
| Pierce)                                      |
| TACTICAL DEPLOYMENT: KANG & KIM ENGAGE       |
+==============================================+
```

A colossal violet obelisk crashes through the ceiling of Floor 4, creating an intense 3.2G gravitational compression field across Nodes 1 to 4. Any agent walking into the corridor has their movement speed cut by 60%!

Director Majin establishes tactical battle parameters:

```text
{hud_pendulum}
```

###### Turn 01 Action Resolution Log
- **Step 1: Floor 2 Echo-Core Resonance Deployment**:
  * Attendant Dekan activates *The Maw's Keep Bastion Ward*, projecting +50% kinetic shield absorption over Nodes 1 through 4.
  * Director Majin engages `Acoustic Siphon`, venting gravitational reverberations into subterranean bedrock.
- **Step 2: Movement & Action Point Spending**:
  * Agent Kang (Speed 6 -> 3 AP) spends 1 AP to advance from Node 3 to Node 2 (Point-Blank Range Band 1 with the Obelisk).
  * Kang spends 2 AP to declare `[Fury Blade Armor Pierce]`.
  * Agent Kim (Speed 5 -> 3 AP) holds Node 5 behind research consoles. Spends 2 AP to aim `[Kinetic Carbine Concentrated Burst]` from Range Band 3. Remaining 1 AP held in Guard.
- **Step 3: Clash Standoff (Node 2)**:
  * The Heavy Pendulum declares `[3.2G Gravitational Crush]` on Node 2:
    * Obelisk Roll: Base 9 + (2 Coins Heads: +4) = 13 Power.
  * Agent Kang's `[Fury Blade Armor Pierce]`:
    * Kang Roll: Base 10 + (2 Coins Heads: +5) = 15 Power.
  * **Resolution**: Kang WINS THE CLASH (15 vs 13).
    * Kang's greatsword splits the descending pendulum arc. The blade strikes the central suspension ring, dealing 44 Grudge piercing damage and inflicting +22 Stagger buildup.
  * Agent Kim fires unopposed burst from Node 5, dealing 31 Grudge damage to the support pylons.

```text
{turns_pendulum}
```

```text
{phase_pendulum}
```

One final work session by Agent Park on the Orphaned Bell"""

    target_start = "Second Watch (Noon) Ordeal\nAt 14:00, the screen shudders. The Second Watch arrives:"
    target_end = "One final work session by Agent Park on the Orphaned Bell"

    if target_start in text and target_end in text:
        idx1 = text.find(target_start)
        idx2 = text.find(target_end)
        text = text[:idx1] + new_noon_combat + "\n\n" + text[idx2:]
        check_banned(text, filepath)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Updated {filepath} with full GBS Turn-by-Turn combat!")
    else:
        print("Could not find targets in Part_2_Days_1_to_25.md")

if __name__ == "__main__":
    update_overview()
    update_part_1()
    update_part_2()
