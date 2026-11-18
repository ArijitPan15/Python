"""Run with: python -m unittest discover -s algorithms -p 'test_*.py'"""
import unittest
from graph_algorithms import bfs, dfs, dijkstra, shortest_unweighted_path, topological_sort


class GraphAlgorithmsTests(unittest.TestCase):
    def setUp(self):
        self.graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}

    def test_bfs(self):
        self.assertEqual(bfs(self.graph, "A"), ["A", "B", "C", "D"])

    def test_dfs(self):
        self.assertEqual(dfs(self.graph, "A"), ["A", "B", "D", "C"])

    def test_missing_start(self):
        self.assertEqual(bfs({}, "X"), ["X"])
        self.assertEqual(dfs({}, "X"), ["X"])

    def test_shortest_path(self):
        self.assertEqual(shortest_unweighted_path(self.graph, "A", "D"), ["A", "B", "D"])
        self.assertIsNone(shortest_unweighted_path(self.graph, "D", "A"))
        self.assertEqual(shortest_unweighted_path({}, "X", "X"), ["X"])

    def test_dijkstra(self):
        graph = {"A": {"B": 4, "C": 1}, "C": {"B": 2}, "B": {"D": 1}}
        self.assertEqual(dijkstra(graph, "A"), {"A": 0, "B": 3, "C": 1, "D": 4})

    def test_dijkstra_rejects_invalid_weights(self):
        for weight in (-1, float("nan"), float("inf"), "3"):
            with self.subTest(weight=weight):
                with self.assertRaises(ValueError):
                    dijkstra({"A": {"B": weight}}, "A")

    def test_topological_sort(self):
        order = topological_sort({"build": ["test"], "test": ["deploy"]})
        self.assertEqual(order, ["build", "test", "deploy"])

    def test_cycle(self):
        with self.assertRaises(ValueError):
            topological_sort({"A": ["B"], "B": ["A"]})


if __name__ == "__main__":
    unittest.main()
