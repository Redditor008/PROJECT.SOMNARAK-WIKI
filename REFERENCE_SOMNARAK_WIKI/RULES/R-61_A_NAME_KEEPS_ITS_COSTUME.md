# R-61 — A Name Keeps Its Costume

**Stated by the archive owner, 2026-10-25:**

> *"ALSO SOME IN THE STORY NEED HIGHLIGHTING LIKE P.S. SPECIFIC TITLE AND SUCH SO IT ABLE TO BE KNOW BY
> READER THAT IT WAS A TITLE OR ELSE AND NOT JUST NONSENSE"*

*P.S.* is Project Somnarak — the house style, not a postscript. He is asking for the archive's own way of
marking a name, used everywhere, so that a reader meeting a word for the first time can tell a title
from a typo.

**Amended the same day, second instruction:**

> *"I ALSO MEAN LIKE THIS EXAMPLE 'The Endurers said it was grief with nowhere to go. The Converters said
> it was grief that could be made useful. The Council, which had inherited both schools and believed
> neither, called it a resource and taxed it.' BECAUSE FROM OUTSIDE PERSPECTIVE IT SOUND LIKE IT WAS NOT
> A TITLE"*

He is right, and the reason is exact. **Every one of those three names opened a sentence.** At the start
of a sentence every word is capitalised, so the capital carried no information, and an outside reader
parsed *Endurers* and *Converters* as ordinary plurals — people who endure, people who convert — rather
than as the names of schools. The mark was there and it was invisible. That produced § 2b and § 2c.

## 1. What was wrong

The same designation was written four ways inside one file:

| where | form |
|---|---|
| The Filing, at its coinage | `**THE ORIGINAL**` |
| three later uses | `*the Original*` |
| the appendix heading | `the Original` |
| the record quote | `THE ORIGINAL` |

Four costumes for one name read as four unrelated things. Worse, four names were used **with no mark at
all**: *the Hand* (first met in a heading, 500 lines before anything explains it), *the Absolvohan*,
*Reaper Hungered*, and *Ω*. A reader encountering `the Hand` in `## Before the Hand Opened` cannot tell
whether it is a structure, a person, or a hand.

That is what *"just nonsense"* means as a defect: not that the words are ugly, but that **the page has
given the reader no way to know what kind of thing each word is.**

## 2. The rule

**Every name in the archive is marked by what it is, with one mark per class, held for the whole file.**

| class | mark | example | why this mark |
|---|---|---|---|
| **Designation** | full caps, always | `THE ORIGINAL` | A label standing where a name should be. Caps say *this is a filing, not a description of her.* |
| **Named thing** | italic at its coining, roman after | `*Reaper Hungered*` → `Reaper Hungered` | An entity, weapon, account or structure the record has named. Marked **once**, at the moment the reader needs to know it is a name; after that the capital letters carry it. |
| **Body** | capital article | `The Endurers`, `The Council of Sighs` | A faction, school, order or council. A capital article is how English says *this is part of the name*. |
| **Office** | plain, lower case after *the* | `the Director`, `the Archive Lead` | A post, not a person, and never a name. |

Four things follow:

**A. The mark is set by what the thing is, not by how important it is.** A designation is caps even when
it appears in a table; a named thing is italic even when it appears in a shout.

**B. A name is coined before it is used.** If a movement heading carries a name — `## Before the Hand
Opened` — the prose that follows must show what the thing is. A heading is not a coining. The Hand of
Change is introduced standing in the middle of it: *five spires set around a palm-shaped court, one for
each finger*.

**C. A short form needs a long form first.** `the Hand` is legal because `*the Hand of Change*` was
coined; `the Cycle` is legal because the disclosure names it in full. Never the reverse.

**C2. A mark must be visible.** A mark that falls only where convention forces a capital has no
meaning. At the start of a sentence, *The Endurers* and *the endurers* look identical on the page; in a
heading, every word is capitalised and nothing is marked. **A name is coined mid-sentence**, in prose,
where the reader can see what the typography is doing.

**C2b. The capital article is a coining mark, not a permanent costume.** `The Endurers` at the moment the
reader is told what they are; `the Endurers` afterwards, exactly as a named thing goes roman after its
italics. A capital article held through every possessive — *not on The Council's instruction* — stops
reading as a title and starts reading as a typo, which is the failure in the other direction.

**C3. A body must be shown to be a body.** `The Endurers` is only a title if the page says what they are
a body *of*. The sentence above was rebuilt to do that: six schools argued it through the Occlusihan, two
survived as schools, and *the body that did the inheriting was The Council of Sighs*. A capitalised word
does not become an institution because it is capitalised; it becomes one because the sentence says so.

**D. The legend is printed in the file.** Every Extended file carries a `REGISTER` line in its record
header stating the three marks, because the convention only works if a reader is told it once. That line
is part of the file, not a note about the file.

## 3. What this is not

**It is not decoration.** Marking a name does not make it good. `*Reaper Hungered*` passes whether it is
evocative or embarrassing; the gate reads the costume, not the tailor.

**It is not the caps ban.** §XII.1c forbids caps on a **roman line of dialogue** — a quiet line set in
caps reads as shouting. A designation is not a line of dialogue, and its caps are the opposite of volume:
they are the mark of a filing.

## 4. The gate

`tools/auditors/check_title_register.py` (gate 55). It holds a declared map per file — each designation
with the casings that are wrong for it, each named thing with its coining, each short form with the long
form it depends on — and fails on any of them drifting, on a name used before it is coined, and on a file
carrying no `REGISTER` line at all.

Measured 2026-10-25: **`01_MAJIN` holds 1 designation, 10 named things, 3 bodies and 1 short form, at 0
defects**; all nine extended files carry the legend. The gate fails a body whose first use is
sentence-initial, which is how the original tricolon is now caught.

What it cannot do is decide whether a name is *worth* having. That is the reader's pass (`O-29`, `R-38`).
