"""Sliding-window algorithms for sequences and strings."""
from collections import Counter


def max_window_sum(numbers, size):
    """Return the maximum sum of any consecutive window of size items."""
    if size <= 0 or size > len(numbers):
        raise ValueError("size must be between 1 and sequence length")
    current = sum(numbers[:size])
    best = current
    for i in range(size, len(numbers)):
        current += numbers[i] - numbers[i - size]
        best = max(best, current)
    return best


def longest_unique_substring(text):
    """Length of the longest substring without repeated characters."""
    last_seen = {}
    left = 0
    best = 0
    for right, char in enumerate(text):
        if char in last_seen:
            left = max(left, last_seen[char] + 1)
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best


def minimum_window_substring(text, pattern):
    """Smallest substring containing all pattern characters with multiplicity."""
    if not pattern:
        return ""
    required = Counter(pattern)
    missing = len(pattern)
    left = 0
    best_start, best_length = 0, float("inf")
    for right, char in enumerate(text):
        if required[char] > 0:
            missing -= 1
        required[char] -= 1
        while missing == 0:
            if right - left + 1 < best_length:
                best_start, best_length = left, right - left + 1
            outgoing = text[left]
            required[outgoing] += 1
            if required[outgoing] > 0:
                missing += 1
            left += 1
    return "" if best_length == float("inf") else text[best_start:best_start + best_length]
