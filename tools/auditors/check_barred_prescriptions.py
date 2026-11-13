#!/usr/bin/env python3
"""check_barred_prescriptions.py — no live surface still hands the pair a retired token.

`R-41` retired `N/A`, `0%` and `-100%` from the Flerehan/Pugnahan cells: the two
cells print **Net-Neutral** or **Negative-Low**, read off the Conversion Guide's
2–10 Threat Score. Three batches carried that to the dossiers, the Side Codex
pages, the guides, the Conversion Guide and the builders that write them.

It came back three times, each time somewhere the sweep had not looked:

* batch 163 — the Conversion Guide's own five `N/A` prescriptions;
* batch 169 — nine live documents, including the SE template primer and the
  published `docs/game-wiki/index.html`;
* batch 169 — four builders that would put the token back on the next run.

A retirement that has to be re-found by hand every batch is not a rule. This
gate reads the surfaces a writer copies from — templates, the docs site, the
canon comparison, the research guides, the rules, and `tools/builders` — and
fails on any line that gives the pair a retired token outside retirement
language.

Not read, on purpose:

* `ARCHIVE/`, `REFERENCE_SOMNARAK_WIKI/AUDITS/`, `SE_APPEARANCE_REVIEWS/` and
  `tools/repairs_and_patches/` — records of past states, which are supposed to
  quote the token they removed;
* `tools/tests/` — fixtures that exist to make another gate fail;
* `CHANGELOG.md` and `WORK_IN_PROGRESS.md` — the batches' own account of it.
"""
import glob
import io
import re
import sys

SURFACES = (
    'TEMPLATES/**/*.md',
    'docs/**/*.md',
    'docs/**/*.html',
    'CANON/**/*.md',
    'PROJECT_MOON_RESEARCH/**/*.md',
    'REFERENCE_SOMNARAK_WIKI/GUIDES/**/*.md',
    'REFERENCE_SOMNARAK_WIKI/RULES/**/*.md',
    'tools/builders/*.py',
)

PAIR = re.compile(r'Flerehan|Pugnahan')
TOKEN = re.compile(r'\bN/A\b|(?<![\d.\u2212])-\s*100\s*%|(?<![\d.])0\s*%')
# A sentence that names the token in order to retire it is the rule working.
RETIRING = re.compile(r'never|retire|no longer|instead of|rather than|gone|not ', re.I)

# (path fragment, text fragment, why it is allowed to print the token)
ALLOW = [
    ('R-40_A_RELIC_IS_HANDLED_NOT_WORKED.md', 'Flerehan / Pugnahan -> N/A',
     'the Old column of an Old -> New mapping table: it records what was replaced'),
    ('R-41_THE_BARRED_CELLS_ARE_WORDS.md', 'N/A',
     'the rule that retires the token names it while doing so'),
]


def allowed(path, line):
    for frag, text, _ in ALLOW:
        if frag in path and text in line:
            return True
    return False


def line_problem(line, path=''):
    """True when the line gives the pair a retired token without retiring it."""
    if not PAIR.search(line) or not TOKEN.search(line):
        return False
    if allowed(path, line):
        return False
    for m in TOKEN.finditer(line):
        # either side: "N/A ... are retired" retires the token just as plainly
        # as "never N/A".
        window = line[max(0, m.start() - 30):m.end() + 40]
        if not RETIRING.search(window):
            return True
    return False


def scan():
    hits = []
    for pattern in SURFACES:
        for path in sorted(glob.glob(pattern, recursive=True)):
            try:
                lines = io.open(path, encoding='utf-8').read().split('\n')
            except (OSError, UnicodeDecodeError):
                continue
            for n, line in enumerate(lines, 1):
                if line_problem(line, path):
                    hits.append((path, n, line.strip()[:150]))
    return hits


def main():
    hits = scan()
    for path, n, line in hits:
        print('%s:%d  %s' % (path, n, line))
    print('live surfaces %d  prescriptions %d  allowlisted %d'
          % (len(SURFACES), len(hits), len(ALLOW)))
    if hits:
        print('RESULT: FAIL')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
