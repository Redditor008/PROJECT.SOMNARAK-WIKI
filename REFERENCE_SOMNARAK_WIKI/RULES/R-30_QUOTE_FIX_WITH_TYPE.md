# R-30 — A Quote Fix Carries The New Quote And Its Type

**Stated by the archive owner, 2026-10-07:** *"Also If Fixing Quote Add In The NEW QUOTE TO CHECK WITH IT TYPE
YOU SHOULD WROTE IT AS A RULE"*.

A quote is the dossier's identity (`SE_QUOTE_GUIDE.md`); the fix that replaces one therefore has to prove two
things at once — that the new line is *this* holding's and no other's, and that the voice is a voice the writer
chose. A new quote without its type is half a record: the next reader can see the sentence but not why it is
allowed to sound the way it does.

## The rule

1. **Every quote fix records, in the same push, the new quote verbatim and its register type** — one of `R1`–`R8`
   from `ABNORMALITY_QUOTE_RESEARCH_2026-10-07.md` (entity speaking · addressed to you · documentary · fable ·
   elegy · question · found speech · aphorism). The owner's reporting format for quote fixes stands: the new
   quote and its type; no generic-mass, words or commit columns (`R-16` fractions do not apply to quote rows).
2. **The type is chosen when the quote is written, not inferred afterwards.** Decide the register before drafting;
   if `--file` reads back a type other than the one intended, the quote is redrafted or the intent is corrected —
   a mismatch between what was written and what is recorded is a failed fix.
3. **Read-back before the push.** `python3 tools/auditors/quote_audit.py --file <path>` must report the written
   quote, its type, and `no exact duplicate` (a file's own quote is not counted against itself). `--check "<draft>"`
   is still run on the draft first; the read-back is the check on what actually landed.
4. **The ledger entry is part of the fix.** Regenerate `REFERENCE_SOMNARAK_WIKI/QUOTE_REGISTER_LEDGER.md`
   (`quote_audit.py --ledger …`) in the same commit: the new quote must appear there against the same type.
   A quote fix that leaves the ledger stale is unfinished, exactly as a unit that is not pushed is unfinished (`A0`).
5. **`R-12` link-both-sides stands** (`R-12`): the record links the fixed dossier *and* the source keeper whose
   quote it was copied from.
6. **`R-15` stands:** the blockquote line is replaced in place; nothing deleted, and the file's word count does not fall.

## How it is checked

| Command | What it must say |
|---|---|
| `quote_audit.py --check "<draft>"` | no exact duplicate; inside the 5–46 word band; flags named |
| `quote_audit.py --file <path>` | the written quote, **its type**, `no exact duplicate` |
| `quote_audit.py --verify` | `301 / 301 quotes typed`; `duplicate families: 0 / 301`; census per type |
| `quote_audit.py --ledger REFERENCE_SOMNARAK_WIKI/QUOTE_REGISTER_LEDGER.md` | regenerated ledger — new quote present, same type |

The classifier is the deterministic first-match order in `tools/auditors/quote_audit.py`; the taxonomy and its
genre evidence are in `ABNORMALITY_QUOTE_RESEARCH_2026-10-07.md`. Register *variety* across the wing is a goal
(`SE_QUOTE_GUIDE.md`), not a threshold; this rule requires only that each quote's type is recorded and consistent.

## Baseline at the time of writing

Quote phase closed with **0 families / 301 / 301 distinct** (`549313b`); ledger baseline: R8 **197 / 301** ·
R2 **27 / 301** · R5 **25 / 301** · R3 **16 / 301** · R1 **15 / 301** · R1b **13 / 301** · R4 **7 / 301** ·
R7 **1 / 301** · R6 **0 / 301** — the wing still speaks mostly in one voice, which is the next quote work's problem,
now measurable in the same command that records each fix.
