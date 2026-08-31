RULE TO FOLLOW — v2 (SUPER DETAILED)

Authority: Direct project-owner instruction (last updated 2026-09-01) Status: Mandatory for every AI, coding session, pull request, and deployment Repository: Redditor008/PROJECT.SOMNARAK-WIKI Integration branch: main Public acceptance URL: https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/ Supersedes: RULE-TO-FOLLOW.md (v1). Where any older file or instruction conflicts with this file, this file wins.

Read this file before changing anything. These rules are not optional. Content, canon, placement, and visual-quality rules in the referenced standards remain binding.
CHANGELOG — what changed from v1
ADDED (new rules that did not exist before)
Tag 	Rule
A0 	PUSH ALWAYS — every file add/edit/delete must be committed and pushed in the same turn. "PUSH, NEVER SAVE IT ON ARENA."
A1 	Session fragility — the Arena workspace is a one-chatroom, temporary thing. Only GitHub is durable.
A2 	Closed ≠ Merged — a closed PR is not live, and closing it kills the session's remote access. Never close a PR unless merging it.
A3 	Asset cache-busting — any wiki.css/wiki.js change must bump ASSET_VERSION and re-sync, or the fix never shows live.
A4 	Sidebar parity — left and right sidebars share one L-Corp terminal style; CSS fixes go at the END of wiki.css.
A5 	File safety — never delete/overwrite the owner's files or history without a direct, file-named instruction.
REMOVED (rules deleted from v1)
Tag 	Rule removed
R1 	REMOVED: "Do not wait for a separate 'please merge' message when the owner's initial request explicitly authorizes completion and deployment." → The owner controls the merge. Never auto-merge.
R2 	REMOVED: automatic "delete the temporary branch after merge." → Branch deletion is now conditional and owner-approved.
CHANGED (rules rewritten from v1)
Tag 	Change
C1 	§2 rewritten around the push-first, push-always doctrine.
C2 	§4 PR lifecycle rewritten: push → open PR early → keep it OPEN → owner merges → closed ≠ merged.
C3 	§9 completion report extended with NOT PUSHED and PR CLOSED (NOT MERGED) states and a mandatory PR_#_NEVER_MERGED.md record when a PR is closed without merge.
A0 — PUSH ALWAYS (the #1 rule, above all others)

Owner's words: "Always push each adding, editing, or anything that is about the file in git."

    Every single file you create, edit, rename, or delete must be committed and pushed to the assigned session branch in the same turn you make it.
    Never end a turn with:
        uncommitted changes, OR
        a local commit that has not been pushed to GitHub.
    Order of operations is fixed:

    make change → validate → git add → git commit → git push  →  (only then) PR operations

    "PUSH, NEVER SAVE IT ON ARENA." The Arena workspace is temporary and tied to one chatroom. Work that exists only in the workspace is effectively lost when the session ends. GitHub is the only durable store.
    If a push fails, you must NOT proceed silently:
        Report NOT PUSHED.
        State the exact blocker.
        Require a new coding session (or the owner pushing manually) before continuing.
    Never claim something is pushed when it is not. Verify with:

    git rev-parse HEAD
    git rev-parse origin/<assigned-branch>    # must equal HEAD after a successful push

    If those two SHAs differ, your latest work is not on GitHub.

A1 — SESSION FRAGILITY (the workspace is one chatroom)

    A session can end at any moment: a PR is merged or closed, a timeout, a disconnect, or the platform closing the session.
    The moment a session ends, git push and gh are permanently blocked in that session. You cannot recover remote access by trying again in the same chat.
    Because of this, never batch work hoping to push later. Complete one small, validated unit, then commit and push immediately.
    Treat every change as potentially the last thing you can push.

A2 / C2 — PULL REQUEST LIFECYCLE

    Open a draft pull request early, immediately after the first push, so GitHub holds a recoverable route even if the chatroom dies.
    Keep the PR open. Do not close it unless you are merging it.
    Closed ≠ Merged. A PR that is "closed" without a merge means:
        the work is not live;
        the session's remote access is cut off;
        remaining local commits can no longer be pushed from that session.
    The owner controls the final merge. If the owner has not explicitly told you to merge, leave the PR open and report its state.
    If a PR is closed without merging:
        Create a record file PR_#_NEVER_MERGED.md at the repo root explaining that it was closed, not merged, and that the work is not live.
        Report the closed PR and the unpushed commits clearly.
        A new session is required to push the remaining commits and open a fresh PR.
    Direction is always:

    base: main   ←   compare: assigned session branch

    Never reverse these.

A3 — ASSET CACHE-BUSTING (mandatory for CSS/JS changes)

    Any change to docs/assets/css/wiki.css or docs/assets/js/wiki.js MUST bump ASSET_VERSION in tools/sync_global_top_bar.py:

    ASSET_VERSION = "YYYYMMDDx"   # e.g. "20260901a" — change the suffix every time

    Then re-sync all pages so the ?v= query updates:

    python3 tools/sync_global_top_bar.py docs --write

    Reason: the pages load wiki.css?v=<version>. If the version string does not change, returning visitors keep the old cached file and your fix never appears live, even after deploy.
    Never change the stylesheet without bumping the version in the same commit.

A4 — SIDEBAR / VISUAL PARITY

    The left sidebar is canonical and generated by tools/sync_global_left_sidebar.py. Its markup must match on all public pages.
    The right sidebar (homepage Facility 01 floor console, body.home-page .floor-rail) must match the left rail's L-Corp terminal presentation: same layered dark gradient, accent strips, signal headers, coded rows, and hover behavior.
    Sidebar bugs are fixed in docs/assets/css/wiki.css — not in the HTML.
    Canonical component blocks belong at the END of the stylesheet so they win the cascade over the many older duplicate rules. Verify with the cascade check and git diff --check.
    The left rail must remain a permanent, full-height, non-scrolling, non-shrinking column on desktop (fixed width, position: static, no max-height scroll box).

A5 — FILE SAFETY (never delete the owner's work)

    Never delete, rename, or move the repository root or .git.
    Never run git clean, git reset --hard, git checkout -- ., or force-push.
    Never delete or overwrite an owner file (including README.md, CHANGELOG.md, RULE-TO-FOLLOW.md) without a direct instruction that names the exact file.
    When the owner says they will delete/replace a root .md, do NOT delete it yourself — create the new file under a distinct name (e.g. _v2.md) and let the owner copy it in.

1. Use main as the permanent integration branch

    main receives completed work.
    Do not rename a temporary branch to main, replace or delete main, create extra branches, use branch chains, or force-push.
    Arena may create and lock a session branch. When it does:
        stay on that branch,
        create no other branch,
        commit and push only that branch,
        open one PR from it into main.
    Direction: main ← assigned branch. Never reverse.

2. Make every session push-resistant

At session start, report:

git branch --show-current
git status --short

Then, for every coherent unit of work:

    Make the change.
    Run the relevant checks.
    git add and git commit.
    git push origin <assigned-branch> immediately — do not wait for the end of the turn.
    Open/refresh a draft PR into main early.
    Continue pushing each later validated commit to the same branch.
    Only the owner triggers the final merge (unless explicitly told to merge).
    End every turn with a clean git status and HEAD == origin/<branch>.

Every newly created file and every validated change must be pushed in the same turn. Never stop at "committed locally."
3. Manual recovery if a chatroom stops before merge

    Open the repository's Pull requests page.
    New pull request.
    base = main; compare = the assigned temporary branch.
    Review Files changed.
    Create the PR, wait for checks, Merge, then optionally delete the branch.
    Verify at the public acceptance URL.

If a PR already exists, continue from step 4 — do not duplicate it. If the branch is missing from GitHub, the work was never pushed (or was deleted too soon). Recreate from a local commit if available; never claim an unpushed commit is recoverable from GitHub.
4. Verify the actual GitHub Pages source

    Merging into main and publishing GitHub Pages are separate facts.
    Confirm the Pages source is main and path /docs.
    If Pages points elsewhere, report the mismatch and ask the owner to set Settings → Pages → Deploy from a branch → main → /docs.
    Never change the Pages source silently.

5. The live website is the final acceptance surface

The owner checks at https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/.

    Wait for the Pages deployment to finish after merge.
    Fetch the URL with a cache-busting query: https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/?verify=COMMIT-SHA.
    Confirm a distinctive marker from the new work.
    Check nested pages and assets, not only the homepage.
    Do not say "live" until those checks pass.

Report states separately and truthfully:

LOCAL ONLY
COMMITTED LOCALLY
NOT PUSHED (with blocker)
PUSHED TO TEMPORARY BRANCH
PULL REQUEST OPEN
PR CLOSED (NOT MERGED)
MERGED INTO MAIN
PAGES BUILDING
VERIFIED LIVE

6. Preserve the Somnarak publication standards

    Release version remains 1.8.31 unless the owner changes it.
    Preserve 197 public HTML files unless the owner approves a route change.
    Every public page must have at least 200 meaningful editorial words (a floor, not a target).
    No page may be plain, generic, filler-driven, or a title/color-swapped template.
    Read REFERENCE_SOMNARAK_WIKI/PROJECT_MOON_WIKI_NESTED_PLACEMENT_RESEARCH.md before changing placement or information architecture.
    SVG design must derive from page content and title; icons/banners/backgrounds/profiles/silhouettes/diagrams/maps allowed.
    Profiles do not require faces, but every visual must be identifiable to its subject.
    Recoloring the same SVG does not count as personalization.
    Canonical top bar, homepage-derived left sidebar, and expanded bottom bar must match on every public page.
    Shared chrome does not count as a page's personalized visual treatment.

Standards live in:

    REFERENCE_SOMNARAK_WIKI/CONTENT_AND_VISUAL_STANDARDS.md
    REFERENCE_SOMNARAK_WIKI/OPERATING_RULES.md
    REFERENCE_SOMNARAK_WIKI/MASTER_HANDOFF_PROTOCOL.md
    REFERENCE_SOMNARAK_WIKI/LIVE_DEPLOYMENT_AND_BRANCH_POLICY.md

7. Required checks before merge

From the repository root:

python3 tools/audit_page_word_floor.py
python3 tools/sync_global_top_bar.py
python3 tools/sync_global_left_sidebar.py
python3 tools/sync_global_bottom_bar.py
python3 tools/audit_site_structure.py
python3 tools/audit_svg_compositions.py
python3 -m py_compile tools/*.py
node --check docs/assets/js/wiki.js
git diff --check

For website-wide chrome changes, also serve docs/ locally and confirm all 197 HTML routes return HTTP 200, and visually review desktop + mobile widths when browser tooling is available.

Do not merge known failures. Do not hide failed checks. Do not report local validation as live-site verification.
8. Required completion report

Every session must end with a concise factual report:

Active branch: <name>
Commit: <full or short SHA>
Push: <pushed / NOT PUSHED (state exact blocker)>
Pull request: <none / URL / CLOSED-NOT-MERGED>
Merged into main: <yes / no>
Pages source: <branch:/path or unverified>
Live verification URL: <URL or not verified>
Distinctive live marker: <marker or not verified>
Temporary branch deleted: <yes / no>
Working tree clean: <yes / no>
Checks: <passed checks and any failures>

Never collapse these states into the single word "done."
