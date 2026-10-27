# Appearance progress — SE bodies and M.A.W. equipment are separate

**Latest: Batch189 OPEN 0/5** (Batch 188 [closed](SE_APPEARANCE_REVIEWS/B188_CLOSE.md); queue N-IIβ-170, C-IVδ-357, C-IIβ-135, N-IIIγ-184, N-IIβ-627. Counters: 274/301 Types, 272/287 Weapon, 18/301 SE; held 201 / pending 80) (all five HELD, latest [evidence](SE_APPEARANCE_REVIEWS/B185_05_HOLLOW_ECHO.md)). Closure next in this prompt. Counters: 271/301 Types, 269/287 Weapon, 18/301 SE; held 186 / pending 95. (five reviews minimum per prompt, ten maximum). Shard of a Broken Promise HELD with **fresh +1 Types / +1 Weapon**; Thralldom, The Convergence, Melting Rope and Pall HELD (latest [evidence](SE_APPEARANCE_REVIEWS/B184_05_PALL.md)). Closure next in this prompt. Counters: 271/301 Types, 269/287 Weapon, 18/301 SE; held 181 / pending 100.

**Previous: Batch183 CLOSED 5/5.** Five HELD reviews, 40 repairs; No change 0/5. [Closure record](SE_APPEARANCE_REVIEWS/B183_CLOSE.md). Special Activation: 153/301 SEs have no breach counter ([note](SPECIAL_ACTIVATION_SE.md)).

**Previous: Batch182 CLOSED 5/5.** Five HELD reviews, 41 supported repairs, No change 0/5. The Final Door earns the batch's only fresh equipment credit, +1 Types / +1 Weapon. [Close report](SE_APPEARANCE_REVIEWS/B182_CLOSE.md).

**Previous: Batch180 CLOSED 5/5.** Five HELD reviews, 39 supported repairs, No change 0/5. [Close report](SE_APPEARANCE_REVIEWS/B180_CLOSE.md). Counters unchanged; ledger held 161 / pending 120.

**Previous: Batch179 CLOSED 5/5.** Five HELD whole designs; 33 supported repairs (23 short / 10 careful), No change 0/5. Equipment coverage +1 Types / +0 Weapon (Wilderness Tide fresh all-type disposition); SE +0. [Full report](SE_APPEARANCE_REVIEWS/B179_CLOSE.md).

**Previous: Batch178 CLOSED5/5.** Five HELD whole designs; 31 supported repairs. No new Types/Weapon/SE credits. [Full report](SE_APPEARANCE_REVIEWS/B178_CLOSE.md).

**Previous: Batch177 CLOSED5/5.** Five HELD whole designs;30 supported repairs. Equipment+1Types/+1Weapon; SE+0. [Full report](SE_APPEARANCE_REVIEWS/B177_CLOSE.md).

**Previous: Batch176 CLOSED5/5.** Five HELD whole designs;45 supported repairs. Equipment coverage+1 Types/+1 Weapon; SE+0. [Full report](SE_APPEARANCE_REVIEWS/B176_CLOSE.md). No177/merge/art/deployment.

**Previous: Batch175 CLOSED5/5.** Five HELD whole designs;49 supported repairs. No new Types/Weapon/SE credits. [Full report](SE_APPEARANCE_REVIEWS/B175_CLOSE.md). No176/merge/art/deployment.

**Previous: Batch174 CLOSED5/5.** Two completed written designs and three held; 58 supported repairs. Equipment coverage +2 Types/+2 Weapon; SE +2. [Full report](SE_APPEARANCE_REVIEWS/B174_CLOSE.md). No175/merge/art/deployment.

**Previous: Batch173 CLOSED5/5.**41supported repairs, fiveHELD, No change0/5. Equipmentcoverage+3Types/+3Weapon;SE+0. [Batch report](SE_APPEARANCE_REVIEWS/B173_CLOSE.md). No174/merge/art/deployment.

**Previous: Batch172 CLOSED5/5.**47supported replacements, five HELD, No change0/5. Equipmentcoverage+2Types/+2Weapon; SE+0. [Batch report](SE_APPEARANCE_REVIEWS/B172_CLOSE.md). No173/merge/deployment.

**Previous: Batch171 CLOSED5/5.**46supported replacements, fiveHELD, No change0/5. Equipmentcoverage+2Types/+1Weapon, SE+0. [Batch report](SE_APPEARANCE_REVIEWS/B171_CLOSE.md). No172/merge/deployment.

**Previous: Batch170 CLOSED5/5.**61supported repairs, five HELD, No change0/5; fresh993equipment review+1/+1, SE+0. [Batch report](SE_APPEARANCE_REVIEWS/B170_CLOSE.md). No171/merge/deployment.

**Previous batch: Batch169 CLOSED 5 / 5.** 48 supported replacements, five HELD whole designs, No change0/5; no new equipment/SE credits. [Closure evidence](SE_APPEARANCE_REVIEWS/B169_CLOSE.json). Historical169authorization ended;170subsequentlyauthorized.


Owner direction, 2026-10-18: start a new X/X for SE appearance fixes and name the older counters by their M.A.W. scope.

## Current counters

Three independent per-SE counters; a reviewed equipment description is not a completed entity-body fix.

| Workstream | Completed | Coverage | Remaining |
|---|---:|---:|---:|
| ALL M.A.W. Types Appearance per SE — source-review coverage | 268 / 301 | 89.04% | 33 / 301 |
| ALL M.A.W.-W Appearance per SE — source-review coverage | 266 / 287 | 92.68% | 21 / 287 |
| SE Appearance Fix — independent written-design pass | 18 / 301 | 5.98% | 283 / 301 |

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

## Batch148 — CLOSED 5/5 reviews; 0 completed fixes

Owner p authorized148only. Fresh285pending/132cue-candidates selected119/103/290/852/518, no substitutions; cues determine read order, not defects. Full before-and-after dossier/source readings, five actual checks per file and five separate verified unit pushes are recorded in [closure evidence](SE_APPEARANCE_REVIEWS/B148_CLOSE.json).

All five primaries received limited supported repairs, but all five whole-file logical outcomes remain held; no completed entity appearance or duplicate equipment credit. No change0/5, so no5→7extension. Counters remain12/301SE,245/301all-types and245/287Weapon. Ledger8changed/4retained/7held/2blocked/280pending; prior12not retroactively certified. Current validation tools cannot establish narrative coherence.

Batch149 is not authorized. Batch301 remains blocked on eight owner-provided bodies and owner4+4selection; generate/validate before wiki copy. PR14OPENdraft→NON-WIKI, ownermergeonly. Historical holds preserved; no artwork completion claimed.

## Batch149 — CLOSED 5/5

Fresh owner P authorizes149only under [R-33 Integrity Visual Live Check Rule](RULES/R-33_INTEGRITY_VISUAL_LIVE_CHECK.md). Opening queue180/330/565/Maw001/585 came from280pending/127reading-cue candidates; that opening snapshot is historical. All five reviews are now complete and held, with no completed-fix credit. [Opening evidence](SE_APPEARANCE_REVIEWS/B149_OPEN.json). Written-design work, not rendered or live-preview verification. No150authorization.


Five complete before/source/final written-design reviews. Five primaries changed; **all five logical outcomes HELD**. Each limited repair passed five checks and its individual gate/verified push. No change **0/5**, so the three-No-change ladder does not open seven. Fresh closing checks **25/25 PASS**, ledger tests **10/10 PASS**, labels **301/301**, couples **0/301**, comparison **287 complete sets / 861 item pairs**; candidates are not resolutions.

- **Owed `C-IIIγ-180`** — [held](SE_APPEARANCE_REVIEWS/B149_01_OWED.md), `060f8b8` PUSH VERIFIED. 7,440→7,674 words.
- **Frozen Window `C-IIβ-330`** — [held](SE_APPEARANCE_REVIEWS/B149_02_FROZEN_WINDOW.md), `51fe931` PUSH VERIFIED. 7,945→8,207 words.
- **Broken Well `C-IIβ-565`** — [held](SE_APPEARANCE_REVIEWS/B149_03_BROKEN_WELL.md), `f7b16cb` PUSH VERIFIED. 7,670→7,933 words.
- **The Maw `C-IVω-001`** — [held](SE_APPEARANCE_REVIEWS/B149_04_THE_MAW.md), `ea24bf8` PUSH VERIFIED. 7,570→7,820 words.
- **Floating Tree `N-IIIγ-585`** — [held](SE_APPEARANCE_REVIEWS/B149_05_FLOATING_TREE.md), `b129240` PUSH VERIFIED. 7,570→7,949 words.

[Closing evidence](SE_APPEARANCE_REVIEWS/B149_CLOSE.json). Primary words 38,195→39,583 (+1,388), C-locale counts. Current counters: SE12/301=3.99%,289remaining (8changed/4retained/12held/2blocked/275pending); ALLTypes245/301=81.40%,56remaining; Weapon245/287=85.37%,42remaining. No equipment coverage increment or body-credit backfill. RuleR33 linked in governance. No rendered/browser/deployment/artwork inspection. Batch150 requires fresh P; no merge. Batch301 still needs eight owner bodies/4+4/generate-validate-before-copy.

## Batch150 — CLOSED 5/5 under Integrity Visual Live Check Rule

Owner p authorizes150only. Fresh275pending/121lexical cue candidates selected Neglect Learned to Listen270 → Inherited Debt019 → Scar Walker011 → Brume007 → Survivors’ Breath895, four matching lines each, ties by full designation. Equipment excluded from screen; cue count is a reading order, not a defect or redesign verdict. No substitutions.

Full current original, exact sources/history, and full final logical reading required underR33. No credit from technical PASS alone. Minimumfive; three cumulative whole-dossier No change triggers5→7→10. All five pending; pending≠No change. Three counters unchanged: SE12/301; ALLTypes245/301; Weapon245/287. No legacy body backfill, source election, fabricated stage, artwork/preview/deployment or merge. No151authorized. Batch301 remains blocked on eight owner bodies/4+4/generate-validate-before-copy. Opening evidence B150_OPEN.json.

[Opening evidence](SE_APPEARANCE_REVIEWS/B150_OPEN.json).

Batch150 unit1: **Neglect Learned to Listen `N-IIβ-270` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B150_01_NEGLECT_LEARNED_TO_LISTEN.md). Movement now describes a spreading place on connected surfaces, not a detached drifting body. N/A Speed now explains absence of a body travel rate and fixed survey reference. Added listening-place/extent note linking nonhuman form, sensation versus anatomy, separate element/manifestation, transferred whispers versus portable kit, and unresolved origins/readability/speech/injury/Transform claims. Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN1/5; No change0/1.

Batch150 unit2: **The Inherited Debt `N-IVβ-019` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B150_02_INHERITED_DEBT.md). No change Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN2/5; No change1/2.

Batch150 unit3: **Scar Walker `O-IIIδ-011` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B150_03_SCAR_WALKER.md). SECC and BreachMovement now explain upright patrol, ordinarypacedescort, undismissedfollowing andclosingondesecration. Restored BattlePhasesResolution with existing respect/salute/acknowledgmentcondition and repaired clipped SustainedObservation with existing ensure-site-not-defiled sentence. Added guardian/grave/carriedweapon note distinguishing collectivephantom, ground, affect, ownarmament andportablekit; explicitlyholdsscar-tissuescaleandweapon-usecontradictions. Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN3/5; No change1/3.

Batch150 unit4: **Brume `O-IIγ-007` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B150_04_BRUME.md). Speed N/A now explains no creaturelocomotionstat andsurveyedmobilePlace edge/bearing/externalclock, not fixedobject. Added travellingPlace note: bankitself, sorrow-not-hiddennomadbodies, silhouettesnotbodilyproof, soundnotmouth, extent/density/personneleffects distinct, noobservedcreatureTransform, andkitoutlines/lightnotfog anatomy. Explicitlyholds incompatiblepace/rate andthinning/dissipation withoutinventedstates. Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN4/5; No change1/4.

Batch150 unit5: **Survivors’ Breath `O-IVδ-895` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B150_05_SURVIVORS_BREATH.md). Identification Position/movement records coldairtrail/temperature/drift/roomscrossed andexplicitnobodilyposture. New sigh/trail/people note connects collectivedetachedbreath, noindividualspeaker/face/lungs, conditionalcoldvisibilitynotdormancy, separatepersonnelroute/ownbreathing/lateeffects, activationthickening/environmentnotbody, and extractedawl/Veil/tokennot sourceanatomy. Huntdiscrepancy explicitlyheld. Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN5/5; No change1/5.

## Batch150 final closure

CLOSED5/5; No change1/5, no extension. All5HELD, four limited repairs; no completedSE increment. Survivors’ Breath fresh exactequipment review adds+1each source-coveragecounter, otherfour+0. SE12/301=3.99%,289remaining; ALLTypes246/301=81.73%,55remaining; Weapon246/287=85.71%,41remaining. Body statuses8changed/4retained/17held/2blocked/270pending. Fresh25checks/10ledgertestsPASS; couples0/301; comparator301/287sets/861pairs. Historical unit snapshots above are not current totals. [Complete closure](SE_APPEARANCE_REVIEWS/B150_CLOSE.md), [raw evidence](SE_APPEARANCE_REVIEWS/B150_CLOSE.json). No151 or merge; Batch301owner-bodyblock unchanged.

## Batch151 — CLOSED 5/5 (opening and unit snapshots below are historical)

Owner p authorizes Batch151 only under R-33. Fresh270pending/117cue candidates; fixed queue Ember Phoenix190 → Heirloom909 → Hollow Saint081 → Burning Root558 → Grieving Maiden041. Signals4/4/3/3/3, ties by full designation; equipment excluded. Reading order, not defect verdict. Full original, exact sources/history and complete final rereading after five actual checks; per-unit Commentary and validated push. Three cumulative No change trigger5→7→10; no forced changes. Counters SE12/301, ALLTypes246/301, Weapon246/287 unchanged. No152 or merge. Batch301owner eight bodies/4+4/generate-validate-before-copy remains blocked. Evidence B151_OPEN.json.

Batch151 unit1: **Ember Phoenix `O-IVδ-190` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B151_01_EMBER_PHOENIX.md). Restored the missing Observation Log heading between the complete equipment source-review note and the existing comprehension/observation records. No body, cycle, value, equipment or Tale prose changed. Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN1/5; No change0/1.

Batch151 unit2: **Heirloom `O-IVδ-909` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B151_02_HEIRLOOM.md). SECC Movement now states stationary chamber with surveyed expanding boundary rather than drifting. N/A Speed distinguishes absent bodily travel from separately recorded wall distances and echo reach. Existing Appearance and all numerical/source claims retained. Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN2/5; No change0/2.

Batch151 unit3: **The Hollow Saint `C-IIIγ-081` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B151_03_THE_HOLLOW_SAINT.md). No change. No primary or linked-source edit; unsupported whole-body or chronology reconciliation deferred explicitly. Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN3/5; No change1/3.

Batch151 unit4: **Burning Root `C-IIIγ-558` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B151_04_BURNING_ROOT.md). Replaced generic SECC gait alternatives with the existing rooting-ahead/tearing-free alternation and permanent floor record. Re-authored generic Registry Trivia classification using the recorded ember-root body, Subject-Grudge and Weight, distinguishing originating family from body. No Appearance anatomy, kit, Tale, or numerical changes. Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN4/5; No change1/4.

Batch151 unit5: **The Grieving Maiden `C-IVβ-041` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B151_05_THE_GRIEVING_MAIDEN.md). No change. No primary or source edits; retain field/assay distinction as written but do not call the broader identity and physical presentation conflicts resolved. Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN5/5; No change2/5.

## Batch151 final closure

CLOSED5/5; No change2/5, no extension. All5HELD, three limited repairs; no completedSE or equipment coverage increments. SE12/301=3.99%,289remaining; ALLTypes246/301=81.73%,55remaining; Weapon246/287=85.71%,41remaining. Body8changed/4retained/22held/2blocked/265pending. Fresh25checks/10ledgertestsPASS; couples0/301; comparator301/287sets/861pairs. Earlier unit snapshots are historical, not current open work. [Complete closure](SE_APPEARANCE_REVIEWS/B151_CLOSE.md), [raw evidence](SE_APPEARANCE_REVIEWS/B151_CLOSE.json). No152 or merge; Batch301owner-bodyblock unchanged.

## Batch152 — CLOSED 5/5

Owner p authorizes Batch152 only under R-33. Fresh265pending/111cue candidates; fixed queue Unspoken Line C-IVδ-251 → Willing Chains C-IVδ-976 → Stormscale Sovereign C-Vδ-949 → Soaking Shadow N-IIIγ-308 → Face Beneath Masks N-IIβ-689. Each3signals, ties by full designation; equipment excluded. Reading order, not defect verdict. Full original/exactsources/history/final logical reread after five actual checks, individual evidence/Commentary/gate/verifiedpush. Three cumulative No change triggers5→7→10. No forced edits. Independent counters SE12/301, ALLTypes246/301, Weapon246/287 unchanged. No153 or merge; PR14OPENdraft→NON-WIKI. Batch301eightownerbodies/one4+4/generatevalidatebeforecopy remainsblocked. Evidence B152_OPEN.json.

Batch152 unit1: **The Unspoken Line `C-IVδ-251` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B152_01_THE_UNSPOKEN_LINE.md). Replaced the generic Fragment/Sovereign identification comparison with fountain, signs, bird avoidance and surveyed seam. Replaced stance/transformation boilerplate with the documented length/bearing, dusk light, bird routes, human crossings and posted conversation record, distinguishing a fixed junction from boundary change and rejecting assumed simultaneous Gauge/visible change. Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN1/5; No change0/1.

Batch152 unit2: **Willing Chains `C-IVδ-976` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B152_02_WILLING_CHAINS.md). No change Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN2/5; No change1/2.

Batch152 unit3: **The Stormscale Sovereign `C-Vδ-949` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B152_03_THE_STORMSCALE_SOVEREIGN.md). Repaired four malformed identification fields into the existing bullet list. Replaced generic live scale/stability survey with historical marker attribution, current Fish/Stone separation observation, no reunification test, and evacuation rather than extending contact to survey a manifest dragon. No source body, numeric or equipment claim elected. Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN3/5; No change1/3.

Batch152 unit4: **Soaking Shadow `N-IIIγ-308` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B152_04_SOAKING_SHADOW.md). Added existing Angry Maiden upright/thickened shadow and temporary outline return, and Frozen Veil non-scorching drips, to Appearance protocol. Separately log outline, grade and scorch hazard with pairing/duration; conditional shadow is not a casting person or ordinary locomotion. Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN4/5; No change1/4.

Batch152 unit5: **Face Beneath Masks `N-IIβ-689` — held**. [Evidence](SE_APPEARANCE_REVIEWS/B152_05_FACE_BENEATH_MASKS.md). No change Five actual checks PASS and full final read complete; individual gate/push follows. Current batch OPEN5/5; No change2/5.

## Batch152 final closure

CLOSED5/5; No change2/5, no extension. Three limited repairs and all five HELD; zero completedSE or equipment coverage credits. SE12/301=3.99%,289remaining; ALLTypes246/301=81.73%,55remaining; Weapon246/287=85.71%,41remaining. Body8changed/4retained/27held/2blocked/260pending. Fresh25checks and10ledger testsPASS; couples0/301; comparator301mapped/287complete sets/861pairs. Earlier open checkpoints are historical. [Full closure](SE_APPEARANCE_REVIEWS/B152_CLOSE.md), [raw evidence](SE_APPEARANCE_REVIEWS/B152_CLOSE.json). No153 or merge; Batch301 owner-body block unchanged.

## Batch153 — OPEN 0/5

Owner p authorizes Batch153 only. Fresh260pending/107cue candidates, equipment excluded. Fixed order N-IIβ-801 Mirror of Soaking → N-IVδ-821 Pent → O-IIIγ-476 Sehnsucht → O-IIIγ-617 Exiles’ Wall → O-Iα-189 Ephemera, each3signals with full-designation tie order. Cues are not defects. Complete original/exact-source/history and complete final logical reading after five actual checks; individual Commentary/evidence/gate/verified push. Three cumulative No change triggers5→7→10. No forced edits, duplicate equipment or legacy body credit. Counters unchanged: SE12/301, alltypes246/301, Weapon246/287. No154 or merge. PR14OPENdraft→NON-WIKI. Batch301eightownerbodies/one4+4/generatevalidatebeforecopy remainsblocked.

Checkout recovery: local10cd20a versus remote2deae5b; all2370remote tracked files, including Unicode paths, hash-matched current files. Branch/index restored by mixedreset only, no working file rewritten or owner file discarded. Scratch helpers from prior turn unavailable; committed evidence is intact.

Batch153 unit1: Mirror of Soaking — **No change; HELD**. Complete448-line original/final and exact sources/history read; five actual checksPASS. [Evidence](SE_APPEARANCE_REVIEWS/B153_01_MIRROR_OF_SOAKING.md). Batch153OPEN1/5, No change1/1; four pending. No credit increment; individual gate/push follows.

Batch153unit2: Pent — **No change; HELD**. Complete472-line original/final and exact sources/history read; fiveactualchecksPASS. [Evidence](SE_APPEARANCE_REVIEWS/B153_02_PENT.md). Batch153OPEN2/5, No change2/2; threepending. Credit+0; individual gate/push follows.

Batch153unit3: Sehnsucht — Movement summary restored to include both sinking and recorded rises. R18:1 batch-short/0 careful-detail; only one clause replaced, original is retained in opening snapshot. **HELD.** FiveactualchecksPASS; fullreadings in [Evidence](SE_APPEARANCE_REVIEWS/B153_03_SEHNSUCHT.md). Batch153OPEN3/5, No change2/3; credit+0. Individual gate/push follows.

Batch153unit4: Exiles’ Wall — Restored blank M.A.W. summary grade to α for all three primary pieces, distinct from source γ. R18:1 batch-short/0 careful-detail; only the blank summary row changed. **HELD.** FiveactualchecksPASS; fullreadings in [Evidence](SE_APPEARANCE_REVIEWS/B153_04_EXILES_WALL.md). Batch153OPEN4/5, No change2/4; SEcredit+0, newequipmentcoverage+1both. Individual gate/push follows.

Batch153unit5: Ephemera — Appearance now attributes survivor clarity to the reader, not proximity-driven alteration of the figure. R18:1 batch-short/0 careful-detail; one Notable Features clause, source Observation Log retained intact. **HELD.** FiveactualchecksPASS; fullreadings in [Evidence](SE_APPEARANCE_REVIEWS/B153_05_EPHEMERA.md). Batch153OPEN5/5, No change2/5; credit+0. Individual gate/push follows.

## Batch153 — CLOSED5/5

Three bounded corrections, two **No change**, all five **HELD**. ALLTypes247/301(82.06%,54remaining),Weapon247/287(86.06%,40remaining); SE12/301(3.99%,289remaining). Exiles’ Wall fresh sourcecredit+1both, otherfour no duplicate. Body8changed/4retained/32held/2blocked/255pending. No change2/5: no expansion. Fresh25checks/10testsPASS,301PhysicalForminventory,source/equipment/digit/296unselectedprimaryinvariants. [Full linked results and individual Commentary](SE_APPEARANCE_REVIEWS/B153_CLOSE.md); [raw evidence](SE_APPEARANCE_REVIEWS/B153_CLOSE.json). No154/merge. Nextbatch requiresnewp; Batch301remainsblocked.

## Batch154 — OPEN 0/5; improve the documents

Owner “p + always fixwd/make the docs batter” authorizes154only and reinforces active source-supported improvement of each whole dossier, not an issues-only audit. Fresh255pending/102cue candidates; fixed Forgotten TearO-Iα-709 → Debt EaterC-IIIβ-014 → Debt ScaleC-IIIβ-015 → DebtorC-IIIγ-061 → RejectorC-IIIγ-063. Complete original/exact sources/history and complete final reading, five actual checks, individual Commentary/gate/verified push. Three cumulative No change triggers5→7→10; no forced edits or invented canon.

Openingbase8a5090c1a3c874158097370fa703ea98035b810e. All2379remote-tracked working bytes matched before index/HEAD-only recovery, no documents rewritten. Evidence `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B154_OPEN.json`. Counters unchanged: ALLTypes247/301,Weapon247/287,SE12/301. No155/merge; PR14OPENdraft→NON-WIKI. Batch301eightownerbodies/one4+4/generatevalidatebeforecopy remainsblocked.

Batch154 unit 1: **Forgotten Tear — HELD**. Five bounded replacements: correct Movement from a structure/location to a crystal that never moves itself but can be carried; make Recommended response acknowledge the death without inventing the unknown mourner and preserve the timed/incident record; make all three five-minute instructions defer to the existing timed contact entries and living-name hard stop. No new interval, threshold, anatomy, transformation or equipment statistic. [Full evidence](SE_APPEARANCE_REVIEWS/B154_01_FORGOTTEN_TEAR.md). OPEN 1/5; No change 0/1. Independent counters unchanged; gate/push follows.

Batch154 unit 2: **The Debt Eater — HELD**. Two source-supported clarifications: Battle Phases now identifies the oversized hands and mouthless body using the existing two-other-small-subjects comparison, rather than an irrelevant claim that half the holdings are tall; Stigma Appearance explicitly distinguishes this set pendant from the separately registered Debt Scale Object. No changed anatomy, attack, stat, threshold, range, form chronology or permission. [Full evidence](SE_APPEARANCE_REVIEWS/B154_02_DEBT_EATER.md). OPEN 2/5; No change 0/2. Independent counters unchanged; gate/push follows.

Batch154 unit 3: **The Debt Scale — HELD**. Three bounded clarifications: Movement now separates plinth-fixed instrument, unaided frame/dish articulation and expanding weighed circle; Appearance identifies this Object rather than Debt Eater’s same-named Stigma; Appearance protocol repeats the existing no-mounted-sensors rule and distinguishes eye-recorded dish series from the wing’s numerical conversion. No change in Work permissions, anonymous/named readings, damage, values or body form. [Full evidence](SE_APPEARANCE_REVIEWS/B154_03_DEBT_SCALE.md). OPEN 3/5; No change 0/3. Independent counters unchanged; gate/push follows.

Batch154 unit 4: **The Debtor — HELD**. Five bounded replacements: both Appearance position descriptions now include the explicitly documented seated Flerehan response; Appearance protocol no longer claims only the recited total can change or that three appearance fields are the whole record; both interaction methods respect the permanent-neighbour/no-solo-baseline limitation and prohibit separation merely to supply a control. Anatomy, mass values, combat, Work responses and all equipment unchanged. [Full evidence](SE_APPEARANCE_REVIEWS/B154_04_DEBTOR.md). OPEN 4/5; No change 0/4. Independent counters unchanged; gate/push follows.

Batch154 unit 5: **The Rejector — HELD**. Three source-supported procedure repairs plus two formatting corrections: Appearance protocol now records actual recurrence and the worker’s within-hour memory loss instead of claiming he never repeats; both interaction methods distinguish archived separation evidence from permission for a fresh trial; removed stray trailing pipes from Escalation Notes and equipment Stat interpretation. No body, family, effect, threshold, timing or numerical change. [Full evidence](SE_APPEARANCE_REVIEWS/B154_05_REJECTOR.md). OPEN 5/5; No change 0/5. Independent counters unchanged; gate/push follows.

## Batch154 — CLOSED 5/5; five documents improved

The owner’s “p + always fixwd/make the docs batter” is implemented as a standing source-supported improvement reminder in R-33. All five complete reviews produced useful primary-document corrections, not only hold reports.

- Forgotten Tear: timed handling and unknown-mourner guidance; carried crystal, not a structure.
- Debt Eater: reliable hands/mouthless identification and clear Stigma-versus-Object identity.
- Debt Scale: fixed instrument versus articulation/field expansion; no-mounted-sensors and conversion guidance.
- Debtor: documented seated Flerehan posture and honest, proximity-safe baseline methods.
- Rejector: recurrence/memory-loss recording method, no-new-separation instructions, and two stray prose separators.

All five whole designs remain HELD. Independent counters are unchanged: ALL M.A.W. Types Appearance per SE 247/301 (82.06%), 54/301 remain; ALL M.A.W.-W Appearance per SE 247/287 (86.06%), 40/287 remain; SE Appearance Fix 12/301 (3.99%), 289/301 remain. SE statuses: 8 changed, 4 retained, 37 held, 2 blocked, 250 pending. These are source-review coverage and written-design completion, not artwork.

All five original/exact-source/history/final readings, five actual validators per unit and individual verified pushes are recorded. Closing reran all 25 checks; ten ledger tests passed; couples 0/301; comparator inspected 301/292/287/861 with 557 candidate findings, not defect verdicts. Digits, all 301 classification Physical Form rows, equipment statistics, all sources and 296 unselected primaries unchanged. Declared equipment prose exceptions are explicit. Total words 38,283→38,736 (+453). No change 0/5; no ladder extension.

[Readable report](SE_APPEARANCE_REVIEWS/B154_CLOSE.md) and [raw evidence](SE_APPEARANCE_REVIEWS/B154_CLOSE.json) under REFERENCE_SOMNARAK_WIKI. No155 or merge. PR14 OPEN draft to NON-WIKI. Batch301 remains blocked on eight owner bodies, one4+4, generation/validation before copy. Closure gate/verified push follows.

## Batch155 — OPEN 0/5

Owner p after Batch154 authorizes this next batch only. The fresh screen finds 97 cue candidates among 250 pending dossiers. Fixed first five: Learned Your Face C-IIIγ-195, Spreading Well C-IIIγ-373, Emberling C-IIβ-101, Laughing Mask C-IIβ-210, Broken Compass C-IIβ-290. Full original/exact-source/history and final reading, supported improvements, five actual validators, individual Commentary and verified push are required. Three cumulative No change reviews trigger 5→7→10; no forced edits.

Opening evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B155_OPEN.json`. All2388remote-tracked files matched75ae73e before metadata-only recovery; no document rewritten. Independent counters unchanged: ALL Types247/301, Weapon247/287, SE12/301. No Batch156 or merge. PR14 OPEN draft to NON-WIKI. Batch301 awaits eight owner bodies in one4+4operation, generation/validation before copy.

Batch155 unit 1: Learned Your Face — HELD. Three supported repairs: summary M.A.W. grade restored to γ; Appearance reporting no longer invites reflection contents into the record; initial-exposure identification pairs range with learned-face count without requiring a fresh viewer. [Evidence](SE_APPEARANCE_REVIEWS/B155_01_LEARNED_YOUR_FACE.md). OPEN 1/5; No change 0/1. Counters unchanged; gate/push follows.

Batch155 unit 2: Spreading Well — HELD. Five supported repairs: three Appearance markers distinguish fixed rim from spreading channels; the Appearance protocol retains rim sounding and seep/depth observations; Suit prose no longer denies the Weight protection recorded in its table. [Evidence](SE_APPEARANCE_REVIEWS/B155_02_SPREADING_WELL.md). OPEN 2/5; No change 0/2. Counters unchanged; gate/push follows.

Batch155 unit 3: Emberling — HELD. Three supported repairs: Work summary states Pugnahan is historical and prohibited; initial observation names carried ember and cautious gait; Appearance protocol labels body versus carried-ember light instead of giving an unqualified brightness verdict. [Evidence](SE_APPEARANCE_REVIEWS/B155_03_EMBERLING.md). OPEN 3/5; No change 0/3. Counters unchanged; gate/push follows.

Batch155 unit 4: Laughing Mask — HELD. Five supported replacements: β equipment grade; non-wearing identification; Stigma charm named in removal cost; +1Composure specified; Use Notes add Empty Ovation/Unscripted Pause, protected memory, identity-fact rear removal, named remover and non-morale restriction. [Evidence](SE_APPEARANCE_REVIEWS/B155_04_LAUGHING_MASK.md). OPEN 4/5; No change 0/4. ALL Types +1; Weapon +1; SE +0; gate/push follows.

Batch155 unit 5: Broken Compass — HELD. Four supported repairs: completed the clipped activation warning; normalized Weapon Appearance label; initial observation checks concrete identity before timing; activation flavor no longer contains a broken Tool Use Profile fragment or implies a Work instruction to lift the compass. [Evidence](SE_APPEARANCE_REVIEWS/B155_05_BROKEN_COMPASS.md). OPEN 5/5; No change 0/5. ALL Types +0; Weapon +0; SE +0; gate/push follows.

## Batch155 — CLOSED 5/5; five dossiers improved

All five fresh reviews made source-supported document improvements; all five whole designs remain HELD. No change0/5; no extension. Exactly Laughing Mask adds one new complete equipment-set review and one exact Weapon-pair review. Counters: ALL M.A.W. Types Appearance per SE248/301(82.39%),53/301remain; ALL M.A.W.-W Appearance per SE248/287(86.41%),39/287remain; SE Appearance Fix12/301(3.99%),289/301remain. Equipment coverage includes source holds, not completed artwork.

Changes: Learned Your Face grade/privacy/identification; Spreading Well rim/reach/protocol/resistance prose; Emberling current Work/identification/brightness labels; Laughing Mask grade/Composure/set safeguards; Broken Compass clipped warning/identification/activation fragment/Appearance label. Each individual review has Commentary, sources, complete readings, five actual checks, commit and verified push.

Closing audit:25fresh validators PASS,10ledger tests PASS,couples0/301,557candidate comparator differences. Every digit sequence, numerical equipment value and all301classification Physical Form rows unchanged;296unselected primaries and fingerprinted sources unchanged. Words38,861→39,105(+244). No156or merge; PR14OPENdrafttoNON-WIKI. No artwork/browser/live-site check. Batch301remains blocked on eight owner bodies, one4+4operation, generate/validate before copy.

[Readable close](SE_APPEARANCE_REVIEWS/B155_CLOSE.md) · [Raw evidence](SE_APPEARANCE_REVIEWS/B155_CLOSE.json).

## Batch156 — OPEN 0/5

Owner p after Batch155 authorizes Batch156 only. Fresh pending-only screen:245dossiers,92cue candidates. Frozen first five: Labyrinth of Stolen Faces C-IVγ-180; Blackened Angel C-IVγ-946; Gavel C-IVδ-140; Rising Wall C-IVδ-255; Swallow C-IVδ-767. Cues prioritize reading rather than diagnose defects. Full original/exact-source/history reading, supported improvements, five actual validators, full final reading and individual Commentary/gate/verified push required. Three cumulative No change dossiers trigger5→7→10. Pending is not No change.

Opening evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B156_OPEN.json`. All2397remote-tracked working files matchedac6bdf0 before metadata-only recovery. No working document overwritten. Independent counters unchanged: ALL Types248/301,Weapon248/287,SE12/301. No157or merge. PR14OPENdrafttoNON-WIKI. Batch301awaits eight owner bodies in one4+4operation, generate/validate before copy.

**Batch156 / unit1 — Labyrinth of Stolen Faces `C-IVγ-180`:** [[SE-C-IVγ-180_Labyrinth_of_Stolen_Faces_기억의_미로](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-180_Labyrinth_of_Stolen_Faces_%EA%B8%B0%EC%96%B5%EC%9D%98_%EB%AF%B8%EB%A1%9C.md "SE-C-IVγ-180_Labyrinth_of_Stolen_Faces_기억의_미로.md")] Restore the missing summary γ grade from all three primary items and Master/A. Replace the Detailed Appearance movement cell’s repeated generic monitoring phrase with the file’s own fixed-entrance/interior-corridor distinction. Replace the nonspecific response summary with the explicit existing anchor/time/line recovery rule. No new Work permissions, forms or numerical changes.

**Evidence/history:** Exact1018 A–D complete; Master214–216 index/details3232–3261; Entity437; complete Tale72 4080–4133; CSV234–237; archetype418; disposition400; complete original434lines and Batch132unit3 evidence/history. 222d4c4eb7051d7fef3e387fa9debe243780cf87 Batch132unit3 explicitly credited the complete set and exact SE-1018-B/MAW-W-1018-01 pair. Owed SE-180/MAW-W-180 is a distinct source; no suffix-only matching. Complete primary original/final reading and all five actual validators PASS. LC_ALL=C wc -w 7564→7576; digit sequences preserved. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B156_01_LABYRINTH_OF_STOLEN_FACES.md`.

**Holds:** Primary non-breaching/no transformation versus exact A transform-capable. Interior rearrangement is compatible with a stationary entrance, but ultimate surface expansion/no outside left versus entrant-confined disposition lacks a supported limit and return account. Registrum and Master Tale Viderehan-only versus Behavior/A Ferrehan valid; gauge never falls versus Ferrehan Decrease; 75% activation versus65%ultimate retained, not conflated. Unentered maze never changes versus incoming forgotten-memory expansion, aboveground reports and nonvisitor material accumulation. Tale does not harm versus conditional identity-eroding damage requires an operational/chronological account rather than deleting either. No amnesia versus per-use nameless memory loss; lens optical disc versus scimitar archetype; A–D insufficient physical forms to certify whole set. Head versus pendant/choker classification, CSV5% versus4%, broad source bonus and nonspecific full-set stabilization remain held. Minor wording repairs do not authorize free navigation or source extraction.

**Commentary:** The fixed entrance makes the changing interior legible without making it safe. I find the outside handler more convincing than any map: the person who cannot share the borrowed memories is the one who can bring an entrant back.

**Counters/progress:** Equipment both+0; SE+0,HELD. Batch156OPEN1/5. Pending≠Nochange; cumulative three Nochange triggers5→7→10. Written-design only; no artwork/preview/deployment/157/merge.

**Batch156 / unit2 — Blackened Angel `C-IVγ-946`:** [[SE-C-IVγ-946_Blackened_Angel_검어진_천사](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-946_Blackened_Angel_%EA%B2%80%EC%96%B4%EC%A7%84_%EC%B2%9C%EC%82%AC.md "SE-C-IVγ-946_Blackened_Angel_검어진_천사.md")] Three source-supported instruction repairs: include spoken or clearly-thought wishes in the activation summary; describe Viderehan as observation rather than a gauge-reduction guarantee; replace the speech-only/no-other-change escalation paragraph with recording instructions that also capture reported directed thoughts and already documented Face strain. Preserve unresolved assurance-reading, materials, range, tear history and channel relationships.

**Evidence/history:** Complete primary513lines and exact946A–D; CSV1091–1094, archetype392 and disposition328. Repeated full Master MAW/Entity/Tales searches by946, English/Korean name, Shrine and three item names: only EntityCodex359 awaiting-row note; no dedicated Master entry/Tale exists. Entire current primary Tale read. Read full Batch140unit3 history and durable earlier range-review record. Batch140unit3 c9a389826c1430ac5c53e81ac31e4bd323daac9d explicitly confirms prior Batch84unit1 exact Plume review and both credits already covered. Historical6b09d5c4 object is unavailable in this shallow checkout; durable Batch84/140 logs are evidence, not an invented re-fetched commit. Both equipment increments zero. Complete primary original/final reading and all five actual validators PASS. LC_ALL=C wc -w 9763→9785; digit sequences preserved. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B156_02_BLACKENED_ANGEL.md`.

**Holds:** Cast metal versus carved stone; statue as source versus Apex tarnish is the entity; static tarnish/unaltered figure versus expansion and visibly changing Face remain uncrosswalked. A transform-capable versus primary nonbreaching, shattering/reformation/elsewhere versus fixed shrine, and return/spatial extent remain held. Primary wishes/clearthought versus speech-only remaining combat/Core/Story accounts; channel concentration/adjacent stabilization versus automatic compelled wishes and no-pairing suppression; no established current granting capacity versus explicit grants. Revised summary does not settle every contradictory clause. All-black present tears versus blue-child event and historical foresight study; cruelty index versus actual knowledge of prospective harm; every speech tear versus wish trigger;31/34blue assurance readings versus current black-only and34total versus34percycle. Study and crew objection preserved, not rewritten as a resolved instrument. Primary range2Medium versus A/B3Medium and archetype Close Cestus; physical forms missing from individual B/C/D, CSVAccessory5% versus Hand4%; set-wide difficulty refusing versus piece-specific unwillingness to ask, unwelcome wishes and involuntary tears; full-set/body-site corrosion insufficiently specified. No numerical normalization or new mode.

**Commentary:** The lamp kept lit is an act of care that asks nothing back. The later assurance scheme unsettles me more than the cruel Collector: it turns an accurate reading into permission not to understand the people affected.

**Counters/progress:** Equipment both+0; SE+0,HELD. Batch156OPEN2/5. Pending≠Nochange; cumulative three Nochange triggers5→7→10. Written-design only; no artwork/preview/deployment/157/merge.

**Batch156 / unit3 — Gavel `C-IVδ-140`:** [[SE-C-IVδ-140_Gavel_철의_판관](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-140_Gavel_%EC%B2%A0%EC%9D%98_%ED%8C%90%EA%B4%80.md "SE-C-IVδ-140_Gavel_철의_판관.md")] Two supported repairs: replace generic first-contact pressure-only/no-sound-or-motion wording with the actual sealed face/chest scale/hot-iron markers and existing independent sealed reporting rule; clarify that Iron Plate resists Grudge pressure but does not make the verdict itself resistible, using Core Resistance and exact Suit/Master ability. No change to physical classification, walking capability, Work permissions or values.

**Evidence/history:** Full426line primary; complete exact1014A–D; Master index244–246/details3566–3597; Entity447; complete Tale82 4645–4699; CSV218–221, archetype414 and disposition405. Original entity/body/equipment reviewed together. ecd502a actual stat plus durable unit5 history read; it changes only primary, not admin history in that commit. Batch120unit5 ecd502ac22bf4271e63937d73360662c27147944 and the complete durable Batch120 opening/pair audit/unit5/closing record already count full set and SE-1014-B/MAW-W-1014-01. Numeric suffix140 Weeping Willow is distinct. Both equipment increments zero. Complete primary original/final reading and all five actual validators PASS. LC_ALL=C wc -w 7664→7676; digit sequences preserved. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B156_03_GAVEL.md`.

**Holds:** The Tale/Entity Master weigh numbers without hearing versus current scale rewarding completeness/hearing and explicit primary correction of older Work instructions. Primary explicitly corrects old Pugnahan-primary and omit-circumstances record; those instructions were not silently reintroduced. No independent historical transition establishing a changed entity. Handless implement/falling Gavel versus upright iron judge raising a gavel; indiscriminate hunt versus breach confined to absent-person decision rooms and chairperson-first. Fixed rest and walking breach are compatible states, but these target/implement accounts are not fully joined. Threshold1, Core90% and65%ultimate have no complete mapping; breach drain5 and gauge10 are distinct quantities not automatically a numeric contradiction. Remote scale response/field jurisdiction remains separate from body travel; no invented body size or pursuit exception. Disposition says nothing structural against cracked walls and structural-pressure record. Primary slender blade/MAW-W-1014blade archetype versus Master gun; exact B/C/D do not supply full physical forms. Stigma boon/effect and set-wide certainty versus piece costs remain unmapped; CSV5% versus4%, generic stat bonus and tail-slot placement retained. Body-site terminal corrosion lacks a whole-source relationship.

**Commentary:** A sealed face makes the clerks’ accounts carry the interpretation instead of an expression. The strongest tension is that submitting the whole record becomes a habit, while nobody acts on what those complete records reveal.

**Counters/progress:** Equipment both+0; SE+0,HELD. Batch156OPEN3/5. Pending≠Nochange; cumulative three Nochange triggers5→7→10. Written-design only; no artwork/preview/deployment/157/merge.

**Batch156 / unit4 — Rising Wall `C-IVδ-255`:** [[SE-C-IVδ-255_Rising_Wall_솟아오른_벽](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-255_Rising_Wall_%EC%86%9F%EC%95%84%EC%98%A4%EB%A5%B8_%EB%B2%BD.md "SE-C-IVδ-255_Rising_Wall_솟아오른_벽.md")] Four bounded repairs: restore δ summary grade from all three pieces/A/Master; replace broken Appearance protocol fragments with existing outline/height/clearance/marked-line/single-voice observations; repair the broken Identification sentence using current concrete markers without a new exposure test; close the unmatched italic marker on the existing Stigma bestowal paragraph. No invented size, surface, movement transition, deposit decision or value.

**Evidence/history:** Full465line primary including entire reconstruction/legal/deposit proposal; complete exact1026A–D; Master277–279 index/details3929–3960; Entity458; complete Tale93 5256–5310; CSV266–269, archetype426, disposition330; full Batch134unit2 history. Batch134unit2 d3f4c2e1a18877d8c8450db24d26397fd384bab2 already completed full set and exact SE-1026-B/MAW-W-1026-01. Source255 Hollow Architect C-IVγ-255 is distinct. Both equipment increments zero. Complete primary original/final reading and all five actual validators PASS. LC_ALL=C wc -w 8338→8358; digit sequences preserved. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B156_04_RISING_WALL.md`.

**Holds:** Retained annual/after-session height and never falling versus explicit Work lowering; invisible pressure/no mass/no surface versus bricks, falling wounds and enclosed structure; humane no-injury record versus conditional combat damage. Neither growth nor mobile Subject implies a literal masonry body; no new material or timeline selected. Indiscriminate hunt versus grief-directed noninterception and no injuries; primary Work list permits Pugnahan while recommendation/Apex prohibit its use. 1/90%/65%threshold scopes still unmapped. Sound/pressure/physical travel and spatial scale need a joined account, not a colour relabel. Unreturned love summary versus Tale formerly mutual love; origin lifetime ended versus continuing one-sided recall chronology not established. Tale ZoneC/Advanced3/Low versus primary ZoneD/Basic2/Critical includes explicit primary correction for level/rating; Master not rewritten. Architectural particulars and currently outstanding deposit proposal preserved in full. Primary resonant crystal blade/Master versus archetype Room tombstone sledge; silk Shroud versus Master living-carapace category; primary perfect-retention Weapon toll versus B unwept grief/weeping; all-piece same cost versus Suit numbness and Stigma attachment truth. Tail4% versus CSVAccessory5%, unnamed bonus and body-site corrosion stay held.

**Commentary:** The Wall’s pressure outline is more specific than a pile of masonry: the barrier is the burden of keeping a shared past alone. Its reconstruction becomes especially painful when the institution trusts it underground but refuses to file it beside the erased district’s record.

**Counters/progress:** Equipment both+0; SE+0,HELD. Batch156OPEN4/5. Pending≠Nochange; cumulative three Nochange triggers5→7→10. Written-design only; no artwork/preview/deployment/157/merge.

**Batch156 / unit5 — Swallow `C-IVδ-767`:** [[SE-C-IVδ-767_Swallow_번져가는_그림자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-767_Swallow_%EB%B2%88%EC%A0%B8%EA%B0%80%EB%8A%94_%EA%B7%B8%EB%A6%BC%EC%9E%90.md "SE-C-IVδ-767_Swallow_번져가는_그림자.md")] Three supported repairs: replace the Identification light-raising test with existing fixed-level/chalk/detail markers; replace the departure claim of containment with custody without control and the existing outside attribution screen; make the activation Risk cell describe misattributed grief rather than refer vaguely to Behavior and a nonexistent Activation section. Preserve the fragile boundaries between screening and the protected attributed line.

**Evidence/history:** Complete472line primary; exact767A–D complete; Master298–300 index/details4161–4192 and duplicate-title Fading Ruin703 inspected/excluded; Entity465; complete current Master Tale100 5645–5698 (older receipt called it97); CSV859–862; archetype316; disposition237; full Batch129unit2 and follow-up history. Batch129unit2 2535efca038f9ff4922303fe8870ed3d60b6c930 explicitly added complete set and exact SE-767-B/MAW-W-767-01 coverage; follow-up d2c8a51fe45d35a90a3cc0dba92bded3296347c3 separately removed a duplicated location, not a second coverage unit. Swallowed Fury683 and Fading RuinO-Iα-189/Master703 duplicate weapon title are distinct. Both equipment increments zero. Complete primary original/final reading and all five actual validators PASS. LC_ALL=C wc -w 8309→8364; digit sequences preserved. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B156_05_SWALLOW.md`.

**Holds:** Primary non-breaching versus exact A Can breach via Transform; stationary no-body dimming region versus fading/sharpening/striking Shadow, forced disappearance and aimed purposeful activation. No invented mobile shadow body, attack permission or source return. Primary no-injury/no-strike account and conditional combat descriptors require an explicit account; numbers alone are not evidence of injury history. Four attributed-quarter withdrawals correlate with lines but establish no repeatable remedy; cannot reduce or bound is operational custody, not proof that historical reversals never occurred. Chalk oldest outermost and continuing spread/reversal geometry need a dated spatial history. Additional light invariance is an observed history, not permission to rerun a harmful test. Unrecognised loss/no office willing to record versus every visitor’s borrowed grief at memorial in A/Tale: relationship not fully established, do not erase legal setting or import a new formation. Master Tale Flerehan-only versus current primary/A Viderehan/Ferrehan only; Basic2/Critical versus old Advanced3/Moderate. Protected attributed line never tested/evidence versus counselor naming requirements are distinct instruments, not merged into leave proof. Primary crystal blade/Master resonant blade versus hanging memorial bell/Close archetype; B/C/D Appearance paragraphs chiefly operational rather than concrete physical crosswalks. Primary return reverses toll versus item shutdown no-refund; generic bodily/composure/memory debit versus individual grief costs; Charm precise truth versus source minor boon, Tail4% versus CSVAccessory5%, unknown +3 stat and body-site corrosion retained. Operational inventory says objects set down are never recovered, while Registry Trivia says takes nothing material and specifically excludes object-consuming holdings. Loss of recoverability does not prove consumption, but the material/recovery account is not fully specified. No objects erased from the inventory or source permissions inferred.

**Commentary:** Keeping the light fixed makes the gloom an observed condition rather than a puzzle someone must solve by spending more power. The attributed line matters because it lets a loss be named without turning the mourner’s account into another application to be judged.

**Counters/progress:** Equipment both+0; SE+0,HELD. Batch156OPEN5/5. Pending≠Nochange; cumulative three Nochange triggers5→7→10. Written-design only; no artwork/preview/deployment/157/merge.

## Batch156 — CLOSED 5/5; five dossiers improved

Five complete fresh reviews, each original/exact-source/history/final read with five actual checks, Commentary and an individual verified push. All five whole designs remain HELD; SE+0 and both equipment+0 because all exact pairs were previously covered. No change0/5; no extension.

Changes: Labyrinth grade/fixed-entrance geometry/tether recovery; Blackened Angel thought-trigger/observation response/Face recording; Gavel concrete contact/pressure-versus-verdict protection; Rising Wall grade/broken identification/protocol/italic closure; Swallow fixed-light identity/custody/attribution risk. Fifteen exact replacements, digits and all301classification Physical Form rows unchanged. Words41,638→41,759(+121), LC_ALL=Cwc.

Closing25fresh validators PASS;10ledger tests PASS;couples0/301;557comparator candidates, not automatic defects.296unselected primaries and all fingerprinted sources unchanged. Full frozen92candidate ranking reproduced from245pending. Counters: ALL M.A.W. Types Appearance per SE248/301(82.39%),53/301remain; ALL M.A.W.-W248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. States8changed/4retained/47held/2blocked/240pending.

[Readable close](SE_APPEARANCE_REVIEWS/B156_CLOSE.md) and [raw evidence](SE_APPEARANCE_REVIEWS/B156_CLOSE.json). PR14OPENdrafttoNON-WIKI; owner controls merge. No157/artwork/preview/deployment. Batch301still waits for eight owner bodies/one4+4/generatevalidatebeforecopy. Final standalone report corrects earlier abbreviated progress note’s missing hash and explicit named counters.

## Batch157 — OPEN 0/5; WIP and CHANGELOG maintained together

Owner repeated p authorizes Batch157 only, not two batches. The owner also requests continuing WIP and CHANGELOG updates: both accompany each completed unit and closure, with source evidence, unresolved holds, actual checks and verified pushes. Batch156 and its five individual units already contain both records.

Fresh pending-only screen:240dossiers,87cue-bearing candidates. Exclude exactly M.A.W. Equipment; rank matching-line count descending, then full designation. Frozen order: Rising Well C-IVδ-869, Kind Healer C-Iα-071, Torn Flower C-Iα-247, Mirror of Rising C-Iα-392, Absent Landmark C-Iα-863. Each has two cues; cues prioritize reading, not defects. All five are pending, not No change. Minimum5; cumulative3Nochange triggers5→7→10.

Recovered stale HEAD/index after proving all2406remote-tracked working files byte-identical to50d2a18; metadata-only mixed reset, no working-file overwrite. Exact selected originals frozen. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B157_OPEN.json`. Whole-file original/exact-sources/history/final readings, supported document improvements and independent Commentary required. No invented design resolution, automatic SE credit, artwork, preview,158or merge. Batch301still blocked on owner eight bodies/one4+4/generatevalidatebeforecopy.

Independent counters unchanged: ALL M.A.W. Types Appearance per SE248/301(82.39%),53/301remain; ALL M.A.W.-W248/287(86.41%),39/287remain; SE Appearance Fix12/301(3.99%),289/301remain.

**Batch157 / unit1 — Rising Well `C-IVδ-869`:** [[SE-C-IVδ-869_Rising_Well_솟아오른_우물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-869_Rising_Well_%EC%86%9F%EC%95%84%EC%98%A4%EB%A5%B8_%EC%9A%B0%EB%AC%BC.md "SE-C-IVδ-869_Rising_Well_솟아오른_우물.md")]

Identification now uses existing ordinary-contact subjective song/rim reports instead of promising an exterior visible shaft; preserves the two Wrath Flame exceptions as exceptional, not repeatable tests. Three event-article errors corrected. No attack, material, stat, number, timing, permission or source history changed.

**Evidence/history:** Complete original459lines; exact1037A–D complete, SourceSECC C-IVδ-869; Master344–346 and4227–4258; Entity467; complete Tale1025754–5807; CSV310–313; archetype437; disposition278. Full-set primary95note and durable Batch95 WIP4824–4840 read. e68e5673 object unavailable in shallow checkout, so durable prior full-set/pair receipt used, not invented gitshow. Batch95 unit1 e68e5673 explicitly recorded fresh full-set and Weapon-pair review. MAW-W-869 Returning Requiem belongs C-Iα-869; use exact1037. Both equipment increments0. Five actual checks PASS, full final read complete. LC_ALL=C words7480→7484; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B157_01_RISING_WELL.md`.

**Holds:** Subject nonbreaching/transform-in-place versus exact A Can breach. Ordinary invisible inner shaft versus material raised shaft/travel station, inverted water/antigravity/vertical physical hits, heights and seasonal fixed ground. Two recorded Wrath Flame external sightings support exceptions, not every physical combat account or a repeatable trial; mobile people versus stationary shaft still unjoined. Absolute never-visible markers remain broader than those sightings. Source Tale has forgotten inaccessible massacre cause; Apex Buried Record and primary Registrum say comprehensively known/open; director/addendum/hearing objection say documents establish burial but explain no cause. No historical epistemic transition supplied. Association refusal/individual-claim liability is preserved rather than settled. Pugnahan absolute prohibition versus valid listed/exception-on-written-authority; Master Tale explicitly older primary approach with some primary correction, not a new permission. Threshold1/Core90/ultimate65 scopes unjoined. Two-worker contact versus three-person restraint supported different phases, not automatically a contradiction. Work shift lowering is not event lowering. Rising Well Fang/Plate/Stone versus Well Within names; primary iron blade versus Master PRIMAL/Bio/Marrow and optical Instant archetype1037; no B/C/D concrete appearance. Stone Tail4% versus CSVAccessory5% and Masterocular; +3 unspecified stat. Piece-specific physical/mental costs versus uniform invented certainty and personal-grief corrosion need full-source mapping. All exact pairs already counted95.

**Commentary:** The strongest image is not the well but a confident explanation arriving before its evidence. I find the descendants’ refusal of collective registration important: recognising a shared harm need not entitle the institution to classify its people.

**Progress:** Batch157OPEN1/5; No change0/1. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no158/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch157 / unit2 — The Kind Healer `C-Iα-071`:** [[SE-C-Iα-071_The_Kind_Healer_친절한_치유자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-071_The_Kind_Healer_%EC%B9%9C%EC%A0%88%ED%95%9C_%EC%B9%98%EC%9C%A0%EC%9E%90.md "SE-C-Iα-071_The_Kind_Healer_친절한_치유자.md")]

Identification uses established visible form and warns that apparent absence of injury is not safety. Breach announcement now says injured-directed walking and nonviolent return, as the dossier’s explicit correction and disposition already require, instead of indiscriminate hunting. Corrected Not→None in the interaction introduction.

**Evidence/history:** Complete442line original; exact071A–D complete; Master359–361 and4393–4424; Entity35/159/472/491/427; complete Tale1076050–6103; CSV118–121; archetype85; disposition219; durable Batch117unit1 WIP4193–4209 read. Actual requested5c1b44a object absent shallow checkout, so durable history used. Batch117unit1 5c1b44a54287f7e3b1f2d5358259b7ecb82d66e4 already full set and exact SE-071-B/MAW-W-071-01. Blessing Giver, Apostle Maker, Dawn and Shadow are distinct states/identities, not extra pair credit. Five actual checks PASS, full final read complete. LC_ALL=C words7699→7721; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B157_02_KIND_HEALER.md`.

**Holds:** Original current-stage care/twelve-tally/treatments after Hope resolution versus A historical-chain-origin/current Hand of Hope. Header unconditional twelve→Dawn versus Hope/Sorrow branching lacks precise state presentation; primary chain blessing progression versus wider EntityCodex Patient Martyr/C-IIIγ-071b/C-Vω-071c example differs from current071b/c rows. Do not invent reset, second healer or transition. Origin employed forty-one-year Office care worker and not failure versus Tale explicitly notcityemployed and defined by failing to save. Both written source records preserved; historical person→crystal figure is compatible, but no sourced explanation joins those life accounts. No aggression/never-struck/rejection gives confusion versus Bitter Medicine rejection strike and generalized injury; formal ValidWorkTypes includes prohibited Pugnahan. Activation4/Core45/ultimate65 scopes unjoined. Primary Comprehension4/Minor versus Tale3/EntityMajor explicitly corrected in primary, not reimported. Document date4232+1778 remains literal rather than fabricated chronology. Equipment Short statistics versus Long glaive archetype, MasterShroud LivingCarapace versus Han silk; Stigma palm-sized crystal versus coin-sized blueglass, precise Tail versus generic Accessory, never-fading pain versus untilrecipientcheck, one-day detection primary-only. Primary general unweptgrief/permanent numbness versus specific finite source costs; unknown+1stat preserved. Later posttransformation equipment distinct, no credit duplication.

**Commentary:** The missing report about the caregiver is more compelling than a simple saint who suffers for everyone. The rule against self-report has a real protective history, which makes its blind spot harder to dismiss and more painful to read.

**Progress:** Batch157OPEN2/5; No change0/2. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no158/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch157 / unit3 — Torn Flower `C-Iα-247`:** [[SE-C-Iα-247_Torn_Flower_찢어진_꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-247_Torn_Flower_%EC%B0%A2%EC%96%B4%EC%A7%84_%EA%BD%83.md "SE-C-Iα-247_Torn_Flower_찢어진_꽃.md")]

Movement summary and detail distinguish ordinary rooted reach from documented walking breach, without presenting it as pursuit. Identification no longer rejects a stepping bloom as another entity, because the file records that step as escalation. Corrected the interaction double negative. Sword Ability now distinguishes flat healing/edge pressure and the exact linked no-restoration limits.

**Evidence/history:** Complete416line original; exact247A–D complete; Master374–376 and4558–4589; Entity478; complete Tale1126336–6389; CSV534–537; archetype164; disposition412/457; complete durable Batch96 opening/unit2/history read. Batch96unit2 2dcfd583 previously reviewed full set and exact SE-247-B/MAW-W-247-01. Exact Side247UnopenedBloom belongs C-Iα-247; UNK247UndeliveredThanks is separate. Both increments0. Five actual checks PASS, full final read complete. LC_ALL=C words7066→7139; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B157_03_TORN_FLOWER.md`.

**Holds:** Primary and disposition no-pursuit versus SideA explicit uproot/pursue at45%/0.95m/s. Conditional stepping supported but Side targets and broad primary never-moves/unchangingweeping language still need scoped whole-source account. Primary noinjuries without grasp versus observing/lingering Grudge and target-wide ultimate; damage stats alone notproof of injury history. Completedunwitnessed flower/tearingincidental versus sourceA/Entity/Tale destroyedremembrance/secondloss, including pre-bloom witness testimonies. Keepers interpretation does not independently establish earlier/later form. Open crack containment versus later containmentseal review; SubjectLament with Grudge is a manifestation/element distinction, not automatic contradiction. Pugnahan listed Valid but explicitlybarred; primary workquietlywitness versus A namememorial secondloss. Threshold4/Core45/ultimate65 scopes not crosswalked. Tide/countandannualtearpositions no inventednewheight. MasterTale IVγ/Comprehension2 vs currentIα/1 explicitly corrected primary; no Masterrewrite. NamesTornFlower/UnopenedBloom and Short/Mediumarchetype, Void1.8Fatal/Weak remainheld. Generalizedallpiece touchharms lovedones versus distinctcosts/reflexessuit/tempercharm; genericboon/finished-hand detection versus originaltear chronology; lackingfullresonance/corrosion/release in primary. Narrow flat/edge limit repair supported by exactB, no full-set approval.

**Commentary:** The bloom being complete but unseen is a strong distinction from ordinary damage. The Standing Day boards deepen it: a scheme can list the workers correctly and still miss the people it was made for.

**Progress:** Batch157OPEN3/5; No change0/3. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no158/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch157 / unit4 — Mirror of Rising `C-Iα-392`:** [[SE-C-Iα-392_Mirror_of_Rising_솟아오른_거울](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-392_Mirror_of_Rising_%EC%86%9F%EC%95%84%EC%98%A4%EB%A5%B8_%EA%B1%B0%EC%9A%B8.md "SE-C-Iα-392_Mirror_of_Rising_솟아오른_거울.md")]

Repaired the broken Entity Type sentence while retaining modelled-only zone corruption and observed heaviness. Appearance protocol no longer dismisses the reflection interval, frame inspection and strike-list records required elsewhere. Field return logs removal and lingering fatigue instead of prescribing extra Mantle wear until a post-removal cost ends.

**Evidence/history:** Complete438line original; exact392A–D complete; Master386–388 and4690–4721; Entity482; complete Tale1166558–6611; CSV651–654; archetype207; disposition149; durable Batch98opening/unit1/history WIP4814–4822 read. Batch98unit1 787ffd31 and date-followup011132fc already full-set and exact SE-392-B/MAW-W-392-01. Later review date notnewpair. Both source-review increments0. Five actual checks PASS, full final read complete. LC_ALL=C words8499→8501; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B157_04_MIRROR_OF_RISING.md`.

**Holds:** PhysicalForm bodypullsout/mirrorstaysempty versus noexterior/neverleftsurface and stableface. Pane loweredge rising versus figureverticalrise needs spatial relationship. Source A fabricatedface pulls representative into reflection versus primary nooneapproached and alwayssameface; conditional state is not established just by labels. Primary current signedlegiblename erasure and explicitlostrecordscorrection versus SideA and Tale116 missingrecords/livingmemory/uncertaincause; do not eraseoldsource. Sourcegenre differences notproof of temporalchange. Work nevermovesseries/gazetteeronly lowers versus BehaviorViderehan and FinalObservation followingevening glasslowering twoofthree; gaugeandheight conflated in those clauses despite explicitseparatecolumns. Activation4/45/65model scopes retained. Modelledstructuralzonecorruption andultimate notobservations; eventtype unclassifiedquery preserved. Singlepass versus reflectioninterval everywatch with tworeaders needs protocolaccount; no newrepeatedfaceview tofix. Paper-onlyrelatedentities and refusal tobringMask retained, noproximitytrial. Threeequiptitlenames, βoverview versus αCharm/βMaster, ShortHammer versus Roomarchetype. LocalHammer silentvaultshelving passage vs B onepassageonlycurrenterasure/noconcealment; blackreflectionfirst head versus unspecifiedlocalmatteedge. C emptycommunalsilhouette/livingoutline/ownbiography protection vs generalheavycloak, and D backwardneverforwardtranscribedfragment vs localcopyingwholewardnames need crosswalk. Dayrage/sixhourfatigue/halfspeed activewear scopes notfullymapped; narrowreturnwordingrepair doesnotcertifyset.

**Commentary:** The dispatch argument gives this mirror real weight: restoring a name is not made harmless by being morally important. Keeping the strike list beside the death record is more honest than choosing an easy villain.

**Progress:** Batch157OPEN4/5; No change0/4. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no158/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch157 / unit5 — Absent Landmark `C-Iα-863`:** [[SE-C-Iα-863_Absent_Landmark_가라앉은_탑](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-863_Absent_Landmark_%EA%B0%80%EB%9D%BC%EC%95%89%EC%9D%80_%ED%83%91.md "SE-C-Iα-863_Absent_Landmark_가라앉은_탑.md")]

Movement now describes the documented old-street route and no target, not pursuit. Replaced generic material/signature prompts with existing cold, ash, climbing light and stable-window observations. Removed the duplicated trailing half of Story Entry1. Corrected the four-record interaction introduction and distinguished its three detailed rows from the additional Clocktower account.

**Evidence/history:** Complete 399-line original; exact863A–D complete; Master401–403 and4855–4886; Entity487; complete Tale1216833–6886; CSV931–934; archetype340; disposition379; durable Batch124unit5 e9f7399 evidence/history/checkpoint3961–3974 read. Batch124unit5 e9f7399 already fullset and exact SE-863-B/MAW-W-863-01. BfilenameEmptyLens is current Culverin-heading record with same exactsource; disputedname notnewpair. Both increments0. Five actual checks PASS, full final read complete. LC_ALL=C words7226→7215; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B157_05_ABSENT_LANDMARK.md`.

**Holds:** Historical disappearedlandmark/currenttowerhumanoid relationship broadlysupported; how visiblemassivewalkingtower occupiesoldstreet versus operationalabsentreliance needs spatial/mechanicalaccount. No presentinterior/onlylight versus occupantsrevealed byWork, Trivia viewerswhoknewtower and traversableTower/descent attacks require supported perception/accessconditions. No inventedrooms,steps,waterbody or externalnetwork. Printonly/solemechanism and hours/yearseries versus emotionalWorkheightchanges, spokennamehaltsdescent and Warden3→11height afterspoken directions. Heightlowering claimedseparateGauge but Registrum lowerreading byFlerehan/Ferrehan; Pugnahanonlycostmetres versus climbingonlycostmetres. Gauge4/Core45/ultimate65 scopes unjoined; breach print-erasure versus paperroute/signsrecoverorientation needs timingaccount. Neutralno-target/disorientation-only versus anklegrasp/foundationsbodydamage/fullstreeterasure combat; walkingthroughfourcorridors no wallmaterialaccount. Comparisons notautomaticalliances; three detailed records and additionalClocktower co-rise mustnot imply everypair tested. Narrow count/wordingrepair preservesallactualobservations. WeaponSunkenCulverin vs EmptyLens split withinsameB/Master; Short profile vs Instantarchetype. SourceBconcretebronze cannonagreesformbut namehistoryunmapped. Veilhabitualroutecost vs sourcefaintselfabsence; allpiecestake sameroutes vs Windowoccupancymemory distinctcharge. C/D chieflyoperationalappearances cannotcertifygossamercloth/glasspalm/OcularMaster category. Head5% versus Accessorygeneric; unknown+1stat; TaleIIβ/2 vs currentIα/1 and sourceprimaryWorkdifference retained.

**Commentary:** The tower works because nobody had to die for its absence to matter. The map notation is a modest, believable response: acknowledge what people still turn toward without pretending the building is there.

**Progress:** Batch157OPEN5/5; No change0/5. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no158/merge/visual claims. WIP and CHANGELOG updated together in this unit.

## Batch157 — CLOSED 5/5

**Batch157 closure (2026-10-21): CLOSED 5/5, No change 0/5, all five whole designs HELD.** Twenty supported replacements across Rising Well, Kind Healer, Torn Flower, Mirror of Rising and Absent Landmark; LC_ALL=C words 37,970→38,060 (+90). Fresh closure checks 25/25 and ledger tests 10/10 PASS; every digit, all 301 classification Physical Form rows, all fingerprinted sources and all 296 unselected primary files preserved. Each unit was separately gated and push-verified with both logs; both logs updated again here. Full per-unit changes, Commentary, unresolved whole-design relationships and machine evidence are in the closure records. Types248/301(82.39%;53 remain); Weapon248/287(86.41%;39 remain;14 excluded); SE12/301(3.99%;289 remain). No duplicate/retroactive credits; equipment coverage is not design/artwork completion. States8changed/4retained/52held/2blocked/235pending. Pending≠No change; no ladder expansion. No158 authorization, no merge, no rendered/live-site inspection. PR14 remains OPEN/draft/NON-WIKI; owner controls merge. Batch301 remains blocked on eight owner bodies/one4+4/generatevalidatebeforecopy.

[Closure report](SE_APPEARANCE_REVIEWS/B157_CLOSE.md) · [Machine evidence](SE_APPEARANCE_REVIEWS/B157_CLOSE.json)

## Batch158 — OPEN 0/5

**Batch158 opening (2026-10-21): OPEN 0/5.** Owner p authorizes this batch only. Fresh screen: 235 pending, 82 source-cue candidates. Frozen queue: C-Vδ-265, N-IIIβ-160, N-IIIγ-407, N-IIIγ-409, N-IIIγ-628. Whole original/source/history and final reads, five actual validators, individual gate/push, Commentary and both WIP/CHANGELOG required per completed unit. Three cumulative No change dossiers trigger 5→7→10; pending is not No change. Current independent counters unchanged: Types248/301(82.39%;53 remain), Weapon248/287(86.41%;39 remain;14 excluded), SE12/301(3.99%;289 remain). Existing held-source coverage is not finished artwork or design. States8changed/4retained/52held/2blocked/235pending. No159/merge/artwork/deployment authorization. Batch301 remains blocked on owner eight bodies/one4+4/generatevalidatebeforecopy.

**Batch158 / unit1 — Forgotten God `C-Vδ-265`:** [[SE-C-Vδ-265_Forgotten_God_잊혀진_신](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-V%CE%B4-265_Forgotten_God_%EC%9E%8A%ED%98%80%EC%A7%84_%EC%8B%A0.md "SE-C-Vδ-265_Forgotten_God_잊혀진_신.md")]

Movement and breach announcement now label waking travel and targeting as unwitnessed contingency. Material/signature instructions retain the posture/light/lamp records required by Appearance instead of ordering only an interval. Stat interpretation distinguishes simulation ratings from custodial measurements rather than denying other numbers exist. Final Observation no longer erases the four ordinary-speech incidents by claiming nobody has spoken.

**Evidence/history:** Complete primary in order, exact Side A Sornos (1/1) complete including prohibition; no B/C/D exist by explicit architecture. Master index431–433 and complete detail5187–5218; Entity498; complete Tale1317394–7448; CSV558; archetype446; disposition270. WIP comparator exception table4925–4960 and earlier series/history note6695–6738 read; primary git history lists only shallow10cd20a. Sornos uses the same full C-Vδ-265 identity despite different name. Fourteen dossiers including this Side-only record are excluded from 287 paired Weapons: no extant SE-265-B/MAW-W-265-01; do not create one or infer extracted equipment. The older full-types individual-credit history could not be established from available shallow history and durable logs, so no new full-types coverage is claimed pending unique-credit reconciliation. Zero new claims is not a claim that a complete equipment pair already shipped. Five actual checks PASS, full final read complete. LC_ALL=C words8086→8124; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B158_01_FORGOTTEN_GOD.md`.

**Holds:** Classification flesh/crystal/fire/ash/stone versus layered crystal rather than flesh; massive figure too large for chamber and root connection require spatial account without inventing size or expanding vault. Fingers/eyelids change and catastrophic coordinated movement need observation scope. Only this holding all-four claim is not independently established by collection analogy. Never awake/never approached/no contact versus Chronicle surveyors finding awake aware, crews entering sanctuary and current laments; nineteen-year sealed era could follow earlier history, but chronology and present authorization are not established. Four ordinary speech irregularities coexist with no address rule; a repair to wording does not prove source current-era no-worship doctrine matches live rostered worship/new liturgy. No Work in nineteen years versus recommendation and inherited Work table/Final Observation using decreases. Fixed41 seconds on every log versus four irregularities, crew elapsed-time withdrawal versus interval-triggered evacuation, threshold1/90 scopes, attack rows and unknown targets remain held. City-directed dreams differ from vault physical travel and cannot certify breach capabilities. Exact Side A prohibits extraction and treats profiles as projected; primary says three gallery-issued pieces and rarely bestowed Answered Prayer, while local Crown is Tail4%+3 hesitation/respect and Chronicle Answered Prayer bears grief. No documented reissue source links sceptre to extracted or borrowed item; do not invent B/C/D or permission. Requiem vs Choral-Sceptre, polearmLong vs localMedium/acoustic twelve paces; palecloth vs MasterCarapace and circlet vs Tail; costs/stock two vs three posts need account. All unchanged.

**Commentary:** The cistern entry is the strongest complication: secrecy protects the sleeper while making honest certification personally dangerous. The officer who refuses is allowed to be right, which keeps the institution from becoming an easy villain.

**Progress:** Batch158OPEN1/5; No change0/1. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no159/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch158 / unit2 — The Debt Chain `N-IIIβ-160`:** [[SE-N-IIIβ-160_The_Debt_Chain_빚의_사슬](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B2-160_The_Debt_Chain_%EB%B9%9A%EC%9D%98_%EC%82%AC%EC%8A%AC.md "SE-N-IIIβ-160_The_Debt_Chain_빚의_사슬.md")]

Movement describes the fixed growing chain rather than a generic device. Identification separates actual iron/name markers from added chalk survey tags. Own-name combat response now preserves on-request reassignment instead of ordering the shift ended. After-use logs Mantle removal and persisting fatigue, consistent with the refusal to prolong wear. Quarterly escalation logging no longer denies the separately documented activation trigger.

**Evidence/history:** Complete primary; exact160A–D complete including all custody/history/care and resonance; Master449–451 and5385–5418; Entity504; complete Tale1377728–7789; CSV422–425; archetype122; disposition174; complete durable Batch129unit5/history/holds/progress at WIP3633–3643. 95fa363a, Batch129unit5, already records full-set review and exact SE-160-B/MAW-W-160-01. Broken Promise N-IIIγ-160 is explicitly a different full designation; no borrowing its source. Both increments zero. Five actual checks PASS, full final read complete. LC_ALL=C words9416→9439; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B158_02_DEBT_CHAIN.md`.

**Holds:** Fixed ground/source never lifts or binds versus classification/Side dragging behind bearer; indumentum/equippable mode versus supported touch-only contact. No added carrying body. One link one name versus surety cut below; legibility absolutes versus412unreadable; inventory never names versus30-second surety transcription require privacy/method account. Work never moves reading, run only changed by signed rule versus4224strike and two load-release deformations lengthen run; sixteen-year series and4219/4222/4233 discovery chronology, retrospectivematching eighteen of twenty-one and absolute correlation not fully joined. Gauge60/65/modelled notobserved and touch-only trigger distinct; no new thresholdmode. Linkage-origin/current deliberatecorrection versus inherited amount/unpayable/ledgeroverflow Tale/Side/Testimony and chronology still held. Quarter register before survey versus after count, mandatory own-name standdown elsewhere versus on-request protection remain unresolved beyond narrow attack wording; final full forty links versus Stigma prohibition on samebearer/fullsurvey. Never lifting original versus Sidefullresonance one link lifts; source wristbinding versus no physicalbinding needs separation equipment/source. Maul vesselwork vs exactB coercive-pressure-only active line and wrist rejection; Short vs Room; Mantle grey/bodyfit/settleddebt draw-in vs black/openpattern/custodian-only tightening/normal next hit and SetItDown. Stigma literalchain vs open singlelink reflection; any-roomvision and nine refusal gifts versus consenting mapping/familyreview gift/oversight exception. Named+1 check unspecified, Head vs MasterRings/CSVAccessory. Primary days-per-link cost versus custody-closure duration, fullset SeeLinks source lifts and piececosts not joined.

**Commentary:** The refusal figures make this more than a chain-shaped debt metaphor. Stopping inherited guarantees helps real people and also shuts others out of borrowing; the file is strongest when it refuses to net those losses away.

**Progress:** Batch158OPEN2/5; No change0/2. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no159/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch158 / unit3 — Fading Whisper `N-IIIγ-407`:** [[SE-N-IIIγ-407_Fading_Whisper_번져가는_속삭임](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-407_Fading_Whisper_%EB%B2%88%EC%A0%B8%EA%B0%80%EB%8A%94_%EC%86%8D%EC%82%AD%EC%9E%84.md "SE-N-IIIγ-407_Fading_Whisper_번져가는_속삭임.md")]

Material/signature now preserves the documented denial-driven volume rise instead of claiming the voice never rises. Story Entry1 ties dimming to watches, not nonexistent completed sentences. Entry2 separates the fixed figure from spreading speech. Key Ability follows exact D: one bounded fragment, no reconstructed place, with present-memory cost recorded equally.

**Evidence/history:** Complete primary; exact407A–D complete, including concrete Lens/Veil/Key forms, source gap/resonance/failures/care; Master470–472 and5616–5647; Entity511; full Tale1448100–8153; CSV655–658; archetype208; disposition279; primary full-set historical receipt read in place, durable WIP Batch98opening/unit2/table4868–4880 and CHANGELOG4169/4174. Batch98unit2 21315218 plus registry-note f46c6043 and date56623941 already counted full review and exact SE-407-B/MAW-W-407-01. Lingering Place is same source designation, not a new pair. Zero new credits. Five actual checks PASS, full final read complete. LC_ALL=C words8125→8165; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B158_03_FADING_WHISPER.md`.

**Holds:** Fire cold/no thermalreading vs mixedburningbody is symbolic and not automatically inconsistent, but crystallized wordprojectiles and memory-erasure/full silence versus neutral acts-on-nobody/disposition need mechanical or evidentiary scope. Source fixed place versus lostplace no longer in anyone memory, recall-dependence/heatless form and erodingphysicalsite need joined existence account. No invented human/anatomy or recovery. Work acceleratesfade and no recoveredvolume versus Flerehanclarification/steadyvoice and denial/repetition strength; twelve-turnwatch vs20turnsimulation and four-hourpersonnel episode, threshold2/75/65 and singleeventmodel scope are not resolved. Rememberingweakens but phrase flame-needs-witness symbolic causalaccount held. Primary explicitly corrects oldZoneD store/lowthreat/Viderehan restriction; do not reintroduce oldinstructions. Only transcripts/no extraction and equipment conferredtwice versus Sideecho formation/Zyrak three deletionpaths; allcharges samekind/order vs separately described memoryloss/absence/certaintytrade. Written fixedfigurespread separation does not settle all perception/fieldextent, nor recorderlimit and legacy nophysicalinstrumentreading absolutes. Local Matchlock/cherrywood/leadball vs exactB burningempty Lens; Bheatedcenter cannotbe importedtoheatlesssource. Names primary/Side/Master differ; Medium3 vs Instant, local nopattern vs Skewerthreefalloff. Veilcloth vague vs identityline/blank and MasterCarapace, keychainhotvs exactDteethlessweightless Head and MasterBrooches, Head4%vsCSVAccessory5%. Bcutsactiveerasure vs genericstrike and fullsetfalseplaceerasesroom, localallabsencelegibility vs Keyboundedrecovery notwhole-restoration. Narrow Keyrepair addsno recovered content or newpermission.

**Commentary:** The anonymity rule is doing two incompatible jobs: protecting the child and preventing the possible adult from reaching her own record. The officer asking that correctness be filed as the problem is the most persuasive voice here.

**Progress:** Batch158OPEN3/5; No change0/3. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no159/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch158 / unit4 — Floating Pillar `N-IIIγ-409`:** [[SE-N-IIIγ-409_Floating_Pillar_떠다니는_기둥](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-409_Floating_Pillar_%EB%96%A0%EB%8B%A4%EB%8B%88%EB%8A%94_%EA%B8%B0%EB%91%A5.md "SE-N-IIIγ-409_Floating_Pillar_떠다니는_기둥.md")]

Story2 now records the fixed Market gap rather than travelling through reflections. Appearance protocol no longer calls two shared-floor sightings an external reference; disagreements remain recorded. Removed stray quotation marks around the transformation notice. Stigma Ability incorporates exact D care: diagnosis does not replace consent or verification of real help.

**Evidence/history:** Complete primary; exact409A–D complete including all forms, source echo, current support, failures and care; Master473–475 and5649–5680; Entity512; complete Tale1458153–8206; CSV659–662; archetype209; disposition280; in-file full-set receipt and durable Batch109opening/history/identity/evidence/table4491–4518 read. Batch109unit3 source-led fullset and exact SE-409-B/MAW-W-409-01 already counted; primary in-file receipt confirms first source-led pair. Earlier e9ac783 and Batch71 only prose/couples not extra coverage. The nine-year survey record is not equipment-credit proof. Both increments zero. Five actual checks PASS, full final read complete. LC_ALL=C words7726→7757; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B158_04_FLOATING_PILLAR.md`.

**Holds:** Fixedposition/elevation/no rise or settle versus cycle settleslower, Pugnahanraises and failureactualrise; driftingTale/Story has no chronology. Nullsurface/no body/vessel versus enormous fullmass fallingattack, striking/undermining impact, allpillarslifting and structural floorloss lack supportedgeometry/conditionalform. Numeric simulations do not establish materialbody or walking. Voice above/below at once as reliablemarker versus successful Worksingle direction; stable dimensions sinceopening versus wideningtransform need stateconditional bounds. Drawings using missing support vs bay foundadequate anotherloadpath need distinguish institution/metaphor/engineering claims, no invisibleloadbearing power invented. Localdatum legalcertification is not externalfix; nineteenclaims failforbaseline notproven subsidence, successorengineerproblem retained. AllfourWork explicitly corrects oldViderehan-only/lowthreat; TaleIα vs currentIIIγ retained. Threshold2/75/65, twelvewatchvs20turnrow,90mincap and expansionthroughseal unresolved; origin supports realneed notdisparagementof trust. Utterance namesmissingthings sometimesfalse versus equipmentaccuracycomplete/no hidden-support distinction not resolved by Stigma care. No vessel/material/extraction source versus Sideecho and Zyrak recordedcuts, primarypiececutfromabsence; notcertifiedextraction. ObsidianShuttleAwl/sutures vs exactBtriangularHan-glassAframe/plumbline; no transformation. Medium3 vs Shortarchetype, Skewer/falloff unstated. Cowlundyed vs paleveil withverticalseam/livingline; Stigmamissingsection vs headshadowlesspillar/MasterOcularcategory, Head4%vsCSVAccessory5%. Source failure rejectsindependencemandate versus primary no-supportnamed protocols; distinctcosts and failuremodes not wholly integrated.

**Commentary:** The local datum is the best image here: the institution cannot prove the ground is stable, so it makes stability the definition. Keeping the traders’ failed claims beside that decision gives the imaginary support a concrete public cost.

**Progress:** Batch158OPEN4/5; No change0/4. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no159/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch158 / unit5 — Flowing Seed `N-IIIγ-628`:** [[SE-N-IIIγ-628_Flowing_Seed_흐르는_씨앗](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-628_Flowing_Seed_%ED%9D%90%EB%A5%B4%EB%8A%94_%EC%94%A8%EC%95%97.md "SE-N-IIIγ-628_Flowing_Seed_흐르는_씨앗.md")]

Ten supported repairs: Movement names actual tendril locomotion, recognition separates entity advance from pin replacement, dammed typo corrected, generic activation price replaced by actual item costs, two no-document absolutes distinguish the earlier personnel-record gap from current limited Plain Statements, and Use Notes/baseline/during/limit rows track the selected piece rather than imposing weapon ageing or Mantle fatigue on every item.

**Evidence/history:** Whole original primary457lines; complete exact628A–D read including source shape, Object/Place protocol, extraction, named route/nonliving bed, fullset and all item Appearance/history/care; Master488–490/5814–5844, Entity517, complete Tale1508426–8477, CSV779–782, archetype260, disposition195; historical in-file fullset and WIP Batch1004852–4869, CHANGELOG4174 read. Batch100unit2 42f35818 already source-led fullset and exactSE-628-B/MAW-W-628-01; sourcegradeγ vs equipmentα deliberately distinct. No earlier cleanup or new current read duplicates counted coverage. Zero new increments both. Five actual checks PASS, full final read complete. LC_ALL=C words7362→7399; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B158_05_FLOWING_SEED.md`.

**Holds:** PhysicalForm/burstseed sprout and Wardenrootmass versus Tale/Storynever sprouted/no growth; mobileemptyplace vs creature/rootvehicle/newseedsprojectiles/blackflowers/fullBloom vs no sprouting and plants inpeople need boundedconditionalbody/activation, not mere manifestation label swap. Primary crawls/slithersinsearchofprey versus breachnotpursuit; fieldextent along roots/underfloor vs exactcreature dimensions/attacks unset. Gauge75 vs65ultimate/40breach, no counter vs condition and fullbloomdamming,20turns vscontinuous perwatch and timeoffloorclosure, firstpersonexposurerule vsplantednotfelt are not unified. Neverstopped/mattersaidflat vs Sidefullset stop/releaseHan and specific 1.1SorrowSeed reduction need state/evidence distinction. Tideincreases/neverfalls vs testedTide lost competingcause; quarterlymeans vs precedingyears wording retained unresolved. Ground ahead supposedly normal/lighter vs fixeddistancecurve aroundentity vs heavytrack not stableclearance model; initial Tension says behindlighter than ahead contrary to rest, requires supported surveygeometry notinvented. Keep counts/readings unaffected. Origin single soldiersrage mixeddormantgrief and fourgenerations vs expandingnewunwrittenservice deaths not fully joined. PlainStatements change acknowledgmentinstitution but no source confirms they reverse advance or curegrief; protected refusals, assaults, sixdraftersunansweredcost retained. SourceA calls Subject but ObjectPlaceWorkprotocol invalid N/A versus primary bothvalid but barred with plantedWardens/dammedcorridor. PrimaryFinalFlerehan revealsmemories thenwithdraws vs actualplantedtwice; SideViderehanmemoryeffect vs localobservational procedure. No source authorizes categoricalresolution of Work/withdrawal. Equipment extraction currentpiececost repair does notsettle SourceA condition/namedbed nor rootstopping. Seaxbogoakbrokenback/copperdiagrams/sporekineticcut vs BblacksteelMaulrootchannels/nonlivingbasin and sourceexplicitcannot safelystrike livingcarrier; noformtransition. Numbers3–6/2/2/max5/15 agree but archetypeRoom vsShort, Single/item100%notimported. Cbreatheswith vs localhalfbeatlate, mantlepressuredelivery vs localgroundcarrywards; Dcoolingsourcepressure vs unresolvedservicerecorddetection/informalunauthorizedpractice no inference all suchrecords createpressure. Closedmatteblackvialsilt vs localgenericheavyvial not resolved; Head5%vsAccessorycategory and nineteenvialsoftwooutsideposting vs Dsuccessfulwork acquisition held. No detachwhencharged/route/discharge maintenance not equivalent to generic armouryreturn; narrowcost repair is not fullsafeoperatingprotocol.

**Commentary:** The Plain Statement is stronger than a simple bad-rule story: it restores facts without buying off an inquiry, yet the families least informed are the ones refused, and the drafters inherit consequences they cannot edit away. The seed’s weight should keep those distinct costs visible, not erase the partial improvement.

**Progress:** Batch158OPEN5/5; No change0/5. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no159/merge/visual claims. WIP and CHANGELOG updated together in this unit.

## Batch158 — CLOSED 5/5

**Batch158 closure (2026-10-21): CLOSED 5/5, No change 0/5, all five whole designs HELD.** Twenty-eight supported replacements across Forgotten God, Debt Chain, Fading Whisper, Floating Pillar and Flowing Seed; LC_ALL=C words 40,715→40,884 (+169). Fresh closure checks 25/25 and ledger tests 10/10 PASS; every digit, all 301 classification Physical Form rows, all fingerprinted sources and all 296 unselected primary files preserved. Each unit was separately gated and push-verified with both logs; both logs updated again here. Full per-unit changes, Commentary, unresolved whole-design relationships and machine evidence are in the closure records. Types248/301(82.39%;53 remain); Weapon248/287(86.41%;39 remain;14 excluded); SE12/301(3.99%;289 remain). No duplicate/retroactive credits; equipment coverage is not design/artwork completion. States8changed/4retained/57held/2blocked/230pending. Pending≠No change; no ladder expansion. No159 authorization, no merge, no rendered/live-site inspection. PR14 remains OPEN/draft/NON-WIKI; owner controls merge. Batch301 remains blocked on eight owner bodies/one4+4/generatevalidatebeforecopy.

[Closure report](SE_APPEARANCE_REVIEWS/B158_CLOSE.md) · [Machine evidence](SE_APPEARANCE_REVIEWS/B158_CLOSE.json)

## Batch159 — OPEN 0/5

**Batch159 opening (2026-10-21): OPEN 0/5.** Owner p authorizes this batch only. Fresh screen: 230 pending, 77 source-cue candidates. Frozen queue: N-IIβ-778, N-IVδ-005, N-IVδ-489, N-IVδ-517, N-IVδ-901. Whole original/source/history and final reads, five actual validators, individual gate/push, Commentary and both WIP/CHANGELOG required per completed unit. Three cumulative No change dossiers trigger 5→7→10; pending is not No change. Current independent counters unchanged: Types248/301(82.39%;53 remain), Weapon248/287(86.41%;39 remain;14 excluded), SE12/301(3.99%;289 remain). Existing held-source coverage is not finished artwork or design. States8changed/4retained/57held/2blocked/230pending. No160/merge/artwork/deployment authorization. Batch301 remains blocked on owner eight bodies/one4+4/generatevalidatebeforecopy.

**Batch159 / unit1 — Well of Unfinished Words `N-IIβ-778`:** [[SE-N-IIβ-778_Well_of_Unfinished_Words_솟구친_우물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-778_Well_of_Unfinished_Words_%EC%86%9F%EA%B5%AC%EC%B9%9C_%EC%9A%B0%EB%AC%BC.md "SE-N-IIβ-778_Well_of_Unfinished_Words_솟구친_우물.md")]

Appearance signature now records the stated salt-cold/rain sensation instead of inferring camera invisibility from no reflection. Log and Method distinguishes interrupted speech from a completed ending. Watch Record no longer calls silent readings the sole sufficient procedure. Registrum names the actual moderate overflow threat and fixed position.

**Evidence/history:** Complete original primary; exact778A–D full with binding, form, no-healing limit, each cost and corrosion; Master545–547/6444–6476, Entity537, full Tale1699452–9505, CSV871–874, archetype319, disposition410, personalization537; WIP4329–4331 and CHANGELOG4055 historical exact pair read. Batch117unit2 754d165 already counted source-led fullset and exactSE-778-B/MAW-W-778-01; Well/SoakingWell same designation. Earlier e329731 Log and Method style edit is not additional source coverage. Both equipment increments zero. Five actual checks PASS, full final read complete. LC_ALL=C words7108→7136; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B159_01_WELL_OF_UNFINISHED_WORDS.md`.

**Holds:** Neglectraises/continuouslyattended vs silence changesnothing/seasonstable; levelonlymovesspeaking vs interruptions and speakingrise/output channel timing. Threshold60/65ultimate vs confessionactivation vs ignoreoverflow and SidecanbreachviaTransform require state distinction, no invented breach counter. Longcontact noinjury vs floodwounds/identitycollapse; all-party flood vs singlelistenerdisposition, channellingmuteness vs needed confessioncompletion and planneddisengage vs forcedspeechfinish unresolved. Reflectless water does not establish nonphotographability; floor/leanstructure vs metaphoriclistening remain measured separately. Yield/extraction while no drain and Placeindestructibility vs physicalcopingwater and equipmentsource without extractionhistory; schoolsourceecho not proof of currentmaterialpermission. Firstperson testimony legitimate vs autobiographicalcorrosion require sourceattribution, not ban all grief accounts. Genericinteraction table asserts MemoryWell transfer but fourattempts unresolved; onejointvisit vs fourattempts scope. Weapon brassstandard/polearmShort2 vs archetypeClose and personalizationsealedhorn/stitchbell/drip; A/Bheading/history/MasterListeningRequiem vs VigilanceSceptre no transition. SuitHan-silk vs MasterLivingChitin; VialTail5% vs CSVGiftAccessory. Setoption-of-silence theory vs separate item costs/involuntaryweeping, protection conditional and sourcecorrosion not fully integrated; bonusstat deliberatelyunknown. No reassignment of ListeningRequiem to WhisperingWalls distinctEntry316.

**Commentary:** The most important decision is to review the schedule rather than blame the listener when a shift cuts a testimony short. The routine dispersal order and the officer who may not have known it was a funeral keep the origin morally specific without inventing an easy villain.

**Progress:** Batch159OPEN1/5; No change0/1. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no160/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch159 / unit2 — The Smothering Mother `N-IVδ-005`:** [[SE-N-IVδ-005_The_Smothering_Mother_질식하는_어머니](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-005_The_Smothering_Mother_%EC%A7%88%EC%8B%9D%ED%95%98%EB%8A%94_%EC%96%B4%EB%A8%B8%EB%8B%88.md "SE-N-IVδ-005_The_Smothering_Mother_질식하는_어머니.md")]

Six replacements: condition row, Battle Resolution and Final Observation now use the already-recorded Presumption Return reading rather than impossible proof-of-peace; generic temperature-swing activation replaced by the fixed heat and actual reach observations; duplicate title word removed; inactive/fixed-entity fragment replaced by stable gauge is not inactivity.

**Evidence/history:** Whole original primary472viewerlines including all Apex/Presumption/ReadingNames; complete exact005A–D including trigger, rescue, clasp/plate and incompatible weapon identity, histories and distinct full-set descriptions; Master560–562/6610–6642, Entity542, full Tale1749725–9778, CSV14–17, archetype59, disposition447; WIP4350–4356/5436, CHANGELOG4071/4303 histories read. Batch85unit3 08cb402c already source-led weapon pair; Batch117unit3 complete set and exactSE-005-B/MAW-W-005-01 durable receipt. Prior source-led counts not added again. Fullsetnewreview is not a new body or weaponform. Five actual checks PASS, full final read complete. LC_ALL=C words8526→8557; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B159_02_SMOTHERING_MOTHER.md`.

**Holds:** Subjectorganicwarmflesh vs crystalafar boundary remains unlocated; chamberroomspan and line both armreach reference need spatialsafeextent. Genericactivationtemperature no longer falsecriterion but knownreaches/activehold/field and movementrate not unified. Current never-squeeze/noinitiatedharm and injuriesfrompullaway vs combatstrikes/crushingbreach/internalpressure, simulation vs observedstatements need deliberate scope. Threshold1failedcycle vs90gauge/65ultimate/start60–80, failedwatchinevitablebreach vs fourbreaches and retreatallowed unresolved. SourceA minimumthreeinside65final vs primaryallpersonnel, Selectionsmall/wounded etc vs primaryonlysmallest; noforcewithdrawal vs rescueinstruction stays different. Opposed lastresorttwo Pugnahan vs one suppression4228 authorization chronology held. Revisedpresumptionreading applies acknowledgedlimited management, not eachsessionfreehonour/falsepeace; SideA memoryproof stillcanonicalsourceconflict, no rewriteofSide. Eightteenrequests vs4219institution/current4238/datedprimary4232 need chronology. Reachinterval saidnooperationalapplication vs watchactivationunderfigure, accurate elevenrefusals vs alltypesquotesinglechildTale174ZoneD. SilentChildstoppedshort vs heldreleasedafterfour minutes remain contradicted. Backlogcorrelation not inventedcause or cure. Cleaversteel/sinew vs BboneclawPRIMAL/Talon and MasterEmbraceTalon no documentedtransition; revised combatnumbersagree. SourceCcrimson/lockedbuckle/allmarkedallies vs localdark/breathing and restrelease, Cclusterimmobilize vs AinterceptGrudgestrike/Bescape-path/DdoubleHoldFast needsfullsetcrosswalk. Dcrimson/sizesdifferent/selfdrifting vs localdark/claspcoolingnearsorrow; Tail4% vsCSV5%/Masterhandring; +3stat unspecified not invented. HandlerSoojin in itemhistory vs sourceSoojin needsidentity notassumed. NothingmakesdirectMothercontactsafe.

**Commentary:** The Presumption Return grants acknowledgment without pretending to certify a death, but charges an annual public retelling for it. Reading both names matters precisely because it lowers the gauge without slowing the empty-room clock; the improvement is real and incomplete.

**Progress:** Batch159OPEN2/5; No change0/2. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no160/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch159 / unit3 — Forgotten Silence `N-IVδ-489`:** [[SE-N-IVδ-489_Forgotten_Silence_잊혀진_침묵](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-489_Forgotten_Silence_%EC%9E%8A%ED%98%80%EC%A7%84_%EC%B9%A8%EB%AC%B5.md "SE-N-IVδ-489_Forgotten_Silence_잊혀진_침묵.md")]

Six repairs: Movement identifies a stationary luminous figure rather than body/drop template; breach announcement and activation distinguish spreading quiet from hunting or locomotion; Lens bonus names source-supported Clarity; Stat interpretation limits it to pressure, not private words; Final failure now matches coercion rather than an unrelated emptycycle.

**Evidence/history:** Whole original primary including entire Apex/depletion/volunteer-ceiling/correct staffingobjection; complete exact489A–D with materials, coercioncut, consent, pressure-not-content and care; Master575–577/6776–6808; Entity547; Tale1799997–10048; CSV699–702, archetype226, disposition242; WIP4133–4137 and CHANGELOG4010–4012 pair/fullset history read. Batch122unit1 f834de2 already counted fullset and exactSE-489-B/MAW-W-489-01. SideSilenceWeForgotWeMade same designation, not new equipmentcoverage. Source-led patterns added in122 not evidence of fullbodydesign completion. Five actual checks PASS, full final read complete. LC_ALL=C words8223→8234; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B159_03_FORGOTTEN_SILENCE.md`.

**Holds:** Figurestationary vs salutereturn/understandingunheldface, dreams/reflectivesurfaces and sourcepicturedoutline vs intangiblematerialvesseldestructibility/tondust/Speed2.45 and shockwave wounds need action/simulation/perceptionbounds. Genuineno physicaldanger vs shovingcrushing oldrows cannot resolved by removinggenericactivation alone. No inventing faceless anatomy from memoryfailure. Gauge1/90/65/start60–80 and failedcountercycles not reliable; forcedspeechraises vs beliefshortemptycycle and volunteerednoeffect, owntruthspokenreduces vs FewFlerehanlosewords/erasedrecall unclear. Figureholdsforgottenabsence notoldtruths but currentWorkrecoverssilencecreation needscope. Glowbrighteronexchange vs brightnessfallswhenname/Choirdims no speech apparentdirectionconflict needs qualifiedseries. Apex writtenlogsaftercomingout vs mandatoryinsidebeforeexit and no supervisoraskwhatgiven vs sealedprecheckcontainsownwithheldthing/secondworkeropens has consent/privacy tension. Fullbodywithdrawalemptycycle and forcedspeech response nowdistinct but conditions/saferecall/handsignals vs speakingworker coordination unresolved. Consentprotectvolunteers costs nonvolunteerselsewhere no nettingaway. Weaponfeltsteelclaymore vs BdeepblueHan-crystalblade andsteelwordinB ownAppearance; same numericcore/Skewerthree noformtransition. Weaponopensspeechunintended vs Bcutscoercion/privatequiet, setreciprocity vs itemawakeningauthorised separate. Local shroudscent/cool/luminous vs Cblueidentityline mostly separate; LenspendantTail vs Masterocular and Dtail-lens; Headnotinferred. Tail4%vsCSVAccessory5%, unknownprevious+3 nowClarityexactA/D; carepressureonly no righttodisclosure. Localallthreeoperatorreticence vs individualgrief/joy/questions, fieldduringonlyweeping andafterforceddisclosure withholding ascondition not fully reconciled.

**Commentary:** The nine-cycle ceiling protects a volunteer by borrowing hours from people who never volunteered. Keeping the staffing office’s objection correct and unanswered stops privacy from becoming a cost-free institutional virtue; the Lens should not undo that privacy by pretending pressure is a transcript.

**Progress:** Batch159OPEN3/5; No change0/3. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no160/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch159 / unit4 — Broken Tear `N-IVδ-517`:** [[SE-N-IVδ-517_Broken_Tear_부서진_눈물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-517_Broken_Tear_%EB%B6%80%EC%84%9C%EC%A7%84_%EB%88%88%EB%AC%BC.md "SE-N-IVδ-517_Broken_Tear_부서진_눈물.md")]

Six replacements: identification now checks code/booking before opening and verifies visible face/lament inside the layer. Consequences, Use Notes and during/limit/after-use rows distinguish Weapon weeping, Shroud joy loss and Shard sleep replay; Shard care includes waking review and original-witness release rather than treating absence of waking tears as clearance.

**Evidence/history:** Complete primary452viewerlines including low-room/surrender-order review; exact517A–D complete including glaive/shroudchannels/shardload and complete witness naturalend; Master578–580/6809–6841, Entity548, complete Tale18010053–10106; CSV711–714, archetype236, disposition243; WIP4928–4936 and CHANGELOG4236 history read. Batch99unit1 d6bcdd32 and reviewdatefollowup666b9a2b already source-led fullset/exactSE-517-B/MAW-W-517-01. A-file now full[LS] vs oldreceipt[D] retained in historicalnote, no identitymerger or duplicatecredit. Five actual checks PASS, full final read complete. LC_ALL=C words8716→8709; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B159_04_BROKEN_TEAR.md`.

**Holds:** Dreamonlyfigure vs physicalvaultTension/thresholdcontact/reflectivesurfaces, alwaysabouttorunneverdoes vs walking/pursuit/floodleaveunderownmotion; intangiblewithoutfluid/no sample vs shardswounds/physicalmaterialpermanence/tondust/vesseldestructibility need separateconditions/evidence. No new solidbody or chronology invented. No naturalend lament vs sourceAechoafterfullnaturalend and fullsetPresentUntilSoundEnds, main24turns/closesclock and donotinterrupt conditional conflict; sincerepresence vs fluentfalsesympathy failure and automaticwaking Pugnahan needauthorization/termination account. Gauge1/90/65 and fullshatter/refusedcycle/floodtiming notunified; crosscyclecumulative but withinentrydurationcost vs sourceboundedend not normalized. No acoustic source vs audibleoutside and suppressionnotouch; subjective musicologistversions vs notes singlemostreliable floodrehearsalclock evidence standards differ. Elevationbasedfixedsequence protectall vs lowroomsfirst and thirteendeclined relocation, seatrejustification vs safetyofficeobjection must remain; notcharacterizedasfoolish or resolved by repairs. Prismindigo/filamentgyroscope/bluefluid vs Bdeepbluecrystalglaive/settledteardrophaft, no transition; localtearsdissolve notsourcefluidproof. Damage10–15/3/3/max2/50, suitresistancesagree; archetypeLongvsMedium3, Skewernotbackfilled. Source clearfragments notsilencecentraltear vs genericmindstrike. Suitnontransferringwetfilm vs Cbluechannels/watershed and sourcecompressionfailure; Stigmamirrorreflectiontile vs Ddeepblueloadwarm/hot, Tail4%vsCSVAccessory5%. Originalmirrorreflectingcrack vs no sourcephysicaltrace, issuedvsafterfullwitness and exactoriginalwitnessidentity notunified; piececostcare repair no fullset safetycertification.

**Commentary:** The low rooms’ seat matters because it can demand a public justification from the clock, not simply a kinder evacuation order. Their one successful correction came from better evidence. Keeping the safety office’s objection beside that success makes the published plan a real choice with costs.

**Progress:** Batch159OPEN4/5; No change0/4. Whole-designHELD/+0SE; equipmentboth+0. Types248/301(82.39%),53/301remain; Weapon248/287(86.41%),39/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no160/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch159 / unit5 — The Mewgical Girl `N-IVδ-901`:** [[SE-N-IVδ-901_The_Mewgical_Girl_야옹_마법소녀](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-N-IV%CE%B4-901_The_Mewgical_Girl_%EC%95%BC%EC%98%B9_%EB%A7%88%EB%B2%95%EC%86%8C%EB%85%80.md "SE-N-IVδ-901_The_Mewgical_Girl_야옹_마법소녀.md")]

Seven supported repairs: alert and movement follow on-foot unspoken-wish pursuit rather than indiscriminate chamber escape; suppression priority defers to existing conditionalManagement and acknowledges Pugnahan risk. Appearance protocol timestamps lagging staff palette separately. After-use care distinguishes Staff/Costume/Bell consent and bearer-voice safeguards instead of deferring every cost; interaction summary restores Trinity’s both-voice scope; idiom repaired.

**Evidence/history:** Complete original449viewerlines; complete exactUNK_901A–D inclcanonicalfieldchecks, splitHeartBurst/twoseparateconsents, CostumePinkSmileLock/three-nameunclasp, BellThirdVoice/threevoicesamples/removal. EntityCodex646 exactdesignation. ExactMasterMAW/Talename/UNKID search finds no matching entry, so no Tale/masteritemcrosscredit. CSV1155–1158 includinggenericBell5%; disposition351 predates narrowedbreach wording; archetype354 is unrelatedDuri and notmatchingMewgical. WIPVOL_01 920–942/959, VOL_02 1287 and all current/archivalWIP/CHANGELOG identity/name/exactUNKpairsearch; primarypathgitlogonlybaseline10cd20a in availablehistory. No prior source-led fullset/exactUNK-901-B/MAW-W-UNK-901-01 disposition found. ArchivedBatch9unit2 f5c779e isprose/section/conditionrepair, notindependent fullset orWeaponcomparativecoverage. No equipmentreviewledgerrow forN-IVδ-901; C-IIβ-901/SE-901-B/Duri’s Heart isdistinct and mustnotbeimported. Thisunit earns fresh +1Types/+1Weapon with completeA–D/currentprimarycomparison, +0SE because unresolvedwhole-designrelationships. Five actual checks accepted, full final read complete. verify has two retained original deliberate dialogue ellipses; not seam[] and not splice defects. LC_ALL=C words6198→6316; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B159_05_MEWGICAL_GIRL.md`.

**Holds:** PhysicalForm says coreoftwosouls(bodyMIMI/soulMadMew) vs ShuShu/onebodyonespirit record; no alias/replacementinvented. Mimi moves/heals/sings beforeShuwakes and neitheractalone vs bondedunintroduced and dreamwishcitizensfourmillennia cause mustkeep chronologyopen. Humanwish supports artificialdoll not compulsory humananatomy. ExternalgreycatgirlspiritduringMimicontrol vs soulunableaffectphysicalalone, multiplevoicesonevessel and vesseltondust ordinarydamageexception onlyselfbomb; transformedoutfittraitmerging 3x boosts and normal2.35/sync3.10 vs forcedseparation selfsoot relationshipunresolved. Eye blue/red in soot vs standardeye onlybright/severe and wholepaletteflicker no invented defaultiris. Stafflag protocol repair doesnotcertifytimingofallcombatactions. 75%orforcedconflict vs75%orthreecontrolconflicts, breach40%+10 vs starting60–80; directedaddresseedrain vs spreadingnamesfacesnumbness and genericidentitymemoryloss notnewcanonproof; mobiletrackednotcontained vs formalEscapecategorynoterased. Suppressiontwoturns permission doesnotprovephysicalreturn, acknowledgementstablegauge notbond; Finalchosenremainone vs involuntaryinitialbond unresolved. ExactUNK_A/Bfocusname/material/size/paw/grade/element and C/Dappearance/bonuscosts align; sourceB10–15/4/5/AoE/max2/50/falloff notpresentlocally and notbackfilled. SourceD/localTail4%vsCSVAccessory5% held; no empiricalchanceinvented. PresentStaffalreadywieldedbyentity vs extractedoperatorfocus requiresownership/embodimentscope; Costumestabilizeonepersona vs Apreventsoneerasure and sourceCthreepersonshutdownnotphysicallyseparating identities; Belltwotones/care notmerge. No WeaponarchetypeforUNK901, Duri901unrelated; MasterMAW/Taleabsence notsourceequivalence; no newXLSXparityclaim.

**Commentary:** The joke works because healing and threat can come from the same smile without making either voice disposable. The separate bearer voice matters too: equipment care must not turn the human operator into an unacknowledged third performance. Soot is a consequence for the doll, not a guarantee of safety for the person she just healed and hurt.

**Progress:** Batch159OPEN5/5; No change0/5. Whole-designHELD/+0SE; equipmentTypes+1/Weapon+1, fresh exactUNK901 pair not Duri901. Types249/301(82.72%),52/301remain; Weapon249/287(86.76%),38/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no160/merge/visual claims. WIP and CHANGELOG updated together in this unit.

## Batch159 — CLOSED 5/5

**Batch159 closure (2026-10-21): CLOSED 5/5; No change 0/5; all five whole designs HELD.** Well of Unfinished Words, Smothering Mother, Forgotten Silence, Broken Tear and The Mewgical Girl each received supported repairs, a complete final reread, individual Commentary, both-log updates and an individually gated, verified push. Exactly 29 replacements; LC_ALL=C words 38,771→38,952 (+181). Fresh closure validators 25/25 accepted, ledger tests 10/10 PASS; Mewgical verify’s two original deliberate dialogue-ellipsis flags explicitly retained, not falsely reported as seam[]. Every digit sequence, all 301 classification Physical Form rows, all fingerprinted sources and all 296 unselected primaries preserved. Fresh exact UNK-901 source review adds +1 Types/+1 Weapon, not Duri’s Heart’s unrelated 901; the other four pairs were already counted. SE completion +0. Current counters: Types249/301 (82.72%;52 remain); Weapon249/287 (86.76%;38 remain;14 excluded); SE12/301 (3.99%;289 remain). States8changed/4retained/62held/2blocked/225pending. Equipment coverage is not design/artwork completion. Pending≠No change; no ladder expansion. Both WIP and CHANGELOG updated again at closure. No Batch160 authorization, merge, deployment or rendered/live-site inspection. PR14 remains OPEN/draft/NON-WIKI; owner controls merge. Batch301 remains blocked on eight owner bodies/one4+4/generatevalidatebeforecopy.

[Closure report](SE_APPEARANCE_REVIEWS/B159_CLOSE.md) · [Machine evidence](SE_APPEARANCE_REVIEWS/B159_CLOSE.json)

## Batch160 — OPEN 0/5

**Batch160 opening (2026-10-21): OPEN 0/5.** Owner p authorizes this batch only. Fresh screen: 225 pending, 72 source-cue candidates. Frozen queue: N-IVδ-902, O-IIIβ-944, O-IIIγ-559, O-IIβ-235, O-IIβ-301. Whole original/source/history and final reads, five actual validators, individual gate/push, Commentary and both WIP/CHANGELOG required per completed unit. Three cumulative No change dossiers trigger 5→7→10; pending is not No change. Current independent counters unchanged: Types249/301(82.72%;52 remain), Weapon249/287(86.76%;38 remain;14 excluded), SE12/301(3.99%;289 remain). Existing held-source coverage is not finished artwork or design. States8changed/4retained/62held/2blocked/225pending. No161/merge/artwork/deployment authorization. Batch301 remains blocked on owner eight bodies/one4+4/generatevalidatebeforecopy.

**Batch160 / unit1 — The Repeated Survivor `N-IVδ-902`:** [[SE-N-IVδ-902_The_Repeated_Survivor_되풀이의_생존자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-N-IV%CE%B4-902_The_Repeated_Survivor_%EB%90%98%ED%92%80%EC%9D%B4%EC%9D%98_%EC%83%9D%EC%A1%B4%EC%9E%90.md "SE-N-IVδ-902_The_Repeated_Survivor_되풀이의_생존자.md")]

Six supported repairs: Appearance protocol separates visible sequence from inferred private intent; Ferrehan is primary endurance rather than guaranteed safety; containment priority no longer treats confrontation or a barrier as permanent suppression. Equipment grade interpretation now names this δ set and its distinct costs; unknown iteration counts may be recorded honestly; broken interaction sentence repaired.

**Evidence/history:** Complete original430viewerlines and complete exact UNK_902-A–D, including canonical field/stat blocks, Uncast Corridor, Actor Four, Line Before the Door, corrosion, maintenance and shutdowns. Entity Codex647; CSV1159–1162; disposition350; full-title/UNK-ID negative Master MAW/Tale/archetype search. WIP4040–4058 and CHANGELOG4020 identify prior source-led review; archived Batch56/69 mentions are prose work. Goru SE-902 is unrelated. Batch125 unit4 444d831 already counted complete source-led set and exact UNK-902-B / MAW-W-UNK-902-01 pair. No new equipment credit. Side A’s post-Cycle prose was already held against within-cycle primary; it remains unresolved, not an authorized chronology change. Five actual checks PASS, full final read complete. LC_ALL=C words6028→6069; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B160_01_REPEATED_SURVIVOR.md`.

**Holds:** Side A subject prose says the Cycle ended, while its own field table and the primary place the body within repeated Absolvohan iterations. Primary twentieth-loop onset, Tale sixth loop, +24/+30 journal, +966/+1778 progression and nine/tenth-death attacks do not establish one reconciled chronology. No timing or return mechanism invented. Ordinary attentive/vacant eyes versus personnel report and Final Observation “smiles without eyes”; anticipated movement versus appearing where personnel just were rather than travelling; stage-like perceived space versus ceiling height and black Han curtain/frozen cast require conditional boundaries. No eye removal, teleportation or extra body stage inferred. Vessel destruction/tonnage versus cannot end within a cycle/returns next iteration, combat killed-trigger immediate return and Resolution withdrawal into next iteration remain distinct unresolved scopes. Threshold80/start70–90 versus ultimate65 and breach40 have not been normalized. Scene-ended Ferrehan and original-surfaced empathy have different outcomes; no promise that enduring cures the original. Exact UNK902 equipment material/shape/statistics agree with A–D and previous source-led repairs. Final Act role-target strike versus Scene Without Cast cutting a mark retains the source’s unresolved targeting relationship; not an imported Goru’s Fist weapon. Coat makes an actor versus no role available and warning against role labels need their original consent/identity limits. Earpiece loops a line versus never same line twice and mark-removal wording not resolved into a new item. Head4% versus CSV Accessory5% remains held; Master/Tale/archetype absence not filled from SE-902. No new XLSX parity claim.

**Commentary:** The ordinary uniform matters: the horror is not a new monster suit but a colleague’s competence surviving their agency. Recovery checks must therefore let the bearer choose, not award the part of “recovered survivor.” The broken interaction clause could be repaired without pretending to solve the Cycle’s chronology.

**Progress:** Batch160OPEN1/5; No change0/1. Whole-designHELD/+0SE; equipmentboth+0. Types249/301(82.72%),52/301remain; Weapon249/287(86.76%),38/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no161/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch160 / unit2 — Calling Bloom `O-IIIβ-944`:** [[SE-O-IIIβ-944_Calling_Bloom_부르는_꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B2-944_Calling_Bloom_%EB%B6%80%EB%A5%B4%EB%8A%94_%EA%BD%83.md "SE-O-IIIβ-944_Calling_Bloom_부르는_꽃.md")]

Ten repairs: crown marker now distinguishes blue petals from the dark eye; both movement summaries describe roots trailing clear rather than serving as a gliding support. Breach notes use the managed wood rather than a cell and replace the unsafe answer-and-embrace instruction with the existing true-name/no-answer/no-touch response. Use Notes and all four field stages now track Vine/Mantle/Petal costs separately with source-attribution and relinquishment safeguards.

**Evidence/history:** Complete original444viewerlines including Warden Seojun/privacy claim; complete exact944A–D with source-trace histories, binding, failure, care and prior range hold. CSV1087–1090; archetype391; disposition336; Entity Codex359 awaiting-row note. Exactcode/name absent from Master MAW and standalone Tale; primary Tale fully read instead. WIP3211–3220 and CHANGELOG3251/4394 source-led Batch133/83 history read. Batch83 unit3 c893035d already counted exact SE-944-B / MAW-W-944-01; Batch133 unit4 d32f0c02853c57d2f419378162516d3e78bbe749 completed full-set care/source review. All equipment credits zero on this repeat. Full designation O-IIIβ-944 resolves the set; close bone mandibles archetype does not authorize replacing the vine. Five actual checks PASS, full final read complete. LC_ALL=C words7423→7485; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B160_02_CALLING_BLOOM.md`.

**Holds:** Stationary until speech versus never-rest wandering, true-name Work versus Warden silence-only approach; target draws by voice versus bloom reads listener’s longing and garden field require condition bounds. Blue/dark-eye marker and root wording repair no extra form. Eye graft/fused child history, new eye on touch failure and many central blooms do not establish their number, past victims or transformation mechanism. Seojun missing/fate unknown in Origin/Counseling versus Warden ordinary verified whereabouts and family privacy request remain conflicting evidence; do not choose a fate or invent a sealed biography. Final first focus in three centuries versus repeated Nari Work responses, wood-edge “home” versus endless lure and uncontained management remain unresolved. Unanswered call as breach trigger versus Ferrehan’s unanswered calling decreases; gentle name versus answer prohibition; compulsory victim steps versus voluntary door imagery. No-touch repair does not make name-use harmless or promise that Nari’s approach ends absorption. Threshold70/90, breach50 and base45–65 held; “does not strike” versus involuntary terrain/catch effects not flattened into generic attacks. Vine names/grade/5–9/speed2/max3/cost24 match A/B, but localRange3(Long) versus A/B4(Long), omitted AoE/falloff and Close snapping-bone-mandible archetype have no crosswalk. Source item appearances describe source-attribution mechanics rather than detailed local mushroom-vine/petal/eye anatomy. Mantle stats/cost20 and PetalHead5%/+1 agree A–D, CSV Accessory5% stays different slot scope. Unnamed +1 stat remains unnamed; no inferred Clarity. Item echo-cost unit versus purchase maximum/use cost ambiguity not normalized. Sole-stolen-voice uniqueness and full-set source ending not certified. No new XLSX parity claim.

**Commentary:** Nari is both the bait and the child caught by it. Calling her by name acknowledges her without making an embrace safe or solving her brother’s history. The Mantle’s wish not to part is especially important: an operator wanting another rotation may be paying the equipment cost rather than consenting freely.

**Progress:** Batch160OPEN2/5; No change0/2. Whole-designHELD/+0SE; equipmentboth+0. Types249/301(82.72%),52/301remain; Weapon249/287(86.76%),38/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no161/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch160 / unit3 — Broken Ruin `O-IIIγ-559`:** [[SE-O-IIIγ-559_Broken_Ruin_부서진_잔해](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-559_Broken_Ruin_%EB%B6%80%EC%84%9C%EC%A7%84_%EC%9E%94%ED%95%B4.md "SE-O-IIIγ-559_Broken_Ruin_부서진_잔해.md")]

Eight repairs: Movement and the two appearance movement summaries now distinguish waiting from recorded walks and remove unsupported pursuit; breach alert/movement follow the two conversational returns rather than guaranteeing collapse. Appearance explicitly separates Total Subsidence’s bodily reassembly from forbidden settlement reconstruction. Filled source-supported γ M.A.W. grade and named the source-supported +2 Clarity without changing figures.

**Evidence/history:** Complete original407viewerlines; complete exact559A–D Souvenir set, including room/doorway first marker, False Shelter, Room With Two Windows, Market Awning, Hearthstone and all failure/care/resonance conditions. Master MAW644–646/details7535–7567; Entity571; entire Tale20211297–11350; CSV735–738; archetype242; disposition364. Full-name/code/Souvenir/exact-pair search across current and archived WIP/CHANGELOG found only Batch35 prose/Final Observation and overlap cleanup, not prior source-led set/pair dispositions. No prior independent equipment-ledger row for O-IIIγ-559; current/archived WIP/CHANGELOG exact SE-559-B/MAW-W-559-01 and full-title/Souvenir history finds no completed comparative review. Batch35unit4 67f2241 is Final Observation/prose work, not equipment source coverage. This complete exact-set review earns +1Types/+1Weapon, while unresolved written-design relationships earn +0SE. Five actual checks PASS, full final read complete. LC_ALL=C words6776→6850; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B160_03_BROKEN_RUIN.md`.

**Holds:** Survivor-only visibility in Warden section versus faint to eligible wardens and detailed immediate material identification, declared/undeclared survivor work, three successful survivor cycles versus all volunteer refusals: observation access and staffing history remain unresolved. Do not normalize infirmary eligibility into a disclosed biography or claim all can see fully. Multiple buildings can belong to one collapsed settlement, so different fragments alone do not disprove Tale continuity; however “not one physical ruin and never have been” versus carried fragments and rooms of the settlement requires provenance scope. Own-body reassembly now distinguished from settlement restoration; no reconstruction of the town authorized. No-face weeping versus collapse sounds and remembered rooms need not imply human facial anatomy. Source A deliberate pursuit/collapse and40%+10perturn versus primary’s two nonpursuing conversational returns and reconstruction-triggered10 changes are retained as conflicting source accounts. Original2count/75% activation and65%ultimate already separate, not reconciled by source review. Direct structural danger, resistance physicalmeaningless versus vessel destruction/drop, once-only DustField and barrier instruction remain held. Steel Scavenger’s Dirk with masonry-prying utility versus B slender deep-blue Han-crystal Ruin Requiem/verified escape route, Master indexDirk/detailRequiem and Room archetype versus Medium3 have no form mapping. A projected walkable witness outline/correction versus local no-drawing/no-reconciling rule and equipment useless to put anything together remains unresolved. Suit dustweave/grit versus C Han-silk crackseams/movingdoors and Master LivingChitin; Stigma glass-backedtimber versus D shiftingcrystal have no documented transition. Item numeric profiles and γ grade align; +2 Clarity is directly supported but no safety/completion follows. Tail4%versusCSVAccessory5%, six note-free grants versus source random acceptedcycle and firstsurvivorgrant timing remain held. No new XLSX parity claim. Narrowed Appearance movement summaries and Total Subsidence note do not certify unchanged Warden waiting-as-whole-activity or Appearance never-rebuild-anything phrasing; read those with the unresolved whole-file scope, not as evidence of a new settled design.

**Commentary:** The gate clerk did not fail by admitting people carrying stones. The stronger tension is the infirmary’s justified protection excluding the clearest witnesses while the market accepts a difficult neighbour. Neither the bodily reassembly nor a useful memory-route weapon should quietly become proof that anyone can rebuild the lost home.

**Progress:** Batch160OPEN3/5; No change0/3. Whole-designHELD/+0SE; Fresh source-review credits +1 Types/+1 Weapon; SE +0. Types250/301(83.06%),51/301remain; Weapon250/287(87.11%),37/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no161/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch160 / unit4 — Myrmidon `O-IIβ-235`:** [[SE-O-IIβ-235_Myrmidon_찢어진_영혼](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-II%CE%B2-235_Myrmidon_%EC%B0%A2%EC%96%B4%EC%A7%84_%EC%98%81%ED%98%BC.md "SE-O-IIβ-235_Myrmidon_찢어진_영혼.md")]

Six repairs: breach alert/movement describe stationary Corrupt-field spread rather than indiscriminate escape/hunting; Final Observation failure no longer makes the figure leave. Restored an Observation Log heading above its existing records, removed doubled warmth wording, and replaced the unrelated mother-lost-child Archive Note with this dossier’s already documented bound service/proceedings record.

**Evidence/history:** Complete original440viewerlines; exact1021A–D complete with binding/source-trace/failure/care (no standalone item Appearance headings). Master668–670/details7799–7831; Entity579; complete Tale21011745–11800; CSV246–249 plus519 control Panopticon; archetypes160/421; disposition268. WIP4926–4944 and CHANGELOG4279–4281 establish Batch102unit4 fullset/exactpair prior review. No swapped SE235 or Panopticon figures. Batch102 unit4 627637ed already counted full-set source review and exactSE-1021-B / MAW-W-1021-01. Same-numeric Panopticon C-IIβ-235 is a different primary/source identity and is not imported or recounted. All three credit increments zero. Five actual checks PASS, full final read complete. LC_ALL=C words7413→7434; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B160_04_MYRMIDON.md`.

**Holds:** Stationary never-moved body versus StoryLog2 moves through corridors, operationalSpeed1.45 and attack backed-into-corner; no scope/chronology resolves this. New breach wording follows repeated current stationary/Corrupt account but retains the contradictory corridor record. Chestsplit vs crown-to-chestFlavor and reaching-throughtear versus bodytranslation need conditions; no two independent bodies inferred. Condition separateperson/office cannot be fully met in Watch attribution law, only approached. Thirty-nine/forty-one narrowings temporary/eleven-daymean/zero cumulativechange remain; neither success nor truth admission cures the originating harm. Registry “no procedural support/protectionabsolute” versus annuallyrenewedwaiver, de-attribution protecting institution and worker lost posting remain unresolved, not whitewashed. Gauge3count/60activation/65ultimate/40breach and representation-triggered10 changes vs per-turndrain left intact; privategrievance target vs nearestperson generic FirstTarget has no resolved priority. Primary exposure-notphysical vs physicalwall/personcracking and split spiritualattack vs BodyGrudge need scopes, not imported elementconversion. Mother-template replacement is explicitly a source-specific archive-summary repair, not an invented identification of servant’s family. ExactA–D identify SE1021/Myrmidon[Fang], not PanopticonSE235WatcherLens. Local/Master-index porcelainSpiritUrn and detailedMasterTornSoulFang/SideMyrmidonFang unresolved; no standalone itemAppearance supports bone-sickles except archetype1021 Room, while archetype235 UrnInstant and localShort2 lack mapping. Local uniform-insignia ban vs operator harness and unspecified institutional marks not permission to represent. Suit/source basic stats andβgrade align; extra obedience toll presentlocally and notselectedasgenericforallpieces. PendantTail5%/+1unnamed remains perA/D and CSVAccessory5% different scope; no inferred named stat. Full-set source resonance cannot settle institutional attribution or undo grief. No new XLSX parity claim.

**Commentary:** The two valid documents are more disturbing than a secretly irregular file: commendation and household ruin can be produced correctly by the same institution. The waiver likewise cannot be celebrated as uncomplicated protection when it left a worker unable to defend themselves. A narrower split is real relief, not a repaired institution.

**Progress:** Batch160OPEN4/5; No change0/4. Whole-designHELD/+0SE; No new source-review coverage claimed; see the individual history and eligibility evidence. Types250/301(83.06%),51/301remain; Weapon250/287(87.11%),37/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no161/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch160 / unit5 — Feu Follet `O-IIβ-301`:** [[SE-O-IIβ-301_Feu_Follet_녹아내린_불꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-II%CE%B2-301_Feu_Follet_%EB%85%B9%EC%95%84%EB%82%B4%EB%A6%B0_%EB%B6%88%EA%BD%83.md "SE-O-IIβ-301_Feu_Follet_녹아내린_불꽃.md")]

Ten supported repairs: Corrupt alert no longer asserts physicalescape; Story1 distinguishes remembered fire from presentheat instead of denying the originalfire; activation no longer says nothing but meltchanges. Condensed duplicated confrontation paragraph and scoped Registry prohibition to suppression, preserving withdrawal aid. Removed the blanket warmth grant from Operational Notes as well as Use Notes. Expanded matching blue-silkSuit from exactC and differentiated Weapon/Shroud/Ember function, tolls, failure, removal and memory care in UseNotes and FieldUseRecord.

**Evidence/history:** Full original446lines. ExactSE301A–D complete including B internalblade/lanterncare discrepancy; C reread separately after combined output truncation. Mastertable671–673/details7832–7864, Entity580, entireTale21111801–11856, Registry587–590, archetype184, disposition267. WIP4675–4714 and CHANGELOG4245 explicitly record prior fullset and exactWeaponreview; old shortcommit6e06fc0 not locally resolvable, so not falsely claimed git-verified. Batch108unit2 recorded as6e06fc0 already reviewed exactSE301A–D and exactSE301B/MAW-W-301-01; both sourcecoverage credits previously earned. No repeat credit for current reread or source-supported Suit detail. Existing O-IIβ-301 is not the separately blocked Batch301 import. Five actual checks PASS, full final read complete. LC_ALL=C words7807→7852; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B160_05_FEU_FOLLET.md`.

**Holds:** Mixedheavycore with instrument beat/diameter/melt/coldgap versus Watch “nothingphysical/noinstrumentalevidence/no thermalreading” remains unresolved. Coreidenticaleveryaccount versus subjectiveface need an observationontology not supplied. No new measurableinstrument or corporealface invented; sourceA supports mentalheartcore but does not settle physicalreadings. Fire originalreal vs memorydecayed retained; people atfire/outlivedthem vs peoplewhoneverreachedit remains uncertain provenance, not conflated. Gauge3count/60activation/65ultimate/40breach and reassurance+10 vs elapsedComposuredrain retained; noassuranceharmabsent anchoredbody is absolute beyond evidence. Feelwarmthvsphysicalheat and fireout/fullmeltthreshold remain scopedholds; no numbers or PhysicalForm changed. Health-informationnotusedforrostering/noask/212unqueriedwithdrawals vs Registry equipmentnotissuedtoactivebereavement remains a policy/equipment tension; no invasive screen invented. Planning objection remains correct and unanswered. Interaction onlyface matters vs gauge/core procedure; HappyMask “withdraws” is core dimming/perceptionthinning, not provedtranslation; elevenmetres not suppressionscope. Zero pairagreement tripwire is not proof of unique identity across all imaginable observers. ExactWeaponB has blade inidentity/care/sheathe but lanternAppearance/shutter; primaryironBrandLance with tissueburn/cauterize/no regeneration versus separator MindLament held. Masterindex631BrandLance/detailRequiem and archetypeW301Instant vsShort2 supply no transition. Local “lash”/bladeTrivia not proof of oneform. Suitcurrent supportedblueHan-silk/coldpatterns/innerthread matches exactC whileMasterLivingChitin remains distinct; EmberTail5%/+1Clarity matchesA/D andlocal, RegistrygenericAccessory andMasterOcularLens not normalized. ExactAsetresonance boundedwarmth cannot mean everypiece suppliescomfort ormemoryerasurecure; no equipmentcoverage recredit.

**Commentary:** The rescue really happened; rejecting its false present authority must not erase that past comfort. The opt-out protects private grief without pretending that the remaining workers or the rota bear no cost. Those distinctions are stronger when the equipment also separates warmth, protection and cutting rather than granting the same comforting effect three times.

**Progress:** Batch160OPEN5/5; No change0/5. Whole-designHELD/+0SE; No new source-review coverage claimed; see the individual history and eligibility evidence. Types250/301(83.06%),51/301remain; Weapon250/287(87.11%),37/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no161/merge/visual claims. WIP and CHANGELOG updated together in this unit.

## Batch160 — CLOSED 5/5

**Batch160 closure (2026-10-21): CLOSED 5/5; No change 0/5; all five whole designs HELD.** Repeated Survivor, Calling Bloom, Broken Ruin, Myrmidon and Feu Follet each received supported repairs, complete final reread, individual Commentary, both-log updates and an individually gated, verified push. Exactly 40 replacements; LC_ALL=C words35,447→35,690(+243). Fresh closure validators25/25 PASS with no acceptance exceptions; ledger tests10/10 PASS. Digit sequences, all301 classification PhysicalForm rows, fingerprinted sources and296 unselected primaries preserved. Only fresh exactSE559 source comparison adds +1Types/+1Weapon; Batch35unit4 prose/FinalObservation was not earlier equipmentcoverage. Other four reviews already counted; no duplicatecredit. SE completion+0. Types250/301(83.06%;51remain), Weapon250/287(87.11%;37remain;14excluded), SE12/301(3.99%;289remain). States8changed/4retained/67held/2blocked/220pending. Equipment/sourcecoverage is not design/artworkcompletion. Pending≠Nochange; no ladder expansion. Comparator unchanged557candidate differences, not proveddefects. Both WIP and CHANGELOG updated again at closure. No Batch161 authorization, merge, deployment or rendered/live-site inspection. PR14 OPEN/draft/NON-WIKI; owner controls merge. SeparateBatch301 import blocked on eight ownerbodies/one4+4/generatevalidatebeforecopy; existingFeuFollet301 is not that import.

[Closure report](SE_APPEARANCE_REVIEWS/B160_CLOSE.md) · [Machine evidence](SE_APPEARANCE_REVIEWS/B160_CLOSE.json)

## Batch161 — OPEN 0/5

**Batch161 opening (2026-10-21): OPEN 0/5.** Owner p authorizes this batch only. Fresh screen: 220 pending, 67 source-cue candidates. Frozen queue: O-IIβ-467, O-IVδ-762, O-Iα-631, O-Iα-973, C-IIIβ-275. Whole original/source/history and final reads, five actual validators, individual gate/push, Commentary and both WIP/CHANGELOG required per completed unit. Three cumulative No change dossiers trigger 5→7→10; pending is not No change. Current independent counters unchanged: Types250/301(83.06%;51 remain), Weapon250/287(87.11%;37 remain;14 excluded), SE12/301(3.99%;289 remain). Existing held-source coverage is not finished artwork or design. States8changed/4retained/67held/2blocked/220pending. No162/merge/artwork/deployment authorization. Batch301 remains blocked on owner eight bodies/one4+4/generatevalidatebeforecopy.

**Batch161 / unit1 — Memory Chain `O-IIβ-467`:** [[SE-O-IIβ-467_Memory_Chain_솟구친_사슬](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-II%CE%B2-467_Memory_Chain_%EC%86%9F%EA%B5%AC%EC%B9%9C_%EC%82%AC%EC%8A%AC.md "SE-O-IIβ-467_Memory_Chain_솟구친_사슬.md")]

Nine repairs: restored the recorded gauge condition alongside the separate failure-count instruction; treated measured transit as a baseline rather than an invariant; distinguished voice travel and line extension in both movement profiles. Three Appearance summaries now retain the pale-wet-crystal account as well as blue spirit-light without inventing a trigger. Use Notes now preserve identity rather than claim the Shroud blocks memories, and record the distinct Weapon/Link consent, cost and return duties; grade no longer certifies extraction stability.

**Evidence/history:** Complete original414lines; exactSE467A–D complete including B wetedge/voices/consent, C distinctidentitydrying, D owners/duration/return and doubleconsent. Mastertable677–679/detail7898–7930, Entity582, completeTale21311913–11968, Registry687–690, archetype223, disposition368. WIP4541–4546/CHANGELOG4226–4228 and existing fullsetparagraph confirm Batch110case2 prior comparative set and pair review. Batch110 originalcase2 recorded7e98119 already reviewed exactSE467A–D and SE467B/MAW-W-467-01. All coverage increments0. SharednameChainofMemories is a counterpart, not an equipmentidentity crosswalk. Five actual checks PASS, full final read complete. LC_ALL=C words6704→6761; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B161_01_MEMORY_CHAIN.md`.

**Holds:** Fixed axis/stationary memorybinding versus castwetiron/rustskin/whiplash/physicaldrag, Speed1.45 and untouched resistance/vesseldestruction assumptions remain unresolved. Pale crystal and blue spiritlight kept as co-recorded visual qualities, not invented separate transformations; voiceoneway versus “andback”, circle/turn/standbeside requires spatial account. Gauge60 and count3 are now both acknowledged without changing figures; 65Ultimate/40breach/turnversuscycle and elapseddrain still not quantitativelymapped. Return19 vs Registryeleven retained without invented chronology. Constanttransit/constantwordinterval/returnshortening/slacklonger and onepermanentinsertion vs twoorderfailures/fivecollapses need distinctstate definitions; no sequence repaired by changing numbers. No sharedword between counterpartchains cannot prove no sharedpeople; Weaverfailedall4 vs sourceB stolenlink cut claim and Risuscausation unclear. Sourceconsensualextraction vs dead/unreachableownername sufficient suppression remain different duties, not expanded extraction permission. No fatalities/no lastinginjury versus11borrowedrecollections not declared psychologicallysafe. ExactB deepblueHancrystalblade/wetvoiceedge versus localbrassvolleygun/lead/waterjacket and MasterindexChainGun/detailRequiem/archetypeMedium vsShort2 remains held. C identityshroud agrees material/removablelinks but local damphem vs source drylinksstoredapart and old overruninversion are not sharedsource warranties. D Tail5%/+1Clarity agrees; local permanentlyopenlink/handword versus consentmechanism stays unmapped, MasterRingsHandSeals and genericCSVAccessory not normalized. FourStigmas/nineteenreturns is observedcorrelation notprocedure. Untouched Registrum Observation Note still says the Shroud holds memories off before inversion; that old claim conflicts with both sourceC and localAbility and remains an explicit hold, not a whole-file equipment seal.

**Commentary:** Returning a memory to a name is not the same as restoring a friendship or proving that the named owner can still answer. The useful relief is temporary and the borrowed fondness may not feel like injury. The equipment should protect distinct people without pretending shared history belongs to whoever speaks most confidently.

**Progress:** Batch161OPEN1/5; No change0/1. Whole-designHELD/+0SE; No new source-review coverage claimed; see the individual history and eligibility evidence. Types250/301(83.06%),51/301remain; Weapon250/287(87.11%),37/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no162/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch161 / unit2 — Grasp `O-IVδ-762`:** [[SE-O-IVδ-762_Grasp_타오르는_다리](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-762_Grasp_%ED%83%80%EC%98%A4%EB%A5%B4%EB%8A%94_%EB%8B%A4%EB%A6%AC.md "SE-O-IVδ-762_Grasp_타오르는_다리.md")]

Eight repairs: Movement distinguishes occupied-gap posture and recorded relocations from unsupported uprightpursuit; Consequences/BreachMovement no longer invent interiorfacilityroutes or universally collapsing spans. Filled supportedγ equipment overview without changingδ entitypotency; preserved count and gauge as separate records; removed guarantee no physicalinjury can occur. UseNotes and AfterUse now distinguish source-specific tolls, testimonialbinding, autobiographicalcorrosion, witnessshutdown and attribution-beforecare.

**Evidence/history:** Full original427lines and exactSE762A–D complete, including each canonically labelled Appearance (functional/testimonial, not invented silhouette), source-trace histories and corrosion/care/shutdown. Master713–715/details8294–8326; Entity595; completeTale22512589–12644; Registry851–854; archetype285; disposition413. Current+botharchivedWIP/CHANGELOG fullidentity/exactpair/itemname searches found only R29/R18managementprose and design-family/disposition mentions, not independent equipmentcoverage; perfilegitlog only availablebaseline10cd20a, not falsely treated as full oldhistory. Fresh exactSE762A–D/fullset and SE762B/MAW-W-762-01 comparison, no prior independent ledgerrow; current and both archived WIP/CHANGELOG hits concern management-clause cleanup, family-shape survey or disposition, not comparativeequipmentreview. Prior same-sorrow mentions in IAloneCrossedSE106 are not this pair. Earn +1Types/+1Weapon, SE0; no retroactive credit. Five actual checks PASS, full final read complete. LC_ALL=C words7052→7185; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B161_02_GRASP.md`.

**Holds:** Gap surveyedneverchanged/archunmoved versus elevenpositions,4filledgaps and “relocates”; explicitstatusconditions/route remain absent. Firstthreeattacks plank/waterbelowphysicalbridge versus suspendedpersoncrystal need mapping; foursecondspan supports limitedcrossinghazard but not generalcollapseunderallcrossers. Ultimatefigures everygap actualmultiplicity vs sourcestilloneidentity need scope. Originalbreachalert collapse guarantee retained as contradictory evidence, not certified by limitedMovementrepair. Pugnahan prohibited inRecommendedResponse versus Escalationpriority drivebackonlyonceallclear and tableallfourvalid remains policyconflict. Count1 vs90activation vs65Ultimate and sourceA escalation gauge require ordering; newnoteacknowledges separatecondition without inventing triggers. Fortyminute limit vs oncehourcycle/24turnBattleLength unresolved; nofatalities/nostrikesunprovoked not immunity. Tearsvanishflavor vs nonevaporatingwarmliquid, hotcontactnophysicalharm but emotionallypainful remain conditions not alternateform proof. Reliefreview says nobodyfailed; prohibition account requiredread vs postedworker refusingread remains governancecontradiction, not erased. Presentphysicalfilledground engineeringcorrect vs gapreal claims remains surveyedextent question. Allnames31/27/4 preserved, not transplanted from anotherrescuer. FlowingBridge namecomparison/crosspermission not newpermission forGrasp; ScarWalker protection not reliablecontainment. ExactB functionalAppearance supplies no local slendercrystalvoicepitch silhouette; archetype bridgearcblade/missingghostspan and MasterReliquaryCenserBell lack mapping to that blade. Coreγ7–12/Fast3/Medium3/Skewer/max3/40 and C resistances/max3/35 align; originalBodyactual span not equipmentform. Suitlocalrain/smokewarm and heatresistance/socialunaskedforhelp toll vs sourceC minorjoynumbness remain distinct; CrowncircletTail vs Masterfloatingorbscoronets/CSVAccessory5% vsA/D4%; +2stat unnamed inA/D, do not inventClarity. SourceD onlyminorwoundhealing nooriginalrescuecure; all3care/costs/sourceattributioncompared but forms/tollsheld.

**Commentary:** This is a failure in which nobody failed. A technically sound plan to cross can still be the hazard, and a span bearing weight does not make its invitation safe. The four unclaimed names matter as much as the claimed ones; neither an efficient detour proposal nor an equipment healing effect can retroactively complete that rescue.

**Progress:** Batch161OPEN2/5; No change0/2. Whole-designHELD/+0SE; Fresh source-review credits +1 Types/+1 Weapon; SE +0. Types251/301(83.39%),50/301remain; Weapon251/287(87.46%),36/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no162/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch161 / unit3 — Errant `O-Iα-631`:** [[SE-O-Iα-631_Errant_사라진_뿌리](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-I%CE%B1-631_Errant_%EC%82%AC%EB%9D%BC%EC%A7%84_%EB%BF%8C%EB%A6%AC.md "SE-O-Iα-631_Errant_사라진_뿌리.md")]

Eight repairs: replaced generic crawl/prowl/pursuit with documented surfacing/sinking and downwardbreach in classification, Consequences and BreachMovement; filled αequipmentoverview. Named supported +1Resolve Charm bonus. Final Observation now requires present belonging without denial of past and uses observed reaching instead of misclassifying StablePugnahan retraction as escalatingfailure. UseNotes separate piece-specific binding, consent, tolls, expiredanchor and voluntaryexit from local universalhold/quartersreport.

**Evidence/history:** Full original393lines, exactSE631A–Dcomplete including BorrowedStall, bladevMaulform, C expiredanchor/hem/choice, DHeadsteel/ConsentBearing/bestowal/exit/stacking. Master755–757/details8756–8788; Entity609; completeTale23913379–13434; Registry783–786; archetype261; disposition359. Current+botharchivedWIP/CHANGELOG identity/pair/name searches found R29/R18managementcondition prose only. Independent equipmentledger no631row. Fresh independent exactSE631A–D/fullset and SE631B/MAW-W-631-01 review; no earlier sourcecoverage disposition found in current/archived logs or ledger. Managementclause cleanup was not an equipmentpaircomparison. Earn +1Types/+1Weapon/+0SE; no newbodycompletion inferred. Five actual checks PASS, full final read complete. LC_ALL=C words6364→6438; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B161_03_ERRANT.md`.

**Holds:** Orientation remains unresolved: PhysicalForm/lowerhalf fades/upperreaches and protocol upperhalf vs Story1/Flavorhiplegslowerbody/nothingabove/Recognitionabsencebothdirections. SourceA supports lowerbodyfades but source does not supply a transition to leg-only form. Sourcefloorphantasmal versus absentrootchannel/stump/crushing and vesselphysicaldestruction remain unscoped; nobodyedit/newanatomy. Presentanchornamingandstay inRecommended/Battle/Story4 versus breach requires bothwithoutdenyingpast remains partialinstruction tension outside repairedFinal. Everyoldaddress“failsall11” versus ViderehanStable showingoldhomes notsameasforcingroot but actualprivatequestionwhoasks notestablished; Final withholdingbriefing while lowesttenuremostexposed remains ethicalpolicyhold. Yield10–14/no injuries not evidence mental safety; +1Resolve named onlysourceD notgaugeadjustment. SourceA BorrowedStall lockednewhome/extraction/onechoosingleave and3floorruptures vs primaryfloorlosswalkbacksingleevent/2breachesmotionlessstorage/worker-staycondition incompatible historywithoutcrosswalk. SourceA +10perturn vs primary placement-based +10; sourceA5%otherresistance vsprimaryeffectivelynone retained. Firstremovalunrecorded vs registeredfirstaddress in failedwalkback remains archivalambiguity. Tree/Banyan lackreaction notproofnowantsearth forever. LocalironGreatCleaver vs exactB compactmatteblackHansteelhoveringMaul, MasterindexCleaver/detailMaul/archetypeRoom vsShort2 noformtransition. Coreα3–6/2/2/Single/5/15 and C1/1/1.5/.5/5/10 align; Mantlepalerootwrongfit/issuedroomprotection/unpackingcost vs sourceblackHanweave with timedchoice/fatigue/rest notprovedsame. Charmdriedrootwire vs exactDsteelHeadengraving/consentclasp, firstelderlywarden vs BorrowedStallresident bestowal; Head5%/+1Resolve sourceagrees, genericAccessory5% taxonomy separate. Local allthree cutoneevent/median19minutes/onlywirewarning vs sourceuniqueformation/care needsresolution; no automaticquarterinspectioncure.

**Commentary:** A present anchor should not erase the places someone lost, and staying should remain a choice rather than a new lock. The source’s opened stall makes that distinction concrete. A Minor label does not make it harmless to keep sending the least-settled people into a holding that reaches for them most often.

**Progress:** Batch161OPEN3/5; No change0/3. Whole-designHELD/+0SE; Fresh source-review credits +1 Types/+1 Weapon; SE +0. Types252/301(83.72%),49/301remain; Weapon252/287(87.80%),35/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no162/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch161 / unit4 — Yggdrasil Wound `O-Iα-973`:** [[SE-O-Iα-973_Yggdrasil_Wound_찢어진_나무](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-I%CE%B1-973_Yggdrasil_Wound_%EC%B0%A2%EC%96%B4%EC%A7%84_%EB%82%98%EB%AC%B4.md "SE-O-Iα-973_Yggdrasil_Wound_찢어진_나무.md")]

Eleven repairs: explicitly scoped movement to existing Non-Breach/Breaching states; corrected AppearanceStates and Registry introductions that falsely said the mixed classification describes only the contained state. Removed two empty-tunnel rationales for a physically damaging but selectively visible breach; did not invent a seal solution. Repaired truncated AfterUse clause and separated cost evidence across Before/During/After fields. Interaction introduction now respects observed pairings and the permanent MemoryWell prohibition. Corrected “an Specialist”.

**Evidence/history:** Full original435lines including complete existingAppearanceStates/onewaycountzero and StatementRecord4203/4226/4230/4237. ExactSE973A–D fullyread including BcenserAppearance/internalLens, C faintselfabsence vs localcopies, DfunctionalAppearance/no namedbonus, source-trace/care/witnessshutdown. Master773–775/details8954–8986; Entity615; entireTale24513719–13774; Registry1123–1126; archetype399; disposition220. WIP4229–4245/CHANGELOG4148 show priorBatch123unit2d760784 sourcecoverage; archivedBatch33unit9 and50unit3 are prosehistory. Batch123unit2d760784 already counted exactSE973A–D and SE973B/MAW-W-973-01; no repeatcoverage. EarlierTornTree name labelled inprimaryhistory, not anotherentitycrosswalk. Wholebodybreachstate logicnotcertified by formerequipmentreview. Credits0/0/0. Five actual checks PASS, full final read complete. LC_ALL=C words8358→8393; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B161_04_YGGDRASIL_WOUND.md`.

**Holds:** Existingstateaccount itself needs evidence/scope: classificationPhysicalbreachform/no-vesselcontained nowexplicitlymixed, notfullyrewritten. AppearancePrimary physicalunqualified vs Identificationmental; identificationeverybodycansee“notthis” vsperceptiongate remains perhaps trueallrestrictedonly. Statezerooneway vs gauge45activation/65Ultimate and count4restoration needs timings, no reversal invented. StateMeasurement directcleft vs Trivia nooneperceivedunderinstrument remains unresolved; rootsbecomevisible FlFollowgrief inside mentalstate vs physicalroots notsameproof. Singlepreservedmemory/Tale/amnesia versus Origintwosignedlocations and statementcannotbothtrue is richerbutnot source-resolvedchronology; 6years service versus60yearTornTreehistory unresolved. Appendonlyarchive protectsagainst4203laundering yet LaterStatementallows officerpreferolder; no correctionseal/deletion invented toclaimcure. Nonperceivingpartner “unabletohelp” vs groundedcareactualfunction remains inaccurateabsolute. Perceptionroster sensitiveexposure notpsychdiagnosis; no assumptioneveryoneunconflicted safe. First3attacks blackroot/physicalwood/earth and felledfulluprooting vs initialincorporealnobody/nogrip requirestatescope. Warmthindexeddenial vs affecteddensitydoubles/triplesgenericFlavor unsourcedquantitativeprose retainednotnew. InteractionMemoryWellfourcmpermanent vs wholeRecordedclefttrend notclaimallcausedbythatpairing; Corners closedprohibition preserved, HollowTreewarmthtransfer notbodyfusion. ExactBcenserAppearance aligns physicaldetails but Btitlecenser/internalTornLens/SideALens/MasterdetailLens unresolved; localhalfpairmemoryloss vs sourceBsmallnamelessmemorycost. ItemCfunctionalAppearance faintselfabsence notsupportedlocalduplicatecopies/clothsilhouette; D functionalHead5%/unnamed+1 and bothmemoriespain notproofforglassroot/cycleforfeiture. Sourceall3autobiographicalcorrosion vs localVeilcost comfortabletwo selves notsame. Field timingweek/rotation stilllocal notuniversalwarranty; unchangedStatinterpretation alloperators“as twopeople” exceeds sources and remainshold. All3corenumericprofilesagree; archetypeLong vs Short2 notnormalized; noXLSXparityclaim.

**Commentary:** An append-only archive can protect testimony from laundering and still trap a person beside words spoken while concussed. Keeping both accounts is not the same as finding either true. The record should preserve that conflict without using it to tell responders that a physically collapsing tunnel contains nothing.

**Progress:** Batch161OPEN4/5; No change0/4. Whole-designHELD/+0SE; No new source-review coverage claimed; see the individual history and eligibility evidence. Types252/301(83.72%),49/301remain; Weapon252/287(87.80%),35/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no162/merge/visual claims. WIP and CHANGELOG updated together in this unit.

**Batch161 / unit5 — Crucible `C-IIIβ-275`:** [[SE-C-IIIβ-275_Crucible_분노의_용광로](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B2-275_Crucible_%EB%B6%84%EB%85%B8%EC%9D%98_%EC%9A%A9%EA%B4%91%EB%A1%9C.md "SE-C-IIIβ-275_Crucible_분노의_용광로.md")]

Eleven repairs: movement and detailed spatial record now describe a fixed Place and its working volume, not a mobile device; removed fuel-demand contradiction from DetailedActivationRisk. Named the source-supported Charm bonus Resilience. Replaced universal object-anger doctrine with exact piece formation/binding, distinct costs, failure/care/release and protected right to stop. All four FieldUse stages now separate those costs, reject invented equal rates and do not postpone observation until a week later. Final failure no longer makes a stationary Place withdraw; FlavorAfter ties cooling to naming rather than departure or door sealing.

**Evidence/history:** Full frozen471line primary read including complete WardenRecord/HeatReturn/retaliation and SweepSheet, whole Origin/Tale and ownmaterial+grievance trigger. Exact275A–D readcomplete, including eachAppearance/binding/corrosion/care/release. MasterMAWinventory53–55/detail937–967; Entity369; Tale5 249–296; Registry563–566; archetype171; dispositionNeutral193. CurrentWIP2749–2762 and CHANGELOG2753–2761 priorBatch139unit2 exactsourcepair review8af82016 read; current/archiveddesignation/name search. Prior139holdlist used as a backlog, not resolution proof. PriorBatch139unit2 commit8af82016cd09de01ea07cb83136fd865019e6672 already reviewed exactA–D and counted SE275B/MAW-W-275-01. Equipment_reviews currentincrement list has no row because baseline absorbs oldercoverage; absence does not authorize duplicate credit. No new Types/Weapon credit, SE remainsHELD. Five actual checks PASS, full final read complete. LC_ALL=C words7780→8047; digits and sources unchanged. Evidence: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B161_05_CRUCIBLE.md`.

**Holds:** Annualidlefloorunaffectedbygoodwork versus fourdegreeinwatchdrop not fullyspecified; no new baseline/timecurve or longtermcure invented. SourceA honestly namedgrief/repairtools vs primarygriefdoesnotcool, primaryStorynevercools vs shorttermmitigation, sourceMasterconsciousfurnace/Pugnahanprimary vs primaryhistoricalcorrection. Namingprotocol takesplacebeforeownsupervisor while archivepromisesstatementsnotshown; HeatReturnanonymity alreadybreached by smallteamelimination and twopeoplemoved/onequit. No claim confidentiality/schemefix. Primarynobodyattacked and onlyreleaseeverinjured vs Hammerdirectstrike/Quenchwound/ultimateAoE needs statescope; inputmaterials+grievance bothneeded vs entryproximityaloneactiontriggers. SourceAexpansionconnectedworkshops vs primaryfixedPlacephysicalworkingvolume notstate-resolved; newmovementscopedoesnotdenyconditionalexpansion. SourceAcontrollednonweaponuse/equipmentextract vs primaryauthorisedArchitectssuspended/alwaysdestroyunattendedobjects notresolvedbynewsetnotes. Do notauthorizeproduction or changesuspension. SourceBcrimsonpulsingnearhiddenanger vsprimarydarkfaintwarm/forge-scaleheadringsflat; sourceCwarmjoints/coldskin vs primarywarmabsorbedheat/creaks/cut; sourceDcooledcoalcrimson vs primarydarkthumbironheatedbysilence. Existingprimary allDistrictmark/forgedlanguage repaireddoctrinebut actualsilhouettes unnormalized. SourceDbestowalnamedrepairtool vs primaryfiveWardensbeforeasuperior retainedaslocalaccount, not universalbestowalrecipe. Primaryeffectinabilityleaveunsaid vs shorttemper doesnotdiagnose hiddenanger. SourceDcare namingmustchangeworkcondition vs primaryspeechalwayscools distinctionnotoverwritten. Numericpieceprofilesagree: BβGrudge5–9/2/2/Single100%/4/25; C L1 G.4 V1.8 W1.2/4/20; DTail5%/+1Resilience nowexplicit. ArchetypeRoom vsShort2 held; RegistryB/Cgenericuntypedstatistics and literal** DElement/Accessory5% notfixed. SourceChotjoints/coldForgeperiod vs continuouslyhotidlefloor distinctionunresolved; no coolingrecipe invented. Localweeklyhold/reissue notclaimedexactsourceuniversal; sourceFormnewbinding/care doesnotmakedesignfinished.

**Commentary:** Permission to shout is not the same as having the cause heard. Crucible’s stronger sorrow is an institution that treats tolerated anger as free productive fuel. The Charm’s warning matters here: naming can itself become another quota, and a logged grievance is not a changed work condition.

**Progress:** Batch161OPEN5/5; No change0/5. Whole-designHELD/+0SE; No new source-review coverage claimed; see the individual history and eligibility evidence. Types252/301(83.72%),49/301remain; Weapon252/287(87.80%),35/287remain; SE12/301(3.99%),289/301remain. Cumulative3Nochange triggers5→7→10; no162/merge/visual claims. WIP and CHANGELOG updated together in this unit.

## Batch161 — CLOSED 5/5

**Batch161 closure (2026-10-21): CLOSED 5/5; No change 0/5; all five whole designs HELD.** Memory Chain, Grasp, Errant, Yggdrasil Wound and Crucible each received supported repairs, complete final reread, individual Commentary, both-log updates and an individually gated verified push. Exactly47 replacements; LC_ALL=C words36,258→36,824(+566). Fresh closure checks25/25 PASS with no exceptions; ledger tests10/10 PASS. Digit sequences, all301 classification PhysicalForm rows, fingerprinted sources and296 unselected primaries preserved. Grasp and Errant alone add +2Types/+2Weapon; MemoryChain prior110, Yggdrasil prior123/d760784, Crucible prior139/8af82016 earn zero repeatcoverage. SE completion+0. Types252/301(83.72%;49remain), Weapon252/287(87.80%;35remain;14excluded), SE12/301(3.99%;289remain). States8changed/4retained/72held/2blocked/215pending. Sourcecoverage and technicalPASS are not completed design/artwork. Pending≠Nochange; no expansion trigger. Comparator unchanged557candidate differences, not proven defects. Additional Yggdrasil backlog explicitly retained: ValidWorkTypes still lists prohibitedPugnahan, and AtLimit/StatInterpretation still overgeneralizeVeilcost; repairedstate/fieldparagraphs do not certify these. Both WIP and CHANGELOG updated again at closure; detailed individual in-chat reporting restored. No162authorization, merge, deployment or rendered/live-site inspection. PR14 OPEN/draft/NON-WIKI; owner controls merge. Batch301 blocked on eight ownerbodies/one4+4/generatevalidatebeforecopy.

[Closure report](SE_APPEARANCE_REVIEWS/B161_CLOSE.md) · [Machine evidence](SE_APPEARANCE_REVIEWS/B161_CLOSE.json)

**Batch162 opening (2026-10-21): OPEN 0/5.** Owner p authorizes this batch only. Latest chat instruction is now R31 points21–22: detailed unit changes, Commentary, holds, checks, push results and links are collected in the final message after every command, not interleaved. Per-unit validation, both logs and individual gate/push remain required. Fresh screen215pending/62source-cue candidates. Frozen queue C-IIIγ-031, C-IIIγ-032, C-IIIγ-033, C-IIIγ-044, C-IIIγ-120; five minimum, cumulative3Nochange triggers5→7→10. Pending≠Nochange. Types252/301(83.72%;49remaining), Weapon252/287(87.80%;35remaining), SE12/301(3.99%;289remaining). States8changed/4retained/72held/2blocked/215pending. No163/merge/artwork/deployment authorization. Batch301 remains blocked on eight ownerbodies/one4+4/generatevalidatebeforecopy. Restored branch safely synchronized to verified161closuree4b8aaf before editing; prior reviews were not rerun.

**Batch162 / unit1 — The Observing Bird `C-IIIγ-031`:** [[SE-C-IIIγ-031_The_Observing_Bird_지켜보는_새](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-031_The_Observing_Bird_%EC%A7%80%EC%BC%9C%EB%B3%B4%EB%8A%94_%EC%83%88.md "SE-C-IIIγ-031_The_Observing_Bird_지켜보는_새.md")]

**What changed:** Seven repairs: replaced the unsupported destructive-hunt consequence with the recorded disclosure survey; removed the equation of Stable Work with harmless exposure. Use Notes now distinguish implant/blade evidence and each piece’s actual costs and limits, including debrief, rest and formal recording. Observation no longer dismisses response as a paper exercise. Final failure no longer invents a gauge rise for every permitted look away. Departure and Stat interpretation no longer promise recovery or personal safety.

**Evidence/history:** Complete original461 lines; all exact031A–D read including each Appearance, limits and history. Master inventory59–61/detail1003–1035; Entity371; complete Tale7 365–422; Registry58–61; archetype70; disposition123. CurrentWIP2076–2097 and CHANGELOG2084–2110 prior Batch143unit3 identify exact previously counted set/pair. Full legal/decode/internal-proceedings and short-watch appendices read, not just appearance. Batch143unit3 already counted exact031A–D and SE031B/MAW-W-031-01. Its holds specifically cover blade/implant and no-attack/action differences; no fresh equipment identity or coverage credit. Earlier32/50/66 prose history does not erase that later exact review. Five checks PASS; full final reread complete; words8629→8781 (LC_ALL=C). Digits, classification Physical Form and sources preserved. Receipt `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B162_01_OBSERVING_BIRD.md`.

**Holds:** Body/behavior: no voice versus breach keening and group singing; never strikes versus Sudden Wing and exactA rule-breaking strike. Gaze damage versus pressure rising when attention leaves, and4-second marks versus local disclosure survey, remain held. Count2, core75% and Ultimate65% are distinct unresolved timings. No numerical normalization or invented peaceful/aggressive state. Chronology: four-thousand-year Ultimate versus Year2847 formation; Year4232+1778 and future DecodeStudy4247–4252 versus current anchors; accurate records with orientation gaps versus absolute holds-everything. Do not invent a new court or treat a proposed commission as an adjudicator. Shared-containment versus separation protocol/12-second convergence remains held; trio singing is conditional, not an isolated power. Equipment: primary/Master ocular implant and all-in-view drain versus B blade/RecordedMoment and linked-three falloff, A Skewer. Current names versus Witness aliases and source Stigma forehead versus cord/collar remain held. C weight/joy-loss versus source lightness/trauma; D fixation endpoint was added without claiming all local properties align. Core stats remain unchanged: B7–12/3/5/3/40; C.4/1/1.6/.8/3/35; DHeadEye4%/+2source/+4Clarity. RegistryAccessory5% and archetypeMedium versus Room5 remain held.

**Commentary:** The missing court matters more than the number of eyes. This is a witness whose accurate record can discipline workers but cannot obtain a hearing for the people who formed it. Preserving that distinction also means not mistaking an unaltered record for a complete judgement.

**Progress:** OPEN1/5, No change0/1. HELD, Types +0 / Weapon +0 / SE +0; prior coverage is not counted again. Types252/301(83.72%;49remain), Weapon252/287(87.80%;35remain), SE12/301(3.99%;289remain). Both logs included; detailed chat and links at turn end after all commands. No163/merge/deployment authorization.

**Batch162 / unit2 — Weighting Bird `C-IIIγ-032`:** [[SE-C-IIIγ-032_Weighting_Bird_재는_새](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-032_Weighting_Bird_%EC%9E%AC%EB%8A%94_%EC%83%88.md "SE-C-IIIγ-032_Weighting_Bird_재는_새.md")]

**What changed:** Eight repairs: replaced generic locomotion and diving alarm with recorded laborious walking, limited flight and attendance control. Consequences now describe structural loading rather than an automatic gauge ceiling. Separated equipment costs and the limits of comparison from moral truth; restored independent review before another full-set judgement. Repaired the broken interaction paragraph. Final failure now records weighed aggression without retaliation. Registrum lists all Work responses accurately and no longer promises no personal risk.

**Evidence/history:** Full471-line original including ConsistencyStudy, opinion and SuccessionReport. Exact032A–D complete including all appearances/limits/history/footer (D footer reopened after combined output truncation). Master inventory62–64/detail1037–1090 read in two chunks; Entity372; fullTale8 423–477; Registry62–65/archetype71/disposition124. Primary2026-10-11 full-set note, WIP5184–5200 and CHANGELOG4447 establish priorBatch94unit1. Batch94unit1 40fecbc6 explicitly reviewed full set and exactWeapon pair, following primary/itemcorrections73560193/89e04568. Its absence from incremental equipment_reviews is baseline absorption, not fresh coverage. No repeated Types/Weapon credit. Five checks PASS; full final reread complete; words7943→8080 (LC_ALL=C). Digits, classification Physical Form and sources preserved. Receipt `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B162_02_WEIGHTING_BIRD.md`.

**Holds:** Organic dive/mark PhysicalForm and combat beak strike versus detailed no-strike, voluntary-only weighing; exactA automatic view-mark/challenge strike versus same local limitations remain held. No peaceful/attack alternate state was invented. Tale hand-carried always-balanced scale versus two working scale-eyes and Flerehan seconds of stillness versus one-second Trivia maximum are unresolved. Count2/core75%/Ultimate65% timing; mass falls slowly alone versus only successfulcycle restoration; baseline19/up-to33 versus11kg perperson and load history need scope. All3100 pair comparisons/no cycles do not by themselves establish completeness for every possible pair. Nobody tested objective moral correctness; succession placement does not establish liability or innocence. Source B firearm appearance/statistics match local7–12/Fast3/Medium3/3/40 and 3-target100/70/50; Master12–18/Normal and archetypeInstant unresolved. MasterSuitG.6/V1.2/W.8 versus local/itemG.4/V1.8/W1.2; CTitlePlate/Hardening versus Greatcoat/Counterweight, localweight-cost versus itemdullreflex/revision resistance; D localcrit/prickling versus current-load comparison/bothburdens. Source forms agree but effects do not. RegistryAccessory5% versus ChestBrooch4% held; no stat normalization. Origin says no date/fire attached to assessors while sharedThreeBird accounts call allbornfromonefire. ConsistencyStudy4245–4250/succession4251 and document4232+1778 remain chronology holds. Primary contents-of-comparison prohibition versus internal Study/report use is a substantive institutional conflict, not erased by new watch-log rules. Trio benefit conditional; no solo suppression claimed.

**Commentary:** A perfectly consistent comparison is not a finding of fault. The sharpest part of this file is the institution calling the same output meaningless when a worker asks for relief and authoritative when it flatters the institution. The equipment should not quietly undo that distinction by promising moral truth.

**Progress:** OPEN2/5, No change0/2. HELD, Types +0 / Weapon +0 / SE +0; prior coverage is not counted again. Types252/301(83.72%;49remain), Weapon252/287(87.80%;35remain), SE12/301(3.99%;289remain). Both logs included; detailed chat and links at turn end after all commands. No163/merge/deployment authorization.

**Batch162 / unit3 — The Guarding Bird `C-IIIγ-033`:** [[SE-C-IIIγ-033_The_Guarding_Bird_지키는_새](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-033_The_Guarding_Bird_%EC%A7%80%ED%82%A4%EB%8A%94_%EC%83%88.md "SE-C-IIIγ-033_The_Guarding_Bird_지키는_새.md")]

**What changed:** Eleven repairs: movement and StoryLog now distinguish held posts and recorded repositioning from generic roaming or universal flight. Removed prohibited Pugnahan from valid work and corrected the misleading all-work-available sentence. Resolution now includes the documented duty-ended clause. Consequences, UseNotes and AtLimit separate all three costs, conditional protection and explicit relief. Grade no longer certifies extraction stability. Corrected the relation count/trio claim and the assertion that departure is unsupported.

**Evidence/history:** Complete439-line original including whole PurposeNote, post-review history and WardenRecord. All exact033A–D complete: gratitude, relief resonance, Lens fair/cruel threshold and conscious release, Veil mark and thanks, Wing once-per-encounter/broad danger/fear. Master65–67/detail1091–1121; Entity373; completeTale9 480–533; Registry66–69/archetype72/disposition125. Current and both archived WIP/CHANGELOG by full identity, names, exactpair;113inventory explicitly only componentSuit checked as Convergence control. Longname prose-overlap list inspected as list, not source review. All-ref B history only10cd20a. No prior independent exactSE033B/MAW-W-033-01 or full-set review found in current/archived logs; no equipment_reviews row. Batch113 read033C only to test Convergence assembly, not033A–D or Weapon coverage. R29/post prose/disposition repairs are not exact equipment comparison. Fresh +1Types/+1Weapon; no body/SE completion credit. Five checks PASS; full final reread complete; words6853→7122 (LC_ALL=C). Digits, classification Physical Form and sources preserved. Receipt `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B162_03_GUARDING_BIRD.md`.

**Holds:** Currentnine-year never-step account versus shelterfollowing, eight relinquishedposts and breach relocations remains not fully dated. PhysicalForm dive/mark versus wingsheldforshield/flightStoryscope; Tale pacing/restless versus currentfixedpost unresolved. Purpose-end alreadyknown versus Birddoesnotacceptgone differs from gratitudeendedduty; no mindreading or newpost authority invented. Count2/core75%/Ultimate65%, grey radius4→11metres versus area9/14/21squaremetres, no contraction versus pausedspread and Tide roughlydoubled need independent measures. Combat11strikes/nineyears/fourblockings versus oneaggression/twocauses and Wardenonlyrelocation aggression are unresolved. Ordinarythanks versus requiredsecondclause holds beyond repairedsummary; no automaticrelief or humanDutyabolition inferred. Equipmentprofilesagree BVoid7–12/Fast3/Medium3/Skewer100/70/50/3/40; C1.2/.8/.3/1.1/3/35; DHead4%/+2unnamedworkstat. PrimarysmallunframeddoorviewLens versus sourcebroadblackframedtwo-handthresholdLens notresolvedasstates. Localhandovermemoryloss versus sourceoutside-lineattention; primarygreyhemveil vs sourcecrown-tochestsilverthreadpressure-redirection; Wingcoldface/warmface vs sourceallywarmvanesclose/grey and Headslot versus collarcord. No sourceper-Tick warranty; archetypeInstant vs Medium and MasterRingHandSeal/RegistryAccessory5% vs Head4% remain held. TaleoneMarketfire/allThree versus Weightingassessororigin; 4232+1778 versus officialcurrentanchor, nofourthousandyearhistory created. Historicalprotectiveemploymentrule/404dismissals and PurposeNote9yearmedian/0relief remain morallyconsequential; no unsupportedhumanrecovery introduced. Stand-downhandovers and identitywelfare do not establish an SEdesigncompletion.

**Commentary:** The duty survives because the review rule once protected workers from arbitrary dismissal. That protection is real, and so is the waste of standing an empty post for years. A safe handover is therefore more important than praising loyalty or assuming the guard will know when to leave.

**Progress:** OPEN3/5, No change0/3. HELD, Types +1 / Weapon +1 / SE +0. Types253/301(84.05%;48remain), Weapon253/287(88.15%;34remain), SE12/301(3.99%;289remain). Both logs included; detailed chat and links at turn end after all commands. No163/merge/deployment authorization.

**Batch162 / unit4 — Broken Clock `C-IIIγ-044`:** [[SE-C-IIIγ-044_Broken_Clock_부서진_시계](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-044_Broken_Clock_%EB%B6%80%EC%84%9C%EC%A7%84_%EC%8B%9C%EA%B3%84.md "SE-C-IIIγ-044_Broken_Clock_부서진_시계.md")]

**What changed:** Ten repairs: extraction’s odd timing no longer declared harmless; resolution distinguishes Ferrehan decrease from Viderehan stable observation. Invalid emotional Work no longer means the object cannot physically react to attack. Inside estimates remain exposure evidence, not authorised time. Corrected observer/object identity and interaction timing claims. No-pattern logging now acknowledges measured Tide association without inventing predictiveclock or expansion. Grade is not a lifetime/recovery certificate; ledger omission in officialservice is notabsenceofrecord. Final failure records actual response rather than auto-gaugerise. General equipment return no longer orders cranial Wheel detachment.

**Evidence/history:** Complete518-line original including census, two judgments and EstablishmentClock. Complete identity-resolved1002A–D, not044Dawn: explicitSourceSECC044WO on all four; Registry170–173/archetype403 versus same-number044Registry86–89/archetype77 and negativecontrol044Asideheader. Mastertable68–70/detail1122–1153; Entity374; fullTale10 536–595; Neutraldisposition308. Current/archivedlogs and prior131unit3 c8dda0e,76unit2 06c5754; read their exactsourcecomparison/holds and current priorindependenttiming/care additions. Batch76unit2 06c5754 already reviewed exactpolearm primary/1002B conflict. Batch131unit3 c8dda0e repeated fullprimary/1002A–D, bothlogs record duplicateWeapon+0 and earlier sourcecredit. No fresh Types or Weapon credit, and no body credit inferred. Five checks PASS; full final reread complete; words8301→8408 (LC_ALL=C). Digits, classification Physical Form and sources preserved. Receipt `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B162_04_BROKEN_CLOCK.md`.

**Holds:** Immovablethree-metre source versus I-Relic mounting/carriedfield remains HELD: no removablecomponent, spatialcoupler or miniaturizedform invented. Four Tooltimedstages/10seconds/30seconds/1minute/2minutes and ten-minute outsidework limit remain independent unreconciled protocols. Wholefieldsevenmetres versus measuredexpandedboundaries and activationexpands-to-seven not normalized; Objecttype preserved. Core75% versus Ultimate65%, baseline45–65, sourceconditionbelow25 and localfourturns need no invented commonthreshold. Physicalclock always3:47testimony versus unpatternedface; Year4231 before elevenyearwatch and loop4222–4223/sources4238 held. Wordcounts are measured fresh, not imported from prior131. PrimaryCudgel11–18/Slow2/OverhandArc/shockwave vs A/B7–12/Fast3/Skewer100–70–50, same135cmbrasspolearmnot evidenceofmultipleforms. ArchetypeRoom versus Medium3; forearmnumbness vs prolongedheaviness/ageing bothremainrecordednotexclusive. Source N/A Work language and outsidecontactresponse are not a license toconfrontobject. Suit1/1/1.5/.5/3/35 and sharedheavycoatappearancesalign; localgroundingunder25Weight not in itemability retainedaslocalnotreplicatedcanon. StigmaHead/4%/+2align but sourceperceptualslow/lifeminutes vs localcrit5%/minor-staggerimmunity/tinnitus notresolved; RegistryAccessory5%/MasterFloatingOrbs versus cranialembeddedWheel unresolved. Shutdownwitnessrelinquishment doesnotcreatecranialremovalprocedure. Duplicationcensus1408acts/1160identical/248different/231adverse, two contraryjudgments and payrollrule remainfull. Identityautobiographicalcorrosion, clinicalage and subjectiveduration are separate; no inventedcompensation/recovery. Neutralinteraction nullresults/limitedTideassociation preserved, not suppressioncredit.

**Commentary:** The horror is that the outside clock is the correct safety instrument and the wrong account of a worker’s life. The revision must preserve both truths: inside estimates cannot run the watch, yet the institution cannot turn that restriction into proof that nobody aged.

**Progress:** OPEN4/5, No change0/4. HELD, Types +0 / Weapon +0 / SE +0; prior coverage is not counted again. Types253/301(84.05%;48remain), Weapon253/287(88.15%;34remain), SE12/301(3.99%;289remain). Both logs included; detailed chat and links at turn end after all commands. No163/merge/deployment authorization.

**Batch162 / unit5 — Redcage `C-IIIγ-120`:** [[SE-C-IIIγ-120_Redcage_분노의_감옥](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-120_Redcage_%EB%B6%84%EB%85%B8%EC%9D%98_%EA%B0%90%EC%98%A5.md "SE-C-IIIγ-120_Redcage_분노의_감옥.md")]

**What changed:** Fourteen repairs: fixed expansion no longer implies travel after activation; removed infallible-protection/never-failed/grade guarantees. SourceI-Relic is explicitly distinguished from released echoes in UseMode, return and OperationalRule: unresolved timedwearer rows no longer authorise wearing the original cage. ThreatAssessment and Entry5 no longer equate recollection with harmlessness or disciplinaryhistory with a legalverdict. Finalfailure now withdraws worker rather than fixedframe. UseNotes separate conditionalpiecebenefits and expectedinjury logging. Weapon release requires knownrecipient/safe route/accountable authority; didnotredesignFang/Censer. A closedexit records failure rather than automatically endedpressure, and routineCharmfollowup cannot delay its actual emergencyclasp/route/partner shutdown.

**Evidence/history:** Whole497-line original including entire409Bars/QuashedIsNotInnocent/ThereAreNoCells appendices. Exact120A–D complete, D65–82care/history/shutdown reopened after combinedoutput truncation. Aside explicitly sourceI-Relic neverworn/issued, echoes not bars; fullAcknowledgeBars/noverdict and OpenBar. B wholeofficialFang/restingactiveversusCenserappearance/saferelease/receiver/authority/oversight/rejection/shutdown; C conditionalone-strike openexit/closedgrid emergency; D singlebarrier/noguilt/unknownfact/oversight/emergency. Mastertable95–97/detail1421–1453; Registry362–365/archetype102; Entity383; fullTale19 1055–1110; Neutraldisposition273. Exact122unit5 5fa0baf/WIP4381–4383 and90unit2 aaf937e1 inbothlogs, cross101 WrathFlame held as differentbetaentity/pair. Batch90unit2 aaf937e1 already reviewed120B/MAW-W-120 and correctedSideWeapontitlewhileholdingFang/Censer. Batch122unit5 5fa0baf completed full120A–D review; repeatedpair+0. Equipmentbaselinealreadyabsorbs these; no freshTypes/Weapon credits. No sharedWrathFlameitem or SEcompletion inferred. Five checks PASS; full final reread complete; words8723→8962 (LC_ALL=C). Digits, classification Physical Form and sources preserved. Receipt `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B162_05_REDCAGE.md`.

**Holds:** Doorless/nohandgap/neverheldbody versus Combatphysicalentry/enclosure/lashing/implosion and stood-inside Testimony remains unresolved. Historicalprisonoccupied versus currentformedObjectempty canbe chronology, not automaticcontradiction; no newprojectedcage or physicalteleport invented. Fixedgrowthandcutmarks preserved, nobodyredesign. Source/tool distinction is now repaired usingAside explicitneverwearsource, but timedharnessrecord10/30/1/2minutes has no exactpieceID or safeapproval; do not silentlymapit toShield. Primaryactivationtouch/open versus proximitypressure/hostileargument; 75% core/65% Ultimate versus threshold25 remains. No removalofsource, portablecage or sourceextractedfragments invented. Censerprimary/Bheading/Appearance/Registry/archetype versus BOfficialFang/restingactive/attack/history/MasterEntry55 remainsheld; nocensertofangstate invented. B/Astats7–12/Fast3/Medium3/Skewer100–70–50/3/40align, artClose vs combatMedium remains. WrathFlamebeta/Single samecenserproseis distinctentity1012set, notshareditem. Localstoresteamvs releasedecho, directdamagevslocalTick noextra warranty inferred. Shieldsharedharness/gap/exitright/one-strikereflection and1/.4/1.8/1.2/3/35align; primarynotchtightening underargument isnot sourceconfirmed. CharmTail4%+2 unnamedsourcecheck aligns but sourcechestbarredwindow/twobarsbright/unknownfactcooling vs primaryheavyiron/grievanceescrow/unrequestedbestowal unreconciled. No legalinnocence oracle; RegistryAccessory5%/MasterHauberk bucket versus physicalharness retained. Freshinjusticebarcount cannot identifycase/person/date, even with IronJudgecompletecourtfile. SourceViderehanreveals eachbar versus institutionalnonecanbe matched remainsheld. AngryMaiden pulse/temperature change withoutcount means sharedseries cannotattesteffect fromcountalone. Count409/361 versus37quashed/3paid/34uncompensated, detentionabsence/two-kilometre/forty-minute harm preservedwhole; no compensatedvictimorcountcontraction invented.

**Commentary:** The count can show that injustice continues without identifying whom the institution should repair it for. Closing the cells is a real sacrifice with real casualties, not a clean moral victory. The equipment must leave someone a safe way out; otherwise the cure becomes another bar.

**Progress:** OPEN5/5, No change0/5. HELD, Types +0 / Weapon +0 / SE +0; prior coverage is not counted again. Types253/301(84.05%;48remain), Weapon253/287(88.15%;34remain), SE12/301(3.99%;289remain). Both logs included; detailed chat and links at turn end after all commands. No163/merge/deployment authorization.

**Batch162 closure (2026-10-21): CLOSED5/5; No change0/5.** All five complete written-design reviews remain HELD; 50 supported repairs, 40449→41353 words (+904; LC_ALL=C wc -w). Whole originals/exact sources/history/finals read;25 fresh closure validators,10 ledger tests, archive/timeline/seam/symmetry PASS. Comparator557 candidates unchanged from161 after stripping locations only. Digits/all301 PhysicalForm rows/all296 unselected/exact sources preserved. GuardingBird alone adds+1Types/+1Weapon; four prior exact reviews add0. SE+0. Types253/301(84.05%;48remain), Weapon253/287(88.15%;34remain), SE12/301(3.99%;289remain); states8changed/4retained/77held/2blocked/210pending. Both logs are in all five verified individual pushes and this closure. Full changes, Commentary, holds and links: `SE_APPEARANCE_REVIEWS/B162_CLOSE.md` (machine evidence .json); entire substantive chat report follows final command under R31points21–22. GuardingBird universalcannot-be-relieved line explicitly backlogged. DraftPR14 OPEN/NON-WIKI/ownermerge; no163/artwork/browser/deployment authorization; Batch301 still ownerblocked eightbodies/one4+4/generatevalidatebeforecopy.

**Batch163 opening (2026-10-21): OPEN0/5.** Owner p after162 verifiedccc141c authorizes163 only. Fresh pending-only source-cue screen: 210pending/57candidates. Frozen order C-IIIγ-145, C-IIIγ-190, C-IIIγ-248, C-IIIγ-649, C-IIIγ-891. Five completed whole-document reviews minimum; cumulative3Nochange triggers5→7→10; pending≠Nochange. R33 actual originals/sources/history/finals; supported improvements, separate holds and no invented forms. Per-unit bothlogs/validators/gate/push; entire substantive report and links at end under R31. Types253/301(84.05%;48remain), Weapon253/287(88.15%;34remain), SE12/301(3.99%;289remain). States8changed/4retained/77held/2blocked/210pending. No164/merge/artwork/deployment authorization. Batch301 remains ownerblocked on8bodies/one4+4/generatevalidatebeforecopy.

**Batch163 / unit1 — Briar `C-IIIγ-145`:** [[SE-C-IIIγ-145_Briar_가시의_정원](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-145_Briar_%EA%B0%80%EC%8B%9C%EC%9D%98_%EC%A0%95%EC%9B%90.md "SE-C-IIIγ-145_Briar_가시의_정원.md")]

**What changed:** Thirteen repairs: concrete movement and non-fixed-device speed; valid Work distinguishes primary permissions from prohibited Pugnahan. Breach quote now matches motion-tracking. Equipment consequence and Use Notes preserve safe-person boundaries, piece-specific tolls and conditional Named Thorn without inventing source-form transitions. All four Field Use stages separate costs and immediate/later review. First-contact and Warden approach no longer imply the marked fence is beyond reach. Final failure preserves evidence rather than claiming universal revelation then no record.

**Evidence/history:** Complete496-line original, all exact145A–D including B reopened after truncation and completeC/D care/shutdown. Mastertable101–103/detail1488–1538; fullTale21 1169–1228; Entity385; Registry390–393/archetype109/disposition282. B105unit5 5db41e1b/B79unit2 1acf773d and bothlogs exact comparison read; prior full-source annotation retained. Subject/Place mobile thicket, entire dedication/quorum/fence-in-reach and count appendices read. B105unit5 already full145A–D review; B79unit2 exactWeaponpair source disposition. No fresh equipment credit or legacy body backfill. Five checks PASS; full final reread complete; words7915→8207 (LC_ALL=C). Digits, classification Physical Form and sources preserved. Receipt `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B163_01_BRIAR.md`.

**Holds:** Primary Subject and Place-Grudge versus exactA management invalidFlerehan/Pugnahan; do not silently change classification. No-breach-counter overview versus escape, no-vessel Place versus mobilebody and Tale does-not-attack versus combat remain. Core75/Ultimate65, pressure15–34 vs Aside18–41 and off-groundescape timing held. Rifle105cm/Range4/7–12 vs item coreRange3 and primaryAddendum/Master11–17/Normal3; Fangresting/defensivebarrier versus riflewinch has no mapping. Hauberk wiremail versus C plateharness; Master resistances differ. Coronet localcompleteimmunity versus active thornboundary, SideTail versus HeadBrow and Registry5% vs4%; sourcegrantcondition versus local threegrippedworkers held. Local no-extraction restriction versus A/B natural-shed echo extraction is recorded distinctly, not overwritten. ZoneB Tale versus ZoneD actualground and fixedmemorial vs mobileescape chronology require evidence. 1406blooms/31initial/58correlations/31unmatched; quorum5/threealive and fenceinjury history allpreserved. Names and case-matching authority cannot be invented.

**Commentary:** The dedication protected mourners from having their memorial cleared for convenience. It now leaves living workers inside the reach, even though the surviving committee would release the promise if it could. That is more compelling than a merely angry hedge: care becomes dangerous when nobody can revise its terms.

**Progress:** OPEN1/5, No change0/1. HELD, Types +0 / Weapon +0 / SE +0; prior coverage is not counted again. Types253/301(84.05%;48remain), Weapon253/287(88.15%;34remain), SE12/301(3.99%;289remain). Both logs included; detailed chat and links at turn end after all commands. No164/merge/deployment authorization.

**Batch163 / unit2 — The Rage Statue `C-IIIγ-190`:** [[SE-C-IIIγ-190_The_Rage_Statue_분노의_조각상](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-190_The_Rage_Statue_%EB%B6%84%EB%85%B8%EC%9D%98_%EC%A1%B0%EA%B0%81%EC%83%81.md "SE-C-IIIγ-190_The_Rage_Statue_분노의_조각상.md")]

**What changed:** Ten repairs: finished truncated classification trigger; movement distinguishes found posture changes and expandingzone from locomotion. Valid Work and operational summary no longer offer prohibitedPugnahan. StoryEntry immobility and Resolution no longer erase posturechanges. Finalfailure retains true-but-irrelevant naming and actual readings instead of automaticrise. Flavor no longer guarantees blowcanneverland. Corrected ThreatAssessment grammar. AfterUse adds actualcurrent-remedy care and witnesscovering without inventing removal of fusedKnuckle or palmseam on anapron.

**Evidence/history:** Whole468-line original including3188petitions, ReceivedAndOwedNothing and emergencydecision fiction. Complete190A–D including C Gauntlet/palmseam and Dfused-knuckle covering; Mastertable107–109/detail1573–1606, Entity387/fullTale23 1285–1346, Registry466–469/archetype133/Neutral294. Both currentlogs prior118unit2 sourceinventory,77–78identity correction and fullitemprofile hold read. Exact190notEmberPhoenix1019 despite W190Culverin alias. Prior118unit2 fullprimary/190A–D and prior77–78 exactWeaponpair already credited. No newTypes/Weapon/SEcredit; preserve existing118 piece-specific notes and profileholds. Five checks PASS; full final reread complete; words7476→7611 (LC_ALL=C). Digits, classification Physical Form and sources preserved. Receipt `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B163_02_RAGE_STATUE.md`.

**Holds:** Colossalcurrentfigure versus person-sizedcourtyardTale has no datedgrowth/relocationaccount. No-witnessedmovement versus visiblyloweringFlerehan and forty-one posturechanges; blowneverlands versus StoneFist/BurstingForth remainsheld. Speed1.95m/s notproof oflocomotion; count2/core75/ultimate65/event55 unnormalized. Exact190Brand vs Registry/W190Culverin and oldPersonalizationjavelin; same120cmMarbleBrand primary12–19/Slow2/Short2/crushstarburst versus item7–12/Fast3/Medium3/Skewer remains. No formorstat crosswalkinvented. CGuantlet/palmseam history vs apron/cuirass actualappearance and MasterMantles bucket; Hand/Knuckles vs AsideTail/RegistryAccessory5% vs4%; localunarmedgripability primary-only. Naminglist3188 and truewrongnotrelevantwrong retained. Emergencydecision-deemedabsent/rule stillstands with harm and draftedbutunlaidexception; no clinicalpermission or compensationinvented. Fourcorruptionevents remainnonbreach despite Neutralindex saying breaches.

**Commentary:** Being received is not being answered. The strongest parallel is the Warden whose correct rescue becomes no decision at all: another person does everything right and still cannot obtain a usable record of it. I would preserve that cruelty rather than make the Statue merely an anger aura.

**Progress:** OPEN2/5, No change0/2. HELD, Types +0 / Weapon +0 / SE +0; prior coverage is not counted again. Types253/301(84.05%;48remain), Weapon253/287(88.15%;34remain), SE12/301(3.99%;289remain). Both logs included; detailed chat and links at turn end after all commands. No164/merge/deployment authorization.

**Batch163 / unit3 — The Unconsoled `C-IIIγ-248`:** [[SE-C-IIIγ-248_The_Unconsoled_위로받지_못한_자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-C-III%CE%B3-248_The_Unconsoled_%EC%9C%84%EB%A1%9C%EB%B0%9B%EC%A7%80_%EB%AA%BB%ED%95%9C_%EC%9E%90.md "SE-C-IIIγ-248_The_Unconsoled_위로받지_못한_자.md")]

**What changed:** Seventeen repairs: drift/eventradius movement, exactgradedset, Workpermission/no Pugtest. Frequencycap no longcycle-safety warranty; removed no-harmworstcase. Concrete identification and appearanceprotocol distinguish measuredsound/personalmemory, drift and damp. Event no-damage no longer means no changes. Equipmentnotes distinguish piececosts/conditionalfullset from invulnerability; During/AtLimit/After include sourcecorrosion, exact shutdown and maintenance without waiting irreversibleendpoint. Grade no longer certifies perpetualstability. Observation and twointeraction summaries preserve Bellmeasuredexception rather than universalnull. Firstcontact datesvisibleelderafterHand while foundationgrief remainsancient.

**Evidence/history:** Whole373-line original in order; all exactUNK-248A–D full including fullsourceblocks, RootVault/BentRecorder/SharedMorning, corrosion, maintenance, shutdown/removal. Side explicitC-IIIγ-248 resolves Unknownalias. Registry1143–1146, Entity641, Neutral354; exact fullMaster M.A.W./Tales searches found no matching248 entry; no matching archetype row. Current/archivedbothlogs fullidentity/itempair search: R28 5fb6ede, R29condition659d753,57-subprosecleanup are not equipmentreview. Currentledger has no248 equipment review. No accessible659d753 gitobject: rely on survivinglogs, not pretendshow. Fresh exact248A–D and MAW-W-UNK-248-01 comparison; no prior full-set or Weapon comparison found in all current/archivedlogs or durable equipment ledger. PriorR28/reclassification, R29condition and prose/disposition only. +1Types/+1Weapon; zeroSE completion. Five checks PASS; full final reread complete; words6208→6499 (LC_ALL=C). Digits, classification Physical Form and sources preserved. Receipt `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B163_03_UNCONSOLED.md`.

**Holds:** Organichalf-flesh/light elder vs pale-blueHancrystal; silentweeping/nooutwardviolence vsKeeningheardattack, RejectedComforttriggerFlerehan and BottomlessGriefcompulsion. No-Pugattempt vsdescriptive forcedFounderMemory and comfortonlyinputraises vsPugraises remain. Speed0.6m/s versus9metres/4yearsdrift; count2/core70/Ultimate65 and event starts58floor→near80 remainsunresolved, no numbersnormalized. Aside copied canonicalsourceTransform/35%otherresistance vs primarynonbreachingCorrupt/untestedotherpressure. Primary wholequarterstillstops/expands notemptyharmless. Hand row unchangedweeping vshopecontrastdistress, annualConsolihan audibleTrivia vs alwayssilent baseline and annualmanifestationtimingheld. Historicalambientgrief→visibleelder allowed withoutinventingearlierface; permanentno-lookup remainsstatementnotproof. Primary permanentunconsolablechosenloss perallthree vs exactsourcepermanentthread and individualdifferentcosts; no invulnerabilitysupported. Sidefullset onecyclehalveburden vs Tearhalvingduration unspecified. Localnonrandomnewlossissuance vs Side/Item4%/Registry5%; source-work+2Composure notuniversalcombat. Entry4 prohibits extraction vslater supervisedoverrulings (no permissionchanged). Weaponprimarynonumericprofile vs exactB7–12/2/2Single3/40 and sourceonlysupport/maintenance remain distinct, notbackfilled. RegistryUNK248 exactC-IIIγ248 matchread; noMasterM.A.W./Tale counterpart or archetypefound, so nonefabricated. Neutralindex nooutwardeffect/worstcase premise nowneedsseparatereview; dispositionindex notsilentlychanged.

**Commentary:** The grief predates the visible elder: hope did not turn a person into a statue, it exposed what the city had always been standing on. The troubling choice is treating that newly visible sorrow as reliable baseload and charging each bearer a permanent loss of comfort. Sharing can help without making extraction morally resolved.

**Progress:** OPEN3/5, No change0/3. HELD, Types +1 / Weapon +1 / SE +0. Types254/301(84.39%;47remain), Weapon254/287(88.50%;33remain), SE12/301(3.99%;289remain). Both logs included; detailed chat and links at turn end after all commands. No164/merge/deployment authorization.

**Batch163 / unit4 — Sunken Pillar `C-IIIγ-649`:** [[SE-C-IIIγ-649_Sunken_Pillar_가라앉은_기둥](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-649_Sunken_Pillar_%EA%B0%80%EB%9D%BC%EC%95%89%EC%9D%80_%EA%B8%B0%EB%91%A5.md "SE-C-IIIγ-649_Sunken_Pillar_가라앉은_기둥.md")]

**What changed:** Fourteen repairs: removed fixeddeviceSpeed; approvedcycle no longer denies physicalsinking; position no longer onlyvariable. Ringmapping not requiredwalkingonassumedmarker. Localabandonedplans not universalequipmentcost. UseNotes distinguishes sourcedformation from localdeniedextraction and removes gradestability warranty. All four FieldUse stages now piece-specific baseline/corrosion/shutdown/care, fullset conditional mourning and immediateplusweekreview. Statinterpretation no stabilitywarranty. StoryEntry5 title matches subscription rather than straySoldier. Finalfailure no longer labelsViderehanvisions automaticfailure or inventsretreat.

**Evidence/history:** Complete460-line original including1744frames/219falsepositiveflags, resultingtrust for94closedestates and withheld mobileexclusion projection. Exact649A–D complete including extendedAppearance/incident/corrosion/maintenance/shutdown. Master128–130/details1804–1835, Entity394, fullTale30 1689–1750, Registry795–798, archetype264/306, Neutral293. Bothlogs B110case3 33ef200 sourceinventory/countercorrection read. TailTale separately reopened after combinedoutput truncation. B110originalcase3 33ef200 already exactfullset and first649Weaponpair MAW-W-649-01. Its valid source-ledannotation remains. No repeatTypes/Weaponcredit, no bodybackfill. Five checks PASS; full final reread complete; words7630→7855 (LC_ALL=C). Digits, classification Physical Form and sources preserved. Receipt `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B163_04_SUNKEN_PILLAR.md`.

**Holds:** Physicalhalfburied versus Taleonlycapital versus buriedlengthseveraltimesvisible; no confirmedtotalheight. Validonlyobservation/endurance versus physicalstrike/topple/undermine combat; those conditions arenotauthorizations. Core75/Ultimate65 and ordinary180mseason/max310mseason vs ringradius400m separateunsettledmodels. Continuoussinking/capitalblankhistoricaltiming and twoapparitions versus noevent origin remain. ExactSide UnbornMonument joinsbydesignation; externalformation/exactitems versus localneverextractionauthorised unresolved withoutinventedgrantor/laterpermission. ItemRange3 versusarchetypeClose; sourceSkewer/falloffnotbackfilled; Head4% vs Registry5%Accessory. Suitglasscolumnhollowbase/bodyrelationship vs genericMasterouterweartaxonomy; no manufacturingproof. SideUninscribedFuture eachbearerlosessmallmemory underfullset vs itemBnameless/Cfutures/Dword kept distinct; primarywordcostoccasional versus Dsmallconstant timingheld. LocalCharm2conferrals/conditionaltensedebrief vs sourceacceptedwork4%, localproximitycold notguaranteedsafering. Bwidthofchildhoodlabel erasedrealreadingmemory; attributiondoesnotrestoreit. Sourceexactthreecyclesseal/three-marker countnotaddedasnewprimarynumbers. 1744frames/twocertainalterations/thirdunresolved6years/219differenceflags preserved; twocasecorrelationnottrend. Resultingtrust94closedestates/moneyunusable and mobileexclusioncrossesclaim/licence/route remain. Trackpublicationblocked not magicallyimplemented; no newcompensation or safecrossing asserted.

**Commentary:** A fund for unborn descendants and an exclusion that arrives on living people’s working ground are two versions of the same mistake: treating a future entitlement as if it already had a claimant, while refusing the people who actually have to live with it. The two certainties and one honest photographic disagreement are worth preserving, not automating into a verdict.

**Progress:** OPEN4/5, No change0/4. HELD, Types +0 / Weapon +0 / SE +0; prior coverage is not counted again. Types254/301(84.39%;47remain), Weapon254/287(88.50%;33remain), SE12/301(3.99%;289remain). Both logs included; detailed chat and links at turn end after all commands. No164/merge/deployment authorization.

**Batch163 / unit5 — Screaming Masonry `C-IIIγ-891`:** [[SE-C-IIIγ-891_Screaming_Masonry_스며든_절규](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-891_Screaming_Masonry_%EC%8A%A4%EB%A9%B0%EB%93%A0_%EC%A0%88%EA%B7%9C.md "SE-C-IIIγ-891_Screaming_Masonry_스며든_절규.md")]

**What changed:** Fourteen repairs: completed truncatednonbreachclassification; mobileSpeed notfixeddevice. Consequence and Statinterpretation separate originalI-Relicwearclock from eachδM.A.W.cost. UseMode no forbiddenmounting and notesundocumentedfit; activationbonus nowrequiresactualwear, notposting. Maul/UseNotes nofalseaudibility or gradinginference; localgrievancecompulsion notsourceuniversalcost. Mantlefatigue nolongerdenied byitsowncostparagraph. UseNotes separateswelfare/localcompulsion/autobiographicalcorrosion; AtLimit firstsourcefailure notwaitforcompulsion orignorewearclock. ThreatAssessment nozero-injurywarranty contradictedbyweartrauma. Flavor matches recordedinaudibility.

**Evidence/history:** Complete497-line original including allI-Relicwearingtimings and transcripts1906/1788/23matches/nilcertificates6/fourconsultationcorpus overlap. All891A–D complete, extendedAppearance/binding/history/corrosion/care/shutdown/set end. Master131–133/details1837–1869; Entity395/fullTale31 1746–1805; Registry947–950/Neutral313; exactarchetype searchnone891. Prior123unit1 7ccf204 bothlogs fullrepair/evidence/heldinventory read; B66effab0e isprosecleanup notfreshcredit. B123unit1 7ccf204 alreadyfull891A–D and newexactMAW-W-891-01. No additional Types/Weaponcredit; preserve sourcedδgrade/attribution/binding/ladders/witnessclosure. B66cleanup notseparatecoverage. Five checks PASS; full final reread complete; words8291→8436 (LC_ALL=C). Digits, classification Physical Form and sources preserved. Receipt `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B163_05_SCREAMING_MASONRY.md`.

**Holds:** Driftinguntouchedcompressed-airshard vs directpersonalwear/detachment/mountfit undocumented; sourceA saysTransformbreach versus localactivation/absorption. Object-Lament Weight [D] vs MasterTale[WO], Bodygrant/Toolclassnotnormalized. No-bearingambientfield vs mappedbearing; audiblecombat/Tale/Testimony versus current4microphonequiet/silenttranscript needchronology notsilentlynewphase. Timedwear10s/30s/1m/2m/5Weight15s vs unspecifiedsaferemovalcondition and no observedshardtouched remainheld. Neverinjuredbaseline nowqualifiesrisks but directattack descriptionsstillunsettled. Core75 vs Ultimate65 and originalI-Relic+3 vs HeadRing+3 require separation; no doubledbonus or unnamedstatfilledin. δMaul physicaltwo-handhead versus Skewer/linepiercing and direct/TicknoTickduration; progressiveagingnotclinicalgradefact. Mantlefatigue loggednevertreated and cyclecontraction notsourceguarantee; δ sourcesnotpromotedtoγ. Ringsteelring Headslot vs Masterhandseal, generic5% vs4%; steadyunbandedsternum versus forensicliebenefitnotresolvedaslie-meter. Localninebestowals/transcriptconditions vssource4% remain. Namedwitnessclosure preservesrecord/nocostrefund, nottoolwearremovalprocedure. SourceMAWcare attribution beforeclean/rest retained. 1900summaryline vs1906corpus/1788wellfounded/23lodgedmatches heldwithoutnormalizingdigits. Sixnil-objectioncertificates/fourwithunlodgedconsultationutterances/31northstair/zero-costinstructionnotlaid preserved; no newpublicrepresentationpolicy.

**Commentary:** The facility is not merely missing a complaint: it can read the very words that the district withheld, then certifies silence using a procedure that is formally correct. The floating silent scream works because the failure is in transmission and reception, not because residents needed louder voices. Keep the unlaid, costless instruction and the accurate certificates together.

**Progress:** OPEN5/5, No change0/5. HELD, Types +0 / Weapon +0 / SE +0; prior coverage is not counted again. Types254/301(84.39%;47remain), Weapon254/287(88.50%;33remain), SE12/301(3.99%;289remain). Both logs included; detailed chat and links at turn end after all commands. No164/merge/deployment authorization.

**Batch163 closure (2026-10-21): CLOSED5/5; No change0/5.** Fresh210pending/57source-cue screen; frozen145/190/248/649/891 complete. Allfive whole designs HELD;68supportedrepairs, 37520→38608words (+1088; LC_ALL=C). Originals/exactsources/history/wholefinals read;25freshclosurevalidators,10ledgertests,archivecomponents/timeline/seam/symmetry PASS. Comparator557candidates unchanged162 after stripping rowlocations only. Digits/all301PhysicalForms/all296unselected/exactsources preserved. Unconsoled alone fresh+1Types/+1Weapon; allothersexistingcoverage. SE+0. Types254/301(84.39%;47remain), Weapon254/287(88.50%;33remain), SE12/301(3.99%;289remain); states8changed/4retained/82held/2blocked/205pending. Bothlogs in allfiveverifiedpushes andthisclosure. Fullchanges/Commentary/holds/links/backlog `SE_APPEARANCE_REVIEWS/B163_CLOSE.md`(.json machineevidence). Allsubstantivechat/links afterfinalcommand underR31. Remaining unqualifiedwording, Unconsoleddispositionindexpremise and Sunkenwalkingring explicitlybacklogged, not silentlycertified. DraftPR14OPEN/NON-WIKI/ownermerge; no164/art/browser/deployment. Batch301ownerblocked eightbodies/one4+4/generatevalidatebeforecopy.

## Batch164 — OPEN 0 / 5

Owner's research-first P and latest continuation authorize this batch. Fresh pending-only ranking:205eligible,52source-cue candidates; frozen order916DevouringBloom,948FoamFlood,C-IIα081BrokenMirror,055WeepingStatue,099MaskedDancer. See [opening evidence](SE_APPEARANCE_REVIEWS/B164_OPEN.json). No review or No change is credited at opening. Apply donor/state/equipment distinctions from the research note. Minimum five reviews and cumulative three-No-change ladder remain. Owner explicitly permits a later full recheck/fix after this pass finishes; unresolved issues remain visible rather than being silently cleared. No Batch165 authorization or automatic old credit follows.

### Batch164 unit1 — OPEN 1 / 5

[Devouring Bloom evidence](SE_APPEARANCE_REVIEWS/B164_01_DEVOURING_BLOOM.md):18supported repairs, allfive checks PASS/fullfinal reread, HELD/no bodycredit. Donor-to-equipment differences are not held by themselves; real source Work/threat conflicts remain. Prior116 exact equipment comparison adds no duplicate credit. No change0/1;948FoamFlood/C-IIα081BrokenMirror/055WeepingStatue/099MaskedDancer remain pending. Owner-approved later full recheck retains the issues; no early close or new batch. All three cumulative counters unchanged.

### Batch164 unit2 — OPEN 2 / 5

[The Foam Flood evidence](SE_APPEARANCE_REVIEWS/B164_02_FOAM_FLOOD.md):12repairs, five checks PASS/fullfinalreread; HELD, no duplicate equipment or body credit. No change0/2; cumulative counters unchanged. Five completed reviews required; later full recheck issues remain visible.

### Batch164 unit3 — OPEN 3 / 5

[Broken Mirror evidence](SE_APPEARANCE_REVIEWS/B164_03_BROKEN_MIRROR.md):6repairs, five checks PASS/fullfinalreread; HELD, no duplicate equipment or body credit. No change0/3; Types255/301, Weapon255/287, SE12/301. Independent fresh equipment credits follow the evidence history; no duplicate or retrospective claim. Five completed reviews required; later full recheck issues remain visible.

### Batch164 unit4 — OPEN 4 / 5

[Weeping Statue evidence](SE_APPEARANCE_REVIEWS/B164_04_WEEPING_STATUE.md):6repairs, five checks PASS/fullfinalreread; HELD, no duplicate equipment or body credit. No change0/4; Types255/301, Weapon255/287, SE12/301. Independent fresh equipment credits follow the evidence history; no duplicate or retrospective claim. Five completed reviews required; later full recheck issues remain visible.

### Batch164 unit5 — OPEN 5 / 5

[The Masked Dancer evidence](SE_APPEARANCE_REVIEWS/B164_05_MASKED_DANCER.md):24repairs, five checks PASS/fullfinalreread; CHANGED, no duplicate equipment or body credit. No change0/5; Types255/301, Weapon255/287, SE13/301. Independent fresh equipment credits follow the evidence history; no duplicate or retrospective claim. Five completed reviews required; later full recheck issues remain visible.

## Batch164 — CLOSED 5 / 5

## Batch164 closure — CLOSED 5 / 5 (2026-10-21)

All five frozen dossier reviews are complete. 66 supported repairs; four whole-design holds and one new written-design completion (Masked Dancer). No change **0 / 5**; no earned seven/ten rung. The owner's latest “always 5 per batch” is satisfied by completed reviews, not by pending names or one-unit checkpoints. No Batch165 authorized.

## Individual deliveries

Each row is one complete review, not a substituted batch.

| Entity | Repairs | Logical result | Checks | Commit / push |
|---|---:|---|---|---|
| [Devouring_Bloom](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-916_Devouring_Bloom_%EC%8A%A4%EB%A9%B0%EB%93%A0_%EA%BD%83.md "SE-C-IIIγ-916_Devouring_Bloom_스며든_꽃.md") `C-IIIγ-916` | 18 | HELD | Five PASS | `528a7e64` PUSH VERIFIED |
| [Foam_Flood](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-948_Foam_Flood.md "SE-C-IIIγ-948_Foam_Flood.md") `C-IIIγ-948` | 12 | HELD | Five PASS | `eeb162d7` PUSH VERIFIED |
| [Broken_Mirror](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B1-081_Broken_Mirror_%EA%B1%B0%EC%9A%B8%EC%9D%98_%EC%A1%B0%EA%B0%81.md "SE-C-IIα-081_Broken_Mirror_거울의_조각.md") `C-IIα-081` | 6 | HELD | Five PASS | `e654a2be` PUSH VERIFIED |
| [Weeping_Statue](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-055_Weeping_Statue_%EC%9A%B0%EB%8A%94_%EC%A1%B0%EC%83%81.md "SE-C-IIβ-055_Weeping_Statue_우는_조상.md") `C-IIβ-055` | 6 | HELD | Five PASS | `bff4f407` PUSH VERIFIED |
| [The_Masked_Dancer](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-099_The_Masked_Dancer_%EA%B0%80%EB%A9%B4_%EB%AC%B4%EC%9A%A9%EC%88%98.md "SE-C-IIβ-099_The_Masked_Dancer_가면_무용수.md") `C-IIβ-099` | 24 | CHANGED | Five PASS | `0b3eda05` PUSH VERIFIED |


### Counters and exclusions

Each row is a separate per-SE measure.

| Workstream | Coverage | Percent | Remaining |
|---|---:|---:|---:|
| ALL M.A.W. Types Appearance per SE — source-review coverage | 255 / 301 | 84.72% | 46 / 301 |
| ALL M.A.W.-W Appearance per SE — source-review coverage | 255 / 287 | 88.85% | 32 / 287 |
| SE Appearance Fix — independent written-design pass | 16 / 301 | 5.32% | 285 / 301 |

Equipment coverage includes source holds; it is not finished artwork or redesigned-set coverage. Broken Mirror's identity-resolved SE1009 set is newly reviewed, so both equipment streams gain one. Numeric081 is Hollow Saint, a different full identity; its older review cannot be borrowed. The other four sets were already covered and gain zero. Only Masked Dancer gains a fresh independent written-design completion. Its same-item equipment holds are not resolved by that body credit. The other four remain HELD for actual source/body/action issues, not a demand that every derived item have the donor's silhouette.

Corpus states: 9 changed, 4 retained, 86 held, 2 blocked, 200 pending = 301. Silent Child and scope-unconfirmed Inheritor stay blocked, no legacy body backfill, no repeat Weapon credit. Research examples earn no body/art credit.

### Validation and preservation

- 66 supported replacements across five primaries. LC_ALL=C wc -w: 40,296 → 42,351.
- Fresh closure checks: verify (residue, seams, pipes, duplicates), tpl (repeated-template residue), sectfile (per-section prose overlap), wikistd (dossier completeness) and sect (whole-file shared-prose fraction): **25 / 25 PASS**.
- Whole original and final primary readings are recorded. Each full final was read after its actual validators; current final fingerprints still match. This is a substantive logical review, not a PASS inferred from booleans.
- Every exact source fingerprint remains unchanged. All 296 unselected primaries are unchanged from opening base. All 300 other classification Physical Form rows are unchanged. Masked Dancer alone has a scoped body-summary qualification for documented pauses; no type, manifestation, material, anatomy, numeric stat, range or timing is invented.
- Each unit updated WIP and CHANGELOG and travelled in its own gate/verified push. Closure carries both logs again. Evidence JSON retains all raw fresh-check outputs, source hashes, commits and local word counts.
- Written-design inspection only. No generated/rendered artwork, browser, running preview, published-site verification or deployment is claimed.

### Next and blockers

Wait for the owner's next batch authorization. Batch165 is not opened. Preserve the later full recheck/fix backlog, including all held relationships, same-item equipment conflicts and historical chronology questions.

The owner controls merging. No merge or pull-request closure is authorized here. Batch301 remains separately blocked pending eight owner-supplied bodies, one4+4 operation, and generation/validation before wiki copy. No owner file or patch upload was deleted, replaced or moved. The removed maw_slotcheck tool stays removed.

Detailed content, individual Commentary and full primary/evidence links: `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B164_CLOSE.md`; raw fresh checks and preserved hashes: `B164_CLOSE.json`. Each individual receipt remains linked there. Closure checkpoint supersedes earlier OPEN164 unit snapshots without rewriting their history.

## Batch165 opening — OPEN 0 / 5

Owner p after CLOSED164 authorizes this next batch only; always five minimum, cumulative three No change triggers5→7→10; later full recheck/fix permission retained.

Fresh pending-only shortest-first whole-dossier cohort across both canonical wings; full designation tie-break. The previous became-a cue screen mostly flags narrative or administrative metaphors, not actual form transitions. Length selects manageable full reviews, not defects or predetermined changes. Includes Unknown entities in the fixed301 denominator. No old-held files selected.

Frozen queue:
1. `O-IIIγ-1052` — `SOMNARAK-WORLD/Unknown_Entities/SE-O-IIIγ-1052_The_Glass_Silt_Drifter_유리모래_방랑자.md`
2. `O-IVγ-1053` — `SOMNARAK-WORLD/Unknown_Entities/SE-O-IVγ-1053_The_Singing_Needle_노래하는_바늘.md`
3. `N-Vω-1055` — `SOMNARAK-WORLD/Unknown_Entities/SE-N-Vω-1055_The_Ancestral_Guilt_조상의_원죄.md`
4. `N-IIIβ-1056` — `SOMNARAK-WORLD/Unknown_Entities/SE-N-IIIβ-1056_The_Unbroken_Pledge_깨어지지_않은_서약.md`
5. `C-IIγ-071c` — `SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-071c_Apostle_Maker_사도_만드는_자.md`

All five are pending, not No change. Complete original/exact-source/history and final reading after five actual validators; separate Commentary, both logs, individual gate and verified push. No owner bodies fabricated; Batch301 eight-body/one4+4/generatevalidatebeforecopy block and owner-controlled merge unchanged. No166 authorization. Opening changes no equipment/body credits:255/301 Types,255/287Weapon,13/301SE.

### Batch165 unit1 — OPEN1/5

[The Glass Silt Drifter evidence](SE_APPEARANCE_REVIEWS/B165_01_GLASS_SILT_DRIFTER.md): HELD, 3repairs, five checks and complete final read. No change0/1; source-review counters255/301and255/287, independentSE13/301. Pending is not No change; later full recheck retained.

### Batch165 unit2 — OPEN2/5

[The Singing Needle evidence](SE_APPEARANCE_REVIEWS/B165_02_SINGING_NEEDLE.md): CHANGED, 4repairs, five checks and complete final read. No change0/2; source-review counters255/301and255/287, independentSE14/301. Pending is not No change; later full recheck retained.

### Batch165 unit3 — OPEN3/5

[The Ancestral Guilt evidence](SE_APPEARANCE_REVIEWS/B165_03_ANCESTRAL_GUILT.md): CHANGED, 4repairs, five checks and complete final read. No change0/3; source-review counters255/301and255/287, independentSE15/301. Pending is not No change; later full recheck retained.

### Batch165 unit4 — OPEN4/5

[The Unbroken Pledge evidence](SE_APPEARANCE_REVIEWS/B165_04_UNBROKEN_PLEDGE.md): CHANGED, 5repairs, five checks and complete final read. No change0/4; source-review counters255/301and255/287, independentSE16/301. Pending is not No change; later full recheck retained.

### Batch165 unit5 — OPEN5/5

[Apostle Maker evidence](SE_APPEARANCE_REVIEWS/B165_05_APOSTLE_MAKER.md): HELD, 4repairs, five checks and complete final read. No change0/5; source-review counters255/301and255/287, independentSE16/301. Pending is not No change; later full recheck retained.

## Batch165 CLOSED — five complete reviews, three written-design completions

**Result:** CLOSED 5 / 5. All five original dossiers and complete final versions were read, validated and individually pushed. There are three CHANGED designs and two HELD designs. No change is 0 / 5. This is a written-design review, not an artwork or deployment completion.

The five-review minimum is met. The cumulative three-No-change trigger is not met. All five have substantial interaction and narrative records, so the older simple-cohort test does not justify expansion. No Batch166, merge, deployment or new artwork is authorized.

### Changes and individual Commentary

#### 1. The Glass Silt Drifter — `O-IIIγ-1052`

Three repairs add an Appearance section separating slag biped, courier origin, shed fragments, mirror images and shell-derived equipment. Recommended response now preserves the standing non-engagement order rather than endorsing carapace shattering. Recovered black pebbles no longer imply that live impact-active shards are harmless.

**Final logical result:** HELD: the nonhuman construct design itself is supported and its field/images/equipment are distinguished, but physical pursuit/ramming and safe response remain mutually unqualified. No appearance credit until that action relationship is supported.

**Holds and later recheck:**

- No off-glass sighting and matching-speed escort account versus sand-speed and direct ramming/charging record need actual conditions, not a fabricated state.
- Non-engagement/throttle-only convoy order versus recommended shattering and mandatory nitrogen boarding response lack an authority crosswalk; hardware recovery is not engagement permission.
- Needle overlap is two observations, not proof that its acoustic song repels the Drifter. Pieces remain primary-only; no exact external Weapon pair or missing Stigma inferred.

**Commentary:** The sealed cylinders give this creature a purpose without making its body a literal messenger. I like that the caravans protect both the road and the unread messages. A bounty for fragments would erase that distinction, so the no-bounty order matters.

**Evidence and individual push:** [B165_01_GLASS_SILT_DRIFTER.md](SE_APPEARANCE_REVIEWS/B165_01_GLASS_SILT_DRIFTER.md); `0996539436d1cd345cb146d370abc8f5eeaff138` — PUSH VERIFIED. 3 supported replacements; LC_ALL=C wc -w 2,482 → 2,732. Full final reading followed actual validation.

#### 2. The Singing Needle — `O-IVγ-1053`

Four repairs identify the spire as the boring/surfacing body and hovering as its halo; replace proven blunt vulnerability with fragment-based projection; mark pneumatic base assault untried; add complete Appearance linking geological sorrow, column, acoustic halo, observable song, failed counter-phase attempts and worked base-crystal equipment.

**Final logical result:** CHANGED: whole written design is coherent after disambiguating the halo from column motion and preserving the explicit boundary between tested fragments and untried body attack. Instruments, wind/proximity conditions, normal/subsurface/surfaced song state, combat methods and equipment are traceable without a new form. The retained experimental uncertainty is not a contradictory body requirement.

**Holds and later recheck:**

- Blunt impact against the complete spire remains untried; no extra vulnerability or clearance asserted.
- Drifter early fallback remains unexplained, with faint tone/no song/no stall. Do not infer acoustic repulsion.
- No exact external A–D set or artwork inspected; previous primary-only source credits are not awarded again.

**Commentary:** The strongest image is not the tall crystal but the cups stopping before anyone bleeds. The morning drill including the cook makes this a staffed, costly pass, not a decorative singing mountain. Keep that uncertainty instead of giving the squad an easy hammer solution.

**Evidence and individual push:** [B165_02_SINGING_NEEDLE.md](SE_APPEARANCE_REVIEWS/B165_02_SINGING_NEEDLE.md); `ed68abb37ad23d5d3cdbb829364ffb772f8c1cd2` — PUSH VERIFIED. 4 supported replacements; LC_ALL=C wc -w 2,929 → 3,230. Full final reading followed actual validation.

#### 3. The Ancestral Guilt — `N-Vω-1055`

Four supported repairs replace absolute inescapability with acknowledgement-sensitive pressure; correct wielder wording to exposed person because no gear exists; qualify repeated mass doubling as a precautionary model after one accidental tear; add Appearance separating ledger phantom, visitor script, slag, limited eyewitness height/count reports, modelled combat and entirely theoretical M.A.W.

**Final logical result:** CHANGED: source-attributed dimensions and count reports remain qualified, and the ledger construct's origin, creeping/audit movement, script effects, acknowledged relief, cutting hazard and modelled combat now distinguish observations from projections. No new transformation is needed. Explicitly theoretical equipment is not a written-body defect or extraction completion.

**Holds and later recheck:**

- No suppression, repeated tearing, mass reconciliation of the purge or gear extraction is claimed; those remain untried.
- The classification height and paired hands are preserved; Jin-Soo's height and short hand/pen reports are not silently converted into measurements. Future measured census belongs in the later recheck backlog.
- InheritedDebt overlap is four people's postings, not co-location, immunity caused by either entity, or shared equipment. No Weapon pair credit.
- Disposition index retains an older absolute mass-growth quotation and modelled-sector-harm language; refresh its evidence wording in the later source recheck, without silently changing Negative classification here.

**Commentary:** The page in the trainee's fist and the Bureau refusing to read its own purge are the sharpest details. The sorrow is inherited bookkeeping made physical, not merely a huge clerk. Protecting that distinction also keeps the blank coat a disturbing theory rather than a conveniently tested escape route.

**Evidence and individual push:** [B165_03_ANCESTRAL_GUILT.md](SE_APPEARANCE_REVIEWS/B165_03_ANCESTRAL_GUILT.md); `0ee44c65aa1c5418a0df2fd465d1560626432260` — PUSH VERIFIED. 4 supported replacements; LC_ALL=C wc -w 3,125 → 3,471. Full final reading followed actual validation.

#### 4. The Unbroken Pledge — `N-IIIβ-1056`

Five repairs add registration and observed slack to the burial instruction; specify bearer rather than generic target in both neck-tightening moves; preserve one-turn book and larger Min-Seok release without an absolute one-turn promise; add Appearance linking tethered cord, bitten coin, survivor history, conditional internal fibres, projected comrade, defensive field and released-cord equipment.

**Final logical result:** CHANGED: the entire written body/action chain is supported as a tethered, bearer-directed cord with projected/field effects, not an independent soldier. Revised release guidance follows the recorded name-entry event and does not overwrite variable response or failed treatment. Material, measured length, orientation, motion, constriction thresholds and derived gear remain intact.

**Holds and later recheck:**

- The cut bearer remains unable to use voice-based treatment. No invented cure, transfer or regrowth.
- Office service-cannot-be-confirmed replies are possible sealed-schedule links, not confirmed identities or permission to solicit forbidden names. BrokenPromise contact remains prohibited and untested.
- Exact cause and generality of differing release counts remain unproven; the instruction no longer guarantees a fixed decrement or a response to any summary. No exact external Weapon pair.

**Commentary:** The twenty-two minutes spent fetching the register turn this from a generic guilt curse into something specifically municipal. The city has to accept the name before the cord lets go. The third unworked cord in the safe is more convincing than inventing a third piece of gear.

**Evidence and individual push:** [B165_04_UNBROKEN_PLEDGE.md](SE_APPEARANCE_REVIEWS/B165_04_UNBROKEN_PLEDGE.md); `6a5823f6a5ac5a00db8f3c06a877c57c6d25c790` — PUSH VERIFIED. 5 supported replacements; LC_ALL=C wc -w 3,511 → 3,894. Full final reading followed actual validation.

#### 5. Apostle Maker — `C-IIγ-071c`

Four repairs add an Appearance stage/body/wing/measurement/chronology/equipment boundary; change eleventh-conversion colour from permanently set to a reading that may shift; make Ferrehan one nonconfrontational approach rather than contradicting stable observation; mark all never-extracted equipment conditional rather than an issued inventory.

**Final logical result:** HELD: named transformation supports the nonidentical early/later body and conditional wing solidity, but span, trigger/branch authority and current-era chain chronology remain unresolved. Improvements do not earn written-design completion or extra equipment credit. No replacement body, flight state or numerical normalization invented.

**Holds and later recheck:**

- Wing width five metres across versus five metres shoulder-to-tip lacks matched endpoints; no numerical change or inferred spread multiplier.
- Stage3 begins after twelve blessings in Origin/BlessingGiver versus begins a twelve-person sequence in chain table; final branch tied to city sorrow versus recipient choice, with no actual resolution crosswalk.
- This active converting account versus SideA current completedHandofHope lacks chronology; MasterEntities RankIII and broader PatientMartyr/C-Vomega071c examples differ from current C-IIgamma071c. No reset, duplicate healer or new transformation invented.
- Suppression is never tried; equipment remains conditional, with no exact external stage-specific pair or safe issue/field-use claim. Awe of unmarked observers and marked command compulsion are different scopes, not blanket voluntary obedience.

**Commentary:** This is the point where care becomes certainty and certainty removes refusal. That is stronger than simply making the healer larger and more radiant. The remaining uncertainty over who decides the final branch matters, because it determines whether the last person still has a meaningful choice.

**Evidence and individual push:** [B165_05_APOSTLE_MAKER.md](SE_APPEARANCE_REVIEWS/B165_05_APOSTLE_MAKER.md); `5b5e5a522ab262bcd7147ed46bc49a703841808f` — PUSH VERIFIED. 4 supported replacements; LC_ALL=C wc -w 3,949 → 4,288. Full final reading followed actual validation.

### Five reviewed dossiers

Linked names open the reviewed dossier; each unit passed all five checks.

| Entity | Changes | Outcome | Checks | Push |
|---|---|---|---|---|
| [The_Glass_Silt_Drifter](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-O-III%CE%B3-1052_The_Glass_Silt_Drifter_%EC%9C%A0%EB%A6%AC%EB%AA%A8%EB%9E%98_%EB%B0%A9%EB%9E%91%EC%9E%90.md "SE-O-IIIγ-1052_The_Glass_Silt_Drifter_유리모래_방랑자.md") `O-IIIγ-1052` | 3 repairs | HELD | 5 / 5 PASS | `0996539` VERIFIED |
| [The_Singing_Needle](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-O-IV%CE%B3-1053_The_Singing_Needle_%EB%85%B8%EB%9E%98%ED%95%98%EB%8A%94_%EB%B0%94%EB%8A%98.md "SE-O-IVγ-1053_The_Singing_Needle_노래하는_바늘.md") `O-IVγ-1053` | 4 repairs | CHANGED | 5 / 5 PASS | `ed68abb` VERIFIED |
| [The_Ancestral_Guilt](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-N-V%CF%89-1055_The_Ancestral_Guilt_%EC%A1%B0%EC%83%81%EC%9D%98_%EC%9B%90%EC%A3%84.md "SE-N-Vω-1055_The_Ancestral_Guilt_조상의_원죄.md") `N-Vω-1055` | 4 repairs | CHANGED | 5 / 5 PASS | `0ee44c6` VERIFIED |
| [The_Unbroken_Pledge](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-N-III%CE%B2-1056_The_Unbroken_Pledge_%EA%B9%A8%EC%96%B4%EC%A7%80%EC%A7%80_%EC%95%8A%EC%9D%80_%EC%84%9C%EC%95%BD.md "SE-N-IIIβ-1056_The_Unbroken_Pledge_깨어지지_않은_서약.md") `N-IIIβ-1056` | 5 repairs | CHANGED | 5 / 5 PASS | `6a5823f` VERIFIED |
| [Apostle_Maker](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-071c_Apostle_Maker_%EC%82%AC%EB%8F%84_%EB%A7%8C%EB%93%9C%EB%8A%94_%EC%9E%90.md "SE-C-Iα-071c_Apostle_Maker_사도_만드는_자.md") `C-IIγ-071c` | 4 repairs | HELD | 5 / 5 PASS | `5b5e5a5` VERIFIED |

### Full dossier links

- [[SE-O-IIIγ-1052_The_Glass_Silt_Drifter_유리모래_방랑자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-O-III%CE%B3-1052_The_Glass_Silt_Drifter_%EC%9C%A0%EB%A6%AC%EB%AA%A8%EB%9E%98_%EB%B0%A9%EB%9E%91%EC%9E%90.md "SE-O-IIIγ-1052_The_Glass_Silt_Drifter_유리모래_방랑자.md")]
- [[SE-O-IVγ-1053_The_Singing_Needle_노래하는_바늘](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-O-IV%CE%B3-1053_The_Singing_Needle_%EB%85%B8%EB%9E%98%ED%95%98%EB%8A%94_%EB%B0%94%EB%8A%98.md "SE-O-IVγ-1053_The_Singing_Needle_노래하는_바늘.md")]
- [[SE-N-Vω-1055_The_Ancestral_Guilt_조상의_원죄](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-N-V%CF%89-1055_The_Ancestral_Guilt_%EC%A1%B0%EC%83%81%EC%9D%98_%EC%9B%90%EC%A3%84.md "SE-N-Vω-1055_The_Ancestral_Guilt_조상의_원죄.md")]
- [[SE-N-IIIβ-1056_The_Unbroken_Pledge_깨어지지_않은_서약](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-N-III%CE%B2-1056_The_Unbroken_Pledge_%EA%B9%A8%EC%96%B4%EC%A7%80%EC%A7%80_%EC%95%8A%EC%9D%80_%EC%84%9C%EC%95%BD.md "SE-N-IIIβ-1056_The_Unbroken_Pledge_깨어지지_않은_서약.md")]
- [[SE-C-Iα-071c_Apostle_Maker_사도_만드는_자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-071c_Apostle_Maker_%EC%82%AC%EB%8F%84_%EB%A7%8C%EB%93%9C%EB%8A%94_%EC%9E%90.md "SE-C-Iα-071c_Apostle_Maker_사도_만드는_자.md")]

### Independent live counters

Equipment source-review coverage is distinct from written entity-design completion and finished artwork.

| Workstream | Completed | Coverage | Remaining |
|---|---:|---:|---:|
| ALL M.A.W. Types Appearance per SE — source-review coverage | 255 / 301 | 84.72% | 46 / 301 |
| ALL M.A.W.-W Appearance per SE — source-review coverage | 255 / 287 | 88.85% | 32 / 287 |
| SE Appearance Fix — independent written-design pass | 16 / 301 | 5.32% | 285 / 301 |

The SE count moves 13 / 301 → 16 / 301 for Needle, Guilt and Pledge. Drifter and Apostle Maker remain held. No repeated equipment credit, no inferred external pair, no backfilled body or art credit. The 301 denominator includes Unknown entities. The 287 Weapon denominator remains unchanged.

Status totals: 12 changed, 4 retained, 88 held, 2 blocked and 195 pending, summing to 301. A completed review with unresolved whole-design claims is not a completed appearance fix.

### Checks, source dependencies and limits

- Twenty-five fresh closure checks PASS: verify (residue and seams), tpl (template residue), sectfile (section repetition), wikistd (document conventions) and sect (shared-prose fraction), for all five dossiers.
- Each original/final hash and bounded replacement reconstruction matches. All digit sequences are unchanged. The actual checker outputs are in [the closure JSON](SE_APPEARANCE_REVIEWS/B165_CLOSE.json).
- All 296 unselected primary dossiers are byte-identical to the frozen opening base. All 301 classification Physical Form rows are unchanged. Needle's Movement row is the only classification-row qualification: body boring versus halo hovering.
- The mutual Drifter/Needle encounter blocks are unchanged from the opening originals. Later counterpart edits do not turn the faint tone/no-stall observations into causation.
- Source fingerprints capture their unit-time versions. Mutable WIP/CHANGELOG were subsequently extended; their fingerprints are not a claim that append-only logs remained frozen.
- Fifty-four repository unit tests PASS. The first closure audit encountered Git's quoted non-ASCII path output; switching to NUL-delimited paths fixed the harness. The full audit was rerun successfully. An unsupported “mountain-sized” phrase in Needle's draft was removed before its final reread and individual push.
- Closure gate initially refused copied receipt links that were relative to the review folder rather than each log. Corrected WIP, CHANGELOG and progress to their own relative link roots, removed an extra EOF blank line and reran validation; the refusal created no commit.
- Final audit recalculated Needle's word count with required LC_ALL=C: 2,929 → 3,230. An intermediate default-locale recount had incorrectly reported 3,265; corrected that metadata in the receipt, batch record, closure and both logs. Primary text and all hashes are unchanged.
- Complete final primary reading followed validation for every unit. Technical PASS alone was not used as logical completion.
- Both WIP and CHANGELOG carry every unit and this closure. Current progress lead is repaired so it no longer carries the stale Batch164 summary or “No165 authorization” text.
- No illustration, browser, rendered page, running preview or published site was inspected. No deployment, merge, new body generation or numeric normalization occurred.
- Later full source/design recheck remains available. Guilt's disposition-index evidence wording, Drifter's action/response conflicts and Apostle Maker's scale/chronology/branch conflicts remain visible.
- Batch301 remains blocked on eight owner-supplied bodies and its separate one4+4 operation. Generation and validation must precede any wiki copy.

Closure metadata is shipped in a separate gate after the five individually verified pushes. The closure commit is identified by this file's history and the final chat report, not a self-referential embedded commit hash. PR14 remains owner-controlled; this closed batch is not a merged PR. No166 is opened.

## Batch166 OPEN — 0 / 5

Owner p after CLOSED165 authorizes Batch166 only; minimum five, cumulative three No change triggers5→7→10; later full recheck retained.

Fresh shortest-pending cohort, ranked with required LC_ALL=C word counts:

1. `C-Iα-114` — `SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-114_A_Letter_Never_Sent_부치지_못한_편지.md` (4,494 words).
2. `O-IIIγ-412` — `SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIIγ-412_The_Wedge_That_Held_끝끝내_버틴_쐐기.md` (4,498 words).
3. `N-IIβ-319` — `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIβ-319_The_Magistrates_Strike-Through_판관의_취소선.md` (4,562 words).
4. `C-Iα-900` — `SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-900_Vellum_Man_잊혀진_이야기꾼.md` (4,669 words).
5. `N-IIβ-919` — `SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIβ-919_Passing_Bell_조상의_시간.md` (4,707 words).

No unit is reviewed by opening. Each needs complete original/exact-source/history review, bounded supported improvements, five actual checks, full final reading, individual Commentary, both logs and verified push. No change is 0 / 0; pending is not No change.

Counters unchanged: Types 255 / 301 (84.72%; 46 / 301 remain); Weapon 255 / 287 (88.85%; 32 / 287 remain); SE 16 / 301 (5.32%; 285 / 301 remain). No167, merge or deployment. Batch301 eight-owner-body/one4+4/generate-validate-before-copy blocker remains.

### Batch166 unit1 — OPEN1/5

[A Letter Never Sent evidence](SE_APPEARANCE_REVIEWS/B166_01_LETTER.md): HELD, 5repairs, five checks and complete final read. No change0/1; source-review counters255/301and255/287, independentSE16/301. Pending is not No change; later full recheck retained.

### Batch166 unit2 — OPEN2/5

[The Wedge That Held evidence](SE_APPEARANCE_REVIEWS/B166_02_WEDGE.md): HELD, 4repairs, five checks and complete final read. No change0/2; source-review counters255/301and255/287, independentSE16/301. Pending is not No change; later full recheck retained.

### Batch166 unit3 — OPEN3/5

[The Magistrate's Strike-Through evidence](SE_APPEARANCE_REVIEWS/B166_03_MAGISTRATE.md): HELD, 5repairs, five checks and complete final read. No change0/3; source-review counters255/301and255/287, independentSE16/301. Pending is not No change; later full recheck retained.

### Batch166 unit4 — OPEN4/5

[Vellum Man evidence](SE_APPEARANCE_REVIEWS/B166_04_VELLUM.md): HELD, 5repairs, five checks and complete final read. No change0/4; source-review counters255/301and255/287, independentSE16/301. Pending is not No change; later full recheck retained.

### Batch166 unit5 — OPEN5/5

[Passing Bell evidence](SE_APPEARANCE_REVIEWS/B166_05_PASSING_BELL.md): HELD, 7repairs, five checks and complete final read. No change0/5; source-review counters255/301and255/287, independentSE16/301. Pending is not No change; later full recheck retained.

## Batch166 CLOSED 5 / 5

26 repairs, five HELD, No change0/5. 25 fresh closure validators and54 repository tests PASS;296 unselected primaries and five reserves unchanged;300 Physical Form rows preserved,919 non-corporeal label qualified from explicit source evidence. [Evidence, Commentary and exact checks](SE_APPEARANCE_REVIEWS/B166_CLOSE.md). No167 authorized.

### Batch167 unit1 — OPEN1/5

[Dead Air evidence](SE_APPEARANCE_REVIEWS/B167_01_DEAD_AIR.md): HELD, 6 supported repairs and five validators PASS. Complete original/final read. No change0/1. No168 authorization.

### Batch167 unit2 — OPEN2/5

[Unwaking Block evidence](SE_APPEARANCE_REVIEWS/B167_02_UNWAKING_BLOCK.md): HELD, 6 supported repairs and five validators PASS. Complete original/final read. No change0/2. No168 authorization.

### Batch167 unit3 — OPEN3/5

[Once Upon evidence](SE_APPEARANCE_REVIEWS/B167_03_ONCE_UPON.md): HELD, 7 supported repairs and five validators PASS. Complete original/final read. No change0/3. No168 authorization.

### Batch167 unit4 — OPEN4/5

[Never Discharged evidence](SE_APPEARANCE_REVIEWS/B167_04_NEVER_DISCHARGED.md): HELD, 8 supported repairs and five validators PASS. Complete original/final read. No change0/4. No168 authorization.

### Batch167 unit5 — OPEN5/5

[Weighted Silence evidence](SE_APPEARANCE_REVIEWS/B167_05_WEIGHTED_SILENCE.md): HELD, 6 supported repairs and five validators PASS. Complete original/final read. No change0/5. No168 authorization.

## Batch167 CLOSED5/5

33repairs, five HELD, No change0/5. 25fresh validators and54tests PASS. 296unselected primaries, five reserves and all interaction blocks unchanged;298 Physical Form rows unchanged, three source-supported qualifications. [Complete evidence and Commentary](SE_APPEARANCE_REVIEWS/B167_CLOSE.md). No168 authorized.

### Batch168 unit1 — OPEN1/5

[Dawn That Forgot evidence](SE_APPEARANCE_REVIEWS/B168_01_DAWN_THAT_FORGOT.md): HELD, 9 repairs, whole original/final read and five actual validators PASS. No change0/1; SE16/301. No169 authorized.

### Batch168 unit2 — OPEN2/5

[Allhallow evidence](SE_APPEARANCE_REVIEWS/B168_02_ALLHALLOW.md): HELD, 8 repairs, whole original/final read and five actual validators PASS. No change0/2; SE16/301. No169 authorized.

### Batch168 unit3 — OPEN3/5

[Father's Broken Bond evidence](SE_APPEARANCE_REVIEWS/B168_03_FATHERS_BROKEN_BOND.md): HELD, 8 repairs, whole original/final read and five actual validators PASS. No change0/3; SE16/301. No169 authorized.

### Batch168 unit4 — OPEN4/5

[The Last Warmth of Forty-Two evidence](SE_APPEARANCE_REVIEWS/B168_04_LAST_WARMTH_OF_FORTY_TWO.md): HELD, 10 repairs, whole original/final read and five actual validators PASS. No change0/4; SE16/301. No169 authorized.

### Batch168 unit5 — OPEN5/5

[Amnesia evidence](SE_APPEARANCE_REVIEWS/B168_05_AMNESIA.md): HELD, 11 repairs, whole original/final read and five actual validators PASS. No change0/5; SE16/301. No169 authorized.

## Batch168 close

CLOSED5/5; all details and Commentary in [closure](SE_APPEARANCE_REVIEWS/B168_CLOSE.md).46 repairs, five held, No change0/5. Counters255/301,255/287,16/301 unchanged. No169.

### Batch169 unit1 — OPEN1/5

[Moktak evidence](SE_APPEARANCE_REVIEWS/B169_01_MOKTAK.md): HELD, 9 repairs, complete original/final reads and five validators PASS. No change0/1;SE16/301. No170 authorized.

### Batch169 unit2 — OPEN2/5

[Once Told evidence](SE_APPEARANCE_REVIEWS/B169_02_ONCE_TOLD.md): HELD, 10 repairs, complete original/final reads and five validators PASS. No change0/2;SE16/301. No170 authorized.

### Batch169 unit3 — OPEN3/5

[The Music Box of Agony evidence](SE_APPEARANCE_REVIEWS/B169_03_MUSIC_BOX_OF_AGONY.md): HELD, 8 repairs, complete original/final reads and five validators PASS. No change0/3;SE16/301. No170 authorized.

### Batch169 unit4 — OPEN4/5

[Hatred Above evidence](SE_APPEARANCE_REVIEWS/B169_04_HATRED_ABOVE.md): HELD, 9 repairs, complete original/final reads and five validators PASS. No change0/4;SE16/301. No170 authorized.

### Batch169 unit5 — OPEN5/5

[Kind Echo evidence](SE_APPEARANCE_REVIEWS/B169_05_KIND_ECHO.md): HELD, 12 repairs, complete original/final reads and five validators PASS. No change0/5;SE16/301. No170 authorized.

## Batch169 current close

CLOSED5/5;48replacements, fiveHELD whole designs, No change0/5. 26,608→28,257words(+1,649);25fresh actual validators54testsPASS. Three counters255/301,255/287,16/301 unchanged. Ledger12changed/4retained/108held/2blocked/175pending; technicalPASS is not logical completion. Five individual verified pushes and exact-source/digit/Tale/corpus audit in [complete report](SE_APPEARANCE_REVIEWS/B169_CLOSE.md). Earlier OPEN snapshots historical; no170authorized.301eightownerbodies/one4+4/generatebeforecopy retained.

### Batch170 unit1 — OPEN1/5

[Dreaming Plague evidence](SE_APPEARANCE_REVIEWS/B170_01_DREAMING_PLAGUE.md): HELD, 14 supported replacements, five actual checks and full final reading. No change0/1. No credits inferred.

### Batch170 unit2 — OPEN2/5

[Miasma evidence](SE_APPEARANCE_REVIEWS/B170_02_MIASMA.md): HELD, 12 supported replacements, five actual checks and full final reading. No change0/2. No credits inferred.

### Batch170 unit3 — OPEN3/5

[Survivor's Span evidence](SE_APPEARANCE_REVIEWS/B170_03_SURVIVORS_SPAN.md): HELD, 13 supported replacements, five actual checks and full final reading. No change0/3. No credits inferred.

### Batch170 unit4 — OPEN4/5

[Drowned Echo evidence](SE_APPEARANCE_REVIEWS/B170_04_DROWNED_ECHO.md): HELD, 11 supported replacements, five actual checks and full final reading. No change0/4. No credits inferred.

### Batch170 unit5 — OPEN5/5

[Backward Hour evidence](SE_APPEARANCE_REVIEWS/B170_05_BACKWARD_HOUR.md): HELD, 11 supported replacements, five actual checks and full final reading. No change0/5. No credits inferred.

## Batch170 — CLOSED5/5

**Batch170 closure (2026-10-21): CLOSED5/5 reviews; No change0/5.** 61 supported replacements, words29,059→31,185(+2,126); allfive written designs HELD.25fresh actual closure validators and54tests PASS; full originals/exactA–D/relevantMaster/history/finals read, individual receipts and verified pushes.296unselected/fivereserves/sourcehashes/digits/allfiveTales unchanged;61operations reconstruct finals,300PhysicalFormrows unchanged except927state-notorganic qualification. Fresh993exactsource review +1Types/+1Weapon; otherfour not recounted;SE+0. Three counters256/30185.05%(45remain),256/28789.20%(31remain),16/3015.32%(285remain). Ledger12changed/4retained/113held/2blocked/170pending. Parallel closurecheck resource SIGKILL disclosed; all25sequential rerun PASS, no exception. Source/gear silhouettes independently evaluated; no invented bodies/transforms. Later full recheck retained. p170spent, no171/merge/deployment/artwork.301eight-owner-body/one4+4/generatevalidatebeforecopy blocker persists.

[Full report](SE_APPEARANCE_REVIEWS/B170_CLOSE.md).

### Batch171 unit1 — OPEN1/5

[Eleven Fifty-Nine evidence](SE_APPEARANCE_REVIEWS/B171_01_ELEVEN_FIFTY_NINE.md): HELD, 8 supported replacements, five actual checks and full final reading. No change0/1. No credits inferred.

### Batch171 unit2 — OPEN2/5

[Floating Fragment evidence](SE_APPEARANCE_REVIEWS/B171_02_FLOATING_FRAGMENT.md): HELD, 10 supported replacements, five actual checks and full final reading. No change0/2. No credits inferred.

### Batch171 unit3 — OPEN3/5

[The Undelivered Thanks evidence](SE_APPEARANCE_REVIEWS/B171_03_UNDELIVERED_THANKS.md): HELD, 12 supported replacements, five actual checks and full final reading. No change0/3. No credits inferred.

### Batch171 unit4 — OPEN4/5

[Lethe evidence](SE_APPEARANCE_REVIEWS/B171_04_LETHE.md): HELD, 9 supported replacements, five actual checks and full final reading. No change0/4. No credits inferred.

### Batch171 unit5 — OPEN5/5

[Blessing Giver evidence](SE_APPEARANCE_REVIEWS/B171_05_BLESSING_GIVER.md): HELD, 7 supported replacements, five actual checks and full final reading. No change0/5. No credits inferred.

## Batch171 — CLOSED5/5

**Batch171 closure (2026-10-21): CLOSED5/5 reviews; No change0/5.** 46 supported replacements (7batch-short/39careful-detail), C-locale words30,917→33,085(+2,168); five whole written designs HELD.25fresh closurevalidatorruns accepted,54testsPASS;247verifyretains one originalquotedellipsis seam warning, not a prose splice and not clean seam[]. Four otherseam[]; allresiduals0,tpl0,sectionthresholdsmet,wikistdTrue.296unselected/fivereserves/digits/allfiveTales/sourcehashes unchanged;46operationsreconstructfinals.300PhysicalFormrows unchanged except928nonbodilyNonOrganicqualification. Five individually verified unit pushes plus928category-position correction; no sixth review. Fresh247forbidden-theory disposition +1Types/+0Weapon;071bexact1007review+1Types/+1Weapon; otherthree not recounted;SE+0. Counters258/30185.71%(43remain),257/28789.55%(30remain),16/3015.32%(285remain). Ledger12changed/4retained/118held/2blocked/165pending. Laterfullrecheck retained;p171spent,no172/merge/deployment/artwork.301eight-owner-body/one4+4/generatevalidatebeforecopy blocker unchanged.

[Full report](SE_APPEARANCE_REVIEWS/B171_CLOSE.md).

### Batch172 unit1 — OPEN1/5

[Last Fruit evidence](SE_APPEARANCE_REVIEWS/B172_01_LAST_FRUIT.md): HELD, 6 supported replacements, five actual checks and full final reading. No change0/1. No credits inferred.

### Batch172 unit2 — OPEN2/5

[Cracked Flesh evidence](SE_APPEARANCE_REVIEWS/B172_02_CRACKED_FLESH.md): HELD, 9 supported replacements, five actual checks and full final reading. No change0/2. No credits inferred.

### Batch172 unit3 — OPEN3/5

[Forgotten Soul evidence](SE_APPEARANCE_REVIEWS/B172_03_FORGOTTEN_SOUL.md): HELD, 11 supported replacements, five actual checks and full final reading. No change0/3. No credits inferred.

### Batch172 unit4 — OPEN4/5

[Fallow evidence](SE_APPEARANCE_REVIEWS/B172_04_FALLOW.md): HELD, 11 supported replacements, five actual checks and full final reading. No change0/4. No credits inferred.

### Batch172 unit5 — OPEN5/5

[Vanished Tree evidence](SE_APPEARANCE_REVIEWS/B172_05_VANISHED_TREE.md): HELD, 10 supported replacements, five actual checks and full final reading. No change0/5. No credits inferred.

## Batch172 — CLOSED5/5

**Batch172 closure (2026-10-21): CLOSED5/5 reviews; No change0/5.** 47supported replacements (11batch-short/36careful-detail). C-locale words31,352→33,767(+2,415). Five whole written designs HELD, not five completed appearance fixes.25fresh closingvalidatorruns PASS without waivers;54testsPASS;fourfreshpreclosingauditsPASS.296unselected/fivereserves/digits/allfiveprimaryTales/fingerprinted sources unchanged.47exactoperationsreconstructfinals;all11shortrepairsgrow.300PhysicalFormrows unchanged;921retainsOrganiccategory with non-occupant qualifier. Five individually verified unit commits. Fresh777/554equipmentreviews+2Types/+2Weapon;921/233/622alreadycounted. Counters260/30186.38%(41remain),259/28790.24%(28remain),16/3015.32%(285remain). Ledger12changed/4retained/123held/2blocked/160pending. Laterfullrecheckretained;p172spent,no173/merge/deployment/artwork.301eight-owner-body/one4+4/generatevalidatebeforecopy blocker unchanged.

[Full report](SE_APPEARANCE_REVIEWS/B172_CLOSE.md).

### Batch173 unit1 — OPEN1/5

[The Extinguished evidence](SE_APPEARANCE_REVIEWS/B173_01_EXTINGUISHED.md): HELD, 12supported repairs, full final reading and five actual checks. No change0/1.

### Batch173 unit2 — OPEN2/5

[Swallowed Fury evidence](SE_APPEARANCE_REVIEWS/B173_02_SWALLOWED_FURY.md): HELD, 7supported repairs, full final reading and five actual checks. No change0/2.

### Batch173 unit3 — OPEN3/5

[Door to Nowhere evidence](SE_APPEARANCE_REVIEWS/B173_03_DOOR_NOWHERE.md): HELD, 9supported repairs, full final reading and five actual checks. No change0/3.

### Batch173 unit4 — OPEN4/5

[Pandora’s Jar evidence](SE_APPEARANCE_REVIEWS/B173_04_PANDORAS_JAR.md): HELD, 7supported repairs, full final reading and five actual checks. No change0/4.

### Batch173 unit5 — OPEN5/5

[Weight of Silence evidence](SE_APPEARANCE_REVIEWS/B173_05_WEIGHT_SILENCE.md): HELD, 6supported repairs, full final reading and five actual checks. No change0/5.

## Batch173 CLOSED5/5 — 2026-10-22

41 supported repairs (R18:17batch-short/24careful-detail), LC_ALL=C words31,987→34,361 (+2,374). Five whole designs HELD; No change0/5. Five separate unit gates, commits and PUSH VERIFIED results.25 fresh closing checks/54tests/four independent audits PASS.296unselected/5reserves/301PhysicalFormrows, all Tale bytes and digit sequences, fingerprinted sources unchanged. Exact replacements reconstruct final and commit blobs match. TechnicalPASS is not whole-design completion.

Three independent counters: ALL M.A.W. Types Appearance per SE263/301(87.38%),38remain; ALL M.A.W.-W Appearance per SE262/287(91.29%),25remain; SE Appearance Fix16/301(5.32%),285remain. +3/+3 only250/922/967;683B116 and285B107 alreadycredited.12changed/4retained/128held/2blocked/155pending. Coverage includes holds, not artwork.

| Dossier | Repairs short/careful | Words before→after | Checks / design | Commit / push |
|---|---:|---:|---|---|
| [The_Extinguished](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-N-IV%CE%B3-250_The_Extinguished_%EA%BA%BC%EC%A7%84_%EC%9E%90.md "SE-N-IVγ-250_The_Extinguished_꺼진_자.md") | 7/5 | 6343→6943 | Five PASS; HELD | [f298e4a2](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/f298e4a270ded7421e0eb7ec32c6a387b75d7992) PUSH VERIFIED |
| [Swallowed_Fury](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-683_Swallowed_Fury_%EC%82%AC%EB%9D%BC%EC%A7%84_%EB%88%88%EB%AC%BC.md "SE-C-Iα-683_Swallowed_Fury_사라진_눈물.md") | 3/4 | 6359→6849 | Five PASS; HELD | [008cdce5](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/008cdce5b9b2420f985fcde7e25ec737dcd2fdec) PUSH VERIFIED |
| [Door_to_Nowhere](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-II%CE%B2-922_Door_to_Nowhere_%EC%86%9F%EC%95%84%EC%98%A4%EB%A5%B8_%EB%AC%B8.md "SE-O-IIβ-922_Door_to_Nowhere_솟아오른_문.md") | 3/6 | 6392→6804 | Five PASS; HELD | [618b0a68](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/618b0a68afd2bbb56d17d037a102f1c224f91bdc) PUSH VERIFIED |
| [Pandoras_Jar](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-967_Pandoras_Jar_%EC%82%AC%EB%9D%BC%EC%A7%84_%EC%9C%A0%EB%AC%BC.md "SE-N-IVδ-967_Pandoras_Jar_사라진_유물.md") | 2/5 | 6445→6880 | Five PASS; HELD | [3e524e8e](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/3e524e8e8ab3971a9e99a437fce25b69c96de15e) PUSH VERIFIED |
| [Weight_of_Silence](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B1-285_Weight_of_Silence_%EC%B9%A8%EB%AC%B5%EC%9D%98_%EB%AC%B4%EA%B2%8C.md "SE-N-IIα-285_Weight_of_Silence_침묵의_무게.md") | 2/4 | 6448→6885 | Five PASS; HELD | [1c227d79](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/1c227d79ced7b254adbaba8dfe72078439ee5d25) PUSH VERIFIED |

[Closure evidence](SE_APPEARANCE_REVIEWS/B173_CLOSE.json)

No change0/5: no extension beyondfive; these full bespoke narratives and interaction/Watch/Apex records are not a simple cohort. Selection was frozen fresh-pending shortest LC_ALL=C words/designation tie, not defect ranking. Owner p173 exhausted;174 requires a new authorization. PR14 remains OPENdraft→NON-WIKI, owner controls merge; none performed. No artwork/deployment. Later full recheck remains available. Batch301 still blocked on eight owner bodies, one4+4operation, generate/validate beforewiki copy.

### Batch174 unit1 — OPEN1/5

[Uprooted evidence](SE_APPEARANCE_REVIEWS/B174_01_UPROOTED.md): CHANGED, 18supported repairs, full final reading and five actual checks. No change0/1.

### Batch174 unit2 — OPEN2/5

[Chain of Memories evidence](SE_APPEARANCE_REVIEWS/B174_02_CHAIN_OF_MEMORIES.md): HELD, 11supported repairs, full final reading and five actual checks. No change0/2.

### Batch174 unit3 — OPEN3/5

[Ninety Seconds evidence](SE_APPEARANCE_REVIEWS/B174_03_NINETY_SECONDS.md): HELD, 9supported repairs, full final reading and five actual checks. No change0/3.

### Batch174 unit4 — OPEN4/5

[Mirror of Broken evidence](SE_APPEARANCE_REVIEWS/B174_04_MIRROR_OF_BROKEN.md): HELD, 9supported repairs, full final reading and five actual checks. No change0/4.

### Batch174 unit5 — OPEN5/5

[Risus evidence](SE_APPEARANCE_REVIEWS/B174_05_RISUS.md): CHANGED, 11supported repairs, full final reading and five actual checks. No change0/5.

## Batch174 CLOSED 5/5 — 2026-10-22

Five complete primary/source/final reviews are finished. Uprooted and Risus complete the independent written-design pass; the other three remain held. No change: 0/5.

There are 58 supported replacements: 25 batch-short and 33 careful-detail, declared before the relevant edits. LC_ALL=C words: 32,585 → 35,307 (+2,722). Every dossier was individually validated, committed and push-verified. Both WIP and CHANGELOG were updated after every unit.

The three independent counters are:
- **ALL M.A.W. Types Appearance per SE:** 265/301 (88.04%); 36/301 remain.
- **ALL M.A.W.-W Appearance per SE:** 264/287 (91.99%); 23/287 remain. Fourteen dossiers remain outside paired scope.
- **SE Appearance Fix:** 18/301 (5.98%); 283/301 remain.

This batch adds +2 Types, +2 Weapon and +2 SE completions. Equipment coverage includes explicit holds; it is not artwork completion. States: 14 changed, 4 retained, 131 held, 2 blocked, 150 pending.

Fresh closure checks passed 25/25. All 54 tests and four archive-wide audits passed. The 296 unselected dossiers, five reserves, all 301 classification Physical Form rows, source fingerprints, digit sequences and primary Tales are unchanged. All replacements reconstruct the reviewed final files and match their individual commit blobs.

The five individually pushed reviews:

| Dossier | Repairs short/careful | Words | Checks / design | Commit / push |
|---|---:|---:|---|---|
| [Uprooted](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-959_Uprooted_%EC%86%9F%EC%95%84%EC%98%A4%EB%A5%B8_%EB%BF%8C%EB%A6%AC.md "SE-O-IIIγ-959_Uprooted_솟아오른_뿌리.md") `O-IIIγ-959` | 10/8 | 6495→7150 | Five PASS; CHANGED | [0ebd5fe8](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/0ebd5fe875e488767276906a05bc4101937a5eaf) PUSH VERIFIED |
| [Chain_of_Memories](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B2-200_Chain_of_Memories_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%82%AC%EC%8A%AC.md "SE-N-IIIβ-200_Chain_of_Memories_기억의_사슬.md") `N-IIIβ-200` | 4/7 | 6496→7040 | Five PASS; HELD | [c2e0cd2d](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/c2e0cd2d7495b5b636d1235fbb103379018f3725) PUSH VERIFIED |
| [Ninety_Seconds](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-918_Ninety_Seconds_%EB%B0%98%EB%B3%B5%EB%90%98%EB%8A%94_%EC%83%9D%EA%B0%81.md "SE-C-IVδ-918_Ninety_Seconds_반복되는_생각.md") `C-IVδ-918` | 3/6 | 6503→7037 | Five PASS; HELD | [3ffc0ca6](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/3ffc0ca6de2e49c68313ce7da8f727e6257db764) PUSH VERIFIED |
| [Mirror_of_Broken](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-127_Mirror_of_Broken_%EB%B6%80%EC%84%9C%EC%A7%84_%EA%B1%B0%EC%9A%B8.md "SE-N-IIIγ-127_Mirror_of_Broken_부서진_거울.md") `N-IIIγ-127` | 4/5 | 6534→6967 | Five PASS; HELD | [69f6004e](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/69f6004e9694f2c065a277b41590706c1e9f623f) PUSH VERIFIED |
| [Risus](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-150_Risus_%EC%9B%83%EC%9D%8C%EC%9D%98_%EB%A9%94%EC%95%84%EB%A6%AC.md "SE-C-Iα-150_Risus_웃음의_메아리.md") `C-Iα-150` | 4/7 | 6557→7113 | Five PASS; CHANGED | [4452575c](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/4452575cf7992bd6cf020c40dab7259ed69ea8aa) PUSH VERIFIED |

[Full evidence](SE_APPEARANCE_REVIEWS/B174_CLOSE.json)

The owner’s p authorized Batch174 only. Selection was fresh pending-only shortest LC_ALL=C word count, with designation ties; it was not a defect ranking. The frozen order was followed without substitution. No change0/5 does not trigger the cumulative-three 5→7→10 extension.

No Batch175 is authorized. PR14 remains OPEN and draft against NON-WIKI; the owner controls merging. No merge or deployment was performed. Batch301 is still blocked on eight owner-supplied bodies, one4+4 operation, with generation and validation before wiki copy. Later complete rechecking and supported fixes remain available.

### Batch175 unit1 — OPEN1/5

[Glass Elsewhere evidence](SE_APPEARANCE_REVIEWS/B175_01_GLASS_ELSEWHERE.md): HELD, 13supported repairs, full final reading and five actual checks. No change0/1.

### Batch175 unit2 — OPEN2/5

[Tower Erased Overnight evidence](SE_APPEARANCE_REVIEWS/B175_02_TOWER_ERASED_OVERNIGHT.md): HELD, 7supported repairs, full final reading and five actual checks. No change0/2.

### Batch175 unit3 — OPEN3/5

[Panopticon evidence](SE_APPEARANCE_REVIEWS/B175_03_PANOPTICON.md): HELD, 9supported repairs, full final reading and five actual checks. No change0/3.

### Batch175 unit4 — OPEN4/5

[Beating Relic evidence](SE_APPEARANCE_REVIEWS/B175_04_BEATING_RELIC.md): HELD, 10supported repairs, full final reading and five actual checks. No change0/4.

### Batch175 unit5 — OPEN5/5

[Labyrinth of the Unfinished Mind evidence](SE_APPEARANCE_REVIEWS/B175_05_LABYRINTH_UNFINISHED_MIND.md): HELD, 10supported repairs, full final reading and five actual checks. No change0/5.

## Batch175 CLOSED 5/5 — 2026-10-22

Five fresh complete primary/source/final reviews are finished in the frozen order. All five written designs remain HELD. This is a completed review batch, not five completed appearance fixes. No change: 0/5.

49 supported replacements: 23 batch-short and 26 careful-detail, predeclared before editing. LC_ALL=C words: 32,837 → 35,300 (+2,463). Every unit was individually validated, committed and push-verified. WIP and CHANGELOG were updated after each unit and at closure.

Three independent counters:
- **ALL M.A.W. Types Appearance per SE — source-review coverage:** 265/301 (88.04%); 36/301 remain.
- **ALL M.A.W.-W Appearance per SE — source-review coverage:** 264/287 (91.99%); 23/287 remain. Fourteen dossiers are outside the paired denominator.
- **SE Appearance Fix — independent written-design pass:** 18/301 (5.98%); 283/301 remain.

Batch increments: +0 Types, +0 Weapon, +0 SE. Equipment coverage includes holds and is not artwork coverage. Ledger: 14 changed, 4 retained, 136 held, 2 blocked, 145 pending.

Fresh closing checks passed25/25, all54 tests and four archive-wide audits PASS. The296 unselected dossiers, five reserves, digit sequences, primary Tales and fingerprinted sources are unchanged. Three supported classification Physical Form edits are recorded; the other298 rows are unchanged. Exact reconstruction and five distinct, reachable individual commit blobs match the final readings.

| Dossier | Repairs short/careful | Words | Checks / design | Commit / push |
|---|---:|---:|---|---|
| [Glass_Elsewhere](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-903_Glass_Elsewhere_%ED%99%98%EC%98%81%EC%9D%98_%EA%B1%B0%EC%9A%B8.md "SE-N-IIβ-903_Glass_Elsewhere_환영의_거울.md") `N-IIβ-903` | 5/8 | 6557→7043 | Five PASS; HELD | [39bd6236](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/39bd62367a43f6c205186ea210fcd81e8145afcb) PUSH VERIFIED |
| [Tower_Erased_Overnight](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-II%CE%B2-677_Tower_Erased_Overnight_%EC%82%AC%EB%9D%BC%EC%A7%84_%ED%83%91.md "SE-O-IIβ-677_Tower_Erased_Overnight_사라진_탑.md") `O-IIβ-677` | 3/4 | 6560→7023 | Five PASS; HELD | [4ce94910](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/4ce949101d9081743463eaae431c632fa7e91121) PUSH VERIFIED |
| [Panopticon](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-235_Panopticon_%EB%B2%BD_%EC%86%8D%EC%9D%98_%EA%B0%90%EC%8B%9C%EC%9E%90.md "SE-C-IIβ-235_Panopticon_벽_속의_감시자.md") `C-IIβ-235` | 4/5 | 6564→7045 | Five PASS; HELD | [4d2cdf2e](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/4d2cdf2e1e9a6dfa8d6d85dc75a7802866f250af) PUSH VERIFIED |
| [Beating_Relic](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-902_Beating_Relic_%EA%B3%A0%EB%8F%99%EC%B9%98%EB%8A%94_%EC%9C%A0%EB%AC%BC.md "SE-C-IIIγ-902_Beating_Relic_고동치는_유물.md") `C-IIIγ-902` | 5/5 | 6569→7044 | Five PASS; HELD | [9f794fde](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/9f794fde5a05a73ba6f1e300ffb36b126b013668) PUSH VERIFIED |
| [Labyrinth_of_the_Unfinished_Mind](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-909_Labyrinth_of_the_Unfinished_Mind_%EC%83%9D%EA%B0%81%EC%9D%98_%EB%AF%B8%EB%A1%9C.md "SE-C-IVδ-909_Labyrinth_of_the_Unfinished_Mind_생각의_미로.md") `C-IVδ-909` | 6/4 | 6587→7145 | Five PASS; HELD | [80da82c8](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/80da82c819f7f8450731e8ae4c9659d2655da1c9) PUSH VERIFIED |

[Full evidence](SE_APPEARANCE_REVIEWS/B175_CLOSE.json)

Selection was fresh pending-only shortest LC_ALL=C word count with designation-byte tie-break, not a defect ranking. No substitution. No change0/5 does not trigger the cumulative-three ladder. Owner p175 discharged at five complete reviews. No change0/5 does not trigger5→7→10. No176, merge, artwork or deployment. PR14 OPEN/draft to NON-WIKI, owner-controlled merge. Batch301 remains blocked on eight owner-supplied bodies, one4+4 operation, generate/validate before wiki copy. Later full rechecking and supported fixes remain available.

### Batch176 unit1 — OPEN1/5

[Holdout evidence](SE_APPEARANCE_REVIEWS/B176_01_HOLDOUT.md): HELD, 9supported repairs, full final reading and five actual checks. No change0/1.

### Batch176 unit2 — OPEN2/5

[Thinking Engine evidence](SE_APPEARANCE_REVIEWS/B176_02_THINKING_ENGINE.md): HELD, 8supported repairs, full final reading and five actual checks. No change0/2.

### Batch176 unit3 — OPEN3/5

[Torn Window evidence](SE_APPEARANCE_REVIEWS/B176_03_TORN_WINDOW.md): HELD, 10supported repairs, full final reading and five actual checks. No change0/3.

### Batch176 unit4 — OPEN4/5

[Flotsam evidence](SE_APPEARANCE_REVIEWS/B176_04_FLOTSAM.md): HELD, 10supported repairs, full final reading and five actual checks. No change0/4.

### Batch176 unit5 — OPEN5/5

[Lacrima evidence](SE_APPEARANCE_REVIEWS/B176_05_LACRIMA.md): HELD, 8supported repairs, full final reading and five actual checks. No change0/5.

## Batch176 CLOSED 5/5 — 2026-10-22

Five fresh complete primary/source/final reviews are finished in the frozen order. All five whole written designs remain HELD. This closes the review batch, not five completed appearance fixes. No change: 0/5.

45 supported repairs: 23 batch-short and 22 individually authored careful-detail. LC_ALL=C words33,345→36,077 (+2,732). Every unit has five actual checks, full final reading, evidence, independent Commentary, WIP/CHANGELOG updates and a separate verified push.

Three independent counters:
- **ALL M.A.W. Types Appearance per SE — source-review coverage:** 266/301 (88.37%); 35/301 remain.
- **ALL M.A.W.-W Appearance per SE — source-review coverage:** 265/287 (92.33%); 22/287 remain. Fourteen dossiers are outside the paired denominator.
- **SE Appearance Fix — independent written-design pass:** 18/301 (5.98%); 283/301 remain.

Batch increments: +1 Types, +1 Weapon (Flotsam only), +0 SE. Equipment coverage includes unresolved source holds, not finished artwork. Ledger:14 changed,4 retained,141 held,2 blocked,140 pending. Paused025/scope-unconfirmed062 stay excluded from credits; non-SE Book remains outside the corpus.

Fresh closing checks25/25 PASS; all54 tests and four archive-wide audits PASS. Exact45-replacement reconstruction matches all five final hashes and individual commit blobs. The296 unselected dossiers, five reserves, digit sequences, primary Tales and fingerprinted sources remain unchanged. Two supported Physical Form rows changed; other299 rows remain byte-identical.

| Dossier | Repairs short/careful | Words | Checks / design | Commit / push |
|---|---:|---:|---|---|
| [Holdout](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-240_Holdout_%EC%82%AC%EB%9D%BC%EC%A7%84_%EC%9E%94%ED%95%B4.md "SE-C-IIβ-240_Holdout_사라진_잔해.md") `C-IIβ-240` | 5/4 | 6589→7108 | Five PASS; HELD | [d7a55745](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/d7a5574594d04c5bc54478405f13be079b46ae9d) PUSH VERIFIED |
| [Thinking_Engine](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-904_Thinking_Engine_%EC%83%9D%EA%B0%81%ED%95%98%EB%8A%94_%EA%B8%B0%EA%B3%84.md "SE-C-IIIγ-904_Thinking_Engine_생각하는_기계.md") `C-IIIγ-904` | 4/4 | 6612→7115 | Five PASS; HELD | [f4c56cc3](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/f4c56cc30292e11e9faffbdf550181b8977fe15c) PUSH VERIFIED |
| [Torn_Window](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-I%CE%B1-686_Torn_Window_%EC%B0%A2%EC%96%B4%EC%A7%84_%EC%B0%BD.md "SE-N-Iα-686_Torn_Window_찢어진_창.md") `N-Iα-686` | 6/4 | 6658→7177 | Five PASS; HELD | [1cf21e0e](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/1cf21e0ea9f3abdfa2e7e74e8897fc97398686f4) PUSH VERIFIED |
| [Flotsam](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-782_Flotsam_%EB%B2%88%EC%A0%B8%EA%B0%80%EB%8A%94_%EC%9C%A0%EB%AC%BC.md "SE-C-IIβ-782_Flotsam_번져가는_유물.md") `C-IIβ-782` | 5/5 | 6712→7299 | Five PASS; HELD | [e269619f](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/e269619f35786568fb584b86fd0ed8a709d2bfd7) PUSH VERIFIED |
| [Lacrima](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-I%CE%B1-905_Lacrima_%EC%98%81%ED%98%BC%EC%9D%98_%EA%B7%B8%EB%A6%87.md "SE-N-Iα-905_Lacrima_영혼의_그릇.md") `N-Iα-905` | 3/5 | 6774→7378 | Five PASS; HELD | [e2903073](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/e29030738996739b2de094ee36bbaa1b7ec0043e) PUSH VERIFIED |

[Full evidence](SE_APPEARANCE_REVIEWS/B176_CLOSE.json)

Selection: fresh pending-only shortest LC_ALL=C word count, designation-byte ties, not a defect ranking. Queue240→904→686→782→905, no substitutions. Owner p176 discharged after five complete reviews. No change0/5 does not trigger5→7→10. Batch177, merge, artwork and deployment are not authorised. PR14 remains OPEN/draft to NON-WIKI; owner controls merge. Batch301 remains blocked on eight owner-supplied bodies, one4+4 operation, generate/validate before wiki copy. Later full rechecks and supported fixes remain available.

### Batch177 unit1 — OPEN1/5

[Banyan evidence](SE_APPEARANCE_REVIEWS/B177_01_BANYAN.md): HELD, 6supported repairs, full final reading and five actual checks. No change0/1.

### Batch177 unit2 — OPEN2/5

[Memory Rain evidence](SE_APPEARANCE_REVIEWS/B177_02_MEMORY_RAIN.md): HELD, 5supported repairs, full final reading and five actual checks. No change0/2.

### Batch177 unit3 — OPEN3/5

[Frozen Mirror evidence](SE_APPEARANCE_REVIEWS/B177_03_FROZEN_MIRROR.md): HELD, 7supported repairs, full final reading and five actual checks. No change0/3.

### Batch177 unit4 — OPEN4/5

[Endless Shift evidence](SE_APPEARANCE_REVIEWS/B177_04_ENDLESS_SHIFT.md): HELD, 6supported repairs, full final reading and five actual checks. No change0/4.

### Batch177 unit5 — OPEN5/5

[Remembrance evidence](SE_APPEARANCE_REVIEWS/B177_05_REMEMBRANCE.md): HELD, 6supported repairs, full final reading and five actual checks. No change0/5.

## Batch177 CLOSED 5/5 — 2026-10-22

Five complete primary/source/final reviews finished in the frozen order. All five whole written designs remain HELD. This closes five reviews, not five completed appearance fixes. No change: 0/5.

30 supported repairs: 17 batch-short and 13 individually authored careful-detail. LC_ALL=C words34,211→35,783 (+1,572). Each unit has five actual checks, full final reading, evidence, independent Commentary, WIP/CHANGELOG updates and a separate verified push.

Three independent counters:
- **ALL M.A.W. Types Appearance per SE — source-review coverage:** 267/301 (88.70%); 34/301 remain.
- **ALL M.A.W.-W Appearance per SE — source-review coverage:** 266/287 (92.68%); 21/287 remain. Fourteen dossiers are outside the paired denominator.
- **SE Appearance Fix — independent written-design pass:** 18/301 (5.98%); 283/301 remain.

Batch increments: +1 Types, +1 Weapon (Frozen Mirror only), +0 SE. Equipment coverage includes source holds, not finished artwork. Ledger:14 changed,4 retained,146 held,2 blocked,135 pending. Paused025/scope-unconfirmed062 earn no credit; non-SE Book remains outside the corpus.

Fresh closing checks25/25 PASS; all54 tests and four archive-wide audits PASS. Exact30-replacement reconstruction matches all five final hashes and individual commit blobs. The296 unselected dossiers, five reserves, digit sequences, primary Tales and fingerprinted sources remain unchanged. All301 Physical Form rows are byte-identical.

| Dossier | Repairs short/careful | Words | Checks / design | Commit / push |
|---|---:|---:|---|---|
| [Banyan](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-606_Banyan_%EA%B0%80%EB%9D%BC%EC%95%89%EC%9D%80_%EB%82%98%EB%AC%B4.md "SE-N-IVδ-606_Banyan_가라앉은_나무.md") `N-IVδ-606` | 4/2 | 6816→7100 | Five PASS; HELD | [4f5b43c9](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/4f5b43c9eb3ed90aea758b55418be8736c0a3e2c) PUSH VERIFIED |
| [Memory_Rain](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-250_Memory_Rain_%EA%B8%B0%EC%96%B5%EC%9D%98_%EB%B9%84.md "SE-C-IIβ-250_Memory_Rain_기억의_비.md") `C-IIβ-250` | 3/2 | 6831→7139 | Five PASS; HELD | [e4c06f74](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/e4c06f746b846d5307c998cf73247283284c5c4d) PUSH VERIFIED |
| [Frozen_Mirror](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-I%CE%B1-643_Frozen_Mirror_%EC%96%BC%EC%96%B4%EB%B6%99%EC%9D%80_%EA%B1%B0%EC%9A%B8.md "SE-O-Iα-643_Frozen_Mirror_얼어붙은_거울.md") `O-Iα-643` | 4/3 | 6844→7137 | Five PASS; HELD | [63a3c45d](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/63a3c45dfe1493e082ff1d04f24f35db6c483cc5) PUSH VERIFIED |
| [Endless_Shift](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-915_Endless_Shift_%EB%81%9D%EC%97%86%EB%8A%94_%EA%B5%90%EB%8C%80.md "SE-C-IVδ-915_Endless_Shift_끝없는_교대.md") `C-IVδ-915` | 3/3 | 6845→7155 | Five PASS; HELD | [c1280388](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/c1280388d739a46d6a35f81879736532c5dc8fa9) PUSH VERIFIED |
| [Remembrance](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/954853ad-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-115_Remembrance_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%9A%B0%EB%AC%BC.md "SE-C-IIIγ-115_Remembrance_기억의_우물.md") `C-IIIγ-115` | 3/3 | 6875→7252 | Five PASS; HELD | [5c469239](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/commit/5c469239886ca29050ba7ba073ce82359e503cc3) PUSH VERIFIED |

[Full evidence](SE_APPEARANCE_REVIEWS/B177_CLOSE.json)

Selection: fresh pending-only shortest LC_ALL=C word count, designation-byte ties, not a defect ranking. Queue606→250→643→915→115, no substitutions. Owner p177 discharged after five complete reviews. No change0/5 does not trigger5→7→10. These long full-record dossiers do not earn a simple-cohort extension. Batch178, merge, artwork and deployment are not authorised. PR14 remains OPEN/draft to NON-WIKI; owner controls merge. Batch301 remains blocked on eight owner-supplied bodies, one4+4 operation, generate/validate before wiki copy. Later full rechecks and supported fixes remain available.
