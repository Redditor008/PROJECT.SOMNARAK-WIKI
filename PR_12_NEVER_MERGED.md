# PR #12 — CLOSED, NOT MERGED (work is live; nothing is lost)

**Required by** `RULE-TO-FOLLOW.md` §A2.5 / §C2.5 ("if a PR is closed without merging, create
`PR_#_NEVER_MERGED.md` at the repo root"). Recorded 2026-10-05 by the session on
`arena/01a10bcc-project-somnarak-wiki`.

## The PR

| Field | Value |
|---|---|
| Number | **#12** |
| Title | *NON-WIKI: continue WIP — Workstream 9 (R-29) 27→54/301, Study 02, Dawn of Mourning pair resolved, R-01 sweep begun, gate sync hazard fixed* |
| Base | `NON-WIKI` |
| Head branch | `arena/01a109ec-project-somnarak-wiki` |
| Head commit | `408797c30d5343e082b33edc0c5b68b0c0907d22` |
| State | **CLOSED** (closed 2026-10-05T11:20:05Z), not merged |

## Is any work lost? No.

The PR's head commit `408797c30d5343e082b33edc0c5b68b0c0907d22` **is the tip of the `NON-WIKI`
branch** on `origin`:

```
$ git ls-remote origin refs/heads/NON-WIKI
408797c30d5343e082b33edc0c5b68b0c0907d22      refs/heads/NON-WIKI
```

Every commit the PR carried is therefore already inside the integration branch. This is the one
case the rule's standard wording does not cover: the PR was closed rather than merged, but the
work **is live**, so no recovery action and no re-application is required.

## Why this file exists

So that the next session does not read `CLOSED` on PR #12, conclude that the Workstream 9 work was
lost, and re-apply or redo it. Do not re-run those units:

- Do **not** re-apply PR #12 as a patch — its commits are in `NON-WIKI` and would conflict or
  duplicate.
- Do **not** reopen or resurrect `arena/01a109ec-project-somnarak-wiki`; Arena assigns one branch
  per session and that session is over.
- The successor session (`arena/01a10bcc-project-somnarak-wiki`) branches from that same head and
  continues from `REFERENCE_SOMNARAK_WIKI/WORK_IN_PROGRESS.md`.

## Standing lesson (kept here, per `R-17` history is not rewritten)

The branch was pushed and then closed; the durable record survives only because the commits had
already been pushed. The push-first rule (`A0`/`A1`) is what made this a non-event, and
`tools/gate.sh` verifies `HEAD == origin/<branch>` after every commit for exactly this reason.
