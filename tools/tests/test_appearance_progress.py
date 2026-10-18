import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / 'appearance_progress.py'
spec = importlib.util.spec_from_file_location('appearance_progress', MODULE)
ap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ap)


class AppearanceProgressTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(ap.LEDGER.read_text())
        self.inventory = {r['designation']: r['path'] for r in self.data['dossiers']}
        # Fixtures model a fresh OPEN pass even after the live batch is CLOSED.
        self.data['active_batch']['status'] = 'OPEN'
        # A clean independent pass must not inherit the two legacy 240 credits.
        for r in self.data['dossiers']:
            r['status'] = 'pending'

    def test_no_legacy_backfill(self):
        counts, done, _ = ap.validate(self.data, self.inventory)
        self.assertEqual(counts['changed'] + counts['retained'], 0)
        self.assertEqual(done, 0)

    def test_duplicate_rejected(self):
        self.data['dossiers'][-1] = copy.deepcopy(self.data['dossiers'][0])
        with self.assertRaises(AssertionError):
            ap.validate(self.data, self.inventory)

    def test_wrong_identity_path_rejected(self):
        self.data['dossiers'][0]['path'] += '.wrong'
        with self.assertRaises(AssertionError):
            ap.validate(self.data, self.inventory)

    def test_completion_needs_evidence(self):
        self.data['dossiers'][0]['status'] = 'changed'
        with self.assertRaises(AssertionError):
            ap.validate(self.data, self.inventory)

    def test_pending_cannot_close(self):
        self.data['active_batch']['status'] = 'CLOSED'
        with self.assertRaises(AssertionError):
            ap.validate(self.data, self.inventory)

    def test_changed_count_is_unique(self):
        row = self.data['dossiers'][0]
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'evidence.md').write_text('Evidence')
            (root / 'source.md').write_text('Source')
            row.update(status='changed', outcome='source-supported repair', evidence='evidence.md',
                       sources=['source.md'], whole_final_reread=True,
                       checks=dict.fromkeys(('verify', 'tpl', 'sectfile', 'wikistd', 'sect'), 'PASS'))
            counts, _, _ = ap.validate(self.data, self.inventory, root)
            self.assertEqual(counts['changed'], 1)

    def test_closed_ladder_uses_cumulative_no_change(self):
        rows = self.data['dossiers'][:10]
        batch = self.data['active_batch']
        batch.update(status='CLOSED', required=5, queue=[r['designation'] for r in rows[:5]])
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'evidence.md').write_text('Evidence')
            (root / 'source.md').write_text('Source')
            for i, row in enumerate(rows):
                row.update(status='retained' if i < 3 else 'changed',
                           outcome='retained design' if i < 3 else 'source-supported repair',
                           evidence='evidence.md', sources=['source.md'], whole_final_reread=True,
                           checks=dict.fromkeys(('verify', 'tpl', 'sectfile', 'wikistd', 'sect'), 'PASS'))
            for rung in (5, 7):
                batch.update(required=rung, queue=[r['designation'] for r in rows[:rung]])
                with self.assertRaises(AssertionError):
                    ap.validate(self.data, self.inventory, root)
            batch.update(required=10, queue=[r['designation'] for r in rows])
            _, done, unchanged = ap.validate(self.data, self.inventory, root)
            self.assertEqual((done, unchanged), (10, 3))

    def test_held_is_not_completion(self):
        self.data['dossiers'][0]['status'] = 'held'
        counts, done, _ = ap.validate(self.data, self.inventory)
        self.assertEqual((counts['held'], done), (1, 0))


if __name__ == '__main__':
    unittest.main()
