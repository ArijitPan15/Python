# Atomic JSON snapshots

A standard-library example of safe snapshot replacement for small local applications.
Requires Python 3.8+.

```python
from store import save, load
save("settings.json", {"theme": "dark"})
print(load("settings.json"))
```

Run from this directory: `python -m unittest -v`.

The temporary file lives in the destination directory, so replacement stays on the same filesystem. Serialization and file synchronization finish before replacement. Failures clean up the temporary file and leave the previous snapshot intact if replacement has not happened.

Limitations: the parent directory must exist. This is not a database or a locking mechanism; concurrent writers can overwrite each other's changes. Directory metadata is not synchronized, so power-loss durability is not guaranteed. Use a trusted directory and do not rely on this example to preserve existing file permissions.
