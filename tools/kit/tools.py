"""Shared measurement layer for the Sorrow Entity dossier quality programme.

Wraps tools/auditors/clone_audit.py so the fix phase can measure couples the
same way every time. A "couple" is two dossiers whose same-named section
overlaps above THRESH; the wing counter is the number of distinct couples.

Why this lives in the repository and not in /tmp: the sandbox is restored at
every turn boundary and untracked files do not survive it. Only tracked content
persists, so the kit has to be committed to be usable across turns.
"""
import os, sys, re, io, collections, itertools

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KIT  = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))
import sect                                    # noqa: E402
from frame_dup import own_tokens, mask          # noqa: E402
import clone_audit as CA                        # noqa: E402

N               = CA.N
DISTINCTIVE_MAX = CA.DISTINCTIVE_MAX  # 25: a gram held by more files is furniture
MIN_SHARED      = 10   # shared distinctive grams before a section pair is measured
THRESH          = 0.50
MIN_SEC_FILES   = 20   # a section must exist in this many files to be compared
FRAGS           = os.path.join(KIT, 'frags.txt')


def files_under(base=None):
    """All 301 dossiers. base defaults to <repo>/SOMNARAK-WORLD, not the repo root."""
    base = base if base is not None else os.path.join(ROOT, 'SOMNARAK-WORLD')
    out = []
    for d in ('Sorrow_Entities', 'Unknown_Entities'):
        p = os.path.join(base, d)
        if not os.path.isdir(p):
            continue
        for f in sorted(os.listdir(p)):
            if f.endswith('.md') and f.startswith('SE-'):
                out.append(os.path.join(p, f))
    return out


def text_grams(t, own):
    m = mask(t, own)
    return CA.grams(m) if m else set()


def body_grams(path):
    own = own_tokens(path)
    g = set()
    for ln in io.open(path, encoding='utf-8'):
        t = ln.strip()
        if not CA.content(t):
            continue
        g |= text_grams(t, own)
    return g


def text_body_grams(text, own):
    g = set()
    for ln in text.split('\n'):
        t = ln.strip()
        if not CA.content(t):
            continue
        g |= text_grams(t, own)
    return g


def secmap(f):
    """Heading -> masked grams, splitting on both ## and ### headings."""
    own = own_tokens(f)
    out = {}
    for name, ls in CA.sections_of(f).items():
        gs = set()
        for t in ls:
            gs |= text_grams(t, own)
        if gs:
            out[name] = gs
    return out


def scan(base=None):
    """Returns (worst, secs, per, total).

    worst: (path_a, path_b) -> highest section ratio between the two
    secs:  (path_a, path_b) -> [(section, cont_a_b, cont_b_a), ...]
    per:   path -> number of couples that file carries
    """
    files = files_under(base)
    secs_of = {f: secmap(f) for f in files}
    by_sec = collections.defaultdict(dict)
    for f in files:
        for name, g in secs_of[f].items():
            by_sec[name][f] = g
    pairs = {}
    for name, fd in by_sec.items():
        if len(fd) < MIN_SEC_FILES:
            continue
        owner = collections.defaultdict(list)
        for f, g in fd.items():
            for x in g:
                owner[x].append(f)
        cand = collections.Counter()
        for x, fl in owner.items():
            if len(fl) > DISTINCTIVE_MAX:
                continue
            for a, b in itertools.combinations(sorted(fl), 2):
                cand[(a, b)] += 1
        for (a, b), c in cand.items():
            if c < MIN_SHARED:
                continue
            ga, gb = fd[a], fd[b]
            cab, cba = CA.cont(ga, gb), CA.cont(gb, ga)
            v = max(cab, cba)
            if v < THRESH:
                continue
            rec = pairs.setdefault((a, b), {'v': 0.0, 'secs': []})
            rec['secs'].append((name, cab, cba))
            if v > rec['v']:
                rec['v'] = v
    worst = {k: r['v'] for k, r in pairs.items()}
    secs  = {k: r['secs'] for k, r in pairs.items()}
    per   = collections.Counter()
    for (a, b) in pairs:
        per[a] += 1
        per[b] += 1
    return worst, secs, dict(per), len(files)
