# Unfinished-Text Register

> *"A file that stops mid-sentence is not a record; it is a note to somebody who never came back to it."*

**Status: closed again, on both scans.** Every truncation that ends a line has been completed and the end-of-line scan returns zero. A second kind then surfaced that no end-of-line scan could see: a sentence cut mid-clause with another fragment fused onto the same line *after* the break, so the line ends on a full stop and looks finished. **79 of these were found in the dossier wings and all 79 are completed.** The 26 mid-line ellipses that remain were each read and judged deliberate — dramatic pauses in dialogue and testimony, and the pause in "It is not hostile. It is simply… heavy." Seven trailing ellipses were read, judged deliberate, and left in place; they are not counted here.

## Final tally

| Class | Fault | Half | Count |
|---|---|---|---|
| **A** | Flavor Text — "At first contact" cut mid-clause | batch | 63 |
| **B** | Story Log origin paragraph cut at "This sorrow …" | batch | 103 |
| **B2** | The same paragraph, cut one sentence earlier | batch | 22 |
| **C** | Identification — Primary marker cut mid-phrase | batch | 31 |
| **F** | `\| **Form** \|` cell cut dead at 150 characters, **no ellipsis** | batch | 30 |
| **E5** | `Threat rating:` fused onto the origin paragraph, itself truncated | careful | 13 |
| **D-unique** | One-off prose truncations, each in a single file | careful | 15 |
| **D-shared** | Six shared Story Log paragraphs, each cut mid-sentence | careful | 35 |
| **G1** | Origin paragraph cut mid-clause with a `Threat rating:` field fused on after the break | batch | 31 |
| **G2** | Flavor Text cut mid-clause with the following sentence fused on after the break | batch | 48 |
| | **Total completed** | | **391** |

Batch half: 249. Careful half: 63.

## Fix standard applied

Every sentence was completed from the entity's own material in the same file — its form, its site, its element, its recorded effect — and never with a clause reused from another dossier. Where a line fused two fragments, the fragments were separated and each given its own field; in every such case the half that had been hidden turned out to be truncated as well.

Division of labour follows `RULES/R-18`. **Batch-short** meant the completing text already existed in that file. **Careful-detail** meant it had to be written, one file at a time.

## Notes on each class

**A — 63.** Sixty-one completed from each entity's own recorded form; two carried a description found nowhere else in their file and were written individually.

**C — 31.** Identification markers restored from each dossier's Physical Form entry. Taken first because an instruction for recognising an entity is read at the moment of contact, and one that stops mid-phrase is unusable exactly then.

**B — 103, B2 — 22.** Origin paragraphs completed from each file's Expanded origin context, so the closing cadence matches that entity's element. B2 is the same fault cut one sentence earlier; it survived the first pass because the surviving text ended on a lower-case *but* while the scan was anchored on a capital.

**E5 — 13.** Thirteen B lines had a `Threat rating:` field fused onto the end. Separating them exposed thirteen further truncations underneath. Each was completed from that entity's recorded Sorrow and Secondary Effect.

**F — 30.** Thirty `| **Form** |` cells were cut dead at 150 characters, mid-word, with no ellipsis of any kind — invisible to every scan built to look for one. Found by diffing the cell against the file's own `**Primary Form:**`, which held the full text in all thirty cases.

**D-unique — 15.** Eleven Story Log and Archive Note paragraphs written out individually, and four Flavor Text lines whose trailing form description was restored from their own Primary Form.

**D-shared — 35.** Six paragraphs that appeared word for word across many dossiers and stopped mid-sentence in all of them. Completing them with one shared ending would have cleared thirty-five ellipses and left the archive worse, since the truncation was the only thing marking the paragraph as boilerplate. Each was replaced with prose written for its own entity: the Compass corridor where instruments agree with a bone needle instead of north, the willow enclosure that has to be swept, the clock that stops when a debt comes due and makes the silence the event.


## Class G — mid-line truncation (cleared)

The break sits in the middle of the line and a fragment of unrelated field text is fused on after it, so the line terminates in a full stop and reads as complete until it is read as a sentence. One instance, found by eye during the Sleeping Shard clean, ran `…But this sorrow was different. This sorrow was …  Threat rating: Per entity classification.`

**G1 — 31.** The origin paragraph completed from the file's own Expanded origin context, and the `Threat rating:` field separated onto its own line. Twenty-nine spliced; two sat in shared paragraphs with no in-file source and were written individually, for Candela and for Every Last Goodbye.

**G2 — 48.** The Flavor Text contact line embeds the entity's own form description, and in these files that description was cut mid-phrase before the next sentence was fused on. Restored by the same anchor-splice used for class A: the longest prefix of the file's own Primary Form that is a suffix of the broken text marks the join.

After the splits, the end-of-line scan was re-run. It returned zero, so no second truncation was hiding underneath this time.

### What this class cost

This is the second defect in the archive to be invisible to the scan written for it, after the thirty `| **Form** |` cells cut at 150 characters with no mark at all. Both were found by reading a file, not by scanning the archive. The rule is recorded in `RULES/R-18`: a scan written around a symptom finds only the cases that show the symptom.
