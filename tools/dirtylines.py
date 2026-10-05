#!/usr/bin/env python3
"""dirtylines.py <path> [...] — the lines that make a dossier's sections dirty (R-27).

`sectfile.py <path>` says WHICH sections are over 0.05. `sect.py <path>` lists every
line in the file that carries a shared 8-gram. Neither shows the thing that decides
the fix: which lines, inside the dirty section, are doing the damage. This joins the two.
For every section over the threshold it prints only the lines inside that section that
carry shared 8-grams, with their counts.

Often it is one sentence. Eight shared shingles from a single slot-filled line were the
whole of four dossiers' dirty sections (Uprooted, Memory Chain, Animus, Forgotten Tear);
replacing that line, growth-only and written for the one entity, finished each dossier.

The score is a pointer, not a verdict (R-24 constraint 3): a human decides which flagged
lines are furniture and which are mad-libs, and a dossier is never edited to chase the number.

Usage:
    dirtylines.py SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIIγ-959_Uprooted_솟아오른_뿌리.md
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sect  # noqa: E402

THIN = 12  # sections with fewer shingles are judged by eye, as in sectfile.py


def sections_with_lines(text):
    """Yield (name, first_line_number, [(line_number, line), ...]) per `## ` section."""
    cur, start, buf = '(preamble)', 1, []
    for i, ln in enumerate(text.split('\n'), 1):
        if ln.startswith('## '):
            yield cur, start, buf
            cur, start, buf = re.sub(r'\s*—.*', '', ln[3:]).strip(), i, []
        else:
            buf.append((i, ln))
    yield cur, start, buf


def main(paths):
    _, _, shared = sect.build()
    for path in paths:
        ap = path if os.path.isabs(path) else os.path.join(sect.ROOT, path)
        text = io.open(ap, encoding='utf-8').read()
        print('=' * 100)
        print(os.path.basename(ap))
        dirty = 0
        for name, start, body in sections_with_lines(text):
            grams = sect.grams('\n'.join(l for _, l in body))
            if len(grams) < THIN:
                continue
            frac = len(grams & shared) / float(len(grams))
            if frac <= sect.CLEAN_AT:
                continue
            dirty += 1
            print('-- SECTION %r (starts line %d): %d grams, %d shared, fraction %.3f'
                  % (name, start, len(grams), len(grams & shared), frac))
            for i, ln in body:
                hit = len(sect.grams(ln) & shared)
                if hit:
                    print('   L%-4d shared=%-3d %s' % (i, hit, ln.strip()[:210]))
        if not dirty:
            print('0 section(s) over %.2f' % sect.CLEAN_AT)
    return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
