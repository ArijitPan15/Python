"""Boyer-Moore majority vote with verification."""
def majority_element(values):
    values = list(values)
    candidate, balance = None, 0
    for value in values:
        if balance == 0:
            candidate = value
        balance += 1 if value == candidate else -1
    if values and sum(value == candidate for value in values) > len(values) // 2:
        return candidate
    return None
