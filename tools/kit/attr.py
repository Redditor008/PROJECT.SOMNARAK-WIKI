"""Row-level attribution. Usage: attr.py <file> <SECTION> <partner path or code>..."""
import os, sys, collections, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tools
path, section = sys.argv[1], sys.argv[2]
codes = sys.argv[3:]
nfc = lambda x: unicodedata.normalize('NFC', x)
files = tools.files_under()
by = {}
for f in files:
    d = tools.secmap(f).get(section)
    if d:
        by[f] = d
owner = collections.Counter()
for f, g in by.items():
    for x in g:
        owner[x] += 1
mine = tools.secmap(path).get(section, set())
for c in codes:
    for f in by:
        if not (c == f or nfc(c) == nfc(f)
                or nfc(os.path.basename(c)) == nfc(os.path.basename(f))
                or nfc(c) in nfc(os.path.basename(f))):
            continue
        shared = mine & by[f]
        print('== %s [%s] distinctive %d (mine %d theirs %d)' % (
            os.path.basename(f)[:34], section, len(shared), len(mine), len(by[f])))
        for x in sorted(shared, key=lambda x: -owner[x])[:8]:
            print('    %2d  %s' % (owner[x], x[:96]))
