# Graph algorithms (Python standard library)

A small educational collection of graph algorithms with no third-party dependencies.

## Included

| Function | Purpose | Time complexity |
| --- | --- | --- |
| `bfs(graph, start)` | Breadth-first traversal | O(V + E) |
| `dfs(graph, start)` | Iterative depth-first traversal | O(V + E) |
| `shortest_unweighted_path(graph, start, target)` | Shortest path in an unweighted graph | O(V + E) |
| `dijkstra(graph, start)` | Shortest weighted distances | O((V + E) log V) |
| `topological_sort(graph)` | Ordering a directed acyclic graph | O(V + E) |

## Example

Run from the `algorithms` directory:

```python
from graph_algorithms import bfs, shortest_unweighted_path, dijkstra

roads = {"home": ["shop", "school"], "shop": ["park"], "school": ["park"]}
print(bfs(roads, "home"))
print(shortest_unweighted_path(roads, "home", "park"))

weighted = {"home": {"shop": 3, "school": 1}, "school": {"shop": 1}}
print(dijkstra(weighted, "home"))
```

## Tests

From the repository root:

```bash
python -m unittest discover -s algorithms -p "test_*.py"
```

## Input conventions

- Traversal and unweighted paths use `dict[vertex, iterable[vertex]]`.
- Dijkstra uses `dict[vertex, dict[vertex, nonnegative_number]]`.
- A missing adjacency entry means no outgoing edges.
- Vertices must be hashable; DFS preserves neighbor order for ordinary ordered collections.
- Negative, infinite, NaN, or nonnumeric weights are rejected.
- Topological sorting raises `ValueError` on directed cycles.

All code is educational and intended to be extended with additional edge cases and benchmarks.
