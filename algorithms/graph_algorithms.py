"""Dependency-free graph algorithms with deterministic traversal order.

Vertices must be hashable. Neighbors are processed in insertion order.
"""
from collections import deque
from heapq import heappop, heappush
from itertools import count
from math import isfinite


def bfs(graph, start):
    """Return reachable vertices in breadth-first order."""
    seen = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, ()):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return order


def dfs(graph, start):
    """Return reachable vertices in iterative depth-first order."""
    seen, order, stack = set(), [], [start]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        order.append(node)
        stack.extend(reversed(tuple(graph.get(node, ()))))
    return order


def shortest_unweighted_path(graph, start, target):
    """Return a shortest path, or None when target is unreachable."""
    queue = deque([start])
    parent = {start: None}
    while queue:
        node = queue.popleft()
        if node == target:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        for neighbor in graph.get(node, ()):
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    return None


def dijkstra(graph, start):
    """Return minimum distances for reachable vertices.

    graph maps each vertex to a mapping of neighbor -> nonnegative weight.
    Raises ValueError for negative or nonfinite weights.
    """
    distances = {start: 0}
    sequence = count()
    heap = [(0, next(sequence), start)]
    while heap:
        distance, _, node = heappop(heap)
        if distance > distances[node]:
            continue
        for neighbor, weight in graph.get(node, {}).items():
            if not isinstance(weight, (int, float)) or not isfinite(weight) or weight < 0:
                raise ValueError("edge weights must be finite nonnegative numbers")
            candidate = distance + weight
            if candidate < distances.get(neighbor, float("inf")):
                distances[neighbor] = candidate
                heappush(heap, (candidate, next(sequence), neighbor))
    return distances


def topological_sort(graph):
    """Return a topological ordering of a directed acyclic graph.

    Includes vertices appearing only as neighbors. Raises ValueError on cycles.
    """
    indegree = {}
    for node, neighbors in graph.items():
        indegree.setdefault(node, 0)
        for neighbor in neighbors:
            indegree[neighbor] = indegree.get(neighbor, 0) + 1
    queue = deque(node for node, degree in indegree.items() if degree == 0)
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, ()):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(result) != len(indegree):
        raise ValueError("graph contains a directed cycle")
    return result
