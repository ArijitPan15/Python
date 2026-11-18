"""Maximum nonempty contiguous subarray sum."""
def max_subarray_sum(values):
    iterator = iter(values)
    try:
        current = best = next(iterator)
    except StopIteration:
        raise ValueError("sequence must not be empty") from None
    for value in iterator:
        current = max(value, current + value)
        best = max(best, current)
    return best
