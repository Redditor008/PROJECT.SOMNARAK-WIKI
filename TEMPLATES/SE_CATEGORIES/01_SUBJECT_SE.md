# 1. Subject SE — 142 of 301

Back to [README](README.md).

## What it is

A **subject**: a being — person-shaped, creature, or presence — with enough mind and will to respond to how it is treated. It can notice disrespect, return a salute, refuse, test a worker, or choose a target. This is the default, "normal" Sorrow Entity, and it is the only category that can hold relationships with other entities.

## Identifying marks (measured on all 301 dossiers)

- `Entity role` reads **Subject** (plain or with a file-specific qualifier).
- `Entity Type` reads **Subject**, most often "Can breach"; a minority record non-breaching in-place transformation or zone-corruption variants instead — they are still Subject SE.
- **No** `### Tool Use Profile` and **no** `### Log and Method`. Their presence would make it a relic regardless of the role row.
- Almost always carries `### Entity Interaction Record` (or the older `## 상호작용 (Entity Interactions)` heading), `### Escalation Notes`, `### Field Use Record`, `### M.A.W. Use Notes`, and `### Operational Work Notes`.
- Manifestation is one of the `Subject-…` forms (Subject-Body, Subject-Phantasmal, Subject-Lament, Subject-Grudge, Subject-Mind, Subject-Dream, and similar).

## Work rules

**All four Work Types are open in principle** — Flerehan, Pugnahan, Viderehan, Ferrehan — because there is a mind to engage (Flerehan) or confront (Pugnahan). A single dossier may still prohibit or punish one of them on its own record; that is a property of the entity, not of the category. Examples: Drowned Roots prohibits Pugnahan outright; The Wrath Flame lists Pugnahan as valid but records that it feeds the gauge and has never been useful.

## Failure mode

**Breach.** A Subject leaves, transforms, expands, corrupts its zone, or otherwise acts in the world when its gauge or conditions fail. The heading follows what the record shows rather than the category: a Subject that walks out heads `## Breach Behavior` with Breach Type, Movement, Effect, First Target and Escalation; one that widens where it stands heads `## Expansion Behavior`; one that warps its own zone heads `## Containment Event Behavior` with `**Event Type**` — and a Subject whose `**Entity Type**` reads non-breaching carries none of the breach fields. First Target matters here and nowhere else in the same way: a subject can *choose* — whoever showed contempt, whoever is wearing a mask, whoever laughed.

## Document structure / template checklist (measured practice)

Use the shared spine in `TEMPLATES/SE/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md`, then, for a Subject:

- Keep all four rows in the `## Behavior` Work table with real gauge effects; mark a work **Prohibited** in its row instead of deleting it, and repeat the prohibition in `Valid Work Types` and `Recommended response`.
- Write the event section as an acting being: movement, target selection, and the condition that ends it — under the heading that matches the file's own `**Entity Type**`.
- Write `### Entity Interaction Record` only from recorded pairings; "no measured effect" is a valid entry.
- Keep `### Field Use Record` piece-specific (Weapon, Suit, and Stigma tolls are three different records, never one blended toll).
- Do **not** add Tool Use Profile, Log and Method, or relic language ("operator", "unequip", "channel", "discharge"). If those sentences feel necessary, the entity is probably being designed as a relic — stop and reclassify first.

## Examples

- [The Wrath Flame](../../SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIIβ-120_The_Wrath_Flame_분노의_불꽃.md) `O-IIIβ-120`
- [Drowned Roots](../../SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIβ-997_Drowned_Roots_솟구친_나무.md) `C-IIβ-997`
- [Hollow Tree](../../SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVγ-205_Hollow_Tree_빈_나무.md) `C-IVγ-205`

Sources this folder consolidates (nothing here overrides them):

- [SE_DOC_STRUCTURES.md](../../REFERENCE_SOMNARAK_WIKI/GUIDES/SE_DOC_STRUCTURES.md) — the measured five-structure taxonomy.
- [The_REVERIE_DIRECTORATE.md](../../SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_REVERIE_DIRECTORATE.md) — the Relic-Entity System chapter (search "RELIC-ENTITY TOOL CLASSES MATRIX").
- [SOMNARAK_ENTITY_CODEX.md](../../SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_CODEX.md) and [SOMNARAK_MAW_CODEX.md](../../SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md) — the short relic-class tables.
- [01_SORROW_ENTITY_DOSSIER_TEMPLATE.md](../SE/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md) — the single writing scaffold (see the template note in the README of this folder).

## Header law (R-28) — what this category's files may print

Three fields decide everything a reader sees at the top of a dossier, and all three follow the category:

- **`**Entity Type**` states a verdict**, never a description. `Can breach via {Breach / Expansion / Corruption / Possession / Manifestation}` or `Non-breaching: {Activation / Expansion / Containment Event / Formation / Manifestation} only; {the file's own evidence}`. A cell that describes the holding and gives no verdict is invisible to `tools/breach.py`, which counts a file as non-breaching only when the word *breach* is absent.
- **The event heading matches the verdict.** A file that leaves containment and roams heads `## Breach Behavior` and carries the `| **Breach Type** |` row. Every other file heads `## Expansion Behavior` (Expansion Trigger · Rate · Effect · Containment), `## Activation Behavior` (Tool Use Profile), `## Containment Event Behavior` (`**Event Type**`), `## Formation Behavior` or `## Manifestation Behavior` — and carries **no** `Breach Type` row. `tools/section_logic.py` fails the contradiction.
- **The gauge label follows the heading** — `on breach` · `on expansion` · `on formation` · `in the event` · `on activation` — and its figure comes out of the file's own `**Escalation**` row. *Starts at 40%, rises 10%/turn* is retired.

And one more, which no tool checks: **a Combat Record is earned**. Where the holding cannot fight, the section is `## Contact Record` and the file says so in a line before the block; where it keeps its rows, it says why they are kept. R-36 decides: the Movement row is Stationary / Fixed / Motionless / Seated / Recumbent / Rooted or the body says it has never moved; the record says it does not strike; nothing records pursuit, aim or a blow.
