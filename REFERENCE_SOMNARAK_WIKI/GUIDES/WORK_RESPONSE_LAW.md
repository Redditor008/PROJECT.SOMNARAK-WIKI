# The work response follows the element — or it is a form

**Measured 2026-11-03 over 290 dossiers.** Every one of them carries an `**Element**` row. Not one of their Behavior tables reads it.

## 1. What the cosmology already decided

`SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/PROJECT_SOMNARAK.md` has carried a **Work Type Effectiveness** matrix since the first cosmology draft:

| Entity Element | Flerehan | Pugnahan | Viderehan | Ferrehan |
|---|---|---|---|---|
| **Lament** | ● Strong | ○ Weak | ◐ Partial | ◐ Partial |
| **Grudge** | ○ Weak | ● Strong | ◐ Partial | ◐ Partial |
| **Void** | ◐ Partial | ◐ Partial | ● Strong | ○ Weak |
| **Weight** | ◐ Partial | ◐ Partial | ○ Weak | ● Strong |

*● Strong — most effective, highest yield · ◐ Partial — moderately effective · ○ Weak — least effective, highest risk.*

The matrix is specific: **exactly one work type is Strong for each element, and it is never the same one twice.** Lament answers to tears, Grudge to confrontation, Void to observation, Weight to endurance. That is four different answers by construction — the variety the archive is missing is already written into its own cosmology.

## 2. What the dossiers say

**Measured 2026-11-03, before `R-40` and before the barred cells were named** — these are the shapes that made the rotation visible, not the shapes the archive carries today (the live count is in `WORK_PREFERENCE_VARIETY.md` §4). Across the 290 dossiers then on disk the response table took **three shapes, in every element**:

| vector (Flerehan : Pugnahan : Viderehan : Ferrehan) | dossiers |
|---|---:|
| N/A : N/A : Stable : Decrease | 117 |
| Decrease : Increase : Stable : Decrease | 112 |
| — : — : Decrease : Decrease | 28 |
| Decrease : Stable : Stable : Decrease | 17 |
| everything else (17 shapes) | 16 |

Split by element, the three shapes appear at almost the same rates under Lament, Grudge, Void and Weight. **285 of 285 graded dossiers are off the matrix; on 2026-11-03 the count of dossiers that agree with their own Element row was zero.**

The signs across all working rows: **Decrease 454 (52%) · Stable 290 (33%) · Increase 131 (15%)**. Working a holding makes it better half the time, for every element, by every work type. That is the "too much on the positive side" the owner named, and it has the same cause as the uniformity: the column was filled from what the last file said.

## 3. Why no gate caught it

Because there is no error in any single dossier. Each Behavior table is defensible on its own page — *Backward Hour*'s observation work really does settle its pressure, and so does *Sehnsucht*'s. The defect is a property of the **set**, and the set had no rule to break until the Element row was cross-read against the response row.

This is the same class as batch 149's slot templates and batch 153's ratios: **the entry names the right mechanic and says nothing about this holding.** Here the giveaway is arithmetic — a 4×4 matrix with 4 distinct Strong cells cannot produce one shape.

## 4. The law

The matrix read across:

| the matrix says | the Gauge Change cell says |
|---|---|
| ● Strong | **Decrease** — the work the element answers to |
| ◐ Partial | **Stable** — a moderate effect, no net movement |
| ○ Weak | **Increase** — least effective, highest risk |

So the four subject shapes are:

| Element | Flerehan | Pugnahan | Viderehan | Ferrehan |
|---|---|---|---|---|
| **Lament** | Decrease | Increase | Stable | Stable |
| **Grudge** | Increase | Decrease | Stable | Stable |
| **Void** | Stable | Stable | Decrease | Increase |
| **Weight** | Stable | Stable | Increase | Decrease |

Each holding now has **exactly one work type that settles it, one that makes it worse, and two that hold it where it is.** The sign totals this produces are Decrease 25%, Stable 50%, Increase 25% — half the archive's current Decrease share.

**This matrix governs Subjects only — and since `R-40` (2026-11-03) that is the whole of it.** A relic has no Work Types at all: it carries `## Handling Process` (Approach · Handling · Withdrawal · Refusal) instead of a response table, and `check_work_response.py` does not grade it. Batch 154 was written against the old Two-Work-Type Rule — which gave a relic two of the four cells — and that rule was retired the same week, for the reason the measurement shows: 117 of 141 relic dossiers carried the identical `N/A : N/A : Stable : Decrease` vector. A relic's two cells were never describing the relic.

The Weight comparison that motivated this guide still stands where it can be applied: **looking at a weight adds to what is being weighed.** For a Subject that is now enforced. For a relic the answer is the Handling Process — you do not look at a weight, you take its measurement and put the instrument back.

## 5. Where a file may disagree

A dossier may leave the matrix when **its own record states why**, and the reason is written into `EXEMPT` in `tools/auditors/check_work_response.py` beside the code:

**`SE-O-IIIγ-476` Sehnsucht** — the file's reading rule is that *stability under Viderehan is correct*, because what it measures is the object's motion and a reader adds nothing to it. Batch 154 converted it first and then put it back: the matrix is a default, and a file with a stated datum outranks a default.

## 6. The conversion, and why it is slow

The sign is not written once per file. It appears in the Behavior table and then again in the `Valid Work Types` row, in the `Operational Work Notes`, in the Work Response line of the containment record, and in the "Sustained observation" summary — **four to six places, each of which has to be re-argued or the file contradicts itself.** That is where the monoculture's inertia came from: changing one holding is a half-hour's work, and copying the previous holding's table is two minutes.

Batch 154 did five — *Endless Shift*, *Broken Clocktower*, *Rift*, *Neglect, Learned to Listen* and *Torpor* — each converted from Weight's old `Stable : Decrease` to the matrix's `Increase : Decrease`, with the observation row given the mechanism that makes looking cost something:

- **Endless Shift** — reconciling three clocks is itself a shift nobody is entered on a timesheet for.
- **Broken Clocktower** — the dilation extends over the ground it is measured across.
- **Rift** — a worker who reads the division is entered on the second list.
- **Neglect** — every reading is paid for out of the reader, and the patch does not shrink.
- **Torpor** — reading the duties means staying awake on purpose where waking hours are the currency.

Ratchet **284**, decremented by however many a batch converts. `python3 tools/auditors/check_work_response.py --stats` prints the current distribution.
