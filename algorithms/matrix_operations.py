"""Rectangular matrix utilities."""
def transpose(matrix):
    if not matrix:
        return []
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("ragged matrix")
    return [list(column) for column in zip(*matrix)]

def matrix_add(a, b):
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise ValueError("matrix shapes must match")
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]
