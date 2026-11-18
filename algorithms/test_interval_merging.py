from interval_merging import merge_intervals
import unittest
class Tests(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge_intervals([(1,3),(2,6),(8,10),(10,12)]), [[1,6],[8,12]])
        self.assertEqual(merge_intervals([]), [])
        with self.assertRaises(ValueError): merge_intervals([(3,1)])
if __name__ == "__main__": unittest.main()
