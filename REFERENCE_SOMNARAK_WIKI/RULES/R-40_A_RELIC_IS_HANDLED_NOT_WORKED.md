# R-40 — A Relic Is Handled, Not Worked

**The owner's instruction, verbatim (2026-11-03):**

> *"THIS IS NEW RULE NO RELIC SE WILL HAVE WORK TYPE INSTEAD HAVE HANDLING PROCESS THAT MEAN YOU NEED TO UPDATE P.S.md, R.D.md And Everything Else That Mentions SE So It Will Match With Our Current SE 'TEMPLATE'."*

## The rule

**A relic has no Work Types.** Viderehan, Ferrehan, Flerehan and Pugnahan are the four ways a *subject* is worked — approached, wept with, borne, confronted. A relic cannot be worked: there is nothing in it to observe into agreement, nothing to weep with, nothing that answers a challenge. It is **approached, handled and left**, and what the file owes the reader is the procedure.

So the dossier shape splits at `Entity Type`:

| Entity Type | The mechanical section | What it answers |
|---|---|---|
| **Subject** | `## Behavior` — four rows | which of the four works, and what it costs |
| **Relic** | `## Handling Process` | what is done, in what order, and what it costs |

The `**Valid Work Types**` row in the Core Stat Line becomes **`**Handling**`** on a relic, pointing at the section. It does not list two work types, because there are none to list.

## Why the old rule is retired

The Two-Work-Type Rule said a relic permits Viderehan and Ferrehan only, and every relic dossier carried four Work Type rows with two of them marked `N/A`. Measured 2026-11-03: **117 of 141 relic dossiers carried the identical vector `N/A : N/A : Stable : Decrease`**, and the other 24 carried three vectors between them. The two live rows were not describing the holding; they were a form with two blanks filled in.

Batch 154 measured the same collapse in the subjects — the element decided nothing — and the fix there was to make the response follow the Element row. For relics the fix is stronger: **there is no response to model.**

Nothing in the old shape is deleted from the record. The `Handling` row of the Contact Record, the `**Recommended response**` row, the Operational Notes and the `**Resolution Condition**` already carried the procedure in every relic file; the new section gathers it into one place and states the stages the prose was already describing.

## The section

```text
## Handling Process

> **This holding is not worked.** {one line saying what it is instead —
> a thing approached, a ground walked, a tool carried — in this file's own terms.}
```

| Stage | What is done | Who holds it | What it costs |
|---|---|---|---|
| **Approach** | posting, distance, covering, instrument | post, rank, count | time, exposure, an instrument |
| **Handling** | the act: touched, read, moved | certified holder, condition | the interval, the reading, fatigue |
| **Withdrawal** | order of leaving, sealing, log | whoever confirms | what is carried out, what is left |
| **Refusal** | the thing never done here | who may authorise: nobody | what happened last time it was tried |

**The four stages are the minimum, not a form.** A file that genuinely has five states writes five rows; a file where withdrawal and refusal are one act writes three and says so. What may not happen is a row that states a general truth: *"handle with care"* is not a stage.

**The Refusal row is where the horror is.** Every relic in this archive is a thing somebody has already done the wrong thing to. Name the wrong thing and the record that set the rule — the batch that rewrote a procedure into a Work Type table was the one that lost it.

## What replaces what

| Old | New |
|---|---|
| `## Behavior` on a relic | `## Handling Process` |
| four Work Type rows | four Handling stages |
| `**Valid Work Types**` | `**Handling**` |
| `Flerehan / Pugnahan -> N/A` | gone: no Work Type is offered to refuse |
| `Viderehan and Ferrehan only` | the two stages that do the work, named |

`tools/auditors/check_relic_work_types.py` (gate line 80) fails any non-subject dossier that still carries a Work Type table or a `**Valid Work Types**` row. Ratchet **131**, decremented as files are converted; it began at 143 and stood at 138 before batch 192.

## What this does to the other documents

The rule reaches every place that describes what an SE is worked with:

- **`PROJECT_SOMNARAK.md` (P.S.)** — the Work Type section and the Effectiveness matrix now govern **subjects only**, and say so.
- **`The_REVERIE_DIRECTORATE.md` (R.D.)** — the energy paragraphs that send a post to work a relic now send it to handle one.
- **`TEMPLATES/SE/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md`** and the five category templates — the Behavior block is conditional on `Entity Type`.
- **`Pages/07-Sorrow Entities`, `37-Relic Entities`, `08-Sorrow List`** — the Two-Work-Type Rule is replaced by this one.
- **`SOMNARAK_RELIC_ENTITIES.md`**, the `Handling` metric in `CANONICAL_METRICS`, and `finishedness`/`wikistd`, whose section lists now accept `## Handling Process`.

A rule that lives in one dossier template and nowhere else is a suggestion. This one is written into every document that tells somebody how to open the box.
