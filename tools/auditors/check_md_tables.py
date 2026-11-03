#!/usr/bin/env python3
"""check_md_tables.py — every markdown table is a table, not a run of pipes.

Owner rule, 2026-11-03:

> *"And Also TRY TO FIX A LOT OF FILE HAVE BROKEN markdown Table"*

Three ways a block of `|`-rows stops being a table in GitHub-flavoured
markdown, and all three were present in the archive:

1. **`single-row`** — a lone row. A one-row block renders as literal text, not
   a table, because there is no separator under a header.
2. **`no-separator`** — two or more rows, no `|---|` row in position 2. The
   whole block renders as paragraphs of pipe characters.
3. **`ragged`** — the block has a separator, but its rows disagree on how many
   cells they carry. GFM pads or drops the surplus, so the last column shifts.

A fourth fault is reported per row rather than per block:

4. **`odd-backticks`** — an odd number of code-span markers on one row. A cell
   that opens a span and never closes it swallows every pipe after it, so the
   row stops being four cells however well it counts.

Two things this scanner deliberately does that a naive `startswith('|')` scan
does not:

* **It skips fenced code blocks.** The archive draws in-world ASCII boxes with
  `|` borders inside `~~~` fences (`tools/textbox.py` geometry). Those are box
  art, not rows; a naive scan reported 4,697 false faults on them.
* **It splits cells on `(?<!\\\\)\\|`.** A table cell escapes an inner pipe as
  `\\|`; counting that as a boundary turns every stat run and every quoted
  residue line into a ragged row.

The archive was at **369 ragged** before the batch-158 repair and is at **0**.
There is no ratchet because there is nothing left to ratchet down: the rule is
the whole corpus, not a moving floor.

    python3 tools/auditors/check_md_tables.py            # the gate check
    python3 tools/auditors/check_md_tables.py -v         # every fault, full width
    python3 tools/auditors/check_md_tables.py PATH ...   # a narrower run
"""
import glob
import io
import re
import sys

# Cells end at an unescaped pipe. The lookbehind is the whole point: `\|` inside
# a cell is content, `\\|` is a literal backslash followed by a real boundary.
PIPESPLIT = re.compile(r'(?<!\\)\|')

# Code-span markers, unescaped. Two per span, so a row must hold an even count.
BACKTICK = re.compile(r'(?<!\\)`')

# A separator row is pipes, dashes, colons and spaces only.
SEP = re.compile(r'^\s*\|[\s:\-|]+\|\s*$')

# A fence is a run of three or more backticks or tildes, and it is closed only by
# the same character at equal or greater length. Tracking the character matters:
# `TEMPLATES/` nests a ```text block inside a ~~~markdown block, and a scanner
# that toggles on "any fence line" sees the inner closing ``` as a new opening and
# reports the template's own box art as ten broken tables.
FENCE = re.compile(r'^\s*(`{3,}|~{3,})')


def fence_state(line, state):
    """Return the new fence state for `line`. state = (char, length) or None."""
    m = FENCE.match(line)
    if not m:
        return state
    run = m.group(1)
    if state is None:
        return (run[0], len(run))
    if run[0] == state[0] and len(run) >= state[1]:
        return None
    return state

# Big enough to hold the reference wiki without listing every file by hand.
CORPUS = ('SOMNARAK-WORLD/**/*.md', 'REFERENCE_SOMNARAK_WIKI/**/*.md',
          'TEMPLATES/**/*.md', 'tools/README.md')


def cells(line):
    """How many cells a row carries. `| a | b |` -> 2."""
    return len(PIPESPLIT.split(line)) - 2


def tables(lines):
    """Yield (start, end) index pairs for each run of table rows outside a fence."""
    i, fence = 0, None
    while i < len(lines):
        line = lines[i]
        nxt = fence_state(line, fence)
        if nxt is not fence and fence is None:
            fence = nxt
            i += 1
            continue
        if fence is not None:
            fence = nxt
            i += 1
            continue
        if not line.lstrip().startswith('|'):
            i += 1
            continue
        j = i
        while j < len(lines) and not FENCE.match(lines[j]) and lines[j].lstrip().startswith('|'):
            j += 1
        yield i, j
        i = j


def scan(paths):
    """Return [(path, first line number, fault, header)] for every broken block."""
    out = []
    for path in paths:
        try:
            with io.open(path, encoding='utf-8') as fh:
                lines = fh.read().split('\n')
        except (IOError, UnicodeDecodeError):
            continue
        for start, end in tables(lines):
            block = lines[start:end]
            if len(block) < 2:
                out.append((path, start + 1, 'single-row', block[0][:60]))
                continue
            if not SEP.match(block[1]):
                out.append((path, start + 1, 'no-separator', block[0][:60]))
                continue
            widths = [cells(line) for line in block]
            if len(set(widths)) > 1:
                out.append((path, start + 1, 'ragged %s' % sorted(set(widths)), block[0][:60]))
            for k, line in enumerate(block):
                if len(BACKTICK.findall(line)) % 2:
                    out.append((path, start + k + 1, 'odd-backticks', line[:60]))
    return out


def corpus():
    paths = []
    for pattern in CORPUS:
        paths.extend(glob.glob(pattern, recursive=True))
    return sorted(set(paths))


def main(argv):
    args = [a for a in argv if not a.startswith('-')]
    paths = args or corpus()
    faults = scan(paths)
    for path, line, kind, header in faults:
        shown = header if '-v' in argv else header[:52]
        print('%s | %s:%d | %s' % (kind, path, line, shown))
    print('%d files | %d broken table blocks | %d single-row, %d no-separator, %d ragged, '
          '%d odd-backticks'
          % (len(paths), len(faults),
             sum(1 for f in faults if f[2] == 'single-row'),
             sum(1 for f in faults if f[2] == 'no-separator'),
             sum(1 for f in faults if f[2].startswith('ragged')),
             sum(1 for f in faults if f[2] == 'odd-backticks')))
    if faults:
        print('RESULT: FAIL')
        print('repair with: python3 tools/fix_md_tables.py --apply')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
