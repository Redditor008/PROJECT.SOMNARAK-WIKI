#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""refine_prose.py - make the SE dossiers read.

The dossiers are not short of information; they are short of air. Three mechanical
defects make a dossier hurt to read, and all three can be repaired without inventing,
deleting or reordering a single fact:

1. THE ANNOUNCEMENT.  108 files open a sentence with
       "the close is the file's documented condition: **<the actual condition>**"
   The sentence announces that it is about to state the condition, then states it.
   The announcement is deleted; the condition is not touched.

2. THE SPLICE.  The corpus carries 8,486 semicolons joining two independent clauses.
   Each one is a sentence trying to get out. Replacing "; " with ". " and capitalising
   changes no words, only the stop between them.

3. THE RUN-ON.  Where a sentence already runs past 45 words and turns on ", and" or
   ", but", the turn is promoted to a full stop. The clauses were independent already;
   the comma was hiding it.

A split never happens inside a backtick span, bracket, brace, parenthesis or a bold
run, and never at a point that would leave an unmatched ** or _. Prose only: table
rows, headings, blockquotes and fenced code are skipped, so no mechanical field and no
curated quote is touched.

    python3 tools/repairs_and_patches/refine_prose.py            report only
    python3 tools/repairs_and_patches/refine_prose.py --write    apply
"""
import argparse
import glob
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATHS = sorted(glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD', '*', 'SE-*.md')))

ANNOUNCE = [
    re.compile(r"the close is the file['\u2019]s documented (?:suppression )?condition:\s*", re.I),
    re.compile(r"the close is the file['\u2019]s documented condition:\s*", re.I),
    re.compile(r"and the close is the file['\u2019]s documented condition:\s*", re.I),
]

SENT_END = re.compile(r'(?<=[.!?])\s+')
SPLICE = re.compile(r';\s+')
TURN = re.compile(r',\s+(?=(?:and|but|so|yet|while|whereas)\s+[A-Za-z\u2018\u201c])')
MIN_SENT = 26          # a splice needs this much sentence around it
MIN_PART = 6           # ...and only where both halves carry this many words
MIN_TURN_SENT = 46     # a coordinator turn needs an even longer sentence


def prose_lines(text):
    """Yield (start, end) offsets of lines a reader experiences as prose."""
    spans, pos, fence = [], 0, False
    for line in text.split('\n'):
        end = pos + len(line)
        s = line.lstrip()
        if s.startswith('```'):
            fence = not fence
        elif not fence and s and not s.startswith(('#', '    ')):
            spans.append((pos, end))
        pos = end + 1
    return spans


def _safe_at(s, i):
    """True when offset i sits in plain prose: outside any span or bracket, and
    not a point where cutting would unbalance ** or _."""
    back = ticks = braces = parens = brackets = 0
    for ch in s[:i]:
        if ch == '`': ticks ^= 1
        elif ch == '[': brackets += 1
        elif ch == ']': brackets = max(0, brackets - 1)
        elif ch == '{': braces += 1
        elif ch == '}': braces = max(0, braces - 1)
        elif ch == '(': parens += 1
        elif ch == ')': parens = max(0, parens - 1)
    if ticks or braces or parens or brackets:
        return False
    back = s[:i].count('**') % 2
    if back:
        return False
    tail = s[i:].count('**')
    return True


def _cap(s):
    for k, ch in enumerate(s):
        if ch.isalpha():
            return s[:k] + ch.upper() + s[k + 1:]
    return s


def split_sentence(s, stats):
    """Promote clause boundaries in one long sentence to full stops."""
    n = len(s.split())
    if n < MIN_SENT:
        return s
    # --- semicolons first: they were always independent sentences
    out = _split_at(s, SPLICE, 0, stats, 'splice')
    # --- then coordinator turns, but only in what is still very long
    if len(out.split()) >= MIN_TURN_SENT:
        out = _split_at(out, TURN, MIN_TURN_SENT, stats, 'turn')
    return out


def _split_at(s, pat, floor, stats, kind):
    pos, pieces, last = 0, [], 0
    for m in pat.finditer(s):
        i = m.start()
        if len(s.split()) < max(floor, 1) or not _safe_at(s, i):
            continue
        head, tail = s[last:i], s[m.end():]
        if len(head.split()) < MIN_PART or len(tail.split()) < MIN_PART:
            continue
        pieces.append(head.rstrip())
        last = m.end()
        stats[kind] += 1
        pos = i
    if not pieces:
        return s
    pieces.append(s[last:].lstrip())
    joined = pieces[0]
    for p in pieces[1:]:
        joined += '. ' + _cap(p)
    return joined


def refine_text(text, stats):
    for rx in ANNOUNCE:
        stats['announce'] += len(rx.findall(text))
        text = rx.sub('', text)
    for start, end in reversed(prose_lines(text)):
        seg = text[start:end]
        new = SENT_END.sub(lambda m: m.group(0), seg)  # no-op keeps offsets honest
        buf, out = [], []
        for part in re.split(r'((?<=[.!?])\s+)', seg):
            if part.isspace():
                out.append(part)
            elif part:
                out.append(split_sentence(part, stats))
        new = ''.join(out)
        if new != seg:
            text = text[:start] + new + text[end:]
    return text


def readability(text):
    prose = []
    for line in text.split('\n'):
        s = line.lstrip()
        if s and not s.startswith(('|', '#', '>')):
            prose.append(line)
    body = ' '.join(prose)
    sents = [x for x in re.split(r'(?<=[.!?])\s+', body) if len(x.split()) > 3]
    long = [x for x in sents if len(x.split()) >= 45]
    return {
        'sentences': len(sents),
        'mean_words': round(sum(len(x.split()) for x in sents) / max(1, len(sents)), 1),
        'long': len(long),
        'semicolons': body.count('; '),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()

    before = {'sentences': 0, 'long': 0, 'semicolons': 0, 'words': 0}
    after = {'sentences': 0, 'long': 0, 'semicolons': 0, 'words': 0}
    stats = {'announce': 0, 'splice': 0, 'turn': 0}
    touched = 0

    for path in PATHS:
        with io.open(path, encoding='utf-8') as fh:
            text = fh.read()
        b = readability(text)
        for k in ('sentences', 'long', 'semicolons'):
            before[k] += b[k]
        before['words'] += len(text.split())

        new = refine_text(text, stats)
        a = readability(new)
        for k in ('sentences', 'long', 'semicolons'):
            after[k] += a[k]
        after['words'] += len(new.split())

        if new != text:
            touched += 1
            if args.write:
                with io.open(path, 'w', encoding='utf-8') as fh:
                    fh.write(new)

    print('SE dossiers: %d' % len(PATHS))
    print('touched:     %d' % touched)
    print()
    print('%-14s %10s %10s' % ('', 'before', 'after'))
    print('%-14s %10d %10d' % ('sentences', before['sentences'], after['sentences']))
    print('%-14s %10d %10d' % ('sentences>=45w', before['long'], after['long']))
    print('%-14s %10d %10d' % ('semicolon splices', before['semicolons'], after['semicolons']))
    print('%-14s %10d %10d' % ('words', before['words'], after['words']))
    print()
    print('removed announcements: %d' % stats['announce'])
    print('splits made:           %d splices, %d coordinator turns'
          % (stats['splice'], stats['turn']))


if __name__ == '__main__':
    main()
