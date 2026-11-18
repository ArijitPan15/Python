from string_matching import kmp_search, prefix_function
import unittest
class Tests(unittest.TestCase):
    def test_kmp(self):
        self.assertEqual(kmp_search("ababa", "aba"), [0,2])
        self.assertEqual(kmp_search("abc", "d"), [])
        self.assertEqual(kmp_search("ab", ""), [0,1,2])
        self.assertEqual(prefix_function("ababaca"), [0,0,1,2,3,0,1])
if __name__ == "__main__": unittest.main()
