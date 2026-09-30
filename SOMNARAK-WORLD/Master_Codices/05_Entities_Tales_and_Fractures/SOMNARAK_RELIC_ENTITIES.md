# SOMNARAK — Relic Entities
## The Still Sorrow: Object, Place, and Time Manifestations

> *“Some sorrows do not walk. They wait.”*

---

## Overview

**Relic Entities** are Sorrow Entities whose manifestation is **stationary** — an Object (e.g., a clock, a scale, a tree), a Place (e.g., a wall, a well, a corridor), or a Time (e.g., an hour that will not pass). Unlike Subject entities that breach and roam, Relic Entities **do not move**. Their danger is not chase — it is **presence**.

88 of the 291 canonical Sorrow Entities are Relic manifestations (30.24%), overseen by the Restricted Registry `Registry_UNK_247_to_903` and the standard registries. They are the Somnarak analogue of stationary sorrow — grief that has soaked into things and places until the thing itself remembers.

---

## I. What Defines a Relic Entity

### Manifestation Triad

| Manifestation | Core | Field Example | Containment Signature |
|---|---|---|---|
| **Object** | A discrete item that holds sorrow | Clock (`SE-C-IVβ-044`), Scale (`SE-C-IIIβ-015`), Mask (`SE-C-IIIδ-010`) | Entity occupies a plinth or case; Work performed at the object |
| **Place** | A bounded space that *is* the sorrow | Wall (`SE-C-Vδ-180`), Well (`SE-C-IIIα-115`), Corridor (`SE-C-IIIβ-073`) | Entity *is* the room; personnel enter the entity to perform Work |
| **Time** | A temporal interval that loops or stalls | Hour (`SE-C-IIIβ-036`), 11:59 (`SE-C-Vγ-032`), The 27th March Shelter | Entity manifests as a repeating time; Work must be timed |

### The Still Law

Relic Entities obey the **Two-Work-Type Rule** — the single most violated protocol in the archive:

```text
+========================================================================+
| THE TWO-WORK-TYPE RULE (RELIC)                                         |
+------------------------------------------------------------------------+
| Relic Entities (Object / Place / Time) permit ONLY:                    |
| • Viderehan — Observation Work                                         |
| • Ferrehan — Endurance Work                                            |
| Flerehan and Pugnahan are strictly N/A                                 |
| Violation = immediate Gauge surge + activation / expansion             |
+========================================================================+
```

This rule exists because you cannot *empathize* with a wall or *suppress* an hour — you can only watch it and endure it. See `SOMNARAK_ENTITY_CODEX.md` and every Relic dossier for per-entity validation.

---

## II. Operational Doctrine

### Work Protocols for Relics

- **Viderehan (Observation):** Remote optical surveillance, spectral capture, Han-density trending. Decreases Sorrow Gauge on 94% of Relics.
- **Ferrehan (Endurance):** Seated vigilance within the manifestation's pressure field, breathing discipline, veil-stone buffering. Decreases Gauge on 89% of Relics.
- **Flerehan / Pugnahan:** Listed as N/A. Attempting them triggers the entity's **activation** — the Object cracks, the Place expands, the Time skips.

### Breach vs Activation vs Expansion

Relics do not “escape” like Subjects. They **activate** or **expand**:

- **Activation:** The station becomes *more itself* — the clock ticks backward, the wall weeps, the hour repeats.
- **Expansion:** The Place-entity grows — corridors lengthen, wells deepen, rooms annex adjacent cells.
- **Containment Response:** Not pursuit — **quarantine**. Seal adjacent sectors, stabilize Lumen, and resume Viderehan/Ferrehan from outside the threshold.

See `SOMNARAK_BATTLE_SYSTEM.md` — Tactical Engine Phase 2 (Clash) for Relic-specific engagement rites.

---

## III. Relic Entity Registry — Representative Index

| SECC | Name | Manifestation | Where to Read |
|---|---|---|---|
| `SE-C-IVβ-044` | The Broken Clock (부서진 시계) | Object-Time | `Sorrow_Entities/SE-C-IVβ-044_The_Broken_Clock_부서진_시계.md` |
| `SE-C-IIIβ-015` | The Debt Scale (빚의 저울) | Object | `Sorrow_Entities/SE-C-IIIβ-015_The_Debt_Scale_빚의_저울.md` |
| `SE-C-IIIα-115` | The Memory Well (기억의 우물) | Place | `Sorrow_Entities/SE-C-IIIα-115_Remembrance_기억의_우물.md` |
| `SE-C-Vδ-180` | The Debt Wall (빚의 벽) | Place | `Sorrow_Entities/SE-C-Vδ-180_The_Debt_Wall_빚의_벽.md` |
| `SE-C-IIIβ-036` | The Cracked Hourglass (금이 간 모래시계) | Object-Time | `Sorrow_Entities/SE-C-IIIβ-036_The_Cracked_Hourglass_금이_간_모래시계.md` |
| `SE-O-Vγ-003` | The Wilderness Tide (황야의 파도) | Place (Planetary) | `Sorrow_Entities/SE-O-Vγ-003_Wilderness_Tide.md` — *exception: Outside Sovereign managed via Geology* |

Full registry: `CANONICAL_METRICS.json` — `relic_entities_count: 88`.

---

## IV. Extraction — Relic M.A.W.

Relic Entities yield M.A.W. as all entities do — but Relic M.A.W. carries **stationary echo**:

- Objects yield **hand-held** M.A.W. (mirrors, scales, hourglasses).
- Places yield **wearable** M.A.W. (mantles stitched from corridor air, veils of well-water).
- Time yields **consumable** M.A.W. (sand, clock-oil, hour-needles).

See `SOMNARAK_MAW_CODEX.md` and `MAW_Codex_Sets/Registry_*` for per-entity Weapon/Suit/Stigma.

---

## V. Authorized Registry

- `Sorrow_Entities/` — 291 dossiers; SECC, Work grids, and per-file Relic flags; indexed by `REFERENCE_SOMNARAK_WIKI/SORROW_ENTITIES_CATALOG.md`.
- `SOMNARAK_ENTITY_CODEX.md` — dossier structure and Relic-specific N/A handling.
- `TEMPLATES/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md` — Two-Work-Type enforcement checklist.

---

## Document Information

**Document ID:** RELIC-01  
**Author:** Archivist, Vault 6 — Relic Registry  
**Classification:** Restricted  
**Cross-References:** `Sorrow_Entities/*`, `SOMNARAK_ENTITY_CODEX.md`, `SOMNARAK_MAW_CODEX.md`, `SOMNARAK_BATTLE_SYSTEM.md`
