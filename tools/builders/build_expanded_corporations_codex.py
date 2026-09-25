#!/usr/bin/env python3
"""
tools/build_expanded_corporations_codex.py
Generates the comprehensive, encyclopedic master codex:
SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_CORPORATIONS.md
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def wrap_box(b):
    return "```text\n" + b + "\n```\n\n"

def build_codex():
    sections = []
    
    # Title & Subtitle
    sections.append("# SOMNARAK — The Sovereign Institutions & Municipal Corporate Trusts\n")
    sections.append("## The Pentagonal Institutional Doctrine, Industrial Guilds & Inter-Agency Jurisdiction\n")
    sections.append("### Master Institutional Codex — Year 4,238 Post-Exile Restoration Epoch\n\n")
    
    # Master Dossier Box
    dossier = make_box("SOVEREIGN INSTITUTIONAL MATRIX: THE FIVE WINGS OF SOMNARAK", [
        "ARCHIVE CODE     : CORP-SOVEREIGN-PENTAGON-4238",
        "RATIFYING BODY   : The High Council of Sighs & Institutional Directorate",
        "PRIMARY THEATER  : Sovereign Territory of Somnarak & Planetary Frontiers",
        "EPOCH            : Year 4,238 (The Dawn of Hope Restoration)",
        "---",
        "THE FIVE AUTONOMOUS INSTITUTIONAL WINGS:",
        "1. Reverie Directorate (R.D.)   : Facility 01 Containment & M.A.W. Forge",
        "2. Exploration Decreed (SED)    : Subterranean Cartography & Abyss Fleet",
        "3. Cleanup Descend (UCD)        : Tactical Urban Purge & Anti-Fray Force",
        "4. The Memory Archive (Gieok)   : Sub-Alpha Spire & Key Page Extraction",
        "5. The Horizon Caravan (Jipyeong): Trans-Desolate Transit & Inter-City Road",
        "---",
        "CIVIC INFRASTRUCTURE CONGLOMERATES & INDUSTRIAL TRUSTS:",
        "- Siphon Guilds (Chakhwi)       : Liquid Han Mining & Geothermal Power",
        "- Weavers' Syndicates (Jikjo)   : Acoustic Veil Weaving & Defense Fabrics",
        "- Acoustic Manufactories        : Heavy Kinetic Artillery & Sonic Pylons",
        "- Municipal Underworld Frays    : Black-Market Cartels & Usury Houses"
    ])
    sections.append(wrap_box(dossier))
    
    # Epigraph
    sections.append('> *"Somnarak does not survive by hope alone; it survives through the division of impossible labor. One institution holds the howling abyss beneath the floorboards; one descends into the dark to chart where we will dig; one polices the blood-drenched alleys where humanity sells its tears for bread; one remembers the names of those the city erased; and one builds the iron road across the burning sand so that we are never alone again."*\n')
    sections.append('> — High Director Majin & Grand Pathfinder Kael, Joint Treaty of the Five Spikes\n\n')
    sections.append('---\n\n')
    
    # Section I: Executive Overview & The Pentagonal Doctrine
    sections.append("## Section I: Ontological Foundation & The Pentagonal Doctrine\n\n")
    sections.append("The survival of human civilization upon the post-cataclysmic world of **Mugenhan (무극한 / 無極限)** rests upon a delicate, multipolar equilibrium. Somnarak is not a unified civic commonwealth in the ancient sense; it is a fortress metropolis governed through the **Pentagonal Institutional Doctrine (오극 제도론 / 五極 制度論)**—five sovereign operational wings functioning alongside the civilian municipal bureaucracy of the **Council of Sighs (탄식의 평의회)**.\n\n")
    sections.append("Each of the Five Sovereign Institutions possesses total jurisdictional extraterritoriality within its assigned operational theater:\n\n")
    
    pentagon_table = make_box("THE PENTAGONAL JURISDICTIONAL MANDATE", [
        "INSTITUTION           | OPERATIONAL DOMAIN      | STRATEGIC MANDATE",
        "----------------------+-------------------------+--------------------",
        "Reverie Directorate   | Subterranean Facility 01| Containment & M.A.W.",
        "Exploration Decreed   | Deep Abyssal Strata     | Maw Cartography",
        "Cleanup Descend       | Municipal Underworld    | Anti-Fray Purge",
        "The Memory Archive    | Sub-Alpha Roots (-3.2km)| Mnemonic Key Pages",
        "The Horizon Caravan   | The Desolate (Overland) | Inter-City Bridge"
    ])
    sections.append(wrap_box(pentagon_table))
    
    sections.append("Under the **Treaty of the Five Spikes (오침조약 / 五針條約)** signed following the great fracture of Year 3,850, no single institution—including the High Council—may usurp the internal chains of command, proprietary technologies, or field armories of another. If the Reverie Directorate locks its blast gates, the Council cannot enter. If the Horizon Caravan launches the Drift Throne into the wastes, no municipal warrant may arrest its treads.\n\n")
    sections.append('---\n\n')
    
    # Section II: The Five Sovereign Institutions
    sections.append("## Section II: The Five Sovereign Institutions (오대 주권 기관)\n\n")
    
    # 2.1 Reverie Directorate
    sections.append("### 2.1 The Reverie Directorate (리버리 지부 — Riberi Jibu / R.D.)\n\n")
    sections.append("Operating directly beneath the towering bio-mechanical **Alpha Tree (알파 나무)** in Zone A, the Reverie Directorate oversees **Facility 01 ('The Hand of Change')**—humanity's primary subterranean containment and sorrow-refining complex.\n\n")
    sections.append("- **Sovereign Headquarters:** Subterranean Facility 01, Zone A (Depths -100m to -1,200m).\n")
    sections.append("- **Primary Operational Mandate:** Permanent acoustic containment of five hundred categorized Sorrow Entities, industrial extraction of M.A.W. (Mental Armament Wear) weapons and suits, and covert management of the **Absolvohan Cycle Device**.\n")
    sections.append("- **Insignia & Colors:** The Broken Hourglass surmounted by the Golden Siphon; obsidian black and burnished bronze.\n\n")
    
    rd_box = make_box("FACILITY 01: EIGHT-FLOOR OPERATIONAL COMMAND", [
        "FLOOR & SECTOR        | EXECUTIVE LEAD          | FUNCTION & CAPACITY",
        "----------------------+-------------------------+--------------------",
        "Floor 1: Neutral Core | Director Majin & Seiyon | Central Decision",
        "Floor 2: Maw's Keep   | Containment Lead Dekan  | Acoustic Clamps",
        "Floor 3: Extraction   | Extraction Lead Zyrak   | M.A.W. Crucible",
        "Floor 4: Insight Forge| Research Lead Ayshuk    | Sorrow Physics",
        "Floor 5: Border Sentry| Border Lead Mellda      | Perimeter Lockdown",
        "Floor 6: Memory Vault | Archive Lead Marjuk     | Stasis Scribe Well",
        "Floor 7: Shadow Corps | Lead Operative Ishall   | Black Ops Strike",
        "Floor 8: Gate Watch   | Boundary Vanguard Xyan  | Outland Airlocks"
    ])
    sections.append(wrap_box(rd_box))
    
    sections.append("Within Facility 01, Supreme Director Majin exercises absolute emergency martial law. The Directorate maintains an internal cadre of over four thousand specialized containment Wardens, Enforcers, and Extraction Technicians trained to perform the Four Work Types (**Ferrehan, Flerehan, Pugnahan, and Viderehan**).\n\n")
    
    # 2.2 Somnarak Exploration Decreed
    sections.append("### 2.2 Somnarak Exploration Decreed (소마나락 탐사령 — SED Corps)\n\n")
    sections.append("The **SED Corps** serves as the city's exploratory vanguard, driving deep vertical boreholes and abyssal shafts through the bedrock beneath Somnarak to map the primordial subterranean channels of the **Weeping (눈물의 강)**.\n\n")
    sections.append("- **Sovereign Headquarters:** The Bore Fleet Bastion, Sub-Level 7, Zone E.\n")
    sections.append("- **Primary Operational Mandate:** Deep subterranean cartography, void geology, structural acoustic stabilization of sinking city foundations, and retrieval of Before-Time industrial relics.\n")
    sections.append("- **Insignia & Colors:** The Golden Piton driving into Cracked Basalt; deep rust orange and steel grey.\n\n")
    
    sed_box = make_box("SED CORPS: THE SEVEN-MEMBER VANGUARD CADRE", [
        "OPERATIVE SPECIALIST  | ROLE & ARMAMENT         | TACTICAL FUNCTION",
        "----------------------+-------------------------+--------------------",
        "Yeonhwa (Cartographer)| Expedition Commander    | Resonant Compass",
        "Doha (The Mason)      | Heavy Vanguard Breaker  | Basalt Maul / Prow",
        "Harin (The Sentinel)  | Aegis Defensive Anchor  | Heavy Kinetic Wall",
        "Sora (The Dreamer)    | Veil Sensory Diviner    | Sub-Acoustic Radar",
        "Minjae (The Chronicler| Biological Scribe       | Suture Relic Pen",
        "Jisoo (The Accountant)| Resource Quartermaster  | Weight Calculations",
        "The Silent One        | Deep Abyss Pathbreaker  | Primordial Siphon"
    ])
    sections.append(wrap_box(sed_box))
    
    sections.append("The SED operates the colossal tracked mining rigs known as the **Bore Fleet (천공 함대)**, traversing vertical drop shafts down to -5,000 meters into the mantle of Mugenhan. Their operational exploits are immortalized in the seven chapters of **Katabagil (카타바길 — The Seven Descents)**.\n\n")
    
    # 2.3 Underworld Cleanup Descend
    sections.append("### 2.3 Underworld Cleanup Descend (지하 청소령 — UCD Task Force)\n\n")
    sections.append("The **UCD Task Force** functions as Somnarak's tactical urban pacification and anti-contraband enforcement wing. While the municipal City Guard mans static checkpoints in Zone A and C, the UCD patrols the sunless alleys, flooded drainage basins, and criminal shantytowns of **The Raw (날것의 구역 — Zone B)**.\n\n")
    sections.append("- **Sovereign Headquarters:** The Sunken Bastion, Municipal Drainage District 4, Zone B.\n")
    sections.append("- **Primary Operational Mandate:** Neutralization of weaponized sorrow syndicates, interception of unregistered Sorrow Entity trafficking, suppression of rogue Frays, and enforcement of the Seven Taboos.\n")
    sections.append("- **Insignia & Colors:** The Cleansing Broom crossed over a Leaded Cask; midnight blue and polished chrome.\n\n")
    
    ucd_box = make_box("UCD TASK FORCE: URBAN PURGE SQUAD CADRE", [
        "TACTICAL OFFICER      | SPECIALTY & LOADOUT     | PURGE OPERATION",
        "----------------------+-------------------------+--------------------",
        "Taeho (The Commander) | Riot Cleaver & Aegis    | Op 1: Velumtal",
        "Yuna (The Auditor)    | Forensic Siphon Scanner | Op 2: Lethepyo",
        "Minho (Investigator)  | Counterfeit Veil Probe  | Op 3: Messischwi",
        "Soojin (The Handler)  | Cryogenic Leaded Casks  | Op 4: Usurachae",
        "Joon (The Engineer)   | Kinetic Blast Gates     | Op 5: Therionok",
        "Echo (The Infiltrator)| Silent Monomolecular Rib| Op 6: Basileugung"
    ])
    sections.append(wrap_box(ucd_box))
    
    sections.append("The UCD's six major campaigns—documenting the takedown of the Veil Smugglers, Memory Laundering Dens, and the Underworld King—are recorded in **Katharcheok (카타르체옥 — The Six Pacifications)**.\n\n")
    
    # 2.4 The Memory Archive
    sections.append("### 2.4 The Memory Archive (기억 저장소 — Gieok Jeojangso)\n\n")
    sections.append("Carved directly inside the sub-Alpha root strata between -2,350m and -3,250m, the **Memory Archive** is the sovereign sanctuary of human consciousness. Here, memories deemed too traumatic, destabilizing, or corrosive for surface life are surgically extracted, cataloged into living books, and transmuted into sovereign **Key Pages (핵심 책장)**.\n\n")
    sections.append("- **Sovereign Headquarters:** The Spire of Living Pages, Deep Sub-Alpha Roots (-3,250m).\n")
    sections.append("- **Primary Operational Mandate:** Reception and pacification of destabilized human souls, archival codification of planetary history prior to the Great Fracture, and synthesis of mnemonic armaments.\n")
    sections.append("- **Insignia & Colors:** The Open Book with an Iris of Silver Light; starlight silver and parchment cream.\n\n")
    
    gieok_box = make_box("THE MEMORY ARCHIVE: SEVEN STRATA RECEPTIONS", [
        "FLOOR & STRATUM       | KEEPING ARCHIVIST       | PSYCHIC TRAUMA KEY",
        "----------------------+-------------------------+--------------------",
        "Floor 1: Ash Strata   | Keeper Vaelen           | Lost Origins",
        "Floor 2: Salt Strata  | Keeper Miran            | Famine & Bitter Han",
        "Floor 3: Iron Strata  | Keeper Brand            | Industrial Mutilation",
        "Floor 4: Rust Strata  | Keeper Sula             | Decay & Abandonment",
        "Floor 5: Silence Strat| Keeper Kaelen           | Acoustic Censorship",
        "Floor 6: Lamentation  | Keeper Elyra            | The First Weeping",
        "Floor 7: The Original | The Original Archivist  | Planetary Awakening"
    ])
    sections.append(wrap_box(gieok_box))
    
    sections.append("Led by the synthesized consciousness of **Secretary Seiyon**, the Archive executes Receptions using dialectic inquests and 10-node combat chambers, transmuting centuries of human agony into enduring crystalline strength.\n\n")
    
    # 2.5 The Horizon Caravan
    sections.append("### 2.5 The Horizon Caravan (지평선대 — Jipyeongseon Dae)\n\n")
    sections.append("The **Horizon Caravan** is Somnarak's trans-continental overland expeditionary armada. Operating aboard the 142.5-meter mobile sand dreadnought **The Drift Throne (표류옥좌)**, the Caravan rejects the static isolation of city walls to chart the burning wastes of **The Desolate (황야)**.\n\n")
    sections.append("- **Sovereign Headquarters:** The Drift Throne Flagship (Class IV Mobile Sand Cruiser).\n")
    sections.append("- **Primary Operational Mandate:** Exploration of the outer badlands, establishment of fortified waystations across 4,800 kilometers of desert, inter-city diplomacy with Cheonbulok and Mugeukji, and cross-continental convoy defense.\n")
    sections.append("- **Insignia & Colors:** The Golden Compass Wheel upon Obsidian Dunes; desert khaki, copper, and amber.\n\n")
    
    jipyeong_box = make_box("THE HORIZON CARAVAN: EXPEDITIONARY ARMADA CADRE", [
        "COMMAND SPECIALIST    | ROLE & EQUIPMENT        | EXPEDITION MILESTONE",
        "----------------------+-------------------------+--------------------",
        "Kael (The Drift King) | Supreme Commander       | The Gate of Sighs",
        "Hwaran (The Guide)    | Caldera Liaison Staff   | Sea of Glass Drift",
        "Wright Gwan (Engineer)| Ley-Siphon Drive Engine | Slag Pit Arena Duel",
        "Sora (Chief Ley-Seer) | 528 Hz Acoustic Sonar   | Magma Core Quench",
        "Heavy Dredger Corps   | Class IV Exo-Armors     | Corsair Defile Rout",
        "Dune Scout Outriders  | Supersonic Sand-Skimmers| Mugeukji Boundary"
    ])
    sections.append(wrap_box(jipyeong_box))
    
    sections.append("The six trans-desolate crossings of the Horizon Caravan—culminating in the rescue of 400 Cheonbulok foundry refugees and the planting of the Horizon Beacon at the edge of Mugeukji—are recorded in **The Jipyeongseondae Chronicles**.\n\n")
    sections.append('---\n\n')
    
    # Section III: Municipal Corporate Conglomerates, Industrial Guilds & Workshops
    sections.append("## Section III: Municipal Corporate Conglomerates & Industrial Guilds\n\n")
    sections.append("Beneath the overarching aegis of the Five Sovereign Institutions, Somnarak's daily industrial economy is driven by private and semi-civic corporate trusts. These commercial conglomerates supply the raw materials, refined energy conduits, armor fabrics, and heavy armaments required to keep the city alive.\n\n")
    
    # 3.1 Siphon Guilds
    sections.append("### 3.1 The Sovereign Siphon Guilds (착취 길드 / Chakhwi Gildeu)\n\n")
    sections.append("The Siphon Guilds hold the municipal monopoly over energy extraction, drawing liquid sorrow from the deep underground and refining it into usable electrical, acoustic, and thermal currents:\n\n")
    sections.append("1. **Giltong Power & Extraction Trust (길통 동력 추출 공사):**\n")
    sections.append("   - Operates the monumental basalt pipeline arrays connecting Zone A to the subterranean Weeping.\n")
    sections.append("   - Refines raw Liquid Han into stable **Han-Batteries** that illuminate Somnarak's streetlamps and charge Warden shock weapons.\n")
    sections.append("   - Employs over twelve thousand high-risk siphon divers who wear heavy rubberized suits to repair cracked conduits beneath the city floor.\n\n")
    sections.append("2. **Alpha Hydrological Consortium (알파 수문 연합):**\n")
    sections.append("   - Manages the city's closed-loop water treatment, atmospheric condenser towers, and cryogenic brine circuits.\n")
    sections.append("   - Maintains the emergency quenching systems that prevent industrial furnaces in Zone C from undergoing catastrophic thermal meltdowns.\n\n")
    sections.append("3. **Basalt & Adamantine Smelting Guild (현무암 제련 길드):**\n")
    sections.append("   - Controls the heavy blast foundries located along the border of Zone C and Zone D.\n")
    sections.append("   - Smelts volcanic basalt with refined iron slag to produce the dense, impact-absorbing armor plates used in blast doors, caterpillar tracks, and Warden fortress shields.\n\n")
    
    # 3.2 Weavers' Syndicates
    sections.append("### 3.2 The Weavers' Syndicates (직조 연합 / Jikjo Yeonhap)\n\n")
    sections.append("In a city where sound can trigger psychological corrosion and despair, fabric is not mere clothing—it is armor:\n\n")
    sections.append("1. **The Silk of Oblivion Manufactory (망각의 비단 공방):**\n")
    sections.append("   - Produces the standard **Veil Fabrics (베일 직조물)** worn by over two million citizens to dampen the ambient howling of Sorrow Entities.\n")
    sections.append("   - Crafts specialized sound-canceling cowls, acoustic ear-seals, and memory-suppression bandages.\n\n")
    sections.append("2. **Woven Armament Works (직조 병기 제작소):**\n")
    sections.append("   - Works under contract with the Reverie Directorate to weave M.A.W. suit linings.\n")
    sections.append("   - Combines synthetic aramid fibers with crystallized sorrow threads to provide defense against the four elemental affinities: Grudge, Lament, Void, and Weight.\n\n")
    
    # 3.3 Acoustic Defense Manufactories
    sections.append("### 3.3 Acoustic Defense Manufactories (음향 방어 공방)\n\n")
    sections.append("1. **The Iron Bell Forge (철종 공방):**\n")
    sections.append("   - Specializes in casting monolithic bronze and steel tuning forks ranging from handheld 440 Hz clappers to thirty-foot municipal resonance towers.\n")
    sections.append("   - When an Ordeal approaches the city walls, Iron Bell harmonic towers strike in synchronized counter-frequencies, repelling low-tier sorrow manifestations.\n\n")
    sections.append("2. **Gwan Heavy Industries (관 중공업):**\n")
    sections.append("   - Master Wright Gwan's family workshop, responsible for manufacturing pneumatic pile-drivers, tracked land-cruiser chassis, and heavy harpoon winches.\n")
    sections.append("   - Primary contractor for the Horizon Caravan's Drift Throne maintenance.\n\n")
    
    # 3.4 Underworld Commercial Frays & Shadow Syndicates
    sections.append("### 3.4 Underworld Commercial Frays & Shadow Syndicates\n\n")
    sections.append("In the unregulated underbelly of Zone B, illicit commercial enterprises thrive outside municipal law:\n\n")
    sections.append("1. **The Debt Brokerage Houses of Zone B (채무 중개 조합):**\n")
    sections.append("   - Predatory syndicates that buy municipal citizen debts from the Council of Sighs at steep discounts, employing brute-force debt collectors to extract unpaid labor.\n")
    sections.append("   - Operates clandestine bone-saw clinics where indebted citizens sell biological organs or traumatic memories to pay interest.\n\n")
    sections.append("2. **The Siphon Smugglers' Union (착취 밀수 연맹):**\n")
    sections.append("   - Criminal networks that tap illegally into Giltong pipelines to siphon unrefined Liquid Han into lead flasks for the black market.\n")
    sections.append("   - Supplies illegal sorrow-stills that brew 'Black Water'—a potent, highly addictive narcotic that numbs physical pain while accelerating mental corrosion.\n\n")
    sections.append("3. **The Flesh-Chirurgeon Frays (육체 외과 프레이):**\n")
    sections.append("   - Rogue biomedical workshops that install black-market cyborg prosthetics, crude mechanical limbs, and weaponized piston arms.\n")
    sections.append("   - Responsible for creating rogue cyborg outlaws and combat gladiators for underground pit fights.\n\n")
    sections.append('---\n\n')
    
    # Section IV: Inter-Institutional Jurisdictions & Resource Pipeline
    sections.append("## Section IV: Inter-Institutional Jurisdictions & Resource Pipeline\n\n")
    sections.append("The Five Institutions depend upon an intricate, closed-loop resource circulation network. No single wing can survive in isolation:\n\n")
    
    pipeline_box = make_box("SOMNARAK STRATEGIC RESOURCE CIRCULATION PIPELINE", [
        "ORIGINATING INSTITUTION | DELIVERED RESOURCE       | RECIPIENT WING",
        "------------------------+--------------------------+--------------------",
        "Reverie Directorate     | Extracted M.A.W. Weapons | UCD & SED Shock Teams",
        "SED Abyssal Bore Fleet  | Pre-Calamity Relic Ores  | R.D. Floor 3 Forge",
        "UCD Strike Force        | Confiscated Sorrow Casks | R.D. Containment Cells",
        "Memory Archive          | Transmuted Key Pages     | All 5 Command Staff",
        "Horizon Caravan         | Cheonbulok Rage-Crystals | Giltong Energy Grid",
        "Horizon Caravan         | Rescued Skilled Refugees | SED & UCD Engineering"
    ])
    sections.append(wrap_box(pipeline_box))
    
    sections.append("When a **Category-5 Ordeal** or **Sovereign Fracture Event** breaches municipal containment, protocol dictates the immediate activation of the **Red Accord (적색 협정)**:\n\n")
    sections.append("1. **Stage 1 (Perimeter Lock):** Horizon Caravan anchors outside city gates, establishing heavy kinetic barricades and long-range spinal cannon artillery.\n")
    sections.append("2. **Stage 2 (Street Sweep):** UCD seals Zone B and C escape avenues with non-lethal acoustic gas and leaded blast gates.\n")
    sections.append("3. **Stage 3 (Abyssal Venting):** SED diverts excess liquid sorrow down borehole release shafts to prevent urban flooding.\n")
    sections.append("4. **Stage 4 (Direct Suppression):** Reverie Directorate Floor 7 Shadow Corps and Floor 1 Command deploy with Grade Omega M.A.W. gear to terminate the sovereign core.\n")
    sections.append("5. **Stage 5 (Mnemonic Recovery):** Memory Archive dispatches projection lenses to gather dissipated soul fragments, preventing residual haunting.\n\n")
    sections.append('---\n\n')
    
    # Section V: The Hexagonal Economic Flow & The Debt Ledger
    sections.append("## Section V: The Hexagonal Economic Flow & The Debt Ledger\n\n")
    sections.append("Economic survival in Somnarak is dictated by the **Municipal Debt Ledger (부채 총장)**. Debt is not merely financial; it is a quantified civic obligation that determines citizen survival tier, housing assignment, food rations, and acoustic curfew privileges:\n\n")
    sections.append("- **Tier 1 (Sovereign Exemption):** Institutional Command, Echo-Core supervisors, and Master Craftsmen. Zero debt; total freedom of movement across Zones A through E.\n")
    sections.append("- **Tier 2 (Indebted Citizens / Zone C):** Standard laborers, workshop artisans, and municipal clerks. Debt interest capped at 4% monthly; eligible for clean water rations and Veil cowls.\n")
    sections.append("- **Tier 3 (Submerged Citizens / Zone B):** Heavy miners, drainage sweepers, and indentured factory hands. Debt exceeding 50,000 credits; subject to mandatory labor drafts and asset forfeiture.\n")
    sections.append("- **Tier 4 (The Unclaimed / The Raw):** Outlaws, deserters, and broken Fray members. Debts purchased by syndicate brokers; zero legal protections under municipal law.\n\n")
    sections.append("The Five Institutions operate outside the Debt Ledger. An operative who joins the Reverie Directorate, the SED Bore Fleet, the UCD Strike Force, or the Horizon Caravan has their entire civic debt erased immediately upon signing the blood charter. In return, they offer their life, their blood, and their sanity to the defense of humanity.\n\n")
    sections.append('---\n\n')
    
    # Section VI: The Dawn Accord & Planetary Transmutation (Year 4,238)
    sections.append("## Section VI: The Dawn Accord & Planetary Transmutation (Year 4,238)\n\n")
    sections.append("In the year 4,238, following the completion of the 1,778th Absolvohan cycle and the successful return of the Horizon Caravan from Cheonbulok, the leaders of the Five Institutions signed the historic **Dawn Accord (여명의 협약 / 黎明의 協約)**.\n\n")
    sections.append("For the first time in four millennia, the institutions shifted their grand doctrine from mere static containment to **active planetary healing**:\n\n")
    sections.append("1. **The 45% Planetary Healing Target:** Integrating the Absolvohan's energy release with the Horizon Caravan's 4,800-kilometer acoustic beacon chain, the Five Wings aim to transmute 45% of Mugenhan's crystallized sorrow into stable, living soil.\n")
    sections.append("2. **The Tri-City Continental Alliance:** Establishing permanent trade, military defense, and resource exchange between Somnarak, the volcanic calderas of Cheonbulok, and the silent frontier of Mugeukji.\n")
    sections.append("3. **The Dissolution of the Raw:** Reclaiming the criminal underworld of Zone B through clean municipal water, free Veil distribution, and the dismantlement of predatory usury syndicates.\n\n")
    
    closing_box = make_box("EXPEDITIONARY RATIFICATION: THE DAWN ACCORD", [
        "RATIFYING COMMANDERS : Majin (R.D.), Yeonhwa (SED), Taeho (UCD),",
        "                       Seiyon (Gieok), Kael (Jipyeongseon Dae)",
        "PRIMARY PROTOCOL     : The Continental Dawn Initiative (Year 4,238)",
        "STATUS               : ACTIVE AND CANONICALLY RATIFIED",
        "---",
        "\"The sorrow was our cradle. The iron was our shield.",
        " Now we build the world that will outlive our grief.\"",
        "- Supreme Directorate Joint Proclamation"
    ])
    sections.append(wrap_box(closing_box))
    
    sections.append("The Five Institutions of Somnarak stand vigilant—no longer five isolated fortresses cowering in the dark, but five pillars holding up the morning sky.\n")
    
    return "".join(sections)

if __name__ == "__main__":
    content = build_codex()
    out_path = "SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_CORPORATIONS.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SOMNARAK_CORPORATIONS.md expanded successfully!")
