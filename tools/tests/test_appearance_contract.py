# -*- coding: utf-8 -*-
"""Gate 50 — Appearance is a category and a way of writing (R-54, O-14, O-40)."""
import unittest

from tools.auditors import check_appearance_contract as gate


def section(body):
    """A dossier with one Appearance section and nothing after it."""
    return '## Identity\n\nstuff\n\n## Appearance\n' + body + '\n## Origin & Formation\n\nstuff\n'


LEDGER = section(
    '\n| Field | Detail |\n|---|---|\n'
    '| **Form** | A palm-sized brass compass with a bone needle. |\n'
    '| **Position / movement** | Fixed on its stand; only the needle moves. |\n'
    '| **Material / signature** | Tarnished brass, warm in the hand. |\n'
    '| **Distinctive markers** | No cardinal points. |\n')

PROSE = section(
    '\nA palm-sized brass compass sits on a fixed stand, its face unmarked and its bone needle '
    'drifting toward concentrated grief. ' + ('The casing is tarnished and warm. ' * 20) + '\n')


class TheCategory(unittest.TestCase):
    """Axis A: every dossier resolves to one of R-32's families."""

    def test_each_family_is_recognised(self):
        cases = {
            'A humanoid figure in a clerk coat.': 'humanoid',
            'A many-limbed amalgam of mouths.': 'monster',
            'A raven with a brass beak.': 'animal',
            'A bodyless voice moving through the hall.': 'abstract',
            'A wall of stacked stone across the district.': 'place',
            'A palm-sized brass compass with a bone needle.': 'object',
            'A clockwork automaton of brass gears.': 'mechanical',
        }
        for text, family in cases.items():
            self.assertEqual(gate.family(text), family, text)

    def test_plurals_are_read(self):
        """`\\bwall\\b` does not match 'walls' — the defect that hid 12 dossiers."""
        self.assertEqual(gate.family('The walls of the Old Lament breathe.'), 'place')

    def test_an_explicit_negative_outranks_an_incidental_body_word(self):
        """'The Choir has no physical body' is abstract, not humanoid."""
        self.assertEqual(
            gate.family('The Choir has no physical body. It manifests as 144 ethereal voices.'),
            'abstract')

    def test_a_zone_of_ground_is_not_an_animal(self):
        self.assertEqual(gate.family('A zone of ground where anyone who stands still cracks.'),
                         'place')

    def test_a_concrete_noun_outranks_a_loose_abstract_one(self):
        """A bell that makes a sound is still a bell."""
        self.assertEqual(gate.family('A cracked bronze bell that sounds at dusk.'), 'object')

    def test_no_family_is_none(self):
        self.assertIsNone(gate.family('There is nothing here to describe.'))

    def test_the_archive_resolves(self):
        """The measurement, not a fixture: no dossier is left unfiled."""
        unfiled = []
        for path in gate.dossier_files():
            issues, _ = gate.audit(gate.read(path))
            if any('no shape family' in why for why, _ in issues):
                unfiled.append(path)
        self.assertEqual(unfiled, [])


class TheFormStatement(unittest.TestCase):
    """The category is read off the section, never off `Physical Form`."""

    def test_a_table_row_is_read(self):
        self.assertIn('brass compass', gate.form_text(LEDGER))

    def test_a_bolded_line_is_read(self):
        self.assertIn('brass compass',
                      gate.form_text('**Physical Form:** A brass compass on a stand.'))

    def test_the_primary_form_variant_is_read(self):
        self.assertIn('compass', gate.form_text('**Primary Form:** A brass compass.'))

    def test_the_marker_fallback_is_read(self):
        self.assertIn('compass', gate.form_text('- **Primary marker:** A brass compass.'))

    def test_a_prose_section_states_its_form_in_the_opening_sentence(self):
        self.assertIn('brass compass', gate.form_text(PROSE.split('## Appearance\n', 1)[1]))


class TheWriting(unittest.TestCase):
    """Axis B: two shapes, both L Corp's, and neither may explain."""

    def test_a_ledger_is_a_ledger(self):
        self.assertEqual(gate.shape(LEDGER), 'ledger')

    def test_a_prose_section_is_an_observation(self):
        self.assertEqual(gate.shape(PROSE), 'observation')

    def test_a_short_prose_section_is_neither(self):
        self.assertIsNone(gate.shape(section('A brass compass. It points at grief.\n')))

    def test_a_ledger_with_a_missing_reading_fails_the_audit(self):
        body = LEDGER.replace('| **Material / signature** | Tarnished brass, warm in the hand. |\n',
                              '')
        issues, _ = gate.audit(body)
        self.assertTrue(any('Material / signature' in why for why, _ in issues), issues)

    def test_a_boundary_movement_row_answers_the_position_reading(self):
        body = LEDGER.replace('**Position / movement**', '**Boundary / movement**')
        issues, _ = gate.audit(body)
        self.assertEqual([why for why, _ in issues if 'Position' in why], [])

    def test_a_symbolic_claim_is_a_tell(self):
        body = LEDGER.replace('No cardinal points.', 'Every bloom stands for a wrong.')
        _, stats = gate.audit(body)
        self.assertEqual(stats['tells'], 1)

    def test_a_duration_is_not_a_tell(self):
        """'stands for more than three minutes' is a stand, not a symbol."""
        body = LEDGER.replace('No cardinal points.',
                              'Anyone who stands for more than three minutes develops cracks.')
        _, stats = gate.audit(body)
        self.assertEqual(stats['tells'], 0)

    def test_the_archive_has_no_tells(self):
        telling = []
        for path in gate.dossier_files():
            _, stats = gate.audit(gate.read(path))
            if stats['tells']:
                telling.append(path)
        self.assertEqual(telling, [])


if __name__ == '__main__':
    unittest.main()
