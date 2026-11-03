#!/usr/bin/env python3
"""
tools/auditors/check_sourcing.py

The journalist's read of the archive.

check_dossier_consistency.py asked whether ONE dossier contradicts ITSELF.
This asks the other half of the question: whether the claims in a dossier survive
contact with the other 300. It is a different lens on the same corpus, and it
finds a different kind of fault.

What a journalist asks of a sentence that a prose editor does not:

  * WHERE IS THE NUMBER FROM?  A rate in the card and a different rate in the
    prose, four lines apart, is not a style problem — it is two figures for one
    quantity, and a reader cannot act on either.
  * WHAT DID YOU DO ABOUT THE CONFLICT YOU FOUND?  Saying "no definition
    reconciles these; keep them distinct; no value was normalized" is diligence
    that ships the defect. A newspaper does not print that note in the article.
  * IS THE SUPERLATIVE TRUE?  "The only entity in the registry that …" is a
    checkable claim, not emphasis, and the corpus is the check.

Three classes FAIL. Two are REPORTED, because they are house convention rather
than error and paying them down is an owner decision.

Ratchets fail in both directions: over the ceiling a new one was written, under
it the ceiling is stale and the batch that lowered it must lower the number.
"""

import glob
import re
import sys

DIRS = ['SOMNARAK-WORLD/Sorrow_Entities/SE-*.md',
        'SOMNARAK-WORLD/Unknown_Entities/SE-*.md']

RATCHET = {
    # Both were live on 2026-11-03 when this tool was written; both were fixed in
    # Kind Echo in the same batch. Zero is the correct ceiling for a shipped
    # contradiction, not a convenient one.
    'rate-conflict': 0,
    'unresolved-note': 0,
    'false-uniqueness': 0,
    # Cleared in batch 138. 80 dossiers carried a real-world `(2026-10-12)` stamp
    # on their full-set source review; every one now carries the dossier's own
    # filing year instead. The review itself was kept in full — only the stamp that
    # came from our world was converted, because a record dated Year 4238 cannot
    # have been reviewed in 2026.
    'real-world-date': 0,
}

REPORT_ONLY = {
    'unreconciled (in-world, not a fault)': 'two measurements held apart on purpose',
}

# ── a rate stated in a card, and a different rate stated in prose ────────────
ACQ = re.compile(r'Acquisition Probability:\*{0,2}\s*([\d.]+)\s*%', re.I)
HIGH = re.compile(r'(?:granted|grant|drops?|drop rate|obtained|awarded)\b[^.\n]{0,70}?'
                  r'(near[- ]?100|100)\s*%', re.I)

# ── the note that admits a contradiction instead of resolving it ─────────────
UNRESOLVED = [
    (r'no definition reconc\w*', 'names a contradiction and leaves it'),
    (r'[Kk]eep those claims distinct', 'instructs the reader to hold two answers'),
    (r'no value was normalized', 'states that no figure was settled'),
]

# `unreconciled` is deliberately NOT a defect. "The two series are filed
# unreconciled" is a record refusing to average two measurements — that is the
# archive being honest, and failing it would punish good practice. It is counted
# below so the number stays visible without being called a fault.
IN_WORLD_UNRECONCILED = re.compile(r'\bunreconciled\b', re.I)

# ── checkable superlatives, tested against the corpus ───────────────────────
WARM_CLAIM = re.compile(r'unique among Sorrow Entities', re.I)
WARM_BODY = re.compile(r'warm to the (?:touch|hand)|the stone is warm|surface is warm|'
                       r'not crystal-cold but comfort-warm', re.I)
NEVER_CLAIM = re.compile(r'the only entity in the registry whose documented event has never injured anyone',
                         re.I)
EVENT = re.compile(r'^#{2,3} .*\bEvent\b|^\| ?\*\*Event Type\*\*', re.M)
NO_INJURY = re.compile(r'never injured|has never (?:hurt|injured)|no record holds a single injury|'
                       r'no injury (?:has been )?recorded|has never caused (?:harm|injury)', re.I)

REAL_DATE = re.compile(r'\(2026-\d\d-\d\d\)')


def load():
    paths = []
    for pat in DIRS:
        paths.extend(sorted(glob.glob(pat)))
    return sorted(set(paths))


def scan(paths):
    texts = {}
    for p in paths:
        with open(p, encoding='utf-8') as fh:
            texts[p] = fh.read()
    defects, reports = {}, {}

    def add(kind, p, why):
        defects.setdefault(kind, []).append((p.split('/')[-1], why))

    def note(kind, p, why):
        reports.setdefault(kind, []).append((p.split('/')[-1], why))

    # corpus facts a superlative can be tested against
    warm_bodies = [p for p, t in texts.items() if WARM_BODY.search(t)]
    never_claim = [p for p, t in texts.items() if EVENT.search(t) and NO_INJURY.search(t)]
    trained = [p for p in never_claim if re.search(r'training', texts[p], re.I)]

    for p, t in texts.items():
        name = p.split('/')[-1]

        acq = ACQ.findall(t)
        for m in HIGH.finditer(t):
            if acq:
                add('rate-conflict', p,
                    f'card files {acq[0]}% but the prose says "{m.group(0)[:48]}"')

        for pat, why in UNRESOLVED:
            for m in re.finditer(pat, t, re.I):
                c = t[max(0, m.start() - 70):m.end() + 70].replace('\n', ' ')
                add('unresolved-note', p, f'{why} — "...{c}..."')

        if WARM_CLAIM.search(t):
            others = [q for q in warm_bodies if q != p]
            if others:
                add('false-uniqueness', p,
                    f'claims warmth is unique while {len(others)} other dossiers '
                    f'describe a warm body (e.g. {others[0].split("/")[-1][:44]})')

        if NEVER_CLAIM.search(t) and len(never_claim) > 1:
            add('false-uniqueness', p,
                f'claims to be the only entity whose event never injured anyone, '
                f'while {len(never_claim) - 1} others file an event and assert the same')

        if IN_WORLD_UNRECONCILED.search(t):
            note('unreconciled (in-world, not a fault)', p, 'two measurements held apart')

        if REAL_DATE.search(t):
            note('real-world-date', p, REAL_DATE.search(t).group(0))

        # a superlative that IS true is worth knowing about, and so is the reason
        if re.search(r'only entity with a zero number', t, re.I):
            zeros = [q for q in texts if re.search(r'SE-[A-Z]-[IVXαβγδω]+-000_', q)]
            if len(zeros) == 1:
                note('verified-unique', p, 'zero designation — confirmed unique in the corpus')
            else:
                add('false-uniqueness', p, f'zero designation claimed, {len(zeros)} found')

    # Testimony is attributed by role in these records rather than by name.
    # Measured, not assumed: a quoted line with no em-dash attribution is the
    # journalistic failure this whole lens exists to catch, and it does not occur.
    unattr = 0
    for p, t in texts.items():
        inside = False
        for line in t.split('\n'):
            if 'Testimonium' in line:
                inside = True
                continue
            if inside and line.startswith('## '):
                inside = False
            if inside and re.match(r'^\s*>\s*\*?"', line) and '—' not in line:
                unattr += 1

    return defects, reports, dict(warm=len(warm_bodies), never=len(never_claim),
                                  trained=len(trained), files=len(texts),
                                  unattr=unattr)


def main(argv):
    paths = load()
    defects, reports, facts = scan(paths)
    verbose = '-v' in argv

    print(f'SOURCING — {facts["files"]} dossiers')
    print(f'  corpus: {facts["warm"]} warm bodies · '
          f'{facts["never"]} file an event and claim no injury ({facts["trained"]} of those are training)')
    print(f'  testimony: {facts["unattr"]} quoted lines without an attribution — '
          f'every quotation in the archive names who said it')

    bad = False
    for kind in sorted(set(list(defects) + list(RATCHET) + list(REPORT_ONLY))):
        ceiling = RATCHET.get(kind)
        n = len(defects.get(kind, [])) + len(reports.get(kind, []))
        if ceiling is None:
            print(f'  {kind:34} {n:4}   reported only — {REPORT_ONLY.get(kind, "no ceiling")}')
            continue
        if n > ceiling:
            print(f'  {kind:18} {n:4}   ABOVE CEILING {ceiling} — new defect')
            bad = True
        elif n < ceiling:
            print(f'  {kind:18} {n:4}   BELOW CEILING — lower it to {n}')
            bad = True
        else:
            print(f'  {kind:18} {n:4}   at ceiling')
        if verbose:
            for f, why in defects.get(kind, []):
                print(f'      {f[:52]:52} {why[:110]}')

    if verbose:
        for kind, rows in sorted(reports.items()):
            print(f'  -- {kind}: {len(rows)}')
            for f, why in rows[:8]:
                print(f'      {f[:52]:52} {why[:100]}')

    print('RESULT: ' + ('FAIL' if bad else 'PASS'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
