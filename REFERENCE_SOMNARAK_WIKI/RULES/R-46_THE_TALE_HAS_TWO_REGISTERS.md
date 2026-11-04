# The Tale Has Two Registers

**The rule.** `이야기 (Narratio) — The Tale` is written in exactly **one of two registers**,
and each dossier declares which one by how it opens. There is no third.

| | **Normalised Story** | **Fairy Tale** |
|---|---|---|
| what it is | a filed account — somebody's job was to write this down | a folktale — the kind of story a district tells about itself |
| who is speaking | a named officer, clerk, warden, keeper, archivist | no one; the voice belongs to the teller's tradition |
| opens with | a filing header: *Filed by / Report of / From the desk of*, then a date | a formula: *Once / There was / Before there was a city / Long ago* |
| time | dated, Year 4,2xx | undated — *before the city*, *in those years* |
| people | named, with a post attached | roles: the woodcutter, the girl, the mother, the third son |
| institutions | named and doing something | absent, or appear as *the collectors* with no office |
| how it ends | on a filing decision — what was recorded, what was refused, what is attached | on a turn or a moral — *and it is still there* |
| Project Moon parallel | the Story Log | The Snow Queen · The Red Shoes · Beauty and the Beast · Warm-Hearted Woodsman · Little Red Riding Hooded Mercenary |

The two are not a quality ranking. Project Moon uses both, and which one an Abnormality
gets is a fact about the entity: a holding that came out of a district's own telling is a
fairy tale; a holding that came out of an incident, a ledger or an extraction is a filed
account.

## The thing that is neither

The essay is not a third register. It is what the archive had in place of both, and it is
the AI default:

> Somnarak is always in a hurry, and the hurry has weight. … Mortality is part of it —
> citizens die, citizens Fracture, citizens run out of days — but mortality is only the
> largest version of a smaller, daily truth … What is spent is spent. What is wasted is
> wasted. What is over is over. … The crack is the point.

No author, no teller, no date, no name. It explains the entity's meaning in the vocabulary
of a thesis, and it breaks the owner's guideline at §5.1 (*every document has an author
with an agenda*) and §1.5 (*humans are not narrators*). A Tale that opens this way is in
neither register and must be rewritten into one.

## How to choose

Ask: **who is telling this, and why do they have the telling?**

- If the answer is a person with a post — a clerk asked for the ninth time why the quotas
  cannot be met; an archivist who will not mark a blank as *cause unknown*; a warden filing
  a recommendation the Directorate has already refused once — it is a **Normalised Story**,
  and it opens on their byline and their reason.
- If the answer is nobody, and the story is one the district says about a place or a thing
  — a child who would not come home, a river that was grief before the city was built, a
  bird that watched a market burn — it is a **Fairy Tale**, and it opens on the formula.

A Tale that cannot answer either question has no reason to exist in the dossier.

## What the registers may not do

Both registers are bound by `R-45` — the owner's Banned List, the 75/25 Project Moon
weighting, and the section contracts. A fairy tale is not a licence for purple prose: it
uses *plainer* words than a filing, not richer ones. *"Before the city there was a river,
and the river was grief"* is a fairy tale. *"A symphony of sorrow danced across the
waterway"* is neither.

A Normalised Story is not a licence for an omniscient narrator either. The clerk knows
what is in the register and no more, and says so.

## Applying it

1. Decide the register from the entity, not from convenience.
2. If Normalised Story: write the byline and the reason first. The rest follows.
3. If Fairy Tale: write the formula, keep the nouns plain, end on the turn.
4. Never leave a thesis sentence, a negation-and-correction, a rhetorical triplet, or an
   announcement of significance anywhere in the section.

Gate `check_tale_register.py` (91) classifies every Narratio on the markers above and
**fails on any Tale that reads as neither**. It reports the split, so the archive can be
seen moving toward two registers rather than drifting in a third.

## Owner direction

Batch 188, 2026-11-04: *"TALE HAVE TWO CATEGORY OF WRITING NORMALIZE STORY AND FAIRY TALE
TYPE OF WRITING."*

## The rollout: what the gate fails and what it only reports

The gate draws a line that matters. **The essay is a defect and fails the build. An
undeclared plain narrative is a backlog item and is reported.**

The difference is what the section is *doing*, not what word it opens with.

* A Tale that carries a thesis, a negation-and-correction, a rhetorical triplet, an
  announcement of significance, or an abstract noun personified is **the essay** — a third
  register the owner never asked for. It fails, and it cannot be repaired by adding a
  byline, because the voice underneath is still the essayist's.
* A Tale that tells a story plainly, in the third person, with no commentary about its own
  significance, is **already in a register**. It has not yet said which. That is a
  bookkeeping debt, and the fix is an aperture or a byline, not a rewrite.

The gate counts the second as `plain narrative, no register yet`. That number must fall to
zero, and it is tracked in the rollout register below.

### The two cheap conversions

**Folk-manner, missing only the aperture.** Most of the backlog is narration that already
reads as a folktale — *"They took the wall down, and they made it unlawful to count the two
sides, and the second of those is why the line is still there."* The body is the register;
the opening just has not declared it. Re-voice the **first sentence only**, keeping every
fact in it:

> `The market emptied, and one stall refused to forget…`
> → `There was a market that emptied, and one stall stood in it and refused to forget…`

**Filed-manner, missing only the byline.** Narration with a named person and a post —
a diver, a Keeper, an organizer — is a Normalised Story that has not been filed. Add the
header above the body and a signed line below it. Rewrite nothing else unless the body ends
on the essayist's habit (see below).

### The ending to cut on sight

`Some sorrows [verb] X. This one is about Y.` closes a large number of Tales. It is not a
turn and it is not a filing decision; it is the essayist telling the reader what to feel
about a story he has just been shown. Delete it and end on the event. R-45 §5: what a gate
cannot check is whether the section trusts the reader.

### Rollout register

| reading | Normalised Story | Fairy Tale | plain, undeclared | the essay |
|---|---|---|---|---|
| batch 188, first run | 4 | 21 | 272 (21 of them the essay) | **21** |
| batch 188, after the 21 essays were rewritten | 16 | 25 | 256 | **0** |
| batch 188, after the first apertures | 19 | 53 | 225 | **0** |

The essays are gone. The remaining 225 are bookkeeping, and they come down 20–30 a batch.
