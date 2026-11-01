# 4. O-Relic SE — Offertorium (집중형/채널형 유물 개체), 28 of 301

Back to [README](README.md). Relic classes compared in the [README table](README.md#the-five-categories).

## What it is

A relic-entity used by **channeling**: the operator opens and holds a continuous connection to it — unbroken touch, steady gaze, or spoken invocation — and the effect persists only while that channel stays open. Let go of the channel and the effect ends; abandon it carelessly and the effect ends badly.

**Spelling note:** the class name is `Offertorium` almost everywhere. Three files write `Officium` (Foam Flood `C-IIIγ-948`, Blackened Angel `C-IVγ-946`, Orphaned Bell `C-IVδ-001`). Both spellings name this same class; the split is recorded in [SE_DOC_STRUCTURES.md](../../REFERENCE_SOMNARAK_WIKI/GUIDES/SE_DOC_STRUCTURES.md) and has not been ruled on.

## Identifying marks (measured on all 301 dossiers)

- The relic triad is present, with the heading **`### Tool Use Profile — O-Relic`**, followed by `### Log and Method` and `### Detailed Activation Record`. (Orphaned Bell `C-IVδ-001` prints the heading twice; audits read the last.)
- Inside the profile: **Use Mode** reads "Continuous / channeled use"; **Duration** is phrased as "until the source is acknowledged / until the channel is closed"; **Termination / Return** describes deliberately closing the channel and putting the instrument away in order.
- The triad decides the class even when other rows disagree: Devouring Bloom `C-IIIγ-916` carries `Entity role: Subject` and is nevertheless built, and counted, as an O-Relic.

## How it is used (the class rules)

- **Activation is opening a channel:** hold the instrument and name the lost thing; meet the mirror's gaze; whisper the wish and keep whispering it correctly.
- **It answers only while the channel is sustained.** Concentration, a second person in a defined supporting role (a case-holder who is not the channeller, a named witness), and hard time limits are typical controls.
- **Closure is a formal act, not an interruption.** If a channel is abandoned mid-use without proper closure, the residue compounds into the surroundings — several dossiers record exactly one such accident and built their rule on it.
- **Canonical examples named by the Directorate:** The Echo Compass (points to the nearest sorrow source; nothing in it ever says stop), The Mirror of Sorrows, The Memory Lock, The Blackened Angel, The Final Door.

## Rules shared by all three relic classes

- **Work:** Viderehan and Ferrehan only. Flerehan and Pugnahan are **prohibited** (an inert tool cannot be wept with or fought).
- **Failure:** no walking breach. Failure is a **threshold activation / activation cascade** — the effect escapes its intended scope, forces obsessive use, or feeds the facility's counters.
- **The toll is the piece's own.** Cost is the ability read backwards, per piece, and it appears in exactly one file archive-wide. The four retired stigma sentences (*moves a little slower*, *temper shortens*, *weeps in their sleep*, *forgets a word*) and the six retired weapon sentences (*headache*, *numbness toward the element*, *hand fatigue*, *progressively heavier*, *unwept grief*, *memory fragmentation*) are defects, not defaults. `**Cost:**` is the Echo price; `**Bearer cost:**` is what the operator pays.
- **The original never leaves:** the relic itself stays in containment permanently. M.A.W. pieces are archetype derivations, distinct objects; "using the relic" in a Tool Use Profile always means an authorised in-chamber operative session, never taking it into the field.
- **Containment is not replaced by use:** a relic session never substitutes for a scheduled Work cycle, and several dossiers state this in their Operational Rule paragraph.

## Document structure / template checklist (measured practice)

Start from the shared spine in `TEMPLATES/SE/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md` (which contains no relic scaffold), then add the triad in this order:

1. `### Tool Use Profile — O-Relic` with the fixed fields: Tool Class, Use Mode (`Continuous / channeled use`), Activation, Primary Effect, Duration, Termination / Return, Risk — followed by an **Operational Rule** paragraph (channel discipline, the second person's role, the time limit, formal closure, and the statement that channeling never replaces scheduled Work).
2. `### Log and Method` — who opens, who witnesses, who may order closure, and how an abandoned channel is recognised after the fact.
3. `### Detailed Activation Record` — the observed activation history in the file's own numbers.

Keep `Valid Work Types` at **Viderehan and Ferrehan**. If the effect would keep running unattended after the operator lets go, it is not channeled — reconsider I-Relic (attachment) or A-Relic (discharge). If the instrument is simply worn, it is an I-Relic even if the prose calls wearing it "sustained".

## Examples

- [The Echo Compass](../../SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIβ-016_The_Echo_Compass_메아리_나침반.md) `C-IIIβ-016`
- [Learned Your Face](../../SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-195_Learned_Your_Face_슬픔의_거울.md) `C-IIIγ-195`
- [Memory Lock](../../SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-300_Memory_Lock_기억의_자물쇠.md) `C-IIIγ-300`
- [Blackened Angel](../../SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVγ-946_Blackened_Angel_검어진_천사.md) `C-IVγ-946`

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
