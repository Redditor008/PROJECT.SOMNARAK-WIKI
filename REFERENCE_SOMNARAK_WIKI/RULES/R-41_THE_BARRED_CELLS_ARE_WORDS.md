# R-41 — The Barred Cells Are Words, Read Off the Threat Score

**The owner's instruction, verbatim (2026-11-03):**

> *"The Threat Point Thing I Mention I Used It From Our Conversion Guide you know the 2–10 things. Also You Dont Write 0% or -100% On Dossier It Look Bad Think It Like This Net-Neutral And Negative-Low."*

Two changes in one sentence, and the second depends on the first.

## 1. The two barred cells are written as words

| the cell | what it says on the page | the mechanic behind it |
|---|---|---|
| **Net-Neutral** | the work is spent and nothing is netted | the activation threshold does not come down, the gauge does not move, and no benefit is paid for the watch |
| **Negative-Low** | the attempt is not an attempt | the activation threshold goes to 0 and the gauge fills to 100%: it activates on the work |

The mechanics are batch 157's, unchanged and verified — *"won't lower the threshold and won't give benefit"* for the first, *"literally just dropping the threshold to 0 and filling gauge to 100%"* for the second. What changes is the label, because `0%` and `-100%` read as **statistics** on a page whose business is not statistics. A Warden reading `-100%` sees a modifier; a Warden reading **Negative-Low** sees a verdict about what happens when somebody tries.

**A dossier may not print a percentage where one of these belongs.** `tools/auditors/check_work_preference.py` reports `percentage-token` for any cell or Work-preference vector that still carries `0%` or `-100%`. The legacy tokens still *parse* — a half-migrated tree must not report a false alphabet failure — but they cannot survive a gate run.

## 2. The Threat Score is the guide's 2–10, not a gauge reading

The barred pair is one reading, and the number it is read off is the **Threat Score** in `PROJECT_MOON_RESEARCH/CROSS_VERSE/PM_ABNORMALITY_TO_PS_SORROW_ENTITY_CONVERSION_GUIDE.md` §III:

> **Threat Score is Coherence rank + Potency rank (I/α = 1 … V/ω = 5)**, and the sum sets the level exactly as the Universal Table's Chapter 4 sets it: **2–3 ZAYIN · 4–5 TETH · 6 HE · 7–8 WAW · 9–10 ALEPH.**

So the scale runs **2 to 10**, both numbers are already filed on every dossier (`**Coherence**` and `**Potency**`), and the cut is the band boundary:

| Threat Score | L Corp level | barred cells |
|---|---|---|
| **2–3** | ZAYIN | **Net-Neutral** |
| **4–5** | TETH | **Net-Neutral** |
| **6** | HE | **Negative-Low** |
| **7–8** | WAW | **Negative-Low** |
| **9–10** | ALEPH | **Negative-Low** |

**The level name may not be printed on a dossier.** The sentence on the page reads *"at a threat score of 6 or more"* and stops there: `ZAYIN · TETH · HE · WAW · ALEPH` is the L Corp-side name the arithmetic produces, and the Conversion Guide is explicit that it *"appears in this guide and the Universal Table and in no dossier anywhere"*. The first draft of batch 159 wrote *"— HE and above —"* into 75 dossiers and `compare_conversion_guide.py` caught it in the gate.

**6 is where a holding stops being an inconvenience** — HE is the first tier that is a major problem — and it is also the first tier whose gauge band begins at 500 — the band that since `R-48` bounds a **charge wall** rather than a resting reading — which is why the earlier `Sorrow Gauge ≥ 500` reading agreed with it on 144 of 149 dossiers. The five it did not agree on were re-read in batch 159 and the gauge was the thing that was wrong: the Threat Score is filed on the same page by two fields that cannot drift, and the gauge is one number that can.

## 3. What batch 159 changed

- **149 dossiers** carry the two words: 298 cells and 298 mechanic sentences (`136 + 162`).
- **Five dossiers were re-read** from `Negative-Low` to `Net-Neutral` because their filed pair sums to 5 or less: `C-IIIβ-015` The Debt Scale (III + β = 5), `C-IIIβ-036` The Cracked Hourglass (5), `C-IIIβ-072` Father's Broken Bond (5), `N-Iα-905` Lacrima (I + α = **2**), `O-IIγ-007` Brume (II + γ = 5). Their tails were rewritten to their own substance rather than swapped wholesale: a scale that only weighs what is owed, sand that runs out of the crack, a clasp that was already snapped, a bowl that keeps what it was given, fog that takes a gesture and gives no account of it.
- **Five relics** keep `Negative-Low` (III + γ = 6) and now say so: *"the threat score 6 (III + γ)"* where they used to say *"the threat point 653/653"*.
- The guide, both SE templates, `WORK_RESPONSE_LAW.md` and the review ledger were updated in the same commit.

## 4. Where it is enforced

| auditor | line | what it holds |
|---|---|---|
| `check_work_preference.py` | gate 81 | the alphabet, the one-reading pair, the Threat Score rule, `percentage-token`, **and the A-page against its dossier** (§5) |
| `check_work_response.py` | gate 79 | the state signs against the Element matrix (unchanged) |
| `check_relic_work_types.py` | gate 80 | a relic has no Work Types (`R-40`, unchanged) |

**The crowded-vector ratchet moved from 172 to 176, and this is a re-take, not an easing.** Four of the five re-read dossiers land on the second most crowded vector, because the rule that decides those two cells is not a free choice. The measure is recorded as it was found after the rule changed; nothing was rewritten to make a state look different.

## 5. The A-page and its dossier are one holding, filed twice

The Side Codex A-page carries the Warden's copy of the work table; the dossier carries the record of what was measured. They were written one at a time, so they could say different things about the same holding — and after batch 159 fixed the dossiers and batch 160 fixed the A-pages, nine still did.

**The rule is three sentences.** Bar status has to agree: if the dossier files both works as valid, the A-page may not carry a barred word, and if the dossier bars the pair the A-page must carry it. The word has to be the one the page's own designation wants. And a compound — `Net-Neutral / escalation`, `Negative-Low / contextual` — is refused, because a reader cannot act on a verdict that is conditional.

**Which side moves is decided by the record, not by seniority.** Where a page applied a generic place protocol to a holding whose dossier records specific grief that worked — Briar's thicket stalling under an offer, Devouring Bloom's front moving for a shift — the page was wrong. Where the dossier said *"Barred."* in prose and then priced the row as if it worked, the dossier was wrong. The dossier is the record; the page is the instruction written from it.

**Evidence, 2026-11-04:** 223 A-pages carry a work table, 446 barred rows. Nine stood against their dossier; all nine are settled above, and the rule reports **0** on the tree. It also prints, separately, how many pages cite a code no dossier files — **0** — because a rule that passes by measuring nothing is the failure this batch exists to prevent.

**The pair-equality rule reached the Subjects too.** It had only ever run on relics, because a relic's two cells are the ones the Two-Work-Type Rule bars. Thirteen Subject dossiers bar both cells on their own record, and nothing checked that the two words matched. It does now, for every dossier and every A-page: one Threat Score cannot produce two words.

**A first draft asked every A-page for a barred word and reported 98.** They were almost all Subject pages, whose Flerehan and Pugnahan are valid work: the rule was asking the wrong question of the right files. The bar belongs to the holding, and the dossier is where the holding says so.

**Not covered by the rule, and known:** 41 A-pages carry a codename their dossier does not (`Rootless` / Floating Tree), with the same code, so nothing disagrees mechanically; and an A-page's `Type / Manifestation` may name a second half the dossier does not (`Subject — Place-Grudge` against `**Subject** — Can breach`), which is how four of the nine arose. Both are recorded in `WORK_IN_PROGRESS.md`, batch 161.
