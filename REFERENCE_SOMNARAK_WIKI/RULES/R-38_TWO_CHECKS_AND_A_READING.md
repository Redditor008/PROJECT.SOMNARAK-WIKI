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

## 4. The box

Finish with a checklist in box form, so the next session can see what was verified without re-deriving it. Every line is a claim that was actually tested, marked `[x]` only if it passed, and every failure stays in the box with its reason.

```
+--------------------------------------------------------------+
| BATCH <n> -- CHECKS                                          |
+--------------------------------------------------------------+
| [x] machine check      ......... PASS  (name the tool)       |
| [x] second check       ......... PASS  (what a reader sees)  |
| [x] reading review     ......... PASS  (or: N files re-read) |
| [ ] item still open    ......... why it stays open           |
+--------------------------------------------------------------+
```

A box with no open items is a box that is lying about something. If the batch genuinely closed everything it touched, say what it did **not** touch.

---

## Why the second check exists

Three separate times the machine check and the reader check disagreed, and the reader was right:

1. **`first- person` ×42.** Every linter passed; a reader hits a word split by a space and stops.
2. **`SE-O-IVδ-515`.** Five Combat Action rows still wrapped in `{{ }}` with real content inside them — the file was complete to every check and unfinished to every reader.
3. **A standalone `| Maximum Amount | 3 |` line** inserted by a script into 190 records: valid Markdown, renders as literal pipes, invisible to a checker that only asks whether a row exists.

And once the reader check itself was wrong: a CRLF line ending made `### Appearance` unmatchable, and 71 good edits were reported as 71 defects. **Check the checker before believing it** — especially when it agrees with what you expected.
