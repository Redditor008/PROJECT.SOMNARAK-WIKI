#!/usr/bin/env python3
"""quote_audit.py — the dossier's opening quote: one identity, one file.

Owner's direction, 2026-10-07 — *"DO The Quote One First Because That An Identity And Learn How To Write SE Quote."*

The quote is the single blockquote between the H1 and `## SECC Classification`: the first thing a reader meets, the thing
the file is remembered by, and — per the clone audit — the single strongest clone call in the archive. A duplicated quote
lifts the chance of a cloned section inside the pair eighteen-fold: 18 / 84 = 21.4% against a 1.20% archive baseline
(CLONE_AUDIT_2026-10-07.md, Finding 7).

This tool is read-only. It measures the house form, names the duplicate families with their keep-side (the lowest
designation — the pre-cover-up text), and checks a candidate quote before it is written into a file.

  quote_audit.py                  families + house-form statistics over the whole archive
  quote_audit.py --check "<text>" is this text already in use? exact match, nearest three, word count, flags
  quote_audit.py --file <path>    one dossier's quote with the same check

The rules a new quote must pass are written down in REFERENCE_SOMNARAK_WIKI/SE_QUOTE_GUIDE.md.
"""
import argparse
import collections
import difflib
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MARK = re.compile(r'^\s*>+\s*')
OPEN = re.compile(r'^(?:\*+|_+)?\s*[\u201c"\u2018\']+')
CLOSE = re.compile(r'[\u201d"\u2019\']+\s*(?:\*+|_+)?\s*$')
BAND = (5, 46)          # archive range; the middle half sits between 8 and 32 words


def dossiers():
    out = []
    for d in ('SOMNARAK-WORLD/Sorrow_Entities', 'SOMNARAK-WORLD/Unknown_Entities'):
        base = os.path.join(ROOT, d)
        if not os.path.isdir(base):
            continue
        for f in sorted(os.listdir(base)):
            if f.endswith('.md') and f.startswith('SE-'):
                out.append(os.path.join(base, f))
    return out


def code(path):
    m = re.search(r'SE-([A-Z])-([IVX]+)([\u03b1-\u03c9]+)-(\d+)([a-z]?)', os.path.basename(path))
    if not m:
        return '?', 0
    return '%s-%s%s-%s%s' % (m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)), int(m.group(4))


def title(path):
    for ln in io.open(path, encoding='utf-8'):
        if ln.startswith('# '):
            return ln[2:].split('\u2014')[0].strip()
    return os.path.basename(path)[:-3]


def raw_quote(path):
    for ln in io.open(path, encoding='utf-8'):
        if ln.startswith('## '):
            return None
        t = ln.strip()
        if t.startswith('>') and t.strip('> ').strip():
            return t
    return None


def plain(raw):
    t = MARK.sub('', raw or '')
    t = OPEN.sub('', t)
    t = CLOSE.sub('', t)
    return t.strip()


def norm(t):
    return re.sub(r'\s+', ' ', t).strip().lower()


def census():
    q = {}
    for f in dossiers():
        r = raw_quote(f)
        if r:
            q[f] = r
    fam = collections.defaultdict(list)
    for f, r in q.items():
        fam[norm(plain(r))].append(f)
    for k in fam:
        fam[k].sort(key=lambda f: code(f)[1])
    return q, fam


def form_stats(texts):
    ws = sorted(len(t.split()) for t in texts)
    n = len(ws) or 1
    quart = (ws[0], ws[n // 4], ws[n // 2], ws[3 * n // 4], ws[-1])
    sents = collections.Counter()
    for t in texts:
        c = max(1, len(re.findall(r'[.!?\u2026](?=\s|$)', t)))
        sents[min(c, 3)] += 1

    def pct(pred):
        return 100.0 * sum(1 for t in texts if pred(t)) / n
    feats = collections.OrderedDict((
        ('question', pct(lambda t: t.rstrip().endswith('?'))),
        ('you', pct(lambda t: 'you' in t.lower())),
        ('we', pct(lambda t: re.search(r'\bwe\b', t.lower()))),
        ('digit', pct(lambda t: re.search(r'\d', t))),
        ('em dash', pct(lambda t: '\u2014' in t)),
        ('entity', pct(lambda t: 'entity' in t.lower())),
    ))
    first = collections.Counter(t.split()[0] for t in texts if t.split())
    return quart, sents, feats, first


def report():
    q, fam = census()
    dups = {k: v for k, v in fam.items() if len(v) > 1}
    distinct = [plain(r) for r in q.values() if len(fam[norm(plain(r))]) == 1]
    quart, sents, feats, first = form_stats(distinct)
    print('QUOTE CENSUS — %d / %d dossiers carry a quote; %d distinct; %d families / %d dossiers duplicated'
          % (len(q), len(dossiers()), len(fam), len(dups), sum(len(v) for v in dups.values())))
    print('  form: words min %d / p25 %d / median %d / p75 %d / max %d' % quart)
    print('  sentences 1 = %d, 2 = %d, 3+ = %d' % (sents.get(1, 0), sents.get(2, 0), sents.get(3, 0)))
    print('  traits: ' + ' | '.join('%s %.1f%%' % (k, v) for k, v in feats.items()))
    print('  first words: ' + ', '.join('%s %d' % (w, c) for w, c in first.most_common(8)))
    if not dups:
        print('no duplicate quotes remain.')
        return 0
    print('\nduplicate families (keep-side is the lowest designation):')
    for k, v in sorted(dups.items(), key=lambda kv: -len(kv[1])):
        keep = v[0]
        print('  x%d  keep %-12s %-34s | "%s"' % (len(v), code(keep)[0], title(keep)[:34], k[:70]))
        for f in v[1:]:
            print('        copy %-12s %s' % (code(f)[0], title(f)[:44]))
    return 0


def check(text, q, fam):
    n = norm(text)
    words = len(text.split())
    print('quote:   "%s"' % text)
    print('words:   %d   (archive band %d-%d; half fall between %d and %d)'
          % (words, BAND[0], BAND[1], 8, 32))
    hits = fam.get(n, [])
    if hits:
        print('match:   DUPLICATE — already used by %d dossier(s):' % len(hits))
        for f in hits:
            print('           %-12s %s' % (code(f)[0], os.path.basename(f)))
        print('verdict: NOT clear to use.')
        return 1
    print('match:   no exact duplicate.')
    pool = {norm(plain(r)): f for f, r in q.items()}
    near = difflib.get_close_matches(n, list(pool), n=3, cutoff=0.55)
    if near:
        print('nearest:')
        for m in near:
            print('           %.2f  %-12s %s' % (difflib.SequenceMatcher(None, n, m).ratio(), code(pool[m])[0], plain(q[pool[m]])[:76]))
    else:
        print('nearest: nothing within 0.55 — the quote reads as its own.')
    flags = []
    if re.search(r'\d', text):
        flags.append('digits present (allowed but rare: 0.7%)')
    if 'entity' in text.lower():
        flags.append('the word "entity" (rare: 0.7%)')
    if text.rstrip().endswith('?'):
        flags.append('question (0.0% in the archive)')
    if not (BAND[0] <= words <= BAND[1]):
        flags.append('outside the band %d-%d words' % BAND)
    print('flags:   ' + ('; '.join(flags) if flags else 'none'))
    print('verdict: CLEAR to use.' if not flags else 'verdict: clear with the flags above.')
    return 0


REGISTERS = (
    ('R1 entity speaks (first person singular)', lambda t: bool(re.search(r'\b(I|my|me|mine)\b', t))),
    ('R1b staff speaks (first person plural)', lambda t: bool(re.search(r'\b(we|us|our|ours)\b', t.lower()))),
    ('R2 addressed to you (second person)', lambda t: bool(re.search(r'\byou(r)?\b', t.lower()))),
    ('R3 documentary record', lambda t: bool(re.search(r'\b(record|file|register|ledger|report|log)\b', t.lower()))),
    ('R6 question', lambda t: t.rstrip().endswith('?')),
    ('R7 nested dialogue', lambda t: t.count('"') >= 2 or t.count('\u201c') >= 1),
    ('R5 lyric / elegy image', lambda t: bool(re.search(r'\b(light|sky|snow|star(s)?|sea|rain|song|music|bloom|flower)\b', t.lower()))),
)
IMPERATIVE = ('do', 'look', 'keep', 'listen', 'remember', 'leave', 'stop', 'hold', 'stand', 'walk', 'run', 'come', 'let', 'count')


def registers():
    """Heuristic register census: the parent genre (Project Moon) speaks in many voices; this measures ours."""
    q, _ = census()
    texts = [plain(r) for r in q.values()]
    n = len(texts) or 1
    print('REGISTER CENSUS (heuristic, read-only) — %d / %d quotes' % (len(texts), len(dossiers())))
    shown = set()
    for name, pred in REGISTERS:
        hits = [t for t in texts if pred(t)]
        print('  %-42s %3d / %-3d %5.1f%%' % (name, len(hits), n, 100.0 * len(hits) / n))
        for t in hits[:1]:
            if name not in shown:
                print('        e.g. "%s"' % t[:92]); shown.add(name)
    imp = [t for t in texts if t.split() and t.split()[0].strip('"\u201c').lower() in IMPERATIVE]
    print('  %-42s %3d / %-3d %5.1f%%' % ('imperative opening', len(imp), n, 100.0 * len(imp) / n))
    print('  Guidance: the genre varies registers across a roster; uniqueness (one quote per file) is not enough —')
    print('  a wing that speaks in one voice still reads as generated. See ABNORMALITY_QUOTE_RESEARCH_2026-10-07.md.')
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description='the dossier opening quote — identity, families, and a pre-write check')
    ap.add_argument('--check', metavar='TEXT', help='test a candidate quote against all 301 quotes')
    ap.add_argument('--file', metavar='PATH', help='show one dossier\'s quote with the same checks')
    ap.add_argument('--registers', action='store_true', help='register census across the archive (heuristic)')
    args = ap.parse_args(argv)
    q, fam = census()
    if args.registers:
        return registers()
    if args.check:
        return check(args.check, q, fam)
    if args.file:
        path = args.file if os.path.isabs(args.file) else os.path.join(ROOT, args.file)
        r = raw_quote(path)
        if not r:
            print('no quote found in', path)
            return 1
        print('file:    %s  [%s]' % (os.path.basename(path), code(path)[0]))
        return check(plain(r), q, fam)
    return report()


if __name__ == '__main__':
    sys.exit(main())
