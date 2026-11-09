# R-52 — A Command Ends In A File

**Stated by the archive owner, 2026-11-05:**

> *"Did You Ever Written Down Or Read The Rule For Example If I Give you Command Or Commanding Tone
> You Should Have Added It To Rule Or WIP Isnt There A RULE Like That"*

## 1. The gap this closes

The answer to that question, asked on 2026-11-05, was **no**. The archive had said it three times, in
prose, in three different files:

- `RULES/README.md`, line 3 — *"A rule that lives only in a conversation is a rule that will be
  broken by whoever reads the file next."*
- `OWNER_DIRECTIVES.md`, line 6 — *"an order that is only in a chat log is not a standard — it is a
  memory."*
- `COMMAND_REGISTER.md`, line 7 — *"indexed so that no command lives only in a chat log."*

Three sentences, all saying the same thing, **and not one of them was a rule, an order, or a check.**
They were preambles. A preamble describes a habit; a rule binds.

The consequence is on the record twice. **The SECC Refinement was given as a command and was not in
the register for four batches** — the register listed fifteen reformations and none of them was the
one you had just named (batch 207). **Three gates were written, tested, indexed and cited, and never
added to the build** — 203's work-effect gate, 204's SE-effect gate, 206's rule-index gate, each
printing `RESULT: PASS` and each unable to fail a push (batch 207). In both cases the command had
been obeyed and never *filed*, and the archive had no way to notice.

## 2. Where a command may end

A command is finished when it is **written somewhere a later reader can find it without the
conversation**. There are exactly three destinations:

| destination | when | where it goes |
|---|---|---|
| **A rule** | the command states a standard that outlives the files it touches | `RULES/R-nn_*.md`, indexed in `RULES/README.md` |
| **An order** | the command states permanent law about how the work is done | `RULES/OWNER_DIRECTIVES.md` as `O-nn`, and `COMMAND_REGISTER.md` Part II |
| **The record** | the command is a one-off instruction, a correction, or a sweep | `COMMAND_REGISTER.md` Part I or Part IV, with your words quoted |

**A command may end in more than one.** A standing order that also states a writing standard gets
both — `O-37` and `check_gate_wiring.py`, `R-51` and §16 of the register.

**Quote the words.** The register's Part I entries open with *"What you said"* and the orders carry
*"Your words"* for a reason: a paraphrase is a second author's opinion of the instruction, and the
file is supposed to preserve the instruction.

## 3. What counts as a command

Not only the imperative. A command arrives in at least four shapes, and all four bind:

- **The imperative** — *"Do It Per 5 in Batch"*, *"Refine the [p] Before Doing p"*.
- **The correction** — *"IT STILL READ ILLOGICAL … AND FEEL BLOATED"*, *"inflation, not a fix"*. A
  correction is a command to change the method, not merely to redo the paragraph.
- **The named lack** — *"I Think There Is Something Missing Example SECC Refinement"*, *"Did You Ever
  Written Down … Isnt There A RULE Like That"*. **A question that names a missing standard is an
  instruction to go and write it**, and answering it in chat alone is the failure it describes.
- **The commanding tone** — a directive given without explanation. The tone is not decoration; it
  marks the sentence as law rather than as a suggestion or an idle reading.

Unclassified instructions default to **the record**, not to silence. If it is not clearly a rule, it
is at minimum an entry; the entry can be promoted to a rule later, and cannot be recovered later if
it was never written.

## 4. What is not a destination

**A chat message.** It ends when the window closes.

**A `WORK_IN_PROGRESS` note with no rule behind it.** The batch log says what was done; it does not
bind the next batch. A standard recorded only in WIP is a standard that the next reader will not
consult, because the next reader opens the rules folder.

**A rule with no index row.** Filed and invisible is the same defect as unfiled — this is what
`check_rule_index.py` (gate 90) exists to catch, and it caught five of them.

**A gate that is not in the build.** Written and cited is not enforced. `O-37`, gate 92.

## 5. What is checked

`check_command_capture.py` (gate 94) reads the three registers against each other and fails on any
command that ends nowhere:

- every `R-nn` file on disk is named in `COMMAND_REGISTER.md`;
- every `O-nn` in `OWNER_DIRECTIVES.md` appears in the register's Part II table;
- every batch heading in `WORK_IN_PROGRESS.md` falls inside an era the register declares;
- the register's declared batch span reaches the highest batch on record.

It reports each count on both sides, so a check that matched nothing is visible rather than green.
