"""Levenshtein edit distance using linear memory."""
def edit_distance(first, second):
    previous = list(range(len(second) + 1))
    for i, a in enumerate(first, 1):
        current = [i]
        for j, b in enumerate(second, 1):
            current.append(min(previous[j] + 1, current[-1] + 1, previous[j-1] + (a != b)))
        previous = current
    return previous[-1]
