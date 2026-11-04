#!/usr/bin/env python3
"""check_special_abnormality.py — a terminus is never worked and never extracted (R-35).

The owner's rule, 2026-11-01:

> *"They Should Never Be File Like Normal SE But Like Special Abno."*

and, 2026-11-04:

> *"The Convergence And Dawn Of Mourning And So The Flood Sovereign So This Three
> Should Never Have Work Type And M.A.W."*

A **Special Abnormality** is the terminus of a transformation line: the form a line
produces when it completes, which the archive never acquires, contains, works or
extracts as itself. A dossier carrying

    | **Special Class** | **Special Abnormality** — ... |

is making that claim, and the claim has consequences the file must honour:

1. **No work table.** There is no work loop, so the four Work Types have nothing to
   describe. A `## Behavior` deck kept as a *historical or projected* reading is
   prose, not four `Flerehan`/`Pugnahan`/`Viderehan`/`Ferrehan` rows.
2. **No Han-Energy yield.** A form that is never held yields nothing; the row reads
   as a dash with a reason, never as a collected figure per cycle.
3. **No M.A.W. production line.** Where the registry files pieces for a terminus
   they are sealed projections — named in the dossier, never presented as three
   extracted pieces (`### M.A.W. Weapon / Suit / Stigma` headings).

The class test itself is provenance and cannot be mechanised; this gate enforces the
consequences on the files that have already declared the class.

    python3 tools/auditors/check_special_abnormality.py       # gate
    python3 tools/auditors/check_special_abnormality.py -v    # every finding
"""
import glob
import io
import re
import sys

DOSSIERS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/*.md')

SPECIAL = re.compile(r'^\|\s*\*\*Special Class\*\*\s*\|\s*\*\*Special Abnormality\*\*', re.M)
WORK_ROW = re.compile(r'^\|\s*\*\*(Flerehan|Pugnahan|Viderehan|Ferrehan)\*\*', re.M)
MAW_SECTION = re.compile(r'^###\s*M\.A\.W\.\s*(Weapon|Suit|Stigma)\b', re.M)
YIELD = re.compile(r'^\|\s*\*\*Han-Energy yield\*\*\s*\|\s*([^\n]*)', re.M)
# A yield row that opens with a figure is claiming a collection; one that opens with
# a dash, an em dash, or a word is disclaiming it.
YIELD_CLAIMS = re.compile(r'^\s*\*{0,2}\d')


def problems(text):
    """What one declared terminus still does that it must not."""
    if not SPECIAL.search(text):
        return []
    bad = []
    rows = WORK_ROW.findall(text)
    if rows:
        bad.append('carries %d Work Type row(s): %s'
                   % (len(rows), ', '.join(sorted(set(rows)))))
    secs = MAW_SECTION.findall(text)
    if secs:
        bad.append('presents an M.A.W. production line (%s)'
                   % ', '.join(sorted(set(secs))))
    m = YIELD.search(text)
    if m and YIELD_CLAIMS.match(m.group(1)):
        bad.append('states a collected Han-Energy yield: %s' % m.group(1).strip()[:60])
    return bad


def main(argv):
    files, bad = [], []
    for pattern in DOSSIERS:
        for path in sorted(glob.glob(pattern, recursive=True)):
            with io.open(path, encoding='utf-8') as fh:
                text = fh.read()
            if not SPECIAL.search(text):
                continue
            files.append(path)
            found = problems(text)
            if found:
                bad.append((path, found))
    for path, found in bad:
        print('%s  %s' % (path, '; '.join(found)[:150]))
    print('declared termini: %d  still worked or extracted: %d' % (len(files), len(bad)))
    if bad:
        print('RESULT: FAIL')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
