# Retry with exponential backoff

A dependency-free Python example for retrying **synchronous, idempotent** operations that fail transiently. `retry_call` retries only selected exception classes (by default `OSError`) and re-raises the original exception after the final attempt.

```python
from retry import retry_call

result = retry_call(lambda: fetch_remote_data(), attempts=4,
                    initial_delay=0.2, max_delay=2.0,
                    retry_on=(ConnectionError, TimeoutError))
```

Delay before retry number `n` (zero-indexed) is `min(initial_delay * multiplier**n, max_delay) + jitter * random_value()`. Inject `sleep` and `random_value` to test without waiting. No delay occurs after the final failure.

Run tests from this directory:

```sh
python -m unittest discover -s . -p 'test_*.py' -v
```

**Cautions:** Retries can duplicate side effects (payments, writes, email); use only with idempotent operations or idempotency keys. This helper does not inspect HTTP status codes, enforce deadlines, or implement asynchronous cancellation. Choose bounded attempts and delays in production.
