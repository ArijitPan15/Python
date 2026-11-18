import unittest
from two_pointers import two_sum_sorted, remove_duplicates_sorted, is_alphanumeric_palindrome


class TwoPointerTests(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum_sorted([1, 2, 4, 7], 9), (1, 3))
        self.assertIsNone(two_sum_sorted([1, 2], 9))
        self.assertIsNone(two_sum_sorted([], 0))
        self.assertEqual(two_sum_sorted([3, 3], 6), (0, 1))

    def test_deduplication(self):
        self.assertEqual(remove_duplicates_sorted([1, 1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(remove_duplicates_sorted([]), [])

    def test_palindrome(self):
        self.assertTrue(is_alphanumeric_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_alphanumeric_palindrome(""))
        self.assertFalse(is_alphanumeric_palindrome("race a car"))


if __name__ == "__main__":
    unittest.main()
