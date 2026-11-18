import unittest
from generators import fibonacci, countdown, chunked, running_average


class GeneratorTests(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(list(fibonacci(7)), [0, 1, 1, 2, 3, 5, 8])
        with self.assertRaises(ValueError):
            list(fibonacci(-1))

    def test_countdown(self):
        self.assertEqual(list(countdown(3)), [3, 2, 1, 0])
        self.assertEqual(list(countdown(-1)), [])

    def test_chunked(self):
        self.assertEqual(list(chunked(range(5), 2)), [[0, 1], [2, 3], [4]])
        with self.assertRaises(ValueError):
            list(chunked([], 0))

    def test_running_average(self):
        self.assertEqual(list(running_average([2, 4, 9])), [2.0, 3.0, 5.0])


if __name__ == "__main__":
    unittest.main()
