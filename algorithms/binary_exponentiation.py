"""Exponentiation by squaring."""
def power(base, exponent, modulus=None):
    if not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be nonnegative")
    if modulus is not None and modulus <= 0:
        raise ValueError("modulus must be positive")
    result = 1 if modulus is None else 1 % modulus
    if modulus is not None:
        base %= modulus
    while exponent:
        if exponent & 1:
            result *= base
            if modulus is not None:
                result %= modulus
        base *= base
        if modulus is not None:
            base %= modulus
        exponent >>= 1
    return result
