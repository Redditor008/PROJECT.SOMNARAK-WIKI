# How to Write an SE Quote

> Owner's direction, 2026-10-07: *"DO The Quote One First Because That An Identity And Learn How To Write SE Quote."*

Every Sorrow Entity dossier opens with an H1, then exactly one blockquote, then `## SECC Classification`. That blockquote is
the dossier's identity: the first thing a reader meets, the thing the file is remembered by, and — per the clone audit — the
single strongest clone call in the archive. A duplicated quote lifts the chance of a cloned section inside the pair
eighteen-fold: **18 / 84 = 21.4%** against a **1.20%** archive baseline (`CLONE_AUDIT_2026-10-07.md`, Finding 7). One quote,
one identity, one dossier.

## What the archive already does (measured 2026-10-07, `tools/auditors/quote_audit.py`)

- **301 / 301** dossiers carry a quote; **275** distinct strings; **270** appear exactly once. The remaining **5 quote
  families / 31 dossiers** are exact duplicates (table below).
- Length: **5–46 words**, median **15**; half fall between **8 and 32**. The five family quotes sit at the short end
  (8–10 words).
- Shape (over the 270 once-only quotes): **one sentence 188**, two sentences 61, three or more 21. The modal opening is a
  definite article or a pronoun: "The" 39, "It" 19, "A" 16, "She" 15, "They" 15, "He" 11, "Every" 8, "I" 5.
- Voice: a third-person statement of what the holding is or does. Second person is rare ("you" 7.8%, "we" 3.7%), and a
  question is almost never used (**0.0%**).
- Marks: em dash in **38.1%**; digits in **0.7%**; the word "entity" in **0.7%**. The quote is not a stat line and not a
  definition.
- Format: `> *"…"*` — one blockquote line, straight double quotes inside italics (older files use curly quotes; new quotes
  use the straight pair).

## The five families (everything still duplicated)

| Family quote | Members | Keep-side (lowest designation) | Copies to re-author |
|---|---|---|---|
| "It does not end. It merely pauses between heartbeats." | 8 | Grimoire `C-IIβ-906` | 7 |
| "The city gave us this. We did not ask for it." | 7 | Breathing Stone `C-IVδ-907` | 6 |
| "The weight is not punishment. It is recognition." | 6 | Glass Elsewhere `N-IIβ-903` | 5 |
| "When it comes, you will know. Everyone knows." | 5 | Beating Relic `C-IIIγ-902` | 4 |
| "Something here remembers what we chose to forget." | 5 | Vellum Man `C-Iα-900` | 4 |

The **lowest designation** in a family keeps its quote — it is the pre-cover-up text, and it becomes unique the moment the
copies are re-authored (the same `--lineage` rule the clean phase used). Every other member gets a quote of its own.

## Rules for a new quote

1. **The identity test.** The quote must be true of this holding and of no other dossier. Before writing it, run
   `python3 tools/auditors/quote_audit.py --check "<text>"` — the check must report no match.
2. **No name, no code, no figure.** Not the entity's name, not a registry code, not a number: the quote is not the record.
3. **One breath.** One to two sentences, 8–32 words. If it needs a third sentence, the file has not decided what it is.
4. **Present tense; no question, no exclamation.** The archive holds none.
5. **Use the file's own furniture** — its object, room, sound, shift, or rule, drawn from its own flavor text, Story Log or
   work notes — never from the family it was copied with.
6. **Leave the blockquote in place.** Replace the line where it stands; nothing is deleted (`R-15`) and the file's word
   count does not fall.

## Procedure for a fix

1. Read the file: SECC line, `감각 묘사 (Flavor Text)`, Story Log Entry 1, its own figures, its M.A.W. weapon name.
2. Draft the quote in its own register — the voice of the people who keep the record, or of the sorrow itself.
3. `quote_audit.py --check "<draft>"` — no match, word count inside the band.
4. Replace the blockquote line in place; run the per-dossier checks (`verify.py`, `sectfile.py`, `tpl.py`, `wikistd.py`).
5. Commit and push the unit (`A0`); one `gate.sh` for the docs row (`R-12`).
