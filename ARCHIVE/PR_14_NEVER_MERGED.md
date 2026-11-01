# PR #14 — CLOSED, NOT MERGED (work is live; nothing is lost)

**Required by** `RULE-TO-FOLLOW.md` §A2.5 / §C2.5 ("if a PR is closed without merging, create
`PR_#_NEVER_MERGED.md` at the repo root"). Recorded 2026-10-25 by the session on
`arena/28e0dc28-project-somnarak-wiki`, continuing where the previous session left off.

## The PR

| Field | Value |
|---|---|
| Number | **#14** |
| Title | *Batch 120: full-SE M.A.W. source review (Hollow Saint, Carrying Nothing, Risus, Every Last Goodbye, Gavel)* |
| Base | `NON-WIKI` |
| Head branch | `arena/954853ad-project-somnarak-wiki` |
| Head commit | `87f1a01546c26499d81846b765d8eefe7aa751bd` |
| State | **CLOSED** (closed 2026-10-25T15:00:46Z), not merged |

## Is any work lost? No.

The PR's head commit `87f1a01546c26499d81846b765d8eefe7aa751bd` **is the tip of the `NON-WIKI`
branch** on `origin`:

```
$ git ls-remote origin refs/heads/NON-WIKI refs/pull/14/head
87f1a01546c26499d81846b765d8eefe7aa751bd      refs/heads/NON-WIKI
87f1a01546c26499d81846b765d8eefe7aa751bd      refs/pull/14/head
```

Every commit the PR carried is therefore already inside the integration branch, including
Batch 179 unit 1 (Mourning a Life I Never Lived). This is the same case as PR #12: the PR was
closed rather than merged, but the work **is live**, so no recovery action and no re-application
is required.

## Why this file exists

So that the next session does not read `CLOSED` on PR #14, conclude that Batches 120–179 were
lost, and re-apply or redo them. Do not re-run those units:

- Do **not** re-apply PR #14 as a patch — its commits are in `NON-WIKI` and would conflict or
  duplicate.
- Do **not** reopen or resurrect `arena/954853ad-project-somnarak-wiki`; Arena assigns one branch
  per session and that session is over. Its branch no longer exists on `origin`.
- The successor session (`arena/28e0dc28-project-somnarak-wiki`) branches from that same head and
  continues Batch 179 from `REFERENCE_SOMNARAK_WIKI/WORK_IN_PROGRESS.md` (OPEN 1 / 5 at recovery).

## Standing lesson (kept here, per `R-17` history is not rewritten)

The branch was pushed and then closed; the durable record survives only because the commits had
already been pushed. The push-first rule (`A0`/`A1`) is what made this a non-event, and
`tools/gate.sh` verifies `HEAD == origin/<branch>` after every commit for exactly this reason.
