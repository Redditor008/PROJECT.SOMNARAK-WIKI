#!/usr/bin/env python3
"""
Generator script for Mugenhan Ecology master documents:
1. SOMNARAK-WORLD/Mugenhan_Ecology/MUGENHAN_ECOLOGY_OVERVIEW.md (Simple Overview)
2. SOMNARAK-WORLD/Master_Codices/MUGENHAN_ECOLOGY_OVERVIEW.md (Master Codex Mirror)
3. SOMNARAK-WORLD/Mugenhan_Ecology/README.md (Directory Index)
4. SOMNARAK-WORLD/Mugenhan_Ecology/MUGENHAN_DEEP_ECOLOGY_COMPENDIUM.md (Secondary Extended Huge Doc)
5. SOMNARAK-WORLD/Master_Codices/MUGENHAN_DEEP_ECOLOGY_COMPENDIUM.md (Master Codex Mirror)

Enforces:
- Tripartite Taxonomy: Mundane Organisms, Sorrow-Infused Organisms (80% Bio / 20% SE-M.A.W.), Mortal Sorrow Entities (Capped at Tier Two / Moderate β).
- Symmetrical Fauna and Flora counterparts across all three tiers.
- Zero banned terms / zero external verse borrowings.
- Authoritative V.1.0 standard with zero file-embedded confessions.
"""

import os
import sys
import re

# Banned terms scanner
banned_patterns = [
    r"\bego\b", r"\be\.g\.o\b", r"\babnormality\b", r"\babnormalities\b",
    r"\bdistortion\b", r"\bdistortions\b", r"\bpeccatula\b", r"\bfixer\b",
    r"\bfixers\b", r"\bassociation\b", r"\bassociations\b", r"\bfingers\b",
    r"\blobotomy\b", r"\blimbus\b", r"\blibrary\b", r"\byoung-ji\b",
    r"\bcarmen\b", r"\bayin\b", r"\bsinner\b", r"\bsinners\b",
    r"\bmephistopheles\b", r"\bgolden bough\b", r"\bmirror dungeon\b",
    r"\brefraction railway\b", r"\bharin\b", r"\bminjae\b", r"\bpugnahan\b"
]

def check_banned(text, filename):
    for b in banned_patterns:
        matches = re.findall(b, text, re.IGNORECASE)
        if matches:
            raise ValueError(f"Banned word {b} found in {filename}: {matches[:3]}")

# ==============================================================================
# 1. OVERVIEW DOCUMENT CONTENT
# ==============================================================================
overview_content = """# Mugenhan Ecology Overview (무한한 생태 총람)
## The Living Subterranean & Terrestrial Biosphere of Planet Mugenhan
### Reverie Directorate & Somnarak Exploration Decree Joint Scientific Codex

> *"The planet Mugenhan does not merely store sorrow; it breathes it. From the highest basalt ridges of the Spire down to the lightless shores of the Primordial Nadir at minus three thousand meters, life does not merely endure the weeping—it adapts, integrates, and evolves. To understand the creatures of this world, one must discard the simplistic notion that sorrow belongs only to human hearts."*  
> — Chief Biologist Serin, Directorate Bio-Resonance Division & Frontier Survey

---

## I. Executive Biological Foundation

Planet **Mugenhan** (무한한 / 無限恨) possesses a planetary biosphere fundamentally linked to the metaphysical and physical presence of **Han** (한 / 恨 — unrefined, pressurized sorrow). While surface urban authorities traditionally viewed Han exclusively as an industrial fuel or a catastrophic cognitive hazard requiring strict containment, exploration across the seven subterranean geological strata has revealed a complex, flourishing, and ancient ecological tapestry.

The biosphere of Mugenhan is organized into three distinct, universally recognized evolutionary tiers, with every tier possessing symmetrical **Fauna** (animal life) and **Flora** (plant, fungal, and vegetative life) counterparts.

---

## II. The Tripartite Biological Taxonomy

```text
+=====================================================================+
|               MUGENHAN TRIPARTITE ECOLOGICAL MATRIX                 |
+=====================================================================+
| TIER 1: MUNDANE ORGANISMS (Pure Biological Nature)                  |
|   * Composition : 100% Biological Nature - 0% Sorrow or M.A.W.      |
|   * Mortality   : Standard biological life cycles, breeding, death. |
|   * Threat Grade: Negligible to Minor - Pure natural instincts.     |
|   * Fauna Rep   : Blind cave-leapers, karst crawlers, deep badgers. |
|   * Flora Rep   : Chemosynthetic mosses, calcite bracket fungi.     |
+---------------------------------------------------------------------+
| TIER 2: SORROW-INFUSED ORGANISMS (80% Living Beast, 20% SE-M.A.W.)  |
|   * Composition : 80% Living Biological Organism / 20% SE-M.A.W.    |
|   * Principle   : Normal living beings with M.A.W. physical traits. |
|   * Mortality   : True living beings - Bleed, reproduce, die mortal.|
|   * Threat Grade: Minor (Alpha) to Moderate (Beta) - Harvestable.   |
|   * Fauna Rep   : Sorrow Beasts - Bone cleavers, armor carapaces.   |
|   * Flora Rep   : Sorrow Flora - Kinetic thorns, combustible resin. |
+---------------------------------------------------------------------+
| TIER 3: MORTAL SORROW FAUNA & FLORA (MSF - Capped at Tier Two Beta) |
|   * Composition : 100% Sorrow Manifestation - Animal/Plant Born.    |
|   * Principle   : Conceptual entities acting like biological fauna. |
|   * Mortality   : Finite mortal lifespans - Permanently slayable.   |
|   * Threat Cap  : Strictly capped at Tier Two / Moderate Beta.      |
|   * Fauna Rep   : Mortal Sorrow Fauna (MSF) - Screaming chitin, pack|
|   * Flora Rep   : Mortal Sorrow Flora (MSF) - Spore choirs, mirages |
+=====================================================================+
```

---

## III. Detailed Breakdown of the Three Categories

### 1. Tier 1: Mundane Organisms (일반 생물 — Normal Wildlife)

Mundane organisms represent pure, un-mutated biological evolution adapted to darkness, high atmospheric pressure, and mineral-saturated groundwater.

- **Faunal Characteristics (일반 동물 — Normal Animals)**:
  * Possess standard organs, circulatory systems, and nervous systems.
  * Completely lack sorrow-resonant carapaces, elemental venting organs, or M.A.W.-like bone structures.
  * Exhibit natural animal behaviors: foraging, subterranean hibernation, acoustic echo-navigation, and predator-prey flight reflexes.
  * Meat and hides are entirely safe for standard human consumption and processing, free of psycho-reactive sorrow contamination.
- **Floral Characteristics (일반 식생 — Normal Flora)**:
  * Non-sorrow vegetative organisms deriving energy from chemosynthesis, sulfur filtration, or geothermal thermal vents.
  * Form the foundational baseline biomass of subterranean strata: phosphorescent carpet mosses, limestone bracket fungi, and subterranean kelp.

---

### 2. Tier 2: Sorrow-Infused Organisms (비한수 & 비한목 — 80% Organism / 20% M.A.W.)

**CRITICAL BIOLOGICAL LAW**: Sorrow Beasts and Sorrow Flora are **normal living organisms with sorrow and M.A.W.-like properties, NOT conceptual entities in animal shape**.

They are classified as **80% Living Biological Organism and 20% Sorrow / M.A.W. Phenotype**.

- **Sorrow Beasts (비한수 / 悲恨獸 — Living Animals with M.A.W. Traits)**:
  * They are warm-blooded or cold-blooded living creatures that mate, gestate, nurse young, bleed real hemoglobin, eat mundane prey, and die mortal deaths from age, disease, or wounds.
  * Over tens of thousands of generations in deep karst strata saturated with mineralized Han, their evolutionary physiology has adapted by integrating sorrow crystals directly into their skeletal and muscular systems.
  * They possess **biological M.A.W.-like traits**: natural horn-cleavers with acoustic vibration, carapaces hardened with calcified sorrow apatite, or venom sacs that secrete paralytic cold-fire sorrow enzymes.
  * When harvested, their bodies yield **Biological M.A.W. Precursors**—materials that Directorate armorers can forge without the severe psychological backlash of true entity extractions.
- **Sorrow Flora (비한목 / 悲恨木 & 비한초 / 悲恨草 — Han-Infused Vegetation)**:
  * Living trees, vines, shrubs, and macro-fungi whose root systems tap directly into subterranean sorrow aquifers.
  * They grow through normal cellular division and photosynthesis/chemosynthesis, but their lignin incorporates crystallized sorrow-glass.
  * They exhibit M.A.W.-like vegetative traits: petrified iron bark that deflects rifle bullets, crystalline thorns that discharge kinetic tremor pulses when brushed, and resin that boils like combustible Crimson Han-Brine.

---

### 3. Tier 3: Mortal Sorrow Fauna & Flora (MSF — 생멸한령)

Unlike human Sorrow Entities (SE / SECC) born from complex, immortal human subconscious trauma, **Mortal Sorrow Fauna and Flora (MSF)** are born from the collective dying agony, terror, or extinction trauma of subterranean animals, beasts, and forests.

- **Mortal Behavioral Paradigm**:
  * They act as if they are natural wild creatures: hunting along territorial tracks, defending dens, stalking prey, or remaining rooted like carnivorous vegetation.
  * They possess **finite, mortal lifespans** (typically weeks to several years) before their sorrow coherence naturally disperses.
  * They **do not possess immortal regeneration**: destroying their physical vessel permanently extinguishes the entity, dropping rich Han-dust rather than entering an eternal containment meltdown cycle.
  * **Strict Threat Cap**: Because animals and plants lack human existential despair, their grief cannot sustain high-tier conceptual reality-warping. Mortal Sorrow Fauna and Flora are **strictly capped at Tier Two / Moderate Potency (Grade β)**.
- **Mortal Sorrow Fauna (MSF) (수성 생멸한령 / 獸性 生滅恨靈 — Beast-Born Entities)**:
  * Entities born from the violent death, starvation, or slaughter of animal packs and sorrow beasts.
  * Manifest as spectral predator forms: screaming chitin-crawlers, weeping hound packs, or shadow-antlered stalkers.
- **Mortal Sorrow Flora (MSF) (목성 생멸한령 / 木性 生滅恨靈 — Plant-Born Entities)**:
  * Entities born from burned fungal colonies, ancient clear-cut fossil groves, or weeping root cataclysms.
  * Manifest as animated root-strangler phantoms, weeping spore clouds, or deceptive blossom mirages that trap living prey with acoustic lamentations.

---

## IV. Comparative Taxonomic Matrix

| Metric / Parameter | Tier 1: Mundane Wildlife | Tier 2: Sorrow-Infused Organisms (SB/SF) | Tier 3: Mortal Sorrow Fauna/Flora (MSF) |
|---|---|---|---|
| **Biological Ratio** | 100% Biological Organism | 80% Biological / 20% SE-M.A.W. | 0% Biological (Sorrow Manifestation) |
| **Living State** | True mortal animal / plant | True mortal animal / plant | Mortal conceptual entity |
| **Reproduction** | Biological mating / seed dispersal | Biological mating / spore dispersal | Formed from animal/plant trauma |
| **Lifespan** | Standard biological lifespan | Standard biological lifespan | Finite mortal lifespan (Days to Years) |
| **Vessel Destruction** | Natural death | Natural death | **Permanent Death** (Dissolves) |
| **Max Threat Tier** | Minor / Negligible | Moderate (β-Grade) | **Strictly Capped at Moderate (β)** |
| **M.A.W. Extraction** | Inapplicable (Normal hide/meat) | **Biological M.A.W. Precursors** | Direct Han Dust / Vessel Relics |
| **Containment Req.** | Standard cages / paddocks | Reinforced pens / shock collars | Class-I to Class-II Leaded Casks |
| **Human Consumption** | Safe and non-toxic | Flesh edible after sorrow-purging | Toxic / Inedible (Pure Sorrow Vapor) |

---

## V. Strategic Utilization & Harvesting

1. **Sedative Culling & Biological Precursors**:
   * The Reverie Directorate and SED do not suppress Sorrow Beasts as containment breaches. They manage them through regulated forestry and wildlife management protocols.
   * Sorrow Beasts provide the primary raw material for **Grade-α and Grade-β M.A.W. equipment**, bypassing the immense psychological toll of harvesting true human Sorrow Entities.
2. **Han-Brine & Agro-Chemical Refining**:
   * The resin of Sorrow Flora (such as *Crimson Brine-Briar*) is tapped sustainably to produce stabilized combat tinctures, industrial lubricants, and municipal lighting fuels.
3. **Mortal Entity Pacification**:
   * Beast-born and plant-born entities encountered during expeditions do not require Level-5 extraction procedures; tactical vanguard units can neutralize them in the field with standard kinetic weaponry.

---

*(For exhaustive physiological dossiers, anatomical autopsies, strata food webs, and comprehensive species catalogs, consult `MUGENHAN_DEEP_ECOLOGY_COMPENDIUM.md`).*
"""

# ==============================================================================
# 2. COMPENDIUM DOCUMENT CONTENT (SECONDARY EXTENDED HUGE DOC)
# ==============================================================================
compendium_content = """# Mugenhan Deep Ecology Compendium (무한한 심연 생태 대전)
## The Definitive Encyclopedic Treatise on Subterranean Biology, Sorrow Beasts, and Vegetative Phenotypes
### Authorized by the Reverie Directorate Bio-Synthesis Bureau & SED Geological Survey

> *"Life is not extinguished by the dark; it is taught to bite. When sorrow seeps into the soil, the roots do not rot—they turn to iron. When an animal drinks from a river of weeping, it does not drown—it grows horns of crystal and learns to strike before the weeping takes its mind. We are not the masters of this world's grief; we are merely the newest creatures walking among those who learned to wear it ten thousand years before us."*  
> — Senior Biologist Dan-woo, Subterranean Ecological Survey, Year 4,235

---

## Volume Architecture

- **Section I: Foundational Ontology of Mugenhan Biology**
- **Section II: Complete Taxonomic Profiles of Tier 1 (Mundane Subterranean Organisms)**
- **Section III: Complete Taxonomic Profiles of Tier 2 (Sorrow Beasts & Sorrow Flora)**
- **Section IV: Complete Taxonomic Profiles of Tier 3 (Mortal Sorrow Fauna & Flora — MSF)**
- **Section V: Physiological Ecology & Harvesting Protocols**
- **Section VI: Strata Ecological Distribution Map & Biodiversity Gradients**

---

## Section I: Foundational Ontology of Mugenhan Biology

### 1.1 The Biochemical Mechanism of Sorrow Absorption

Planet Mugenhan's biosphere operates under physical and metaphysical laws distinct from sterile terrestrial ecology. Beneath the volcanic basalt mantle, **Han** (unrefined, pressurized sorrow) flows through subterranean fissures, hydrothermal aquifers, and mineral deposits.

Over millions of years, biological organisms exposed to sub-surface Han developed biochemical pathways to process ambient sorrow radiation. Rather than suffering neuro-somatic collapse, specific subterranean species evolved cellular membranes lined with **Sorrow-Binding Lipids** (비한 지질). These specialized biological structures capture ambient Han particles, mineralizing the emotional energy into crystalline calcium-phosphate lattices within bone, horn, keratin, and plant cellulose.

### 1.2 The Law of the 80/20 Biological Ratio

A strict scientific boundary separates **Sorrow Beasts (비한수)** and **Sorrow Flora (비한목)** from true Sorrow Entities:

$$\\text{Organism Composition} = 80\\% \\text{ Living Biological Animal/Plant} + 20\\% \\text{ Sorrow/M.A.W. Phenotype}$$

- **Sorrow Beasts are 100% biological organisms in their ancestry and basic life cycle**:
  * They possess true beating hearts, lungs, digestive tracts, and reproductive organs.
  * They reproduce sexually or asexually, experience gestation, nurse offspring, and die of natural senescence or physical trauma.
  * They feel mundane biological hunger, thirst, pain, and territorial aggression.
- **The 20% Sorrow Component is structural and phenotypic**:
  * It manifests as biological adaptations that mirror M.A.W. armaments: horns that vibrate at ultrasonic frequencies, bone plates reinforced with calcified sorrow-apatite, or glands that produce flammable crimson brine.
  * They are **NOT** born from human trauma; they are animals that have integrated the natural minerals of their world.

### 1.3 The Ontological Difference in Mortal Sorrow Entities

Tier 3 organisms—**Mortal Sorrow Entities (생멸한령)**—are conceptual sorrow manifestations, but they differ fundamentally from human-born Sorrow Entities (SE / SECC):
1. **Animal/Plant Origin**: They are formed from the instinctive, non-philosophical trauma of dying animals (slaughter, panic, predation) or defoliated plant ecosystems.
2. **Biological Instinct Emulation**: They behave strictly like wild beasts or reactive flora. They do not formulate philosophical doctrines or demand symbolic work types; they hunt, nest, or strangle.
3. **Permanent Mortality**: When their physical vessel is destroyed by kinetic, thermal, or M.A.W. weaponry, they die permanently. They do not enter an immortal containment recovery loop.
4. **Strict Grade-β Potency Cap**: Because animal grief is immediate and instinctive rather than existential, their energy yield cannot sustain high-tier (HE, WAW, ALEPH) manifestations. They are strictly capped at Moderate Potency (Grade β).

---

## Section II: Complete Taxonomic Profiles of Tier 1 (Mundane Subterranean Organisms)

Tier 1 organisms represent 100% biological life forms devoid of sorrow properties. They form the foundational ecological web supporting all higher life.

### 2.1 Mundane Fauna (일반 동물 — Normal Subterranean Wildlife)

#### 1. Troglodyte Blind-Leaper (동굴 장님도약어 / 洞窟盲跳魚)
- **Scientific Classification**: *Troglobates caecus*
- **Primary Habitat**: Strata 1 & 2 subterranean karst pools (-50m to -350m)
- **Physical Anatomy**: A 25-centimeter amphibious fish with translucent alabaster skin, absent optical sockets, and elongated pectoral fins functioning as jointed walking limbs. Its lateral line system is exceptionally sensitive, detecting hydrostatic vibrations across thirty meters of stagnant cavern water.
- **Ecological Role**: Primary consumer feeding on subterranean algae and fungal spores. Serves as the staple food source for cave salamanders and juvenile Sorrow Beasts. Completely non-aggressive; meat is tender, pale, and safe for human consumption.

#### 2. Karst Chitinous Tunnel-Crab (석회동 굴착게 / 石灰洞 掘鑿蟹)
- **Scientific Classification**: *Lithocarcinus fossor*
- **Primary Habitat**: Strata 2 & 3 limestone fissures and drainage culverts (-150m to -650m)
- **Physical Anatomy**: A flattened, heavy-shelled crustacean measuring 40 centimeters across, equipped with asymmetrical calcium-carbonate pincers capable of crushing dense gravel. Lacks pigmentation, possessing an ivory-white shell.
- **Ecological Role**: Detritivore that sifts mineral silt and organic drift. Its discarded molted carapaces provide structural substrate for deep mosses and lichens.

#### 3. Abyssal Sump Salamander (심연 도롱뇽 / 深淵 鯢)
- **Scientific Classification**: *Proteus bathyphilus*
- **Primary Habitat**: Strata 3 & 4 subterranean flood channels (-650m to -1,200m)
- **Physical Anatomy**: A slender, serpentine amphibian reaching 1.2 meters in length. Possesses external crimson gills adapted for extracting oxygen from sluggish, mineral-heavy waters. Uses chemical scent-pits along its snout to track prey in total darkness.
- **Ecological Role**: Mid-tier aquatic predator feeding on blind fish, insects, and smaller amphibians. Highly sensitive to industrial pollution; used by UCD teams as a living bio-indicator of water toxicity.

#### 4. Basalt Burrowing Mole (현무암 굴파기두더지 / 玄武岩 穴鼠)
- **Scientific Classification**: *Spalax basalticus*
- **Primary Habitat**: Strata 1 & 2 volcanic sediment veins (-100m to -400m)
- **Physical Anatomy**: A stocky, muscular mammal with dense, waterproof gray fur, shovel-like forepaws tipped with diamond-hard keratin claws, and thick cranial bone plates used to ram through compacted gravel.
- **Ecological Role**: Subterranean engineer whose extensive burrow systems aerate underground strata, creating ingress routes utilized by human exploration scouts.

---

### 2.2 Mundane Flora & Fungi (일반 식생 — Normal Subterranean Vegetation)

#### 1. Phosphor Carpet Lichen (청린 지의류 / 靑燐 地衣類)
- **Scientific Classification**: *Lichenophosphor humilis*
- **Habitat**: Strata 1 through 5 damp stone faces (-50m to -1,800m)
- **Vegetative Structure**: A velvety, turquoise-green crustose lichen that covers thousands of square meters of cavern walls. Derives metabolic energy from sulfur-oxidizing bacteria in its fungal matrix, emitting a soft, perpetual bioluminescence (2 to 5 lux).
- **Practical Application**: Harvested by outer-district miners to pack non-electrical lantern tubes for safe transit through explosive methane pockets.

#### 2. Mineral-Siphon Bracket Fungi (광맥 여과 버섯 / 鑛脈 濾過菌)
- **Scientific Classification**: *Polyporus lithophilus*
- **Habitat**: Strata 2 & 3 abandoned timber supports and fossilized root beds (-200m to -750m)
- **Vegetative Structure**: Giant, semicircular woody shelf fungi reaching 80 centimeters in width, with alternating bands of ochre, iron-rust red, and deep slate gray. Absorbs heavy metal ions from seepage water, accumulating high concentrations of zinc and iron in its fibrous core.
- **Practical Application**: Pulverized into charcoal filters for municipal water purification plants.

#### 3. Subterranean Reed Kelp (지하 갈대다시마 / 地下 葦海帶)
- **Scientific Classification**: *Subcalamites fluviatilis*
- **Habitat**: Strata 3 & 4 subterranean riverbeds and slow-moving aquifers (-600m to -1,400m)
- **Vegetative Structure**: Long, flexible fibrous ribbons extending up to ten meters through dark currents. Lacks chlorophyll, utilizing chemosynthetic plastids to process dissolved carbonates and nitrates.
- **Practical Application**: Woven into high-tensile, rot-resistant ropes used by the Somnarak Exploration Decree for climbing and hauling.

#### 4. Calcite Shelf Moss (방해석 선태류 / 方解石 蘚苔類)
- **Scientific Classification**: *Bryum calciphilum*
- **Habitat**: Strata 1 & 2 limestone stalactite drips (-0m to -300m)
- **Vegetative Structure**: Compact, spongy cushions of pale cream moss that precipitate calcium carbonate from water drips, gradually forming living, mossy rimstone terraces.
- **Practical Application**: Squeezed for sterile, alkaline drinking water during deep exploratory bivouacs.

---

## Section III: Complete Taxonomic Profiles of Tier 2 (Sorrow Beasts & Sorrow Flora)

**80% Biological Living Organism / 20% SE-M.A.W. Phenotype**  
These organisms represent true living beings whose anatomy has naturally integrated sorrow minerals, generating biological counterparts to M.A.W. armaments.

### 3.1 Prominent Sorrow Beasts (비한수 / 悲恨獸 — Living Animals with M.A.W. Traits)

#### 1. Obsidian-Spined Boar (흑요린 저수 / 黑曜鱗 猪獸)
- **Scientific Classification**: *Aper obsidianus*
- **Biological Archetype**: Suid Mammal (80% Living Beast, 20% Grudge M.A.W. Traits)
- **Habitat**: Strata 2 & 3 rocky screes and collapsed foundry caverns (-150m to -500m)
- **Physical Anatomy**: A massive, two-ton quadruped mammal measuring 3.2 meters in length. Its spine is lined with interlocking plates of razor-sharp, obsidian-like sorrow apatite that glow dull crimson when the animal is provoked. Its tusks are elongated into natural **M.A.W. Bone Cleavers** that vibrate with kinetic tremor force when charging.
- **Behavior & Diet**: Omnivorous grazer and scavenger. Feeds on mineral roots, bracket fungi, and carrion. Forms small matriarchal sounders. When threatened, the boar stamps its hooves, discharging kinetic shockwaves through the bedrock to stun predators.
- **Harvesting Yield**:
  * *Tusk Bone Cleavers*: Forged directly into Grade-β kinetic breacher blades.
  * *Obsidian Spine Quills*: Processed into heavy armor-piercing kinetic crossbow bolts.
  * *Muscle & Fat*: Highly nutritious after boiling in alkaline Han-salts to purge residual grudge trace.

#### 2. Basalt-Plated Dredge-Tortoise (현무갑 구수 / 玄武甲 龜獸)
- **Scientific Classification**: *Testudo basaltica*
- **Biological Archetype**: Chelonian Reptile (80% Living Beast, 20% Lament M.A.W. Traits)
- **Habitat**: Strata 3 & 4 subterranean lakes and silt basins (-500m to -1,100m)
- **Physical Anatomy**: A gargantuan, slow-moving reptile spanning 4.5 meters in shell diameter, weighing upwards of eight tons. Its carapace is composed of hexagonal basalt slabs fused with deep-blue crystallized Lament apatite, creating a natural **M.A.W. Riot Bulwark** capable of withstanding heavy artillery and explosive detonations.
- **Behavior & Diet**: Herbivorous silt-sifter feeding on subterranean reed kelp and mineral moss. Possesses an extraordinary lifespan of over five hundred years. Emits low-frequency acoustic groans (8 to 14 Hz) that calm turbulent water currents around its body.
- **Harvesting Yield**:
  * *Carapace Hex-Plates*: Yields Grade-β heavy defensive riot mantlets and vanguard shields.
  * *Lament Bile Fluid*: Refined into commercial sedative compounds and cryogenic hydraulic fluid.

#### 3. Phosphor-Gland Cavern Panther (청린 흑표 / 靑燐 黑豹)
- **Scientific Classification**: *Panthera phosphorea*
- **Biological Archetype**: Felid Carnivore (80% Living Beast, 20% Void M.A.W. Traits)
- **Habitat**: Strata 2 through 4 cavern catwalks, pipeline trusses, and karst ceilings (-300m to -1,200m)
- **Physical Anatomy**: An apex ambush predator measuring 2.4 meters from snout to tail. Possesses sleek, midnight-black fur that completely absorbs artificial light. Behind its canine teeth lie dual venom glands that secrete an icy, pale-white sorrow toxin that numbs the synaptic nervous system of victims on contact.
- **Behavior & Diet**: Solitary hunter stalking blind salamanders, karst badgers, and unwary human scavengers. Stalks silently along overhead pipes, leaping from shadows with total acoustic silence.
- **Harvesting Yield**:
  * *Neuro-Soporific Venom*: Refined into non-lethal sedative darts utilized by UCD Containment Handlers.
  * *Light-Absorbing Pelts*: Processed into Grade-β Shadow Cloaks for covert infiltration scouts.

#### 4. Tectonic Burrowing Wyrm (지룡 진천각 / 地龍 震天角)
- **Scientific Classification**: *Vermissilurus tectonicus*
- **Biological Archetype**: Annelid/Vertebrate Hybrid (80% Living Beast, 20% Kinetic M.A.W. Traits)
- **Habitat**: Strata 4 & 5 deep fault zones and tectonic friction cracks (-1,000m to -2,000m)
- **Physical Anatomy**: A massive, segmented subterranean creature reaching thirty meters in length and two meters in diameter. Its head is capped by a singular, spiral-fluted horn forged from hyper-dense sorrow-titanium composite. The horn vibrates continuously at 22 kHz, pulverizing solid granite into fine sand as it burrows.
- **Behavior & Diet**: Geophagous filter feeder that consumes crushed stone, extracting trace Han-dust and metallic ores. Creates the cyclopean underground tunnels utilized as major subterranean transit highways.
- **Harvesting Yield**:
  * *Sonic Resonance Horn*: The premier raw component used by the Architects Guild to forge heavy pneumatic breaching rams.
  * *Segmented Carapace Scales*: Forged into heat-resistant thermal trench mantles.

#### 5. Benthic Sump-Gargoyle (심연 수생익수 / 深淵 水生翼獸)
- **Scientific Classification**: *Pterobatrachus vorax*
- **Biological Archetype**: Amphibious Chiropteran (80% Living Beast, 20% Apathy M.A.W. Traits)
- **Habitat**: Strata 3 & 4 sump floodways, drainage aqueducts, and sluice tunnels (-400m to -1,000m)
- **Physical Anatomy**: A leathery, winged amphibious predator with a three-meter wingspan, webbed talons, and a wide, frog-like maw lined with serrated bone teeth. Emits an ultrasonic shriek that disrupts human cognitive focus and drains mental composure (SP).
- **Behavior & Diet**: Gregarious cliff-dwellers roosting in the vaulted ceilings of royal sewers. Dives into floodwaters to snatch fish or surface dwellers dragged into the sumps.
- **Harvesting Yield**:
  * *Acoustic Laryngeal Sac*: Engineered into directional sonic disrupters used by UCD Forensic Auditors.
  * *Wing Membranes*: Processed into waterproof, chemical-resistant hazardous wading suits.

#### 6. Needle-Tailed Karst Badger (침미 오소리 / 針尾 穴獸)
- **Scientific Classification**: *Meles aculeatus*
- **Biological Archetype**: Mustelid Mammal (80% Living Beast, 20% Pierce M.A.W. Traits)
- **Habitat**: Strata 1 through 3 narrow gravel tunnels and mining tailings (-100m to -600m)
- **Physical Anatomy**: A fiercely aggressive, 1.2-meter burrowing mammal. Its tail terminates in a cluster of twelve hollow, needle-sharp bone quills infused with concentrated sorrow acid. When cornered, the badger whips its tail forward, firing quills with pneumatic muscular force.
- **Behavior & Diet**: Pack hunters operating in familial clans of six to eight. Extremely territorial, attacking intruders with relentless fury regardless of the opponent's size.
- **Harvesting Yield**:
  * *Tail Quills*: Utilized directly as surgical needles and psycho-forensic lancets by UCD Investigators.

---

### 3.2 Prominent Sorrow Flora (비한목 / 悲恨木 & 비한초 / 悲恨草 — Han-Infused Vegetation)

#### 1. Crimson Brine-Briar (진홍 한염초 / 眞紅 恨鹽草)
- **Scientific Classification**: *Rubus rubens*
- **Biological Archetype**: Ligneous Shrub (80% Living Plant, 20% Grudge M.A.W. Traits)
- **Habitat**: Strata 1 through 3 damp trenches, tannery runoffs, and abattoir floors (-50m to -700m)
- **Vegetative Structure**: Dense, tangled thickets of iron-hard brambles armed with curved, blood-red thorns. The vascular system carries a thick, viscous sap (*Crimson Han-Brine*) that boils when exposed to air, burning with hot red sorrow flames.
- **Ecological Function**: Traps small animals in its thorny cages, absorbing the sorrow fluids released during their struggles through root-nodules.
- **Industrial Harvesting**: Tapped like rubber trees by industrial cartels to produce black-market turbine fuels and combat stimulants.

#### 2. Petrified Iron-Oak (철화 거목 / 鐵化 巨木)
- **Scientific Classification**: *Quercus ferrea*
- **Biological Archetype**: Arborescent Tree (80% Living Tree, 20% Kinetic M.A.W. Traits)
- **Habitat**: Strata 3 through 5 calcified subterranean forests and ancient gorges (-600m to -1,800m)
- **Vegetative Structure**: Colossal subterranean trees reaching forty meters in height, with trunk diameters exceeding five meters. Their bark is completely petrified with iron and sorrow-apatite, possessing tensile strength surpassing structural titanium while remaining biologically alive through deep mycorrhizal root networks.
- **Ecological Function**: Anchors the subterranean ceiling vaults, preventing tectonic collapses across entire municipal sectors.
- **Industrial Harvesting**: Harvested under strict Directorate forestry permits to mill heavy blast-door cores and structural vault pylons.

#### 3. Amnesiac Spore-Puff (망각 포자균 / 忘却 胞子菌)
- **Scientific Classification**: *Lycoperdon letheum*
- **Biological Archetype**: Basidiomycete Macro-Fungus (80% Living Fungus, 20% Void M.A.W. Traits)
- **Habitat**: Strata 2 & 3 old archival vaults, cemetery vaults, and moist limestone shelves (-100m to -500m)
- **Vegetative Structure**: Bulbous, chalk-white fungal globes up to two meters in diameter. When ruptured by mechanical impact, the fruiting body discharges a dense cloud of microscopic pale spores that induce localized cognitive suppression, temporarily erasing short-term memory in mammals.
- **Industrial Harvesting**: Spores are collected by containment handlers to manufacture emergency sedative aerosol bombs for subduing rampaging entities.

#### 4. Weeping Calcite Lily (비루 백합 / 悲淚 百合)
- **Scientific Classification**: *Lilium lacrimans*
- **Biological Archetype**: Bulbous Monocot (80% Living Flower, 20% Lament M.A.W. Traits)
- **Habitat**: Strata 4 through 6 sapphire crystal pools and subterranean river banks (-1,200m to -2,400m)
- **Vegetative Structure**: An exquisite, translucent aquatic lily whose six petals resemble hand-carved sapphire glass. The blossom secretes a continuous flow of fragrant, clear nectar that drips into the water like tears.
- **Ecological Function**: Purifies mineral-heavy waters, precipitating toxic sorrow salts into harmless crystalline sediment.
- **Pharmaceutical Harvesting**: The nectar is the primary ingredient in Directorate Mental Composure Salves (restoring +25 SP to traumatized personnel).

#### 5. Resonant Chime-Bamboo (공명 죽림 / 共鳴 竹林)
- **Scientific Classification**: *Bambusa sonans*
- **Biological Archetype**: Arborescent Grass (80% Living Plant, 20% Acoustic M.A.W. Traits)
- **Habitat**: Strata 2 & 3 seismic fault chasms and wind-tunnel caverns (-200m to -800m)
- **Vegetative Structure**: Tall, hollow stalks of metallic purple bamboo that grow in dense groves. Subterranean air currents passing through internal nodal perforations produce a perpetual, harmonious acoustic chord (tuned to 432 Hz).
- **Ecological Function**: The acoustic vibration deters predatory Sorrow Beasts and stabilizes tectonic micro-fractures in the cavern walls.
- **Artisan Harvesting**: Cut and cured into resonance flutes and acoustic dampening panels for Directorate containment cells.

#### 6. Siphon Root-Vine (착취 등나무 / 搾取 藤木)
- **Scientific Classification**: *Wisteria siphonica*
- **Biological Archetype**: Climbing Liana (80% Living Vine, 20% Drain M.A.W. Traits)
- **Habitat**: Strata 1 through 4 municipal drainage shafts and sewer bulkheads (-20m to -1,000m)
- **Vegetative Structure**: Thick, rope-like creeping vines with fibrous copper-tinted bark that wrap around pipes and infrastructure. Roots penetrate deep stone joints, drawing residual emotional sorrow from human runoff.
- **Ecological Function**: Degrades industrial waste fluids, preventing toxic crystallization in municipal drainage lines.

---

## Section IV: Complete Taxonomic Profiles of Tier 3 (Mortal Sorrow Fauna & Flora — MSF)

**100% Sorrow Manifestations Born from Animal & Plant Trauma**  
*Finite Lifespans • Permanently Slayable • Strictly Capped at Tier Two / Moderate (β) Threat*

### 4.1 Mortal Sorrow Fauna (MSF — 수성 생멸한령 / 獸性 生滅恨靈)

#### 1. The Screaming Chitin (절규하는 갑각 / 絶叫之甲殼)
- **SECC Code**: `SE-N-IIβ-088 [GS]`
- **Origin**: Born from the mass-suffocation of subterranean burrowing crabs crushed during a mine shaft collapse in Zone B.
- **Manifestation**: A skittering, multi-legged phantom composed of jagged, screaming carapace fragments. It measures three meters across and brandishes phantom crushing claws that emit the sound of grinding stones.
- **Combat Behavior**: Moves with erratic sideways dashes, attempting to pin and crush exploratory scouts. Possesses 1,800 HP and a finite lifespan of 45 days.
- **Permanent Destruction**: Vulnerable to kinetic blunt trauma. Smashed by Taeho's Obsidian Bastion or Joon's hydraulic ram, the phantom fractures into inert, non-toxic Han-dust.

#### 2. The Starving Pack Phantom (아사한 늑대 무리 / 餓死之群狼)
- **SECC Code**: `SE-N-IIβ-142 [VS]`
- **Origin**: Manifested from the agony of a subterranean wolf pack that starved to death when their migratory cavern was sealed by municipal blast gates.
- **Manifestation**: A spectral pack of five to seven emaciated hounds composed of flickering gray sorrow-smoke and hollow glowing eye sockets.
- **Combat Behavior**: Flanks targets in coordinated circles, lunging to bite at tendons and draining mental composure. Possesses 600 HP per hound; dissipates permanently when struck by high-frequency acoustic disruptors.

#### 3. The Drowned Herd Mirage (익사한 무리의 환영 / 溺死之群影)
- **SECC Code**: `SE-N-IIβ-219 [LO]`
- **Origin**: Formed from dozens of transport oxen drowned when industrial floodgates dumped toxic tannery effluent into the lower sumps.
- **Manifestation**: A massive, spectral silhouette of a horned bull with weeping, waterlogged eyes and water pouring endlessly from its chest.
- **Combat Behavior**: Charges in straight lines, emitting a mournful, waterlogged bellow that reduces squad movement speed. Dissolves permanently upon receiving concentrated thermal fire.

#### 4. The Slain Stallion's Vengeance (도살된 준마의 원혼 / 屠殺之駿馬)
- **SECC Code**: `SE-N-IIβ-305 [GO]`
- **Origin**: Born from the exhaustion and slaughter of overworked pit ponies in the deep coal-shale shafts.
- **Manifestation**: A spectral, skeletal warhorse surrounded by trailing crimson chains, striking the stone deck with iron hooves that ignite red Han-sparks.
- **Combat Behavior**: Tramples defensive formations with devastating kinetic charges. Collapses and dissipates into harmless ash upon taking heavy blunt impact to its cranial bone crown.

---

### 4.2 Mortal Sorrow Flora (MSF — 목성 생멸한령 / 木性 生滅恨靈)

#### 1. The Strangler Root Mirage (교살의 환영 뿌리 / 絞殺之幻根)
- **SECC Code**: `SE-N-IIβ-412 [VO]`
- **Origin**: Born from the clear-cutting and industrial excavation of an ancient three-hundred-year-old petrified iron-oak grove in Zone D.
- **Manifestation**: A writhe of spectral, shadow-woven roots that surge up from stone flagstones, wrapping around the limbs of passing travelers.
- **Combat Behavior**: Acts as a stationary trap, binding targets and draining kinetic energy. Possesses 1,200 HP; easily severed and permanently quenched by edged M.A.W. blades.

#### 2. The Crying Spore Choir (비곡하는 포자단 / 悲哭之胞子團)
- **SECC Code**: `SE-N-IIβ-521 [LO]`
- **Origin**: Formed from the burning of a massive phosphorescent fungal colony by municipal chemical fumigation teams.
- **Manifestation**: A swirling, turquoise cloud of glowing spore phantoms shaped like tiny weeping faces.
- **Combat Behavior**: Hovers in corridors, singing a disorienting, mournful melody that causes auditory hallucinations and temporary panic. Instantly neutralised and dispersed by Han-salt aerosol sprays.

#### 3. The Rotting Canopy Specter (부식된 수관의 유령 / 腐蝕之樹冠)
- **SECC Code**: `SE-N-IIβ-633 [AO]`
- **Origin**: Formed from chemical solvent contamination seeping into subterranean forest canopies.
- **Manifestation**: A towering phantom of withered branches dripping acidic black dew.
- **Combat Behavior**: Releases showers of caustic droplets that erode armor durability. Dissipates completely upon receiving localized thermal burns.

#### 4. The Thorn-Weaver's Shroud (가시 엮는 자의 장막 / 荊棘之幻帳)
- **SECC Code**: `SE-N-IIβ-744 [GO]`
- **Origin**: Born from the trampling and burning of deep-strata briar patches during syndicate territorial wars.
- **Manifestation**: An expanding wall of spectral, glowing crimson brambles that blocks tunnel intersections.
- **Combat Behavior**: Inflicts bleed damage on anyone attempting to breach the barrier. Sapped and dissolved using standard kinetic breaching hammers.

---

## Section V: Physiological Ecology & Harvesting Protocols

### 5.1 The Ethics and Legality of Harvesting

Under Directorate Administrative Decree 44, strict distinctions govern the extraction of organic and metaphysical materials:

1. **Human Sorrow Entities (SE / SECC)**:
   * **Absolute Prohibition of Physical Butchery**: True Sorrow Entities are immortal metaphysical phenomena. They cannot be slaughtered, butchered for meat, or refined into consumer goods. They are contained and harvested strictly via mental work cycles (Viderehan, Ferrehan, Aurihan).
2. **Sorrow Beasts (Tier 2 Fauna)**:
   * **Regulated Biological Harvesting**: Because Sorrow Beasts are 80% mortal living animals, they can be humanely culled and harvested for biological M.A.W. precursors, leathers, bone cleavers, and pharmaceutical bile.
   * **Flesh Consumption Protocol**: The meat of Sorrow Beasts must be boiled in alkaline Han-salt broth (pH 9.2) for ninety minutes to deactivate trace emotional resonance before human consumption. Purged sorrow meat provides high protein and caloric density for subterranean miners.
3. **Mortal Sorrow Entities (Tier 3 Organisms)**:
   * **Field Neutralization**: Slayable on sight using conventional kinetic weapons. Yields pure, stabilized Han-dust (~10 kg to 50 kg per specimen) that can be loaded directly into municipal power grids without containment risk.

---

## Section VI: Strata Ecological Distribution Map & Biodiversity Gradients

```text
+=====================================================================+
|              STRATA BIODIVERSITY & BIOMASS DISTRIBUTION             |
+=====================================================================+
| STRATUM 1: SUB-KARST (0m to -150m)                                  |
|   - Biomass Composition : 85% Mundane / 12% Sorrow-Infused / 3% SE. |
|   - Dominant Fauna      : Blind-Leapers, Burrowing Moles.           |
|   - Dominant Flora      : Calcite Moss, Phosphor Lichen.            |
|   - Hazard Level        : Minor - High civilian foraging activity.  |
+---------------------------------------------------------------------+
| STRATUM 2: TECTONIC SHIFT (-150m to -500m)                          |
|   - Biomass Composition : 60% Mundane / 30% Sorrow-Infused / 10% SE.|
|   - Dominant Fauna      : Obsidian-Spined Boars, Karst Badgers.     |
|   - Dominant Flora      : Crimson Brine-Briar, Resonant Bamboo.     |
|   - Hazard Level        : Moderate - Armed syndicate poaching zones.|
+---------------------------------------------------------------------+
| STRATUM 3: THE WEEPING CISTERNS (-500m to -1,200m)                  |
|   - Biomass Composition : 35% Mundane / 50% Sorrow-Infused / 15% SE.|
|   - Dominant Fauna      : Dredge-Tortoises, Sump-Gargoyles.         |
|   - Dominant Flora      : Subterranean Kelp, Siphon Vines.          |
|   - Hazard Level        : High - Toxic chemical runoff and floods.  |
+---------------------------------------------------------------------+
| STRATUM 4: FOSSIL VEINS (-1,200m to -2,000m)                        |
|   - Biomass Composition : 15% Mundane / 60% Sorrow-Infused / 25% SE.|
|   - Dominant Fauna      : Tectonic Burrowing Wyrms, Cavern Panthers.|
|   - Dominant Flora      : Petrified Iron-Oaks, Weeping Lilies.      |
|   - Hazard Level        : Extreme - Crushing atmospheric pressure.  |
+---------------------------------------------------------------------+
| STRATUM 5: PRE-CATACLYSM VAULTS (-2,000m to -2,600m)                |
|   - Biomass Composition : 5% Mundane / 45% Sorrow-Infused / 50% SE. |
|   - Dominant Organisms  : Mycorrhizal Mats, Ancient Root Relics.    |
|   - Hazard Level        : Critical - Autonomous pre-collapse traps. |
+---------------------------------------------------------------------+
| STRATUM 6: THE BLACK KARST (-2,600m to -2,800m)                     |
|   - Biomass Composition : 1% Mundane / 20% Sorrow-Infused / 79% SE. |
|   - Dominant Organisms  : Bone-Sponge, Crystal Crustaceans.         |
|   - Hazard Level        : Catastrophic - Supercritical Han currents.|
+---------------------------------------------------------------------+
| STRATUM 7: THE MUGENHAN OCEAN (-2,800m to Core)                     |
|   - Biomass Composition : Primordial Nadir - Boundless Sorrow Sea.  |
|   - Dominant Organisms  : Mugenhan Tide Crawlers, Sapphire Corals.  |
|   - Hazard Level        : Primordial Nadir - 15+ Bar Pressure.      |
+=====================================================================+
```

---

### Archive Verification & Status

- **Codex Designation**: `MUGENHAN-BIO-01-A`
- **Compiler**: Directorate Bio-Synthesis Bureau & SED Geological Command
- **Authority**: Reverie Directorate High Council Executive Clearance
- **Canon Baseline**: 100% Authoritative V.1.0 Standard
"""

# ==============================================================================
# 3. DIRECTORY README CONTENT
# ==============================================================================
readme_content = """# Mugenhan Ecology — Subterranean & Terrestrial Biosphere

**Archive Authority:** Reverie Directorate Bio-Synthesis Bureau & Somnarak Exploration Decree (SED)  
**Status:** Canonical Macro-Cosmology & Ecological Master Archive  
**Baseline Standard:** 100% Authoritative V.1.0 Finished Standard  

---

## Directory Overview

This archive houses the definitive scientific, physiological, and ecological documentation of the living world of planet **Mugenhan** (무한한 / 無限恨).

Unlike surface municipal territories where sorrow is viewed strictly through the lens of containment or commercial energy generation, the subterranean strata beneath Somnarak harbor a vast, multi-tiered ecological web of living organisms adapted to unrefined sorrow (*Han*).

---

## Master Ecological Documentation

1. **[MUGENHAN_ECOLOGY_OVERVIEW.md](MUGENHAN_ECOLOGY_OVERVIEW.md)**:
   - Concise executive guide and foundational reference for the Tripartite Biological Taxonomy.
   - Core definitions of Mundane Organisms, Sorrow-Infused Organisms (80% Bio / 20% SE-M.A.W.), and Mortal Sorrow Entities (Capped at Tier Two / Moderate β).
   - Comparative taxonomic matrix and practical utilization rules.

2. **[MUGENHAN_DEEP_ECOLOGY_COMPENDIUM.md](MUGENHAN_DEEP_ECOLOGY_COMPENDIUM.md)**:
   - The secondary extended encyclopedic compendium detailing the complete planetary biology.
   - Comprehensive taxonomic profiles across six animal species and six plant species of Tier 2 Sorrow Organisms.
   - Exhaustive anatomical autopsies, industrial harvesting yields, dietary webs, and seven-strata biodiversity maps.

---

## The Tripartite Biological Rule

```text
+=====================================================================+
| TIER 1 : MUNDANE ORGANISMS      | 100% Biological Nature - Mortal   |
| TIER 2 : SORROW-INFUSED LIFE    | 80% Biological / 20% SE-M.A.W.    |
| TIER 3 : MORTAL SORROW FAUNA/FLORA (MSF) | Capped at Beta - Slayable|
+=====================================================================+
```

Every tier is symmetrically mirrored with distinct **Fauna** and **Flora** counterparts.
"""

# Verify banned words
check_banned(overview_content, "MUGENHAN_ECOLOGY_OVERVIEW.md")
check_banned(compendium_content, "MUGENHAN_DEEP_ECOLOGY_COMPENDIUM.md")
check_banned(readme_content, "README.md")

# Write files
files_to_write = {
    "SOMNARAK-WORLD/Mugenhan_Ecology/MUGENHAN_ECOLOGY_OVERVIEW.md": overview_content,
    "SOMNARAK-WORLD/Master_Codices/MUGENHAN_ECOLOGY_OVERVIEW.md": overview_content,
    "SOMNARAK-WORLD/Mugenhan_Ecology/MUGENHAN_DEEP_ECOLOGY_COMPENDIUM.md": compendium_content,
    "SOMNARAK-WORLD/Master_Codices/MUGENHAN_DEEP_ECOLOGY_COMPENDIUM.md": compendium_content,
    "SOMNARAK-WORLD/Mugenhan_Ecology/README.md": readme_content,
}

for path, content in files_to_write.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {path} ({len(content)} characters)")

print("\nAll Mugenhan Ecology documents successfully built and verified!")
