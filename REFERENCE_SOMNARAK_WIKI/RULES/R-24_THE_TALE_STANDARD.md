# R-24 — The Tale Standard

**Stated:** 2026-10-05, by the archive owner. **Status:** standing.

> *"Make sure that a lot of text is not just copy & paste text … for real info and good paragraph.
> For a good fixed example, the Tale section is already fixed. Fix anything that only sounds generic
> or templatey."*

## The rule

**`## 이야기 (Narratio) — The Tale` is the standard every other prose section in a dossier is held to.**
It was not chosen by preference. It is the only long-prose section in the archive that measures
clean: across the 298 dossiers that carry one, **not a single Tale section shares an eight-word run
with ten or more other dossiers.** `## 증언 (Testimonium)` is the only other section at zero.

A section meets the Tale standard when its sentences could not be moved into another dossier by
changing a name and an element word.

## How it is measured

`/home/user/wikitools/sect.py`. Lower-case the dossier, take the set of 8-word shingles, and call a
shingle **shared** when it appears in ten or more dossiers.

- **Generic fraction of a dossier** = shared shingles ÷ its own shingles.
- **Score of a section** = the fraction of dossiers in which that section contains any shared shingle.

```
sect.py                 archive summary and the clean counter
sect.py --sections      per-section league table, worst first
sect.py --files N       N best and N worst dossiers
sect.py <path>          per-line attribution: exactly which lines to rewrite
```

## The threshold, and why it is not zero

A dossier is **clean at a generic fraction ≤ 0.05.** Zero is not the target and is not reachable at
file level: table headers, the R.D. and M.A.W. blockquotes, and the values forced by the SECC code
are *supposed* to match across the archive (`R-23`). 0.05 is the figure the eleven already-bespoke
dossiers achieve with all of that furniture intact — the bar is set by the archive's own best work,
not by an invented number.

## What this rule adds that the existing tools cannot see

`tools/boilerplate_report.py` and `tpl.py` both compare **whole lines**. A paragraph generated from a
pattern and then given a different noun is not a repeated line and is invisible to both. Proof:
the ten dossiers rewritten in the second Workstream 6 batch all reached `RESIDUAL 0` and residue 0,
and still measured **0.103–0.129** generic. Clearing the line-level tools is necessary and not
sufficient.

## Binding constraints

1. **Growth only.** As with every de-boilerplate rule, generic text is replaced with longer specific
   text. Nothing is deleted to improve a score.
2. **Furniture is exempt.** The `R-23` sanctioned list is not a target. If a rewrite would make two
   dossiers disagree about what a Qliphoth-style threshold or a resistance band *means*, it is wrong.
3. **The score is a pointer, not a verdict.** `sect.py <path>` names the lines; a human decides which
   are furniture and which are mad-libs. A dossier is never edited to chase the number.
4. **This applies to my own writing too.** The bespoke sections added during Workstream 1 —
   `Warden Record` 0.62, `Watch Record` 0.45, `Apex Record` 0.42 — are not at the standard either.
   They are original per entity but have acquired a house tic, and they are in scope.
