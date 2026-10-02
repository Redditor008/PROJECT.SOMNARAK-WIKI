# R-18 — Divide Every Defect Set Into Batch-Short and Careful-Detail

## The rule

Before fixing a set of defects, split it in two and say which half each item is in.

- **Batch-short.** The correct text already exists somewhere in the same file. The fix is to move it, splice it, or separate it. These are done by script, all at once, with asserts.
- **Careful-detail.** The correct text does not exist yet and has to be written. These are done one at a time, by reading the file, and the result is different in every file.

The split is stated with counts before any fixing starts, and both halves are reported separately afterwards.

## What this forbids

- Running a single script across a mixed set. The careful half will come out of it looking fixed and reading as boilerplate.
- Treating "the same sentence is broken in forty files" as evidence that one replacement will serve. It is evidence of the opposite: a sentence shared by forty files is already a defect under `R-14` before it is truncated, and completing it with a shared clause makes it worse while hiding the ellipsis that advertised it.
- Hand-writing fixes for items whose completion is sitting ten lines up in the same file. That is slow, and it invents text where the record already had it.

## What this permits

- Mechanical completion, with no per-file authorship, whenever the completing text is that file's own material — `R-04` is satisfied because the text is already the entity's.
- Scripted structural surgery: splitting a line that fused two fields, restoring a cell truncated at a fixed width, re-attaching a continuation.

## How to decide which half an item is in

Ask one question: **can I name the field in this file that already holds the right answer?**

If yes — the Form cell, the Physical Form row, the Expanded origin context, the Primary Effect, the Sorrow row — it is batch-short.
If no, or if the answer would have to be the same words used in another dossier, it is careful-detail.

## Traps

- **A truncated line that appears in many files is almost always careful-detail, and it will look like the easiest batch in the set.** The six shared Story Log paragraphs in this archive were cut mid-sentence in thirty-five files. One completion would have fixed thirty-five ellipses and created thirty-five identical endings.
- **Batch-short is not low-risk, it is low-authorship.** It still needs a per-item assert that the replacement is longer than the original, that the source field is not itself truncated, and that exactly one match was found.
- **Finishing the batch half does not reduce the careful half.** Report the two counts separately so the remaining work is not flattered by the batch.
- **A defect can hide with no ellipsis at all.** Thirty `| **Form** |` cells here were cut dead at 150 characters, mid-word, with no mark. They were invisible to every ellipsis scan and were only found by comparing the cell against the file's own `**Primary Form:**`. When one field is supposed to mirror another, diff them; do not scan for punctuation.
