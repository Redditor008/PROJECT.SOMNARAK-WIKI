# -*- coding: utf-8 -*-
"""Gate 56 — every scene carries a stamp (R-62, § IV.6).

The owner's instruction, 2026-10-25:

  "YOU SHOULD USED xxx Time[Can Be Days/Month/Years/Just Hour/Minute] BEFORE [REDACTED] Happened.
   The Redacted Will Only Be Shown On The 00:00 Before XXX Happened Instead Of [REDACTED] So There
   Is A Clear Time Stamp For Easier Pinning."

A stamp is one line under a scene heading:

  > **STAMP — 9 days before [REDACTED] happened · 17:40 · Floor 3, the bench**

WHAT THIS CHECKS

  * every scene heading in a Backstory_Extended file is followed by a stamp;
  * the stamp has an offset, a clock and a place;
  * the offset uses a unit — years, months, weeks, days, hours, minutes;
  * `[REDACTED]` never appears after the scene that lifts it;
  * the lifting scene is stamped from 00:00.

WHAT IT DOES NOT DO

It cannot tell whether the offset is *true*. A stamp of "3 days before" on a scene that is a year
later still passes. Correctness is the reader's pass and the spine's job.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR = os.path.join(ROOT, 'SOMNARAK-WORLD', 'Echo_Cores', 'Backstory_Extended')

HEAD = re.compile(r'^(#{2,4}) (.+)$', re.M)
STAMP = re.compile(r'^> \*\*STAMP — (.+)\*\*\s*$', re.M)
UNIT = re.compile(r'\b(year|years|month|months|week|weeks|day|days|hour|hours|minute|minutes)\b', re.I)
CLOCK = re.compile(r'\b([01]?\d|2[0-3]):[0-5]\d\b')
# headings that are apparatus, not scenes
# Files converted to the stamp convention. The rest are carried as visible debt and do not fail
# the gate, exactly as NAMED_THINGS/BODIES began on one file. A file joins this list when it is
# stamped, and the debt count below is the work remaining.
CONVERTED = {'01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md'}

SKIP = re.compile(r'^(Appendix|Scene ledger|Cast|Holds|HOLDs|Source ledger|Continuity note|'
                  r'Validation record|Promotion Check|Knowledge boundaries|The one wound|'
                  r'Chronological spine|Objects, rooms|Relationships in motion|Connection string|'
                  r'The name she is filed under|§IV|REGISTER)', re.I)


def read(path):
    with io.open(path, encoding='utf-8') as fh:
        return fh.read()


def scenes(text):
    """(heading, level, body) for every scene unit before the appendix."""
    i = text.find('\n## Appendix')
    body = text if i < 0 else text[:i]
    marks = list(HEAD.finditer(body))
    out = []
    for n, m in enumerate(marks):
        end = marks[n + 1].start() if n + 1 < len(marks) else len(body)
        out.append((m.group(2).strip(), m.group(1), body[m.end():end]))
    return out


def check_file(path, verbose=False):
    issues = []
    text = read(path)
    base = os.path.basename(path)
    redacted_seen = []
    lifted = None

    for name, level, body in scenes(text):
        if SKIP.match(name) or level == '##' and name.lower().startswith('appendix'):
            continue
        # a chapter heading (##) whose next heading is a scene is a division, not a scene
        m = STAMP.search(body)
        first_line = body.strip().split('\n')[0] if body.strip() else ''
        if not m:
            if level == '##' and HEAD.search(body):
                continue          # a division, not a scene
            issues.append('%s: %r carries no STAMP' % (base, name))
            continue
        fields = [f.strip() for f in m.group(1).split('·')]
        if len(fields) < 3:
            issues.append('%s: %r stamp needs offset · clock · place, got %d field(s)'
                          % (base, name, len(fields)))
            continue
        offset, clock, place = fields[0], fields[1], fields[2]
        if not UNIT.search(offset):
            issues.append('%s: %r stamp offset %r names no unit' % (base, name, offset))
        if not CLOCK.search(clock) and '00:00' not in offset:
            issues.append('%s: %r stamp carries no clock time' % (base, name))
        if not place:
            issues.append('%s: %r stamp carries no place' % (base, name))
        if '[REDACTED]' in body:
            redacted_seen.append(name)
        if lifted is None and 'redaction lifts' in body:
            lifted = name
            if '00:00' not in offset:
                issues.append('%s: the lifting scene %r is not stamped from 00:00' % (base, name))
        if verbose:
            print('  %-44s %-30s %s' % (base[:42], name[:28], offset[:40]))

    # nothing may count toward [REDACTED] after the bracket has been lifted
    if lifted:
        order = [n for n, _, _ in scenes(text)]
        after = order[order.index(lifted) + 1:] if lifted in order else []
        for name, _, body in scenes(text):
            if name in after and '[REDACTED]' in body:
                issues.append('%s: %r still counts toward [REDACTED] after the lift at %r'
                              % (base, name, lifted))
    return issues


def main(argv):
    verbose = '-v' in argv
    issues = []
    files = sorted(f for f in os.listdir(DIR) if f.endswith('.md'))
    debt = 0
    for f in files:
        if f not in CONVERTED:
            debt += len([1 for n, lv, _ in scenes(read(os.path.join(DIR, f)))
                         if not SKIP.match(n) and lv != '##'])
            continue
        issues.extend(check_file(os.path.join(DIR, f), verbose))
    print('stamped scenes audited across %d file(s) · %d scene(s) of debt in files not yet converted'
          % (len(CONVERTED), debt))
    for i in issues:
        print('  ' + i)
    if issues:
        print('RESULT: FAIL — %d stamp defects' % len(issues))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
