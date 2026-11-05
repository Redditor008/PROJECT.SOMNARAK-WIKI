#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_se_effect.py — gate 89: some holdings have one thing they do (R-50).

The owner's instruction, 2026-11-05:

> *"An Individual Specific SE Effect Can Happen In Any Ways Of Forms [When Breach Happen [Any Kind],
> Finished Working The SE, Special Effect Of SE And More] And It Will Be Only On 45% Of The SE"*

`**SE Effect**` is the one row in a dossier that is not derived from a rule: it is the holding's own
law, and it fires on an occasion read off the file's own `**Activation threshold**` and
`**Entity Type**`.

WHAT FAILS
  * a row count other than **135 of 301** (45 %);
  * a trigger outside the six, or a cell that does not open `**On …** —`;
  * an effect under ten words, or one that reads as a percentage, a cooldown or a dice roll;
  * two dossiers carrying the same effect;
  * an effect drawing more than a tenth of its vocabulary from outside its own dossier — an invented
    sentence that leans on boilerplate;
  * a Work Type name in a relic's effect (`R-40`: a relic offers none);
  * `**On the breach**` on a holding whose `**Entity Type**` permits no breach.

    python3 tools/auditors/check_se_effect.py          # ratchet check
    python3 tools/auditors/check_se_effect.py -v       # per-dossier trigger
    python3 tools/auditors/check_se_effect.py --stats  # the split
"""
import collections
import glob
import io
import re
import sys

PATHS = [p for p in sorted(glob.glob('SOMNARAK-WORLD/**/SE-*.md', recursive=True))
         if 'MAW_Codex' not in p]
TARGET = 135
TRIGGERS = ('the breach', 'the counter', 'the wall', 'the contact', 'the completion', 'the refusal')
CELL = re.compile(r'^\|\s*\*\*SE Effect\*\*\s*\|(.+?)\s*\|\s*$', re.M)
OPEN = re.compile(r'^\*\*On (the breach|the counter|the wall|the contact|the completion|the refusal)\*\* — (.+)$')
TYPE = re.compile(r'\*\*Entity Type\*\*\s*\|\s*([^|\n]+)')
WORKTYPE = re.compile(r'\b(Viderehan|Ferrehan|Flerehan|Pugnahan)\b')
STOP = set('''the a an and or of to in on for with is are was were be it its this that their they them not
no as at by from into out over under than then so if but what which who whom when where why how all any
each more most some such only own same very can will just do does did has have had also one two three
every anybody nobody somebody there here still never always once first last new old'''.split())
RATCHET_SET = '2026-11-05'


def field(t, label):
    m = re.search(r'^\|\s*\*\*' + label + r'\*\*\s*\|([^|\n]*)', t, re.M)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''


def borrowed(body, text):
    """The share of the effect's content words the *rest of* the dossier does not contain.

    The row itself is struck out first: an effect that only ever appears inside its own cell
    has not been drawn from the record, it has been written at it.
    """
    words = [w.lower().strip(".,;:—–-'()[]") for w in body.split()]
    words = [w for w in words if len(w) >= 4 and w.isalpha() and w not in STOP]
    if not words:
        return 0.0
    rest = CELL.sub('', text)
    low = rest.lower()
    missing = [w for w in words if w[:5] not in low]
    return len(missing) / float(len(words))


def problems(text):
    """Failures on one dossier. Pure function; the tests drive it directly."""
    m = CELL.search(text)
    if not m:
        return []
    cell = m.group(1).strip()
    bad = []
    o = OPEN.match(cell)
    if not o:
        return ['the cell does not open **On <trigger>** — ']
    trigger, body = o.group(1), o.group(2).strip().rstrip('.')

    if len(body.split()) < 10:
        bad.append('the effect is %d words — a law, not a label' % len(body.split()))
    if re.search(r'\d+\s*%|cooldown|per cent of the time|\bd\d+\b|dice|\broll(?:s|ed)? (?:a|an|the) (?:d\d+|die)\b', body, re.I):
        bad.append('the effect reads as a percentage, a cooldown or a dice roll')
    if borrowed(body, text) > 0.10:
        bad.append('more than a tenth of the effect is vocabulary from outside this dossier')
    if WORKTYPE.search(body) and 'Subject' not in field(text, 'Entity Type'):
        bad.append('a Work Type name in a relic effect (R-40)')
    et = field(text, 'Entity Type')
    if trigger == 'the breach' and not re.search(r'\bcan breach|possession', et, re.I):
        bad.append('**On the breach** on a holding its Entity Type does not let breach')
    return bad


def measure():
    rows, fail = [], []
    for path in PATHS:
        text = io.open(path, encoding='utf-8').read()
        m = CELL.search(text)
        if not m:
            continue
        cell = m.group(1).strip()
        o = OPEN.match(cell)
        rows.append((path, o.group(1) if o else '?'))
        bad = problems(text)
        if bad:
            fail.append((path, bad))
    seen = collections.Counter()
    for path, _t in rows:
        text = io.open(path, encoding='utf-8').read()
        o = OPEN.match(CELL.search(text).group(1).strip())
        if o:
            seen[o.group(2).strip().rstrip('.')] += 1
    for body, n in seen.items():
        if n > 1:
            fail.append((body[:60], ['%d dossiers carry this effect verbatim' % n]))
    return rows, fail


def main(argv):
    rows, fail = measure()
    triggers = collections.Counter(t for _p, t in rows)
    if '--stats' in argv:
        print('dossiers %d · with an SE Effect %d (%.0f%% — target %d)'
              % (len(PATHS), len(rows), 100.0 * len(rows) / len(PATHS), TARGET))
        for k, v in triggers.most_common():
            print('  %-16s %3d' % (k, v))
        return 0
    if '-v' in argv:
        for path, t in rows:
            print('%-16s %s' % (t, path.split('/')[-1][:70]))
    for path, bad in fail:
        print('%s  %s' % (str(path).split('/')[-1][:60], '; '.join(bad)[:150]))
    if len(rows) != TARGET:
        print('the archive carries %d SE Effects; R-50 fixes %d' % (len(rows), TARGET))
    if fail or len(rows) != TARGET:
        print('SE Effect failures: %d' % (len(fail) + (len(rows) != TARGET)))
        print('RESULT: FAIL')
        return 1
    print('SE Effect %d of %d dossiers (%.0f%%)  ratchet %s'
          % (len(rows), len(PATHS), 100.0 * len(rows) / len(PATHS), RATCHET_SET))
    print('  ' + ' · '.join('%s %d' % (k, v) for k, v in triggers.most_common()))
    print('se-effect failures: 0')
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
