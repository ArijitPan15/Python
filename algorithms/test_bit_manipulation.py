from bit_manipulation import count_set_bits, is_power_of_two
import unittest
class Tests(unittest.TestCase):
    def test_bits(self):
        self.assertEqual(count_set_bits(15), 4)
        self.assertTrue(is_power_of_two(1024))
        self.assertFalse(is_power_of_two(6))
        with self.assertRaises(ValueError): count_set_bits(-1)
if __name__ == "__main__": unittest.main()
