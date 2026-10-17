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


if __name__ == '__main__':
    unittest.main()
