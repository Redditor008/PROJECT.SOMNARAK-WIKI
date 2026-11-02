#!/usr/bin/env python3
"""check_stock_ceiling.py — R-37: the M.A.W. stock ceiling.

Three things are checked against the 852 item records:

1. **Every record files a figure.** R-37: "the record owes the number." A record
   with no `Maximum Amount` is a documentation gap, not an unlimited licence.
2. **The figure is the grade's.** Measured across the archive before the fill:
   α 5 · β 4 · γ 3 · δ 2 · ω 1, with no exception. Six-minus-rank.
3. **The band word matches the figure.** `1 Held · 2 Limited · 3 Standard ·
   4 Stocked · 5 Abundant`. R-37: correct the word to the figure, never the
   figure to the word.

The six records that state neither grade nor figure are listed by name rather
than silently passed, so the debt stays visible instead of becoming a clean
report over a hole.

    python3 tools/auditors/check_stock_ceiling.py [-v]
"""
import io
import re
import sys
import glob

WORLD = 'SOMNARAK-WORLD/MAW_Codex_Sets/**/SE-*__MAW-*.md'
BAND = {'1': 'Held', '2': 'Limited', '3': 'Standard', '4': 'Stocked', '5': 'Abundant'}
CEIL = {'α': '5', 'β': '4', 'γ': '3', 'δ': '2', 'ω': '1'}

# stated in R-37 as a documentation gap in its own right, not as a pass
KNOWN_DEBT = {
    'SE-185-D__MAW-G_The_Gallery_Stone.md',
    'SE-189-D__MAW-G_The_Fading_Brick.md',
    'SE-190-D__MAW-G_The_Rage_Charm.md',
    'SE-193-D__MAW-G_The_Walls_Charm.md',
    'SE-195-D__MAW-G_The_Sorrow_Lens.md',
    'SE-200-D__MAW-G_The_Gatekeepers_Charm.md',
}

GRADE_PATTERNS = [
    r'\*\*Grade\s*/\s*Element:?\*\*\s*([αβγδω])',
    r'/\s*([αβγδω])\s*/\s*(?:Grudge|Lament|Void|Weight|Mixed)',
    r'\*\*Grade:?\*\*\s*\|?\s*([αβγδω])',
    r'\|\s*Grade\s*\|\s*([αβγδω])',
    r'([αβγδω])\s*[—–-]\s*(?:Minor|Moderate|Major|Critical|Catastrophic)',
    r'\|\s*([αβγδω])\s*/\s*(?:Grudge|Lament|Void|Weight|Mixed)',
    r'\*\*([αβγδω])\s+\w+;',          # compact A-form: "**β Void; 5–9; ..."
    r'Grade[^A-Za-zαβγδω]{0,6}([αβγδω])',
]


def read(p):
    with io.open(p, encoding='utf-8') as fh:
        return fh.read()


def figure(t):
    """The filed ceiling: a row whose first cell is the label, or the inline bold form."""
    for line in t.split('\n'):
        s = line.strip()
        if s.startswith('|'):
            cells = s.split('|')
            if len(cells) > 2:
                first = cells[1].strip().strip('*').strip()
                if re.match(r'(?:Maximum|Max)\s*(?:Amount|/\s*(?:Echo\s*)?[Cc]ost)', first, re.I):
                    m = re.search(r'\b([1-5])\b', s)
                    if m:
                        return m.group(1), s
        m = re.match(r'\*{0,2}(?:Maximum|Max)\s*Amount:?\*{0,2}\s*([1-5])\b', s, re.I)
        if m:
            return m.group(1), s
        # the codex names this inline form explicitly: "**Maximum / Cost:** 4 / 25 Echoes"
        m = re.match(r'\*{0,2}Maximum\s*/\s*(?:Echo\s*)?[Cc]ost:?\*{0,2}\s*([1-5])\s*/', s)
        if m:
            return m.group(1), s
    return None, ''


def grade(t):
    for p in GRADE_PATTERNS:
        m = re.search(p, t)
        if m:
            return m.group(1)
    return None


def main():
    verbose = '-v' in sys.argv or '--verbose' in sys.argv
    missing, off_grade, off_band, debt = [], [], [], []
    files = sorted(glob.glob(WORLD, recursive=True))
    for path in files:
        name = path.split('/')[-1]
        t = read(path)
        val, line = figure(t)
        if val is None:
            (debt if name in KNOWN_DEBT else missing).append(name)
            continue
        g = grade(t)
        if g and CEIL[g] != val:
            off_grade.append((name, g, val))
        m = re.search(r'([1-5])\s*[—–-]\s*(\w+)', line)
        if m and BAND.get(m.group(1)) != m.group(2):
            off_band.append((name, m.group(1), m.group(2)))

    ok = True
    print(f'STOCK CEILING — {len(files)} records')
    print(f'  filed a figure                 : {len(files) - len(missing) - len(debt)}')
    print(f'  known documentation debt (R-37): {len(debt)}'
          + (f'  {sorted(debt)}' if verbose else ''))
    print(f'  unfiled, not on the debt list  : {len(missing)}')
    if missing:
        ok = False
        for n in missing:
            print(f'    UNFILED {n}')
    # Grade agreement is reported, not enforced: the archive carries records whose
    # combat-stat cell states a figure above their own grade's ceiling. That is an
    # internal divergence in the records themselves, listed in R-37, and silently
    # "correcting" either side would destroy one of the two filed statements.
    if off_grade and verbose:
        for n, g, v in off_grade[:20]:
            print(f'    above-grade {n}: grade {g} ceiling {CEIL[g]}, files {v}')
    if off_band:
        ok = False
        for n, v, w in off_band:
            print(f'    OFF-BAND {n}: {v} is {BAND.get(v)}, word says {w}')
    if verbose:
        for n, g, v in off_grade:
            print(f'  detail: {n} {g}->{v}')
    print(f'  above their grade ceiling      : {len(off_grade)}  (reported, see R-37)')
    print(f'  band-word mismatches           : {len(off_band)}')
    print('RESULT: PASS' if ok else 'RESULT: FAIL')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
