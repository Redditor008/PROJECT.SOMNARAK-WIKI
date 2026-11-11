#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_echo_backstory.py — gate 52: a backstory is a story (R-56, O-42).

WHY THIS EXISTS

The owner read Majin's page and said the back story *"doesnt make sense"*, is *"confusing"*, and
*"not at all look like his back story"*. All three were true, and the third was measurable.

`THE_DIRECTOR.md` § Backstory ran **365 words** in five stub paragraphs — `Origins`, `The
Solidification`, `The Sovereign-Class Containment`, `Chosen by the Alpha Tree`, `Formation of the
R.D.` Each paragraph answered a question an encyclopaedia would ask. None of them told a story. The
other eight Echo-Core dossiers ran **1,099 to 4,932 words**. The central character of the setting had
the shortest life story in the set by a factor of three, and it was not a story at all; it was a
classification with dates missing.

WHAT THE FLOOR IS FOR

A backstory has to carry a person from who they were to who they are, and that takes room. **800
words** is the floor this gate holds, set below the shortest sibling (`THE_RESEARCH_LEAD`, 1,099) so
that the floor catches an absent section rather than policing style.

The floor is a floor, not a target. `O-16` still binds: padding a thin section with adjectives is the
same failure as leaving it thin, disguised. The gate cannot tell the difference between 900 words of
story and 900 words of weather. Only the reader can, and `O-29` / `R-38` still govern that pass.

WHAT FAILS

  * an Echo-Core dossier with no `Backstory` / `Origins` / `History` / `Origin` section;
  * a backstory section under the floor.

    python3 tools/auditors/check_echo_backstory.py
    python3 tools/auditors/check_echo_backstory.py -v
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR = os.path.join(ROOT, 'SOMNARAK-WORLD', 'Echo_Cores')
FLOOR = 800

SECTION = re.compile(r'^## (Backstory|Origins|History|Origin)\s*$(.*?)(?=^## )', re.M | re.S)


def files():
    return [p for p in sorted(glob.glob(os.path.join(DIR, 'THE_*.md')))]


def read(path):
    with io.open(path, encoding='utf-8') as fh:
        return fh.read()


def audit(text):
    """(words, subheads, issue) for one dossier. Pure."""
    m = SECTION.search(text)
    if not m:
        return 0, 0, 'no backstory section'
    body = m.group(2)
    words = len(body.split())
    subheads = len(re.findall(r'^### ', body, re.M))
    if words < FLOOR:
        return words, subheads, 'under the floor'
    return words, subheads, None


def main(argv):
    verbose = '-v' in argv
    rows, bad = [], []
    for path in files():
        words, subs, issue = audit(read(path))
        rows.append((os.path.basename(path), words, subs, issue))
        if issue:
            bad.append((os.path.basename(path), issue, words))
    counts = sorted(r[1] for r in rows if r[1])
    if verbose or bad:
        for name, words, subs, issue in rows:
            print('  %-30s %5dw  subheads %2d  %s' % (name[:28], words, subs, issue or ''))
    if counts:
        mid = counts[len(counts) // 2]
        print('backstories %d · words min %d · median %d · max %d · floor %d'
              % (len(rows), counts[0], mid, counts[-1], FLOOR))
    print('backstories under the floor: %d' % len(bad))
    if bad:
        print('RESULT: FAIL — %d backstories are summaries' % len(bad))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
