#!/usr/bin/env python3
"""review.py — a whole-wing audit for defects the gate tools do not catch.

The five gate tools (verify, tpl, sectfile, wikistd, couples) each answer one
narrow question. This one asks the questions none of them ask: is the prose
finished, does a section declare one type and contain another, is a table row
sitting in the file twice, is there placeholder text, is a section empty.

  review.py                full audit, summary then findings
  review.py --check NAME   run one check only
  review.py --file PATH    audit one dossier

Checks
  truncated    a prose paragraph that does not end in terminal punctuation
  midlower     a sentence beginning lower-case straight after ". " or "? "
  placeholder  TODO / TBD / XXX / ??? / [insert ...] and friends
  duprow       a bold table label appearing twice with identical values
  typemix      a M.A.W. section whose declared Category contradicts its heading
  emptysec     a heading with nothing under it before the next heading
  shortsec     a prose section below a word floor (default 25)
  heading      heading level skips and duplicate headings in one file
"""
import glob, io, os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TERMINAL = tuple('.!?:;"\')]}…*_~')
# Weapon-class words. A Suit or Stigma slot declaring one of these is the
# one type contradiction that occurs in this archive (a Weapon's Category
# copied into the Suit and Stigma blocks).
WEAPON_CLASS = (
    'SHORT BLADE', 'LONG BLADE', 'BLADES', 'BLADE', 'GUN', 'GUN SHAPE',
    'BLUNT', 'POLEARM', 'SPEAR', 'BOW', 'STAFF', 'SCEPTRE', 'SCEPTER',
    'MAUL', 'HAMMER', 'TALON', 'SICKLE', 'FALX', 'DAGGER', 'CUDGEL',
)
PLACEHOLDER = re.compile(
    r'(\bTODO\b|\bTBD\b|\bXXX\b|\bFIXME\b|\?\?\?|\[insert\b|\bPLACEHOLDER\b|\bLorem\b)', re.I)

# A prose paragraph is a non-empty line that is not a heading, table row,
# bullet, blockquote, separator or HTML.
def is_prose(line):
    s = line.strip()
    if not s:                       return False
    if s.startswith('#'):           return False
    if s.startswith('|'):           return False
    if s.startswith('>'):           return False
    if s.startswith('-'):           return False
    if s.startswith('*'):           return False
    if set(s) <= set('-=_* '):      return False
    if s.startswith('<'):           return False
    if re.match(r'^\d+\.\s', s):    return False
    return True

def split_sentences(text):
    """Sentence starts that should be capitalised."""
    out = []
    # Require a lowercase letter (or closing quote/bracket) immediately
    # before the stop: that is a real sentence end. An uppercase single
    # letter before the stop is an initial (R.D., M.A.W.), not an end.
    for m in re.finditer(r'(?<=[a-z\u201d"\')][.!?])\s+([a-z])', text):
        out.append(text[max(0, m.start() - 40):m.end() + 30].replace('\n', ' '))
    return out


# --------------------------------------------------------------------------
# checks
# --------------------------------------------------------------------------

def check_truncated(path, text):
    """A PARAGRAPH whose final line stops short of terminal punctuation.

    Single lines are not tested: these files hard-wrap prose across lines, so a
    mid-paragraph line without a full stop is normal. Only the last line of a
    block is meaningful — if that is cut, the sentence was left unfinished.
    """
    bad = []
    lines = text.split('\n')
    run, start = [], 0
    def flush():
        if not run:
            return
        last = run[-1][1].strip()
        if last and last[-1] not in TERMINAL:
            bad.append((run[-1][0], last[-95:]))
    for i, line in enumerate(lines, 1):
        if is_prose(line):
            if not run:
                start = i
            run.append((i, line))
        else:
            flush()
            run = []
    flush()
    return bad


def check_midlower(path, text):
    bad = []
    for i, line in enumerate(text.split('\n'), 1):
        if not is_prose(line):
            continue
        for frag in split_sentences(line):
            bad.append((i, frag.strip()))
    return bad


def check_placeholder(path, text):
    bad = []
    for i, line in enumerate(text.split('\n'), 1):
        m = PLACEHOLDER.search(line)
        if not m:
            continue
        # "the placeholder fields have been filled from the SECC header"
        # describes work that was completed. Only an un-filled slot is a defect.
        tail = line[max(0, m.start() - 60):m.end() + 60].lower()
        if re.search(r'\b(were|was|been)\b[^.]{0,40}\bfill', tail) or \
           re.search(r'\bfill[^.]{0,40}\bplaceholder', tail):
            continue
        bad.append((i, m.group(1), line.strip()[-80:]))
    return bad


def check_duprow(path, text):
    """Same bold label twice in the file carrying the same value."""
    rows = collections.defaultdict(list)
    for i, line in enumerate(text.split('\n'), 1):
        m = re.match(r'^\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|$', line)
        if m:
            rows[m.group(1)].append((i, m.group(2)))
    bad = []
    for label, hits in rows.items():
        if len(hits) < 2:
            continue
        vals = {v for _, v in hits}
        if len(vals) == 1 and len(hits) > 1:
            bad.append(([h[0] for h in hits], label, hits[0][1][:70]))
    return bad


TYPE_WORDS = {
    'Suit':   ('armor', 'armour', 'suit'),
    'Weapon': ('weapon', 'blade', 'sword', 'staff', 'sceptre', 'scepter',
               'spear', 'bow', 'maul', 'hammer'),
    'Stigma': ('accessory', 'stigma', 'charm', 'trinket'),
}

def check_typemix(path, text):
    """A M.A.W. section whose Category line contradicts the heading."""
    bad = []
    lines = text.split('\n')
    cur = None
    for i, line in enumerate(lines, 1):
        m = re.match(r'^###\s+M\.A\.W\.\s+(Suit|Weapon|Stigma)\b.*$', line)
        if m:
            cur = (m.group(1), i, line.strip()[:60])
            continue
        if cur and re.match(r'^\*\*(Type|Category):?\*\*\s*:?', line):
            kind, hline, head = cur
            declared = re.sub(r'^\*\*(Type|Category):?\*\*\s*:?', '', line)
            # Compare only the leading category words, before ' (' or ' |'.
            lead = re.split(r'\s*[|(]\s*', declared)[0].strip().upper()
            # Vocabulary was derived from all 301 dossiers: Weapon sections use
            # WEAPON/FANTASY/PRIMAL/BLUNT/RANGE/... , Suit uses ARMOR or
            # PROTECTIVE ATTIRE, Stigma uses ACCESSORY or STIGMA. So the only
            # reliable signal is a Suit or Stigma slot declaring a weapon class.
            if kind in ('Suit', 'Stigma') and any(w in lead for w in WEAPON_CLASS):
                bad.append((i, head, kind, lead))
            cur = None
    return bad


def check_emptysec(path, text):
    bad = []
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if not re.match(r'^#{2,4}\s+\S', line):
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j >= len(lines):
            bad.append((i + 1, line.strip()[:70], 'end of file'))
        elif re.match(r'^#{2,4}\s+\S', lines[j]):
            bad.append((i + 1, line.strip()[:70], lines[j].strip()[:50]))
    return bad


def check_shortsec(path, text, floor=25):
    bad = []
    lines = text.split('\n')
    heads = [(i, l) for i, l in enumerate(lines) if re.match(r'^#{2,4}\s+\S', l)]
    for n, (i, head) in enumerate(heads):
        end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        body = ' '.join(lines[i + 1:end]).strip()
        if not body:
            continue
        words = len(body.split())
        if words < floor:
            bad.append((i + 1, head.strip()[:70], words))
    return bad


def check_heading(path, text):
    bad = []
    lines = text.split('\n')
    prev = 0
    for i, line in enumerate(lines, 1):
        m = re.match(r'^(#{1,6})\s+(\S.*)$', line)
        if not m:
            continue
        lvl = len(m.group(1))
        if prev and lvl > prev + 1:
            bad.append((i, 'level skip %d -> %d' % (prev, lvl), m.group(2)[:60]))
        prev = lvl
    # A heading name repeated under DIFFERENT parents is by design in this
    # archive — "### Escalation Notes" legitimately appears once under
    # Activation / Expansion Behavior and again under Breach Behavior, with
    # different content. Only a repeat under the SAME parent is a real
    # duplicate block.
    parents, cur = collections.defaultdict(set), None
    for line in lines:
        m = re.match(r'^(#{2,4})\s+(\S.*)$', line)
        if not m:
            continue
        if len(m.group(1)) == 2:
            cur = m.group(2).strip()
        parents[m.group(2).strip()].add(cur)
    counts = collections.Counter()
    for line in lines:
        m = re.match(r'^#{2,4}\s+(\S.*)$', line)
        if m:
            counts[m.group(1).strip()] += 1
    # A SINGLE repeated heading name is almost always the benign
    # activation-vs-breach pattern above. When TWO OR MORE headings repeat
    # together, a whole block has been duplicated — that is always a defect,
    # even when the two parents are near-synonyms of each other.
    repeated = {d: n for d, n in counts.items() if n > 1}
    block = len(repeated) >= 2
    for d, n in repeated.items():
        if block or len(parents[d]) == 1:
            bad.append((0, 'duplicate heading x%d' % n, d[:70]))
    return bad


CHECKS = {
    'truncated':   check_truncated,
    'midlower':    check_midlower,
    'placeholder': check_placeholder,
    'duprow':      check_duprow,
    'typemix':     check_typemix,
    'emptysec':    check_emptysec,
    'shortsec':    check_shortsec,
    'heading':     check_heading,
}


def main(argv):
    only = None
    files = None
    if '--check' in argv:
        only = argv[argv.index('--check') + 1]
    if '--file' in argv:
        files = [argv[argv.index('--file') + 1]]

    if files is None:
        files = sorted(glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD', '*', 'SE-*_*.md')))

    names = [only] if only else list(CHECKS)
    findings = collections.defaultdict(list)
    for p in files:
        text = io.open(p, encoding='utf-8').read()
        for name in names:
            for hit in CHECKS[name](p, text):
                findings[name].append((p, hit))

    print('REVIEW — %d dossiers, checks: %s' % (len(files), ', '.join(names)))
    print('-' * 78)
    for name in names:
        print('  %-12s %4d finding(s) in %d file(s)' % (
            name, len(findings[name]), len({p for p, _ in findings[name]})))
    print()

    limit = 25
    for name in names:
        hits = findings[name]
        if not hits:
            continue
        print('=' * 78)
        print('%s — %d' % (name.upper(), len(hits)))
        print('=' * 78)
        for p, hit in hits[:limit]:
            print('  %s' % os.path.basename(p)[:58])
            print('      %s' % (hit,))
        if len(hits) > limit:
            print('  … %d more' % (len(hits) - limit))
        print()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
