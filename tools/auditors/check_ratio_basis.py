#!/usr/bin/env python3
"""check_ratio_basis.py — a proportion of a series must show its two counts.

Batch 135 set the standard for this archive: every claim should name **who**,
**when** and **how it was measured**. A proportion is the one claim where the
third of those is arithmetic rather than prose — *"78 per cent of the readings"*
means nothing a reader can check unless the readings' total and the matching
count are on the same page.

This guard exists because batch 150 broke that rule while fixing a different
one. Replacing the pooled numerals (188 cycles in twelve dossiers, 211 in five)
with the dossiers' own clocks left the ratios that had been computed against the
pooled denominators — and then converted them into percentages, which looks like
rounding rather than what it was:

    147 of 188 cycles          ->  78 per cent of the readings
    94 of 188 declined         ->  half have declined to
    94 of 211 cycles           ->  45 per cent of cycles

**Both halves of every one of those ratios were fabricated.** The percentage
carried the fabrication through a filter that reads like precision. Found in
batch 153 by reading `SE-C-IIIγ-904` whole; eleven sentences in six dossiers.

The rule now enforced: a proportion of an **observation series** is legitimate
only when the dossier also states the two counts it came from, so a reader can
do the division. Percentages about mechanics — *"resistance 30 per cent"*,
*"threshold 65 per cent"* — are not proportions of a series and are not touched.
Measured: 182 percentages in the corpus have no count pair beside them, and
almost all of them are mechanics. Restricting the pattern to series nouns is what
makes a ceiling of zero possible without a false positive.

    python3 tools/auditors/check_ratio_basis.py        # ratchet check
    python3 tools/auditors/check_ratio_basis.py -v     # per-instance listing
    python3 tools/auditors/check_ratio_basis.py --files A.md B.md
"""
import glob
import io
import os
import re
import sys

DOSSIERS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/*.md')

SERIES = (r'(?:readings|cycles|descents|intervals|observations|sessions|watches|'
          r'arrivals|entries|shifts|incidents|occurrences|channels|viewings|'
          r'surveys|pulls|passes|pairings|namings|sittings|circuits)')

# "78 per cent of the readings" / "45 per cent of cycles"
PCT = re.compile(r'\b(\d{1,3}(?:\.\d+)?)\s+(?:per cent|per-cent|percent)\s+of\s+'
                 r'(?:the\s+|all\s+|these\s+|those\s+|recorded\s+)?' + SERIES + r'\b',
                 re.I)
# Fractions are written in words as often as in digits — "nineteen of every
# twenty" is how the batch-150 repair wrote it, and a digit-only pattern walked
# straight past it. Both forms, both orders.
WORDS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
         'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
         'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
         'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
         'twenty-five': 25, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60}
_N = r'(\d{1,4}|' + '|'.join(sorted(WORDS, key=len, reverse=True)) + r')'
FRAC_A = re.compile(r'\b' + _N + r'\s+of\s+every\s+' + _N + r'\b', re.I)
FRAC_B = re.compile(r'\b' + _N + r'\s+' + SERIES + r'\s+of\s+(?:every\s+|the\s+|those\s+)?'
                    + _N + r'\b', re.I)


def _value(token):
    token = token.lower()
    return WORDS[token] if token in WORDS else int(token)
# "147 of 188" — a stated pair anywhere in the same dossier.
PAIR = re.compile(r'\b(\d{1,4})\s+of\s+(\d{1,4})\b')

RATCHET = 0
RATCHET_SET = '2026-11-03'


def dossier_files():
    found = []
    for pattern in DOSSIERS:
        found.extend(glob.glob(pattern, recursive=True))
    return sorted(p for p in set(found) if 'Dramaturgy' not in p
                  and not p.endswith('README.md'))


def scan_text(text):
    """[(what, excerpt)] for every proportion of a series without a stated basis."""
    pairs = set()
    for a, b in PAIR.findall(text):
        a, b = int(a), int(b)
        if b and a <= b:
            pairs.add((a, b))
    shares = {round(100.0 * a / b, 1) for a, b in pairs}

    out = []
    for match in PCT.finditer(text):
        value = float(match.group(1))
        if any(abs(share - value) <= 1.0 for share in shares):
            continue
        out.append((match.group(0), match.start()))
    for pattern in (FRAC_A, FRAC_B):
        for match in pattern.finditer(text):
            a, b = _value(match.group(1)), _value(match.group(2))
            if not b:
                continue
            if (a, b) in pairs or any(abs(share - 100.0 * a / b) <= 1.0 for share in shares):
                continue
            out.append((match.group(0), match.start()))
    return [(what, ' '.join(text[max(0, at - 70):at + len(what) + 30].split()))
            for what, at in sorted(out, key=lambda item: item[1])]


def measure(paths=None):
    files = paths if paths is not None else dossier_files()
    hits = []
    for path in files:
        try:
            with io.open(path, encoding='utf-8') as handle:
                text = handle.read()
        except OSError:
            continue
        for what, excerpt in scan_text(text):
            hits.append((path, what, excerpt))
    return files, hits


def audit_files(paths):
    bad = 0
    for path in paths:
        try:
            with io.open(path, encoding='utf-8') as handle:
                found = scan_text(handle.read())
        except OSError:
            print(f'  MISSING {path}')
            bad += 1
            continue
        leaf = path.split('/')[-1]
        if found:
            bad += 1
            for what, excerpt in found:
                print(f'  DIRTY {leaf}: [{what}] {excerpt[:110]}')
        else:
            print(f'  clean {leaf}')
    print(f'RESULT: {"FAIL" if bad else "PASS"} — {bad} of {len(paths)} files carry an unsupported proportion')
    return 1 if bad else 0


def main(argv):
    if '--files' in argv:
        named = argv[argv.index('--files') + 1:]
        if not named:
            print('RESULT: FAIL — --files needs at least one path')
            return 1
        return audit_files(named)

    verbose = '-v' in argv or '--verbose' in argv
    files, hits = measure()
    if not files:
        print('RESULT: FAIL — no dossiers matched; the glob is wrong, not the corpus')
        return 1

    print(f'check_ratio_basis — {len(files)} dossiers, ceiling {RATCHET} set {RATCHET_SET}')
    if verbose:
        for path, what, excerpt in hits:
            print(f'      {os.path.basename(path)[:44]} [{what}] {excerpt[:110]}')
    print(f'  proportion-without-basis  {len(hits)}   ceiling {RATCHET}')
    if len(hits) > RATCHET:
        print(f'RESULT: FAIL — {len(hits)} ABOVE CEILING {RATCHET}')
        return 1
    if len(hits) < RATCHET:
        print(f'RESULT: FAIL — BELOW CEILING, lower it to {len(hits)}')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
