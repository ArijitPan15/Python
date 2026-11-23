# Token bucket rate limiter (Python standard library)

A small, thread-safe **in-memory** rate limiter for learning backend traffic
control. It starts with a full burst capacity, replenishes at a configurable
number of tokens per second, and rejects requests that exceed the quota.

## Run

From this directory:

```bash
python -m unittest discover -s . -p 'test_*.py' -v
```

Example:

```python
from limiter import TokenBucket

bucket = TokenBucket(capacity=5, refill_rate=2)
if bucket.try_acquire():
    print("request accepted")
else:
    print(f"retry after {bucket.wait_time():.2f} seconds")
```

## Behavior and tradeoffs

- Fractional token costs are supported (e.g. `try_acquire(0.5)`).
- `wait_time()` estimates a delay but **does not reserve** future tokens.
- The default clock is monotonic, avoiding wall-clock changes.
- Locks protect concurrent threads within one Python process.
- Instances do **not** share quota across workers, containers or machines.
  Production Django/Celery systems typically need an atomic Redis-backed
  implementation for global limits, plus per-user keys and key expiration.
- Do not use this example as a security boundary or DDoS mitigation system.
