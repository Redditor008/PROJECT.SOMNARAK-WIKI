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
| 1 | Verdict | Unit, hash, `PUSH VERIFIED` |
| 2 | What changed | Two to five plain sentences |
| 3 | Tables | Before → after, with captions |
| 4 | Links | One `R-12` link per finished dossier |
| 5 | Live counters | The stage counters, each as `x / y` |
| 6 | Next | What comes next, and what is needed from the owner |

### A failure is redone

A report that breaks any of 1–15 is rewritten in the same turn, before any further work is started.
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

## How it is checked

| Check | Where it is applied |
|---|---|
| This rule read before the report is written | Every turn, at session open and before replying |
| The 15 points walked once, top to bottom | Before sending any chatroom message |
| Counters re-measured, not remembered | `verify.py` · `tpl.py` · `sectfile.py` · `wikistd.py` · the couples planner |

No tool can read a chatroom, so the check is the list above, applied by hand before sending. This rule
governs how a result is written; it never decides whether the result is true. Truth still comes from the
tools, and every counter quoted in a report is one that was measured in that same turn.

## Baseline at the time of writing

Written during b62 (the fix phase), after u7 `a4c81d2` and the held Homecoming Tree unit `be95f5e`.
Live counters at the moment of writing: couples **182 / 301** · residue-free dossiers **301 / 301** ·
quote families **0 / 301** · `R-29` clauses **301 / 301**.
