# 3. I-Relic SE — Indumentum (장착형 유물 개체), 53 of 301

Back to [README](README.md). Relic classes compared in the [README table](README.md#the-five-categories).

## What it is

A relic-entity used by **wearing, holding, or mounting** it. *Indumentum* is Latin for a garment or covering, and the class behaves like one: nothing happens until the operator physically takes it up, and it stays active for exactly as long as it remains attached to them.

## Identifying marks (measured on all 301 dossiers)

- The relic triad is present, with the heading **`### Tool Use Profile — I-Relic`**, followed by `### Log and Method` and `### Detailed Activation Record`.
- Inside the profile: **Use Mode** reads "Equippable / mounting use"; **Duration** is phrased as "until removed / until the hand is lifted / while worn"; **Termination / Return** describes a deliberate unequip or detachment protocol.
- `Entity role` is usually Object/Place, but the triad decides, not the row: Collapsed Seed `N-IVδ-315` is an I-Relic even though its role row begins "Subject, worked throughout under Object/Place rules…".

## How it is used (the class rules)

- **Activation is contact plus taking-up:** a hand placed on the dish, a mask put on, chains allowed to wrap the bearer.
- **It does not release on its own.** The operator must meet the file's criteria and manually unequip it. Premature return, or exceeding the threshold, leaves the measured effect behind in the operator after the instrument itself has reset — that leftover is the class's signature risk.
- **Canonical examples named by the Directorate:** The Debt Scale (a hand on one dish; the measured burden remains emotionally after release), The Cracked Hourglass (touch slows local time; the operator's lifespan shortens per use), The Dancing Chains, The Happy Mask, The First Tear.

## Rules shared by all three relic classes

- **Work:** Viderehan and Ferrehan only. Flerehan and Pugnahan are **prohibited** (an inert tool cannot be wept with or fought).
- **Failure:** no walking breach. Failure is a **threshold activation / activation cascade** — the effect escapes its intended scope, forces obsessive use, or feeds the facility's counters.
- **The toll is the piece's own.** Cost is the ability read backwards, per piece, and it appears in exactly one file archive-wide. The four retired stigma sentences (*moves a little slower*, *temper shortens*, *weeps in their sleep*, *forgets a word*) and the six retired weapon sentences (*headache*, *numbness toward the element*, *hand fatigue*, *progressively heavier*, *unwept grief*, *memory fragmentation*) are defects, not defaults. `**Cost:**` is the Echo price; `**Bearer cost:**` is what the operator pays.
- **The original never leaves:** the relic itself stays in containment permanently. M.A.W. pieces are archetype derivations, distinct objects; "using the relic" in a Tool Use Profile always means an authorised in-chamber operative session, never taking it into the field.
- **Containment is not replaced by use:** a relic session never substitutes for a scheduled Work cycle, and several dossiers state this in their Operational Rule paragraph.

## Document structure / template checklist (measured practice)

Start from the shared spine in `TEMPLATES/SE/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md` (which contains no relic scaffold), then add the triad in this order:

1. `### Tool Use Profile — I-Relic` with the fixed fields: Tool Class, Use Mode (`Equippable / mounting use`), Activation, Primary Effect, Duration, Termination / Return, Risk — followed by an **Operational Rule** paragraph (who may equip it, the detachment protocol, and the statement that a session never replaces scheduled Work).
2. `### Log and Method` — how sessions are witnessed, baselined, and entered, and who may call the stop (never the wearer alone where the toll hides from its bearer).
3. `### Detailed Activation Record` — the observed activation history in the file's own numbers.

Keep `Valid Work Types` at **Viderehan and Ferrehan**, and write Movement as the object's own stillness or creep — an I-Relic is carried; it does not prowl. If Activation starts to require sustained concentration rather than attachment, you are designing an O-Relic; if one use consumes it, an A-Relic.

## Examples

- [The Debt Scale](../../SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIβ-015_The_Debt_Scale_빚의_저울.md) `C-IIIβ-015`
- [The Cracked Hourglass](../../SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIβ-036_The_Cracked_Hourglass_금이_간_모래시계.md) `C-IIIβ-036`
- [The Dancing Chains](../../SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-102_The_Dancing_Chains_춤추는_사슬.md) `C-IIIγ-102`
- [The Happy Mask](../../SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIβ-051_The_Happy_Mask_행복한_가면.md) `C-IIβ-051`

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
