"""Disjoint-set union with path compression and union by size."""
class DisjointSet:
    def __init__(self, elements=()):
        self.parent = {}
        self.size = {}
        for element in elements:
            self.add(element)

    def add(self, element):
        if element not in self.parent:
            self.parent[element] = element
            self.size[element] = 1

    def find(self, element):
        if element not in self.parent:
            raise KeyError(element)
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, first, second):
        a, b = self.find(first), self.find(second)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

    def connected(self, first, second):
        return self.find(first) == self.find(second)
