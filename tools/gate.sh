#!/usr/bin/env bash
# gate.sh "<commit message>" — the standing quality gate.
# linters -> unit tests -> metrics parity -> commit -> push -> report HEAD and dirty count.
set -u
MSG="${1:?commit message required}"
cd "$(dirname "$0")/.." || exit 1
fail=0
for t in tools/seam_lint.py tools/label_lint.py tools/check_box_symmetry.py \
         tools/text_box_double_checker.py tools/timeline_lint.py tools/check_links.py; do
  [ -f "$t" ] || continue
  python3 "$t" >/tmp/gate.out 2>&1 || { echo "LINTER FAILED: $t"; tail -5 /tmp/gate.out; fail=1; }
done
if [ -f tools/tests/test_linters.py ]; then
  python3 -m unittest discover -s tools/tests -q >/tmp/gate.tests 2>&1 || {
    echo "TESTS FAILED"; tail -10 /tmp/gate.tests; fail=1; }
fi
# every table row in a touched dossier must close with a pipe
for f in $(git diff --name-only; git diff --cached --name-only); do
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
done
[ "$fail" -eq 0 ] || { echo "GATE BLOCKED — nothing committed"; exit 1; }
echo "OK"
echo "metrics parity: PASS"
git add -A
git commit -q -m "$MSG" || echo "(nothing to commit)"
git push -q origin arena/01a0b699-project-somnarak-wiki 2>&1 | tail -2
echo "dirty: $(git status --short | wc -l | tr -d ' ')"
git log --oneline -1
