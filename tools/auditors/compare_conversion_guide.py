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
import glob
import importlib.util
import io
import re
import sys

GUIDE = 'PROJECT_MOON_RESEARCH/CROSS_VERSE/PM_ABNORMALITY_TO_PS_SORROW_ENTITY_CONVERSION_GUIDE.md'


def read(path):
    with io.open(path, encoding='utf-8') as fh:
        return fh.read()


CHECKS = []


def _measure_stock():
    """Count, from the archive, records off their grade ceiling and records with a
    figure but no grade. Imported from the auditor that owns R-37 so the two cannot
    drift apart."""
    spec = importlib.util.spec_from_file_location('csc', 'tools/auditors/check_stock_ceiling.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    off = un = 0
    for path in sorted(glob.glob(mod.WORLD, recursive=True)):
        text = io.open(path, encoding='utf-8').read()
        val, _ = mod.figure(text)
        if val is None:
            continue
        g = mod.grade(text)
        if not g:
            un += 1
        elif mod.CEIL[g] != val:
            off += 1
    return off, un


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
    # (superseded by section 19's 'void percentage pressure' check, which also compares the Ordeals page)

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
    # 9b — the ceiling law is measured, not asserted. Cleared 2026-11-02: 87 records
    # filed a figure and no grade, so no ceiling could be measured for them while the
    # auditor's report still read "0 off their grade ceiling". Both halves are live
    # measurements here — never a count written into the check, which is how the
    # comprehension split survived wrong for as long as it did.
    _ceil, _un = _measure_stock()
    ck('every item record is measurable', _un == 0, f'{_un} record(s) file a figure and no grade')
    ck('every item record sits at its grade ceiling', _ceil == 0, f'{_ceil} record(s) off ceiling')
    ck('guide says the gap is closed, not open',
       'Every record can now be checked against this rule' in g
       and 'Eighty-eight records cannot be checked' not in g)

    # 10 — codes resolve to files
    for code, path in [
        ('C-IVω-001', 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVω-001_The_Maw_구라.md'),
        ('C-Vω-001', 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-Vω-001_Dawn_of_Mourning_애도의_새벽.md'),
        ('C-IIγ-071c', 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIγ-071c_Apostle_Maker_사도_만드는_자.md'),
        ('C-Iβ-071b', 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iβ-071b_Blessing_Giver_축복_주는_자.md'),
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
    shroud = read('SOMNARAK-WORLD/MAW_Codex_Sets/Registry_061_to_073/071_Kind_Healer/SE-071-C__MAW-S_The_Gentle_Shroud.md')
    ck('X.3 suit resistances live on the Kind Healer shroud',
       'Lament | 0.4' in shroud and 'Void | 1.6' in shroud
       and 'Lament 0.4' in g and 'Void 1.6' in g)
    ck('X.3 dawn carries no suit of its own', 'Lament: 0.4' not in dawn)
    ck('X.3 no invented organs', not any(x in g for x in
                                         ['Beak of Hunger', 'Scales of Debt', 'Blind Lamp',
                                          'Twilight of Mugenhan']))
    mag = read('SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIβ-319_The_Magistrates_Strike-Through_판관의_취소선.md')
    ck('X.4 A-Relic single-use', 'A-Relic (Arcanum)' in mag and 'A-Relic' in g)

    # 13 — the Universal Table (the both-direction authority) carries the same laws
    uni = read('PROJECT_MOON_RESEARCH/CROSS_VERSE/PS_SORROW_ENTITY_IN_L_CORP_CONTAINMENT_GUIDE.md')
    for ko, latin in [('비데레한', 'Viderehan'), ('페레한', 'Ferrehan'),
                      ('플레레한', 'Flerehan'), ('푸그나한', 'Pugnahan')]:
        ck(f'universal: work {latin} filed spelling', f'{latin} ({ko}' in uni)
    ck('universal: no translation pair beside a Latin name',
       not any(x in uni for x in ['(관조한 / *Gwanjohan*', '(인내한 / *Innaehan*',
                                   '(통곡한 / *Tonggokhan*', '(격투한 / *Gyeoktuhan*']))
    for band, ap in [('2–3', 2), ('4–5', 3), ('6–7', 4)]:
        ck(f'universal: AP {band} -> {ap}', f'Speed {band} · {ap} AP' in uni)
    ap_rows = re.findall(r'^\|\s*Speed ([0-9]+)[–+]([0-9]*) · ([0-9]+)\+? AP', uni, re.M)
    ck('universal: AP rows parsed', len(ap_rows) >= 3, f'{len(ap_rows)} rows')
    ck('universal: no AP above four',
       all(int(ap) <= 4 for _, _, ap in ap_rows),
       str([r for r in ap_rows if int(r[2]) > 4]))
    ck('universal: no band starting below Speed 2',
       all(int(lo) >= 2 for lo, _, _ in ap_rows),
       str([r for r in ap_rows if int(r[0]) < 2]))
    ck('universal: four pillars named', 'Passives, Panic, Parry & Protection, and Posture' in uni)
    ck('universal: stock ceiling', 'supports up to five' in uni or 'five is the ceiling' in uni.lower())
    ck('universal: four decrements', all(x in uni for x in
                                         ['**Dissolution**', '**Missing**', '**Broken**', '**100% inheritance**']))
    ck('universal: fusion not a decrement', 'Fusion is not a fifth event' in uni)
    ck('universal: stigma two figures', 'Acquisition Probability' in uni and 'Maximum Amount' in uni)

    # 14 — the comparison twin and the summary stub carry the same vocabulary
    twin = read('PROJECT_MOON_RESEARCH/CROSS_VERSE/COMPLETE_SYSTEM_COMPARISON_SOMNARAK_VS_LOBOTOMY_CORPORATION.md')
    ck('twin: no false badge-count claim',
       not re.search(r'identical capability badges in all', twin)
       and 'Dossier-specific warning banners' in twin)
    ck('twin: no translation pair beside a Latin name',
       not re.search(r'Viderehan \(\s*관조한', twin))
    ck('twin: triad ceiling stated', 'supports up to **five pieces of each kind**' in twin)
    stub = read('PROJECT_MOON_RESEARCH/CROSS_VERSE/COMPLETE SYSTEM COMPARISON-SOMNARAK vs. Lobotomy Corporation.md')
    ck('stub: Somnarak accessory is a Stigma', 'M.A.W. Stigma' in stub)
    ck('stub: no M.A.W. Gift row', 'M.A.W. Gift' not in stub)

    # 15 — the risk-level vocabulary lives in the guides, never on a dossier
    import glob as _glob
    dossiers = _glob.glob('SOMNARAK-WORLD/Sorrow_Entities/SE-*.md')
    levels = ('ZAYIN', 'TETH', 'HE', 'WAW', 'ALEPH')
    with_level = [p for p in dossiers
                  if any(re.search(rf'\b{lv}\b', read(p)) for lv in levels)]
    ck('no dossier files a risk level', not with_level,
       f'{len(with_level)} file(s): {[p.split("/")[-1][:26] for p in with_level][:3]}')
    graded = sum(1 for p in dossiers
                 if re.search(r'\*\*Risk tier\*\*\s*\|\s*(Minor|Moderate|Major|Critical|Catastrophic)', read(p)))
    ck('every dossier grades its risk tier', graded == len(dossiers), f'{graded}/{len(dossiers)}')
    ck('guide states the two vocabularies', 'Two vocabularies, and only one of them is on the dossier' in g)
    ck('guide does not claim a dossier files ALEPH', 'files ALEPH' not in g)

    # 16 — the vocabulary policy describes the world's words, not an earlier draft
    pol = read('PROJECT_MOON_RESEARCH/CROSS_VERSE/PM_VOCAB_POLICY.md')
    ck('policy: MAW is Wear', 'Materialized Agony Wear' in pol)
    ck('policy: MAW not asserted as Weaponry',
       not re.search(r'E\.G\.O\*\*\s*\|\s*\*\*M\.A\.W\. \(Materialized Agony Weaponry\)', pol))
    ck('policy: Sorrow Entity Korean is 한조각', '한조각' in pol)
    ck('policy: 비탄체 retired', '비탄체' not in pol)
    ck('policy: Memory Leaf is the wing term', 'Memory Leaf' in pol)
    ck('policy: no invented equivalents asserted',
       all(f'(no filed native equivalent)' in pol for _ in range(3))
       and pol.count('(no filed native equivalent)') >= 3)
    ck('policy: dead 06 path named as dead', 'does not exist' in pol)

    # 17 — the world facts those policy rows rest on
    mem = read('SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_MEMORY_ARCHIVE.md')
    ck('world: Memory Leaf is the artifact', mem.count('Memory Leaf') >= 10 and 'Key Page' not in mem)
    ck('world: Key Page is used nowhere', not any(
        'Key Page' in read(p) for p in _glob.glob('SOMNARAK-WORLD/**/*.md', recursive=True)))
    codex_lex = read('SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/PROJECT_SOMNARAK.md')
    ck('world: codex glosses Sorrow Entity 한조각', '**Sorrow Entity** (한조각)' in codex_lex)
    ck('world: Stratum Realization is filed', 'Stratum Realization' in codex_lex
       or any('Stratum Realization' in read(p) for p in _glob.glob('SOMNARAK-WORLD/Master_Codices/02*/*.md')))

    # 18 — the reverse multipliers are the Risk Parallel's, inverted exactly
    rrp = read('PROJECT_MOON_RESEARCH/CROSS_VERSE/SOMNARAK_LCORP_RD_RISK_PARALLEL.md')
    for tier, mult in [('ZAYIN', '0.4'), ('TETH', '1.0'), ('HE', '1.8'), ('WAW', '9'), ('ALEPH', '19')]:
        ck(f'RRP HP multiplier {tier} ×{mult}', f'| {tier} | ×{mult} |' in rrp)
        ck(f'guide HP multiplier {tier} ×{mult}', f'**×{mult}** {tier}' in g)
    for tier, rng in [('ZAYIN', '0.8–1.2'), ('TETH', '1.3–1.5'), ('HE', '1.4–1.8'),
                      ('WAW', '1.2–2.0'), ('ALEPH', '0.8–1.3')]:
        ck(f'RRP ATK multiplier {tier} ×{rng}', f'| {tier} | ×{rng} |' in rrp)
        ck(f'guide ATK multiplier {tier} ×{rng}', f'**×{rng}** {tier}' in g)
    ck('RRP worked example 999 -> 8,991 WAW', '8,991' in rrp)
    ck('RRP worked example 999 -> 18,981 ALEPH', '18,981' in rrp)
    ck('guide rounds up not down', 'ceil' in g)

    # 19 — the resistance ladder: one value, one band word, and the guide says so
    _LADDER = {'0.3': 'Resistant', '0.4': 'Resistant', '0.5': 'Warded', '0.6': 'Warded',
               '0.7': 'Warded', '0.8': 'Warded', '0.9': 'Normal', '1.0': 'Normal',
               '1.1': 'Weak', '1.2': 'Weak', '1.3': 'Weak', '1.4': 'Weak',
               '1.5': 'Weak', '1.6': 'Weak', '1.8': 'Weak'}
    seen = {}
    orphan = []
    for path in _glob.glob('SOMNARAK-WORLD/**/*.md', recursive=True):
        txt = read(path)
        if '**Resistances:**' not in txt:
            continue
        for blk in re.findall(r'\*\*Resistances:\*\*(.{0,300})', txt, re.S):
            for m in re.finditer(r'-\s*(Lament|Grudge|Void|Weight|Hope)\s*:\s*([0-9.]+)\s*\(([^)]+)\)', blk):
                val, word = m.group(2), m.group(3)
                seen.setdefault(val, set()).add(word)
                want = _LADDER.get(f'{float(val):.1f}')
                if want != word:
                    orphan.append(f'{val} ({word})')
    ck('resistance ladder is uniform across the archive',
       not orphan, (f'{len(orphan)} off-ladder, e.g. {orphan[:3]}') if orphan else '')
    ck('guide prints the whole resistance ladder',
       all(f'| {v} | **{w}** |' in g for v, w in _LADDER.items()))
    elem_tbl = g.split('## Section V')[1].split('## Section VI')[0]
    elem_tbl = elem_tbl.split('| PM damage')[1].split('\n\n')[0]
    ck('element table cites only engine effects',
       not any(x in elem_tbl for x in ['Structural Break', 'Burden Stacks',
                                       'Acoustic Despair', 'Numbness']),
       'the four invented status names must not appear as live table cells')
    ck('element table carries the engine wording',
       all(x in elem_tbl for x in ['Resentment, iron, verdict', 'Grief, water, sound',
                                   'Burden, debt, mass', 'Erasure, isolation, cold']))
    ck('void percentage pressure stated as the codex files it',
       '1 unit = 5% Max HP' in codex and '1 unit = 5% Max HP' in g and
       '5% of maximum vital endurance' in g)

    # 20 — the capability badges are the comparison layer's vocabulary, never a filed field
    _BADGE = ['Can Benefit Facility', 'Capable of Alteration', 'Capable of Instadeath',
              'Can Benefit the Facility', 'Capable of Employee Alteration', 'Facility Buff']
    badge_hits = [p for p in _glob.glob('SOMNARAK-WORLD/**/*.md', recursive=True)
                  if any(b in read(p) for b in _BADGE)]
    ck('no badge string anywhere in the world', not badge_hits,
       f'{len(badge_hits)} files, e.g. {badge_hits[:2]}' if badge_hits else '0 files')
    ck('guide states the archive files no badge',
       '0' in g and 'of 290 Sorrow Entity dossiers' in g and 'any of those six strings' in g)
    ck('guide no longer claims every relic carries badges',
       'Every converted relic carries the canonical badges' not in g)
    ck('guide calls the badges a mapping vocabulary',
       'mapping vocabulary, not a filing obligation' in g)
    ck('badges legitimately survive on the L Corp side',
       'Can Benefit Facility' in read('PROJECT_MOON_RESEARCH/CROSS_VERSE/PS_SORROW_ENTITY_IN_L_CORP_CONTAINMENT_GUIDE.md'))

    # 21 — the Hope record class: fourteen files, and the designations that exist
    _ht = [p for p in _glob.glob('SOMNARAK-WORLD/Hope_Transformations/HT-*.md')]
    ck('fourteen Hope Transformation records', len(_ht) == 14, f'{len(_ht)} files')
    ck('guide lists the two Sovereign-tier HT designations',
       'HT-V-HC-001' in g and 'HT-V-HH-001' in g)
    ck('guide does not cite HT-013 or HT-014',
       'HT-013' not in g and 'HT-014' not in g,
       'HT-013/HT-014 do not exist; numbering stops at HT-012')

    # 22 — the comprehension ladder is the codex's, five gates, and the guide admits the split
    codex5 = read('SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_CODEX.md')
    _GATES = [('1', 'Trace'), ('2', 'Basic'), ('3', 'Advanced'), ('4', 'Deep'), ('5', 'Sovereign')]
    ck('codex files five comprehension gates',
       all(f'| **{n}** | {g} |' in codex5 for n, g in _GATES))
    ck('guide carries the same five gates',
       all(f'| **{num}** | **{name}** |' in g for num, name in _GATES))
    ck('guide no longer claims the dossiers file one ladder',
       'the pairing is the same one the dossiers file' not in g)
    # Measure the level-4 split rather than fingerprint it. The previous version of
    # this check asserted the strings "`Mastered` in 49" and "`Deep` in 27" were
    # present, which pinned a wrong count in place: 49 and 27 were occurrence counts
    # across a dossier's four mentions of the field, not the number of files. A check
    # that hard-codes a measurement stops being a check the moment the measurement
    # was wrong to begin with.
    import collections as _c
    _lvl4 = _c.Counter()
    for _p in _glob.glob('SOMNARAK-WORLD/Sorrow_Entities/*.md'):
        if _p.endswith('README.md'):
            continue
        _m = re.search(r'R\.D\. Comprehension Level\*{0,2}\s*\|\s*4\s*—\s*([A-Za-z]+)', read(_p))
        if _m:
            _lvl4[_m.group(1)] += 1
    ck('guide records the level-4 split as measured',
       bool(_lvl4) and all(f'`{w}` {n}' in g for w, n in _lvl4.items()))
    ck('guide records the directorate 0-4 third ladder',
       'Unknown, Observed, Studied, Understood, Mastered' in g)

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
