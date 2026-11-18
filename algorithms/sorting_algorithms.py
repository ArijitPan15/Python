"""Educational comparison sorting algorithms.

All functions return new lists and leave the original sequence unchanged.
"""
def insertion_sort(values):
    result = list(values)
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result


def merge_sort(values):
    result = list(values)
    if len(result) < 2:
        return result
    middle = len(result) // 2
    left = merge_sort(result[:middle])
    right = merge_sort(result[middle:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def heap_sort(values):
    """Sort ascending with a min heap; supports comparable items."""
    from heapq import heapify, heappop
    heap = list(values)
    heapify(heap)
    return [heappop(heap) for _ in range(len(heap))]
