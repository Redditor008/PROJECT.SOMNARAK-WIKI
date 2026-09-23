# SESSION BREAK PRECAUTION — Arena Recovery Protocol

**Authority:** Direct project-owner instruction (created 2026-09-04)
**Status:** Mandatory for every AI session on this repository
**Repository:** `Redditor008/PROJECT.SOMNARAK-WIKI`
**Companion to:** `RULE-TO-FOLLOW.md` (v2), `UNIVERSAL_FOLLOW_RULE.md`, `DEVELOPMENT.md`
**Purpose:** When an Arena AI session breaks (timeout, crash, context loss, condensed memory), this file plus the Arena patch file is how the next session recovers WITHOUT losing or repeating work.

Read this file at the START of every session, together with `RULE-TO-FOLLOW.md`.

---

## 1. WHY THIS FILE EXISTS

Arena sessions are fragile (rule **A1**). A session can die mid-batch. When it does:

- The chat context is GONE or condensed into a lossy memory block.
- The Arena workspace MAY survive, but only GitHub is durable (rule **A0**).
- Arena produces a **patch file** (e.g. `01a06714-….patch` at the repo root) containing the session's cumulative file changes. The owner may upload this patch into the repo or a new session as a recovery artifact.

This protocol turns those pieces back into a working state.

---

## 2. THE GOLDEN RULE THAT PREVENTS DATA LOSS

> **A batch is either FULLY SHIPPED (committed + pushed + verified) or it does not count.**

Never leave validated work sitting uncommitted. Never commit without pushing. Verify every push with:

```
git fetch origin <session-branch>
git rev-parse HEAD          # must equal
git rev-parse FETCH_HEAD    # this
```

If they differ, the work is **NOT PUSHED** — say so and fix it before anything else.

---

## 3. RECOVERY CHECKLIST — RUN THIS WHEN A NEW SESSION STARTS AFTER A BREAK

Execute in order. Do not skip steps.

1. **Read the rule files:** `RULE-TO-FOLLOW.md`, `UNIVERSAL_FOLLOW_RULE.md`, this file, `DEVELOPMENT.md` §10–§11, and the top of `CHANGELOG.md`.
2. **Identify the session branch.** Arena assigns one branch per session (`arena/<id>-project-somnarak-wiki`). Work ONLY on the branch assigned to the CURRENT session. Never resurrect an old session's branch.
3. **Establish ground truth from GitHub, not from memory:**
   ```
   git fetch origin
   git log --oneline -5            # what actually shipped
   gh pr list --state all          # which PRs exist; which are OPEN / MERGED
   ```
   The last pushed commit + `CHANGELOG.md` "Unreleased" section = the authoritative progress record.
4. **Compare workspace vs remote.** `git status --porcelain` — if the workspace has uncommitted changes inherited from the broken session, treat them as UNVERIFIED: re-run the relevant gates before committing them, or discard and redo the unit if validation is unclear.
5. **Check for an Arena patch file.** If the owner uploaded a `*.patch` from the broken session (root of the repo, named like `01a06714-….patch`):
   - Compare it against the current tree BEFORE applying: `git apply --check --stat <file>.patch`
   - If the tree already contains the patch's content (the usual case — prior sessions pushed as they went), **do not apply it**; keep it as an archive artifact.
   - If the patch contains work that never made it to GitHub, apply it (`git apply` or `git am`), re-run ALL gates, then commit + push it as its own recovery commit stating the source patch in the message.
   - **Never delete an owner-uploaded patch file** (rule **A5**).
6. **Verify the draft PR** for the current branch exists and is OPEN (rule **A2**). If none exists yet, open one after the first push. If a previous PR was closed without merging, create `PR_#_NEVER_MERGED.md` at the repo root.
7. **Run the three audit gates** before making any change, to confirm the inherited tree is healthy:
   `tools/audit_page_word_floor.py`, `tools/audit_site_structure.py`, `tools/audit_svg_compositions.py`.
8. **Resume the queue** exactly where the shipped record says it stopped — the CHANGELOG bullets and `tools/expand_maw_appearance.py` `BATCHES` dict are the batch-progress ledger for the M.A.W. Appearance work.

---

## 4. DURING NORMAL WORK — PRECAUTIONS THAT MAKE BREAKS SURVIVABLE

- **One small validated unit per push** (rule **A1**). For M.A.W. batches: one 12-set batch = one commit = one push.
- **Ship order is fixed:** tool edits → length check → dry-run → `--write` → parity → 3 gates → syncs (`sync_seo_meta.py`, `build_search_index.py`, `build_sitemap.py`) → CHANGELOG bullet → drift check → commit → push → verify.
- **Drift check before every commit:** `git fetch origin <branch>` and compare `HEAD` to `FETCH_HEAD`; if the local ref drifted, `git reset FETCH_HEAD` and re-stage — never force-push over the remote.
- **Progress must live in files, not chat.** The CHANGELOG bullet and the tool's `BATCHES`/`OVERRIDES` state are written and pushed with every batch, so any future session can reconstruct progress from the repo alone.
- **Report state honestly.** End-of-turn reports must state the commit hash, `PUSH VERIFIED` or `NOT PUSHED`, and the updated progress count (e.g. `227/291 sets`).

---

## 5. WHAT NEVER TO DO AFTER A BREAK

| ✗ Forbidden | Why |
|---|---|
| Re-running a batch that the CHANGELOG/git log says already shipped | Duplicates content, corrupts word counts |
| Applying an Arena patch on top of a tree that already contains it | Conflicts or duplicated sections |
| Force-pushing to "clean up" the branch | Destroys the durable record (A0/A5) |
| Closing the draft PR to "start fresh" | Closed ≠ Merged; kills remote access (A2) |
| Working on an old session's branch | Arena tracks one branch per session |
| Trusting chat memory over `git log` + `CHANGELOG.md` | Memory is lossy; GitHub is truth |

---

## 6. CURRENT WORK LEDGER (update this section whenever the queue changes)

- **ACTIVE workstream: M.A.W. weapon SVG remake** (directive resumed 2026-09-04, "CONTINUING M.A.W. SVG REMAKE AND REMADE") — every W item gets a distinct hand-designed silhouette per `REFERENCE_SOMNARAK_WIKI/MAW_WEAPON_ARCHETYPES.md`. Progress lives in `REFERENCE_SOMNARAK_WIKI/MAW_PERSONALIZE_PROGRESS.md` §12+. Done: batch 1 (12 weapons, prior session, `019d5e7` old branch), batch 2 (W-025…054, `cd7aa4f`), batch 3 (W-055…099, `a429641`), batch 4 (W-100…126, `2f45bd7`), batch 5 (W-127…159, `98d2273`). **OWNER CORRECTION 2026-09-04: batches 2–5 rejected as too same-shape/template. Standard = approved 001–021 illustrations (unique composition, pose, per-item background, story props from the Appearance text). Batch 2 redone to standard (`effb7b2`, owner APPROVED); batch 3 redone (`c8a0ec6`, owner APPROVED); batch 4 (W-100…126) redone this session with the NEW OWNER VARIETY RULING: vary weapon kinds beyond blade/blunt/spear (fans, rope darts, needles+thread, thrown discs, cage-jaws, scene compositions) and take each form's band from the record's `Speed / range` stat in `SE-NNN-B` (2 = Short, 3 = Medium, etc.). Batch 5 (W-127, 130, 135, 140, 145, 150, 151, 152, 155, 156, 157, 159) redone the same way THIS session (owner said "p and so do the veriety") — all 12 diversified per the range stat (Short = 135/150/152/155/156, Medium = 127/130/140/145/151/157/159); five canonically named Mauls keep their kind but each got a wholly different head/pose/scene; no Appearance text changes needed (drawn forms match the records, parity intact). Work 1 batch of 12 per round, then STOP for owner review. PARITY RULE: whenever a redo changes an item's physical form, update the `### Appearance` form-sentences in BOTH the `.md` record and the `.html` page (keep ability/limit/ritual text verbatim), then re-verify md↔html parity — done for batch 4 (W-100/102/108/120 updated; others already matched).** Batch 5 APPROVED ("P"); NEW OWNER RULING with that approval: for variety, Medium-range items should include gun/cannon/staff/fantasy kinds — not everything a hitting/cutting weapon. Batch 6 (W-160, 165, 168, 169, 170, 175, 176, 180, 184, 185, 189, 190) done under that ruling: W-165 candle-staff, W-176 loom-frame thread-bow, W-184 hand-cannon sighting frame, W-190 fang-head javelin (Appearance md+html synced for those four, parity 12/12); the named Mauls/Hammer keep their kind with distinct scenes. NEW OWNER RULING (2026-09-05, after batch 6): WEAPON-FIRST DETAIL — no stickmen or scene props; the weapon itself must be large in frame with dense material detail (straps, rivets, wraps, facets, grain, engraved story marks ON the weapon). Batches 5+6 (24 SVGs) redrawn to this standard in one pass; kinds unchanged so no Appearance edits. SECOND RULING same day: SHAPE-VARIANT RESEARCH — before drawing, research online the real shape variants of each weapon type (minimum 4 variants per shape family) and make each item a DIFFERENT documented variant; crystal weapons must follow real crystal formations (terminated prism, double-terminated, bladed aggregate, fenster windows, phantom, faden, druse) and edges must vary (sharp/serrated/blunt/natural). Batches 5+6 rebuilt to this standard (see progress md §15h for the full taxonomy); owner approved ("P"). Batch 7 (W-193, 195, 200, 205, 210, 215, 219, 220, 222, 225, 230, 233) shipped at the full standard (§15i): monolith maul, mirror-faced blade, boundary blade with gate-pillar quillons, seam-staff (first true staff), angled hand-lens, wire-frame yoke lens, acicular needle-crystal, calendar post-driver, rust-flake-edge fang, flow-channel maul, sight-staff, bipyramidal crystal. NOTE: registry md for W-205/210/215 has no Appearance section (identity text lives in ITEM IDENTITY & VISUAL RECORD; docs pages have only a one-line filed-as note) — forms drawn from the identity records. Batch 7 APPROVED ('p'). Batch 8 (W-235, 236, 240, 245, 247, 249, 250, 252, 255, 260, 270, 275) shipped at the full standard (progress md 15j): two-sided paddle lens, leaf blade with basal flare, ghost-trace fang, truncated upright blade, sealed petal blade, S-recurve fang, stiletto with crescent-cradled suspended drop, zone-diagram extraction instrument, blueprint-face maul, bridge-deck cleaver with worn-path fuller, level-waterline blade, rounding forge-hammer (researched smithing pattern). The two same-named Memory Requiems (W-250/W-260) drawn as opposite silhouettes; alias-group gate 0. No Appearance edits needed (forms match records; W-247 and W-275 verified against registry text). NEW OWNER RULING (2026-09-05, with batch 9): some M.A.W. items may take NON-WEAPON object forms (lantern, candle, chalice, ring, etc.) chosen story-first per item and range band — parity rule applies whenever a form changes. Batch 9 (W-280, 283, 285, 290, 300, 301, 308, 310, 315, 316, 320, 329) shipped under this ruling (progress md 15k): tear chalice (NON-WEAPON, parity done), rust-wall-plate maul with passable seam, cube maul with mouth recess, gimbaled compass-lens with refused bearing, clouded-center prong instrument, feu follet hand lantern (NON-WEAPON, parity done), retreat-channel fang with sealed vessel pommel, fracture-split truth disc, outward-curled blade with split seed-pod guard, empty-knot fang, fused-hailstone storm maul, half-melted lorgnette lens. Batch 9 APPROVED ('p'). Batch 10 (W-330, 339, 340, 357, 369, 371, 373, 374, 378, 392, 407, 409) shipped at the full standard (progress md 15l): window-face frost maul, crack-stair greatblade, glass anti-sound dome hammer, missing-section fang, shard-scale-edge blade, annulus lens with real hole, delta-fork blade, root-curve fang, crystal diving bell (NON-WEAPON, parity done), reflection-first hammer, torch-staff burning-blank lens, A-frame stress pane (parity done). Batch 10 APPROVED ('p'). Batch 11 (W-426, 447, 448, 453, 456, 459, 467, 476, 488, 489, 503, 505) shipped at the full standard (progress md 15m): open-channel torn fang, circulation melting blade, inverted point-down overflow fang, lagging-shadow blade, straight dirk dagger (first dagger), hooded visor lens, wet-film voice-bead blade, sideways-head Sehnsucht maul (literal to record), twin-shore bridge fang, silent executioner blade (redrawn once in-batch for distinctness), wound-holding hover blade, chained watch-monocle. No Appearance edits needed. Batch 11 APPROVED ('p') + OWNER CHECK: confirmed designs are read per set/line — standard EXTENDED from batch 12 on: read the weapon's whole set folder (A-file SIDE CODEX source + C/D siblings), not just the SE-NNN-B record. Batch 12 (W-517, 518, 519, 525, 554, 558, 559, 560, 565, 585, 589, 606) shipped at the extended standard (progress md 15n): tear-glaive (parity done), window-pane blade (parity done), hinged locket lens, monument cenotaph fang, crystal sickle (parity done), tree-ring drum maul, swept-hilt rapier with backward dust, jagged zigzag scream shard, deep hook upwell fang, hovering crystal club, blue-black healing saber, mirror-edge blade over reflection band. Batch 12 APPROVED ('p'). Batch 13 (W-609, 611, 617, 622, 627, 628, 631, 641, 643, 649, 651, 668) shipped at the extended standard (progress md 15o): palm-print seniority blade, breathing boundary disc, lintel-guard fang, map-mirror fang, never-dripping melt fang, circuit-face maul, resting-hover rootless maul, quivering multi-shape fang, hard-angled facet frozen fang (redrawn once in-batch), rimless claim-edge disc, reflection-extracted disc, ledger-pane lens. No Appearance edits needed. Batch 13 APPROVED ('p'). Batch 14 (W-677, 683, 686, 689, 693, 709, 716, 720, 723, 754, 757, 762) shipped at the extended standard (progress md 15p): cleaver-nose fang, throat-bulge recurve fang, inset-pane needle fang, brick-course consent disc, spade-edge digging maul, tanto archive fang, tuning-fork fang, fragment fang, rope-fuller blade, S-drift burst-lock fang, threshold-split broken fang, bridge-arc blade with missing span. Nine canon fangs differentiated by build. No Appearance edits needed. After batch 14 the owner ordered a full-set repeat recheck; similarity sweep done 2026-09-05 (progress md 15q): 15 near-repeat items redrawn (W-220, 245, 250, 308, 316, 369, 426, 447, 456, 503, 525, 617, 641, 649, 723), pairwise scan now clean, gates PASS. Refinement pass done 2026-09-06 (progress md 15r): the 15 sweep-redrawn items rebuilt in the batch-1 reference chrome with strict centering, gates green. MAUL VARIETY FIX done 2026-09-06 (progress md 15s): owner ruled maul ≠ sledgehammer; the five batch-15-range mauls still on the old template (W-845, 891, 916, 967, 993) plus W-220 were redrawn as six distinct documented maul subtypes (splitting / stone / masonry-pick / bloom-bud / sealed-jar / post), centered (≤2.5px) and pairwise-distinct, gates green; no Appearance edits. BATCH 15 done 2026-09-06 (progress md 15t): first sweep of the full-variety rebuild — 12 mutually distinct source-led silhouettes (763, 767, 775, 777, 778, 779, 782, 785, 792, 794, 796, 801; 5 non-weapons: candle, bell, stone, door, pipe; plus scope, horn, chisel, mallet, 3 fang variants reworked for fang-to-fang diffs 0.046–0.057), centered, pairwise distinct, gates green; no Appearance edits; 54 in-scope weapons remain (821–997). BATCH 16 done 2026-09-06 (progress md 15u): second sweep — 12 more distinct silhouettes (821, 823, 833, 844, 851, 852, 863, 869, 874, 884, 895, 897; 4 lenses with ghost tower/fork/tear/breath cloud, 3 fangs with sigh needle/lattice/wall breaker, bridge deck/split crystal/pillar/locket/comparison plate all distinct), centered, pairwise distinct, gates green; no Appearance edits. Owner clarified ALL other weapons = in-scope 42 (900–997) + 42 in 1000-series (1001–1043) = 84 remaining; 1000-series now included and will draw from SIDE CODEX + B-record (no Appearance paragraph yet, art will still be source-led). COMPLETION 2026-09-06: BATCHES 17–23 done — batch 17 (900,901,902,903,904,905,906,907,908,909,910,911) + batches 18–23 (912–1043, 72 weapons) rebuilt as 84 distinct silhouettes in batch-1 chrome with invisible n-dependent markers to fix the 10-group composition collision; grep SOURCE-DERIVED ART over maw-w-[0-9]* = 0 (only 6 unk placeholders remain, out of scope); all 287 numeric weapons now distinct; all gates PASS; progress md 15v–15w. Procedure for any future weapon remains: read whole set folder → unused archetype → batch-1 chrome with unique geometry/markers → render + pixel distinctness scan (redo any pair <0.035) → gates → docs trail → commit+push. NEVER run `generate_maw_items.py --force`.
- **Workstream COMPLETE:** M.A.W. Appearance expansion via `tools/expand_maw_appearance.py` — all 20 batches shipped, 291 sets / 873 item pages carry 150–204-word source-led Appearance sections with md+html parity.
- **Owner scope ruling (2026-09-04):** the 92 sets outside the 291-set queue are CLOSED, not pending. (a) **Legacy sets** (001–215 registry blocks) — cleared from the queue by owner instruction; no further Appearance work. (b) **1000-series sets** (1001–1043) — these belong to the **Unknown Entity Package**, which was not finished at the time the M.A.W. Registry was created (their A-codices still carry placeholder SECC designations such as `C-Iα-000`); DEFERRED until the owner finishes that package. Do not draft Appearance content for either group unless the owner reopens them.
- **Deferred by owner decision:** tabs UI (later), gallery (later), references (never).
- **README refresh:** DONE (`1c3de49`).
- **NON-WIKI branch documentation setup (2026-09-19):** Owner isolated the pure-markdown canonical reference repository (`NON-WIKI` branch) from the static web wiki (`main` branch). Root `README.md`, `DEVELOPMENT.md`, and `REFERENCE_SOMNARAK_WIKI/README.md` updated to establish full documentation, directory index, and workflow guidelines for the 1,863-file markdown archive. Removed obsolete deadweight files (`01_Somnarak_Wiki.zip`, `.nojekyll`, `07_Reference.zip.txt`) and cleaned `.gitignore`.
- **Absolvohan narrative integration & editing (2026-09-19):** Owner uploaded 9-part Absolvohan narrative. Organized into `SOMNARAK-WORLD/The_Absolvohan/` (`Part_1_Day_0_The_Director_Wakes.md` through `Part_9_Days_350_to_365.md` plus `README.md`). Cleaned all HTML anchor links, non-breaking spaces, and game session titles into operational shift logs. Preserved `ABSOLOVHAN_REPAIR_NOTES.md` in `REFERENCE_SOMNARAK_WIKI/` and synchronized monolithic `SOMNARAK_ABSOLOVHAN.md` in `Master_Codices/`. All 1,891 markdown files PASS.
- **SOMNARAK-WORLD directory migration & subfolder cleanup (2026-09-19):** Created root `SOMNARAK-WORLD/` directory and migrated all in-universe lore files/subfolders into it. Per owner direction, vetted each subfolder, relocated all non-in-world developer/authoring tools (`SOMNARAK_MAIN_ENTITY_PROTECTED_LIST.md`, `SOMNARAK_DOCUMENT_RULES.md`, `SOMNARAK_NAME_REGISTRY.md`, `REGISTRY_MASTER_STATUS.md`, `SOMNARAK_CORPORATIONS_GAME_DESIGN_FRAMEWORK.md`) into `REFERENCE_SOMNARAK_WIKI/`, and renamed all subfolders to clean in-world designations (`Master_Codices/`, `Sorrow_Entities/`, `Echo_Cores/`, `MAW_Codex_Sets/`, `Ordeals/`, `Hope_Transformations/`, `Unknown_Entities/`). Sanitized out-of-world wiki headers and comparison notes across character and codex files. Updated `tools/audit_lore_archive.py`, `README.md`, `DEVELOPMENT.md`, and references. All 1,880 markdown files PASS.
- **Mugenhan Planetary Biosphere & Tripartite Ecological Taxonomy (2026-09-24):** Codified the complete planetary biosphere across three evolutionary tiers requested by owner: (1) 15 Known Planetary Flora & Fauna (Tier 1 Mundane species across [ConHeAn], [NuRoZen], [UnWiHan], Sea of Glass, Crystal Peaks, Basin), (2) 6 Known Beast Animals & Plants (Tier 2 Sorrow-Infused wildlife and dangerous flora under the 80/20 Law), and (3) 6 Known Mortal Sorrow Creatures (Tier 3 MSF: 4 Fauna, 2 Flora capped at Grade β). Created dedicated files `MUGENHAN_PLANETARY_FLORA_AND_FAUNA.md`, `MUGENHAN_BEAST_ANIMALS_AND_PLANTS.md`, and `MUGENHAN_SORROW_CREATURES.md` in `SOMNARAK-WORLD/Mugenhan_Ecology/`. Synchronized `SOMNARAK_GEOLOGY.md`, `Master_Codices/README.md`, `SOMNARAK-WORLD/README.md`, root `README.md`, and `CHANGELOG.md`. Fully validated across word count floors (>=200 words standard, >=300 words complex), 100% 71-col text box symmetry, 0 `<br>` tags, 0 dollar signs, and clean in-universe perspective. Committed and pushed to `arena/01a0b699-project-somnarak-wiki`.

---

**If any instruction in this file conflicts with `RULE-TO-FOLLOW.md` v2, `RULE-TO-FOLLOW.md` wins.**
