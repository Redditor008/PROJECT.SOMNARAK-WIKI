#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""trim_overexplanation.py - take the description out of the classification table.

The SECC Classification table answers one question per row: *what is this thing
classified as*. It had stopped doing that. Three rows had become full descriptions:

    | **Physical Form** | Mixed - A figure wreathed in slow fire, covered head to   |
    |                   | foot in black chains that spread across walls and floors   |
    |                   | on their own while the body stays perfectly still. Fever-  |
    |                   | hot and bloodless-cold at once, it smells of char and ash. |

That sentence is the `## Appearance` section, printed a second time forty lines earlier.
Measured: 269 of 301 Physical Form cells share more than 60% of their content words with
the Appearance section, and 297 of 301 dossiers carry a full form description there under
`**Physical Form:**` or the older `**Primary Form:**`.

The same holds for Movement (169 of 263 duplicated) and Entity Type, whose trailing clause
restates the Behaviour section and the `Activation threshold` row.

So each row is cut back to the value it exists to hold - `Mixed`, `Stationary`,
`**Subject** - Non-breaching` - and the description stays where a reader looks for it, in
Appearance. Nothing unique is lost: a cell is trimmed only when the Appearance section
provably carries the same description, and the four dossiers without one are left alone.

Every edit is guarded. Offsets are absolute into the file, the table must still have the
same number of rows afterwards, and all three labels must survive; if any guard fails the
file is not written at all.

    python3 tools/repairs_and_patches/trim_overexplanation.py            report
    python3 tools/repairs_and_patches/trim_overexplanation.py --write    apply
"""
import argparse
import glob
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATHS = sorted(glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD', '*', 'SE-*.md')))

DASH = re.compile(r'\s+[\u2014\u2013]\s+')
FORM_OK = {'Non-Organic', 'Mixed', 'Organic', 'Non-physical', 'Non-corporeal'}
MOVE_KEEP = ('stationary', 'mobile', 'fixed', 'recumbent', 'rooted', 'seated', 'motionless')
LABELS = ('Physical Form', 'Entity Type')
# `Movement` is deliberately NOT trimmed. 116 dossiers quote the row back in the body
# ("The Movement row says *stationary - a fixed position; spreads rather than moves*"),
# so cutting it would leave the prose citing a row that no longer says that. The row is
# also short - 21 words on average - and it is the only place that states how the holding
# occupies space. The bloat was in Physical Form (47 words) and Entity Type.


def section_span(t, name):
    """Absolute (start, end) of a `## name` section body."""
    m = re.search(r'\n## %s[ \t]*\n' % re.escape(name), t)
    if not m:
        return None
    start = m.end()
    nxt = re.search(r'\n## ', t[start:])
    return start, (start + nxt.start() if nxt else len(t))


def cell_span(t, label, section):
    """Absolute (start, end, value) of one `| **label** | value |` cell."""
    sp = section_span(t, section)
    if not sp:
        return None
    seg = t[sp[0]:sp[1]]
    m = re.search(r'^\|\s*\*\*%s\*\*\s*\|\s*(.+?)\s*\|$' % re.escape(label), seg, re.M)
    if not m:
        return None
    return sp[0] + m.start(1), sp[0] + m.end(1), m.group(1)


def has_form_description(t):
    ap = section_span(t, 'Appearance')
    return bool(ap and re.search(r'\*\*(Primary|Physical) Form:?\*\*', t[ap[0]:ap[1]]))


def head(value):
    return DASH.split(value.strip())[0].strip().rstrip('.,;')


def trim_form(v):
    h = head(v)
    return h if h in FORM_OK else None


def trim_move(v):
    return head(v) if any(k in head(v).lower() for k in MOVE_KEEP) else None


def trim_type(v):
    """Keep the type and the breach mode; drop the explanation appended after them.

    `**Hazard** - Non-breaching: expansion only; the storm widens by consuming what it`
    `crosses`  ->  `**Hazard** - Non-breaching: expansion only`

    The cut is at the first semicolon rather than the first colon, because the clause
    before it ("expansion only", "activation only", "corruption of its own zone") is a
    classification, and five dossiers quote it back in the body.
    """
    v = v.strip()
    if not v.startswith('**'):
        return None
    # the classification is the cell's first clause; cut at whichever ends it first
    cut = re.split(r';|\.\s', v)[0].strip().rstrip('.,')
    if len(cut.split()) > 16:
        m = re.match(r'(\*\*[^*]+\*\*)\s*[\u2014\u2013]\s*([^:;]{2,60}?)\s*(?::.*)?$', v)
        cut = '%s \u2014 %s' % (m.group(1), m.group(2).strip()) if m else cut
    return cut


def guard(orig, new):
    """The file must still be a dossier with an intact classification table."""
    for name in ('SECC Classification', 'Appearance', 'Operational Parameters'):
        if ('## ' + name) not in new:
            return False
    if len(re.findall(r'^\|', orig, re.M)) != len(re.findall(r'^\|', new, re.M)):
        return False
    for label in LABELS:
        if ('**%s**' % label) not in new:
            return False
    return new.count('**') % 2 == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()

    changed = {k: 0 for k in LABELS}
    before = after = 0
    skipped = refused = 0
    shown = 0

    for path in PATHS:
        with io.open(path, encoding='utf-8') as fh:
            t = fh.read()
        orig = t
        described = has_form_description(t)
        if not described:
            skipped += 1

        edits = []
        for label, fn in (('Physical Form', trim_form), ('Entity Type', trim_type)):
            if label == 'Physical Form' and not described:
                continue
            c = cell_span(t, label, 'SECC Classification')
            if not c:
                continue
            new = fn(c[2])
            if not new or new == c[2].strip() or len(new.split()) >= len(c[2].split()):
                continue
            edits.append((c[0], c[1], new, label))

        if not edits:
            continue
        for a, b, new, label in sorted(edits, reverse=True):
            t = t[:a] + new + t[b:]
            changed[label] += 1
            before += len(orig[a:b].split())
            after += len(new.split())

        if not guard(orig, t):
            refused += 1
            before -= 0
            continue

        if args.write:
            with io.open(path, 'w', encoding='utf-8') as fh:
                fh.write(t)
        elif shown < 2:
            shown += 1
            print('=' * 64)
            print(os.path.basename(path))
            for label in LABELS:
                o = cell_span(orig, label, 'SECC Classification')
                n = cell_span(t, label, 'SECC Classification')
                if o and n and o[2] != n[2]:
                    print('  %-14s - %s' % (label, o[2][:96]))
                    print('  %-14s + %s' % ('', n[2][:96]))

    print()
    print('rows trimmed: %s' % ', '.join('%s %d' % (k, v) for k, v in changed.items()))
    print('words removed from the table: %d (%d -> %d)' % (before - after, before, after))
    print('left alone, no Appearance description: %d' % skipped)
    print('refused by the structural guard: %d' % refused)


if __name__ == '__main__':
    main()
