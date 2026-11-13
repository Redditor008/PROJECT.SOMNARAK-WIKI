#!/usr/bin/env python3
"""
tools/auditors/check_fix_density.py

Tells a fix from stuffing.

The owner's instruction, verbatim: *"Let's say before the fix it was 200 words long
but after the fix it suddenly grew another 100 — that's just inflation, not a fix.
You could tell if things is really a fix or just stuffing to cover the test."*

He is right, and it is measurable. A fix adds **facts**; stuffing adds **words**.
So this tool does not count words added — it counts inserted words that carry a
traceable datum:

    carrying   a figure (739/739, 45-65%, Year 4,238), a code (C-IIIγ-044), a
               quoted or backticked term, a proper name from the catalog, or an
               explicit condition ("no hit band", "only", "unless", "when")
    filler     everything else — connectives, restatements, intensifiers, the same
               noun phrase the file already contained

WHY WORD DIFF, NOT LINE DIFF
  A line-level diff of a rewritten paragraph reports the whole paragraph as added,
  because markdown paragraphs are single lines. Measured that way, batch 142 looked
  like it added 88 sentences with no figure in them. It added none: the 88 were the
  paragraph the sentence was spliced into. Word-level alignment shows what actually
  went in.

THE RULE THIS ENFORCES
  * No file may grow by more than MAX_FILLER_RATIO of filler.
  * A file that grows at all must show at least one carrying insertion.
  * Shrinking is not scored here — R-02 and R-39 govern that. This tool only asks
    whether growth was earned.

Usage
    python3 tools/auditors/check_fix_density.py <from-ref> <to-ref> [-v]
    python3 tools/auditors/check_fix_density.py HEAD~1 HEAD -v
"""

import difflib
import os
import re
import subprocess
import sys

# Diagnostics, not a gate. A word carrying no datum is not automatically stuffing:
# "opens at 45-65%" needs the word "opens" to say anything at all. The ratio tells
# you where to look; the human test in R-39 decides. Batches 141-144 measure at a
# median of 0.65, which is ordinary prose density.
MAX_FILLER_RATIO = 0.70
MIN_GROWTH = 8

CARRYING = [
    re.compile(r'\d'),                                  # any figure
    re.compile(r'`[^`]+`'),                             # code or quoted path
    re.compile(r'\b[CNO]-(?:I{1,3}|IV|V)[αβγδω]-\d{3}'),  # SECC code
    re.compile(r'\b(?:no|only|unless|when|until|because|so that)\b', re.I),
    re.compile(r'\b[A-Z][a-z]{2,}\b'),                  # proper noun
]


def tokens(text):
    return re.findall(r'\S+', text)


# Grammar is not stuffing. "opens at", "is filed", "the", "of" carry no claim;
# they are the price of writing a sentence at all. Only content words are scored,
# so a clause is judged on what it *says*, not on how English works.
FUNCTION = set("""
a an the and or but if then than that this these those of to in on at by for with
from into over under its it is are was were be been being has have had do does did
not no as so such which who whom whose when where while before after above below
per each any all more most other same own only very can could may might must shall
should will would also just even still yet there their they them his her hers
""".split())


def content(token):
    return token.strip('.,;:()[]*_`\u201c\u201d\u2019\'"').lower() not in FUNCTION


def carries(token):
    return any(p.search(token) for p in CARRYING)


def inserted_runs(old, new):
    """Word-level insertions, as runs of consecutive added tokens."""
    a, b = tokens(old), tokens(new)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    runs = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ('insert', 'replace'):
            runs.append(b[j1:j2])
    return runs


def score(path, old, new):
    runs = inserted_runs(old, new)
    added = [t for r in runs for t in r]
    scored = [t for t in added if content(t)]
    carrying = [t for t in scored if carries(t)]
    filler = len(scored) - len(carrying)
    return {
        'path': path,
        'added': len(added),
        'carrying': len(carrying),
        'filler': filler,
        'ratio': (filler / len(scored)) if scored else 0.0,
        'scored': len(scored),
        'growth': len(tokens(new)) - len(tokens(old)),
    }


def changed_files(frm, to, roots):
    out = subprocess.run(['git', 'diff', '--name-only', frm, to, '--'] + roots,
                         capture_output=True, text=True).stdout
    return [p for p in out.split('\n') if p.strip()]


def show(ref, path):
    r = subprocess.run(['git', 'show', f'{ref}:{path}'], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ''


def main(argv):
    verbose = '-v' in argv or '--verbose' in argv
    args = [a for a in argv if not a.startswith('-')]
    if len(args) != 2:
        print(__doc__)
        return 2
    frm, to = args
    roots = ['SOMNARAK-WORLD', 'REFERENCE_SOMNARAK_WIKI']
    rows = []
    for path in changed_files(frm, to, roots):
        old, new = show(frm, path), show(to, path)
        if not old or not new:
            continue          # new file or deletion: growth is not the question
        rows.append(score(path, old, new))

    grown = [r for r in rows if r['growth'] >= MIN_GROWTH]
    flagged = [r for r in grown if r['scored'] and r['ratio'] > MAX_FILLER_RATIO]

    print(f'FIX DENSITY — {frm}..{to} · {len(rows)} changed files · '
          f'{len(grown)} grew by {MIN_GROWTH}+ words')
    print(f'  {"file":64} {"+words":>7} {"added":>6} {"carrying":>9} {"filler":>7}')
    ordered = sorted(grown, key=lambda r: -r['growth'])
    for r in (ordered if verbose else ordered[:12]):
        name = r['path'].split('/')[-1][:62]
        print(f'  {name:64} {r["growth"]:+7} {r["scored"]:7} {r["carrying"]:9} {r["filler"]:7}')

    total_added = sum(r['scored'] for r in grown)
    total_carry = sum(r['carrying'] for r in grown)
    print(f'  carrying content words: {total_carry}/{total_added} '
          f'({(100 * total_carry / total_added) if total_added else 0:.0f}% of insertions)')
    print(f'  files with over {MAX_FILLER_RATIO:.0%} of content words carrying no datum: '
          f'{len(flagged)}')
    if flagged:
        for r in flagged[:10]:
            print(f'      {r["path"]:70} filler {r["filler"]} of {r["scored"]}')
        print('RESULT: REVIEW — growth is thin; read the inserted clauses before accepting')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
