# 2. Non-Subject SE — 71 of 301

Back to [README](README.md).

## What it is

Sorrow with **no subject in it**: an **object, a place, a time, or a hazard** that a sorrow has soaked into or that a sorrow simply is. A border that surges, a market stair, an hour that runs backward, a tree with nobody home. It can be dangerous, responsive to conditions, and fully documented — but there is no mind to persuade, enrage, salute, or forgive.

## Identifying marks (measured on all 301 dossiers)

- `Entity role` reads **Object/Place** (the large majority), or `Object`, `Place`, `Time`, or `Hazard`.
- `Entity Type` reads one of those same words, typically "Can breach via Transform" or a non-breaching "manifestation in place; activates on …" formula.
- **No** `### Tool Use Profile` and **no** `### Log and Method` — this absence, together with the role row, is what separates a Non-Subject from a relic.
- Many print the banner `> **Object/Place Work Rule:** …` inside the dossier (36 of the 71 at the structural measurement), and 40 of the 71 carry a `### Detailed Activation Record`.
- Manifestation is one of the non-subject forms (Place-…, Object-…, Time-…, Hazard-…).

## Work rules — the two-Work-Type rule

Only **Viderehan (Observation)** and **Ferrehan (Endurance)** are valid. **Flerehan is N/A** (emotional engagement needs somebody to engage) and **Pugnahan is N/A** (confrontation needs somebody to confront). This is a hard archive rule, enforced in the template and tracked as its own compliance metric. In the `## Behavior` table the Flerehan and Pugnahan rows are still printed (the table shape is shared), but they record N/A / no effect rather than a response, and `Valid Work Types` names only the two permitted works.

## Failure mode

Not an escape by a being. A Non-Subject **transforms, expands, spreads, or activates in place**: a boundary moves, an hour lengthens, a room gains a door, pressure becomes physical where it already stood. A Non-Subject dossier **does not head `## Breach Behavior`** and does not carry a `| **Breach Type** |` row: it heads the section by what actually happens — `## Expansion Behavior`, `## Activation Behavior`, `## Containment Event Behavior`, `## Formation Behavior` or `## Manifestation Behavior` — and reads "First Target" as a *condition that selects* (a covered face, a spoken name, a person standing in the flow), never as a choice, because there is no chooser. `tools/section_logic.py` fails the contradiction, and the nine cells the archive had to re-type were all in this category.

## Document structure / template checklist (measured practice)

Use the shared spine in `TEMPLATES/SE/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md`, then, for a Non-Subject:

- Set `Entity role` and `Handling` consistently: role Object/Place (or Object / Place / Time / Hazard); **no Work Types at all** (`R-40`); the section is `## Handling Process` with Approach, Handling, Withdrawal and Refusal. Files still carrying the old `Object/Place Work Rule` banner and a two-work table are being converted under batch 155 onward — the banner is retired, not rewritten.
- Give the activation a *condition*, not a motive ("activates on new debt", "on direct gaze", "on none — continuous"). If you catch yourself writing what it wants, hates, or decides, the design has drifted into Subject.
- Movement fields describe creep, spread, surge, recurrence, or relocation of the phenomenon — never a creature gait list.
- `### Detailed Activation Record` is welcome here; it does not make the file a relic. What would make it a relic is adding Tool Use Profile + Log and Method and an operator who *uses* it — see the relic files before doing that deliberately.
- Interaction records are thinner by nature: record measured co-presence effects and null results; do not invent alliances for a place.

## Examples

- [Wilderness Tide](../../SOMNARAK-WORLD/Sorrow_Entities/SE-O-Vγ-003_Wilderness_Tide_야생의_조수.md) `O-Vγ-003`
- [Weeping Willow](../../SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-140_Weeping_Willow_우는_버드나무.md) `C-IIIγ-140`
- [Backward Hour](../../SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-913_Backward_Hour_카운트다운_시계.md) `C-IIIγ-913`

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
