#!/usr/bin/env python3
"""
tools/apply_speed_range_maw_p_system.py
Implements:
1. Agent Base Speed & Range Attributes
2. M.A.W.-W (Weapon) Speed & Range Modifier Engine
3. The Four P-Framework:
   - P1: Passives (M.A.W.-W Weapon Passives & Operative Synergy)
   - P2: Panic (Mental Collapse, SP Mechanics, Burden & Recovery)
   - P3: Parry / Protection (Defensive Action System & Range Interceptions)
   - P4: Posture & Poise (Stagger Buildup & Kinetic Momentum Multipliers)

Target files:
- SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM.md
- SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM_STYLES.md
- SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md
- SOMNARAK-WORLD/The_Absolvohan/ABSOLOVHAN_OVERVIEW.md
"""

import sys
import re

banned_patterns = [
    r"\bego\b", r"\be\.g\.o\b", r"\babnormality\b", r"\babnormalities\b",
    r"\bdistortion\b", r"\bdistortions\b", r"\bpeccatula\b", r"\bfixer\b",
    r"\bfixers\b", r"\bassociation\b", r"\bassociations\b", r"\bthe fingers\b",
    r"\blobotomy\b", r"\blimbus\b", r"\blibrary of ruina\b", r"\byoung-ji\b",
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
# 1. Update SOMNARAK_BATTLE_SYSTEM.md
# -------------------------------------------------------------
def update_battle_system():
    filepath = "SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM.md"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    box_maw_mods = make_box("M.A.W.-W WEAPON SPEED & RANGE MODIFIERS ENGINE", [
        "Weight Class | Spd Mod | AP | Optimal Band | Trait Mechanics",
        "---",
        "Feather / UL | +2 Spd  | 1  | Band 1 (N01) | Momentum Surge (+2 Pwr)",
        "Light Class  | +1 Spd  | 1  | Band 1-2     | Rapid Flanking / Bleed",
        "Medium Class | +0 Spd  | 1  | Band 1-3     | Balanced Clash Profile",
        "Heavy Class  | -1 Spd  | 2  | Band 1 / B04 | Heavy Poise (+2 Base)",
        "Colossal Rel | -2 Spd  | 2  | Band 1 / B05 | Unstoppable (+4 Base)"
    ])

    box_four_p = make_box("THE FOUR P-FRAMEWORK (PASSIVE / PANIC / PARRY / POSTURE)", [
        "Pillar Code | Tactical Domain       | Core Battle Mechanical Function",
        "---",
        "P1: Passive | Weapon & Trait Arts   | Speed-delta triggers & range bonuses",
        "P2: Panic   | SP & Sanity Breakdown | Burden drain, panic states & recovery",
        "P3: Parry   | Active Defense & Guard| Melee deflects, shields & intercepts",
        "P4: Posture | Poise & Stagger Meter | Momentum math & dual-threshold breaks"
    ])

    new_section = f"""### Operative Base Speed & Range Classification on the 10-Node Grid

Every operative commanding weapons in Somnarak operates with an intrinsic **Base Speed Die** and **Natural Range Affinity** determined by training, augmentation tier, and physiological weight:

| Operative Role | Base Speed Die | Action Points (AP) | Natural Range | Optimal Tactical Role |
|---|---|---|---|---|
| **Vanguard Skirmisher** | Speed 5–8 | 3 to 4 AP | Band 1 (0–2m) | Node 1–2 Melee Interception, High Mobility |
| **Line Warden / Breacher** | Speed 3–6 | 2 to 3 AP | Band 1–2 (2–5m) | Node 2–3 Shield Bracing, CQB Clashing |
| **Mid-Field Specialist** | Speed 3–5 | 2 to 3 AP | Band 3 (5–12m) | Node 5–6 Console Work, Carbines, Healing |
| **Suppression Marksman** | Speed 4–7 | 2 to 4 AP | Band 4 (12–25m)| Node 7–8 Precision Sniping, Beam Lasers |
| **Ballast Heavy / Anchor** | Speed 2–4 | 1 to 2 AP | Band 1 or Band 5| Colossal Hammer Crushes, Artillery Shells |

---

### M.A.W.-W (Weapon) Speed & Range Modifier Engine

When equipping Materialized Agony Wear weaponry (**M.A.W.-W**), the weapon's emotional weight, physical density, and metaphysical reach modify the operative's baseline Speed and Range Band parameters:

```text
{box_maw_mods}
```

#### Range Band Penalties & Spatial Falloff Rules
1. **Point-Blank Penalty for Ranged Arms**: Any ranged weapon (Band 3–5) firing within Point-Blank melee distance (Band 1 / Nodes 1–2) incurs a penalty of **-2 Clash Power** and **-20% Accuracy**, unless fitted with an integrated bayonet or defensive buckler.
2. **Melee Reach Constraints**: Melee weapons cannot target hostiles beyond Band 2 (Nodes 3–4) without spending 1 AP per node of movement to close the gap. Striking at Band 2 with a strict Band 1 weapon incurs **-3 Clash Power**.
3. **Out-of-Band Falloff**:
   - Striking 1 Range Band beyond optimal: **-2 Clash Power**, **-15% Damage**.
   - Striking 2+ Range Bands beyond optimal: **-4 Clash Power**, **-35% Damage**.

---

### The Universal Four P-Framework (Passives, Panic, Parry, Posture)

All combatants and M.A.W. loadouts interact through four interconnected mechanical pillars known as **The Four P's**:

```text
{box_four_p}
```

#### P1: Passives (M.A.W.-W Weapon Passives & Operative Synergy)
Every M.A.W.-W weapon carries unique passive traits triggered by spatial positioning and speed differences:
- **Momentum Surge**: When an operative's Speed exceeds the target's Speed by 3 or more, gain **+2 Final Clash Power** and recover +1 AP on a clash win.
- **Point-Blank Dissection**: Striking an enemy at exact optimal Range Band 1 grants **+25% Critical Hit Chance** and applies 3 stacks of elemental Bleed or Weeping.
- **Overwatch Stance**: Remaining stationary on Nodes 7–8 for 1 full turn grants **+3 Clash Power** on subsequent ranged strikes and bypasses hostile cover.
- **Heavy Ballast Poise**: Heavy and Colossal weapons ignore the first 5 incoming Stagger damage sustained each turn.

#### P2: Panic (SP Mechanics, Mental Burden & Emergency Recovery)
Sanity (SP) dictates cognitive composure. Wielding high-tier M.A.W.-W equipment places heavy psychic strain on the wielder:
- **Equipment Burden Drain**: Equipping an α-to-ω M.A.W. weapon that exceeds the operative's clearance tier inflicts a passive drain of **-5 SP per turn**.
- **Panic State Typologies**: When SP hits 0, the operative collapses into one of four Panic States:
  * *Berserk Panic*: Operative loses control, gaining free 0 AP sprint to Node 1–2 and attacking the nearest ally or enemy with maximum AP.
  * *Despair Panic*: Operative freezes in place; Speed drops to 1 (1 AP); defense drops to 0; radiates weeping aura that damages ally SP.
  * *Wandering Panic*: Operative shifts randomly (+/- 2 nodes per turn), unlocking bulkhead seals and tripping hazard traps.
  * *Catatonic Panic*: Operative falls unconscious; Speed 0 (0 AP); posture broken; enters immediate Stagger state.
- **Panic Restoration**: An ally within Range Band 2–3 may spend 1 AP to deliver a soothing *Flerehan* communion or a non-lethal blunt Lament shock, restoring the panicked target's SP to +25.

#### P3: Parry & Protection (Active Defensive Actions)
Operatives may spend Action Points on reactive defensive techniques rather than attacks:
- **Parry Action (1 AP)**: Declared against an incoming melee clash. Operative rolls weapon defense die. If Parry Roll > Attack Roll, the operative completely deflects incoming damage and delivers an immediate riposte dealing **50% weapon base damage**.
- **Guard Shield (1 AP)**: Deploys a stationary directional barrier that absorbs flat damage equal to `(Weapon Defense + Suit Defense) * Tier Multiplier`. Excess damage bleeds through to HP.
- **Evade Roll (1 AP)**: High-mobility defensive leap. If Evade Roll > Attack Roll, the operative takes 0 damage and shifts 1 node backward. If failed, takes full unmitigated damage.
- **Kinetic Interception**: Operatives positioned on Nodes 3–4 may spend 1 AP to interpose their shields in front of allies on Nodes 5–6, deflecting linear projectile lines.

#### P4: Posture & Poise (Stagger Buildup & Momentum Multipliers)
Posture represents physical balance and structural integrity before a Stagger break occurs:
- **Posture Meter**: Calculated as `Base Resilience + M.A.W. Weight Class Bonus`.
- **Kinetic Momentum Multiplier**: Striking with higher speed magnifies posture damage. Bonus Posture Damage = `(Attacker Speed - Defender Speed) * Weapon Weight Multiplier`.
- **Posture Shatter**: Depleting the Posture meter triggers **Dual-Threshold Stagger**:
  * *Stagger Threshold 1 (60% Max HP)*: Posture broken for 1 turn; 0 defense; takes **2.0× direct damage**; all queued action slots wiped.
  * *Terminal Stagger 2 (25% Max HP)*: Neural and physical collapse; 1 turn complete paralysis; takes **2.5× direct damage**; unlocks 3 AP Climax Execution Finishers."""

    target_anchor = "### Multi-Target Line & AoE Falloff Mechanics (다중 대상 감쇄 규칙)"
    if target_anchor in text:
        idx = text.find(target_anchor)
        text = text[:idx] + new_section + "\n\n---\n\n" + text[idx:]
        check_banned(text, filepath)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Updated {filepath} successfully!")
    else:
        print("Target anchor not found in SOMNARAK_BATTLE_SYSTEM.md")

# -------------------------------------------------------------
# 2. Update SOMNARAK_BATTLE_SYSTEM_STYLES.md
# -------------------------------------------------------------
def update_styles():
    filepath = "SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM_STYLES.md"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    box_maw_mods = make_box("M.A.W.-W WEAPON SPEED & RANGE MODIFIERS ENGINE", [
        "Weight Class | Spd Mod | AP | Optimal Band | Trait Mechanics",
        "---",
        "Feather / UL | +2 Spd  | 1  | Band 1 (N01) | Momentum Surge (+2 Pwr)",
        "Light Class  | +1 Spd  | 1  | Band 1-2     | Rapid Flanking / Bleed",
        "Medium Class | +0 Spd  | 1  | Band 1-3     | Balanced Clash Profile",
        "Heavy Class  | -1 Spd  | 2  | Band 1 / B04 | Heavy Poise (+2 Base)",
        "Colossal Rel | -2 Spd  | 2  | Band 1 / B05 | Unstoppable (+4 Base)"
    ])

    box_four_p = make_box("THE FOUR P-FRAMEWORK (PASSIVE / PANIC / PARRY / POSTURE)", [
        "Pillar Code | Tactical Domain       | Core Battle Mechanical Function",
        "---",
        "P1: Passive | Weapon & Trait Arts   | Speed-delta triggers & range bonuses",
        "P2: Panic   | SP & Sanity Breakdown | Burden drain, panic states & recovery",
        "P3: Parry   | Active Defense & Guard| Melee deflects, shields & intercepts",
        "P4: Posture | Poise & Stagger Meter | Momentum math & dual-threshold breaks"
    ])

    new_section_styles = f"""### 2.3 Operative Base Speed & Range Classification on the 10-Node Grid

Every combat operative commands an intrinsic **Base Speed Die** and **Natural Range Band** on the 10-node spatial grid:
- **Vanguard Skirmisher**: Speed 5–8 (3–4 AP), Band 1 (Nodes 1–2). Intercepts frontline breaches.
- **Line Warden / Breacher**: Speed 3–6 (2–3 AP), Band 1–2 (Nodes 2–4). Deploys heavy shields and kinetic parries.
- **Mid-Field Specialist**: Speed 3–5 (2–3 AP), Band 3 (Nodes 5–6). Operates consoles, acoustic weapons, and field healing.
- **Suppression Marksman**: Speed 4–7 (2–4 AP), Band 4 (Nodes 7–8). Provides precision overwatch snipes and laser suppression.
- **Ballast Heavy / Anchor**: Speed 2–4 (1–2 AP), Band 1 or 5 (Nodes 1 or 9–10). Delivers catastrophic maul smashes and mortar artillery.

---

### 2.4 M.A.W.-W (Weapon) Speed & Range Modifier Engine

Equipping Materialized Agony Wear weaponry (**M.A.W.-W**) applies mechanical modifications to the operative's baseline speed, Action Point economy, and engagement range:

```text
{box_maw_mods}
```

---

### 2.5 The Universal Four P-Framework Across All Branches

Every institutional combat style executes the universal **Four P-Framework**:

```text
{box_four_p}
```

1. **P1: Passives**:
   - *Momentum Surge*: Gain +2 Clash Power when Speed > enemy Speed by 3+.
   - *Point-Blank Dissection*: +25% Critical Hit Chance at optimal Band 1.
   - *Overwatch Anchor*: +3 Clash Power from Bands 4–5 when remaining stationary for 1 turn.
   - *Heavy Ballast Poise*: Heavy weapons ignore the first 5 Stagger buildup per turn.
2. **P2: Panic (SP & Mental Burden)**:
   - *Burden Drain*: Wielding M.A.W.-W exceeding clearance tier drains -5 SP per turn.
   - *Panic Typologies*: Berserk (0 AP sprint to Node 1), Despair (Speed 1, 0 defense), Wandering (random node shifts), Catatonic (Speed 0, instant Stagger).
   - *Panic Recovery*: Allies at Band 2–3 spend 1 AP on Flerehan communion or non-lethal blunt Lament shock to restore SP to +25.
3. **P3: Parry & Protection**:
   - *Parry (1 AP)*: Roll defense die vs melee attack; winning deflects 100% damage and counters for 50% weapon power.
   - *Guard Shield (1 AP)*: Directional barrier absorbing flat damage based on weapon and suit defense.
   - *Evade Roll (1 AP)*: Full mobility dodge; 0 damage on win, full damage on loss.
   - *Kinetic Interception*: Wardens at Nodes 3–4 spend 1 AP to deflect linear projectile lines targeting allies at Nodes 5–6.
4. **P4: Posture & Poise**:
   - Posture meter = `Base Resilience + M.A.W. Weight Bonus`.
   - Momentum Multiplier = `(Attacker Speed - Defender Speed) * Weapon Weight Multiplier`.
   - Depleting Posture triggers Dual-Threshold Stagger: Stagger 1 (60% HP, 2.0x damage) and Terminal Stagger 2 (25% HP, 2.5x damage)."""

    target_anchor = "## V. Branch 1: Generic P.S. Combat Core (The Universal Engine)"
    if target_anchor in text:
        idx = text.find(target_anchor)
        text = text[:idx] + new_section_styles + "\n\n---\n\n" + text[idx:]
        check_banned(text, filepath)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Updated {filepath} successfully!")
    else:
        print("Target anchor not found in SOMNARAK_BATTLE_SYSTEM_STYLES.md")

# -------------------------------------------------------------
# 3. Update SOMNARAK_MAW_CODEX.md
# -------------------------------------------------------------
def update_maw_codex():
    filepath = "SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    box_maw_mods = make_box("M.A.W.-W WEAPON SPEED & RANGE MODIFIERS ENGINE", [
        "Weight Class | Spd Mod | AP | Optimal Band | Trait Mechanics",
        "---",
        "Feather / UL | +2 Spd  | 1  | Band 1 (N01) | Momentum Surge (+2 Pwr)",
        "Light Class  | +1 Spd  | 1  | Band 1-2     | Rapid Flanking / Bleed",
        "Medium Class | +0 Spd  | 1  | Band 1-3     | Balanced Clash Profile",
        "Heavy Class  | -1 Spd  | 2  | Band 1 / B04 | Heavy Poise (+2 Base)",
        "Colossal Rel | -2 Spd  | 2  | Band 1 / B05 | Unstoppable (+4 Base)"
    ])

    box_four_p = make_box("THE FOUR P-FRAMEWORK (PASSIVE / PANIC / PARRY / POSTURE)", [
        "Pillar Code | Tactical Domain       | Core Battle Mechanical Function",
        "---",
        "P1: Passive | Weapon & Trait Arts   | Speed-delta triggers & range bonuses",
        "P2: Panic   | SP & Sanity Breakdown | Burden drain, panic states & recovery",
        "P3: Parry   | Active Defense & Guard| Melee deflects, shields & intercepts",
        "P4: Posture | Poise & Stagger Meter | Momentum math & dual-threshold breaks"
    ])

    new_section_maw = f"""---

## V. M.A.W.-W (Weapon) Combat Stat Profiles: Speed, Range & The Four P's

Every M.A.W. Weapon (**M.A.W.-W**) extracted from a Sorrow Entity functions according to strict physical and metaphysical parameters governing **Speed Modifiers**, **Range Bands**, and **The Four P's (Passives, Panic, Parry, Posture)**:

```text
{box_maw_mods}
```

```text
{box_four_p}
```

### 5.1 Weapon Category Specifications & Combat Metrics

| Weapon Category | Weight Class | Speed Modifier | AP Cost | Optimal Range Band | Base Parry Defense | Core Passive Trait |
|---|---|---|---|---|---|---|
| **Daggers & Scalpels** | Feather / Ultra-Light | +2 Speed | 1 AP | Band 1 (0–2m) | Low (Parry Base 7) | *Momentum Surge* (+2 Clash Power if Speed > enemy by 3+) |
| **Short Swords & Rapiers** | Light Class | +1 Speed | 1 AP | Band 1–2 (2–5m) | Medium (Parry Base 9) | *Rapid Flank* (+20% damage when striking from behind) |
| **Broadswords & Batons** | Medium Class | +0 Speed | 1 AP | Band 1–3 (5–12m) | Standard (Parry Base 10)| *Balanced Stance* (+1 Coin value on defensive clash) |
| **Greatswords & Warhammers**| Heavy Class | -1 Speed | 2 AP | Band 1 or Band 4 | Heavy (Parry Base 12) | *Heavy Poise* (Ignores first 5 stagger buildup per turn)|
| **Siege Mauls & Cannons** | Colossal Relic | -2 Speed | 2 AP | Band 1 or Band 5 | Titanic (Parry Base 14)| *Unstoppable* (Clash strikes cannot be deflected) |

### 5.2 The Four P's in M.A.W.-W Equipment Management
1. **Passives (P1)**: Intrinsic weapon abilities that trigger automatically during combat based on operative positioning and speed superiority.
2. **Panic (P2)**: High-tier M.A.W.-W gear (Grades γ, δ, ω) imposes a psychic weight on the wielder's soul. If the operative's Composure is lower than the weapon's grade threshold, the weapon siphons -5 SP per turn, accelerating entry into Panic States.
3. **Parry & Protection (P3)**: Weapons with reinforced crossguards, broad blades, or acoustic resonators can spend 1 AP to execute a direct physical or psychic Parry, canceling hostile strikes and returning 50% counter-damage.
4. **Posture & Poise (P4)**: Heavy impact weapons deliver massive posture damage magnified by kinetic momentum (`Speed Difference * Weight Class`), rapidly triggering Dual-Threshold Stagger (Stagger 1 at 60% HP, Terminal Stagger at 25% HP)."""

    text = text.rstrip() + "\n\n" + new_section_maw + "\n"
    check_banned(text, filepath)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Updated {filepath} successfully!")

# -------------------------------------------------------------
# 4. Update ABSOLOVHAN_OVERVIEW.md
# -------------------------------------------------------------
def update_absolvohan_overview():
    filepath = "SOMNARAK-WORLD/The_Absolvohan/ABSOLOVHAN_OVERVIEW.md"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    box_maw_mods = make_box("M.A.W.-W WEAPON SPEED & RANGE MODIFIERS ENGINE", [
        "Weight Class | Spd Mod | AP | Optimal Band | Trait Mechanics",
        "---",
        "Feather / UL | +2 Spd  | 1  | Band 1 (N01) | Momentum Surge (+2 Pwr)",
        "Light Class  | +1 Spd  | 1  | Band 1-2     | Rapid Flanking / Bleed",
        "Medium Class | +0 Spd  | 1  | Band 1-3     | Balanced Clash Profile",
        "Heavy Class  | -1 Spd  | 2  | Band 1 / B04 | Heavy Poise (+2 Base)",
        "Colossal Rel | -2 Spd  | 2  | Band 1 / B05 | Unstoppable (+4 Base)"
    ])

    box_four_p = make_box("THE FOUR P-FRAMEWORK (PASSIVE / PANIC / PARRY / POSTURE)", [
        "Pillar Code | Tactical Domain       | Core Battle Mechanical Function",
        "---",
        "P1: Passive | Weapon & Trait Arts   | Speed-delta triggers & range bonuses",
        "P2: Panic   | SP & Sanity Breakdown | Burden drain, panic states & recovery",
        "P3: Parry   | Active Defense & Guard| Melee deflects, shields & intercepts",
        "P4: Posture | Poise & Stagger Meter | Momentum math & dual-threshold breaks"
    ])

    new_section_abso = f"""### 4.8 Agent Speed & Range Profile and M.A.W.-W Modifiers

Within Facility 01, containment agents operate with an intrinsic **Base Speed Die** and **Natural Range Affinity** on the 10-node facility grid, modified by equipped Materialized Agony Wear weaponry (**M.A.W.-W**):

```text
{box_maw_mods}
```

- **Speed Modifiers**: Feather/Ultra-Light weapons grant +2 Speed, allowing rapid movement across nodes; Heavy and Colossal weapons impose -1 to -2 Speed penalties but grant devastating base power and stagger shock.
- **Range Band Boundaries**: Melee weapons operate at Band 1 (Nodes 1–2). Ranged carbines and sonic bows operate at Bands 3–4 (Nodes 5–8). Ranged weapons firing at Node 1 suffer -2 Clash Power and -20% accuracy.

---

### 4.9 The Four P-Framework (Passives, Panic, Parry, Posture) in Facility Operations

Containment engagements integrate the universal Four P-Framework:

```text
{box_four_p}
```

1. **P1: Passives (M.A.W.-W Weapon Passives & Floor Synergy)**:
   - *Momentum Surge*: +2 Clash Power when Speed exceeds target by 3+.
   - *Point-Blank Dissection*: +25% Critical Hit Chance at Node 1.
   - *Overwatch Anchor*: +3 Clash Power from Node 7–8 when stationary for 1 turn.
   - *Heavy Ballast Poise*: Heavy weapons ignore the first 5 stagger buildup per turn.
2. **P2: Panic (SP & Mental Collapse)**:
   - *Burden Drain*: High-grade M.A.W.-W beyond agent clearance siphons -5 SP per turn.
   - *Panic Typologies*: Berserk (0 AP sprint to Node 1), Despair (Speed 1, 0 defense), Wandering (random node shifts), Catatonic (Speed 0, instant Stagger).
   - *Panic Restoration*: Allies at Band 2–3 spend 1 AP on Flerehan communion or non-lethal blunt Lament strike to restore SP to +25.
3. **P3: Parry & Protection**:
   - *Parry (1 AP)*: Roll defense die vs incoming melee strike; win completely deflects damage and counter-strikes for 50% weapon power.
   - *Guard Shield (1 AP)*: Directional barrier absorbing flat damage based on weapon and suit defense.
   - *Kinetic Interception*: Wardens at Node 3–4 spend 1 AP to intercept ranged lines targeting clerks or mid-field operators.
4. **P4: Posture & Poise**:
   - Posture meter = `Base Resilience + M.A.W. Weight Bonus`.
   - Momentum Multiplier = `(Speed Diff) * (Weapon Weight Multiplier)`.
   - Depleting Posture triggers Dual-Threshold Stagger: Stagger 1 (60% HP, 2.0x damage) and Terminal Stagger 2 (25% HP, 2.5x damage)."""

    target_anchor = "## V. Facility Architecture & The 8 Operational Floors"
    if target_anchor in text:
        idx = text.find(target_anchor)
        text = text[:idx] + new_section_abso + "\n\n---\n\n" + text[idx:]
        check_banned(text, filepath)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Updated {filepath} successfully!")
    else:
        print("Target anchor not found in ABSOLOVHAN_OVERVIEW.md")

if __name__ == "__main__":
    update_battle_system()
    update_styles()
    update_maw_codex()
    update_absolvohan_overview()
