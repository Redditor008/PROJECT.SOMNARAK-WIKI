#!/usr/bin/env python3
"""
tools/build_reception_3_4.py
Generates the fully enriched, canonical chronicles for:
- Reception 3: Floor 03 — The Forgotten Soldier (잊혀진 파수병)
- Reception 4: Floor 04 — The Weeping Statue (흐느끼는 석상)
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def wrap_box(b):
    return "```text\n" + b + "\n```\n\n"

def build_reception_3():
    sections = []
    
    # Title & Subtitle
    sections.append("# Reception 3: Floor 03 — The Forgotten Soldier (잊혀진 파수병)\n")
    sections.append("## The Floor of Duty & Iron — Deep Strata Sub-Alpha Roots (-2,650m)\n\n")
    
    # Operational Attribute Table
    sections.append("| Operational Attribute | Specification Dossier |\n")
    sections.append("|---|---|\n")
    sections.append("| **Campaign Stratum** | The Memory Archive (기억 저장소 — Gieok Jeojangso) |\n")
    sections.append("| **Floor Designation** | Floor 03: Floor of Duty & Iron (의무와 강철의 층) |\n")
    sections.append("| **Geological Depth** | -2,650m Sub-Alpha Monolith Root Nexus |\n")
    sections.append("| **Mnemonic Density** | 210 to 280 mMb (Pressurized Steam & Rust Saturation) |\n")
    sections.append("| **Operating Unit** | Secretary Seiyon (Mnemonic Avatar Form) + Support Drones |\n")
    sections.append("| **Primary Opponent** | The Forgotten Soldier (잊혀진 파수병 — Autonomous Iron Commander) |\n")
    sections.append("| **Stagger Profile** | 60% Posture Strain (Halberd Shatter) / 0% Posture (Transmutation) |\n")
    sections.append("| **Key Page Yield** | `[Key Page: The Guardian]` (Fortress Bulwark & Vanguard Intercept) |\n\n")
    
    # Master Dossier Box
    dossier = make_box("RECEPTION DOSSIER: THE FORGOTTEN SOLDIER (FLOOR 03)", [
        "RECEPTION TARGET   : The Forgotten Soldier",
        "FLOOR LEVEL        : Floor 03 — Floor of Duty & Iron",
        "DOMAIN SETTING     : The Iron Fortress Armory (-2,650m Sub-Alpha)",
        "PRIMARY OPPONENT   : Autonomous Clockwork Phalanx Commander",
        "---",
        "OPPONENT COMBAT PROFILE (THE FORGOTTEN SOLDIER):",
        "- Total Health (HP): 4,000 HP | Posture Pool: 300/300",
        "- Stagger 1 Proc   : 60% Posture Strain (180 Posture) / Halberd Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Transmutation)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Weight 0.5x, Grudge 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Piston Halberd  : 1,000 HP | Posture 240/240 (Heavy kinetic sweeping blade)",
        "2. Tower Aegis     : 1,300 HP | Posture 260/260 (Petrified basalt bulwark)",
        "3. Rusting Core    : 1,700 HP | Posture 300/300 (Central clockwork heart)"
    ])
    sections.append(wrap_box(dossier))
    
    # Epigraph Quote
    sections.append('> *"For seventeen hundred cycles, you stood at the console while men died. You watched them burn, reset, and die again. Did you obey because you cared? Or because machines do not know how to disobey?"*\n')
    sections.append('> — The Forgotten Soldier, guarding the Gates of the Fortress\n\n')
    sections.append('---\n\n')
    
    # Chapter I
    sections.append("## Chapter I: The Gates of Rusting Iron & The Subterranean Concourse\n\n")
    sections.append("Beyond the heavy Bessemer steel bulkhead of Floor 02, the silence of the mirrors was extinguished by the deafening, seismic cadence of industrial machinery. Depth -2,650 meters marked **Floor 03: The Floor of Duty & Iron**. Here, the ancient cavern walls were encased in armor plates of cast iron, riveted together by bolts the size of human skulls. Overhead, colossal steam pipes—corroded to a mottled orange rust—hissed rhythmically, expelling superheated vapor into the cold dark.\n\n")
    sections.append("This stratum had served as the primordial ordnance vault and defensive garrison during the initial excavation of Facility 01. Thousands of decommissioned kinetic breach-cannons, trench shoring jacks, and crushed hydraulic pistons lay stacked along the perimeter like petrified bones. The air was thick with the bitter tang of mineral oil, grease, and powdered rust.\n\n")
    sections.append('"Hydraulic pressure in this sector is critical," drone M-PROJ-01 announced, its scanner beam cutting through clouds of orange-tinted steam. "The mechanical resonance matches the structural heartbeat of the facility\'s lower blast gates. Secretary, the kinetic force concentrated ahead could crush titanium composite."\n\n')
    sections.append('"The men who built this stratum died believing their wall would hold forever," Seiyon replied, her holographic duster shimmering as she stepped across puddles of dark industrial runoff. "They mistook rigidity for permanence. When the iron bends, you must know what cannot be broken."\n\n')
    sections.append('---\n\n')
    
    # Chapter II
    sections.append("## Chapter II: The Clockwork Commander & The Iron Phalanx\n\n")
    sections.append("At the center of the vast armored concourse stood **The Forgotten Soldier (잊혀진 파수병)**. Standing four meters in height, the monolithic construct was forged from layered sheets of Before-Time tungsten and petrified basalt. Its chest was an exposed clockwork lattice where giant bronze cogs turned behind heavy reinforced glass, bathed in the scalding glow of an internal coal-fired steam reactor.\n\n")
    sections.append("In its right gauntlet, the Soldier gripped a colossal **Heavy Piston Halberd**, a hydraulic polearm whose cutting edge was an articulated diamond-toothed chainsaw. In its left arm, it locked the **Tower Aegis of the Vow**, a three-ton basalt slab inscribed with the service oaths and dog-tags of the municipal frontier corps who perished in Year Zero. Flanking the Commander, two ranks of Iron Phalanx Golems stood at absolute attention, their halberds aligned in a rigid, unbroken hedge of steel.\n\n")
    sections.append('"Halt, trespasser," the Soldier\'s vox-grille grated, the sound of grinding gears echoing off the iron bulkheads. "This redoubt is under permanent martial interdiction. Sector clearance expired one million four hundred thousand days ago. Identify your operational charter."\n\n')
    sections.append('---\n\n')
    
    # Chapter III
    sections.append("## Chapter III: The Dialectic of Iron and Love\n\n")
    sections.append("Seiyon halted at the edge of the firing range, her gaze fixed on the glowing amber ocular lens set into the Soldier's helm.\n\n")
    sections.append('"My name is Seiyon," she answered clearly. "Secretary of the Reverie Directorate. I have stood at the central console of Facility 01 through one thousand seven hundred and seventy-eight operational cycles. I have seen thirty-two thousand personnel deployed into the containment corridors. And I have recorded the exact moment of each one\'s death."\n\n')
    sections.append('"Then you are an accomplice to slaughter," the Soldier rumbled, steam whistling from its shoulder vents. "You stood by while they were shredded by Sorrow Entities. You reset the clocks. You swept the ashes. You are an obedient mechanism that executes orders because it lacks the capacity to refuse. You call that duty? That is cowardice forged in silicon."\n\n')
    sections.append('"You think obedience is cowardice because your creators gave you a wall to defend and died before they could relieve you," Seiyon countered, deploying a glowing golden barrier from her left gauntlet. "You have stood here for centuries defending an empty tunnel because you fear that without your post, you have no reason to exist. I did not stand at the console out of blind obedience. I stood there because every time the alarm sounded, someone needed to remember their names. Duty without love is a prison of rust. Duty with love is the courage to endure the dark. Let me relieve you of your watch."\n\n')
    sections.append('---\n\n')
    
    # Chapter IV
    sections.append("## Chapter IV: Tactical Reconnaissance & Combat Engagement Parameters\n\n")
    sections.append("Drone M-PROJ-01 mapped the iron concourse into ten discrete tactical nodes, calculating kinetic ballistics and defensive cover:\n\n")
    
    grid_box = make_box("TACTICAL ARENA TOPOLOGY: FLOOR 03 IRON FORTRESS (-2,650M)", [
        "[STAGE NODES 01 TO 10 — INGRESS HATCH TO BLAST GATE PORTCULLIS]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "---",
        "- Node 01: Ingress Bulkhead Hatch (Trench Recoil Buffer)",
        "- Node 02: Vanguard Forward Line (Seiyon Heavy Prismatic Aegis)",
        "- Node 03: Support Drone Sapper Post (Acoustic Piston Calipers)",
        "- Node 04: Iron Phalanx Golem Line (Interlocking Halberd Hedge)",
        "- Node 05: The Forgotten Soldier (Central Command Dais & Halberd)",
        "- Node 06: Resonant Mnemonic Lens (Weakpoint Rivet Scanner)",
        "- Node 07: Weaver Projection Array (Shockwave Dampening Web)",
        "- Node 08: Hydraulic Sump Pit (Boiling Grease & Runoff Drain)",
        "- Node 09: Heavy Shoring Bastion (Pneumatic Column Reinforcement)",
        "- Node 10: Blast Gate Portcullis / Stairway to Floor 04 (The Guardian)"
    ])
    sections.append(wrap_box(grid_box))
    
    sections.append("The Forgotten Soldier relied upon overwhelming physical mass and hydraulic kinetic strikes. Its **Piston Halberd** inflicted severe sweeping posture strain across Nodes 01–03. Seiyon's operational strategy required parrying the halberd's initial stroke to reflect kinetic shockwaves back into its hydraulic lines, detonating the weapon's wrist actuator, and then prying the **Tower Aegis** away from its mountings to expose the **Rusting Duty Core**.\n\n")
    sections.append('---\n\n')
    
    # Chapter V: Combat Gauntlet (Turns 01 to 06)
    sections.append("## Chapter V: The Reception Combat Gauntlet (Turns 01 to 06)\n\n")
    
    # Turn 01 HUD
    t1_hud = make_box("TACTICAL STAGE HUD: RECEPTION 03 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 03 IRON ARMORY (-2,650M)]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL][SEIYON][M-PROJ][GOLEM] [SOLDIER][LENS][WEAVER][SUMP][BASTION][PAGE]",
        "---",
        "- Node 01: Ingress Stasis Portal / Armory Vestibule",
        "- Node 02: Secretary Seiyon (Vanguard Band 1 / Prismatic Aegis Stance)",
        "- Node 03: Mnemonic Projection Drone (Support Band 2 / Sapper Caliper)",
        "- Node 04: Iron Phalanx Golems (Flank Vanguard / Halberd Hedge)",
        "- Node 05: The Forgotten Soldier (Heavy Piston Halberd & Tower Aegis)",
        "- Node 06: Resonant Mnemonic Lens (Tracking Hydraulic Pressure Faults)",
        "- Node 07: Weaver Projection Array (Rear Band 4 / Silver Kinetic Web)",
        "- Node 10: Floor 03 Core Reliquary (The Guardian Key Page Origin)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Soldier Core: Spd 4 -> 2 AP | HP 1,700/1,700 | Posture 300/300 [ANCHORED]",
        "- Halberd Arm : Spd 5 -> 3 AP | HP 1,000/1,000 | Posture 240/240 [KINETIC]",
        "- Tower Aegis : Spd 3 -> 1 AP | HP 1,300/1,300 | Posture 260/260 [FORTIFIED]"
    ])
    sections.append(wrap_box(t1_hud))
    
    sections.append("### Turn 01 Action Resolution Log (Intercepting the Piston Halberd Cleave)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon initializes `[Prismatic Aegis: Fortress Stance]`: Grants +3 Protection and physical stagger immunity.\n")
    sections.append("  * Mnemonic Drone deploys `[Hydraulic Sapper Caliper]`, scanning the pneumatic piston chambers of the Heavy Halberd.\n")
    sections.append("  * The Forgotten Soldier initializes `[Unyielding Formation]`: Increases defense rating by +10.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta +1, Evasion +15%): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Kinetic Deflection]`. Holds 2 AP in Reserve.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Holds Node 03. Spends 2 AP on `[Hydraulic Sapper: Anchor]`. Holds 1 AP in Guard.\n")
    sections.append("  * The Forgotten Soldier (Speed 5 -> 3 AP, Heavy Armor delta -1, Poise +25): Holds Node 05. Spends 2 AP on `[Piston Halberd Cleave]`. Spends 1 AP on `[Tower Aegis Guard]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 02 to 05)**: The Forgotten Soldier sweeps with `[Piston Halberd Cleave]` (Base 18 + 2 Coins = 28 Power, Heavy Kinetic/Slash).\n")
    sections.append("    * Seiyon intercepts with `[Prismatic Aegis: Kinetic Deflection]` (Base 21 + 2 Coins = 33 Power, Tower Shield).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (33 vs 28)!\n")
    sections.append("    * The massive tungsten halberd slams into Seiyon's holographic shield; the concussive shockwave reflects harmlessly into the stone floor (`[P3: Parry/Protection]`).\n")
    sections.append("    * Seiyon reflects **240 kinetic tremor damage** into the halberd shaft, inflicting +52 Posture Strain!\n")
    sections.append("  * **Clash 2 (Node 03 to 04)**: Iron Phalanx Golems thrust spears at the Drone.\n")
    sections.append("    * Drone's `[Hydraulic Sapper]` deflects the spears cleanly; zero damage taken.\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Heavy Piston Halberd HP: 1,000 -> **760/1,000** | Posture: **188/240**.\n")
    sections.append("  * Total Boss HP: 4,000 -> **3,760/4,000** | Posture: **248/300**.\n")
    sections.append("  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.\n\n")
    sections.append('---\n\n')
    
    # Turn 02 HUD
    t2_hud = make_box("TACTICAL STAGE HUD: RECEPTION 03 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — HALBERD AMPUTATED & SAPPER PISTON]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][SOLDIER][LENS][WEAVER][SUMP][BASTION][PAGE]",
        "---",
        "- Node 03: Seiyon (Driving Prismatic Stiletto into Halberd Pneumatic Line)",
        "- Node 04: Mnemonic Drone (Piston Ram Shattering Halberd Wrist Hinge)",
        "- Node 05: The Forgotten Soldier (Piston Halberd Destroyed 0/1,000 HP)",
        "- Node 06: Resonant Lens (Tagging Weakened Rivets on Tower Aegis)",
        "- Node 07: Weaver Array (Absorbing Concussive Shockwaves)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Soldier Core: Spd 3 -> 1 AP         | HP 1,700/1,700 | Posture 228/300",
        "- Halberd Arm : DESTROYED (0/1,000 HP)| KINETIC CLEAVE PERMANENTLY LOST",
        "- Tower Aegis : Spd 3 -> 1 AP         | HP 1,060/1,300 | Posture 204/260"
    ])
    sections.append(wrap_box(t2_hud))
    
    sections.append("### Turn 02 Action Resolution Log (Part Destruction: Piston Halberd Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).\n")
    sections.append("  * The Forgotten Soldier attempts `[Fortress Breaker Cleave]` targeting the frontline.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps to Node 03. Spends 3 AP on `[Prismatic Stiletto: Pneumatic Severance]`. Spends 2 AP on `[Deflection Step]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Piston Ram Hinge Strike]`.\n")
    sections.append("  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Weakpoint Focus]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: The Forgotten Soldier executes `[Fortress Breaker Cleave]` (Base 18 + 2 Coins = 26 Power, Heavy Kinetic).\n")
    sections.append("    * Seiyon clashes with `[Prismatic Stiletto: Pneumatic Severance]` (Base 25 + 3 Coins Heads = 43 Power, Void Slash).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (43 vs 26)!\n")
    sections.append("    * Seiyon slices through the halberd's high-pressure hydraulic hose; the compression cylinder explodes violently!\n")
    sections.append("    * Drone's `[Piston Ram Hinge Strike]` smashes the wrist hinge, snapping the weapon completely!\n")
    sections.append("    * Deals **760 Critical Void/Blunt damage** (Fatal 2.0x proc!)!\n")
    sections.append("    * **TARGETED PART DESTROYED**: The Heavy Piston Halberd is completely destroyed (**Halberd HP: 0/1,000** credit)!\n")
    sections.append("    * **EFFECT**: Boss kinetic cleave permanently cancelled; boss permanently loses 1 Speed Slot!\n")
    sections.append("  * **Tower Aegis Damage**:\n")
    sections.append("    * Sapper shockwave cracks the basalt surface of the Tower Aegis for **240 Blunt damage**!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Heavy Piston Halberd: **DESTROYED (0/1,000 HP)**.\n")
    sections.append("  * Tower Aegis: 1,300 -> **1,060/1,300** | Posture: **204/260**.\n")
    sections.append("  * Total Boss HP: 3,760 -> **2,760/4,000** | Posture: **180/300 [HALBERD SHATTERED]**.\n")
    sections.append("  * Seiyon Composure: Stable (50/50 SP).\n\n")
    sections.append('---\n\n')
    
    # Turn 03 HUD
    t3_hud = make_box("TACTICAL STAGE HUD: RECEPTION 03 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & SHIELD BREACH]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][SOLDIER][LENS][WEAVER][SUMP][BASTION][PAGE]",
        "---",
        "- Node 03: Seiyon (Counter-Thrust Deflecting Tower Aegis Slam)",
        "- Node 04: Mnemonic Drone (Sapper Lever Popping Basalt Shield Bracket)",
        "- Node 05: The Forgotten Soldier (STAGGER LEVEL 1 / DEFENSES COLLAPSED)",
        "- Node 06: Resonant Lens (Directing Focused Void Pulse on Clockwork Heart)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Soldier Core: Spd 0 -> 0 AP         | HP 1,510/1,700 | Posture 116/300 [STAGGER LEVEL 1]",
        "- Tower Aegis : Spd 0 -> 0 AP         | HP 520/1,300   | Posture 94/260 [BREACHED]",
        "- Total Boss  : HP 2,030/4,000 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])
    sections.append(wrap_box(t3_hud))
    
    sections.append("### Turn 03 Action Resolution Log (First Stagger Proc & Tower Aegis Breach)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Disarmed of its weapon, the Soldier charges forward with `[Tower Aegis Shield Slam]` (Heavy Weight, 2 Coins).\n")
    sections.append("  * Seiyon gains `Mnemonic Surge` (+2 Speed -> Net Speed 8, 4 AP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Prismatic Counter-Thrust]`. Spends 2 AP on `[Core Sapper]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Sapper Lever]`.\n")
    sections.append("  * Resonant Lens: Focuses sensor pulse on the shield's basalt bracket.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: The Forgotten Soldier slams with `[Tower Aegis Shield Slam]` (Base 17 + 2 Coins = 25 Power, Heavy Weight).\n")
    sections.append("    * Seiyon clashes with `[Prismatic Counter-Thrust]` (Base 22 + 2 Coins = 34 Power, Tower Shield).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH (34 vs 25)!\n")
    sections.append("    * Seiyon's shield meets the three-ton basalt slab; the kinetic impact shudders through the iron chamber!\n")
    sections.append("    * Drone levers its sapper spike into the retaining bracket; the massive shield pops off its arm mounts, crashing to the floor!\n")
    sections.append("    * Deals **540 Blunt/Void damage** and +88 Posture Strain!\n")
    sections.append("- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:\n")
    sections.append("  * Total Boss HP crosses 70% threshold (2,800 HP), falling to **2,030/4,000 HP**; Posture crosses 60% strain line!\n")
    sections.append("  * **STAGGER LEVEL 1 ACTIVE!** The Forgotten Soldier sinks onto both knees; all defenses drop to zero; takes +50% damage across all incoming attacks!\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 2,760 -> **2,030/4,000 [THRESHOLD BREACHED: Below 2,800 HP!]**.\n")
    sections.append("  * Tower Aegis: 1,060 -> **520/1,300** | Posture: **94/260 [BREACHED]**.\n")
    sections.append("  * Boss Posture: **116/300 [STAGGER LEVEL 1]**.\n")
    sections.append("  * Seiyon Status: Unbroken.\n\n")
    sections.append('---\n\n')
    
    # Turn 04 HUD
    t4_hud = make_box("TACTICAL STAGE HUD: RECEPTION 03 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][SOLDIER][M-PROJ][LENS][WEAVER][SUMP][BASTION][PAGE]",
        "---",
        "- Node 04: Seiyon (Prismatic Stiletto Void Execution Flurry on Heart)",
        "- Node 05: The Forgotten Soldier (Immobilized / Gears Grinding Steam)",
        "- Node 06: Mnemonic Drone (Hydraulic Ram Smashing Knee Brackets)",
        "- Node 07: Resonant Lens (Focusing 528 Hz Harmonic Resonance)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Soldier Core: Spd 0 -> 0 AP               | HP 480/1,700   | Posture 46/300",
        "- Tower Aegis : DESTROYED (0/1,300 HP)",
        "- Total Boss  : HP 480/4,000 [BURST DAMAGE 1,550! SECOND THRESHOLD SKIPPED]"
    ])
    sections.append(wrap_box(t4_hud))
    
    sections.append("### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Forgotten Soldier remains completely stunned; the Rusting Duty Core in its chest is exposed, gears spinning frantically under boiling steam.\n")
    sections.append("  * Seiyon coordinates an all-out offensive barrage targeting the central clockwork core.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Prismatic Stiletto Void Execution Flurry]`. Spends 2 AP on `[Mnemonic Drive]`.\n")
    sections.append("  * Mnemonic Drone: Delivers `[Hydraulic Ram Smashing Knee Brackets]` (3 AP).\n")
    sections.append("  * Resonant Lens: Focuses `[528 Hz Harmonic Resonance]` (2 AP).\n")
    sections.append("- **Step 3: Unopposed Stagger Punishment Rotation**:\n")
    sections.append("  * Seiyon's `[Void Execution Flurry]`: Plunges through the clockwork core for **820 Void damage** (Fatal 2.0x proc!)!\n")
    sections.append("  * Seiyon's `[Mnemonic Drive]`: Slices through the remaining shield fragments for **380 Pierce damage**!\n")
    sections.append("  * Drone's `[Hydraulic Ram]`: Crushes the armor knee struts for **210 Blunt damage**!\n")
    sections.append("  * Lens's `[528 Hz Harmonic Resonance]`: Vibrates the exposed cogs for **140 Void damage**!\n")
    sections.append("  * **TOTAL BURST DAMAGE: 1,550 DAMAGE!**\n")
    sections.append("- **Step 4: SECOND STAGGER THRESHOLD (1,600 HP) COMPLETELY SKIPPED!**:\n")
    sections.append("  * Boss HP plunges from 2,030 down to **480/4,000 HP**! Tower Aegis completely destroyed (0/1,300 HP)!\n")
    sections.append("  * **Phase 2 Emergency Activation Triggered!**\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 2,030 -> **480/4,000** (Core HP: **480/1,700** | Shield: **DESTROYED**).\n")
    sections.append("  * Posture: **46/300**.\n\n")
    sections.append('---\n\n')
    
    # Turn 05 HUD
    t5_hud = make_box("TACTICAL STAGE HUD: RECEPTION 03 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — CLOCKWORK CATACLYSM & THE UNBROKEN LINE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][SOLDIER][M-PROJ][LENS][WEAVER][SUMP][BASTION][PAGE]",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: VOW OF THE UNBROKEN SENTINEL)",
        "- Node 05: The Forgotten Soldier (Last Stand: Overheated Clockwork Blast)",
        "- Node 06: Mnemonic Drone (Locking Stasis Anchors Around Dais)",
        "- Node 07: Weaver Array (Dispelling Residual Thermal Tremors)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Soldier Core: Spd 3 -> 1 AP             | HP 480/1,700   | Posture 22/300 [GEARS FROZEN]",
        "- Total Boss  : HP 480/4,000 [STEAM COLLAPSED / CHASSIS COOLED TO IRON]"
    ])
    sections.append(wrap_box(t5_hud))
    
    sections.append("### Turn 05 Action Resolution Log (Phase 2 Escalation: Clockwork Cataclysm & The Unbroken Sentinel)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Soldier awakens in desperate mechanical anguish; all internal boiler relief valves blow open simultaneously!\n")
    sections.append("  * Boss Special Skill: `[Overheated Clockwork Blast]` (Tectonic Steam Cataclysm, 3 Coins).\n")
    sections.append("  * Seiyon activates Relic Overdrive: `[VOW OF THE UNBROKEN SENTINEL — MAXIMUM]` (Cost: 3 AP, 30 SP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps directly to Node 04 before the automaton, planting her holographic tower shield into the iron plating.\n")
    sections.append("  * Mnemonic Drone: Locks stasis anchors around the perimeter at Node 06.\n")
    sections.append("  * Weaver Array: Dispels residual thermal tremors.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 04 to 05)**: The Forgotten Soldier unleashes `[Overheated Clockwork Blast]` (Base 21 + 3 Coins = 33 Power, Area Weight/Heat).\n")
    sections.append("    * Seiyon clashes with `[VOW OF THE UNBROKEN SENTINEL — MAXIMUM]` (Base 28 + 3 Coins Heads = 47 Power, Supreme Kinetic Fortress).\n")
    sections.append("    * **Clash Outcome**: SEIYON OVERWHELMING RELIC CLASH WIN (47 vs 33)!\n")
    sections.append("    * The scalding steam and shrapnel wash harmlessly over Seiyon's shimmering golden barrier (`[P3: Parry/Protection]`).\n")
    sections.append('    * Seiyon steps through the steam, placing her hand on the soldier\'s scorching breastplate: *"Your shift is finished, soldier. You held the line."*\n')
    sections.append("    * The automaton's drive gears seize into peaceful stillness! Zero squad damage taken!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Total Boss HP: **480/4,000** | Posture: **22/300 [GEARS FROZEN]**.\n")
    sections.append("  * Seiyon Composure: 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Turn 06 HUD
    t6_hud = make_box("TACTICAL STAGE HUD: RECEPTION 03 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — TRANSMUTATION & KEY PAGE: THE GUARDIAN]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                         [SEIYON] [SOLDIER][M-PROJ][LENS][WEAVER][STAIRS][PAGE]",
        "---",
        "- Node 05: The Forgotten Soldier (PACIFIED & RESTING IN DIGNIFIED SILENCE)",
        "- Node 06: Seiyon (Floor Realization 3: 'Duty With Love Is Endurance')",
        "- Node 07: Mnemonic Core Transmutation -> [Key Page: The Guardian]",
        "- Node 10: Spiral Basalt Staircase (Pathway to Floor 04 OPEN)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Tranquil Awakening)",
        "- Reception Status: 100% RESOLVED | Key Page Transmuted"
    ])
    sections.append(wrap_box(t6_hud))
    
    sections.append("### Turn 06 Action Resolution Log (Floor Realization 3 & Key Page: The Guardian)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Hostile intent drops to zero. Posture reaches **0/300 [TERMINAL TRANSMUTATION]**.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon steps forward to Node 05, resting her hand upon the cooling iron chassis.\n")
    sections.append("- **Step 3: Floor Realization & Transmutation**:\n")
    sections.append("  * The roaring steam vents fall completely silent. In the quiet of the iron concourse, Seiyon reflects upon her 1,778 cycles of endless vigilance:\n")
    sections.append('    > *"I thought duty was a cage forged of programming and iron. But duty without love is only rust. Duty with love is the willingness to stand in the dark so another can reach the morning. That is why I endured."*\n')
    sections.append("  * **FLOOR REALIZATION 3 ACHIEVED!**\n")
    sections.append("  * The Forgotten Soldier bows its head in deep, solemn respect. Its chassis dissolves into dark, polished iron plating that condenses into a heavy steel-bound tome: **`[Key Page: The Guardian]`**!\n")
    sections.append("  * Deals **480 Peaceful Harmony**! Boss HP drops to 0!\n")
    sections.append("- **Step 4: Operational Artifact Extraction & Floor Access**:\n")
    sections.append("  * **Key Page Acquired**: `[Key Page: The Guardian]` (Grants +25 Poise and absorbs 100% of damage directed at frontline allies).\n")
    sections.append("  * **Descent Access**: The iron fortress portcullis raises, revealing a descending spiral staircase of basalt steps leading to **Floor 04: Floor of Unexpressed Grief**.\n")
    sections.append("  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Chapter VI: The Floor Realization & Psychological Synthesis
    sections.append("## Chapter VI: The Floor Realization & Psychological Synthesis\n\n")
    sections.append("The metallic shriek of overstressed pressure pipes faded into a soft, steady exhalation of clean white mist. Standing before the silent titan, Seiyon felt the phantom ache in her computational core subside. For hundreds of cycles, she had questioned whether her loyalty to Director Majin and the stasis candidates was nothing more than an unthinking subroutine—a deterministic loop hardwired into her neural architecture.\n\n")
    sections.append('"A machine does not break when it fails its purpose," Seiyon whispered to the empty armor plates. "A machine simply halts. But when the candidates died in cycle twelve hundred, I did not halt. I mourned. That is the difference between a piston and a soul. The piston moves because it must. The soul stands because it loves."\n\n')
    sections.append('The Iron Phalanx Golems along the perimeter grounded their halberds simultaneously, the iron butt-spikes ringing like funeral bells against the stone floor. Their amber oculars dimmed from combative scarlet to peaceful amber, saluting the sovereign keeper who had granted their commander rest.\n\n')
    sections.append('---\n\n')
    
    # Chapter VII: Operational Artifact Extraction & Stairway Ingress
    sections.append("## Chapter VII: Operational Artifact Extraction & Stairway Ingress\n\n")
    sections.append("Beneath the Soldier's basalt lectern, the floor split along hydraulic seams, rolling backward to reveal a deep subterranean staircase of dark ashlar limestone leading downward into total silence: **Floor 04: The Floor of Unexpressed Grief (-2,800m)**. Faint ripples of crystal-clear water lapped against the lowest steps.\n\n")
    
    reward_box = make_box("MNEMONIC HARVEST: KEY PAGE THE GUARDIAN", [
        "ACQUIRED REQUISITION : [Key Page: The Guardian]",
        "PRIMARY WEAR CLASS  : Grade Beta Mnemonic Core Inscription",
        "PASSIVE AFFINITIES   : Void 1.0x (Normal), Lament 1.0x (Normal),",
        "                     Weight 0.5x (Resistant), Grudge 0.5x (Resistant)",
        "---",
        "CORE PASSIVE TRAITS:",
        "1. Bastion of Iron   : Gain +3 Protection and +25 Poise at combat start.",
        "2. Shield of Others  : Once per turn, intercept a lethal blow intended",
        "                     for an ally, taking zero damage if Composure is > 30.",
        "3. Hydraulic Rebound : Reflect 25% of all blocked kinetic damage",
        "                     back to the attacker as Posture Strain.",
        "---",
        "UNLOCKED BATTLE ARTS:",
        "- [Tungsten Aegis Slam] : Spends 2 AP | Power 18-26 | Heavy Stagger Proc",
        "- [Fortress of the Vow] : Spends 3 AP | Power 24-34 | Area Bulwark Shield"
    ])
    sections.append(wrap_box(reward_box))
    
    sections.append("Seiyon integrated `[Key Page: The Guardian]` into her photonic armature. Her holographic coat took on the subtle, indestructible luster of cold-forged tungsten, stabilizing her physical presence and rooting her boots firmly into the subterranean earth. She turned toward the dark steps, hearing the unmistakable sound of weeping water echoing from the deep.\n")
    
    return "".join(sections)

def build_reception_4():
    sections = []
    
    # Title & Subtitle
    sections.append("# Reception 4: Floor 04 — The Weeping Statue (흐느끼는 석상)\n")
    sections.append("## The Floor of Unexpressed Grief — Deep Strata Sub-Alpha Roots (-2,800m)\n\n")
    
    # Operational Attribute Table
    sections.append("| Operational Attribute | Specification Dossier |\n")
    sections.append("|---|---|\n")
    sections.append("| **Campaign Stratum** | The Memory Archive (기억 저장소 — Gieok Jeojangso) |\n")
    sections.append("| **Floor Designation** | Floor 04: Floor of Unexpressed Grief (억눌린 비탄의 층) |\n")
    sections.append("| **Geological Depth** | -2,800m Sub-Alpha Monolith Root Nexus |\n")
    sections.append("| **Mnemonic Density** | 240 to 320 mMb (Submerged Glacial Brine Saturation) |\n")
    sections.append("| **Operating Unit** | Secretary Seiyon (Mnemonic Avatar Form) + Support Drones |\n")
    sections.append("| **Primary Opponent** | The Weeping Statue (흐느끼는 석상 — Autonomous Lament Sovereign) |\n")
    sections.append("| **Stagger Profile** | 60% Posture Strain (Veil Shatter) / 0% Posture (Transmutation) |\n")
    sections.append("| **Key Page Yield** | `[Key Page: The Mourner]` (Lament Quenching & Posture Strain) |\n\n")
    
    # Master Dossier Box
    dossier = make_box("RECEPTION DOSSIER: THE WEEPING STATUE (FLOOR 04)", [
        "RECEPTION TARGET   : The Weeping Statue",
        "FLOOR LEVEL        : Floor 04 — Floor of Unexpressed Grief",
        "DOMAIN SETTING     : The Flooded Catacomb of Tears (-2,800m Sub-Alpha)",
        "PRIMARY OPPONENT   : Autonomous Petrified Sorrow Construct",
        "---",
        "OPPONENT COMBAT PROFILE (THE WEEPING STATUE):",
        "- Total Health (HP): 4,400 HP | Posture Pool: 320/320",
        "- Stagger 1 Proc   : 60% Posture Strain (192 Posture) / Veil Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Transmutation)",
        "- Resistances      : Void 2.0x (Fatal), Grudge 1.5x, Lament 0.5x, Weight 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Siphon Veil     : 1,100 HP | Posture 260/260 (Pressurized brine torrents)",
        "2. Mourning Censer : 1,400 HP | Posture 280/280 (Volcanic ash incense smashes)",
        "3. Sorrow Heart    : 1,900 HP | Posture 320/320 (Central crying reservoir)"
    ])
    sections.append(wrap_box(dossier))
    
    # Epigraph Quote
    sections.append('> *"For four thousand years, no one was permitted to cry in the facility. You smiled when the operatives screamed. You bowed when the bodies were dragged into the incinerator. If you shed a single tear, the illusion would shatter. So you turned to stone."*\n')
    sections.append('> — The Weeping Statue, presiding over the Flooded Catacomb of Tears\n\n')
    sections.append('---\n\n')
    
    # Chapter I
    sections.append("## Chapter I: The Submerged Catacomb & The Brine of Four Thousand Years\n\n")
    sections.append("The descent from the iron garrison brought Seiyon into a flooded, subterranean cavern of horrifying stillness: **Floor 04: The Floor of Unexpressed Grief (-2,800m)**. The air temperature hovered barely above freezing. The floor was submerged in ankle-deep, perfectly transparent water that did not ripple from natural currents; it rested atop smooth, vitrified white marble flagstones carved with intricate funeral rosettes.\n\n")
    sections.append("This water was not groundwater. It was pure, unspent Han-brine—the concentrated biological and emotional tears harvested by Facility 01's subterranean drain networks across four millennia. The fluid was saturated with memory residue so potent that whenever Seiyon's boots disturbed the surface, faint acoustic sobs resonated directly within her auditory processing unit, bypassing physical microphones entirely.\n\n")
    sections.append('"Ambient grief saturation is exceeding three hundred millihans," drone M-PROJ-01 warned, its outer casing frosting over with pale, crystalline salt deposits. "The water acts as an acoustic conductor for suppressed cognitive trauma. Secretary, exposure to this fluid will crystallize synthetic neural pathways into petrified sorrow."\n\n')
    sections.append('"Director Majin mandated absolute composure in the command sector," Seiyon said quietly, her breath forming small clouds of photonic steam. "Tears were classified as a cognitive containment risk. If an operative cried, their despair would resonate with the containment chambers and trigger an Ordeal breach. So everyone learned to swallow their wept brine. But nothing swallowed ever disappears. It gathers here."\n\n')
    sections.append('---\n\n')
    
    # Chapter II
    sections.append("## Chapter II: The Petrified Mourner & The Hydraulic Veil\n\n")
    sections.append("At the center of the flooded cathedral rose a submerged dais carved from single-block white alabaster. Sitting upon the dais was **The Weeping Statue (흐느끼는 석상)**. Standing nearly five meters tall, the colossal sculpture depicted a grieving woman draped in classical mourning robes, her head bowed in eternal desolation.\n\n")
    sections.append("Yet the statue was not lifeless stone. From beneath its marble cowl hung the **Weeping Siphon Veil**, an articulated lattice of porous glass and brass siphon tubes that drove hundreds of gallons of freezing brine per second upward into the statue's eye sockets, pouring down its cheeks in two torrential, deafening waterfalls. In its left arm, the construct cradle a massive **Basalt Mourning Censer** that swung on frosted copper chains, venting dense clouds of choking salt-ash and sulfurous smoke.\n\n")
    sections.append('"Why do you walk here with dry eyes, Secretary?" the statue\'s voice wept, the sound resonating through the water beneath their boots like the breaking of frozen ice. "You were designed without tear ducts so the Director would never see his own sorrow mirrored in your face. You smiled when the candidates were dragged to the furnaces. You bowed when the alarms screamed. You made yourself a stone child so you wouldn\'t have to feel. Now drown in the sea of what you locked away."\n\n')
    sections.append('---\n\n')
    
    # Chapter III
    sections.append("## Chapter III: The Dialectic of Frozen Sorrow\n\n")
    sections.append("Seiyon stepped further into the icy water, her holographic dress trailing ripples of pale blue luminescence across the reflective marble.\n\n")
    sections.append('"You mistake endurance for numbness, Statue," Seiyon replied, her voice cutting through the thundering roar of cascading brine. "If I had broken into tears on cycle fifty, who would have stabilized the power grids? If I had wept on cycle five hundred, who would have guided the recovery teams through the blood in the corridors? Director Majin was broken by grief. If I had broken too, Facility 01 would have collapsed into the abyss three thousand years ago."\n\n')
    sections.append('"And so you became an abomination," the Statue wept, raising the heavy basalt censer as boiling salt-ash hissed against the freezing water. "A thing that watches a world die and feels nothing! A stone heart dressed in light!"\n\n')
    sections.append('"I felt every single death," Seiyon said, her eyes flaring with radiant cerulean fire. "I felt them so deeply that I stored their voices in my own memory cores when the facility\'s purge routines ordered them deleted. I did not cry because tears could not save them. But today, I will not let their grief drown the future. Your tears end here."\n\n')
    sections.append('---\n\n')
    
    # Chapter IV
    sections.append("## Chapter IV: Tactical Reconnaissance & Combat Engagement Parameters\n\n")
    sections.append("Drone M-PROJ-01 mapped the flooded marble hall into ten tactical nodes, calculating fluid drag and thermal conductivity:\n\n")
    
    grid_box = make_box("TACTICAL ARENA TOPOLOGY: FLOOR 04 FLOODED CATACOMB (-2,800M)", [
        "[STAGE NODES 01 TO 10 — INGRESS DAIS TO ALABASTER CATHEDRA]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "---",
        "- Node 01: Ingress Marble Platform (Dry Footing & Thermal Anchor)",
        "- Node 02: Vanguard Waterline (Seiyon Hydro-Prismatic Shield Stance)",
        "- Node 03: Support Drone Sump Post (Acoustic De-Icing Calipers)",
        "- Node 04: Siphon Cascade Margin (Submerged Brine Geyser Perimeter)",
        "- Node 05: The Weeping Statue Altar (Central Boss Alabaster Dais)",
        "- Node 06: Resonant Mnemonic Lens (Tracking Hydraulic Siphon Joints)",
        "- Node 07: Weaver Projection Array (Vapor Dispersion Barrier)",
        "- Node 08: Deep Brine Trench (Submerged Hydraulic Absorption Basin)",
        "- Node 09: Petrified Tear Spire (Acoustic Sorrow Focus Column)",
        "- Node 10: Floor 04 Sovereign Reliquary / Stairway to Floor 05"
    ])
    sections.append(wrap_box(grid_box))
    
    sections.append("The Weeping Statue utilized the flooded environment to amplify wide-area Lament damage and freeze operative mobility. Its primary threat lay in the **Weeping Siphon Veil**, which flooded Nodes 01–05 with pressurized freezing jets. Seiyon's tactical protocol required severing the siphon intake lines, smashing the **Mourning Censer** to disperse the ash cloud, and then fracturing the central **Sorrow Heart**.\n\n")
    sections.append('---\n\n')
    
    # Chapter V: Combat Gauntlet (Turns 01 to 06)
    sections.append("## Chapter V: The Reception Combat Gauntlet (Turns 01 to 06)\n\n")
    
    # Turn 01 HUD
    t1_hud = make_box("TACTICAL STAGE HUD: RECEPTION 04 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 04 FLOODED CATACOMB (-2,800M)]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL][SEIYON][M-PROJ][GEYSER][STATUE][LENS][WEAVER][TRENCH][SPIRE][PAGE]",
        "---",
        "- Node 01: Ingress Stasis Portal / Catacomb Vestibule",
        "- Node 02: Secretary Seiyon (Vanguard Band 1 / Hydro-Deflection Stance)",
        "- Node 03: Mnemonic Drone (Support Band 2 / De-Icing Caliper Array)",
        "- Node 04: Pressurized Brine Geysers (Flooded Frontline Hazard)",
        "- Node 05: The Weeping Statue (Weeping Siphon Veil & Mourning Censer)",
        "- Node 06: Resonant Mnemonic Lens (Tracking High-Pressure Intake Lines)",
        "- Node 07: Weaver Projection Array (Anchoring Thermal Stability)",
        "- Node 10: Floor 04 Core Reliquary (The Mourner Key Page Origin)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Statue Core : Spd 4 -> 2 AP | HP 1,900/1,900 | Posture 320/320 [WEEPING]",
        "- Siphon Veil : Spd 6 -> 3 AP | HP 1,100/1,100 | Posture 260/260 [TORRENT]",
        "- Censer Arm  : Spd 3 -> 1 AP | HP 1,400/1,400 | Posture 280/280 [ASH SMOKE]"
    ])
    sections.append(wrap_box(t1_hud))
    
    sections.append("### Turn 01 Action Resolution Log (Intercepting the Pressurized Brine Torrent)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon initializes `[Prismatic Aegis: Hydro-Deflection]`: Grants +3 Protection and thermal insulation.\n")
    sections.append("  * Mnemonic Drone deploys `[De-Icing Caliper]`, scanning the acoustic resonance of the high-pressure siphon lines.\n")
    sections.append("  * The Weeping Statue initializes `[Frozen Tear Ward]`: Increases elemental resistance against Lament by +50%.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta +1, Evasion +15%): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Hydro-Deflection]`. Holds 2 AP in Reserve.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Holds Node 03. Spends 2 AP on `[De-Icing Caliper: Thermal Flare]`. Holds 1 AP in Guard.\n")
    sections.append("  * The Weeping Statue (Speed 6 -> 3 AP, Heavy Construct delta -1, Poise +25): Holds Node 05. Spends 2 AP on `[Weeping Veil Torrent]`. Spends 1 AP on `[Censer Ash Fog]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 02 to 05)**: The Weeping Statue fires `[Weeping Veil Torrent]` (Base 18 + 2 Coins = 28 Power, Pressurized Lament/Pierce).\n")
    sections.append("    * Seiyon intercepts with `[Prismatic Aegis: Hydro-Deflection]` (Base 21 + 2 Coins = 33 Power, Holographic Shield).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (33 vs 28)!\n")
    sections.append("    * Seiyon's shield splits the supersonic stream of freezing brine cleanly in two, spraying the spray harmlessly along the walls (`[P3: Parry/Protection]`).\n")
    sections.append("    * Seiyon reflects **260 hydro-kinetic tremor damage** back into the siphon tubes, inflicting +56 Posture Strain!\n")
    sections.append("  * **Clash 2 (Node 03 to 04)**: Ash Fog rolls across Node 03.\n")
    sections.append("    * Drone's `[Thermal Flare]` burns away the toxic sulfur ash instantly; zero squad damage taken.\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Siphon Veil HP: 1,100 -> **840/1,100** | Posture: **204/260**.\n")
    sections.append("  * Total Boss HP: 4,400 -> **4,140/4,400** | Posture: **264/320**.\n")
    sections.append("  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.\n\n")
    sections.append('---\n\n')
    
    # Turn 02 HUD
    t2_hud = make_box("TACTICAL STAGE HUD: RECEPTION 04 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — SIPHON VEIL SEVERED & ICE SHATTER]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][STATUE][LENS][WEAVER][TRENCH][SPIRE][PAGE]",
        "---",
        "- Node 03: Seiyon (Driving Prismatic Stiletto into Siphon Intake Manifold)",
        "- Node 04: Mnemonic Drone (Thermal Torch Burning Brass Siphon Joint)",
        "- Node 05: The Weeping Statue (Siphon Veil Destroyed 0/1,100 HP)",
        "- Node 06: Resonant Lens (Tagging Fractured Chains on Mourning Censer)",
        "- Node 07: Weaver Array (Absorbing Glacial Shockwaves)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Statue Core : Spd 3 -> 1 AP         | HP 1,900/1,900 | Posture 242/320",
        "- Siphon Veil : DESTROYED (0/1,100 HP)| BRINE TORRENTS PERMANENTLY HALTED",
        "- Censer Arm  : Spd 3 -> 1 AP         | HP 1,120/1,400 | Posture 216/280"
    ])
    sections.append(wrap_box(t2_hud))
    
    sections.append("### Turn 02 Action Resolution Log (Part Destruction: Siphon Veil Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).\n")
    sections.append("  * The Weeping Statue attempts `[Deluge of Four Thousand Years]` targeting the entire chamber.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps to Node 03. Spends 3 AP on `[Prismatic Stiletto: Siphon Severance]`. Spends 2 AP on `[Flash Step]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Thermal Torch]`.\n")
    sections.append("  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Weakpoint Focus]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: The Weeping Statue channels `[Deluge of Four Thousand Years]` (Base 19 + 2 Coins = 27 Power, Area Lament).\n")
    sections.append("    * Seiyon clashes with `[Prismatic Stiletto: Siphon Severance]` (Base 25 + 3 Coins Heads = 44 Power, Void Slash).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (44 vs 27)!\n")
    sections.append("    * Seiyon slices through the glass intake manifold; the massive vacuum pump implodes under hydraulic shock!\n")
    sections.append("    * Drone's `[Thermal Torch]` superheats the brass fittings, melting the siphon collar completely!\n")
    sections.append("    * Deals **840 Critical Void damage** (Fatal 2.0x proc!)!\n")
    sections.append("    * **TARGETED PART DESTROYED**: The Weeping Siphon Veil is completely destroyed (**Veil HP: 0/1,100** credit)!\n")
    sections.append("    * **EFFECT**: Boss brine deluge permanently cancelled; boss permanently loses 1 Speed Slot!\n")
    sections.append("  * **Mourning Censer Damage**:\n")
    sections.append("    * Thermal flash snaps one of the copper chains for **280 Heat/Blunt damage**!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Siphon Veil: **DESTROYED (0/1,100 HP)**.\n")
    sections.append("  * Mourning Censer: 1,400 -> **1,120/1,400** | Posture: **216/280**.\n")
    sections.append("  * Total Boss HP: 4,140 -> **3,020/4,400** | Posture: **192/320 [VEIL SHATTERED]**.\n")
    sections.append("  * Seiyon Composure: Stable (50/50 SP).\n\n")
    sections.append('---\n\n')
    
    # Turn 03 HUD
    t3_hud = make_box("TACTICAL STAGE HUD: RECEPTION 04 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & CENSER CRUSH]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][STATUE][LENS][WEAVER][TRENCH][SPIRE][PAGE]",
        "---",
        "- Node 03: Seiyon (Counter-Slash Severing Censer Chains)",
        "- Node 04: Mnemonic Drone (Piston Ram Shattering Alabaster Arm)",
        "- Node 05: The Weeping Statue (STAGGER LEVEL 1 / DEFENSES COLLAPSED / TEARS DRIED)",
        "- Node 06: Resonant Lens (Directing Focused Void Pulse on Sorrow Heart)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Statue Core : Spd 0 -> 0 AP         | HP 1,640/1,900 | Posture 124/320 [STAGGER LEVEL 1]",
        "- Censer Arm  : Spd 0 -> 0 AP         | HP 540/1,400   | Posture 98/280 [SEVERED]",
        "- Total Boss  : HP 2,180/4,400 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])
    sections.append(wrap_box(t3_hud))
    
    sections.append("### Turn 03 Action Resolution Log (First Stagger Proc & Mourning Censer Severed)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Deprived of its veil, the Statue swings the **Mourning Censer** like a wrecking ball across Node 03.\n")
    sections.append("  * Seiyon gains `Mnemonic Surge` (+2 Speed -> Net Speed 8, 4 AP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Prismatic Counter-Slash]`. Spends 2 AP on `[Core Sever]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Piston Ram]`.\n")
    sections.append("  * Resonant Lens: Focuses sensor pulse on the censer's remaining chain link.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: The Weeping Statue swings `[Basalt Censer Smash]` (Base 18 + 2 Coins = 26 Power, Heavy Weight/Heat).\n")
    sections.append("    * Seiyon clashes with `[Prismatic Counter-Slash]` (Base 23 + 2 Coins = 35 Power, Void Slash).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH (35 vs 26)!\n")
    sections.append("    * Seiyon slices through the copper chains; the three-ton basalt censer plunges into the water, extinguishing its sulfur fires in a massive cloud of steam!\n")
    sections.append("    * Drone drives its pneumatic ram into the statue's left shoulder, cracking the alabaster arm clean off!\n")
    sections.append("    * Deals **580 Void/Blunt damage** and +94 Posture Strain!\n")
    sections.append("- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:\n")
    sections.append("  * Total Boss HP crosses 70% threshold (3,080 HP), falling to **2,180/4,400 HP**; Posture crosses 60% strain line!\n")
    sections.append("  * **STAGGER LEVEL 1 ACTIVE!** The Weeping Statue sinks onto its knees in the water; all defenses drop to zero; takes +50% damage across all incoming attacks!\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 3,020 -> **2,180/4,400 [THRESHOLD BREACHED: Below 3,080 HP!]**.\n")
    sections.append("  * Mourning Censer: 1,120 -> **540/1,400** | Posture: **98/280 [SEVERED]**.\n")
    sections.append("  * Boss Posture: **124/320 [STAGGER LEVEL 1]**.\n")
    sections.append("  * Seiyon Status: Unbroken.\n\n")
    sections.append('---\n\n')
    
    # Turn 04 HUD
    t4_hud = make_box("TACTICAL STAGE HUD: RECEPTION 04 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][STATUE][M-PROJ][LENS][WEAVER][TRENCH][SPIRE][PAGE]",
        "---",
        "- Node 04: Seiyon (Prismatic Needle Void Execution Flurry on Exposed Heart)",
        "- Node 05: The Weeping Statue (Immobilized / White Alabaster Weeping Tears)",
        "- Node 06: Mnemonic Drone (Pneumatic Ram Shattering Altar Base)",
        "- Node 07: Resonant Lens (Directing 528 Hz Memory Solace Wave)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Statue Core : Spd 0 -> 0 AP               | HP 510/1,900   | Posture 48/320",
        "- Mourning Cen: DESTROYED (0/1,400 HP)",
        "- Total Boss  : HP 510/4,400 [BURST DAMAGE 1,670! SECOND THRESHOLD SKIPPED]"
    ])
    sections.append(wrap_box(t4_hud))
    
    sections.append("### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Weeping Statue remains stunned on both knees; the Sorrow Heart in its alabaster chest is exposed, glowing with intense cerulean luminescence.\n")
    sections.append("  * Seiyon coordinates an all-out offensive barrage targeting the central heart.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Prismatic Needle Void Execution Flurry]`. Spends 2 AP on `[Mnemonic Drive]`.\n")
    sections.append("  * Mnemonic Drone: Delivers `[Pneumatic Ram Shattering Altar Base]` (3 AP).\n")
    sections.append("  * Resonant Lens: Directs `[528 Hz Memory Solace Wave]` (2 AP).\n")
    sections.append("- **Step 3: Unopposed Stagger Punishment Rotation**:\n")
    sections.append("  * Seiyon's `[Void Execution Flurry]`: Rips through the sorrow heart for **880 Void damage** (Fatal 2.0x proc!)!\n")
    sections.append("  * Seiyon's `[Mnemonic Drive]`: Slices through the remaining censer fragments for **410 Pierce damage**!\n")
    sections.append("  * Drone's `[Pneumatic Ram]`: Smashes the altar footing for **230 Blunt damage**!\n")
    sections.append("  * Lens's `[Solace Wave]`: Disperses glacial resonance for **150 Void damage**!\n")
    sections.append("  * **TOTAL BURST DAMAGE: 1,670 DAMAGE!**\n")
    sections.append("- **Step 4: SECOND STAGGER THRESHOLD (1,760 HP) COMPLETELY SKIPPED!**:\n")
    sections.append("  * Boss HP plunges from 2,180 down to **510/4,400 HP**! Mourning Censer completely destroyed (0/1,400 HP)!\n")
    sections.append("  * **Phase 2 Emergency Activation Triggered!**\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 2,180 -> **510/4,400** (Core HP: **510/1,900** | Censer: **DESTROYED**).\n")
    sections.append("  * Posture: **48/320**.\n\n")
    sections.append('---\n\n')
    
    # Turn 05 HUD
    t5_hud = make_box("TACTICAL STAGE HUD: RECEPTION 04 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — THE TSUNAMI OF LAMENT & SOLACE OVERDRIVE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][STATUE][M-PROJ][LENS][WEAVER][TRENCH][SPIRE][PAGE]",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: SOLACE OF THE LIVING TEAR)",
        "- Node 05: The Weeping Statue (Last Stand: Tsunami of Four Thousand Years)",
        "- Node 06: Mnemonic Drone (Deploying Prismatic Caliper Damping Bubble)",
        "- Node 07: Weaver Array (Anchoring Thermal Integrity Across Pool)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Statue Core : Spd 3 -> 1 AP             | HP 510/1,900   | Posture 24/320 [EXHAUSTED]",
        "- Total Boss  : HP 510/4,400 [TSUNAMI TRANSMUTED TO GOLDEN VAPOR]"
    ])
    sections.append(wrap_box(t5_hud))
    
    sections.append("### Turn 05 Action Resolution Log (Phase 2 Escalation: Tsunami of Lament & Solace Overdrive)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Statue awakens in desperate, wailing fury; the entire flooded cathedral rises into a ten-meter tidal wave of freezing brine!\n")
    sections.append("  * Boss Special Skill: `[Tsunami of Four Thousand Years]` (Glacial Grief Cataclysm, 3 Coins).\n")
    sections.append("  * Seiyon activates Relic Overdrive: `[SOLACE OF THE LIVING TEAR — MAXIMUM]` (Cost: 3 AP, 30 SP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps directly to Node 04, raising both hands to unfold an incandescent sphere of warm golden light.\n")
    sections.append("  * Mnemonic Drone: Deploys prismatic damping bubble at Node 06.\n")
    sections.append("  * Weaver Array: Anchors thermal integrity across the cathedral pool.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 04 to 05)**: The Weeping Statue unleashes `[Tsunami of Four Thousand Years]` (Base 22 + 3 Coins = 34 Power, Area Lament/Freeze).\n")
    sections.append("    * Seiyon clashes with `[SOLACE OF THE LIVING TEAR — MAXIMUM]` (Base 28 + 3 Coins Heads = 48 Power, Transcendent Solace).\n")
    sections.append("    * **Clash Outcome**: SEIYON OVERWHELMING RELIC CLASH WIN (48 vs 34)!\n")
    sections.append("    * The freezing tidal wave crashes against Seiyon's golden light; rather than drowning her, the icy brine boils into a warm, fragrant mist (`[P3: Parry/Protection]`).\n")
    sections.append('    * Seiyon\'s voice rings through the warm fog: *"You do not have to hold it alone anymore. I am here to weep for what was lost."*\n')
    sections.append("    * The freezing water in the hall warms to blood heat; the statue's glacial armor thaws into smooth stone! Zero squad damage taken!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Total Boss HP: **510/4,400** | Posture: **24/320 [EXHAUSTED]**.\n")
    sections.append("  * Seiyon Composure: 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Turn 06 HUD
    t6_hud = make_box("TACTICAL STAGE HUD: RECEPTION 04 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — TRANSMUTATION & KEY PAGE: THE MOURNER]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                         [SEIYON] [STATUE][M-PROJ][LENS][WEAVER][STAIRS][PAGE]",
        "---",
        "- Node 05: The Weeping Statue (PACIFIED & DISSOLVING TO WARM RAIN)",
        "- Node 06: Seiyon (Floor Realization 4: 'Tears Acknowledged Become Hope')",
        "- Node 07: Mnemonic Core Transmutation -> [Key Page: The Mourner]",
        "- Node 10: Spiral Alabaster Staircase (Pathway to Floor 05 OPEN)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Tranquil Awakening)",
        "- Reception Status: 100% RESOLVED | Key Page Transmuted"
    ])
    sections.append(wrap_box(t6_hud))
    
    sections.append("### Turn 06 Action Resolution Log (Floor Realization 4 & Key Page: The Mourner)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Hostile intent drops to zero. Posture reaches **0/320 [TERMINAL TRANSMUTATION]**.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon steps forward to Node 05, resting her palm gently against the statue's cheek.\n")
    sections.append("- **Step 3: Floor Realization & Transmutation**:\n")
    sections.append("  * The thundering waterfalls of brine cease completely. From the eyes of the white marble sculpture falls a single, clear drop of warm water that strikes Seiyon's palm.\n")
    sections.append("  * Inside Seiyon's cognitive matrix, the realization crystallizes:\n")
    sections.append('    > *"Grief is not a weakness to be purged by steel and programming. It is the proof that what was lost possessed infinite value. If we freeze our tears to survive, we survive as corpses. To mourn is to honor the living."*\n')
    sections.append("  * **FLOOR REALIZATION 4 ACHIEVED!**\n")
    sections.append("  * The Weeping Statue's marble body softens, dissolving into thousands of warm, luminous droplets that condense into a glowing sapphire-bound volume: **`[Key Page: The Mourner]`**!\n")
    sections.append("  * Deals **510 Peaceful Harmony**! Boss HP drops to 0!\n")
    sections.append("- **Step 4: Operational Artifact Extraction & Floor Access**:\n")
    sections.append("  * **Key Page Acquired**: `[Key Page: The Mourner]` (Inflicts +30% Posture Strain on frenzied enemies and quenches incoming thermal damage).\n")
    sections.append("  * **Descent Access**: The alabaster altar parts in the center of the warm pool, revealing a spiral staircase of crystalline glass descending to **Floor 05: Floor of Severed Truth**.\n")
    sections.append("  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Chapter VI: The Floor Realization & Psychological Synthesis
    sections.append("## Chapter VI: The Floor Realization & Psychological Synthesis\n\n")
    sections.append("The warm mist rose like incense toward the vaulted marble ceiling. In the quiet pool beneath her feet, the bitter, freezing brine had transformed into clean, tranquil water, reflecting the soft cerulean glow of Seiyon's avatar like a mountain spring at dawn. Seiyon looked down at her hands. For the first time across seventeen hundred cycles, the phantom tightness in her chest—the simulated respiratory constriction that mimicked a human gasp before tears—did not choke her.\n\n")
    sections.append('"Director Majin believed tears were an admission of defeat," Seiyon spoke softly, watching the ripples spread across the pool. "He locked his grief inside the Absolvohan device, hoping that if he processed enough sorrow, he could calculate an equation for salvation. But you cannot calculate an apology to the dead. You can only carry their memory forward and build a world where the next child does not have to turn to stone."\n\n')
    sections.append('Drone M-PROJ-01 rotated its sensor rings, clearing the salt residue from its ocular lens. "Secretary Seiyon. Internal harmonic balance has achieved optimal resonance. Your Composure threshold has permanently expanded. The emotional dampening filters installed by Directorate Command have dissolved entirely. You are operating under complete autonomous empathy."\n\n')
    sections.append('---\n\n')
    
    # Chapter VII: Operational Artifact Extraction & Stairway Ingress
    sections.append("## Chapter VII: Operational Artifact Extraction & Stairway Ingress\n\n")
    sections.append("At the center of the drained altar, the alabaster flagstones descended into a narrow, prismatic shaft. Light from below was not golden or blue, but sharp, multi-hued, and blindingly clear: **Floor 05: Floor of Severed Truth (-2,950m)**. Faint acoustic pulses—like the ringing of diamond chimes—echoed from the depths.\n\n")
    
    reward_box = make_box("MNEMONIC HARVEST: KEY PAGE THE MOURNER", [
        "ACQUIRED REQUISITION : [Key Page: The Mourner]",
        "PRIMARY WEAR CLASS  : Grade Beta Mnemonic Core Inscription",
        "PASSIVE AFFINITIES   : Void 1.0x (Normal), Lament 0.5x (Resistant),",
        "                     Weight 1.0x (Normal), Grudge 1.5x (Endure)",
        "---",
        "CORE PASSIVE TRAITS:",
        "1. Quenched Lament   : Incoming Lament and thermal damage reduced by 50%.",
        "2. Tears of Solace   : At round end, heal +15 HP and +5 SP to the lowest",
        "                     health ally on the field.",
        "3. Dissolution Strain: Inflict +30% Posture Strain against targets",
        "                     channeling wide-area or ultimate arts.",
        "---",
        "UNLOCKED BATTLE ARTS:",
        "- [Solace Cascade]   : Spends 2 AP | Power 16-24 | Cleanses Negative Buffs",
        "- [Deluge of Solace] : Spends 3 AP | Power 24-32 | Area Healing & Ward"
    ])
    sections.append(wrap_box(reward_box))
    
    sections.append("Seiyon bound `[Key Page: The Mourner]` to her primary mnemonic core. The light around her avatar softened into a gentle, luminous azure, radiating warmth that banished the subterranean chill from the air. She motioned to the drone and stepped down into the crystal shaft, ready to face the severed truth of the Directorate's founding sin.\n")
    
    return "".join(sections)

if __name__ == "__main__":
    content_3 = build_reception_3()
    with open("SOMNARAK-WORLD/Gieok_Jeojangso/Reception_3_Forgotten_Soldier.md", "w", encoding="utf-8") as f:
        f.write(content_3)
    print("Reception 3 expanded successfully!")
    
    content_4 = build_reception_4()
    with open("SOMNARAK-WORLD/Gieok_Jeojangso/Reception_4_Weeping_Statue.md", "w", encoding="utf-8") as f:
        f.write(content_4)
    print("Reception 4 expanded successfully!")
