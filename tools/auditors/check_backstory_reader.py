#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_backstory_reader.py — gate 51: a file is read once, in order (R-55, O-41).

WHY THIS EXISTS

The owner read the Echo-Core Backstory Extended set as a reader and reported that some of it does
not make sense. He gave one example: *Majin*.

He was right, and the fault was structural rather than stylistic. In `01_MAJIN_` the section
`## The Break` sat **before** the Day 149 scene it describes — the reader meets a man reflecting on
an event that has not happened yet. In `02_SEIYON_` Part One ended on **Day 108** and Part Two
opened on **Day 0**, so the file walks backwards through a single cycle. In `07_MARJUK_` a
post-Cycle scene headed **Year 4,235** was filed between Day 49 and Day 77, and the anniversary
scene headed **Day 365** came after the Year 4,238 scene it precedes.

None of that is a matter of taste. A file that is read once, top to bottom, cannot present its
anchors out of order and still be followed. The structure standard already requires a **Scene
ledger** and a **Chronological spine** in every appendix; the spine is the file's own statement of
the order it means to be read in. So the order is not something this gate has to guess at — it is
written down twice, and the gate checks that the body agrees with it.

WHAT FAILS

  * a day anchor going backwards (`### Day 108 — …` followed by `### Day 0 — …`);
  * a year anchor followed by an earlier day anchor, which files the end of the Cycle before the
    middle of it;
  * a body day anchor that the appendix spine does not mention — a scene the file cannot account
    for in its own chronology;
  * a missing `## Appendix`, `### Scene ledger` or `### Chronological spine`.

WHAT IT DOES NOT CHECK

Whether the prose is good, whether a scene earns its place, or whether the numbers reconcile.
Those are the reader's pass (`O-29`, `R-38`). This gate checks only what the file states about
itself, so it cannot go green on a file that is merely told about rather than written.

    python3 tools/auditors/check_backstory_reader.py
    python3 tools/auditors/check_backstory_reader.py -v
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR = os.path.join(ROOT, 'SOMNARAK-WORLD', 'Echo_Cores', 'Backstory_Extended')

DAY = re.compile(r'^#{2,4}\s+Day\s+(\d+)\b', re.M)
YEAR = re.compile(r'^#{2,4}\s+Year\s+(\d[\d,]*)\b', re.M)
SPINE = re.compile(r'^###\s+Chronological spine\s*$(.*?)(?=^###\s|\Z)', re.M | re.S)


def files():
    return sorted(glob.glob(os.path.join(DIR, '*.md')))


def read(path):
    with io.open(path, encoding='utf-8') as fh:
        return fh.read()


def split(text):
    """(body, appendix). The appendix is the file's own account of its order."""
    i = text.find('\n## Appendix')
    return (text, '') if i < 0 else (text[:i], text[i:])


def anchors(body):
    """[(offset, kind, value)] in the order a reader meets them."""
    out = [(m.start(), 'day', int(m.group(1))) for m in DAY.finditer(body)]
    out += [(m.start(), 'year', int(m.group(1).replace(',', ''))) for m in YEAR.finditer(body)]
    return sorted(out)


def appendix_days(appendix):
    """Every day number the appendix names anywhere — ledger or spine."""
    days = {int(d) for d in re.findall(r'\bDay\s+(\d+)\b', appendix)}
    for group in re.findall(r'\bDays\s+([\d,\s]+)', appendix):
        days |= {int(d) for d in re.findall(r'\d+', group)}
    return days


def spine_days(appendix):
    """The day numbers the appendix spine accounts for.

    A spine may name a day alone (`Day 145`) or group several in one row (`Days 7, 41, 73`), which
    is how files 05 and 06 file their flashbacks. Both are the file accounting for the day, so both
    are read rather than only the singular form.
    """
    m = SPINE.search(appendix)
    if not m:
        return None
    text = m.group(1)
    days = {int(d) for d in re.findall(r'\bDay\s+(\d+)\b', text)}
    for group in re.findall(r'\bDays\s+([\d,\s]+)', text):
        days |= {int(d) for d in re.findall(r'\d+', group)}
    return days


def audit(text):
    """(issues) for one file. Pure."""
    issues = []
    body, appendix = split(text)
    if not appendix:
        return [('no Appendix', '')]
    if '### Scene ledger' not in appendix:
        issues.append(('appendix has no Scene ledger', ''))
    seq = anchors(body)
    day_last = None
    year_seen = None
    for _, kind, value in seq:
        if kind == 'day':
            if day_last is not None and value < day_last:
                issues.append(('day anchor goes backwards', '%d then %d' % (day_last, value)))
            day_last = value if day_last is None else max(day_last, value)
            if year_seen is not None:
                issues.append(('day anchor after a year anchor', 'Year %s then Day %d' % (year_seen, value)))
                year_seen = None
        else:
            year_seen = '{:,}'.format(value)
    named = appendix_days(appendix)
    for _, kind, value in seq:
        if kind == 'day' and value not in named:
            issues.append(('day anchor the appendix never accounts for', 'Day %d' % value))
    spine = spine_days(appendix)
    if spine is None:
        issues.append(('appendix has no Chronological spine', ''))
    else:
        # Only a row whose first cell *is* a day anchor sets the spine's order. A day number
        # mentioned inside a description ("Day 157 of the last iteration") is prose, not an anchor.
        order = []
        for row in SPINE.search(appendix).group(1).split('\n'):
            if not row.startswith('|'):
                continue
            first = row.strip('|').split('|')[0]
            m = re.match(r'\s*Day\s+(\d+)\s*$', first)
            if m:
                order.append(int(m.group(1)))
        for a, b in zip(order, order[1:]):
            if b < a:
                issues.append(('the spine itself runs backwards', 'Day %d then Day %d' % (a, b)))
    return issues


def main(argv):
    verbose = '-v' in argv
    total, bad = 0, 0
    for path in files():
        total += 1
        issues = audit(read(path))
        if issues:
            bad += 1
            if verbose:
                for why, detail in issues:
                    print('  %-46s %-34s %s' % (os.path.basename(path)[:44], why, detail))
    print('backstory files %d · read in order %d' % (total, total - bad))
    print('order defects: %d' % bad)
    if bad:
        print('RESULT: FAIL — %d files are not read in the order they state' % bad)
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
