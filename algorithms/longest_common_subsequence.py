"""Longest common subsequence length using linear memory."""
def lcs_length(first, second):
    previous = [0] * (len(second) + 1)
    for a in first:
        current = [0]
        for j, b in enumerate(second, 1):
            current.append(previous[j-1] + 1 if a == b else max(previous[j], current[-1]))
        previous = current
    return previous[-1]
