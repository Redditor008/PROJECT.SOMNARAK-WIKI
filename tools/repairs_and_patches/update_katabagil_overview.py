#!/usr/bin/env python3
"""
tools/update_katabagil_overview.py
Updates Section III in SOMNARAK-WORLD/Katabagil/KATABAGIL_OVERVIEW.md
with the universal 10-node vertical abyss grid, Speed/AP economy, M.A.W.-W modifiers,
decibel sonar mechanics, tectonic pressure, and Four P-framework.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def get_section_iii():
    grid_box = make_box("SED UNIVERSAL 10-NODE VERTICAL ABYSS COMBAT GRID", [
        "[STAGE NODES 01 TO 10 — UPPER RIG INGRESS TO PRIMORDIAL CORE]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "|--BOREHOLE RIG-| |--FLOODED LEDGE-| |--CENTRAL DAIS---|",
        "|--SOVEREIGN SOUL|",
        "---",
        "- Node 01: Borehole Rig Staging ('The Iron Mole' Anchor / Heavy Lift)",
        "- Node 02-03: Bedrock Causeways & Trenches (Harin & Doha Vanguard)",
        "- Node 04: Sluice Conduits & Spore Clearings (Sora Mnemonic Repose)",
        "- Node 05: Central Altar / Strata Dais (Apex Boss Sovereign Core)",
        "- Node 06-07: High Spire Catwalks & Arches (Yeonhwa Sonar / Minjae Scribe)",
        "- Node 08: Forensic Balconies & Ballast Gauges (Jisoo Cryo Harpoon)",
        "- Node 09: Sub-Dais Abyssal Chasm (Tectonic Pressure Buffer)",
        "- Node 10: Strata Descent Sluice / Sovereign Reliquary (The Silent One)",
        "---",
        "RANGE BANDS (1 TO 5):",
        "- Band 1 (Nodes 1-2): Heavy Tower Shields, Pneumatic Rams, Relic Cleavers",
        "- Band 2 (Nodes 3-4): Sapper Drills, Incendiary Wedges, Shock Pikes",
        "- Band 3 (Nodes 5-6): Sonar Theodolites, Silver Cowl Resonators, Carbines",
        "- Band 4 (Nodes 7-8): Forensic Scribe Tablets, Archaeological Lancets",
        "- Band 5 (Nodes 9-10): Hydraulic Winches, Cryo Harpoons, Anchor Cables"
    ])

    framework_box = make_box("THE FOUR P-FRAMEWORK IN ABYSSAL EXPEDITIONS", [
        "P1: PASSIVES (MOMENTUM SURGE & SONAR TARGET LOCK)",
        "- Momentum Surge: Winning clashes awards +2 Speed on the next turn.",
        "- Sonar Target Lock: Yeonhwa tags part seams, giving +25% Stagger Dmg.",
        "- Primordial Resonator: Sora 528 Hz aura nullifies psychic miasma.",
        "---",
        "P2: PANIC / COMPOSURE (DEPTH CLAUSTROPHOBIA & SANITY ANCHOR)",
        "- Composure (SP): Operative sanity against depth terror (0 to 50 SP).",
        "- Panic Meltdown: Dropping below 10 SP triggers emotional fracture.",
        "- Mnemonic Recall Needles: Sora and Jisoo restore +15 to +20 SP.",
        "---",
        "P3: PARRY / PROTECTION (KINETIC BULWARK & HARMONIC REPOSE)",
        "- Bastion Kinetic Lock: Harin reflects physical impact back as tremor.",
        "- Sapper Counter-Lever: Doha absorbs kinetic force to pop armor seams.",
        "- Leaded Damping Dome: Sora vacuum sphere capturing rogue sorrow waves.",
        "---",
        "P4: POSTURE / POISE (MODULAR STAGGER & TERMINAL PACIFICATION)",
        "- Part Posture Pools: Boss weapons/cores have discrete posture pools.",
        "- Stagger 1 Proc (60% Strain): Destroys modular weapon parts.",
        "- Stagger 2 Proc (0% Collapse): Terminal Stagger; communion pacification."
    ])

    return f"""## III. The Spire Path System & Subterranean Topology Mechanics

### 3.1 Node-Based Subterranean Navigation
Because standard radio, GPS, and optical line-of-sight are impossible thousands of meters beneath solid rock, the Somnarak Exploration Decree utilizes the **Spire Path Navigation System**. Every descent through a stratum is mapped as a directed tactical topology composed of six distinct node classifications:

```text
+==============================================+
|       SPIRE PATH NODE CLASSIFICATION         |
+==============================================+
| NODE TYPE            | STRATEGIC FUNCTION    |
+======================+=======================+
| Waypoint (Transit)   | Elevation change,     |
|                      | path clearance        |
+----------------------+-----------------------+
| Scouting (Sonar Ping)| Unveils forward nodes,|
|                      | detects hazards       |
+----------------------+-----------------------+
| Relic Cache          | Unearths pre-cataclysm|
|                      | gear & ancient ledgers|
+----------------------+-----------------------+
| Geological Hazard    | Sapping, filtration,  |
|                      | structural anchoring  |
+----------------------+-----------------------+
| Respite Camp         | SP restoration, meal  |
|                      | rationing, repairs    |
+----------------------+-----------------------+
| Apex Sanctuary       | Boss pacification &   |
|                      | strata seal unlocking |
+======================+=======================+
```

1. **Waypoint Nodes (Transit & Descent)**: Stable rock tunnels, pneumatic shafts, or staircases connecting distinct elevation shelves. Moving through these nodes consumes fuel and water ballast but presents minimal immediate danger.
2. **Scouting Nodes (Sonar & Cartography)**: High-vantage outcroppings or acoustic sounding chambers where Cartographer Yeonhwa deploys *The Horizon Theodolite*. Successful sounding reveals hidden branching paths, entity ambush locations, and geological stability ratings for the subsequent three nodes.
3. **Relic Cache Nodes (Archaeological Recovery)**: Sealed pre-cataclysm bunkers, crushed supply trains, or mineralized fossil beds. Excavating these nodes yields ancient historical diaries, high-grade crystalline Han raw material, or specialized M.A.W. weapon components.
4. **Geological Hazard Nodes (Structural Chokepoints)**: Tectonic compression faults, flooded fissures, or boiling sorrow geysers. Passing these nodes requires a designated specialist to lead a breach protocol: Master Doha deploys hydraulic shoring, Warden Harin anchors kinetic blast shields, or Weaver Sora creates an acoustic damping web.
5. **Respite Camp Nodes (Sub-Strata Havens)**: Natural dry caves or fortified steel bunkers equipped with acoustic nullification field generators. At these nodes, the vanguard rests, repairs suits, restores Composure (SP), and shares emotional counsel.
6. **Apex Sanctuary Nodes (Strata Terminus)**: The lowest point of each stratum, sealed by an ancient geological or hydraulic lock and guarded by an apex Sorrow Entity. Clearing the apex entity and unsealing the gate is mandatory to unlock descent into the subsequent stratum.

### 3.2 The Universal 10-Node Vertical Abyss Grid (Spatial Combat Engine)
When the Vanguard engages apex entities guarding strata gates, all tactical combat executes across the canonical **10-Node Vertical Abyss Grid**:

```text
{grid_box}
```

- **Speed, Action Points & Movement**:
  * Operatives generate Action Points based on their net Speed rating (`Speed 4-5 = 2-3 AP`, `Speed 6-7 = 3-4 AP`, `Speed 8-9+ = 4-5 AP`).
  * Movement between adjacent nodes costs 1 AP per node displacement. Range Bands 1 through 5 establish line-of-sight and weapon reach.
- **M.A.W.-W Weight Class Delta Modifiers**:
  * *Heavy Armor Class* (Warden Harin): Speed delta -1, Poise +25. Kinetic redirection and immovable anchoring.
  * *Medium Rig Class* (Architect Doha, The Silent One): Speed delta 0, Poise +20, Crit +30\%. Structural sapping and relic striking.
  * *Light Suit Class* (Weaver Sora, Cartographer Yeonhwa, Scribe Minjae, Assessor Jisoo): Speed delta +1, Evasion +15\%. High-frequency acoustic resonance and forensic recording.

### 3.3 The Four P-Framework in Abyssal Expeditions
Every encounter throughout the seven subterranean descents operates under the **Four P-Framework**:

```text
{framework_box}
```

### 3.4 Subterranean Tectonic Pressure & Decibel Acoustic Sonar
Operating at depths between -150m and -2,800m imposes unique environmental mechanics:
1. **Depth Tectonic Pressure**: Bedrock compression strain inflicts continuous passive posture stress on all combatants unless counterbalanced by Warden Harin's ground anchors and Master Doha's hydraulic shoring.
2. **Decibel Acoustic Sonar Management**: High-impact kinetic detonations echo across subterranean caverns. Excessive acoustic noise (>90 dB) risks triggering rockfalls or alerting dormant abyssal swarms, requiring Weaver Sora's 528 Hz damping cowls and Cartographer Yeonhwa's theodolite null-fields.

### 3.5 Targeted Part Dismantling & Non-Lethal Communion Protocols
Apex guardians of the Before-Time are not malicious monsters; they are the petrified mourners and automated gatekeepers of ancient humanity. SED doctrine strictly enforces **Targeted Part Dismantling**:
1. **Shattering Offensive Weaponry**: Destroying primary weapon parts (e.g. Siphon arms, Siege hammers, Rail mandibles, Root tendrils, Magma cleavers, Fury glaives, Tear halos) neutralizes lethal AoE threats and triggers **Stagger Level 1 (60% Posture Strain)**.
2. **Armor Shell Penetration**: Sapping heavy carapaces and slag shields reduces boss defenses to zero and skips dangerous phase escalations.
3. **Communion & Peaceful Release**: Once the entity reaches **Terminal Stagger (0% Posture Collapse)**, the Vanguard executes non-lethal communion, offering empathetic acknowledgment and releasing the ancient grief to unlock the stratum gate permanently.

### 3.6 Path Divergence & Stability Risk Modeling
During an expedition, the Vanguard Lead must choose between multiple branching paths. Each route carries an operational trade-off between **Descent Velocity**, **Resource Ballast Expenditure**, and **Tectonic Stability Cost**:

| Route Designation | Stability Cost | Composure Risk | Resource & Tactical Yield |
|---|---|---|---|
| **The Sapper Way** (Excavated Tunnel) | High (-15% Stability) Seismic Cave-in Risk | Low (-5 SP Drain) Steady, Secure Pace | High Relic & Ancient Blueprints sapped from pre-cataclysm masonry |
| **The Smuggler Artery** (Syndicate Bypass) | Medium (-8% Stability) Gravity Well Trap | High (-18 SP Drain) Ambush Hazard | Moderate Illicit Contraband & Pneumatic High-Velocity Tubes |
| **The Resonant Fissure** (Natural Chasm) | Low (-2% Stability) Solid Ancient Bedrock | Critical (-35 SP Drain) Psychic Hallucinations | Maximum Pure Crystalline Han & Primordial Dream Relics |

- **Tectonic Stability Index (100% to 0%)**: Represents the structural integrity of the surrounding rock ceiling. If stability drops below 25%, seismic tremors trigger frequent rockfalls during combat, inflicting unblockable blunt trauma on all combatants. If stability reaches 0%, a catastrophic cave-in occurs, triggering **Branch I: The Tectonic Catastrophe**."""

def update_overview():
    path = "SOMNARAK-WORLD/Katabagil/KATABAGIL_OVERVIEW.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "## III. The Spire Path System & Subterranean Topology Mechanics"
    end_str = "## IV. The Seven Specialists of the Core Vanguard (Comprehensive Tactical & Lore Profiles)"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error locating boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_sec = get_section_iii() + "\n\n"
    new_content = content[:start_idx] + new_sec + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated KATABAGIL_OVERVIEW.md successfully!")

if __name__ == "__main__":
    update_overview()
