"""Prime number sieve with inclusive upper bound."""
def sieve(limit):
    if limit < 2:
        return []
    prime = bytearray(b"\x01") * (limit + 1)
    prime[0:2] = b"\x00\x00"
    for p in range(2, int(limit ** 0.5) + 1):
        if prime[p]:
            prime[p * p:limit + 1:p] = b"\x00" * ((limit - p * p) // p + 1)
    return [i for i, flag in enumerate(prime) if flag]
