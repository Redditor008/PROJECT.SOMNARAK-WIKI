#!/usr/bin/env python3
"""compare_conversion_guide.py — check the Conversion Guide against the archive.

Every value the guide asserts is compared with the file that owns it: the band
table against the linter that enforces it, the AP ladder against the combat
engine's resolution layer, the four pillars against the tactical template, the
work names against the world codex, the colours against the Ordeals register,
and the two resolving case studies against their own dossiers.

The point is not that the guide is internally tidy — it has always been that.
The point is that it says the same thing as the world.

    python3 tools/auditors/compare_conversion_guide.py          # audit
    python3 tools/auditors/compare_conversion_guide.py -v       # list every check
"""
import importlib.util
import io
import re
import sys

GUIDE = 'PROJECT_MOON_RESEARCH/CROSS_VERSE/PM_ABNORMALITY_TO_PS_SORROW_ENTITY_CONVERSION_GUIDE.md'


def read(path):
    with io.open(path, encoding='utf-8') as fh:
        return fh.read()


CHECKS = []


def ck(name, cond, detail=''):
    CHECKS.append((name, bool(cond), detail))


def load_bands():
    spec = importlib.util.spec_from_file_location('csb', 'tools/check_stat_bands.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.BANDS


def fmt(n):
    return f'{n:,}' if n >= 1000 else str(n)


def main():
    g = read(GUIDE)

    # 1 — the band table is the linter's own table
    for tier, (hf, hc, af, ac) in load_bands().items():
        row = re.search(rf'\| \*\*{tier}\*\* \| [^|]+ \| [^|]+ \| ([^|]+) \| ([^|]+) \|', g)
        if not row:
            ck(f'{tier} row present', False)
            continue
        hp, atk = row.group(1).strip(), row.group(2).strip()
        ck(f'{tier} HP band', hp in (f'{fmt(hf)}–{fmt(hc)}', f'{fmt(hf)}-{fmt(hc)}'), hp)
        ck(f'{tier} ATK band', atk.startswith(f'{af:02d}'), atk)

    # 2 — the AP ladder is the engine's resolution layer
    eng = read('SOMNARAK-WORLD/Tactical_Combat_Engine/ACTION_DICE_AND_CLASH_RULES.md')
    for band, ap, label in [('2–3', 2, '2-3'), ('4–5', 3, '4-5'), ('6–7', 4, '6-7')]:
        ck(f'AP {label} -> {ap}', f'| {band} | {ap} AP |' in eng and f'**{band}** | {ap}' in g)
    iv1 = g.split('### IV.1')[1].split('### IV.1a')[0]
    ck('no fifth AP band', '| 5 |' not in iv1)

    # 3 — the four pillars are the template's four pillars
    tpl = read('TEMPLATES/GAME/18_TACTICAL_COMBAT_ENGINE_TEMPLATE.md')
    ck('template pillar order', 'Passives (P1), Panic (P2), Parry (P3), Posture (P4)' in tpl)
    ck('guide pillar order', all(x in g for x in
                                 ['P1 — Passives', 'P2 — Panic', 'P3 — Parry', 'P4 — Posture']))

    # 4 — work names are the world codex's spellings
    world = read('SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/PROJECT_SOMNARAK.md')
    for ko, latin in [('비데레한', 'Viderehan'), ('페레한', 'Ferrehan'),
                      ('플레레한', 'Flerehan'), ('푸그나한', 'Pugnahan')]:
        ck(f'work {latin}', f'{latin} ({ko})' in world and ko in g)

    # 5 — elements: four, plus Mixed as a filing, plus Hope as a vector
    codex = read('SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_CODEX.md')
    ck('Mixed is a filing', '**Mixed**' in codex and '`Mixed`' in g)
    ck('Hope is a vector', 'Hope | Dawn-grade' in eng and '**Hope**' in g)
    ck('Void 1 unit = 5%', '1 unit = 5% Max HP' in codex and '1 unit = 5% max HP' in g)

    # 6 — the four watches and the five colours
    ordeals = read('SOMNARAK-WORLD/Ordeals/README.md')
    for col in ['BLUE', 'GREY', 'OBSIDIAN', 'ASHEN', 'PURPLE']:
        ck(f'colour {col}', f'**{col} ' in ordeals and f'**{col}**' in g)
    ck('four watch names', all(x in g for x in ['제1감시', '제2감시', '제3감시', '만조감시']))

    # 7 — relic classes are the codex's use classes
    maw = read('SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md')
    ck('A/O/I use classes', all(x in maw for x in
                                ['A-Relic / Arcanum', 'O-Relic / Offertorium', 'I-Relic / Indumentum'])
       and all(x in g for x in ['A-Relic', 'O-Relic', 'I-Relic']))

    # 8 — the five comprehension gates, named
    ck('comprehension gates', all(x in codex for x in ['Trace', 'Basic', 'Advanced', 'Deep', 'Sovereign'])
       and all(f'**{x}**' in g for x in ['Trace', 'Basic', 'Advanced', 'Deep', 'Sovereign']))

    # 9 — the stock law
    ck('ceiling five', 'supports up to five of each kind' in g)
    ck('four decrements', all(x in g for x in
                              ['**Dissolution**', '**Missing**', '**Broken**', '**100% inheritance**']))
    ck('five band words', all(x in g for x in
                              ['**Held**', '**Limited**', '**Standard**', '**Stocked**', '**Abundant**']))

    # 10 — codes resolve to files
    for code, path in [
        ('C-IVω-001', 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVω-001_The_Maw_구라.md'),
        ('C-Vω-001', 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-Vω-001_Dawn_of_Mourning_애도의_새벽.md'),
        ('C-IIγ-071c', 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-071c_Apostle_Maker_사도_만드는_자.md'),
        ('C-Iβ-071b', 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-071b_Blessing_Giver_축복_주는_자.md'),
    ]:
        ck(f'code {code}', code in read(path) and code in g)

    # 11 — material classes are the comparison codex's five, with no invented Hangul
    canonical = read('CANON/COMPLETE_SYSTEM_COMPARISON_SOMNARAK_VS_LOBOTOMY_CORPORATION.md')
    ck('five material classes', all(x in canonical for x in
                                    ['Primal Marrow', 'Tempered Brass', 'Resonant Alloy',
                                     'Woven Thread', 'Void Glass']))
    ck('no invented class Hangul', not any(k in g for k in
                                           ['골수형', '단조황동', '공명합금', '직조사', '공허유리']))

    # 12 — the two resolving case studies, against their dossiers
    dawn = read('SOMNARAK-WORLD/Sorrow_Entities/SE-C-Vω-001_Dawn_of_Mourning_애도의_새벽.md')
    ck('X.3 gauge 12,000', '12,000/12,000' in dawn and '12,000/12,000' in g)
    ck('X.3 suit resistances', 'Lament: 0.4' in dawn and 'Lament 0.4' in g and 'Void 1.6' in g)
    ck('X.3 no invented organs', not any(x in g for x in
                                         ['Beak of Hunger', 'Scales of Debt', 'Blind Lamp',
                                          'Twilight of Mugenhan']))
    mag = read('SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIβ-319_The_Magistrates_Strike-Through_판관의_취소선.md')
    ck('X.4 A-Relic single-use', 'A-Relic (Arcanum)' in mag and 'A-Relic' in g)

    verbose = '-v' in sys.argv or '--verbose' in sys.argv
    bad = [c for c in CHECKS if not c[1]]
    if verbose:
        for name, passed, detail in CHECKS:
            print(('  ok   ' if passed else '  FAIL ') + name + (f'  [{detail}]' if detail else ''))
    print(f'CONVERSION GUIDE vs ARCHIVE — {len(CHECKS)} checks · '
          f'{len(CHECKS) - len(bad)} pass · {len(bad)} fail')
    for name, _, detail in bad:
        print(f'  FAIL {name}' + (f' — {detail}' if detail else ''))
    print('RESULT:', 'PASS' if not bad else 'FAIL')
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
