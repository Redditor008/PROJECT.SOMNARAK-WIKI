#!/usr/bin/env bash
# unit_np.sh <unit> <file> "<message>" — run the per-dossier gates, then commit and push.
# Refuses and leaves the edits uncommitted if any gate fails.
set -u
U="$1"; F="$2"; M="$3"
cd "$(git rev-parse --show-toplevel)" || exit 1
v="$(python3 tools/verify.py "$F" 2>&1 | head -1)"
t="$(python3 tools/tpl.py "$F" 2>&1 | head -1)"
s="$(python3 tools/sectfile.py "$F" 2>&1 | tail -1)"   # verdict is the LAST line
w="$(python3 tools/wikistd.py "$F" 2>&1)"
echo "verify:   $v"
echo "tpl:      $t"
echo "sectfile: $s"
echo "wikistd:  $(printf '%s' "$w" | tr '\n' ' ' | cut -c1-200)"
for c in "$v:RESIDUAL 0" "$t:RESIDUE 0"; do
  printf '%s' "${c%%:*}" | grep -qF -- "${c##*:}" || { echo "UNIT $U REFUSED — edits left uncommitted"; exit 1; }
done
printf '%s' "$s" | grep -qE '^0 section' || { echo "UNIT $U REFUSED — edits left uncommitted"; exit 1; }
printf '%s' "$w" | grep -qE 'meets +True'  || { echo "UNIT $U REFUSED — edits left uncommitted"; exit 1; }
git add "$F" && git commit -q -m "$M" && git push -q origin HEAD
git fetch -q origin
H="$(git rev-parse HEAD)"; R="$(git rev-parse origin/"$(git branch --show-current)")"
if [ "$H" = "$R" ]; then
  echo "UNIT PUSHED: $(git rev-parse --short HEAD) | $(basename "$F")"
else
  echo "UNIT $U: NOT PUSHED (HEAD $H vs remote $R)"; exit 1
fi
