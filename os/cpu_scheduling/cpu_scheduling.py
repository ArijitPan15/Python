"""Reference implementations of non-preemptive FCFS and SJF schedulers."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Process:
    pid: str
    arrival: int
    burst: int

    def __post_init__(self):
        if not self.pid:
            raise ValueError("pid must be nonempty")
        if self.arrival < 0 or self.burst <= 0:
            raise ValueError("arrival must be >= 0 and burst must be > 0")


@dataclass(frozen=True)
class Result:
    pid: str
    start: int
    finish: int
    waiting: int
    turnaround: int


def schedule(processes: list[Process], algorithm: str = "fcfs") -> list[Result]:
    """Run FCFS or non-preemptive shortest-job-first; ties use input order."""
    if algorithm not in {"fcfs", "sjf"}:
        raise ValueError("algorithm must be fcfs or sjf")
    if len({p.pid for p in processes}) != len(processes):
        raise ValueError("process IDs must be unique")

    pending = list(enumerate(processes))
    results = []
    now = 0
    while pending:
        available = [(i, p) for i, p in pending if p.arrival <= now]
        if not available:
            now = min(p.arrival for _, p in pending)
            available = [(i, p) for i, p in pending if p.arrival <= now]
        if algorithm == "fcfs":
            index, job = min(available, key=lambda pair: (pair[1].arrival, pair[0]))
        else:
            index, job = min(available, key=lambda pair: (pair[1].burst, pair[1].arrival, pair[0]))
        start = now
        now += job.burst
        results.append(Result(job.pid, start, now, start - job.arrival, now - job.arrival))
        pending.remove((index, job))
    return results


def averages(results: list[Result]) -> dict[str, float]:
    if not results:
        return {"waiting": 0.0, "turnaround": 0.0}
    return {
        "waiting": sum(r.waiting for r in results) / len(results),
        "turnaround": sum(r.turnaround for r in results) / len(results),
    }


if __name__ == "__main__":
    sample = [
        Process("P1", arrival=0, burst=7),
        Process("P2", arrival=2, burst=4),
        Process("P3", arrival=4, burst=1),
    ]
    for algorithm in ("fcfs", "sjf"):
        print(algorithm.upper(), schedule(sample, algorithm))
        print("Average times:", averages(schedule(sample, algorithm)))
