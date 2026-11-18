"""Binary search helpers for sorted sequences."""
def lower_bound(values, target):
    """Index of the first value >= target."""
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left


def upper_bound(values, target):
    """Index of the first value > target."""
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] <= target:
            left = middle + 1
        else:
            right = middle
    return left


def binary_search(values, target):
    """Return the first matching index or -1."""
    index = lower_bound(values, target)
    return index if index < len(values) and values[index] == target else -1


def search_insert_position(values, target):
    """Find the insertion index that preserves ascending order."""
    return lower_bound(values, target)


def occurrence_count(values, target):
    """Count occurrences of target in ascending sorted values."""
    return upper_bound(values, target) - lower_bound(values, target)
