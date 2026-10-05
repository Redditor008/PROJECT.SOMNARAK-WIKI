#!/usr/bin/env python3
"""ladder.py - what changes with level in this archive (R-29, Comparative Study 02).

Comparative Study 02 read twenty Abnormality pages across all five risk levels and found
that the reference wiki's frame does not change with level while its contents do:
breach capability, harm radius, the price of the remedy and the facility's own numbers
all climb from ZAYIN to ALEPH. This tool measures the same climb in the dossiers, by
Coherence rank (I..V), so the study's figures can be regenerated and tracked.

  ladder.py            the five tables below
  ladder.py --rows     one line per dossier (code, rank, potency, HP, ATK, breach, ...)

It reports and never edits. It is not part of the gate.
"""
import collections, glob, io, os, re, statistics, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import breach, sect, wikistd  # noqa: E402

RANKS = ['I', 'II', 'III', 'IV', 'V']
POTENCIES = '\u03b1\u03b2\u03b3\u03b4\u03c9'
EVENT = ['## Breach Behavior', '## Activation Behavior', '## Expansion Behavior',
         '## Containment Event Behavior']
# The record section that each rank adds on top of the shared frame.
RANK_RECORD = {'II': '## Watch Record', 'III': '## Warden Record',
               'IV': '## Apex Record', 'V': '## Sovereign Chronicle'}
# SOMNARAK_PM_CONVERSION guide, Section III: Sorrow Gauge range per rank.
GUIDE_HP = {'I': (150, 300), 'II': (300, 500), 'III': (500, 750), 'IV': (750, 1000),
            'V': (1000, 12000)}
FIVE = re.compile(r'(?:\+|by\s+)\s*(?:5|five)\b[^|.;]{0,40}?(?:per|each|every)\s+'
                  r'(?:turn|cycle|round)|\b(?:5|five)\s+(?:\w+\s+){0,3}(?:per|each)\s+'
                  r'(?:turn|cycle)', re.I)
BANNER = re.compile(r'^> \*\*(This (?:Relic|Entity|Object|Place)[^*]+)\*\*\s*$', re.M)


def section(s, head):
    i = s.find('\n' + head)
    if i < 0:
        return ''
    j = s.find('\n## ', i + 5)
    return s[i:j if j > 0 else len(s)]


def med(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None


def fmt(x, nd=0):
    if x is None:
        return '-'
    return ('%.*f' % (nd, x)) if nd else ('%d' % round(x))


def dispositions():
    """code -> Positive/Neutral/Negative, read from the Entity Disposition Index."""
    g = {}
    exec(open('tools/disp.py', encoding='utf-8').read().split('def main')[0], g)
    t = io.open('REFERENCE_SOMNARAK_WIKI/ENTITY_DISPOSITION_INDEX.md', encoding='utf-8').read()
    codes = g['classified_codes'](t)
    pos = dict((n, t.find('\n## %s\n' % n)) for n in ('Positive', 'Neutral', 'Negative'))
    end = {'Positive': pos['Neutral'], 'Neutral': pos['Negative'],
           'Negative': t.find('\n## Why the Negative')}
    out = {}
    for c in codes:
        for n in ('Positive', 'Neutral', 'Negative'):
            if c in t[pos[n]:end[n]]:
                out[c] = n
                break
    return out


def scan():
    g = {}
    exec(open('tools/disp.py', encoding='utf-8').read().split('def main')[0], g)
    idx = io.open('REFERENCE_SOMNARAK_WIKI/ENTITY_DISPOSITION_INDEX.md', encoding='utf-8').read()
    classified = g['classified_codes'](idx)
    _, _, shared = sect.build()
    disp = dispositions()
    rows = []
    for f in sorted(glob.glob('SOMNARAK-WORLD/*/SE-*.md')):
        b = os.path.basename(f)
        m = re.match(r'SE-([CON])-([IVX]+)([\u03b1-\u03c9])-(\d+[a-z]?)_', b)
        if not m:
            continue
        s = io.open(f, encoding='utf-8').read()
        r = dict(file=b, origin=m.group(1), rank=m.group(2), pot=m.group(3),
                 code='%s-%s%s-%s' % m.groups())
        r['words'] = len(s.split())
        hp = re.search(r'\*\*Sorrow Gauge \[HP\]\*\*\s*\|\s*([\d,]+)', s)
        r['hp'] = int(hp.group(1).replace(',', '')) if hp else None
        am = re.search(r'\*\*Han Pressure \[ATK\]\*\*\s*\|\s*(\d+)\s*[\u2013\-]\s*(\d+)', s)
        r['atk'] = (am.group(0).split('|')[-1].strip(), int(am.group(2))) if am else None
        sp = re.search(r'\*\*Speed\*\*\s*\|\s*([\d.]+)', s)
        r['speed'] = float(sp.group(1)) if sp else None
        ym = re.search(r'\*\*Han-Energy yield\*\*\s*\|\s*(\d+)\s*[\u2013\-]\s*(\d+)', s)
        r['yield'] = (int(ym.group(1)), int(ym.group(2))) if ym else None
        _, r['breaching'], _, _ = breach.classify(f)
        body = ''
        for h in EVENT:
            body = section(s, h)
            if body:
                break
        r['event_words'] = len(body.split()) if body else None
        em = re.search(r'\|\s*\*\*Escalation\*\*\s*\|\s*(.+?)\s*\|\s*$', body, re.M)
        r['esc_cell'] = em.group(1) if em else None
        r['esc_five'] = bool(r['esc_cell'] and FIVE.search(r['esc_cell']))
        rec = RANK_RECORD.get(r['rank'])
        r['record_words'] = len(section(s, rec).split()) if rec and section(s, rec) else None
        r['banners'] = BANNER.findall(s)
        chk = wikistd.check(f, classified, shared)
        r['meets'] = chk['meets']
        r['disp'] = disp.get(r['code'])
        rows.append(r)
    return rows


def main(argv):
    rows = scan()
    if '--rows' in argv:
        for r in rows:
            print('%-12s %-3s %s hp=%-6s atk=%-10s breach=%-5s event_w=%-4s record_w=%-5s %s'
                  % (r['code'], r['rank'], r['pot'], r['hp'], (r['atk'] or ('-',))[0],
                     r['breaching'], r['event_words'], r['record_words'], r['disp']))
        return 0
    by = collections.defaultdict(list)
    for r in rows:
        by[r['rank']].append(r)

    print('1. LADDER BY COHERENCE RANK (%d dossiers)' % len(rows))
    print('%-5s %4s %6s %6s %6s %6s %7s %8s %8s %8s %-11s %5s' % (
        'rank', 'n', 'words', 'HP', 'ATKmax', 'speed', 'yield', 'breach%', 'event w',
        'record w', 'P / Ne / Ng', 'R-29'))
    for rk in RANKS:
        R = by[rk]
        d = collections.Counter(r['disp'] for r in R)
        ylo = med([r['yield'][0] if r['yield'] else None for r in R])
        yhi = med([r['yield'][1] if r['yield'] else None for r in R])
        print('%-5s %4d %6s %6s %6s %6s %7s %7.0f%% %8s %8s %-11s %5d' % (
            rk, len(R), fmt(med([r['words'] for r in R])), fmt(med([r['hp'] for r in R])),
            fmt(med([r['atk'][1] if r['atk'] else None for r in R])),
            fmt(med([r['speed'] for r in R]), 2), '%s-%s' % (fmt(ylo), fmt(yhi)),
            100.0 * sum(1 for r in R if r['breaching']) / len(R),
            fmt(med([r['event_words'] for r in R])), fmt(med([r['record_words'] for r in R])),
            '%d/%d/%d' % (d['Positive'], d['Neutral'], d['Negative']),
            sum(1 for r in R if r['meets'])))
    print('   yield    = Han-Energy yield per work cycle, median low-high')
    print('   breach%  = Entity Type cell claims a breach capability (tools/breach.py)')
    print('   record w = the section each rank adds: Watch (II), Warden (III), Apex (IV), '
          'Sovereign Chronicle (V)')

    print('\n2. THE STAT LINE FOLLOWS POTENCY (Sorrow Gauge [HP] median, shared values)')
    hp = collections.Counter(r['hp'] for r in rows if r['hp'])
    for p in POTENCIES:
        P = [r for r in rows if r['pot'] == p]
        print('   %s  n=%-3d HP median %-6s ATKmax median %-4s distinct HP values %d' % (
            p, len(P), fmt(med([r['hp'] for r in P])),
            fmt(med([r['atk'][1] if r['atk'] else None for r in P])),
            len(set(r['hp'] for r in P if r['hp']))))
    top = hp.most_common(4)
    print('   %d distinct HP values over %d dossiers; the four commonest (%s) cover %d'
          % (len(hp), sum(hp.values()), ', '.join('%d x%d' % kv for kv in top),
             sum(c for _, c in top)))

    print('\n3. CONFORMANCE TO THE CONVERSION GUIDE (Sorrow Gauge range per rank)')
    for rk in RANKS:
        lo, hi = GUIDE_HP[rk]
        R = [r for r in by[rk] if r['hp']]
        inside = sum(1 for r in R if lo <= r['hp'] <= hi)
        print('   %-4s guide %5d-%-6d inside %3d / %-3d  below %3d  above %3d' % (
            rk, lo, hi, inside, len(R), sum(1 for r in R if r['hp'] < lo),
            sum(1 for r in R if r['hp'] > hi)))

    print('\n4. THE ESCALATION FIGURE (event table row, "5 per turn or cycle")')
    for rk in RANKS:
        cells = [r for r in by[rk] if r['esc_cell']]
        five = sum(1 for r in cells if r['esc_five'])
        print('   %-4s cells %3d / %-3d  mention 5 per turn/cycle: %3d (%.0f%%)' % (
            rk, len(cells), len(by[rk]), five, 100.0 * five / max(1, len(cells))))
    allc = [r for r in rows if r['esc_cell']]
    print('   all  cells %3d / %-3d  mention 5 per turn/cycle: %3d (%.0f%%)' % (
        len(allc), len(rows), sum(1 for r in allc if r['esc_five']),
        100.0 * sum(1 for r in allc if r['esc_five']) / max(1, len(allc))))

    print('\n5. RELIC BANNER VOCABULARY (capability banners above the Activation table)')
    ban = collections.Counter(b for r in rows for b in r['banners'])
    print('   %d dossiers carry a banner; %d distinct strings' % (
        sum(1 for r in rows if r['banners']), len(ban)))
    for b, c in ban.most_common():
        print('   %3d  %s' % (c, b))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
