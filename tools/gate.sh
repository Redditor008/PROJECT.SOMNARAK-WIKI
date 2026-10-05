#!/usr/bin/env bash
# gate.sh "<commit message>" — the standing quality gate.
#
#   sync -> linters (explicit PASS strings, R-11) -> unit tests -> row-pipe check
#        -> breach floors (R-28) -> metrics parity (regenerated and staged)
#        -> commit -> push -> verify HEAD == origin/<branch>.
#
# The push target is whatever session branch is checked out. It is never
# hard-coded: a hard-coded branch name once pointed this script at an earlier
# session's branch, which would have pushed the current session's commits to
# the wrong place. main and NON-WIKI are integration branches and are refused.
set -u
MSG="${1:?commit message required}"
cd "$(dirname "$0")/.." || exit 1

BRANCH="$(git branch --show-current)"
case "$BRANCH" in
  ''|main|NON-WIKI)
    echo "REFUSED: '${BRANCH:-detached HEAD}' is not an assigned session branch."
    echo "gate.sh commits and pushes only to the checked-out session branch."
    exit 1;;
esac

# R-11: sync with the remote branch first. Local history truncates between
# turns; the reset is a no-op when history is intact and a repair when it is
# not. It only ever moves HEAD forward (never drops a local-only commit).
if git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
  git fetch -q origin "$BRANCH" 2>/dev/null
  if git merge-base --is-ancestor HEAD FETCH_HEAD 2>/dev/null; then
    git reset -q --mixed FETCH_HEAD
  else
    echo "BLOCKED: local HEAD is ahead of, or has diverged from, origin/$BRANCH."
    echo "Push or reconcile before gating; nothing was committed."
    exit 1
  fi
fi

fail=0

# check <expected PASS string> <command...>
# A gate passes only when it exits 0 AND prints its explicit PASS string.
# Exit status alone is not trusted (R-11: a linter once printed violations
# and still exited 0).
check() {
  local pat="$1"; shift
  local out rc
  out="$("$@" 2>&1)"; rc=$?
  if [ "$rc" -ne 0 ] || ! printf '%s' "$out" | grep -qF -- "$pat"; then
    echo "GATE FAILED: $* (exit $rc, expected: $pat)"
    printf '%s\n' "$out" | tail -6
    fail=1
  fi
}

check "RESULT: PASSED"                                   python3 tools/check_box_symmetry.py
check "OVERALL LORE HEALTH: PASS"                        python3 tools/audit_lore_archive.py
check "[PASS] 0 timeline contradictions"                 python3 tools/timeline_lint.py
check "[PASS] 0 semantic seams"                          python3 tools/seam_lint.py
check "BROKEN TOTAL: 0"                                  python3 tools/check_links.py
check "[PASS] 0 label or code-tag violations found!"     python3 tools/label_lint.py
check "RESULT: PASSED"                                   python3 tools/text_box_double_checker.py

if [ -f tools/tests/test_linters.py ]; then
  check "OK" python3 -m unittest discover -s tools/tests -q
fi

# every table row in a touched dossier must close with a pipe.
# `core.quotepath=off` is load-bearing: by default git prints a non-ASCII path
# quoted and octal-escaped, so the `SOMNARAK-WORLD/*.md` pattern below never
# matched a dossier (every dossier name carries Greek or Hangul) and this check
# was silently skipped for all of them. Deleted files are skipped (-f test).
while IFS= read -r f; do
  [ -f "$f" ] || continue
  case "$f" in SOMNARAK-WORLD/*.md)
    python3 - "$f" <<'PY' || fail=1
import io,sys
bad=[l for l in io.open(sys.argv[1],encoding='utf-8').read().split('\n')
     if l.startswith('|') and not l.rstrip().endswith('|')]
if bad:
    print('PIPE FAILED: %s' % sys.argv[1])
    for l in bad[:5]: print('   %s' % l[:90])
    sys.exit(1)
PY
  ;; esac
done < <(git -c core.quotepath=off diff --name-only; git -c core.quotepath=off diff --cached --name-only)

python3 tools/breach.py >/tmp/gate.breach 2>&1 || { echo "BREACH FLOORS UNMET (R-28)"; cat /tmp/gate.breach; fail=1; }

# Metrics parity (R-11 step 8 / the CI 'SSOT Parity' step). The generators are
# the single source of truth: regenerate here so the three generated files
# travel with the commit and CI's `git diff --exit-code` has nothing to find.
python3 tools/generate_canonical_metrics_registry.py >/tmp/gate.metrics 2>&1 \
  || { echo "METRICS GENERATOR FAILED"; tail -5 /tmp/gate.metrics; fail=1; }
python3 tools/sync_readme_metrics.py >>/tmp/gate.metrics 2>&1 \
  || { echo "README METRICS SYNC FAILED"; tail -5 /tmp/gate.metrics; fail=1; }

[ "$fail" -eq 0 ] || { echo "GATE BLOCKED — nothing committed"; exit 1; }
echo "OK"
echo "metrics parity: regenerated and staged"

git add -A
git commit -q -m "$MSG" || echo "(nothing to commit)"
git push -q origin "$BRANCH" 2>&1 | tail -2

# Never claim a push that did not happen: compare HEAD with the remote ref.
LOCAL="$(git rev-parse HEAD)"
REMOTE="$(git ls-remote origin "refs/heads/$BRANCH" 2>/dev/null | cut -f1)"
if [ "$LOCAL" = "$REMOTE" ]; then
  echo "PUSH VERIFIED: $LOCAL -> origin/$BRANCH"
  rc=0
else
  echo "NOT PUSHED: local $LOCAL, origin/$BRANCH ${REMOTE:-absent}"
  rc=2
fi
echo "dirty: $(git status --short | wc -l | tr -d ' ')"
git log --oneline -1
exit "$rc"
