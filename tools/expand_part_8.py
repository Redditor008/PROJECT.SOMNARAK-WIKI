#!/usr/bin/env python3
"""
tools/expand_part_8.py
Expands Part 8 (Days 149 to 177) into an exhaustive operational chronicle:
- Full turn-by-turn combat and harmonic communion logs for Days 149, 151, 153, 155, 157 across Turns 02 to 06.
- Enforces 100% box symmetry and dual-environment typography (<= 71 chars for boxes).
"""

def make_box(title, rows, width=71):
    top = "+" + "=" * (width - 2) + "+"
    bottom = "+" + "=" * (width - 2) + "+"
    sep = "+" + "-" * (width - 2) + "+"
    
    out = [top]
    if title:
        title_str = f" {title} "
        out.append(f"|{title_str.center(width - 2)}|")
        out.append(sep)
    
    for r in rows:
        if r == "---":
            out.append(sep)
        elif r.startswith("==="):
            out.append(top)
        else:
            text = r[:width - 4]
            out.append(f"| {text.ljust(width - 4)} |")
    out.append(bottom)
    return "\n".join(out)

# --- DAY 149 EXPANSION ---
def get_day_149_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: HARMONIC COMMUNION — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 1 RETROFIT VAULT CONDUITS]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[FIREFLIES]     [PARK]          [SEIYON]                [MAJIN]         ",
        "---",
        "- Node 01: Swarm of Twilight Fireflies (Agitation 52/120 / 432Hz)",
        "- Node 03: Agent Park (Range Band 2 / Flerehan Acoustic Staff)",
        "- Node 05: Secretary Seiyon (Range Band 3 / Tuning Conduit Valves)",
        "- Node 08: Director Majin (Command Console / Manifold Monitoring)",
        "---",
        "- Seiyon      : Spd 5 -> 3 AP | HP 120/120 | SP +40 | Posture 70/70",
        "- Agent Park  : Spd 6 -> 3 AP | HP 120/120 | SP +35 | Posture 65/65",
        "- Fireflies   : Spd 4 -> 2 AP | Agitation 52/120 [60% STAGGER TRIGGERED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: HARMONIC COMMUNION — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — HARMONIC STAGGER & HOPE CONVERSION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [SWARM] [PARK]          [SEIYON]                [MAJIN]         ",
        "---",
        "- Node 02: Swarm (Advancing Calmly / Agitation 28/120 / Hope 75%)",
        "- Node 03: Agent Park (Momentum Surge / Choral Resonance Amplified)",
        "- Node 05: Secretary Seiyon (Priming Manifold Intake Flanges)",
        "---",
        "- Seiyon      : Spd 5 -> 3 AP | HP 120/120 | SP +40 | Posture 70/70",
        "- Agent Park  : Spd 8 -> 4 AP [SURGE] | HP 120/120 | SP +35 | Posture 65/65",
        "- Fireflies   : Spd 3 -> 1 AP | Agitation 28/120 | Hope Index +75%"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: HARMONIC COMMUNION — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MANIFOLD CIRCULATION & INTAKE ALIGNMENT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                [SWARM] [PARK]  [SEIYON]                [MAJIN]         ",
        "---",
        "- Node 03: Fireflies Swarm (Encircled Around Open Acoustic Valve)",
        "- Node 04: Agent Park (Directional Guard Absorption / Guided Flow)",
        "- Node 05: Secretary Seiyon (Opening Primary Intake Manifold)",
        "---",
        "- Seiyon      : Spd 5 -> 3 AP | HP 120/120 | SP +40 | Posture 70/70",
        "- Agent Park  : Spd 8 -> 4 AP | HP 120/120 | SP +35 | Posture 65/65",
        "- Fireflies   : Spd 2 -> 1 AP | Agitation 12/120 | Hope Index +90%"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: HARMONIC COMMUNION — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER & VIDEREHAN LOCK]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                        [INTAKE][SEIYON]                [MAJIN]         ",
        "                        [PARK]",
        "---",
        "- Node 04: Fireflies (TERMINAL STAGGER / AGITATION 0/120 / PURE HOPE)",
        "- Node 04: Agent Park (Executing Viderehan Harmonic Phase Lock)",
        "- Node 05: Secretary Seiyon (Aligning Pressure Gradients)",
        "---",
        "- Fireflies   : Spd 0 -> 0 AP | Agitation 0/120 | Transmutation: 100%"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: HARMONIC COMMUNION — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — INTEGRATION & RESERVOIR CHARGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                        [CLEAR] [SEIYON]                [MAJIN]         ",
        "                                [PARK]",
        "---",
        "- Node 04: Conduits (Seamless Fluid Integration / Zero Loss)",
        "- Node 05: Secretary Seiyon (Logging +0.025 Tons Refined Han)",
        "- Node 08: Director Majin (Confirming Absolute Reservoir Stability)",
        "---",
        "- Fireflies   : INTEGRATED | +0.025 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Conduit Tuning & Harmonic Stagger)
- **Acoustic Alignment & Stagger Induction**:
  * Secretary Seiyon tunes the Floor 1 acoustic bypass to resonate at exactly 432.18 Hz.
  * Agent Park channels a gentle Flerehan wave from Node 03:
    * Deals **0 Physical Harm**, delivering **38 Harmonic Pacification Points**!
    * Agitation drops to **52/120**, crossing the **60% Stagger Threshold (72 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The fireflies cease defensive darting and begin a slow, synchronized orbital dance.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Hope Conversion & Momentum Surge)
- **Resonant Harmonization (1.5x Harmonic Multiplier)**:
  * Agent Park's `Momentum Surge` activates! (+2 Speed next turn).
  * Park channels pure weeping accord, converting remaining sorrow frequencies into golden Hope.
  * Firefly Agitation drops to **28/120**; swarm Hope index rises to **+75%**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Manifold Ingress & Guided Stream)
- **Acoustic Ingress**:
  * The firefly swarm drifts toward the open intake manifold at Node 04.
  * Secretary Seiyon uses `[Directional Guard Absorption]` to cushion atmospheric back-pressure, ensuring no turbulence harms the delicate light bodies.
  * Swarm Agitation drops to **12/120**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Harmonic Stagger & Viderehan Lock)
- **Viderehan Harmonic Phase Lock**:
  * Park delivers the Viderehan chord from the Flerehan staff, stripping the final 12 Agitation points!
  * **TERMINAL STAGGER TRIGGERED!** Agitation reaches **0/120**. The swarm aligns into an unbroken ribbon of pure golden luminescence.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Integration & Reservoir Harvest)
- **Seamless Conduit Ingestion**:
  * The golden ribbon glides into the secondary collection conduits without friction.
  * Floor 1 reservoirs register **+0.025 tons of refined Han**!
"""

# --- DAY 151 EXPANSION ---
def get_day_151_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: SPIRITUAL PACIFICATION — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 2 DORMITORY VAULT GALLERY]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SPIRITS]       [SHIN]  [DEKAN]                         [MAJIN]         ",
        "---",
        "- Node 01: Sleep-Spirits (Sorrow 46/130 / Sinking into Deep Reverie)",
        "- Node 03: Agent Shin (Range Band 2 / Singing First Verse of Lullaby)",
        "- Node 04: Attendant Dekan (Range Band 2 / Maw Bastion Acoustic Ward)",
        "- Node 08: Director Majin & Attendants (Gallery Acoustic Overlook)",
        "---",
        "- Agent Shin  : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Dekan       : Spd 5 -> 3 AP | HP 210/210 | SP +40 | Posture 105/105",
        "- Spirits     : Spd 3 -> 1 AP | Sorrow 46/130 [60% STAGGER TRIGGERED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: SPIRITUAL PACIFICATION — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK & REVERIE DESCENT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [SPIRITS][SHIN] [DEKAN]                         [MAJIN]         ",
        "---",
        "- Node 02: Spirits (Arms Lowered in Peace / Sorrow 24/130)",
        "- Node 03: Agent Shin (Momentum Surge / Second Verse Chanted)",
        "- Node 04: Attendant Dekan (Shielding Acoustic Bounce off Vault Walls)",
        "---",
        "- Agent Shin  : Spd 8 -> 4 AP [SURGE] | HP 125/125 | SP +35 | Posture 65/65",
        "- Dekan       : Spd 5 -> 3 AP | HP 210/210 | SP +40 | Posture 105/105",
        "- Spirits     : Spd 2 -> 1 AP | Sorrow 24/130 | Agitation Transmuted"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: SPIRITUAL PACIFICATION — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAW'S LULLABY & HARMONIC MIRROR]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                [SPIRITS][SHIN][DEKAN]                  [MAJIN]         ",
        "---",
        "- Node 03: Sleep-Spirits (Humming in Synchrony with Choral Staff)",
        "- Node 04: Agent Shin (Matching Pitch with Ancient Floor Canticle)",
        "- Node 05: Attendant Dekan (Directional Guard / Nullifying Discord)",
        "---",
        "- Agent Shin  : Spd 8 -> 4 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Dekan       : Spd 5 -> 3 AP | HP 210/210 | SP +40 | Posture 105/105",
        "- Spirits     : Spd 2 -> 1 AP | Sorrow 10/130 | Trance Pacified"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: SPIRITUAL PACIFICATION — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER & SOOTHING BARRIER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                        [SPIRITS]                       [MAJIN]         ",
        "                        [SHIN]  [DEKAN]",
        "---",
        "- Node 04: Sleep-Spirits (TERMINAL STAGGER / SORROW 0/130 / PEACEFUL)",
        "- Node 04: Agent Shin (Final Verse Resonance Complete)",
        "- Node 05: Attendant Dekan (Opening Bedrock Drain Wells)",
        "---",
        "- Spirits     : Spd 0 -> 0 AP | Sorrow 0/130 | Transmutation: 100%"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: SPIRITUAL PACIFICATION — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — DISSOLUTION & CLEAR WATER RECEPTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                        [WATER] [SHIN]  [DEKAN]         [MAJIN]         ",
        "---",
        "- Node 04: Sleep-Spirits (Dissolved into Pure Living Crystalline Water)",
        "- Node 05: Floor 2 Ballast Well (Absorbing Clean Hydrological Han)",
        "---",
        "- Spirits     : PACIFIED | +0.024 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (First Verse & Spiritual Stagger)
- **Melodic Cadence & Shielded Reflection**:
  * Agent Shin sings the opening verse of the ancient lullaby from Node 03.
  * Attendant Dekan anchors his tower shield at Node 04, preventing acoustic backwash from disorienting the gallery:
    * Spirits absorb **42 Melodic Pacification Points**!
    * Sorrow drops to **46/130**, breaching the **60% Stagger Threshold (78 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The spirits lower their ethereal limbs and close their weeping eyes.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Peaceful Reverie & Momentum Surge)
- **Gentle Slumber (1.5x Harmonic Multiplier)**:
  * Agent Shin's `Momentum Surge` activates! (+2 Speed next turn).
  * Shin's second verse reverberates through the vault, dissolving centuries of trapped sorrow into calm stillness.
  * Sorrow drops to **24/130**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Harmonic Resonance & Pitch Match)
- **Synchronized Canticle**:
  * The sleep-spirits echo Shin's melody, humming the Maw's ancestral slumber refrain.
  * Dekan deploys `[Directional Guard Absorption]`, completely dampening any lingering spiritual pressure.
  * Sorrow falls to **10/130**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger & Soothing Barrier)
- **Final Harmonic Release**:
  * Shin sustains the concluding harmonic chord, removing the final 10 Sorrow points!
  * **TERMINAL STAGGER TRIGGERED!** Sorrow reaches **0/130**. The spirits bow in gratitude.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Dissolution into Clear Water & Harvest)
- **Purity Dissolution**:
  * The spirits dissolve softly into sparkling, clear crystalline water that flows directly into Floor 2's deep cisterns.
  * Ballast telemetry records **+0.024 tons of refined Han**!
"""

# --- DAY 153 EXPANSION ---
def get_day_153_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: CELESTIAL EQUILIBRIUM — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 2 BIRD ROTUNDA]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[AVIAN]         [HAN]   [SONG]  [DEKAN]                         [MAJIN] ",
        "---",
        "- Node 01: Celestial Silhouette (Pale Resonance 54/140 / 60% Stagger)",
        "- Node 03: Agent Han (Range Band 2 / Feather Mantle Vocal Resonance)",
        "- Node 04: Agent Song (Range Band 2 / Cherub's Lyre Harmonic Chords)",
        "- Node 05: Attendant Dekan (Range Band 3 / Maw Grounding Pylons)",
        "---",
        "- Agent Han   : Spd 6 -> 3 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Agent Song  : Spd 6 -> 3 AP | HP 120/120 | SP +35 | Posture 60/60",
        "- Silhouette  : Spd 4 -> 2 AP | Pale 54/140 [60% STAGGER TRIGGERED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: CELESTIAL EQUILIBRIUM — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — THREE BIRDS CHIME & LIGHT SOFTENING]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [AVIAN] [HAN]   [SONG]  [DEKAN]                         [MAJIN] ",
        "---",
        "- Node 02: Celestial Silhouette (Wings Folded / Pale Light Warm Gold)",
        "- Node 03: Agent Han (Momentum Surge / High-Octave Flerehan Duet)",
        "- Node 04: Agent Song (Lyre Strings Chiming in Perfect Fifths)",
        "---",
        "- Agent Han   : Spd 8 -> 4 AP [SURGE] | HP 125/125 | SP +35 | Posture 65/65",
        "- Agent Song  : Spd 6 -> 3 AP | HP 120/120 | SP +35 | Posture 60/60",
        "- Silhouette  : Spd 3 -> 1 AP | Pale 26/140 | Sorrow Converting"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: CELESTIAL EQUILIBRIUM — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — WING EXTENSION & GROUNDING FIELD]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                [AVIAN] [HAN]   [SONG]  [DEKAN]                 [MAJIN] ",
        "---",
        "- Node 03: Avian Silhouette (Extending Wings in Graceful Display)",
        "- Node 04: Agent Han & Song (Singing Before-Time Forgiveness Refrain)",
        "- Node 06: Attendant Dekan (Directional Guard Absorption Active)",
        "---",
        "- Agent Han   : Spd 8 -> 4 AP | HP 125/125 | SP +35 | Posture 65/65",
        "- Silhouette  : Spd 2 -> 1 AP | Pale 10/140 | Resonance Stabilized"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: CELESTIAL EQUILIBRIUM — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER & FLEREHAN DUET]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                        [AVIAN]                                 [MAJIN] ",
        "                        [HAN]   [SONG]  [DEKAN]",
        "---",
        "- Node 04: Silhouette (TERMINAL STAGGER / PALE 0/140 / PURE DAWN LIGHT)",
        "- Node 04: Agent Han & Song (Flerehan Duet Climaxes in Absolute Accord)",
        "---",
        "- Silhouette  : Spd 0 -> 0 AP | Pale 0/140 | Transmutation: 100%"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: CELESTIAL EQUILIBRIUM — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CELESTIAL MERGER & CONDUIT CHARGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                        [LIGHT] [HAN]   [SONG]  [DEKAN]         [MAJIN] ",
        "---",
        "- Node 04: Celestial Light (Merging Gracefully into Accumulators)",
        "- Node 05: Attendant Dekan (Logging Full Conduit Charging)",
        "---",
        "- Silhouette  : PACIFIED | +0.026 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Avian Octave & Pale Stagger)
- **Octave Convergence & Bell Resonance**:
  * Agent Han matches the avian frequency with vocal precision, while Agent Song strums the resonant chords on the lyre.
  * Attendant Dekan grounds the rotunda floorplates:
    * Silhouette absorbs **44 Harmonization Points**!
    * Pale resonance drops to **54/140**, crossing the **60% Stagger Threshold (84 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The avian silhouette folds its luminous wings and emits a clear, bell-like ring.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Three Birds Chime & Momentum Surge)
- **Harmonic Chord Progression (1.5x Multiplier)**:
  * Agent Han's `Momentum Surge` activates! (+2 Speed next turn).
  * The chimes of Big Bird, Judgement Bird, and Punishing Bird echo through the acoustic chambers, softening the Pale light into warm amber dawn.
  * Pale resonance drops to **26/140**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Avian Grace & Grounding Field)
- **Maw Grounding Field**:
  * The silhouette stretches its wings wide, showering the chamber in soft golden feathers.
  * Attendant Dekan deploys `[Directional Guard Absorption]`, grounding the intense luminescence into the containment batteries.
  * Pale resonance falls to **10/140**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger & Flerehan Duet)
- **Forgiveness Duet & Terminal Peace**:
  * Han and Song execute the climactic Flerehan duet, stripping the final 10 Pale points!
  * **TERMINAL STAGGER TRIGGERED!** Pale resonance drops to **0/140**. All ancient sorrow dissolves into brilliant clarity.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Celestial Merger & Battery Charge)
- **Accumulator Infusion**:
  * The celestial light flows like liquid gold into the rotunda accumulators, filling them to maximum capacity.
  * Energy telemetry logs **+0.026 tons of refined Han**!
"""

# --- DAY 155 EXPANSION ---
def get_day_155_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: CORONA STABILIZATION — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 4 RESEARCH HUB PLAZA]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CORONA]        [AYSHUK][APOSTLES]                      [MAJIN]         ",
        "---",
        "- Node 01: Dawn Corona (Cleansing Radiation 56/150 / 60% Stagger)",
        "- Node 03: Research Lead Ayshuk (Predictive HUD Projecting Trajectories)",
        "- Node 04: Twelve Apostles (Range Band 2 / Consecrated Vows Intact)",
        "- Node 08: Director Majin & Attendants (Observation Rail)",
        "---",
        "- Ayshuk      : Spd 6 -> 3 AP | HP 135/135 | SP +40 | Posture 75/75",
        "- Apostles    : Spd 5 -> 3 AP | HP 150/150 | SP +40 | Posture 80/80",
        "- Corona      : Spd 4 -> 2 AP | Pale 56/150 [60% STAGGER TRIGGERED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: CORONA STABILIZATION — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — HALO DESCENT & SANITY TRANSFERENCE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [CORONA][AYSHUK][APOSTLES]                      [MAJIN]         ",
        "---",
        "- Node 02: Dawn Corona (Twelve Halos Hovering Above Operatives)",
        "- Node 03: Research Lead Ayshuk (Momentum Surge / Alignment Vector Max)",
        "- Node 04: Apostles (Receiving Descending Halos Without Burn)",
        "---",
        "- Ayshuk      : Spd 8 -> 4 AP [SURGE] | HP 135/135 | SP +40 | Posture 75/75",
        "- Apostles    : Spd 5 -> 3 AP | HP 150/150 | SP +40 | Posture 80/80",
        "- Corona      : Spd 3 -> 1 AP | Pale 28/150 | Transmuting to Hope"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: CORONA STABILIZATION — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — WARM CLEANSING PULSE & FIELD LOCK]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                [CORONA][AYSHUK][APOSTLES]              [MAJIN]         ",
        "---",
        "- Node 03: Corona (Pulsing Warm Pale Light / Purging Latent Stress)",
        "- Node 04: Research Lead Ayshuk (Directional Guard Absorption Active)",
        "- Node 05: Apostles (Forming Circular Communion Ring)",
        "---",
        "- Ayshuk      : Spd 8 -> 4 AP | HP 135/135 | SP +40 | Posture 75/75",
        "- Corona      : Spd 2 -> 1 AP | Pale 12/150 | Field Equilibrium"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: CORONA STABILIZATION — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER & VIDEREHAN COMMUNION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                        [CORONA]                                [MAJIN] ",
        "                        [AYSHUK][APOSTLES]",
        "---",
        "- Node 04: Dawn Corona (TERMINAL STAGGER / PALE 0/150 / 12 CROWNS REST)",
        "- Node 04: Research Lead Ayshuk & Apostles (Communion Complete)",
        "---",
        "- Corona      : Spd 0 -> 0 AP | Pale 0/150 | Transmutation: 100%"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: CORONA STABILIZATION — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — RESEARCH HUB SANCTIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                        [PEACE] [AYSHUK][APOSTLES]              [MAJIN] ",
        "---",
        "- Node 04: Plaza (Bathed in Radiant Warm Gold / Full Sanctification)",
        "- Node 05: Apostles (Crowned with Twelve Halos of Stable Hope)",
        "---",
        "- Corona      : INTEGRATED | +0.026 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Predictive Alignment & Stagger Build)
- **Analytical Communion & Trajectory Mapping**:
  * Research Lead Ayshuk activates the *Insight Forge HUD*, calculating exact descent vectors for the twelve golden halos.
  * The apostles raise their hands in synchronized reception:
    * Corona absorbs **46 Analytical Communion Points**!
    * Pale radiation drops to **56/150**, crossing the **60% Stagger Threshold (90 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The scouring light ceases its burning heat, shifting to soft celestial dawn.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Halo Descent & Momentum Surge)
- **Gentle Transference (1.5x Communion Multiplier)**:
  * Ayshuk's `Momentum Surge` activates! (+2 Speed next turn).
  * The twelve halos descend in serene arcs, hovering inches above the apostles' heads without releasing dangerous heat.
  * Pale radiation drops to **28/150**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Warm Cleansing Light & Field Stabilization)
- **Purification Pulse**:
  * The corona pulses a soft expanding wave that washes over all research personnel, cleansing lingering fatigue.
  * Ayshuk deploys `[Directional Guard Absorption]`, maintaining perfect thermal balance across the chamber.
  * Pale radiation falls to **12/150**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger & Twelvefold Crowning)
- **Viderehan Communion Finale**:
  * The apostles recite their vows, stripping the final 12 Pale points!
  * **TERMINAL STAGGER TRIGGERED!** Pale radiation reaches **0/150**. The twelve halos settle gently onto their brows as permanent crowns of Hope.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Hub Sanctification & Harvest)
- **Radiant Peace**:
  * The Dawn Corona dissolves into ambient golden tranquility, fully sanctifying the Floor 4 research hub.
  * Collection manifolds log **+0.026 tons of refined Han**!
"""

# --- DAY 157 EXPANSION ---
def get_day_157_combat():
    hud_t02 = make_box("TACTICAL STAGE HUD: PLANETARY CONDENSATION — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FLOOR 1 RETROFIT VAULT WELLHEAD]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CLOUD]         [LOWER-LEADS]   [UPPER-LEADS]                   [MAJIN] ",
        "---",
        "- Node 01: Gathering Dawn Cloud (Atmospheric Pale 62/160 / 60% Stagger)",
        "- Node 03: Lower Leads (Majin, Seiyon, Dekan, Zyrak / Kinetic Crucible)",
        "- Node 05: Upper Leads (Ayshuk, Mellda, Marjuk, Ishall / Condenser Array)",
        "- Node 08: Twelve Main Release Valves (Primed for Hydraulic Stroke)",
        "---",
        "- Lower Leads : Spd 6 -> 3 AP | HP 200/200 | SP +40 | Posture 100/100",
        "- Upper Leads : Spd 6 -> 3 AP | HP 180/180 | SP +40 | Posture 90/90",
        "- Dawn Cloud  : Spd 4 -> 2 AP | Pale 62/160 [60% STAGGER TRIGGERED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: PLANETARY CONDENSATION — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — LIQUEFACTION & GOLDEN FLUID GENESIS]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [LIQUID][LOWER-LEADS]   [UPPER-LEADS]                   [MAJIN] ",
        "---",
        "- Node 02: Dawn Vapor (Liquefying into Dense Golden Fluid / Pale 32/160)",
        "- Node 03: Lower Leads (Momentum Surge / Channelling Pneumatic Flow)",
        "- Node 05: Upper Leads (Stabilizing Viscosity Gradient Across Valves)",
        "---",
        "- Lower Leads : Spd 8 -> 4 AP [SURGE] | HP 200/200 | SP +40 | Posture 100/100",
        "- Upper Leads : Spd 6 -> 3 AP | HP 180/180 | SP +40 | Posture 90/90",
        "- Dawn Cloud  : Spd 3 -> 1 AP | Pale 32/160 | Liquefaction: 70%"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: PLANETARY CONDENSATION — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — VALVE BLANKETING & ZERO FRICTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                [LUBRICANT]     [LEADS]                 [VALVES][MAJIN] ",
        "---",
        "- Node 03: Golden Fluid (Blanketing the 12 Hydraulic Piston Sleeves)",
        "- Node 05: The Eight Attendants (Unified Directional Guard Absorption)",
        "- Node 08: Twelve Release Valves (Friction Coefficient Dropped to 0.00)",
        "---",
        "- The 8 Leads : Spd 8 -> 4 AP | HP 200/200 | SP +40 | Posture 100/100",
        "- Dawn Cloud  : Spd 2 -> 1 AP | Pale 14/160 | Liquefaction: 90%"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: PLANETARY CONDENSATION — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER & PNEUMATIC LOCK]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                                [LEADS]                 [VALVES][MAJIN] ",
        "---",
        "- Node 05: Dawn Cloud (TERMINAL STAGGER / PALE 0/160 / FULL CONDENSATION)",
        "- Node 05: Zyrak & Dekan (Aligning High-Pressure Hydraulic Lines)",
        "- Node 08: Twelve Valves (Completely Primed for Day 160 Dawn Release)",
        "---",
        "- Dawn Cloud  : Spd 0 -> 0 AP | Pale 0/160 | Condensation: 100%"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: PLANETARY CONDENSATION — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — FINAL CONDENSATION & PRIMING COMPLETE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "                                [THE EIGHT ATTENDANTS]  [READY] [MAJIN] ",
        "---",
        "- Node 06: The Eight Attendants (All Systems Locked and In Golden Phase)",
        "- Node 08: Twelve Release Valves (Zero Resistance / Primed for Cycle 1,778)",
        "---",
        "- Condensation: COMPLETE | +0.028 TONS REFINED HAN HARVESTED"
    ])

    return f"""
```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Eightfold Aura & Condensation Stagger)
- **Synchronized Department Aura**:
  * The Eight Attendants unify their core frequencies across the Floor 1 vault.
  * The kinetic pressure and temporal stabilization condense the turbulent Pale vapor:
    * The Dawn Cloud absorbs **48 Condensation Points**!
    * Atmospheric Pale drops to **62/160**, crossing the **60% Stagger Threshold (96 Points)**!
    * **STAGGER LEVEL 1 TRIGGERED!** The vapor stops churning and begins to liquefy into golden droplets.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Golden Liquefaction & Momentum Surge)
- **Deep Phase Shift (1.5x Condensation Multiplier)**:
  * The Attendants' `Momentum Surge` activates! (+2 Speed next turn).
  * The golden droplets coalesce into a luminous, low-viscosity fluid that coats the chamber walls with soothing warmth.
  * Atmospheric Pale drops to **32/160**!

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Valve Piston Lubrication & Zero Friction)
- **Hydraulic Coating**:
  * The golden fluid flows directly into the twelve massive release valve assemblies at Node 08.
  * Zyrak and Dekan deploy `[Directional Guard Absorption]`, guiding the fluid into every piston seal.
  * Internal friction drops to absolute zero! Pale drops to **14/160**!

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Terminal Stagger & Pneumatic Lock)
- **Pneumatic Priming Finale**:
  * Zyrak and Dekan lock the high-pressure pneumatic channels, stripping the final 14 Pale points!
  * **TERMINAL STAGGER TRIGGERED!** Pale drops to **0/160**. The entire cloud has converted into super-refined golden fluid.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Prime Complete & Final Day 160 Readiment)
- **Valves Primed for the Dawn of Cycle 1,778**:
  * All twelve release valves hum in quiet, golden readiness, prepared to exhale the Apotheosis of Dawn upon the planet.
  * Ballast telemetry records **+0.028 tons of refined Han**!
"""

def update_part_8():
    path = "SOMNARAK-WORLD/The_Absolvohan/Part_8_Days_149_to_177.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Day 149
    old_d149 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Seiyon tunes acoustic conduit; Park channels gentle      |
| Flerehan wave.                                                      |
| - Turn 03: Fireflies hit 60% Stagger 1; sorrow frequency converts   |
| to Hope.                                                            |
| - Turn 04: Fireflies encircle open manifold; Seiyon opens intake    |
| valve.                                                              |
| - Turn 05: Park executes Viderehan harmonic lock, aligning energy   |
| phases.                                                             |
| - Turn 06: Harmonic communion complete; entities merge smoothly     |
| into pipes.                                                         |
+=====================================================================+
```"""
    if old_d149 in content:
        content = content.replace(old_d149, get_day_149_combat())
        print("Replaced Day 149 summary successfully!")

    # Day 151
    old_d151 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Shin sings the first verse; Dekan shields acoustic       |
| bounce; 60% Stagger 1.                                              |
| - Turn 03: Posture broken; spirits lower arms in peaceful reverie;  |
| Sorrow at 10%.                                                      |
| - Turn 04: Spirits hum the Maw's lullaby; Shin matches pitch with   |
| Choral Staff.                                                       |
| - Turn 05: Dekan projects soothing barrier, nullifying trance       |
| pressure.                                                           |
| - Turn 06: Shin sings final verse; spirits bow and dissolve into    |
| clear water.                                                        |
+=====================================================================+
```"""
    if old_d151 in content:
        content = content.replace(old_d151, get_day_151_combat())
        print("Replaced Day 151 summary successfully!")

    # Day 153
    old_d153 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Han matches vocal octave; Song plays lyre; Shadow hits   |
| 60% Stagger 1.                                                      |
| - Turn 03: Posture broken; Three Birds chime in unison; Pale light  |
| softens.                                                            |
| - Turn 04: Silhouette spreads wings; Dekan channels Maw's grounding |
| field.                                                              |
| - Turn 05: Han & Song execute Flerehan duet, dissolving lingering   |
| Before-Time grief.                                                  |
| - Turn 06: Celestial light merges into conduits; accumulators       |
| charge to max.                                                      |
+=====================================================================+
```"""
    if old_d153 in content:
        content = content.replace(old_d153, get_day_153_combat())
        print("Replaced Day 153 summary successfully!")

    # Day 155
    old_d155 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: Ayshuk raises arms; predictive HUD aligns angles; 60%    |
| Stagger 1.                                                          |
| - Turn 03: Posture broken; halos descend gently toward apostle      |
| ranks.                                                              |
| - Turn 04: Corona pulses warm Pale cleansing light; Ayshuk          |
| stabilizes field.                                                   |
| - Turn 05: Viderehan communion complete; twelve halos crown the     |
| apostles.                                                           |
| - Turn 06: Anomaly dissolves into radiant peace; research hub fully |
| sanctified.                                                         |
+=====================================================================+
```"""
    if old_d155 in content:
        content = content.replace(old_d155, get_day_155_combat())
        print("Replaced Day 155 summary successfully!")

    # Day 157
    old_d157 = """```text
+=====================================================================+
|         TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)          |
+---------------------------------------------------------------------+
| - Turn 02: All 8 Leads unify auras; cloud condenses; 60% Stagger 1. |
| - Turn 03: Posture broken; Pale vapor liquefies into radiant golden |
| fluid.                                                              |
| - Turn 04: Cloud blankets the twelve release valves without         |
| friction.                                                           |
| - Turn 05: Zyrak & Dekan channel pneumatic conduits; pistons        |
| lubricated.                                                         |
| - Turn 06: Final condensation complete; valves primed for Day 160   |
| release.                                                            |
+=====================================================================+
```"""
    if old_d157 in content:
        content = content.replace(old_d157, get_day_157_combat())
        print("Replaced Day 157 summary successfully!")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated Part 8 successfully!")

if __name__ == "__main__":
    update_part_8()
