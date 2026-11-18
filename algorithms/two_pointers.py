"""Two-pointer solutions for sorted arrays and string normalization."""


def two_sum_sorted(numbers, target):
    """Return zero-based pair of indices or None. Requires ascending input."""
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return left, right
        if total < target:
            left += 1
        else:
            right -= 1
    return None


def remove_duplicates_sorted(numbers):
    """Return a deduplicated list from ascending sorted input."""
    result = []
    for item in numbers:
        if not result or result[-1] != item:
            result.append(item)
    return result


def is_alphanumeric_palindrome(text):
    """Ignore nonalphanumeric characters and case when testing a palindrome."""
    left, right = 0, len(text) - 1
    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1
        if text[left].casefold() != text[right].casefold():
            return False
        left += 1
        right -= 1
    return True
