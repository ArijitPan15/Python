from binary_exponentiation import power
import unittest
class Tests(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(2, 100, 7), pow(2, 100, 7))
        self.assertEqual(power(3, 0), 1)
        with self.assertRaises(ValueError): power(2, -1)
if __name__ == "__main__": unittest.main()
