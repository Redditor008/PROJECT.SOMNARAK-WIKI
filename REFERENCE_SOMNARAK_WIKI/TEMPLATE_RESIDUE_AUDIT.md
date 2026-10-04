# Template Residue Audit — the part of the dossier Workstream 1 could not see

**Raised:** 2026-10-04 · **Rule:** [`R-23`](RULES/R-23_LABELS_MAY_REPEAT_VALUES_MAY_NOT.md)
**Tool:** `/home/user/wikitools/tpl.py` · **Scope:** all 303 catalogued dossiers (both wings)

---

## Why this audit exists

The owner's observation, verbatim: *"Some From What You Explain Is Still Templatey Because Of
The Previous AI"* — made after Workstream 1 reported a headline of `0.00%`.

Both statements are true at once, and the reason is a scope boundary rather than a mistake in
the count.

`tools/boilerplate_report.py` measures the `body` scope:

```python
body = lambda s: len(s) > 40 and not s.startswith(('|', '#', '>', '`'))
```

A line that begins with a pipe is a table row, and **no table row was ever counted**. The same
goes for blockquotes and headings. Workstream 1 drove shared *paragraph prose* at a thirty-
dossier threshold from 34.3% to 0.00% across 291 files, and that result stands. It simply never
looked inside the tables, which is where this archive keeps most of its operative text.

## The measurement

Residue = a line shared by **≥ 10 dossiers**, carrying **≥ 10 words** of content, that is **not**
sanctioned furniture. The sanctioned list lives in `tpl.py` and covers table headers and
separators, the five system blockquotes (R.D. Operational Record, R.D. Field Parameters,
Mechanics Reference, M.A.W. definition, Object/Place Work Rule), the rows whose value is forced
by the SECC code or by the entity's role, and the two global combat rules.

```
dossiers                      303
distinct residue lines        146  (shared by >= 10 dossiers)
residue instances            3745
dossiers carrying residue     292 / 303
clean dossiers                 11
median residue per dossier     13
```

**Counter: 11 / 303 dossiers free of template residue.**

Threshold ten, not thirty, because this defect clusters by *role* rather than across the whole
archive. Six Object/Place dossiers sharing one word-identical breach block is the defect at its
normal size, and a thirty-dossier threshold scores that as zero.

## The eleven clean dossiers

`Soot_Fry` · `Blessing_Giver` · `Apostle_Maker` · `Dawn_of_Mourning (C-Vω-002)` ·
`Wilderness_Tide` · `The_Music_Box_of_Agony` · `The_Unbroken_Pledge` · `The_Ancestral_Guilt` ·
`The_Glass_Silt_Drifter` · `The_Singing_Needle` · `Book_of_Regressor_Log_Dramaturgy`

They matter because they prove the target is reachable inside the existing format. None of them
dropped a section to get there.

## The worst twelve

| Residue lines | Dossier |
|---|---|
| 31 | `SE-N-Iα-686` Torn Window |
| 29 | `SE-O-IIIγ-233` Forgotten Soul |
| 29 | `SE-O-IIβ-119` Homeless Sorrow |
| 29 | `SE-O-Iα-453` Floating Fragment |
| 28 | `SE-N-IVδ-606` Banyan |
| 27 | `SE-C-Vδ-111` The Final Door |
| 27 | `SE-N-IVδ-339` Breach |
| 27 | `SE-O-IIβ-378` Drowned Echo |
| 27 | `SE-O-IIβ-922` Door to Nowhere |
| 26 | `SE-N-IIIβ-200` Chain of Memories |
| 26 | `SE-O-IIIγ-915` Corrosion Dream |
| 23 | `SE-C-IVγ-176` Loom of Unlived Dreams |

## The ten heaviest residue lines

| Dossiers | Line |
|---|---|
| 207 | `| **After use** | Removal or discharge, injuries, lingering effects, cooldown, repair need, reuse authorization. |` |
| 206 | `| **During use** | Activation time, visual feedback, effect strength, target or protected area, first cost. |` |
| 206 | `| **At limit** | Duration, activations, attribute changes, rejection signs, and source behavior. |` |
| 178 | `| Endure it — bear the weight without flinching. | Struggle free — try to throw it off. |` |
| 99 | `| **Recommended response** | Reduce Gauge through the listed valid Work Types; Object/Place entities use Viderehan and Ferrehan only. |` |
| 96 | `| Weep with it — share the sorrow aloud. | Hold your composure — refuse to feel it. |` |
| 61 | `| **Distinctive markers** | Confirm the primary form and elemental signature before contact. |` |
| 60 | `| **Activation or escalation** | The team records the first visible activation, breach, or expansion change … |` |
| 48 | `| **First Target** | The nearest personnel or the one whose sorrow matches the entity's origin. |` |
| 47 | `| **Position / movement** | The subject manifests independently within the registered area; posture and distance must be recorded. |` |

Read them together and the diagnosis is unambiguous. Four of the ten are the authoring
template's **own field list**, published as content — the previous AI filled the entity's name
into the furniture and left the instructions where the values belonged. Two are a binary choice
offered to the reader in words that have nothing to do with the entity in front of them. One,
`**First Target**`, is an *operative* value shared by 48 unrelated entities, and it is the single
line most responsible for Workstream 5's pending pool.

## Re-research: how the reference wikis draw the same line

Re-checked 2026-10-04 against `lobotomycorporation.wiki.gg/wiki/Nothing_There`,
`lobotomycorporationmodded.wiki.gg/wiki/Template:AbnormalityPage`, and
`lobotomycorp.fandom.com/wiki/Example_Page`.

The published page and the template page of the same wiki share **all** their furniture: the
infobox, the section order (Appearance → Ability → Details → E.G.O. → Story → Flavor Text →
Trivia), the work-favour grid, the observation-level list. Nothing about repetition at that
level is a defect; it is the format working.

What separates them is the values:

| | Template page | Published page |
|---|---|---|
| Ability | *"Placeholder for Ability Description"* | *"Decrease by 1 when an employee completes the work with Justice Level 3 or lower. This takes priority over its other mechanics."* |
| Work favour | `"Chance" (%)` in every cell | measured percentages per work and level |
| Escape info | `0 Immune` in every damage type | the entity's actual resistances |
| Story | empty observation levels | distinct in-world text per level |

Our dossiers inherited the furniture correctly, and in roughly 3,700 places they published the
placeholder with it. Where a value is genuinely unknown, the convention on those wikis is a
redaction — `███████`, `<name>` — never a field list and never a trailing instruction.

## What this is not

- **Workstream 1 is not reopened and its counter is not revised.** `291 / 291`, `0.00%`, census
  `[(0, 291)]` remain exactly true of shared body prose at thirty dossiers. This is a different
  measurement of a different region, with its own tool and its own denominator (`R-20`).
- **This is not a formatting complaint.** A dossier is not improved by deleting the `**After
  use**` row. It is improved by that row saying what happens after *this* entity's M.A.W. is
  used. Fixes are growth, as in Workstream 1 (`R-15`).
- **This is not optional for Workstream 5.** The 48 pending dispositions are pending because
  their operative cells are stock. Classifying them requires authoring first; reading harder
  will never produce an answer that the file does not contain.

## Order of work

1. **Operative values first** — `**First Target**`, breach `**Movement**` / `**Effect**`,
   interaction effect cells. These are the ones that block Workstream 5 and the ones a reader
   would call wrong rather than thin.
2. **Placeholder-instruction cells** — the `**Before/During/After use**` and `**At limit**`
   family, `**Distinctive markers**`, `**Position / movement**`, `**Material / signature**`.
   Highest instance count, most mechanical to fix, lowest risk.
3. **Reader-facing binary choices** — the `Endure it … / Struggle free …` pair and its siblings,
   which should name what *this* entity makes a person want to do.
4. **Slot-filled Origin prose** — the *"Space was the vessel; spirit was the content"* paragraph
   shape in the thin files. Lowest instance count, highest authoring cost, done entity by entity
   alongside its disposition.

Progress is reported as `clean / 303` under `R-16` and `R-20`, re-measured by `tpl.py` each
time, never incremented by hand.
