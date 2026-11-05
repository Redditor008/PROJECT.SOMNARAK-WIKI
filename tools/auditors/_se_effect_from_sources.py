"""Build the `**SE Effect**` row for the 45 % of holdings that have one (R-50).

The occasion comes from the dossier's own `**Activation threshold**` and
`**Entity Type**`; the law is a sentence already in the record — the strongest
behavioural sentence in the Observation Log, the Consequences list, the Contact
Events table or the Combat Actions table. Nothing is invented: the gate
re-checks each body against the file it came from.

Selection is stratified by wing and grade so the 135 are not all one colour.

    python3 tools/auditors/_se_effect_from_sources.py --dry
    python3 tools/auditors/_se_effect_from_sources.py --write
"""
import collections
import glob
import io
import re
import sys

PATHS = [p for p in sorted(glob.glob('SOMNARAK-WORLD/**/SE-*.md', recursive=True))
         if 'MAW_Codex' not in p]
TARGET = 135

BEHAVE = re.compile(
    r'\b(alters?|answers?|follows?|returns?|repeats?|spreads?|speaks?|counts?|moves?|opens?|closes?|'
    r'names?|learns?|remembers?|forgets?|takes?|keeps?|refuses?|calls?|marks?|writes?|draws?|'
    r'changes?|grows?|sings?|weeps?|waits?|wakes?|hunts?|watches?|listens?|lowers?|raises?|'
    r'turns?|breaks?|holds?|carries?|reads?|hears?)\b')
BAD = re.compile(r'the file|this file|N/A|Threshold|threat score|ratio|gauge|\*\*|^\||Work Type|'
                 r'R\.D\.|Comprehension|Personnel Note')
META = re.compile(r'record|debrief|equipment|section|measurement|instrument|camera|photograph|'
                  r'report|ledger|sheet|inventory|survey|percentage', re.I)
STATIC = re.compile(r'\breads?\b|\bmeasured?\b|has read|is recorded|was recorded|has been', re.I)
PROCEDURE = re.compile(r'containment is|post at|is staffed|requires somebody outside|is authorised|'
                       r'permit(?:ted)? only|procedure|is entered|is logged|watch list|no-contact', re.I)
WORKTYPE = re.compile(r'\b(Viderehan|Ferrehan|Flerehan|Pugnahan)\b')
ROLE = {'Viderehan': 'the observer', 'Ferrehan': 'the stander',
        'Flerehan': 'the mourner', 'Pugnahan': 'the confronter'}
ACTOR = re.compile(r"^(It|Its|They|The [A-Z][\w'-]+(?: [A-Z][\w'-]+)?)\b")
WHO = re.compile(r'^(a|the) (worker|watch|observer|handler|reader|viewer|crew|party|warden|bearer|'
                 r'pair|visitor|personnel|guard)\b', re.I)
RANKS = {'Residue': 'I', 'Fragment': 'II', 'Remnant': 'III', 'Vestige': 'IV', 'Sovereign': 'V'}
GRADES = {'Minor': 'α', 'Moderate': 'β', 'Major': 'γ', 'Critical': 'δ', 'Absolute': 'ω'}


def section(t, name):
    keys = [m for m in re.finditer(r'^(#{2,3})\s+(.+)$', t, re.M)]
    for i, m in enumerate(keys):
        if name in m.group(2):
            return t[m.end():keys[i + 1].start() if i + 1 < len(keys) else len(t)]
    return ''


def bullets(s):
    return [l.strip()[2:].strip() for l in s.split('\n') if l.strip().startswith('- ')]


def field(t, label):
    m = re.search(r'^\|\s*\*\*' + label + r'\*\*\s*\|([^|\n]*)', t, re.M)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''


def score(b):
    s = 2 if BEHAVE.search(b) else 0
    if PROCEDURE.search(b):
        s -= 4
    if WORKTYPE.search(b):
        s -= 2
    if ACTOR.match(b):
        s += 3
    if META.search(b):
        s -= 3
    if STATIC.search(b):
        s -= 2
    if 55 <= len(b) <= 155:
        s += 1
    return s


def column(t, name, col):
    out = []
    for line in section(t, name).split('\n'):
        if not line.startswith('|') or set(line) <= set('|- '):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) > col and cells[0] and '---' not in cells[0] \
                and not cells[0].startswith(('Event', 'Name')):
            out.append(re.sub(r'^\[|\]$', '', cells[col]).strip().rstrip('.'))
    return out


def candidates(t):
    out = []
    for src in ('Observation Log', 'Consequences'):
        for b in bullets(section(t, src)):
            if 45 <= len(b) <= 190 and not BAD.search(b) and BEHAVE.search(b):
                out.append((score(b) + 3, len(b), b, src))
    for src, col in (('Contact Events', 1), ('Combat Actions', 2)):
        for b in column(t, src, col):
            if 30 <= len(b) <= 175 and not BAD.search(b) and BEHAVE.search(b):
                out.append((score(b), len(b), b, src))
    return sorted(out, key=lambda x: (-x[0], x[1]))


def lands_on(t, law):
    for _s, _l, b, _src in candidates(t)[1:]:
        if WHO.match(b) and 45 <= len(b) <= 150 and b[:30] != law[:30]:
            return b.rstrip('.')
    return ''


def trigger(t):
    et = field(t, 'Entity Type').lower()
    act = field(t, 'Activation threshold').lower()
    if re.search(r'can breach|possession', et):
        return 'the breach'
    if re.search(r'gauge|%', act):
        return 'the wall'
    if re.search(r'threshold|counter|ignored', act):
        return 'the counter'
    if re.search(r'touch|contact|enter|read|speak|name|open|hold', act):
        return 'the contact'
    return 'the completion'


def effect_text(t):
    c = candidates(t)
    if not c or c[0][0] < 3:
        return None, 0
    law = WORKTYPE.sub(lambda m: ROLE[m.group(1)], c[0][2].rstrip('.'))
    tail = lands_on(t, law)
    body = law + '.' + ((' ' + tail + '.') if tail else '')
    return body, c[0][0]


def strata(t, path):
    r = next((v for k, v in RANKS.items() if k in field(t, 'Coherence')), '?')
    g = next((v for k, v in GRADES.items() if k in field(t, 'Potency')), '?')
    wing = re.search(r'SE-([A-Z])-', path.split('/')[-1])
    return (wing.group(1) if wing else '?', r, g)


def select():
    scored = []
    for p in PATHS:
        t = io.open(p, encoding='utf-8').read()
        body, sc = effect_text(t)
        if not body:
            continue
        scored.append(dict(path=p, text=t, body=body, score=sc, trigger=trigger(t),
                           strata=strata(t, p)))
    groups = collections.defaultdict(list)
    for d in scored:
        groups[d['strata']].append(d)
    quota, rema = {}, []
    for k, v in groups.items():
        exact = len(v) * TARGET / float(len(scored))
        quota[k] = int(exact)
        rema.append((exact - int(exact), k))
    for _f, k in sorted(rema, reverse=True)[:TARGET - sum(quota.values())]:
        quota[k] += 1
    chosen = []
    for k, v in groups.items():
        v.sort(key=lambda d: (-d['score'], d['path']))
        chosen.extend(v[:quota[k]])
    return scored, sorted(chosen, key=lambda d: d['path'])


def row_of(d):
    return '| **SE Effect** | **On %s** — %s |' % (d['trigger'], d['body'])


def insert(d):
    t = d['text']
    anchor = (re.search(r'^\|\s*\*\*(?:Work Gift|Work Damage)\*\*\s*\|.*$', t, re.M)
              or re.search(r'^\|\s*\*\*Activation threshold\*\*\s*\|.*$', t, re.M))
    if not anchor:
        return None
    lines = t.split('\n')
    lines.insert(t[:anchor.end()].count('\n'), row_of(d))
    return '\n'.join(lines)


def main(argv):
    scored, chosen = select()
    print('dossiers with a usable law: %d · selected %d (target %d)'
          % (len(scored), len(chosen), TARGET))
    print('triggers:', collections.Counter(d['trigger'] for d in chosen).most_common())
    print('wings:', collections.Counter(d['strata'][0] for d in chosen).most_common())
    print('scores: top %d · lowest %d' % (chosen[0]['score'], min(d['score'] for d in chosen)))
    if '--dry' in argv:
        for d in chosen[:10]:
            print('\n##', d['path'].split('/')[-1][:50], '| score', d['score'])
            print('  ', row_of(d)[:300])
    if '--write' in argv:
        wrote = 0
        for d in chosen:
            new = insert(d)
            if new:
                io.open(d['path'], 'w', encoding='utf-8').write(new)
                wrote += 1
        print('written %d' % wrote)


if __name__ == '__main__':
    main(sys.argv[1:])
