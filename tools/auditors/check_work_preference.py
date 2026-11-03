#!/usr/bin/env python3
"""check_work_preference.py — the four cells, and the one number behind the barred pair.

Owner rule, 2026-11-03:

> *"INSTEAD OF N/A For Non-Subject Write It Either 0% e.g. Will Not Give Anything
> Or For Special Non-Subject SE -100% ... and how you logic it is using the SE
> Threat Point because it's easier than checking both at the same time."*

Three things are enforced here:

1. **The alphabet.** A cell is `Down`, `Up`, `Neutral`, `0%` or `-100%`. `N/A` on a
   barred register is retired: it said *not applicable*, which is not an answer to
   "what happens if somebody tries".
2. **The barred pair is one reading.** The two barred cells must be equal, because
   both come from the threat point rather than from two separate judgements.
3. **The threat point decides.** `Sorrow Gauge [HP]` under 500 -> `0%`; 500 or
   more -> `-100%`. Checked wherever a dossier prints both the pair and the gauge.

    python3 tools/auditors/check_work_preference.py            # ratchet check
    python3 tools/auditors/check_work_preference.py -v         # per-dossier listing
    python3 tools/auditors/check_work_preference.py --variety  # the live distribution
"""
import collections
import glob
import io
import re
import sys

DOSSIERS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/*.md')

TYPE = re.compile(r'\*\*Entity Type\*\*\s*\|\s*([^|]+)\|')
HP = re.compile(r'\*\*Sorrow Gauge \[HP\]\*\*\s*\|\s*([0-9]+)\s*/')
ROW = re.compile(r'^\|\s*\*\*(Flerehan|Pugnahan|Viderehan|Ferrehan)\*\*[^|]*\|[^|]*\|([^|]*)\|', re.M)
VEC = re.compile(r'`?(-100%|0%|Down|Up|Neutral)\s*:\s*(-100%|0%|Down|Up|Neutral)\s*:\s*'
                 r'(-100%|0%|Down|Up|Neutral)\s*:\s*(-100%|0%|Down|Up|Neutral)`?')

ORDER = ('Flerehan', 'Pugnahan', 'Viderehan', 'Ferrehan')
GOOD = {'Down', 'Up', 'Neutral', '0%', '-100%'}
BAR = {'0%', '-100%'}

# A cell that still says N/A, a dash, or a sentence. Retired for barred registers.
# `\b` after a dash never fires at end of string, so the lookahead is explicit,
# and it keeps `-100%` out of the retired class.
DEAD = re.compile(r'^\s*(?:N/A|—|–|-)(?![A-Za-z0-9])', re.I)

# 172 dossiers sat on two vectors when the percentage alphabet went in.
# The ratchet counts dossiers on the two most crowded vectors; it may only fall.
TIERED = [0]
RATCHET = 172
RATCHET_SET = '2026-11-03'


# The L Corp ladder has five grades. The archive writes the middle three today; the
# two extremes are legal so a dossier may claim one without tripping the auditor.
TIERS = ('V.H', 'High', 'Common', 'Low', 'V.L')


def split_tier(cell):
    """`Down · High` -> ('Down', 'High'). A bare sign has no tier."""
    parts = [p.strip().strip('*').strip() for p in cell.replace('**', '').split('·')]
    return parts[0], (parts[1] if len(parts) > 1 else None)


def normalize(cell):
    """Map a written cell to the alphabet, or None when it is prose.

    The percentage forms are tested BEFORE the dash form: `-100%` begins with a
    dash, and a dead-cell pattern run first reads it as a retired `—`.
    """
    c = split_tier(cell)[0]
    if re.match(r'^[-\u2212]100\s*%', c):
        return '-100%'
    if re.match(r'^0\s*%', c):
        return '0%'
    low = c.lower()
    if low in ('down', 'up', 'neutral'):        # the canonical word itself
        return low.capitalize()
    if low.startswith('stable') or low.startswith('no movement'):
        return 'Neutral'
    if low.startswith('decrease') or low.startswith('slight decrease'):
        return 'Down'
    if low.startswith('increase'):
        return 'Up'
    if DEAD.match(c):
        return 'RETIRED'
    return None


def cells_of(text):
    """The four raw cells, in file order, or None when the table is not four rows."""
    rows = dict((w, g) for w, g in ROW.findall(text))
    if len(rows) != 4:
        return None
    return [rows[w] for w in ORDER]


def vector_of(text):
    """The four-cell vector of a dossier, from its table or its Work preference row."""
    m = VEC.search(text)
    if m and 'Work preference' in text:
        return list(m.groups())
    cells = cells_of(text)
    if cells is None:
        return None
    return [normalize(c) for c in cells]


def tier_problems(cells):
    """The L Corp ladder: High / Common / Low, one High at most, none on a barred cell."""
    out = []
    tiers = [split_tier(c)[1] for c in cells]
    seen = [x for x in tiers if x]
    for i, tier in enumerate(tiers):
        if tier and tier not in TIERS:
            out.append('cell %d tier %r is off the ladder' % (i + 1, tier))
        if tier and tiers is not None and normalize(cells[i]) in BAR:
            out.append('cell %d is barred and carries no preference' % (i + 1))
    if seen.count('High') > 1:
        out.append('%d High cells — a holding answers to one register best'
                   % seen.count('High'))
    if seen.count('V.H') > 1:
        out.append('%d V.H cells — a holding answers to one register best'
                   % seen.count('V.H'))
    if seen and len(seen) != 4:
        out.append('only %d of four cells carry a tier' % len(seen))
    return out


def is_relic(text):
    m = TYPE.search(text)
    return bool(m) and 'Subject' not in m.group(1)


def barred_pair_problems(vec):
    """Barred cells must be equal and must be one of the two percentages."""
    out = []
    for i in (0, 1):
        if vec[i] not in BAR and vec[i] is not None:
            out.append('cell %d is %r, not 0%% or -100%%' % (i + 1, vec[i]))
    if vec[0] in BAR and vec[1] in BAR and vec[0] != vec[1]:
        out.append('barred pair disagrees (%s vs %s) — it is one threat reading'
                   % (vec[0], vec[1]))
    return out


def measure():
    files, problems, distribution = [], [], collections.Counter()
    tiered = [0]
    for pattern in DOSSIERS:
        for path in sorted(glob.glob(pattern, recursive=True)):
            text = io.open(path, encoding='utf-8').read()
            files.append(path)
            vec = vector_of(text)
            if vec is None:
                continue
            bad = []
            if 'RETIRED' in vec:
                bad.append('barred cell still written N/A or a dash')
            for word in vec:
                if word is not None and word != 'RETIRED' and word not in GOOD:
                    bad.append('cell %r is off the alphabet' % word)
            if is_relic(text):
                bad.extend(barred_pair_problems(vec))
            cells = cells_of(text)
            if cells is not None:
                bad.extend(tier_problems(cells))
                if any(split_tier(c)[1] for c in cells):
                    tiered[0] += 1
            hp = HP.search(text)
            if hp and vec[0] in BAR and vec[1] in BAR:
                want = '-100%' if int(hp.group(1)) >= 500 else '0%'
                if vec[0] != want:
                    bad.append('threat point %s wants %s, cells say %s'
                               % (hp.group(1), want, vec[0]))
            if bad:
                problems.append((path, bad))
            if all(v is not None and v != 'RETIRED' for v in vec):
                distribution[tuple(vec)] += 1
    TIERED[0] = tiered[0]
    return files, problems, distribution


def main(argv):
    files, problems, dist = measure()
    if '--variety' in argv:
        for vec, n in dist.most_common():
            print('%5d  %s' % (n, ' : '.join(vec)))
        print('%d graded dossiers, %d distinct vectors' % (sum(dist.values()), len(dist)))
        return 0
    for path, bad in problems:
        if '-v' in argv:
            print('%s  %s' % (path, '; '.join(bad)))
        else:
            print('%s  %s' % (path, '; '.join(bad)[:110]))
    on_two = sum(n for _, n in dist.most_common(2))
    print('off alphabet: %d  on the two crowded vectors: %d  ratchet %d  set %s'
          % (len(problems), on_two, RATCHET, RATCHET_SET))
    print('carrying a preference tier: %d of %d graded' % (TIERED[0], sum(dist.values())))
    if problems or on_two > RATCHET:
        print('RESULT: FAIL')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
