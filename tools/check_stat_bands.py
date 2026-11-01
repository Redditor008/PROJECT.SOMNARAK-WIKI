#!/usr/bin/env python3
"""check_stat_bands.py - every Sorrow Entity's filed stat line must sit inside its risk tier.

The bands are not invented here. They are Section III of the Conversion Guide
(`PROJECT_MOON_RESEARCH/CROSS_VERSE/PM_ABNORMALITY_TO_PS_SORROW_ENTITY_CONVERSION_GUIDE.md`,
"Statistical conversion matrix"), read across as the dossier input check:

    ZAYIN  150-300     HP   06-14   ATK
    TETH   300-500          12-22
    HE     500-750          18-35
    WAW    750-1,000        30-55
    ALEPH  1,000-12,000     50-80

Tier is filed by score, not by the diagonal: Coherence rank (I=1 ... V=5) + Potency grade
(alpha=1 ... omega=5), 2-3 ZAYIN / 4-5 TETH / 6 HE / 7-8 WAW / 9-10 ALEPH.

What fails
  * a dossier with no `Sorrow Gauge [HP]` row at all;
  * a `## Combat Record` dossier with no `Han Pressure [ATK]` row;
  * a `## Contact Record` dossier (R-36: a fixed thing that never strikes) that still files an
    attack row, or that has neither section shape;
  * an HP base below the tier floor;
  * an ATK range whose high end is below the tier floor (the whole range sits under the band).

What is reported but does not fail
  * an HP base above the tier ceiling, and an ATK range whose low end is under the floor but
    whose high end is not. Both are recorded precedents inside the archive - a body whose
    escalation crosses a seam, or a chain scaled to its parent line - and the owner's directive
    was one-directional: nothing is to sit *under* its risk level. Ceilings are printed one
    record at a time so a ruling can be made; straddling ranges are counted, and listed under
    --verbose. Nothing is silently rescaled.
  * the exempt record: Kind Echo `C-Iα-000 [LS]`, the non-standard entity the directive names.

  python3 tools/check_stat_bands.py              audit
  python3 tools/check_stat_bands.py --verbose    also list every straddling range
  python3 tools/check_stat_bands.py --strict     exit 1 on over-ceiling/straddling notes too
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RANK = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
GRADE = {'α': 1, 'β': 2, 'γ': 3, 'δ': 4, 'ω': 5}
BANDS = {
    'ZAYIN': (150, 300, 6, 14),
    'TETH': (300, 500, 12, 22),
    'HE': (500, 750, 18, 35),
    'WAW': (750, 1000, 30, 55),
    'ALEPH': (1000, 12000, 50, 80),
}
# The one record the owner exempted from the band check: a non-standard entity.
# Written as the dossier files it, in the body's Designation row.
EXEMPT = {'C-Iα-000'}


def tier_of(score):
    if score <= 3:
        return 'ZAYIN'
    if score <= 5:
        return 'TETH'
    if score == 6:
        return 'HE'
    if score <= 8:
        return 'WAW'
    return 'ALEPH'


def row(text, label):
    m = re.search(r'\*\*%s\*\*\s*\|([^\n]*)' % label, text)
    return m.group(1) if m else None


def numbers(cell):
    return [float(x) for x in re.findall(r'\d+(?:\.\d+)?', (cell or '').replace(',', ''))]


def main():
    strict = '--strict' in sys.argv
    verbose = '--verbose' in sys.argv
    paths = sorted(glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD', '*', 'SE-*.md')))
    missing, under, ceiling, straddle, exempted, tiers = [], [], [], [], [], {}

    for path in paths:
        text = open(path, encoding='utf-8').read()
        name = os.path.basename(path)
        designation = row(text, 'Designation') or ''
        code = re.sub(r'[`\[\]]', '', designation).split()[0] if designation.strip() else name

        coherence, potency = row(text, 'Coherence'), row(text, 'Potency')
        if not coherence or not potency:
            missing.append('%s: no Coherence/Potency row' % name)
            continue
        r = re.search(r'\b(I{1,3}|IV|V)\b', coherence)
        g = re.search(r'([αβγδω])', potency)
        if not r or not g:
            missing.append('%s: unreadable Coherence/Potency' % name)
            continue

        tier = tier_of(RANK[r.group(1)] + GRADE[g.group(1)])
        tiers[tier] = tiers.get(tier, 0) + 1
        contact = '## Contact Record' in text
        combat = '## Combat Record' in text
        hp_cell, atk_cell = row(text, r'Sorrow Gauge \[HP\]'), row(text, r'Han Pressure \[ATK\]')
        if hp_cell is None:
            missing.append('%s: no Sorrow Gauge [HP] row' % name)
            continue
        if not contact and not combat:
            missing.append('%s: neither a Combat Record nor a Contact Record' % name)
            continue
        if contact and atk_cell is not None:
            missing.append('%s: Contact Record still carries Han Pressure [ATK]' % name)
            continue
        if combat and atk_cell is None:
            missing.append('%s: Combat Record has no Han Pressure [ATK] row' % name)
            continue
        if code in EXEMPT:
            exempted.append('%s (%s, %s)' % (name, tier, hp_cell.strip()))
            continue

        hp_floor, hp_ceil, atk_floor, atk_ceil = BANDS[tier]
        hp, atk = numbers(hp_cell), numbers(atk_cell)
        if hp[0] < hp_floor:
            under.append('%s [%s] HP %s under floor %d' % (name, tier, hp_cell.strip(), hp_floor))
        elif hp[0] > hp_ceil:
            ceiling.append('%s [%s] HP %s over ceiling %d'
                           % (name, tier, hp_cell.strip(), hp_ceil))
        if not atk:
            continue
        if atk[-1] < atk_floor:
            under.append('%s [%s] ATK %s wholly under floor %d'
                         % (name, tier, atk_cell.strip(), atk_floor))
        elif atk[0] < atk_floor:
            straddle.append('%s [%s] ATK %s straddles floor %d'
                            % (name, tier, atk_cell.strip(), atk_floor))
        if atk[0] > atk_ceil:
            ceiling.append('%s [%s] ATK %s over ceiling %d'
                           % (name, tier, atk_cell.strip(), atk_ceil))

    print('STAT BAND AUDIT - %d dossiers - %s'
          % (len(paths), ' · '.join('%s %d' % (t, tiers[t]) for t in
                                    ('ZAYIN', 'TETH', 'HE', 'WAW', 'ALEPH') if t in tiers)))

    for line in missing:
        print('  MISSING FIELD  ' + line)
    for line in under:
        print('  UNDER BAND    ' + line)
    for line in ceiling:
        print('  OVER CEILING  ' + line)
    if verbose:
        for line in straddle:
            print('  STRADDLES     ' + line)
    elif straddle:
        print('  STRADDLES     %d range(s) start under the floor and end inside it '
              '(--verbose to list)' % len(straddle))
    for line in exempted:
        print('  EXEMPT        ' + line)

    print('RESULT: %d missing · %d under band · %d over ceiling · %d straddling · %d exempt'
          % (len(missing), len(under), len(ceiling), len(straddle), len(exempted)))
    if missing or under or (strict and (ceiling or straddle)):
        print('OVERALL STAT BANDS: FAIL')
        return 1
    print('OVERALL STAT BANDS: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
