#!/usr/bin/env python3
"""personal_audit.py — which dossiers still sound generic, and in which sentences?

Owner's direction, 2026-10-07 — *"Now Readying For Per-10 Batch Update For All SE That Need It Because A Lot Sound
Generic And Not Personalize At ALL."*

Method. A dossier is *personalized* where its prose is its own and *generic* where its prose is built from phrasing it
shares with other dossiers. The clone audit measures copies (verbatim blocks); this tool measures the finer grain that
remains after the copies are gone: every prose line is masked (names, registry codes, sector ids and figures removed) and
cut into 6-word shingles, exactly as `frame_dup.py` does, and each shingle is sorted into a **family** — the set of
dossiers carrying it.

  generic mass   = share of the file's prose shingles whose family holds >= 3 dossiers (mechanics lines exempt)
  house mass     = the share of those held by >= 10 (furniture-level: the frames a reader meets everywhere)
  personal mass  = 1 - generic mass

Read-only. Output feeds the per-10 batch queue.

  personal_audit.py                 summary + ranked worst-first list
  personal_audit.py --top N         show N files (default 40)
  personal_audit.py --threshold T   the "needs it" line in percent (default 5.0)
  personal_audit.py --batch K       print the K-th ten-file batch of the queue (1-based)
  personal_audit.py --frames P      top generic frames of one dossier (path or basename fragment)
  personal_audit.py --report FILE   write the full plan (markdown) to FILE
"""
import argparse
import collections
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))
import frame_dup  # noqa: E402  (own_tokens, mask, is_prose, scan, N)

HOUSE = 10      # families this wide read as house furniture, not shared prose
STRUCT = ('viderehan', 'ferrehan', 'flerehan', 'pugnahan', 'sorrow gauge', 'work type', 'object place',
          'r d comprehension', 'm a w', 'han energy', 'vessel destructible', 'sector')  # mechanics, exempt from the prose queue


def designation(path):
    m = re.search(r'SE-([A-Z])-([IVX]+)([\u03b1-\u03c9]+)-(\d+)([a-z]?)', os.path.basename(path))
    return '%s-%s%s-%s%s' % (m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)) if m else '?'


def name_of(path):
    return os.path.basename(path)[:-3].split('_', 1)[1].replace('_', ' ')


def analyse():
    files, owner, sample, per, lines = frame_dup.scan()
    rows = []
    for f in files:
        gs = per[f]
        if not gs:
            continue
        gen = [g for g in gs if len(owner[g]) >= 3]
        house = [g for g in gen if len(owner[g]) >= HOUSE]
        struct = [g for g in gen if any(t in g for t in STRUCT)]
        free = [g for g in gen if g not in set(struct)]
        worst = sorted(free, key=lambda g: (-len(owner[g]), -len(g)))[:6]
        rows.append({
            'file': f,
            'code': designation(f),
            'name': name_of(f),
            'grams': len(gs),
            'generic': len(gen),
            'house': len(house),
            'struct': len(struct),
            'free': len(free),
            'mass': 100.0 * len(free) / len(gs),
            'housemass': 100.0 * len(house) / len(gs),
            'worst': [(g, len(owner[g])) for g in worst],
        })
    rows.sort(key=lambda r: -r['mass'])
    return rows, owner, lines


def fmt(r):
    return '%-46s %-12s %5.1f%%  generic %5d / %-5d  house %5.1f%%' % (
        r['name'][:46], r['code'], r['mass'], r['generic'], r['grams'], r['housemass'])


def main(argv=None):
    ap = argparse.ArgumentParser(description='generic-phrasing audit and the per-10 personalization queue')
    ap.add_argument('--top', type=int, default=40)
    ap.add_argument('--threshold', type=float, default=5.0)
    ap.add_argument('--batch', type=int, default=0)
    ap.add_argument('--frames', metavar='PATH')
    ap.add_argument('--report', metavar='FILE')
    args = ap.parse_args(argv)

    rows, owner, lines = analyse()
    need = [r for r in rows if r['mass'] >= args.threshold]
    n = len(rows)

    if args.frames:
        hit = [r for r in rows if args.frames in r['file'] or args.frames in r['name']]
        if not hit:
            print('no dossier matches', args.frames)
            return 1
        r = hit[0]
        print('%s  [%s]  generic %.1f%%  ( %d / %d shingles )' % (r['name'], r['code'], r['mass'], r['generic'], r['grams']))
        for g, c in r['worst']:
            print('  x%-3d %s' % (c, g))
        return 0

    if args.batch:
        lo = (args.batch - 1) * 10
        sel = need[lo:lo + 10]
        if not sel:
            print('batch %d is past the end of the queue (%d files need it, %d batches)'
                  % (args.batch, len(need), (len(need) + 9) // 10))
            return 1
        print('PERSONALIZATION BATCH %d — files %d-%d of %d (of %d needing it)' % (
            args.batch, lo + 1, lo + len(sel), len(need), n))
        for i, r in enumerate(sel, lo + 1):
            print('%3d. %s' % (i, fmt(r)))
        return 0

    print('PERSONALIZATION AUDIT — %d dossiers measured, %d shingles distinct' % (n, len(owner)))
    print('  needs it (generic mass >= %.1f%%): %d / %d  ->  %d batches of ten' % (
        args.threshold, len(need), n, (len(need) + 9) // 10))
    tiers = [('heavy  (>= 10%)', [r for r in rows if r['mass'] >= 10]),
             ('moderate (7-10%)', [r for r in rows if 7 <= r['mass'] < 10]),
             ('light  (5-7%)', [r for r in rows if 5 <= r['mass'] < 7]),
             ('fine   (< 5%)', [r for r in rows if r['mass'] < 5])]
    for label, rs in tiers:
        print('  %-16s %d / %d' % (label, len(rs), n))
    print()
    for r in rows[:args.top]:
        print('  ' + fmt(r))

    if args.report:
        with io.open(args.report, 'w', encoding='utf-8') as fh:
            fh.write('# Personalization plan — per-10 batch update\n\n')
            fh.write("Owner's direction, 2026-10-07: *\"Now Readying For Per-10 Batch Update For All SE That Need It Because A Lot "
                     "Sound Generic And Not Personalize At ALL.\"*\n\n")
            fh.write('Measured by `tools/auditors/personal_audit.py` (read-only). Method: every prose line masked like the frame '
                     'audit (names, codes, sectors and figures removed) and cut into 6-word shingles; a shingle belongs to a family '
                     'of the dossiers carrying it. **Generic mass** = share of the file\'s shingles held by 3 or more dossiers; '
                     '**house mass** = share held by 10 or more. Mechanics lines (work types, gauges, the M.A.W. vocabulary) are '
            'exempt from the prose queue and counted separately.\n\n')
            fh.write('| tier | files |\n|---|---|\n')
            for label, rs in tiers:
                fh.write('| %s | **%d / %d** |\n' % (label, len(rs), n))
            fh.write('\n**Queue: %d / %d need it -> %d batches of ten.**\n\n' % (len(need), n, (len(need) + 9) // 10))
            fh.write('## The queue, worst first\n\n| # | dossier | code | generic mass | house mass |\n|---|---|---|---|---|\n')
            for i, r in enumerate(need, 1):
                fh.write('| %d | %s | `%s` | **%.1f%%** | %.1f%% |\n' % (i, r['name'], r['code'], r['mass'], r['housemass']))
            fh.write('\n## Batch assignments\n\n')
            for b in range(1, (len(need) + 9) // 10 + 1):
                sel = need[(b - 1) * 10:b * 10]
                fh.write('**Batch %d.** %s\n\n' % (b, ' · '.join('%s `%s`' % (r['name'], r['code']) for r in sel)))
            fh.write('## Method for a unit\n\n')
            fh.write('1. `personal_audit.py --frames "<name>"` — read the file\'s top shared frames.\n')
            fh.write('2. Find those sentences in the file; re-author each **in place** in that file\'s own terms, using its own '
                     'furniture (its objects, rooms, shifts, figures, Story Log entries) — growth-only (`R-15`), never deleted.\n')
            fh.write('3. Re-run the per-dossier checks; the file\'s generic mass must fall and its word count must rise.\n')
            fh.write('4. One wave per unit, one commit, one push (`A0`); docs row with the SE link (`R-12`).\n')
        print('\nreport written:', args.report)
    return 0


if __name__ == '__main__':
    sys.exit(main())
