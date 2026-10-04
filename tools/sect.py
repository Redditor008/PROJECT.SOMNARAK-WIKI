#!/usr/bin/env python3
"""Generic-prose census by 8-gram sharing (Workstream 6, second measure).

Line-level tools (`tools/boilerplate_report.py`, `tpl.py`) only catch text that
repeats *verbatim as a whole line*. They cannot see a paragraph that was
generated from a pattern and differs from its siblings by one or two nouns --
which is most of what the previous AI left behind. This tool measures that.

Method: lower-case every dossier, take the set of 8-word shingles, and call a
shingle SHARED when it occurs in >= 10 dossiers. A file's GENERIC FRACTION is
the share of its own shingles that are shared ones. A section's score is the
fraction of dossiers carrying that section in which it contains at least one
shared shingle.

The benchmark is set inside the archive, not invented: the Tale section
(`## 이야기 (Narratio)`) scores 0.000 across all 298 dossiers that have one, and
the eleven fully bespoke dossiers score 0.012-0.046 overall. A dossier is
counted CLEAN here at <= 0.05.

Usage:
    sect.py                 archive summary and the clean counter
    sect.py --sections      per-section league table (worst first)
    sect.py --files [N]     N best and N worst dossiers (default 10)
    sect.py <path>          per-line shared-shingle attribution for one file
"""
import os
import re
import sys
import collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WINGS = ['SOMNARAK-WORLD/Sorrow_Entities', 'SOMNARAK-WORLD/Unknown_Entities']
N = 8
MIN_SHARE = 10
CLEAN_AT = 0.05


def dossiers():
    out = []
    for d in WINGS:
        for f in sorted(os.listdir(os.path.join(ROOT, d))):
            if f.endswith('.md') and f != 'README.md':
                out.append(os.path.join(ROOT, d, f))
    return out


FURNITURE_PREFIX = (
    '> **R.D. Operational Record:', '> **R.D. Field Parameters:',
    '> **Mechanics Reference:', '> **Materialized Agony Wear',
    '> **Object/Place Work Rule:', '> Progressive declassified records',
    '**Document ID:', '**Author:', '**Date:', '**Classification:',
    '**Registry:', '**Canon Status:', '**Type:', '**Slot:',
    '**Damage:', '**Resistances:', '**Max Amount:', '**Falloff Rule:',
    '**Damage Application:', '**Containment Status:', '**Comprehension Level:',
)
FURNITURE_LABEL = re.compile(
    r'^\|\s*\*\*(Coherence modifier|Potency modifier|Entity role|Entity Type|'
    r'Sorrow Category|Valid Work Types|Work difficulty|Difficulty|Comprehension Level|'
    r'R\.D\. Comprehension Level|Vessel-Destructible|Speed|Movement|Flerehan|Pugnahan|'
    r'Viderehan|Ferrehan|Activation threshold|Tool / M\.A\.W\. grade|Risk tier|'
    r'Han Dust Drop|Element|Designation|Coherence|Potency|Manifestation)\*\*')


def is_furniture(line):
    t = line.strip()
    if not t or t.startswith('#'):
        return True
    if t.startswith('|') and (set(t) <= set('|- :') or '| Field | Value |' in t
                              or t.startswith('| Statistic |') or t.startswith('| Stat |')
                              or t.startswith('| Name / Category |')):
        return True
    if FURNITURE_LABEL.match(t):
        return True
    return t.startswith(FURNITURE_PREFIX)


def grams(text, prose_only=True):
    """8-grams. By default only from lines that are not R-23 sanctioned furniture."""
    out = set()
    lines = text.split('\n') if prose_only else [text]
    for ln in lines:
        if prose_only and is_furniture(ln):
            continue
        w = re.sub(r'[^a-z\s]', ' ', ln.lower()).split()
        for i in range(len(w) - N + 1):
            out.add(' '.join(w[i:i + N]))
    return out


def split_sections(text):
    out, cur, buf = [], '(preamble)', []
    for ln in text.split('\n'):
        if ln.startswith('## '):
            out.append((cur, '\n'.join(buf)))
            cur = re.sub(r'\s*—.*', '', ln[3:]).strip()
            buf = []
        else:
            buf.append(ln)
    out.append((cur, '\n'.join(buf)))
    return out


def build():
    files = dossiers()
    per, owner = {}, collections.defaultdict(set)
    for p in files:
        g = grams(open(p, encoding='utf-8').read())
        per[p] = g
        for x in g:
            owner[x].add(p)
    shared = {x for x, v in owner.items() if len(v) >= MIN_SHARE}
    return files, per, shared


def main():
    args = sys.argv[1:]
    paths = [a for a in args if not a.startswith('-') and not a.isdigit()]
    files, per, shared = build()
    score = {p: len(g & shared) / len(g) for p, g in per.items() if g}

    if paths:
        for p in paths:
            ap = p if p.startswith('/') else os.path.join(ROOT, p)
            tot = 0
            for i, ln in enumerate(open(ap, encoding='utf-8'), 1):
                hit = len(grams(ln) & shared)
                if hit:
                    tot += hit
                    print('%5d %3d  %s' % (i, hit, ln.strip()[:130]))
            print('GENERIC %.3f  (%d shared shingles)  %s'
                  % (score.get(ap, 0), tot, os.path.basename(ap)))
        return

    if '--sections' in args:
        own = collections.defaultdict(set)
        dirty = collections.defaultdict(set)
        for p in files:
            for name, body in split_sections(open(p, encoding='utf-8').read()):
                own[name].add(p)
                if grams(body) & shared:
                    dirty[name].add(p)
        rows = sorted(((len(dirty[k]) / len(v), len(v), k)
                       for k, v in own.items() if len(v) >= 20), reverse=True)
        print('%6s %6s  %s' % ('score', 'files', 'section'))
        for f, n, k in rows:
            print('%6.2f %6d  %s' % (f, n, k))
        return

    if '--files' in args:
        k = 10
        for a in args:
            if a.isdigit():
                k = int(a)
        rows = sorted((v, os.path.basename(p)) for p, v in score.items())
        print('BEST %d:' % k)
        for v, b in rows[:k]:
            print('  %.3f  %s' % (v, b[:72]))
        print('WORST %d:' % k)
        for v, b in rows[-k:]:
            print('  %.3f  %s' % (v, b[:72]))
        return

    vals = sorted(score.values())
    med = vals[len(vals) // 2]
    clean = sum(1 for v in vals if v <= CLEAN_AT)
    print('dossiers                      %d' % len(score))
    print('shared 8-grams (>= %d files)  %d' % (MIN_SHARE, len(shared)))
    print('median generic fraction       %.3f' % med)
    print('worst                         %.3f' % vals[-1])
    print('clean at <= %.2f               %d / %d' % (CLEAN_AT, clean, len(score)))


if __name__ == '__main__':
    main()
