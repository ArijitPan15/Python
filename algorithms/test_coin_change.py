from coin_change import min_coins
import unittest
class Tests(unittest.TestCase):
    def test_coins(self):
        self.assertEqual(min_coins([1,2,5], 11), 3)
        self.assertEqual(min_coins([2], 3), -1)
        self.assertEqual(min_coins([], 0), 0)
        with self.assertRaises(ValueError): min_coins([0], 3)
if __name__ == "__main__": unittest.main()
