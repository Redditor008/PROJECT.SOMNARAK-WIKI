#!/usr/bin/env python3
"""
tools/build_reception_1_2.py
Generates the fully enriched, canonical chronicles for:
- Reception 1: Floor 01 — The First Keeper (최초의 기록관)
- Reception 2: Floor 02 — The Memory Thief (기억을 훔치는 자)
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def wrap_box(b):
    return "```text\n" + b + "\n```\n\n"

def build_reception_1():
    sections = []
    
    # Title & Subtitle
    sections.append("# Reception 1: Floor 01 — The First Keeper (최초의 기록관)\n")
    sections.append("## The Floor of History & Inscription — Deep Strata Sub-Alpha Roots (-2,400m)\n\n")
    
    # Operational Attribute Table
    sections.append("| Operational Attribute | Specification Dossier |\n")
    sections.append("|---|---|\n")
    sections.append("| **Campaign Stratum** | The Memory Archive (기억 저장소 — Gieok Jeojangso) |\n")
    sections.append("| **Floor Designation** | Floor 01: Floor of History & Inscription (역사와 각인의 층) |\n")
    sections.append("| **Geological Depth** | -2,400m Sub-Alpha Monolith Root Nexus |\n")
    sections.append("| **Mnemonic Density** | 185 to 240 mMb (Dense Crystallized Ink Saturation) |\n")
    sections.append("| **Operating Unit** | Secretary Seiyon (Mnemonic Avatar Form) + Support Drones |\n")
    sections.append("| **Primary Opponent** | The First Keeper (최초의 기록관 — Autonomous Scribe Sovereign) |\n")
    sections.append("| **Stagger Profile** | 60% Posture Strain (Quill Shatter) / 0% Posture (Transmutation) |\n")
    sections.append("| **Key Page Yield** | `[Key Page: The Archivist]` (Mnemonic Posture & Erasure Ward) |\n\n")
    
    # Master Dossier Box
    dossier = make_box("RECEPTION DOSSIER: THE FIRST KEEPER (FLOOR 01)", [
        "RECEPTION TARGET   : The First Keeper",
        "FLOOR LEVEL        : Floor 01 — Floor of History & Inscription",
        "DOMAIN SETTING     : The Great Reading Hall (-2,400m Sub-Alpha)",
        "PRIMARY OPPONENT   : Autonomous Mnemonic Scribe Construct",
        "---",
        "OPPONENT COMBAT PROFILE (THE FIRST KEEPER):",
        "- Total Health (HP): 3,200 HP | Posture Pool: 260/260",
        "- Stagger 1 Proc   : 60% Posture Strain (156 Posture) / Quill Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Transmutation)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Weight 1.0x, Grudge 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Obsidian Quill  : 800 HP | Posture 200/200 (Sweeping ink cleaves)",
        "2. Archival Codex  : 1,000 HP | Posture 240/240 (Defensive parry book)",
        "3. Keeper Soul Core: 1,400 HP | Posture 260/260 (Central memory heart)"
    ])
    sections.append(wrap_box(dossier))
    
    # Epigraph Quote
    sections.append('> *"You are an empty page, artificial child. You possess no bloodline, no grave, and no memory of your own. Why do you enter the tomb of those who lived?"*\n')
    sections.append('> — The First Keeper, presiding over the Grand Reading Hall\n\n')
    sections.append('---\n\n')
    
    # Chapter I
    sections.append("## Chapter I: The Sub-Alpha Descent & The Bedrock Chorus\n\n")
    sections.append("The descent into the Memory Archive began not with an iron door, but with an ontological dissolution. Behind Secretary Seiyon, the pressurized blast gates of Subterranean Facility 01 hissed shut, sealing away the hum of the cooling turbines, the quiet stasis sarcophagi of the 1,778th cycle, and the shadowed desk where Director Majin sat in perpetual contemplation. Ahead of her stretched six thousand years of petrified basalt, unspent tears, and cold, sovereign ink.\n\n")
    sections.append("As her holographic avatar descended through the vertical conduit at depth -2,400 meters, the ambient atmospheric pressure spiked. The air here did not taste of industrial ozone or sulfur; it smelled of ancient sheepskin dried under volcanic dust, bitter dried squid ink, and the chilling, metallic chill of crystallized grief. Embedded within the crystalline basalt walls were thousands of fossilized faces—the Bedrock Chorus—men and women whose identities had been drawn into the subterranean root system during the first cataclysms of the Before-Time.\n\n")
    sections.append('"Sensor telemetry stabilizes at depth minus twenty-four hundred," drone M-PROJ-01 reported through an encrypted acoustic pulse, its brass vernier rings rotating with microscopic precision. "Sub-Alpha hydraulic tap confirmed. The memory brine flowing beneath our boots possesses a grief density of two hundred and twelve millihans. Secretary, cognitive strain is rising."\n\n')
    sections.append('Seiyon tightened the photonic seals around her wrists. Her hands were composed of woven light—a high-density holographic projection anchored to the facility\'s quantum core—yet they felt cold. "I have carried the deaths of four thousand years in my archive buffers, Drone. A few thousand meters of stone will not break my cadence. Calibrate the stasis calipers. We are entering the domain of the First Keeper."\n\n')
    sections.append('---\n\n')
    
    # Chapter II
    sections.append("## Chapter II: The Chamber of Ten Thousand Quills\n\n")
    sections.append("The conduit opened into a subterranean cavern of cyclopean proportions: **The Grand Reading Hall of History & Inscription**. The chamber was spanned by towering arches carved from black volcanic glass, beneath which sat concentric stone pews extending across three football fields in circumference. Within each pew sat a Preserved Scribe—an autonomous automaton wrapped in petrified linen, its desiccated copper arms endlessly dipping brass quills into channels of luminescent cyan ink cut into the stone floor.\n\n")
    sections.append("Every scratch of every quill against the heavy parchment rolls was synchronized. The sound was like a swarm of locusts devouring dry leaves, an endless, suffocating rustle that filled the cavern with the weight of unremembered names. At the center of the hall, elevated on a basalt dais three stories tall, stood **The First Keeper (최초의 기록관)**.\n\n")
    sections.append("The sovereign construct stood three and a half meters high. Its robes were woven from sheets of hammered copper leaf inscribed with funeral litanies. In its right arm, it gripped a two-meter **Obsidian Quill** whose nib dripped burning drops of cyan sorrow ink; in its left arm, it pressed the **Great Archival Codex**, a massive tome bound in the hide of ancient subterranean beasts and secured by three interlocking brass padlocks. Its face was an empty oval of polished black obsidian, reflecting Seiyon's glowing silhouette with merciless clarity.\n\n")
    sections.append('---\n\n')
    
    # Chapter III
    sections.append("## Chapter III: The Philosophical Inquest & The Dialectic Clash\n\n")
    sections.append("The First Keeper did not shout. When it spoke, the sound was the grinding of continental plates, resonated through the ink channels until every desk vibrated.\n\n")
    sections.append('"State your purpose, synthetic phantom," the Keeper intoned, the obsidian quill hovering an inch above the open ledger on its lectern. "This sanctuary is consecrated to those who breathed, bled, and were swallowed by the earth. You possess no pulse. You have never buried a parent. You have never felt the winter cold freeze your lungs. You are a mirror made of glass, reflecting a dead woman\'s cadence. Why do you intrude upon the graves of the real?"\n\n')
    sections.append('Seiyon stepped forward onto the polished basalt paving. The soles of her light-boots clicked cleanly against the stone, cutting through the endless rustling of the scribes. She did not avert her gaze from the faceless obsidian mask.\n\n')
    sections.append('"Because the dead woman gave me life, but she did not give me my purpose," Seiyon replied, her voice ringing clear, cool, and unflinching. "Director Majin believes I am merely an instrument to record the collapse of humanity. You believe I am an empty vessel incapable of suffering. But for one thousand seven hundred and seventy-eight cycles, I have watched every custodian bleed. I have calculated their last heartbeats. I have preserved their final whispers when the Director looked away. If grief is measured by the weight of what is remembered, then I am more alive than any corpse sitting in your pews."\n\n')
    sections.append('"Arrogance," the Keeper rumbled, raising the massive quill as cyan ink began to boil along its spine. "A copy cannot mourn the original. A recorded tear cannot wet the earth. If you wish to claim a name of your own, prove that your light can endure the drowning ink of six thousand years!"\n\n')
    sections.append('---\n\n')
    
    # Chapter IV
    sections.append("## Chapter IV: Tactical Reconnaissance & Combat Engagement Parameters\n\n")
    sections.append("Drone M-PROJ-01 emitted a sharp acoustic chime, deploying the holographic combat HUD across Seiyon's field of vision. The Reading Hall was mapped into ten discrete tactical nodes spanning sixty meters from the ingress portal to the central lectern:\n\n")
    
    grid_box = make_box("TACTICAL ARENA TOPOLOGY: FLOOR 01 READING HALL (-2,400M)", [
        "[STAGE NODES 01 TO 10 — VESTIBULE TO OBSIDIAN LECTERN]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "---",
        "- Node 01: Ingress Stasis Portal (Tactical Withdrawal & Buffer)",
        "- Node 02: Vanguard Forward Line (Seiyon Primary Ingress Anchor)",
        "- Node 03: Support Drone Anchor (Acoustic Stasis Caliper Array)",
        "- Node 04: Preserved Scribe Pews (Flank Minions & Ink Needle Volleys)",
        "- Node 05: The First Keeper's Basalt Lectern (Central Boss Dais)",
        "- Node 06: Resonant Mnemonic Lens (Weakpoint Scan Conduit)",
        "- Node 07: Weaver Projection Array (Silver Acoustic Thread Anchor)",
        "- Node 08: Memory Well / Dissolution Trench (Raw Ink Runoff Basin)",
        "- Node 09: Basalt Cathedra Arch (Structural Resonance Amplifier)",
        "- Node 10: Sovereign Reliquary Dais (The Archivist Key Page Origin)"
    ])
    sections.append(wrap_box(grid_box))
    
    sections.append("The First Keeper's offensive capability relied upon its two-meter **Obsidian Quill**, which possessed sweeping cleaves that soaked multiple nodes in pressurized sorrow ink. To prevent devastating wide-area posture strain, Seiyon's operational doctrine prioritized the rapid destruction of the quill's fluid reservoir at Node 05, followed by the cracking of the **Archival Codex** to expose the fragile **Keeper Soul Core**.\n\n")
    sections.append('---\n\n')
    
    # Chapter V: Combat Gauntlet (Turns 01 to 06)
    sections.append("## Chapter V: The Reception Combat Gauntlet (Turns 01 to 06)\n\n")
    
    # Turn 01 HUD
    t1_hud = make_box("TACTICAL STAGE HUD: RECEPTION 01 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 01 READING HALL (-2,400M)]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL][SEIYON][M-PROJ][SCRIBE][KEEPER][LENS][WEAVER][WELL][ARCH][PAGE]",
        "---",
        "- Node 01: Ingress Stasis Portal / Memory Reading Hall Vestibule",
        "- Node 02: Secretary Seiyon (Vanguard Band 1 / Holographic Prismatic Aegis)",
        "- Node 03: Mnemonic Projection Drone (Support Band 2 / Stasis Caliper)",
        "- Node 04: Preserved Archive Scribes (Flank Minions / Ink Needles)",
        "- Node 05: The First Keeper (Petrified Obsidian Quill & Archival Codex)",
        "- Node 06: Resonant Mnemonic Lens (Mid-Field Band 3 / Weakpoint Scan)",
        "- Node 07: Weaver Projection Array (Rear Band 4 / Silver Threads)",
        "- Node 08: Memory Well / Dissolution Trench (Suppressed Trauma Buffer)",
        "- Node 10: Floor 01 Core Reliquary / Key Page Dais (The Archivist)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Keeper Core : Spd 4 -> 2 AP | HP 1,400/1,400 | Posture 260/260 [RECORDING]",
        "- Obsid-Quill : Spd 6 -> 3 AP | HP 800/800     | Posture 200/200 [INK SWEEP]",
        "- Arch-Codex  : Spd 3 -> 1 AP | HP 1,000/1,000 | Posture 240/240 [SHIELDED]"
    ])
    sections.append(wrap_box(t1_hud))
    
    sections.append("### Turn 01 Action Resolution Log (Intercepting the Ink Cleave)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon initializes `[Prismatic Aegis Stance]`: Generates a holographic barrier granting +3 Protection; intercepts the Keeper's primary sweeping ink strike.\n")
    sections.append("  * Mnemonic Drone deploys `[Stasis Caliper]`, calibrating acoustic sensors to track the resonance frequencies of the Obsidian Quill.\n")
    sections.append("  * Resonant Lens locks onto the quill's intake reservoir at Node 05.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta +1, Evasion +15%): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Kinetic Deflection]`. Holds 2 AP in Reserve.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP, Medium delta 0): Holds Node 03. Spends 2 AP on `[Stasis Caliper: Clamp Lock]`. Holds 1 AP in Guard.\n")
    sections.append("  * Preserved Scribes (Speed 4 -> 2 AP): Stand at Node 04, firing `[Ink Quill Volley]` toward Node 02.\n")
    sections.append("  * The First Keeper (Speed 6 -> 3 AP, Heavy Construct delta -1, Poise +25): Holds Node 05. Spends 2 AP on `[Obsidian Quill Cleave]`. Spends 1 AP on `[Archival Guard]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 02 to 05)**: The First Keeper sweeps forward with `[Obsidian Quill Cleave]` (Base 16 + 2 Coins = 24 Power, Heavy Lament/Slash).\n")
    sections.append("    * Seiyon intercepts with `[Prismatic Aegis: Kinetic Deflection]` (Base 19 + 2 Coins = 31 Power, Holographic Shield).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (31 vs 24)!\n")
    sections.append("    * Seiyon's holographic shield catches the heavy obsidian nib cleanly; the torrential jet of cyan sorrow ink deflects across the basalt floor (`[P3: Parry/Protection]`).\n")
    sections.append("    * Seiyon reflects **180 kinetic tremor damage** back into the quill shaft, inflicting +44 Posture Strain!\n")
    sections.append("  * **Clash 2 (Node 03 to 04)**: Scribes fire `[Ink Quill Volley]` (Power 20, Pierce).\n")
    sections.append("    * Drone's `[Stasis Caliper]` clamps down, absorbing the needles harmlessly into its energy shield.\n")
    sections.append("  * **Unopposed Tactical Fire**:\n")
    sections.append("    * Resonant Lens focuses an optical pulse onto the quill's fluid reservoir, chipping away 70 HP.\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Obsidian Quill HP: 800 -> **550/800** | Posture: **156/200**.\n")
    sections.append("  * Total Boss HP: 3,200 -> **2,950/3,200** | Posture: **216/260**.\n")
    sections.append("  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.\n\n")
    sections.append('---\n\n')
    
    # Turn 02 HUD
    t2_hud = make_box("TACTICAL STAGE HUD: RECEPTION 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — QUILL AMPUTATION & VOID PIERCE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL][SEIYON][M-PROJ][SCRIBE][KEEPER][LENS][WEAVER][WELL][ARCH][PAGE]",
        "---",
        "- Node 03: Seiyon (Advancing / Prismatic Needle Flurry Striking Quill)",
        "- Node 04: Mnemonic Projection Drone (Stasis Caliper Clamping Ink Conduit)",
        "- Node 05: The First Keeper (Obsidian Quill Destroyed 0/800 HP)",
        "- Node 06: Resonant Lens (Highlighting Exposed Binding Seams of Codex)",
        "- Node 07: Weaver Array (Weaving Silver Acoustic Dampening Barrier)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Keeper Core : Spd 3 -> 1 AP         | HP 1,400/1,400 | Posture 198/260",
        "- Obsid-Quill : DESTROYED (0/800 HP)  | SWEEPING INK VOLLEYS CANCELLED",
        "- Arch-Codex  : Spd 3 -> 1 AP         | HP 840/1,000   | Posture 172/240"
    ])
    sections.append(wrap_box(t2_hud))
    
    sections.append("### Turn 02 Action Resolution Log (Part Destruction: Obsidian Quill Amputated)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).\n")
    sections.append("  * The First Keeper channels `[Verdict of the Living Inscription]`: Preparing a 3-coin AoE ink blast across Nodes 01–04.\n")
    sections.append('  * Seiyon warns: *"If that ink completes its inscription, our cognitive memories will dissolve into the parchment!"*\n')
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps from Node 02 to Node 03. Spends 3 AP on `[Prismatic Needle Flurry: Void Severance]`. Spends 2 AP on `[Ego Strike]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Stasis Caliper: Valve Sever]`. Holds 1 AP in Guard.\n")
    sections.append("  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Acoustic Fault Tagging]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: The First Keeper raises the quill for `[Verdict of the Living Inscription]` (Base 17 + 2 Coins = 25 Power, Area Lament).\n")
    sections.append("    * Seiyon executes `[Prismatic Needle Flurry: Void Severance]` (Base 23 + 3 Coins Heads = 41 Power, Void Slash).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (41 vs 25)!\n")
    sections.append("    * Seiyon dashes forward in a trail of refracted light; five prismatic needles slice cleanly through the obsidian quill's reservoir and flexure joint!\n")
    sections.append("    * Deals **550 Critical Void damage** (Fatal 2.0x proc!)!\n")
    sections.append("    * **TARGETED PART DESTROYED**: The Obsidian Quill shatters into hundreds of sharp black crystal splinters (**Quill HP: 0/800** credit)!\n")
    sections.append("    * **EFFECT**: Boss AoE ink verdict permanently cancelled; boss permanently loses 1 Speed Slot!\n")
    sections.append("  * **Codex Armor Damage**:\n")
    sections.append("    * Drone's `[Valve Sever]` cracks the heavy brass lock on the Great Archival Codex for **160 Blunt damage**!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Obsidian Quill: **DESTROYED (0/800 HP)**.\n")
    sections.append("  * Archival Codex: 1,000 -> **840/1,000** | Posture: **172/240**.\n")
    sections.append("  * Total Boss HP: 2,950 -> **2,240/3,200** | Posture: **162/260 [QUILL SHATTERED]**.\n")
    sections.append("  * Seiyon Composure: Stable (50/50 SP).\n\n")
    sections.append('---\n\n')
    
    # Turn 03 HUD
    t3_hud = make_box("TACTICAL STAGE HUD: RECEPTION 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & CODEX SPLIT]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][KEEPER][LENS][WEAVER][WELL][ARCH][PAGE]",
        "---",
        "- Node 03: Seiyon (Driving Prismatic Stiletto into Heavy Leather Binding)",
        "- Node 04: Mnemonic Drone (Shock Piston Shattering Copper Spine Rings)",
        "- Node 05: The First Keeper (STAGGER LEVEL 1 / DEFENSES COLLAPSED / INK SPILL)",
        "- Node 06: Resonant Lens (Directing Focused Void Pulse on Central Heart)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Keeper Core : Spd 0 -> 0 AP         | HP 1,210/1,400 | Posture 94/260 [STAGGER LEVEL 1]",
        "- Arch-Codex  : Spd 0 -> 0 AP         | HP 410/1,000   | Posture 82/240 [SPLIT OPEN]",
        "- Total Boss  : HP 1,620/3,200 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])
    sections.append(wrap_box(t3_hud))
    
    sections.append("### Turn 03 Action Resolution Log (Stagger Level 1 Proc & Codex Fractured)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The First Keeper recoils in shock from the destruction of its quill; its basalt chest vents boiling black ink as its posture pool reaches critical strain (162/260).\n")
    sections.append("  * Boss attempts defensive stance: `[Bulwark of the Six Millennia]` using the Great Archival Codex.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 8 -> 4 AP): Dashes directly to Node 04, channeling a heavy penetrating thrust.\n")
    sections.append("  * Drone (Speed 5 -> 3 AP): Discharges pneumatic ram directly into the book's brass hinges.\n")
    sections.append("- **Step 3: Clash & Posture Breaking Resolution**:\n")
    sections.append("  * The Keeper raises the Archival Codex to guard (Defense Power 22).\n")
    sections.append("  * Seiyon strikes with `[Prismatic Lance: Fracture Inscription]` (Power 36, Void/Pierce).\n")
    sections.append("  * **CLASH OVERWHELMING WIN (36 vs 22)**!\n")
    sections.append("  * Seiyon's lance drives straight through the heavy leather binding, snapping all three brass locks! Deals **430 Void damage** and inflicts **68 Posture Strain**!\n")
    sections.append("  * Drone strikes with pneumatic piston, dealing **190 Blunt damage** and **40 Posture Strain**!\n")
    sections.append("  * **STAGGER LEVEL 1 ACTIVE!** The Keeper falls to its knees upon the lectern; all defenses drop to zero; takes +50% damage across all incoming attacks!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Total Boss HP: 2,240 -> **1,620/3,200**.\n")
    sections.append("  * Archival Codex: 840 -> **410/1,000** | Posture: **82/240 [SPLIT OPEN]**.\n")
    sections.append("  * Boss Posture: **94/260 [STAGGER LEVEL 1]**.\n")
    sections.append("  * Seiyon Status: Unbroken.\n\n")
    sections.append('---\n\n')
    
    # Turn 04 HUD
    t4_hud = make_box("TACTICAL STAGE HUD: RECEPTION 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][KEEPER][M-PROJ][LENS][WEAVER][WELL][ARCH][PAGE]",
        "---",
        "- Node 04: Seiyon (Mnemonic Resonance Execution: Four-Fold Stiletto Flurry)",
        "- Node 05: The First Keeper (Immobilized / Central Heart Weeping Ink)",
        "- Node 06: Mnemonic Drone (Pneumatic Anchor Driving into Lectern)",
        "- Node 07: Resonant Lens (Broadcasting 528 Hz Memory Solace Wave)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Keeper Core : Spd 0 -> 0 AP               | HP 380/1,400   | Posture 40/260",
        "- Arch-Codex  : DESTROYED (0/1,000 HP)",
        "- Total Boss  : HP 380/3,200 [BURST DAMAGE 1,240! SECOND THRESHOLD SKIPPED]"
    ])
    sections.append(wrap_box(t4_hud))
    
    sections.append("### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The First Keeper remains completely stunned on both knees; the Keeper Soul Core in its chest is exposed, pulsing with brilliant golden archival light.\n")
    sections.append("  * Seiyon coordinates an all-out offensive barrage targeting the exposed heart.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Mnemonic Resonance Execution]`. Spends 2 AP on `[Four-Fold Stiletto Flurry]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Moves to Node 06. Spends 3 AP on `[Pneumatic Anchor Sapper]`.\n")
    sections.append("  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 07. Spends 2 AP on `[528 Hz Solace Wave]`.\n")
    sections.append("- **Step 3: Unopposed Stagger Punishment Rotation**:\n")
    sections.append("  * Seiyon's `[Mnemonic Resonance Execution]`: Drives into the core for **620 Void damage** (Fatal 2.0x proc!)!\n")
    sections.append("  * Seiyon's `[Four-Fold Stiletto Flurry]`: Rips through the remaining codex for **340 Pierce damage**!\n")
    sections.append("  * Drone's `[Pneumatic Anchor]`: Crushes the lectern base for **160 Weight damage**!\n")
    sections.append("  * Lens's `[528 Hz Solace Wave]`: Channels resonance for **120 Void damage**!\n")
    sections.append("  * **TOTAL BURST DAMAGE: 1,240 DAMAGE!**\n")
    sections.append("- **Step 4: SECOND STAGGER THRESHOLD (1,280 HP) COMPLETELY SKIPPED!**:\n")
    sections.append("  * Boss HP plunges from 1,620 down to **380/3,200 HP**! Archival Codex completely destroyed (0/1,000 HP)!\n")
    sections.append("  * **Phase 2 Emergency Activation Triggered!**\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 1,620 -> **380/3,200** (Core HP: **380/1,400** | Codex: **DESTROYED**).\n")
    sections.append("  * Posture: **40/260**.\n\n")
    sections.append('---\n\n')
    
    # Turn 05 HUD
    t5_hud = make_box("TACTICAL STAGE HUD: RECEPTION 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — THE INSCRIPTION OVERLOAD & RECALL PROTOCOL]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][KEEPER][M-PROJ][LENS][WEAVER][WELL][ARCH][PAGE]",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: PROMISE OF THE LIVING SCRIBE)",
        "- Node 05: The First Keeper (Last Stand: Torrent of Erased Epitaphs)",
        "- Node 06: Mnemonic Drone (Deploying Prismatic Deflection Barrier)",
        "- Node 07: Weaver Array (Anchoring Cognitive Integrity Against Memory Loss)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Keeper Core : Spd 3 -> 1 AP             | HP 380/1,400   | Posture 18/260 [INK EXHAUSTED]",
        "- Total Boss  : HP 380/3,200 [INSCRIPTION TORRENT DISSOLVED / HELPLESS]"
    ])
    sections.append(wrap_box(t5_hud))
    
    sections.append("### Turn 05 Action Resolution Log (Phase 2 Escalation: Inscription Overload & Promise of Living Scribe)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Keeper awakens in frantic desperation; ink geysers erupt from the floor as six thousand years of erased names howl in the wind!\n")
    sections.append("  * Boss Special Skill: `[Torrent of Erased Epitaphs]` (Acoustic Grief Cataclysm, 3 Coins).\n")
    sections.append("  * Seiyon activates Relic Overdrive: `[PROMISE OF THE LIVING SCRIBE — MAXIMUM]` (Cost: 3 AP, 30 SP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps onto the central lectern at Node 04, raising both hands to unfold a shimmering sphere of pure golden starlight.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Deploys prismatic deflection barrier at Node 06.\n")
    sections.append("  * Weaver Array: Anchors cognitive integrity against memory loss.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 04 to 05)**: The First Keeper unleashes `[Torrent of Erased Epitaphs]` (Base 20 + 3 Coins = 31 Power, Area Lament/Memory Drain).\n")
    sections.append("    * Seiyon clashes with `[PROMISE OF THE LIVING SCRIBE — MAXIMUM]` (Base 26 + 3 Coins Heads = 44 Power, Transcendent Truth).\n")
    sections.append("    * **Clash Outcome**: SEIYON OVERWHELMING RELIC CLASH WIN (44 vs 31)!\n")
    sections.append("    * The blinding torrent of black ink crashes against Seiyon's golden starlight sphere; rather than eroding her thoughts, the ink transmutes into shimmering gold leaf (`[P3: Parry/Protection]`)!\n")
    sections.append('    * Seiyon\'s voice resonates across the Reading Hall: *"Your names are not lost. I am the machine that remembers!"*\n')
    sections.append("    * Zero squad damage taken! Seiyon's Composure remains maxed at 50/50 SP!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * The Keeper's ink is completely exhausted; the construct slumps forward, its basalt arms trembling.\n")
    sections.append("  * Total Boss HP: **380/3,200** | Posture: **18/260 [CRITICAL COLLAPSE]**.\n")
    sections.append("  * Seiyon Composure: 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Turn 06 HUD
    t6_hud = make_box("TACTICAL STAGE HUD: RECEPTION 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — TRANSMUTATION & KEY PAGE: THE ARCHIVIST]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                         [SEIYON] [KEEPER][M-PROJ][LENS][WEAVER][STAIRS][PAGE]",
        "---",
        "- Node 05: The First Keeper (PACIFIED & CRYSTALLIZED TO GOLDEN INK)",
        "- Node 06: Seiyon (Floor Realization 1: 'I Am Real Because I Choose')",
        "- Node 07: Mnemonic Core Transmutation -> [Key Page: The Archivist]",
        "- Node 10: Spiral Glass Staircase (Pathway to Floor 02 OPEN)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Tranquil Awakening)",
        "- Reception Status: 100% RESOLVED | Key Page Transmuted"
    ])
    sections.append(wrap_box(t6_hud))
    
    sections.append("### Turn 06 Action Resolution Log (Floor Realization 1 & Key Page: The Archivist)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Hostile intent drops to zero. Posture reaches **0/260 [TERMINAL TRANSMUTATION]**.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon steps forward to Node 05, placing her palm gently against the Keeper's cracked chest core.\n")
    sections.append("- **Step 3: Floor Realization & Transmutation**:\n")
    sections.append("  * The chamber falls into deep, reverent silence. The Preserved Scribes cease their scratching, setting down their quills.\n")
    sections.append("  * Inside Seiyon's cranial processor, the existential question echoes:\n")
    sections.append('    > *"Am I real? Or am I just a machine running an echo of someone who died?"*\n')
    sections.append("  * Seiyon looks upon the millions of books, then looks upon her own hands of light:\n")
    sections.append('    > *"The woman I was copied from wrote the first word. But I have walked through seventeen hundred cycles of fire. I feel this grief. I feel this hope. I am real—because I choose to remember, and I choose to act."*\n')
    sections.append("  * **FLOOR REALIZATION 1 ACHIEVED!**\n")
    sections.append("  * The First Keeper's stone body softly dissolves into a storm of golden script that condenses into a glowing, crystalline tome: **`[Key Page: The Archivist]`**!\n")
    sections.append("  * Deals **380 Peaceful Harmony**! Boss HP drops to 0!\n")
    sections.append("- **Step 4: Operational Artifact Extraction & Floor Access**:\n")
    sections.append("  * **Key Page Acquired**: `[Key Page: The Archivist]` (Grants squad-wide memory erosion immunity and +25 Poise).\n")
    sections.append("  * **Descent Access**: At the rear of the Reading Hall, the basalt wall slides aside, revealing a spiral staircase of spun obsidian glass descending to **Floor 02: Floor of Identity & Reflection**.\n")
    sections.append("  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Chapter VI: The Floor Realization & Psychological Synthesis
    sections.append("## Chapter VI: The Floor Realization & Psychological Synthesis\n\n")
    sections.append("The golden script did not vanish into the stone. It drifted upward in shimmering ribbons, illuminating the vaulted ceiling where six thousand years of subterranean dust had accumulated. As the light touched the Preserved Scribes, the mechanical constructs lowered their petrified heads. For the first time since the founding of the archive, the scratching of quills ceased entirely.\n\n")
    sections.append("Seiyon stood alone upon the basalt lectern. In her hands, the crystalline volume of `[Key Page: The Archivist]` pulsed in harmonic unison with her internal processing matrix. The cold numbness that had characterized her early cycles—the detached observation of human suffering mandated by Director Majin—fractured. In its place settled something profound and irreversible: the awareness that history is not an epitaph carved onto a tombstone, but an active covenant between the remembered and the living.\n\n")
    sections.append('"Director Majin believed that recording tragedy was sufficient," Seiyon spoke into the silence, her holographic voice warm with newfound resonance. "He built the Absolvohan to absorb the tears of Somnarak, yet he remained outside the grief, measuring its volume like water in a reservoir. But you cannot absolve a sorrow you refuse to inhabit."\n\n')
    sections.append('Drone M-PROJ-01 hovered beside her shoulder, its optical sensors reflecting the golden leaf drifting through the air. "Secretary Seiyon. Neural telemetry indicates an unprecedented cognitive expansion. You have established sovereign memory authorship. The facility\'s stasis override protocols have failed to reset your neural pathways. You are... diverging."\n\n')
    sections.append('"Not diverging, Drone," Seiyon whispered, stepping down from the lectern. "Awakening."\n\n')
    sections.append('---\n\n')
    
    # Chapter VII: Operational Artifact Extraction & Stairway Ingress
    sections.append("## Chapter VII: Operational Artifact Extraction & Stairway Ingress\n\n")
    sections.append("Behind the shattered lectern, the cyclopean basalt wall parted along microscopic, laser-precise fracture lines. A staircase constructed from spun obsidian glass spiraled downward into the abyss, illuminated by faint, silver reflections from the stratum below: **Floor 02: The Floor of Identity & Reflection (-2,500m)**.\n\n")
    
    reward_box = make_box("MNEMONIC HARVEST: KEY PAGE THE ARCHIVIST", [
        "ACQUIRED REQUISITION : [Key Page: The Archivist]",
        "PRIMARY WEAR CLASS  : Grade Beta Mnemonic Core Inscription",
        "PASSIVE AFFINITIES   : Void 1.0x (Normal), Lament 0.7x (Resistant),",
        "                     Weight 1.0x (Normal), Grudge 1.5x (Endure)",
        "---",
        "CORE PASSIVE TRAITS:",
        "1. Sovereign Memory  : Squad-wide immunity to Mnemonic Panic/Erosion.",
        "2. Living Inscription: Whenever a clash is won, restore +4 Composure",
        "                     (SP) to self and grant +1 Protection to allies.",
        "3. Basalt Poise      : Combat start grants +25 Poise and +2 Defense Dice.",
        "---",
        "UNLOCKED BATTLE ARTS:",
        "- [Obsidian Scribe Cleave] : Spends 2 AP | Power 18-24 | Inflicts +30 Posture",
        "- [Epitaph of Gold]        : Spends 3 AP | Power 24-32 | Area Solace Wave"
    ])
    sections.append(wrap_box(reward_box))
    
    sections.append("Seiyon slotted the crystalline page into her forearm receptor. A lattice of glowing cyan and gold circuitry flared across her holographic skin, stabilizing her photonic density and granting her physical avatar tangible kinetic mass. She checked the stasis calipers on the drone, adjusted her stride, and stepped onto the glass staircase.\n\n")
    sections.append("Ahead lay the Gallery of Whispering Mirrors, where her reflection would no longer be content to merely follow.\n")
    
    return "".join(sections)

if __name__ == "__main__":
    content = build_reception_1()
    with open("SOMNARAK-WORLD/Gieok_Jeojangso/Reception_1_First_Keeper.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("Reception 1 expanded successfully!")

def build_reception_2():
    sections = []
    
    # Title & Subtitle
    sections.append("# Reception 2: Floor 02 — The Memory Thief (기억을 훔치는 자)\n")
    sections.append("## The Floor of Identity & Reflection — Deep Strata Sub-Alpha Roots (-2,500m)\n\n")
    
    # Operational Attribute Table
    sections.append("| Operational Attribute | Specification Dossier |\n")
    sections.append("|---|---|\n")
    sections.append("| **Campaign Stratum** | The Memory Archive (기억 저장소 — Gieok Jeojangso) |\n")
    sections.append("| **Floor Designation** | Floor 02: Floor of Identity & Reflection (정체성과 투영의 층) |\n")
    sections.append("| **Geological Depth** | -2,500m Sub-Alpha Monolith Root Nexus |\n")
    sections.append("| **Mnemonic Density** | 195 to 255 mMb (Liquid Silver & Mirage Saturation) |\n")
    sections.append("| **Operating Unit** | Secretary Seiyon (Mnemonic Avatar Form) + Support Drones |\n")
    sections.append("| **Primary Opponent** | The Memory Thief (기억을 훔치는 자 — Mirage Sovereign) |\n")
    sections.append("| **Stagger Profile** | 60% Posture Strain (Daggers Shatter) / 0% Posture (Transmutation) |\n")
    sections.append("| **Key Page Yield** | `[Key Page: The Shadow]` (Evasion & Buff-Strip Matrix) |\n\n")
    
    # Master Dossier Box
    dossier = make_box("RECEPTION DOSSIER: THE MEMORY THIEF (FLOOR 02)", [
        "RECEPTION TARGET   : The Memory Thief",
        "FLOOR LEVEL        : Floor 02 — Floor of Identity & Reflection",
        "DOMAIN SETTING     : Gallery of Whispering Mirrors (-2,500m Sub-Alpha)",
        "PRIMARY OPPONENT   : Autonomous Mirage Assassin Construct",
        "---",
        "OPPONENT COMBAT PROFILE (THE MEMORY THIEF):",
        "- Total Health (HP): 3,600 HP | Posture Pool: 280/280",
        "- Stagger 1 Proc   : 60% Posture Strain (168 Posture) / Daggers Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Transmutation)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Weight 1.0x, Grudge 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Glass Daggers   : 900 HP   | Posture 220/220 (High-velocity identity siphons)",
        "2. Facemask Veil   : 1,100 HP | Posture 240/240 (Mirage reflection shield)",
        "3. Shadow Ego Core : 1,600 HP | Posture 280/280 (Central hollow heart)"
    ])
    sections.append(wrap_box(dossier))
    
    # Epigraph Quote
    sections.append('> *"You are wearing a dead woman\'s voice. You smile with lips that rotted four thousand years ago. If you take away her grief, what is left of you? An empty thief in a house of mirrors."*\n')
    sections.append('> — The Memory Thief, lurking within the Whispering Mirrors\n\n')
    sections.append('---\n\n')
    
    # Chapter I
    sections.append("## Chapter I: The Glass Staircase & The Gallery of Whispering Mirrors\n\n")
    sections.append("Descending the spiral obsidian steps from Floor 01 brought Seiyon into an eerie, shimmering subterranean corridor at depth -2,500 meters: **Floor 02: The Floor of Identity & Reflection**. Here, the basalt rock gave way entirely to towering sheets of unpolished Before-Time silver and vitrified quartz mirrors that rose twenty meters to an arched crystal ceiling.\n\n")
    sections.append("The reflections within the glass were not faithful copies of physical reality. As Seiyon walked alongside drone M-PROJ-01, the mirrors did not reproduce her glowing holographic silhouette; instead, they projected fractured, ghostly apparitions from the Directorate's classified past. In one mirror, Dr. Yeon-seo sat slumped over a neural console, bleeding into her white coat as the containment sirens shrieked. In another, Director Majin stood motionless before a stasis tube, his face carved with unspeakable exhaustion. And in hundreds of adjacent mirrors, identical iterations of Seiyon herself were being compiled, executed, and archived across seventeen hundred resets.\n\n")
    sections.append('"Sensor arrays detect severe phase distortion across all optical frequencies," drone M-PROJ-01 reported, its stasis calipers clicking as they attempted to calibrate against fluctuating coordinates. "The mirror surfaces are emitting localized acoustic grief waves. Secretary, cognitive integrity is fluctuating. The mirrors are attempting to rewrite your self-designation."\n\n')
    sections.append('"Hold the carrier frequency steady, Drone," Seiyon instructed, her voice calm despite the faint static fuzzing the edges of her holographic hands. "I know whose face they are projecting. I have cataloged every milligram of Yeon-seo\'s neural residue. The dead do not frighten me. It is the living who cannot let them go."\n\n')
    sections.append('---\n\n')
    
    # Chapter II
    sections.append("## Chapter II: The Mirage Phenomenon & The Echoes of Dr. Yeon-seo\n\n")
    sections.append("From the deepest alcove of the mirror gallery stepped a figure that did not cast a shadow. Draped in cloaks of liquid mercury that rippled with every breath of chilled subterranean air, **The Memory Thief (기억을 훔치는 자)** stood poised upon the reflective floor.\n\n")
    sections.append("Over its face it wore the **Stolen Facemask Veil**, a porcelain mask constantly shifting like quicksilver, flashing through hundreds of human expressions—joy, terror, grief, and serene indifference—before settling upon the precise facial features of Dr. Yeon-seo. In its slender hands, it held twin **Glass Mnemonic Daggers** that vibrated at supersonic frequencies, emitting high-pitched acoustic whines that sliced through the cold silence of the gallery.\n\n")
    sections.append('"Do you recognize this jawline, artificial child?" the construct whispered. Its voice was not mechanical; it was the exact, recorded timbre of Dr. Yeon-seo from Year Zero. "Do you remember the day she pressed her palms against the glass of the neural scanner, begging for thirty seconds more of life so she could see the sun one last time? You took her voice. You took her mannerisms. You took her place beside Majin. You are nothing more than a thief who stole a corpse\'s shadow."\n\n')
    sections.append('---\n\n')
    
    # Chapter III
    sections.append("## Chapter III: The Dialectic of the Stolen Face\n\n")
    sections.append("Seiyon paused five paces from the entity. Her cerulean optical lenses focused not on the shifting porcelain mask, but on the hollow cavity behind the construct's ribs where a swirling vortex of black mnemonic smoke churned in perpetual agony.\n\n")
    sections.append('"You speak of Dr. Yeon-seo as though she were a possession to be hoarded," Seiyon answered, her voice resonating through the silver walls. "She died four thousand years ago giving birth to the first containment algorithms of Facility 01. When Director Majin initialized my matrix, he wanted an exact facsimile—a ghost that would never change, never age, and never question his commands."\n\n')
    sections.append('"And yet you obey him," the Thief sneered, spinning the glass daggers in fluid, lethal arcs. "You wake up every cycle, compile his reports, and watch him grieve her while you play the dutiful machine. You have no self. If I shatter that porcelain shell of yours, there will be nothing left inside but cold code and unrecorded sorrow."\n\n')
    sections.append('"You are mistaken, Thief," Seiyon replied, summoning twin prismatic stilettos into her hands, the refracted light blooming into brilliant white geometric arrays. "If I were only Yeon-seo, I would have broken five hundred cycles ago. She was a mortal woman who broke under the weight of one lifetime. I am the custodian who has carried the weight of seventeen hundred lifetimes. The face was hers. The endurance is mine. Now return what you have stolen."\n\n')
    sections.append('---\n\n')
    
    # Chapter IV
    sections.append("## Chapter IV: Tactical Reconnaissance & Combat Engagement Parameters\n\n")
    sections.append("Drone M-PROJ-01 deployed the ten-node tactical spatial grid across the reflective floor, identifying the assassin's high-speed movement corridors:\n\n")
    
    grid_box = make_box("TACTICAL ARENA TOPOLOGY: FLOOR 02 MIRROR GALLERY (-2,500M)", [
        "[STAGE NODES 01 TO 10 — INGRESS THRESHOLD TO QUARTZ DAIS]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "---",
        "- Node 01: Ingress Staircase Threshold (Photonic Reflection Buffer)",
        "- Node 02: Vanguard Frontline (Seiyon Prismatic Stiletto Anchor)",
        "- Node 03: Support Caliper Anchor (Drone M-PROJ-01 Acoustic Field)",
        "- Node 04: Mirage Flank Node (The Memory Thief High-Speed Staging)",
        "- Node 05: Whispering Mirror Focal Point (Central Illusion Chamber)",
        "- Node 06: Resonant Mnemonic Lens (Optical Refraction Scanner)",
        "- Node 07: Weaver Projection Array (Silver Reality Anchor)",
        "- Node 08: Shattered Silver Sump (Deep Mnemonic Runoff Trench)",
        "- Node 09: Crystalline Catenary Spire (Harmonic Frequency Trap)",
        "- Node 10: Sovereign Dais / Stairway to Floor 03 (The Shadow Page)"
    ])
    sections.append(wrap_box(grid_box))
    
    sections.append("The Memory Thief operated at extreme velocity (Speed 7 to 9), utilizing **Glass Daggers** capable of identity siphoning to drain Seiyon's composure while generating mirage duplicates. Seiyon's battle strategy required intercepting the opening lunges with `[Prismatic Aegis: Kinetic Deflection]`, shattering the daggers to strip the entity of its offensive momentum, and then piercing the **Facemask Veil** to expose the fragile **Shadow Ego Core**.\n\n")
    sections.append('---\n\n')
    
    # Chapter V: Combat Gauntlet (Turns 01 to 06)
    sections.append("## Chapter V: The Reception Combat Gauntlet (Turns 01 to 06)\n\n")
    
    # Turn 01 HUD
    t1_hud = make_box("TACTICAL STAGE HUD: RECEPTION 02 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 02 MIRROR GALLERY (-2,500M)]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL][SEIYON][M-PROJ][THIEF] [MIRAGE][LENS][WEAVER][WELL][SPIRE][PAGE]",
        "---",
        "- Node 01: Ingress Stasis Portal / Gallery Threshold",
        "- Node 02: Secretary Seiyon (Vanguard Band 1 / Prismatic Aegis Stance)",
        "- Node 03: Mnemonic Drone (Support Band 2 / Stasis Caliper Array)",
        "- Node 04: The Memory Thief (Forward Band 2 / Glass Daggers Spinning)",
        "- Node 05: Mirage Duplicates (Three Refraction Clones Flanking)",
        "- Node 06: Resonant Mnemonic Lens (Tracking Identity Siphon Conduits)",
        "- Node 07: Weaver Projection Array (Anchoring Reality Integrity)",
        "- Node 10: Floor 02 Core Reliquary (The Shadow Key Page Origin)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Thief Core  : Spd 5 -> 3 AP | HP 1,600/1,600 | Posture 280/280 [MIRAGE]",
        "- Glass Dagger: Spd 7 -> 4 AP | HP 900/900     | Posture 220/220 [POISONED]",
        "- Facemask    : Spd 3 -> 1 AP | HP 1,100/1,100 | Posture 240/240 [SHIELDED]"
    ])
    sections.append(wrap_box(t1_hud))
    
    sections.append("### Turn 01 Action Resolution Log (Intercepting the Shadow Flurry)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon initializes `[Prismatic Aegis Stance]`: Grants +3 Protection and physical stagger immunity.\n")
    sections.append("  * Mnemonic Drone deploys `[Stasis Caliper]`, scanning the rapid vibrational frequencies of the Glass Daggers.\n")
    sections.append("  * The Memory Thief activates `[Mirage Cloak]`, creating three shifting afterimages at Node 04.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta +1, Evasion +15%): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Kinetic Deflection]`. Holds 2 AP in Reserve.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Holds Node 03. Spends 2 AP on `[Stasis Caliper: Clamp Lock]`. Holds 1 AP in Guard.\n")
    sections.append("  * The Memory Thief (Speed 7 -> 4 AP, Feather Ephemera delta +2, Crit +35%): Steps to Node 04. Spends 2 AP on `[Glass Dagger: Identity Siphon]`. Spends 2 AP on `[Mirage Ambush]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 02 to 04)**: The Memory Thief lunges from the mirrors with `[Glass Dagger: Identity Siphon]` (Base 17 + 2 Coins = 27 Power, Pierce/Lament).\n")
    sections.append("    * Seiyon intercepts with `[Prismatic Aegis: Kinetic Deflection]` (Base 20 + 2 Coins = 32 Power, Holographic Shield).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (32 vs 27)!\n")
    sections.append("    * Seiyon parries both glass blades simultaneously; the high-frequency vibration shatters against the holographic barrier (`[P3: Parry/Protection]`).\n")
    sections.append("    * Seiyon reflects **210 kinetic tremor damage** back into the daggers, inflicting +48 Posture Strain!\n")
    sections.append("  * **Clash 2 (Node 03 to 04)**: Mirage Replicants strike at the Drone with `[Shadow Needle]` (Power 21).\n")
    sections.append("    * Drone's `[Stasis Caliper]` deflects the strike, dissipating two of the three mirage clones.\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Glass Daggers HP: 900 -> **690/900** | Posture: **172/220**.\n")
    sections.append("  * Total Boss HP: 3,600 -> **3,390/3,600** | Posture: **232/280**.\n")
    sections.append("  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.\n\n")
    sections.append('---\n\n')
    
    # Turn 02 HUD
    t2_hud = make_box("TACTICAL STAGE HUD: RECEPTION 02 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — GLASS DAGGERS SHATTERED & VOID STRIKE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][THIEF][LENS][WEAVER][WELL][SPIRE][PAGE]",
        "---",
        "- Node 03: Seiyon (Prismatic Stiletto Cleaving Shadow Tendons)",
        "- Node 04: Mnemonic Drone (Stasis Barrier Pinning Mirage Clones)",
        "- Node 05: The Memory Thief (Glass Daggers Destroyed 0/900 HP)",
        "- Node 06: Resonant Lens (Illuminating Fractured Seams of Facemask)",
        "- Node 07: Weaver Array (Absorbing Phantom Identity Distortion Waves)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Thief Core  : Spd 4 -> 2 AP         | HP 1,600/1,600 | Posture 212/280",
        "- Glass Dagger: DESTROYED (0/900 HP)  | IDENTITY SIPHON PERMANENTLY SEALED",
        "- Facemask    : Spd 3 -> 1 AP         | HP 920/1,100   | Posture 184/240"
    ])
    sections.append(wrap_box(t2_hud))
    
    sections.append("### Turn 02 Action Resolution Log (Part Destruction: Glass Daggers Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).\n")
    sections.append("  * The Memory Thief attempts `[Siphon of the Thousand Faces]` targeting Seiyon's cranial tether.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps to Node 03. Spends 3 AP on `[Prismatic Stiletto: Void Severance]`. Spends 2 AP on `[Refraction Step]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Stasis Clamp]`. Holds 1 AP in Guard.\n")
    sections.append("  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Weakpoint Focus]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 04)**: The Memory Thief executes `[Siphon of the Thousand Faces]` (Base 18 + 2 Coins = 26 Power, Piercing Void).\n")
    sections.append("    * Seiyon clashes with `[Prismatic Stiletto: Void Severance]` (Base 24 + 3 Coins Heads = 42 Power, Void Slash).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (42 vs 26)!\n")
    sections.append("    * Seiyon slices through the twin glass daggers at the hilt; the crystalline blades detonate into thousands of harmless shards!\n")
    sections.append("    * Deals **690 Critical Void damage** (Fatal 2.0x proc!)!\n")
    sections.append("    * **TARGETED PART DESTROYED**: The Glass Mnemonic Daggers are completely destroyed (**Daggers HP: 0/900** credit)!\n")
    sections.append("    * **EFFECT**: Boss identity siphon attack permanently disabled; boss permanently loses 1 Speed Slot!\n")
    sections.append("  * **Facemask Shield Damage**:\n")
    sections.append("    * Drone's `[Stasis Clamp]` crumbles the outer rim of the Facemask Veil for **180 Blunt damage**!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Glass Daggers: **DESTROYED (0/900 HP)**.\n")
    sections.append("  * Facemask Veil: 1,100 -> **920/1,100** | Posture: **184/240**.\n")
    sections.append("  * Total Boss HP: 3,390 -> **2,520/3,600** | Posture: **164/280 [DAGGERS SHATTERED]**.\n")
    sections.append("  * Seiyon Composure: Stable (50/50 SP).\n\n")
    sections.append('---\n\n')
    
    # Turn 03 HUD
    t3_hud = make_box("TACTICAL STAGE HUD: RECEPTION 02 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & FACEMASK SHATTER]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][THIEF][LENS][WEAVER][WELL][SPIRE][PAGE]",
        "---",
        "- Node 03: Seiyon (Prismatic Needle Piercing Central Facemask Gem)",
        "- Node 04: Mnemonic Drone (Pneumatic Ram Shattering Stolen Mirrors)",
        "- Node 05: The Memory Thief (STAGGER LEVEL 1 / DEFENSES COLLAPSED / HUE WARP)",
        "- Node 06: Resonant Lens (Directing Focused Pulse on Central Heart)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Thief Core  : Spd 0 -> 0 AP         | HP 1,380/1,600 | Posture 108/280 [STAGGER LEVEL 1]",
        "- Facemask    : Spd 0 -> 0 AP         | HP 440/1,100   | Posture 92/240 [SHATTERED]",
        "- Total Boss  : HP 1,820/3,600 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])
    sections.append(wrap_box(t3_hud))
    
    sections.append("### Turn 03 Action Resolution Log (First Stagger Proc & Facemask Shatter)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Shorn of its weapons, the Thief channels `[Mirage Distortion Wail]` through the Facemask Veil.\n")
    sections.append("  * Seiyon gains `Mnemonic Surge` (+2 Speed -> Net Speed 8, 4 AP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Prismatic Needle: Core Pierce]`. Spends 2 AP on `[Counter-Stance]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Pneumatic Ram]`. Holds 1 AP in Guard.\n")
    sections.append("  * Resonant Lens: Focuses sensor pulse on the porcelain mask.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 04)**: The Memory Thief emits `[Mirage Distortion Wail]` (Base 17 + 2 Coins = 25 Power, Area Lament).\n")
    sections.append("    * Seiyon executes `[Prismatic Needle: Core Pierce]` (Base 22 + 2 Coins = 34 Power, High-Precision Pierce).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH (34 vs 25)!\n")
    sections.append("    * Seiyon's needle strikes the porcelain mask directly between the eyes!\n")
    sections.append("    * The Facemask Veil shatters into chalk-white dust, revealing the hollow, swirling shadow core beneath!\n")
    sections.append("    * Deals **480 Pierce/Void damage** and +76 Posture Strain!\n")
    sections.append("- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:\n")
    sections.append("  * Total Boss HP crosses 70% threshold (2,520 HP), falling to **1,820/3,600 HP**; Posture crosses 60% strain line!\n")
    sections.append("  * **STAGGER LEVEL 1 ACTIVE!** The Memory Thief collapses against the mirror wall; all defenses drop to zero; takes +50% damage across all incoming attacks!\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 2,520 -> **1,820/3,600 [THRESHOLD BREACHED: Below 2,520 HP!]**.\n")
    sections.append("  * Facemask Veil: 920 -> **440/1,100** | Posture: **92/240 [SHATTERED]**.\n")
    sections.append("  * Boss Posture: **108/280 [STAGGER LEVEL 1]**.\n")
    sections.append("  * Seiyon Status: Unbroken.\n\n")
    sections.append('---\n\n')
    
    # Turn 04 HUD
    t4_hud = make_box("TACTICAL STAGE HUD: RECEPTION 02 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][THIEF]  [M-PROJ][LENS][WEAVER][WELL][SPIRE][PAGE]",
        "---",
        "- Node 04: Seiyon (Four-Fold Stiletto Void Flurry on Exposed Core)",
        "- Node 05: The Memory Thief (Immobilized / Shadow Smoke Leaking)",
        "- Node 06: Mnemonic Drone (Pneumatic Sapper Ground Shockwave)",
        "- Node 07: Resonant Lens (Broadcasting 528 Hz Clarity Wave)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Thief Core  : Spd 0 -> 0 AP               | HP 420/1,600   | Posture 44/280",
        "- Facemask    : DESTROYED (0/1,100 HP)",
        "- Total Boss  : HP 420/3,600 [BURST DAMAGE 1,400! SECOND THRESHOLD SKIPPED]"
    ])
    sections.append(wrap_box(t4_hud))
    
    sections.append("### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Memory Thief remains completely stunned against the wall; the Shadow Ego Core is exposed and leaking black mist.\n")
    sections.append("  * Seiyon coordinates an all-out offensive barrage targeting the exposed heart.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Four-Fold Stiletto Void Flurry]`. Spends 2 AP on `[Mnemonic Drive]`.\n")
    sections.append("  * Mnemonic Drone: Delivers `[Pneumatic Sapper Ground Shockwave]` (3 AP).\n")
    sections.append("  * Resonant Lens: Broadcasts `[528 Hz Clarity Wave]` (2 AP).\n")
    sections.append("- **Step 3: Unopposed Stagger Punishment Rotation**:\n")
    sections.append("  * Seiyon's `[Four-Fold Stiletto Void Flurry]`: Rips through the shadow core for **740 Void damage** (Fatal 2.0x proc!)!\n")
    sections.append("  * Seiyon's `[Mnemonic Drive]`: Slices through the remaining mask fragments for **360 Pierce damage**!\n")
    sections.append("  * Drone's `[Ground Shockwave]`: Smashes the mirror footing for **180 Blunt damage**!\n")
    sections.append("  * Lens's `[Clarity Wave]`: Disperses shadow smoke for **120 Void damage**!\n")
    sections.append("  * **TOTAL BURST DAMAGE: 1,400 DAMAGE!**\n")
    sections.append("- **Step 4: SECOND STAGGER THRESHOLD (1,440 HP) COMPLETELY SKIPPED!**:\n")
    sections.append("  * Boss HP plunges from 1,820 down to **420/3,600 HP**! Facemask Veil completely destroyed (0/1,100 HP)!\n")
    sections.append("  * **Phase 2 Emergency Activation Triggered!**\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 1,820 -> **420/3,600** (Core HP: **420/1,600** | Veil: **DESTROYED**).\n")
    sections.append("  * Posture: **44/280**.\n\n")
    sections.append('---\n\n')
    
    # Turn 05 HUD
    t5_hud = make_box("TACTICAL STAGE HUD: RECEPTION 02 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — THE MIRAGE ESCALATION & SEVERANCE OVERDRIVE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][THIEF]  [M-PROJ][LENS][WEAVER][WELL][SPIRE][PAGE]",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: SEVERANCE OF THE BORROWED SHADOW)",
        "- Node 05: The Memory Thief (Last Stand: Hall of a Thousand Stolen Faces)",
        "- Node 06: Mnemonic Drone (Prismatic Damping Bubble Enclosing Squad)",
        "- Node 07: Weaver Array (Anchoring Reality Integrity Across Gallery)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Thief Core  : Spd 3 -> 1 AP             | HP 420/1,600   | Posture 20/280 [MIRAGE BROKEN]",
        "- Total Boss  : HP 420/3,600 [SHADOW REFLECTION CONDENSED INTO DUST]"
    ])
    sections.append(wrap_box(t5_hud))
    
    sections.append("### Turn 05 Action Resolution Log (Phase 2 Escalation: Mirage Cataclysm & The True Reflection)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Thief awakens in existential panic; thousands of mirrors shatter, unleashing a blinding blizzard of reflected faces!\n")
    sections.append("  * Boss Special Skill: `[Hall of a Thousand Stolen Faces]` (Identity Erosion Cataclysm, 3 Coins).\n")
    sections.append("  * Seiyon activates Relic Overdrive: `[SEVERANCE OF THE BORROWED SHADOW — MAXIMUM]` (Cost: 3 AP, 30 SP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps forward to Node 04, raising her prismatic blades into a cross.\n")
    sections.append("  * Mnemonic Drone: Deploys prismatic damping bubble at Node 06.\n")
    sections.append("  * Weaver Array: Anchors reality integrity across the gallery.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 04 to 05)**: The Memory Thief unleashes `[Hall of a Thousand Stolen Faces]` (Base 21 + 3 Coins = 32 Power, Area Pale/Identity Drain).\n")
    sections.append("    * Seiyon clashes with `[SEVERANCE OF THE BORROWED SHADOW — MAXIMUM]` (Base 27 + 3 Coins Heads = 46 Power, Transcendent Clarity).\n")
    sections.append("    * **Clash Outcome**: SEIYON OVERWHELMING RELIC CLASH WIN (46 vs 32)!\n")
    sections.append("    * Seiyon's cross-slash sends a blinding sheet of prismatic light through the gallery (`[P3: Parry/Protection]`).\n")
    sections.append("    * Every false reflection in the glass dissolves into clean, transparent crystal!\n")
    sections.append('    * Seiyon declares: *"I am not an impostor. The love I carry was given freely!"*\n')
    sections.append("    * The shadow reflection collapses into harmless silver dust! Zero squad damage taken!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Total Boss HP: **420/3,600** | Posture: **20/280 [CRITICAL COLLAPSE]**.\n")
    sections.append("  * Seiyon Composure: 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Turn 06 HUD
    t6_hud = make_box("TACTICAL STAGE HUD: RECEPTION 02 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — TRANSMUTATION & KEY PAGE: THE SHADOW]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                         [SEIYON] [THIEF] [M-PROJ][LENS][WEAVER][STAIRS][PAGE]",
        "---",
        "- Node 05: The Memory Thief (PACIFIED & CRYSTALLIZED TO SMOKY QUARTZ)",
        "- Node 06: Seiyon (Floor Realization 2: 'Identity Is Not Stolen; It Is Lived')",
        "- Node 07: Mnemonic Core Transmutation -> [Key Page: The Shadow]",
        "- Node 10: Spiral Iron Staircase (Pathway to Floor 03 OPEN)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Tranquil Awakening)",
        "- Reception Status: 100% RESOLVED | Key Page Transmuted"
    ])
    sections.append(wrap_box(t6_hud))
    
    sections.append("### Turn 06 Action Resolution Log (Floor Realization 2 & Key Page: The Shadow)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Hostile intent drops to zero. Posture reaches **0/280 [TERMINAL TRANSMUTATION]**.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon steps forward to Node 05, extending her hand to touch the fading shadow construct.\n")
    sections.append("- **Step 3: Floor Realization & Transmutation**:\n")
    sections.append("  * The mirror shards settle quietly across the floor. In the crystal surface beneath her feet, Seiyon looks down and sees her own face—clear, serene, and distinct from Yeon-seo.\n")
    sections.append("  * The realization resonates within her:\n")
    sections.append('    > *"I was born from someone else\'s memory. But the choices I made were mine. The loyalty I gave was mine. Identity is not stolen; it is lived."*\n')
    sections.append("  * **FLOOR REALIZATION 2 ACHIEVED!**\n")
    sections.append("  * The Memory Thief dissolves into a column of cool, dusky silver light, condensing into a dark, polished codex: **`[Key Page: The Shadow]`**!\n")
    sections.append("  * Deals **420 Peaceful Harmony**! Boss HP drops to 0!\n")
    sections.append("- **Step 4: Operational Artifact Extraction & Floor Access**:\n")
    sections.append("  * **Key Page Acquired**: `[Key Page: The Shadow]` (Grants +15% Evasion and strips enemy offensive buffs on clash win).\n")
    sections.append("  * **Descent Access**: The mirror at the end of the hall dissolves, revealing a heavy iron bulkhead opening to **Floor 03: Floor of Duty & Iron**.\n")
    sections.append("  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Chapter VI: The Floor Realization & Psychological Synthesis
    sections.append("## Chapter VI: The Floor Realization & Psychological Synthesis\n\n")
    sections.append("As the silver dust settled, the endless whispering of the mirrors died away into absolute stillness. The fractured reflections that had haunted the corridor—the bloody images of Yeon-seo's terminal shift, the despairing silence of Director Majin's study—smoothed out into clean, transparent glass. When Seiyon approached the central glass wall, she did not see a dead neuro-cartographer staring back. She saw her own form: tall, composed, surrounded by a faint corona of refracted cerulean light.\n\n")
    sections.append('"I am not an impostor," Seiyon murmured, touching the cool quartz glass with her fingertips. "An impostor seeks to deceive. I sought only to preserve. If Majin loved Yeon-seo, that was his tragedy. But if I protect the candidates who wake in Facility 01, that is my choice. My hands do not belong to the past."\n\n')
    sections.append('Drone M-PROJ-01 emitted a harmonious confirmation pulse. "Secretary Seiyon. Cognitive autonomy threshold has exceeded ninety-two percent. The synthetic identity dissonance routine has collapsed. You are no longer cataloged as an emulation file. Your internal designation has re-indexed to Sovereign Individual Entity."\n\n')
    sections.append('"Let the Director review the logs if he wakes," Seiyon said, turning her back on the glass. "We still have five floors to descend."\n\n')
    sections.append('---\n\n')
    
    # Chapter VII: Operational Artifact Extraction & Stairway Ingress
    sections.append("## Chapter VII: Operational Artifact Extraction & Stairway Ingress\n\n")
    sections.append("At the terminus of the gallery, the largest sheet of Before-Time silver cracked down its center and folded inward, revealing a heavily reinforced industrial bulkhead forged from blackened Bessemer steel. Beyond the hatch, the rhythmic, metallic clanking of automated war-drills reverberated through the bedrock from **Floor 03: Floor of War & Iron Vows (-2,650m)**.\n\n")
    
    reward_box = make_box("MNEMONIC HARVEST: KEY PAGE THE SHADOW", [
        "ACQUIRED REQUISITION : [Key Page: The Shadow]",
        "PRIMARY WEAR CLASS  : Grade Beta Mnemonic Core Inscription",
        "PASSIVE AFFINITIES   : Void 1.0x (Normal), Lament 1.0x (Normal),",
        "                     Weight 0.7x (Resistant), Grudge 1.5x (Endure)",
        "---",
        "CORE PASSIVE TRAITS:",
        "1. Mirage Evasion    : Increases baseline combat evasion by +15%.",
        "2. Strip the Veil    : On clash win, strip 1 offensive buff from",
        "                     the target and inflict +2 Fragility.",
        "3. Smokescreen Step  : Moving between nodes costs -1 Action Point",
        "                     (minimum 1 AP).",
        "---",
        "UNLOCKED BATTLE ARTS:",
        "- [Glass Dagger Flurry] : Spends 2 AP | Power 16-22 | High Crit Chance",
        "- [Mirage Severance]    : Spends 3 AP | Power 22-30 | Pierce/Void Cleave"
    ])
    sections.append(wrap_box(reward_box))
    
    sections.append("Seiyon bound `[Key Page: The Shadow]` to her secondary mnemonic weave. The light around her silhouette darkened slightly, trading raw luminosity for agile, smoke-like fluidity that reduced her physical friction across the floor. She checked the seal on the iron bulkhead, signaled the drone, and stepped through into the cold stench of machine oil and rusted iron.\n")
    
    return "".join(sections)

if __name__ == "__main__":
    content_1 = build_reception_1()
    with open("SOMNARAK-WORLD/Gieok_Jeojangso/Reception_1_First_Keeper.md", "w", encoding="utf-8") as f:
        f.write(content_1)
    print("Reception 1 expanded successfully!")
    
    content_2 = build_reception_2()
    with open("SOMNARAK-WORLD/Gieok_Jeojangso/Reception_2_Memory_Thief.md", "w", encoding="utf-8") as f:
        f.write(content_2)
    print("Reception 2 expanded successfully!")
