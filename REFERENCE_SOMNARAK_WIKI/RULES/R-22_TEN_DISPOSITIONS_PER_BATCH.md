# R-22 — Ten Dispositions Per Batch, Each Batch Done Right

**Status:** standing
**Raised:** 2026-10-04, by the archive owner
**Binds:** Workstream 5 (Entity Disposition Index)
**Interacts with:** `R-18` (batch-short versus careful-detail), `R-19` (disposition classes),
`R-20` (one fixed denominator), `R-21` (five whole-file cleans per prompt)

---

## The instruction

Verbatim: *"After We Done Clean Can The Disposition Batch Done In 10 File Per Batch And For The
Disposition You Need To Done It Right Per Batch"*.

Two things are being asked for, and they are separate.

1. **Size.** Once Workstream 1 is finished, the remaining disposition work runs in batches of
   **ten entities per prompt**, not one and not five.
2. **Quality.** Each batch is to be *finished* — correct, evidenced, and gated — before the next
   one starts. A batch is not a list of ten guesses to be tidied later.

---

## When this rule starts

`R-22` governs Workstream 5 **after Workstream 1 closes at `291 / 291`**. Until then, disposition
rows continue to be written one at a time, in the same commit as the clean that evidences them,
exactly as `R-19` requires. Nothing in this rule authorises classifying an entity ahead of its
clean.

## What a batch of ten means

- **Ten entities per prompt.** If ten cannot honestly be evidenced, ship the number that can and
  say which ones were held and why. The same discipline `R-21` applies to cleans applies here:
  a short batch is reported as short, never padded.
- **One commit per entity**, not one commit per batch. Ten entities means ten commits and ten
  passes of the gate chain. This mirrors `R-21` and exists for the same reason: a single batch
  commit hides which row broke the parity check.
- **The split is stated first.** Before any classifying starts, the ten are divided under `R-18`
  into batch-short and careful-detail, with counts, and the two halves are reported separately
  afterwards.

## What "done right" means, per entity

A row is finished only when all six hold:

1. **The class is one of the three in `R-19`** — Positive, Neutral, or Negative — on the owner's
   definitions, not on a general impression of the entity.
2. **The evidence is quoted from the entity's own dossier**, inside the row, in quotation marks.
   No paraphrase. No reasoning that the file does not support.
3. **A conditional is written as conditional.** If the effect needs a trio, a co-presence, or a
   particular Work Type, the row says so in the row.
4. **A null is evidence.** Where a file records pairings that did nothing, quote them. A Neutral
   row built from quoted null results is stronger than one built from silence.
5. **Nothing is defaulted.** An entity with no disposition-bearing line stays **pending**. A blank
   is not a finding, and pending is a legitimate outcome of a batch of ten.
6. **The coverage table moves in the same commit.** Classified count, pending count, and both
   `R-18` halves are patched together with the row — never afterwards.

## Reporting

Every disposition batch reports, per entity: the name, the code, the class, and whether it was
batch-short or careful-detail. Then the two coverage numbers, in the `N / 303` form required by
`R-20`. The index is never described as complete while pending is above zero.

## Why ten and not five

Cleans are authorship and are slow. A disposition row is a reading of a file that already exists,
and the cost is in the reading rather than in the writing. Ten is the size at which the reading
stays careful and the batch still closes inside one prompt. If a batch of ten ever starts producing
rows that would not survive being read back aloud, the size is wrong and the batch is cut, not the
standard.
