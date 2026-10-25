# SE Categories — the five kinds of Sorrow Entity dossier, in one folder

**Created:** 2026-10-25, at the owner's request, because this explanation previously lived only in scattered places and in no root file.
**Measured on:** all 301 dossiers at commit `117ec18`. Counts re-verified on the day of writing.
**Status of this folder:** a reading guide. It explains and links; it does not change any dossier, rule, or canon fact. Where this folder and a dossier disagree, the dossier and the sources below govern.

## The five categories

| # | Category | Count | One-line meaning | Detail file |
|---|---|---:|---|---|
| 1 | **Subject SE** | 142 / 301 | A being with a mind that can be engaged or confronted | [01_SUBJECT_SE.md](01_SUBJECT_SE.md) |
| 2 | **Non-Subject SE** | 71 / 301 | An object, place, time, or hazard — sorrow with no mind in it | [02_NON_SUBJECT_SE.md](02_NON_SUBJECT_SE.md) |
| 3 | **I-Relic SE — Indumentum** | 53 / 301 | A tool-entity the operator wears or holds | [03_I_RELIC_SE_INDUMENTUM.md](03_I_RELIC_SE_INDUMENTUM.md) |
| 4 | **O-Relic SE — Offertorium** | 28 / 301 | A tool-entity the operator channels continuously | [04_O_RELIC_SE_OFFERTORIUM.md](04_O_RELIC_SE_OFFERTORIUM.md) |
| 5 | **A-Relic SE — Arcanum** | 7 / 301 | A tool-entity that is spent in a single discharge | [05_A_RELIC_SE_ARCANUM.md](05_A_RELIC_SE_ARCANUM.md) |

142 + 71 + 53 + 28 + 7 = **301 / 301**. Every dossier belongs to exactly one category. The first two are the "normal" SEs (213 files). The three relics (88 files) are SEs the facility also keeps and uses as operational tools.

## How to tell which category a dossier is (ten seconds)

1. **Search the file for `### Tool Use Profile —`.** If it is there, the dossier is a **relic**, and the letter after the dash is its class: I, O, or A. This heading, together with `### Log and Method`, appears in 88 of 88 relic files and in 0 of 213 non-relic files.
2. **If it is not there, read the `Entity role` row** in `## Operational Parameters`. `Subject` means **Subject SE**. Anything else (`Object/Place`, `Object`, `Place`, `Time`, `Hazard`) means **Non-Subject SE**.
3. **Structure beats the role row.** Two dossiers say one thing in the role row and are built to another structure, and both are counted by their structure: Devouring Bloom `C-IIIγ-916` (role says Subject, built O-Relic) and Collapsed Seed `N-IVδ-315` (role says Subject worked under Object/Place rules, built I-Relic). The `Tool / M.A.W. grade` row can also be blank on a relic (Sleeping Tree `O-IIIγ-374` reads `— · —`); the heading is the authority.

## The biggest practical difference: which Work Types are allowed

The four Work Types are **Flerehan** (Tears — emotional engagement), **Pugnahan** (Confrontation — direct challenge), **Viderehan** (Observation — witnessing and recording), and **Ferrehan** (Endurance — bearing the presence).

| Category | Flerehan | Pugnahan | Viderehan | Ferrehan | Why |
|---|---|---|---|---|---|
| Subject SE | open | open | open | open | There is a mind to engage or confront (a single file may still prohibit one) |
| Non-Subject SE | N/A | N/A | open | open | The two-Work-Type rule: you cannot weep with or fight an object, place, time, or hazard |
| I-Relic SE | prohibited | prohibited | open | open | Relic protocol: inert tools are observed and endured, never fought or wept with |
| O-Relic SE | prohibited | prohibited | open | open | Same relic protocol |
| A-Relic SE | prohibited | prohibited | open | open | Same relic protocol |

## What the category is NOT

- **Not the designation letters.** In `O-IIIβ-120`, the first letter is the sorrow origin (C / N / O), not a relic class. The Wrath Flame `O-IIIβ-120` is a plain Subject SE.
- **Not Manifestation.** Manifestation (Subject-Body, Subject-Phantasmal, Object-Weight, Place-Lament, Time-…, and similar) describes the form the sorrow takes. It correlates with category but does not decide it.
- **Not Coherence (I–V), Potency (α–ω), or Element (Lament / Grudge / Void / Weight).** Those are separate axes on every dossier.
- **Not the M.A.W. codex file family** (`-A` Side Codex, `-B` Weapon, `-C` Suit, `-D` Stigma). Those are companion documents, not SE categories.
- **Not enemy disposition** (Positive / Neutral / Negative). That judgment lives in the disposition index and is independent of structure.

## The template note (read before writing a new dossier)

There is exactly **one** writing scaffold: `TEMPLATES/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md`. It lays out the shared spine every dossier uses — SECC Classification, Operational Parameters, Combat Record, Appearance, Origin, Behavior, Breach Behavior, Observation Log, Story Log, Final Observation, and the rest — and it encodes only one category rule: Subject may use all four Work Types; Object / Place / Time use only Viderehan + Ferrehan. It does **not** contain the relic triad scaffold and does not name the five structures. The per-category files in this folder therefore include a "document structure / template checklist" measured from the 301 existing dossiers: which sections a category always has, which it never has, and which rows change meaning. Treat those checklists as measured practice, not as a sixth template.

## Known inconsistencies in the archive (recorded, not corrected here)

- **O-Relic is spelled two ways:** `Offertorium` almost everywhere, `Officium` in Foam Flood `C-IIIγ-948`, Blackened Angel `C-IVγ-946`, and Orphaned Bell `C-IVδ-001`.
- **Two files print the Tool Use Profile heading twice:** Orphaned Bell `C-IVδ-001` (O-Relic twice) and Driftglass `O-IIIγ-914` (I-Relic twice). Audits read the last one.
- **One comparison codex swaps the I/O glosses** (`06…COMPLETE_SYSTEM_COMPARISON…` calls O-Relics wearable and I-Relics stationary). The Directorate chapter, the Entity Codex, the M.A.W. Codex, and all 88 relic dossiers agree the other way: I = equippable, O = channeled.
- **`Detailed Activation Record` alone does not prove a relic:** it also appears in 40 Non-Subject files and 3 Subject files. It identifies a relic only together with Tool Use Profile and Log and Method.

Sources this folder consolidates (nothing here overrides them):

- [SE_DOC_STRUCTURES.md](../REFERENCE_SOMNARAK_WIKI/SE_DOC_STRUCTURES.md) — the measured five-structure taxonomy.
- [The_REVERIE_DIRECTORATE.md](../SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_REVERIE_DIRECTORATE.md) — the Relic-Entity System chapter (search "RELIC-ENTITY TOOL CLASSES MATRIX").
- [SOMNARAK_ENTITY_CODEX.md](../SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_CODEX.md) and [SOMNARAK_MAW_CODEX.md](../SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md) — the short relic-class tables.
- [01_SORROW_ENTITY_DOSSIER_TEMPLATE.md](../TEMPLATES/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md) — the single writing scaffold (see the template note in the README of this folder).

**Re-measure it yourself:** `grep -h "^### Tool Use Profile" SOMNARAK-WORLD/Sorrow_Entities/SE-*.md | sort | uniq -c` (plus the dossiers outside that folder) reproduces the relic counts; the `Entity role` row splits the rest.
