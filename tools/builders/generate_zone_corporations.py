#!/usr/bin/env python3
"""
tools/generate_zone_corporations.py
Generates SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_ZONE_CORPORATIONS.md
Codifies:
1. The 25 Zone Corporations (exactly 5 corporations per Zone across Zones A, B, C, D, E).
2. The Curfew Sanitation Corps (Haz-scorchers & Cleansers).
3. Giltong as Project Somnarak's sole Arbiter-tier authority.
4. The Outer Cities of Mugenhan as living, populated urban metropolises.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from box_formatter import make_box

def wrap_box(b):
    return "```text\n" + b + "\n```\n\n"

def build_codex():
    content = []
    content.append("# SOMNARAK — The Municipal Zone Corporations & Curfew Sanitation Corps\n")
    content.append("## The Twenty-Five Zone Charters, Haz-Scorchers & Sovereign Arbiter Mandate\n")
    content.append("### Master Demographic & Commercial Codex — Year 4,238 Restoration Epoch\n\n")

    box1 = make_box("MUNICIPAL ZONE CORPORATIONS — YEAR 4,238", [
        "JURISDICTION : The High Council of Sighs & Five Municipal Zones",
        "CLASSIFICATION: Sovereign Corporate Charters (CORP-ZONE-001 to 025)",
        "ARCHITECTURE  : Pentagonal Zone Division — Exactly 5 Corps Per Zone",
        "---",
        "Zone A (The Veil)      : 5 Sovereign Administrative & Refining Corps",
        "Zone B (The Raw)       : 5 Undercity Sump, Drainage & Slag Corps",
        "Zone C (Collector Row) : 5 Mnemonic Debt, Ledger & Currency Corps",
        "Zone D (Echo Forge)    : 5 Crucible Foundry & Resonance Apparatus Corps",
        "Zone E (Bastion Ring)  : 5 Deep-Bore, Transit & Frontier Defense Corps",
        "---",
        "ARBITER JURISDICTION   : Giltong Cadre Holds Sovereign Arbiter Law",
        "CURFEW SANITATION      : Haz-Scorchers (Thermal) & Cleansers (Chemical)"
    ], width=71)
    content.append(wrap_box(box1))

    content.append("> *\"The ancient world built twenty-six global monopolies that choked the horizon until their wars set the sky on fire. Somnarak does not permit global sprawl. Here, each Zone is an engine of exactly five corporations—chained together by debt, watched by the Council, and policed by the Breachers. Beyond our perimeter walls, the other cities of Mugenhan build their own spires, their own laws, and their own machines. We do not govern the planet; we govern our survival.\"*\n")
    content.append("> — High Chancellor O-Gwan, Municipal Address to the Council of Sighs\n\n")
    content.append("---\n\n")

    content.append("## Section I: The Municipal Zone Corporate Doctrine (5 Corps Per Zone)\n\n")
    content.append("In the civic governance of Somnarak, corporate power is deliberately decentralised across the city's five geographic and societal sectors. Rather than permitting corporate conglomerates to establish monopolistic hegemony across the entire metropolis, the Council of Sighs enforces the **Zone Quinquennial Law (구역 5사제 / 區域 五社制)**: exactly five chartered corporations are licensed to operate within each Zone.\n\n")
    content.append("Each Zone's corporate cluster forms an interdependent operational ecosystem:\n\n")
    content.append("- **Zone A (The Veil):** Administrative governance, sovereign energy refining, high-spire architecture, and arbiter registry.\n")
    content.append("- **Zone B (The Raw):** Heavy industrial scrap recycling, deep-culvert drainage, curfew thermal incineration, and tenement housing.\n")
    content.append("- **Zone C (Collector's Row):** Mnemonic banking, debt bond underwriting, usury liquidation, and chemical sanitation.\n")
    content.append("- **Zone D (The Echo Forge):** Heavy metallurgical casting, acoustic instrumentation, biological cybernetics, and resonance pigment labs.\n")
    content.append("- **Zone E (The Bastion Ring):** Subterranean drilling, trans-Desolate transit crawlers, perimeter artillery, and frontier quarantine.\n\n")

    box2 = make_box("ZONE CORPORATE MATRIX (5 CORPS PER ZONE)", [
        "ZONE A (THE VEIL) : ADMINISTRATIVE & HIGH REFINING",
        "  A-01: Cheonsang Han-Refining    | A-02: Baek-Aegis Architecture",
        "  A-03: Giltong Sovereign Bureau  | A-04: Central Siphon Energy",
        "  A-05: Scribe Patent Tribunal    |",
        "---",
        "ZONE B (THE RAW) : SUMP, DRAINAGE & INDUSTRIAL LABOR",
        "  B-01: Undercity Slag-Reclaim    | B-02: Asbestos Drainage",
        "  B-03: Haz-Scorchers Sanitation  | B-04: Contraband Smelting",
        "  B-05: Raw Shanty Housing        |",
        "---",
        "ZONE C (COLLECTOR ROW) : FINANCIAL LEDGER & RECEPTION",
        "  C-01: Municipal Debt Registry   | C-02: Mnemonic Ledger Clearing",
        "  C-03: Usury Liquidation Bureau  | C-04: Cleansers Chemical Corp",
        "  C-05: Standard Coin & Crystal   |",
        "---",
        "ZONE D (ECHO FORGE) : CRUCIBLE SMELTING & APPARATUS",
        "  D-01: Great Crucible Foundry    | D-02: Resonance Instrument",
        "  D-03: Doll Maker Biological     | D-04: Basalt Carapace Forges",
        "  D-05: Echo-Pigment Synthetics   |",
        "---",
        "ZONE E (BASTION RING) : BORE DRILLING & PERIMETER DEFENSE",
        "  E-01: Deep-Bore Trenching Corp  | E-02: Trans-Desolate Crawler",
        "  E-03: Perimeter Wall Defense    | E-04: Overland Supply Board",
        "  E-05: Frontier Quarantine Gate  |"
    ], width=71)
    content.append(wrap_box(box2))

    content.append("## Section II: Zone A Corporate Directory (The Veil & High Spire)\n\n")
    content.append("Zone A represents the political, administrative, and technological summit of Somnarak. Enclosed beneath the protective aura of the bio-mechanical **Alpha Tree (알파 나무)**, Zone A's five corporations maintain the core life-support, energy, and legislative systems of the metropolis:\n\n")
    content.append("### A-01: Cheonsang Han-Refining Syndicate (천상 한 정제 공사)\n")
    content.append("- **Municipal Charter:** CORP-ZA-001\n")
    content.append("- **Operational Domain:** High-purity liquid Han extraction, catalytic atmospheric filtration, and upper-city Veil density generators.\n")
    content.append("- **Core Technology:** The Cheonsang Siphon Spire, which draws raw ambient sorrow from the lower atmosphere and refines it into Grade 4 and Grade 5 stabilized liquid Han used to power the Council Spire.\n\n")
    content.append("### A-02: Baek-Aegis Architecture Trust (백호 건축 신탁)\n")
    content.append("- **Municipal Charter:** CORP-ZA-002\n")
    content.append("- **Operational Domain:** Structural engineering of resonance-nullifying bastions, acoustic insulation tiles, and municipal bunker foundations.\n")
    content.append("- **Core Technology:** Basalt-alloy composite interlocking masonry treated with leaded acoustic damping resins, capable of withstanding Rank V tectonic tremors without wall fracture.\n\n")
    content.append("### A-03: Giltong Sovereign Registry Bureau (길통 주권 등기국)\n")
    content.append("- **Municipal Charter:** CORP-ZA-003\n")
    content.append("- **Operational Domain:** The administrative civil arm of the Giltong Arbiter Cadre. Manages inter-zone passports, sovereign passage rights, corporate patent disputes, and municipal treaty registration.\n")
    content.append("- **Sovereign Arbiter Authority:** Holds absolute extraterritorial jurisdiction granted directly by the Council of Sighs. Possesses unilateral legal veto over all lower corporate actions.\n\n")
    content.append("### A-04: Central Siphon Energy Board (중앙 착취 에너지 공단)\n")
    content.append("- **Municipal Charter:** CORP-ZA-004\n")
    content.append("- **Operational Domain:** Municipal power generation, primary geothermal steam networks, and emergency acoustic barrier batteries.\n")
    content.append("- **Core Technology:** The Grand Basalt Conduits linking subterranean geothermal reservoirs to upper-tier municipal power grids.\n\n")
    content.append("### A-05: Scribe-General Patent Tribunal (서기 총감 특허원)\n")
    content.append("- **Municipal Charter:** CORP-ZA-005\n")
    content.append("- **Operational Domain:** Registration, judicial arbitration, and enforcement of proprietary workshop blueprints, M.A.W. alloy patents, and engram formulations.\n")
    content.append("- **Jurisdiction:** Resolves intellectual property disputes between the Six Great Workshops and prosecutes unlicensed contraband copying.\n\n")

    content.append("---\n\n")

    content.append("## Section III: Zone B Corporate Directory (The Raw & Undercity Sump)\n\n")
    content.append("Zone B, known as **The Raw (날것의 구역)**, is the dense industrial and drainage underbelly of Somnarak. Located in the shadow of the central spires, its five corporations handle the hazardous, toxic, and physical reclamation tasks essential to municipal survival:\n\n")
    content.append("### B-01: Undercity Slag-Reclamation Corp (지하 슬래그 재생 공사)\n")
    content.append("- **Municipal Charter:** CORP-ZB-001\n")
    content.append("- **Operational Domain:** Heavy industrial slag recycling, metal scrap recovery from breach zones, and basalt crushed-gravel production.\n")
    content.append("- **Role in Undercity:** Operates the monumental smelting funnels in Drainage District 3, extracting structural iron from discarded foundry slag.\n\n")
    content.append("### B-02: Asbestos Drainage & Siphon Logistics (석면 배수 물류)\n")
    content.append("- **Municipal Charter:** CORP-ZB-002\n")
    content.append("- **Operational Domain:** Maintenance of the 400-kilometer subterranean culvert and sewer network, toxic stormwater channeling, and chemical runoff disposal.\n")
    content.append("- **Hazard Protocols:** Deploys deep-well dredge teams in pressurized asbestos dive suits to clear blockages caused by crystallized sorrow sludge.\n\n")
    content.append("### B-03: The Haz-Scorchers Sanitation Guild (방호 소각수 조합)\n")
    content.append("- **Municipal Charter:** CORP-ZB-003\n")
    content.append("- **Operational Domain:** Curfew thermal sanitation, biological residue incineration, and illegal graft destruction during the Fourth Watch.\n")
    content.append("- **Field Personnel:** The Haz-Scorchers (방호 소각수)—armored municipal incinerator crews equipped with heavy slag-burners and thermal lances.\n\n")
    content.append("### B-04: Contraband Reclamation & Smelting Trust (밀수 회수 제련 신탁)\n")
    content.append("- **Municipal Charter:** CORP-ZB-004\n")
    content.append("- **Operational Domain:** Seizure, decontamination, and chemical re-smelting of black-market weapons, unlicensed forge frames, and illicit M.A.W. knockoffs seized by the UCD.\n")
    content.append("- **Oversight:** Operates under joint military supervision of the Underworld Cleanup Descend.\n\n")
    content.append("### B-05: Raw Shanty Housing Directorate (날것 주거 관리청)\n")
    content.append("- **Municipal Charter:** CORP-ZB-005\n")
    content.append("- **Operational Domain:** Tenement housing administration, modular zinc sheet distribution, and structural blast wall reinforcement for low-income citizens.\n")
    content.append("- **Social Role:** Manages citizen bunkhouse leases, communal water dispensing stations, and emergency shelter blast gates.\n\n")

    content.append("---\n\n")

    content.append("## Section IV: Zone C Corporate Directory (Collector's Row & Financial Concourse)\n\n")
    content.append("Zone C is the administrative and financial hub of debt management, accounting, and legal recording. Its five corporations govern the circulation of credits, the custody of ledgers, and municipal chemical decontamination:\n\n")
    content.append("### C-01: Municipal Debt Registry Concourse (시립 채무 등기 공단)\n")
    content.append("- **Municipal Charter:** CORP-ZC-001\n")
    content.append("- **Operational Domain:** Maintenance of the Central Municipal Debt Ledger, issuance of civic labor bonds, and citizen debt tier classification.\n")
    content.append("- **Authority:** Coordinates with the Collector Bureau to calculate mandatory labor hours and asset garnishments for indebted citizens.\n\n")
    content.append("### C-02: Mnemonic Ledger Clearinghouse (기억 원장 청산소)\n")
    content.append("- **Municipal Charter:** CORP-ZC-002\n")
    content.append("- **Operational Domain:** Appraisal, archival, and financial liquidation of recovered memory fragments, Key Pages, and unrecorded personal records.\n")
    content.append("- **Institutional Link:** Works in direct commercial partnership with the Memory Archive (Gieok Jeojangso) on Floor 01.\n\n")
    content.append("### C-03: The Usury Liquidation Bureau (고리 청산 감찰국)\n")
    content.append("- **Municipal Charter:** CORP-ZC-003\n")
    content.append("- **Operational Domain:** Regulation of interest rates, audit of licensed debt brokerage houses, and prosecution of predatory underworld loan sharks exceeding the 4% legal ceiling.\n")
    content.append("- **Enforcement:** Employs financial auditors and armed bailiffs authorized to seize collateral property.\n\n")
    content.append("### C-04: Cleansers Chemical Sanitation Corp (정화대 화학 방역 공사)\n")
    content.append("- **Municipal Charter:** CORP-ZC-004\n")
    content.append("- **Operational Domain:** Chemical neutralisation of sorrow contamination, acoustic wash spraying, and decontamination of public concourses.\n")
    content.append("- **Field Personnel:** The Cleansers (정화대)—specialist decontamination crews armed with high-pressure neutralizing foam tanks and acoustic scrubbers.\n\n")
    content.append("### C-05: Standard Coin & Crystal Mint (표준 주화 결정 조폐청)\n")
    content.append("- **Municipal Charter:** CORP-ZC-005\n")
    content.append("- **Operational Domain:** Minting of standardized crystalline Han currency chips, bullion storage in subterranean basalt vaults, and foreign trade exchange rates.\n")
    content.append("- **Monetary Standard:** Guarantees currency stability backed by certified liquid Han reserves held within the Council Spire.\n\n")

    content.append("---\n\n")

    content.append("## Section V: Zone D Corporate Directory (The Forge District & Echo Gardens)\n\n")
    content.append("Zone D is the industrial manufacturing, artisan, and resonance development quarter of Somnarak. Centred around the monumental foundries and acoustic workshops, its five corporations supply weapons, instrumentation, and biological cybernetics:\n\n")
    content.append("### D-01: Great Crucible Foundry Works (대도가니 주조 공방)\n")
    content.append("- **Municipal Charter:** CORP-ZD-001\n")
    content.append("- **Operational Domain:** Heavy metallurgical casting of basalt-infused steel alloys, hydraulic press operation, and structural armor chassis fabrication.\n")
    content.append("- **Production:** Supplies primary structural steel for Facility 01 containment cells and UCD breacher armor plates.\n\n")
    content.append("### D-02: Resonance Instrument Guild (공명 계측 장비 조합)\n")
    content.append("- **Municipal Charter:** CORP-ZD-002\n")
    content.append("- **Operational Domain:** Manufacturing of acoustic tuning forks, frequency prisms, emotional resonance stress meters, and M.A.W. diagnostic gauges.\n")
    content.append("- **Clientele:** Reverie Directorate research teams, workshop master wrights, and SED cartographic surveyors.\n\n")
    content.append("### D-03: Doll Maker's Biological Graft Trust (인형 제작 생체 결합 신탁)\n")
    content.append("- **Municipal Charter:** CORP-ZD-003\n")
    content.append("- **Operational Domain:** Advanced biological cybernetics, prosthetic limb synthesis, flesh-suture scaffolding, and reinforced artificial tendons.\n")
    content.append("- **Clinical Application:** Reconstructs shattered limbs of wounded wardens and UCD breachers using sorrow-neutralized biological grafts.\n\n")
    content.append("### D-04: Basalt Carapace Forges (현무암 갑각 제련소)\n")
    content.append("- **Municipal Charter:** CORP-ZD-004\n")
    content.append("- **Operational Domain:** Specialized forging of heavy kinetic breacher shields, hydraulic pile-bunkers, and seismic anchoring spikes.\n")
    content.append("- **Design:** Works closely with Workshop Cheol-Gyeong and Master Wright Gwan to forge high-density kinetic defenses.\n\n")
    content.append("### D-05: Echo-Pigment Synthetics Lab (반향 안료 합성소)\n")
    content.append("- **Municipal Charter:** CORP-ZD-005\n")
    content.append("- **Operational Domain:** Chemical synthesis of indelible emotional pigments, acoustic glass tinting, and mnemonic canvas coatings.\n")
    content.append("- **Application:** Used for protective Veil tapestry dying, ceremonial funerary shrouds, and architectural acoustic damping glazes.\n\n")

    content.append("---\n\n")

    content.append("## Section VI: Zone E Corporate Directory (The Bastion Ring & Border)\n\n")
    content.append("Zone E encompasses the outer defensive ring, the massive perimeter wall batteries, and the expeditionary deployment staging grounds. Its five corporations govern deep-abyss drilling, overland transport, and frontier quarantine:\n\n")
    content.append("### E-01: Deep-Bore Trenching & Drilling Corp (심도 시추 굴착 공사)\n")
    content.append("- **Municipal Charter:** CORP-ZE-001\n")
    content.append("- **Operational Domain:** Engineering and maintenance of heavy subterranean boring rigs, hydraulic rotary cutters, and deep-karst vertical elevator shafts.\n")
    content.append("- **Expeditionary Partner:** Primary mechanical contractor for Somnarak Exploration Decreed (SED) bore fleets.\n\n")
    content.append("### E-02: Trans-Desolate Crawler Works (사막 횡단 차체 제작소)\n")
    content.append("- **Municipal Charter:** CORP-ZE-002\n")
    content.append("- **Operational Domain:** Construction and servicing of heavy multi-tread land crawlers, glass-sand caterpillar tracks, and sand-skiff hulls.\n")
    content.append("- **Fleet Support:** Constructs the colossal chassis of the Horizon Caravan's Drift Throne and accompanying escort transports.\n\n")
    content.append("### E-03: Perimeter Wall Defense Trust (외곽 방벽 수호 신탁)\n")
    content.append("- **Municipal Charter:** CORP-ZE-003\n")
    content.append("- **Operational Domain:** Maintenance of the 30-meter reinforced basalt outer perimeter walls, automated sonic deterrent turrets, and seismic warning sensor grids.\n")
    content.append("- **Defense Role:** First line of municipal defense against rogue Sorrow Beasts and tectonic shockwaves originating in the Desolate.\n\n")
    content.append("### E-04: Overland Supply & Logistics Board (지상 보급 물류 공단)\n")
    content.append("- **Municipal Charter:** CORP-ZE-004\n")
    content.append("- **Operational Domain:** Long-range supply depot staging, hermetic vacuum-sealed ration packaging, and water purification cisterns for overland expeditions.\n")
    content.append("- **Logistics Hub:** Manages the Gatehouse Freight Depots at the northern and eastern borders of Somnarak.\n\n")
    content.append("### E-05: Frontier Quarantine & Decontamination Gate (국경 방역 검역소)\n")
    content.append("- **Municipal Charter:** CORP-ZE-005\n")
    content.append("- **Operational Domain:** Mandatory medical screening of incoming overland travelers, sorrow-spore fumigation chambers, and external contraband inspection.\n")
    content.append("- **Quarantine Mandate:** Enforces strict 72-hour quarantine holding protocols for all caravans arriving from foreign territories.\n\n")

    content.append("---\n\n")

    content.append("## Section VII: Curfew Sanitation Corps (Haz-Scorchers & Cleansers)\n\n")

    box3 = make_box("CURFEW SANITATION CORPS TACTICAL PROFILE", [
        "FORCE DESIGNATION : The Fourth Watch Sanitation Corps (02:00 to 06:00)",
        "PRIMARY ARM       : The Haz-Scorchers (Thermal Incinerators)",
        "SECONDARY ARM     : The Cleansers (Chemical Neutralizers)",
        "COMPOSITION       : 100% Human / Augmented Specialist Crews (No Robots)",
        "---",
        "HAZ-SCORCHERS LOADOUT:",
        "  Armor  : Grade 4 Asbestos Pressurized Hazard Suit & Thermal Visor",
        "  Weapon : Hydraulic Slag-Burner & Pneumatic Thermal Lance",
        "  Role   : Complete Incineration of Biological Waste & Graft Debris",
        "---",
        "CLEANSERS LOADOUT:",
        "  Armor  : Chemical-Resistant Rubberized Cowl & Vapor Filter",
        "  Weapon : High-Pressure Caustic Foam Gun & Acoustic Scrubber Tank",
        "  Role   : Neutralizing Sorrow-Spore Pools & Ground Washing",
        "---",
        "CURFEW LAW: Anyone caught on streets without Siphon Pass is burned"
    ], width=71)
    content.append(wrap_box(box3))

    content.append("During the **Fourth Watch (Midnight to Dawn / 02:00 to 06:00)**, the municipal sirens sound across Somnarak. Ambient Han thickens, and the city enters mandatory curfew lockdown. Streets, undercity alleys, and drainage culverts must be cleared of accumulated biological refuse, discarded sorrow tissue, and black-market flesh scraps before the citizens awaken.\n\n")
    content.append("This sanitation operation is **not carried out by mindless automata**. It is executed by dedicated, heavily trained human and cybernetically augmented personnel organised into two complementary municipal branches:\n\n")
    content.append("### 7.1 The Haz-Scorchers (방호 소각수 — Bangho Sogaksu)\n")
    content.append("- **Recruitment & Training:** Recruited primarily from Zone B heavy foundry veterans and retired breachers with high heat tolerance and resilient psychological constitution.\n")
    content.append("- **Equipment Profile:**\n")
    content.append("  - *Heavy Asbestos Hazard Suit:* Multi-layered heat-reflective suit lined with leaded acoustic fabric and pressurized air recirculation systems, rated to withstand 1,200°C temperatures.\n")
    content.append("  - *Hydraulic Slag-Burner:* High-temperature thermal flamer powered by pressurized liquid Han and naphtha slurry, capable of liquefying organic sorrow tissue and basalt debris within seconds.\n")
    content.append("  - *Thermal Lance:* Compact magnesium-core cutting torch used to sever welded biological grafts and breach jammed incinerator chutes.\n")
    content.append("- **Operational Mandate:** Total thermal destruction. Any unapproved organic material—whether a severed limb from an illegal suture clinic or a feral sorrow residue puddle—is incinerated on the spot.\n\n")
    content.append("### 7.2 The Cleansers (정화대 — Jeonghwadae)\n")
    content.append("- **Recruitment & Training:** Chemical technicians and environmental decontamination specialists managed by Zone C Corporation C-04.\n")
    content.append("- **Equipment Profile:**\n")
    content.append("  - *Chemical-Resistant Sealed Cowl:* Heavy rubberized full-body apron with dual-cartridge vapor scrubbers filtering airborne grief spores.\n")
    content.append("  - *High-Pressure Caustic Foam Lance:* Backpack-fed chemical sprayer discharging alkaline neutralizer that breaks down sticky sorrow-spore films.\n")
    content.append("  - *Acoustic Scrubbing Tank:* Wheeled sonic resonance tank that emits high-frequency ultrasound waves, detaching micro-crystal sorrow flakes from cobblestones.\n")
    content.append("- **Operational Mandate:** Secondary chemical sterilization. Following the Haz-Scorchers' thermal pass, the Cleansers saturate the ground with caustic wash, ensuring that no active emotional resonance remains to trigger civilian contamination at dawn.\n\n")

    content.append("---\n\n")

    content.append("## Section VIII: Sovereign Arbiters of Somnarak (Giltong's Extraterritorial Law)\n\n")
    content.append("Within the municipal hierarchy of Somnarak, **The Giltong Cadre (길통 — Giltong Bureau)** occupies the supreme sovereign position equivalent to an Arbiter. While the Council of Sighs legislates and the twenty-five Zone Corporations operate civil commerce, Giltong answers to no commercial body and obeys only the **First Sovereign Charter**.\n\n")
    content.append("### 8.1 The Arbiter Jurisdiction of Giltong\n")
    content.append("- **Unconditional Passage:** Giltong Arbiters carry the **Golden Transit Seal (금패 / 金牌)**, granting unrestricted passage across all five zones, sealed military installations, deep-stratum archives, and the Desolate frontier.\n")
    content.append("- **Extraterritorial Judicial Authority:** Giltong possesses unilateral authority to conduct audits, seize corporate assets, execute immediate field decrees against taboo violators, and halt any corporate project deemed an existential threat to the city's Composure equilibrium.\n")
    content.append("- **Absence of Subordinate Executioner Castes:** Unlike external empires that deploy secondary castes of enforcers (such as Claws or Beholders), **Giltong operates as a unified sovereign tier**. Subordinate executioner castes have not been manifested in the Somnarak canon; Giltong arbiters execute their own field adjudications directly through specialized M.A.W. resonance implements.\n\n")

    content.append("---\n\n")

    content.append("## Section IX: The Sovereign Metropolises of Mugenhan (Outer Cities Codex)\n\n")
    content.append("A foundational canon law of Mugenhan cosmology governs all exploration and geopolitical records: **all cities beyond the Desolate are living, fully populated, urban civilizations—NOT merely geological formations or physical terrain anomalies.**\n\n")

    box4 = make_box("MUGENHAN SOVEREIGN METROPOLISES OVERVIEW", [
        "SOMNARAK CITY (Corner 1) : The Fortress of Structured Han & Spires",
        "  Population : ~1.2 Billion | Structure : 5 Zones, 25 Corporations",
        "  Doctrine   : Pentagonal Institutions, Council of Sighs & Giltong",
        "---",
        "CHEONBULOK (Corner 2)    : The City of a Thousand Rages",
        "  Population : ~800 Million | Urban Form : Forged Iron Spire Citadels",
        "  Doctrine   : Emotional Combustive Fury, Military Forge Councils",
        "---",
        "MYEONGWOLSEONG (Corner 3): The City of the Bright Moon",
        "  Population : ~650 Million | Urban Form : Silvered Basalt Terraces",
        "  Doctrine   : Reflective Stasis, Lunar Mnemonic Filtration Guilds",
        "---",
        "RULE: Outer cities are sovereign civil metropolises, never mere geology"
    ], width=71)
    content.append(wrap_box(box4))

    content.append("While Somnarak's geologists and caravan pilots record the rugged terrain encountered during overland journeys—such as the Sea of Glass or the Basin of Tears—these geological features are merely the **intervening wilderness** between sovereign urban centers:\n\n")
    content.append("1. **Cheonbulok (천불록 — The City of a Thousand Rages):**\n")
    content.append("   - Located in the Northwest quadrant of Mugenhan, Cheonbulok is a sprawling metropolis of roughly 800 million citizens. Its urban landscape features immense forged-iron citadels, blast-furnace residential sectors, and sovereign warrior councils.\n")
    content.append("   - It is an urban civilization centered around the combustive channeling of emotional rage, maintaining its own internal corporate workshops, defense legions, and municipal laws.\n\n")
    content.append("2. **Myeongwolseong (명월성 — The City of the Bright Moon):**\n")
    content.append("   - Located in the Northeast quadrant of Mugenhan, Myeongwolseong is a vast urban civilization of approximately 650 million citizens constructed across tiered terraces of silvered basalt and translucent silicate domes.\n")
    content.append("   - It functions under strict lunar stasis charters, where emotional sorrow is filtered into serene, reflective memory crystals administered by sovereign monastic guilds.\n\n")
    content.append("3. **Authoring Standard:** All historical, caravan, and exploration files must treat external cities as sovereign foreign civilizations with their own municipal governance, legal charters, and populated districts, strictly prohibiting the reductive error of describing them as uninhabited rocks or natural biomes.\n\n")

    return "".join(content)

if __name__ == "__main__":
    out_dir = "/home/user/PROJECT.SOMNARAK-WIKI/SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics"
    out_path = os.path.join(out_dir, "SOMNARAK_ZONE_CORPORATIONS.md")
    text = build_codex()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Successfully generated {out_path} ({len(text)} bytes)")
