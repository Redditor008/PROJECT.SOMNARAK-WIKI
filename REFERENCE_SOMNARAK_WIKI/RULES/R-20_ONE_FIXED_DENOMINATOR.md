# R-20 — One Fixed Denominator, With Bands as Side Figures

> *"If the bottom of the fraction moves, the fraction is not a progress report. It is a description of the queue."*

## The defect this rule corrects

Workstream 1 reported its progress against the **worst band**: `73 / 73` on the 30+ band, then
`10 / 10` on the 25+, then `8 / 8` on the 20+, then `1 / 76` on the 15+. Every time a band emptied,
the denominator was re-pointed at a lower threshold and the counter reset to near zero.

That is wrong in two separate ways, and both of them flatter the work:

1. **The denominator is not fixed, so the counter cannot be compared to itself.** `8 / 8` and
   `1 / 76` are not two readings of the same instrument. Nothing in the first number tells a reader
   how much of the archive is done.
2. **Band membership moves without anybody cleaning anything.** Cleaning one file lowers the global
   count of a shared line, which drops *other* files below the threshold. The 15+ band fell from 85
   to 74 across three cleans. Eleven files left the band; three files were rewritten. A band counter
   silently books the other eight as progress. That is the spillover this project has repeatedly
   promised not to present as work.

## The rule

**There is exactly one progress counter for Workstream 1, and its denominator never changes.**

> **N / 291 dossiers rewritten**, where 291 is every dossier in the measured archive —
> `tools/boilerplate_report.py :: dossiers()` — counted once, at the start, and never re-pointed.

The numerator increases **only** when a file has actually been rewritten end to end in this campaign.
It never increases because of a threshold, a re-measurement, or another file's clean.

## Bands are kept, demoted to side figures

The band counts are still useful — they say where the remaining damage is concentrated and which
file to open next. They are reported as a **distribution**, not as a progress fraction, and they are
labelled as the queue:

| Side figure | What it is |
|---|---|
| Dossiers at 20+ shared lines | queue depth, worst tier |
| Dossiers at 15+ shared lines | queue depth |
| Dossiers at 10+ shared lines | queue depth |
| Dossiers at 1+ shared lines | how many files are untouched by any clean |

A side figure falling is **not** reported as progress and is never written in `x / y` form.

## What must be said every turn

Three numbers, in this order:

1. **`N / 291`** — the fixed counter.
2. **The headline percentage** — shared lines as a proportion of all body lines.
3. **Lines actually rewritten this turn** — the only figure that is immune to spillover.

Band movement may be mentioned afterwards, in prose, with the word *spillover* where it applies.

## Why 291 and not 303

303 is the catalogue count used by the disposition index and includes the Unknown wing. The
de-boilerplate measurement — every figure in `WORK_IN_PROGRESS.md`, including the headline — is
computed over `dossiers()`, which is the 291 Sorrow-wing dossiers. The counter uses the same
population as the measurement it sits next to. Mixing the two would reintroduce exactly the problem
this rule exists to stop.

## Precedence

`R-20` binds `R-16` (Always Report the Progress Counter). Where `R-16` says *report the counter*,
`R-20` says *which counter*. The old band fractions are superseded and must not be quoted again as
progress, including in retrospective summaries of earlier turns.
