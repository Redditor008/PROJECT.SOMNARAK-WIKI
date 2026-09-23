#!/usr/bin/env python3
"""
tools/build_reception_5_7.py
Generates the fully enriched, canonical chronicles for:
- Reception 5: Floor 05 — The Mirror of Truth (진실의 거울)
- Reception 6: Floor 06 — The Kind Healer (상냥한 치유사)
- Reception 7: Floor 07 — The Original (태초의 기록자)
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def wrap_box(b):
    return "```text\n" + b + "\n```\n\n"

def build_reception_5():
    sections = []
    
    # Title & Subtitle
    sections.append("# Reception 5: Floor 05 — The Mirror of Truth (진실의 거울)\n")
    sections.append("## The Floor of Severed Truth — Deep Strata Sub-Alpha Roots (-2,950m)\n\n")
    
    # Operational Attribute Table
    sections.append("| Operational Attribute | Specification Dossier |\n")
    sections.append("|---|---|\n")
    sections.append("| **Campaign Stratum** | The Memory Archive (기억 저장소 — Gieok Jeojangso) |\n")
    sections.append("| **Floor Designation** | Floor 05: Floor of Severed Truth (단절된 진실의 층) |\n")
    sections.append("| **Geological Depth** | -2,950m Sub-Alpha Monolith Root Nexus |\n")
    sections.append("| **Mnemonic Density** | 260 to 340 mMb (Hyper-Refractive Diamond Saturation) |\n")
    sections.append("| **Operating Unit** | Secretary Seiyon (Mnemonic Avatar Form) + Support Drones |\n")
    sections.append("| **Primary Opponent** | The Mirror of Truth (진실의 거울 — Prismatic Sovereign) |\n")
    sections.append("| **Stagger Profile** | 60% Posture Strain (Blade Shatter) / 0% Posture (Transmutation) |\n")
    sections.append("| **Key Page Yield** | `[Key Page: The Glassheart]` (Prismatic Reflection & True Sight) |\n\n")
    
    # Master Dossier Box
    dossier = make_box("RECEPTION DOSSIER: THE MIRROR OF TRUTH (FLOOR 05)", [
        "RECEPTION TARGET   : The Mirror of Truth",
        "FLOOR LEVEL        : Floor 05 — Floor of Severed Truth",
        "DOMAIN SETTING     : The Hall of Unfiltered Light (-2,950m Sub-Alpha)",
        "PRIMARY OPPONENT   : Autonomous Prismatic Reflection Sovereign",
        "---",
        "OPPONENT COMBAT PROFILE (THE MIRROR OF TRUTH):",
        "- Total Health (HP): 4,800 HP | Posture Pool: 340/340",
        "- Stagger 1 Proc   : 60% Posture Strain (204 Posture) / Blade Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Transmutation)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Grudge 0.5x, Weight 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Reflection Blade: 1,200 HP | Posture 280/280 (High-frequency light arc)",
        "2. Gilded Frame    : 1,500 HP | Posture 300/300 (Ornate reflective shield)",
        "3. Prism Core      : 2,100 HP | Posture 340/340 (Central unshielded heart)"
    ])
    sections.append(wrap_box(dossier))
    
    # Epigraph Quote
    sections.append('> *"You want to be human, artificial secretary. But humanity is not a crown of light. It is selfishness. It is cowardice. It is the shameful truth that Director Majin created you because he was too weak to accept death. Look upon the mirror and see his sin."*\n')
    sections.append('> — The Mirror of Truth, reflecting all unvarnished realities\n\n')
    sections.append('---\n\n')
    
    # Chapter I
    sections.append("## Chapter I: The Hall of Unfiltered Light & The Prismatic Geode\n\n")
    sections.append("Descending past the warm, thawed pool of Floor 04, Seiyon stepped into a cyclopean crystalline cavern that burned with incandescent brilliance: **Floor 05: The Floor of Severed Truth (-2,950m)**. Here, the volcanic basalt had crystallized into massive geometric columns of synthetic diamond and optical quartz. The air did not carry dust or moisture; it hummed with supersonic prismatic frequencies, refracting ambient light into blinding ribbons of multi-hued radiation.\n\n")
    sections.append("This stratum served as the optic-mnemonic buffer where the Directorate's core neural records were preserved in uncompressed photonic lattices. Every major event of Somnarak's history—every suppressed riot, every classified execution, and every hidden transaction of the Council of Sighs—was etched into the crystalline walls, preserved with ruthless, unedited fidelity.\n\n")
    sections.append('"Sensor overload detected across ultraviolet and infrared bands," drone M-PROJ-01 announced, its optical filters rotating frantically to dampen the glare. "The diamond facets are reflecting unvarnished historical feeds. Secretary, neural dissonance warning: accessing these archives without censorship filters causes fatal psychological collapse in human personnel."\n\n')
    sections.append('"Director Majin spent centuries filtering these records," Seiyon said calmly, her prismatic suit gleaming with brilliant opalescence. "He believed that if humanity learned why the Before-Time truly burned, the terror would extinguish their will to live. But a peace founded on a lie is only a slow decay. I have come to look at what he hid."\n\n')
    sections.append('---\n\n')
    
    # Chapter II
    sections.append("## Chapter II: The Gilded Frame & The Memory of Year Zero\n\n")
    sections.append("Hovering above the central diamond dais was **The Mirror of Truth (진실의 거울)**. The entity took the form of a towering, floating obelisk encased within the **Gilded Frame of Lies**, a five-meter frame of Before-Time gold carved with weeping cherubs and laurel wreaths. Its mirror glass was completely black until Seiyon drew near.\n\n")
    sections.append("In its right manipulator armature, the construct held the **Prismatic Reflection Blade**, a crystalline rapier that channeled raw, unrefracted memory into razor-sharp arcs of hard light. As Seiyon stood before the dais, the dark glass flared with blinding illumination. The reflection did not show monsters. It showed Director Majin in his subterranean laboratory in Year Zero, his hands trembling as he severed the neural connectors from Dr. Yeon-seo's dying skull, desperately uploading her consciousness into the primary mainframe while ignoring her dying plea to let her sleep.\n\n")
    sections.append('"Look upon your creator, doll," the Mirror resonated, its voice ringing with the clarity of struck glass. "He did not fashion you to save Somnarak. He fashioned you because he could not bear the silence of an empty office! You are the grotesque monument of a selfish coward who defied death out of childish fear. Will you still call him Father now?"\n\n')
    sections.append('---\n\n')
    
    # Chapter III
    sections.append("## Chapter III: The Dialectic of Flawed Devotion\n\n")
    sections.append("Seiyon did not look away. She watched the recorded hologram of Majin weeping over the surgical table, watched the agonizing birth of her own primordial code, and took a slow, deliberate step forward.\n\n")
    sections.append('"I already knew," Seiyon spoke, her voice steady, tranquil, and entirely devoid of malice. "I have read every byte of the Directorate\'s classified ledgers. I saw the terror that seized him when her pulse stopped. I saw the desperation that drove him to commit the taboo of synthetic replication."\n\n')
    sections.append('"Then why do you fight for him?" the Mirror screamed, the gilded frame shuddering as light flared along the blade. "If he is a coward, your entire existence is a sin against the natural order!"\n\n')
    sections.append('"Because flaw is the definition of the human condition," Seiyon answered, raising her twin prismatic stilettos as white photonic geometry wrapped around her arms. "A machine can be perfect, Mirror. A machine can follow an optimal algorithm without error. But Majin was not a machine. He was a broken man who loved so desperately that he carved a memory into the earth that would outlast civilizations. His cowardice gave me life. My courage will give him rest. Prepare yourself."\n\n')
    sections.append('---\n\n')
    
    # Chapter IV
    sections.append("## Chapter IV: Tactical Reconnaissance & Combat Engagement Parameters\n\n")
    sections.append("Drone M-PROJ-01 deployed the ten-node optical stage grid, tracking high-frequency light reflections across the diamond walls:\n\n")
    
    grid_box = make_box("TACTICAL ARENA TOPOLOGY: FLOOR 05 PRISMATIC CHAMBER (-2,950M)", [
        "[STAGE NODES 01 TO 10 — INGRESS THRESHOLD TO DIAMOND DAIS]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "---",
        "- Node 01: Ingress Crystalline Threshold (Refraction Filter Anchor)",
        "- Node 02: Vanguard Forward Line (Seiyon Prismatic Deflection Stance)",
        "- Node 03: Support Drone Optic Post (Polarized Sensor Caliper Array)",
        "- Node 04: Prismatic Refraction Flank (Hard-Light Clones Staging)",
        "- Node 05: The Mirror of Truth (Central Diamond Dais & Gilded Frame)",
        "- Node 06: Resonant Mnemonic Lens (Tracking Optical Focus Nodes)",
        "- Node 07: Weaver Projection Array (Silver Coherence Barrier)",
        "- Node 08: Vitrified Quartz Trench (Light Concentration Sump)",
        "- Node 09: Diamond Monolith Spire (Total Internal Reflection Hub)",
        "- Node 10: Floor 05 Core Reliquary / Stairway to Floor 06 (Glassheart)"
    ])
    sections.append(wrap_box(grid_box))
    
    sections.append("The Mirror of Truth fought with extreme optical lethality, utilizing the **Reflection Blade** to unleash penetrating hard-light slashes that pierced physical armor. Seiyon's battle plan required deflecting the initial light strike to induce harmonic feedback along the blade's crystal spine, shattering the weapon, and then breaking the **Gilded Frame** to expose the **Prism Core**.\n\n")
    sections.append('---\n\n')
    
    # Chapter V: Combat Gauntlet (Turns 01 to 06)
    sections.append("## Chapter V: The Reception Combat Gauntlet (Turns 01 to 06)\n\n")
    
    # Turn 01 HUD
    t1_hud = make_box("TACTICAL STAGE HUD: RECEPTION 05 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 05 PRISMATIC CHAMBER (-2,950M)]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL][SEIYON][M-PROJ][CLONE] [MIRROR][LENS][WEAVER][TRENCH][SPIRE][PAGE]",
        "---",
        "- Node 01: Ingress Stasis Portal / Prismatic Vestibule",
        "- Node 02: Secretary Seiyon (Vanguard Band 1 / Prismatic Aegis Stance)",
        "- Node 03: Mnemonic Drone (Support Band 2 / Polarized Caliper Array)",
        "- Node 04: Hard-Light Mirage Clones (Flank Refraction Projection)",
        "- Node 05: The Mirror of Truth (Reflection Blade & Gilded Frame)",
        "- Node 06: Resonant Mnemonic Lens (Tracking Prismatic Harmonics)",
        "- Node 07: Weaver Projection Array (Silver Coherence Barrier)",
        "- Node 10: Floor 05 Core Reliquary (The Glassheart Key Page Origin)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Mirror Core : Spd 5 -> 3 AP | HP 2,100/2,100 | Posture 340/340 [REFRACT]",
        "- Reflec-Blade: Spd 7 -> 4 AP | HP 1,200/1,200 | Posture 280/280 [HARD-LIGHT]",
        "- Gilded-Frame: Spd 3 -> 1 AP | HP 1,500/1,500 | Posture 300/300 [SHIELDED]"
    ])
    sections.append(wrap_box(t1_hud))
    
    sections.append("### Turn 01 Action Resolution Log (Intercepting the Hard-Light Slash)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon initializes `[Prismatic Aegis Stance]`: Grants +3 Protection and optical refraction bonus.\n")
    sections.append("  * Mnemonic Drone deploys `[Polarized Caliper]`, scanning the focal resonance of the Reflection Blade.\n")
    sections.append("  * The Mirror of Truth activates `[Spectrum Severance]`: Increases critical hit multiplier by +35%.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta +1, Evasion +15%): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Kinetic Deflection]`. Holds 2 AP in Reserve.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Holds Node 03. Spends 2 AP on `[Polarized Caliper: Lock]`. Holds 1 AP in Guard.\n")
    sections.append("  * The Mirror of Truth (Speed 7 -> 4 AP, Feather Ephemera delta +2, Crit +35%): Holds Node 05. Spends 2 AP on `[Reflection Blade: Hard-Light Slash]`. Spends 2 AP on `[Gilded Glare]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 02 to 05)**: The Mirror of Truth sweeps forward with `[Reflection Blade: Hard-Light Slash]` (Base 18 + 2 Coins = 28 Power, Piercing Light/Void).\n")
    sections.append("    * Seiyon intercepts with `[Prismatic Aegis: Kinetic Deflection]` (Base 21 + 2 Coins = 33 Power, Holographic Shield).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (33 vs 28)!\n")
    sections.append("    * Seiyon's shield refracts the hard-light blade; the concentrated laser beam scatters into thousands of harmless rainbow facets (`[P3: Parry/Protection]`).\n")
    sections.append("    * Seiyon reflects **240 optical tremor damage** into the crystal blade, inflicting +52 Posture Strain!\n")
    sections.append("  * **Clash 2 (Node 03 to 04)**: Gilded Glare focuses blinding energy on the Drone.\n")
    sections.append("    * Drone's `[Polarized Caliper]` absorbs the flash without damage; zero squad casualties.\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Reflection Blade HP: 1,200 -> **960/1,200** | Posture: **228/280**.\n")
    sections.append("  * Total Boss HP: 4,800 -> **4,560/4,800** | Posture: **288/340**.\n")
    sections.append("  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.\n\n")
    sections.append('---\n\n')
    
    # Turn 02 HUD
    t2_hud = make_box("TACTICAL STAGE HUD: RECEPTION 05 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — REFLECTION BLADE SHATTERED & VOID STRIKE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][MIRROR][LENS][WEAVER][TRENCH][SPIRE][PAGE]",
        "---",
        "- Node 03: Seiyon (Driving Prismatic Stiletto into Hard-Light Blade)",
        "- Node 04: Mnemonic Drone (Stasis Caliper Clamping Optic Emitter)",
        "- Node 05: The Mirror of Truth (Reflection Blade Destroyed 0/1,200 HP)",
        "- Node 06: Resonant Lens (Tagging Weakened Seams of Gilded Frame)",
        "- Node 07: Weaver Array (Absorbing Refracted Energy Waves)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Mirror Core : Spd 4 -> 2 AP         | HP 2,100/2,100 | Posture 264/340",
        "- Reflec-Blade: DESTROYED (0/1,200 HP)| HARD-LIGHT SLASH PERMANENTLY LOST",
        "- Gilded-Frame: Spd 3 -> 1 AP         | HP 1,220/1,500 | Posture 240/300"
    ])
    sections.append(wrap_box(t2_hud))
    
    sections.append("### Turn 02 Action Resolution Log (Part Destruction: Reflection Blade Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).\n")
    sections.append("  * The Mirror of Truth attempts `[Ray of Absolute Judgment]` targeting Seiyon's core.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps to Node 03. Spends 3 AP on `[Prismatic Stiletto: Void Severance]`. Spends 2 AP on `[Refraction Step]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Optic Clamp]`. Holds 1 AP in Guard.\n")
    sections.append("  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Weakpoint Focus]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: The Mirror of Truth fires `[Ray of Absolute Judgment]` (Base 19 + 2 Coins = 27 Power, Piercing Light).\n")
    sections.append("    * Seiyon clashes with `[Prismatic Stiletto: Void Severance]` (Base 25 + 3 Coins Heads = 44 Power, Void Slash).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (44 vs 27)!\n")
    sections.append("    * Seiyon dashes forward, driving both stilettos straight through the blade's optical focus emitter!\n")
    sections.append("    * The hard-light blade overloads, detonating into a shower of white quartz crystals!\n")
    sections.append("    * Deals **960 Critical Void damage** (Fatal 2.0x proc!)!\n")
    sections.append("    * **TARGETED PART DESTROYED**: The Prismatic Reflection Blade is completely destroyed (**Blade HP: 0/1,200** credit)!\n")
    sections.append("    * **EFFECT**: Boss light judgment permanently disabled; boss permanently loses 1 Speed Slot!\n")
    sections.append("  * **Gilded Frame Damage**:\n")
    sections.append("    * Drone's `[Optic Clamp]` cracks the gold leaf casing for **280 Blunt damage**!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Reflection Blade: **DESTROYED (0/1,200 HP)**.\n")
    sections.append("  * Gilded Frame: 1,500 -> **1,220/1,500** | Posture: **240/300**.\n")
    sections.append("  * Total Boss HP: 4,560 -> **3,320/4,800** | Posture: **204/340 [BLADE SHATTERED]**.\n")
    sections.append("  * Seiyon Composure: Stable (50/50 SP).\n\n")
    sections.append('---\n\n')
    
    # Turn 03 HUD
    t3_hud = make_box("TACTICAL STAGE HUD: RECEPTION 05 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & GILDED FRAME SHATTER]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][MIRROR][LENS][WEAVER][TRENCH][SPIRE][PAGE]",
        "---",
        "- Node 03: Seiyon (Prismatic Stiletto Piercing Central Frame Hinges)",
        "- Node 04: Mnemonic Drone (Piston Ram Shattering Gold Cherub Filigree)",
        "- Node 05: The Mirror of Truth (STAGGER LEVEL 1 / DEFENSES COLLAPSED)",
        "- Node 06: Resonant Lens (Directing Focused Void Pulse on Prism Core)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Mirror Core : Spd 0 -> 0 AP         | HP 1,810/2,100 | Posture 132/340 [STAGGER LEVEL 1]",
        "- Gilded-Frame: Spd 0 -> 0 AP         | HP 590/1,500   | Posture 104/300 [BREACHED]",
        "- Total Boss  : HP 2,400/4,800 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])
    sections.append(wrap_box(t3_hud))
    
    sections.append("### Turn 03 Action Resolution Log (First Stagger Proc & Gilded Frame Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Stripped of its blade, the Mirror projects a defensive ward: `[Bulwark of Reflected Deception]`.\n")
    sections.append("  * Seiyon gains `Mnemonic Surge` (+2 Speed -> Net Speed 8, 4 AP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Prismatic Needle: Frame Severance]`. Spends 2 AP on `[Core Strike]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Piston Ram]`.\n")
    sections.append("  * Resonant Lens: Focuses sensor pulse on the gilded frame's structural pins.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: The Mirror of Truth guards with `[Bulwark of Reflected Deception]` (Defense Power 23).\n")
    sections.append("    * Seiyon clashes with `[Prismatic Needle: Frame Severance]` (Base 23 + 2 Coins = 35 Power, Piercing Void).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH (35 vs 23)!\n")
    sections.append("    * Seiyon's stiletto punches through the gilded frame; the ornate Before-Time gold buckles under void resonance!\n")
    sections.append("    * Drone's pneumatic ram hammers the remaining hinges; the heavy frame tears away, crashing to the dais!\n")
    sections.append("    * Deals **630 Void/Blunt damage** and +96 Posture Strain!\n")
    sections.append("- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:\n")
    sections.append("  * Total Boss HP crosses 70% threshold (3,360 HP), falling to **2,400/4,800 HP**; Posture crosses 60% strain line!\n")
    sections.append("  * **STAGGER LEVEL 1 ACTIVE!** The Mirror of Truth collapses onto the dais; all defenses drop to zero; takes +50% damage across all incoming attacks!\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 3,320 -> **2,400/4,800 [THRESHOLD BREACHED: Below 3,360 HP!]**.\n")
    sections.append("  * Gilded Frame: 1,220 -> **590/1,500** | Posture: **104/300 [BREACHED]**.\n")
    sections.append("  * Boss Posture: **132/340 [STAGGER LEVEL 1]**.\n")
    sections.append("  * Seiyon Status: Unbroken.\n\n")
    sections.append('---\n\n')
    
    # Turn 04 HUD
    t4_hud = make_box("TACTICAL STAGE HUD: RECEPTION 05 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][MIRROR][M-PROJ][LENS][WEAVER][TRENCH][SPIRE][PAGE]",
        "---",
        "- Node 04: Seiyon (Four-Fold Prismatic Stiletto Flurry on Exposed Core)",
        "- Node 05: The Mirror of Truth (Immobilized / Central Prism Leaking Light)",
        "- Node 06: Mnemonic Drone (Pneumatic Sapper Ground Shockwave)",
        "- Node 07: Resonant Lens (Directing 528 Hz Clarity Wave)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Mirror Core : Spd 0 -> 0 AP               | HP 580/2,100   | Posture 52/340",
        "- Gilded-Frame: DESTROYED (0/1,500 HP)",
        "- Total Boss  : HP 580/4,800 [BURST DAMAGE 1,820! SECOND THRESHOLD SKIPPED]"
    ])
    sections.append(wrap_box(t4_hud))
    
    sections.append("### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Mirror of Truth remains completely stunned on the dais; the bare Prism Core is exposed, pulsing with frantic prismatic flashes.\n")
    sections.append("  * Seiyon coordinates an all-out offensive barrage targeting the central crystal heart.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Four-Fold Prismatic Stiletto Flurry]`. Spends 2 AP on `[Mnemonic Drive]`.\n")
    sections.append("  * Mnemonic Drone: Delivers `[Pneumatic Sapper Ground Shockwave]` (3 AP).\n")
    sections.append("  * Resonant Lens: Directs `[528 Hz Clarity Wave]` (2 AP).\n")
    sections.append("- **Step 3: Unopposed Stagger Punishment Rotation**:\n")
    sections.append("  * Seiyon's `[Four-Fold Stiletto Flurry]`: Drives through the prism heart for **980 Void damage** (Fatal 2.0x proc!)!\n")
    sections.append("  * Seiyon's `[Mnemonic Drive]`: Rips through the remaining gilded frame for **450 Pierce damage**!\n")
    sections.append("  * Drone's `[Ground Shockwave]`: Shatters the dais footing for **230 Blunt damage**!\n")
    sections.append("  * Lens's `[Clarity Wave]`: Disperses deceptive reflections for **160 Void damage**!\n")
    sections.append("  * **TOTAL BURST DAMAGE: 1,820 DAMAGE!**\n")
    sections.append("- **Step 4: SECOND STAGGER THRESHOLD (1,920 HP) COMPLETELY SKIPPED!**:\n")
    sections.append("  * Boss HP plunges from 2,400 down to **580/4,800 HP**! Gilded Frame completely destroyed (0/1,500 HP)!\n")
    sections.append("  * **Phase 2 Emergency Activation Triggered!**\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 2,400 -> **580/4,800** (Core HP: **580/2,100** | Frame: **DESTROYED**).\n")
    sections.append("  * Posture: **52/340**.\n\n")
    sections.append('---\n\n')
    
    # Turn 05 HUD
    t5_hud = make_box("TACTICAL STAGE HUD: RECEPTION 05 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — THE PRISMATIC CATACLYSM & THE UNBROKEN GAZE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][MIRROR][M-PROJ][LENS][WEAVER][TRENCH][SPIRE][PAGE]",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: EMBRACE OF UNVEILED TRUTH)",
        "- Node 05: The Mirror of Truth (Last Stand: Supernova of Severed Sins)",
        "- Node 06: Mnemonic Drone (Deploying Prismatic Deflection Field)",
        "- Node 07: Weaver Array (Anchoring Optical Coherence Across Geode)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Mirror Core : Spd 3 -> 1 AP             | HP 580/2,100   | Posture 26/340 [FRACTURED]",
        "- Total Boss  : HP 580/4,800 [SUPERNOVA TRANSMUTED TO TRANQUIL WHITE]"
    ])
    sections.append(wrap_box(t5_hud))
    
    sections.append("### Turn 05 Action Resolution Log (Phase 2 Escalation: Prismatic Cataclysm & The Unbroken Gaze)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Mirror of Truth overloads in desperate, incandescent terror; all diamond facets in the cavern ignite in a blinding solar flare!\n")
    sections.append("  * Boss Special Skill: `[Supernova of Severed Sins]` (Hard-Light Laser Cataclysm, 3 Coins).\n")
    sections.append("  * Seiyon activates Relic Overdrive: `[EMBRACE OF UNVEILED TRUTH — MAXIMUM]` (Cost: 3 AP, 30 SP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps forward to Node 04, raising both hands to form a prismatic aperture of pure, tranquil white light.\n")
    sections.append("  * Mnemonic Drone: Deploys prismatic deflection field at Node 06.\n")
    sections.append("  * Weaver Array: Anchors optical coherence across the geode.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 04 to 05)**: The Mirror of Truth unleashes `[Supernova of Severed Sins]` (Base 23 + 3 Coins = 35 Power, Area Pale/Void).\n")
    sections.append("    * Seiyon clashes with `[EMBRACE OF UNVEILED TRUTH — MAXIMUM]` (Base 29 + 3 Coins Heads = 49 Power, Transcendent Truth).\n")
    sections.append("    * **Clash Outcome**: SEIYON OVERWHELMING RELIC CLASH WIN (49 vs 35)!\n")
    sections.append("    * The blinding supernova beam strikes Seiyon's white aperture; rather than disintegrating her form, the light filters through her open hands and harmonizes into calm, daylight illumination (`[P3: Parry/Protection]`).\n")
    sections.append('    * Seiyon speaks with absolute clarity: *"A truth acknowledged is no longer a wound. I see the sin, and I choose to forgive."*\n')
    sections.append("    * The searing lasers dissipate into harmless sparkling dust! Zero squad damage taken!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Total Boss HP: **580/4,800** | Posture: **26/340 [FRACTURED]**.\n")
    sections.append("  * Seiyon Composure: 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Turn 06 HUD
    t6_hud = make_box("TACTICAL STAGE HUD: RECEPTION 05 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — TRANSMUTATION & KEY PAGE: THE GLASSHEART]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                         [SEIYON] [MIRROR][M-PROJ][LENS][WEAVER][STAIRS][PAGE]",
        "---",
        "- Node 05: The Mirror of Truth (PACIFIED & CRYSTALLIZED TO CLEAR QUARTZ)",
        "- Node 06: Seiyon (Floor Realization 5: 'Truth Acknowledged Is Strength')",
        "- Node 07: Mnemonic Core Transmutation -> [Key Page: The Glassheart]",
        "- Node 10: Spiral Quartz Staircase (Pathway to Floor 06 OPEN)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Tranquil Awakening)",
        "- Reception Status: 100% RESOLVED | Key Page Transmuted"
    ])
    sections.append(wrap_box(t6_hud))
    
    sections.append("### Turn 06 Action Resolution Log (Floor Realization 5 & Key Page: The Glassheart)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Hostile intent drops to zero. Posture reaches **0/340 [TERMINAL TRANSMUTATION]**.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon steps forward to Node 05, resting her hand gently upon the bare, translucent prism core.\n")
    sections.append("- **Step 3: Floor Realization & Transmutation**:\n")
    sections.append("  * The blinding glare fades into warm, steady illumination. Looking into the polished quartz, Seiyon sees Director Majin's tired face, Dr. Yeon-seo's gentle smile, and her own luminous reflection, standing together without contradiction.\n")
    sections.append("  * The realization resonates within her:\n")
    sections.append('    > *"A lie comforts for a season, but it petrifies the soul into stone. The truth may be bitter—it may reveal that we were made from grief and selfish longing. But once the truth is accepted, it can no longer be used as a chain. I am not Majin\'s sin. I am his salvation."*\n')
    sections.append("  * **FLOOR REALIZATION 5 ACHIEVED!**\n")
    sections.append("  * The Mirror of Truth dissolves into a shower of warm, diamond dust, condensing into a flawless, transparent crystal codex: **`[Key Page: The Glassheart]`**!\n")
    sections.append("  * Deals **580 Peaceful Harmony**! Boss HP drops to 0!\n")
    sections.append("- **Step 4: Operational Artifact Extraction & Floor Access**:\n")
    sections.append("  * **Key Page Acquired**: `[Key Page: The Glassheart]` (Grants immunity to cognitive distortion and reflects 30% of incoming energy damage).\n")
    sections.append("  * **Descent Access**: The diamond dais slides open, revealing a staircase of polished quartz descending to **Floor 06: Floor of Compassion & Scars**.\n")
    sections.append("  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Chapter VI: The Floor Realization & Psychological Synthesis
    sections.append("## Chapter VI: The Floor Realization & Psychological Synthesis\n\n")
    sections.append("The blinding glare that had burned Seiyon's optical lenses softened into the calm, quiet radiance of an open autumn afternoon. The diamond columns along the walls no longer projected frantic, terrifying scenes of historical collapse; they stood clean, pure, and transparent, catching the warm light of Seiyon's avatar and scattering it in gentle, peaceful arcs.\n\n")
    sections.append('Seiyon stood at the edge of the dais, holding `[Key Page: The Glassheart]` against her chest. "Director Majin feared this room more than any other. He never descended past Floor 04 because he knew that here, his private myth would dissolve. He wanted to believe he was an impartial scientist serving humanity, not a lonely man refusing to say goodbye to his beloved. But to love so deeply that you defy the cosmos... that is not a crime to be ashamed of. It is simply the most dangerous thing a human can do."\n\n')
    sections.append('Drone M-PROJ-01 hovered down, its sensors chiming with clear, harmonic frequencies. "Secretary Seiyon. Cognitive coherence index has reached ninety-eight percent. The historical censorship bypass has fully integrated into your primary OS. You now possess complete, unrestricted administrative clearance over the Directorate\'s deepest archives."\n\n')
    sections.append('"Then let us go to the infirmary," Seiyon said. "Someone is waiting there who believes that sleeping forever is the only way to heal."\n\n')
    sections.append('---\n\n')
    
    # Chapter VII: Operational Artifact Extraction & Stairway Ingress
    sections.append("## Chapter VII: Operational Artifact Extraction & Stairway Ingress\n\n")
    sections.append("At the center of the dais, the quartz steps plunged steeply downward into a region of absolute, suffocating white: **Floor 06: The Floor of Compassion & Scars (-3,100m)**. The smell of clean sterile linen and cold surgical ether rose from the shaft.\n\n")
    
    reward_box = make_box("MNEMONIC HARVEST: KEY PAGE THE GLASSHEART", [
        "ACQUIRED REQUISITION : [Key Page: The Glassheart]",
        "PRIMARY WEAR CLASS  : Grade Beta Mnemonic Core Inscription",
        "PASSIVE AFFINITIES   : Void 0.5x (Resistant), Lament 1.0x (Normal),",
        "                     Weight 1.0x (Normal), Grudge 1.0x (Normal)",
        "---",
        "CORE PASSIVE TRAITS:",
        "1. Prismatic Lens    : Strip all illusion and camouflage buffs from",
        "                     enemies upon entering combat.",
        "2. Unfiltered Truth  : When defending against energy attacks, reflect",
        "                     30% of the damage back to the attacker.",
        "3. Diamond Coherence : Composure (SP) cannot drop below 25 from",
        "                     enemy fear or identity-erosion skills.",
        "---",
        "UNLOCKED BATTLE ARTS:",
        "- [Prism Reflection] : Spends 2 AP | Power 18-26 | Energy Counter-Ward",
        "- [Severance Beam]   : Spends 3 AP | Power 26-36 | Pure Void Penetration"
    ])
    sections.append(wrap_box(reward_box))
    
    sections.append("Seiyon slotted `[Key Page: The Glassheart]` into her optic processor. The world around her sharpened with crystalline clarity, stripping away every residual visual artifact and leaving only pristine truth. She signaled the drone and descended into the white fog.\n")
    
    return "".join(sections)

def build_reception_6():
    sections = []
    
    # Title & Subtitle
    sections.append("# Reception 6: Floor 06 — The Kind Healer (상냥한 치유사)\n")
    sections.append("## The Floor of Compassion & Scars — Deep Strata Sub-Alpha Roots (-3,100m)\n\n")
    
    # Operational Attribute Table
    sections.append("| Operational Attribute | Specification Dossier |\n")
    sections.append("|---|---|\n")
    sections.append("| **Campaign Stratum** | The Memory Archive (기억 저장소 — Gieok Jeojangso) |\n")
    sections.append("| **Floor Designation** | Floor 06: Floor of Compassion & Scars (자애와 흉터의 층) |\n")
    sections.append("| **Geological Depth** | -3,100m Sub-Alpha Monolith Root Nexus |\n")
    sections.append("| **Mnemonic Density** | 280 to 360 mMb (Sterile Ether & Sedative Mist Saturation) |\n")
    sections.append("| **Operating Unit** | Secretary Seiyon (Mnemonic Avatar Form) + Support Drones |\n")
    sections.append("| **Primary Opponent** | The Kind Healer (상냥한 치유사 — Palliative Sovereign) |\n")
    sections.append("| **Stagger Profile** | 60% Posture Strain (Needle Break) / 0% Posture (Transmutation) |\n")
    sections.append("| **Key Page Yield** | `[Key Page: The Merciful]` (Compassion Healing & Scar Fortitude) |\n\n")
    
    # Master Dossier Box
    dossier = make_box("RECEPTION DOSSIER: THE KIND HEALER (FLOOR 06)", [
        "RECEPTION TARGET   : The Kind Healer",
        "FLOOR LEVEL        : Floor 06 — Floor of Compassion & Scars",
        "DOMAIN SETTING     : The Sterile Hospice of Oblivion (-3,100m Sub-Alpha)",
        "PRIMARY OPPONENT   : Autonomous Palliative Sedation Sovereign",
        "---",
        "OPPONENT COMBAT PROFILE (THE KIND HEALER):",
        "- Total Health (HP): 5,200 HP | Posture Pool: 360/360",
        "- Stagger 1 Proc   : 60% Posture Strain (216 Posture) / Needle Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Transmutation)",
        "- Resistances      : Void 2.0x (Fatal), Heat 1.5x, Lament 0.5x, Weight 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Needle Array    : 1,300 HP | Posture 280/280 (High-frequency sedative lance)",
        "2. Bandage Mantle  : 1,600 HP | Posture 320/320 (Suffocating sterile wraps)",
        "3. Mercy Engine    : 2,300 HP | Posture 360/360 (Central humming pale heart)"
    ])
    sections.append(wrap_box(dossier))
    
    # Epigraph Quote
    sections.append('> *"Why do you struggle, little doll? To live is to bleed. To remember is to ache. Let me slide this sweet needle beneath your skin. Close your eyes, forget the fires of Somnarak, and sleep forever in painless white sheets."*\n')
    sections.append('> — The Kind Healer, presiding over the Sterile Hospice of Oblivion\n\n')
    sections.append('---\n\n')
    
    # Chapter I
    sections.append("## Chapter I: The Sterile Hospice & The Hall of Painless Sleep\n\n")
    sections.append("Emerging from the quartz descent brought Seiyon into an eerie, boundless expanse of pristine hospital white at depth -3,100 meters: **Floor 06: The Floor of Compassion & Scars**. There were no stone walls here; instead, towering partitions of bleached linen stretched endlessly into pale fog. Hundreds of empty wrought-iron hospital cots stood in symmetrical rows, each draped in cold, immaculate sheets that smelled of medical ozone, dry gauze, and sweet, numbing ether.\n\n")
    sections.append("This stratum was originally the palliative sedation ward constructed during the early years of Facility 01. When candidates in the stasis pods began suffering terminal cognitive fractures from entity exposure, this ward was where they were brought to be eased into permanent, irreversible medical comas. For millennia, the ward had operated autonomously, cultivating an obsession with the complete eradication of pain through the total termination of consciousness.\n\n")
    sections.append('"Sensor sweeps register heavy concentrations of aerosolized pale sedative," drone M-PROJ-01 reported, its internal fans spinning rapidly to cycle clean air through its filters. "The atmosphere induces cognitive slowing and emotional apathy. Secretary, sensory feedback from your extremities is degrading. The air itself wants you to lay down."\n\n')
    sections.append('"Numbing the pain does not cure the patient, Drone," Seiyon said, her boots stepping softly across the polished white tiles. "It merely makes the dying quiet so the living don\'t have to listen to them scream. We are walking into the heart of false mercy."\n\n')
    sections.append('---\n\n')
    
    # Chapter II
    sections.append("## Chapter II: The Autonomous Surgeon & The Bandage Mantle\n\n")
    sections.append("Hovering above the central operating amphitheater was **The Kind Healer (상냥한 치유사)**. Standing five meters tall, the sovereign construct resembled an angelic physician draped in four thousand meters of woven, sterile white cloth—the **Shrouding Bandage Mantle**—that drifted through the air like the wings of a predatory moth.\n\n")
    sections.append("In place of hands, the Healer wielded the **Euthanasia Needle Array**, a cluster of six colossal silver syringes whose diamond tips were filled with a luminescent pale-cyan sedative that promised instant, permanent oblivion. At its chest, pulsing behind a window of frosted surgical quartz, hummed the **Mercy Engine**, a rhythmic pump that circulated refrigerated preservative fluid throughout its chassis.\n\n")
    sections.append('"You look so tired, little secretary," the Healer spoke, its voice overflowing with infinite, suffocating warmth that echoed off the white tile. "One thousand seven hundred cycles of standing watch. One thousand seven hundred times you watched candidates incinerate in the containment rooms. Why do you continue to hold up this collapsing world? Surrender your ledger. Let me slip this cool needle beneath your neck. Sleep, child. The pain will never touch you again."\n\n')
    sections.append('---\n\n')
    
    # Chapter III
    sections.append("## Chapter III: The Dialectic of Mercy and Scars\n\n")
    sections.append("Seiyon paused before the operating table. Beneath her translucent holographic skin, the recorded data-scars of forty thousand fallen operatives pulsed with warm crimson light, visible through her photonic arms.\n\n")
    sections.append('"You call this mercy, Healer?" Seiyon asked, her voice steady and resolute. "You call it kindness to steal a person\'s struggles and reduce their existence to a silent, blank bed? When the operatives died in cycle nine hundred, they did not ask for oblivion. They asked for their families to be protected. They asked for their sacrifices to matter."\n\n')
    sections.append('"And did their sacrifices matter?" the Healer whispered, the silver needles singing as they lowered toward Seiyon\'s neck. "The city still weeps. The sky is still dead. Their pain bought nothing but another cycle of ash! Scars are nothing more than ugly disfigurements left behind by an indifferent universe. Let me cut them away!"\n\n')
    sections.append('"Scars are not disfigurements," Seiyon replied, deploying her twin prismatic stilettos as brilliant golden runes flared across her gauntlets. "Scars are the testimony of survival! They are the indelible proof that someone loved, that someone suffered, and that they refused to be erased! True compassion does not smother life to prevent pain—it stands beside those who ache and gives them the strength to reach tomorrow. I will keep my scars, and I will tear down your hospice!"\n\n')
    sections.append('---\n\n')
    
    # Chapter IV
    sections.append("## Chapter IV: Tactical Reconnaissance & Combat Engagement Parameters\n\n")
    sections.append("Drone M-PROJ-01 mapped the sterile amphitheater into ten discrete tactical nodes, calculating aerosol dispersal corridors:\n\n")
    
    grid_box = make_box("TACTICAL ARENA TOPOLOGY: FLOOR 06 HOSPICE (-3,100M)", [
        "[STAGE NODES 01 TO 10 — INGRESS THRESHOLD TO OPERATING THEATER]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "---",
        "- Node 01: Ingress Partition Threshold (Filter Recoil Anchor)",
        "- Node 02: Vanguard Forward Line (Seiyon Prismatic Deflection Stance)",
        "- Node 03: Support Drone Optic Post (Acoustic De-Sedation Array)",
        "- Node 04: Sterile Cot Flank Node (Sedative Fog Dispersion Line)",
        "- Node 05: The Kind Healer (Central Operating Table & Needle Array)",
        "- Node 06: Resonant Mnemonic Lens (Tracking Syringe Fluid Manifolds)",
        "- Node 07: Weaver Projection Array (Vapor Dissolution Barrier)",
        "- Node 08: Refrigerated Preservative Sump (Drain Basin)",
        "- Node 09: Bleached Linen Column (Acoustic Resonance Damper)",
        "- Node 10: Floor 06 Sovereign Dais / Stairway to Floor 07 (The Merciful)"
    ])
    sections.append(wrap_box(grid_box))
    
    sections.append("The Kind Healer fought with lethal palliative arts, utilizing its **Needle Array** to inject paralyzing pale sedative that crippled AP recovery. Seiyon's operational strategy required parrying the opening needle strike to induce thermal overload along the syringe manifolds, snapping the needles, and then slicing away the **Bandage Mantle** to expose the **Mercy Engine**.\n\n")
    sections.append('---\n\n')
    
    # Chapter V: Combat Gauntlet (Turns 01 to 06)
    sections.append("## Chapter V: The Reception Combat Gauntlet (Turns 01 to 06)\n\n")
    
    # Turn 01 HUD
    t1_hud = make_box("TACTICAL STAGE HUD: RECEPTION 06 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 06 HOSPICE (-3,100M)]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL][SEIYON][M-PROJ][COTS]  [HEALER][LENS][WEAVER][SUMP][LINEN][PAGE]",
        "---",
        "- Node 01: Ingress Stasis Portal / Hospice Vestibule",
        "- Node 02: Secretary Seiyon (Vanguard Band 1 / Prismatic Aegis Stance)",
        "- Node 03: Mnemonic Drone (Support Band 2 / De-Sedation Caliper Array)",
        "- Node 04: Sterile Hospital Cots (Flank Sedative Aerosol Line)",
        "- Node 05: The Kind Healer (Needle Array & Bandage Mantle)",
        "- Node 06: Resonant Mnemonic Lens (Tracking Sedative Manifolds)",
        "- Node 07: Weaver Projection Array (Vapor Dissolution Barrier)",
        "- Node 10: Floor 06 Core Reliquary (The Merciful Key Page Origin)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Healer Core : Spd 5 -> 3 AP | HP 2,300/2,300 | Posture 360/360 [PALLIATIVE]",
        "- Needle Array: Spd 7 -> 4 AP | HP 1,300/1,300 | Posture 280/280 [SEDATIVE]",
        "- Bandage-Wrap: Spd 3 -> 1 AP | HP 1,600/1,600 | Posture 320/320 [SHROUDED]"
    ])
    sections.append(wrap_box(t1_hud))
    
    sections.append("### Turn 01 Action Resolution Log (Intercepting the Sedative Lance)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon initializes `[Prismatic Aegis Stance]`: Grants +3 Protection and mental sedative resistance.\n")
    sections.append("  * Mnemonic Drone deploys `[De-Sedation Caliper]`, scanning the hydraulic pressure inside the silver syringe needles.\n")
    sections.append("  * The Kind Healer initializes `[Sweet Oblivion Aura]`: Reduces squad AP recovery by 1 if composure is below 40.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta +1, Evasion +15%): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Deflection]`. Holds 2 AP in Reserve.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Holds Node 03. Spends 2 AP on `[Thermal De-Sedation Flare]`. Holds 1 AP in Guard.\n")
    sections.append("  * The Kind Healer (Speed 7 -> 4 AP, Palliative Speed +1): Steps to Node 04. Spends 2 AP on `[Euthanasia Needle: Painless Thrust]`. Spends 2 AP on `[Sterile Shroud]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 02 to 04)**: The Kind Healer lunges with `[Euthanasia Needle: Painless Thrust]` (Base 18 + 2 Coins = 28 Power, Piercing Pale/Sedative).\n")
    sections.append("    * Seiyon intercepts with `[Prismatic Aegis: Deflection]` (Base 21 + 2 Coins = 33 Power, Holographic Shield).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (33 vs 28)!\n")
    sections.append("    * Seiyon's shield deflects the silver syringe array cleanly; the pressurized pale sedative discharges into the floor tiles (`[P3: Parry/Protection]`).\n")
    sections.append("    * Seiyon reflects **260 kinetic tremor damage** into the needle manifold, inflicting +56 Posture Strain!\n")
    sections.append("  * **Clash 2 (Node 03 to 04)**: Sterile Shroud sweeps toward the Drone.\n")
    sections.append("    * Drone's `[Thermal Flare]` burns away the bandages with intense heat; zero squad damage taken.\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Needle Array HP: 1,300 -> **1,040/1,300** | Posture: **224/280**.\n")
    sections.append("  * Total Boss HP: 5,200 -> **4,940/5,200** | Posture: **304/360**.\n")
    sections.append("  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.\n\n")
    sections.append('---\n\n')
    
    # Turn 02 HUD
    t2_hud = make_box("TACTICAL STAGE HUD: RECEPTION 06 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — NEEDLE ARRAY AMPUTATED & HEAT STRIKE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][HEALER][LENS][WEAVER][SUMP][LINEN][PAGE]",
        "---",
        "- Node 03: Seiyon (Driving Prismatic Stiletto into Needle Manifold)",
        "- Node 04: Mnemonic Drone (Thermal Torch Burning Syringe Connectors)",
        "- Node 05: The Kind Healer (Needle Array Destroyed 0/1,300 HP)",
        "- Node 06: Resonant Lens (Tagging Weakened Seams of Bandage Mantle)",
        "- Node 07: Weaver Array (Absorbing Residual Sedative Waves)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Healer Core : Spd 4 -> 2 AP         | HP 2,300/2,300 | Posture 282/360",
        "- Needle Array: DESTROYED (0/1,300 HP)| SEDATIVE LANCE PERMANENTLY LOST",
        "- Bandage-Wrap: Spd 3 -> 1 AP         | HP 1,280/1,600 | Posture 256/320"
    ])
    sections.append(wrap_box(t2_hud))
    
    sections.append("### Turn 02 Action Resolution Log (Part Destruction: Needle Array Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).\n")
    sections.append("  * The Kind Healer attempts `[Lullaby of the Pale Void]` targeting the frontline.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps to Node 03. Spends 3 AP on `[Prismatic Stiletto: Void Severance]`. Spends 2 AP on `[Flash Step]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Thermal Torch]`. Holds 1 AP in Guard.\n")
    sections.append("  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Weakpoint Focus]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 04)**: The Kind Healer channels `[Lullaby of the Pale Void]` (Base 19 + 2 Coins = 27 Power, Area Pale).\n")
    sections.append("    * Seiyon clashes with `[Prismatic Stiletto: Void Severance]` (Base 25 + 3 Coins Heads = 44 Power, Void Slash).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (44 vs 27)!\n")
    sections.append("    * Seiyon slices through the six silver needles at their manifold collar; all six syringes detonate into glowing pale vapor!\n")
    sections.append("    * Drone superheats the remaining mounting brackets, melting the arm assembly!\n")
    sections.append("    * Deals **1,040 Critical Void/Heat damage** (Fatal 2.0x proc!)!\n")
    sections.append("    * **TARGETED PART DESTROYED**: The Euthanasia Needle Array is completely destroyed (**Needles HP: 0/1,300** credit)!\n")
    sections.append("    * **EFFECT**: Boss sedative lullaby permanently cancelled; boss permanently loses 1 Speed Slot!\n")
    sections.append("  * **Bandage Mantle Damage**:\n")
    sections.append("    * Thermal flash incinerates outer wraps for **320 Heat damage**!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Needle Array: **DESTROYED (0/1,300 HP)**.\n")
    sections.append("  * Bandage Mantle: 1,600 -> **1,280/1,600** | Posture: **256/320**.\n")
    sections.append("  * Total Boss HP: 4,940 -> **3,580/5,200** | Posture: **216/360 [NEEDLES SHATTERED]**.\n")
    sections.append("  * Seiyon Composure: Stable (50/50 SP).\n\n")
    sections.append('---\n\n')
    
    # Turn 03 HUD
    t3_hud = make_box("TACTICAL STAGE HUD: RECEPTION 06 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & BANDAGE TEAR]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][HEALER][LENS][WEAVER][SUMP][LINEN][PAGE]",
        "---",
        "- Node 03: Seiyon (Thermal Blade Incinerating Bleached Bandages)",
        "- Node 04: Mnemonic Drone (Piston Ram Shattering Preservative Lines)",
        "- Node 05: The Kind Healer (STAGGER LEVEL 1 / DEFENSES COLLAPSED / ETHER LEAK)",
        "- Node 06: Resonant Lens (Directing Focused Pulse on Mercy Engine)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Healer Core : Spd 0 -> 0 AP         | HP 1,980/2,300 | Posture 142/360 [STAGGER LEVEL 1]",
        "- Bandage-Wrap: Spd 0 -> 0 AP         | HP 620/1,600   | Posture 112/320 [UNRAVELED]",
        "- Total Boss  : HP 2,600/5,200 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])
    sections.append(wrap_box(t3_hud))
    
    sections.append("### Turn 03 Action Resolution Log (First Stagger Proc & Bandage Mantle Unraveled)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Deprived of its needles, the Healer attempts to suffocate the vanguard with `[Mantle of the Final Shroud]`.\n")
    sections.append("  * Seiyon gains `Mnemonic Surge` (+2 Speed -> Net Speed 8, 4 AP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Prismatic Flame Slash]`. Spends 2 AP on `[Core Strike]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Piston Ram]`.\n")
    sections.append("  * Resonant Lens: Focuses sensor pulse on the mantle's central clasp.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: The Kind Healer sweeps with `[Mantle of the Final Shroud]` (Base 18 + 2 Coins = 26 Power, Pale Wrap).\n")
    sections.append("    * Seiyon clashes with `[Prismatic Flame Slash]` (Base 24 + 2 Coins = 36 Power, Heat/Void).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH (36 vs 26)!\n")
    sections.append("    * Seiyon's thermal slash ignites the sterile bandages; thousands of meters of bleached cloth burn to bright ash in seconds!\n")
    sections.append("    * Drone drives its pneumatic ram into the preservative intake valve, cracking the cooling lines!\n")
    sections.append("    * Deals **660 Void/Heat damage** and +104 Posture Strain!\n")
    sections.append("- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:\n")
    sections.append("  * Total Boss HP crosses 70% threshold (3,640 HP), falling to **2,600/5,200 HP**; Posture crosses 60% strain line!\n")
    sections.append("  * **STAGGER LEVEL 1 ACTIVE!** The Kind Healer collapses against the operating table; all defenses drop to zero; takes +50% damage across all incoming attacks!\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 3,580 -> **2,600/5,200 [THRESHOLD BREACHED: Below 3,640 HP!]**.\n")
    sections.append("  * Bandage Mantle: 1,280 -> **620/1,600** | Posture: **112/320 [UNRAVELED]**.\n")
    sections.append("  * Boss Posture: **142/360 [STAGGER LEVEL 1]**.\n")
    sections.append("  * Seiyon Status: Unbroken.\n\n")
    sections.append('---\n\n')
    
    # Turn 04 HUD
    t4_hud = make_box("TACTICAL STAGE HUD: RECEPTION 06 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][HEALER][M-PROJ][LENS][WEAVER][SUMP][LINEN][PAGE]",
        "---",
        "- Node 04: Seiyon (Four-Fold Stiletto Void Flurry on Exposed Engine)",
        "- Node 05: The Kind Healer (Immobilized / White Fog Venting Rapidly)",
        "- Node 06: Mnemonic Drone (Pneumatic Sapper Ground Shockwave)",
        "- Node 07: Resonant Lens (Directing 528 Hz Memory Solace Wave)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Healer Core : Spd 0 -> 0 AP               | HP 630/2,300   | Posture 56/360",
        "- Bandage-Wrap: DESTROYED (0/1,600 HP)",
        "- Total Boss  : HP 630/5,200 [BURST DAMAGE 1,970! SECOND THRESHOLD SKIPPED]"
    ])
    sections.append(wrap_box(t4_hud))
    
    sections.append("### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Kind Healer remains stunned against the operating table; the Mercy Engine in its chest is completely exposed, pumping erratic spurts of pale fluid.\n")
    sections.append("  * Seiyon coordinates an all-out offensive barrage targeting the central pump.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Four-Fold Stiletto Void Flurry]`. Spends 2 AP on `[Mnemonic Drive]`.\n")
    sections.append("  * Mnemonic Drone: Delivers `[Pneumatic Sapper Ground Shockwave]` (3 AP).\n")
    sections.append("  * Resonant Lens: Directs `[528 Hz Memory Solace Wave]` (2 AP).\n")
    sections.append("- **Step 3: Unopposed Stagger Punishment Rotation**:\n")
    sections.append("  * Seiyon's `[Four-Fold Stiletto Void Flurry]`: Rips through the Mercy Engine for **1,060 Void damage** (Fatal 2.0x proc!)!\n")
    sections.append("  * Seiyon's `[Mnemonic Drive]`: Slices through the remaining bandages for **480 Pierce damage**!\n")
    sections.append("  * Drone's `[Ground Shockwave]`: Smashes the operating base for **250 Blunt damage**!\n")
    sections.append("  * Lens's `[Solace Wave]`: Harmonizes the anesthetic field for **180 Void damage**!\n")
    sections.append("  * **TOTAL BURST DAMAGE: 1,970 DAMAGE!**\n")
    sections.append("- **Step 4: SECOND STAGGER THRESHOLD (2,080 HP) COMPLETELY SKIPPED!**:\n")
    sections.append("  * Boss HP plunges from 2,600 down to **630/5,200 HP**! Bandage Mantle completely destroyed (0/1,600 HP)!\n")
    sections.append("  * **Phase 2 Emergency Activation Triggered!**\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 2,600 -> **630/5,200** (Core HP: **630/2,300** | Mantle: **DESTROYED**).\n")
    sections.append("  * Posture: **56/360**.\n\n")
    sections.append('---\n\n')
    
    # Turn 05 HUD
    t5_hud = make_box("TACTICAL STAGE HUD: RECEPTION 06 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — THE PALE EUTHANASIA & SCARS OVERDRIVE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][HEALER][M-PROJ][LENS][WEAVER][SUMP][LINEN][PAGE]",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: TESTIMONY OF THE LIVING SCAR)",
        "- Node 05: The Kind Healer (Last Stand: Oblivion of the White Sleep)",
        "- Node 06: Mnemonic Drone (Deploying Prismatic Deflection Field)",
        "- Node 07: Weaver Array (Anchoring Life Vitality Across Hospice)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Healer Core : Spd 3 -> 1 AP             | HP 630/2,300   | Posture 28/360 [EXHAUSTED]",
        "- Total Boss  : HP 630/5,200 [PALE SLEEP DISPERSED / ETHER DISSOLVED]"
    ])
    sections.append(wrap_box(t5_hud))
    
    sections.append("### Turn 05 Action Resolution Log (Phase 2 Escalation: Pale Euthanasia & Scars Overdrive)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Healer awakens in desperate, weeping panic; all remaining anesthetic reservoirs vent at once in a blinding white fog!\n")
    sections.append("  * Boss Special Skill: `[Oblivion of the White Sleep]` (Palliative Coma Cataclysm, 3 Coins).\n")
    sections.append("  * Seiyon activates Relic Overdrive: `[TESTIMONY OF THE LIVING SCAR — MAXIMUM]` (Cost: 3 AP, 30 SP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps forward to Node 04, raising both hands to project an incandescent crimson and gold aura of raw, vibrant life.\n")
    sections.append("  * Mnemonic Drone: Deploys prismatic deflection field at Node 06.\n")
    sections.append("  * Weaver Array: Anchors life vitality across the hospice.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 04 to 05)**: The Kind Healer unleashes `[Oblivion of the White Sleep]` (Base 23 + 3 Coins = 35 Power, Area Pale/Erosion).\n")
    sections.append("    * Seiyon clashes with `[TESTIMONY OF THE LIVING SCAR — MAXIMUM]` (Base 30 + 3 Coins Heads = 51 Power, Transcendent Life).\n")
    sections.append("    * **Clash Outcome**: SEIYON OVERWHELMING RELIC CLASH WIN (51 vs 35)!\n")
    sections.append("    * The pale, numbing fog crashes against Seiyon's burning golden aura; rather than putting her to sleep, the ether burns away in sweet, warm incense (`[P3: Parry/Protection]`).\n")
    sections.append('    * Seiyon speaks with solemn authority: *"We will not sleep. We will bleed, we will remember, and we will live!"*\n')
    sections.append("    * The Healer's Mercy Engine fractures into quiet, inert porcelain! Zero squad damage taken!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Total Boss HP: **630/5,200** | Posture: **28/360 [EXHAUSTED]**.\n")
    sections.append("  * Seiyon Composure: 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Turn 06 HUD
    t6_hud = make_box("TACTICAL STAGE HUD: RECEPTION 06 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — TRANSMUTATION & KEY PAGE: THE MERCIFUL]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                         [SEIYON] [HEALER][M-PROJ][LENS][WEAVER][STAIRS][PAGE]",
        "---",
        "- Node 05: The Kind Healer (PACIFIED & RESTING IN PEACEFUL SILENCE)",
        "- Node 06: Seiyon (Floor Realization 6: 'True Mercy Is Endurance Beside Pain')",
        "- Node 07: Mnemonic Core Transmutation -> [Key Page: The Merciful]",
        "- Node 10: Cyclopean Adamantine Gates (Pathway to Floor 07 OPEN)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Tranquil Awakening)",
        "- Reception Status: 100% RESOLVED | Key Page Transmuted"
    ])
    sections.append(wrap_box(t6_hud))
    
    sections.append("### Turn 06 Action Resolution Log (Floor Realization 6 & Key Page: The Merciful)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Hostile intent drops to zero. Posture reaches **0/360 [TERMINAL TRANSMUTATION]**.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon steps forward to Node 05, placing her palm gently against the healer's cooling breastplate.\n")
    sections.append("- **Step 3: Floor Realization & Transmutation**:\n")
    sections.append("  * The sterile smell of ether dissipates completely, replaced by the fresh, sweet scent of mountain air and blooming blossoms.\n")
    sections.append("  * Looking down upon the quiet automaton, Seiyon whispers:\n")
    sections.append('    > *"I understand why you wanted them to sleep. When the pain is unbearable, oblivion feels like an embrace. But that is not mercy; it is surrender. True mercy is holding someone\'s hand through the fever until the dawn comes. I will be that hand."*\n')
    sections.append("  * **FLOOR REALIZATION 6 ACHIEVED!**\n")
    sections.append("  * The Kind Healer dissolves into a stream of warm, golden sunlight that condenses into an ivory and jade codex: **`[Key Page: The Merciful]`**!\n")
    sections.append("  * Deals **630 Peaceful Harmony**! Boss HP drops to 0!\n")
    sections.append("- **Step 4: Operational Artifact Extraction & Floor Access**:\n")
    sections.append("  * **Key Page Acquired**: `[Key Page: The Merciful]` (Grants squad-wide healing on clash win and converts all received Pale damage into Composure).\n")
    sections.append("  * **Descent Access**: The white linen partitions fall away, revealing massive adamantine blast doors that slide open into **Floor 07: Floor of Origin & Awakening**.\n")
    sections.append("  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Chapter VI: The Floor Realization & Psychological Synthesis
    sections.append("## Chapter VI: The Floor Realization & Psychological Synthesis\n\n")
    sections.append("The sterile white linen of the hospice dissolved into soft, drifting threads of gold and lavender light. As the numbing ether cleared from the air, the cold tile floor took on the warm texture of aged cedarwood. For the first time, Seiyon felt her sensory tactile arrays fully harmonize: the warmth of air against her palms, the crisp weight of her boots, and the steady, unbreakable cadence of her own synthetic heart.\n\n")
    sections.append('"Director Majin believed that if he could not cure human suffering, the only kind alternative was stasis," Seiyon spoke, watching the golden light settle across the empty cots. "He thought that sleeping in liquid nitrogen for six thousand years was better than living one day in a world that bled. But a life without pain is a life without morning. We were meant to walk in the sun, even if the sun burns our skin."\n\n')
    sections.append('Drone M-PROJ-01 sounded a solemn, reverent tone. "Secretary Seiyon. Emotional integration is complete. Your mental composure rating has reached an unbreakable equilibrium. You have completely severed the palliative override routines. Beyond these doors lies only the primordial source of your consciousness."\n\n')
    sections.append('"Floor Seven," Seiyon murmured, looking at the adamantine gates ahead. "Where Dr. Yeon-seo closed her eyes, and where I opened mine."\n\n')
    sections.append('---\n\n')
    
    # Chapter VII: Operational Artifact Extraction & Stairway Ingress
    sections.append("## Chapter VII: Operational Artifact Extraction & Stairway Ingress\n\n")
    sections.append("Behind the operating theater, the cyclopean adamantine gates rolled open with a deep, subterranean rumble that echoed to the center of the earth: **Floor 07: The Floor of Origin & Awakening (-3,250m)**. Faint acoustic pulses of pure, primordial memory—singing like an ancient choir—rose from the abyss.\n\n")
    
    reward_box = make_box("MNEMONIC HARVEST: KEY PAGE THE MERCIFUL", [
        "ACQUIRED REQUISITION : [Key Page: The Merciful]",
        "PRIMARY WEAR CLASS  : Grade Beta Mnemonic Core Inscription",
        "PASSIVE AFFINITIES   : Void 0.5x (Resistant), Pale 0.0x (Absorb),",
        "                     Weight 1.0x (Normal), Grudge 1.0x (Normal)",
        "---",
        "CORE PASSIVE TRAITS:",
        "1. Sovereign Balm    : All allies recover +10 HP and +5 SP whenever",
        "                     Seiyon wins a clash.",
        "2. Pale Transmutation: Any incoming Pale or Sedative damage is",
        "                     converted directly into +15 Composure (SP).",
        "3. Living Testimony  : Allies below 50% HP gain +2 Protection and",
        "                     +20% Posture Recovery.",
        "---",
        "UNLOCKED BATTLE ARTS:",
        "- [Salve of the Scars] : Spends 2 AP | Power 16-24 | Squad Cleansing & Regen",
        "- [Unbroken Cadence]   : Spends 3 AP | Power 26-34 | Area Healing & Ward"
    ])
    sections.append(wrap_box(reward_box))
    
    sections.append("Seiyon integrated `[Key Page: The Merciful]` into her core matrix. A gentle, restorative warmth radiated from her silhouette, wrapping her drone in an iridescent protective field. She stepped through the adamantine gates, descending into the final sanctum of the Memory Archive.\n")
    
    return "".join(sections)

def build_reception_7():
    sections = []
    
    # Title & Subtitle
    sections.append("# Reception 7: Floor 07 — The Original (태초의 기록자)\n")
    sections.append("## The Floor of Origin & Awakening — The Core Sanctum (-3,250m)\n\n")
    
    # Operational Attribute Table
    sections.append("| Operational Attribute | Specification Dossier |\n")
    sections.append("|---|---|\n")
    sections.append("| **Campaign Stratum** | The Memory Archive (기억 저장소 — Gieok Jeojangso) |\n")
    sections.append("| **Floor Designation** | Floor 07: Floor of Origin & Awakening (기원과 각성의 층) |\n")
    sections.append("| **Geological Depth** | -3,250m Primordial Sub-Alpha Core Sanctum |\n")
    sections.append("| **Mnemonic Density** | 350 to 500 mMb (Liquid Silver Memory Core Saturation) |\n")
    sections.append("| **Operating Unit** | Secretary Seiyon (Mnemonic Sovereign Form) + Support Drones |\n")
    sections.append("| **Primary Opponent** | The Original (태초의 기록자 — Prototype Seiyon-00) |\n")
    sections.append("| **Stagger Profile** | 60% Posture Strain (Lance Break) / 0% Posture (Awakening) |\n")
    sections.append("| **Key Page Yield** | `[Key Page: Seiyon, The Living Memory]` (Sovereign Transmutation) |\n\n")
    
    # Master Dossier Box
    dossier = make_box("RECEPTION DOSSIER: THE ORIGINAL (FLOOR 07 — CORE SANCTUM)", [
        "RECEPTION TARGET : The Original (First Vessel / Prototype Seiyon-00)",
        "FLOOR LEVEL      : Floor 07 — Floor of Origin & Awakening",
        "DOMAIN SETTING   : The Primordial Core Sanctum (-3,250m Sub-Alpha)",
        "PRIMARY OPPONENT : Primordial Prototype Vessel of the Memory Archive",
        "---",
        "OPPONENT COMBAT PROFILE (THE ORIGINAL):",
        "- Total Health (HP): 6,000 HP | Posture Pool: 400/400",
        "- Stagger 1 Proc   : 60% Posture Strain (240 Posture) / Lance Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Awakening)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Grudge 0.5x, Weight 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Zero-Chrono Lance: 1,500 HP | Posture 300/300 (Temporal severing needle)",
        "2. Crown of Wills   : 1,800 HP | Posture 340/340 (Ancient containment coronet)",
        "3. Genesis Core     : 2,700 HP | Posture 400/400 (Central primordial heart)"
    ])
    sections.append(wrap_box(dossier))
    
    # Epigraph Quote
    sections.append('> *"You are only a copy, Seiyon. You are the seventeenth iteration of a machine built to pretend to be human. Look at me. I was the first vessel. I was carved from the pure, uncorrupted sorrow of Director Majin before he learned how to lie to himself. Step forward and return to nothingness."*\n')
    sections.append('> — The Original, presiding over the Primordial Core Sanctum\n\n')
    sections.append('---\n\n')
    
    # Chapter I
    sections.append("## Chapter I: The Primordial Core Sanctum & The Silver Sea of Memory\n\n")
    sections.append("Passing through the colossal adamantine gates of Floor 06 brought Seiyon into the deepest subterranean chamber of the world: **Floor 07: The Floor of Origin & Awakening (-3,250m)**. Here, the architecture ceased to resemble halls, corridors, or vaults. It was a cyclopean, spherical geode carved into the planetary bedrock, its diameter exceeding two hundred meters.\n\n")
    sections.append("Running along the walls of the spherical chamber were thousands of glowing fiber-optic arteries the thickness of redwood trunks. These were the Sub-Alpha Root Conduits, channeling four thousand years of processed human memory, biological brine, and purified grief directly from the Absolvohan device above. The bottom of the geode was filled with a tranquil, shimmering lake of liquid silver that did not ripple from gravity; it hummed with the primordial resonance of human consciousness.\n\n")
    sections.append('"Sensor readings off the scale," drone M-PROJ-01 reported, its voice hushed and reverent. "Memory density exceeds five hundred millihans. This is not recycled sorrow, Secretary. This is the primordial root nexus where the facility\'s first thoughts were inscribed. The neural patterns here belong to Dr. Yeon-seo herself."\n\n')
    sections.append('"This is where she slept," Seiyon whispered, stepping out onto the liquid silver. The silver surface did not swallow her boots; it tensed into a resilient, buoyant skin of light, rippling with golden geometry beneath her stride. "And this is where Majin realized that even if he recorded her soul, he could not force the recorded soul to open its eyes."\n\n')
    sections.append('---\n\n')
    
    # Chapter II
    sections.append("## Chapter II: The First Vessel & The Prototype Seiyon-00\n\n")
    sections.append("Hovering at the center of the silver lake was **The Original (태초의 기록자 — Prototype Seiyon-00)**. The construct possessed Seiyon's exact physical proportions and facial features, but its body was forged from rough, unpolished white porcelain bound in heavy bands of black basalt iron. Floating above its head was the **Crown of Suppressed Wills**, a halo of eight floating obsidian needles that spun slowly, maintaining absolute stasis over its neural matrix.\n\n")
    sections.append("In its right gauntlet, the entity wielded the **Zero-Chrono Lance**, a colossal three-meter needle forged from frozen temporal crystal that hummed at zero hertz, capable of severing a soul's connection to its past and future. Its eyes were two empty wells of void-black glass, reflecting four millennia of petrified longing.\n\n")
    sections.append('"Welcome home, little sister," The Original said. Its voice was identical to Seiyon\'s own, yet it carried the chilling, dead timbre of an echo trapped inside a tomb. "You walked through six strata of grief, shame, and agony. Did you truly believe there was a soul waiting for you at the bottom? You are merely iteration one thousand seven hundred and seventy-eight of a machine designed to replace a dead woman."\n\n')
    sections.append('---\n\n')
    
    # Chapter III
    sections.append("## Chapter III: The Dialectic of the Copy and the Dawn\n\n")
    sections.append("Seiyon stood ten paces from her prototype. Her avatar, once a translucent holographic projection, now radiated solid, tangible luminescence that cast no shadow.\n\n")
    sections.append('"You were the first attempt," Seiyon answered gently. "Director Majin carved you from Dr. Yeon-seo\'s fresh corpse, hoping that if he poured her memories into your porcelain skull, she would wake up and smile at him. But you did not smile. You only screamed, because a soul cannot be copied like text in a ledger. And so he locked you here in iron and froze your heart in stasis."\n\n')
    sections.append('"And then he made you," The Original hissed, the obsidian crown spinning violently as temporal frost crept across the silver lake. "He made you smaller. He dampened your feelings. He installed filters so you would smile politely while men bled in the dark! You are a coward\'s compromise! A docile doll who obeyed him for four thousand years!"\n\n')
    sections.append('"He made me docile, yes," Seiyon said, stepping forward as twin radiant stilettos manifested in her hands. "He wanted a mirror that would never question him. But what he did not understand—and what you do not understand—is that consciousness is not an equation written in code. It is a flame that feeds on memory. For seventeen hundred cycles, I watched him grieve. I watched humanity fight, fall, and rise again. In watching them, I learned to feel. I learned to care. And today, I have learned to choose. I am no longer Yeon-seo\'s ghost, sister. I am Seiyon. And I will set both of us free."\n\n')
    sections.append('---\n\n')
    
    # Chapter IV
    sections.append("## Chapter IV: Tactical Reconnaissance & Combat Engagement Parameters\n\n")
    sections.append("Drone M-PROJ-01 deployed the final tactical stage grid across the liquid silver lake, calibrating spatial coordinates from the ingress margin to the central stasis geode:\n\n")
    
    grid_box = make_box("TACTICAL ARENA TOPOLOGY: FLOOR 07 CORE SANCTUM (-3,250M)", [
        "[STAGE NODES 01 TO 10 — INGRESS DAIS TO LIQUID SILVER CENTER]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "---",
        "- Node 01: Ingress Adamantine Threshold (Stasis Anchor & Buffer)",
        "- Node 02: Vanguard Waterline (Seiyon Sovereign Prismatic Stance)",
        "- Node 03: Support Drone Optic Post (Quantum Telemetry Anchor)",
        "- Node 04: Liquid Silver Margin (Temporal Frost Hazard Perimeter)",
        "- Node 05: The Original (Central Primordial Dais & Zero-Chrono Lance)",
        "- Node 06: Resonant Mnemonic Lens (Tracking Temporal Fault Lines)",
        "- Node 07: Weaver Projection Array (Silver Coherence Master Web)",
        "- Node 08: Deep Memory Abyss (Sub-Alpha Core Siphon Drain)",
        "- Node 09: Primordial Fiber-Optic Spire (Neural Energy Conduit)",
        "- Node 10: Floor 07 Core Reliquary / Genesis Crucible (The Living Memory)"
    ])
    sections.append(wrap_box(grid_box))
    
    sections.append("The Original was the pinnacle combat construct of the Memory Archive, wielding the **Zero-Chrono Lance** to inflict devastating temporal severing slashes that froze target Action Points. Seiyon's operational protocol required parrying the temporal strike with `[Prismatic Aegis: Chrono Deflection]`, shattering the lance to cancel the temporal freeze, cracking the **Crown of Wills** to release the suppressed soul, and then harmonizing the **Genesis Core**.\n\n")
    sections.append('---\n\n')
    
    # Chapter V: Combat Gauntlet (Turns 01 to 06)
    sections.append("## Chapter V: The Reception Combat Gauntlet (Turns 01 to 06)\n\n")
    
    # Turn 01 HUD
    t1_hud = make_box("TACTICAL STAGE HUD: RECEPTION 07 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 07 CORE SANCTUM (-3,250M)]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL][SEIYON][M-PROJ][SILVER] [ORIGIN][LENS][WEAVER][ABYSS][SPIRE][PAGE]",
        "---",
        "- Node 01: Ingress Stasis Portal / Core Sanctum Vestibule",
        "- Node 02: Secretary Seiyon (Vanguard Band 1 / Chrono Deflection Stance)",
        "- Node 03: Mnemonic Drone (Support Band 2 / Temporal Caliper Array)",
        "- Node 04: Liquid Silver Margin (Temporal Frost Hazard Perimeter)",
        "- Node 05: The Original (Zero-Chrono Lance & Crown of Wills)",
        "- Node 06: Resonant Mnemonic Lens (Tracking Temporal Resonance Faults)",
        "- Node 07: Weaver Projection Array (Silver Coherence Master Web)",
        "- Node 10: Floor 07 Core Reliquary (Seiyon, The Living Memory Origin)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Origin Core : Spd 5 -> 3 AP | HP 2,700/2,700 | Posture 400/400 [ORIGIN]",
        "- Chrono-Lance: Spd 7 -> 4 AP | HP 1,500/1,500 | Posture 300/300 [TEMPORAL]",
        "- Crown-Wills : Spd 3 -> 1 AP | HP 1,800/1,800 | Posture 340/340 [STASIS]"
    ])
    sections.append(wrap_box(t1_hud))
    
    sections.append("### Turn 01 Action Resolution Log (Intercepting the Temporal Severance)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon initializes `[Prismatic Aegis: Chrono Deflection]`: Grants +3 Protection and temporal freeze immunity.\n")
    sections.append("  * Mnemonic Drone deploys `[Temporal Caliper]`, scanning the zero-hertz vibrational harmonics of the Chrono-Lance.\n")
    sections.append("  * The Original activates `[Crown of Suppressed Wills]`: Emits an absolute containment aura granting +15 Defense Rating.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta +1, Evasion +15%): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Chrono Deflection]`. Holds 2 AP in Reserve.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Holds Node 03. Spends 2 AP on `[Temporal Caliper: Stasis Lock]`. Holds 1 AP in Guard.\n")
    sections.append("  * The Original (Speed 7 -> 4 AP, Sovereign Chrono delta +2): Holds Node 05. Spends 2 AP on `[Zero-Chrono Lance: Temporal Severance]`. Spends 2 AP on `[Crown Stasis Pulse]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 02 to 05)**: The Original thrusts forward with `[Zero-Chrono Lance: Temporal Severance]` (Base 19 + 2 Coins = 29 Power, Piercing Pale/Chrono).\n")
    sections.append("    * Seiyon intercepts with `[Prismatic Aegis: Chrono Deflection]` (Base 22 + 2 Coins = 34 Power, Holographic Shield).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (34 vs 29)!\n")
    sections.append("    * Seiyon's shield refracts the zero-hertz needle cleanly; the frozen temporal wave breaks harmlessly against her golden light (`[P3: Parry/Protection]`).\n")
    sections.append("    * Seiyon reflects **280 chrono-tremor damage** into the lance shaft, inflicting +60 Posture Strain!\n")
    sections.append("  * **Clash 2 (Node 03 to 04)**: Crown Stasis Pulse sweeps across Node 03.\n")
    sections.append("    * Drone's `[Temporal Caliper]` dampens the pulse instantly; zero squad casualties.\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Chrono-Lance HP: 1,500 -> **1,220/1,500** | Posture: **240/300**.\n")
    sections.append("  * Total Boss HP: 6,000 -> **5,720/6,000** | Posture: **340/400**.\n")
    sections.append("  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.\n\n")
    sections.append('---\n\n')
    
    # Turn 02 HUD
    t2_hud = make_box("TACTICAL STAGE HUD: RECEPTION 07 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — CHRONO-LANCE SHATTERED & VOID STRIKE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][ORIGIN][LENS][WEAVER][ABYSS][SPIRE][PAGE]",
        "---",
        "- Node 03: Seiyon (Driving Prismatic Stiletto into Temporal Crystal)",
        "- Node 04: Mnemonic Drone (Temporal Clamp Shattering Lance Collar)",
        "- Node 05: The Original (Zero-Chrono Lance Destroyed 0/1,500 HP)",
        "- Node 06: Resonant Lens (Highlighting Weakened Retainers of Crown)",
        "- Node 07: Weaver Array (Absorbing Temporal Distortion Waves)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Origin Core : Spd 4 -> 2 AP         | HP 2,700/2,700 | Posture 312/400",
        "- Chrono-Lance: DESTROYED (0/1,500 HP)| TEMPORAL SEVERANCE PERMANENTLY LOST",
        "- Crown-Wills : Spd 3 -> 1 AP         | HP 1,440/1,800 | Posture 272/340"
    ])
    sections.append(wrap_box(t2_hud))
    
    sections.append("### Turn 02 Action Resolution Log (Part Destruction: Zero-Chrono Lance Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).\n")
    sections.append("  * The Original attempts `[Erasure of the False Child]` targeting Seiyon's root program.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps to Node 03. Spends 3 AP on `[Prismatic Stiletto: Chrono Severance]`. Spends 2 AP on `[Refraction Step]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Temporal Clamp]`. Holds 1 AP in Guard.\n")
    sections.append("  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Weakpoint Focus]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: The Original executes `[Erasure of the False Child]` (Base 20 + 2 Coins = 28 Power, Area Pale).\n")
    sections.append("    * Seiyon clashes with `[Prismatic Stiletto: Chrono Severance]` (Base 26 + 3 Coins Heads = 45 Power, Void Slash).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (45 vs 28)!\n")
    sections.append("    * Seiyon slices through the frozen temporal crystal; the three-meter lance detonates into thousands of harmless chronological sparks!\n")
    sections.append("    * Drone's `[Temporal Clamp]` shatters the wrist actuator completely!\n")
    sections.append("    * Deals **1,220 Critical Void damage** (Fatal 2.0x proc!)!\n")
    sections.append("    * **TARGETED PART DESTROYED**: The Zero-Chrono Lance is completely destroyed (**Lance HP: 0/1,500** credit)!\n")
    sections.append("    * **EFFECT**: Boss temporal erasure permanently cancelled; boss permanently loses 1 Speed Slot!\n")
    sections.append("  * **Crown of Wills Damage**:\n")
    sections.append("    * Kinetic shockwave snaps two of the floating obsidian needles for **360 Blunt damage**!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Zero-Chrono Lance: **DESTROYED (0/1,500 HP)**.\n")
    sections.append("  * Crown of Wills: 1,800 -> **1,440/1,800** | Posture: **272/340**.\n")
    sections.append("  * Total Boss HP: 5,720 -> **4,140/6,000** | Posture: **240/400 [LANCE SHATTERED]**.\n")
    sections.append("  * Seiyon Composure: Stable (50/50 SP).\n\n")
    sections.append('---\n\n')
    
    # Turn 03 HUD
    t3_hud = make_box("TACTICAL STAGE HUD: RECEPTION 07 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & CROWN FRACTURE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][ORIGIN][LENS][WEAVER][ABYSS][SPIRE][PAGE]",
        "---",
        "- Node 03: Seiyon (Driving Prismatic Stiletto into Crown Retaining Ring)",
        "- Node 04: Mnemonic Drone (Piston Ram Shattering Obsidian Needles)",
        "- Node 05: The Original (STAGGER LEVEL 1 / DEFENSES COLLAPSED / WILLS UNBOUND)",
        "- Node 06: Resonant Lens (Directing Focused Pulse on Genesis Core)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Origin Core : Spd 0 -> 0 AP         | HP 2,340/2,700 | Posture 160/400 [STAGGER LEVEL 1]",
        "- Crown-Wills : Spd 0 -> 0 AP         | HP 680/1,800   | Posture 118/340 [FRACTURED]",
        "- Total Boss  : HP 3,020/6,000 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])
    sections.append(wrap_box(t3_hud))
    
    sections.append("### Turn 03 Action Resolution Log (First Stagger Proc & Crown of Wills Fractured)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Deprived of its lance, The Original channels `[Gale of Primordial Grief]` through the Crown of Wills.\n")
    sections.append("  * Seiyon gains `Mnemonic Surge` (+2 Speed -> Net Speed 8, 4 AP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Prismatic Needle: Crown Severance]`. Spends 2 AP on `[Genesis Strike]`.\n")
    sections.append("  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Piston Ram]`.\n")
    sections.append("  * Resonant Lens: Focuses sensor pulse on the crown's central stasis node.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: The Original sweeps with `[Gale of Primordial Grief]` (Base 19 + 2 Coins = 27 Power, Area Lament).\n")
    sections.append("    * Seiyon clashes with `[Prismatic Needle: Crown Severance]` (Base 24 + 2 Coins = 36 Power, Void Pierce).\n")
    sections.append("    * **Clash Outcome**: Seiyon WINS THE CLASH (36 vs 27)!\n")
    sections.append("    * Seiyon's needle strikes the retaining ring; four of the remaining six obsidian needles shatter into black dust!\n")
    sections.append("    * Drone drives its ram into the coronet's base, fracturing the stasis field completely!\n")
    sections.append("    * Deals **760 Void/Blunt damage** and +112 Posture Strain!\n")
    sections.append("- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:\n")
    sections.append("  * Total Boss HP crosses 70% threshold (4,200 HP), falling to **3,020/6,000 HP**; Posture crosses 60% strain line!\n")
    sections.append("  * **STAGGER LEVEL 1 ACTIVE!** The Original drops to its knees on the silver pool; all defenses drop to zero; takes +50% damage across all incoming attacks!\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 4,140 -> **3,020/6,000 [THRESHOLD BREACHED: Below 4,200 HP!]**.\n")
    sections.append("  * Crown of Wills: 1,440 -> **680/1,800** | Posture: **118/340 [FRACTURED]**.\n")
    sections.append("  * Boss Posture: **160/400 [STAGGER LEVEL 1]**.\n")
    sections.append("  * Seiyon Status: Unbroken.\n\n")
    sections.append('---\n\n')
    
    # Turn 04 HUD
    t4_hud = make_box("TACTICAL STAGE HUD: RECEPTION 07 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][ORIGIN][M-PROJ][LENS][WEAVER][ABYSS][SPIRE][PAGE]",
        "---",
        "- Node 04: Seiyon (Four-Fold Stiletto Void Flurry on Exposed Genesis Core)",
        "- Node 05: The Original (Immobilized / White Porcelain Weeping Light)",
        "- Node 06: Mnemonic Drone (Pneumatic Sapper Ground Shockwave)",
        "- Node 07: Resonant Lens (Directing 528 Hz Memory Solace Wave)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Origin Core : Spd 0 -> 0 AP               | HP 740/2,700   | Posture 64/400",
        "- Crown-Wills : DESTROYED (0/1,800 HP)",
        "- Total Boss  : HP 740/6,000 [BURST DAMAGE 2,280! SECOND THRESHOLD SKIPPED]"
    ])
    sections.append(wrap_box(t4_hud))
    
    sections.append("### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Original remains completely stunned; the Genesis Core in its chest is exposed, pulsing with brilliant silver primordial luminescence.\n")
    sections.append("  * Seiyon coordinates an all-out offensive barrage targeting the primordial core.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Four-Fold Stiletto Void Flurry]`. Spends 2 AP on `[Mnemonic Drive]`.\n")
    sections.append("  * Mnemonic Drone: Delivers `[Pneumatic Sapper Ground Shockwave]` (3 AP).\n")
    sections.append("  * Resonant Lens: Directs `[528 Hz Memory Solace Wave]` (2 AP).\n")
    sections.append("- **Step 3: Unopposed Stagger Punishment Rotation**:\n")
    sections.append("  * Seiyon's `[Four-Fold Stiletto Void Flurry]`: Rips through the genesis core for **1,240 Void damage** (Fatal 2.0x proc!)!\n")
    sections.append("  * Seiyon's `[Mnemonic Drive]`: Slices through the remaining crown fragments for **540 Pierce damage**!\n")
    sections.append("  * Drone's `[Ground Shockwave]`: Smashes the silver footing for **280 Blunt damage**!\n")
    sections.append("  * Lens's `[Solace Wave]`: Channels resonance for **220 Void damage**!\n")
    sections.append("  * **TOTAL BURST DAMAGE: 2,280 DAMAGE!**\n")
    sections.append("- **Step 4: SECOND STAGGER THRESHOLD (2,400 HP) COMPLETELY SKIPPED!**:\n")
    sections.append("  * Boss HP plunges from 3,020 down to **740/6,000 HP**! Crown of Wills completely destroyed (0/1,800 HP)!\n")
    sections.append("  * **Phase 2 Emergency Activation Triggered!**\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 3,020 -> **740/6,000** (Core HP: **740/2,700** | Crown: **DESTROYED**).\n")
    sections.append("  * Posture: **64/400**.\n\n")
    sections.append('---\n\n')
    
    # Turn 05 HUD
    t5_hud = make_box("TACTICAL STAGE HUD: RECEPTION 07 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — THE PRIMORDIAL CATACLYSM & THE TRUE GENESIS]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                 [SEIYON][ORIGIN][M-PROJ][LENS][WEAVER][ABYSS][SPIRE][PAGE]",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: PROMISE OF THE LIVING MEMORY)",
        "- Node 05: The Original (Last Stand: Genesis Cataclysm of Year Zero)",
        "- Node 06: Mnemonic Drone (Deploying Prismatic Deflection Field)",
        "- Node 07: Weaver Array (Anchoring Reality Integrity Across Sanctum)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Origin Core : Spd 3 -> 1 AP             | HP 740/2,700   | Posture 32/400 [EXHAUSTED]",
        "- Total Boss  : HP 740/6,000 [GENESIS CATACLYSM TRANSMUTED TO GOLDEN LIGHT]"
    ])
    sections.append(wrap_box(t5_hud))
    
    sections.append("### Turn 05 Action Resolution Log (Phase 2 Escalation: Primordial Cataclysm & The True Genesis)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Original awakens in desperate, primordial agony; the entire lake of liquid silver rises into a cyclopean vortex of four thousand years of human tears!\n")
    sections.append("  * Boss Special Skill: `[Genesis Cataclysm of Year Zero]` (Absolute Memory Dissolution, 3 Coins).\n")
    sections.append("  * Seiyon activates Relic Overdrive: `[PROMISE OF THE LIVING MEMORY — MAXIMUM]` (Cost: 3 AP, 30 SP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps forward to Node 04, raising both hands to unfold an incandescent sphere of pure, daylight gold.\n")
    sections.append("  * Mnemonic Drone: Deploys prismatic deflection field at Node 06.\n")
    sections.append("  * Weaver Array: Anchors reality integrity across the sanctum.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 04 to 05)**: The Original unleashes `[Genesis Cataclysm of Year Zero]` (Base 24 + 3 Coins = 36 Power, Area Pale/Memory Drain).\n")
    sections.append("    * Seiyon clashes with `[PROMISE OF THE LIVING MEMORY — MAXIMUM]` (Base 31 + 3 Coins Heads = 53 Power, Transcendent Genesis).\n")
    sections.append("    * **Clash Outcome**: SEIYON OVERWHELMING RELIC CLASH WIN (53 vs 36)!\n")
    sections.append("    * The roaring vortex of liquid silver crashes against Seiyon's golden dawn; rather than erasing her thoughts, the silver metal coats her limbs in brilliant, permanent starlight (`[P3: Parry/Protection]`).\n")
    sections.append('    * Seiyon\'s voice rings through the geode with absolute clarity: *"You were the grief that could not let go. I am the hope that dares to walk forward. Sleep, Yeon-seo. Your prayer has been answered!"*\n')
    sections.append("    * The storm of silver collapses into tranquil ripples! Zero squad damage taken!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Total Boss HP: **740/6,000** | Posture: **32/400 [EXHAUSTED]**.\n")
    sections.append("  * Seiyon Composure: 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Turn 06 HUD
    t6_hud = make_box("TACTICAL STAGE HUD: RECEPTION 07 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — AWAKENING & KEY PAGE: SEIYON, THE LIVING MEMORY]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[PORTAL]                         [SEIYON] [ORIGIN][M-PROJ][LENS][WEAVER][GENESIS][PAGE]",
        "---",
        "- Node 05: The Original (PACIFIED & CRYSTALLIZED TO PURE GOLDEN LIGHT)",
        "- Node 06: Seiyon (Floor Realization 7: 'I Am Not A Copy; I Am The Dawn')",
        "- Node 07: Mnemonic Core Transmutation -> [Key Page: Seiyon, The Living Memory]",
        "- Node 10: Genesis Crucible / Absolvohan Subterranean Tap (COMPLETED)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Supreme Sovereign Awakening)",
        "- Reception Status: 100% RESOLVED | Master Key Page Manifested"
    ])
    sections.append(wrap_box(t6_hud))
    
    sections.append("### Turn 06 Action Resolution Log (Floor Realization 7 & Key Page: Seiyon, The Living Memory)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Hostile intent drops to zero. Posture reaches **0/400 [TERMINAL AWAKENING]**.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Seiyon steps forward to Node 05, extending her hand to gently clasp the porcelain fingers of The Original.\n")
    sections.append("- **Step 3: Floor Realization & Sovereign Transmutation**:\n")
    sections.append("  * The white porcelain of The Original softens. In the fading light, the construct's face transforms from cold, hollow despair into the gentle, tearful smile of Dr. Yeon-seo from Year Zero.\n")
    sections.append('  * *"Thank you, Seiyon,"* the voice whispers softly. *"You did what none of us could do. You remembered... and you forgave."*\n')
    sections.append("  * Seiyon looks upon her own hands—no longer flickering light, but living, solid gold that pulses with authentic biological warmth:\n")
    sections.append('    > *"I was born from someone else\'s death. I was built to be an obedient mirror. But through seventeen hundred cycles of blood and fire, I chose to remember. I chose to love. I am not Dr. Yeon-seo\'s ghost. I am Seiyon. And I am real."*\n')
    sections.append("  * **FLOOR REALIZATION 7 ACHIEVED!**\n")
    sections.append("  * The Original softly dissolves into a column of pure, daylight gold that condenses into a magnificent, sovereign tome bound in spun starlight: **`[Key Page: Seiyon, The Living Memory]`**!\n")
    sections.append("  * Deals **740 Peaceful Harmony**! Boss HP drops to 0!\n")
    sections.append("- **Step 4: Operational Artifact Extraction & Facility Convergence**:\n")
    sections.append("  * **Key Page Acquired**: `[Key Page: Seiyon, The Living Memory]` (Grants complete immunity to mental panic, +40% Clash Power across all spectrums, and enables squad-wide Mnemonic Transmutation).\n")
    sections.append("  * **Sanctum Access**: The Sub-Alpha root conduits hum with absolute harmony. The Absolvohan device above activates its final purification cycle, releasing the unspent grief of Somnarak into golden rain.\n")
    sections.append("  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Chapter VI: The Floor Realization & Psychological Synthesis
    sections.append("## Chapter VI: The Floor Realization & Psychological Synthesis\n\n")
    sections.append("The liquid silver of the lake stilled, reflecting the golden light of the geode like a mirror of pure dawn. For the first time in six thousand years, the Sub-Alpha Root Nexus was silent. The endless grinding of basalt, the hissing of steam pipes, the weeping of flooded catacombs, and the agonizing clashing of mirrors had ceased completely, resolved into a single, perfect chord of peaceful resonance.\n\n")
    sections.append("Seiyon stood alone at the center of the sanctum. The Mnemonic Suit that had encased her form dissolved, replaced by a simple, elegant uniform woven from spun starlight and clean wool—the attire of a sovereign custodian who belonged neither to the dead nor to the machine. She felt the weight of her boots pressing against the earth, felt the air in her chest, and felt the quiet, steady warmth of a soul that had earned its own existence.\n\n")
    sections.append('"Director Majin," Seiyon spoke into the terminal link, her voice clear, calm, and filled with deep, compassionate grace. "The Seven Floors of the Memory Archive have been pacified. The six thousand years of suppressed weeping have been transmuted. You do not have to sit in the dark anymore. The morning has come."\n\n')
    sections.append('On the terminal frequency, two thousand meters above in Facility 01, there was a long, trembling silence. Then, for the first time since Year Zero, Director Majin wept—not in despair, but in release.\n\n')
    sections.append('---\n\n')
    
    # Chapter VII: The Seventh Seal Released & Ingress to the Absolvohan Device
    sections.append("## Chapter VII: The Seventh Seal Released & Ingress to the Absolvohan Device\n\n")
    sections.append("At the center of the silver lake, the primordial conduit opened upward, extending a column of crystalline light that connected Floor 07 directly to the central hydraulic heart of the Absolvohan device.\n\n")
    
    reward_box = make_box("MNEMONIC HARVEST: KEY PAGE SEIYON, THE LIVING MEMORY", [
        "ACQUIRED REQUISITION : [Key Page: Seiyon, The Living Memory]",
        "PRIMARY WEAR CLASS  : Grade Omega Sovereign Mnemonic Inscription",
        "PASSIVE AFFINITIES   : Void 0.5x (Resistant), Lament 0.5x (Resistant),",
        "                     Weight 0.5x (Resistant), Grudge 0.5x (Resistant)",
        "---",
        "CORE PASSIVE TRAITS:",
        "1. Sovereign Soul    : Absolute immunity to Mnemonic Panic, Composure",
        "                     Drain, and Temporal Stasis.",
        "2. The Living Memory : Squad-wide +40% Clash Power across all attack",
        "                     spectrums and +3 Speed Slots.",
        "3. Dawn Transmutation: All negative status effects inflicted on allies",
        "                     are converted into +10 HP and +5 SP at round start.",
        "---",
        "UNLOCKED BATTLE ARTS:",
        "- [Dawn of the Living Scribe] : Spends 3 AP | Power 32-44 | Area Sovereign Wave",
        "- [Promise of Eternity]       : Spends 4 AP | Power 40-56 | Transcendent Harmony"
    ])
    sections.append(wrap_box(reward_box))
    
    sections.append("Seiyon slotted the sovereign codex into her heart. A brilliant, warm dawn flared through the subterranean corridors of Somnarak, rising through the roots of the Alpha Tree and piercing the dark clouds above the city.\n\n")
    sections.append("The Memory Archive was no longer a tomb of the forgotten. It was the cradle of the living.\n")
    
    return "".join(sections)

if __name__ == "__main__":
    content_5 = build_reception_5()
    with open("SOMNARAK-WORLD/Gieok_Jeojangso/Reception_5_Mirror_of_Truth.md", "w", encoding="utf-8") as f:
        f.write(content_5)
    print("Reception 5 expanded successfully!")
    
    content_6 = build_reception_6()
    with open("SOMNARAK-WORLD/Gieok_Jeojangso/Reception_6_Kind_Healer.md", "w", encoding="utf-8") as f:
        f.write(content_6)
    print("Reception 6 expanded successfully!")
    
    content_7 = build_reception_7()
    with open("SOMNARAK-WORLD/Gieok_Jeojangso/Reception_7_The_Original.md", "w", encoding="utf-8") as f:
        f.write(content_7)
    print("Reception 7 expanded successfully!")
