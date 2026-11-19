import unittest

from cpu_scheduling import Process, averages, schedule


class SchedulingTests(unittest.TestCase):
    def setUp(self):
        self.jobs = [Process("P1", 0, 7), Process("P2", 2, 4), Process("P3", 4, 1)]

    def test_fcfs_order_and_wait(self):
        result = schedule(self.jobs)
        self.assertEqual([r.pid for r in result], ["P1", "P2", "P3"])
        self.assertEqual([r.waiting for r in result], [0, 5, 7])

    def test_sjf_order_and_wait(self):
        result = schedule(self.jobs, "sjf")
        self.assertEqual([r.pid for r in result], ["P1", "P3", "P2"])
        self.assertEqual([r.waiting for r in result], [0, 3, 6])

    def test_idle_cpu(self):
        result = schedule([Process("P1", 5, 3)])
        self.assertEqual((result[0].start, result[0].waiting), (5, 0))

    def test_reject_duplicate_pid(self):
        with self.assertRaises(ValueError):
            schedule([Process("A", 0, 1), Process("A", 2, 2)])

    def test_invalid_process(self):
        with self.assertRaises(ValueError):
            Process("P1", -1, 2)
        with self.assertRaises(ValueError):
            Process("P1", 0, 0)

    def test_empty_average(self):
        self.assertEqual(averages([]), {"waiting": 0.0, "turnaround": 0.0})

    def test_average_calculation(self):
        summary = averages(schedule(self.jobs))
        self.assertAlmostEqual(summary["waiting"], 4)
        self.assertAlmostEqual(summary["turnaround"], 8)


if __name__ == "__main__":
    unittest.main()
