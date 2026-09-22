#!/usr/bin/env python3
"""
tools/expand_absolvohan_battles_part3_remaining.py
Expands remaining Ordeals in SOMNARAK-WORLD/The_Absolvohan/Part_3_Days_29_to_49.md:
1. Third Watch (Dusk) Ordeal — The Gilded Drowners
2. Amber Dusk Ordeal — The Churning Hive
3. The Midnight Herald — First Glimpse of the Sovereign Watch
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

# -------------------------------------------------------------
# 1. The Gilded Drowners (Violet Dusk)
# -------------------------------------------------------------
box_drowners_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (VIOLET DUSK)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [MONUMENT]    [MELLDA][PARK]          [HWANG]        [MAJIN]",
    "DIST    : Mellda at N03 (Band 1); Park at N04 (Band 2); Hwang at N06.",
    "---",
    "Border Lead Mellda: Speed 5 -> 3 AP | HP: 190/190 | SP: +30 | Threshold Vow",
    "Agent Park        : Speed 6 -> 3 AP | HP: 120/120 | SP: +25 | Lament Requiem",
    "Agent Hwang       : Speed 5 -> 3 AP | HP: 110/110 | SP: +20 | Observing Scepter",
    "Gilded Monument   : Speed 4 -> 2 AP | HP: 340/340 | Sorrow: 60% | Void Beam"
])

box_drowners_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Mellda locks N02; Park delivers 44 Lament; Monument 60% Stagger 1.",
    "- Turn 03: Posture broken; all allied attacks deal 2.0x direct damage; HP at 130.",
    "- Turn 04: Monument charges corridor laser [Oblivion Torrent]; Mellda shields.",
    "- Turn 05: Hwang pierces Void focal lens from N06, canceling high-yield blast.",
    "- Turn 06: Park unleashes Climax Smite; Terminal Stagger shatters monument."
])

box_drowners_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Tri-sector Void conduits discharge and power down.",
    "2. Status Equilibrium : Hallway radiation dissipates; team SP rises to +35.",
    "3. Containment Check   : All 3 monuments reduced to pulverized slag.",
    "4. OUTCOME             : ZERO AGENT CASUALTIES, +22 REFINED RHR SECURED."
])

old_drowners = """##### Ordeal Manifestation: Third Watch (Dusk) Ordeal — The Gilded Drowners
At 0.145 tons harvested, the facility's emergency sirens shift from amber to violet. A Dusk Ordeal has arrived:

```text
> ORDEAL WARNING: DUSK ORDEAL — THE GILDED DROWNERS (VIOLET DUSK)
> THREAT: Three colossal stone monuments emerge on Floors 1, 3, and 5.
> BEHAVIOR: Periodically fire high-yield Void lasers across entire corridors!
```

This requires split suppression teams:
- **Floor 1 Monolith**: Suppressed by Agent Hwang and Agent Lee using Void-resistant loadouts.
- **Floor 3 Monolith**: Suppressed by Agent Song and Agent Choi from Range Band 3 with bows.
- **Floor 5 Monolith**: Mellda and Agent Park engage in point-blank melee. Mellda tanks the laser discharge with *Iron Perimeter*, while Park shatters the monument with four heavy maul swings!

All three monoliths collapse simultaneously into inert slag! +22 RHR reagents collected!"""

new_drowners = f"""##### Ordeal Manifestation: Third Watch (Dusk) Ordeal — The Gilded Drowners
At 0.145 tons harvested, the facility's emergency sirens shift from amber to violet. A Dusk Ordeal has arrived:

```text
+==============================================+
| TACTICAL DOSSIER: THIRD WATCH (DUSK) ORDEAL  |
| DESIGNATION : THE GILDED DROWNERS            |
| CLASSIFICATION : VIOLET (VOID/DECAY) DUSK    |
| INTRUSION POINT : FLOORS 1, 3, AND 5         |
| HOSTILE PARAMETERS:                          |
| - Entities: 3x Colossal Gilded Monoliths     |
| - Attack Affinity: Piercing Void Lasers      |
| - Weakness Affinity: Lament / Weight         |
| TACTICAL DEPLOYMENT: TRI-SECTOR INTERCEPT    |
+==============================================+
```

Three colossal gilded monuments materialize across Floors 1, 3, and 5, aiming high-yield Void beams along the main thoroughfares!

Director Majin establishes coordinated GBS tactical commands:
- **Floor 1 Team**: Hwang & Lee lock down the lower data junction.
- **Floor 3 Team**: Song & Choi suppress the processing corridor from Range Band 3.
- **Floor 5 Strike Force**: Lead Mellda and Agent Park advance directly into Point-Blank range.

```text
{box_drowners_hud}
```

###### Turn 01 Action Resolution Log (Floor 5 Bulwark Gate)
- **Step 1: Floor 5 Echo-Core Resonance (Border Lead Mellda)**:
  * Mellda deploys *The Bulwark Perimeter*, erecting golden barriers over Nodes 2 through 4 that nullify Void laser penetration by 40%.
- **Step 2: Movement & Action Point Spending**:
  * Border Lead Mellda (Speed 5 -> 3 AP) spends 1 AP to advance from Node 3 to Node 2 (Point-Blank Range Band 1). Spends 2 AP to brace *Threshold Vow* in reflective parry stance.
  * Agent Park (Speed 6 -> 3 AP) advances to Node 3 behind Mellda. Spends 2 AP to prepare `[Lament Requiem Resonant Crush]`. Remaining 1 AP held in Guard.
  * Agent Hwang (Speed 5 -> 3 AP) takes Node 6 (Range Band 3). Spends 2 AP to prepare concentrated Void disruption targeting the monument's optical crown.
- **Step 3: Clash Resolution (Node 2)**:
  * Gilded Monument declares `[Oblivion Prismatic Lance]` on Node 2 (Base 8 + 2 Coins = 12 Power).
  * Mellda's `[Threshold Vow Reflective Parry]` (Base 10 + 2 Coins = 14 Power).
  * **Resolution**: Mellda WINS THE CLASH (14 vs 12).
    * Mellda's spearhead refracts the purple laser into the ceiling, creating an opening.
  * Agent Park follows with `[Lament Requiem Resonant Crush]` unopposed:
    * The massive acoustic hammer strikes the monument's pedestal, dealing **44 direct Lament damage** and inflicting +24 Stagger!

```text
{box_drowners_turns}
```

```text
{box_drowners_phase}
```

All three monoliths collapse simultaneously into inert slag! +22 RHR reagents collected!"""

if old_drowners in text:
    text = text.replace(old_drowners, new_drowners)
    print("Replaced Gilded Drowners section successfully!")
else:
    print("Could not find Gilded Drowners section!")

# -------------------------------------------------------------
# 2. Amber Dusk Ordeal — The Churning Hive
# -------------------------------------------------------------
box_hive_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (AMBER DUSK)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [HIVE-QUEEN]  [MELLDA][HWANG]         [BAE]          [MAJIN]",
    "DIST    : Mellda at N03 (Band 1); Hwang at N04 (Band 2); Bae at N06.",
    "---",
    "Border Lead Mellda: Speed 5 -> 3 AP | HP: 195/195 | SP: +30 | Threshold Vow",
    "Agent Hwang       : Speed 6 -> 3 AP | HP: 120/120 | SP: +25 | Blessed Scalpel",
    "Agent Bae         : Speed 5 -> 3 AP | HP: 130/130 | SP: +25 | Bulwark Maul",
    "The Churning Hive : Speed 4 -> 2 AP | HP: 380/380 | Sorrow: 65% | Earth Maw"
])

box_hive_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Mellda locks Gate 5; Hwang flanks N02; Hive hits 60% Stagger 1.",
    "- Turn 03: Carapace cracked; all attacks deal 2.0x direct damage; HP at 150.",
    "- Turn 04: Hive attempts tectonic burrow; Dekan engages Jaw Clamp pin.",
    "- Turn 05: Bae lands heavy maul strike on ventral nerve; forces Terminal Stagger.",
    "- Turn 06: Mellda executes Threshold Execution; Hive dissolves to amber dust."
])

box_hive_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Sector 5 floorplates sealed; subterranean grates locked.",
    "2. Status Equilibrium : Tremor vibrations cease; team SP stabilizes at +35.",
    "3. Containment Check   : Queen burrower fully dissolved into crystallized dust.",
    "4. OUTCOME             : ZERO AGENT CASUALTIES, +25 REFINED RHR SECURED."
])

old_hive = """##### Ordeal Manifestation: Amber Dusk Ordeal — The Churning Hive
At 0.165 tons collected, the subterranean bedrock shudders. Colossal segmented centipedes burst through the flagstones of Floor 5 and Floor 6:

```text
> ORDEAL DETECTED: AMBER DUSK — THE CHURNING HIVE
> THREAT: Massive burrowers that deal heavy compound damage and consume clerks!
> TACTICAL INTERVENTION: Mellda anchors the choke point at Sector 5 Gate!
```

Mellda activates *Iron Perimeter* at maximum aperture, holding the two primary burrowers in the doorway. Agent Hwang circles around their rear flanks, using the *Blessed Scalpel*'s rapid Void strikes to pierce their chitinous armor plates. In 25 seconds of blistering combat, the queen burrower dissolves into crystallized Han dust! +25 RHR reagents secured!"""

new_hive = f"""##### Ordeal Manifestation: Amber Dusk Ordeal — The Churning Hive
At 0.165 tons collected, the subterranean bedrock shudders. Colossal segmented centipedes burst through the flagstones of Floor 5 and Floor 6:

```text
+==============================================+
| TACTICAL DOSSIER: AMBER DUSK ORDEAL          |
| DESIGNATION : THE CHURNING HIVE              |
| CLASSIFICATION : AMBER (WEIGHT/GRUDGE) DUSK  |
| INTRUSION POINT : FLOOR 5 GATEWAY SLUICE     |
| HOSTILE PARAMETERS:                          |
| - Entity: 1x Colossal Segmented Burrower     |
| - Attack Affinity: Crushing Weight Shock     |
| - Weakness Affinity: Physical Slash / Void   |
| TACTICAL DEPLOYMENT: MELLDA, HWANG & BAE     |
+==============================================+
```

A massive, armored subterranean centipede erupts through the reinforced masonry at Node 1, gnashing four pairs of serrated diamond mandibles!

Director Majin establishes GBS tactical positioning:

```text
{box_hive_hud}
```

###### Turn 01 Action Resolution Log (Floor 5 Gateway Sluice)
- **Step 1: Floor 5 Echo-Core Resonance (Border Lead Mellda)**:
  * Mellda engages *Blast Gate Lockdown*, dropping heavy steel portcullises at Node 4 to isolate Nodes 1–3 and trap the beast in the gateway vestibule.
- **Step 2: Movement & Action Point Spending**:
  * Border Lead Mellda (Speed 5 -> 3 AP) stands firm at Node 3 (Point-Blank Range Band 1). Spends 2 AP to prepare `[Threshold Vow Bulwark Stance]`.
  * Agent Hwang (Speed 6 -> 3 AP) spends 1 AP to shift from Node 4 to Node 2 behind the beast's rear segment. Spends 2 AP to ready `[Blessed Scalpel Void Dissection]`.
  * Agent Bae (Speed 5 -> 3 AP) positions at Node 6 (Range Band 3). Spends 2 AP to wind up `[Bulwark Maul Ground Breaker]`. Remaining 1 AP held in Guard.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * The Churning Hive declares `[Tectonic Mandible Crush]` on Node 3 (Base 9 + 2 Coins = 13 Power).
  * Mellda's `[Threshold Vow Bulwark Stance]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Mellda WINS THE CLASH (15 vs 13).
    * Mellda's golden arm-blade locks the centipede's primary mandibles. The counter-force reverberates through the beast's chitinous segments, dealing 36 Grudge damage and inflicting +24 Stagger!
  * Agent Hwang strikes from Node 2 unopposed, driving the *Blessed Scalpel* deep into the exposed ventral joint for **42 Void damage**!

```text
{box_hive_turns}
```

```text
{box_hive_phase}
```

In 25 seconds of blistering combat, the queen burrower dissolves into crystallized Han dust! +25 RHR reagents secured!"""

if old_hive in text:
    text = text.replace(old_hive, new_hive)
    print("Replaced Hive section successfully!")
else:
    print("Could not find Hive section!")

# -------------------------------------------------------------
# 3. The Midnight Herald
# -------------------------------------------------------------
box_herald_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (SOVEREIGN MIDNIGHT)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [DOOR-ECHO]   [MARJUK][HWANG]         [PARK]         [XYAN]",
    "DIST    : Marjuk at N03 (Band 1); Hwang at N04 (Band 2); Park at N05.",
    "---",
    "Archive Lead Marjuk: Speed 5 -> 3 AP | HP: 200/200 | SP: +40 | Chrono Stasis",
    "The Exile Xyan     : Speed 6 -> 3 AP | HP: 210/210 | SP: +45 | Singularity Arc",
    "Agent Hwang        : Speed 6 -> 3 AP | HP: 125/125 | SP: +30 | Blessed Scalpel",
    "Agent Park         : Speed 6 -> 3 AP | HP: 125/125 | SP: +30 | Lament Requiem",
    "Final Door Echo    : Speed 5 -> 3 AP | HP: 520/520 | Sorrow: 75% | Void Pulse"
])

box_herald_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Marjuk freezes Node 1; Hwang & Park strike; Echo 60% Stagger 1.",
    "- Turn 03: Posture broken; all 4-affinity strikes deal 2.0x direct damage.",
    "- Turn 04: Echo attempts dimensional toll; Xyan deploys Singularity Well.",
    "- Turn 05: Park executes Flerehan resonance, purging the sorrow harmonic.",
    "- Turn 06: Marjuk & Xyan coordinate terminal lockdown; Echo dissolves."
])

box_herald_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Deep Vault acoustic and temporal seals fully restore.",
    "2. Status Equilibrium : Pale radiation drains; all agent SP restored to max.",
    "3. Containment Check   : Sovereign Door Echo dissipated into bedrock.",
    "4. OUTCOME             : HISTORIC MIDNIGHT CLEAR — ZERO CASUALTIES, +30 RHR."
])

old_herald = """##### Ordeal Manifestation: The Midnight Herald — First Glimpse of the Sovereign Watch
At 0.205 tons harvested, the lights across the vertical spine cut to complete darkness. A deep, subterranean bell tolls from beneath Floor 8:

```text
> ORDEAL WARNING: SOVEREIGN MIDNIGHT ANOMALY — THE FINAL DOOR ECHO
> A shadow of the Before-Time passes through Floor 7 and Floor 8 corridors...
> TACTICAL RESPONSE: Marjuk and Xyan activate Deep Vault stasis wards!
```

Marjuk anchors the Archive stasis field while Agent Hwang and Agent Park deploy to the lower elevator shaft, holding the boundary line until the harmonic pulse dissipates back into the bedrock. +30 RHR reagents collected!"""

new_herald = f"""##### Ordeal Manifestation: The Midnight Herald — First Glimpse of the Sovereign Watch
At 0.205 tons harvested, the lights across the vertical spine cut to complete darkness. A deep, subterranean bell tolls from beneath Floor 8:

```text
+==============================================+
| TACTICAL DOSSIER: SOVEREIGN MIDNIGHT ANOMALY |
| DESIGNATION : THE FINAL DOOR ECHO            |
| CLASSIFICATION : PALE / VOID MIDNIGHT HERALD |
| INTRUSION POINT : FLOOR 7 & 8 BOUNDARY SHAFT |
| HOSTILE PARAMETERS:                          |
| - Entity: 1x Colossal Dimensional Projection |
| - Attack Affinity: Pale (% Max HP) & Void    |
| - Weakness Affinity: Balanced (All 4 Types)  |
| TACTICAL DEPLOYMENT: DEEP VAULT GUARDS       |
+==============================================+
```

A towering shadow from the Before-Time manifests in the lower boundary shaft at Node 1, ringing with the resonant chime of the Final Door!

Director Majin establishes Deep Vault GBS tactical parameters:

```text
{box_herald_hud}
```

###### Turn 01 Action Resolution Log (Deep Vault Boundary Shaft)
- **Step 1: Floor 6 & 8 Echo-Core Resonances (Marjuk & Xyan)**:
  * Marjuk deploys *The Temporal Stasis Array*, locking Node 1 in amber suspension and canceling the Echo's initial area-sweep.
  * Xyan activates *The Singularity Well*, anchoring the hostile at Node 1 and preventing any displacement toward the elevator shaft.
- **Step 2: Movement & Action Point Spending**:
  * Archive Lead Marjuk (Speed 5 -> 3 AP) holds Node 3 (Range Band 1). Spends 2 AP to maintain the chronological clamp.
  * The Exile Xyan (Speed 6 -> 3 AP) stands at Node 10, spending 2 AP to channel gravitational ballast downward.
  * Agent Hwang (Speed 6 -> 3 AP) advances to Node 4 (Range Band 2). Spends 2 AP to declare `[Blessed Scalpel Precision Void Dissection]`.
  * Agent Park (Speed 6 -> 3 AP) positions at Node 5 (Range Band 3). Spends 2 AP to ready `[Lament Requiem Resonant Wave]`.
- **Step 3: Clash Resolution (Node 1 to 3)**:
  * Final Door Echo attempts `[Chime of the Before-Time]` (Base 10 + 2 Coins = 14 Power).
  * Marjuk's `[Chrono Stasis Seal]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Marjuk WINS THE CLASH (15 vs 14).
    * Marjuk's stasis seal encapsulates the acoustic pulse before it can detonate, reflecting 38 Pale damage back into the projection with +26 Stagger!
  * Hwang and Park deliver coordinated Void and Lament strikes from Nodes 4 and 5, destabilizing the shadow's harmonic cohesion.

```text
{box_herald_turns}
```

```text
{box_herald_phase}
```

Marjuk anchors the Archive stasis field while Agent Hwang and Agent Park deploy to the lower elevator shaft, holding the boundary line until the harmonic pulse dissipates back into the bedrock. +30 RHR reagents collected!"""

if old_herald in text:
    text = text.replace(old_herald, new_herald)
    print("Replaced Herald section successfully!")
else:
    print("Could not find Herald section!")

check_banned(text, filepath)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
print(f"Updated {filepath} with all remaining expanded GBS battles!")
