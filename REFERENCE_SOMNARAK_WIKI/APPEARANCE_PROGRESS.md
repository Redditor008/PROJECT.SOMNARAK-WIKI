# Appearance progress — SE bodies and M.A.W. equipment are separate

Owner direction, 2026-10-18: start a new X/X for SE appearance fixes and name the older counters by their M.A.W. scope.

## Current counters

Three independent per-SE counters; a reviewed equipment description is not a completed entity-body fix.

| Workstream | Completed | Coverage | Remaining |
|---|---:|---:|---:|
| ALL M.A.W. Types Appearance per SE — source-review coverage | 245 / 301 | 81.40% | 56 / 301 |
| ALL M.A.W.-W Appearance per SE — source-review coverage | 245 / 287 | 85.37% | 42 / 287 |
| SE Appearance Fix — independent written-design pass | 12 / 301 | 3.99% | 289 / 301 |

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

### Batch146 unit5 — `C-Iα-884`

One careful object-profile repair: tray-held palm shard rather than structure/location; record retained AngryMaiden hairline separately from tear count and surrounding moving ground.6,349→6,379(+30). Equipment No change; independentSEheld,notcompleted. [Individual evidence](SE_APPEARANCE_REVIEWS/B146_05_SEETHING_TUNDRA.md). Current batch OPEN5/5; Nochange0/5. Current totals all-types245/301, Weapon245/287, SE8/301; previous snapshots above are historical.

## Batch146 current close

**CLOSED5/5**, primarychanges5, No change0/5. No7rung triggered. Combined batch credits: equipment+5/all-types and+5/Weapon; SE+3, not+5. Hollowcast already completed145, Tundra held despite limited profile repair. Current totals245/301all-types81.40%,245/287Weapon85.37%,8/301SE2.66%; SE6changed/2retained/1held/290pending/2blocked. All preceding unit/opening snapshots are historical. Older five-item equipment queue reviewed with explicit holds, not erased as all-resolved.

Five individual PUSH VERIFIED units461b1e1/8e10c21/8891dba/85d53a3/ebe4b19; fresh25checksPASS,10testsPASS,couples0/301,20unchangedexactsourcefingerprints. LC_ALL=C words37,645→37,789(+144). [Full closing evidence](SE_APPEARANCE_REVIEWS/B146_CLOSE.json). No147withoutnewP. Next pending cue-screen611/909/641/371/169 is reading order only;884heldfollowup remains separate. PR14OPENdraft→NON-WIKIownermergeonly.301blocked8bodies/owner4+4generatevalidatebeforecopy.

## Batch147 opening — SE appearance pass, OPEN 0/5

Owner's fresh `p` after Batch146 authorizes one next batch, not Batch148. The older five-item equipment queue was reviewed in146. Continue the independent written SE appearance pass, preserving source-supported nonhuman and historical/conditional forms. No artwork completion or broad collection redesign is claimed.

Fresh pending-only body cue screen at fa57929: 290 pending, one held, two blocked, eight completed; 136 reading-cue candidates. Equipment text excluded. Highest cue counts select Sleeping Shard N-IVδ-611 (9), Dormant Monolith N-IVδ-909 (8), Home to No One Who Knew Me N-IVδ-641 (7), Protest No One Remembers O-IIIγ-371 (7), Atlas O-Iα-169 (6), ties by designation. This is reading order, not confirmed-defect ranking or anatomy census. No substitution. Opening evidence: B147_OPEN.json.

Cumulative counters unchanged: ALL M.A.W. Types Appearance per SE — source-review coverage245/301=81.40%,56/301remain; ALL M.A.W.-W Appearance per SE — source-review coverage245/287=85.37%,42/287remain; SE Appearance Fix — independent written-design pass8/301=2.66%,293/301remain. Equipment coverage includes explicit holds, not resolved redesign/artwork. SE6changed/2retained/1held/290pending/2blocked. Do not infer new equipment credit from a body review or repeat historical exact pairs.

Read each complete primary, exactA–D and identity-resolved Masters/Tales/history. Predeclare short/careful changes; preserve uncertainty and reread full finals. Actual five checks and separate individual gates/pushes remain required, in multiple focused Bash steps. Minimum five completed reviews; three cumulative whole-dossier No change results trigger5→7→10. No mandatory edits; pending is not No change. A couple is an excessive-prose-overlap dossier pair, not an equipment pair. Human/Monster/Animal/Abstract are collection-wide families, not four required forms for each entity. Never invent transitions to resolve conflicts.

Held884's undescribed Transform, blue/clearwhite relationship and disposition-index/sectorbenefit mismatch stay explicit follow-ups; not silently counted. Blocked025/062 remain in301denominator. Corpus290Sorrow+11Unknown excludes non-SEBook. PR14OPENdraft→NON-WIKI, ownermergeonly. Batch301stillblocked8ownerbodies/owner4+4; generate/validate before wiki copy. No deployment or merge authorized.

### Batch147 unit1: `N-IVδ-611`

Careful spatial/state repair: floating curled figure and unchanged carried crystal are recorded separately from entrant-specific Dream-layer shape changes. Corrupt expansion remains a field around a stationary figure, not pursuit or an enlarged crystal body. Movement header and current flavor no longer imply a fixed object or an observed changing face. [Evidence](SE_APPEARANCE_REVIEWS/B147_01_SLEEPING_SHARD.md). SE 9/301; equipment unchanged245/301 and245/287. Batch147 OPEN1/5; No change0/1. Earlier snapshots are historical.

### Batch147 unit2: `N-IVδ-909`

Short limited repair: replace the unsupported indiscriminate-hunting alert and generic physical-zone movement with the recorded mental column/spread. Clarify worker-to-mind-pillar origin without a stone human. Broader Transform shape remains held; SE completion +0. [Evidence](SE_APPEARANCE_REVIEWS/B147_02_DORMANT_MONOLITH.md). SE 9/301; equipment unchanged245/301 and245/287. Batch147 OPEN2/5; No change0/2. Earlier snapshots are historical.

### Batch147 unit3: `N-IVδ-641`

No change. Retain the black, hot, char-scented object with crimson inner light across unobserved shape changes; its changing silhouette and observer-specific recognition are the design, not an absent definitive sculpture. [Evidence](SE_APPEARANCE_REVIEWS/B147_03_HOME_TO_NO_ONE.md). SE 10/301; equipment unchanged245/301 and245/287. Batch147 OPEN3/5; No change1/3. Earlier snapshots are historical.

### Batch147 unit4: `O-IIIγ-371`

Careful shape/state pass: Appearance now distinguishes ordinary upright voice-like absence, the documented low flat perimeter-pairing state and Transform spread through structure. Earlier community/speech is origin, not a portrait or recovered content. No body, face, garment, slogan or solid attack form invented. [Evidence](SE_APPEARANCE_REVIEWS/B147_04_PROTEST_NO_ONE_REMEMBERS.md). SE 11/301; equipment unchanged245/301 and245/287. Batch147 OPEN4/5; No change1/4. Earlier snapshots are historical.

### Batch147 unit5: `O-Iα-169`

No change. Independently retain the existing earlier-worker/incorporation/current-pillar distinction from Batch143: warm rough rusted iron, orange over brown, embedded in the Forge floor, no separable person and no emerging or alternating human form. Expansion loads nearby supports rather than making the column walk. [Evidence](SE_APPEARANCE_REVIEWS/B147_05_ATLAS.md). SE 12/301; equipment unchanged245/301 and245/287. Batch147 OPEN5/5; No change2/5. Earlier snapshots are historical.

## Batch147 current close

CLOSED5/5reviews, No change2/5; no7rung triggered. Four SE completions:611/371repaired,641/169retained;909held despite limited correction. Equipment+0: prior99/118/121/109/143reviews not repeated. Current245/301all-types81.40%,245/287Weapon85.37%,12/301SE3.99%; SE8changed/4retained/2held/285pending/2blocked,289remain. Written work, not artwork. Earlier unit/opening snapshots historical.

Five individual PUSH VERIFIED unitsdb6d971/7abec5c/276f1df/0aab347/5af0f14.25fresh checks,10tests,labelcheckPASS,couples0/301.40,584→41,232words(+648),originaldigits/equipmentunchanged,25unchangedsourcefingerprints. [Closing evidence](SE_APPEARANCE_REVIEWS/B147_CLOSE.json). No148withoutfreshP; no next queue selected. PR14OPENdraft→NON-WIKIownermergeonly.301blocked8bodies/owner4+4generatevalidatebeforecopy.

## Batch148 current opening

OPEN0/5:119/103/290/852/518pending. Before-and-after whole-file logical reading required; record connection evidence and unresolved contradictions rather than treating local fixes or automated checks as a logical PASS. Counters unchanged12/301SE,245/301all-types,245/287Weapon. Prior completions not retroactively re-certified. [Opening evidence](SE_APPEARANCE_REVIEWS/B148_OPEN.json).
