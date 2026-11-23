"""Deterministic tests: no sleeping or external services required."""

import math
import threading
import unittest

from limiter import TokenBucket


class FakeClock:
    def __init__(self):
        self.now = 0.0

    def __call__(self):
        return self.now


class TokenBucketTests(unittest.TestCase):
    def setUp(self):
        self.clock = FakeClock()
        self.bucket = TokenBucket(3, 2, clock=self.clock)

    def test_initial_burst(self):
        self.assertTrue(self.bucket.try_acquire(3))
        self.assertFalse(self.bucket.try_acquire())

    def test_partial_refill(self):
        self.bucket.try_acquire(3)
        self.clock.now = 0.25
        self.assertAlmostEqual(self.bucket.available, 0.5)
        self.assertTrue(self.bucket.try_acquire(0.5))

    def test_capacity_is_capped(self):
        self.clock.now = 100
        self.assertEqual(self.bucket.available, 3)

    def test_wait_time(self):
        self.bucket.try_acquire(3)
        self.assertAlmostEqual(self.bucket.wait_time(2), 1.0)
        self.clock.now = 0.5
        self.assertAlmostEqual(self.bucket.wait_time(2), 0.5)

    def test_clock_regression_does_not_double_count(self):
        self.bucket.try_acquire(3)
        self.clock.now = 1
        self.assertEqual(self.bucket.available, 2)
        self.clock.now = 0
        self.assertEqual(self.bucket.available, 2)
        self.clock.now = 1.5
        self.assertEqual(self.bucket.available, 3)

    def test_invalid_constructor_values(self):
        for value in (0, -1, math.inf, math.nan):
            with self.subTest(value=value), self.assertRaises(ValueError):
                TokenBucket(value, 1)
        with self.assertRaises(TypeError):
            TokenBucket(True, 1)

    def test_invalid_requests(self):
        for value in (0, -1, 4, math.inf, math.nan):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.bucket.try_acquire(value)
        with self.assertRaises(TypeError):
            self.bucket.wait_time(True)

    def test_concurrent_acquires_never_exceed_capacity(self):
        successes = []
        barrier = threading.Barrier(20)

        def worker():
            barrier.wait()
            successes.append(self.bucket.try_acquire())

        threads = [threading.Thread(target=worker) for _ in range(20)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual(sum(successes), 3)


if __name__ == "__main__":
    unittest.main()
