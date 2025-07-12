import unittest
import json
from streamfix_pro import fix_top_n_no_duplicates

class TestStreamRankFixer(unittest.TestCase):
    def test_no_duplicates_needed(self):
        data = [
            {'streamerID': 'A'},
            {'streamerID': 'B'},
            {'streamerID': 'C'},
            {'streamerID': 'D'}
        ]
        result = fix_top_n_no_duplicates(data, 3)
        self.assertEqual(result[:3], ['A', 'B', 'C'])

    def test_duplicates_in_top_n(self):
        data = [
            {'streamerID': 'A'},
            {'streamerID': 'A'},
            {'streamerID': 'B'},
            {'streamerID': 'C'},
            {'streamerID': 'D'}
        ]
        result = fix_top_n_no_duplicates(data, 3)
        self.assertEqual(len(set(result[:3])), 3)
        self.assertIn('A', result[:3])
        self.assertIn('B', result[:3])
        self.assertIn('C', result[:3])

    def test_less_than_n(self):
        data = [
            {'streamerID': 'A'},
            {'streamerID': 'A'}
        ]
        result = fix_top_n_no_duplicates(data, 3)
        self.assertEqual(result[0], 'A')
        self.assertEqual(len(result), 1)

    def test_empty(self):
        data = []
        result = fix_top_n_no_duplicates(data, 3)
        self.assertEqual(result, [])

    def test_summary_tracking(self):
        data = [
            {'streamerID': 'A'},
            {'streamerID': 'A'},
            {'streamerID': 'B'}
        ]
        summary = {}
        fix_top_n_no_duplicates(data, 2, section_id='test', summary=summary)
        self.assertIn('test', summary)
        self.assertGreaterEqual(summary['test'], 1)

if __name__ == '__main__':
    unittest.main() 