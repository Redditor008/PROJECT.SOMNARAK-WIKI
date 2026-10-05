#!/usr/bin/env python3
"""wikistd.py — the R-29 test: abnormality-wiki parity, plus the clauses above it.

  wikistd.py            archive summary
  wikistd.py --gaps N   the N dossiers furthest from the standard
  wikistd.py <path>     one dossier, clause by clause
"""
import glob, io, os, re, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sect

PARITY = [
    ('classification', ['## SECC Classification']),
    ('stats',          ['## Combat Record']),
    ('work results',   ['## Behavior']),
    ('event behaviour',['## Breach Behavior', '## Activation Behavior',
                        '## Expansion Behavior', '## Containment Event Behavior']),
    ('equipment',      ['## M.A.W. Equipment']),
    ('flavour',        ['## 감각 묘사']),
    ('observation log',['## 관찰 기록']),
    ('story log',      ['## 이야기 보고']),
    ('trivia',         ['## Trivia']),
    ('interactions',   ['### Entity Interaction Record', '## 상호작용']),
]
GENERIC_COND = ('entity-specific management condition', 'Enforce valid Work Types')


def condition(s):
    for pat in (r'suppression condition: \*\*(.+?)\*\*', r'^Management: (.+?)(?:\.|$)',
                r'^\| \*\*Management\*\* \| (.+?) \|$'):
        m = re.search(pat, s, re.M)
        if m:
            t = m.group(1).strip()
            if any(g in t for g in GENERIC_COND) or len(t) < 12:
                continue
            return t
    return None


def own_series(s):
    """A numeric series of the dossier's own: digits inside its record sections."""
    for head in ('## 관찰 기록', '## 기록 (Registrum)', '## Trivia'):
        i = s.find(head)
        if i < 0:
            continue
        j = s.find('\n## ', i + 3)
        body = s[i:j if j > 0 else len(s)]
        if len(re.findall(r'\b\d{1,5}\b', body)) >= 4:
            return True
    return False


def check(path, classified, shared):
    s = io.open(path, encoding='utf-8').read()
    res = {}
    res['parity'] = [name for name, keys in PARITY if not any(k in s for k in keys)]
    res['condition'] = condition(s) is not None
    res['series'] = own_series(s)
    code = re.search(r'`([A-Z]-[IVX]+[\u03b1-\u03c9]-\d+[a-z]?)', s)
    res['disposition'] = bool(code) and code.group(1) in classified
    dirty = 0
    for _, body in sect.split_sections(s):
        g = sect.grams(body)
        if len(g) < 12:
            continue
        if len(g & shared) / float(len(g)) > 0.05:
            dirty += 1
    res['dirty_sections'] = dirty
    res['meets'] = (not res['parity']) and res['condition'] and res['series'] \
        and res['disposition'] and dirty == 0
    return res


def main(argv):
    g = {}
    exec(open(os.path.join(os.path.dirname(__file__), 'disp.py')).read().split('def main')[0], g)
    idx = io.open('REFERENCE_SOMNARAK_WIKI/ENTITY_DISPOSITION_INDEX.md', encoding='utf-8').read()
    classified = g['classified_codes'](idx)
    files, per, shared = sect.build()
    rows = {}
    for f in sorted(glob.glob('SOMNARAK-WORLD/*/SE-*.md')):
        rows[f] = check(f, classified, shared)
    if len(argv) > 1 and argv[1].endswith('.md'):
        r = rows[argv[1]] if argv[1] in rows else check(argv[1], classified, shared)
        for k in ('parity', 'condition', 'series', 'disposition', 'dirty_sections', 'meets'):
            print('%-16s %s' % (k, r[k]))
        return 0
    tot = len(rows)
    meets = sum(1 for r in rows.values() if r['meets'])
    miss = collections.Counter()
    for r in rows.values():
        for p in r['parity']:
            miss[p] += 1
    print('R-29: %d / %d dossiers meet the standard' % (meets, tot))
    print('  parity complete          %d' % sum(1 for r in rows.values() if not r['parity']))
    print('  specific condition       %d' % sum(1 for r in rows.values() if r['condition']))
    print('  own numeric series       %d' % sum(1 for r in rows.values() if r['series']))
    print('  disposition classified   %d' % sum(1 for r in rows.values() if r['disposition']))
    print('  section-clean (R-27)     %d' % sum(1 for r in rows.values() if r['dirty_sections'] == 0))
    if miss:
        print('  missing parity sections:')
        for k, v in miss.most_common():
            print('    %-18s %d' % (k, v))
    if '--gaps' in argv:
        n = int(argv[argv.index('--gaps') + 1])
        worst = sorted(rows.items(), key=lambda kv: (-len(kv[1]['parity']), -kv[1]['dirty_sections']))
        for f, r in worst[:n]:
            print('  %-46s parity-missing=%s dirty=%d cond=%s series=%s'
                  % (f.split('/')[-1][:46], ','.join(r['parity']) or '-', r['dirty_sections'],
                     r['condition'], r['series']))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
