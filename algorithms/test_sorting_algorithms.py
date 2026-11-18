import unittest
from sorting_algorithms import insertion_sort, merge_sort, heap_sort


class SortingTests(unittest.TestCase):
    def test_algorithms(self):
        samples = [[], [1], [3, 1, 2, 1], [-4, 0, 2, -1], [5, 4, 3, 2, 1]]
        for algorithm in (insertion_sort, merge_sort, heap_sort):
            for sample in samples:
                with self.subTest(algorithm=algorithm.__name__, sample=sample):
                    original = sample[:]
                    self.assertEqual(algorithm(sample), sorted(sample))
                    self.assertEqual(sample, original)

    def test_strings(self):
        for algorithm in (insertion_sort, merge_sort, heap_sort):
            self.assertEqual(algorithm(["pear", "apple"]), ["apple", "pear"])


if __name__ == "__main__":
    unittest.main()
