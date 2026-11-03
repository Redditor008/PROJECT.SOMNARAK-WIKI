#!/usr/bin/env python3
"""reading_ledger.py — who has actually read what, in a form that can be checked.

The owner ordered a review of **every** SE file. Twenty-two auditors and four
cross-boundary measurements can say a great deal about 301 dossiers, but none of
them can say a page was *read*, and after batch 151 that distinction stopped
being academic: the only two defects on the page in `SE-C-IVδ-909` were created by
the repair two batches earlier, in a file every check had passed. Reading is not
a nicer way to run the checks. It finds things the checks cannot represent.

The ledger therefore carries a state per dossier, and the states are ordered by
how much evidence stands behind them:

    read-whole    read end to end; the defects found were fixed in a named batch
    read-back     a repair was made to it and the surrounding section was read
                  afterwards for coherence — not the whole file
    machine       passed the auditors; no person has read it this session

Nothing is marked read-whole on the strength of having opened it. Each entry
names the batch and what was found, so the claim can be audited against that
batch's script and diff. A ledger that records intentions is a wish list; this
one records evidence.

    python3 tools/reading_ledger.py            # write the MD and CSV
    python3 tools/reading_ledger.py --summary  # print the counts, write nothing
"""
import csv
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_MD = os.path.join(ROOT, 'REFERENCE_SOMNARAK_WIKI', 'AUDITS',
                      'SE_READING_LEDGER_2026-11-03.md')
OUT_CSV = os.path.join(ROOT, 'REFERENCE_SOMNARAK_WIKI', 'AUDITS',
                       'SE_READING_LEDGER_2026-11-03.csv')

DOSSIERS = ('SOMNARAK-WORLD/Sorrow_Entities/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/*.md')
SKIP = {'README.md'}

# stem-prefix -> (state, evidence). Only entries that survive an inspection of
# the batch's own script and diff belong here.
EVIDENCE = {
    'SE-C-IVδ-909_Labyrinth': (
        'read-whole', '151 — a lost sentence start and a bullet restating the one '
        'beneath it, both written by the 150 repair; both fixed'),
    'SE-C-IIβ-901_Duri': (
        'read-whole', '152 — the replacement clock said nineteen years where the '
        'file says forty-eight, twice; fixed'),
    'SE-C-IIIγ-904_Thinking_Engine': (
        'read-whole', '153 — the 150 repair had turned a fabricated 94-of-211 into '
        '"45 per cent of cycles"; replaced with the 640 staff the catalogue names'),
    'SE-C-IIIγ-033_The_Guarding_Bird': (
        'read-back', '152 — clock audit: the 150/151 repairs said nine years '
        'where the post served eleven; fixed twice'),
    'SE-C-IVγ-205_Hollow_Tree': (
        'read-back', '152 — clock audit: two repairs dated the sitting record '
        'nineteen years against 31 relocations in nine; span removed'),
}

REPAIR_SCRIPTS = ('tools/fix_slot_templates.py', 'tools/fix_series_counts.py',
                  'tools/fix_sentence_starts.py')


def repair_batches():
    """{stem: [batch numbers]} from the repair scripts, which are the record."""
    batches = {}
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    try:
        import fix_slot_templates as b149
        import fix_series_counts as b150
        import fix_sentence_starts as b151
    except Exception:                                    # pragma: no cover
        return batches
    for stem in b149.NEW:
        batches.setdefault(stem, set()).add(149)
    for stem in b150.EDITS:
        batches.setdefault(stem, set()).add(150)
    for stem, _, _ in b151.EDITS:
        batches.setdefault(stem, set()).add(151)
    return batches


def dossiers():
    found = []
    for pattern in DOSSIERS:
        found.extend(glob.glob(os.path.join(ROOT, pattern), recursive=True))
    return sorted(p for p in set(found) if os.path.basename(p) not in SKIP
                  and 'Dramaturgy' not in p)


def state_for(stem):
    for prefix, entry in EVIDENCE.items():
        if stem.startswith(prefix):
            return entry
    return ('machine', 'passed the auditors; not read by a person this session')


def rows():
    batches = repair_batches()
    out = []
    for path in dossiers():
        with io.open(path, encoding='utf-8') as handle:
            text = handle.read()
        code = re.search(r'`([A-Z]-[IV]+[^\s`]*-\d{3})', text)
        title = re.match(r'# (.+?)\s+—', text)
        stem = os.path.basename(path)[:-3]
        state, note = state_for(stem)
        touched = set()
        for prefix, found in batches.items():
            if stem.startswith(prefix):
                touched |= found
        touched = sorted(touched)
        out.append({
            'code': code.group(1) if code else '?',
            'title': title.group(1).strip() if title else stem,
            'words': len(re.findall(r'\S+', text)),
            'sections': len(re.findall(r'^## ', text, re.M)),
            'repairs': ','.join(str(b) for b in touched) or '—',
            'state': state,
            'note': note,
            'path': os.path.relpath(path, ROOT),
        })
    order = {'read-whole': 0, 'read-back': 1, 'machine': 2}
    out.sort(key=lambda r: (order[r['state']], -len(r['repairs'].replace('—', '').split(',')),
                           -r['words']))
    return out


def write(entries):
    counts = {'read-whole': 0, 'read-back': 0, 'machine': 0}
    for entry in entries:
        counts[entry['state']] += 1
    total_words = sum(e['words'] for e in entries)
    read_words = sum(e['words'] for e in entries
                     if e['state'] in ('read-whole', 'read-back'))
    lines = [
        '# SE READING LEDGER — 2026-11-03',
        '',
        'Every one of the **%d** dossiers, with the state of its coverage. '
        'Regenerate with `python3 tools/reading_ledger.py`.' % len(entries),
        '',
        '| state | dossiers | words | what it means |',
        '|---|---|---|---|',
        '| **read-whole** | %d | %s | read end to end; what was found was fixed in a named batch |'
        % (counts['read-whole'], f"{sum(e['words'] for e in entries if e['state'] == 'read-whole'):,}"),
        '| **read-back** | %d | %s | repaired, and the surrounding section read afterwards |'
        % (counts['read-back'], f"{sum(e['words'] for e in entries if e['state'] == 'read-back'):,}"),
        '| **machine** | %d | %s | passed every auditor; no person has read it |'
        % (counts['machine'], f"{sum(e['words'] for e in entries if e['state'] == 'machine'):,}"),
        '',
        '**%s of %s words (%0.1f%%) have been read by a person.** That is the honest '
        'figure, and the point of writing it down is that the other 97 per cent is '
        'not a claim of quality — it is a claim of coverage, which is a different '
        'thing.' % (f'{read_words:,}', f'{total_words:,}', 100.0 * read_words / total_words),
        '',
        '## The reading order',
        '',
        'Ranked by exposure: a dossier repaired by three different batches is the one '
        'most likely to carry a defect created by a repair, which is the class batch '
        '151 proved passes every check.',
        '',
        '| # | code | dossier | words | repairs | state | evidence |',
        '|---|---|---|---|---|---|---|',
    ]
    for n, entry in enumerate(entries, 1):
        lines.append('| %d | `%s` | %s | %s | %s | %s | %s |' % (
            n, entry['code'], entry['title'], f"{entry['words']:,}",
            entry['repairs'], entry['state'], entry['note']))
    lines += [
        '',
        '## How to change a row',
        '',
        'Read the file. Fix what is wrong in it. Add the batch number and what was '
        'found to `EVIDENCE` in `tools/reading_ledger.py`, then regenerate. A row '
        'moves when a diff exists, not when an intention does.',
        '',
    ]
    with io.open(OUT_MD, 'w', encoding='utf-8') as handle:
        handle.write('\n'.join(lines))
    with io.open(OUT_CSV, 'w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(entries[0]), extrasaction='ignore')
        writer.writeheader()
        writer.writerows(entries)
    return counts


def main(argv):
    entries = rows()
    counts = write(entries) if '--summary' not in argv else None
    if counts is None:
        counts = {}
        for entry in entries:
            counts[entry['state']] = counts.get(entry['state'], 0) + 1
        print('no files written (--summary)')
    else:
        print('wrote', os.path.relpath(OUT_MD, ROOT))
        print('wrote', os.path.relpath(OUT_CSV, ROOT))
    print('dossiers %d · read-whole %d · read-back %d · machine %d'
          % (len(entries), counts.get('read-whole', 0), counts.get('read-back', 0),
             counts.get('machine', 0)))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
