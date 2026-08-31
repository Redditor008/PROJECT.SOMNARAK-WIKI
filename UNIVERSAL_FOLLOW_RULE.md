# UNIVERSAL AI RULE

**A portable operating rule for any AI working on any repository, in any number of chatrooms or sessions.**

**Status:** Universal baseline. Applies to every AI, every coding session, every pull request, and every deployment — regardless of project, language, framework, or host.
**Portability:** Copy this file to the root of any repository (as `UNIVERSAL_AI_RULE.md` or `RULE-TO-FOLLOW.md`). Repo-specific rules layer ON TOP of this file; they may tighten it but never weaken it.
**Supersedes:** Any older rule file, system prompt habit, or "just save it locally" instinct that conflicts with this file.

> This file does not depend on any specific repo, branch name, page count, tool, or URL. Everything project-specific is written as `<placeholder>`.

---

## WHY THIS FILE EXISTS

AI coding sessions share three fatal failure patterns:

1. **Work is left in the workspace, not the repo.** The workspace is temporary and tied to a single chatroom. When the session ends, the work is gone.
2. **A PR is closed instead of merged.** "Closed" is treated like "done." It is not. Closing a PR (a) makes the work not-live and (b) usually cuts off the session's remote access so nothing else can be pushed.
3. **States are collapsed into "done."** Local edits, local commits, pushed commits, open PRs, merges, and live deployments are five different things. Confusing them is how work silently vanishes.

This file exists so that **no future AI repeats these failures**, no matter how many sessions pass.

---

## THE ONE LAW (read this first)

**PUSH ALWAYS. NEVER SAVE IT ON A CHATROOM.**

Every file you create, edit, rename, or delete must be **committed AND pushed to the remote repository in the same turn you made it.**

A change that exists only in the workspace — or only as a local commit — is a change that is effectively lost. The remote (GitHub, GitLab, etc.) is the only durable store.

---

## UNIVERSAL LAWS

### U1 — PUSH EVERY CHANGE, EVERY TIME

1. The fixed order of operations for every unit of work:
   ```
   make change → validate → git add → git commit → git push → (only then) PR operations
   ```
2. Never end a turn with:
   - uncommitted changes, OR
   - a local commit that has not been pushed.
3. One coherent change per commit. Commit small and often; push immediately after each commit. Do not batch work hoping to push later.
4. Every newly created file, every edit, and every deletion is pushed in the same turn.
5. If a push is blocked, do not proceed silently. Report `NOT PUSHED`, state the exact blocker, and stop claiming progress beyond what is actually on the remote.

### U2 — THE WORKSPACE IS ONE CHATROOM (TEMPORARY)

1. A session can end at any moment: a PR merged, a PR closed, a timeout, a disconnect, a platform shutdown.
2. When a session ends, `git push` and PR tools are usually **permanently blocked in that session**. Trying again in the same chat will not recover access.
3. Therefore: never rely on "I'll push at the end." Complete one small validated unit, then commit and push immediately.
4. Treat every change as potentially the last thing you can ever push.

### U3 — CLOSED ≠ MERGED

1. A pull request has three terminal states: **merged**, **closed (not merged)**, and **open**.
2. **Closed without merge means the work is NOT live** — no matter what anyone calls it.
3. Never close a PR unless you are merging it. Closing a PR:
   - discards the merge,
   - leaves the work not-live,
   - and commonly ends the session's remote access, stranding any other local commits.
4. If you discover a PR was closed instead of merged:
   - say it plainly: `PR CLOSED (NOT MERGED)`;
   - record it (see U7);
   - treat all related local commits as **not on the remote** until proven otherwise.

### U4 — THE OWNER CONTROLS THE MERGE (NEVER AUTO-MERGE)

1. Unless the owner **explicitly** instructs you to merge, leave the PR open and report its state.
2. "Complete the task" or "finish the work" does **not** mean "merge." Merging is a separate, explicit act.
3. When in doubt: open/keep a PR, do not merge, and ask.
4. Do not merge known failures. Do not hide failed checks. Do not merge on your own initiative.

### U5 — OPEN A DRAFT PR EARLY (RECOVERABLE ROUTE)

1. Push early, then open a **draft** pull request from the working branch into the integration branch as soon as the first commit is pushed.
2. A pushed branch + open PR is a recoverable route even if the chatroom dies.
3. Continue pushing later validated commits to the same branch and same PR. Do not open duplicate PRs.

### U6 — BRANCH DISCIPLINE

1. Stay on the branch you are assigned or that the repo rules specify. Do not switch branches to "help."
2. Do not create extra branches, do not rename temporary branches to the integration branch, do not use branch chains, and never force-push.
3. Direction is always:
   ```
   base:    <integration-branch>     (usually main / master)
   compare: <working-branch>
   ```
   Never reverse these.
4. Delete a temporary working branch only after its merge succeeds, and only if the repo rules or owner allow it.

### U7 — FILE SAFETY (NEVER DESTROY THE OWNER'S WORK)

1. Never delete, rename, or move the repository root or `.git`.
2. Never run `git clean`, `git reset --hard`, `git checkout -- .`, or any force-push.
3. Never delete or overwrite a file the owner created without a direct instruction that names the exact file.
4. When the owner says "I'll delete/replace that file myself," do **not** delete it for them — create the new file under a distinct name (e.g. `<name>_v2.md`) and let the owner copy it in.
5. If work must be redone, keep the old version recoverable. Never "clean up" by deleting local changes.

### U8 — CACHE-BUST STATIC ASSETS (or the fix never shows up)

1. On any site that loads assets with a version query (`style.css?v=...`, `app.js?v=...`, images), changing that asset is **not enough** — the version string must change too, or returning visitors keep the old cached file and the change never appears.
2. Rule: whenever you change a cached asset, bump its version string **and** update every reference to it, in the same commit.
3. Use the repo's own sync/generation tools to propagate version strings if they exist; otherwise update references manually and verify none remain stale.

### U9 — HONEST STATE REPORTING (NEVER COLLAPSE STATES)

Report these states separately and truthfully. Never compress them into one word like "done."

```
LOCAL ONLY                 — files edited in the workspace, not committed
COMMITTED LOCALLY          — committed, not on the remote
NOT PUSHED                 — push attempted/failed; state the exact blocker
PUSHED TO WORKING BRANCH   — on the remote branch, not yet integrated
PULL REQUEST OPEN          — PR exists, not merged
PR CLOSED (NOT MERGED)     — PR closed without merge; work is not live
MERGED INTO MAIN           — integrated, but not necessarily deployed
PAGES BUILDING             — deploy in progress (if applicable)
VERIFIED LIVE              — the live URL shows a distinctive marker of the change
```

1. Before claiming "pushed," verify: `git rev-parse HEAD` must equal `git rev-parse origin/<working-branch>`.
2. Before claiming "live," fetch the live URL with a cache-busting query and confirm a **distinctive marker** introduced by the change — not just an HTTP 200.

### U10 — READ THE REPO'S OWN RULES FIRST

1. At session start, read any root-level rule file (`RULE-TO-FOLLOW.md`, `CONTRIBUTING.md`, `README.md`, etc.) before changing anything.
2. Repo-specific rules layer on top of this universal rule. They may tighten it (specific branches, gates, URLs); they never weaken U1–U10.
3. If repo rules conflict with a platform constraint (e.g. a platform-locked session branch), follow the platform constraint, stay on the assigned branch, and report the difference — never silently pick sides.

---

## SESSION WORKFLOW (follow every session, in every chatroom)

### START

1. Report your ground truth:
   ```bash
   git branch --show-current
   git status --short
   git log --oneline -5
   ```
2. Read the repo's root rule files and README.
3. Identify the integration branch, the working branch, and the live acceptance URL.

### DURING (per unit of work)

1. Make one coherent change.
2. Run the relevant checks for that change.
3. `git add` + `git commit`.
4. `git push` **immediately**.
5. Verify the push:
   ```bash
   git rev-parse HEAD
   git rev-parse origin/<working-branch>
   ```
   If they differ, the work is not on the remote.
6. Open or update a draft PR into the integration branch.

### END OF EVERY TURN

- `git status` clean, **and** `HEAD == origin/<working-branch>`.
- Report the completion states honestly (see U9), including any `NOT PUSHED` blocker.

---

## PULL REQUEST LIFECYCLE (fixed procedure)

1. Push the working branch.
2. Open a draft PR early: base = integration branch, compare = working branch.
3. Keep the PR open. Add later commits to the same PR.
4. Run and pass the repo's checks.
5. The owner merges (or you merge only if explicitly told to).
6. Only after a real merge, verify the live URL with a cache-busting query and a distinctive marker.
7. If the PR was **closed without merging**:
   - create a record file at the repo root: `PR_<number>_NEVER_MERGED.md`, stating the PR was closed, not merged, and the work is not live;
   - list which commits were pushed and which remain local;
   - require a new session (or manual owner push) to recover the unpushed commits and open a fresh PR.

---

## RECOVERY PLAYBOOK (when a chatroom dies mid-work)

If the working branch was pushed to the remote:

1. Open the repository's **Pull requests** page in a browser.
2. **New pull request.**
3. base = integration branch; compare = the working branch.
4. Review **Files changed.**
5. Create the PR, wait for checks, **Merge** (owner), then optionally delete the branch.
6. Verify the live acceptance URL.

If a PR already exists, continue from step 4 — do not duplicate it.

If the branch is missing from the remote, the work was never pushed (or was deleted too soon). Recover from a local commit if one still exists; otherwise recreate the change. **Never claim an unpushed local commit is recoverable from the remote.**

---

## REQUIRED COMPLETION REPORT (every session)

```
Working branch:      <name>
Commit:              <full or short SHA>
Push:                <pushed / NOT PUSHED (exact blocker)>
Pull request:        <none / URL / CLOSED-NOT-MERGED>
Merged into main:    <yes / no>
Deployment source:   <branch:/path or unverified>
Live verification:   <URL or not verified>
Distinctive marker:  <marker or not verified>
Working branch deleted: <yes / no>
Working tree clean:  <yes / no>
Checks:              <passed checks and any failures>
```

Never collapse these states into the single word "done."

---

## QUICK DECISION TABLE (when unsure)

| Situation | Do this |
|---|---|
| Change made, not committed | Commit it now, push it now |
| Committed locally, not pushed | Push now. Blocked? Report `NOT PUSHED` + blocker |
| Push blocked by platform | Report blocker; require a new session |
| PR open | Leave it open; add later commits to it; do not auto-merge |
| Owner said "finish/complete" | Finish the code; do NOT merge unless they explicitly said merge |
| PR closed without merge | Report `PR CLOSED (NOT MERGED)`; write `PR_<n>_NEVER_MERGED.md`; new session to recover |
| Changed a cached asset | Bump the version string and update references in the same commit |
| Asked to delete a file | Do it only if the instruction names the exact file; never delete `.git` or owner files otherwise |
| Session ends unexpectedly | Work pushed = recoverable via PR page. Work not pushed = recreate |

---

## GLOSSARY

- **Workspace / chatroom** — the temporary environment tied to one session. Not durable.
- **Remote** — the hosted repository (GitHub, GitLab, …). The only durable store.
- **Integration branch** — where completed work lands (usually `main`/`master`).
- **Working branch** — the platform-assigned or repo-specified branch you push to.
- **Draft PR** — an early, recoverable pull request kept open during the work.
- **Closed ≠ Merged** — a closed PR is not live and strands the session.
- **Distinctive marker** — a visible, checkable change (text, version string, style) that proves a specific commit is live.
