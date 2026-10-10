#!/usr/bin/env python3
"""frame_dup.py — repeated prose frames across the wing, with names and figures masked.

Owner's observation, 2026-10-07 — *"Look Like From The 300 Something SE A Lot Of Then Just A
Copy With Change Name"*. The standing tools cannot see this. `sect.py` / `sectfile.py` count
8-grams shared by >= 10 dossiers only and mask nothing, and `tpl.py` compares raw lines, so a
sentence with the dossier's own name and figures substituted into it never matches anything
anywhere. A frame repeated across 115 dossiers therefore passes every gate in the repository.

This auditor closes the gap. Each prose line is masked before it is counted:

  * registry codes       `C-IVδ-907`            -> ~
  * sector ids           SECTOR-C-928, sector-n-910 -> ~
  * figures              1 to 5 digits          -> ~
  * the dossier's own name words, English and Korean -> ~

A *family* is a masked 6-gram carried by K dossiers. R-29's parity clause requires the same
sections; it does not license the same sentences.

  frame_dup.py                   summary: families >= 3 files, exactly-2 pairs, per-file worst
  frame_dup.py --min-files K     families carried by K or more dossiers (default 3)
  frame_dup.py --top N           the N widest families, each with a sample line
  frame_dup.py --closest N       closest dossier pairs by whole-file masked overlap (Jaccard)
  frame_dup.py --budget F        exit 1 if any family spans F files or more; 0 disables (default 0)
  frame_dup.py <path>            one dossier: its share in families, its frames, its neighbours

Read-only; it writes nothing and is not wired into gate.sh, so it can be run at any time.
"""
import collections
import io
import itertools
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WINGS = ['SOMNARAK-WORLD/Sorrow_Entities', 'SOMNARAK-WORLD/Unknown_Entities']
N = 6          # shingle width
MIN_TOK = 8    # a prose line shorter than this (after masking) is not counted
CODE = re.compile(r'[A-Z]-[IVX]+[\u03b1-\u03c9]-\d+[a-z]?')

sys.path.insert(0, os.path.join(ROOT, 'tools'))
import sect  # noqa: E402  (furniture rules and the dossier list live there)


def dossiers():
    out = []
    for d in WINGS:
        base = os.path.join(ROOT, d)
        for f in sorted(os.listdir(base)):
            if f.endswith('.md') and f != 'README.md' and f.startswith('SE-'):
                out.append(os.path.join(base, f))
    return out


def own_tokens(path):
    """The dossier's own name words, English and Korean, as they appear in prose."""
    parts = os.path.basename(path)[:-3].split('_')[1:]
    toks = set()
    for p in parts:
        for w in re.split(r'[_\-\s]+', p):
            if not w:
                continue
            if re.search(r'[\uac00-\ud7a3]', w):
                if len(w) >= 2:
                    toks.add(w)
            elif len(w) > 2 and w.lower() not in ('the', 'of', 'and', 'for'):
                toks.add(w.lower())
    return toks


def is_prose(line):
    t = line.strip()
    if not t or t.startswith(('#', '|', '>', '- **', '**', '<', '[')):
        return False
    if sect.is_furniture(t):
        return False
    return len(t.split()) >= MIN_TOK


def mask(text, own):
    s = text.lower()
    s = CODE.sub('~', s)
    s = re.sub(r'sector[-\s]?[a-z]?[-\s]?\d+', '~', s)
    s = re.sub(r'\b\d{1,5}\b', '~', s)
    for w in sorted(own, key=len, reverse=True):
        s = s.replace(w, '~')
    s = re.sub(r'[^a-z~\s]', ' ', s)
    s = re.sub(r'~+', '~', s)
    return re.sub(r'\s+', ' ', s).strip()


def scan(paths=None):
    files = paths or dossiers()
    owner = collections.defaultdict(set)   # masked gram -> files carrying it
    sample = {}                            # masked gram -> (file, raw line)
    per = {}                               # file -> set of its masked grams
    lines = {}                             # file -> [(raw line, set of grams)]
    for f in files:
        own = own_tokens(f)
        gs, ls = set(), []
        for ln in io.open(f, encoding='utf-8'):
            if not is_prose(ln):
                continue
            w = mask(ln, own).split()
            if len(w) < N:
                continue
            g = {' '.join(w[i:i + N]) for i in range(len(w) - N + 1)}
            for x in g:
                owner[x].add(f)
                sample.setdefault(x, (f, ln.strip()))
            gs |= g
            ls.append((ln.strip(), g))
        per[f] = gs
        lines[f] = ls
    return files, owner, sample, per, lines


def main(argv):
    args = list(argv)
    min_files = 3
    top = 0
    closest = 0
    budget = 0
    paths = []
    i = 0
    while i < len(args):
        a = args[i]
        if a == '--min-files':
            min_files = int(args[i + 1]); i += 1
        elif a == '--top':
            top = int(args[i + 1]); i += 1
        elif a == '--closest':
            closest = int(args[i + 1]); i += 1
        elif a == '--budget':
            budget = int(args[i + 1]); i += 1
        else:
            paths.append(a)
        i += 1

    single = None
    if paths:
        single = paths[0] if os.path.isabs(paths[0]) else os.path.join(ROOT, paths[0])
    files, owner, sample, per, lines = scan([single] if single else None)

    if single:
        gs = per[single]
        fam = {g: owner[g] for g in gs if g in owner}
        wide = [(len(v), g) for g, v in gs and ((g, owner[g]) for g in gs) if len(v) >= 2]
        share = sum(1 for g in gs if len(owner[g]) >= 3) / float(len(gs)) if gs else 0.0
        print('%s' % os.path.basename(single))
        print('  masked %d-grams                 %d' % (N, len(gs)))
        print('  in families of >= 3 dossiers    %d  (%.1f%% of its material)'
              % (sum(1 for g in gs if len(owner[g]) >= 3), share * 100))
        print('  in exactly-2-dossier pairs      %d' % sum(1 for g in gs if len(owner[g]) == 2))
        for c, g in sorted(wide, reverse=True)[:8]:
            f, ln = sample[g]
            print('    %3d files | %s' % (c, ln[:120]))
        return 0

    fam = {g: v for g, v in owner.items() if len(v) >= min_files}
    tot = sum(len(g) for g in per.values())
    inst = sum(len(v) for v in fam.values())
    two = sum(1 for v in owner.values() if len(v) == 2)
    print('dossiers                        %d' % len(files))
    print('distinct masked %d-grams        %d' % (N, len(owner)))
    print('families at >= %d dossiers      %d  (%d instances = %.1f%% of prose material)'
          % (min_files, len(fam), inst, 100.0 * inst / tot if tot else 0.0))
    print('grams in exactly-2-dossier pairs %d' % two)
    rows = sorted(((sum(1 for g in gs if len(owner[g]) >= min_files) / float(len(gs))
                    if gs else 0.0, len(gs), f) for f, gs in per.items()), reverse=True)
    if rows:
        print('worst dossier                   %.1f%%  (%s)'
              % (rows[0][0] * 100, os.path.basename(rows[0][2])))
        mid = rows[len(rows) // 2][0]
        print('median dossier                  %.1f%%' % (mid * 100))
    if top:
        print('\ntop %d families:' % top)
        for c, g in sorted(((len(v), k) for k, v in fam.items()), reverse=True)[:top]:
            f, ln = sample[g]
            print('  %3d files | %s' % (c, ln[:150]))
    if closest:
        print('\nclosest dossier pairs:')
        pairs = []
        for a, b in itertools.combinations(files, 2):
            A, B = per[a], per[b]
            u = len(A | B)
            if u:
                pairs.append((len(A & B) / float(u), a, b))
        pairs.sort(reverse=True)
        for j, a, b in pairs[:closest]:
            print('  %.3f  %-50s  %s' % (j, os.path.basename(a)[:48], os.path.basename(b)[:48]))
    if budget:
        over = [(len(v), k) for k, v in fam.items() if len(v) >= budget]
        print('\nBUDGET: %d family gram(s) span >= %d dossiers' % (len(over), budget))
        if over:
            c, g = max(over)
            print('  widest: %d files | %s' % (c, sample[g][1][:150]))
            return 1
        print('  none')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
