"""Atomic replacement of JSON snapshots (single-writer use)."""
import json
import os
import tempfile
from pathlib import Path


def save(path, value):
    path = Path(path)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent,
            prefix=".snapshot-", delete=False
        ) as stream:
            temporary = Path(stream.name)
            json.dump(value, stream, ensure_ascii=False, allow_nan=False)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def load(path):
    with Path(path).open(encoding="utf-8") as stream:
        return json.load(stream)
