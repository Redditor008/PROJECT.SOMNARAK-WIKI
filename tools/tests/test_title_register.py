# -*- coding: utf-8 -*-
"""Gate 55 — a name keeps its costume (R-61, O-46)."""
import os
import unittest

from tools.auditors import check_title_register as gate

HEAD = '> **REGISTER:** a **designation** is set in full caps (THE ORIGINAL).\n\n'


class TheDesignation(unittest.TestCase):
    def test_caps_pass(self):
        bad, uses = gate.audit_designation(HEAD + 'He wrote THE ORIGINAL in box one.', 'THE ORIGINAL')
        self.assertEqual((bad, uses), ([], 1))

    def test_a_mixed_case_use_fails(self):
        bad, _ = gate.audit_designation(HEAD + 'He still says the Original.', 'THE ORIGINAL')
        self.assertEqual(bad, ['the Original'])

    def test_the_ordinary_word_is_not_a_casing(self):
        """`they were the original` is English, not a claim to be the name."""
        bad, _ = gate.audit_designation(HEAD + 'Both said they were the original.', 'THE ORIGINAL')
        self.assertEqual(bad, [])

    def test_the_legend_does_not_count_as_a_use(self):
        bad, uses = gate.audit_designation(HEAD, 'THE ORIGINAL')
        self.assertEqual(uses, 0)


class TheCoining(unittest.TestCase):
    def test_italic_at_first_use_passes(self):
        text = HEAD + 'It was called *Reaper Hungered*, and the name stuck.'
        self.assertTrue(gate.audit_named_thing(text, 'Reaper Hungered'))

    def test_a_bare_first_use_fails(self):
        text = HEAD + 'It was called Reaper Hungered, and the name stuck.'
        self.assertFalse(gate.audit_named_thing(text, 'Reaper Hungered'))

    def test_a_heading_is_not_the_coining(self):
        text = HEAD + '## Before the Hand Opened\n\nHe walked in.'
        self.assertIsNone(gate.audit_named_thing(text, 'the Hand'))

    def test_a_table_row_is_not_the_coining(self):
        text = HEAD + '| a | b |\n\nIt was *the Hand* that held.\n'
        self.assertTrue(gate.audit_named_thing(text, 'the Hand'))

    def test_a_capitalised_the_at_a_sentence_start_still_counts(self):
        text = HEAD + 'The Absolvohan began as a line on a slip.'
        self.assertTrue(gate.audit_named_thing(text, 'the Absolvohan') is False)
        text2 = HEAD + '*The Absolvohan* began as a line on a slip.'
        self.assertTrue(gate.audit_named_thing(text2, 'the Absolvohan'))


class TheBody(unittest.TestCase):
    def test_a_capital_article_mid_line_is_the_mark(self):
        text = HEAD + 'The room was silent, and The Endurers said nothing.'
        ok, why = gate.audit_body(text, 'The Endurers')
        self.assertTrue(ok, why)

    def test_a_sentence_initial_name_has_no_mark(self):
        """At the start of a sentence every word is capitalised, so the capital proves nothing."""
        text = HEAD + 'The Endurers said it was grief with nowhere to go.'
        ok, why = gate.audit_body(text, 'The Endurers')
        self.assertFalse(ok)
        self.assertIn('sentence-initial', why)

    def test_a_lower_case_article_fails(self):
        text = HEAD + 'The room was silent, and the endurers said nothing.'
        ok, why = gate.audit_body(text, 'The Endurers')
        self.assertFalse(ok)

    def test_a_body_is_found_by_its_core_not_its_article(self):
        text = HEAD + 'By Majin\'s century only two schools remained, and one of them was The Converters.'
        ok, _ = gate.audit_body(text, 'The Converters')
        self.assertTrue(ok)

    def test_an_unused_body_is_reported(self):
        ok, why = gate.audit_body(HEAD + 'Nothing here.', 'The Endurers')
        self.assertIsNone(ok)
        self.assertEqual(why, 'never used')

    def test_a_paragraph_start_is_sentence_initial(self):
        text = HEAD + 'Text.\n\nThe Endurers said nothing.'
        ok, _ = gate.audit_body(text, 'The Endurers')
        self.assertFalse(ok)


class TheArchive(unittest.TestCase):
    def test_every_file_explains_its_marks(self):
        import glob
        missing = []
        for path in glob.glob(os.path.join(gate.DIR, '*.md')):
            if '**REGISTER:**' not in gate.read(path)[:2500]:
                missing.append(os.path.basename(path))
        self.assertEqual(missing, [])

    def test_majin_holds_the_register(self):
        path = os.path.join(gate.DIR, '01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md')
        text = gate.read(path)
        bad, uses = gate.audit_designation(text, 'THE ORIGINAL')
        self.assertEqual(bad, [])
        self.assertGreater(uses, 0)
        for name in gate.NAMED_THINGS['01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md']:
            self.assertTrue(gate.audit_named_thing(text, name), name)

    def test_majin_bodies_carry_a_visible_mark(self):
        path = os.path.join(gate.DIR, '01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md')
        text = gate.read(path)
        for name in gate.BODIES['01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md']:
            ok, why = gate.audit_body(text, name)
            self.assertTrue(ok, '%s: %s' % (name, why))


if __name__ == '__main__':
    unittest.main()
