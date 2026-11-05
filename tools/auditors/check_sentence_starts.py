#!/usr/bin/env python3
"""check_sentence_starts.py — two ways a field can read as a fragment.

Both found by reading a dossier whole, in the batch-151 review, after a repair
had already been applied to it. Neither is a factual error and no fact-checker
can see either: the sentence is true, it just does not start.

**Family 1 — a sentence that begins lowercase.** Thirteen in the corpus, two of
them written by the batch-150 repair itself:

    ...the room count matching. the descent record; the count has matched in
    nineteen descents of every twenty and the nine that did not are the nine pulls.

The cause is a replacement made against a fragment: the old text ended the
sentence and the new text continued one. Read whole, it is visible in a glance;
searched for by number, it is invisible, because every figure in it is correct.

**Family 2 — a field answered by another field's label.** Five in four dossiers:

    | **Position / movement** | Physical Form: A market stall that appears overnight... |

The label is not a value. The field has been filled with the name of the field
above it, which is the same failure as `check_boilerplate`'s activation-echo —
a cell that looks filled and answers nothing — but written in the detailed
appearance table instead of the field-parameters block.

A third family was considered and rejected: a lone `vs.` inside a sentence
("gold vs. violet") trips a naive lowercase test and is correct English. The
allowlist below is exactly the abbreviations that occur in this corpus, and it
is short on purpose — every entry has to be justified by a use on the record.

    python3 tools/auditors/check_sentence_starts.py        # ratchet check
    python3 tools/auditors/check_sentence_starts.py -v     # per-instance listing
    python3 tools/auditors/check_sentence_starts.py --files A.md B.md
"""
import glob
import io
import os
import re
import sys

DOSSIERS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/*.md')

# Abbreviations that legitimately precede a lowercase word after a full stop.
# `vs` is used in SE-C-IIγ-071c (\"gold vs. violet\"); `etc` and `no` are the only
# others on the record. Anything else must be a real sentence.
ALLOWED = {'vs', 'etc', 'no', 'al', 'cf'}

LOWERCASE = re.compile(r'(?<![A-Z.])\.\s+([a-z][a-z\-]{2,})')

# Field labels that must never open a different field's value.
LABELS = ('Physical Form', 'Movement', 'Location', 'Entity Type', 'Element',
          'Manifestation', 'Coherence', 'Potency', 'Designation', 'Primary Form',
          'Primary marker', 'Identification Profile', 'Appearance')
# The colon sits inside the bold in a bullet (`**Position / movement:** value`)
# and outside it in a table row (`| **Position / movement** | value |`). Both.
ROW = re.compile(r'^\s*(?:[-*]\s*\*\*|\|\s*\*\*)(?P<label>[^*|]{2,40}?)\s*:?\*\*\s*[:|]?\s*')
ECHO = re.compile(r'^\s*(?:\*\*)?(?P<value>' + '|'.join(sorted(LABELS, key=len, reverse=True))
                  + r')\s*:', re.I)

RATCHET = {'lowercase-start': 0, 'label-echo': 0}
RATCHET_SET = '2026-11-03'


def dossier_files():
    found = []
    for pattern in DOSSIERS:
        found.extend(glob.glob(pattern, recursive=True))
    return sorted(set(found))


def scan_text(text):
    """[(family, line_number, excerpt)] for one dossier."""
    out = []
    for number, line in enumerate(text.split('\n'), 1):
        if line.strip().startswith('```'):
            continue
        for match in LOWERCASE.finditer(line):
            # The abbreviation is the word *before* the full stop, not after it:
            # "gold vs. violet" trips a naive test and is correct English.
            before = re.search(r'([A-Za-z]+)\.$', line[:match.start() + 1])
            if before and before.group(1).lower() in ALLOWED:
                continue
            if match.group(1).lower() in ALLOWED:
                continue
            out.append(('lowercase-start', number, line.strip()[:140]))
        row = ROW.match(line)
        if row:
            value = line[row.end():]
            echo = ECHO.match(value)
            if echo and echo.group('value').lower() != row.group('label').strip().lower():
                out.append(('label-echo', number, line.strip()[:140]))
    return out


def measure(paths=None):
    files = paths if paths is not None else dossier_files()
    hits = []
    for path in files:
        try:
            with io.open(path, encoding='utf-8') as handle:
                text = handle.read()
        except OSError:
            continue
        for family, number, excerpt in scan_text(text):
            hits.append((family, path, number, excerpt))
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
            for family, number, excerpt in found:
                print(f'  DIRTY {leaf}:{number} [{family}] {excerpt}')
        else:
            print(f'  clean {leaf}')
    print(f'RESULT: {"FAIL" if bad else "PASS"} — {bad} of {len(paths)} files carry a fragment')
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

    failed = 0
    total = 0
    print(f'check_sentence_starts — {len(files)} dossiers, ceilings set {RATCHET_SET}')
    for family, ceiling in RATCHET.items():
        found = [h for h in hits if h[0] == family]
        total += len(found)
        if len(found) > ceiling:
            failed += 1
        elif len(found) < ceiling:
            failed += 1
            print(f'  {family:18s} {len(found):3d}  BELOW CEILING {ceiling} — lower it')
            continue
        print(f'  {family:18s} {len(found):3d}  ceiling {ceiling}')
        if verbose:
            for _, path, number, excerpt in found:
                print(f'      {os.path.basename(path)[:46]}:{number}  {excerpt[:110]}')
    print(f'  {"TOTAL":18s} {total:3d}  fragments')
    print(f'RESULT: {"FAIL" if failed else "PASS"} — {failed} families off ratchet, {total} fragments')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
