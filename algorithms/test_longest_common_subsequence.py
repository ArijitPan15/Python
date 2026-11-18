from longest_common_subsequence import lcs_length
import unittest
class Tests(unittest.TestCase):
    def test_lcs(self):
        self.assertEqual(lcs_length("abcde", "ace"), 3)
        self.assertEqual(lcs_length("", "abc"), 0)
        self.assertEqual(lcs_length("abc", "def"), 0)
if __name__ == "__main__": unittest.main()
