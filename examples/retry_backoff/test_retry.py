import unittest
from retry import retry_call


class RetryTests(unittest.TestCase):
    def test_success_without_delay(self):
        delays = []
        self.assertEqual(7, retry_call(lambda: 7, sleep=delays.append))
        self.assertEqual([], delays)

    def test_transient_failure_then_success(self):
        calls, delays = [], []

        def unstable():
            calls.append(1)
            if len(calls) < 3:
                raise ConnectionError("temporary")
            return "ok"

        self.assertEqual("ok", retry_call(unstable, initial_delay=0.5, max_delay=0.75, sleep=delays.append))
        self.assertEqual([0.5, 0.75], delays)

    def test_final_exception_is_preserved(self):
        delays = []
        with self.assertRaisesRegex(OSError, "still down"):
            retry_call(lambda: (_ for _ in ()).throw(OSError("still down")), attempts=2, sleep=delays.append)
        self.assertEqual([0.1], delays)

    def test_unselected_exception_is_not_retried(self):
        delays = []
        with self.assertRaises(ValueError):
            retry_call(lambda: (_ for _ in ()).throw(ValueError("bad input")), sleep=delays.append)
        self.assertEqual([], delays)

    def test_deterministic_jitter(self):
        delays = []
        with self.assertRaises(OSError):
            retry_call(lambda: (_ for _ in ()).throw(OSError()), attempts=2, jitter=0.4, random_value=lambda: 0.5, sleep=delays.append)
        self.assertAlmostEqual(0.3, delays[0])

    def test_invalid_arguments(self):
        for options in ({"attempts": 0}, {"attempts": True}, {"initial_delay": -1}, {"multiplier": 0.5}, {"max_delay": -1}, {"jitter": -1}, {"retry_on": ()}, {"retry_on": (BaseException,)}):
            with self.subTest(options=options), self.assertRaises(ValueError):
                retry_call(lambda: 1, **options)

    def test_custom_retry_exception(self):
        calls = []
        def task():
            calls.append(1)
            if len(calls) == 1:
                raise ValueError("retry me")
            return 12
        self.assertEqual(12, retry_call(task, retry_on=(ValueError,), sleep=lambda _: None))


if __name__ == "__main__":
    unittest.main()
