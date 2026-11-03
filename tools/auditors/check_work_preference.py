#!/usr/bin/env python3
"""check_work_preference.py — the four cells, and the Threat Score behind the barred pair.

Owner rules, 2026-11-03:

> *"INSTEAD OF N/A For Non-Subject Write It Either 0% ... and how you logic it is
> using the SE Threat Point because it's easier than checking both at the same
> time."*
>
> *"The Threat Point Thing ... I Used It From Our Conversion Guide you know the
> 2–10 things. Also You Dont Write 0% or -100% On Dossier It Look Bad Think It
> Like This Net-Neutral And Negative-Low."*

Four things are enforced here:

1. **The alphabet.** A cell is `Down`, `Up`, `Neutral`, `Net-Neutral` or
   `Negative-Low`. `N/A` on a barred register is retired: it said *not
   applicable*, which is not an answer to "what happens if somebody tries".
2. **The barred cells are words, not percentages.** `0%` and `-100%` were the
   batch-156 labels and they read badly on a dossier page. They are the *same two
   mechanics* under their written names: **Net-Neutral** (nothing is returned: the
   threshold does not come down, the gauge does not move, no benefit is paid) and
   **Negative-Low** (the attempt is charged in full: threshold to 0, gauge to
   100%). A page that still prints a percentage token fails on `percentage-token`.
3. **The barred pair is one reading.** The two cells must be equal, because both
   come from one number rather than from two separate judgements.
4. **The Threat Score decides, and it is the guide's 2–10.** `PM_ABNORMALITY_TO_PS_
   SORROW_ENTITY_CONVERSION_GUIDE.md` §III: *Threat Score is Coherence rank +
   Potency rank (I/α = 1 … V/ω = 5)*, so it runs **2–10** — 2–3 ZAYIN, 4–5 TETH,
   6 HE, 7–8 WAW, 9–10 ALEPH. Below 6 the attempt simply fails (**Net-Neutral**);
   6 and above the holding is heavy enough to collect in full (**Negative-Low**).
   The band boundary *is* the rule: HE is the first tier that is a major problem.

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
COHERENCE = re.compile(r'\|\s*\*{0,2}Coherence\*{0,2}\s*\|\s*([^|\n]*)')
POTENCY = re.compile(r'\|\s*\*{0,2}Potency\*{0,2}\s*\|\s*([^|\n]*)')
ROW = re.compile(r'^\|\s*\*\*(Flerehan|Pugnahan|Viderehan|Ferrehan)\*\*[^|]*\|[^|]*\|([^|]*)\|', re.M)
_CELL = r'(?:-100%|0%|Down|Up|Neutral|Net-Neutral|Negative-Low)'
VEC = re.compile(r'`?(' + _CELL + r')\s*:\s*(' + _CELL + r')\s*:\s*(' + _CELL +
                 r')\s*:\s*(' + _CELL + r')`?')

ORDER = ('Flerehan', 'Pugnahan', 'Viderehan', 'Ferrehan')
NET_NEUTRAL = 'Net-Neutral'
NEGATIVE_LOW = 'Negative-Low'
GOOD = {'Down', 'Up', 'Neutral', NET_NEUTRAL, NEGATIVE_LOW}
BAR = {NET_NEUTRAL, NEGATIVE_LOW}

# Legacy tokens. They parse — a batch may not be half-migrated into a false fail —
# but a page that still prints one is reported, so the words have to land everywhere.
LEGACY = {'0%': NET_NEUTRAL, '-100%': NEGATIVE_LOW, '\u2212100%': NEGATIVE_LOW}

# The guide's arithmetic: Coherence rank + Potency rank, I/α = 1 … V/ω = 5.
ROMAN = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
GREEK = {'\u03b1': 1, '\u03b2': 2, '\u03b3': 3, '\u03b4': 4, '\u03c9': 5}
HE = 6                 # ZAYIN 2–3 · TETH 4–5 · **HE 6** · WAW 7–8 · ALEPH 9–10

# A cell that still says N/A, a dash, or a sentence. Retired for barred registers.
# `\b` after a dash never fires at end of string, so the lookahead is explicit,
# and it keeps `-100%` out of the retired class.
DEAD = re.compile(r'^\s*(?:N/A|—|–|-)(?![A-Za-z0-9])', re.I)

# Still printing a percentage where a word belongs.
PERCENT = re.compile(r'(?<![\d.])-[\u2212]?100\s*%|(?<![\d.])0\s*%')

# The ratchet counts dossiers on the two most crowded vectors; it may only fall.
#
# 172 -> 176 in batch 159, and the rise is recorded rather than dressed up. The
# Threat Score replaced the gauge reading as the source of the barred pair, and
# four of the five dossiers that re-read under it landed on the second crowded
# vector. A rule change moves the measure; nothing was rewritten to move it.
TIERED = [0]
RATCHET = 176
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

    The two named cells are tested first, then the legacy percentages, then the
    signs. The percentage forms must be tested BEFORE the dash form: `-100%`
    starts with a dash, and a dead-cell pattern run first reads it as a retired `—`.
    """
    c = split_tier(cell)[0]
    low = c.lower().replace('*', '').strip()
    if low in ('net-neutral', 'net neutral', 'netneutral', 'net zero', 'net-zero'):
        return NET_NEUTRAL
    if low in ('negative-low', 'negative low', 'negativelow'):
        return NEGATIVE_LOW
    if re.match(r'^[-\u2212]100\s*%', c):
        return NEGATIVE_LOW
    if re.match(r'^0\s*%', c):
        return NET_NEUTRAL
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
        return [normalize(c) for c in m.groups()]
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


def threat_score(text):
    """Coherence rank + Potency rank, the guide's 2–10. None when either is unfiled.

    The fields are written `| **Coherence** | Entity (IV) |` and `| **Potency** |
    Major (γ) |`, and the row labels have a `modifier` sibling that must not be
    read as the field itself.
    """
    coh, pot = COHERENCE.search(text), POTENCY.search(text)
    if not coh or not pot:
        return None
    c = re.search(r'\b(IV|V|III|II|I)\b', coh.group(1))
    g = re.search(r'([\u03b1\u03b2\u03b3\u03b4\u03c9])', pot.group(1))
    if not c or not g:
        return None
    return ROMAN[c.group(1)] + GREEK[g.group(1)]


def wanted_barred(score):
    """Below HE the attempt fails; HE and above it is collected in full."""
    return NEGATIVE_LOW if score >= HE else NET_NEUTRAL


def is_relic(text):
    m = TYPE.search(text)
    return bool(m) and 'Subject' not in m.group(1)


def barred_pair_problems(vec):
    """The barred cells must be equal, and must be words rather than percentages."""
    out = []
    for i in (0, 1):
        if vec[i] not in BAR and vec[i] is not None:
            out.append('cell %d is %r, not Net-Neutral or Negative-Low' % (i + 1, vec[i]))
    if vec[0] in BAR and vec[1] in BAR and vec[0] != vec[1]:
        out.append('barred pair disagrees (%s vs %s) — it is one threat reading'
                   % (vec[0], vec[1]))
    return out


def measure():
    files, problems, distribution = [], [], collections.Counter()
    tiered = [0]
    for pattern in DOSSIERS:
        for path in sorted(glob.glob(pattern, recursive=True)):
            with io.open(path, encoding='utf-8') as fh:
                text = fh.read()
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
            score = threat_score(text)
            if score is not None and vec[0] in BAR and vec[1] in BAR:
                want = wanted_barred(score)
                if vec[0] != want:
                    bad.append('threat score %d (%s) wants %s, cells say %s'
                               % (score, 'HE or above' if score >= HE
                                  else 'under HE', want, vec[0]))
            # Scoped to the cells, not the file: "the store is the same size at
            # 0 % as at 45 %" is a gauge reading in prose, not a work-response
            # cell, and a whole-file scan reported it as one.
            raw = cells_of(text) or []
            vrow = [l for l in text.split('\n') if 'Work preference' in l and VEC.search(l)]
            if any(PERCENT.search(x) for x in raw) or any(
                    PERCENT.search(VEC.search(l).group(0)) for l in vrow):
                bad.append('percentage-token: still prints a percentage where the '
                           'alphabet has a word')
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
    pct = sum(1 for _, bad in problems for b in bad if b.startswith('percentage-token'))
    print('off alphabet: %d  printing a percentage: %d  on the two crowded vectors: %d  '
          'ratchet %d  set %s'
          % (len(problems), pct, on_two, RATCHET, RATCHET_SET))
    print('carrying a preference tier: %d of %d graded' % (TIERED[0], sum(dist.values())))
    if problems or on_two > RATCHET:
        print('RESULT: FAIL')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
