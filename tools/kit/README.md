# `tools/kit/` — fix-phase measurement tooling

Session tooling for the Sorrow Entity / Unknown Entity dossier quality
programme. Nothing here edits the archive on its own; every edit is applied by
a unit, in one dossier at a time, and every unit is gated and pushed.

**Why it is committed.** The sandbox is restored at every turn boundary and
untracked files do not survive it — only tracked content persists. The kit was
rebuilt from scratch at the open of four consecutive turns, and each rebuild
reintroduced bugs. It lives in the repository so the numbers are measured the
same way every time.

| Script | What it does |
|---|---|
| `couples.py [BASE] [CODE]` | The wing counter: couples / 301, files carrying, section-pairs, tier split. With a code, prints that file's couples and the section behind each. |
| `attr.py <file> <SECTION> <partner>...` | Row-level attribution: which masked n-grams a section shares with a partner, and how many dossiers hold each. |
| `apply.py <spec.json> <file> [--dry]` | Applies `{"sub", "repl"}` entries line by line. Aborts unless each substring occurs exactly once. |
| `precheck.py <spec> <file> [frags]` | Echo check against the unit's own comparison list. |
| `precheck_all.py <spec> <file>` | Echo check against all 301 dossiers. |
| `unit_np.sh <unit> <file> "<msg>"` | Runs `verify.py`, `tpl.py`, `sectfile.py`, `wikistd.py`, then commits and pushes. Refuses and leaves edits uncommitted on any failure. |

## Measurement rules

`tools.py` wraps `tools/auditors/clone_audit.py` and changes nothing about its
thresholds: `N = 5` shingles, `DISTINCTIVE_MAX = 25` (a gram held by more
dossiers is furniture, not evidence), a section must appear in 20 or more
files, a pair needs 10 shared distinctive grams before it is measured, and a
couple is a section pair at 0.50 or above in **either** direction.

Three traps are worth naming, because each one is silent:

- `files_under()` takes the directory holding `Sorrow_Entities/` and
  `Unknown_Entities/`, which is `<repo>/SOMNARAK-WORLD` and not the repo root.
- `sectfile.py` prints its verdict on the **last** line, after the per-section
  listing.
- Filenames compare only after Unicode normalisation; a designator containing
  γ will not match a byte-for-byte comparison.
