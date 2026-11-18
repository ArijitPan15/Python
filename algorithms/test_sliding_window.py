import unittest
from sliding_window import max_window_sum, longest_unique_substring, minimum_window_substring


class SlidingWindowTests(unittest.TestCase):
    def test_window_sum(self):
        self.assertEqual(max_window_sum([2, -1, 4, 3], 2), 7)
        self.assertEqual(max_window_sum([-4, -2, -9], 1), -2)
        with self.assertRaises(ValueError):
            max_window_sum([1], 0)
        with self.assertRaises(ValueError):
            max_window_sum([1], 2)

    def test_unique_substring(self):
        self.assertEqual(longest_unique_substring("abcabcbb"), 3)
        self.assertEqual(longest_unique_substring(""), 0)
        self.assertEqual(longest_unique_substring("bbbb"), 1)

    def test_minimum_window(self):
        self.assertEqual(minimum_window_substring("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(minimum_window_substring("a", "aa"), "")
        self.assertEqual(minimum_window_substring("abc", ""), "")
        self.assertEqual(minimum_window_substring("aaab", "aab"), "aab")


if __name__ == "__main__":
    unittest.main()
