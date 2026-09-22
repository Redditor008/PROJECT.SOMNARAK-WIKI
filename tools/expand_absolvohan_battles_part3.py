#!/usr/bin/env python3
"""
tools/expand_absolvohan_battles_part3.py
Expands all major combat and Ordeal encounters in SOMNARAK-WORLD/The_Absolvohan/Part_3_Days_29_to_49.md
with full Gameplay Battle System (GBS) Reverie Directorate Style mechanics:
- 10-Node Stage Grid ([N01] to [N10])
- Speed-to-AP Conversion
- Clash Resolution with Coin Rolls and Power math
- Dual-Threshold Stagger Engine (60% and 25%)
- Echo-Core Floor Resonances (Floor 2 Dekan, Floor 5 Mellda, Floor 1 Majin)
- 6-Turn Phase Combat Structure with Phase-End ticks
- Zero banned terms, 100% 71-col box symmetry
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

def make_box(title, raw_rows, width=71):
    top = "+" + "=" * (width - 2) + "+"
    div = "+" + "-" * (width - 2) + "+"
    bot = top
    out = [top]
    if title:
        t_pad = (width - 2 - len(title)) // 2
        t_line = "|" + " " * t_pad + title + " " * (width - 2 - len(title) - t_pad) + "|"
        out.append(t_line)
        out.append(div)
    max_len = width - 4

    rows = []
    for r in raw_rows:
        if r == "---":
            rows.append("---")
        elif len(r) <= max_len:
            rows.append(r)
        else:
            words = r.split()
            cur = []
            cur_len = 0
            for w in words:
                if cur_len + len(w) + (1 if cur else 0) <= max_len:
                    cur.append(w)
                    cur_len += len(w) + (1 if len(cur) > 1 else 0)
                else:
                    if cur:
                        rows.append(" ".join(cur))
                    cur = [w]
                    cur_len = len(w)
            if cur:
                rows.append(" ".join(cur))

    for r in rows:
        if r == "---":
            out.append(div)
        else:
            pad_len = width - 2 - 1 - len(r)
            out.append("| " + r + " " * pad_len + "|")
    out.append(bot)
    return "\n".join(out)

filepath = "SOMNARAK-WORLD/The_Absolvohan/Part_3_Days_29_to_49.md"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Expand The Grieving Monolith (Green Noon)
box_monolith_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (GREEN NOON ORDEAL)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [MONOLITH]    [MELLDA][PARK]          [KIM]          [DEKAN]",
    "DIST    : Mellda at N03 (Band 1); Park at N04 (Band 2); Kim at N06.",
    "---",
    "Border Lead Mellda: Speed 5 -> 3 AP | HP: 180/180 | SP: +30 | Threshold Vow",
    "Agent Park        : Speed 6 -> 3 AP | HP: 110/110 | SP: +25 | Lament Requiem",
    "Agent Kim         : Speed 5 -> 3 AP | HP: 105/105 | SP: +20 | Kinetic Carbine",
    "Grieving Monolith : Speed 3 -> 2 AP | HP: 320/320 | Sorrow: 65% | Grudge Wave"
])

box_monolith_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Mellda holds N02; Park deals 38 Lament damage; Monolith 60% Stagger.",
    "- Turn 03: Posture broken; all attacks deal 2.0x direct damage; HP falls to 125.",
    "- Turn 04: Monolith recovers; charges massive shockwave [Tectonic Toll].",
    "- Turn 05: Kim at N06 uses 2 AP to fire Stasis Disruption, canceling skill.",
    "- Turn 06: Park unleashes Requiem Climax; Terminal Stagger shatters monolith."
])

box_monolith_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Seismic tremors dissipate across Floor 2 junction.",
    "2. Status Equilibrium : Stagger meters reset; team-wide SP rises to +35.",
    "3. Containment Check   : Monolith pulverized into inert river silt.",
    "4. OUTCOME             : FLAWLESS VICTORY — 0 CASUALTIES, +12 REFINED RHR."
])

old_monolith_section = """Ordeal Manifestation: Second Watch (Noon) Ordeal — The Grieving Monolith
At 0.110 tons collected, the ceiling groans. A colossal slab of weeping green stone materializes in Floor 2's primary junction corridor:

```text
> ORDEAL DETECTED: NOON ORDEAL — THE GRIEVING MONOLITH (GREEN NOON)
> THREAT: Deals heavy Grudge physical shockwaves every 6 seconds.
> TACTICAL RESPONSE: Mellda leads Floor 5 squad to Floor 2 for pincer clash.
```

Mellda anchors Range Band 1 with her tower shield, absorbing 45 physical damage per shockwave while her aura reduces incoming damage to 32. Agent Park steps up with his *Lament Requiem* warhammer, delivering massive Lament/Mental clashing blows from Range Band 2. In 18 seconds of coordinated fire, the monolith fractures into inert river silt, dropping +12 refined RHR reagents!"""

new_monolith_section = f"""Ordeal Manifestation: Second Watch (Noon) Ordeal — The Grieving Monolith
At 0.110 tons collected, the ceiling groans. A colossal slab of weeping green stone materializes in Floor 2's primary junction corridor:

```text
+==============================================+
| TACTICAL DOSSIER: SECOND WATCH (NOON) ORDEAL |
| DESIGNATION : THE GRIEVING MONOLITH          |
| CLASSIFICATION : GREEN (WEIGHT/LAMENT) NOON  |
| INTRUSION POINT : FLOOR 2 PRIMARY JUNCTION   |
| HOSTILE PARAMETERS:                          |
| - Entity: 1x Colossal Weeping Stone Slab     |
| - Attack Affinity: Grudge Physical Shockwave |
| - Weakness Affinity: Lament (Acoustic Echo)  |
| TACTICAL DEPLOYMENT: MELLDA, PARK & KIM      |
+==============================================+
```

A massive, weeping slab of ancient green basalt crashes down at Node 1, radiating compressive shockwaves that shake the corridor foundations!

Director Majin establishes real-time GBS tactical coordinates:

```text
{box_monolith_hud}
```

###### Turn 01 Action Resolution Log
- **Step 1: Floor 5 Echo-Core Resonance (Border Lead Mellda)**:
  * Mellda projects *The Bulwark Perimeter*, establishing heavy blast mantlets across Nodes 2 through 4 that absorb +30% physical shock.
  * Director Majin issues tactical command: *Administrative Clarity* active team-wide.
- **Step 2: Movement & Action Point (AP) Spending**:
  * Border Lead Mellda (Speed 5 -> 3 AP) spends 1 AP to advance from Node 3 to Node 2 (Point-Blank Range Band 1 with the Monolith).
  * Mellda spends 2 AP to brace *Threshold Vow* in a heavy kinetic parry stance.
  * Agent Park (Speed 6 -> 3 AP) holds Node 4 behind Mellda's mantlet. Spends 2 AP to wind up `[Lament Requiem Resonant Smash]` (Range Band 2). Remaining 1 AP held in Guard (+10 Shield).
  * Agent Kim (Speed 5 -> 3 AP) positions at Node 6 (Range Band 3). Spends 2 AP to prepare concentrated carbine fire targeting the slab's stress fissure.
- **Step 3: Clash Standoff (Node 2)**:
  * The Grieving Monolith declares `[Tectonic Ground Pound]` on Node 2:
    * Monolith Roll: Base 8 + (2 Coins Heads: +4) = 12 Power.
  * Mellda's `[Threshold Vow Kinetic Parry]`:
    * Mellda Roll: Base 10 + (2 Coins Heads: +4) = 14 Power.
  * **Resolution**: Mellda WINS THE CLASH (14 vs 12).
    * Mellda's golden arm-blade turns the crashing stone slab aside. The impact shocks the monolith's crystalline base, dealing 26 Grudge damage and inflicting +18 Stagger.
  * Agent Park follows through with `[Lament Requiem Resonant Smash]` from Node 4:
    * Attack is unopposed! Deals 36 Lament damage directly through the acoustic crack, eroding the monolith's composure.
  * Agent Kim delivers a 3-round burst from Node 6, adding 24 piercing damage.

```text
{box_monolith_turns}
```

```text
{box_monolith_phase}
```"""

if old_monolith_section in text:
    text = text.replace(old_monolith_section, new_monolith_section)
    print("Replaced Monolith section successfully!")
else:
    print("Could not find Monolith section!")

# 2. Expand The Sanguine Larvae (Crimson Noon)
box_larvae_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (CRIMSON NOON)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [LARVA-A] [LARVA-B][KANG]          [SONG]         [DEKAN]",
    "DIST    : Kang at N03 (Band 1); Song at N05 (Band 3); Dekan at N09.",
    "---",
    "Agent Kang  : Speed 6 -> 3 AP | HP: 125/125 | SP: +25 | Fury Greatsword",
    "Agent Song  : Speed 5 -> 3 AP | HP: 100/100 | SP: +20 | Kinetic Cleaver",
    "Sanguine Larvae (x2): Speed 6 -> 3 AP | HP: 140 each | Bleed Pincer"
])

box_larvae_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Kang cleaves Larva-A; triggers 60% Stagger 1; Song flanks N04.",
    "- Turn 03: All allied strikes deal 2.0x direct damage; Larva-A destroyed.",
    "- Turn 04: Larva-B charges [Sanguine Frenzy]; Dekan activates Jaw Clamp.",
    "- Turn 05: Kang intercepts at N02; wins clash 15 vs 11; inflicts Stagger 2.",
    "- Turn 06: Song executes Climax Finisher; Larva-B dissolves into red mist."
])

box_larvae_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Biological acid vents sealed; floor neutralized.",
    "2. Status Equilibrium : Bleed counters purge; team SP rises to +30.",
    "3. Containment Check   : Both Sanguine Larvae eradicated.",
    "4. OUTCOME             : ZERO AGENT CASUALTIES, +14 RHR HARVESTED."
])

old_larvae = """Ordeal Manifestation: Crimson Noon Ordeal — The Sanguine Larvae
At 0.125 tons harvested, the floor vents rupture. Four chitinous red insectoids crawl from the drainage grates of Floor 3:

```text
> ORDEAL DETECTED: CRIMSON NOON — SANGUINE LARVAE (RED NOON)
> BEHAVIOR: Rapid pincer advance, stacking bleed hemorrhage on contact.
> SUPPRESSION TEAM: Agent Kang (Fury Greatsword) & Agent Song deployed.
```

Kang charges into the corridor, swinging his wide-arc greatsword to cleave three larvae in a single sweep! Song follows up with kinetic cleavers, crushing the fourth before it can latch onto the extraction conduits. Zero breach leaks. Energy quota safe!"""

new_larvae = f"""Ordeal Manifestation: Crimson Noon Ordeal — The Sanguine Larvae
At 0.125 tons harvested, the floor vents rupture. Four chitinous red insectoids crawl from the drainage grates of Floor 3:

```text
+==============================================+
| TACTICAL DOSSIER: CRIMSON NOON ORDEAL        |
| DESIGNATION : SANGUINE LARVAE                |
| CLASSIFICATION : RED (GRUDGE/WEIGHT) NOON    |
| INTRUSION POINT : FLOOR 3 DRAINAGE GRATES    |
| HOSTILE PARAMETERS:                          |
| - Entities: 4x Chitinous Sanguine Larvae     |
| - Attack Affinity: Grudge Bleed Hemorrhage   |
| - Weakness Affinity: Weight (Kinetic Impact) |
| TACTICAL DEPLOYMENT: KANG & SONG ENGAGE      |
+==============================================+
```

The skittering horrors burst through the floorplates at Node 1 and Node 2, snapping razor mandibles dripping with corrosive crimson bile!

Director Majin directs the clash through the 10-node combat grid:

```text
{box_larvae_hud}
```

###### Turn 01 Action Resolution Log
- **Step 1: Floor 2 Echo-Core Resonance (Dekan)**:
  * Dekan anchors *Bastion of the Keep*, raising kinetic hardness across Nodes 1 to 4 and granting +40% physical resistance against bleed bites.
- **Step 2: Movement & Action Point Spending**:
  * Agent Kang (Speed 6 -> 3 AP) spends 1 AP to charge from Node 3 to Node 2, physically blocking the hallway and engaging Larva-A and Larva-B.
  * Kang spends 2 AP to unleash `[Fury Wide-Arc Cleave]`.
  * Agent Song (Speed 5 -> 3 AP) advances to Node 4 (Range Band 2). Spends 2 AP to ready `[Kinetic Pincer Smash]`. Remaining 1 AP held in Guard.
- **Step 3: Clash Resolution (Node 2)**:
  * Larva-A declares `[Acid Mandible Latch]` against Kang (Base 7 + 2 Coins = 11 Power).
  * Kang's `[Fury Wide-Arc Cleave]` (Base 9 + 2 Coins = 14 Power).
  * **Resolution**: Kang WINS THE CLASH (14 vs 11).
    * The massive greatsword shears through Larva-A's carapace, dealing 38 Weight damage and knocking it back into Node 1 with +20 Stagger buildup!
  * Larva-B attempts a flanking bite; Song intercepts from Node 4, smashing its flank for 26 kinetic damage.

```text
{box_larvae_turns}
```

```text
{box_larvae_phase}
```"""

if old_larvae in text:
    text = text.replace(old_larvae, new_larvae)
    print("Replaced Larvae section successfully!")
else:
    print("Could not find Larvae section!")

check_banned(text, filepath)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
print(f"Updated {filepath} successfully with expanded GBS battles!")
