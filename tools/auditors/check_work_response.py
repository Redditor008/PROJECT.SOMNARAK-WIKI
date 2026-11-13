#!/usr/bin/env python3
"""check_work_response.py — the four work responses must answer the Element row.

`SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/PROJECT_SOMNARAK.md`
has carried a **Work Type Effectiveness** matrix since the first cosmology
draft: for each of the four elements, which of the four Work Types is Strong,
Partial or Weak against it.

    | Entity Element | Flerehan | Pugnahan | Viderehan | Ferrehan |
    | Lament         | Strong   | Weak     | Partial   | Partial  |
    | Grudge         | Weak     | Strong   | Partial   | Partial  |
    | Void           | Partial  | Partial  | Strong    | Weak     |
    | Weight         | Partial  | Partial  | Weak      | Strong   |

Every dossier carries its own `**Element**` row three tables above its Behavior
table. Measured on 2026-11-03: **285 of 285 dossiers break the matrix.** The same
three sign vectors appear under Lament, Grudge, Void and Weight alike —

    (Decrease, Increase, Stable, Decrease)   107
    (N/A, N/A, Stable, Decrease)             118
    (—, —, Decrease, Decrease)                29

— so the element, which the cosmology says decides how a holding answers, decides
nothing. The responses were written one file at a time and each one is defensible
alone; it is the *set* that is uniform. That is why no gate caught it: there was
no error to find in any single dossier.

The mapping enforced here is the matrix read across:

    Strong  -> Decrease   the work type the element answers to
    Partial -> Stable     moderate effect, no net movement
    Weak    -> Increase   least effective, highest risk

A non-subject holding is bound by the Two-Work-Type Rule, so its Flerehan and
Pugnahan cells are expected to be N/A or — whatever the matrix says. What is
checked for a relic is the two cells it actually has.

**Exemptions.** A dossier may leave the matrix when its own record states why —
`SE-O-IIIγ-476` Sehnsucht's reading rule is that *stability under Viderehan is
correct*, because the object's motion is the datum the file measures. An
exemption needs a reason in the same shape as the ones below; it is not a way to
avoid work.

    python3 tools/auditors/check_work_response.py        # ratchet check
    python3 tools/auditors/check_work_response.py -v     # per-dossier listing
    python3 tools/auditors/check_work_response.py --stats
"""
import collections
import glob
import io
import re
import sys

DOSSIERS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/*.md')

# Strong / Partial / Weak, in the order the matrix prints them:
# Flerehan, Pugnahan, Viderehan, Ferrehan.
MATRIX = {
    'Lament': ('Decrease', 'Increase', 'Stable', 'Stable'),
    'Grudge': ('Increase', 'Decrease', 'Stable', 'Stable'),
    'Void':   ('Stable', 'Stable', 'Decrease', 'Increase'),
    'Weight': ('Stable', 'Stable', 'Increase', 'Decrease'),
}

ROW = re.compile(r'^\|\s*\*\*(Flerehan|Pugnahan|Viderehan|Ferrehan)\*\*[^|]*\|'
                 r'([^|]*)\|([^|]*)\|', re.M)
ELEMENT = re.compile(r'\|\s*\*\*Element\*\*\s*\|\s*([^|]+)\|')
TYPE = re.compile(r'\*\*Entity Type\*\*\s*\|\s*([^|]+)\|')
SIGN = re.compile(r'^(Decrease|Increase|Stable)\b')

EXEMPT = {
    'SE-O-IIIγ-476': ('The file\'s own reading rule is that stability under '
                      'Viderehan is correct: the object\'s motion is the datum '
                      'it measures, and a reader adds nothing to it.'),
}

# 290 dossiers graded, 290 off the matrix on 2026-11-03; batch 154 repaired five
# and exempted one on its own record, leaving 284.
RATCHET = 284
RATCHET_SET = '2026-11-03'


def scan_text(text, name=''):
    """Return [(work type, written, prescribed)] for every cell off the matrix."""
    e = ELEMENT.search(text)
    y = TYPE.search(text)
    if not e or not y:
        return None
    element = e.group(1).strip()
    want = MATRIX.get(element)
    if not want:
        return None                      # mixed or emerging element: not graded
    subject = 'Subject' in y.group(1)
    rows = dict((k, g.strip()) for k, _, g in ROW.findall(text))
    if len(rows) != 4:
        return None
    out = []
    for i, work in enumerate(('Flerehan', 'Pugnahan', 'Viderehan', 'Ferrehan')):
        written = rows[work]
        if not subject and i < 2:
            if not (written.startswith('N/A') or written.startswith('—')):
                out.append((work, written, 'N/A'))
            continue
        m = SIGN.match(written)
        if not m:
            out.append((work, written, want[i]))     # unreadable cell
        elif m.group(1) != want[i]:
            out.append((work, written, want[i]))
    return out


def measure():
    files, hits = [], []
    for pattern in DOSSIERS:
        for path in sorted(glob.glob(pattern, recursive=True)):
            files.append(path)
            text = io.open(path, encoding='utf-8').read()
            code = re.search(r'(SE-[A-Z]-[IV]+[^\s`]*-\d{3})', text)
            key = code.group(1) if code else path
            if key in EXEMPT:
                continue
            bad = scan_text(text, path)
            if bad is None:
                continue
            if bad:
                hits.append((path, key, bad))
    return files, hits


def stats(files):
    vectors = collections.Counter()
    signs = collections.Counter()
    for path in files:
        text = io.open(path, encoding='utf-8').read()
        rows = dict((k, g.strip()) for k, _, g in ROW.findall(text))
        if len(rows) != 4:
            continue
        vec = tuple(rows[w].split()[0].rstrip(',') for w in
                    ('Flerehan', 'Pugnahan', 'Viderehan', 'Ferrehan'))
        vectors[vec] += 1
        for w in ('Flerehan', 'Pugnahan', 'Viderehan', 'Ferrehan'):
            m = SIGN.match(rows[w])
            if m:
                signs[m.group(1)] += 1
    total = sum(signs.values())
    print('sign total: ' + ' · '.join('%s %d (%.0f%%)' % (k, v, 100.0 * v / total)
                                      for k, v in signs.most_common()))
    for vec, n in vectors.most_common(6):
        print('%5d  %s' % (n, ':'.join(vec)))


def main(argv):
    files, hits = measure()
    if '--stats' in argv:
        stats(files)
        return 0
    limit = RATCHET
    if '-v' in argv:
        for path, key, bad in hits:
            print('%s  %s' % (key, path))
            for work, written, want in bad:
                print('    %-10s %-14s prescribed %s' % (work, written[:14], want))
    else:
        for path, key, bad in hits:
            print('%s  %s' % (key, ', '.join('%s=%s' % (w, g[:12])
                                             for w, g, _ in bad)))
    n = len(hits)
    print('work-response off matrix: %d  ratchet %d  set %s' % (n, limit, RATCHET_SET))
    if n > limit:
        print('RESULT: FAIL — %d over the ratchet' % (n - limit))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
