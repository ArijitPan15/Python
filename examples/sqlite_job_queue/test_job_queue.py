import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from job_queue import JobQueue


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = str(Path(self.temp.name) / "jobs.db")
        self.queue = JobQueue(self.path)

    def test_empty(self):
        self.assertIsNone(self.queue.claim())

    def test_fifo_and_persistence(self):
        first = self.queue.enqueue({"value": 1})
        second = self.queue.enqueue({"value": 2})
        reopened = JobQueue(self.path)
        self.assertEqual(reopened.claim(), (first, {"value": 1}))
        self.assertEqual(reopened.claim(), (second, {"value": 2}))
        self.assertIsNone(reopened.claim())

    def test_finish_requires_claim(self):
        job = self.queue.enqueue({})
        self.assertFalse(self.queue.finish(job))
        self.queue.claim()
        self.assertTrue(self.queue.finish(job, success=False))
        self.assertFalse(self.queue.finish(job))

    def test_concurrent_claims_are_unique(self):
        expected = {self.queue.enqueue({"value": i}) for i in range(20)}
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(lambda _: self.queue.claim(), range(20)))
        self.assertEqual({row[0] for row in results}, expected)
        self.assertIsNone(self.queue.claim())


if __name__ == "__main__":
    unittest.main()
