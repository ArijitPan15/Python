"""Lazy generators demonstrating yield and streaming iteration."""
def fibonacci(limit):
    """Yield the first limit Fibonacci numbers."""
    if limit < 0:
        raise ValueError("limit must be nonnegative")
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def countdown(start):
    """Yield integers from start down to zero."""
    while start >= 0:
        yield start
        start -= 1


def chunked(iterable, size):
    """Yield lists of up to size elements without loading all input."""
    if size <= 0:
        raise ValueError("size must be positive")
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def running_average(iterable):
    total = 0
    for index, value in enumerate(iterable, 1):
        total += value
        yield total / index
