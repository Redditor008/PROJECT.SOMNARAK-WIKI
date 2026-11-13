# R-55 — A File Is Read Once, in Order

**Stated by the archive owner, 2026-10-25:**

> *"Also Echo Core Back Story Some Of Them Is Really Plain And Not At All Make Sense When Read
> Example Majin If You Read It With Reader Logic"*

## 1. What the reading found

The owner read the nine Echo-Core backstories as a reader and named one: **Majin**. He was right, and
the fault was not the prose. `01_MAJIN_` breaks its own order three ways, and each one is visible on a
single pass:

- **`## The Break` is printed before the Day 149 scene it describes.** A man at 04:00 understands
  what the word *shared* means — and says so in terms of a Day 149 the reader has not reached.
- **Day 160 is missing.** The file builds a cannon, spends eleven hundred years on it, cuts it into a
  fountain on Day 149, and then skips to *"nine days after the dispersal"*. The climax of the
  Director's story happens in a subordinate clause.
- **Day 365 states three anniversaries that have not happened.** *"One year since the Cycle ended"* —
  the Cycle ends that night. *"One year since the Hand of Hope opened"* — 210 days.

The same class was found in two more files: `02_SEIYON_` ended Part One on Day 108 and opened Part Two
on Day 0; `07_MARJUK_` filed a **Year 4,235** scene between Day 49 and Day 77, and put the Day 365
anniversary after the Year 4,238 scene it precedes.

## 2. The rule

**A file is read once, top to bottom. Its anchors must be in the order a reader walks them.**

The structure standard already requires every appendix to carry a **Scene ledger** and a
**Chronological spine**. Those are the file's own statement of the order it means to be read in. So
the order is written down twice, and the gate holds the body to it:

- a day anchor may not go backwards;
- an era anchor (`Year 4,2XX`) may not be followed by an earlier day anchor;
- every day the body anchors must be accounted for somewhere in the appendix;
- the spine's own day rows must not run backwards.

**A scene the file skips is a defect, not a style.** Where a file has built toward an event across a
whole record, the event gets a scene. Majin's Day 160 was *"referenced only, filed by 05, 06, and the
Parts"* — a defensible economy for a secondary chronicle and the wrong choice for the file that owns
the character. The Director's own account of the day he opened the hand is not optional material.

## 3. What a gate can and cannot see

`check_backstory_reader.py` (gate 51) fails `02_SEIYON_` and `07_MARJUK_` on their pre-fix text.

**It passes `01_MAJIN_` on its broken text.** Majin's defect was a `##`-level section placed before
the scene it describes; no anchor was out of order, because the scene ledger and the spine were wrong
in the same way as the body. The file agreed with itself and disagreed with time.

> **A gate can check that a file agrees with itself. Only a reader can check that it agrees with the
> world.**

This is `R-38` and `O-29` restated by a failure, and it is why `O-41` is filed STANDING and not DONE.
The mechanical half is now enforced. The reader's half never can be.

**And the reverse is just as wrong.** The first draft of gate 51 failed three files that were
correct: `05_AYSHUK_` and `06_MELLDA_` file their flashbacks as `Days 7, 41, 73` in one spine row,
and `09_XYAN_` writes its spine by beat and scene number rather than by day. A checker that reads
only the singular form, or only the day form, invents defects. The reader was fixed, not the archive.

## 4. The span error

Fifteen occurrences across four files gave a 1,778-iteration life as *"four thousand years"*.

Every Echo-Core's operational span is the **1,778-Cycle era** — `THE_DIRECTOR.md`: *"Active across
1,778 Cycle iterations plus the unlooped years"*. Four thousand years is the **city's** age, read off
the calendar year 4,232. It is correct for the Maw, the thousand, the archive and the Cheongula. It is
wrong for a person.

A reader who is told *"1,778 mornings"* in one paragraph and *"four thousand years"* three paragraphs
later has been told two different things about one life. The phrase is now restricted to what is
older than the Directorate, and the corrected figure is the one the dossier prints.

## 5. What is checked

`check_backstory_reader.py` (gate 51) reads all nine files and reports order defects. `how_finished.py`
carries it as a standing standard, so a file that stops agreeing with its own spine is OPEN, not
merely noted.

The reserve arithmetic — 0.02 × 1,778 = 35.56 against 47.3 / 49.80 / 49.88 / 50.92 / "0 remaining" —
is **not** resolved by this rule and must not be averaged into one number. It is filed as a HOLD in
`BACKSTORY_READER_LOGIC_AUDIT.md` §4 and needs an owner decision.
