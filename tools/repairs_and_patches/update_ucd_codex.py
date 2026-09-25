#!/usr/bin/env python3
"""
tools/update_ucd_codex.py
Updates Section VIII of SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_UNDERWORLD_CLEANUP_DESCEND.md
with the universal 10-node spatial engine, Speed/AP economy, M.A.W.-W modifiers, and Four P-framework.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def get_section_viii():
    phase_box = make_box("THREE-PHASE RECLAMATION SEQUENCE", [
        "PHASE STAGE          | OPERATIONAL PROTOCOL",
        "===+",
        "Phase I: Forensic    | Digital bank freeze, server drive cloning",
        "Interdiction         | Comms wiretap, transaction tracing",
        "---",
        "Phase II: Kinetic    | Magnetic barrier ram, acoustic damping grid",
        "Breach & Lockdown    | 10-Node CQB room-to-room pacification",
        "---",
        "Phase III: Entity    | Lead cask vacuum seal, hostage extraction",
        "Confiscation         | Maw's Keep Floor 2 transfer within 24h"
    ])

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

    framework_box = make_box("THE FOUR P-FRAMEWORK IN UCD INTERVENTIONS", [
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

    return f"""## Section VIII: Tactical Breaching Physics, Forensic Rules & Engagement Protocols

### The Three-Phase Reclamation Doctrine (도시 진압 및 탈환 3단계)
Every kinetic intervention executed by the UCD adheres to a strict, non-negotiable three-phase operational sequence:

```text
{phase_box}
```

1. **Phase I: Forensic & Financial Interdiction**:
   - Auditor Yuna freezes all syndicate banking relays and promissory credit nodes.
   - Investigator Minho deploys cryo-data shunts to clone and isolate server hard drives before syndicate technicians can execute emergency memory-wipe scripts.
   - Objectives: Preserve victim identity traces, isolate financial transaction roots, and map clandestine tunnel escape routes.

2. **Phase II: Kinetic Breach & Sector Isolation**:
   - Engineer Joon and Commander Taeho deploy magnetic pneumatic rams to breach fortified blast doors within 8 seconds.
   - Sapper units immediately deploy acoustic dampening curtains around the breach perimeter, containing all gunfire, explosion noise, and scream frequencies within the structure.
   - Non-Lethal Rules of Engagement: Acoustic riot pikes and tear-brine canisters are prioritized against low-level cartel muscle. Lethal kinetic force is authorized exclusively against syndicate captains actively employing illicit M.A.W. weaponry or threatening hostages.

3. **Phase III: Entity Confiscation & Containment Handoff**:
   - Handler Soojin immobilizes and secures all abused Sorrow Entities into leaded-basalt vacuum casks.
   - Liberated civilian captives are screened for counterfeit Veil stones, provided with electrolyte broth, and evacuated via *The Iron Vanguard* cruisers.
   - All seized Sorrow Entities are loaded onto *The Leaded Paddywagon* and transferred directly to Reverie Directorate Floor 2 within twenty-four hours.

### The Universal 10-Node Urban CQB Grid System (Spatial Combat Engine)
All room-to-room kinetic engagements executed by the UCD are mapped onto the canonical **10-Node Urban CQB Grid**:

```text
{grid_box}
```

- **Speed, Action Points & Range Bands**:
  * Operatives spend Action Points (AP) generated by their net Speed rating (`Speed 4-5 = 2-3 AP`, `Speed 6-7 = 3-4 AP`, `Speed 8-9+ = 4-5 AP`).
  * Movement between discrete nodes costs 1 AP per node displacement. Range Bands 1 through 5 determine optimal weapon efficiency and line-of-sight penalties.
- **M.A.W.-W Weight Class Delta Modifiers**:
  * *Heavy Armor Class* (Commander Taeho): Speed delta -1, Poise +25.
  * *Medium Rig Class* (Engineer Joon, Handler Soojin): Speed delta 0, Poise +15 to +20.
  * *Light Suit Class* (Auditor Yuna, Investigator Minho): Speed delta +1, Poise +5, Evasion +15\%.
  * *Feather Shroud Class* (Infiltrator Echo): Speed delta +2, Poise 0, Stealth +35\%.

### The Four P-Framework in Sub-Municipal Law Enforcement
Every engagement in The Raw integrates the **Four P-Framework**:

```text
{framework_box}
```

### Targeted Part Dismantling & Modular Boss Destruction
UCD doctrine focuses kinetic fire on modular weapon components (pneumatic hammers, chemical sprayers, harvest hooks, foreclosure cudgels, shock whips, and crown scepters) to induce **Stagger Level 1 (60% Posture Strain)** before destroying the boss chassis and securing captive Sorrow Entities into cryogenic lead casks at **Terminal Stagger (0% Posture Collapse)**."""

def update_codex():
    path = "SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_UNDERWORLD_CLEANUP_DESCEND.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "## Section VIII: Tactical Breaching Physics, Forensic Rules & Engagement Protocols"
    end_str = "## Section IX: Operational Context: The Katharcheok Campaign (Operations 1 to 6)"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error locating boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_sec = get_section_viii() + "\n\n"
    new_content = content[:start_idx] + new_sec + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated The_UNDERWORLD_CLEANUP_DESCEND.md successfully!")

if __name__ == "__main__":
    update_codex()
