# Absolvohan — Repair Notes (Option C)

Repaired copy of the nine-part Absolvohan gameplay narrative.
The generated management-log layer was **kept**; its internal contradictions were fixed
so it no longer disagrees with the hand-written narrative.

Originals are untouched in `../ABSOLOVHAN PART/`.

## Canon rule applied
The **narrative layer wins**. Where a `[BRACKET]` block contradicted dialogue or prose,
the block was corrected to match, never the reverse.

Narrative anchors used:
- **Day 0** — reserves 47.3 t (Part 1, `[FACILITY STATUS — MORNING REPORT]`)
- **Day 160** — 49.8 t dispersed into Zone B, the Raw
- **Day 177** — Seiyon: *"For a full city-wide release? 100 tons. We have... 0."*
- **Days 350+** — post-Cycle; the Absolvohan is no longer an accumulator

## Changes

### 1. Absolvohan reserves — 45 lines rewritten
Was a random walk with a `100.1 tons` spike roughly every fifth day, including on Day 177
where the narrative states the reserve is empty.

**Authority:** `The_REVERIE_DIRECTORATE.md` → *R.D. Classified — The Cycle* → *Absolvohan Reserve*:

> "Ordinary working stock was **reclaimed by reset**; only secretly diverted surplus —
> approximately **0.02 tons per iteration** — persisted."

The reserve therefore grows **per Cycle iteration (one civic year), not per day**.
Across the entire final Cycle that is ~0.0086 t — invisible at two decimals.
**The reserve is flat within a single Cycle.** Daily quota production powers the city and
is reclaimed at each reset; it never enters the reserve.

Now:
- Days 0–160 — `47.3 tons (persistent surplus; unchanged — daily production is reclaimed at reset)`
- Days 165–177 — `0 tons — 49.8t dispersed into Zone B on Day 160`
- Days 350–365 — `decommissioned — dismantled after the Hand opened`

**Retained the narrative's 47.3 t** rather than the R.D.'s archived ~36 t estimate
(0.02 × 1,778 = 35.56). The R.D. explicitly calls its own figure
*"an operational approximation rather than an exact multiplication warranty,"* which
accommodates the gap; the narrative number is the one the story dramatizes.

### 2. M.A.W. registry — 45 lines
**1,778 is the Cycle number — Somnarak is living its 1,778th and final Cycle.
It is not a count of days.** Each Cycle is a repetition of Year 4,232.

The generated layer treated it as a day counter, ticking `1743` → `1783` across the
run in two inconsistent formats (`... entries across 1,778 cycles` and `... entries.`).

A registry that advances +1 per day is wrong twice over: it implies one extraction
every single day, and it conflates the Cycle number with an entry count.

All 45 lines now read:
`- M.A.W. registry total: 1,743 entries logged this Cycle`

A fixed figure — the tally for the current Cycle, not a running day count.

### 3. Ordeal lines — 45 lines rewritten
**Authority:** `SOMNARAK_ORDEALS_FRAMEWORK.md` — Ordeals are classified on **two axes**,
**Five Colors × Four Times = 20 Ordeal Types**. The generated layer recorded only the element.

- **Colour** = Han source. BLUE (Lament) · BLACK (Weight) · PALE (Void) ·
  GREY (Grudge, desaturated Crimson) · PURPLE (raw unprocessed Han — outside the four
  elements, which is why no fifth element exists).
- **Time / Watch** = severity tier. First → Second → Third → Tide (≈ TETH / HE / WAW / ALEPH).

Watch tier is **not** arbitrary: the framework's Han-Density Gauge governs spawning
(Clear 0–20 / Elevated 21–40 / Critical 41–60 / Overload 61–80 / Cascading 81–100).
Each day already logged a `Sorrow Gauge average`, so the Watch was **derived from that
existing reading**, not invented. Verified: **0 mismatches across all 45 days.**

Before → after:
```
- Ordeal: **The Voice** (Void (Pale White)) — identity dissolution — ...
- Ordeal: **The Voice** — PALE, Second Watch (Void — Pale White) — identity dissolution — ...
```
`No Ordeal` became `**None** — Han-density held below spawn threshold; a rare quiet day`,
tying quiet days to the same gauge mechanic.

### 4. Duplicate trainee names — 4 lines
e.g. `Agent Lee (Ferrehan), Agent Choi (Ferrehan), Agent Lee (Ferrehan)`.
Repeat surnames removed; 0 remain.

### 5. `Cell Cell` typo — 20 lines
Doubled word corrected to `Cell`.

## Deliberately NOT changed
- All dialogue and narrative prose — untouched.
- Ordeal *frequency* distribution (12/12/12/5/4). Only the classification format changed.
- `Agents levelled up`, morale, deployment counts, Sorrow Gauge averages.
- The 20-name agent pool.
- Line counts are identical to the originals, file for file.

## Correction log
- **"The Voice" and "The Stampede" were wrongly called generator inventions.** They are
  legitimate Ordeals — the PALE and BLACK colour entries. The error came from comparing them
  against `The_REVERIE_DIRECTORATE.md`'s Whisper/Surge/Breach/Abyss, which is the **Watch
  axis**, not the colour axis. Both documents were right; they describe perpendicular axes.
- **Second pass corrected the reserve curve.** The first repair invented a *daily*
  accumulation (47.3 → 49.8 t climbing each day). `The_REVERIE_DIRECTORATE.md` establishes
  surplus persists **per iteration**, not per day, so the reserve is flat within a Cycle.
  Tidy, but wrong physics. Now flat.
- **First pass got 1,778 wrong.** It was treated as a day/iteration count and the registry
  was renumbered 1,743 → 1,787 to match. That was incorrect. 1,778 is the **Cycle number**.
  Corrected on the second pass to a fixed per-Cycle tally.
- The narrative layer's own use of "1,778 cycles" was verified correct in all 30 occurrences
  (e.g. *"I have watched you for 1,778 cycles"*, *"Day 1 of Year 4232+1778"*) and left alone.

## Open discrepancies (NOT changed — flagged for your ruling)
- **Reserve size.** Narrative says 47.3 t; R.D. archived estimate is ~36 t. Kept 47.3 t.
- **Zone B release.** Narrative disperses 49.8 t, which exceeds a ~36 t reserve under the
  R.D.'s own arithmetic. Left as written.
- **Kael vs. the Drift King.** `The_REVERIE_DIRECTORATE.md` Day 355 names **Kael**;
  `THE_DIRECTOR.md` calls the same figure *"the Drift King."* Not reconciled.
- **Echo-Core continuity.** The R.D. grades memory per Echo-Core — only Majin, Seiyon,
  Ayshuk and Marjuk have full knowledge. `THE_DIRECTOR.md`'s flat *"the Nine retained
  knowledge"* is inconsistent with this and should be revised.

## Known remaining softness
- `Agent Lee` is both a named character (Day 0, the Orphaned Bell reassignment) and a
  generic name in the generated pool. Not resolved — would require renaming background agents.
- Daily produced tonnage still exceeds quota on nearly every day.
