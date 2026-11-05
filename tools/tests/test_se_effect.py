# -*- coding: utf-8 -*-
"""Gate 89 — some holdings have one thing they do (R-50)."""
import unittest

from tools.auditors import check_se_effect as gate

BASE = ('| **Entity Type** | **{etype}** |\n'
        '| **Activation threshold** | {act} |\n'
        '{row}\n')

BODY = ('the moss around the basin is alive in conditions that should have killed it, and the '
        'beds take the overflow')
GOOD = '| **SE Effect** | **On the counter** \u2014 %s. |' % BODY
SOURCE = '\n### Consequences\n\n- %s.\n' % BODY


def page(row=GOOD, etype='Object/Place \u2014 Non-breaching: expansion only',
         act='3 ignored conditions', source=SOURCE):
    return BASE.format(etype=etype, act=act, row=row) + source


class TheShape(unittest.TestCase):

    def test_a_well_formed_effect_passes(self):
        self.assertEqual(gate.problems(page()), [])

    def test_a_trigger_outside_the_six_fails(self):
        row = GOOD.replace('On the counter', 'On a whim')
        self.assertTrue(gate.problems(page(row)))

    def test_a_cell_with_no_trigger_fails(self):
        row = GOOD.replace('**On the counter** \u2014 ', '')
        self.assertTrue(gate.problems(page(row)))

    def test_a_short_effect_fails(self):
        row = '| **SE Effect** | **On the counter** \u2014 it moves. |'
        self.assertTrue(any('law, not a label' in b for b in gate.problems(page(row))))

    def test_a_percentage_fails(self):
        row = GOOD.replace('and the beds take the overflow', 'and the beds take 65% of the overflow')
        self.assertTrue(any('percentage' in b for b in gate.problems(page(row))))

    def test_a_dice_roll_fails(self):
        row = GOOD.replace('and the beds take the overflow', 'and roll a d6 for the overflow')
        self.assertTrue(any('dice roll' in b for b in gate.problems(page(row))))


class TheProvenance(unittest.TestCase):

    def test_an_effect_made_of_borrowed_words_fails(self):
        row = ('| **SE Effect** | **On the counter** \u2014 a wholly invented apparatus of '
               'calibrated instruments and liaison officers reports sideways. |')
        self.assertTrue(any('vocabulary' in b for b in gate.problems(page(row))))

    def test_a_work_type_name_in_a_relic_fails(self):
        row = ('| **SE Effect** | **On the counter** \u2014 Viderehan reads the moss and the beds '
               'take the overflow. |')
        bad = gate.problems(page(row))
        self.assertTrue(any('Work Type name in a relic' in b for b in bad), bad)

    def test_a_work_type_name_in_a_subject_is_allowed(self):
        row = ('| **SE Effect** | **On the counter** \u2014 Viderehan reads the moss and the beds '
               'take the overflow. |')
        src = '\n### Consequences\n\n- Viderehan reads the moss and the beds take the overflow.\n'
        self.assertEqual(gate.problems(page(row, etype='**Subject** \u2014 activation only',
                                           source=src)), [])


class TheBreach(unittest.TestCase):

    def test_the_breach_on_a_holding_that_cannot_breach_fails(self):
        row = GOOD.replace('On the counter', 'On the breach')
        bad = gate.problems(page(row))
        self.assertTrue(any('does not let breach' in b for b in bad), bad)

    def test_the_breach_on_a_breaching_holding_passes(self):
        row = GOOD.replace('On the counter', 'On the breach')
        ok = page(row, etype='Hazard \u2014 Can breach via Expansion')
        self.assertEqual(gate.problems(ok), [])


class TheShippedSplit(unittest.TestCase):

    def test_the_archive_carries_135_of_301(self):
        rows, fail = gate.measure()
        self.assertEqual(len(rows), gate.TARGET)
        self.assertEqual(fail, [], '%d effects off the rule' % len(fail))

    def test_no_two_effects_are_the_same(self):
        rows, _ = gate.measure()
        import io
        bodies = []
        for path, _t in rows:
            cell = gate.CELL.search(io.open(path, encoding='utf-8').read()).group(1)
            bodies.append(gate.OPEN.match(cell.strip()).group(2).strip())
        self.assertEqual(len(bodies), len(set(bodies)))


if __name__ == '__main__':
    unittest.main()
