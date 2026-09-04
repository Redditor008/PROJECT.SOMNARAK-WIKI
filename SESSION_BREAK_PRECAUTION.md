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

- **ACTIVE workstream: M.A.W. weapon SVG remake** (directive resumed 2026-09-04, "CONTINUING M.A.W. SVG REMAKE AND REMADE") — every W item gets a distinct hand-designed silhouette per `REFERENCE_SOMNARAK_WIKI/MAW_WEAPON_ARCHETYPES.md`. Progress lives in `REFERENCE_SOMNARAK_WIKI/MAW_PERSONALIZE_PROGRESS.md` §12+. Done: batch 1 (12 weapons, prior session, `019d5e7` old branch), batch 2 (W-025…054, `cd7aa4f`), batch 3 (W-055…099, `a429641`), batch 4 (W-100…126, `2f45bd7`), batch 5 (W-127…159, `98d2273`). **OWNER CORRECTION 2026-09-04: batches 2–5 rejected as too same-shape/template. Standard = approved 001–021 illustrations (unique composition, pose, per-item background, story props from the Appearance text). Batch 2 redone to standard (`effb7b2`, owner APPROVED); batch 3 redone (`c8a0ec6`, owner APPROVED); batch 4 (W-100…126) redone this session with the NEW OWNER VARIETY RULING: vary weapon kinds beyond blade/blunt/spear (fans, rope darts, needles+thread, thrown discs, cage-jaws, scene compositions) and take each form's band from the record's `Speed / range` stat in `SE-NNN-B` (2 = Short, 3 = Medium, etc.). Batch 5 (W-127, 130, 135, 140, 145, 150, 151, 152, 155, 156, 157, 159) redone the same way THIS session (owner said "p and so do the veriety") — all 12 diversified per the range stat (Short = 135/150/152/155/156, Medium = 127/130/140/145/151/157/159); five canonically named Mauls keep their kind but each got a wholly different head/pose/scene; no Appearance text changes needed (drawn forms match the records, parity intact). Work 1 batch of 12 per round, then STOP for owner review. PARITY RULE: whenever a redo changes an item's physical form, update the `### Appearance` form-sentences in BOTH the `.md` record and the `.html` page (keep ability/limit/ritual text verbatim), then re-verify md↔html parity — done for batch 4 (W-100/102/108/120 updated; others already matched).** Batch 5 APPROVED ("P"); NEW OWNER RULING with that approval: for variety, Medium-range items should include gun/cannon/staff/fantasy kinds — not everything a hitting/cutting weapon. Batch 6 (W-160, 165, 168, 169, 170, 175, 176, 180, 184, 185, 189, 190) done under that ruling: W-165 candle-staff, W-176 loom-frame thread-bow, W-184 hand-cannon sighting frame, W-190 fang-head javelin (Appearance md+html synced for those four, parity 12/12); the named Mauls/Hammer keep their kind with distinct scenes. NEW OWNER RULING (2026-09-05, after batch 6): WEAPON-FIRST DETAIL — no stickmen or scene props; the weapon itself must be large in frame with dense material detail (straps, rivets, wraps, facets, grain, engraved story marks ON the weapon). Batches 5+6 (24 SVGs) redrawn to this standard in one pass; kinds unchanged so no Appearance edits. SECOND RULING same day: SHAPE-VARIANT RESEARCH — before drawing, research online the real shape variants of each weapon type (minimum 4 variants per shape family) and make each item a DIFFERENT documented variant; crystal weapons must follow real crystal formations (terminated prism, double-terminated, bladed aggregate, fenster windows, phantom, faden, druse) and edges must vary (sharp/serrated/blunt/natural). Batches 5+6 rebuilt to this standard (see progress md §15h for the full taxonomy). Next: after owner approves, batch 7 = next 12 W numbers >190 and <1000, applying ALL rules: shape-variant research + weapon-first detail + variety (incl. non-melee kinds) + range + parity. Procedure per batch: read page Appearance → assign unused archetype → hand-write SVG in batch-1 format → render contact sheet (`npm install --no-save @resvg/resvg-js` + `tools/render_maw_svg.mjs`) → SVG + structure gates → update catalog mapping + progress log + this ledger → commit + push. NEVER run `generate_maw_items.py --force`.
- **Workstream COMPLETE:** M.A.W. Appearance expansion via `tools/expand_maw_appearance.py` — all 20 batches shipped, 291 sets / 873 item pages carry 150–204-word source-led Appearance sections with md+html parity.
- **Owner scope ruling (2026-09-04):** the 92 sets outside the 291-set queue are CLOSED, not pending. (a) **Legacy sets** (001–215 registry blocks) — cleared from the queue by owner instruction; no further Appearance work. (b) **1000-series sets** (1001–1043) — these belong to the **Unknown Entity Package**, which was not finished at the time the M.A.W. Registry was created (their A-codices still carry placeholder SECC designations such as `C-Iα-000`); DEFERRED until the owner finishes that package. Do not draft Appearance content for either group unless the owner reopens them.
- **Deferred by owner decision:** tabs UI (later), gallery (later), references (never).
- **README refresh:** DONE (`1c3de49`).

---

**If any instruction in this file conflicts with `RULE-TO-FOLLOW.md` v2, `RULE-TO-FOLLOW.md` wins.**
