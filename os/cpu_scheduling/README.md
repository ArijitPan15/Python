# OS: CPU Scheduling Simulator

A standard-library reference implementation for **First Come, First Served (FCFS)** and
**non-preemptive Shortest Job First (SJF)** CPU scheduling. Designed for
operating-systems practice; it does not schedule actual OS processes.

Each process has a unique ID, an arrival time, and a positive CPU burst.
The simulator reports start, finish, waiting, and turnaround times, and
computes average waiting/turnaround times. Idle CPU periods and ties are handled
deterministically (ties follow arrival time then input order).

Run the example:

```bash
python cpu_scheduling.py
```

Run unit tests from this directory:

```bash
python -m unittest discover -s . -p 'test_*.py' -v
```

**Formulas:** turnaround = finish - arrival; waiting = start - arrival.
SJF is non-preemptive; when a job starts, it runs until its burst finishes.
