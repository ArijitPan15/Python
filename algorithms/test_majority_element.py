from majority_element import majority_element
import unittest
class Tests(unittest.TestCase):
    def test_majority(self):
        self.assertEqual(majority_element([2,2,1,2,3]), 2)
        self.assertIsNone(majority_element([1,2,3]))
        self.assertIsNone(majority_element([]))
if __name__ == "__main__": unittest.main()
