# SE Document Structures — the five distinct shapes an SE dossier takes

**Raised:** 2026-10-08, as an owner correction · **Measured on:** the 301 dossiers at `fb4b8db`
**Method:** read off the files themselves (headings, the `**Entity role**` row, the `### Tool Use Profile — …` heading), not off `TEMPLATES/`.
**Why it is written down:** an SE doc is not one document type. Five structures are in use, they partition all 301 dossiers, and a fix that reads the wrong structure reads the wrong sections.

---

## The correction, verbatim

> *"Wrong The Five SE Docs Is Subject SE, Non-Subject SE, And The Three Relic Type SE That Why I Test You, You Not Even Know That SE Have Five Distinct Structure For It DOCS"*

An earlier answer in chat had named the five structures as the entity dossier plus the four M.A.W. codex documents (`-A__SIDE_CODEX`, `-B__MAW-W`, `-C__MAW-S`, `-D__MAW-G`). That is a count of the archive's `SE-`-prefixed **file families** (1,438 files), and it is a different question. The five **dossier structures** are the ones below.

---

## The five structures

| # | Structure | Files | Identifying sections |
|---|---|---|---|
| 1 | **Subject SE** | 142 / 301 | `**Entity role** | Subject`; no relic triad; `## 상호작용 (Entity Interactions)` or `### Entity Interaction Record`; `### Registry Addendum`, `### Field Use Record`, `### Escalation Notes`, `### M.A.W. Use Notes`, `### Operational Work Notes` |
| 2 | **Non-Subject SE** | 71 / 301 | `**Entity role** | Object/Place` (also `Object`, `Place`, `Time`, `Hazard`); no relic triad; `> **Object/Place Work Rule:**` on 36 of the 71; `### Detailed Activation Record` on 40 of the 71 |
| 3 | **I-Relic SE** — Indumentum | 53 / 301 | the relic triad with `### Tool Use Profile — I-Relic` |
| 4 | **O-Relic SE** — Offertorium | 28 / 301 | the relic triad with `### Tool Use Profile — O-Relic` |
| 5 | **A-Relic SE** — Arcanum | 7 / 301 | the relic triad with `### Tool Use Profile — A-Relic` |

Totals: 142 + 71 + 53 + 28 + 7 = **301 / 301**. Every dossier is in exactly one group.

**The relic triad** is the discriminator, and it is the same three headings in all three relic structures:

```
### Tool Use Profile — {I,O,A}-Relic
### Log and Method
### Detailed Activation Record
```

Measured: `### Tool Use Profile` appears in **88 / 88** relic-class files and in **0 / 213** non-relic files. `### Log and Method` is the same, 88 / 88 against 0 / 213. `### Detailed Activation Record` is looser — it also appears in 40 Non-Subject files and 3 Subject files — so it identifies the triad only together with the other two.

---

## Reading order

1. Look for `### Tool Use Profile — …`. If it is there, the file is a relic structure, and the class letter is the answer: **I**, **O** or **A**.
2. If it is not there, read `**Entity role**` in `## Operational Parameters`. `Subject` → Subject SE. Anything else (`Object/Place`, `Object`, `Place`, `Time`, `Hazard`) → Non-Subject SE.
3. The structure governs, not the role row. Two files say one thing in the role row and are built to another structure, and both are counted by their structure:
   - Devouring Bloom `C-IIIγ-916` — role row `Subject`, built to **O-Relic**.
   - Collapsed Seed `N-IVδ-315` — role row *"Subject, worked throughout under Object/Place rules — it is mobile and it roots, but there is no mind here to engage or confront"*, built to **I-Relic**.

---

## Things the archive says that do not agree with themselves

Recorded, not corrected — a content change is a batch unit, and none of these has been ruled on.

- **The O-Relic expansion is spelled two ways.** `O-Relic (Offertorium)` on 49 lines, `O-Relic (Officium)` on 3 files: Foam Flood `C-IIIγ-948`, Blackened Angel `C-IVγ-946`, Orphaned Bell `C-IVδ-001`.
- **Two files carry the Tool Use Profile heading twice.** Orphaned Bell `C-IVδ-001` has two `### Tool Use Profile — O-Relic`; Driftglass `O-IIIγ-914` has two `### Tool Use Profile — I-Relic`. Audits that key on the heading read the **last** one.
- **`**Tool / M.A.W. grade**` does not always name the relic class.** Sleeping Tree `O-IIIγ-374` is built to I-Relic and its grade row reads `— · —`. The heading is the authority, not the row.

---

## Why this matters to the fix phase

The hardest overlap in the wing sits inside a relic structure, in the triad: **Sleeping Tree `O-IIIγ-374` × Driftglass `O-IIIγ-914`, 0.77, `### Tool Use Profile`** — both I-Relic files, one of which carries the heading twice.

Two consequences for the work:

- A unit on a relic file has three sections that non-relic files do not have, and they are the sections most often shared, because they were generated from one pattern per class. Editing one relic file's `### Log and Method` moves its ties against the other 52, 27 or 6 files of the same class.
- A unit on a Subject or Non-Subject file has no triad at all, so its overlaps live in `### Core Stat Line`, `### Consequences`, `## Operational Parameters` and the M.A.W. cells. Different structure, different queue.
