# SOMNARAK-WORLD — Canonical In-Universe Document Archive

**Repository:** `SOMNARAK-WORLD/`
**Temporal Setting:** Year 4,238 · Dawn Initiative Epoch
**Issuing Authority:** The Reverie Directorate (몽환국) & Facility 01 Central Command
**Document Nature:** 100% In-Universe Narrative & Operational Source Corpus

---

## Overview

The **`SOMNARAK-WORLD/`** directory is the dedicated repository for all **in-world documents** of the Somnarak universe. Every file, dossier, field manual, legal treatise, and narrative log within this tree is written strictly from the perspective of an in-universe observer: a Directorate clerk, a Facility 01 Echo-Core, a containment worker, a Giltong enforcer, or an Outskirts wanderer.

Out-of-world developer handbooks, AI instructions, transfer percentage reports, and structural audit manifests are housed separately in `REFERENCE_SOMNARAK_WIKI/`.

---

## Directory Architecture

```
SOMNARAK-WORLD/
├── README.md                           # This in-world archival overview
│
├── 07_Reference/                       # 34 Foundational Macro-Canon Master Codices (~435,000 words)
│   ├── PROJECT_SOMNARAK.md             # The Grand Worldbuilding Bible & Metaphysical Cosmology
│   ├── The_REVERIE_DIRECTORATE.md      # Facility 01 Architecture, 8 Subterranean Floors & Echo-Cores
│   ├── SOMNARAK_CHEONGULA.md           # The First Sorrow, Year 0 Cataclysm & Maw Origins
│   ├── SOMNARAK_THE_WEEPING.md         # Hydrology of the Underground River of Liquid Han
│   ├── SOMNARAK_BATTLE_SYSTEM.md       # Combat Engine: 4 Elements, Work Types & Panic Mechanics
│   ├── SOMNARAK_MAW_CODEX.md           # Master Materialized Armament of Woe Extraction Science
│   ├── SOMNARAK_ABSOLOVHAN.md          # Sovereign Golden Dawn, Resonant Clash & Sorrow Release
│   └── (27 additional master codices covering factions, laws, underworld, and curfews)
│
├── 01_Sorrow_Entities/                 # 529 Entity Dossiers & Tales (285 Unique Entities)
│   ├── README.md                       # SECC classification guide & work-type affinity rules
│   └── SE-<Manifestation>-<Tier>-<ID>_*.md # Containment procedures, work affinities & breach tales
│
├── 02_Hope_Transformation/             # 14 Sacred Resonance Ascensions
│   ├── README.md                       # Lore of Hope crystallization and the Dawn Protocol
│   └── HT-*.md                         # HT-001 to HT-012, Trinity of Dawn, and Hand of Hope
│
├── 03_Unknown_Entities/                # 8 Black-Level Quarantined Anomaly Files
│   ├── README.md                       # Deep Vault (Floor 6) isolation protocols
│   ├── Book_of_Regressor_Log_Dramaturgy.md # Cyclical recurrence manuscript
│   └── SE-*.md                         # UNK-248, UNK-251, UNK-901 (The Mewgical Girl), etc.
│
├── 04_Ordeals/                         # 60 Cyclical Incursion Threat Logs
│   ├── README.md                       # The Five Colors & Four Watches framework
│   ├── Ordeal_BLACK_*.md               # Weight (Density / Gravitational Collapse)
│   ├── Ordeal_BLUE_*.md                # Lament (Brine Floods / Weeping Tides)
│   ├── Ordeal_GREY_*.md                # Grudge (Physical Armed Battalions)
│   ├── Ordeal_PALE_*.md                # Void (Conceptual Erasure / Soul Severance)
│   └── Ordeal_PURPLE_*.md              # Mixed (Reality Convergence / Altar Hazards)
│
├── CHARACTER_WIKI/                     # 9 Echo-Core Personnel Files (~115,000 words)
│   ├── README.md                       # Facility 01 Floor Leadership Directory
│   ├── THE_DIRECTOR.md                 # Director Ayshuk (Executive Command & Dawn Protocol)
│   ├── THE_SECRETARY.md                # Chief Secretary Seiyon (Facility 01 Central)
│   ├── THE_CONTAINMENT_LEAD.md         # Floor 1: Majin (Primary Restraint & Suppression)
│   ├── THE_ARCHIVE_LEAD.md             # Floor 2: Dekan (Historical Records & Anomaly Memory)
│   ├── THE_EXTRACTION_LEAD.md          # Floor 3: Mellda (Han Refining Forge Master)
│   ├── THE_RESEARCH_LEAD.md            # Floor 4: Ishall (Behavioral Insight & Biology)
│   ├── THE_BORDER_LEAD.md              # Floor 5: Marjuk (Perimeter Quarantine & Defense)
│   ├── THE_EXILE.md                    # Floor 6: Zyrak (Deep Vault Warden)
│   └── THE_OUTSIDER.md                 # Floor 8: Xyan (Gate Watch Threshold Commander)
│
└── M.A.W. Codex_Set Registry/          # 1,196 Files across 42 Registry Range Folders
    ├── README.md                       # Master Registry status & set structure overview
    ├── REGISTRY_MASTER_STATUS.md       # Comprehensive set completion ledger
    └── Registry_<Range>/               # 42 folders containing quadripartite equipment sets:
        └── <Set_ID>_<Entity_Name>/
            ├── SE-<ID>-A__SIDE_CODEX_*.md # Entity extraction lore & identity
            ├── SE-<ID>-B__MAW-W_*.md      # Weapon specs, damage element & combat actions
            ├── SE-<ID>-C__MAW-S_*.md      # Suit defense ratings & passive resistances
            └── SE-<ID>-D__MAW-G_*.md      # Gift equip slot, appearance & resonance perks
```

---

## Core In-Universe Metaphysical Concepts

When consulting or authoring records in `SOMNARAK-WORLD/`, maintain complete fidelity to the foundational laws of Somnarak:

1. **Han (한 / 恨):** The primordial energy born of unexpressed human sorrow, injustice, and longing. It powers the city's machinery, flows through the Weeping River, and condenses into Sorrow Entities.
2. **The Maw (구라 / 口羅):** The colossal subterranean chasm beneath Somnarak from which the Weeping emerged during the Year 0 Cheongula Cataclysm.
3. **Absolvohan (해한 / 解恨):** The metaphysical unbinding and purification of sorrow; the final objective of Director Ayshuk's Dawn Initiative.
4. **Sorrow Entities (슬픔의 실체):** Autonomous manifestations categorized by SECC designations and threat classifications: `ZAYIN` (I), `TETH` (II), `HE` (III), `WAW` (IV), and `ALEPH` (V).
5. **M.A.W. (Materialized Armament of Woe):** Resonant armaments extracted and stabilized from entity cores, essential for surviving high-potency sorrow fields.
6. **The Four Damage Elements:**
   - **Grudge (원한 / Crimson):** Physical and kinetic trauma.
   - **Lament (비탄 / Blue):** Psychic erosion, tears, and despair.
   - **Void (공허 / Pale White):** Existential erasure targeting memory and identity.
   - **Weight (비중 / Black):** Irreversible gravitational compaction and existential burden.

---

## Master Recommended In-World Reading Sequence

```
1. 07_Reference/PROJECT_SOMNARAK.md          → The foundational scripture of Somnarak cosmology
2. 07_Reference/The_REVERIE_DIRECTORATE.md   → Architecture of Facility 01 and its departmental mandates
3. 07_Reference/SOMNARAK_BATTLE_SYSTEM.md    → Combat physics, work types, and energy containment
4. 07_Reference/SOMNARAK_MAW_CODEX.md        → The science of sorrow extraction and armaments
5. CHARACTER_WIKI/README.md                  → The Nine Echo-Cores who sustain the facility
6. 01_Sorrow_Entities/README.md              → Containment protocols for the registered entities
7. 07_Reference/SOMNARAK_ABSOLOVHAN.md       → The prophecy of the Golden Dawn
```
