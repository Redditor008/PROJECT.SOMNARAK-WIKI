#!/usr/bin/env python3
"""check_event_claims.py — a dossier that files a containment event may not deny having one.

**The defect this exists for.** `SE-C-Iα-000 Kind Echo` was given an updated
Containment Event Behavior table: the entity answers a worker's kindness with the
same kindness and does not know when to stop, draining Composure by repetition
until the worker cannot tell their own voice from the reply. The rest of the
dossier was never brought across. Its SECC line still described *"waves of cold
grief"*, its observation ladder said *"the entity does not activate"*, its
containment notice said an event was *"practically impossible"*, its threat
assessment said *"no direct danger"*, and its trivia said *"zero event risk"* —
five places in one file, any of which a reader could have opened first.

No linter caught it. Every one of those sentences is well-formed Markdown in a
file with all its sections, its tables closed, its links resolving and its
finishedness at 100 %. It was caught by a reader using the dossier for another
project, who noticed the file told two stories about the same event.

**The rule, stated so it can be tested.** A dossier that files a containment
event — an `Event Behavior` section carrying an `Event Type` row — has a
procedure. It may describe that procedure as rare, quiet, non-breaching or
harmless. It may not say the entity does not activate, that the event is
impossible, or that the file carries no risk; those are claims about the same
fact in the opposite direction, and a reader has no way to know which one the
Archive means.

**What this does not forbid.** An entity with no containment event at all may
say so as plainly as it likes — `no activation trigger known`, `does not breach`
and `no counter` are ordinary filings on the 200-plus dossiers without an event
table, and none of them is touched here. *Special activation* is a different
field from *containment event* (`R-06`: the counter is the counter), so a file
may carry a documented event and still record that it has no counter. The scan
only asks a file to be consistent about the one thing it has already filed.

    python3 tools/auditors/check_event_claims.py            # whole archive
    python3 tools/auditors/check_event_claims.py -v         # list every dossier with an event table
    python3 tools/auditors/check_event_claims.py --files A.md
"""
import glob
import io
import re
import sys

DOSSIERS = ['SOMNARAK-WORLD/Sorrow_Entities/**/*.md',
            'SOMNARAK-WORLD/Unknown_Entities/**/*.md']

# Phrases that assert the absence of the event the file has already filed.
# Deliberately narrow: each of these denies the event itself, not the counter.
FORBIDDEN = [
    'zero event risk',
    'no event risk',
    'does not activate',
    'never activates',
    'event is impossible',
    'event is practically impossible',
    'events are impossible',
    'risk-free',
]
PATTERN = re.compile('|'.join(re.escape(p) for p in FORBIDDEN), re.I)

EVENT_HEADING = re.compile(r'^#{2,3}\s+.*Event Behavior\s*$', re.M | re.I)


def has_event_table(text):
    """A filed event is a heading for it plus the Event Type row that starts it."""
    return bool(EVENT_HEADING.search(text)) and '**Event Type**' in text


def offending(text):
    return sorted({m.group(0).lower() for m in PATTERN.finditer(text)})


def scan(paths):
    filed = bad = 0
    problems = []
    for path in paths:
        try:
            text = io.open(path, encoding='utf-8').read()
        except OSError:
            continue
        if not has_event_table(text):
            continue
        filed += 1
        hits = offending(text)
        if hits:
            bad += 1
            problems.append((path, hits))
    return filed, bad, problems


def main(argv):
    verbose = '-v' in argv or '--verbose' in argv
    if '--files' in argv:
        paths = argv[argv.index('--files') + 1:]
        if not paths:
            print('RESULT: FAIL — --files needs at least one path')
            return 1
    else:
        paths = []
        for pattern in DOSSIERS:
            paths.extend(sorted(glob.glob(pattern, recursive=True)))
        paths = sorted(set(paths))

    filed, bad, problems = scan(paths)
    print(f'EVENT CLAIMS — {len(paths)} dossiers scanned · {filed} file a containment event')
    if verbose:
        for path in paths:
            text = io.open(path, encoding='utf-8').read()
            if has_event_table(text):
                print(f'    filed: {path.split("/")[-1]}')
    for path, hits in problems:
        print(f'  CONTRADICTION {path.split("/")[-1]}: files an event and also says '
              f'{", ".join(hits)}')
    print(f'  dossiers filing an event that deny it: {bad}')
    print('RESULT: ' + ('FAIL' if bad else 'PASS'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
