# The Owner's Standing Orders

**What this is.** Every instruction the archive owner has given for this project, in one place,
in his own words, with where it now lives and whether it has been done. The dossiers were built
by many hands and drifted; this is the register that stops the drift, because an order that is
only in a chat log is not a standard — it is a memory.

**How to read an entry.**

| field | meaning |
|---|---|
| **Your words** | quoted verbatim. Where a quote is a paraphrase the entry says `[paraphrase]`. |
| **What it means** | the ordinary-language reading, so the rule can be applied without guessing. |
| **Lives in** | the rule file that now carries it. |
| **Checked by** | the gate that fails the build if it is broken. `—` means nothing checks it yet. |
| **Status** | **DONE** · **OPEN** (not done) · **PARTIAL** (some files) · **STANDING** (permanent) |

---

## A. The world — what may exist at all

### O-01 · Nothing non-in-world in the world folder
**Your words (batch 139):** *"NEVER ADD ANYTHING THAT IS NON-IN-WORLD STUFF IN SOMNARAK WORLD FOLDER."*

**What it means.** `SOMNARAK-WORLD/` contains only what a citizen of Somnarak could hold in their
hands. No build notes, no meta commentary, no "this was updated in batch N", no scaffolding.
**Lives in:** `R-01`. **Checked by:** `check_world_purity.py`. **Status:** DONE.

### O-02 · No dates from our world
**Your words (batch 140):** *"WHY IS THERE A DATE OF OUR WORLD IN A DOSSIER"*

**What it means.** The calendar is Somnarak's: `Year 4,231`, not 2026. A real-world date in a
dossier breaks the fiction on the first line the reader sees.
**Lives in:** `R-01`. **Checked by:** `check_ordeal_dates.py`. **Status:** DONE.

### O-03 · Project Moon is the sister universe, not SCP alone
**Your words (batch 186):** *"DONT USED ONLT SCP USED ITS SISTER UNIVERSE PROJECT MOON"*
**Your words (batch 187):** *"STILL AFTER THIS RELEARN AND RERESEARCH P.M."*

**What it means.** The reference tradition is Project Moon first — Lobotomy Corporation's
Abnormalities, Work Types, Story Logs, E.G.O — and SCP second. Research is continuous, not a
one-off.
**Lives in:** `R-29`, `R-44`. **Checked by:** — **Status:** STANDING.

### O-04 · 75% Project Moon, 25% other
**Your words (batch 187):** *"75% P.M. BECAUSE ITS A SISTER VERSE AND 25% OTHER VERSE."*

**What it means.** Three quarters of the reference weight is Project Moon; one quarter is other
traditions. Written out as a weighting table in `R-45 §0`.
**Lives in:** `R-45 §0`. **Checked by:** — **Status:** STANDING.

---

## B. The dossier's shape — what a file must contain

### O-05 · Four work types, in a fixed order
**Your words:** `[paraphrase — batch 155/157]` *four works, fixed order, and all files that
mention an SE must agree.*

**What it means.** Flerehan · Pugnahan · Viderehan · Ferrehan, always in that order, and the
A-page, the dossier and the M.A.W. record must say the same thing about which are valid.
**Lives in:** `R-41`. **Checked by:** `check_work_preference.py`, `check_set_agreement.py`.
**Status:** DONE.

### O-06 · `N/A` is retired from the barred cells
**Your words (batch 158):** *"N/A"* — banned from barred cells.

**What it means.** A barred cell is a verdict, not a blank. It reads **Net-Neutral** or
**Negative-Low**, because *"a Warden reading N/A sees a gap where a judgement should be."*
**Lives in:** `R-41`. **Checked by:** `check_barred_prescriptions.py`. **Status:** DONE.

### O-07 · Never write `0%` or `-100%`
**Your words:** *"Also You Dont Write 0% or -100% On Dossier It Look Bad Think It Like This
Net-Neutral And Negative-Low."*

**What it means.** Percentages read as statistics on a page whose business is judgement.
**Lives in:** `R-41`. **Checked by:** `check_work_preference.py` (percentage-token).
**Status:** DONE.

### O-08 · A relic is handled, not worked
**Your words:** *"THIS IS NEW RULE NO RELIC SE WILL HAVE WORK TYPE INSTEAD HAVE HANDLING
PROCESS THAT MEAN YOU NEED TO UPDATE P.S.md, R.D.md And Everything Else That Mentions SE So It
Will Match With Our Current SE 'TEMPLATE'."*

**What it means.** A subject has `## Behavior` with four work rows. A relic has
`## Handling Process` with stages — approach, handling, withdrawal, refusal — and a
`**Handling**` row instead of `**Valid Work Types**`. There is nothing in a relic to work.
**Lives in:** `R-40`. **Checked by:** `check_relic_work_types.py` (ratchet 131).
**Status:** **OPEN — 131 of 143 relic dossiers still carry Work Types.**

### O-09 · Consequence means the cost of working on it
**Your words:** *"The meaning of consequence to all SE is: there will be a cost on working on
them, and what the cost is based on what they are and what they do. Try to research L Corp stuff
— work damage, work interaction, and much more."*

**What it means.** Every holding charges the person who works it, in its own terms — not "causes
sorrow" but what it takes and from where.
**Lives in:** `R-43`, `R-44`. **Checked by:** `check_consequence_register.py`.
**Status:** DONE (14 noted, deliberate).

### O-10 · Work Damage and Work Preference — the L Corp block
**Your words (batch 175):** *"consequence includes the cost of working on an SE."*

**What it means.** Every dossier carries Work Damage (amount + type, in band) and a Work
Preference level on each open cell. Rolled out in batches 174–191.
**Lives in:** `R-44 §2`, `R-44 §2.1`. **Checked by:** `check_work_damage.py`,
`check_work_preference.py`. **Status:** DONE — 294 of 294 dossiers carry a preference level.

### O-11 · T Counter, not Q
**Your words (batch 176):** *"T Counter, not Q."*

**What it means.** The counter is Somnarak's own, read against the Threshold. Missing terms go
into their logical section, not bolted on at the end.
**Lives in:** `R-06`. **Checked by:** `check_gauge_chain.py`. **Status:** DONE.

### O-12 · Tiers differ in sight and in action
**Your words:** `[paraphrase — batches 171–174]`

**What it means.** ZAYIN/TETH/HE/WAW/ALEPH are not a difficulty slider; each tier perceives
differently and acts differently. A Special Case reads **HIGH THREAT**. A thing that cannot be
worked is **un-workable**, not *unauthorized*. The three termini carry no Work Type, no
Counter-Gauge and no M.A.W. line.
**Lives in:** `R-42`, `R-35`. **Checked by:** `check_special_abnormality.py`,
`check_threat_form.py`. **Status:** DONE.

### O-13 · Not everything breaches, fights, or is a subject
**Your words:** *"is the event a breach, activation, or expansion"* · *"Can you fix a lot of SE
that should never have combat"* · *"Can You Make Sure Not All SE is Breaching SE Because…"*

**What it means.** A file must answer which event it is and stop claiming combat it never had.
**Lives in:** `R-28`, `R-36`. **Checked by:** `check_event_claims.py`. **Status:** DONE.

### O-14 · Subject shape diversity
**Your words:** *"What About Diversity On Shape and Look … For Subject There Cant Be Just One
Type Of Shape At Minimum Four Human, Monster, Animal, And Abstract … Example One Sin And Singing
Machine."*

**What it means.** At minimum four shapes across the subjects; not every holding is a humanoid.
**Lives in:** `R-32`. **Checked by:** — **Status:** PARTIAL.

---

## C. How it must read — the voice

### O-15 · Refine, do not expand
**Your words (batch 181):** *"YOU NEED TO REFINE A LOT OF SE BECAUSE WHEN I TRY TO READ THEM IT
MAKE MY HEAD HURT REFINE NOT JUST EXPAND"*

**What it means.** The problem is not length. Adding words to a confusing passage makes it a
longer confusion. Cut, sharpen, split. Wordcount going up is a warning sign, not an achievement.
**Lives in:** `R-45 §0.2`. **Checked by:** — **Status:** STANDING.

### O-16 · Inflation is not a fix
**Your words (batch 142/143):** *"inflation, not a fix."*

**What it means.** Padding a thin section with adjectives is the same failure as leaving it thin,
disguised. A section earns its length with content.
**Lives in:** `R-45`. **Checked by:** `check_form_line.py` (upper bound). **Status:** STANDING.

### O-17 · No cutting rule
**Your words:** `[paraphrase]` — refine may not become deletion.

**What it means.** Refining removes confusion, not facts. Nothing in the record is deleted to
make a paragraph read better; it is rewritten until it reads and still holds everything.
**Lives in:** `R-39`. **Checked by:** — **Status:** STANDING.

### O-18 · Write-and-chain
**Your words:** *"Also when fixing by writing instead of erasing or cutting used logic for
whatever you're fixing, and the logic needs to chain to one another."*

**What it means.** A fixed paragraph must connect to the paragraph above and below it. Repairing
one sentence so it contradicts its neighbours is not a repair.
**Lives in:** `R-39`. **Checked by:** `section_logic.py`. **Status:** STANDING.

### O-19 · Reader logic and L Corp writer logic, not AI logic
**Your words (batch 183):** *"Check Again For Unnecessary Word … Used Reader Logic + L Corp
Writer Logic Instead Of AI Logic."*

**What it means.** Every sentence must survive two tests: can a reader follow it in one pass, and
would an L Corp writer have put it that way. Words that exist to sound impressive fail both.
**Lives in:** `R-45 §0.2`. **Checked by:** `check_ai_prose.py` (reported). **Status:** PARTIAL —
311 essayist constructions still reported.

### O-20 · No AI prose — the banned list
**Your words (batch 187):** *"I SEE A LOT OF AI PROSE/WRITING"* · *"TRY TO READ THE STORY WRITING
GUIDELINE TO SEE WHAT AI STUFF THAT I MEAN"*

**What it means.** The twelve banned constructions in your guideline are hard failures:
*"a palpable wave of X"*, *"the weight of Y"*, *"in that moment"*, *"something changed"*,
*"a testament to"*, *"the air crackled with ozone"*, *"reverberates"*, *"tapestry"* and the rest.
The guideline you sent is filed at `RULES/SOURCE_Unified_Narrative_Writing_Rules_for_AI.md`.
**Lives in:** `R-45 §0.1`. **Checked by:** `check_ai_prose.py`. **Status:** DONE — 0 banned hits.

### O-21 · Concrete, not vague — the middle
**Your words (batch 184):** *"Also Some Has Really Vague Description … So Basically You Right Now
Doing QoL"*
**Your words (batch 185):** *"NEW APPEARANCE … NOT OVER OR VAGUE ALSO STILL UPGRADE MORE SE AS A
WHOLE"*

**What it means.** The Convergence Appearance is the exemplar of the failure: description that
could belong to anything. Say the ordinary noun, the plain colour, the size, the state. Not
over-written, not under-specified — the middle.
**Lives in:** `R-45 §2`. **Checked by:** — (the keyword scorer was deleted; keyword frequency is
not evidence). **Status:** PARTIAL — measured by size only.

### O-22 · Every section to its contract
**Your words (batch 186):** *"…ReLearn Every Section In SE Dossier On All Category"*

**What it means.** Eleven sections, eleven different jobs. Appearance describes, Origin explains,
Behavior answers work, Testimonium gives testimony. Writing tale-voice into a stat table is the
failure.
**Lives in:** `R-45 §3`. **Checked by:** `section_logic.py`, `check_form_line.py`.
**Status:** PARTIAL.

---

## D. The Tale

### O-23 · The Tale has four registers
**Your words (batch 188):** *"TALE HAVE TWO CATEGORY OF WRITING NORMALIZE STORY AND FAIRY TALE
TYPE OF WRITING"*
**Your words (batch 189):** *"WHAT IF TALE CATEGORIZE INTO THIS STORY TALE, FAIRY TALE, DIALOGUE
STORY, And HYBRID[It Mean It Can have Dialogue Or Like How Most Of L Corp Abnormality Story
Structure/Look Like]"*

**What it means.** `이야기 (Narratio)` is one of four: **Story Tale** (a filed account),
**Fairy Tale** (a folktale the district tells), **Dialogue Story** (a transcript — the Queen of
Hatred form), **Hybrid** (a filed account that kept the words). The essay is none of them and
fails the build.
**Lives in:** `R-46`. **Checked by:** `check_tale_register.py`. **Status:** PARTIAL —
116 declared, **0 essays**, 181 still plain.

### O-24 · Dialogue must carry its feeling
**Your words:** *"you only used plain text for dialogue and not at all used any styling on how
the dialogue should feel … Is Majin screaming, shouting, OR scared I can't see it because there
no flare."*
And: *"IF THE TITLE IS IMPORTANT IN THE STORY THAN THAT WILL BE NEEDED AS A TITLE … THE MIX STYLE
OF GIVING TITLE OR NAMING."*

**What it means.** A speaker line is not enough; the reader must know how it is said, and a title
that matters gets set as a title.
**Lives in:** `R-24`, `R-46`. **Checked by:** — **Status:** STANDING.

---

## E. Presentation

### O-25 · Links must be absolute and live
**Your words (batch 180):** `[paraphrase]` — absolute live GitHub URLs, on the SE name.

**What it means.** `[SE-C-IIIβ-014 The Debt Eater](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/28e0dc28-project-somnarak-wiki/…)`
— clickable, resolving, never a bare path.
**Lives in:** `R-12`, `R-31`. **Checked by:** `check_links.py`. **Status:** DONE — 0 broken.

### O-26 · Link the files you fixed, not a report about them
**Your words (batches 178–179):** `[paraphrase]` — link the SE files fixed.

**What it means.** The chat report must let you open the thing that changed.
**Lives in:** `R-31`. **Checked by:** — **Status:** STANDING.

### O-27 · The chat report must be readable
**Your words:** *"Update/Overhaul The Chatroom Written Text Report Its Look Ugly And To Clutter"*
· *"Refine The Chatroom Text Into A More Readable Fill Information Not Just AI…"*

**What it means.** Tables, short lines, no wall of prose, every SE named and linked.
**Lives in:** `R-31`. **Checked by:** — **Status:** STANDING.

---

## F. Process — how the work is done

### O-28 · `P` means proceed and push
**Your words:** *"So P"* · *"P P"*

**What it means.** Do the work and push it in the same turn. Do not stop to ask again.
**Lives in:** `R-17`. **Status:** STANDING.

### O-29 · Double-check, then read, then tick
**Your words:** *"Each time you try to fix or check things you do double check, and the second
check used reader viewing logic; than after finished fixing you do reading review with logic;
than you can check it in check list/box."*

**What it means.** Check it · check it again as a reader · read it back as a reviewer · then mark
it done. Marking before reading is the failure.
**Lives in:** `R-38`. **Status:** STANDING.

### O-30 · Fixed, not labelled
**Your words:** `[paraphrase]` — a fix is a change to the file, not a note saying it was fixed.

**What it means.** If the answer is a table entry saying "resolved", nothing was resolved.
**Lives in:** `R-15`. **Status:** STANDING.

### O-31 · Batch size and the full gate set
**Your words:** *"Do It Per 5 in Batch"* · *"Always 3 or 5 then 7 or 10"*.

**What it means.** Work in batches, and run the whole gate set before pushing — never a partial
check followed by a push.
**Lives in:** `R-25`, `R-26`, `R-11`. **Checked by:** `tools/gate.sh`. **Status:** STANDING.

### O-32 · Whole file, cross-checked
**Your words:** `[paraphrase]` — fix the whole file, then cross-check it against the files that
mention it.

**What it means.** A dossier is not five independent sections; editing one obliges you to check
the ones that reference it.
**Lives in:** `R-34`. **Status:** STANDING.

---

## The open list

These are the orders that are **not** satisfied today. This is the honest state of the archive.

| # | order | measure | why it is still open |
|---|---|---|---|
| **O-08** | relic Handling Process | **131 of 143** | The largest single unfixed order. Each file needs its Behavior section rebuilt as a four-stage Handling Process. |
| **O-23** | Tale registers | **181 plain** | 116 declare a register; 181 Tales read as a story but never say which. Cheap per file, many files. |
| **O-19** | no AI constructions | **311 reported** | Down from 332. Every one needs a sentence rewritten, not deleted. |
| **O-21** | concrete, not vague | unmeasured | No checker exists. Held by reading only. |
| **O-22** | section contracts | partial | Form lines: 188 under 40 words · 7 over 130 · 86 repeat their own marker · 134 thin. |
| **O-14** | subject shape diversity | partial | Not audited. |
| — | duplicated sections | **2,269 pairs** | `Appearance`↔`Detailed Appearance Profile` in 233 files. |
| — | A-page titles | **41** | A-page carries a title its dossier does not. |
| — | The Maw | 1 conflict | Stat line 22–34 against `SE-1003-B` 14–24; A-page forbids extraction while three records exist. |
| — | R-45 §2 contradiction | 1 | The rule says 60–110 words; the gate allows 40–130. Must be settled before any form-line sweep. |
| — | PR #15 title | 1 | Still reads *"The barred cells are words: batches 159-169"*. |

---

## Owner direction

This register is itself an order — batch 192, 2026-11-04:

> *"CAN YOU WRITE DOWN ALL MY COMMAND OF EVERY THING THAT I TOLD YOU TO FIX BECAUSE THE OLD
> DOSSIER IS SUPPER MESSY AND UNPROFESSIONAL"*

It is maintained as the project's single source of truth for what was asked. A new instruction
becomes an entry here before it becomes a change to a dossier.
