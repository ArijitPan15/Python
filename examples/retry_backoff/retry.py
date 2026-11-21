"""Synchronous retry helper for transient failures."""
import random
import time


def retry_call(operation, *, attempts=3, initial_delay=0.1, multiplier=2.0,
               max_delay=10.0, jitter=0.0, retry_on=(OSError,),
               sleep=time.sleep, random_value=random.random):
    """Retry selected exceptions; return success or re-raise the final error."""
    if not isinstance(attempts, int) or isinstance(attempts, bool) or attempts < 1:
        raise ValueError("attempts must be a positive integer")
    if initial_delay < 0 or multiplier < 1 or max_delay < 0 or jitter < 0:
        raise ValueError("invalid backoff parameters")
    if not retry_on or not all(isinstance(kind, type) and issubclass(kind, Exception) for kind in retry_on):
        raise ValueError("retry_on must contain Exception subclasses")

    for index in range(attempts):
        try:
            return operation()
        except retry_on:
            if index == attempts - 1:
                raise
            delay = min(initial_delay * multiplier ** index, max_delay)
            sleep(delay + jitter * random_value())
    raise AssertionError("unreachable")
