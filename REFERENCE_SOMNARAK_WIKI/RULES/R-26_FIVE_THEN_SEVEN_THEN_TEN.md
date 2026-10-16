# R-26 — Five, Then Seven, Then Ten

**Historical owner directions:** On 2026-10-05, the owner first said *"Do It Per 5 or 10 If It Was Simple E.G. If Per 5 Is Fast Continue To 7 Then 10"*, then corrected the opening size: *"You Start With 3 per batch but if it small enough you up it to 5 then to 7 then to 10 so per batch it can be per 3 SE File Up To Per 10 SE File : 3 > 5 > 7 > 10"*. On 2026-10-06, the owner said *"Always 3 or 5 then 7 or 10"*. On 2026-10-08, the owner said *"P + Never Batch Anything Below 3"*. These are historical instructions, not the current floor.

**Current owner direction (2026-10-15):** A batch must contain **at least five dossiers** unless the owner explicitly authorizes fewer for that batch or fewer than five eligible pending dossiers remain. This latest instruction supersedes the earlier three-dossier opening and floor, and the short-batch exception in `R-25`.

## The current rule

**Start at five.** The only ordinary batch sizes are **5, 7, and 10**. The floor is five, not three. Never pad a batch, and never close one below five while five or more eligible pending dossiers remain.

**Owner clarification (2026-10-16):** Five means five completed dossier reviews, not five mandatory edits. If the file and its sources support leaving it unchanged, report **No change** under What changed and still include its individual **Commentary**, evidence and checks. An unchanged primary can be a completed review only after the required review and individual log/gate/push are complete. Pending files do not count as no-change reviews. See the matching amendment in `R-31`.

The simplicity ratchet is **5 → 7 → 10**:

| Stage | Condition to move up |
|---|---|
| **5** | The opening five are simple by the test below and each passes its first repository gate. |
| **7** | The first five earned the move to seven; then all seven are simple and each passes its first repository gate. |
| **10** | The first seven earned the move to ten; then all ten are simple and each passes its first repository gate. |

Do not skip a rung. If the opening five are not all simple, finish and close at five. If seven are not all simple, do not start the ten-unit rung. A rung that has been opened is not closed at an intermediate size: if six or eight dossiers have been completed, keep the batch open until the next permitted size is completed or the owner authorizes a smaller close. The quality clause can stop expansion; it cannot reduce a batch below five.

If fewer than five eligible pending dossiers remain at the start, complete all of them and close at that smaller number. Do not add already-reviewed or out-of-scope dossiers to reach five. If five or more eligible cases remain but fewer than five can be completed properly, leave the batch open and carry the unfinished units forward; do not report it as closed. An explicit owner authorization for fewer applies only to the named batch and does not carry forward.

A `p` authorizes **one next batch only**. It does not authorize a second batch in the same turn. Any separate size instruction applies to that batch; it does not change the standing five-dossier minimum for later batches.

## What counts as “simple”

A dossier is simple when, on inspection, it is one of:

- **Short-form** — roughly 3,000–4,000 words, a stub Combat Record, no Interaction Record table, and no Warden/Apex/Watch section. These take about 35 substitutions and no follow-up heredoc.
- **Already part-bespoke** — real canon is in place and the prose score is under about 0.15, so the work is an extension rather than a replacement.

A dossier is **not** simple when it carries a full Interaction Record, a bespoke record section, a duplicated Tale, or a prose score above about 0.20. Those run 50–63 substitutions, usually need a follow-up pass, and one is worth two of the simpler cases.

## What does not change

`R-25`'s five quality conditions per dossier remain binding: `verify.py` RESIDUAL 0, `tpl.py` RESIDUE 0, `sect.py` ≤ 0.05, an `R-19` disposition or a stated hold, and one `gate.sh` commit per dossier. The five-dossier floor changes neither the checks nor the rule to complete each unit properly.

`R-25` previously said to ship however many units could be completed if five could not be finished. The current minimum-five direction supersedes that clause only as to closing below five: keep the batch open unless the owner authorizes fewer or fewer than five eligible cases remain. “Never pad” still applies.

## Historical correction record

The earlier versions opened at three or five and used a 3 → 5 → 7 → 10 ladder. The 2026-10-08 version made three the absolute floor. The owner’s 2026-10-15 direction supersedes both: start at five and do not close below five unless an explicit batch-specific authorization applies or fewer than five eligible pending dossiers remain. The earlier directions remain recorded above as history, not as current policy.

The filename remains `R-26_FIVE_THEN_SEVEN_THEN_TEN.md` because other files reference it. Its current ladder starts at five and retains the seven- and ten-unit upper rungs.
