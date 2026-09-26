#!/usr/bin/env python3
"""
tools/update_katharcheok_overview.py
Updates Section III and strike officer attributes in SOMNARAK-WORLD/Katharcheok/KATHARCHEOK_OVERVIEW.md
with the universal 10-node spatial grid, Speed/AP economy, M.A.W.-W modifiers, and Four P-framework.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def get_section_iii():
    grid_box = make_box("UCD UNIVERSAL 10-NODE URBAN CQB COMBAT GRID", [
        "[STAGE NODES 01 TO 10 — CORDON INGRESS TO SANCTUM DAIS]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "|--BREACH CORDON-| |--SLUICE ALLEY--| |--FOUNDRY FLOOR-|",
        "|--SANCTUM DAIS--|",
        "---",
        "- Node 01: Breach Cordon (Entry Ram / Cruiser 'The Iron Vanguard')",
        "- Node 02-03: Tight Corridors & Sluice Alleys (Taeho & Joon Vanguard)",
        "- Node 04-05: Industrial Foundry / Usury Floor (Syndicate Enforcers)",
        "- Node 06-07: Server Vault & Data Terminal (Yuna Wiretap / Minho Sniper)",
        "- Node 08-09: Hostage Holding Berths & Slag Sluice (Civilian Rescue)",
        "- Node 10: Syndicate Command Dais / Cask Vault (Boss Core / Echo Stealth)",
        "---",
        "RANGE BANDS (1 TO 5):",
        "- Band 1 (Nodes 1-2): Melee, Tower Shields, Hydraulic Sapping Rams",
        "- Band 2 (Nodes 3-4): Riot Truncheons, Shotguns, Acoustic Shock Pikes",
        "- Band 3 (Nodes 5-6): Carbines, Forensic Data Lances, Resonance Snares",
        "- Band 4 (Nodes 7-8): Sniper Lancets, Cryo Dart Rifles, Heavy EMP Units",
        "- Band 5 (Nodes 9-10): Siege Mortars, Command Slates, Catenary Harpoons"
    ])

    framework_box = make_box("THE FOUR P-FRAMEWORK IN SUB-MUNICIPAL OPERATIONS", [
        "P1: PASSIVES (TACTICAL BREACH INSTINCTS & MOMENTUM SURGE)",
        "- Momentum Surge: Winning clashes awards +2 Speed on the next turn.",
        "- Breach Poise: Operating adjacent to allies grants +3 Protection.",
        "- Suppression Stance: Point-blank strikes inflict +25% Posture Strain.",
        "---",
        "P2: PANIC / COMPOSURE (CIVIL PANIC & STREET TERROR DYNAMICS)",
        "- Composure (SP): Operative mental resilience against black-market M.A.W.",
        "- Civil Panic Index (0-100%): Excessive noise triggers tenement riots.",
        "- Non-Lethal Calibrated Salves: Minho and Soojin restore +15 SP.",
        "---",
        "P3: PARRY / PROTECTION (PHALANX DEFLECTION & VACUUM ABSORPTION)",
        "- Phalanx Bastion: Directional absorption converting damage to tremor.",
        "- Deployable Mantlet: Absorbs ranged projectile volleys and slag.",
        "- Leaded Damping Bubble: Vacuum sphere capturing rogue entity miasma.",
        "---",
        "P4: POSTURE / POISE (MODULAR STAGGER & CASK VACUUM CONTAINMENT)",
        "- Posture Meters: Exoskeletons and boss chassis have discrete posture.",
        "- Stagger 1 Proc (60% Strain): Disables weapon arms; deals 1.5x damage.",
        "- Stagger 2 Proc (0% Collapse): Terminal Stagger; cask vacuum sealing."
    ])

    return f"""## III. Urban Breach Topology & The Tactical Grid System

### 3.1 The Universal 10-Node Urban CQB Grid System (Spatial Combat Engine)
Urban counter-insurgency inside dense, multi-story tenements, illegal foundries, and subterranean usury vaults requires methodical, room-by-room clearance. The UCD executes all tactical kinetic sweeps across a standardized **10-Node Urban CQB Grid**:

```text
{grid_box}
```

- **Range Bands 1 through 5**: Combatants occupy discrete nodes from `[N01]` to `[N10]`. Melee breachers (Commander Taeho and Engineer Joon) control Nodes 01–03 to anchor the breach and absorb hostile kinetic energy. Mid-field analysts (Auditor Yuna and Handler Soojin) operate from Nodes 04–06 to deploy electromagnetic wiretaps and resonance damping fields. High-precision snipers (Investigator Minho) and shadow assassins (Infiltrator Echo) utilize elevated rafters and catenary catwalks at Nodes 07–10 to dismantle critical boss components from extreme range.
- **Action Point (AP) Economy & Speed Ratings**: Base Speed directly determines Action Point generation per Battle Turn (`Speed 4-5 = 2-3 AP`, `Speed 6-7 = 3-4 AP`, `Speed 8-9+ = 4-5 AP`). Operatives spend AP to advance across nodes (1 AP per node displacement), execute standard tactical skills (2 AP), or channel specialized Climax Overdrives (3 AP).
- **M.A.W.-W Weight Class Delta Modifiers**:
  * **Heavy Armor Class** (Commander Taeho): Speed delta -1, Poise +25. Unyielding kinetic inertia.
  * **Medium Rig Class** (Engineer Joon, Handler Soojin): Speed delta 0, Poise +15 to +20. Balanced industrial loadout.
  * **Light Suit Class** (Auditor Yuna, Investigator Minho): Speed delta +1, Poise +5, Evasion +15\%. High-frequency maneuverability.
  * **Feather Shroud Class** (Infiltrator Echo): Speed delta +2, Poise 0, Stealth +35\%. Unmatched velocity and critical ambush potential.

### 3.2 The Four P-Framework in Sub-Municipal Counter-Insurgency
Every clash, maneuver, and containment protocol executed by the UCD operates under the **Four P-Framework**:

```text
{framework_box}
```

### 3.3 Targeted Part Dismantling & Modular Boss Destruction
Syndicate kingpins in The Raw rarely fight unarmored; they augment their bodies with stolen industrial exoskeletons, black-market pneumatic sledges, high-voltage whips, and chemical distillation rigs. UCD protocol mandates **Targeted Part Dismantling**:
1. **Pneumatic / Hydraulic Weapon Arms**: Targeting weapon couplings (e.g. Boss Gwangseok's *Forging Hammer*, Sura's *Distillation Sprayer*, Boknam's *Harvest Hook*, Man-sik's *Foreclosure Cudgel*, Jagyeon's *Shock Whip*, Cheon's *Crown Scepter*) destroys the syndicate's primary lethal threat and triggers **Stagger Level 1**.
2. **Exoskeleton Chassis & Power Cells**: Once primary armaments are shattered, focused sapping strikes destroy hydraulic servos and thermal batteries, reducing boss defenses to zero.
3. **Contraband Sorrow Entity Isolation**: Criminal syndicates exploit captive Sorrow Entities as biological batteries. Handler Soojin and Infiltrator Echo sever the illicit neural siphons, isolating the entity from the syndicate boss and deploying cryogenic vacuum casks to achieve non-lethal **Terminal Stagger Containment**."""

def update_overview():
    path = "SOMNARAK-WORLD/Katharcheok/KATHARCHEOK_OVERVIEW.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "## III. Urban Breach Topology & The Tactical Grid System"
    end_str = "## IV. The Six Strike Officers of the Joint Task Force (Comprehensive Tactical & Lore Profiles)"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error locating boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_sec = get_section_iii() + "\n\n"
    new_content = content[:start_idx] + new_sec + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated KATHARCHEOK_OVERVIEW.md successfully!")

if __name__ == "__main__":
    update_overview()
