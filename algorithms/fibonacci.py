"""Fast doubling Fibonacci in logarithmic time."""
def fibonacci(n):
    if n < 0:
        raise ValueError("n must be nonnegative")
    def pair(k):
        if k == 0:
            return 0, 1
        a, b = pair(k // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        return (d, c + d) if k % 2 else (c, d)
    return pair(n)[0]
