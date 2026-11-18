from disjoint_set import DisjointSet
import unittest
class Tests(unittest.TestCase):
    def test_union(self):
        d = DisjointSet([1,2,3])
        self.assertTrue(d.union(1,2))
        self.assertTrue(d.connected(1,2))
        self.assertFalse(d.connected(1,3))
        self.assertFalse(d.union(2,1))
        with self.assertRaises(KeyError): d.find(99)
if __name__ == "__main__": unittest.main()
