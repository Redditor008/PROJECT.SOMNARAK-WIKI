#!/usr/bin/env python3
"""
tools/generate_story_cantos.py
Generates the Vector 5 Story Cantos Suite:
1. SOMNARAK-WORLD/Story_Cantos/README.md
2. SOMNARAK-WORLD/Story_Cantos/CANTO_01_THE_BASTION_ANCHOR_MIN_JAE.md
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from box_formatter import make_box

def wrap_box(b):
    return "```text\n" + b + "\n```\n\n"

def build_cantos_readme():
    content = []
    content.append("# SOMNARAK — The Character Story Cantos (  비탄의 장  )\n")
    content.append("## Canonical Literary Suite & Personal Narrative Chronicles\n")
    content.append("### Reverie Directorate Cultural & Psychological Archive — Year 4,238\n\n")

    box = make_box("THE CHARACTER STORY CANTOS CATALOGUE", [
        "ARCHIVE CODE : LORE-CANTO-SUITE-4238",
        "JURISDICTION : Reverie Directorate Central Archive & Memory Vaults",
        "STRUCTURE    : 6 Core Protagonist Cantos across 3-Act Prose Format",
        "PURPOSE      : Dialogue-Driven Narrative Fiction & Emotional Realization",
        "---",
        "CANTO I   : The Bastion Anchor   (Warden Min-Jae / Facility 01)",
        "CANTO II  : The Acoustic Void    (Specialist Seol-A / Resonance)",
        "CANTO III : The Shattered Striker(Vanguard Taeho / Forge District)",
        "CANTO IV  : The Sub-Zero Ridge   (Marksman Ha-Eun / Bastion Frontier)",
        "CANTO V   : Suture of Lost Pages (Secretary Seiyon / Memory Spire)",
        "CANTO VI  : The Slum Breacher    (Breacher Kang / Undercity Pacification)",
        "---",
        "FORMAT    : Monospace 71-Col ASCII HUDs, Zero HTML, Pure Lore"
    ], width=71)
    content.append(wrap_box(box))

    content.append("> *\"An archive without the voices of its soldiers is merely a graveyard of numbers. We recorded the weight of every entity, the tensile strength of every basalt bulkhead, and the caloric output of every piece of Han-bread. But when the long night fell across the facility, it was not the formulas that kept the gates sealed. It was the warden who planted his boots in the cracked stone, swallowed his own blood, and whispered that he would not yield.\"*\n")
    content.append("> — Secretary Seiyon, Preface to the Human Ledger of Cycle 1,778\n\n")
    content.append("---\n\n")

    content.append("## 1. Overview & Narrative Purpose\n\n")
    content.append("The **Character Story Cantos (  비탄의 장  )** represent the definitive literary and narrative heart of Project Somnarak. While the Master Codices document the macroscopic laws of cosmology, geology, and corporate governance, the Cantos chronicle the lived human experience of the men and women who hold the perimeter of human existence upon Mugenhan.\n\n")
    content.append("Each Canto is authored as an expansive, multi-act literary chapter structured around three core narrative beats:\n\n")
    content.append("1. **Act I: The Heavy Morning (  일상의 멍에  ):** The routine burdens, sensory atmosphere, interpersonal friction, and personal psychological fractures of everyday life in Somnarak.\n")
    content.append("2. **Act II: The Fracture Point (  균열의 순간  ):** The sudden onset of operational crisis, moral conflict, rising Composure stress, and the confrontation with mortality.\n")
    content.append("3. **Act III: The Resonant Catharsis (  공명의 해탈  ):** The climactic combat engagement mirroring the 10-node tactical spatial engine, culminating in emotional catharsis and the forging of unbreakable resolve.\n\n")

    content.append("---\n\n")

    content.append("## 2. Master Cantos Registry\n\n")
    content.append("| Canto | Document Title | Protagonist | Setting & Theater | Core Emotional Theme |\n")
    content.append("|---|---|---|---|---|\n")
    content.append("| Canto I | [`CANTO_01_THE_BASTION_ANCHOR_MIN_JAE.md`](CANTO_01_THE_BASTION_ANCHOR_MIN_JAE.md) | Warden Min-Jae | Facility 01 Floor 01 Frontline Gates | Survivor's guilt and unyielding defense |\n")
    content.append("| Canto II | [`CANTO_02_THE_ACOUSTIC_VOID_SEOL_A.md`](CANTO_02_THE_ACOUSTIC_VOID_SEOL_A.md) | Specialist Seol-A | Facility 01 Floor 04 Resonance Labs | Auditory trauma and the lost frequency choir |\n")
    content.append("| Canto III | `CANTO_03_THE_SHATTERED_STRIKER_TAEHO.md` | Vanguard Taeho | Zone D Forge District & Zone B Slums | Destructive rage and debt foreclosure |\n")
    content.append("| Canto IV | `CANTO_04_THE_SUB_ZERO_RIDGE_HA_EUN.md` | Marksman Ha-Eun | Zone E Bastion & Desolate Frontier | Emotional isolation and solitary sniper vigils |\n")
    content.append("| Canto V | `CANTO_05_SUTURE_OF_LOST_PAGES_SEIYON.md` | Secretary Seiyon | Memory Archive Sub-Alpha Spire | Machine memory and the grief of 1,778 cycles |\n")
    content.append("| Canto VI | `CANTO_06_THE_SLUM_BREACHER_KANG.md` | Breacher Kang | Zone B Drainage District & Mask Market | Undercity brotherhood vs municipal duty |\n\n")

    content.append("---\n\n")

    content.append("## 3. Strict Authoring Standards for Cantos\n\n")
    content.append("Every Canto document must strictly adhere to the following mandatory guidelines:\n\n")
    content.append("- **Symmetrical Monospace HUDs:** Every Act opens with a verified 71-column ASCII metadata HUD enclosed in non-markdown code fences (````text ... ````).\n")
    content.append("- **Prose Purity:** Strictly zero raw `<br>` tags, zero raw HTML elements, and zero LaTeX math dollar delimiters.\n")
    content.append("- **Native Somnarak Lexicon:** Uncompromising adherence to native terms (Han-Energy, Composure, Sorrow Entities, M.A.W., Meltdown, Wardens, Enforcers, Watches).\n")
    content.append("- **Combat Fidelity:** Action sequences in Act III must strictly respect the 10-node spatial grid, Speed Bands, AP allocation, and Four P-Framework established in `GAME_BATTLE/`.\n")

    return "".join(content)

def build_canto_01():
    content = []
    content.append("# CANTO I: THE BASTION ANCHOR (  바스티온의 닻  )\n")
    content.append("## Warden Min-Jae and the Unbroken Wall of Floor 01\n")
    content.append("### The Reverie Directorate — Containment Chronicles of Cycle 1,778\n\n")

    box_main = make_box("CANTO I: THE BASTION ANCHOR", [
        "PROTAGONIST  : Warden Min-Jae (The Bastion Anchor / Iron Quad)",
        "AFFILIATION  : The Reverie Directorate — Facility 01 Floor 01",
        "THEATER      : Frontline Quarantine Sector 4 (-150m Below Alpha Tree)",
        "FRACTURE     : Survivor Guilt & The Nightmare of the Broken Shield",
        "EQUIPMENT    : The Mourning Maul & Heavy Basalt Bastion Aegis",
        "COMPOSURE    : Baseline 115 / Crisis Threshold 45 / Max Posture 210",
        "---",
        "ACT I   : The Heavy Morning — Mess Hall & Shield Rigging",
        "ACT II  : The Fracture Point — Tectonic Breach & Jammed Gate",
        "ACT III : The Resonant Catharsis — The Unbroken Wall"
    ], width=71)
    content.append(wrap_box(box_main))

    content.append("> *\"A shield is not forged to preserve the man behind it. A shield is forged so that the men behind him might live to see another morning. If the stone shatters, you do not drop your hands. You become the stone.\"*\n")
    content.append("> — Warden Min-Jae, Field Inscription upon the Bastion Aegis\n\n")
    content.append("---\n\n")

    # ACT I
    content.append("## Act I: The Heavy Morning (  일상의 멍에  )\n\n")

    box_act1 = make_box("ACT I: THE HEAVY MORNING", [
        "LOCATION  : Sub-Level 2 Warden Armory & Sector 4 Mess Hall",
        "TIMESTAMP : First Watch (06:45 Morning / Shift Rotation)",
        "PERSONNEL : Warden Min-Jae, Specialist Seol-A, Vanguard Taeho",
        "STATUS    : Baseline Composure 115/115 | Ambient Han 14.2 Hz"
    ], width=71)
    content.append(wrap_box(box_act1))

    content.append("The grease smelled like cold soot and rancid sorrow-oil.\n\n")
    content.append("Min-Jae dipped his thumb into the iron tin, scooping a dollop of thick black lubricant, and worked it into the pneumatic hinge of his left gauntlet. The metal was cold—colder than the subterranean air that drifted down the ventilation shafts from the root wells of the Alpha Tree. Every morning for nine years, he had sat on this exact steel bench, stripped down to his grey linen undershirt, listening to the facility wake up around him.\n\n")
    content.append("Above him, thirty meters through layered plates of reinforced basalt, the central turbines hummed at 14.2 Hertz. It was a sound you did not hear with your ears; you felt it in your teeth, in the marrow of your collarbones, in the slow, rhythmic ache of old scar tissue where a basalt splinter had pierced his lung during the breach of Year Zero.\n\n")
    content.append("Beside the bench, resting against the stone locker, stood the shield.\n\n")
    content.append("The *Heavy Basalt Bastion Aegis* weighed one hundred and forty kilograms. Its outer face was slab-cut volcanic rock, quarried from the deepest fault line of the Weeping and bound in three bands of rolled carbon iron. Deep gouges scarred the dark surface—claws, acoustic acid burns, and the jagged white impact crater where an entity's horn had struck during the suppression of Floor 2. Min-Jae reached out, running his calloused palm over the cold basalt. The stone hummed faintly against his skin, absorbing the warmth of his hand like a thirsty beast.\n\n")
    content.append("\"You're staring at it again, Min-Jae.\"\n\n")
    content.append("The voice was quiet, melodic, carrying the slight metallic rasp of someone whose throat had breathed too much acoustic vapor. Specialist Seol-A stood by the armory threshold, leaning against the doorframe. She wore her dark blue Directorate tunic, unbuttoned at the collar, revealing the silver resonance collar locked around her neck. In her right hand, she held two tin mugs that steamed with thin, greyish broth.\n\n")
    content.append("\"Checking the hydraulic latch,\" Min-Jae said without looking up. His voice was gravelly, worn smooth by years of shouting through containment blast masks. \"The seal was sluggish on the secondary return yesterday. If the piston jams during a clash, the recoil will snap my elbow.\"\n\n")
    content.append("\"The piston didn't jam,\" Seol-A said, stepping into the alcove and offering him one of the mugs. \"You took a direct seismic ground-slam from a Rank IV Murmur on Floor 2 and your arm stayed attached. Drink your soup. It tastes like chalk and old rain, but it's warm.\"\n\n")
    content.append("Min-Jae took the mug. The warmth seeped through his oil-stained fingers. He took a sip. It was standard Sector 4 ration broth—diluted Veil-water boiled with crushed Han-crystals and dried kelp grown in the underground water cisterns. It tasted bitter, faintly metallic, like sucking on a copper coin. But it settled the hollow churning in his stomach.\n\n")
    content.append("\"Where's the boy?\" Min-Jae asked.\n\n")
    content.append("\"Taeho?\" Seol-A smiled faintly, though her eyes remained shadowed. \"In the mess hall. Arguing with the logistics clerk over his cleaver's edge. He claims the grindstone in Zone D gave him a three-degree deviation on the fuller. He wanted to file a formal grievance with the Council.\"\n\n")
    content.append("\"He's nervous,\" Min-Jae said softly. \"When Taeho talks about blade angles, it means his hands are shaking.\"\n\n")
    content.append("\"We're all nervous,\" Seol-A replied. She sat down on the edge of the adjoining wooden crate, drawing her knees up against her chest. The silver collar at her throat gave a faint, rhythmic tick—the internal damper monitoring her sensory frequency. \"The shift report from Central Command came down twenty minutes ago. Lead Dekan's containment monitors flagged anomalous seismic harmonics in Sector 4. The Monolith's cell is trembling. It's whispering through the pipes.\"\n\n")
    content.append("Min-Jae didn't reply immediately. He took another sip of the bitter broth, his pale grey eyes drifting back to the battered surface of his shield.\n\n")
    content.append("He remembered Cycle 1,440.\n\n")
    content.append("He remembered the deafening sound of basalt cracking like thunder in an enclosed room. He remembered Warden Jun-Seo—twenty-two years old, laughing that morning about his younger sister's wedding in Zone C—standing three paces to his right when the blast gate failed. He remembered the sound Jun-Seo made when the falling bulkhead crushed his pelvis, and he remembered how Jun-Seo had reached out with blood-soaked fingers, clawing at Min-Jae's boot, begging him to pull him free. But Min-Jae had held the shield forward, bracing against forty tons of collapsing stone, unable to step back, unable to look down, until the screaming stopped and there was only the smell of hot copper and wet dust.\n\n")
    content.append("Every cycle, the facility reset. Every cycle, the bodies disappeared and the ledgers were rewritten. But Min-Jae's shoulders still carried the phantom weight of forty tons of rock, and his boot still felt the touch of a dead boy's hand.\n\n")
    content.append("\"Min-Jae?\" Seol-A's voice was gentle now, reaching through the fog of his memory.\n\n")
    content.append("\"I'm here,\" he muttered, setting the empty mug down on the bench. He stood up, towering over her, his broad chest rising as he pulled on his reinforced padded gambeson. \"Get your needles, Seol-A. Go find Taeho before he punches the supply officer. We rotate to Sector 4 in fifteen minutes.\"\n\n")

    content.append("---\n\n")

    # ACT II
    content.append("## Act II: The Fracture Point (  균열의 순간  )\n\n")

    box_act2 = make_box("ACT II: THE FRACTURE POINT", [
        "LOCATION  : Sector 4 Primary Quarantine Conduit (-180m)",
        "TIMESTAMP : Second Watch (11:22 Midday / Emergency Alert)",
        "HAZARD    : SE-C-IVδ-008 The Quaking Monolith / Seismic Breach",
        "INCIDENT  : Hydraulic Blast Gate 4-B Jammed at 60% Closure",
        "THREAT    : Catastrophic Floorplate Collapse & Acoustic Backlash"
    ], width=71)
    content.append(wrap_box(box_act2))

    content.append("The sirens in Sector 4 did not wail; they groaned.\n\n")
    content.append("Deep, acoustic resonance klaxons installed in the basalt arches emitted a pulsing 80-decibel drone that vibrated inside the chest cavity. Yellow emergency strobes cut through the haze of pulverized stone dust that poured from the ceiling expansion joints. Across the catwalks, red containment runes flashed furiously along the conduit conduits:\n\n")
    content.append("`[ALERT: SECTOR 4 PRIMARY CONTAINMENT BREACH — CELL 08 COMPOSURE 0% — CODE RED]`\n\n")
    content.append("Min-Jae sprinted down the access stairs, his steel-toed boots ringing against the iron grating. The shield was locked to his left forearm, its weight shifting with familiar inertia as he moved. Behind him, Taeho ran with his twin cleavers already drawn, the polished edges catching the amber strobe light, while Seol-A held her brass siphon rig close to her chest, her sensory needles humming in their leather bandolier.\n\n")
    content.append("\"Report!\" Min-Jae roared into the comm-collar.\n\n")
    content.append("Secretary Seiyon's voice cut through the static, crisp and cold, echoing through the corridor speakers:\n\n")
    content.append("> **Seiyon (Comm):** _\"Entity SE-C-IVδ-008, The Quaking Monolith, has breached internal containment seals. Secondary hydraulic blast gate 4-B has descended to sixty percent and suffered mechanical seizure. Tectonic shear stress along Sub-Level 3 is rising exponentially. The gate will not close from central override.\"_\n\n")
    content.append("\"What's the damage?\" Taeho yelled, vaulting over a ruptured steam line that hissed violently across the floor.\n\n")
    content.append("> **Seiyon (Comm):** _\"If the gate remains unsealed for more than one hundred and eighty seconds, the tectonic resonance will propagate upward through the primary conduits, compromising the root well of the Alpha Tree. Protocol Nine requires automated thermal lockdown. In two minutes, the corridor will be flooded with liquid napalm and leaded acoustic gas.\"_\n\n")
    content.append("\"With us inside?\" Taeho snarled, his eyes widening in fury. \"Those bastard bureaucrats in Zone A are going to cook us!\"\n\n")
    content.append("\"Focus!\" Min-Jae barked, rounding the final corner into the primary containment hall.\n\n")
    content.append("The scene before them was hell carved in basalt.\n\n")
    content.append("The massive ten-meter blast gate hung crookedly in its guide rails, wedged halfway down by a massive slab of collapsed bedrock. Beneath the gap, a figure loomed in the darkness of the chamber—a towering, four-meter colossus of cracked volcanic stone and weeping iron veins. *The Quaking Monolith* was not merely an entity of rock; it was the embodied grief of every miner who had ever been buried alive beneath Mugenhan's crust. As it moved, grinding stone joints squealed with deafening agony, and with every step, the concrete floorplates beneath their feet buckled and heaved.\n\n")
    content.append("\"It's heading for the gap!\" Seol-A cried, pressing her hands against her ears as the acoustic feedback screeched through her resonance collar. \"Min-Jae! The harmonic pressure is at two hundred percent! It's going to crush through the gate!\"\n\n")
    content.append("\"Taeho! Seol-A! Fall back to Node 2!\" Min-Jae ordered, planting his boots into the center of the corridor at Node 5.\n\n")
    content.append("\"Hell no!\" Taeho shouted, stepping forward, his knuckles white around the grips of his cleavers. \"I'm breaking its knees! If I shatter the joint anchors, the weight will drop it before it hits the door!\"\n\n")
    content.append("\"You'll get pulverized in the shear zone, you idiot!\" Min-Jae grabbed the collar of Taeho's leather vest with his free hand and threw him violently backward toward Seol-A. \"Look at the floor! The bedrock is liquefying! You charge now, you sink to your waist and it crushes your skull in one swing!\"\n\n")
    content.append("Taeho stumbled, catching his balance against the catwalk railing, his teeth bared in impotent rage. \"Then what do we do?! Look at the timer! Ninety seconds until the napalm fires!\"\n\n")
    content.append("Min-Jae didn't look at the timer. He looked at the jammed blast gate. He looked at the trembling stone monolith advancing toward the opening, its stone fists dragging across the ground, sending waves of shattered rock skimming through the air like cannon shot.\n\n")
    content.append("He reached down to the base of his shield. With a sharp twist of his wrist, he engaged the primary pneumatic anchors.\n\n")
    content.append("*KER-CHUNK.* Two forty-centimeter spikes of case-hardened steel slammed downward from the bottom edge of the shield, driving directly into the reinforced floorplates. The hydraulic pistons hissed, locking his left arm into a rigid, impenetrable triangle with the earth.\n\n")
    content.append("\"Min-Jae, no!\" Seol-A screamed through the dust. \"You can't hold that alone! The impact will shatter your spine!\"\n\n")
    content.append("\"I am not alone,\" Min-Jae said. His voice was completely steady now. The tremor in his hands was gone. The phantom touch of Jun-Seo's dying grip vanished, replaced by the icy, crystalline clarity of a man who had found his purpose. \"Taeho! Prepare your part-breaker rush on Node 7! Seol-A! Set the resonance siphon to four hundred Hertz and dump the acoustic feedback into my shield conduits!\"\n\n")
    content.append("He lowered his head behind the viewing slit of the basalt plate, drawing the heavy carbon-iron maul from his shoulder holster with his right hand.\n\n")
    content.append("\"Let it come,\" Min-Jae whispered into the dark. \"Let the mountain hit the wall.\"\n\n")

    content.append("---\n\n")

    # ACT III
    content.append("## Act III: The Resonant Catharsis (  공명의 해탈  )\n\n")

    box_act3 = make_box("ACT III: THE RESONANT CATHARSIS", [
        "COMBAT ENGAGEMENT : Tactical Grid Clash — Node 04 to 06",
        "PRIMARY OPPONENT  : SE-C-IVδ-008 The Quaking Monolith",
        "STRIKE TEAM       : Iron Quad (Min-Jae, Seol-A, Taeho)",
        "SPEED ALLOCATION  : Min-Jae Spd 3 (2 AP) | Taeho Spd 5 (3 AP)",
        "COMPOSURE LOAD    : 45 -> 95/115 [CRISIS CLASH DETECTED]"
    ], width=71)
    content.append(wrap_box(box_act3))

    content.append("The Monolith roared—not with vocal cords, but with the sound of a continent tearing in two.\n\n")
    content.append("It lunged forward through the sixty-percent gap in the blast door, its massive right arm swinging in a sweeping horizontal arc. A five-ton slab of solid granite, jagged with broken basalt crystals, hurtled directly at Min-Jae's chest.\n\n")
    content.append("`[TACTICAL HUD — CLASH RESOLUTION: NODE 05]`\n")
    content.append("`* Monolith Action : [Tectonic Cleave] (Power 18-24 Weight Blunt)`\n")
    content.append("`* Min-Jae Action  : [Immovable Bastion Parry] (Power 20-26 Kinetic Guard)`\n\n")
    content.append("Min-Jae did not flinch. He leaned his entire body weight into the curved face of the shield, his right shoulder locked against the interior brace, and roared a vow into the deafening wind:\n\n")
    content.append("\"NOT. ONE. STEP.\"\n\n")
    content.append("The collision shook the foundations of Floor 1.\n\n")
    content.append("The granite arm struck the center of the *Bastion Aegis*. A shockwave of pulverized stone dust and sparks erupted outward, shattering the glass floodlights along the corridor walls. The pneumatic anchor spikes shrieked as they carved two deep, smoking furrows through six inches of reinforced concrete, but they held. Min-Jae's teeth slammed together, biting through his lower lip, blood filling his mouth as the kinetic force traveled through his bones—120 points of Weight damage crashing into his armor.\n\n")
    content.append("His Posture gauge dropped precipitously: 210... 140... 75.\n\n")
    content.append("His Composure load spiked from 45 to 95, teetering on the razor edge of Meltdown.\n\n")
    content.append("In his mind, the darkness yawned. The memory of Jun-Seo reached for him again, the voices of a thousand failed cycles whispering that it was time to let go, that the stone was too heavy, that Somnarak was doomed to drown in tears regardless of whether he held this corridor.\n\n")
    content.append("\"MIN-JAE! TAKE THE DAMPING!\"\n\n")
    content.append("Seol-A's voice cut through the acoustic fog like a silver bell.\n\n")
    content.append("She lunged forward to Node 03, thrusting her brass siphon needles into the floorplates behind his boots. Her silver collar glowed with incandescent blue light as she activated *The Hollow Siphon*. The kinetic vibration threatening to shatter Min-Jae's spine was suddenly siphoned away, flowing through the conductive floor cables into her mantle. A halo of pale blue resonance rippled around her shoulders as she converted the entity's destructive tremor into clean acoustic shielding:\n\n")
    content.append("`[PASSIVE TRIGGER: Siphon Veil — Min-Jae Posture +65, Composure Load -30]`\n\n")
    content.append("The crushing pressure lifted from his chest. Min-Jae exhaled a cloud of hot red mist, his eyes snapping wide.\n\n")
    content.append("The Monolith's arm was locked against the face of his shield, its stone fingers splintering under the counter-pressure of the parry. The entity recoiled, thrown off balance by the unyielding rebound of the basalt wall.\n\n")
    content.append("\"TAEHO! THE KNEE!\" Min-Jae roared.\n\n")
    content.append("\"ON IT!\" Taeho's battle cry was pure adrenaline.\n\n")
    content.append("The young vanguard surged forward from Node 02, utilizing his 3 Action Points in a blistering, acrobatic leap. His boots slammed onto the top rim of Min-Jae's shield, using the immovable warden as a springboard to vault three meters into the air. In the apex of his arc, Taeho gripped *The Debt Cleaver* with both hands, channeling pure Grudge Pierce energy into the hardened fuller.\n\n")
    content.append("\"DIE, YOU OVERGROWN HEADSTONE!\"\n\n")
    content.append("`* Taeho Action : [Part-Breaker Execution] vs [Left Knee Pillar]`\n")
    content.append("`* Damage: 185 Grudge Pierce (FATAL CRITICAL)`\n\n")
    content.append("The heavy steel cleaver plunged directly into the fissure behind the Monolith's left knee joint. The blade bit deep, shattering the crystalline marrow. With a sickening crunch of fracturing granite, the entity's left leg collapsed beneath its own immense weight. The colossus stumbled forward, falling onto one knee, its face coming level with Min-Jae's shield.\n\n")
    content.append("Min-Jae released the pneumatic floor spikes.\n\n")
    content.append("He stepped forward. One stride. Heavy. Inevitable.\n\n")
    content.append("He swung *The Mourning Maul* with both hands, the fifty-kilogram forged iron head whistling through the dust. The strike struck the Monolith directly between its hollow, glowing eye sockets with the sound of a meteor striking a cliff face.\n\n")
    content.append("`* Min-Jae Finisher : [Citadel Ground-Slam]`\n")
    content.append("`* Result: Entity Posture Broken (0/200) — Composure Meltdown Stasis Achieved`\n\n")
    content.append("The Monolith shuddered. The glowing yellow veins along its chest dimmed to a dull, dead amber. With a slow, grinding groan, the entity tipped backward into the containment chamber, collapsing into an inert, motionless mound of dormant stone.\n\n")
    content.append("\"Seiyon!\" Min-Jae shouted, dropping his maul and throwing his armored shoulders under the crooked edge of the jammed blast door. \"Drop the gate! NOW!\"\n\n")
    content.append("Behind the console on Floor 1, Seiyon's fingers flew across the emergency overrides:\n\n")
    content.append("> **Seiyon (Comm):** _\"Secondary hydraulic bypass engaged. Clearance confirmed. Dropping bulkheads in three... two... one.\"_\n\n")
    content.append("Min-Jae shoved the jammed wedge of rock free with his boot. The eighty-ton steel blast door slammed downward with a thunderous *BOOM*, the interlocking teeth engaging the floor seal with a pneumatic hiss of pressurized steam. The emergency lockdown sirens stuttered and died, replaced by the cool, steady chime of restored quarantine integrity:\n\n")
    content.append("`[SECTOR 4 QUARANTINE SEALED — BREACH RESOLVED — AUTOMATED PURGE CANCELLED]`\n\n")

    content.append("---\n\n")

    # EPILOGUE
    content.append("## Epilogue: The Bread of Survival (  생존의 빵  )\n\n")
    content.append("The corridor was quiet now.\n\n")
    content.append("The only sound was the steady hiss of water spraying from the ruptured cooling pipe and the ragged, shallow breathing of three wardens sitting on the debris-littered floorplates.\n\n")
    content.append("Taeho sat with his back against the wall, his cleavers lying across his lap, his hands trembling violently as the combat adrenaline drained from his veins. He looked at his shaking fingers, then looked up at Min-Jae with a mixture of shock and reluctant awe. \"You... you actually parried five tons of rock. My arms felt like they were going to tear off just jumping off your shield.\"\n\n")
    content.append("\"Your cleaver didn't deviate three degrees,\" Min-Jae said calmly, wiping a smear of dark blood from his split lip with the back of his forearm. \"The strike was centered. Good cut, Taeho.\"\n\n")
    content.append("Taeho blinked, then looked away, a faint flush coloring his dust-streaked cheeks. \"...Yeah. Well. It was in the way.\"\n\n")
    content.append("Seol-A sat beside Min-Jae, leaning her head gently against the basalt face of his shield. The stone was cool again, its hum quiet, almost peaceful. She unclipped a small pouch from her belt and drew out three pieces of hard, dark Han-crystal bread. She handed one to Taeho, one to Min-Jae, and kept the smallest piece for herself.\n\n")
    content.append("\"Breakfast is late,\" she murmured, her voice soft in the dim yellow light.\n\n")
    content.append("Min-Jae took the bread. It was stale, hard as quarry stone, and tasted of ash and sorrow. He bit into it, chewing slowly, feeling the rough texture grind against his teeth. He felt the cold iron of his gauntlets, the ache in his shoulders, the steady beating of his heart, and the quiet presence of his squad beside him.\n\n")
    content.append("He was alive. They were alive.\n\n")
    content.append("High above them, through hundreds of meters of stone and iron, the dawn was rising over Somnarak. The city would wake up, the citizens would put on their masks, the Collectors would count their debt, and the machines would turn. They would never know the name of Warden Min-Jae. They would never know that eighty tons of basalt had almost crushed their morning into ash.\n\n")
    content.append("And as Min-Jae swallowed the bitter bread, he looked at his battered shield, leaned his head back against the cold wall, and closed his eyes in peace.\n\n")
    content.append("It was enough.\n\n")

    return "".join(content)

if __name__ == "__main__":
    base_dir = "/home/user/PROJECT.SOMNARAK-WIKI/SOMNARAK-WORLD/Story_Cantos"
    os.makedirs(base_dir, exist_ok=True)

    readme_text = build_cantos_readme()
    readme_path = os.path.join(base_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_text)
    print(f"Wrote {readme_path} ({len(readme_text)} bytes)")

    canto1_text = build_canto_01()
    canto1_path = os.path.join(base_dir, "CANTO_01_THE_BASTION_ANCHOR_MIN_JAE.md")
    with open(canto1_path, "w", encoding="utf-8") as f:
        f.write(canto1_text)
    print(f"Wrote {canto1_path} ({len(canto1_text)} bytes)")
