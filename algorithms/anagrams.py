"""Unicode-aware anagram grouping."""
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word.casefold()))
        groups[key].append(word)
    return list(groups.values())
