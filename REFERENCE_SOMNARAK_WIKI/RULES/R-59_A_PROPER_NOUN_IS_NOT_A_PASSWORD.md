# R-59 — A Proper Noun Is Not a Password

**Stated by the archive owner, 2026-10-25:**

> *"DO MORE AND ALSO MAKE EVERYTHING MORE CLEARER AND UNDERSTANDABLE AND MORE DRAMATIC AND EMOTIONAL
> NOT PLAIN, GENERIC AND STALE"*

## 1. What was wrong

Reading `01_MAJIN` cold, the first fifty pages hand a reader this:

> *"She gave it. Envelope, Veil, conduits, gauges, Maw."*

Four of those five words name a system in a city the reader has not been shown. The file explained the
**Consolihan twice**, in two separate scenes, and explained the **Veil** never. The **Cheongula** was
first named as a place a man's sister died in. **Cheonbulok** was a set of families with a cable. **Ω**
was a letter in a header. **Reaper Hungered** was an asset with no account of where a name like that
comes from.

That is the specific failure the owner's word *"clearer"* names. It is not that the prose is difficult.
It is that the prose **asks the reader to carry vocabulary instead of a story**, and the reader's
response to an unexplained proper noun is not confusion and a question. It is to stop asking and skim
past it — which is the same thing as not reading.

## 2. The rule

**Every corpus term a reader cannot infer from the page is glossed at the point where the reader first
meets it — in the voice of the file, in the same breath, without stopping the scene.**

Five things follow:

**A. First use, not best use.** A gloss in scene nine does not help a reader who met the word in scene
two. The first use is the only use that counts.

**B. The gloss is one clause, not a footnote.** `Han — the substance the whole city sat on and had
never once agreed about —` costs eight words and carries the whole world. An appendix, a glossary or a
parenthetical dump is the same failure in a tidier dress: it tells the reader the book is homework.

**C. Prefer the gloss that does a second job.** The best glosses in this file also characterise whoever
is speaking or explain why the word matters. *"The Veil was the suppression net laid over the districts
that made them livable and numbed them"* explains a system and the city's whole bargain at once.

**D. Gloss the substance, not the sound.** A fantasy term is not clarified by a synonym the reader also
does not know. *The Weeping is a river of liquid Han* is a gloss only because *Han* has already been
glossed.

**E. Never gloss twice for the same reader.** A second definition reads as the author distrusting the
first one. After the gloss, the word is a word.

## 3. The gate

`tools/auditors/check_backstory_gloss.py` (gate 54). For each Extended file it takes a fixed list of
corpus terms no reader can infer — *Han, Cheongula, Consolihan, Weeping, Veil, Maw, Fracture,
Absolvohan, Cheonbulok, Alpha Tree, Reaper Hungered, Echo-Core* — finds the first use of each **in the
narrative body**, and requires an explanatory construction **adjacent to that use**: an appositive dash
within 110 characters, a parenthesis within 70, a copular definition within 60, or a cue phrase in the
same window.

Adjacency is the whole design. An em-dash anywhere in a two-sentence window matches every third sentence
in this corpus and would certify nothing; the first draft of the gate did exactly that and passed all
nine files while the Veil was still unexplained.

Measured 2026-10-25 after the pass: **all nine extended files at zero cold terms.** The other eight were
not glossed when this gate was written — they carried 34 between them — and the table that would have
recorded them is now empty, which is a better state than a debt of zero.

**What it cannot check:** whether the gloss is true, or good, or short enough not to stop the scene.
That is the reader's pass (`O-29`, `R-38`).
