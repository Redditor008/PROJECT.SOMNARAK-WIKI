# Run the Full Gate Set Before Every Push

**The rule.** The pre-push chain and the CI chain are the same chain. It runs in full before every push, in order, and each gate's explicit PASS string is read.

**The chain.**

1. `check_box_symmetry.py` → ` RESULT: PASSED`
2. `audit_lore_archive.py` → ` OVERALL LORE HEALTH: PASS`
3. `timeline_lint.py` → `[PASS] 0 timeline contradictions`
4. `seam_lint.py` → `[PASS] 0 semantic seams`
5. `check_links.py` → `BROKEN TOTAL: 0`
6. `label_lint.py` → `[PASS] 0 label or code-tag violations found!`
7. `python3 -m unittest tools/tests/test_linters.py` → `OK`
8. `generate_canonical_metrics_registry.py` + `sync_readme_metrics.py`, then `git diff --exit-code` on the three generated files → metrics parity

**Order matters.** `git fetch origin <branch>` and `git reset --mixed FETCH_HEAD` run **first**, before the generators. Local history has truncated between turns seven times; the reset is a no-op when history is intact and a repair when it is not. Detector: `git rev-parse HEAD FETCH_HEAD | uniq | wc -l` returns 2 when truncated.

**Two traps.**

- `set -e` does not abort on a failing left-hand side of `&&`. `cmd && echo PASS` silently skips the echo and continues. Read for the presence of each PASS string rather than trusting the exit code.
- `label_lint.py` exits 0 while printing violations. This caused one broken gate to be pushed. Grep its output.

**Never force-push.** Blemishes in pushed history are disclosed and left standing.
