"""Prefix sums and range queries."""
def prefix_sums(values):
    result = [0]
    for value in values:
        result.append(result[-1] + value)
    return result

def range_sum(prefix, start, stop):
    if not 0 <= start <= stop < len(prefix):
        raise IndexError("invalid half-open range")
    return prefix[stop] - prefix[start]
