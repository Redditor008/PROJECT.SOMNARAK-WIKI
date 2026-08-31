# Somnarak Wiki — Live Deployment and Branch Continuity Policy

**Effective:** 2026-08-31  
**Authority:** Direct project-owner instruction  
**Status:** Binding operating rule for every current and successor coding session

This policy records why the public URL was supplied and how repository branches must be handled without creating avoidable clutter.

## Rule 1 — The live GitHub Pages URL is the acceptance surface

The canonical public site is:

> https://redditor008.github.io/PROJECT.SOMNARAK-WIKI/

The project owner uses this URL to inspect every update. Localhost, an Arena preview, a clean audit, a local commit, a pushed feature branch, and an open pull request are intermediate states; none proves that the requested change is live.

Any task that changes `docs/` is not deployment-complete until the following sequence is handled honestly:

1. Run the relevant local publication gates.
2. Commit the changes and push the branch permitted by the active coding environment.
3. Integrate that work into the branch and directory currently configured as the GitHub Pages source.
4. Wait for the Pages build to complete or report explicitly that it is still pending.
5. Fetch the canonical live URL with a cache-busting query and verify a distinctive marker from the requested change.
6. Fetch each directly changed public route or newly referenced public asset when the task is narrower than a site-wide change.
7. State separately whether work is local, committed, pushed, merged, building, or verified live. Never collapse those states into the word “done.”

A completion report that says “live” must name the URL checked and the marker observed there. An HTTP 200 by itself is insufficient when it could still be serving the previous build. If remote access is unavailable, a pull request is unmerged, or Pages has not rebuilt, say that the change is **not yet live**.

The public page may retain cached HTML or CSS briefly. Use a query such as `?deploy=<commit>` for verification and instruct the owner to hard-refresh after the new marker is visible from an independent fetch.

## Rule 2 — Use the established Pages branch when the environment permits

At the time this policy was written, GitHub Pages publishes `/docs` from:

> `arena/01a04eea-project-somnarak-wiki`

Before publishing, query the current Pages configuration rather than assuming this value can never change. When the coding environment permits direct work on the established Pages source branch, continue using that branch instead of creating a new ad-hoc branch.

Do not manually create throwaway, experiment, release, fix, or duplicate Arena branches merely to perform routine wiki updates. Branch names must not be invented for convenience when an established integration branch already exists.

## Rule 3 — Arena-assigned branches are an explicit exception, not permission for more branches

Arena Agent Mode may create and lock a new session to a platform-assigned branch before the agent begins work. An agent cannot silently switch that session to the established Pages branch when the environment requires the assigned branch.

When that restriction applies:

1. Use only the one branch assigned to the session.
2. Do not create any additional branch.
3. Open the pull request directly from the assigned branch into the configured Pages source branch—not into an unrelated intermediate branch.
4. Merge only when the owner requests it or repository policy already grants that authority.
5. Verify the live Pages URL after merge; do not stop at the pull request.
6. If the platform closes remote access after merge, do not pretend that later local edits were published. Start a new coding session for further GitHub changes.

The existence of an Arena-assigned branch should be described accurately as platform-managed. Future agents must not claim that they chose to create it, nor promise that repository instructions can prevent Arena from assigning one in a new chatroom.

## Rule 4 — Keep branch clutter bounded

For each task, prefer one working branch and one direct integration pull request. Never build chains such as feature → staging → previous Arena branch → Pages branch unless the owner explicitly requests that topology.

After a pull request is merged and live verification succeeds, no successor should reuse the merged branch for unrelated work merely because it exists. Remote branch deletion is a repository-maintenance action and must only be performed when the active platform allows it and the owner authorizes it; never delete the branch currently required by GitHub Pages.

## Required completion language

Use an explicit state report:

```text
Local gates: PASS / FAIL
Commit: <hash or NOT COMMITTED>
Push: <branch or NOT PUSHED>
Pull request: <URL and state, or NONE>
Pages source: <branch>:<path>
Deployment: PENDING / FAILED / VERIFIED LIVE
Live verification: <public URL and distinctive marker>
```

This policy supplements `OPERATING_RULES.md`, `MASTER_HANDOFF_PROTOCOL.md`, and `CONTENT_AND_VISUAL_STANDARDS.md`. If an older note implies that a local preview or pushed branch is enough, this policy supersedes it.
