#!/usr/bin/env python3
"""tests for check_work_preference.py — the two words, and the Threat Score behind them.

Batch 159 replaced the batch-156 percentage labels with **Net-Neutral** and
**Negative-Low**, and replaced the `Sorrow Gauge [HP] ≥ 500` reading with the
Conversion Guide's **Threat Score** (Coherence rank + Potency rank, 2–10). Both
changes are pinned here, including the one that is easy to lose: a legacy `0%` in
a cell must still *parse*, because a half-migrated tree should report the page
that is wrong rather than reporting every page.
"""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))

import check_work_preference as pref  # noqa: E402

NN, NL = pref.NET_NEUTRAL, pref.NEGATIVE_LOW


def table(a, b, c, d, kind='**Object/Place**', coherence='Fragment (III)',
          potency='Major (γ)'):
    rows = [('Flerehan', a), ('Pugnahan', b), ('Viderehan', c), ('Ferrehan', d)]
    body = '\n'.join('| **%s** (x) | what it does | %s |' % (k, g) for k, g in rows)
    return ('| **Entity Type** | %s |\n| **Coherence** | %s |\n| **Potency** | %s |\n'
            '| Work Type | Response | Gauge Change |\n|---|---|---|\n%s\n'
            % (kind, coherence, potency, body))


class TheAlphabet(unittest.TestCase):
    def test_the_two_named_cells_read_back(self):
        self.assertEqual(pref.normalize('Net-Neutral'), NN)
        self.assertEqual(pref.normalize('net neutral'), NN)
        self.assertEqual(pref.normalize('Negative-Low'), NL)
        self.assertEqual(pref.normalize('negative low'), NL)
        self.assertEqual(pref.normalize('**Negative-Low**'), NL)

    def test_the_retired_percentages_still_parse(self):
        # They are the batch-156 labels. Parsing them keeps a half-migrated tree
        # honest — the fault is then `percentage-token` on the page that still
        # prints one, not a false alphabet failure on every page.
        self.assertEqual(pref.normalize(' -100% '), NL)
        self.assertEqual(pref.normalize('0%'), NN)
        self.assertEqual(pref.normalize('**-100%**'), NL)
        self.assertEqual(pref.normalize('−100%'), NL)

    def test_the_old_forms_are_retired_not_silently_accepted(self):
        self.assertEqual(pref.normalize('N/A'), 'RETIRED')
        self.assertEqual(pref.normalize('—'), 'RETIRED')

    def test_a_minus_sign_is_not_a_retired_cell(self):
        # The bug this test exists for: a dead-cell pattern run before the
        # percentage pattern read `-100%` as a dash and every converted relic
        # was reported as still carrying N/A.
        self.assertNotEqual(pref.normalize('-100%'), 'RETIRED')

    def test_the_signs_and_neutral(self):
        self.assertEqual(pref.normalize('Decrease'), 'Down')
        self.assertEqual(pref.normalize('Increase'), 'Up')
        self.assertEqual(pref.normalize('Stable'), 'Neutral')
        self.assertEqual(pref.normalize('No movement'), 'Neutral')


class TheBarredPair(unittest.TestCase):
    def test_a_converted_relic_is_clean(self):
        text = table(NN, NN, 'Neutral', 'Down', coherence='Residue (I)', potency='Minor (α)')
        self.assertEqual(pref.vector_of(text), [NN, NN, 'Neutral', 'Down'])
        self.assertEqual(pref.barred_pair_problems([NN, NN]), [])

    def test_an_unequal_pair_is_refused(self):
        bad = pref.barred_pair_problems([NN, NL])
        self.assertTrue(bad)
        self.assertIn('one threat reading', ' '.join(bad))

    def test_a_recorded_increase_on_a_barred_cell_is_refused(self):
        self.assertTrue(pref.barred_pair_problems([NN, 'Up']))


class TheThreatScore(unittest.TestCase):
    """The Conversion Guide's 2–10: Coherence rank + Potency rank."""

    def test_the_score_is_the_sum_of_the_two_filed_fields(self):
        self.assertEqual(pref.threat_score(table(NN, NN, 'Neutral', 'Down')), 6)
        self.assertEqual(pref.threat_score(table(NN, NN, 'Neutral', 'Down',
                                                coherence='Residue (I)',
                                                potency='Minor (α)')), 2)
        self.assertEqual(pref.threat_score(table(NL, NL, 'Neutral', 'Down',
                                                coherence='Sovereign (V)',
                                                potency='Catastrophic (ω)')), 10)

    def test_an_unfiled_field_gives_no_score_rather_than_a_guess(self):
        self.assertIsNone(pref.threat_score('| **Entity Type** | Subject |'))

    def test_the_cut_is_the_HE_band(self):
        for score in (2, 3, 4, 5):
            self.assertEqual(pref.wanted_barred(score), NN, 'score %d' % score)
        for score in (6, 7, 8, 9, 10):
            self.assertEqual(pref.wanted_barred(score), NL, 'score %d' % score)

    def test_the_two_cells_are_one_number_not_two_checks(self):
        # A dossier whose pair is split cannot be produced by the rule at all.
        self.assertTrue(pref.barred_pair_problems([NL, NN]))

    def test_a_teth_holding_with_a_heavy_gauge_is_net_neutral(self):
        # `N-Iα-905` Lacrima: I + α = 2, ZAYIN, and it files 502 HP. The gauge is
        # the field that was wrong; the two rank fields cannot drift.
        text = table(NN, NN, 'Neutral', 'Down', coherence='Residue (I)', potency='Minor (α)')
        self.assertEqual(pref.threat_score(text), 2)
        self.assertEqual(pref.wanted_barred(2), NN)


class ShippedTree(unittest.TestCase):
    def test_corpus_is_on_the_alphabet_and_under_the_ratchet(self):
        files, problems, dist = pref.measure()
        self.assertGreater(len(files), 295, 'the glob stopped matching dossiers')
        self.assertEqual(problems, [], '%d dossiers off the alphabet' % len(problems))
        on_two = sum(n for _, n in dist.most_common(2))
        self.assertLessEqual(on_two, pref.RATCHET, '%d on two vectors' % on_two)

    def test_no_dossier_prints_a_percentage_in_a_response_cell(self):
        _, problems, _ = pref.measure()
        pct = [p for p, bad in problems if any(b.startswith('percentage-token') for b in bad)]
        self.assertEqual(pct, [], '%d dossiers still print a percentage' % len(pct))

    def test_the_palette_is_bigger_than_what_is_in_use(self):
        # Measured on the cells, not on the (Viderehan, Ferrehan) pairs: R-40
        # took the Work Type table off every relic, so the pair count now
        # measures how many *subjects* the corpus has, which is not the claim.
        # The claim is that the alphabet has more combinations than the corpus
        # uses, and the grammar fixes that at five cells by five tiers.
        _, _, dist = pref.measure()
        self.assertGreater(len(dist), 5)
        cells = {c for v in dist for c in v[2:]}
        self.assertLess(len(cells), len(pref.GOOD) * 5)


class TheTierLadder(unittest.TestCase):
    """L Corp's five-grade ladder, imported as a second axis (batch 157–158)."""

    def test_the_state_and_the_tier_are_read_separately(self):
        self.assertEqual(pref.split_tier('Neutral · High'), ('Neutral', 'High'))
        self.assertEqual(pref.normalize('Neutral · High'), 'Neutral')
        self.assertEqual(pref.split_tier('Down'), ('Down', None))

    def test_one_high_per_dossier(self):
        good = ['Down · High', 'Up · Low', 'Neutral · Common', 'Down · Common']
        self.assertEqual(pref.tier_problems(good), [])
        bad = ['Down · High', 'Up · High', 'Neutral · Common', 'Down · Common']
        self.assertTrue(any('High' in p for p in pref.tier_problems(bad)))

    def test_a_barred_cell_carries_no_preference(self):
        self.assertTrue(pref.tier_problems([NN + ' · High', NN, 'Neutral · Common', 'Down · Common']))

    def test_off_ladder_words_are_refused(self):
        self.assertTrue(pref.tier_problems(['Down · Very High', 'Up · Low',
                                            'Neutral · Common', 'Down · Common']))

    def test_the_two_extreme_grades_are_legal(self):
        # The owner lists L Corp's grades as `Common / V.H / High / V.L / Low`:
        # five, not three. The archive writes the middle three; the extremes must
        # still be accepted, or the first dossier to use one fails on vocabulary.
        self.assertEqual(pref.tier_problems(['Down · V.H', 'Up · V.L',
                                             'Neutral · Common', 'Down · Low']), [])

    def test_only_one_top_grade_per_dossier(self):
        self.assertTrue(pref.tier_problems(['Down · V.H', 'Up · V.H',
                                            'Neutral · Common', 'Down · Low']))

    def test_the_two_axes_can_disagree(self):
        # The whole point of batch 157: `Neutral · High` says a good reading that
        # settles nothing, and the checker must accept it.
        self.assertEqual(pref.tier_problems(['Down · Common', 'Up · Low',
                                             'Neutral · High', 'Down · Common']), [])


# --- batch 161: the A-page and its dossier are one holding, filed twice --------

def page(flerehan, pugnahan, code='C-IIIγ-145', shape=2):
    """A Side Codex work table in either of the two shapes the corpus uses."""
    if shape == 2:
        body = ('| Flerehan | %s |\n| Pugnahan | %s |\n'
                '| Viderehan | watched |\n| Ferrehan | endured |\n'
                % (flerehan, pugnahan))
        head = '| Work | Source response |\n|---|---|\n'
    else:
        body = ('| Flerehan | what it does | %s | keep |\n'
                '| Pugnahan | what it does | %s | keep |\n' % (flerehan, pugnahan))
        head = '| Work Type | Response | Gauge result | Field rule |\n|---|---|---|---|\n'
    return ('**SECC Designation:** `%s [N]`\n\n' % code) + head + body


class OneHoldingOneStanding(unittest.TestCase):
    """Batch 161: a holding may not carry two standings in two collections."""

    def test_a_page_and_its_dossier_agreeing_is_silent(self):
        self.assertEqual(
            pref.side_codex_problems(page(NL + ' — barred.', NL + ' — barred.'),
                                     NL), [])

    def test_a_page_silent_where_its_dossier_bars_is_a_problem(self):
        # SE-003-A before the batch: `| Flerehan | Invalid | ... |` and no word.
        bad = pref.side_codex_problems(page('Invalid.', 'Invalid.'), NL)
        self.assertTrue(any('records no standing' in b for b in bad), bad)

    def test_a_page_barring_where_its_dossier_files_valid_work_is_a_problem(self):
        # SE-145-A and SE-916-A before the batch: the codex page applied the
        # Object/Place protocol to a holding whose dossier records the work as
        # valid. The dossier is the record, so the page is the thing that moves.
        bad = pref.side_codex_problems(page(NL + ' — invalid.', NL + ' — invalid.'),
                                       '')
        self.assertTrue(any('files both works as valid' in b for b in bad), bad)

    def test_the_word_must_be_the_one_its_threat_score_wants(self):
        # C-Vδ is 5 + 4 = 9, so the pair is Negative-Low whatever the page likes.
        bad = pref.side_codex_problems(page(NN + ' — spent.', NN + ' — spent.',
                                            code='C-Vδ-111'), NN)
        self.assertTrue(any('threat score 9 wants Negative-Low' in b for b in bad), bad)

    def test_a_compound_verdict_is_refused(self):
        # `Net-Neutral / escalation` is two standings in one cell; SE-015-A.
        bad = pref.side_codex_problems(page(NN + ' — spent.', NN + ' / escalation.'),
                                       NN)
        self.assertTrue(any('compound verdict' in b for b in bad), bad)

    def test_the_legacy_n_a_is_still_reported(self):
        bad = pref.side_codex_problems(page('N/A', 'N/A'), NL)
        self.assertTrue(any('written N/A' in b for b in bad), bad)

    def test_a_page_with_no_work_table_is_not_measured(self):
        text = '**SECC Designation:** `C-IIIγ-145 [N]`\n\nNo table here.\n'
        self.assertEqual(pref.side_codex_problems(text, NL), [])
        self.assertEqual(pref.side_codex_rows(text), [])

    def test_the_corpus_stands_with_its_dossiers(self):
        # The rule has to run on the real tree: a pass that measured nothing is
        # the failure this batch exists to prevent.
        files, problems, unpaired = pref.measure_side_codex(pref.dossier_word_map())
        self.assertGreater(len(files), 200)
        self.assertEqual(problems, [])
        self.assertEqual(unpaired, [])


    def test_a_subject_that_bars_the_pair_reads_it_off_one_number(self):
        # Thirteen Subject dossiers bar both cells on their own record. The
        # equality rule used to run only on relics, so a Subject could carry two
        # different readings of one Threat Score and nothing said so.
        self.assertTrue(pref.pair_equality((NN, NL, 'Neutral', 'Down')))
        self.assertEqual(pref.pair_equality((NN, NN, 'Neutral', 'Down')), [])
        self.assertEqual(pref.pair_equality(('Down', 'Up', 'Neutral', 'Down')), [])

    def test_an_a_page_barring_the_pair_with_two_words_is_a_problem(self):
        bad = pref.side_codex_problems(page(NN + ' — spent.', NL + ' — charged.',
                                            code='C-IIIβ-015'), '')
        self.assertTrue(any('barred pair disagrees' in b for b in bad), bad)


if __name__ == '__main__':
    unittest.main()
