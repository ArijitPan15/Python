"""Lossless run-length encoding for sequences of strings."""
def encode(text):
    if not text:
        return []
    result = []
    current, count = text[0], 1
    for char in text[1:]:
        if char == current:
            count += 1
        else:
            result.append((current, count))
            current, count = char, 1
    result.append((current, count))
    return result

def decode(runs):
    result = []
    for char, count in runs:
        if len(char) != 1 or not isinstance(count, int) or count < 0:
            raise ValueError("invalid run")
        result.append(char * count)
    return "".join(result)
