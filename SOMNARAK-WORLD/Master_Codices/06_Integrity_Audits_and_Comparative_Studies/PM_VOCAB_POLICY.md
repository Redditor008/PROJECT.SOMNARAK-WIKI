# PROJECT SOMNARAK // PROJECT MOON VOCABULARY SCOPE & WHITELIST POLICY
## Master Architecture Standard for Terminology Hygiene & Cross-System Lexicons

```text
+========================================================================+
|         PROJECT SOMNARAK // PROJECT MOON VOCABULARY POLICY             |
+========================================================================+
| Document ID          | STD-VOCAB-001-CANON                             |
| Status               | Authoritative Policy (Zero Unintended PM Leaks) |
| Core Principle       | In-Universe Purity vs. Comparative Translation  |
| Target Wings         | SOMNARAK-WORLD, GAME_BATTLE, docs/, PM_RESEARCH |
+========================================================================+
```

---

## 1. PURPOSE & ARCHITECTURAL SCOPE

Project Somnarak is an independent, original gothic-industrial dieselpunk universe. While developed with deep reverence for Korean indie narrative design and tactical management philosophy (exemplified by Project Moon's *Lobotomy Corporation*, *Library of Ruina*, and *Limbus Company*), its **in-universe narrative corpus must remain 100% linguistically autonomous**.

This document codifies the strict folder-by-folder boundary between:
1. **The In-Universe Canonical Sphere:** Absolute prohibition of external developer terms.
2. **The Comparative & Academic Sphere:** Whitelisted comparative terminology permitted exclusively for structural analysis, game system translation, and wiki references.

---

## 2. REPOSITORY JURISDICTION MATRIX

| Repository Subtree | PM Vocabulary Status | Policy Mandate |
| :--- | :--- | :--- |
| **`SOMNARAK-WORLD/Story_Cantos/`** | **STRICTLY PROHIBITED (0.0%)** | Zero PM terminology. Pure in-universe narrative only. |
| **`SOMNARAK-WORLD/Sorrow_Entities/`** | **STRICTLY PROHIBITED (0.0%)** | Sorrow Entities, M.A.W., Coherence I–V, Potency α–ω only. |
| **`SOMNARAK-WORLD/Ordeals/`** | **STRICTLY PROHIBITED (0.0%)** | Watches (First, Second, Third, Tide), Han Pressure only. |
| **`SOMNARAK-WORLD/Gieok_Jeojangso/`** | **CANONICAL NATIVE (Whitelisted)** | Memory Archive Sub-Alpha protocol: Key Pages (  핵심 책장  ), Reception (  접대  ). |
| **`SOMNARAK-WORLD/Echo_Cores/`** | **STRICTLY NATIVE (Contextual Whitelist)**| Seiyon / Memory Archive uses Key Pages; all other Leads use Engram Pages. |
| **`GAME_BATTLE/`** | **STRICTLY NATIVE (Contextual Whitelist)**| Scenario 06 uses Stratum Realization & Key Page yield; all others use native terms. |
| **`SOMNARAK-WORLD/Master_Codices/` (01–05)** | **STRICTLY NATIVE (Contextual Whitelist)**| The Memory Archive doctrine codifies Key Pages; other codices use Engram Pages. |
| **`Master_Codices/06_...` (Comparative)** | **WHITELISTED (Comparative)** | Authoritative translation matrices and system cross-studies. |
| **`PROJECT_MOON_RESEARCH/`** | **WHITELISTED (Research)** | Exhaustive 16-volume encyclopedic analysis of PM canon. |
| **`docs/game-wiki/`** | **WHITELISTED (Game Wiki)** | Dedicated Moon-style gameplay mechanics & conversion portal. |

---

## 3. CANONICAL IN-UNIVERSE MAPPING TABLE & MEMORY ARCHIVE WHITEMARK

### General In-Universe Equivalence
When referencing concepts that share mechanical lineage with tactical deckbuilders or containment simulators, operatives and scribes must adhere strictly to native terminology:

| PM / LoR Legacy Term | Somnarak In-Universe Native Equivalent | Context & Usage |
| :--- | :--- | :--- |
| **Abnormality** | **Sorrow Entity (  비탄체  , *Bitanche*)** | Manifested human sorrow |
| **E.G.O** | **M.A.W. (Materialized Agony Weaponry)** | Extracted equipment |
| **Enkephalin (PE-Box)** | **Han-Energy (  한 에너지  )** | Refined sorrow fuel |
| **Reception** | **Archival Encounter / Reception (  기록 조우 / 접대  )** | Tactical battle engagement |
| **Key Page** | **Engram Record Page / M.A.W. Attire (  핵심 책장  )** | Operative loadout sheet |
| **Combat Page** | **Action Strike / Tactical Intention** | Turn combat action |
| **Floor Realization** | **Stratum Realization (  지층 구현전  )** | Psychological boss descent |
| **Light** | **Posture / Coherence Will** | Turn resource expenditure |
| **Emotion Level** | **Resonance Depth (  공명 심도  )** | Psychological escalation |

### The Memory Archive Proprietary Lexicon (Whitelisted Canon Law)
Under Municipal Directive MA-01, the subterranean sector known as **The Memory Archive (  기억저장소  , *Gieok Jeojangso*)** (strata -2,350m to -3,250m) operates under the sovereign **Library Reception Protocol (  서고 접대 규약  )**. Within this specific municipal wing:
1. **Key Pages (  핵심 책장  , *Haeksim Chaekjang*):** The crystallized mnemonic codices extracted from suppressed memory entities and floor sovereigns (e.g., `[Key Page: The Archivist]`, `[Key Page: The Promise]`) are authentic, native Somnarak terminology.
2. **Receptions (  접대  , *Jeopdae*):** The formal 6-turn combat audits conducted by Secretary Seiyon and her projection retinue are canonical institutional designations.
3. **Cross-Departmental Mentions:** Mentions in other departmental records (e.g. Echo-Cores, Horizon Caravan, Master Codices) describing the acquisition, liquidation, or absence of Memory Archive Key Pages are canonically valid.
4. **General Operative Standard:** In general surface combat, SED tunneling, and UCD pacification, operatives equip **M.A.W. Attire** and **Mnemonic Cycle Engrams**.

---

## 4. ENFORCEMENT & LINTING

Any pull request or commit modifying files in `SOMNARAK-WORLD/` (outside Section 06) will be linted against `tools/seam_lint.py` and `tools/banned_strings.txt`. Verbatim PM terms appearing in non-comparative narrative files will trigger an immediate build failure.
