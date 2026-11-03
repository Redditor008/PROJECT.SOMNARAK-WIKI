# SE CLOCK AUDIT — every span a repair introduced

**Batch 152.** Batch 150 replaced 37 numerals with durations, on one rule: *a numeral is never swapped for another numeral — use the dossier's own clock.* The rule was right. Its application was not checked, and batch 152 found why it needed to be: reading `SE-C-IIβ-901` end to end, the repair called a **forty-eight-year** beat record **nineteen years** old.

The file says *"every handler in forty-eight years"* three times, *"the tissue has not degraded in forty-eight years"*, *"extraction has been sought twice in forty-eight years"*. The nineteen came from the corpus — nineteen years is the commonest span in the archive, and it was the span the repair reached for.

## Every span introduced, re-read against its own file

| # | dossier | span introduced | the file's own span for that record | verdict |
|---|---|---|---|---|
| 1 | `SE-C-IIIγ-033` Guarding Bird | nine years | **eleven** — *"stood posts for eleven years"* | **wrong → corrected** |
| 2 | `SE-C-IIIγ-033` Guarding Bird | nine years | **eleven** | **wrong → corrected** |
| 3 | `SE-C-IIIγ-115` Remembrance | nine years | nine — *"risen eleven centimetres in nine years"* | ok |
| 4–6 | `SE-C-IIIγ-928` Lethe | nineteen years | nineteen — *"across nineteen years"* ×9 | ok |
| 7 | `SE-C-IIβ-777` Last Fruit | nine years | nine — *"every trading day for nine years"* | ok |
| 8 | `SE-C-IIβ-901` Duri's Heart | nineteen years | **forty-eight** — *"every handler in forty-eight years"* | **wrong → corrected** |
| 9 | `SE-C-IIβ-901` Duri's Heart | nineteen years | **forty-eight** | **wrong → corrected** |
| 10 | `SE-C-IVγ-205` Hollow Tree | nineteen years | **nine** for the relocations (*"31 relocations in nine years"*), ninety-one for the rotas | **wrong → span removed** |
| 11 | `SE-C-IVγ-205` Hollow Tree | nineteen years | as above | **wrong → span removed** |
| 12 | `SE-C-IVδ-193` Rift | nine years | nine — *"1.1 metres to 2.9 in nine years"* | ok |
| 13 | `SE-C-IVδ-869` Rising Well | nine years | nine | ok |
| 14–16 | `SE-C-IVδ-907` Breathing Stone | nineteen years | nineteen — *"Nineteen years, 188 cycles…"* | ok |
| 17 | `SE-C-IVδ-909` Labyrinth | nineteen years | nineteen | ok |
| 18–22 | `SE-C-IVδ-918` Ninety Seconds | nineteen years | nineteen | ok |
| 23 | `SE-C-Iα-622` Vanished Tree | nine years | nine — *"from nineteen to four in nine years"* | ok |
| 24 | `SE-C-Iα-884` Seething Tundra | eleven years | eleven | ok |
| 25 | `SE-C-Vδ-265` Forgotten God | nineteen years | nineteen | ok |
| 26 | `SE-N-IIIγ-127` Mirror of Broken | nine years | nine | ok |

**26 spans. 6 wrong, in 3 dossiers.** Every wrong one failed the same way: the span was taken from the corpus rather than read out of the file that was being edited.

## The repairs

| dossier | was | is |
|---|---|---|
| Duri's Heart | *Nineteen years of the beat record* | *Forty-eight years of the beat record* |
| Duri's Heart | *across nineteen years of the beat record* | *across forty-eight years of the beat record* |
| Guarding Bird | *nine years of the post's record* | *eleven years of the post's record* |
| Guarding Bird | *runs nine years* | *runs eleven years* |
| Hollow Tree | *Nineteen years of sittings have closed that way and the tree has moved 31 times* | *Every sitting has closed that way, and the tree has moved 31 times* |
| Hollow Tree | *across nineteen years of sittings without exception* | *across every sitting without exception* |

Hollow Tree is the interesting one. Rather than pick between nine years (the relocation rate) and ninety-one years (the rotas), the span came out: *"every sitting"* is what the record actually establishes, and a number that cannot be defended should not be printed.

## Why this class cannot be gated

A duration is legitimate in one dossier and wrong in the next. *"forty years of heavy labour"* is a comparison, *"six years of Grudge holdings"* is a specialist's career, *"thirty years of life"* is a cost — none of them is a series length, and a dossier can honestly hold four different spans at once. Two candidate rules were measured on the corpus:

| rule tested | flags | true defects |
|---|---|---|
| a span must be the dossier's modal duration | 28 | 3 |
| a span must be corroborated anywhere in the file | 25 | 0 (Duri's file holds nineteen years too — for the suit) |

Both are worse than useless as a gate: they would have failed seventeen correct sentences to catch three wrong ones, and the second would not have caught Duri at all, because the number *was* in the file — attached to a different object.

**What caught it was reading one file end to end.** That is now the ledger's job: `tools/reading_ledger.py` records which dossiers have been read, names the batch and the finding behind each claim, and ranks the unread ones by how many repairs they have taken — because a dossier edited three times is the one most likely to carry a defect created by an edit.
