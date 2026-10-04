#!/usr/bin/env python3
"""sectfile.py <path> — the Tale Standard applied section by section (R-27).

`sect.py <path>` scores a whole dossier. That hides the failure mode R-27 names:
a file can pass at 0.05 overall while one description-heavy section — Behavior,
the sensory block, Registrum, the M.A.W. profile, Trivia — is still entirely
generated. This reports every section separately so none of them can hide
behind the file's average.

A section is CLEAN at <= 0.05 of its own prose shingles being shared, and is
reported DIRTY otherwise. Sections shorter than 12 shingles are reported as
THIN and judged by eye rather than by the number.
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sect

CLEAN_AT = 0.05
THIN = 12


def main(path):
    files, per, shared = sect.build()
    text = io.open(path, encoding='utf-8').read()
    rows, dirty = [], 0
    for name, body in sect.split_sections(text):
        g = sect.grams(body)
        if not g:
            continue
        hit = g & shared
        frac = len(hit) / float(len(g))
        if len(g) < THIN:
            state = 'THIN'
        elif frac <= CLEAN_AT:
            state = 'clean'
        else:
            state = 'DIRTY'
            dirty += 1
        rows.append((frac, len(g), state, name))
    rows.sort(reverse=True)
    for frac, n, state, name in rows:
        print('%6.3f  %-5s  %4d grams  %s' % (frac, state, n, name[:70]))
    print('%d section(s) over %.2f' % (dirty, CLEAN_AT))
    return 1 if dirty else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
