import unittest
from decorators import repeat, count_calls, timed


class DecoratorTests(unittest.TestCase):
    def test_repeat(self):
        @repeat(3)
        def double(value):
            return value * 2
        self.assertEqual(double(4), [8, 8, 8])
        self.assertEqual(double.__name__, "double")

    def test_count_calls(self):
        @count_calls
        def square(x):
            return x * x
        self.assertEqual(square(3), 9)
        self.assertEqual(square(4), 16)
        self.assertEqual(square.calls, 2)

    def test_timed(self):
        @timed
        def add(a, b):
            return a + b
        self.assertEqual(add(2, 3), 5)
        self.assertGreaterEqual(add.last_elapsed, 0)

    def test_invalid_repeat(self):
        with self.assertRaises(ValueError):
            repeat(-1)


if __name__ == "__main__":
    unittest.main()
