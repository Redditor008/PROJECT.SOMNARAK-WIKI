# -*- coding: utf-8 -*-
"""Gate 54 — a proper noun is not a password (R-59, O-45)."""
import os
import unittest

from tools.auditors import check_backstory_gloss as gate


class TheMeasurement(unittest.TestCase):
    def test_an_appositive_dash_glosses(self):
        self.assertTrue(gate.glossed('Han — the substance the city sat on — came up through the floor',
                                     'Han'))

    def test_a_parenthesis_glosses(self):
        self.assertTrue(gate.glossed('the Veil (the suppression net over the districts) held',
                                     'Veil'))

    def test_a_copular_sentence_glosses(self):
        self.assertTrue(gate.glossed('A Fracture is what the city calls it when a person goes past '
                                     'what a person can be.', 'Fracture'))

    def test_a_bare_name_drop_does_not_gloss(self):
        self.assertFalse(gate.glossed('She gave it. Envelope, Veil, conduits, gauges, Maw.',
                                      'Veil'))

    def test_distance_does_not_gloss(self):
        """A dash three sentences later is not an explanation of this word."""
        far = ('Envelope, Veil, conduits, gauges, Maw. He signed the order. ' + 'x ' * 80
               + ' — and then the door.')
        self.assertFalse(gate.glossed(far, 'Veil'))

    def test_an_unused_term_is_not_counted(self):
        missing, used = gate.audit('## Prologue\n\nHe stood still.\n')
        self.assertEqual(missing, [])
        self.assertEqual(used, [])

    def test_the_appendix_is_not_where_a_reader_meets_a_word(self):
        text = '## Prologue\n\nThe Veil held.\n\n## Appendix\n\nThe Veil (a suppression net).\n'
        missing, _ = gate.audit(text)
        self.assertIn('Veil', missing)

    def test_a_glossed_body_passes_the_term(self):
        text = '## Prologue\n\nThe Veil (the suppression net) held all winter.\n'
        missing, used = gate.audit(text)
        self.assertEqual(missing, [])
        self.assertIn('Veil', used)


class TheArchive(unittest.TestCase):
    def test_majin_carries_no_cold_terms(self):
        path = os.path.join(gate.DIR, '01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md')
        missing, _ = gate.audit(gate.read(path))
        self.assertEqual(missing, [])

    def test_the_debt_is_current(self):
        stale = {}
        for name, recorded in gate.DEBT.items():
            missing, _ = gate.audit(gate.read(os.path.join(gate.DIR, name)))
            if len(missing) != recorded:
                stale[name] = (recorded, len(missing))
        self.assertEqual(stale, {})


if __name__ == '__main__':
    unittest.main()
