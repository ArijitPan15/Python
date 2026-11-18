from edit_distance import edit_distance
import unittest
class Tests(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(edit_distance("kitten", "sitting"), 3)
        self.assertEqual(edit_distance("", "abc"), 3)
        self.assertEqual(edit_distance("same", "same"), 0)
if __name__ == "__main__": unittest.main()
