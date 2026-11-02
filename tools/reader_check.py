#!/usr/bin/env python3
"""reader_check.py — the second check: what a reader sees, not what a regex matches.

The other linters ask "is this string right". This one asks "does this file read".
It is deliberately about structure a reader experiences in order:

  1. Heading ladder — a document never opens a level before its parent. No H3
     under an H1, no H2 appearing after an H3 has started a subtree.
  2. Empty section — a heading with no prose under it. A reader who follows the
     heading finds nothing.
  3. Sentence cut off — a section whose last sentence ends without terminal
     punctuation. The file was assembled, not written.
  4. Duplicated paragraph — the same sentence block printed twice. The reader
     reads it twice and trusts it less.
  5. Orphan table row — a `| ... |` line with no table around it. Valid Markdown
     that renders as literal pipes.
  6. Trailing pipe row directly under a heading — a table that lost its header.
  7. File opens without an H1 — the reader lands in the middle of a document.

Every finding carries the line number, because the fix needs to be found.

    python3 tools/reader_check.py            # summary
    python3 tools/reader_check.py -v         # every finding
    python3 tools/reader_check.py --top 25   # worst files
"""
import io
import os
import re
import sys
import glob

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SKIP_PREFIX = ('.git/', 'ARCHIVE/')


def read(p):
    with io.open(p, encoding='utf-8', errors='ignore') as fh:
        return fh.read().replace('\r\n', '\n')


def body_after(t, m, lvl):
    """Text under this heading up to the next heading of the same or higher level.
    A parent heading that holds only sub-sections is not empty: the reader reads
    its children."""
    start = m.end()
    nxt = re.search(r'^#{1,%d}\s' % lvl, t[start:], re.M)
    return t[start:start + (nxt.start() if nxt else len(t) - start)]


def strip_fences(t):
    t = re.sub(r'^```.*?^```', '', t, flags=re.S | re.M)
    return re.sub(r'^~~~.*?^~~~', '', t, flags=re.S | re.M)


def strip_boxes(t):
    """Blank out ASCII box art. The archive draws its headers and record cards as
    bordered boxes; a reader sees a card, but a line-based checker sees a heading
    with no prose and a thousand orphan table rows. Boxes are content."""
    out, i, n = [], 0, len(t.split('\n'))
    lines = t.split('\n')
    while i < n:
        s = lines[i].strip()
        if re.match(r'^[+|].*[+|]$', s) and ('+-' in s or '--+' in s or '+=' in s):
            # consume the whole box
            while i < n:
                cur = lines[i].strip()
                out.append('')
                i += 1
                if re.match(r'^\+[-=+]+\+$', cur):
                    break
                if not cur:
                    break
            continue
        out.append(lines[i])
        i += 1
    return '\n'.join(out)


def check_file(path, t):
    out = []
    t = strip_boxes(t)
    lines = t.split('\n')

    heads = [(m.start(), len(m.group(1)), m.group(2).strip(), m)
             for m in re.finditer(r'^(#{1,6})\s+(.+)$', t, re.M)]

    # 7 — opens with an H1
    if not heads or heads[0][1] != 1:
        out.append(('no H1', 1, 'file opens without an H1'))

    # 1 — heading ladder
    stack = []
    for pos, lvl, name, m in heads:
        while stack and stack[-1] >= lvl:
            stack.pop()
        if stack and lvl > stack[-1] + 1:
            out.append(('heading jump', t[:pos].count('\n') + 1,
                        f'H{stack[-1]} -> H{lvl} at "{name}"'))
        stack.append(lvl)

    # 2 / 3 — empty section, sentence cut off
    for _, lvl, name, m in heads:
        if lvl > 3:
            continue
        body = body_after(t, m, lvl)
        prose = [l.strip() for l in strip_fences(body).split('\n')
                 if l.strip() and not l.strip().startswith(('|', '---', '>', '#', '```', '~~~',
                                                            '+', '- ', '* ', '1.', '2.', '3.'))
                 and not re.match(r'^\*\*[A-Z][^*]{2,32}:\*\*', l.strip())      # metadata field line
                 and not re.match(r'^[\w./-]+\.(py|sh|md|json|svg)(\s|$)', l.strip())]
        # a section is not empty if it carries a table, a metadata block or a box
        has_content = bool(re.search(r'^\||^\*\*[A-Z][^*]{2,32}:\*\*|^\+[-=+]|^[-*] |^\d+\. ', body, re.M))
        if not prose and not has_content:
            out.append(('empty section', t[:m.start()].count('\n') + 1,
                        f'"{name[:40]}" has no prose'))
            continue
        if not prose:
            continue
        last = prose[-1].rstrip()
        if last and not last.endswith(('.', '!', '?', '”', '"', ')', ':', '…', '*')):
            out.append(('cut off', t[:m.start()].count('\n') + 1,
                        f'"{name[:30]}" ends: …{last[-46:]}'))

    # 4 — duplicated paragraph
    paras = {}
    for i, blk in enumerate(re.split(r'\n\s*\n', t)):
        b = ' '.join(blk.split())
        if len(b) < 90 or b.startswith(('|', '#', '>', '---')):
            continue
        if b in paras:
            out.append(('duplicate paragraph', i + 1, b[:60]))
        else:
            paras[b] = True

    # 5 / 6 — orphan table rows
    for i, line in enumerate(lines):
        s = line.strip()
        if not (s.startswith('|') and s.endswith('|')) or set(s) <= set('|-: '):
            continue
        prev = next((lines[j].strip() for j in range(i - 1, -1, -1) if lines[j].strip()), '')
        nxt = next((lines[j].strip() for j in range(i + 1, len(lines)) if lines[j].strip()), '')
        if not prev.startswith('|') and not nxt.startswith('|'):
            out.append(('orphan table row', i + 1, s[:60]))
    return out


def main():
    verbose = '-v' in sys.argv or '--verbose' in sys.argv
    files = sorted(glob.glob('**/*.md', recursive=True))
    files = [f for f in files if not f.startswith(SKIP_PREFIX)]
    tally, per_file = {}, []
    for f in files:
        found = check_file(f, read(f))
        if found:
            per_file.append((f, found))
            for kind, _, _ in found:
                tally[kind] = tally.get(kind, 0) + 1

    print(f'READER CHECK — {len(files)} files')
    for kind, n in sorted(tally.items(), key=lambda x: -x[1]):
        print(f'  {n:>5}  {kind}')
    if not tally:
        print('  0 findings')

    if verbose:
        for f, found in per_file:
            for kind, ln, detail in found:
                print(f'  {f}:{ln}  [{kind}] {detail}')

    if '--top' in sys.argv:
        n = int(sys.argv[sys.argv.index('--top') + 1])
        print(f'\nWORST {n}:')
        for f, found in sorted(per_file, key=lambda x: -len(x[1]))[:n]:
            kinds = {}
            for k, _, _ in found:
                kinds[k] = kinds.get(k, 0) + 1
            print(f'  {len(found):>3}  {f}  {kinds}')

    print('RESULT: PASS' if not tally else 'RESULT: REVIEW')
    return 0 if not tally else 1


if __name__ == '__main__':
    sys.exit(main())
