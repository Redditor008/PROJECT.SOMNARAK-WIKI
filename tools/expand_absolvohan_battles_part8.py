#!/usr/bin/env python3
"""
tools/expand_absolvohan_battles_part8.py
Expands the 5 pre-apotheosis Ordeal tactical engagements in SOMNARAK-WORLD/The_Absolvohan/Part_8_Days_149_to_177.md
with full Gameplay Battle System (GBS) Reverie Directorate Style mechanics:
1. The Spark of Transformation (Pale Dawn)
2. The Sleeping Choir (Lament Dusk)
3. The Choral Harmony (Pale Midnight)
4. The Dawn Corona (Pale Midnight)
5. The Gathering Dawn (Pale Midnight)
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

filepath = "SOMNARAK-WORLD/The_Absolvohan/Part_8_Days_149_to_177.md"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# -------------------------------------------------------------
# 1. The Spark of Transformation (Pale Dawn)
# -------------------------------------------------------------
box_spark_hud = make_box("COMBAT WORK HUD: PHASE 01 — BATTLE TURN 01 (SPARK OF DAWN)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [FIREFLIES]   [PARK]          [SEIYON]               [MAJIN]",
    "DIST    : Fireflies at N02; Park at N03 (Band 1); Seiyon at N05 (Console).",
    "---",
    "Agent Park          : Speed 6 -> 3 AP | HP: 140/140 | SP: +45 | Lament Requiem",
    "Secretary Seiyon    : Speed 5 -> 3 AP | HP: 200/200 | SP: +50 | Acoustic Matrix",
    "Floating Fireflies  : Speed 5 -> 3 AP | HP: 300/300 | Sorrow: 30% | Life Shock"
])

box_spark_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Seiyon tunes acoustic conduit; Park channels gentle Flerehan wave.",
    "- Turn 03: Fireflies hit 60% Stagger 1; sorrow frequency converts to Hope.",
    "- Turn 04: Fireflies encircle open manifold; Seiyon opens intake valve.",
    "- Turn 05: Park executes Viderehan harmonic lock, aligning energy phases.",
    "- Turn 06: Harmonic communion complete; entities merge smoothly into pipes."
])

box_spark_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Retrofit Vault dispersal lines pre-charged (+0.05t).",
    "2. Status Equilibrium : Atmospheric resonance tranquil; team SP at max.",
    "3. Containment Check   : Gentle Life Shock integrated into plumbing safely.",
    "4. OUTCOME             : ZERO WEAPON DISCHARGES — PERFECT HARMONIC CLEAR."
])

old_spark = """Three floating Pale fireflies manifested directly above the open dispersal manifold during welding. Instead of engaging with weapons, Seiyon synchronized the facility's acoustic field, absorbing the entities peacefully into the plumbing system to charge the lines."""

new_spark = f"""Three floating Pale fireflies manifest directly above the open dispersal manifold during welding, pulsing with concentrated primordial life shock!

Director Majin establishes GBS tactical engagement parameters for mid-combat communion:

```text
{box_spark_hud}
```

###### Turn 01 Action Resolution Log (Floor 1 Retrofit Vault)
- **Step 1: Floor 1 Echo-Core Resonance (Director Majin & Secretary Seiyon)**:
  * Seiyon deploys *The Acoustic Matrix*, tuning Floor 1's resonance dampers to match the fireflies' gentle 432Hz frequency.
- **Step 2: Movement & Action Point Spending**:
  * Secretary Seiyon (Speed 5 -> 3 AP) operates from Node 5 (Mid-Field Range Band 3). Spends 2 AP to execute `[Flerehan Acoustic Synchronization]`. Remaining 1 AP in Guard.
  * Agent Park (Speed 6 -> 3 AP) steps up to Node 3 (Close Range Band 2). Spends 2 AP to channel non-lethal `[Lament Requiem Pure Harmonic Weeping]`.
- **Step 3: Clash Resolution (Harmonic Communion)**:
  * Floating Fireflies declare `[Gentle Life Shockwave]` (Base 9 + 2 Coins = 13 Power).
  * Seiyon's `[Flerehan Acoustic Synchronization]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Seiyon WINS THE CLASH (15 vs 13).
    * The acoustic wave wraps the fireflies in gentle, soothing counter-frequencies. Their agitation drops instantly, lowering their Sorrow Gauge by 25% and inflicting +24 Stagger without dealing vessel damage!
  * Park channels pure harmonic weeping from Node 3, aligning the fireflies' energy vectors toward the manifold intake.

```text
{box_spark_turns}
```

```text
{box_spark_phase}
```

Three floating Pale fireflies manifested directly above the open dispersal manifold during welding. Instead of engaging with weapons, Seiyon synchronized the facility's acoustic field, absorbing the entities peacefully into the plumbing system to charge the lines."""

if old_spark in text:
    text = text.replace(old_spark, new_spark)
    print("Replaced Spark of Transformation section successfully!")
else:
    print("Could not find Spark of Transformation section!")

# -------------------------------------------------------------
# 2. The Sleeping Choir (Lament Dusk)
# -------------------------------------------------------------
box_choir_hud = make_box("COMBAT WORK HUD: PHASE 01 — BATTLE TURN 01 (SLEEPING CHOIR)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [SPIRIT-A][SPIRIT-B]  [SHIN]  [DEKAN]                         [MAJIN]",
    "DIST    : Spirits at N02; Shin at N04 (Band 2); Dekan at N05 (Aegis).",
    "---",
    "Agent Shin          : Speed 6 -> 3 AP | HP: 135/135 | SP: +45 | Choral Staff",
    "Attendant Dekan     : Speed 5 -> 3 AP | HP: 215/215 | SP: +50 | Maw's Aegis",
    "Sleep-Spirits(x2)   : Speed 5 -> 3 AP | HP: 360 each | Trance Pulse"
])

box_choir_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Shin sings the first verse; Dekan shields acoustic bounce; 60% Stagger 1.",
    "- Turn 03: Posture broken; spirits lower arms in peaceful reverie; Sorrow at 10%.",
    "- Turn 04: Spirits hum the Maw's lullaby; Shin matches pitch with Choral Staff.",
    "- Turn 05: Dekan projects soothing barrier, nullifying trance pressure.",
    "- Turn 06: Shin sings final verse; spirits bow and dissolve into clear water."
])

box_choir_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Floor 2 Gallery acoustics clear and pure.",
    "2. Status Equilibrium : Trance fog dissolves; team SP at full capacity.",
    "3. Containment Check   : Sleep-Spirits transformed into holy mineral water.",
    "4. OUTCOME             : ZERO CONFLICT — HISTORIC LULLABY RESOLUTION."
])

old_choir = """Two sleep-spirits manifested on Floor 2 during the Dusk Ordeal. Instead of clashing, Agent Shin sang the final verse of *Sleep Under the Willow*. The spirits bowed respectfully toward the Maw, dissolving into clear, blessed mineral water without conflict."""

new_choir = f"""Two sleep-spirits manifest on Floor 2 during the Dusk Ordeal, radiating a heavy 95dB trance frequency down the gallery!

Director Majin establishes GBS tactical parameters for melodic pacification:

```text
{box_choir_hud}
```

###### Turn 01 Action Resolution Log (Floor 2 Gallery)
- **Step 1: Floor 2 Echo-Core Resonance (Attendant Dekan)**:
  * Dekan deploys *The Maw's Keep Bastion Ward*, projecting a soft acoustic dampening dome that prevents the trance pulses from escaping into clerk dormitories.
- **Step 2: Movement & Action Point Spending**:
  * Agent Shin (Speed 6 -> 3 AP) advances to Node 4 (Close Range Band 2). Spends 2 AP to channel `[Choral Staff Melodic Communion: Sleep Under the Willow]`. Remaining 1 AP in Guard.
  * Attendant Dekan (Speed 5 -> 3 AP) stands at Node 5, spending 2 AP to maintain *Maw's Aegis*.
- **Step 3: Clash Resolution (Melodic Harmony)**:
  * Sleep-Spirits emit `[Gentle Trance Pulse]` (Base 10 + 2 Coins = 14 Power).
  * Agent Shin's `[Melodic Communion]` (Base 12 + 2 Coins = 16 Power).
  * **Resolution**: Shin WINS THE CLASH (16 vs 14).
    * Shin's vocal resonance matches the spirits' ancient cadence perfectly. The discordant trance melts into gentle sorrow, lowering their Sorrow Gauge by 35% and inflicting +28 Stagger!

```text
{box_choir_turns}
```

```text
{box_choir_phase}
```

Two sleep-spirits manifested on Floor 2 during the Dusk Ordeal. Instead of clashing, Agent Shin sang the final verse of *Sleep Under the Willow*. The spirits bowed respectfully toward the Maw, dissolving into clear, blessed mineral water without conflict."""

if old_choir in text:
    text = text.replace(old_choir, new_choir)
    print("Replaced Sleeping Choir section successfully!")
else:
    print("Could not find Sleeping Choir section!")

# -------------------------------------------------------------
# 3. The Choral Harmony (Pale Midnight)
# -------------------------------------------------------------
box_harmony_hud = make_box("COMBAT WORK HUD: PHASE 01 — BATTLE TURN 01 (CHORAL HARMONY)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [AVIAN-SHADOW] [HAN]   [SONG]          [THREE-BIRDS]          [DEKAN]",
    "DIST    : Shadow at N02; Han at N03 (Band 1); Song at N04 (Band 2); Birds at N06.",
    "---",
    "Agent Han           : Speed 6 -> 3 AP | HP: 145/145 | SP: +50 | Feather Mantle",
    "Agent Song          : Speed 6 -> 3 AP | HP: 140/140 | SP: +45 | Cherub's Lyre",
    "Avian Silhouette    : Speed 5 -> 3 AP | HP: 480/480 | Pale Light | Midnight Core"
])

box_harmony_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Han matches vocal octave; Song plays lyre; Shadow hits 60% Stagger 1.",
    "- Turn 03: Posture broken; Three Birds chime in unison; Pale light softens.",
    "- Turn 04: Silhouette spreads wings; Dekan channels Maw's grounding field.",
    "- Turn 05: Han & Song execute Flerehan duet, dissolving lingering Before-Time grief.",
    "- Turn 06: Celestial light merges into conduits; accumulators charge to max."
])

box_harmony_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Bird Rotunda accumulators charged with Pale energy.",
    "2. Status Equilibrium : All agents healed; SP overflowing at maximum +50.",
    "3. Containment Check   : Celestial Avian Silhouette peacefully absorbed.",
    "4. OUTCOME             : HISTORIC MIDNIGHT HARMONY — ZERO CASUALTIES."
])

old_harmony = """A Midnight Ordeal manifested as a celestial avian silhouette in the central rotunda of Floor 2. Agents Han and Song harmonized their voices with the construct, which bowed gracefully and dissolved into the ceiling conduits, charging the facility's accumulators with pure Pale energy."""

new_harmony = f"""A Midnight Ordeal manifests as a celestial avian silhouette in the central rotunda of Floor 2, shimmering with pure, transmutative Pale light!

Director Majin establishes GBS tactical parameters in the Bird Rotunda:

```text
{box_harmony_hud}
```

###### Turn 01 Action Resolution Log (Floor 2 Bird Rotunda)
- **Step 1: Floor 2 Echo-Core Resonance (Attendant Dekan)**:
  * Dekan opens the rotunda acoustic channels, allowing the harmonic chime of the Three Birds to reverberate across Nodes 1 to 6.
- **Step 2: Movement & Action Point Spending**:
  * Agent Han (Speed 6 -> 3 AP) stands at Node 3 (Point-Blank Range Band 1). Spends 2 AP to declare `[Feather Mantle Avian Choral Calling]`. Remaining 1 AP held in Guard.
  * Agent Song (Speed 6 -> 3 AP) advances to Node 4 (Close Range Band 2). Spends 2 AP to ready `[Cherub's Lyre Resonant Accord]`.
- **Step 3: Clash Resolution (Avian Harmonic Equilibrium)**:
  * Celestial Avian Silhouette radiates `[Transmutative Pale Dawn Aura]` (Base 11 + 2 Coins = 15 Power).
  * Agent Han & Agent Song's `[Resonant Choral Accord]` (Base 13 + 2 Coins = 17 Power).
  * **Resolution**: The Agents WIN THE CLASH (17 vs 15).
    * Their synchronized vocal octave matches the silhouette's vibration, converting the lethal Pale sunder into golden life energy and inflicting +32 Stagger!

```text
{box_harmony_turns}
```

```text
{box_harmony_phase}
```

A Midnight Ordeal manifested as a celestial avian silhouette in the central rotunda of Floor 2. Agents Han and Song harmonized their voices with the construct, which bowed gracefully and dissolved into the ceiling conduits, charging the facility's accumulators with pure Pale energy."""

if old_harmony in text:
    text = text.replace(old_harmony, new_harmony)
    print("Replaced Choral Harmony section successfully!")
else:
    print("Could not find Choral Harmony section!")

# -------------------------------------------------------------
# 4. The Dawn Corona (Pale Midnight)
# -------------------------------------------------------------
box_corona_hud = make_box("COMBAT WORK HUD: PHASE 01 — BATTLE TURN 01 (DAWN CORONA)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [TWELVE-HALOS] [AYSHUK][APOSTLES]                             [MAJIN]",
    "DIST    : Halos at N02; Ayshuk at N03 (Band 1); Apostles at N04-N05.",
    "---",
    "Research Lead Ayshuk: Speed 6 -> 3 AP | HP: 200/200 | SP: +50 | Insight Forge",
    "Twelve Apostles     : Speed 5 -> 3 AP | HP: 150/150 | SP: +45 | Consecrated Vow",
    "Dawn Corona         : Speed 5 -> 3 AP | HP: 500/500 | Sorrow: 20% | Cleansing"
])

box_corona_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Ayshuk raises arms; predictive HUD aligns angles; 60% Stagger 1.",
    "- Turn 03: Posture broken; halos descend gently toward apostle ranks.",
    "- Turn 04: Corona pulses warm Pale cleansing light; Ayshuk stabilizes field.",
    "- Turn 05: Viderehan communion complete; twelve halos crown the apostles.",
    "- Turn 06: Anomaly dissolves into radiant peace; research hub fully sanctified."
])

box_corona_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Research Hub bathed in perpetual warm dawn light.",
    "2. Status Equilibrium : All twelve apostles crowned; team SP at absolute max.",
    "3. Containment Check   : Dawn Corona fully transmuted into blessing.",
    "4. OUTCOME             : HISTORIC TRANSCENDENCE — ZERO CASUALTIES."
])

old_corona = """A Midnight Ordeal manifested as a crown of twelve glowing halos above the research hub. Ayshuk stepped into the center of the light, raising her arms. The halos gently descended, settling onto the heads of the twelve apostles and dissolving the anomaly into radiant peace."""

new_corona = f"""A Midnight Ordeal manifests as a crown of twelve glowing halos above the research hub, radiating high-order Pale cleansing pulses!

Director Majin establishes GBS tactical parameters in the Insight Forge:

```text
{box_corona_hud}
```

###### Turn 01 Action Resolution Log (Floor 4 Research Hub)
- **Step 1: Floor 4 Echo-Core Resonance (Research Lead Ayshuk)**:
  * Ayshuk activates *The Predictive HUD*, analyzing the twelve halos' geometric trajectory and projecting golden descent angles for each apostle.
- **Step 2: Movement & Action Point Spending**:
  * Research Lead Ayshuk (Speed 6 -> 3 AP) steps into the center of Node 3 (Point-Blank Range Band 1). Spends 2 AP to declare `[Insight Forge Communion: Open Arms of Dawn]`. Remaining 1 AP in Guard.
  * Twelve Apostles (Speed 5 -> 3 AP) kneel across Nodes 4 and 5 in open communion, spending 2 AP to channel `[Consecrated Vow Harmonic Alignment]`.
- **Step 3: Clash Resolution (Cleansing Light Accord)**:
  * Dawn Corona unleashes `[Cleansing Pale Descent]` (Base 12 + 2 Coins = 16 Power).
  * Ayshuk's `[Open Arms of Dawn]` (Base 14 + 2 Coins = 18 Power).
  * **Resolution**: Ayshuk WINS THE CLASH (18 vs 16).
    * Ayshuk embraces the blinding light directly. Her calm analytical composure transmutes the scouring wave into gentle starlight, lowering its Sorrow Gauge to 0% and triggering peaceful Stagger!

```text
{box_corona_turns}
```

```text
{box_corona_phase}
```

A Midnight Ordeal manifested as a crown of twelve glowing halos above the research hub. Ayshuk stepped into the center of the light, raising her arms. The halos gently descended, settling onto the heads of the twelve apostles and dissolving the anomaly into radiant peace."""

if old_corona in text:
    text = text.replace(old_corona, new_corona)
    print("Replaced Dawn Corona section successfully!")
else:
    print("Could not find Dawn Corona section!")

# -------------------------------------------------------------
# 5. The Gathering Dawn (Pale Midnight)
# -------------------------------------------------------------
box_gathering_hud = make_box("COMBAT WORK HUD: PHASE 01 — BATTLE TURN 01 (GATHERING DAWN)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [PALE-CLOUD]  [LEADS-1-4]      [LEADS-5-8]            [VALVES]",
    "DIST    : Cloud at N02; Leads 1-4 at N03; Leads 5-8 at N05; Valves at N09.",
    "---",
    "Eight Attendants    : Speed 6 -> 3 AP | Team Synergy | Resonance Overdrive",
    "Gathering Dawn Cloud: Speed 5 -> 3 AP | HP: 600/600 | Sovereign Pale Pulse"
])

box_gathering_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: All 8 Leads unify auras; cloud condenses; 60% Stagger 1.",
    "- Turn 03: Posture broken; Pale vapor liquefies into radiant golden fluid.",
    "- Turn 04: Cloud blankets the twelve release valves without friction.",
    "- Turn 05: Zyrak & Dekan channel pneumatic conduits; pistons lubricated.",
    "- Turn 06: Final condensation complete; valves primed for Day 160 release."
])

box_gathering_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : All 12 release valves coated in friction-free gold.",
    "2. Status Equilibrium : Atmospheric pressure at absolute optimum.",
    "3. Containment Check   : Sovereign Pale energy converted to valve lubricant.",
    "4. OUTCOME             : HISTORIC TRANSCENDENCE — READY FOR DAY 160 RELEASE."
])

old_gathering = """A Midnight Ordeal manifested as a luminous cloud of Pale energy that settled over the twelve release valves. All eight leads joined their auras, condensing the cloud into liquid golden lubricant that coated the valve pistons, ensuring friction-free release."""

new_gathering = f"""A Midnight Ordeal manifests as a luminous cloud of Pale energy settling over the twelve release valves at the facility wellhead!

Director Majin coordinates the Eight-Lead Echo-Core convergence on the 10-node grid:

```text
{box_gathering_hud}
```

###### Turn 01 Action Resolution Log (Floor 1 Retrofit Vault Wellhead)
- **Step 1: Universal Echo-Core Resonance (The Eight Attendants)**:
  * Majin, Seiyon, Dekan, Zyrak, Ayshuk, Mellda, Marjuk, and Ishall join their department auras across Nodes 3 to 6, creating an absolute unified field.
- **Step 2: Movement & Action Point Spending**:
  * Lower Floor Leads (Nodes 3–4) spend 2 AP to maintain *The Kinetic and Acoustic Crucible*.
  * Upper Floor Leads (Nodes 5–6) spend 2 AP to channel *The Temporal and Archive Condensation Array*.
- **Step 3: Clash Resolution (The Eightfold Resonance)**:
  * Gathering Dawn Cloud pulses `[Primordial Awakening Wave]` (Base 13 + 2 Coins = 17 Power).
  * The Eight Leads' `[Unified Attendant Aura]` (Base 15 + 2 Coins = 19 Power).
  * **Resolution**: The Attendants WIN THE CLASH (19 vs 17).
    * The combined force of the eight department auras condenses the gaseous Pale anomaly into a thick, glowing golden fluid, coating the pistons of the twelve release valves!

```text
{box_gathering_turns}
```

```text
{box_gathering_phase}
```

A Midnight Ordeal manifested as a luminous cloud of Pale energy that settled over the twelve release valves. All eight leads joined their auras, condensing the cloud into liquid golden lubricant that coated the valve pistons, ensuring friction-free release."""

if old_gathering in text:
    text = text.replace(old_gathering, new_gathering)
    print("Replaced Gathering Dawn section successfully!")
else:
    print("Could not find Gathering Dawn section!")

check_banned(text, filepath)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
print(f"Updated {filepath} with all expanded GBS battles!")
