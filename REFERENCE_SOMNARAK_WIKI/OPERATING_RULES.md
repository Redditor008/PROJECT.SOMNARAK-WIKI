# SOMNARAK — OPERATING RULES FOR THE AGENT WHO COMMITS
**Applies because:** the AI session performs every commit and push. The human does not.
**Repo:** `Redditor008/PROJECT.SOMNARAK-WIKI` · **State as written:** 2026-08-30 ~13:00 UTC
**Full audit context:** `somnarak/SOMNARAK_STATE.md` §0. This file adds the git/branch rules that
postdate it. Where the two disagree, this file wins — it is newer and it is about pushing, not building.

```
main    8d58b3b   3,990 files   root: .gitignore  01_Somnarak_Wiki/  README.md  REFERENCE_SOMNARAK_WIKI/
        index.html at root: NO      .nojekyll: NO      FOR_WIKI.zip: YES (13.66 MiB)
arena/01a04eea-…  0d89b5bf   4,023 files   root: + .nojekyll  index.html  docs/  01_Somnarak_Wiki.zip
        index.html at root: YES     .nojekyll: YES     FOR_WIKI.zip: NO  ← it deleted the corpus
        ahead of main by 36, behind 0        has_pages: False       repo .git: 106.7 MiB
```

---

## RULE 0 — Content depth and visual identity are blocking publication gates.

`CONTENT_AND_VISUAL_STANDARDS.md` records the project owner’s binding 2026-08-31 direction and supersedes older quality language elsewhere in the archive:

- every public HTML page contains at least **200 meaningful editorial words**, excluding shared chrome; 200 is a floor, never a ceiling;
- no page may be plain, generic, or produced by swapping a title and color into a repeated body template;
- every SVG is designed only after reading the complete page and relevant source, and must use details from that writing rather than the title alone;
- SVG work includes icons, banners, backgrounds, profiles, silhouettes, diagrams, and other page-specific visual forms;
- profiles may be non-facial, but every silhouette or shape must remain specific to its subject;
- recolor-only or geometry-identical SVG variants fail review.

Do not publish or report completion until the page and visual checklist in that document passes.

## RULE 1 — Never force-push, ever. Especially not arena → main.

`main` is currently the **only** branch containing `FOR_WIKI.zip`, the 13.66 MiB archive that holds
the 62-of-65 sha256-verified source corpus. The working branch already deleted it once. Any
`git push --force`, `--force-with-lease`, branch reset, or "make main match my branch" operation
**destroys the only verified copy of the project's sources.**

```bash
git push origin --force              # NEVER
git push origin HEAD:main --force    # NEVER — this specifically deletes FOR_WIKI.zip
git checkout main && git reset --hard origin/arena/...   # NEVER
```

To move work onto `main`, use a fast-forward merge only, and **abort if it isn't one**:

```bash
git fetch origin
git rev-list --count main..origin/arena/01a04eea-project-somnarak-wiki   # expect 36 or higher
git rev-list --count origin/arena/01a04eea-project-somnarak-wiki..main   # MUST be 0
# if the second number is not 0: STOP. main has commits the branch lacks. Report, do not merge.
git merge --ff-only origin/arena/01a04eea-project-somnarak-wiki && git push origin main
```

## RULE 2 — Prove the corpus survived, every single push.

Run this before and after each push. If the count changes from 1 to 0, revert immediately.

```bash
git ls-files | grep -c 'FOR_WIKI.zip'    # must stay ≥ 1 on main
```

`FOR_WIKI.zip` has a **corrupt central directory** (301 entries disagree with their local headers,
UTF-8 name flag unset). If you ever need to read it, read entries from their local header —
`zf.open(name)` raises `BadZipFile` on Python 3.13+. Working implementation: `somnarak/recover_sources.py`.

## RULE 3 — Stop the 106 MB bleed. Never commit a generated archive.

Repo history went 37.1 → 58.2 → **106.7 MiB in about a day**, mostly from `01_Somnarak_Wiki.zip`
(5.35 MiB, shrinking each run) being regenerated and re-committed by
`REFERENCE_SOMNARAK_WIKI/tools/update_wiki_zip.py`. ZIPs do not delta-compress, so every wiki edit
adds a fresh full-size blob to history **permanently** — no later commit can reclaim it.

```bash
# one-time cleanup; keep FOR_WIKI.zip, delete the auto-generated one and its generator
git rm -f 01_Somnarak_Wiki.zip REFERENCE_SOMNARAK_WIKI/tools/update_wiki_zip.py
printf '\n# never version a regenerated archive\n*.zip\n!01_Somnarak_Wiki/downloads/FOR_WIKI.zip\n' >> .gitignore
git add .gitignore
```

If a downloadable wiki bundle is wanted, publish it as a **GitHub Release asset** (2 GB limit,
does not touch repo history) or have visitors use GitHub's own `/archive/main.zip` download —
which already exists, is always current, and costs you zero bytes.

## RULE 4 — GitHub Pages: pick the branch that can actually serve.

`main` has no root `index.html`, so Pages-from-main-root today renders only the README. Choose one:

- **Fastest, zero git changes:** enable Pages on `arena/01a04eea-project-somnarak-wiki` / Root.
  It has `index.html`, `docs/index.html` and a root `.nojekyll`. Works immediately.
- **Correct:** Rule 1's ff-merge first, then `main` / Root.
- Pages cannot be enabled from inside a sandbox without a token. If you have write scope:
  ```bash
  curl -s -X POST -H "Authorization: Bearer $GH_TOKEN" -H "Content-Type: application/json" \
    -d '{"source":{"branch":"main","path":"/"}}' \
    https://api.github.com/repos/Redditor008/PROJECT.SOMNARAK-WIKI/pages
  ```
  If that returns 401, tell the human it's a Settings click — do not fake it or claim it's live.

`.nojekyll` must be at the **root of the publishing source** or Jekyll will process the tree and
strip `_`-prefixed files. After enabling, verify by fetching the URL — not by the commit message.

## RULE 5 — Netlify is dead. Do not restore it.

`project-somnarak-wiki.netlify.app` returns `404 "Not Found"` for every path, which is a deleted
site, not a paused deploy. `netlify.toml` (`publish = "docs"`) is inert config. Do not "fix" it, do
not re-link it, and do not build workflow around a host that pauses on metered credits.

## RULE 6 — Report a commit honestly, or not at all.

Every completion report must include:

```bash
git log --oneline -1 && git status --short | wc -l && git rev-list --count origin/main..HEAD
```

and state the URL that returns 200 if claiming deployment. The previous session's
`"Publish static site at root; add .gitignore"` (8d58b3b) **moved nothing** — the commit message was
written from intent, not from a verified tree. That is the failure mode this rule exists to kill:
`git mv A/* .` silently no-ops on conflict, and the message still sounded like success.

## RULE 7 — Sandbox budget still applies to you, even though GitHub is the store.

```
checkout of this repo today: 4,023 files · ~97 MB with .git
sandbox caps              : 10,000 files · 128 MB → 40% / 78% spent BEFORE you start
```
Extract nothing into the repo or workspace (`/tmp` only). Never materialise the corpus as ~1,862
loose files in a session that will also do work — that is precisely how 3,754 files were lost once.
Commit state to git; git is the durable store, the sandbox is a conveyor belt.

---

## Definition of done — per session, all five lines

```
[ ] git ls-files | grep -c 'FOR_WIKI.zip'  ≥ 1 on main
[ ] pushed branch, `git status --short | wc -l` = 0
[ ] no new *.zip tracked (except never: FOR_WIKI.zip is exempt and frozen)
[ ] if Pages was claimed: an HTTP 200 from the live URL, pasted
[ ] no force-push occurred; if main ≠ ff-ancestor, escalated instead of merging
```

**The single most important line here is RULE 1.** Everything else is housekeeping. Deleting the
corpus is the one unrecoverable act available to you in this repository, and the branch you were
told to trust already did it once.
