#!/usr/bin/env python3
"""check_relic_work_types.py — a relic is handled, not worked (R-40).

The owner's rule, 2026-11-03:

> *"NO RELIC SE WILL HAVE WORK TYPE INSTEAD HAVE HANDLING PROCESS."*

A relic — Object, Place, Time, Hazard, Possession — is not worked. The four Work
Types are the ways a *subject* is approached, and each of them assumes something
in the holding that answers back. An artefact has nothing that answers, so its
dossier carries **`## Handling Process`** (Approach · Handling · Withdrawal ·
Refusal) and the core table's `Valid Work Types` row reads `**Handling**`.

Measured at the moment the rule was made: **143 relic dossiers still carry a
Work Type table**, and 117 of them carry the identical `N/A : N/A : Stable :
Decrease` vector — a form with two blanks filled in, which is why the rule was
retired rather than repaired. The ratchet starts there and only goes down.

    python3 tools/auditors/check_relic_work_types.py        # ratchet check
    python3 tools/auditors/check_relic_work_types.py -v     # per-dossier listing
    python3 tools/auditors/check_relic_work_types.py --stats
"""
import glob
import io
import re
import sys

DOSSIERS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/*.md')

TYPE = re.compile(r'\*\*Entity Type\*\*\s*\|\s*([^|]+)\|')
WORK_ROW = re.compile(r'^\|\s*\*\*(Flerehan|Pugnahan|Viderehan|Ferrehan)\*\*', re.M)

RATCHET = 131
RATCHET_SET = '2026-11-04'


def is_relic(text):
    m = TYPE.search(text)
    if not m:
        return False
    return 'Subject' not in m.group(1)


def offences(text):
    """Everything on this page that still treats the holding as workable."""
    out = []
    if re.search(r'^\|\s*\*\*Valid Work Types\*\*\s*\|', text, re.M):
        out.append('Valid Work Types row')
    if re.search(r'^## Behavior\s*$', text, re.M):
        out.append('## Behavior section')
    n = len(WORK_ROW.findall(text))
    if n:
        out.append('%d Work Type row(s)' % n)
    return out


def measure():
    files, hits, converted = [], [], []
    for pattern in DOSSIERS:
        for path in sorted(glob.glob(pattern, recursive=True)):
            text = io.open(path, encoding='utf-8').read()
            if not is_relic(text):
                continue
            files.append(path)
            bad = offences(text)
            if bad:
                hits.append((path, bad))
            elif '## Handling Process' in text:
                converted.append(path)
    return files, hits, converted


def main(argv):
    files, hits, converted = measure()
    if '--stats' in argv:
        print('relic dossiers: %d · converted to Handling Process: %d · still worked: %d'
              % (len(files), len(converted), len(hits)))
        return 0
    for path, bad in hits:
        print('%s  %s' % (path, ', '.join(bad)))
    n = len(hits)
    print('relic dossiers still carrying Work Types: %d  ratchet %d  set %s'
          % (n, RATCHET, RATCHET_SET))
    if n > RATCHET:
        print('RESULT: FAIL — %d over the ratchet' % (n - RATCHET))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
