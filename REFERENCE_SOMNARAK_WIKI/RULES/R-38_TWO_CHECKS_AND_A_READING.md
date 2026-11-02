# R-38 — Every fix gets two checks, a reading, and a box

**The rule, in the owner's words.** *"Each time you try to fix or check things you do double check, and the second check used reader viewing logic; than after finished fixing you do reading review with logic; than you can check it in check list/box."*

Four steps, in order, every time. Not one of them is optional and the third cannot be skipped by passing the first two.

---

## 1. Check — machine logic

Run the linter that owns the thing. `check_links`, `seam_lint`, `section_logic`, `label_lint`, `timeline_lint`, `check_stat_bands`, `text_box_double_checker`, `check_box_symmetry`, `audit_lore_archive`, `compare_conversion_guide`, `check_stock_ceiling`, `finishedness`.

This pass answers *"is the string right"*. It is necessary and it is never sufficient. Every serious defect this archive has produced passed a machine check first: a guide that named four status effects that do not exist, a record whose `Risk tier` carried a coherence letter, 42 files spelling `first- person`, a dossier still wearing `{{ }}` braces.

## 2. Double check — reader viewing logic

Read the file the way its reader does: top to bottom, in order, asking what a person sees.

- Does the page answer the question the reader came with? A record with no Appearance section does not tell a reader what the thing looks like, however correct its stat table is.
- Does the order hold? Title, identifiers, identity, appearance, statistics, history.
- Does any sentence stop mid-clause, any heading stand over nothing, any paragraph print twice, any table row sit outside a table?
- Does the file end, or does it stop?

Use `python3 tools/reader_check.py` for the mechanical half of this pass (heading ladder, empty sections, cut-off sentences, duplicated paragraphs, orphan rows, missing H1) and your own eyes for the rest. **`reader_check.py` is advisory, not a gate**: its findings are leads, and a lead that reads fine when opened is not a defect.

## 3. Reading review — logic

After the fixing stops, read the changed files again as a whole and ask whether the *result* is coherent, not whether the edit landed. This pass catches what neither earlier pass can:

- An insertion that is correct in isolation and duplicates what the next paragraph already says.
- A heading that now sits above content belonging to the section before it.
- A transcribed line that is right about a *different* piece than the one the record describes.
- A fix that answered the metric and not the reader.

Record the reading review's result even when it is "no change" — a batch that was read is a different claim from a batch that was checked.

## 4. The checklist

Finish with a checklist written as a **standard Markdown task list**, so the next session can see what was verified without re-deriving it. Every line is a claim that was actually tested, ticked `[x]` only if it passed, and every failure stays in the list with its reason.

```markdown
### Batch <n> — checks

- [x] **machine check** — PASS — `tools/<name>.py`, <what it covers>
- [x] **second check** — PASS — <what a reader actually sees>
- [x] **reading review** — PASS — <N> files read whole
- [ ] **still open** — <the item> — <why it stays open, and what would close it>
```

Rules for the list:

- **Markdown task syntax only.** `- [x]` and `- [ ]` render as real checkboxes everywhere the archive is read — GitHub, the wiki, the editor. Do **not** draw the checklist as ASCII box art (`+---+` frames, `|` gutters, dotted leaders): it does not render, it does not tick, and inside a table it collides with the archive's own row-pipe rule.
- **Bold the claim, not the verdict.** The label is what was checked; the verdict follows it.
- **A tick is a claim that was tested.** If it was not run this batch, it does not get a tick and it does not get a line.
- **An unticked line needs a reason and a route.** `[ ] still open — h1_match, 125 records — needs a file-named instruction per file (A5).`
- **A list with no open items is a list that is lying about something.** If the batch genuinely closed everything it touched, add a final unticked line naming what it did **not** touch.

> **Owner ruling, 2026-11-02:** *"the check box/list used the standard Markdown style, not using the textbox."* The procedure is unchanged — the box was only ever a way of drawing it. Batches 116–119 were reported to the owner in box form; their `WORK_IN_PROGRESS.md` entries never carried one, and no later entry will.

---

## Why the second check exists

Three separate times the machine check and the reader check disagreed, and the reader was right:

1. **`first- person` ×42.** Every linter passed; a reader hits a word split by a space and stops.
2. **`SE-O-IVδ-515`.** Five Combat Action rows still wrapped in `{{ }}` with real content inside them — the file was complete to every check and unfinished to every reader.
3. **A standalone `| Maximum Amount | 3 |` line** inserted by a script into 190 records: valid Markdown, renders as literal pipes, invisible to a checker that only asks whether a row exists.

And once the reader check itself was wrong: a CRLF line ending made `### Appearance` unmatchable, and 71 good edits were reported as 71 defects. **Check the checker before believing it** — especially when it agrees with what you expected.

---

## Calibration log — batch 116

Six more obligations were the checker's, not the archive's. Each had been scoring real files as unfinished:

1. **`tools/tests/fixtures/` were being scored.** Nine files that exist in order to fail were counted among the 2,352, dragging the whole set down. A fixture is not a document.
2. **`sections` demanded an H2 of everything.** A short rule file and a batch-close record legitimately run as bold-led paragraphs under one H1. Accept an H2, a table, or three bold lead-ins.
3. **`corrosion_stock` asked for a section that does not exist.** `TEMPLATES/SE/03–05` carry no corrosion section, so the obligation was invented — and the check rewarded the stock sentence over bespoke text, inverting the thing it claimed to measure. Removed from both rubrics.
4. **`statistics` asked suits for damage.** Weapons file damage/speed/range, suits file a resistance table, stigmas file slot/chance/bonus. It also read one resistance notation of the four in use. Now type-aware.
5. **`cost_line` rejected a stated rate.** *"Bestowal probability is 5 %"* is a filed cost. Any percentage passes.
6. **`substance` measured prose in a listing and in a record.** A registry index README's substance is its rows; a file carrying `**Document ID:**` and a record field is a record at 200 words, whatever its path is called. Side Codices and the `UNK_` pieces were held to the 250-word prose floor because `classify()` only recognised `SE-\d+-[BCD]`.

**The pattern worth keeping:** every one of these was found by asking *"is this file actually unfinished, or is my rule wrong about what finished means here?"* — and in all six cases the file was fine. Score a listing as a listing, a record as a record, and do not ask a template for a section it never had.

**And the limit of the machine check:** reading `SE-1010-B` whole rather than grepping its headings found a raw template phrase — *"the entity-specific management condition is satisfied and the Sorrow Gauge falls below 25 %"* — sitting in 76 files where an entity's own condition belongs. No regex asked for that sentence, so no regex found it. That is what step 3 is for.
