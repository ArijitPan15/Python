"""Knuth-Morris-Pratt substring search."""
def prefix_function(pattern):
    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi

def kmp_search(text, pattern):
    if not pattern:
        return list(range(len(text) + 1))
    pi = prefix_function(pattern)
    matches, j = [], 0
    for i, char in enumerate(text):
        while j and char != pattern[j]:
            j = pi[j - 1]
        if char == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = pi[j - 1]
    return matches
