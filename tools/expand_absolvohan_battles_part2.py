#!/usr/bin/env python3
"""
tools/expand_absolvohan_battles_part2.py
Expands the remaining 4 combat encounters in SOMNARAK-WORLD/The_Absolvohan/Part_2_Days_1_to_25.md:
1. First Watch (Dawn) Ordeal — The Whispering Spores
2. Second Watch (Noon) Ordeal — The Wandering Tempest
3. Third Watch (Dusk) Ordeal — The Rusting Archive
4. Fourth Watch (Midnight) Ordeal — The Echo of Cheonbulok
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

filepath = "SOMNARAK-WORLD/The_Absolvohan/Part_2_Days_1_to_25.md"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# -------------------------------------------------------------
# 1. First Watch (Dawn) Ordeal — The Whispering Spores
# -------------------------------------------------------------
box_spores_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (SPORES DAWN)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [SPORE-A][SPORE-B][KIM]   [PARK]  [LEE]                  [MAJIN]",
    "DIST    : Spores at N01-N02; Kim at N03 (Band 1); Park at N04; Lee at N05.",
    "---",
    "Agent Kim     : Speed 5 -> 3 AP | HP: 105/105 | SP: +20 | Embrace Fang",
    "Agent Park    : Speed 6 -> 3 AP | HP: 110/110 | SP: +25 | Lament Requiem",
    "Agent Lee     : Speed 4 -> 2 AP | HP:  95/ 95 | SP: +15 | Stun Baton",
    "Spore Carrier : Speed 4 -> 2 AP | HP: 120/120 | Sorrow: 45% | Toxin Slash"
])

box_spores_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Kim locks N02; Park unleashes Lament pulse; Spore-A 60% Stagger.",
    "- Turn 03: Posture broken; all allied strikes deal 2.0x damage; Spore-A dead.",
    "- Turn 04: Spore-B & C vent toxic cloud; Lee activates air scrubber at N05.",
    "- Turn 05: Park executes Flerehan acoustic resonance; Spores lose momentum.",
    "- Turn 06: Kim executes Climax Fang; Terminal Stagger shatters carriers."
])

box_spores_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : East corridor ventilation purged of fungal spore.",
    "2. Status Equilibrium : Clerk sanity stabilized; team SP rises to +30.",
    "3. Containment Check   : All 3 Spore Carriers dissolved into inert powder.",
    "4. OUTCOME             : ZERO CASUALTIES — 38.4s RECORD CLEAR TIME."
])

old_spores = """Three fungal spore-carriers drop from the ceiling grates of Corridor East. A patrolling clerk panics and flees directly toward the beasts!

Director Majin issues tactical commands:
1. **Directive Deployed:** `Veil Mist Dampener` activated in Corridor East, reducing spore toxin dispersal.
2. **Combat Interception:** Agent Park leads the clash from Range Band 3, firing concentrated sonic waves with the *Lament Requiem*. The Lament vulnerability triggers—each acoustic pulse deals double damage to the fungal carapaces!
3. **Flank Suppression:** Agent Kim charges in with the *Embrace Fang*, drawing the beasts' physical claws against his armored chest while Agent Lee knocks the panicking clerk unconscious with a stun baton.
4. **Resolution:** All three carriers burst into inert gray powder in 38.4 seconds! Zero casualties!

Secretary Seiyon prompts: `Quota Realized. Locking sector bulkheads. Concluding Day 1 shift.`"""

new_spores = f"""Three fungal spore-carriers drop from the ceiling grates of Corridor East. A patrolling clerk panics and flees blindly toward Node 2!

Director Majin establishes GBS tactical engagement parameters:

```text
{box_spores_hud}
```

###### Turn 01 Action Resolution Log (Corridor East)
- **Step 1: Floor 1 Echo-Core Resonance (Majin & Seiyon)**:
  * Majin engages `Veil Mist Dampener`, reducing toxic spore dispersal across Nodes 1 to 4 by 40%.
  * Seiyon routes tactical coordinates: *Administrative Clarity* active for clash winners.
- **Step 2: Movement & Action Point Spending**:
  * Agent Lee (Speed 4 -> 2 AP) spends 1 AP to sprint from Node 5 to Node 3, catching the panicking clerk before they cross into the beasts' claws. Spends 1 AP to deliver a gentle non-lethal stun, escorting the clerk back to Node 7!
  * Agent Kim (Speed 5 -> 3 AP) spends 1 AP to advance from Node 3 to Node 2 (Point-Blank Range Band 1). Spends 2 AP to declare `[Embrace Fang Vicious Guard]`.
  * Agent Park (Speed 6 -> 3 AP) positions at Node 4 (Range Band 2). Spends 2 AP to channel `[Lament Requiem Harmonic Blast]`. Remaining 1 AP held in Guard.
- **Step 3: Clash Resolution (Node 2)**:
  * Spore Carrier A lunges with `[Toxic Scythe Slash]` on Node 2 (Base 7 + 2 Coins = 11 Power).
  * Agent Kim's `[Embrace Fang Vicious Guard]` (Base 8 + 2 Coins = 12 Power).
  * **Resolution**: Kim WINS THE CLASH (12 vs 11).
    * Kim parries the fungal blade, locking the beast in place and dealing 24 Grudge damage.
  * Agent Park unloads `[Lament Requiem Harmonic Blast]` from Node 4 unopposed:
    * The acoustic wave exploits the Spore's Lament weakness, dealing **46 direct Lament damage** and inflicting +26 Stagger!

```text
{box_spores_turns}
```

```text
{box_spores_phase}
```

Secretary Seiyon prompts: `Quota Realized. Locking sector bulkheads. Concluding Day 1 shift.`"""

if old_spores in text:
    text = text.replace(old_spores, new_spores)
    print("Replaced Spores section successfully!")
else:
    print("Could not find Spores section!")

# -------------------------------------------------------------
# 2. Second Watch (Noon) Ordeal — The Wandering Tempest
# -------------------------------------------------------------
box_tempest_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (TEMPEST NOON)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [STALKER-A][STALKER-B][MELLDA][MOON]                  [MAJIN]",
    "DIST    : Mellda at N03 (Band 1); Moon at N04 (Band 2); Majin at N10.",
    "---",
    "Border Lead Mellda: Speed 6 -> 3 AP | HP: 185/185 | SP: +30 | Threshold Vow",
    "Agent Moon        : Speed 5 -> 3 AP | HP: 120/120 | SP: +25 | Lead Maul",
    "Tempest Stalker (x2): Speed 5 -> 3 AP | HP: 190 each | Void Vapor"
])

box_tempest_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Mellda anchors Gate 03; Moon smashes Stalker-A; 60% Stagger 1.",
    "- Turn 03: Posture broken; direct Weight damage deals 2.0x; Stalker-A dead.",
    "- Turn 04: Stalker-B swirls into Void cyclone; Mellda pins with spear aura.",
    "- Turn 05: Moon executes Pugnahan heavy slam; forces Terminal Stagger.",
    "- Turn 06: Mellda executes Climax Impale; Stalker shatters into gray salt."
])

box_tempest_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Gate 03 atmospheric seals fully re-engaged.",
    "2. Status Equilibrium : Corrosive fog dissipates; team SP stabilizes at +35.",
    "3. Containment Check   : Both Tempest Stalkers completely eradicated.",
    "4. OUTCOME             : ZERO CASUALTIES — 44.8s ENGAGEMENT RESOLUTION."
])

old_tempest = """Two vaporous stalkers riding the storm force their way through the secondary seals of Gate 03, hissing corrosive Void mist down Corridor South!

Manager tactical execution:
1. **Directive Deployed:** `Quarantine Severance` triggered on Gate 03 airlocks, preventing outside storm air from entering the primary ventilation grid.
2. **Lead Activation:** Mellda manifests her Hope Transformation weapon—**Threshold Vow**! She drives her massive golden energy spear into the corridor floor, generating an omnidirectional gravitational anchor that pins both stalkers at Range Band 2!
3. **Clash Execution:** Agent Moon charges in with the *Lead Maul* (Weight/Purple damage). Striking their pinned ethereal nuclei, Moon shatters both stalkers into harmless gray salt within 44.8 seconds! Zero casualties!

Agent Noh conducts one final pruning run on Chamber 145, pushing daily harvest to **0.068 / 0.050 tons!**"""

new_tempest = f"""Two vaporous stalkers riding the storm force their way through the secondary seals of Gate 03, hissing corrosive Void mist down Corridor South!

Director Majin establishes GBS tactical command at the Gate 03 perimeter:

```text
{box_tempest_hud}
```

###### Turn 01 Action Resolution Log (Gate 03 Perimeter)
- **Step 1: Floor 5 Echo-Core Resonance (Border Lead Mellda)**:
  * Mellda projects *The Bulwark Perimeter*, locking down Node 3 with reinforced gravitational anchors that nullify the stalkers' mist phase-shift.
  * Director Majin engages `Quarantine Severance`, isolating Corridor South ventilation.
- **Step 2: Movement & Action Point Spending**:
  * Border Lead Mellda (Speed 6 -> 3 AP) holds Node 3 (Point-Blank Range Band 1). Spends 2 AP to brandish *Threshold Vow* in an anchoring thrust. Remaining 1 AP in Guard.
  * Agent Moon (Speed 5 -> 3 AP) stands at Node 4 (Range Band 2). Spends 2 AP to prepare `[Lead Maul Heavy Gravitational Downswing]`. Remaining 1 AP held in Guard.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * Tempest Stalker A launches `[Corrosive Void Tendril]` against Mellda (Base 8 + 2 Coins = 12 Power).
  * Mellda's `[Threshold Vow Golden Pin]` (Base 10 + 2 Coins = 14 Power).
  * **Resolution**: Mellda WINS THE CLASH (14 vs 12).
    * Mellda's golden spear skewers the vapor core, grounding its electrical mist into the stone floor and inflicting 34 Weight damage with +20 Stagger!
  * Agent Moon swings the *Lead Maul* into Stalker A's pinned nucleus unopposed:
    * The massive blunt weight strikes true, dealing **48 Weight damage** and shaking its ethereal density!

```text
{box_tempest_turns}
```

```text
{box_tempest_phase}
```

Agent Noh conducts one final pruning run on Chamber 145, pushing daily harvest to **0.068 / 0.050 tons!**"""

if old_tempest in text:
    text = text.replace(old_tempest, new_tempest)
    print("Replaced Tempest section successfully!")
else:
    print("Could not find Tempest section!")

# -------------------------------------------------------------
# 3. Third Watch (Dusk) Ordeal — The Rusting Archive
# -------------------------------------------------------------
box_archive_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (RUSTING DUSK)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [CENOTAPH-A][CENOTAPH-B][KWON]   [SIM]   [SEO]                  [ZYRAK]",
    "DIST    : Kwon at N03 (Band 1); Sim at N04 (Band 2); Seo at N05 (Band 3).",
    "---",
    "Agent Sim   : Speed 6 -> 3 AP | HP: 115/115 | SP: +25 | Lead Maul",
    "Agent Kwon  : Speed 5 -> 3 AP | HP: 110/110 | SP: +20 | Kinetic Stun Baton",
    "Agent Seo   : Speed 5 -> 3 AP | HP: 100/100 | SP: +20 | Sonic Rifle",
    "Stone Cenotaph (x2): Speed 4 -> 2 AP | HP: 220 each | Lament Screech"
])

box_archive_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Sim pulverizes Cenotaph-A base; exploits Grudge; 60% Stagger 1.",
    "- Turn 03: Posture shattered; 2.0x direct damage breaks Cenotaph-A into dust.",
    "- Turn 04: Cenotaph-B unleashes 90dB wail; Zyrak engages Extraction Siphon.",
    "- Turn 05: Seo fires high-frequency sonic burst, cracking the stone crown.",
    "- Turn 06: Sim executes Climax Maul Strike; Cenotaph-B collapses to gravel."
])

box_archive_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Data corridor acoustic frequencies return to baseline.",
    "2. Status Equilibrium : Clerks recovered; agent SP stabilized at +32.",
    "3. Containment Check   : Both Rusting Cenotaphs reduced to inert gravel.",
    "4. OUTCOME             : ZERO AGENT CASUALTIES — 58.2s CLEAR TIME."
])

old_archive = """Two monolithic stone cenotaphs erupt from the data floor, screeching corrupted legal statutes from the Before-Time. Two junior research clerks drop their tablets and enter **Panic State: Lament Despair**, falling to their knees and crying uncontrollably!

Managerial tactical execution:
1. **Directive Deployed:** `Acoustic Siphon` engaged in Floor 3, damping the cognitive screech by 35%.
2. **Panic Restoration:** Agent Kwon sprints over, striking both weeping clerks with his stun baton. The precise Lament shockwaves reboot their nervous systems, restoring their sanity bars to full!
3. **Clash Standoff:** Agent Sim charges the lead cenotaph with the *Lead Maul* (blunt physical damage). Exploiting its Grudge weakness, Sim pulverizes the first tablet in three massive downward swings.
4. **Clean-up:** Kwon and Seo focus-fire the second tablet with sonic beams, shattering it into inert gravel within 58.2 seconds! Zero fatalities!

One final quick observation session yields +0.017 tons. Daily harvest: **0.065 / 0.050 tons!**"""

new_archive = f"""Two monolithic stone cenotaphs erupt from the data floor, screeching corrupted legal statutes from the Before-Time. Two junior research clerks drop their tablets and enter **Panic State: Lament Despair**, falling to their knees and crying uncontrollably at Node 5!

Director Majin establishes GBS tactical battle commands:

```text
{box_archive_hud}
```

###### Turn 01 Action Resolution Log (Floor 3 Data Corridor)
- **Step 1: Floor 3 Echo-Core Resonance (Extraction Lead Zyrak)**:
  * Zyrak activates *The Acoustic Siphon*, damping the cenotaphs' 85dB cognitive screech by 35% and converting excess sound energy into containment reserve.
  * Majin deploys `Veil Mist Dampener` across Nodes 4 through 6.
- **Step 2: Movement & Action Point Spending**:
  * Agent Kwon (Speed 5 -> 3 AP) spends 1 AP to shift to Node 5 over the despairing clerks. Spends 1 AP to administer calibrated Lament stun strikes, dispelling their sorrow trance and restoring their SP from 0 to +25! Remaining 1 AP held in Guard.
  * Agent Sim (Speed 6 -> 3 AP) advances from Node 4 to Node 3 (Point-Blank Range Band 1 with Cenotaph A). Spends 2 AP to wind up `[Lead Maul Crushing Swing]`.
  * Agent Seo (Speed 5 -> 3 AP) holds Node 5 behind the work consoles, spending 2 AP to prepare a concentrated sonic pulse from Range Band 3.
- **Step 3: Clash Resolution (Node 2 to 3)**:
  * Cenotaph A declares `[Statute of Condemnation]` on Node 3 (Base 8 + 2 Coins = 12 Power).
  * Agent Sim's `[Lead Maul Crushing Swing]` (Base 10 + 2 Coins = 14 Power).
  * **Resolution**: Sim WINS THE CLASH (14 vs 12).
    * Sim's heavy maul shatters the legal tablet's front inscription, exploiting its Grudge vulnerability to deal **42 Grudge blunt damage** and inflicting +24 Stagger!
  * Agent Seo fires a sonic beam from Node 5, chipping away at Cenotaph B's stone frame.

```text
{box_archive_turns}
```

```text
{box_archive_phase}
```

One final quick observation session yields +0.017 tons. Daily harvest: **0.065 / 0.050 tons!**"""

if old_archive in text:
    text = text.replace(old_archive, new_archive)
    print("Replaced Archive section successfully!")
else:
    print("Could not find Archive section!")

# -------------------------------------------------------------
# 4. Fourth Watch (Midnight) Ordeal — The Echo of Cheonbulok
# -------------------------------------------------------------
box_leviathan_hud = make_box("COMBAT HUD: PHASE 01 — BATTLE TURN 01 (PALE MIDNIGHT)", [
    "[STAGE] : [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
    "POS     : [LEVIATHAN]   [TAK]   [ZYRAK]         [HONG]  [JO]   [MARJUK]",
    "DIST    : Tak at N02 (Band 1); Zyrak at N03; Hong & Jo at N05-N06 (Band 3).",
    "---",
    "Agent Tak         : Speed 6 -> 3 AP | HP: 135/135 | SP: +30 | Fury Blade",
    "Extraction Lead Zyrak: Speed 5 -> 3 AP | HP: 160/160 | SP: +35 | Extraction Lance",
    "Agent Hong        : Speed 5 -> 3 AP | HP: 110/110 | SP: +25 | Lament Requiem",
    "Agent Jo          : Speed 5 -> 3 AP | HP: 105/105 | SP: +20 | Guardian Lens",
    "Echo of Cheonbulok: Speed 4 -> 3 AP | HP: 480/480 | Sorrow: 70% | Pale Pulse"
])

box_leviathan_turns = make_box("TURNS 02 THROUGH 06 PROGRESSION (PHASE 01 SUMMARY)", [
    "- Turn 02: Tak & Zyrak pierce scales; Hong beams Lament; 60% Stagger 1.",
    "- Turn 03: Posture broken; balanced 4-affinity attacks deal 2.0x direct damage.",
    "- Turn 04: Leviathan charges [Midnight Tidal Wave]; Marjuk activates Stasis.",
    "- Turn 05: Jo focuses prismatic beam; burns off leviathan thermal crest.",
    "- Turn 06: Tak executes Overdrive Climax Cleave; Terminal Stagger shatters beast."
])

box_leviathan_phase = make_box("PHASE 01 RESOLUTION (PHASE-END TICK)", [
    "1. Environmental Check : Deep thermal vents of Floor 6 purged and stabilized.",
    "2. Status Equilibrium : Pale decay aura halted; team HP restored by regenerator.",
    "3. Containment Check   : Spectral Leviathan disintegrated into glowing embers.",
    "4. OUTCOME             : ZERO FATALITIES — 74.3s CRITICAL MIDNIGHT CLEAR."
])

old_leviathan = """A spectral ash leviathan slithers up from the deepest heat vents of Floor 6! It radiates an omnidirectional Pale aura that drains 15% of max HP from every agent in the same corridor every 8 seconds!

Managerial combat command:
1. **Directive Deployed:** `Four-Sign Aegis` thrown around Floor 6's central corridor, trapping the leviathan inside the combat arena and shielding innocent clerks.
2. **Directive Deployed:** `Han Salve Jet` sprayed over Agent Tak's kinetic gauntlets to neutralize thermal decay.
3. **Range Band Positioning:**
   - Agent Hong and Agent Jo take Range Band 4, unleashing continuous sonic Lament beams from *Lament Requiem* and *Guardian Lens*.
   - Agent Tak and Zyrak charge into Range Band 1, executing high-heat smelting thrusts with the *Fury Blade* and extraction lance!
4. **Clash Resolution:** Under balanced fire from all four damage types, the spectral ash leviathan shudders, fractures, and disintegrates into glowing cyan embers in 74.3 seconds!
5. **Casualties:** ZERO Fatalities! Three agents sustained moderate HP decay, immediately healed by Floor 6's regenerator!

We slam the **[Shift Complete]** toggle!"""

new_leviathan = f"""A spectral ash leviathan slithers up from the deepest heat vents of Floor 6! It radiates an omnidirectional Pale aura that drains 15% of max HP from every agent in the same corridor every 8 seconds!

Director Majin establishes multi-floor GBS combat coordination:

```text
{box_leviathan_hud}
```

###### Turn 01 Action Resolution Log (Floor 6 Central Vent Core)
- **Step 1: Floor 6 Echo-Core Resonance (Archive Lead Marjuk)**:
  * Marjuk deploys *The Temporal Stasis Array*, locking Node 1 in chronological amber to slow the leviathan's advance.
  * Director Majin engages `Four-Sign Aegis` around Floor 6, shielding auxiliary personnel.
- **Step 2: Movement & Action Point Spending**:
  * Agent Tak (Speed 6 -> 3 AP) charges to Node 2 (Point-Blank Range Band 1). Spends 2 AP to declare `[Fury Blade High-Heat Thrust]`. Remaining 1 AP held in Guard.
  * Extraction Lead Zyrak (Speed 5 -> 3 AP) stands at Node 3 (Close Range Band 2). Spends 2 AP to ready `[Extraction Lance Energy Siphon]`.
  * Agent Hong (Speed 5 -> 3 AP) and Agent Jo (Speed 5 -> 3 AP) deploy at Nodes 5 and 6 (Range Band 3), spending 2 AP each to lock optical and sonic targeting on the leviathan's dorsal crest.
- **Step 3: Clash Resolution (Node 1 to 2)**:
  * The Echo of Cheonbulok unleashes `[Subterranean Ash Tidal Wave]` (Base 10 + 2 Coins = 14 Power).
  * Agent Tak's `[Fury Blade High-Heat Thrust]` (Base 11 + 2 Coins = 15 Power).
  * **Resolution**: Tak WINS THE CLASH (15 vs 14).
    * Tak's molten blade drives through the leviathan's ash mantle, canceling the tidal wave and dealing **45 Grudge/Pale damage** with +28 Stagger!
  * Zyrak thrusts the Extraction Lance into the fracture point, siphoning 30 Han-Energy and dealing 32 kinetic damage.
  * Hong and Jo unleash combined Lament and Void beams from Nodes 5 and 6, overwhelming the entity's multi-spectral defenses!

```text
{box_leviathan_turns}
```

```text
{box_leviathan_phase}
```

We slam the **[Shift Complete]** toggle!"""

if old_leviathan in text:
    text = text.replace(old_leviathan, new_leviathan)
    print("Replaced Leviathan section successfully!")
else:
    print("Could not find Leviathan section!")

check_banned(text, filepath)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
print(f"Updated {filepath} with all expanded GBS battles!")
