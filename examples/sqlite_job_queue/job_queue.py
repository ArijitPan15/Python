"""Persistent FIFO queue with atomic claims (Python 3.10+)."""
import json
import sqlite3
from contextlib import closing


class JobQueue:
    def __init__(self, path: str):
        self.path = path
        with closing(self._connect()) as db, db:
            db.execute("""CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY, payload TEXT NOT NULL,
                state TEXT NOT NULL DEFAULT 'pending'
                CHECK(state IN ('pending', 'running', 'done', 'failed'))
            )""")

    def _connect(self):
        return sqlite3.connect(self.path, timeout=10)

    def enqueue(self, payload: dict) -> int:
        with closing(self._connect()) as db, db:
            cursor = db.execute("INSERT INTO jobs(payload) VALUES (?)",
                                (json.dumps(payload),))
            return cursor.lastrowid

    def claim(self) -> tuple[int, dict] | None:
        with closing(self._connect()) as db, db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute(
                "SELECT id, payload FROM jobs WHERE state='pending' ORDER BY id LIMIT 1"
            ).fetchone()
            if row is None:
                return None
            db.execute("UPDATE jobs SET state='running' WHERE id=?", (row[0],))
            return row[0], json.loads(row[1])

    def finish(self, job_id: int, *, success: bool = True) -> bool:
        with closing(self._connect()) as db, db:
            cursor = db.execute(
                "UPDATE jobs SET state=? WHERE id=? AND state='running'",
                ("done" if success else "failed", job_id),
            )
            return cursor.rowcount == 1
