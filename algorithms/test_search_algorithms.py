"""Tests for binary search boundaries."""
import unittest
from search_algorithms import (
    binary_search, lower_bound, upper_bound, search_insert_position, occurrence_count
)


class SearchTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(binary_search([], 4), -1)
        self.assertEqual(lower_bound([], 4), 0)
        self.assertEqual(upper_bound([], 4), 0)

    def test_duplicates(self):
        values = [1, 2, 2, 2, 4]
        self.assertEqual(binary_search(values, 2), 1)
        self.assertEqual(lower_bound(values, 2), 1)
        self.assertEqual(upper_bound(values, 2), 4)
        self.assertEqual(occurrence_count(values, 2), 3)

    def test_absent(self):
        values = [1, 3, 5]
        self.assertEqual(binary_search(values, 4), -1)
        self.assertEqual(search_insert_position(values, 4), 2)
        self.assertEqual(occurrence_count(values, 4), 0)

    def test_extremes(self):
        self.assertEqual(lower_bound([2, 4], 1), 0)
        self.assertEqual(upper_bound([2, 4], 5), 2)


if __name__ == "__main__":
    unittest.main()
