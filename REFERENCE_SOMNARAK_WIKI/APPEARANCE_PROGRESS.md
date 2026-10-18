# Appearance progress — SE bodies and M.A.W. equipment are separate

Owner direction, 2026-10-18: start a new X/X for SE appearance fixes and name the older counters by their M.A.W. scope.

## Current counters

Three independent per-SE counters; a reviewed equipment description is not a completed entity-body fix.

| Workstream | Completed | Coverage | Remaining |
|---|---:|---:|---:|
| ALL M.A.W. Types Appearance per SE — source-review coverage | 244 / 301 | 81.06% | 57 / 301 |
| ALL M.A.W.-W Appearance per SE — source-review coverage | 244 / 287 | 85.02% | 43 / 287 |
| SE Appearance Fix — independent written-design pass | 8 / 301 | 2.66% | 293 / 301 |

These are coverage counters, **not promises that every held discrepancy is repaired**. The first two retain their historical criteria and explicit source holds. The new counter starts at zero; old equipment reviews, general prose fixes, shape screening and the R-32 clarification are not backfilled as SE appearance completions.

### Names and historical continuity

- **ALL M.A.W. Types Appearance per SE** replaces the ambiguous current reporting label **Full-SE**. The inherited count is the combined whole-primary/all-equipment-source review stream, including Weapon, Suit and Stigma comparisons, not three items counted separately. Historical reviews may leave shape, artwork, ability or chronology disagreements explicitly held. Do not relabel that coverage as 240 fully redesigned sets.
- **ALL M.A.W.-W Appearance per SE** replaces **Weapon-only**. It counts unique exact Weapon/source dispositions, including holds, not the number of distinct silhouettes or finished SVGs. Rechecking Animus does not award its already-counted Weapon pair again.
- **SE Appearance Fix** counts distinct completed reviews in the new written-body pass. Changed and justified No change outcomes both count after complete review, validation, individual commit and verified push. Report those outcomes separately. A shape relationship left unresolved is **held**, not a completed fix.
- **Rendered artwork is separate.** A written-description fix does not claim an image was drawn, redrawn, published or visually verified. Appearance-source review coverage does not mean generated-art completion.

Historical log wording and commit messages are preserved. Their label crosswalk lives here; do not rewrite past reports to imply they were a different program.

## New SE appearance pass

The machine-readable per-dossier record is [SE_APPEARANCE_LEDGER.json](SE_APPEARANCE_LEDGER.json). It inventories the same 301 SE dossiers as the established corpus, with full designations and exact paths, not numeric identifiers alone. `python3 tools/appearance_progress.py` validates it against that corpus and prints the new count. No old-credit inference runs in this checker.

Initial ledger: 299 pending, two blocked, zero completed. Paused `N-Iα-025` and scope-unconfirmed `C-IIIγ-062` stay in the fixed 301 denominator but are not eligible for silent work. The fixed corpus contains 290 Sorrow Entity dossiers and 11 identity-resolved Unknown Entity dossiers. The non-SE Book and README files are outside the counter; do not drop the Unknown wing merely because it has a separate directory. There is no authorization to import Batch301 stubs or fabricate its eight missing bodies.

### Completion evidence

For each dossier, read the full primary and identity-resolved sources/history. Assess its actual silhouette, anatomy, movement and spatial organisation, including supported earlier/later and conditional forms. Apply [R-32](RULES/R-32_SUBJECT_SHAPE_DIVERSITY.md): human sorrow does not imply a human body; symbolic or contrasting nonhuman bodies are allowed. This is an appearance-fix program, not only a classification audit.

Record whether the result is a source-supported repair, a deliberate owner-authorized redesign, or a justified retained design. A redraw invented now must not be described as a recovered historical transformation. Do not invent an Animal or Monster stage just to fill a quota. Human, Monster, Animal and Abstract are collection-level minimum families, not four states for every SE.

Completion requires a durable individual evidence record with source references, before/after and chronology reasoning, holds, independent Commentary, whole-final reread, five dossier checks and an individual gate/push. A completed No change outcome must justify why the existing shape is retained, not call an unread file unchanged. Equipment holds can remain without awarding new equipment credit; unresolved entity-shape relationships must stay held.

## Batch145 — CLOSED 5/5

The latest P authorizes one next batch. Its scope is the independent SE appearance pass, not another batch of old equipment-credit claims. Minimum five completed reviews; apply the cumulative three-No-change 5→7→10 progression. Never close below the required rung. No Batch146 is authorized.

Fresh source-signal screening used current primary files and checked for supported form/state cues absent from an Appearance States block. This is a reading-order screen, not a defect verdict or an anatomy census. Priority goes to explicit witnessed conditional forms, then documentary earlier/later forms, then less settled change-of-form or scale cues. The tie-breaking/context shortlist remains documented rather than manufactured as a numeric quality score.

Opening queue:

1. **Animus `O-Iα-108`** — the interaction record reports a brief human outline beside an otherwise bodiless heat-line; inspect how Appearance represents that conditional state.
2. **Whispering Gallery `C-IIβ-185`** — the Watch record supplies a document-supported face-loss/restoration chronology; inspect earlier versus current portraits.
3. **Relic of a Thousand Owners `O-IVδ-792`** — current text mentions changing form near the Exile's Gate; resolve its supported scope before proposing a transition.
4. **Hollowcast `N-IIβ-426`** — inspect the stable-looking outline, changing opening and Transform wording; a scale difference is not automatically a new body.
5. **Breathing Stone `C-IVδ-907`** — compare the physical wall with its described expansion; do not turn an expanding structure into a walking human for variety.

Selection is new-pass pending-only. Some dossiers have prior equipment/prose reviews, but none is credited in this newly initialized SE pass. Their previous credits are not repeated. The legacy equipment pending queue remains Aphasia, Happy Mask, Black River, Hollowcast and Seething Tundra; it has not been completed, cancelled or silently relabelled as this queue.

## Completed new-pass evidence

- **Animus `O-Iα-108`** — [Batch145 unit1 evidence](SE_APPEARANCE_REVIEWS/B145_01_ANIMUS.md). Source-supported shape/state repair, not a new-body redesign: ordinary heat-line versus the briefly witnessed Maiden-induced outline. Five checks PASS; whole final reread complete. Neither legacy equipment counter increases.

Historical unit1 snapshot: 1 changed, 0 retained, 0 held, 2 blocked and 298 pending. Written-design completion does not mean new artwork. Batch145 is OPEN1/5 with zero completed No change dossiers; four units remain under the existing P. The initial 0/301 baseline above is historical, not a second current counter. Corpus scope was checked directly: 290 Sorrow Entity dossiers plus 11 Unknown Entity dossiers; an initial prose statement excluding the Unknown wing was corrected before the first new completion. The ledger always contained the correct 301 identities.
## Current Batch145 updates

Current state: **CLOSED 5/5**, No change **2/5**. Independent SE counter **5/301**, 1.66%; 296/301 remaining. 3 changed, 2 retained, two blocked, 294 pending. Both legacy equipment counters stay 240/301 and 240/287. Earlier completion snapshots above are historical.

- `C-IIβ-185` — changed: [The Appearance States block now connects the named memorial, subsequent loss of faces, and current four documentary restorations. The hall stays fixed while acoustic coverage can widen.](SE_APPEARANCE_REVIEWS/B145_02_185.md)
- `C-IVδ-907` — retained: [No change](SE_APPEARANCE_REVIEWS/B145_05_907.md)
- `N-IIβ-426` — changed: [Added the held/Transform appearance block, including conscious torn-fruit impression versus photographic empty outline. Added breach continuity separating loss of fixed scale from a new botanical body and from healing.](SE_APPEARANCE_REVIEWS/B145_04_426.md)
- `O-IVδ-792` — retained: [No change](SE_APPEARANCE_REVIEWS/B145_03_792.md)
- `O-Iα-108` — changed: [Ordinary abstract heat-line distinguished from witnessed Maiden-induced outline; no new body invented.](SE_APPEARANCE_REVIEWS/B145_01_ANIMUS.md)

## Batch145 close

**CLOSED5/5**, three changed and two retained. No change2/5 does not trigger5→7. Individual commits: Animus`4fdbb67`, Gallery`c8f24b2`, Relic`47bf309`, Hollowcast`646a427`, Stone`0cd3ed5`, all PUSH VERIFIED. Gallery’s same-unit SideA exception correction`247df76` earns no extra credit. The updated SideA now records the four restored faces and unverifiable likeness; its earlier unit2 source hold is superseded only on that point. All equipment holds remain.

Fresh25checks PASS, eight ledger tests PASS, couples0/301, comparison557candidates/861pairs/287complete sets. Primary words36,137→37,257(+1,120); SideA666→700(+34) separately. The closing word-count check corrects Gallery’s pre-label7,713 to final7,712. See [complete closing evidence and fresh read-only cue screen](SE_APPEARANCE_REVIEWS/B145_CLOSE.json).

Next batch requires a fresh P. No146is open. Batch301still awaits owner8bodies/4+4. PR14OPENdraft→NON-WIKI; owner controls merge. No artwork completion, deployment, equipment-credit increment or legacy backfill is claimed.
## Batch146 — OPEN0/5: equipment-first combined appearance review

Owner P authorizes one next batch. Owner permits finishing the older work first or combining both workstreams, and accepts longer execution. Use separate Bash steps for source reading, each edit, checks, evidence and each gate/push; never dump the entire batch into one Bash command.

Prioritize the preserved older pending queue: Aphasia O-Iα-720, Happy Mask C-IIβ-051, Black River C-Vγ-225, Hollowcast N-IIβ-426, Seething Tundra C-Iα-884. Batch144's pending-only source-review shortlist supports this order; current identity/path inventory checked. Screening is reading order, not a confirmed-defect ranking. Read whole primaries and exact A–D/history; body and equipment decisions are made together per dossier, not credited together automatically.

Counters start at ALL M.A.W. Types Appearance per SE source-review coverage240/301=79.73%,61/301remain; ALL M.A.W.-W Appearance per SE source-review coverage240/287=83.62%,47/287remain; SE Appearance Fix independent written-design pass5/301=1.66%,296/301remain. Coverage includes holds, not all conflicts resolved or artwork finished. Body status starts3changed/2retained/0held/2blocked/294pending. Hollowcast already earned SE credit in145 and earns no second SE credit here. Each new equipment credit requires unique-history proof. Unresolved body relationships remain held, not SE completions.

The ledger now records fresh batch reviews separately from cumulative SE credits, so Hollowcast's earlier completion does not make this batch1/5 at opening. Immutable baseline remains240/240; post-baseline equipment dispositions are separate evidence records. Validator gains corresponding checks and tests. Batch145 stays historically CLOSED5/5; no146unit is completed yet.

Minimum five completed dossiers. Three cumulative No change dossiers trigger5→7→10. Never force an edit or close below the opened rung. Pending is not No change. All final rereads, five checks, individual Commentary and individual gate/push remain mandatory. No147authorized. PR14ownermergeonly; no deployment. Batch301separateblocked8bodies/owner4+4generatevalidatebeforecopy. Recovery preserved /home/user/b146/restored.patch and restored metadata only after every remote tracked file matched workspace bytes.

### Batch146 unit1 — `O-Iα-720`

One short movement repair: the header now preserves upright/flowing wax forms and drift toward speech instead of unsupported pursuit. Existing multi-form Appearance retained. LC_ALL=C words7,104→7,118(+14). [Individual evidence](SE_APPEARANCE_REVIEWS/B146_01_APHASIA.md). Current batch OPEN1/5; Nochange0/1. Current totals all-types241/301, Weapon241/287, SE6/301; previous snapshots above are historical.

### Batch146 unit2 — `C-IIβ-051`

Joy Lens gains sourceB-supported convex disc, short black handle, thumb rest and tether ring. The mask stays tray-bound rather than executing an invented violent exit. One careful/one short change, separately applied; words7,520→7,569(+49). [Individual evidence](SE_APPEARANCE_REVIEWS/B146_02_HAPPY_MASK.md). Current batch OPEN2/5; Nochange0/2. Current totals all-types242/301, Weapon242/287, SE7/301; previous snapshots above are historical.

### Batch146 unit3 — `C-Vγ-225`

One careful Maul opposed-face/downstream construction addition; separate short flavor repair to lead-cold liquid and line-based interval, retaining historical warm-instrument testimony. Words9,026→9,053(+27). [Individual evidence](SE_APPEARANCE_REVIEWS/B146_03_BLACK_RIVER.md). Current batch OPEN3/5; Nochange0/3. Current totals all-types243/301, Weapon243/287, SE8/301; previous snapshots above are historical.

### Batch146 unit4 — `N-IIβ-426`

One short Torn Fang Appearance addition: exactB empty central groove, torn-out material deliberately unfilled and channel kept clear. Wholeprimary otherwise byte-identical;7,646→7,670(+24). SEbody unchanged; no duplicate SEcredit. [Individual evidence](SE_APPEARANCE_REVIEWS/B146_04_HOLLOWCAST.md). Current batch OPEN4/5; Nochange0/4. Current totals all-types244/301, Weapon244/287, SE8/301; previous snapshots above are historical.
