# R-26 — Three, Then Five, Then Seven, Then Ten

**Stated by the archive owner, 2026-10-05:** *"Do It Per 5 or 10 If It Was Simple E.G. If Per 5 Is
Fast Continue To 7 Then 10"*, and **corrected the same day**: *"You Start With 3 per batch but if it
small enough you up it to 5 then to 7 then to 10 so per batch it can be per 3 SE File Up To Per 10
SE File : 3 > 5 > 7 > 10"*.

**Stated again by the archive owner, 2026-10-08:** *"P + Never Batch Anything Below 3"*. The floor of
three is **absolute**. No batch closes at one or two units, and the quality clause at the foot of this
file no longer produces a short batch. When fewer than three units can be finished properly the batch
**stays open**: it carries into the next turn, the record names the units that were finished and the
ones still owed, and the batch is never reported as closed below three.

## The rule

**Stated again by the archive owner, 2026-10-06:** *"Always 3 or 5 then 7 or 10"*. The batch size is
always one of those four numbers and never any other: a cohort opens at **3 or 5**, and the ladder
climbs to **7** and then to **10**. There is no batch of four, six, eight or nine, and the opening
number is never skipped — a cohort does not begin at seven. **A batch below three is never
permitted** (owner, 2026-10-08: *"Never Batch Anything Below 3"*). The earlier wording permitted one
by the quality clause at the foot of this file, named and explained; that permission is superseded
and is recorded here rather than removed (`R-17`: history is not rewritten).


The batch size is not fixed. It is a **floor that ratchets on evidence**, and the floor is **three**.

| Stage | Condition to move up |
|---|---|
| **3** | The standing batch floor. Always start here. |
| **5** | The first three were *simple* — see the test below — and all three passed the gate first time. |
| **7** | Five were simple too. |
| **10** | Seven were simple too. |

The ladder is **3 > 5 > 7 > 10** and it stops at 10. A batch never ratchets up inside the same turn
after a file has turned out hard; it stops at whatever number was honestly finished. A batch of
fewer than three is not shipped at all — the batch stays open, the finished units are named in the
record, and the remainder is worked next turn. The superseded wording, which permitted such a batch
by the quality clause below when it was named and explained, is kept here as history (`R-17`) and
stopped being the rule on 2026-10-08.

The earlier wording of this rule put the floor at five, which was the owner's first instruction and
is superseded by the correction above; the superseded figure is recorded here rather than removed
(`R-17`: history is not rewritten). Beyond ten the rule is silent: more than ten SE files in one
batch is not contemplated, and a turn that has ten finished units reports them and stops rather
than starting an eleventh.

## What counts as "simple"

A dossier is simple when, on inspection, it is one of:

- **Short-form** — roughly 3,000–4,000 words, a stub Combat Record, no Interaction Record table, no
  Warden/Apex/Watch section. These take about 35 substitutions and no follow-up heredoc.
- **Already part-bespoke** — real canon in place, prose score under about 0.15, so the work is
  extension rather than replacement.

A dossier is **not** simple when it carries a full Interaction Record, a bespoke record section, a
duplicated Tale, or a prose score above about 0.20. Those run 50–63 substitutions, usually need a
follow-up pass, and one of them is worth two of the others.

## What does not change

`R-25`'s five conditions per dossier are untouched and are the reason the number may rise at all:
`verify.py` RESIDUAL 0 · `tpl.py` RESIDUE 0 · `sect.py` ≤ 0.05 · a disposition row or a stated hold ·
one `gate.sh` commit per dossier.

The filename of this rule still reads `FIVE_THEN_SEVEN_THEN_TEN`. It is left as it is because other
files reference it by name and the ladder it describes is the same ladder with a lower floor; the
title above is the corrected one and the correction is dated in the header.

**The quality clause outranks the size clause.** `R-22` said each batch must be done right and
`R-25` repeated it; this rule only says that when the work is genuinely easy, the archive should get
more of it in the same turn. Ship the number that was finished properly, name anything held, and
never pad a batch to reach a number.

Since 2026-10-08 that clause has one hard limit. Quality can stop a batch **ratcheting up** — a
cohort that turns out hard stays at three rather than climbing to five — but quality can never take a
batch **below three**. If only one or two units can be finished properly, the batch is not closed: it
stays open at three, the turn reports what was finished and what is still owed, and the next turn
completes it. Padding is still forbidden, so the two clauses meet in one behaviour: an open batch,
never a short one and never a stuffed one.
