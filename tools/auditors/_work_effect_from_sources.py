"""Assign the three work outcomes (R-49) across the worked subjects.

    Damage 101   Neutral 39   Gift 15        (155 subjects; 3 termini have no loop)

Gift is hand-picked: the fifteen holdings whose own record already pays something
out. Neutral takes the quietest readings — the smallest bands left after the
gifts. Damage is everyone else, and their rows are not rewritten.

    python3 tools/auditors/_work_effect_from_sources.py --dry
    python3 tools/auditors/_work_effect_from_sources.py --write
"""
import glob
import io
import re
import sys

N_NEUTRAL = 39

GIFTS = {
    '071b_Blessing_Giver': (
        'the blessing is given and the room is left exactly as it was',
        '+5–10 Composure for the rest of the cycle — she does not wait to be asked, and what she '
        'blesses is drawn out of a memory the worker cannot choose'),
    '071_The_Kind_Healer': (
        'it treats what it finds and leaves the room untouched',
        '+5–10 Resilience for the rest of the cycle — the injuries are real, including the ones '
        'nobody reported, and the memory it works from is taken out of the worker'),
    '280_Kind_Healer': (
        'it gives ground to the worker and never escalates',
        '+5–10 Composure for the rest of the cycle — it withdraws rather than escalates, and the '
        'ground it gives up is the worker\'s to stand on afterwards'),
    '897_Welcome_Haven': (
        'the walls come down and the room is survivable',
        '+5–10 Resilience for the rest of the cycle — the flames lower and the broken pieces become '
        'visible, and the debt for the shelter is entered against the worker\'s name'),
    '844_Repose': (
        'the rubble settles and the figure sleeps deeper',
        '+5–10 Composure for the rest of the cycle — the sleep is deeper and steadier, and it takes '
        'a memory down with it each time it is entered'),
    '869_Homecoming_Tree': (
        'the ground under it stays where it is',
        '+5–10 Composure for the rest of the cycle — it returns the worker to somewhere they have '
        'been before, and the record cannot say where it took them from'),
    '000_Kind_Echo': (
        'the lesson is taught and the chamber is left as it was',
        '+5–10 Composure for the rest of the cycle — this is the training entity and the gentleness '
        'is genuine, and every lesson is paid for out of the worker\'s own recollection of learning it'),
    '796_Spire_of_Unanswered': (
        'the song lowers and nothing descends',
        '+5–10 Composure for the rest of the cycle — the warmth gentles and the settlement holds, '
        'and the prayer it answers is never quite the one that was made'),
    '301_Feu_Follet': (
        'the flame steadies and the melting stops',
        '+5–10 Resilience for the rest of the cycle — it restores nothing, and the fire that saved '
        'the tree is drawn out of the worker\'s memory of it'),
    '895_Survivors': (
        'the Sigh settles and quiets for a time',
        '+5–10 Composure for the rest of the cycle — it resolves nothing, and what it lends it takes '
        'back at the end of the cycle without naming an interest rate'),
    '033_The_Guarding_Bird': (
        'it stands where it has always stood and moves for nobody',
        '+5–10 Resilience for the rest of the cycle — it puts itself between the worker and the '
        'other two, and the position is lent rather than given'),
    '448_Floating_Well': (
        'the well hangs where nothing holds it and the floor takes no weight',
        '+5–10 Resilience for the rest of the cycle — water out of a shaft that opens into nothing, '
        'and the drawing is entered against the worker\'s name'),
    '973_Yggdrasil': (
        'the split closes a little and the roots come into view',
        '+5–10 Resilience for the rest of the cycle — the two halves do not rejoin, and the loan is '
        'taken back when the cycle ends'),
    '101_Emberling': (
        'the embers neither go out nor spread',
        '+5–10 Composure for the rest of the cycle — they warm without spreading, and the memory '
        'they are fed from is one the worker will not be able to check'),
    '247_The_Undelivered_Thanks': (
        'a thanks is finally delivered and the satchel is lighter for it',
        '+5–10 Composure for the rest of the cycle — the stone it was carried in is gone for good, '
        'and the weight is never returned'),
}


def subjects():
    out = []
    for p in sorted(glob.glob('SOMNARAK-WORLD/**/SE-*.md', recursive=True)):
        if 'MAW_Codex' in p:
            continue
        t = io.open(p, encoding='utf-8').read()
        if 'Subject' not in (re.search(r'\*\*Entity Type\*\*\s*\|\s*([^|\n]+)', t) or [None, ''])[1]:
            continue
        sec = re.search(r'^## Operational Parameters\s*$(.*?)(?=^## |\Z)', t, re.M | re.S)
        m = re.search(r'^\|\s*\*\*Work Damage\*\*\s*\|([^|\n]*)\|', sec.group(1) if sec else t, re.M)
        if not m:
            continue
        b = re.match(r'(\d+)\s*[–-]\s*(\d+)', m.group(1).strip())
        if not b:
            continue
        el = re.search(r'^\|\s*\*\*Element\*\*\s*\|\s*([A-Za-z ]+)', t, re.M)
        elem = el.group(1).strip() if el else 'Grudge'
        elem = elem if elem in ('Lament', 'Grudge', 'Void', 'Weight') else 'Lament'
        out.append(dict(path=p, text=t, row=m.group(0), value=m.group(1).strip(),
                        lo=int(b.group(1)), hi=int(b.group(2)), element=elem))
    return out


def assign():
    subs = subjects()
    gift = [d for d in subs if any(k in d['path'] for k in GIFTS)]
    gset = {d['path'] for d in gift}
    rest = [d for d in subs if d['path'] not in gset]
    neutral = sorted(rest, key=lambda d: (d['lo'] + d['hi'], d['path']))[:N_NEUTRAL]
    nset = {d['path'] for d in neutral}
    for d in subs:
        d['verdict'] = 'gift' if d['path'] in gset else ('neutral' if d['path'] in nset else 'damage')
    return subs, [d for d in subs if d['verdict'] == 'neutral'], gift


def key_of(d):
    for k in GIFTS:
        if k in d['path']:
            return k
    return None


def build(d):
    if d['verdict'] == 'damage':
        return d['text']
    if d['verdict'] == 'neutral':
        new = ('| **Work Damage** | None — the %s it draws is spent in the chamber and not carried '
               'out; the worker leaves with what they brought in. |' % d['element'])
        return d['text'].replace(d['row'], new, 1)
    room, gift = GIFTS[key_of(d)]
    new = ('| **Work Damage** | None — %s. |\n| **Work Gift** | %s. |' % (room, gift))
    return d['text'].replace(d['row'], new, 1)


def main(argv):
    subs, neutral, gift = assign()
    counts = {v: sum(1 for d in subs if d['verdict'] == v) for v in ('damage', 'neutral', 'gift')}
    print('subjects in scope %d · damage %d · neutral %d · gift %d'
          % (len(subs), counts['damage'], counts['neutral'], counts['gift']))
    if '--dry' in argv:
        for d in (neutral[:2] + gift[:2]):
            print('\n--', d['verdict'].upper(), d['path'].split('/')[-1][:44])
            for line in build(d).split('\n'):
                if '**Work Damage**' in line or '**Work Gift**' in line:
                    print('   ', line[:200])
    if '--write' in argv:
        for d in subs:
            if d['verdict'] != 'damage':
                io.open(d['path'], 'w', encoding='utf-8').write(build(d))
        print('written %d' % (counts['neutral'] + counts['gift']))


if __name__ == '__main__':
    main(sys.argv)
