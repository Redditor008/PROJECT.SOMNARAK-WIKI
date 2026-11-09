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

# R-11: sync with the remote branch first. Local history truncates between turns, the sandbox can
# be restored from an older snapshot, and another session may have pushed to the same branch.
# tools/syncbranch.py brings HEAD *and the working tree* level with origin, or refuses and says
# why. The earlier `git reset --mixed FETCH_HEAD` moved HEAD but not the files, so with the
# remote ahead the next `git add -A` would have staged the old files and reverted the other
# session's commits.
if git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
  python3 tools/syncbranch.py \
    || { echo "BLOCKED: this checkout is not level with origin/$BRANCH; nothing was committed."; exit 1; }
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
check "OVERALL STAT BANDS: PASS"                         python3 tools/check_stat_bands.py
check "RESULT: PASSED"                                   python3 tools/text_box_double_checker.py
check "RESULT: PASS (0 crooked boxes)"                   python3 tools/check_box_geometry.py
check "SECTION LOGIC: PASS"                               python3 tools/section_logic.py
check "RESULT: PASS"                                    python3 tools/auditors/compare_conversion_guide.py
check "RESULT: PASS"                                    python3 tools/auditors/check_stock_ceiling.py
check "RESULT: PASS"                                    python3 tools/auditors/check_boilerplate.py
check "RESULT: PASS"                                    python3 tools/auditors/check_event_claims.py
check "RESULT: PASS"                                    python3 tools/auditors/check_dossier_consistency.py
check "RESULT: PASS"                                    python3 tools/auditors/check_sourcing.py
check "RESULT: PASS"                                    python3 tools/auditors/check_set_agreement.py
check "RESULT: PASS"                                    python3 tools/auditors/check_citations.py
check "RESULT: PASS"                                    python3 tools/auditors/check_world_purity.py
check "RESULT: PASS"                                    python3 tools/auditors/check_gauge_chain.py
check "RESULT: PASS"                                    python3 tools/auditors/check_appearance_dupe.py
check "RESULT: PASS"                                    python3 tools/auditors/check_form_line.py
check "RESULT: PASS"                                    python3 tools/auditors/check_ai_prose.py
check "RESULT: PASS"                                    python3 tools/auditors/check_tale_register.py
check "RESULT: PASS"                                    python3 tools/auditors/check_entity_links.py
check "RESULT: PASS"                                    python3 tools/auditors/check_mutual_interactions.py
check "RESULT: PASS"                                    python3 tools/auditors/check_slot_templates.py
check "RESULT: PASS"                                    python3 tools/auditors/check_series_counts.py
check "RESULT: PASS"                                    python3 tools/auditors/check_sentence_starts.py
check "RESULT: PASS"                                    python3 tools/auditors/check_ratio_basis.py
check "RESULT: PASS"                                    python3 tools/auditors/check_work_response.py
check "RESULT: PASS"                                    python3 tools/auditors/check_relic_work_types.py
check "RESULT: PASS"                                    python3 tools/auditors/check_relic_interaction_damage.py
check "RESULT: PASS"                                    python3 tools/auditors/check_relic_gauge.py
check "RESULT: PASS"                                    python3 tools/auditors/check_work_preference.py
check "RESULT: PASS"                                    python3 tools/auditors/check_md_tables.py
check "RESULT: PASS"                                    python3 tools/auditors/check_barred_prescriptions.py
check "RESULT: PASS"                                    python3 tools/auditors/check_special_abnormality.py
check "RESULT: PASS"                                    python3 tools/auditors/check_threat_form.py
check "RESULT: PASS"                                    python3 tools/auditors/check_consequence_register.py
check "RESULT: PASS"                                    python3 tools/auditors/check_work_damage.py
# batch 203/204/206 shipped these three; none of them was ever added here, so the build
# could not fail on them. Gate 92 now makes an unwired gate a failure in its own right.
check "RESULT: PASS"                                    python3 tools/auditors/check_work_effect.py
check "RESULT: PASS"                                    python3 tools/auditors/check_se_effect.py
check "RESULT: PASS"                                    python3 tools/auditors/check_rule_index.py
check "RESULT: PASS"                                    python3 tools/auditors/check_secc_shape.py
check "RESULT: PASS"                                    python3 tools/auditors/check_gate_wiring.py

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
bad=[];fence=False
for l in io.open(sys.argv[1],encoding='utf-8').read().split('\n'):
    if l.lstrip().startswith('```'):
        fence = not fence; continue
    # a table row is prose outside a fence; ASCII box art inside one is not a row
    if not fence and l.startswith('|') and not l.rstrip().endswith('|'):
        bad.append(l)
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
