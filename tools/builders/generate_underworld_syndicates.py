#!/usr/bin/env python3
"""
tools/generate_underworld_syndicates.py
Generates SOMNARAK_UNDERWORLD_SYNDICATES.md with 100% strict 71-column ASCII text box symmetry.
"""

import sys
from box_formatter import make_box

def wrap_box(title, rows, width=71):
    box = make_box(title, rows, width)
    return "```text\n" + box + "\n```\n\n"

def build_codex():
    content = []
    
    # Title Header
    content.append("# SOMNARAK — The Five Syndicates of The Raw\n")
    content.append("## The Shadow Governance, Extralegal Hegemonies, and Subterranean Cartels\n")
    content.append("### Master Municipal Underworld Codex — CODEX-DEM-UNDERWORLD-SYNDICATES-001\n\n")
    
    # Header Box
    b0 = wrap_box("RESTRICTED UNDERWORLD INTELLIGENCE DOSSIER", [
        "ARCHIVE CODE    : CODEX-DEM-UNDERWORLD-SYNDICATES-001",
        "COMPILING BODY  : Directorate Subterranean Security Bureau (DSSB)",
        "CROSS-AUTHORITY : Collector's Bureau Special Audit & Municipal Wardens",
        "SECURITY LEVEL  : CLASS-IV RESTRICTED / SOVEREIGN RECORD ONLY",
        "PRIMARY THEATER : The Subterranean Raw (Zones B, C, D Sub-Strata)",
        "CANONICAL ERA   : Dawn of Hope Restoration (Post-Exile Year 4,238)",
        "---",
        "THE FIVE EXTRALEGAL SYNDICATES OF THE RAW:",
        "1. THE MENDERS GUILD   : Independent Fixers, Repairmen, & Husk Wardens",
        "2. THE RUST FRAYS      : Heavy Scavenger Miners & Hydraulic Enforcers",
        "3. THE VEIL MERCHANTS  : Contraband Resonance Bafflers & Mask Cartels",
        "4. THE MEMORY WASHERS  : Illicit Mnemonic Scrubbers & Grief Crystallizers",
        "5. THE DEBT CONCOURSE  : Shadow Usury Lords, Bailiffs, & Lien Enforcers"
    ])
    content.append(b0)
    
    content.append("""---

## I. Executive Overview & The Extralegal Realpolitik of The Raw

In the sovereign metropolitan hierarchy of Somnarak, civic life is cleanly bifurcated by the reach of the Great Acoustic Veil. Above and within the Veil's resonant dome lie the Sanctioned Quarters: paved basalt boulevards, Directorate research spires, registered merchant bazaars, and residential blocks where citizens pay their monthly Veil-Tax in crystallized Echoes to sleep shielded from planetary sorrow.

Beneath the paved flagstones and beyond the drainage flues lies **The Raw** (날것 — *Nalgeot*).

The Raw encompasses the vast, unpaved labyrinth of decommissioned dredging flues, abandoned basalt quarries, sub-strata aqueducts, and makeshift tenement warrens extending between depth markers -800 meters and -3,200 meters. Within this forgotten expanse, municipal authority does not merely waver—it ceases to exist. The Council of Sighs lacks the administrative manpower to govern subterranean squalor; the Reverie Directorate restricts its subterranean sorties strictly to Sorrow Entity containment and Facility 01 perimeter defense; and the Collector's Bureau refuses to send lone assessors into shafts where tax collectors routinely vanish into the dark.

Into this governance vacuum have stepped **The Five Syndicates of The Raw** (심층의 다섯 범죄 조직 — *Simcheung-ui Daseot Beomjoe Jojik*).

Rather than being mindless criminal gangs, these syndicates represent an extralegal parallel civilization. They collect their own tariffs, maintain their own armed security militias, broker disputes, extract raw subterranean wealth, and enforce ruthless behavioral codes. To the sovereign wings above, they are an illegal blight; yet to the millions who dwell beneath the Veil, the Five Syndicates provide the only functional infrastructure, economic opportunity, and violent protection available.

""")

    # Overview Matrix Box
    b1 = wrap_box("THE FIVE SYNDICATES OF THE RAW — SUMMARY MATRIX", [
        "SYNDICATE NAME   | TERRITORY        | CORE MONOPOLY     | THREAT TIER",
        "-----------------+------------------+-------------------+------------",
        "Menders Guild    | Needle Warrens   | Repair & Husks    | Moderate",
        "Rust Frays       | The Rust Sump    | Basalt Scavenging | Extreme",
        "Veil Merchants   | The Mask Market  | Smuggled Baffles  | Severe",
        "Memory Washers   | The Blank Stacks | Mnemonic Eradication| Extreme",
        "Debt Concourse   | Concourse Vaults | Usury & Liens     | Sovereign"
    ])
    content.append(b1)

    content.append("""---

## II. Syndicate 1: The Menders Guild (수선단 — Suseondan)
### *The Needle-Carriers of the Broken Seams*

> *"The Wardens guard the Veil. The Directorate guards their research. Nobody guards the tenement walls when the mortar turns to weeping dust. That is why we charge our needles."*  
> — Senior Mender Jo Min-Hyuk, Needle Warrens Sector 4

### 1. Sociological Profile & Ideological Doctrine
The **Menders Guild** constitutes the oldest and most organized extralegal network in Somnarak. Unlike their purely criminal counterparts, the Menders view themselves as an honorable civic guild of frontline fixers, civil engineers, and minor containment specialists who operate where municipal services refuse to tread.

When sorrow seepages cause tenement masonry to crack, when low-grade Sorrow Entities (Rank I Whispers or Rank II Murmurs) slip through drainage conduits, or when blood-feuds between tenement families threaten to burn down entire wards, the Raw does not call the Directorate. They hire a Mender.

### 2. Organizational Hierarchy & Ranks
The Guild operates a rigid seven-tier ranking ladder, strictly audited by the Guild Council of Needles:

| Rank | In-Universe Title | Functional Role & Responsibilities | Common Contracting Tier |
|:---:|:---|:---|:---|
| **Rank 7** | **Novice (초심자)** | Basic Han-sensing, masonry caulking, suture packing | Tenement residents, street stalls |
| **Rank 6** | **Journeyman (숙련공)** | Minor entity trapping, basalt brace forging, escort work | Neighborhood elders, grease shops |
| **Rank 5** | **Adept (수선사)** | Rank II entity suppression, structural fracture stabilization | District markets, merchant caravans |
| **Rank 4** | **Veteran (정예사)** | Resonance baffle repair, combat containment, raid leaders | Workshop syndicates, mining clans |
| **Rank 3** | **Expert (거장)** | Advanced Han architecture, Rank III entity neutralizations | Wealthy underworld trusts |
| **Rank 2** | **Master (수선명장)** | Facility breach support, tactical field command | High Council black contracts |
| **Rank 1** | **Grandmaster (대수선사)**| Living legends of the Raw; near-Architect level shaping | Macro-crisis underworld mediation |

### 3. The Mythical Marks
Standing above the numerical ranks are the **Marks** (표식 — *Pyosik*)—legendary independent operators whose renown transcends the Guild itself:
- **The Grey Veil (회색 장막)**: An enigmatic Grandmaster whose custom resonance cloak completely suppresses environmental grief within a 50-meter radius. They operate alone, appearing without notice to stabilize cataclysmic tenement collapses before vanishing.
- **The Crimson Thread (진홍의 실)**: A fallen legend who fell while solo-binding a Rank V Sovereign. Their customized M.A.W. weapon—a spool of monomolecular crimson wire—remains actively humming in the subterranean deep, unbonded and lethal to all who approach.
- **The Iron Needle (강철 침)**: The sitting Guild Chief, an eighty-year-old veteran who enforces the Guild's neutrality with absolute violence, wielding a two-meter Grade 4 Yeoul pneumatic harpoon.

### 4. Operational Modus & Equipment
Menders favor precision over brute force. Their workshops forge specialized **Resonance Needles**—hollow steel and basalt spikes capable of injecting rapid-curing Han sealants into cracked walls or anchoring entity appendages to the stone floor. They commonly commission armor from **Cheol-Gyeong Workshop** (Grade 2–3 Mirror Carapaces) paired with **Yeoul Workshop** rapid-deployment harpoons.

""")

    b_mender = wrap_box("MENDERS GUILD COMBAT DOCTRINE & PROFILE", [
        "COMBAT ROLE     : Vanguard Control, Field Suture, Kinetic Binding",
        "SPEED BAND      : [3 to 6] (High agility, tactical re-positioning)",
        "ACTION POINTS   : 2 Action Slots per Battle Turn",
        "FAVORED GEAR    : Yeoul Pneumatic Needles (Gr 3), Cheol-Gyeong Mail",
        "SIGNATURE MOVE  : 'Seven Seam Suture' (Pins target node, restores allied Posture)",
        "AFFLICTION CAUSE: 'Suture Bind' (Target Speed reduced by -2 on Node 1-5)",
        "VULNERABILITY   : Low raw blunt armor; overwhelmed by high kinetic mass"
    ])
    content.append(b_mender)

    content.append("""---

## III. Syndicate 2: The Rust Frays (녹슨 올 — Nokseun Ol)
### *The Basalt Breakers & Sump Dredgers*

> *"The high-born up top call us trash. But when their sewage clogs and their slag lines burst, they pay our weight in echoes to crawl down the pipes. We don't weave the fabric. We tear it down for iron."*  
> — Iron-Foreman Baek "Cinder-Grip", The Lower Dredge Sump

### 1. Sociological Profile & Ideological Doctrine
The **Rust Frays** are the industrial muscle and heavy shock troops of the subterranean underworld. Formed over two centuries from discarded basalt quarrymen, decommissioned boiler crews, and sewer-dredging convicts, the Rust Frays despise the delicate pretensions of Veil society.

They dwell within **The Rust Sump**—a massive, sulfurous basin at depth -2,400 meters where the industrial runoff, scrap metal, and slag of the Zone D manufactories collect. In this searing, toxic environment, the Rust Frays have built an iron kingdom sustained by illicit salvage, illegal smelting, and violent racketeering.

### 2. Augmentations & The Iron Flesh
Unlike the sovereign citizenry who fear physical mutilation, Rust Fray enforcers practice aggressive, crude mechanical and basalt augmentation:
- **Vitrified Basalt Grafts**: Severed limbs replaced with solid basalt cylinders driven by scavenged pneumatic pistons.
- **Sulfur Respirators**: Heavy cast-iron snout masks bolted directly into facial bone to filter subterranean gas.
- **Boiler Carapaces**: Welded industrial plates stripped from ancient dredging barges, offering extreme resistance to kinetic and Void trauma at the cost of crippling mobility penalties.

### 3. Organizational Structure
The syndicate is organized like a militant industrial collective:
- **Rust-Pounders (녹슨 타격수)**: The frontline foot soldiers, wielding two-handed iron sledges and heavy scavenged crowbars.
- **Scrap-Breakers (잔해 파쇄병)**: Heavily armored shock troopers carrying pneumatic demolition lances and high-temperature sulfur cutting torches.
- **Iron-Foremen (강철 십장)**: Brutal cadre commanders who direct salvage operations and lead turf wars against rival syndicates.
- **High Overseer Baek "Cinder-Grip"**: A colossal former foundry master whose entire right upper torso has been replaced with a twin-cylinder steam-driven basalt crusher.

""")

    b_rust = wrap_box("RUST FRAYS TACTICAL PROFILE & BATTLE ENGINE STATS", [
        "COMBAT ROLE     : Heavy Juggernaut, Armor Shredding, Area Demolition",
        "SPEED BAND      : [1 to 4] (Low agility, immovable frontline presence)",
        "ACTION POINTS   : 1 to 2 Action Slots per Battle Turn",
        "FAVORED GEAR    : Hwa-Seok Thermal Lances (Gr 3), Scavenged Crusher Plates",
        "SIGNATURE MOVE  : 'Pneumatic Quake' (Blunt strike causing ground rupture)",
        "AFFLICTION CAUSE: 'Oxidized Rust' (Reduces target Resilience by -25% per stack)",
        "VULNERABILITY   : Vulnerable to high-speed piercing and psychic grief attacks"
    ])
    content.append(b_rust)

    content.append("""---

## IV. Syndicate 3: The Veil Merchants (장막 상인회 — Jangmak Sanginhoe)
### *The Mask Smugglers & Resonance Bafflers*

> *"The Council tells you the Veil is a divine gift. We tell you the Veil is a pipe. And like any pipe, if you know where to tap it, the water runs free."*  
> — Factor Jin, The Whisper Bazaar of Zone C

### 1. Sociological Profile & Contraband Monopolies
The **Veil Merchants** are the undisputed masters of subterranean black-market commerce, counterfeiting, and contraband logistics. While the Rust Frays control heavy muscle and the Menders provide maintenance, the Veil Merchants control the flow of survival goods.

Their empire is built on three illicit monopolies:
1. **Counterfeit Veil Masks & Visors**: Replicas of civic Veil filters that allow unregistered wanderers to breathe safely within sorrow-heavy zones without paying municipal Veil taxes.
2. **Bootleg Resonance Baffles**: Stripped-down acoustic dampening runes—often stolen or reverse-engineered from **Chim-Mok Workshop** designs—that mute the emotional resonance of illegal operations to prevent detection by Reverie Directorate sensors.
3. **Forged Citizenship Seals & Travel Warrants**: Masterfully forged brass engrams that permit underworld bosses and fugitives to pass through Directorate checkpoints into the Sanctioned Quarters.

### 2. Operational Stronghold: The Mask Market
The epicenter of their power is **The Mask Market** (가면 시장 — *Gamyeon Sijang*), located in the sprawling limestone caverns of Zone C. In this subterranean trade hub, illuminated entirely by pale violet quartz lamps, hundreds of stalls buy and sell every prohibited commodity in Somnarak: bootleg Han-canisters, unlicensed weapons, stolen entity materials, and counterfeit identification tokens.

### 3. Smuggling Corridors & The Shadow Flues
The syndicate maintains an exhaustive private map of every drainage flue, abandoned ventilation shaft, and subterranean aqueduct connecting the lower depths to the upper municipal spires. Their runners, known as **Shroud Couriers**, can transport contraband from the depths of the Raw to the doorstep of a Council noble's estate within four hours.

""")

    b_veil = wrap_box("VEIL MERCHANTS COMBAT PROFILE & GRID ATTRIBUTES", [
        "COMBAT ROLE     : Skirmisher, Acoustic Mirage, Ranged Saboteur",
        "SPEED BAND      : [4 to 8] (Extremely high mobility, evasive positioning)",
        "ACTION POINTS   : 2 to 3 Action Slots per Battle Turn",
        "FAVORED GEAR    : Baek-Gwang Prism Darts (Gr 3), Chim-Mok Stilettos (Gr 4)",
        "SIGNATURE MOVE  : 'Acoustic Blindfold' (Disrupts target perception on Node 1-10)",
        "AFFLICTION CAUSE: 'Resonance Mirage' (Target clash rolls suffer -3 coin power)",
        "VULNERABILITY   : Extremely low health pool; folds instantly to heavy blunt hits"
    ])
    content.append(b_veil)

    content.append("""---

## V. Syndicate 4: The Memory Washers (기억 세탁단 — Gieok Setakdan)
### *The Mnemonic Scrubbers & Grief Crystallizers*

> *"Bring us your guilt, your debts, your murders, your beloved daughter's dying scream. Leave them in our basin. Tomorrow you will wake up with an empty ledger, an empty chest, and no tears left to weep."*  
> — Chief Washer Kyeong, The Blank Stacks of Zone B

### 1. Sociological Profile & Illicit Mnemonic Extraction
The **Memory Washers** represent the most dreaded and psychologically terrifying cartel in the subterranean depths. Born from rogue mnemonic technicians, disgraced scholars exiled from **The Memory Archive (Gieok Jeojangso)**, and renegade psychiatric alchemists, the Memory Washers traffic in the most volatile commodity in Somnarak: human remembrance.

In a metropolis powered by emotional sorrow, memories are not mere subjective thoughts—they are physically quantifiable energy repositories. The Memory Washers exploit this reality through two ruthless commercial pipelines:
- **Voluntary & Coerced Scrubbing**: Desperate debtors, hunted criminals, and grief-shattered survivors pay the syndicate to surgically excise memories of trauma, criminal culpability, or crippling emotional agony.
- **Trauma Crystallization**: The excised memories are not destroyed; they are boiled, distilled, and crystallized into high-grade "Grief Fuel" and synthetic engrams, which are then sold on the black market to fuel illegal weapons, black-market workshops, and illicit resonance furnaces.

### 2. The Horror of The Blank Husks
Those who cannot pay their debts to the syndicate undergo **Total Amnesiac Scrubbing** (완전 기억 말소 — *Wanjeon Gieok Malso*). Their personalities, names, skills, and personal histories are completely erased, reducing them to pliable, emotionless automatons known as **Blank Husks** (백색 껍데기 — *Baeksaek Kkeopdegi*).

The syndicate equips these husks with cheap basalt cudgels and chemical injectors, using them as disposable meat-shield enforcers who feel no fear, no physical pain, and no psychological distress during battle.

### 3. The Blank Stacks
Operating within subterranean vaults reinforced with acoustic lead plates, **The Blank Stacks** serve as the syndicate's clinical processing centers. Thousands of glass ampoules containing glowing cyan, violet, and deep crimson fluid line the walls—each vial holding the stolen or sold life memories of a Somnarak citizen.

""")

    b_memory = wrap_box("MEMORY WASHERS TACTICAL PROFILE & MNEMONIC WARFARE", [
        "COMBAT ROLE     : Mnemonic Saboteur, Sanity Eraser, Coherence Drainer",
        "SPEED BAND      : [2 to 6] (Controlled, methodical pacing)",
        "ACTION POINTS   : 2 Action Slots per Battle Turn",
        "FAVORED GEAR    : Yeoul Neural Harpoons (Gr 3), Mnemonic Siphon Vials",
        "SIGNATURE MOVE  : 'Retrograde Scrub' (Attacks opponent's Action Queue)",
        "AFFLICTION CAUSE: 'Amnesiac Void' (Drains 15 Clarity & locks 1 Skill Slot)",
        "VULNERABILITY   : Highly susceptible to emotional overload and pure Han bursts"
    ])
    content.append(b_memory)

    content.append("""---

## VI. Syndicate 5: The Debt Concourse (채무 공회 — Chaemu Gonghoe)
### *The Shadow Usury Lords & Mort-Gage Bailiffs*

> *"The Collector's Bureau above wears white coats and carries golden calipers. Down here, our scales are cast from raw basalt, and our ink is mixed with marrow. You signed the bond. Your great-grandson will pay it."*  
> — High Bailiff Ma, The High Concourse Vaults

### 1. Sociological Profile & The Shadow Banking Network
The **Debt Concourse** is the absolute apex of underworld power, operating as the black-market central bank and sovereign usury authority of the subterranean deep. While the municipal Collector's Bureau operates under legal mandates and civic regulations, the Debt Concourse operates under the unyielding law of the predatory contract.

The Concourse was founded by corrupt former Collector assessors, rogue ledger-clerks, and ruthless merchant princes who realized that in Somnarak, physical violence is temporary, but emotional debt is eternal. They issue loans in crystallized Echoes to desperate citizens, failing workshops, and rival gangs at astronomical interest rates, secured by contracts that pledge the borrower's life, organs, family lineage, and soul-resonance as collateral.

### 2. The Living Mort-Gage & Ancestral Liens
The Concourse's legal instruments are terrifying in their thoroughness:
- **The Living Mort-Gage (생체 담보 채권)**: A contract granting the Concourse full ownership of the borrower's physical body. If payment lapses by one second, Concourse Bailiffs possess the legal authority under underworld treaty to harvest organs or auction the borrower to the Memory Washers.
- **The Ancestral Han Lien (혈통 한 저당권)**: A generational debt bond that automatically transfers unpaid interest to the borrower's children and grandchildren, legally binding an entire family lineage into perpetual servitude.

### 3. The Enforcement Arm: Concourse Bailiffs
The Concourse maintains the best-equipped private army in the Raw. Their **Lien-Executioners** and **Concourse Bailiffs** wear heavy basalt armor reinforced with **Cheol-Gyeong Workshop** mirrors, brandishing massive weighted chain-flails and enchanted ledger-brands that sear glowing debt-runes directly into the skin of defaulters.

""")

    b_debt = wrap_box("DEBT CONCOURSE COMBAT PROFILE & FINANCIAL EXECUTION", [
        "COMBAT ROLE     : Heavy Controller, Stat Siphoner, Action Locking",
        "SPEED BAND      : [3 to 7] (Dominant tempo, relentless advance)",
        "ACTION POINTS   : 2 to 3 Action Slots per Battle Turn",
        "FAVORED GEAR    : Cheol-Gyeong Heavy Shields (Gr 4), Basalt Weighted Chains",
        "SIGNATURE MOVE  : 'Foreclosure Seal' (Binds opponent in heavy debt manacles)",
        "AFFLICTION CAUSE: 'Crushing Indenture' (Siphons 20% of target damage as Posture)",
        "VULNERABILITY   : Slow windup animations; vulnerable to rapid multi-hit rushes"
    ])
    content.append(b_debt)

    content.append("""---

## VII. Inter-Syndicate Geopolitics & The Treaty of Broken Needles

The subterranean underworld of Somnarak is not in a state of perpetual chaos; rather, it is governed by a strict, fragile peace established in Year 4,190 known as **The Treaty of Broken Needles** (부러진 침의 조약 — *Bureojin Chim-ui Joyak*).

Brokered by the legendary Grandmasters of the Menders Guild and ratified by the chiefs of all five syndicates, this underworld concordat established the definitive boundaries of territory, trade, and violence across the subterranean depths.

### 1. Territorial Boundaries of The Raw

| Syndicate | Sovereign Underworld Sector | Depth Range | Permitted Commercial Monopoly |
|:---|:---|:---:|:---|
| **The Menders Guild** | The Needle Warrens & East Flues | -800m to -1,600m | Structural repair, civilian husk trapping, neutral mediation |
| **The Rust Frays** | The Rust Sump & Slag Dredges | -2,000m to -2,800m | Heavy salvage, illegal metallurgy, boiler repair, demolition |
| **The Veil Merchants** | The Mask Market & Whisper Bazaars | -1,200m to -2,200m | Contraband resonance gear, counterfeit visors, smuggling routes |
| **The Memory Washers** | The Blank Stacks & Deep Cisterns | -1,800m to -2,600m | Memory scrubbing, trauma fuel distilling, husk manufacturing |
| **The Debt Concourse** | The High Vaults of Sorrow | -1,000m to -2,000m | Shadow banking, loan underwriting, asset auctions, bailiff raids |

### 2. The Three Underworld Taboos
Under the Treaty of Broken Needles, any syndicate or rogue operative who violates the Three Underworld Taboos is marked for joint extermination by the remaining four syndicates:

1. **Taboo of the Great Veil Anchor (대장막 닻 훼손 금지)**: No syndicate may tamper with or sabotage the primary acoustic grounding pylons that anchor the Great Veil of Somnarak. If the Veil above collapses, the resulting Sorrow Flood will drown the Raw first.
2. **Taboo of Facility 01 Perimeter (제1시설 경계 침범 금지)**: No syndicate personnel may enter or conduct operations within 500 meters of the Reverie Directorate's Facility 01 perimeter fence. A single clash with Directorate enforcers invites orbital kinetic strikes into the subterranean warrens.
3. **Taboo of Scribe Execution (기록관 살해 금지)**: Underworld disputes may result in bloodshed, but unarmed neutral scribes, Guild arbitrators, and designated envoys carrying the white-and-iron needle banner are granted absolute diplomatic immunity.

""")

    b_geo = wrap_box("INTER-SYNDICATE RELATIONSHIP DIPLOMATIC MATRIX", [
        "SYNDICATE       | MENDERS   | RUST FRAYS| VEIL MERCH| MEMORY W. | DEBT CONC.",
        "----------------+-----------+-----------+-----------+-----------+-----------",
        "Menders Guild   | ALLIED    | TENSE WAR | COLD TRADE| HOSTILE   | CAUTIOUS  ",
        "Rust Frays      | TENSE WAR | ALLIED    | BULK BUYER| NEUTRAL   | HEAVY DEBT",
        "Veil Merchants  | COLD TRADE| BULK TRADE| ALLIED    | HIGH BUYER| BROKERAGE ",
        "Memory Washers  | HOSTILE   | NEUTRAL   | CLIENT    | ALLIED    | BODY SUPPL",
        "Debt Concourse  | CAUTIOUS  | ENFORCING | PARTNER   | MAJOR BUY | ALLIED    "
    ])
    content.append(b_geo)

    content.append("""---

## VIII. Syndicate Armament Supply & The Six Workshops Integration

While the sovereign military and the Reverie Directorate maintain exclusive extraction monopolies over high-grade M.A.W. armaments, the Five Syndicates arm their elite cadres through deep, covert partnerships with **The Six Great Basalt & Resonance Workshops** (see `SOMNARAK_WORKSHOPS.md`).

Under the strict **Workplace Law of Somnarak**, Grade 4 and Grade 5 artisan weapons can only be commissioned by operatives holding official employment tenure. The Five Syndicates bypass this municipal restriction through elaborate paper corporations, shadow guild registries, and front mining enterprises registered in Zone D.

### 1. Syndicate Armament Procurement Pipeline

| Syndicate | Primary Supplying Workshop | Favored Equipment Grade | Tactical Purpose in Underworld Clashes |
|:---|:---|:---:|:---|
| **Menders Guild** | **Yeoul Workshop** & **Cheol-Gyeong** | Grade 2–3 (Superior) | High-speed pneumatic harpoons for binding beasts; mirror carapaces for shielding civilians |
| **Rust Frays** | **Hwa-Seok Workshop** | Grade 3–4 (Masterwork) | Vitrified sulfur torches, slag crushers, and superheated basalt demolition picks |
| **Veil Merchants** | **Chim-Mok Workshop** & **Baek-Gwang** | Grade 3–4 (Masterwork) | Acoustic suppression cloaks and quartz prism darts for silent smuggling and escape |
| **Memory Washers** | **Yeoul Workshop** (Specialized) | Grade 3–4 (Masterwork) | Micro-needle pneumatic projectors for neural disruption and spinal fluid extraction |
| **Debt Concourse** | **Cheol-Gyeong** & **Sim-Yeon** | Grade 4–5 (Legendary) | Basalt tower shields and abyssal lead-weighted chain-whips for crushing defaulters |

### 2. The Hunt for Grade 5 Legendary Relics
In the subterranean black markets, an authentic Grade 5 Legendary workshop weapon—such as Master Wright Gwan's fabled *Pneumatic Piercer 'Flash-Flood'* or an ancient *Vitrified Basalt Aegis*—is worth more than an entire tenement district. Because the crafting probability of a Grade 5 armament is strictly fixed at **0.5%**, syndicates wage brutal covert wars to assassinate lone sovereign contractors and strip their bodies of legendary workshop weapons.

""")

    b_clash = wrap_box("UNDERWORLD SYNDICATE 10-NODE COMBAT ENCOUNTER SCENARIO", [
        "ENCOUNTER CODE  : COMBAT-SIM-UNDERWORLD-RAW-001",
        "THEATER LOCATION: Depth -1,850m (The Mask Market Abandoned Siphon Canal)",
        "ENGAGEMENT TYPE : Subterranean Turf Enforcement Clash",
        "---",
        "STAGE NODES 01 TO 10 (DISCRETE SPATIAL ENGAGEMENT GRID):",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]    ",
        "[OPERATIVE SQUAD]           [NO MAN'S LAND]          [SYNDICATE STRIKE]",
        "  [N01] Giltong Vanguard    [N04] Neutral Flue       [N08] Rust Pounder",
        "  [N02] Su-Ho Warden        [N05] Broken Pylon       [N09] Memory Washer",
        "  [N03] Tam-Sa Scribe       [N06] Slag Drainage      [N10] Concourse Bailiff",
        "---",
        "TACTICAL CADENCE & PHASE RESOLUTION RULES:",
        "- 6 Battle Turns constitute 1 Combat Phase macro-cycle.",
        "- End of Turn 6: 'Subterranean Slag Venting' environmental hazard.",
        "- Nodes 04-07 flooded with boiling sulfur sludge; 30 burn damage to occupants."
    ])
    content.append(b_clash)

    content.append("""---

## IX. Tactical Profiles & Combat Mechanics on the 10-Node Grid

When contractors, Directorate expeditionaries, or rival gangs encounter underworld syndicate strike teams, combat resolves across the standardized **10-Node Spatial Grid Engine** (see `SOMNARAK_BATTLE_SYSTEM.md`).

Each syndicate deploys distinct tactical archetypes with unique speed thresholds, range preferences, action slot allocations, and status afflictions.

### 1. Syndicate Archetype Battle Specifications

```text
+=====================================================================+
|               SYNDICATE UNIT BATTLE ATTRIBUTE MATRIX                |
+---------------------------------------------------------------------+
| UNIT DESIGNATION   | HP / POSTURE | SPEED | AP | FAVORITE NODES     |
+--------------------+--------------+-------+----+--------------------+
| Mender Veteran     | 1,250 / 220  |  3-6  |  2 | Nodes 03 to 06     |
| Rust Scrap-Breaker | 1,850 / 380  |  1-4  |  1 | Nodes 05 to 08     |
| Veil Shadow-Runner |   920 / 160  |  4-8  |  3 | Nodes 01 to 04     |
| Memory Scrubber    | 1,100 / 190  |  2-5  |  2 | Nodes 06 to 09     |
| Concourse Bailiff  | 2,100 / 420  |  3-7  |  2 | Nodes 04 to 07     |
+=====================================================================+
```

### 2. Underworld Status Afflictions

The syndicates utilize specialized chemical, acoustic, and psychological status effects that mirror their underworld trade:

1. **Oxidized Rust (산화 녹 — Sanhwa Nok)**:
   - *Source*: Rust Fray pneumatic sledges and sulfur cutters.
   - *Mechanic*: Inflicts 1 stack on clash loss. Each stack reduces target Resilience by 5% and clashing power by 1. At 5 stacks, the target's weapon suffers "Corrosion Jamming," locking their highest-cost skill for 1 turn.

2. **Acoustic Blindfold (음향 암전 — Eumhyang Amjeon)**:
   - *Source*: Veil Merchant acoustic baffles and prism darts.
   - *Mechanic*: Target cannot target units beyond adjacent nodes (Range Band restricted to 1). Clash coin flip results are obscured, and evasive skills gain +4 power.

3. **Amnesiac Void (기억 공백 — Gieok Gongbaek)**:
   - *Source*: Memory Washer neural siphons.
   - *Mechanic*: Depletes 15 Clarity immediately. Upon reaching 0 Clarity, target enters "Mnemonic Panic," randomly targeting allies or skipping their action slot during the subsequent Battle Turn.

4. **Foreclosure Lien (차압 유치권 — Chaap Yuchigwon)**:
   - *Source*: Debt Concourse chain-flails and ledger brands.
   - *Mechanic*: Afflicts target with a legalistic curse. Whenever the target suffers damage, 25% of that damage is converted into temporary Posture shields for the Concourse Bailiff. If the target is staggered while under Lien, they surrender 1 Action Slot to the Bailiff on the following turn.

---

## X. Municipal Response & Sovereign Strategic Recommendations

```text
+=====================================================================+
|       SOVEREIGN STRATEGIC DIRECTIVE: UNDERWORLD INTERVENTION        |
+---------------------------------------------------------------------+
| DIRECTIVE ID  : DIR-SEC-RAW-PACIFICATION-4238                       |
| ISSUING BODY  : Reverie Directorate Subterranean Security Bureau    |
| CLEARANCE     : RANK-IV CONTRACTORS, COMMANDERS, & FIELD SCRIBES   |
+---------------------------------------------------------------------+
| OPERATIONAL MANDATES:                                               |
| 1. MAINTAIN CONTAINMENT: Do not initiate total eradication campaigns|
|    against the Five Syndicates. The Raw absorbs 40% of the city's   |
|    ambient sorrow seepage. Total destruction of the syndicates will |
|    trigger an immediate municipal sorrow flood into Sanctioned      |
|    Quarters.                                                        |
| 2. ENFORCE THE THREE TABOOS: Any syndicate observed touching the   |
|    Great Veil Anchors or approaching Facility 01 is to be subjected |
|    to immediate surgical liquidation via Grade-γ M.A.W. strike teams|
| 3. EXPLOIT INTER-SYNDICATE RIVALRY: Subsidize the Menders Guild with|
|    low-grade Han supplies to check the expansion of the Debt        |
|    Concourse and the violent territorial incursions of Rust Frays.  |
+=====================================================================+
```

### Concluding Archival Summary
The Five Syndicates of The Raw represent neither an anomaly nor a temporary criminal insurrection; they are the natural, unyielding institutional shadow of Somnarak itself. As long as the sovereign spires above demand that citizens pay for their sanctuary in tears and Echoes, the abandoned millions below will continue to forge their own laws from rusted basalt, black-market baffles, stolen memories, and predatory bonds.

---
*End of Master Municipal Underworld Codex CODEX-DEM-UNDERWORLD-SYNDICATES-001.*
""")
    
    return "".join(content)

if __name__ == "__main__":
    codex_text = build_codex()
    target_path = "SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_UNDERWORLD_SYNDICATES.md"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(codex_text)
    print(f"Successfully wrote {len(codex_text)} bytes to {target_path}")
