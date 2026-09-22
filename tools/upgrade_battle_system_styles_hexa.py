#!/usr/bin/env python3
"""
tools/upgrade_battle_system_styles_hexa.py
Upgrades SOMNARAK_BATTLE_SYSTEM_STYLES.md from Quad-Style to Hexa-Style:
- Branch 1: Generic P.S. Combat Core
- Branch 2: Reverie Directorate (R.D.) Style
- Branch 3: Underworld Cleanup Descend (UCD) Style
- Branch 4: Somnarak Exploration Decree (SED) Style
- Branch 5: The Memory Archive (Gieok Jeojangso) Style
- Branch 6: The Horizon Caravan (Jipyeongseondae) Style
"""

import unicodedata

def get_display_width(text):
    w = 0
    for ch in text:
        if unicodedata.east_asian_width(ch) in ('F', 'W'):
            w += 2
        else:
            w += 1
    return w

def pad_to_display_width(text, target_width):
    cur_w = get_display_width(text)
    if cur_w < target_width:
        return text + " " * (target_width - cur_w)
    elif cur_w > target_width:
        res = ""
        res_w = 0
        for ch in text:
            ch_w = 2 if unicodedata.east_asian_width(ch) in ('F', 'W') else 1
            if res_w + ch_w > target_width:
                break
            res += ch
            res_w += ch_w
        return res + " " * (target_width - res_w)
    return text

def make_box(title, rows, width=71):
    top = "+" + "=" * (width - 2) + "+"
    bottom = "+" + "=" * (width - 2) + "+"
    sep = "+" + "-" * (width - 2) + "+"
    inner_width = width - 4
    
    out = [top]
    if title:
        title_str = f" {title} "
        title_w = get_display_width(title_str)
        left_pad = (width - 2 - title_w) // 2
        right_pad = width - 2 - title_w - left_pad
        out.append("|" + " " * left_pad + title_str + " " * right_pad + "|")
        out.append(sep)
    
    for r in rows:
        if r == "---":
            out.append(sep)
        elif r.startswith("==="):
            out.append(top)
        else:
            padded = pad_to_display_width(r, inner_width)
            out.append(f"| {padded} |")
    out.append(bottom)
    return "\n".join(out)

def build_section_9_and_10():
    archive_box = make_box("MEMORY ARCHIVE (GIEOK JEOJANGSO) RECEPTION GRID", [
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "|--THRESHOLD--| |--MINIONS----| |--APEX CONSTRUCT-| |--DAIS---|",
        "---",
        "N01     : Ingress Sluice / Archive Threshold Vestibule",
        "N02     : Seiyon Vanguard (Prismatic Stilettos & Aegis)",
        "N03     : Mnemonic Projection Drone (Sapper Systems)",
        "N04     : Memory Phantoms / Traumatic Minion Echoes",
        "N05     : Sovereign Construct Apex (Targetable Anchors)",
        "N06     : Resonant Mnemonic Lens (Weakpoint Diagnostics)",
        "N07     : Weaver Projection Array (Silver Thread Buffers)",
        "N08-N09 : Suppressed Trauma Sump / Subterranean Chasm",
        "N10     : Floor Core Reliquary / Key Page Transmutation Dais"
    ])

    caravan_box = make_box("HORIZON CARAVAN (JIPYEONGSEONDAE) EXPEDITION GRID", [
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "|--RAMPS------| |--OUTRIDERS--| |--DUNE BASIN-----| |--BRIDGE-|",
        "---",
        "N01     : Drift Throne Debarkation Ramps (Kael Vanguard)",
        "N02     : Outrider Sand-Skimmer Lane (Hwaran Support)",
        "N03     : Fortified Sand Berms (Heavy Dredger Phalanx)",
        "N04     : Sinking Sand Basin / Primary Skirmish Zone",
        "N05     : Sovereign Adversary Apex (Behemoths / War-Rigs)",
        "N06     : Elevated Catwalk Pylon / Sniper Overwatch Mast",
        "N07     : Rear Sand Dune Ridge (Acoustic Heavy Mortars)",
        "N08     : Deep Sand Chasm / Sinking Sand Hazard Sump",
        "N09     : Subterranean Geothermal Han-Flow Ley-Vent",
        "N10     : Drift Throne Bridge & Spinal Siege Railgun"
    ])

    return f"""## IX. Branch 5: The Memory Archive (Gieok Jeojangso) Style

**Operational Focus**: Deep Strata Sub-Alpha Roots (-2,350m to -3,250m), 7-Floor Mnemonic Reception Chambers.  
**Tactical Philosophy**: The Library Reception Protocol, subjugation through comprehension, modular memory anchor dismantling, and the transmutation of suffering into Key Pages.

```text
{archive_box}
```

### 9.1 Spatial 10-Node Mnemonic Reception Topology

In Memory Archive receptions, combat takes place within cyclopean subterranean vaults carved into the roots of the Alpha Tree:
- **Node 01 (Threshold Sluice)**: Ingress archway where Seiyon's synthetic holographic projection enters the floor.
- **Node 02 (Seiyon Vanguard)**: Point-Blank Band 1. Seiyon engages with dual Prismatic Stilettos and deploys the Prismatic Aegis for kinetic and hydro-deflections.
- **Node 03 (Mnemonic Projection Drone)**: Support Band 2. Autonomous drone deploying thermal, pneumatic, and resonant sappers to strip enemy armor.
- **Node 04 (Echo Minions)**: Intermediary lane where memory phantoms, phantom soldiers, and mirror doppelgangers spawn.
- **Node 05 (Sovereign Boss Anchor)**: The central dais occupied by the floor's guardian construct (e.g., The First Keeper, The Weeping Statue, The Original).
- **Node 06 (Resonant Mnemonic Lens)**: Band 3. Telemetric scanner highlighting weakpoint seams and broadcasting harmonic solace.
- **Node 07 (Weaver Projection Array)**: Band 4. Deploys silver threads of light that absorb ambient psychological trauma and stabilize squad composure.
- **Nodes 08–09 (Suppressed Trauma Sump & Chasm)**: Deep subterranean rifts that vent unexpressed tears or void feedback.
- **Node 10 (Key Page Dais)**: The master reliquary where crystallized memories condense into equipable Key Pages upon Floor Realization.

### 9.2 Modular Memory Anchor Dismantling
Adversaries in the Memory Archive possess discrete targetable memory anchors:
- Each anchor represents a physical manifestation of repressed trauma (e.g., Weeping Siphon Veil, Gilded Frame of Lies, Zero-Chrono Lance).
- Reducing an anchor to 0 HP permanently disables signature boss attacks, deducts 1 enemy Action Point, and triggers **Stagger 1**.

### 9.3 Floor Realization & Key Page Transmutation
When the sovereign construct's Posture meter is reduced to 0 (Stagger 2):
- Hostile intent drops to zero as Seiyon shares the emotional weight of the construct's forgotten trauma.
- The construct dissolves into crystalline light, condensing into a permanent **Key Page** that unlocks passive combat arts and elemental affinities for subsequent floors.

---

## X. Branch 6: The Horizon Caravan (Jipyeongseondae) Style

**Operational Focus**: The Desolate Overland Corridors, Sea of Glass, Cheonbulok Volcanic Caldera, Mugeukji Polar Tundra.  
**Tactical Philosophy**: Open-field vehicular combat, high-speed sand maneuvers, planetary ley-frequency tuning, and heavy kinetic artillery.

```text
{caravan_box}
```

### 10.1 Spatial 10-Node Overland Expedition Topology

In Horizon Caravan operations, battle unfolds across vast desert plains anchored by the mobile sand fortress **The Drift Throne**:
- **Node 01 (Crawler Ramps)**: Debarkation gangway of the Drift Throne. Grants $+2$ Protection to allied defenders.
- **Node 02 (Outrider Skimmer Lane)**: Rapid flanking lane for sand-skimmers and agile skirmishers (Hwaran). Grants $+15\\%$ Evasion.
- **Node 03 (Sand Barricades)**: Fortified dune berms equipped with deployable ballistic mantlets anchored by Heavy Dredgers.
- **Node 04 (Sinking Sand Basin)**: Forward clash zone where medium melee and close-range firearms collide.
- **Node 05 (Sovereign Adversary Apex)**: The central node occupied by colossal burrowers, marauder war-rigs, or enemy champions.
- **Node 06 (Elevated Catwalk Pylon)**: Telescopic sniper mast providing $+1$ Range Band to marksmen.
- **Node 07 (Rear Sand Dune Ridge)**: High ground utilized by acoustic mortar crews.
- **Node 08 (Sand Chasm Sump)**: Shifting quicksand hazard that penalizes movement by $-2$ Speed.
- **Node 09 (Geothermal Ley-Vent)**: Planetary fracture venting boiling Han-brine or volatile steam every 3 turns.
- **Node 10 (Command Bridge & Siege Railgun)**: The central helm of the Drift Throne housing Kael's command seat and the spinal kinetic railgun.

### 10.2 Planetary Ley-Drive & Seismic Acoustics
- The Drift Throne siphons acoustic vibrations from deep subterranean Han-flow lines.
- Kael uses his vitrified Han-glass arm to channel seismic shockwaves, stabilizing shifting sands, flipping enemy war-rigs, and grounding volcanic firestorms.

### 10.3 Vehicular Part Severance & Planetary Relic Overdrives
- Targetable vehicular components (crawler treads, rotary autocannons, sand mandibles) can be dismantled through targeted kinetic fire.
- High-intensity climax turns (Turn 05) feature supreme **Relic Overdrives** (3 AP, 30 SP) such as *Song of the Buried Earth* and *Oath of the Unchained Horizon* that parry cataclysmic environmental attacks and lead to peaceful resolution.
"""

def main():
    path = "SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM_STYLES.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update title and overview box
    old_title = "## The Four Canonical Tactical Branches of Combat & Tactical Physics"
    new_title = "## The Six Canonical Tactical Branches of Combat & Tactical Physics"
    content = content.replace(old_title, new_title)

    old_quad = "PROJECT SOMNARAK: QUAD-STYLE BATTLE SYSTEM ARCHITECTURE"
    new_hexa = "PROJECT SOMNARAK: HEXA-STYLE BATTLE SYSTEM ARCHITECTURE"
    content = content.replace(old_quad, new_hexa)

    # Replace the box in Section I
    old_box_start = "+=====================================================================+\n|       PROJECT SOMNARAK: QUAD-STYLE BATTLE SYSTEM ARCHITECTURE"
    # Find the end of this box
    box_end = content.find("+=====================================================================+\n\nEvery battle encounter")
    
    hexa_rows = [
        "1. GENERIC P.S. CORE FOUNDATION (Universal Combat Engine)",
        "   - 10-Node Room Stage Grid (Node 1 to Node 10 spatial positions).",
        "   - Speed-to-AP Action Economy (Initiative, Movement, Clashes).",
        "   - Macro Phase Structure (6 Battle Turns = 1 Combat Phase).",
        "   - Dual-Resource Pool: Sorrow Gauge (0-100%) and Composure (SP).",
        "   - Dual-Threshold Stagger Engine (Stagger 1 at 60%, Terminal 25%).",
        "   - M.A.W. Quadripartite Armaments & 4 Sorrow Elements.",
        "---",
        "2. REVERIE DIRECTORATE (R.D.) STYLE - Facility Oversight & Contain",
        "   - Domain: Subterranean Facility 01 (Hand of Change).",
        "   - Topology: 10-Node Containment Vault & Console Grid.",
        "   - Core: Echo-Core Floor Resonance (Floors 1 to 8).",
        "   - Focus: Work Cycles (Flere/Pugna/etc), meltdowns, and Ordeals.",
        "---",
        "3. UNDERWORLD CLEANUP DESCEND (UCD) STYLE - Urban CQB & Interdict",
        "   - Domain: Undercity slums, drainage kilns, vaults.",
        "   - Topology: 10-Node Ingress Grid (Cordon to Sanctum).",
        "   - Core: Targeted Part Dismantling (Modular Parts).",
        "   - Focus: In-combat forensic hacking, civilian cover, collateral.",
        "---",
        "4. SOMNARAK EXPLORATION DECREE (SED) STYLE - Abyssal Descents",
        "   - Domain: Unmapped karst caverns (-50m to -3,500m).",
        "   - Topology: 10-Node Vertical Karst & Chasm Grid.",
        "   - Core: Strata Depth Atmospheric Pressure per Phase.",
        "   - Focus: Acoustic stealth / decibel sonar, seismic pitons, relics.",
        "---",
        "5. THE MEMORY ARCHIVE (GIEOK JEOJANGSO) STYLE - Mnemonic Reception",
        "   - Domain: Deep Strata Sub-Alpha Roots (-2,350m to -3,250m).",
        "   - Topology: 10-Node Strata Reception & Key Page Dais Grid.",
        "   - Core: Mnemonic Projection Array & Floor Realization.",
        "   - Focus: Memory anchor dismantling, Key Page transmutation.",
        "---",
        "6. THE HORIZON CARAVAN (JIPYEONGSEONDAE) STYLE - Overland Expedition",
        "   - Domain: The Desolate, Sea of Glass, Cheonbulok, Mugeukji.",
        "   - Topology: 10-Node Mobile Crawler Ramps & Sand Basin Grid.",
        "   - Core: Planetary Ley-Drive Navigation & Vehicular Severance.",
        "   - Focus: High-speed sand maneuvers, crawler siege railguns."
    ]
    new_hexa_box = make_box("PROJECT SOMNARAK: HEXA-STYLE BATTLE SYSTEM ARCHITECTURE", hexa_rows)

    if old_box_start in content and box_end != -1:
        content = content[:content.find(old_box_start)] + new_hexa_box + content[box_end + len("+=====================================================================+"):]
        print("Replaced Section I box successfully!")

    # Now find where Section IX begins and insert Sections IX and X before it, renumbering XI and XII
    old_sec_ix = "## IX. Complete Combat Visualization Template & Step-by-Step Scenario"
    new_sec_xi = "## XI. Complete Combat Visualization Template & Step-by-Step Scenario"
    old_sec_x = "## X. Story Combat Adaptation Guidelines"
    new_sec_xii = "## XII. Story Combat Adaptation Guidelines"

    content = content.replace(old_sec_ix, new_sec_xi)
    content = content.replace(old_sec_x, new_sec_xii)

    sec_9_10 = build_section_9_and_10()
    content = content.replace(new_sec_xi, sec_9_10 + "\n\n" + new_sec_xi)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated SOMNARAK_BATTLE_SYSTEM_STYLES.md successfully!")

if __name__ == "__main__":
    main()
