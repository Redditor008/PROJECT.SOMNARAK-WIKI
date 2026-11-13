# -*- coding: utf-8 -*-
"""Gate 53 — the extended file is built on the dossier (R-57, O-43)."""
import os
import unittest

from tools.auditors import check_backstory_appearance as gate

DOSSIER = """
## Appearance

He has black veins across the left arm to a scythe mark at the wrist. Three hooked scars cross his
cheek. His eyes are deep blue and his hair is silver at the temples. He wears a charcoal coat.
"""

BODY = ("## Prologue\n\nThe veins came up the arm and stopped at the scythe. Three hooked lines "
        "opened on his cheek. His eyes were deep blue.\n")

APPENDIX = ("\n## Appendix\n\n| Director's appearance | black veins; scythe mark; hooked scars; blue eyes; "
            "silver hair; coat | Not dramatized. |\n")


class TheMapping(unittest.TestCase):
    def test_a_backstory_finds_its_dossier(self):
        path = os.path.join(gate.DIR, '01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md')
        self.assertEqual(os.path.basename(gate.dossier_for(path)), 'THE_DIRECTOR.md')

    def test_every_backstory_has_one(self):
        for path in __import__('glob').glob(os.path.join(gate.DIR, '*.md')):
            self.assertTrue(os.path.exists(gate.dossier_for(path)), path)


class TheMeasurement(unittest.TestCase):
    def test_the_vocabulary_comes_from_the_appearance_section(self):
        vocab = gate.appearance_vocabulary(DOSSIER)
        for word in ('veins', 'scythe', 'hooked', 'scars', 'blue', 'silver', 'coat'):
            self.assertIn(word, vocab)

    def test_ordinary_words_are_not_appearance(self):
        self.assertNotIn('the', gate.appearance_vocabulary(DOSSIER))

    def test_a_dossier_with_no_appearance_yields_nothing(self):
        self.assertEqual(gate.appearance_vocabulary('## Profile\n\nstuff\n'), set())

    def test_an_appearance_section_that_ends_the_file_still_counts(self):
        self.assertIn('veins', gate.appearance_vocabulary(DOSSIER))

    def test_a_body_that_shows_him_scores_well(self):
        used, avail, missing = gate.audit(BODY, DOSSIER)
        self.assertEqual(used, 7)          # veins, scythe, hooked, blue, eyes, cheek, arm

    def test_the_appendix_does_not_count(self):
        """The defect this gate exists for: the old Majin file named 'three hooked scars' and
        'scythe mark' in its own HOLD table while never showing either in a scene."""
        used, avail, _ = gate.audit('## Prologue\n\nHe stood still.\n' + APPENDIX, DOSSIER)
        self.assertEqual(used, 0)

    def test_narrative_stops_at_the_appendix(self):
        self.assertNotIn('Appendix', gate.narrative(BODY + APPENDIX))
        self.assertIn('Appendix', gate.narrative('x') + APPENDIX)


class TheArchive(unittest.TestCase):
    """The measurement, not a fixture."""

    def test_majin_is_at_or_above_the_floor(self):
        path = os.path.join(gate.DIR, '01_MAJIN_THE_DIRECTOR_BACKSTORY_EXTENDED.md')
        used, avail, _ = gate.audit(gate.read(path), gate.read(gate.dossier_for(path)))
        self.assertGreaterEqual(used / avail, gate.FLOOR)

    def test_the_debt_is_current(self):
        """A recorded remainder that has drifted is a stale claim (R-53: a status is a claim)."""
        stale = {}
        for name, (used0, avail0) in gate.DEBT.items():
            path = os.path.join(gate.DIR, name)
            used, avail, _ = gate.audit(gate.read(path), gate.read(gate.dossier_for(path)))
            if (used, avail) != (used0, avail0):
                stale[name] = ((used0, avail0), (used, avail))
        self.assertEqual(stale, {})

    def test_no_file_is_worse_than_recorded(self):
        worse = {}
        for name, (used0, _) in gate.DEBT.items():
            path = os.path.join(gate.DIR, name)
            used, _, _ = gate.audit(gate.read(path), gate.read(gate.dossier_for(path)))
            if used < used0:
                worse[name] = (used0, used)
        self.assertEqual(worse, {})


if __name__ == '__main__':
    unittest.main()
