"""Thread-safe in-memory token bucket for educational backend applications."""

from __future__ import annotations

import math
import threading
import time
from collections.abc import Callable


class TokenBucket:
    """Allow bursts up to capacity and replenish tokens at a steady rate.

    A single instance controls one logical quota. This is not a distributed
    limiter; use shared atomic storage for multi-process deployments.
    """

    def __init__(
        self,
        capacity: float,
        refill_rate: float,
        *,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        for name, value in (("capacity", capacity), ("refill_rate", refill_rate)):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(f"{name} must be a finite number")
            if not math.isfinite(value) or value <= 0:
                raise ValueError(f"{name} must be positive and finite")
        if not callable(clock):
            raise TypeError("clock must be callable")
        self.capacity = float(capacity)
        self.refill_rate = float(refill_rate)
        self._tokens = self.capacity
        self._clock = clock
        self._updated = clock()
        if not math.isfinite(self._updated):
            raise ValueError("clock must return a finite timestamp")
        self._lock = threading.Lock()

    def _replenish(self) -> None:
        now = self._clock()
        if not math.isfinite(now):
            raise ValueError("clock must return a finite timestamp")
        elapsed = max(0.0, now - self._updated)
        self._tokens = min(self.capacity, self._tokens + elapsed * self.refill_rate)
        self._updated = max(self._updated, now)

    def try_acquire(self, tokens: float = 1.0) -> bool:
        """Atomically consume tokens if enough are available."""
        self._validate_amount(tokens)
        with self._lock:
            self._replenish()
            if self._tokens < tokens:
                return False
            self._tokens -= tokens
            return True

    def wait_time(self, tokens: float = 1.0) -> float:
        """Return seconds until the requested amount is available."""
        self._validate_amount(tokens)
        with self._lock:
            self._replenish()
            return max(0.0, (tokens - self._tokens) / self.refill_rate)

    @property
    def available(self) -> float:
        """Current available tokens, including elapsed-time replenishment."""
        with self._lock:
            self._replenish()
            return self._tokens

    def _validate_amount(self, tokens: float) -> None:
        if isinstance(tokens, bool) or not isinstance(tokens, (int, float)):
            raise TypeError("tokens must be a finite number")
        if not math.isfinite(tokens) or tokens <= 0 or tokens > self.capacity:
            raise ValueError("tokens must be positive, finite, and <= capacity")
