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
- **Mugenhan Planetary Biosphere & Tripartite Ecological Taxonomy (2026-09-24):** Codified the complete planetary biosphere across three evolutionary tiers requested by owner: (1) 15 Known Planetary Flora & Fauna (Tier 1 Mundane species across [ConHeAn], [NuRoZen], [UnWiHan], Sea of Glass, Crystal Peaks, Basin), (2) 6 Known Beast Animals & Plants (Tier 2 Sorrow-Infused wildlife and dangerous flora under the 80/20 Law), and (3) 6 Known Mortal Sorrow Creatures (Tier 3 MSF: 4 Fauna, 2 Flora capped at Grade β). Created dedicated files `MUGENHAN_PLANETARY_FLORA_AND_FAUNA.md`, `MUGENHAN_BEAST_ANIMALS_AND_PLANTS.md`, and `MUGENHAN_SORROW_CREATURES.md` in `SOMNARAK-WORLD/Mugenhan_Ecology/`. Synchronized `SOMNARAK_GEOLOGY.md`, `Master_Codices/README.md`, `SOMNARAK-WORLD/README.md`, root `README.md`, and `CHANGELOG.md`. Fully validated across word count floors (>=200 words standard, >=300 words complex), 100% 71-col text box symmetry, 0 raw HTML line-break tags, 0 dollar signs, and clean in-universe perspective. Committed and pushed to `arena/01a0b699-project-somnarak-wiki`.
- **Repository Root Documentation & Canon Architecture Synchronization (2026-09-24):** Synchronized repository root documentation (root `README.md` and `DEVELOPMENT.md`). Overhauled the 35 Macro-Canon Master Codices catalog into its 6 canonical subfolders, de-duplicating corporate entries and purging obsolete draft references. Added comprehensive dedicated sections for the Root Master Architectural & Cartographic Blueprints (`SOMNARAK_CITY_LAYOUT.svg`, `THE_HAND_DR_LAYOUT.svg`), Mugenhan Planetary Biosphere & Ecology Suite (`SOMNARAK-WORLD/Mugenhan_Ecology/`), the 6 specialized operational & narrative suites (`The_Absolvohan/`, `Katabagil/`, `Katharcheok/`, `Gieok_Jeojangso/`, `Jipyeongseondae/`, `Tactical_Combat_Engine/`), and the 12-volume Project Moon research compendium (`PROJECT_MOON_RESEARCH/`). Fully sanitized formatting to 100% 127-128 wide-format benchmark, 0 crooked text boxes, 0 raw HTML line-break tags, 0 LaTeX math symbols, and authentic in-universe perspective. All 1,731 markdown files PASS.
- **Game Battle Operations & Tactical Simulation Suite (`GAME_BATTLE/`) (2026-09-24):** Established the root-level `GAME_BATTLE/` directory for turn-based combat encounters, boss battle mechanics, tactical battle templates, and authoring guidelines. Authored `README.md`, `INTRODUCTION_AND_GUIDE.md` (authoring guide and SOP), `BATTLE_SCENARIO_TEMPLATE.md` (canonical encounter template), and `CANONICAL_ENCOUNTER_01_GRIEVING_COLOSSUS.md` (6-turn scenario demonstrating 10-node movement, speed AP allocation, Left Knee part rupture, Composure Meltdown, and synchronized execution). Updated root `README.md`, `DEVELOPMENT.md`, and `CHANGELOG.md`. All 1,735 markdown files PASS across all validation tools with 0 crooked text boxes, 0 raw HTML line-break tags, 0 LaTeX math symbols, and authentic in-universe perspective.
- **Mnemonic Cycle Engram Framework (`GAME_BATTLE/CYCLE_ENGRAM_SYSTEM.md`) (2026-09-24):** Codified System 1 of the approved 5-system expansion roadmap. Established the 1,778-cycle identity attunement system modifying Speed Bands (AP 2 to 5), Action Slots, and P1 Passives under the Composure Load Law. Documented complete canonical engram profiles for Taeho, Seol-A, Min-Jae, and Ha-Eun. All checks PASS.
- **Squad Archetype Manual: Reverie Containment Cadre (`GAME_BATTLE/SQUAD_ARCHETYPE_REVERIE_CONTAINMENT.md`) (2026-09-24):** Codified comprehensive squad doctrine manual for the standard 4-warden Facility 01 containment team ("The Iron Quad"). Details Vanguard Shield, Acoustic Siphon, Core Striker, and Cryo-Anchor loadouts, 10-node spatial formations, 6-turn rotation combos, and containment breach SOPs. All checks PASS.
- **Squad Archetype Manual: UCD CQB Pacification Cadre (`GAME_BATTLE/SQUAD_ARCHETYPE_UCD_PACIFICATION.md`) (2026-09-24):** Codified comprehensive squad doctrine manual for the Underworld Cleanup Descend close-quarters combat squad ("The Breacher Quad" / "The Slum Sweepers"). Details Heavy Breacher (Kang), Debt Cauterizer (Yuna), CQB Enforcer (Jin), and Harpoon Wincher (Doyun) loadouts, 10-node spatial formations, 6-turn breach rotations, destructible cover clearance, and debt-mark cauterization SOPs. Completes Section 4.3 Squad Archetype Manuals (2/2, 100.0%) and completes all 10 deliverables on the Master Roadmap (10/10, 100.0%). All checks PASS.
- **Text Box Symmetry Checkers & Formatters (Extend-to-Longest-Row Architecture) (2026-09-24):** Overhauled `tools/check_box_symmetry.py`, `tools/text_box_double_checker.py`, and `tools/box_formatter.py`. All tools now count all rows in each text box, benchmark against the longest row, report misalignments as extension requirements, and feature an automated `--fix` engine that adds padding and border fills to extend shorter rows up to the longest row rather than shortening or slicing text. All 1,750 files audited and 100% PASS.
- **Syndicate Boss Mechanics Folio: The King of Menders (`GAME_BATTLE/BOSS_MECHANICS_KING_OF_MENDERS.md`) (2026-09-24):** Codified comprehensive technical boss specification for Underworld Syndicate Boss `The King of Menders`. Features 4-modular part profiles, 3-phase graft evolution, debt-mark stacking, multi-node tether traps, and Grade 5 M.A.W. synthesis manifest. Completes Section 4.2 Boss Mechanics Folios (3/3, 100.0%). All checks PASS.
- **Sovereign Boss Mechanics Folio: The Weeping Mirror (`GAME_BATTLE/BOSS_MECHANICS_WEEPING_MIRROR.md`) (2026-09-24):** Codified comprehensive technical boss specification for Rank IV Sovereign `SE-C-IVδ-195`. Features 4-modular part profiles, 3-phase shatter evolution, twin simulacra duplication, intention deck decision trees, and Grade 5 M.A.W. synthesis manifest. All checks PASS.
- **Sovereign Boss Mechanics Folio: The Grieving Colossus (`GAME_BATTLE/BOSS_MECHANICS_GRIEVING_COLOSSUS.md`) (2026-09-24):** Codified comprehensive technical boss specification for Rank V Sovereign `SE-C-Vδ-002`. Features 4-modular part profiles, 3-phase tectonic shifts, ground liquefaction, intention deck decision trees, and Grade 5 M.A.W. synthesis manifest. All checks PASS.
- **Canonical Scenario 06: Memory Archive Stratum Realization (`GAME_BATTLE/SCENARIO_06_MEMORY_ARCHIVE_STRATUM_REALIZATION.md`) (2026-09-24):** Codified full 6-turn combat scenario depicting Floor 04 Realization against `The Weeping Statue` (Autonomous Lament Core). Features Siphon Veil rupture, Basalt Censer shatter, Mnemonic Suture mechanics, Seiyon's catharsis dialogue, and extraction of `[Key Page: The Mourner]`. Completes Section 4.1 High-Priority Scenarios (5/5, 100.0%). All checks PASS.
- **Canonical Scenario 05: Caravan Leviathan Siege (`GAME_BATTLE/SCENARIO_05_HORIZON_CARAVAN_LEVIATHAN_SIEGE.md`) (2026-09-24):** Codified full 6-turn combat scenario depicting the Horizon Caravan defense of the Drift Throne against `SECC-088 The Titanic Glass Burrower`. Features mandible shattering, pile-bunker carapace rupture, harpoon cable winch lock, and terminal Meltdown. All checks PASS.
- **Canonical Scenario 04: SED Sunken Aqueduct Descent (`GAME_BATTLE/SCENARIO_04_SED_SUNKEN_AQUEDUCT_DESCENT.md`) (2026-09-24):** Codified full 6-turn combat scenario depicting SED Katabagil Passage 1 against `SECC-012 The Drowned Guardian of Year Zero`. Features tendril severance, shell cracking, acoustic water buffs, and culvert gate drainage. All checks PASS.
- **Canonical Scenario 03: UCD Rust & Veil Purge (`GAME_BATTLE/SCENARIO_03_UNDERWORLD_RUST_VEIL_PURGE.md`) (2026-09-24):** Codified full 6-turn combat scenario depicting UCD Operation 1 (The Mask Market) against illicit construct `RIG-FRAY-019 The Slag-Forged Breaker`. Features pneumatic arm severance, basalt carapace shattering, contraband core seizure, and terminal Meltdown. All checks PASS.
- **Canonical Scenario 02: Floor 2 Containment Breach (`GAME_BATTLE/SCENARIO_02_CONTAINMENT_BREACH_FLOOR_02.md`) (2026-09-24):** Codified full 6-turn combat scenario pitting Dekan's Floor 2 Maw Keepers squad against Rank IV Entity `SE-N-IVδ-005 The Smothering Mother`. Features modular arm severing, cryo-anchor lockdown, and terminal Composure meltdown. All checks PASS.
- **Echo-Core Resonant Realization Wars Codex (`GAME_BATTLE/ECHO_CORE_REALIZATION_SYSTEM.md`) (2026-09-24):** Codified System 5 of the approved 5-system expansion roadmap. Enshrined the 4-phase psychological catharsis engine (Denial -> Anger -> Bargaining -> Catharsis), Sorrow Inversion Meltdowns, dialogue scripts, full Floor 2 Dekan realization battle specifications, all 9 departmental realization profiles, and realization reward engrams. All checks PASS.
- **The Ten Specialist Cadres Codex (`Master_Codices/SOMNARAK_SPECIALIST_CADRES.md`) (2026-09-24):** Codified System 4 of the approved 5-system expansion roadmap. Enshrined the Section 1 to Section 6 universal ladder, the ten contractor bureaus (Giltong, Su-Ho, Tam-Sa, Sim-Pan, Il-Gwang, Hwa-Yong, Jeong-Bo, Un-Song, Ui-Ryo, Gyeo-Tu), 10-node spatial grid mechanics, and workshop procurement. All checks PASS.
- **The Five Syndicates of The Raw Codex (`Master_Codices/SOMNARAK_UNDERWORLD_SYNDICATES.md`) (2026-09-24):** Codified System 3 of the approved 5-system expansion roadmap. Enshrined the Treaty of Broken Needles, the Three Underworld Taboos, and the five syndicates (Menders Guild, Rust Frays, Veil Merchants, Memory Washers, Debt Concourse) with 10-node spatial combat grid profiles and workshop supply ties. All checks PASS.
- **The Six Great Workshops Codex (`Master_Codices/SOMNARAK_WORKSHOPS.md`) (2026-09-24):** Codified System 2 of the approved 5-system expansion roadmap. Enshrined the Workplace Law (employment requirement), the 0.5% / 1.0% / 5.0% acquisition curve, and Grade 1 to 5 scaling (Legendary Stat at Grade 5). Documented Yeoul, Cheol-Gyeong, Chim-Mok, Hwa-Seok, Baek-Gwang, and Sim-Yeon. All checks PASS.
- **PENDING EXPANSION QUEUE (APPROVED BY OWNER 2026-09-24):** All 5 major systems derived from Project Moon comparative research have been completely and natively codified into the Project Somnarak canon and game battle engine: (1) Mnemonic Cycle Engrams [COMPLETED], (2) The Six Great Workshops [COMPLETED], (3) The Five Syndicates of The Raw [COMPLETED], (4) The Ten Specialist Cadres & Contractor Bureaus [COMPLETED], and (5) Echo-Core Resonant Realization Wars [COMPLETED]. All 5 systems are fully integrated with the 10-node spatial grid combat engine, verified across all audit tools, and safely preserved in git.
- **OWNER RULINGS ON WORLD-BUILDING & NARRATIVE EXPANSION (2026-09-24):**
  * Vector 1 (Arbiters): Giltong (길통) is Project Somnarak's Arbiter-tier sovereign authority. The other subordinate executioners are not established yet.
  * Vector 2 (Corporate Scale): Corporate Wings in Somnarak are structured on a tighter zone scale: exactly 5 Corporations per Zone (Zone A, B, C, D, etc.), rather than 26 global wings.
  * Vector 3 (Curfew Sanitation): Curfew sweeps are NOT mindless machines; they are human/augmented "Haz-scorchers" and "Cleansers" equipped with heavy thermal/chemical hazard gear and slag-burners.
  * Vector 4 (Identities): Parallel Mirror Identity Extraction is NOT needed for Somnarak; instead, a different native mechanic is used (Mnemonic Cycle Engram attunement under Composure Load).
  * Extra Note (Cities vs Geology): All Unknown/Outer Cities are full living CITIES with urban society, infrastructure, and municipal laws—NOT merely geological biomes or terrain features. Do not reduce them to geology.
  * Vector 5 (Character Cantos): Approved for natural narrative story development, but requires structured refinement into grounded, dialogue-driven prose fiction.
  * Vector 6 (Realization Encounters): Departmental Realization Boss Battles for Floors 01, 03-09 are placed ON HOLD until actively required for gameplay/narrative progression.
- **The Twenty-Five Municipal Zone Corporations Codex (`Master_Codices/SOMNARAK_ZONE_CORPORATIONS.md`) (2026-09-24):** Codified master codex for the 25 Zone Corporations (exactly 5 corporations per Zone across Zones A, B, C, D, E), Fourth Watch Curfew Sanitation Corps (Haz-scorchers and Cleansers), Giltong's sovereign Arbiter authority, and living outer metropolises of Mugenhan. All checks PASS.
- **The Character Story Cantos Suite & Canto I: The Bastion Anchor (`Story_Cantos/`) (2026-09-24):** Established the literary prose fiction suite `SOMNARAK-WORLD/Story_Cantos/`. Codified `README.md` (3-Act narrative framework for 6 core protagonist cantos) and authored `CANTO_01_THE_BASTION_ANCHOR_MIN_JAE.md` (21.2 KB dialogue-driven novella chapter featuring Min-Jae, Seol-A, and Taeho facing the tectonic breach of `SE-C-IVδ-008 The Quaking Monolith`). All checks PASS.
- **Character Story Canto II: The Acoustic Void (`Story_Cantos/CANTO_02_THE_ACOUSTIC_VOID_SEOL_A.md`) (2026-09-24):** Authored 29.2 KB novella chapter centering on Specialist Seol-A, her 14.2 kHz tinnitus, M.A.W. weapon The Silenced Requiem (`MAW-W-021-01`), and the 10-node clash against `SE-C-IIIγ-021 The Hollow Choir`. Implemented mandatory two-space buffer for all Korean text (`  [korean]  `). All checks PASS.
- **Character Story Canto III: The Shattered Striker (`Story_Cantos/CANTO_03_THE_SHATTERED_STRIKER_TAEHO.md`) (2026-09-24):** Authored 29.3 KB novella chapter centering on Vanguard Taeho, his industrial debt trauma, M.A.W. weapon The Ancestral Gravitational Signet (`MAW-W-019-01`), and the 10-node clash against `SE-N-IVβ-019 The Inherited Debt`. Strictly verified zero P.M. vocabulary and enforced two-space buffer for all Korean text (`  [korean]  `). All checks PASS.
- **Character Story Canto IV: The Sub-Zero Ridge (`Story_Cantos/CANTO_04_THE_SUB_ZERO_RIDGE_HA_EUN.md`) (2026-09-24):** Authored 26.3 KB novella chapter centering on Marksman Ha-Eun, her solitary vigil at Outpost E-09 (-40°C to -68°C), M.A.W. weapon The Cold Lens (`MAW-W-103-01`), and the 10-node clash against `SE-C-IVδ-103 The Frozen Veil`. Strictly verified zero P.M. vocabulary and enforced two-space buffer for all Korean text (`  [korean]  `). All checks PASS.
- **Character Story Canto V: Suture of Lost Pages (`Story_Cantos/CANTO_05_SUTURE_OF_LOST_PAGES_SEIYON.md`) (2026-09-24):** Authored 26.4 KB novella chapter centering on Secretary Seiyon (Echo-Core 2), the cumulative memory burden of 1,778 cycles, M.A.W. weapon The Forgotten Lens (`MAW-W-009-01`), and the 10-node clash against `SE-C-IVγ-009 The Memory Weaver`. Strictly verified zero P.M. vocabulary, maintained the two-space buffer, and integrated root Hanja/Kanji brackets (`[Kanji]`) alongside Korean terms. All checks PASS.
- **Character Story Canto VI: The Slum Breacher (`Story_Cantos/CANTO_06_THE_SLUM_BREACHER_KANG.md`) (2026-09-24):** Authored 26.0 KB novella chapter centering on Chief Breacher Kang (The Ram), underworld brotherhood vs municipal duty in Zone B, M.A.W. weapon The Void Maul (`MAW-W-054-01`), and the 10-node clash against `SE-C-IIβ-054 The Empty Mask`. Completed all 6 protagonist Cantos (100.0%). Strictly verified zero P.M. vocabulary, enforced two-space buffer, and paired Alphabet/Romanization style alongside Korean terms. All checks PASS.
- **Departmental Realization Scenario: Floor 02 — Dekan (`GAME_BATTLE/SCENARIO_REALIZATION_FLOOR_02_DEKAN.md`) (2026-09-24):** Authored 14.9 KB 4-phase Realization boss encounter for Echo-Core 3 Lead Dekan (The Maw's Keep). Implemented the 10-node spatial engine, Turns 1-6 Phase 4 climax, and Key Page rewards. Enforced strictly zero Korean Hangul in text boxes (Korean Alphabet Romanization only), with two-space buffer outside boxes. Zero P.M. vocabulary. All checks PASS.
- **Repository-Wide Comprehensive Integrity & Text Box Sweep (2026-09-24):** Completed full audit across all 1,759 markdown files (21.49 MB). Eradicated all generic template placeholders and drafting bracket directives across all content documents, fully canonicalizing `GAME_BATTLE/BATTLE_SCENARIO_TEMPLATE.md`. Enforced strictly zero Korean Hangul in text boxes and code fences across all directories. Confirmed 0 symmetry flaws, 0 raw `<br>` tags, 0 math dollar signs, and 0 P.M. crossover vocabulary. All checks PASS.

---

---

## 7. HANDOVER CAUTION: APPROVED P.M.-BASED EXPANSION ROADMAP & OWNER SPECIFICATIONS

```text
+---------------------------------------------------------------------+
|        HANDOVER CAUTION — APPROVED P.M.-BASED EXPANSION ROADMAP     |
+---------------------------------------------------------------------+
| Ratification Date : 2026-09-24 (Approved by Project Owner)          |
| Purpose           : Inviolable Handover Caution for Session Breaks  |
| Sovereign Canon   : 100% In-Universe Divergence (Zero PM Crossover) |
| Core Deliverables : 5 Approved Systems across Codices & GAME_BATTLE |
+---------------------------------------------------------------------+
```

### 7.1 Executive Summary of Owner Rulings (2026-09-24)
On 2026-09-24, the repository owner reviewed five major high-impact systems adapted from Project Moon comparative research into native Somnarak equivalents. The owner explicitly approved all five options and laid down binding design parameters:

1. **Option 1 (Mnemonic Cycle Engrams):** APPROVED ("Option 1 OK").
2. **Option 2 (The Six Great Workshops):** APPROVED WITH BINDING RULINGS ("Option 2 OK And There Already An Example And For Grade It Can Come Up To Grade 5 But Its Attain Legendary Stat And To Even obtain It You Need To Work Some Where So 0.5% to 1% to 5% Is How It Percentage").
3. **Option 3 (The Five Syndicates of The Raw):** APPROVED ("Option 3 OK").
4. **Option 4 (The Ten Specialist Cadres):** APPROVED ("Option 4 OK").
5. **Option 5 (Echo-Core Resonant Realization Wars):** APPROVED ("Option 5 OK").

If a session breaks down, encounters context limits, or transfers to a successor AI instance, **this section is the binding contract**. The incoming session must resume work from these exact parameters.

---

### 7.2 System 1: Mnemonic Cycle Engrams (주기 각인 / Cycle Engrams)
* **Concept:** Somnarak's native equivalent to Mirror World Identities.
* **In-Universe Foundation:** Somnarak has endured **1,778 consecutive historical reset loops** before the current Year 4,238 resolution. Named operatives (Taeho, Seol-A, Min-Jae, Ha-Eun, Kang, Seiyon) lived radically different lives across those 1,800 years (e.g. Underworld Fray-Hunter, Abyssal Chasm Surveyor, Council Inquisitor, Mender Suture-Apprentice).
* **Storage & Mechanics:** Historical memory crystallizations are housed in the Subterranean Memory Wells of Facility 01 Floor 06 (`The_REVERIE_DIRECTORATE.md`) and the deep root archives of the Memory Archive (`The_MEMORY_ARCHIVE.md`). Operatives attune these engrams to modify their **Speed Band, Action Slot economy, and innate P1 Passives**.
* **Target Files:**
  - `GAME_BATTLE/CYCLE_ENGRAM_SYSTEM.md`: Master mechanical codex defining attunement thresholds, memory resonance costs, and stat modifiers.
  - Integration into operative roster sheets across future `GAME_BATTLE/SCENARIO_*.md` files.

---

### 7.3 System 2: The Six Great Basalt & Resonance Workshops (육대 공방)
* **Concept:** Specialized artisan armories manufacturing non-M.A.W. military equipment, kinetic weaponry, and environmental gear for standard wardens, militia, and contractors who lack the psychological fortitude to bear M.A.W. wear.
* **Canonical Precedents & Existing Examples:**
  - *Master Wright Gwan's family workshop* (`SOMNARAK_CAST.md`, `SOMNARAK_CORPORATIONS.md`): manufactures pneumatic pile-drivers, crawler chassis, and heavy harpoon winches.
  - *The Doll Maker's Workshop* (`SOMNARAK_DAWN_OF_HOPE.md`): Zone D crystal artisan atelier.
  - *Zone C & D workshop smiths* (`MUGENHAN_BEAST_ANIMALS_AND_PLANTS.md`): process Tier 2 Beast carapaces (Dune-Crusher, Ram-Gorgon) into reinforced kinetic trench-shields and breastplates.

```text
+---------------------------------------------------------------------+
|       WORKSHOP EQUIPMENT GRADING & WORKPLACE ACQUISITION LAW        |
+---------------------------------------------------------------------+
| Grade Scale       : Grade 1 through Grade 5                         |
| Grade 5 Pinnacle  : Attains LEGENDARY STAT (Pinnacle Tier Rarity)   |
| Workplace Law     : Operative MUST WORK SOMEWHERE to obtain/craft   |
| Acquisition Rates : Grade 3 = 5.0% | Grade 4 = 1.0% | Grade 5 = 0.5%|
+---------------------------------------------------------------------+
```

* **CRITICAL OWNER DESIGN PARAMETERS:**
  1. **Grading Tier System:** Workshop gear scales strictly from **Grade 1 up to Grade 5** (Grade 1 Standard, Grade 2 Reinforced, Grade 3 Superior, Grade 4 Masterwork, Grade 5 Legendary).
  2. **Grade 5 Legendary Stat:** Grade 5 equipment achieves **Legendary Stat**, featuring unique non-M.A.W. resonance arts and extreme mechanical power rivaling Grade-γ M.A.W. suits without psychological corruption risks.
  3. **The Workplace Law (Employment Requirement):** Grade 3, 4, and 5 equipment **cannot be bought or found casually**. To even qualify to obtain, commission, or craft these armaments, an operative or citizen **must be actively employed or affiliated with a certified industrial workplace, guild, or sovereign workshop** (e.g., apprentice service, foundry tenure, or guild standing).
  4. **The Rarity & Acquisition Percentage Curve:**
     - **Grade 5 (Legendary Stat):** Exactly **0.5%** acquisition / crafting success rate.
     - **Grade 4 (Masterwork):** Exactly **1.0%** acquisition / crafting success rate.
     - **Grade 3 (Superior):** Exactly **5.0%** acquisition / crafting success rate.
     - (Grades 1 and 2: Standard industrial guild issue for working personnel).
* **The Six Sovereign Workshops:**
  1. *Yeoul Workshop (여울 공방 / Rapid Flow):* High-velocity pneumatic harpoons, acoustic needle repeaters (Vanguard / Agility).
  2. *Cheol-Gyeong Workshop (철경 공방 / Iron Mirror):* Vitrified basalt slab-shields, kinetic mauls, blast armor (Fortress Anchor).
  3. *Chim-Mok Workshop (침묵 공방 / Absolute Silence):* Acoustic dampening blades, foam-suppressed carbines (Taboo Enforcers).
  4. *Hwa-Seok Workshop (화석 공방 / Vitrified Ember):* Sulfur-furnace thermal lances, superheated glass blades (UCD Pacification).
  5. *Baek-Gwang Workshop (백광 공방 / White Luster):* Precision quartz lenses, pale void rifles (Band 4–5 Snipers).
  6. *Sim-Yeon Workshop (심연 공방 / Deep Marrow):* Pressurized diving harnesses, depth-gauge tether rigs (SED Abyss Explorers).
* **Target Files:**
  - `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_WORKSHOPS.md`: Definitive 6-workshop codex documenting history, forge techniques, the 0.5%/1%/5% acquisition curve, and Grade 1–5 item catalogs.
  - Integration into `GAME_BATTLE/` loadout options.

---

### 7.4 System 3: The Five Syndicates of The Raw (오대 지하 조직)
* **Concept:** Somnarak's native equivalent to the Five Fingers, commanding the subterranean underworld slums ("The Raw") beneath the Mantle Commons of Zones B, C, and D.
* **The Five Syndicates:**
  1. *The Menders Guild (봉합회):* Surgical flesh-to-stone stitchers led by the King of Menders. Fights with barbed suture hooks, tendon wire, and bone-clamps.
  2. *The Rust Frays (녹슨 올):* Acoustic anarchists clad in discordant vibrating scrap-armor that emits continuous shrill resonance, actively shredding enemy composure.
  3. *The Veil Merchants (장막 상인회):* Black-market cartel trading raw Liquid Han and weeping tears. Masters of pale vapor screens and evasive silk cowls.
  4. *The Memory Washers (기억 세탁소):* Illicit cognitive extractors utilizing mnemonic pneumatic drills to erase enemy Action Points and memories.
  5. *The Debt Concourse (부채 결탁):* Predatory usury enforcers who apply Karma Debt promissory notes in combat; detonates accrued interest upon Stagger.
* **Target Files:**
  - `SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_RAW_SYNDICATES.md`: Full municipal dossier detailing territory, criminal codes, internal hierarchies, and combat doctrines.
  - Enemy rosters for UCD urban pacification scenarios in `GAME_BATTLE/`.

---

### 7.5 System 4: The Ten Specialist Cadres & Contractor Bureaus (십대 전문 기단)
* **Concept:** Somnarak's native equivalent to the 12 Fixer Associations and specialized offices, licensed by the Council of Sighs to handle municipal defense, civil investigations, and district security.
* **The Ten Standardized Cadres:**
  1. *Cadre 01 (Giltong / 길통):* Acoustic curfew enforcement and verbal Door-Speech taboo filtration.
  2. *Cadre 02 (Su-Ho / 수호):* Civic infrastructure defense, convoy escort, and outer bulwark sentries.
  3. *Cadre 03 (Tam-Sa / 탐사):* Structural surveyors, collapsed tenement recovery, and shallow aquifer mapping.
  4. *Cadre 04 (Sim-Pan / 심판):* Commercial arbitration, debt notary, and asset foreclosure repossession.
  5. *Cadre 05 (Il-Gwang / 일광):* High-noon patrol squads specialized in repressing Second Watch Ordeals.
  6. *Cadre 06 (Hwa-Yong / 화용):* Hazardous materials decontamination neutralizing Han-dust spills and acid leaks.
  7. *Cadre 07 (Jeong-Bo / 정보):* Intelligence brokers, anonymous district surveillance, and rumor containment.
  8. *Cadre 08 (Un-Song / 운송):* Armored pneumatic transit operators navigating subterranean rail tubes.
  9. *Cadre 09 (Ui-Ryo / 의료):* Secular emergency trauma triage and acute composure restoration (Wound Walker allies).
  10. *Cadre 10 (Gyeo-Tu / 결투):* Judicial dueling champions licensed to resolve high-tier inter-faction disputes.
* **Target Files:**
  - `SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_SPECIALIST_CADRES.md`: Definitive codex establishing licensing, ranks, uniform styles, and sector offices.
  - Operative background rosters for `GAME_BATTLE/` squad creation.

---

### 7.6 System 5: Echo-Core Resonant Realization Wars (반향핵 공명 각성전)
* **Concept:** Somnarak's native equivalent to Floor Realizations.
* **In-Universe Crisis:** The Nine Echo-Core Leads of Facility 01 carry the unresolved emotional grief of their operational sectors. When an Echo-Core reaches an emotional inflection point, their floor undergoes an **Acoustic Realization Crisis**.
* **4-Phase Engagement Structure:**
  - *Phase 1:* The Echo-Core manifests the traits and skills of Floor Cell 01 (Rank I–II).
  - *Phase 2:* Environmental distortion; floor topography mutates; Cell 02 entity merges with the Echo-Core.
  - *Phase 3:* The Echo-Core manifests full Sovereign form, wielding both departmental M.A.W. and personal grief auras.
  - *Phase 4 (Climax):* The directorate squad executes a synchronized parry-clash to shatter the trauma vessel without killing the Echo-Core, achieving **Emotional Catharsis and Resonant Awakening**.
* **Target Files:**
  - `GAME_BATTLE/SCENARIO_REALIZATION_FLOOR_02_DEKAN.md`: Floor 2 Containment Realization Boss Encounter.

---

### 7.7 Invariant Architectural & Formatting Laws for Successors
1. **Push Always (Rule A0):** Every change must be committed and pushed in the same turn (`git rev-parse HEAD == FETCH_HEAD`).
2. **Text Box Symmetry & Auto-Extension:** All ASCII HUDs must be enclosed in non-markdown code fences (````text ... ````), measuring exactly 71 columns compact or 127/128 columns wide. Symmetrical border closure (+ and |) with zero crooked rows. Verification tools count all rows and extend shorter rows up to the longest row.
3. **Arena.ai Chatroom 74-Character Auto-Wrap Law:** In the Arena.ai chatroom interface, the viewport auto-wraps lines exceeding 74 characters. When authoring text boxes in chatroom responses, count all rows to guarantee width <= 74 characters (wrap content into visual sub-rows so no line auto-wraps down). If a box or banner does NOT have left and right borders (e.g. borderless header/separator bars using `=` or `-`), make those top and bottom border bars EXACTLY 74 characters long (`"=" * 74` or `"-" * 74`).
4. **Zero Formatting Leaks:** Zero raw HTML line-break tags, zero LaTeX math dollar signs.
5. **Zero PM Terminology Leaks:** Strictly Somnarak-native terminology (Sorrow Entities, M.A.W., Composure, Meltdown, Wardens, Enforcers).

### 7.8 Universal Chatroom Text Box Rule (47 Columns Exact)
- **User Directive:** "Also Just Always Do 47 Box For The Chatroom Because You Always Fail To Deliver I Still See Many Crooked Line And Border"
- **Mandatory Specification:** In all assistant chatroom responses, all ASCII text boxes must be formatted to **EXACTLY 47 columns wide** (`width=47`, e.g. `+` + 45 `=` + `+`).
- **No Line-Wrapping:** Standard 71-column or 74-column boxes soft-wrap on narrow mobile or split chat screens in Arena.ai, causing crooked borders and broken rows. Setting width to exactly 47 ensures zero line-wrapping and 100% geometric symmetry on all viewports.
- **Strict Character Rule:** Never use Korean Hangul inside ASCII boxes (only Korean Alphabet Romanization / Romaja), ensuring 1-to-1 character-to-column monospace alignment.

---

**If any instruction in this file conflicts with `RULE-TO-FOLLOW.md` v2, `RULE-TO-FOLLOW.md` wins.**
