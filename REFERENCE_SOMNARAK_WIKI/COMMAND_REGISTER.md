# The Command Register

**What this is.** Every instruction the owner has given for this project, gathered into one place,
in the order it was given, with what it built and where it now stands. `OWNER_DIRECTIVES.md` holds
the **standing orders** — the ones that became permanent law. This file holds **everything else**:
the reformations, the sweeps, the audits, and the one-off corrections, indexed so that no command
lives only in a chat log.

**Batches run 1 to 238.** The numbered record is complete from batch 52; batches 1–51 are recorded
by subject in `WORK_IN_PROGRESS_VOL_01.md`, `VOL_02.md` and the earliest `CHANGELOG` entries, before
numbering settled.

---

## How the commands arrive

| form | meaning |
|---|---|
| **`p`** | *proceed and push* — a destination, refined in batch 201 into a seven-step method (`OWNER_DIRECTIVES.md`, *The `p` directive*) |
| **`P P`** | the same, with the emphasis that the turn is to be a complete unit |
| a sentence of direction | a reform, a standard, or a correction — the substance of this register |
| **batch sizing** | `R-25`/`R-26`: 3 → 5 → 7 → 10 files per batch, never fewer than three |

**The seven steps of `p`, because every command below is executed this way:** read the words back →
refine them into a testable claim → measure before changing → refuse invention → make the change in
one unit (rule, gate, sweep, every file that quotes it) → verify the whole suite and read the count
lines → push, then say what is still open.

---

# Part I — The named reformations

Eighteen programmes, in the order they were opened. Each entry gives **what you said**, **what it
meant**, **what changed**, **where it lives**, **what checks it**, and **where it stands today**.

---

## 1. The Dossier Reformation — the first sixty batches

**What you said.** That the entity files were not yet an encyclopaedia: sections were
inconsistent, codex sets contradicted their dossiers, and the M.A.W. equipment blocks were
boilerplate. `[paraphrase — batches 1–60]`

**What it changed.** The nine parity sections (`R-29`: *"What You Do Is Just Basically Do What An
Abnormality Wiki Do But Better For SE"*), the four work types in fixed order, the Tale as the
prose benchmark (`R-24`), and the first stock-clause sweeps.

**Where it lives.** `R-03` · `R-04` · `R-23` · `R-24` · `R-29`.
**Checks it.** `check_stock_clauses.py`, `section_logic.py`, `check_slot_templates.py`.
**Status.** **PARTIAL.** The structure is done — nine parity sections, four work types in fixed
order, a Tale slot in every file. The prose standard has since been raised twice (§8, §13) and the
remainder is measured, not estimated: **308** essayist openers, **181** dossiers with no Tale,
**134** thin form lines, **86** form lines repeating their own marker, **7** dossiers over their
rank's stat ceiling. Calling this DONE was the archive's oldest overstatement; the numbers were
always in `how_finished.py`, and nobody read past the PASS line.

---

## 2. The M.A.W. Reformation — batches 52–56, 68, 172

**What you said.** *"Two Suits that described weapons"*; the equipment sets were three sentences
of stock text and one set described another set's weapon. `[batch 74]`

**What it changed.** Every set given its own weapon, its own cost, and its own bearer tax
(`R-37`: five pieces of each kind per entity, falling only four ways). **287 pieces** on file,
**284 of 287** carried through the appearance pass. Six holdings that cannot be worked were
carrying equipment anyway and were stripped (batch 172).

**Where it lives.** `R-37`, `MAW_EQUIPMENT_MASTER_REGISTRY.csv`, `AUDITS/MAW_PERSONALIZE_PROGRESS.md`.
**Checks it.** `check_maw_stock.py`, `check_maw_sets.py`, `check_set_agreement.py`.
**Status.** DONE.

---

## 3. The Codex Reformation — batches 66–68

**What you said.** *"the 528 legacy codex records, read rather than counted"* `[batch 68]`, and
earlier, that a codex page and its dossier were printing two different standings.

**What it changed.** **528 legacy codex records** read individually rather than bulk-replaced;
then, in batch 160, **124 A-pages / 247 barred rows** given the same words as their dossiers, and
in batch 161 the two collections made to agree by rule rather than by eye.

**Where it lives.** `R-41`, `check_work_preference.py` gate 81.
**Checks it.** `check_work_preference.py` — *"217 pages carry a work table; 0 stand against their
dossier"*.
**Status.** DONE.

---

## 4. The Conversion-Guide Reformation — batches 84–86, 105–107, 128, 159, 163

**What you said.** That the conversion guide the archive was using had drifted from the world it
described: it prescribed a rule the owner had retired, and it was being read against itself
instead of against the dossiers.

**What it changed.** The guide audited line by line three times, an **AP table found a whole band
out**, and — batch 163 — *"the guide the owner named was still prescribing `N/A`"* corrected.
`compare_conversion_guide.py` now fails a guide that names a tier inside a dossier.

**Where it lives.** `GUIDES/`, `compare_conversion_guide.py`.
**Checks it.** `compare_conversion_guide.py`.
**Status.** DONE; the guide is checked against the world, not against itself.

---

## 5. The Appearance Reformation — batches 116, 147–156, 171, 180–187

**What you said.** That Appearance was the weakest section in the archive: vague comparisons with
no referent (*"wider than the chamber it forms in"*), materials named but never placed, and
appearances that were never written at all. You named **The Convergence** as the example and were
right. `[batches 116, 183, 184]`

**What it changed.** Five waves:

| wave | what it did |
|---|---|
| **116** | the header and the appearances that had never been written |
| **147–156** | the independent appearance review series — **692 review files**, five dossiers at a time, HELD only when the change survives a reader pass |
| **182** | all **301** files refined for long sentences and semicolon splices |
| **183** | the **over-explanation** taken out — 294 dossiers, **19,469 words removed, no fact removed** |
| **184–187** | the vague descriptions made picturable — *"wider than the chamber"* replaced with a measurable span; the **form line** introduced and enforced |

**Where it lives.** `R-45 §2`, `SE_CONCRETE_APPEARANCE.md`, `SE_FORM_LINE_185.md`,
`AUDITS/APPEARANCE_PROGRESS.md`, `SE_APPEARANCE_REVIEWS/`.
**Checks it.** `check_form_line.py` (over-130 = 0 PASS; **thin 134**; **marker repeats 86**),
`check_concreteness.py`.
**Status.** **PARTIAL — 3 of 5 closed.** The ceiling is enforced; 134 thin form lines and 86
marker repeats are still ratcheted, and the review series sits at *Types 286/301, Weapon 284/287,
SE 18/301*.

---

## 6. The Work-Preference Reformation — batches 155–163

**What you said.** *"Also You Dont Write 0% or -100% On Dossier It Look Bad Think It Like This
Net-Neutral…"* and *"TALE…"* — that a barred work is **a word**, read off one threat number, not a
percentage and not two separate checks.

**What it changed.** `N/A` retired outright; `0%` and `−100%` banned; **Net-Neutral** and
**Negative-Low** made the only two words a barred cell may carry, both read from the same threat
score (`R-41`); `R-42` made threat readable off the form rather than the designation. Then batch
166–167 found `R-23` itself still teaching the retired token.

**Where it lives.** `R-41`, `R-42`.
**Checks it.** `check_work_preference.py` — *off alphabet 0 · printing a percentage 0 · side codex
0 disagreements*.
**Status.** **DONE.**

---

## 7. The Handling Reformation — `R-40`, batches 154–202

**What you said.** *"NO RELIC SE WILL HAVE WORK TYPE INSTEAD HAVE HANDLING PROCESS."*

**What it changed.** A relic has no work types at all. Its mechanical section is
`## Handling Process` — four stages, **Approach · Handling · Withdrawal · Refusal** — and its core
table reads `**Handling**`. The gate opened at **131 relic dossiers still worked** and closed at
**0**: all **143** converted, with each file's stages drawn from its own `### Watch Sequence` and
its `[**Refusal**]` contact event, not a template. 121 rows distinct out of 121.

**Where it lives.** `R-40`.
**Checks it.** `check_relic_work_types.py` — **0 remaining, ratchet 0**.
**Status.** **DONE (batch 202).** The largest single reform in the archive's history.

---

## 8. The Refinement Reformation — batches 179–187, 200

**What you said.** *"YOU NEED TO REFINE A LOT OF SE BECAUSE WHEN I TRY TO READ THEM IT [reads
illogical / feels bloated]"*, *"inflation, not a fix"*, and — batch 200 — *"A HARD LIMIT THAT IS
UNIVERSAL FOR ALL RELIC SE."*

**What it changed.** Refine, never expand (`R-45 §0`); a fix writes a replacement and chains it to
the logic around it (`R-39`); no cutting as a substitute for refining (`O-17`, carried by `R-39`); the **form line**
ceiling at **130 words** (batch 200 trimmed 7 lines, moving prose into Appearance rather than
deleting it).

**Where it lives.** `R-39`, `R-45`, `R-14`.
**Checks it.** `check_form_line.py`, `check_fix_density.py` (measured on every commit pair),
`check_banned_ai.py`.
**Status.** **STANDING** — a permanent method, not a finished sweep.

---

## 9. The Consequence Reformation — batches 174–177, `R-43`

**What you said.** *"Consequence in general, not just the section. I mean consequence in how the
SE interacts with agents, other SE, and more — and consequence in broader terms."*

**What it changed.** Consequence read across **three registers** — personnel, peer, institution —
with the register required to match the tier: a Top holding's loss must reach a wing or a district,
a Common one may not. Batch 177 finished the last 52 Top records and batched the field taxonomy into
the world document.

**Where it lives.** `R-43`.
**Checks it.** `check_consequence_register.py` (gate 40).
**Status.** **PARTIAL — failures 0, reported 14.** `check_consequence_register.py` (gate 40) prints
`RESULT: PASS` above **14** dossiers whose consequence cell it reports but does not fail — HE
consequences claiming city scale, **HE=10 · TETH=4**. A pass over a non-zero count is a ratchet,
not a finish: those 14 are open, and they are open *for you to rule on* rather than to be edited to
suit a regex.

---

## 10. The Charge Reformation — `R-47` / `R-48`, batches 193–201

**What you said.** First: *"Also Do Relic SE Need HP, ATK Still Can But It Interaction Dmg As In
The Longer The Agent Used/Equip/Hold It The Higher The Dmg Taken…"* Then, when the gauge was
written: *"TRANSFORMS THE HP NUMBER INTO A MEANINGFUL GAUGE…"* · *"IT STILL READ ILLOGICAL … AND
FEEL BLOATED"* · *"inflation, not a fix"* · *"ARENT 60 s Is Super Short I Mean Some SE Goes Up To
More Than 60s That Is Above 2 m"* · **`2 m` meaning two minutes.**

**What it changed, in five drafts.** The gauge fills from **000** to a wall fixed by grade — **240
/ 420 / 660 / 880 / 1,080** — and the wall is **six doses of that holding's own clock**:

```
Indumentum / worn            10 s →  60 s    50 relics
Officium / Hazard            15 s →  90 s    12
Arcanum / Time               20 s → 120 s    15
Offertorium / Object / Place 30 s → 180 s    57
⇒ 84 of 134 above a minute · 72 at two minutes or longer
```

`[HP]` retired on non-breaching relics (kept on the 9 possessions); run-down a tenth of the length,
one minute; at the wall the relic is spent and the first dose lands at once.

**Where it lives.** `R-47`, `R-48`.
**Checks it.** `check_relic_gauge.py`, `check_relic_interaction_damage.py` — both 0.
**Status.** **DONE (batch 201).** `2 m` is read as minutes; the size reading was purged from §3.

---

## 11. The Work-Effect Reformation — `R-44` / `R-49`, batches 175–177, 203

**What you said.** *"Can You Add Work Dmg/Buff To Normal SE TOO So Like L Corp When Working With SE
Agent Can Get Hurt Or Buff Base Of The SE And Buff Is Rare So Either Dmg/Neutral/Buff The Agent Who
Is Doing Work On The SE And For Percentage Dmg 65%/ Neutral 25% / Buff 10% Of All SE"*

**What it changed.** Every worked subject now carries one of three verdicts, and the split is a
constant of the setting rather than a per-file guess:

| verdict | count | share |
|---|---|---|
| **Damage** | 101 | 65.2 % |
| **Neutral** | 39 | 25.2 % |
| **Gift** | 15 | 9.7 % |

A gift is **a loan with a ceiling, an end and a price** — `+5–10 Composure/Resilience for the rest
of the cycle`, paid in the holding's own element. The percentages live in the rule, never in a cell.

**Where it lives.** `R-44`, `R-49`.
**Checks it.** `check_work_damage.py` (87), `check_work_effect.py` (88).
**Status.** **DONE (batch 203).**

---

## 12. The Tale Reformation — `R-24` / `R-46`, batches 188–189, 205

**What you said.** *"TALE HAVE TWO CATEGORY OF WRITING NORMALIZE STORY AND FAIRY TALE TYPE OF
WRITING."* · *"STORY TALE, FAIRY TALE, DIALOGUE STORY, And HYBRID [It Mean It can have Dialogue Or
Like How Most Of L Corp Abnormality Story Structure]"*

**What it changed.** The Narratio must be written in exactly one of four registers:

| register | declared | share |
|---|---|---|
| Story Tale | **20** | 6.6 % |
| Fairy Tale | **92** | 30.6 % |
| Dialogue Story | **5** | 1.7 % |
| Hybrid | **3** | 1.0 % |
| plain, no register yet | **181** | 60.1 % |
| the essay | **0** | — |
| no Tale at all | **0** | — |

**120 of 301 — 39.9 %.** The essay has been at zero since batch 188. Batch 205 found **four
dossiers with no Tale at all** and wrote them; the gate now fails above zero.

**Where it lives.** `R-24`, `R-46`.
**Checks it.** `check_tale_register.py`, `check_narratio.py`.
**Status.** **PARTIAL — 120 of 301.** The remaining 181 have not been given a byline they did not
earn; `--next N` lists the closest tranche.

---

## 13. The Section-Contract Reformation — `R-45`, batches 186–199

**What you said.** *"…ReLearn Every Section In SE Dossier On All Category"* · *"75% P.M. because
it's a sister verse and 25% other verse"* · *"I SEE A LOT OF AI PROSE/WRITING"* · *"NOW IT READS
LIKE AN AI WROTE IT"*

**What it changed.** Every section written to its own contract, taken from the SCP Description and
the Project Moon dossier form; a banned-construction list; and the **form line** — one line that
must carry a colour, a material or a number.

**Where it lives.** `R-45` (§0 voice, §0.1 banned, §0.2 essayist, §2 form line, §3 sections).
**Checks it.** `check_banned_ai.py`, `check_form_line.py`, `check_section_contract.py`.
**Status.** **PARTIAL** — AI constructions 0, but thin form lines 134 and marker repeats 86 remain,
and batch 208's reader pass found **29 sections missing across 16 dossiers**: 13 Rank IV–V records
with no `Apex Record`, and 4 dossiers with no closing tail at all. Five of the 13 were written in
that batch; the rest are counted, not estimated (`check_section_registry.py`, gate 93).

---

## 14. The World-Law Reformation — `R-01`, batches 138–140

**What you said.** *"NEVER ADD ANYTHING THAT IS NON-IN-WORLD STUFF IN SOMNARAK WORLD FOLDER."* ·
*"WHY IS THERE A DATE OF OUR WORLD IN A DOSSIER"* · *"Folder law"* (batch 139).

**What it changed.** `SOMNARAK-WORLD/` holds only what a citizen could hold; no build notes, no
batch numbers, no 2026 dates, no meta. The reference folder is where the machinery lives.

**Where it lives.** `R-01`.
**Checks it.** `check_world_purity.py`.
**Status.** **DONE.**

---

## 15. The Report & Link Reformation — `R-12`, `R-17`, `R-31`, batches 12–33

**What you said.** *"You Need To Write The Information In Chatroom More Clearly and More Readable…
Write It As A Must Follow RULE"* · that links must open the file on GitHub, not describe it.

**What it changed.** Absolute live links on every finished file (`R-12`); the compact report form
(`R-31`); the shorthand register (`R-17`); the two-checks-a-reading-and-a-box method (`R-38`).

**Where it lives.** `R-12`, `R-17`, `R-31`, `R-38`.
**Checks it.** `check_links.py` (0 broken), `check_box_symmetry.py`.
**Status.** **DONE / STANDING.**

---

## 16. The SECC Reformation — `R-51`, batches 179–207

**What you said.** *"I Think There Is Something Missing Example SECC Refinement"* — named after the
register had already indexed fifteen reformations without it.

**What it changed.** The two classification rows were given one question each. `Coherence` reads
`Rank (Numeral)`, `Potency` reads `Grade (Greek)`; either may carry a single descriptor of twelve
words or less, and nothing longer. The value is read off the code and cross-checked against the
dossier's own `Designation` field, so a cell cannot disagree with the file it lives in.

The fault was not in the dossiers, mostly — it was between two documents. The template asked for
`{{Rank Written}} ({{I-V}}) — {{Behaviour descriptor}}`; `R-45` §3 said *"values only"*; and no gate
read either, so **7 files had written the pair backwards** (`I — Residue (barely formed)`) and
**5 had let the descriptor become a sentence** — a clause of behaviour with its own verb, exactly
what `R-45` was objecting to. Both are now repaired, and `R-45`'s row points at `R-51` instead of
contradicting it.

**Where it lives.** `R-51`; `R-45` §3 row amended; template lines 70–71 unchanged and now enforced.
**Checks it.** `check_secc_shape.py` (gate 45) — 301 dossiers, 301 `Designation` codes
cross-checked, **0** cells off contract.
**Status.** **DONE** — and gated, which is the distinction this batch was about.

---

## 17. The Capture Reformation — `R-52` / `O-38`, batches 206–209

**What you said.** *"Did You Ever Written Down Or Read The Rule For Example If I Give you Command Or
Commanding Tone You Should Have Added It To Rule Or WIP Isnt There A RULE Like That"*

**What it changed.** The answer was no. The archive had said it three times in prose — *"a rule that
lives only in a conversation will be broken by whoever reads the file next"* (`RULES/README.md`),
*"an order that is only in a chat log is not a standard — it is a memory"* (`OWNER_DIRECTIVES.md`),
*"no command lives only in a chat log"* (this register) — and none of the three was a rule, an order,
or a check. They were preambles, and a preamble describes a habit where a rule binds.

**What the absence cost, measured.** The SECC Refinement was given and was not in this register for
four batches (§16). Three gates were written, tested, indexed, cited, and never added to the build
(`O-37`). Both are the same failure: the command was obeyed and never filed.

**What it now is.** Three destinations — a rule, an order, the record — and a command is finished
when it reaches one. A question that names a missing standard (*"isn't there a rule like that"*) is
an instruction to write the rule, not to answer the question. Unclassified instructions default to
the record rather than to silence, because an entry can be promoted and a lost sentence cannot be
recovered.

**Where it lives.** `R-52`; `O-38`; this §17.
**Checks it.** `check_command_capture.py` (gate 48): every rule named in this register, every order a
row of Part II, every batch inside a declared era, and the declared span reaching the highest batch
on record.
**Status.** **DONE and gated.**

---

## 18. The Hunt Reformation — `R-53` / `O-39`, batch 213

**What you said.** *"If You can find other Command That You Forgotten/Ignore"*

**What it changed.** Three commands were not missing but **mis-stated**, which is harder to see than
an absence:

- **`O-08` claimed undone work.** It read *"OPEN — 131 of 143 relic dossiers still carry Work Types"*.
  The gate had been reading **0** since batch 202. Ten batches of a status that under-claimed.
- **`O-14` claimed a partial no gate can reach.** The four shapes — Human, Monster, Animal, Abstract —
  are not a recorded field; `**Physical Form**` is `Mixed` on 104 of 158 subjects. Classifying them
  would mean a keyword scorer, which `R-15` forbids.
- **Gate numbers named more than one gate.** `gate 92` was cited for both
  `check_relic_interaction_damage.py` and `check_gate_wiring.py`; `gate 93` for both
  `check_relic_gauge.py` and `check_section_registry.py`. No register defined what a number meant.

**Where it lives.** `R-53`; `O-39`; `GATES.md` — every gate numbered by its position in `tools/gate.sh`,
which is derived and cannot drift.
**Checks it.** `check_gate_numbers.py` (gate 49) reconciles the register with the build and fails on a
citation that disagrees. `O-08` is DONE; `O-14` states why it needs a schema change rather than a sweep.
**Status.** **DONE and gated.**

---

# Part II — The thirty-nine standing orders

The permanent law, each with your words where they survive verbatim. Full text in
`OWNER_DIRECTIVES.md`.

| # | order | batch | status |
|---|---|---|---|
| **O-01** | Nothing non-in-world in the world folder | 139 | DONE |
| **O-02** | No dates from our world | 140 | DONE |
| **O-03** | Project Moon is the sister universe, not SCP alone | — | STANDING |
| **O-04** | 75 % Project Moon, 25 % other | — | STANDING |
| **O-05** | Four work types in a fixed order | 155/157 | DONE |
| **O-06** | `N/A` is retired from the barred cells | 158 | DONE |
| **O-07** | Never write `0%` or `−100%` | 156 | DONE |
| **O-08** | A relic is handled, not worked | 154 | **DONE (202)** |
| **O-09** | Consequence means the cost of working on it | 174 | DONE |
| **O-10** | Work Damage and Work Preference — the L Corp block | 175 | DONE |
| **O-11** | T Counter, not Q | 176 | DONE |
| **O-12** | Tiers differ in sight and in action | 171–174 | DONE |
| **O-13** | Not everything breaches, fights, or is a subject | 160s | DONE |
| **O-14** | Subject shape diversity | 165 | PARTIAL |
| **O-15** | Refine, do not expand | 181 | STANDING |
| **O-16** | Inflation is not a fix | 142/143 | STANDING |
| **O-17** | No cutting rule | — | STANDING |
| **O-18** | Write-and-chain | 144 | STANDING |
| **O-19** | Reader logic and L Corp writer logic, not AI logic | 186 | PARTIAL |
| **O-20** | No AI prose — the banned list | 187 | DONE |
| **O-21** | Concrete, not vague — the middle | 184 | PARTIAL |
| **O-22** | Every section to its contract | 186 | PARTIAL |
| **O-23** | The Tale has four registers | 188–189 | **PARTIAL (120/301)** |
| **O-24** | Dialogue must carry its feeling | 176 | STANDING |
| **O-25** | Links must be absolute and live | 12 | DONE |
| **O-26** | Link the files you fixed, not a report about them | — | STANDING |
| **O-27** | The chat report must be readable | 187 | STANDING |
| **O-28** | `P` means proceed and push | 76 | STANDING |
| **O-29** | Double-check, then read, then tick | 116 | STANDING |
| **O-30** | Fixed, not labelled | — | STANDING |
| **O-31** | Batch size and the full gate set | 25/26 | STANDING |
| **O-32** | Whole file, cross-checked | 134 | STANDING |
| **O-33** | A relic charges by the second | 193 | DONE |
| **O-34** | The charge: punishment and limit in one number | 197–201 | DONE |
| **O-35** | A work can cost, cost nothing, or give | 203 | DONE |
| **O-36** | Some holdings have one thing they do | 204 | DONE |
| **O-37** | A gate cited is a gate wired — an auditor named by `how_finished.py` must be invoked by `tools/gate.sh` | 207 | DONE |
| **O-38** | A command ends in a file — a rule, an order, or the register; never only in the conversation | 209 | DONE |
| **O-39** | A number names one gate, and a status is a claim — `GATES.md` derives every number from its position in the build | 213 | DONE |
| **O-40** | Appearance is a category and a way of writing — the shape from the dossier's own form statement, the voice from what is seen rather than what it means | 214 | PARTIAL |
| **O-41** | A file is read once, in order — anchors follow the reader's walk, a skipped scene gets written, and a 1,778-iteration life is not four thousand years | 215 | STANDING |
| **O-42** | The backstory is a story — a person in it, cause shown not named, every proper term glossed, and the last beat belongs to the man the reader met in the Profile | 216 | DONE |
| **O-43** | Build the extended file from the dossier — read the dossier first, § Appearance is a writing brief, the appendix is not the story, L Corp for the look and the guide for the reading | 217 | DONE |
| **O-44** | A death belongs to the person who dies — caused by their own discipline, leaving an object and a changed world; research other verse before writing one; never resolve a deliberate ambiguity | 218 | PARTIAL |
| **O-45** | Clearer, and not plain — every corpus term glossed at first use, and every beat that changes what can happen next dramatized rather than reported | 219 | DONE |
| **O-46** | A name keeps its costume — a designation is full caps, a named thing is italic at its coining, an office is plain; a name is coined before it is used, and every file prints the legend | 220 | DONE |

---

# Part III — The rule index

Every command that became law has a file. **62 rules**, `R-01`–`R-62`.

`R-01` no edit-meta · `R-02` growth-only · `R-03` no label decoration · `R-04` bespoke per entity ·
`R-05` no threshold gaming · `R-06` the threshold is the counter · `R-07` percentage where no
counter · `R-08` dual-state appearance · `R-09` verify borrowed mechanics · `R-10` repeated headers ·
`R-11` full gate set before push · `R-12` refer to GitHub · `R-13` work until broken down ·
`R-14` what boilerplate is · `R-15` clean fix, not cover-up · `R-16` report the counter ·
`R-17` shorthand · `R-18` batch-short versus careful · `R-19` disposition classes ·
`R-20` one fixed denominator · `R-21` five whole-file cleans · `R-22` ten dispositions ·
`R-23` labels may repeat, values may not · `R-24` the Tale standard · `R-25` five per batch ·
`R-26` five, then seven, then ten · `R-27` the standard is per section · `R-28` not everything
breaches · `R-29` an abnormality wiki, done better · `R-30` a quote fix carries its type ·
`R-31` chatroom reports · `R-32` subject shape diversity · `R-33` integrity live check ·
`R-34` full-file audit before any fix · `R-35` the special abnormality · `R-36` not everything
fights · `R-37` the M.A.W. stock ceiling · `R-38` two checks and a reading · `R-39` write and
chain · **`R-40` a relic is handled, not worked** · **`R-41` the barred cells are words** ·
`R-42` threat is read off the form · `R-43` the consequence register · **`R-44` the cost of the
session** · `R-45` write every section to its contract · **`R-46` the Tale has four registers** ·
**`R-47` a relic charges by the second** · **`R-48` the charge** · **`R-49` a work can cost, cost
nothing, or give** · **`R-50` some holdings have one thing they do** · **`R-51` a table row
answers one question** · **`R-52` a command ends in a file** · **`R-53` a number names one gate** · **`R-54` the appearance is a
category and a way of writing** · **`R-55` a file is read once, in order** · **`R-56` the backstory is a story** · **`R-57` build the extended file from the dossier** · **`R-58` a death belongs to the person who dies** · **`R-59` a proper noun is not a password** · **`R-60` the turning point is a scene** · **`R-61` a name keeps its costume**.

*(Bold = the thirteen reform laws of batches 193–216.)*

---

# Part IV — The batch record, by era

**216 batches, 622 commits, 2026-10-22 → 2026-10-25.** What each stretch of the record was for:

| era | batches | what it was for |
|---|---|---|
| **Founding** | 1–50 | the dossier built: nine sections, the Tale as benchmark, the first codex sets |
| **Equipment** | 52–56 | every M.A.W. block states what it takes; the oldest eight sets personalised |
| **Epigraphs** | 58–65 | 42 epigraphs per wave across registries 762–1043 |
| **Stock clauses** | 66–79 | the retired work pair, the charm formula, the doubled article, the archetype openers |
| **Legacy reads** | 68, 84–107 | 528 legacy codex records read individually; the conversion guide audited three times |
| **Numbers corrected** | 108–115 | vocabularies reconciled, 653 blank stock figures closed, every file numbered |
| **Appearances** | 116–156 | the header, the review series, the paragraphs that were never written |
| **Barred cells** | 157–167 | `N/A` retired, the two words installed, the A-pages made to agree, `R-23` corrected |
| **Registers** | 168–177 | consequence across three registers; the tier's cost reaches every rung |
| **Reading** | 178–187 | refine not expand, over-explanation cut, vague made picturable, the form line |
| **The Tale** | 188–189 | four registers; the first Dialogue Stories in the archive |
| **The charge** | 190–202 | `R-40` closed, `R-47`/`R-48` drafted five times, six doses and the minutes |
| **The effects** | 203–205 | three work verdicts, individual SE effects, the Tale measured |
| **The gate audit** | 206–213 | the register itself; three gates the build never ran; SECC given one question per row; a command made to end in a file |
| **The appearance** | 214 | the category read off the section instead of the column; 301 of 301 resolve; prose accepted as a shape; interpretation told from correspondence |
| **The reading** | 215 | the owner read the backstories as a reader; Majin's break found and fixed; the missing climax written; a file now has to be read in the order it states |
| **The person** | 216 | Majin's own page rebuilt: a 365-word classification replaced by a life story, the mishearing given a mechanism, and the present explained by the past |
| **The names** | 220 | every title marked by what it is; the legend printed in all nine files; the Hand of Change coined where a reader stands in it; and the arithmetic of a 126-year-old man who has lived 1,778 years |
| **Put the voice in the dialogue** | 238 | §9 could set volume and break type, and could not make a line sound like anything. Added **the third dial** — volume, vocalization, lettering — and the four rules under it: what emotion does to a voice, stress landing on one word, where the breath is, and the sound that isn't a word. All of it was already in the corpus and unnamed. Added the tenth defect class, **the flat page**, and a read-aloud question to the read-back. |
| **Finish the dialogue standard** | 237 | §9 carried eight dialogue rules and neither of the two failures it exists for. Added the **stacked block** and the **mention compression** as named defects with cures, the balance rule, the body in the room, the share (interview vs. chorus), the welded classifier for a shared office with no name, and a six-question read-back. §9 is now 13 rules; the document is 90 across 25 sections. |
| **Make the writing rules portable** | 236 | The owner's guideline rewritten as a universal edition: 85 rules, 24 sections, eight parts, no setting. Its own numbering ran backwards and its addendum duplicated its delivery rules; both fixed. Added the ledger half it never had — time, names, deaths, turning points, in-world citation, numbers, extending an existing work — plus a twelve-question cold read, a nine-class defect taxonomy, and a six-step procedure for binding it to any project. §1 and §2 kept by number because four documents and one gate cite them. |
| **Update the story writing guide** | 235 | The guide was 151 lines and five counts short of true. It taught a **M.A.W. pendant** — a fourth equipment kind that the codex says does not exist — because *quadripartite* counts the four **files** of a set, not four objects. Counts corrected (290 dossiers, 45 codices, 285 M.A.W. sets), two dead pointers repaired, and three sections added: the Echo-Core backstories, how a scene is written here, and the six traps this session found in its own prose. `R-24`'s dangling path fixed. |
| **Read as a reader** | 234 | not measured — read. His deathlessness was dated **63 days early**, before the fusion that canon says made him immortal, so the fusion scene warned a man who already could not die. A Day 29 debrief stamped 09:00 and a catwalk stamped 14:00 were called *one hour apart*. The frame never said **why he submitted to forty-one questions**. And 233's own new scene re-told a resolution *The Public Archive* already carried — cut from 24 dialogue lines to 14, and the comparison row corrected. |
| **The yardstick, backwards** | 233 | every claim in the dossier searched for in the extended's story body — `R-57` run in the direction it had never been run. His **ending** was missing: Stratum Realization 3, *"I carry the weight"*, *"not a burden — a gift"* had no scene while the source ledger already cited it. Written as **The Room — The Weight** (tenth session, Year 4,238), with the cross-file tension declared in a new HOLD rather than resolved silently. Also: the file used *the Solidification* for two events, keeping "his was not that one" where no reader meets it. Dialogue census stale for the third time (381 → **405**). |
| **The pointer** | 232 | a dossier should act as if it were a dossier, so it must never print the shelf: `R-63`, gate 57, ceiling zero. Four leaks — a filename mid-sentence in the Director's Solidification, a full folder path in a Sorrow-Entity's Archival Note, and filenames in three backstory PROVENANCE lines. **2,276 markdown links were left alone**, because a link renders as its label and never as a filename: the rule is about what a reader can see. The new checker could not see its own founding example until it was fed it. |
| **The stack** | 231 | the owner found the Story dialogue *"squish in one line"*. It was not the Director file: **117 dialogue lines across all nine dossiers** had no blank line between them, so every renderer joined them into one paragraph. Thirteen lines of speech in the dossier's Story had been compressed into mentions — Day 0's report, Day 29's forgiveness, Day 108's gate order, Day 177's instrument argument — and R-60's own named example (*"the city weeps, rages, and hopes"*) was still standing. The M.A.W. event was in the extended and its **name** was not: a reader met an Ω-grade extraction register without being told what was extracted. Glossed, sourced, and recorded in the comparison table. |
| **The integrity** | 230 | three standards at once: the ledger's own cells, the timeline's own spine, and the structure standard. Five ledger rows carried a status the standard does not allow (*ON THE PAGE*); the validation record counted three section headings where there are five; the compliance table gave the Founder's micro-ink line to the Director and invented a reading Insu never did. Row 18 dated a Year 4,238 scene by the warm floor, the doorway stamp put the doorway nine days *after* what it precedes, and a fourth-return conversation was printed after the seventeenth return. Three division stamps described spans their parts do not have; the reserve HOLD was reconciled by the dossier's own cause (Abyssal surges) instead of left standing. |
| **The whole** | 229 | is the file true about itself? Five source-ledger citations named dossier sections that stopped existing at batch 216 — *Origins*, *Chosen by the Alpha Tree*, *Formation of the R.D.*, *The Sovereign-Class Containment* — plus a codex section that never existed. The Zone D failure was dated to an earlier iteration against the dossier's final one, while the comparison table claimed it Kept. The dialogue census (269/24/6) described a file at 370 lines; measured, 381/19/4. Three cast counts stale, two of them by my own edits. The dossier's Story ran 82 before 77 and 92 before 55; now Day 1 to Day 365 with no step backwards. |
| **The readable pass** | 228 | read again, for whether a reader can follow. The dossier opened on *the Hand of Change* and *Doorspeech* before either was defined. Day 160 answered Floor 4 before it was called and then ran 6, 5 — a descending check with nowhere left to go; now 6, 5, 4. That line is Ayshuk's in the Parts and stays with Seiyon because she owns the console, and the HOLD now says so. Three repetitions cut. Long sentences measured and left: they are the voice. |
| **The full read** | 227 | both files read end to end, in order, nothing skipped. The Maw was given a provenance the dossier forbids — the Door's fragment 오누스도, *"the Maw is not using Majin"*, *"never been informed"* — and both passages were rewritten to keep him ignorant. Four clocks disagreed with their own logs (23:26 at 23:24; 23:41 at 23:24; 02:00 against 23:45; two rooms at 15:00). The Field's 02:40 fracture became 23:40 on the last night, because the directive closes at 23:59:58 and the city cannot be evacuated in twenty-one hours. Day 121 cannot have quoted *shared*; the 188 days belong to the facility, not the gates. Day 53's question restored. 178 → 180, twenty-seven → twenty-eight, 689 → 748, nine days → 205. The names legend left the dossier. |
| **The comparison** | 226 | claim-by-claim against the dossier. Three assertions had never made it in — the four steps, the Eight, the pulse — each already cited in the source ledger. Four provable errors: he slept; the directive stamped 04:00 against a 23:59:58 closure; the Absolvohan named in Year 4,231, before its own program; Day 365 counting 210 back to a Day 160. The check is now a table in the file. |
| **The stamp** | 225 | every scene opens with a STAMP line — offset, clock, place. The anchor is `[REDACTED]` until 00:00 on the day of it, where the bracket lifts once and is never used again. Units chosen by distance: years, months, days, hours, minutes. R-62, § IV.6, gate 56. 51 stamps in `01_MAJIN`, 140 scenes of debt in files 02–09. |
| **The pin** | 224 | the chronology was stated three times and denied twice. The Doorway is Day −9, not the same night; the two "last ordinary" claims are corrected. The spine now carries both calendars — loss days and cycle days — with an offset on every row, and The Sovereign moves from "the same hour" to Day 63. The Doorway was missing from the Scene ledger. |
| **Six women, one label** | 223b | `[she]` was five different women and `[him]` four different men, and the Cast table listed three of them twice. Every unnamed speaker now carries a role; the counts were regenerated from the file. Chapter read continues: the Consolihan, the station. |
| **The key belongs in the rulebook** | 223 | the register legend was a style manual in the front matter of a story. Deleted from all nine files; gate 55 inverted to fail a file that carries one. Five passages that explained their own mechanism cut. Re-read from the prologue: the lamp taught twice, a pronoun that flipped subject, a man's coat on a woman, box four confused with box three, and the Sovereign wearing bold. |
| **The order it hurt** | 222 | read chronologically, the file had no present: 21,000 words of PAST and FLASHBACK with no room to be told in. The testimony frame — a clerk, a printed sheet of forty-one questions, five sessions across eleven months — now opens it and closes it. Every date in the file is relative to the floor warming because he refuses to write a year number, and the file says so. |
| **The marks you can see** | 221 | a faction is a body, not a description: capital article at the coining, coined mid-sentence where the mark is visible, and the sentence says what it is a body of |
| **The reading** | 219 | thirteen corpus terms glossed where a reader meets them; the disclosure dramatized in three movements; the coldest act in the file — filing her as *the Original* — written as a scene instead of an appendix row |
| **The death** | 218 | Yeon-seo's death rebuilt as the sacrifice canon already had: her own discipline kills her, the seal she wrote is the object she leaves, and the containment standard of the whole city dates from the year after |
| **The dossier read first** | 217 | the extended file built from the dossier instead of beside it: the fusion given a body, the loss a place, the arithmetic a closure, and a gate that measures appearance in the narrative body only |

---

# Part V — Where the commands stand

**32 standards are measured every batch** (`tools/auditors/how_finished.py`). **27 are DONE, 5
OPEN, 0 unknown:**

| OPEN standard | remainder |
|---|---|
| Every command ends in a file (R-52) | **2**, this batch's filings, transient |
| Tale declared in a register | **181** of 301 |
| Form line thin (no colour, material or number) | **134** |
| Form line repeats its marker | **86** |
| Essayist constructions | **310** of openers |
| Stat bands over ceiling | **7** |

**What that means, honestly.** *"Every law is enforced by a gate and the gate is green"* was not true
when this paragraph was first written, and batch 207 is what found it out. `how_finished.py`
measured **fifteen** auditors; `tools/gate.sh` invoked **twelve**. The three batches immediately
before this one — 203's work-effect gate, 204's SE-effect gate, 206's rule-index gate — were
written, tested, indexed, cited in the changelog, and **never added to the build.** Each printed
`RESULT: PASS` on demand and none of them could fail a push. `O-37` and `check_gate_wiring.py` (gate 46) now make an unwired gate a failure in its own right, so a citation cannot stand in for an
invocation again.

The seven OPEN standards are now **prose volume only** — no section is missing anywhere in the
archive, and since batch 214 no dossier is without a shape family either. 181 Tales to re-voice, 220
form lines to deepen, 310 essayist constructions to rewrite, 7 stat bands to bring under the ceiling.
None of them can be closed by adding a byline, and none of them should be listed as DONE until the
counter above them reads zero.
