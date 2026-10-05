#!/usr/bin/env python3
"""breach.py — breach-capability census and quota check (R-28).

Groups every entity dossier as:
  RE  relic entities (a Tool Type is declared)
  OP  Object/Place entities with no Tool Type
  SE  everything else (Subject, Time, Hazard, Phenomenon ...)

An entity counts as BREACHING when its Entity Type cell claims a breach capability
(the token 'non-breaching' is discounted first). R-28 sets floors for the non-breaching share of each group:
  RE >= 75%   SE >= 25%   OP >= 50%

Exit status is non-zero if any floor is unmet, so gate.sh can refuse a commit
that regresses the balance.
"""
import glob, io, re, sys, collections

FLOOR = {'RE': 0.75, 'SE': 0.25, 'OP': 0.50}


def classify(path):
    s = io.open(path, encoding='utf-8').read()
    m = re.search(r'\| \*\*Entity Type\*\* \| (.+?) \|', s)
    et = m.group(1).strip() if m else ''
    tool = bool(re.search(r'\| \*\*Tool Type\*\* \|', s))
    if tool:
        g = 'RE'
    elif et.startswith('**Object') or et.startswith('**Place'):
        g = 'OP'
    else:
        g = 'SE'
    low = et.lower().replace('non-breaching', '')
    return g, ('breach' in low), et, s


def main(argv):
    tot, nb = collections.Counter(), collections.Counter()
    listing = collections.defaultdict(list)
    for f in glob.glob('SOMNARAK-WORLD/*/SE-*.md'):
        g, breaching, et, s = classify(f)
        tot[g] += 1
        if not breaching:
            nb[g] += 1
            listing[g].append(f)
    bad = 0
    print('group  total  non-breaching   share   floor   status')
    for g in ('RE', 'SE', 'OP'):
        share = nb[g] / float(tot[g]) if tot[g] else 0.0
        ok = share >= FLOOR[g]
        bad += 0 if ok else 1
        print('%-5s  %5d  %13d  %6.1f%%  %5.0f%%   %s'
              % (g, tot[g], nb[g], share * 100, FLOOR[g] * 100, 'OK' if ok else 'UNDER'))
    print('%d / %d dossiers non-breaching overall' % (sum(nb.values()), sum(tot.values())))
    if '--list' in argv:
        for g in ('RE', 'SE', 'OP'):
            print('\n%s non-breaching:' % g)
            for f in sorted(listing[g]):
                print('   ' + f.split('/')[-1])
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
