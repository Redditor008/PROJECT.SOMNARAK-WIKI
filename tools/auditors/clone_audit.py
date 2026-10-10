#!/usr/bin/env python3
"""clone_audit.py — is any dossier the same file as another, renamed and re-designated?

Owner's question, 2026-10-07 — *"How To Check It They Are The Same SE But Just Change Title +
Designation : [Combat Actions] Se It And Also Check Everything Else Like Comparison Between SE
File Maybe Some Already Change But You Could Detect If It Just A Change To Try To Hide It"*.

Method. A renamed copy keeps everything except the title, the registry code and the dossier's own
name, so the audit removes exactly those from **both** sides before comparing, and then compares
everything else on four layers:

  1. body        masked 5-gram containment both ways over every content line (tables included,
                 so the Combat Actions move table is inside the measurement)
  2. prose       the same over narrative lines only (table rows excluded)
  3. sections    per-section containment — '### Combat Actions', '### Battle Phases', the
                 registrum, the observation log and every other heading are compared separately,
                 so a copied table cannot hide behind an original narrative or the reverse
  4. lines       exact and near-identical line matches, the last of these with a similarity ratio,
                 which is what catches a copy that had a few words changed to disguise it

Masking: registry codes (`C-IIIγ-928`), sector ids, 1-5 digit figures, and the dossier's own name
words in English and Korean. Table pipes are dropped so column text still counts.

  clone_audit.py                 summary + top suspect pairs
  clone_audit.py --top N         show N pairs (default 15)
  clone_audit.py --report FILE   write the full report to FILE
  clone_audit.py <path>          one dossier: its closest matches and the shared lines

Read-only. This tool changes no dossier; it is a detector, not a repair.
"""
import collections
import difflib
import io
import itertools
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))
import sect                      # noqa: E402
from frame_dup import own_tokens, mask   # noqa: E402  (same masking used by the frame auditor)

N = 5            # shingle width for this audit; shorter than frame_dup's 6 to catch looser copies
STOP = {'that', 'with', 'from', 'this', 'they', 'into', 'over', 'under', 'their', 'there', 'then',
        'than', 'them', 'these', 'those', 'when', 'where', 'which', 'while', 'have', 'been', 'were',
        'will', 'would', 'could', 'should', 'upon', 'after', 'before', 'every', 'each', 'only',
        'also', 'even', 'more', 'most', 'much', 'such', 'same', 'both', 'does', 'did', 'its'}
MIN_TOK = 4
DISTINCTIVE_MAX = 25   # a gram held by more than this many dossiers is furniture, not evidence


def dossiers():
    out = []
    for d in ('SOMNARAK-WORLD/Sorrow_Entities', 'SOMNARAK-WORLD/Unknown_Entities'):
        base = os.path.join(ROOT, d)
        for f in sorted(os.listdir(base)):
            if f.endswith('.md') and f.startswith('SE-'):
                out.append(os.path.join(base, f))
    return out


def content(line):
    t = line.strip()
    if not t or t.startswith('#'):
        return False
    if sect.is_furniture(t):
        return False
    return len(re.sub(r'[|*`>\[\]{}]', ' ', t).split()) >= MIN_TOK


def prose(line):
    t = line.strip()
    if not content(t):
        return False
    return not t.startswith('|')


def grams(text):
    w = text.split()
    if len(w) < N:
        return set()
    return {' '.join(w[i:i + N]) for i in range(len(w) - N + 1)}


def sections_of(path):
    """Heading -> masked content text, splitting on both ## and ### headings."""
    out, cur = collections.OrderedDict(), None
    for ln in io.open(path, encoding='utf-8'):
        if ln.startswith('## ') or ln.startswith('### '):
            cur = re.sub(r'\s*—.*', '', ln.strip().lstrip('#').strip()).strip()
            out.setdefault(cur, [])
        elif cur is not None and content(ln):
            out[cur].append(ln.strip())
    return out


def load(files):
    data = {}
    for f in files:
        own = own_tokens(f)
        body, prosel, lines = set(), set(), []
        for ln in io.open(f, encoding='utf-8'):
            t = ln.strip()
            if not content(t):
                continue
            m = mask(t, own)
            if not m:
                continue
            g = grams(m)
            body |= g
            if prose(t):
                prosel |= g
            lines.append((m, t))
        secs = {}
        for name, ls in sections_of(f).items():
            gs = set()
            for t in ls:
                gs |= grams(mask(t, own))
            if gs:
                secs[name] = gs
        data[f] = {'body': body, 'prose': prosel, 'lines': lines, 'secs': secs,
                   'name': os.path.basename(f)}
    return data


def cont(a, b):
    return len(a & b) / float(len(a)) if a else 0.0


DESIG = re.compile(r'SE-([A-Z]-[IVX]+[\u03b1-\u03c9]-(\d+)[a-z]?)_')


def designation(path):
    """(code, number) from the filename — the registry's own ordering key."""
    m = DESIG.match(os.path.basename(path))
    if not m:
        return None, None
    return m.group(1), int(m.group(2))


def raw_tokens(line):
    return re.sub(r'[^0-9A-Za-z\uac00-\ud7a3\s\u03b1-\u03c9\u2019\u2014-]', ' ', line).split()


def line_map(path, own):
    out = {}
    for ln in io.open(path, encoding='utf-8'):
        t = ln.strip()
        if content(t):
            out.setdefault(mask(t, own), t)
    return out


def substitutions(ta, tb):
    """Which raw tokens the copy changed against the source, position by position."""
    wa, wb = raw_tokens(ta), raw_tokens(tb)
    if len(wa) != len(wb):
        return []
    return [(x, y) for x, y in zip(wa, wb) if x != y]


def lineage(data, pairs, top_pairs=40):
    """Within a copied pair the lower designation number is the source. For each copy this
    reports what it was before the cover-up: the substitutions against the source, and the
    source's own vocabulary left behind in the copy as residue."""
    codes = {}
    for f in data:
        c, n = designation(f)
        if c:
            codes[f] = (n, c)
    by_sec = collections.defaultdict(dict)
    for f, d in data.items():
        for name, g in d['secs'].items():
            by_sec[name][f] = g
    fam = []
    for (a, b) in pairs[:top_pairs]:
        for name in set(data[a]['secs']) & set(data[b]['secs']):
            ga, gb = data[a]['secs'][name], data[b]['secs'][name]
            if len(ga) < 12 or len(gb) < 12:
                continue
            if cont(ga, gb) >= 0.5 or cont(gb, ga) >= 0.5:
                if a in codes and b in codes:
                    win, cop = (a, b) if codes[a][0] < codes[b][0] else (b, a)
                    fam.append((name, win, cop, cont(ga, gb), cont(gb, ga)))
    return fam, codes


def section_scan(data):
    """Every section, every pair: which headings hold two dossiers that are copies of each other.

    Whole-file overlap can stay low while a whole block — the Combat Actions move table, the
    Consequences list, the equipment tables — was copied across. This reports each section's
    clone pairs, and the most widely shared line inside it, which is the template itself.
    """
    by_sec = collections.defaultdict(dict)
    for f, d in data.items():
        for name, g in d['secs'].items():
            by_sec[name][f] = g
    rows = []
    for name, files in by_sec.items():
        if len(files) < 20:
            continue
        owner = collections.defaultdict(list)
        for f, g in files.items():
            for x in g:
                owner[x].append(f)
        cand = collections.Counter()
        for x, fl in owner.items():
            if len(fl) > DISTINCTIVE_MAX:
                continue
            for a, b in itertools.combinations(sorted(fl), 2):
                cand[(a, b)] += 1
        res = []
        for (a, b), c in cand.items():
            if c < 10:
                continue
            ga, gb = files[a], files[b]
            cab, cba = cont(ga, gb), cont(gb, ga)
            res.append((max(cab, cba), a, b, cab, cba))
        res.sort(reverse=True)
        rows.append((name, len(files), sum(1 for r in res if r[0] >= 0.9),
                     sum(1 for r in res if r[0] >= 0.5), sum(1 for r in res if r[0] >= 0.3), res[:3]))
    rows.sort(key=lambda r: -r[3])
    print('%-34s %5s %7s %7s %7s  %s' % ('section', 'files', '>=0.90', '>=0.50', '>=0.30', 'strongest pair'))
    for name, n, c9, c5, c3, top3 in rows:
        if top3:
            w = top3[0]
            pair = '%s / %s  %.2f' % (os.path.basename(w[1])[:26], os.path.basename(w[2])[:26], w[0])
        else:
            pair = '-'
        print('%-34s %5d %7d %7d %7d  %s' % (name[:34], n, c9, c5, c3, pair))
    return rows


def print_lineage(data, fam, codes):
    per = collections.defaultdict(lambda: {'secs': set()})
    for name, win, cop, cab, cba in fam:
        per[(win, cop)]['secs'].add((name, cab, cba))
    rows = []
    for (win, cop), info in per.items():
        ownw, ownc = own_tokens(win), own_tokens(cop)
        mw, mc = line_map(win, ownw), line_map(cop, ownc)
        shared = sorted(set(mw) & set(mc))
        subs = collections.Counter(); subst_lines = 0
        for k in shared:
            sub = substitutions(mw[k], mc[k])
            if sub:
                subst_lines += 1
                for x, y in sub:
                    subs[(x, y)] += 1
        res = collections.Counter()
        for ln in io.open(cop, encoding='utf-8'):
            t = ln.strip()
            if not content(t):
                continue
            low = t.lower()
            for w in ownw:
                if w in ownc or w in STOP:
                    continue
                if re.search(r'(?<![A-Za-z0-9])%s(?![A-Za-z0-9])' % re.escape(w), low):
                    res[w] += 1
        rows.append((len(info['secs']), len(shared), subst_lines, sum(res.values()),
                     win, cop, info['secs'], subs, res))
    rows.sort(reverse=True)
    print('lineage — the lower designation number is the source; each copy below shows what')
    print('it carried before the title, designation and figures were changed:\n')
    for nsec, nshare, nsub, nres, win, cop, secs, subs, res in rows[:24]:
        print('%s  [%s]   winner (lower designation)' % (codes[win][1], os.path.basename(win)[:46]))
        print('    copy %s  [%s]' % (os.path.basename(cop)[:46], codes[cop][1]))
        print('    copied sections (%d): %s' % (nsec, ', '.join(sorted(x[0] for x in secs))[:130]))
        print('    shared lines %d | lines with substitutions %d | source-name residue left in copy %d'
              % (nshare, nsub, nres))
        if subs:
            print('    substitutions: ' + ', '.join('%s -> %s' % (x, y) for (x, y), c in subs.most_common(8)))
        if res:
            print('    residue: ' + ', '.join('%s x%d' % (w, c) for w, c in res.most_common(8)))
        print()


def opening_quote(path):
    """The blockquote between the H1 title and ## SECC Classification — the line the reskin
    passes paste in whole. Owner's finding, 2026-10-07: this is the first call of a clone."""
    out, seen = [], False
    for ln in io.open(path, encoding='utf-8'):
        t = ln.rstrip('\n')
        if t.startswith('# ') and not seen:
            seen = True
            continue
        if seen and t.startswith('## '):
            if 'SECC Classification' in t:
                break
            continue
        if seen and t.strip().startswith('>'):
            out.append(t.strip())
        elif seen and out and t.strip():
            break
    q = re.sub(r'\s+', ' ', ' '.join(out).lstrip('> ').strip())
    return re.sub(r'^[*_"]+|[*_"]+$', '', q).strip()


def quotes_report(data):
    """Restart of the check from the opening quote: families first, then the clones inside them."""
    fam = collections.defaultdict(list)
    for f in data:
        q = opening_quote(f)
        if q:
            fam[q].append(f)
    groups = [(q, v) for q, v in fam.items() if len(v) >= 2]
    groups.sort(key=lambda kv: -len(kv[1]))
    members = sum(len(v) for _, v in groups)
    print('dossiers %d | opening quotes present %d | duplicated quote families %d covering %d dossiers'
          % (len(data), sum(1 for f in data if opening_quote(f)), len(groups), members))
    # section-clone index once
    by = collections.defaultdict(dict)
    for f, d in data.items():
        for k, v in d['secs'].items():
            by[k][f] = v
    clone = set()
    for name, fl in by.items():
        if len(fl) < 20:
            continue
        owner = collections.defaultdict(list)
        for f, g in fl.items():
            for x in g:
                owner[x].append(f)
        cand = collections.Counter()
        for x, lst in owner.items():
            if len(lst) > DISTINCTIVE_MAX:
                continue
            for a, b in itertools.combinations(sorted(lst), 2):
                cand[(a, b)] += 1
        for (a, b), c in cand.items():
            if c < 10:
                continue
            if max(cont(fl[a], fl[b]), cont(fl[b], fl[a])) >= 0.5:
                clone.add((a, b) if a < b else (b, a))
    tot = withn = 0
    for v in groups:
        for a, b in itertools.combinations(sorted(v[1]), 2):
            k = (a, b) if a < b else (b, a)
            tot += 1
            if k in clone:
                withn += 1
    print('within-family pairs carrying a section clone: %d / %d = %.1f%%  (archive baseline %.2f%% -> lift %.0fx)'
          % (withn, tot, 100.0 * withn / tot if tot else 0,
             100.0 * len(clone) / (len(data) * (len(data) - 1) / 2), (100.0 * withn / tot) / (100.0 * len(clone) / (len(data) * (len(data) - 1) / 2)) if tot else 0))
    print()
    for q, v in groups:
        print('QUOTE "%s"  -- %d dossiers' % (q[:100], len(v)))
        for f in v:
            print('    %s' % os.path.basename(f))
        hits = []
        for a, b in itertools.combinations(sorted(v), 2):
            best = None
            for name in set(data[a]['secs']) & set(data[b]['secs']):
                ga, gb = data[a]['secs'][name], data[b]['secs'][name]
                if len(ga) < 12 or len(gb) < 12:
                    continue
                m = max(cont(ga, gb), cont(gb, ga))
                if best is None or m > best[0]:
                    best = (m, name)
            if best and best[0] >= 0.5:
                na, nb = designation(a)[1], designation(b)[1]
                win, cop = (a, b) if (na or 0) < (nb or 0) else (b, a)
                hits.append((best[0], best[1], os.path.basename(win)[:34], os.path.basename(cop)[:34]))
        for m, name, win, cop in sorted(hits, reverse=True)[:8]:
            print('    clone %.2f  %-26s  %s  ->  %s' % (m, name[:26], win, cop))
        print()


def plan_report(data):
    """Restart-and-plan: light vs heavy for every pair carrying a copied section.

    wholesale (W) = a section carried across whole  (>= 0.85 containment)
    partial   (P) = a section sharing a few lines  (0.50 - 0.85)

    Owner's method, 2026-10-07: fix the light side's small overlaps; clean the heavy side's
    whole-block copies (Combat Actions, Operational Parameters named as the usual two).
    """
    by = collections.defaultdict(dict)
    for f, d in data.items():
        for k, v in d['secs'].items():
            by[k][f] = v
    pair_secs = collections.defaultdict(list)
    for name, fl in by.items():
        if len(fl) < 20:
            continue
        owner = collections.defaultdict(list)
        for f, g in fl.items():
            for x in g:
                owner[x].append(f)
        cand = collections.Counter()
        for x, lst in owner.items():
            if len(lst) > DISTINCTIVE_MAX:
                continue
            for a, b in itertools.combinations(sorted(lst), 2):
                cand[(a, b)] += 1
        for (a, b), c in cand.items():
            if c < 10:
                continue
            cab, cba = cont(fl[a], fl[b]), cont(fl[b], fl[a])
            if max(cab, cba) >= 0.50:
                pair_secs[(a, b)].append((name, cab, cba))
    rows = []
    for (a, b), secs in pair_secs.items():
        wa = sum(1 for n, x, y in secs if x >= 0.85)
        wb = sum(1 for n, x, y in secs if y >= 0.85)
        pa = sum(1 for n, x, y in secs if 0.50 <= x < 0.85)
        pb = sum(1 for n, x, y in secs if 0.50 <= y < 0.85)
        if (wa, pa) >= (wb, pb):
            heavy, light, hW, hP, lW, lP, hx, lx = a, b, wa, pa, wb, pb, True, False
        else:
            heavy, light, hW, hP, lW, lP, hx, lx = b, a, wb, pb, wa, pa, False, True
        rows.append([max(wa + pa, wb + pb), max(wa, wb), heavy, light, hW, hP, lW, lP, secs, hx])
    rows.sort(key=lambda r: (-r[0], -r[1]))
    print('PAIR PLANNER — light side (small overlaps to fix) vs heavy side (whole blocks to clean)')
    print('%-36s %-36s %4s %4s %4s %4s' % ('heavy side', 'light side', 'hW', 'hP', 'lW', 'lP'))
    for r in rows[:24]:
        print('%-36s %-36s %4d %4d %4d %4d' % (os.path.basename(r[2])[:36], os.path.basename(r[3])[:36],
              r[4], r[5], r[6], r[7]))
    heavy_files = collections.Counter()
    for r in rows:
        heavy_files[r[2]] += 1
    print()
    print('heavy sides: %d files | light sides: %d files | pairs: %d'
          % (len({r[2] for r in rows}), len({r[3] for r in rows}), len(rows)))
    print('clean-first work order (heavy sides, worst first):')
    for f, n in heavy_files.most_common(12):
        print('   %2d pair(s)  %s' % (n, os.path.basename(f)))
    return rows


def print_pair(a, b, data):
    """Everything needed to compare one pair by hand, in one command."""
    A, B = data[a], data[b]
    ca, cb = designation(a), designation(b)
    win, cop = (a, b) if (ca[0] or 0) <= (cb[0] or 0) else (b, a)
    print('pair report')
    print('  A  %s  [%s]' % (os.path.basename(a), ca[0]))
    print('  B  %s  [%s]' % (os.path.basename(b), cb[0]))
    print('  source (lower designation): %s' % os.path.basename(win))
    print('  A contains %.3f of B | B contains %.3f of A | prose %.3f / %.3f'
          % (cont(A['body'], B['body']), cont(B['body'], A['body']),
             cont(A['prose'], B['prose']), cont(B['prose'], A['prose'])))
    print()
    print('  sections compared separately:')
    rows = []
    for name in sorted(set(A['secs']) & set(B['secs'])):
        ga, gb = A['secs'][name], B['secs'][name]
        if len(ga) < 12 or len(gb) < 12:
            continue
        cab, cba = cont(ga, gb), cont(gb, ga)
        if max(cab, cba) >= 0.30:
            rows.append((max(cab, cba), name, cab, cba))
    for m, name, cab, cba in sorted(rows, reverse=True):
        flag = '  <-- identical block' if m >= 0.9 else ''
        print('    %-34s A-in-B %5.2f  B-in-A %5.2f%s' % (name[:34], cab, cba, flag))
    if not rows:
        print('    none above 0.30')
    print()
    ma, mb = line_map(win, own_tokens(win)), line_map(cop, own_tokens(cop))
    shared = sorted(set(ma) & set(mb))
    subs = [(mw := ma[k], mb[k], substitutions(ma[k], mb[k])) for k in shared]
    subs = [x for x in subs if x[2]]
    print('  shared lines: %d  | with substitutions: %d' % (len(shared), len(subs)))
    print()
    print('  the shared lines themselves (source / copy):')
    n = 0
    for k in shared:
        if n >= 15:
            break
        ta, tb = ma[k], mb[k]
        sub = substitutions(ta, tb)
        tag = ('changed: ' + ', '.join('%s->%s' % x for x in sub[:4])) if sub else 'identical'
        print('    [%s]' % tag)
        print('      source: %s' % ta[:150])
        print('      copy  : %s' % tb[:150])
        n += 1


def main(argv):
    top = 15
    report = None
    single = None
    do_sections = False
    do_lineage = False
    pair_paths = None
    do_quotes = False
    do_plan = False
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == '--top':
            top = int(argv[i + 1]); i += 1
        elif a == '--report':
            report = argv[i + 1]; i += 1
        elif a == '--sections':
            do_sections = True
        elif a == '--lineage':
            do_lineage = True
        elif a == '--quotes':
            do_quotes = True
        elif a == '--plan':
            do_plan = True
        elif a == '--pair':
            pair_paths = [argv[i + 1], argv[i + 2]]
            i += 2
        else:
            single = a
        i += 1

    if do_plan:
        plan_report(load(dossiers()))
        return 0

    if do_quotes:
        quotes_report(load(dossiers()))
        return 0

    if pair_paths:
        a = pair_paths[0] if os.path.isabs(pair_paths[0]) else os.path.join(ROOT, pair_paths[0])
        b = pair_paths[1] if os.path.isabs(pair_paths[1]) else os.path.join(ROOT, pair_paths[1])
        print_pair(a, b, load([a, b]))
        return 0

    files = dossiers()
    if single:
        single = single if os.path.isabs(single) else os.path.join(ROOT, single)
        files = [single]
    data = load(files)
    if single:
        target = data[single]
        rows = []
        for f, d in data.items():
            if f == single:
                continue
            rows.append((cont(target['body'], d['body']), cont(d['body'], target['body']), d['name']))
        rows.sort(reverse=True)
        print('closest matches to %s' % os.path.basename(single))
        for cab, cba, name in rows[:5]:
            print('  contains / contained-by  %.3f / %.3f  %s' % (cab, cba, name[:60]))
        return 0

    if do_sections:
        section_scan(data)
        return 0

    # ---- pairwise pass 1: distinctive-gram index, cheap candidate counts
    owner = collections.defaultdict(list)
    for f, d in data.items():
        for g in d['body']:
            owner[g].append(f)
    cand = collections.Counter()
    for g, fl in owner.items():
        if len(fl) > DISTINCTIVE_MAX:
            continue
        for a, b in itertools.combinations(sorted(fl), 2):
            cand[(a, b)] += 1

    # ---- pairwise pass 2: exact metrics for candidates + top of the field
    keys = [k for k, c in cand.most_common(400) if c >= 5]
    metrics = {}
    for a, b in keys:
        A, B = data[a], data[b]
        metrics[(a, b)] = {
            'cab': cont(A['body'], B['body']), 'cba': cont(B['body'], A['body']),
            'pab': cont(A['prose'], B['prose']), 'pba': cont(B['prose'], A['prose']),
            'cand': cand[(a, b)]}
    ranked = sorted(metrics.items(), key=lambda kv: -max(kv[1]['cab'], kv[1]['cba'], kv[1]['pab'], kv[1]['pba']))

    if do_lineage:
        fam, codes = lineage(data, [k for k, _ in ranked])
        print_lineage(data, fam, codes)
        return 0

    # ---- section-level clones (Combat Actions and every other heading)
    sec_clone = collections.defaultdict(list)
    for (a, b), m in ranked[:300]:
        for name in set(data[a]['secs']) & set(data[b]['secs']):
            ga, gb = data[a]['secs'][name], data[b]['secs'][name]
            if len(ga) < 12 or len(gb) < 12:
                continue
            if cont(ga, gb) >= 0.5 or cont(gb, ga) >= 0.5:
                sec_clone[name].append((a, b, cont(ga, gb), cont(gb, ga)))

    # ---- exact and near-identical lines for the strongest pairs
    line_hits = {}
    norm_index = collections.defaultdict(list)
    for f, d in data.items():
        for m, t in d['lines']:
            norm_index[m].append(f)
    for (a, b), m in ranked[:40]:
        da, db = data[a], data[b]
        exact = 0
        for na, _ in da['lines']:
            if na in {nb for nb, _ in db['lines']}:
                exact += 1
        near = []
        for na, ta in da['lines']:
            wa = set(na.split())
            if len(wa) < 6:
                continue
            best = 0.0
            best_raw = None
            for nb, tb in db['lines']:
                wb = set(nb.split())
                if abs(len(wa) - len(wb)) > max(4, len(wa) // 3):
                    continue
                ov = len(wa & wb) / float(min(len(wa), len(wb)))
                if ov < 0.6:
                    continue
                r = difflib.SequenceMatcher(None, na, nb).ratio()
                if r > best:
                    best, best_raw = r, tb
            if best >= 0.75:
                near.append((best, ta, best_raw))
        near.sort(reverse=True)
        line_hits[(a, b)] = {'exact': exact, 'near': near[:3]}

    # ---- Combat Actions move-table comparison, explicit
    ca_rows = {}
    for f, d in data.items():
        ls = sections_of(f)
        for name, body in ls.items():
            if name.lower().startswith('combat actions'):
                ca_rows[f] = frozenset(mask(x, own_tokens(f)) for x in body)
    ca_groups = collections.defaultdict(list)
    for f, rows in ca_rows.items():
        ca_groups[rows].append(f)
    ca_clones = sorted(((len(v), k) for k, v in ca_groups.items() if len(v) >= 2), reverse=True)

    # ---- printed summary
    out = []
    def p(s=''):
        out.append(s)
        print(s)

    p('dossiers                       %d' % len(data))
    p('distinctive masked %d-grams   %d' % (N, len(owner)))
    p('candidate pairs                 %d' % len(cand))
    p('Combat Actions tables found     %d / %d' % (len(ca_rows), len(data)))
    p('Combat Actions tables shared byte-for-byte (after masking): %d group(s)' % len(ca_clones))
    p()
    if ranked:
        worst = ranked[0][1]
        p('strongest pair: %s / %s'
          % (data[ranked[0][0][0]]['name'][:40], data[ranked[0][0][1]]['name'][:40]))
        p('  contains %.3f | contained-by %.3f | prose %.3f/%.3f | shared distinctive grams %d'
          % (worst['cab'], worst['cba'], worst['pab'], worst['pba'], worst['cand']))
        vals = [max(m['cab'], m['cba'], m['pab'], m['pba']) for _, m in ranked]
        p('  pairs at >= 0.50: %d | >= 0.30: %d | >= 0.15: %d | >= 0.08: %d'
          % (sum(1 for v in vals if v >= .5), sum(1 for v in vals if v >= .3),
             sum(1 for v in vals if v >= .15), sum(1 for v in vals if v >= .08)))
    p()
    p('%-42s %-42s %6s %6s %6s %5s' % ('file A', 'file B', 'A in B', 'B in A', 'prose', 'lines'))
    for (a, b), m in ranked[:top]:
        lh = line_hits.get((a, b), {'exact': 0, 'near': []})
        p('%-42s %-42s %6.3f %6.3f %6.3f %5d' % (data[a]['name'][:40], data[b]['name'][:40],
          m['cab'], m['cba'], max(m['pab'], m['pba']), lh['exact']))
    p()
    p('section-level clones (containment >= 0.50 both directions tested):')
    for name, lst in sorted(sec_clone.items(), key=lambda kv: -len(kv[1]))[:12]:
        p('  %-34s %2d pair(s)  e.g. %s / %s' % (name[:34], len(lst),
          data[lst[0][0]]['name'][:28], data[lst[0][1]]['name'][:28]))
    if ca_clones:
        p()
        p('Combat Actions move tables shared between dossiers:')
        for c, rows in ca_clones[:10]:
            fl = ca_groups[rows]
            p('  %d dossiers share one table-set: %s' % (c, ', '.join(os.path.basename(x)[:34] for x in fl[:6])))

    if report:
        rp = report if os.path.isabs(report) else os.path.join(ROOT, report)
        with io.open(rp, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(out) + '\n')
            fh.write('\nEVIDENCE — strongest pairs, near-identical lines:\n')
            for (a, b), m in ranked[:top]:
                lh = line_hits.get((a, b))
                if not lh or not lh['near']:
                    continue
                fh.write('\n%s  <->  %s   (contains %.3f / %.3f)\n'
                         % (data[a]['name'], data[b]['name'], m['cab'], m['cba']))
                for r, ta, tb in lh['near']:
                    fh.write('  ratio %.2f\n    A: %s\n    B: %s\n' % (r, ta[:180], (tb or '')[:180]))
        print('\nreport written: %s' % report)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
