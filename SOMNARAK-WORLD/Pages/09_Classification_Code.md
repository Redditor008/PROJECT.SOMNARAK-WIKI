# Classification Code — SECC

**Page ID:** `Pages/09_Classification_Code`  
**Archive Path:** `SOMNARAK-WORLD/Pages/09_Classification_Code.md`  
**Parent Archive:** [[SOMNARAK-WORLD](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/tree/arena/01a0b699-project-somnarak-wiki/SOMNARAK-WORLD "SOMNARAK-WORLD")]  
**Backing Codex:** `Sorrow_Entities/README.md` + `Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_CODEX.md`

```text
+========================================================================+
| SECC — SORROW ENTITY CLASSIFICATION                                    |
+------------------------------------------------------------------------+
| Format | SE-[Origin]-[Rank][Potency]-[Number]                          |
| Example | SE-C-IIIβ-014 (City, Fragment, Moderate,                     |
| | 14th City sorrow)                                                    |
| Origins | C City / N Inner / O Outside                                 |
| Ranks I–V | Whisper I → Murmur II → Fragment III →                     |
| | Entity IV → Sovereign V                                              |
| Potencies α–ω | Minor α → Moderate β → Major γ → Critical δ            |
| | → Sovereign ω                                                        |
| Registry Count | 292 dossiers (159 C / 61 O / 72 N)                    |
+========================================================================+
```

## Summary

The **Sorrow Entity Classification Code (SECC)** is the single-line identifier stamped on every dossier. It encodes origin, coherence, potency, and archive number — the analogue of a library call number for grief.

## Description — Code Anatomy

**Format:** `SE-[Origin]-[Coherence][Potency]-[Number] [Element][Manifestation]`

- **Origin (first letter):**
  - `C` — City Sorrow (도한) — Somnarak's walls and institutions (159).
  - `N` — Inner Sorrow (내한) — personal, intimate grief (72).
  - `O` — Outside Sorrow (외한) — Desolate wilds and planetary pressure (61) — includes the single Outside Sovereign `SE-O-Vγ-003` Wilderness Tide.

- **Coherence (Rank I–V):**
  - `I` Whisper (속삭임) — Residue, trace self — 46 dossiers.
  - `II` Murmur (웅얼거림) — Echo, repeating pattern — 70.
  - `III` Fragment (파편) — Personality shaped by origin — 82.
  - `IV` Entity (존재) — Self-aware, can communicate — 79.
  - `V` Sovereign (군주) — City-scale, near-mythic — 10 + 5 other.

- **Potency (α–ω):** Minor α → Moderate β → Major γ → Critical δ → Sovereign ω — maps to M.A.W. grade.

- **Number:** Archive sequence (e.g., `014` → The Debt Eater). Unique per Origin block.

- **Trailing:** `[Element][Manifestation]` — e.g., `[VS]` Void + Subject-Body — documented per dossier header.

## Information — The Registry

All 292 codes are listed in `Sorrow_Entities/README.md` with SECC, Korean name, threat tier, and element affinity. `SOMNARAK_ENTITY_CODEX.md` §SECC details the five dimensions; `TEMPLATES/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md` enforces the format.

Distribution is not uniform — see `CANONICAL_METRICS.json`:

- Sovereigns: 10 (13 City-origin per `PROJECT_SOMNARAK.md` archival note, 1 Outside, 0 Inner — personal trauma cannot reach Sovereign without collectivizing into City Sorrow).
- Relic flag: 88 dossiers include Object/Place/Time manifestation (see `Pages/08_Relic_Entities.md`).

## Operational Notes

- **SECC ≠ Risk:** SECC encodes origin/coherence/potency/number; threat element and Work affinity are separate axes.
- **Reading path:** Origin tells *where* the sorrow formed, Rank tells *how complete* the self is, Potency tells *how strongly* it pressures, Number tells *when* it was archived.
- **Template enforcement:** Every new dossier must pass `TEMPLATES/01` and `23_CANONICAL_NAMING_AND_BANNED_STRINGS_TEMPLATE.md` checks.

## Related Pages

- `02_Behavior.md` — Work affinity by Rank/Element.
- `08_Relic_Entities.md` — manifestation triad and Two-Work-Type rule.
- `Sorrow_Entities/SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.md` — live example: `C-IIIβ-014 [VS]`.

---
*Backing is a real catalog — 292 dossiers; no Pages-only invention.*
