# R-31 — Chatroom Reports Are Written To Be Read

**Stated by the archive owner, 2026-10-08:** *"You Need To Write The Information In Chatroom More Clearly and
More Readable, This For Normal Text And Table. Write It As A Must Follow RULE And Always Read The Rule Before
Doing Anything."*

The chatroom is where the owner reads the work. A report that has to be decoded is a defect, even when the
dossier edit behind it is perfect. Readability is part of the deliverable, not decoration around it.

This rule codifies and extends the owner's table directive of 2026-10-07 (b51, *"Remember The Table In
Chatroom"*). It binds every report: units, batches, audits, closes, answers to questions.

## The rule

0. **Read this rule before doing anything.** Read it at every session open, together with
   `RULE-TO-FOLLOW.md` and `SESSION_BREAK_PRECAUTION.md`, and read it again before writing any chatroom
   report. It is a must-follow rule, not a style preference.

### Normal text

1. **The answer comes first.** Line one of a report states the outcome: what was pushed, its hash, and
   `PUSH VERIFIED` or `NOT PUSHED`. Never bury the verdict at the bottom.
2. **Short sentences.** One idea per sentence. Around 25 words is the ceiling. No chains of clauses joined
   by `·` or by semicolons. If a sentence needs a second reading, split it.
3. **Short paragraphs, real bullets.** Three sentences is the longest paragraph. A list of three or more
   items is written as bullets, never as prose.
4. **Plain words, glossed once.** Every tool name, counter name and internal term is glossed on first use in
   the turn, in brackets: `verify.py (the residue check)`. No unexplained jargon. No abbreviation that the
   owner has not used first.
5. **Nothing stacked into one line.** Several facts separated by middle dots is a table's job, not a
   sentence's. Split them, or tabulate them.
6. **Bold only what matters.** The dossier name, the counter, the verdict. Never a whole sentence, never a
   whole paragraph.
7. **Answer the question asked.** When the owner asks a question, the reply answers it in its own words
   before anything else is reported. A question is never answered by a batch summary alone.

### Tables

8. **Five columns, maximum.** Needing a sixth means two tables.
9. **One row per dossier, or one row per counter.** Never two dossiers sharing a row.
10. **Every counter carries its denominator.** `x / y`, always. Never a bare number.
11. **Headers are short nouns.** `Partner` · `Section` · `Before` · `After` · `Result`. No sentence-length
    headers, no header that needs its own explanation.
12. **Cells stay short.** Before and after share one cell with an arrow: `0.72/0.66 → < 0.50`. No paragraph
    lives inside a cell.
13. **The SE name in a cell is a link.** In any table that lists an entity together with what was fixed on
    it, the name in the cell carries that dossier's GitHub link, in either accepted form: a plain markdown
    link, `[The_Debt_Scale](url "SE-C-IIIβ-015_The_Debt_Scale_빚의_저울.md")`, or the `R-12` double-bracket
    form. `tools/ghlink.py --short --plain <path>` prints the first one, so it is generated and never
    hand-typed. The designation code follows the linked name. A file path is still never written as plain
    text in a cell, and the `R-12` link below the table is still required for every finished dossier: the
    cell link is additional, not a replacement.
14. **Numbers agree with each other.** Ratios to two decimals. One unit per column. No column mixing
    `0.7` and `0.66` and `72%`.
15. **Caption every table.** One line above it saying what it shows. Three tables per unit is the ceiling;
    more than that is split across turns or cut.

### The fixed order of a report

| Order | Block | What it holds |
|---|---|---|
| 1 | Verdict | Unit, hash, `PUSH VERIFIED` or `NOT PUSHED` |
| 2 | Progress lead | Full-SE and Weapon-only percentages, then denominator-bearing remaining counts |
| 3 | What changed | Two or three plain content sentences per dossier, then that dossier's commentary |
| 4 | Table | Caption, one row per dossier, linked name, short change, checks, commit and push |
| 5 | Links | One full `R-12` link per finished dossier, below the table |
| 6 | Live counters | Separate Full-SE and Weapon-only totals, definitions, exclusions, then batch-local progress |
| 7 | Next | Next step, any owner authorization needed, and branch/PR state when relevant |

### A failure is redone

A report that breaks any of 1–20 is rewritten in the same turn, before any further work is started.
Readability refusals are recorded like gate refusals: what failed, what was rewritten, and that the corrected
version is the one that stands.

## Amendment, 2026-10-08 — the SE name in a table carries its link

**Stated by the archive owner, 2026-10-08:** *"In The Table That Show The SE And Its Fixed Section On The SE
Name Puts Its Git Link"* — with both forms accepted: the `R-12` double-bracket link, or a plain markdown link
carrying the file name as its tooltip.

Point 13 was rewritten in the same turn to require it, and `tools/ghlink.py` gained `--plain` so the cell form
is printed rather than typed. It binds every table that pairs an entity with what was fixed on it: unit rows,
partner rows, batch recaps and close reports.

Worked example, one row per dossier, four columns:

| Entity | Section fixed | Before → after | Result |
|---|---|---|---|
| [The_Debt_Scale](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B2-015_The_Debt_Scale_%EB%B9%9A%EC%9D%98_%EC%A0%80%EC%9A%B8.md "SE-C-IIIβ-015_The_Debt_Scale_빚의_저울.md") `C-IIIβ-015` | Core Stat Line | 0.75/0.62 → < 0.50 | couple broken |

## Amendment, 2026-10-09 — the report carries the information, not the process

**Stated by the archive owner:** *"Refine The Chatroom Text Into A More Readable Fill Information Not Just AI
Text That Only You Know"* — read with the standing table and readability rules above, which this amendment
extends rather than replaces.

A report can satisfy every point 1–15 and still fail this amendment. The failure it names is a report made
of **process**: tool names, scores, and notes about how the work was done, with nothing about what the work
actually changed. Such a report is readable and empty at the same time, and the owner cannot use it.

16. **Fill in the information.** The report carries the substance of the change, not only the measurements
    around it. Having read it, the owner knows what the entity is and what the dossier now says. Each unit
    gets two or three plain sentences of **content** — what the file claimed before, what it claims now, and
    why that is truer to the entity. The measurements follow the content; they do not replace it.
17. **No insider shorthand.** A word the agent invented is not a word the owner agreed to. Terms such as
    *gram*, *frag*, *spec*, *rep*, *attr*, *precheck*, *heavy side* and *self-echo* are either replaced with
    plain words or glossed in one short sentence on first use. If a term cannot be explained in one sentence,
    it does not belong in the report. Tool names are named once, in brackets, and then spoken of in plain
    words: `label_lint.py (the label vocabulary check)`.
18. **The report stands alone.** It is written for a reader who was not in the session. Once per turn, in
    plain words, it says what a couple is, what the fix phase is, and what each counter counts. It never
    assumes the reader remembers what the previous turn did, and it never refers to "as above" across a
    turn boundary.

### What this changes in the fixed order

Block 3, *What changed*, holds the **content** of the change first and the measurement second. Block 4,
*Table*, holds the compact per-dossier recap. Block 2 is a deliberately short cumulative-progress lead; it is
repeated in full, with definitions, in Block 6. A report that puts numbers where the content belongs has the
order right and the emphasis wrong, and is rewritten.

## Amendment, 2026-10-15 — the approved chatroom report is the standard

**Stated by the archive owner, 2026-10-15:** *"What You Do On Chatroom Is What You Should Always Do From Now On
And IF Can Write It As RULE That Need To Be Followed."*

The previous readable batch-close format is now the must-follow default for every chatroom progress report,
not only for this batch. The fixed order above applies. The cumulative-progress lead comes immediately after
the verdict, so both independent workstreams are visible before the content recap.

19. **Lead with cumulative progress.** Immediately after the verdict, report Full-SE and Weapon-only
    separately as a percentage out of 100%, followed by the remaining count with its named denominator, such
    as `191 / 301 remain`. Do not combine the two workstreams. Repeat the complete counts later in the live
    counter block; batch-local `x / y` is secondary and must not replace cumulative coverage.
20. **Close a batch with eight required fields.** The report is stand-alone and records: (1) the owner's
    authorization and batch size; (2) the fresh ranking, selected order, and any correction; (3) two or three
    content sentences for each dossier; (4) the source evidence checked and disagreements left on hold; (5)
    validation results; (6) each dossier's commit and verified push status; (7) separate cumulative counters,
    exclusions, and secondary batch-local progress; and (8) the next step, any authorization needed, and
    branch or pull-request status when relevant. Put each field in the block that fits the fixed order; do not
    add a second dossier-summary table just to repeat it.

A `p` authorization is one next batch only. An explicit batch-size instruction applies only to that batch.
Never imply that a held disagreement is a defect finding, that an unreviewed dossier is defective, or that a
previously reviewed Weapon pair was counted again. Generate each table's dossier link with
`tools/ghlink.py --short --plain <path>`; keep the separate full `R-12` link below the table.

## Amendment, 2026-10-15 — the report carries the reviewer's commentary

**Stated by the archive owner, 2026-10-15:** *"In What Change In Chatroom Can You Add Commentary Section Of About
What You Though About The Entity So I Can Read What OTHER-OTHER AI Though About IT Other Than The AI That Write
The Entity."*

Every dossier in this archive was written by an earlier session, and often by a different model. The agent
reporting on it now is a later, separate reader. The owner wants that reader's actual opinion of the entity in the
report, not only the list of what was edited on it. Block 3 therefore carries two halves: the content recap, then
the commentary.

21. **Every reported dossier carries a commentary.** After the content sentences for a dossier, the report adds
    two to four plain sentences in the reporting agent's own voice: what this reader understands the entity to
    be, what about it works, and what it finds thin, risky or unresolved. It is marked with the word
    **Commentary** so it can never be mistaken for the record.

The rules that keep a commentary honest:

- It is **opinion, not evidence**. It never changes a dossier, never argues canon into place, and is never
  counted as a check, a counter or a disposition.
- It is **never a defect finding**. A held or unreviewed dossier is not made defective by a commentary
  (point 20 binds it as well).
- A canon conflict found while writing it is entered as a hold in the normal way, and the commentary points at
  that hold; the commentary is not the hold.
- Points 16–18 bind it: plain words, no tool names, no scores, no internal shorthand, no process talk.
- It is **one per dossier**, in the unit report and again in the batch close. One paragraph covering a whole
  batch is not a commentary.
- If it would only repeat the content sentences, it is not written. Said in one line instead, or left out with
  that said plainly — an empty sentence is worse than a shorter report.

**What this changes in the fixed order.** Block 3 reads content first, commentary second, dossier by dossier. The
Block 4 table is unchanged: a commentary never becomes a table column. A report shipped without its commentaries,
or with them placed before the content, is rewritten in the same turn.

## Amendment, 2026-10-16 — report reviewed dossiers even when nothing changes

**Owner direction:** Include dossiers that need no change so the owner can see all five reviews in a batch. Write **No change** under What changed and still provide the individual Commentary. The decision must follow the file and its sources, not the agent's wish to edit it.

22. **A completed review is reported whether or not it produces an edit.** Every completed dossier gets its own linked table row, content recap and separate **Commentary**. For an unchanged dossier, the **What changed** entry says exactly **No change**. Explain separately what was checked and why the existing file and sources support leaving it as written. Keep any unresolved disagreement explicit; no change does not mean every source agrees.

- The five-dossier floor is five completed reviews, not five forced rewrites. Never add prose or alter canon just to make a review look productive.
- Retain the complete primary, identity-resolved source and history review, validation and individual gate/push requirements. A no-change unit ships its evidence and disposition in the logs; it does not need an artificial primary-file edit.
- Count an unchanged dossier only after that review is complete and shipped. Apply the independent counter rules: a previously counted exact Weapon pair still adds zero.
- A five-dossier close shows all five reviewed dossiers, including unchanged ones, with one Commentary per dossier. In an open-batch report, distinguish completed reviews from pending units. **Pending** is not **No change**; do not invent a review or commentary for an unread file.

This amendment extends points 16, 20 and 21 and clarifies `R-26`. It does not authorize closing below five, counting an unreviewed file, or repeating a previous review to pad a batch.

## Amendment, 2026-10-16 — show the No change ladder decision

**Owner clarification:** Five is the minimum, ten the ceiling. A batch with three or more completed No change SE–M.A.W. dossiers progresses **5 → 7 → 10**, per dossier rather than per matching field or pair.

23. **Report the rung and its evidence.** At five and seven, state the completed batch's cumulative count of No change dossiers and the resulting progression under `R-26`. Three or more triggers the next rung within the same authorized batch, even when the dossiers are long or carry explicit source holds. Show every completed dossier and its individual Commentary; never present five as the automatic ceiling. Pending units are neither completed nor No change. If the required rung is unfinished, report OPEN, completed versus required counts, and the remaining units, not a smaller close.

## How it is checked


| Check | Where it is applied |
|---|---|
| This rule read before the report is written | Every turn, at session open and before replying |
| The 20 points walked once, top to bottom | Before sending any chatroom message |
| The commentary half of Block 3 present, per dossier, headed **Commentary** | Before sending any chatroom message |
| Counters re-measured, not remembered | `verify.py` · `tpl.py` · `sectfile.py` · `wikistd.py` · the couples planner |

No tool can read a chatroom, so the check is the list above, applied by hand before sending. This rule
governs how a result is written; it never decides whether the result is true. Truth still comes from the
tools, and every counter quoted in a report is one that was measured in that same turn.

## Baseline at the time of writing

Written during b62 (the fix phase), after u7 `a4c81d2` and the held Homecoming Tree unit `be95f5e`.
Live counters at the moment of writing: couples **182 / 301** · residue-free dossiers **301 / 301** ·
quote families **0 / 301** · `R-29` clauses **301 / 301**.

## Amendment, 2026-10-18 — three separately named appearance counters

The owner requires a new SE appearance-fix X/X, distinct from the older M.A.W. streams. In current progress leads and tables, use the explicit R-16 names: **ALL M.A.W. Types Appearance per SE — source-review coverage**, **ALL M.A.W.-W Appearance per SE — source-review coverage**, and **SE Appearance Fix — independent written-design pass**.

This refines the older Full-SE/Weapon-only label wording above without rewriting historical reports. Keep all three denominators, percentages and remaining counts separate. State that inherited equipment coverage includes holds and is not completed artwork/redesign coverage. New SE appearance credit is never backfilled from old reviews or from a naming change. For an open batch, show the completed versus required rung and pending queue; never call a smaller open result a completed batch. R-31's per-dossier content, Commentary, linked table and full R-12 links still apply to completed new-pass units.

## Amendment, 2026-10-18 — equipment-first or combined batches

Owner permits completing the older appearance stream first or reviewing equipment and SE bodies in the same batch, even if execution takes longer. Work in separate, focused Bash calls; do not place the entire batch in one giant command. Preserve independent counters, per-dossier evidence, prior-credit exclusions, individual Commentary, validation and individual pushes. A combined batch counts freshly completed dossier reviews, not inherited body credits. No permission to force edits, convert a source hold into a resolution claim, or skip5→7→10 follows from combining the workflow.
