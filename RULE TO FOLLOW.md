# RULE TO FOLLOW

**Authority:** Direct project-owner instruction  
**Status:** Mandatory for every future AI, coding session, pull request, and deployment  
**Repository:** `Redditor008/PROJECT.SOMNARAK-WIKI`  
**Integration branch:** `main`  
**Public acceptance URL:** <https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/>

Read this file before changing anything. These rules are not optional. If an older branch or deployment instruction elsewhere in the repository conflicts with this file, **this root-level file is the newer owner instruction and takes precedence**. Content, canon, placement, and visual-quality rules in the referenced standards remain binding.

---

## 1. Use `main` as the permanent integration branch

The owner has selected **`main`** as the branch that receives completed work.

- Do not rename a temporary branch to `main`.
- Do not replace or delete `main`.
- Do not manually create another branch.
- Do not use a chain of intermediate branches.
- Do not force-push.
- Do not merge `main` into an unrelated branch and call that deployment.

Arena may create and lock a session to a temporary branch before the AI starts. Repository instructions cannot prevent that platform-created branch. When Arena assigns one:

1. Stay on that assigned branch.
2. Create no additional branch.
3. Commit and push only the assigned branch.
4. Open one pull request directly from the assigned branch into `main`.
5. Merge the pull request after the requested work and validation gates pass.
6. Delete the temporary branch only after the merge succeeds.

The required direction is:

```text
base:    main
compare: Arena-assigned temporary branch

Arena branch  ──pull request──>  main
```

Never reverse those two selections.

---

## 2. Make every session resistant to a broken chatroom

At the beginning of the session, report the output of:

```bash
git branch --show-current
git status --short
```

Then follow this workflow:

1. Complete one coherent unit of work.
2. Run the relevant checks.
3. Commit the validated unit immediately.
4. Push it to the one Arena-assigned branch while remote access remains available.
5. Open a **draft pull request into `main` early**, so GitHub retains a recoverable route even if the chatroom stops unexpectedly.
6. Continue pushing later validated commits to that same branch and draft pull request.
7. When all requested work passes, mark the pull request ready and merge it into `main`.
8. Do not wait for a separate “please merge” message when the owner’s initial request explicitly authorizes completion and deployment.
9. Delete the temporary branch after merge, preferably through GitHub’s **Automatically delete head branches** setting.

Files must exist in a Git working tree before Git can commit them, so literally avoiding the workspace is impossible. Apply the owner’s intent this way: never leave finished work only as uncommitted files. Do not commit a knowingly broken partial merely for speed; validate first, then commit immediately. End completed work with a clean `git status`.

**Every newly created file and every coherent validated change must be pushed in the same turn as its commit whenever remote access is available. Never stop at “committed locally” when pushing is possible.** In Arena, push to the one platform-assigned session branch and then integrate it into `main` through the direct pull request described above. If authentication, a closed session, or another platform restriction makes pushing impossible, do not pretend it succeeded: report `NOT PUSHED`, state the exact blocker, and require a new active coding session.

Once a session branch has been merged and deleted, that coding session is finished. Start a new coding session before requesting another code change.

---

## 3. Manual recovery if a chatroom stops before merge

If the temporary branch was pushed to GitHub:

1. Open the repository’s **Pull requests** page.
2. Select **New pull request**.
3. Set **base** to `main`.
4. Set **compare** to the Arena temporary branch containing the work.
5. Review **Files changed**.
6. Create the pull request.
7. Wait for required checks, if any.
8. Select **Merge pull request** and confirm.
9. Delete the temporary branch.
10. Verify the result at the public acceptance URL.

If a pull request already exists, open it and continue from step 5. Do not create a duplicate pull request.

If the branch is missing from GitHub, its work was never pushed or was deleted too soon. GitHub cannot merge a branch it does not have. Recover the original Arena workspace/local commit if available; otherwise the change must be recreated. Never claim an unpushed local commit is recoverable from GitHub.

---

## 4. Verify the actual GitHub Pages source

Merging into `main` and publishing GitHub Pages are separate facts. Before deployment, inspect the repository’s current Pages configuration and confirm which branch/path it serves.

The intended public content lives in:

```text
main:/docs
```

If GitHub Pages still points to another branch, do not report a merge into `main` as live. Report the mismatch and ask the owner to configure **Settings → Pages → Deploy from a branch → `main` → `/docs`**, unless the owner explicitly chooses another source.

Never change the Pages source silently.

---

## 5. The live website is the final acceptance surface

The owner checks every update at:

> <https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/>

A local preview, commit, pushed branch, open pull request, successful merge, or HTTP 200 response does not by itself prove that the new version is live.

After merge:

1. Wait for the GitHub Pages deployment to finish.
2. Fetch the public URL with a cache-busting query, for example:

   ```text
   https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/?verify=COMMIT-SHA
   ```

3. Confirm a distinctive marker introduced by the new work.
4. Check relevant nested pages and assets, not only the homepage.
5. Do not say “live” until those checks pass.

Report these states separately and truthfully:

```text
LOCAL ONLY
COMMITTED LOCALLY
PUSHED TO TEMPORARY BRANCH
PULL REQUEST OPEN
MERGED INTO MAIN
PAGES BUILDING
VERIFIED LIVE
```

---

## 6. Preserve the Somnarak publication standards

The following requirements remain binding:

- Release version remains **1.8.31** unless the owner explicitly changes it.
- Preserve the verified **197 public HTML files** unless the owner approves a route change.
- Every public page must contain at least **200 meaningful editorial words**; 200 is a floor, not a target or maximum.
- No page may be plain, generic, filler-driven, or a title/color-swapped template.
- Read `REFERENCE_SOMNARAK_WIKI/PROJECT_MOON_WIKI_NESTED_PLACEMENT_RESEARCH.md` before changing page placement or information architecture.
- SVG design must derive from the page’s written content as well as its title.
- SVGs may be icons, banners, backgrounds, profiles, silhouettes, diagrams, maps, or other page-specific forms.
- Profiles do not require faces, but every visual must remain personally identifiable to its subject.
- Recoloring the same SVG composition does not count as personalization.
- The canonical top bar must match on every public page.
- The homepage-derived left sidebar must match on every public page.
- The expanded canonical bottom bar must match on every public page.
- Shared chrome does not count as a page’s personalized visual treatment.

Read the full standards in:

- `REFERENCE_SOMNARAK_WIKI/CONTENT_AND_VISUAL_STANDARDS.md`
- `REFERENCE_SOMNARAK_WIKI/OPERATING_RULES.md`
- `REFERENCE_SOMNARAK_WIKI/MASTER_HANDOFF_PROTOCOL.md`
- `REFERENCE_SOMNARAK_WIKI/LIVE_DEPLOYMENT_AND_BRANCH_POLICY.md`

---

## 7. Required checks before merge

Run the relevant publication gates from the repository root:

```bash
python3 tools/audit_page_word_floor.py
python3 tools/sync_global_top_bar.py
python3 tools/sync_global_left_sidebar.py
python3 tools/sync_global_bottom_bar.py
python3 tools/audit_site_structure.py
python3 tools/audit_svg_compositions.py
python3 -m py_compile tools/*.py
node --check docs/assets/js/wiki.js
git diff --check
```

For website-wide chrome changes, also serve `docs/` locally and verify all 197 HTML routes return HTTP 200. Perform visual review at desktop and mobile widths when browser tooling is available.

Do not merge known failures. Do not hide failed checks. Do not report local validation as live-site verification.

---

## 8. Required completion report

Every future AI must finish with a concise factual report containing:

```text
Active branch: <name>
Commit: <full or short SHA>
Push: <not pushed / pushed>
Pull request: <none / URL>
Merged into main: <yes / no>
Pages source: <branch:/path or unverified>
Live verification URL: <URL or not verified>
Distinctive live marker: <marker or not verified>
Temporary branch deleted: <yes / no / automatic deletion pending>
Working tree clean: <yes / no>
Checks: <passed checks and any failures>
```

Never collapse these states into the single word “done.”
