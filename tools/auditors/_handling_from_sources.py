"""Build `## Handling Process` for a relic out of the file's own fields (R-40).

Preferred source — the dossier already narrates the four stages in order:

    Approach   <- ### Watch Sequence  1. **What is confirmed:**
    Handling   <- ### Watch Sequence  2. **What the watch does:**
    Withdrawal <- ### Watch Sequence  3. **How it closes:**
    Refusal    <- the Contact Events row tagged [**Refusal**]

Fallback for the dossiers that predate that block — **Recommended response**,
the Contact Events "what the watch carries out" column, **Resolution Condition**,
and the Contact Record's own **Handling** field.

Nothing is invented. Work Type names are stripped, because the section exists to
replace them. The `**Valid Work Types**` row is deleted where the Contact Record
already has a `**Handling**` row — renaming it there would leave two rows with
the same label.
"""
import io
import re
import sys

sys.path.insert(0, 'tools/auditors')
import check_relic_work_types as g

WT = re.compile(r'\b(Viderehan|Ferrehan|Flerehan|Pugnahan)\b')
POINTER = ' — see `## Handling Process`'


def lead_sentence(s, cap=170):
    s = re.sub(r'\s+', ' ', s or '').strip()
    if not s:
        return 'It is a holding that is approached, handled and left'
    m = re.match(r'(.+?[.!?])(?:\s|$)', s)
    if m and len(m.group(1)) <= cap:
        return m.group(1).rstrip('.')
    if len(s) <= cap:
        return s.rstrip('.')
    return s[:cap].rsplit(' ', 1)[0].rstrip(',;:.') + '…'


def field(t, lbl):
    m = re.search(r'^\|\s*\*\*' + lbl + r'\*\*\s*\|([^|\n]*)', t, re.M)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''


ROLE = {'Viderehan': 'the observer', 'Ferrehan': 'the stander',
        'Flerehan': 'the mourner', 'Pugnahan': 'the confronter'}


def clean(s):
    """Replace the Work Type names with the roles they name (R-40: the relic
    offers no Work Type, but the procedure still needs its two people)."""
    for k, v in ROLE.items():
        s = re.sub(r'\b' + k + r'\b', v, s)
    s = re.sub(r'the observer (?:and the stander )?only\b', 'the observer and the stander', s)
    s = re.sub(r'(the observer|the stander|the mourner|the confronter) to\b', r'\1 is to', s)
    s = re.sub(r'Only\s+\(?Observation\)?\s+and\s+\(?Endurance\)?\s+are valid Work Types\.?', '', s)
    s = re.sub(r'\bvalid Work Types\b\.?', '', s)
    s = re.sub(r'\bWork Types?\b', 'stages', s)
    s = re.sub(r'\s{2,}', ' ', s)
    s = s.strip(' ,;')
    return s[0].upper() + s[1:] if s else s


def pick(s, cap=300):
    s = clean(re.sub(r'\s+', ' ', s or '')).strip()
    if not s:
        return ''
    if len(s) > cap:
        s = s[:cap].rsplit(' ', 1)[0].rstrip(',;:') + '…'
    return s if s.endswith(('.', '!', '?', '…')) else s + '.'


def watch_sequence(t):
    m = re.search(r'^### Watch Sequence\s*$(.*?)(?=^###?\s|\Z)', t, re.M | re.S)
    if not m:
        return {}
    body = m.group(1)
    out = {}
    for key, pat in (('approach', r'What is confirmed'), ('handling', r'What the watch does'),
                     ('withdrawal', r'How it closes')):
        mm = re.search(r'^\d+\.\s*\*\*' + pat + r':\*\*\s*(.+)$', body, re.M)
        if mm:
            out[key] = mm.group(1).strip()
    return out


def events(t):
    m = re.search(r'^### Contact Events\s*$(.*?)(?=^###?\s|\Z)', t, re.M | re.S)
    out = []
    if not m:
        return out
    for line in m.group(1).split('\n'):
        if not line.startswith('|') or set(line) <= set('|- '):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) >= 3 and cells[0] and not cells[0].startswith('Event') and '---' not in cells[0]:
            out.append(cells)
    return out


def sentences(s):
    return [x.strip() for x in re.split(r'(?<=[.!?])\s+', re.sub(r'\s+', ' ', s or '').strip()) if x.strip()]


def rule_reason(t):
    m = re.search(r'>\s*\*\*Object/Place Work Rule:\*\*\s*(.+)', t)
    return re.sub(r'\s*Only .*$', '', m.group(1)).strip().rstrip('.') if m else ''


def neutral_reason(t):
    m = re.search(r'\|\s*\*\*(Flerehan|Pugnahan)\*\*[^|]*\|[^|]*\bNet-Neutral\b[^|]*[—–-]\s*([^|]+)\|', t)
    return re.sub(r'\s+', ' ', m.group(2)).strip().rstrip('.') if m else ''


def build(p):
    t = io.open(p, encoding='utf-8').read()
    bm = re.search(r'^## Behavior\n(.*?)(?=\n## )', t, re.M | re.S)
    if not bm:
        return None, 'no ## Behavior'

    ws, ev = watch_sequence(t), events(t)
    rec, res = field(t, 'Recommended response'), field(t, 'Resolution Condition')
    mode, act, oldhand = field(t, 'Mode of presence'), field(t, 'Activation threshold'), field(t, 'Handling')

    refusal = ''
    for cells in ev:
        if 'Refusal' in cells[0]:
            refusal = pick(cells[2])
            break
    if not refusal:
        refusal = pick(oldhand)
    if not refusal and act:
        a = act.strip().rstrip('.')
        a = (a[0].lower() + a[1:]) if len(a) > 1 and a[1].islower() else a
        refusal = 'Nothing that would meet the activation — ' + a + ' — is done on purpose.'

    DEGRADED = re.compile(r'^The (?:observer|stander)\b.*\bfor\b', re.I)
    rs = [x for x in sentences(rec) if len(clean(x)) > 40]
    ra = ws.get('approach')
    approach = pick('Confirm ' + ra[0].lower() + ra[1:]) if ra else pick(rs[0] if rs else act)
    handling = pick(ws.get('handling') or '')
    if not handling or DEGRADED.match(handling):
        handling = ''
        if ev:
            handling = 'The watch ' + pick(ev[0][2])[0].lower() + pick(ev[0][2])[1:]
    if not handling and len(rs) > 1:
        handling = pick(rs[1])
    if not handling:
        return None, 'no procedural source for Handling'
    withdrawal = pick(ws.get('withdrawal') or res)
    if DEGRADED.match(withdrawal) and res:
        withdrawal = pick(res)

    for name, v in (('approach', approach), ('handling', handling),
                    ('withdrawal', withdrawal), ('refusal', refusal)):
        if not v or v == '.':
            return None, 'missing ' + name

    lead = lead_sentence(mode)
    sec = ('## Handling Process\n\n'
           '> **This holding is not worked.** %s. What follows is procedure; '
           'nothing in it answers an approach.\n\n'
           '| Stage | What is done |\n|---|---|\n'
           '| **Approach** | %s |\n'
           '| **Handling** | %s |\n'
           '| **Withdrawal** | %s |\n'
           '| **Refusal** | %s |\n'
           % (lead, approach, handling, withdrawal, refusal))
    new = t[:bm.start()] + sec + t[bm.end():]

    if re.search(r'^\|\s*\*\*Handling\*\*\s*\|', new, re.M):
        new = re.sub(r'^\|\s*\*\*Valid Work Types\*\*\s*\|.*\n', '', new, count=1, flags=re.M)
        if '## Handling Process' not in re.search(r'^\|\s*\*\*Handling\*\*\s*\|.*$', new, re.M).group(0):
            new = re.sub(r'^(\|\s*\*\*Handling\*\*\s*\|[^\n]*?)\s*\|$',
                         lambda m: m.group(1) + POINTER + ' |', new, count=1, flags=re.M)
    else:
        new = re.sub(r'^\|\s*\*\*Valid Work Types\*\*\s*\|.*$',
                     '| **Handling** | No Work Type (`R-40`) — the four stages below are the whole of the contact |',
                     new, count=1, flags=re.M)

    if re.search(r'^## Behavior\s*$', new, re.M) or '**Valid Work Types**' in new:
        return None, 'replace failed'
    return new, 'ok'


def main(argv):
    limit = int(argv[1]) if len(argv) > 1 else 5
    _, hits, _ = g.measure()
    done, fails = 0, []
    for p, _bad in hits[:limit]:
        out, st = build(p)
        if st != 'ok':
            fails.append((p.split('/')[-1][:46], st))
            continue
        io.open(p, 'w', encoding='utf-8').write(out)
        done += 1
    print('converted %d · skipped %d' % (done, len(fails)))
    for f in fails:
        print('  skipped', f[0], '—', f[1])


if __name__ == '__main__':
    main(sys.argv)


def build_legacy(p):
    """Second pass for the nine relics that predate Watch Sequence and Contact
    Events: their **Recommended response** is the procedure, in one breath."""
    t = io.open(p, encoding='utf-8').read()
    bm = re.search(r'^## Behavior\n(.*?)(?=\n## )', t, re.M | re.S)
    if not bm:
        return None, 'no ## Behavior'
    rec, res = field(t, 'Recommended response'), field(t, 'Resolution Condition')
    mode, act, oldhand = field(t, 'Mode of presence'), field(t, 'Activation threshold'), field(t, 'Handling')
    if not rec:
        return None, 'no Recommended response'
    parts = [x for x in sentences(rec)]
    keep = [x for x in parts if 'Work Type' not in x and not re.match(r'^(the observer|the stander and|Viderehan)', x)]
    handling = pick(' '.join(keep) if keep else rec)
    guard = ''
    for x in parts:
        if re.search(r'\b(never|nobody|do not|does not|is not|no )\b', x, re.I):
            guard = pick(x)
            break
    approach = pick('Before approach, know what meets you: ' + act) if act else pick(mode)
    if not approach:
        return None, 'no approach source'
    refusal = pick(oldhand) or guard or pick(rule_reason(t))
    if not refusal:
        return None, 'no refusal source'
    lead = lead_sentence(mode)
    sec = ('## Handling Process\n\n'
           '> **This holding is not worked.** %s. What follows is procedure; '
           'nothing in it answers an approach.\n\n'
           '| Stage | What is done |\n|---|---|\n'
           '| **Approach** | %s |\n| **Handling** | %s |\n'
           '| **Withdrawal** | %s |\n| **Refusal** | %s |\n'
           % (lead, approach, handling, pick(res) or 'The watch ends when the resolution condition is met.',
              refusal))
    new = t[:bm.start()] + sec + t[bm.end():]
    if re.search(r'^\|\s*\*\*Handling\*\*\s*\|', new, re.M):
        new = re.sub(r'^\|\s*\*\*Valid Work Types\*\*\s*\|.*\n', '', new, count=1, flags=re.M)
    else:
        new = re.sub(r'^\|\s*\*\*Valid Work Types\*\*\s*\|.*$',
                     '| **Handling** | No Work Type (`R-40`) — the four stages below are the whole of the contact |',
                     new, count=1, flags=re.M)
    if re.search(r'^## Behavior\s*$', new, re.M) or '**Valid Work Types**' in new:
        return None, 'replace failed'
    return new, 'ok'
