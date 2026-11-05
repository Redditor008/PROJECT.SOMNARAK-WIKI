# -*- coding: utf-8 -*-
"""Gate 86 — consequence reaches as far as the band does (R-43)."""
import unittest

from tools.auditors import check_consequence_register as gate

HIGH = ('| **Coherence** | Sovereign (V) |\n'
        '| **Potency** | Critical (\u03b4) |\n'
        '### Consequences\n\n'
        '%s\n\n## Appearance\n')
LOW = ('| **Coherence** | Residue (I) |\n'
       '| **Potency** | Minor (\u03b1) |\n'
       '### Consequences\n\n- A worker loses an afternoon.\n\n## Appearance\n')

INSTITUTION = '- The perimeter is surveyed every quarter and the district has never rebuilt.'
PERSON = '- A worker who breaks simply leaves.'


class HighReach(unittest.TestCase):

    def test_high_naming_an_institution_passes(self):
        self.assertEqual(gate.problems(HIGH % INSTITUTION), [])

    def test_high_that_stops_at_one_worker_fails(self):
        bad = gate.problems(HIGH % PERSON)
        self.assertTrue(any('institution-scale' in b for b in bad), bad)

    def test_high_with_no_consequences_fails(self):
        text = ('| **Coherence** | Sovereign (V) |\n| **Potency** | Catastrophic (\u03c9) |\n'
                '## Appearance\n')
        bad = gate.problems(text)
        self.assertTrue(any('no Consequences section' in b for b in bad), bad)


class LowAction(unittest.TestCase):

    def test_low_with_an_ultimate_fails(self):
        text = LOW + '\n| { *The Last Move* [**Ultimate**] } | x | y | z | w |\n'
        bad = gate.problems(text)
        self.assertTrue(any('Ultimate' in b for b in bad), bad)

    def test_low_with_an_overload_passes(self):
        text = LOW + '\n| { *The Last Move* [**Overload**] } | x | y | z | w |\n'
        self.assertEqual(gate.problems(text), [])


class ReportsOnly(unittest.TestCase):

    def test_top_that_stays_personal_is_only_reported(self):
        text = ('| **Coherence** | Entity (IV) |\n| **Potency** | Critical (\u03b4) |\n'
                '### Consequences\n\n' + PERSON + '\n\n## Appearance\n')
        self.assertEqual(gate.problems(text), [])
        self.assertTrue(gate.notes(text))

    def test_common_claiming_the_city_is_only_reported(self):
        text = ('| **Coherence** | Fragment (III) |\n| **Potency** | Major (\u03b3) |\n'
                '### Consequences\n\n' + INSTITUTION + '\n\n## Appearance\n')
        self.assertEqual(gate.problems(text), [])
        self.assertTrue(gate.notes(text))


if __name__ == '__main__':
    unittest.main()
