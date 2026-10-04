# R-26 — Five, Then Seven, Then Ten

**Stated by the archive owner, 2026-10-05:** *"Do It Per 5 or 10 If It Was Simple E.G. If Per 5 Is
Fast Continue To 7 Then 10"*.

## The rule

The batch size is no longer fixed at five. It is a **floor that ratchets on evidence**.

| Stage | Condition to move up |
|---|---|
| **5** | The standing batch. Always start here. |
| **7** | The first five were *simple* — see the test below — and all five passed the gate first time. |
| **10** | Seven were simple too. |

A batch never ratchets back up inside the same turn after a file has turned out hard; it stops at
whatever number was honestly finished.

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

**The quality clause outranks the size clause.** `R-22` said each batch must be done right and
`R-25` repeated it; this rule only says that when the work is genuinely easy, the archive should get
more of it in the same turn. Ship the number that was finished properly, name anything held, and
never pad a batch to reach a number.
