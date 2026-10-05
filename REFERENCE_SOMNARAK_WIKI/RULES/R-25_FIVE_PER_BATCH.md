# R-25 — Five Per Batch

**Stated by the archive owner, 2026-10-05:** *"Do It Per 5 in Batch"*.

## The rule

The unit of work is **five dossiers per prompt**, not one.

A dossier is finished when all of the following are true, and the batch is finished when
five dossiers are:

1. `verify.py` **RESIDUAL 0**, no seam, no dupes.
2. `tools/tpl.py` **RESIDUE 0** — line-scope template residue (`R-23`).
3. `tools/sect.py <path>` **≤ 0.05** — the Tale standard (`R-24`), prose scope.
4. A disposition row, classified under `R-19` with quoted evidence, or the row stays pending
   and the reason is stated.
5. One `gate.sh` commit per dossier. Five dossiers, five commits. Never two in one gate — that
   mistake has been made twice and must not be made a third time.

## Relationship to the earlier batch rules

- `R-21` (five whole-file cleans per prompt) governed Workstream 1 and is spent; Workstream 1
  closed at 291 / 291.
- `R-22` (ten dispositions per batch) governs Workstream 5 when a batch is *only* classifying
  already-clean dossiers. It is not repealed.
- **`R-25` governs the combined per-entity pass**: rewrite to the Tale standard *and* classify, on
  the worst-first pending queue. Five is the number because each dossier in this pass costs
  roughly 50–60 authored substitutions and 600–1,200 new words, which is where ten stopped being
  honest work.

## The quality clause carries over unchanged

From `R-22`, and it is the half of the instruction that matters: **each batch done right.** If five
cannot be finished to the five conditions above, ship the number that can, say which were held, and
say why. A short batch that is correct beats five that are not.

## Order

Worst first by `tools/sect.py --files`, filtered to dossiers with no disposition row yet. The
pending-only ranking is recomputed at the start of every batch, not carried over from the last one.
