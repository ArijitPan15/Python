# SQLite job queue

A dependency-free Python 3.10+ example of a persistent FIFO work queue.
Use a file-backed database (not :memory:, since operations open separate connections).

```python
from job_queue import JobQueue

queue = JobQueue("jobs.db")
queue.enqueue({"task": "send_report"})
job = queue.claim()
if job is not None:
    job_id, payload = job
    print(payload)
    queue.finish(job_id)
```

Run tests from this directory:

```sh
python -m unittest -v
```

BEGIN IMMEDIATE serializes competing claims; the selection and state transition
occur in one transaction. Each operation closes its connection. A worker must
explicitly finish a claimed job, with success=False for failure.

This is an educational example, not a production broker: it has no leases,
automatic retries, crash recovery, scheduling, or exactly-once processing.
A crashed worker leaves its job in running state. Use a dedicated broker or
implement recovery and idempotent handlers for production workloads.
