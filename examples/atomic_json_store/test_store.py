import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from store import load, save


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.path = Path(directory.name) / "data.json"

    def test_round_trip(self):
        value = {"name": "বাংলা", "items": [1, None, True]}
        save(self.path, value)
        self.assertEqual(load(self.path), value)

    def test_replace(self):
        save(self.path, [1])
        save(self.path, [2])
        self.assertEqual(load(self.path), [2])

    def test_serialization_failure_preserves_previous_value(self):
        save(self.path, {"old": True})
        with self.assertRaises(TypeError):
            save(self.path, {"bad": object()})
        self.assertEqual(load(self.path), {"old": True})
        self.assertEqual(list(self.path.parent.iterdir()), [self.path])

    def test_replace_failure_cleans_temporary_file(self):
        save(self.path, 1)
        with patch("store.os.replace", side_effect=OSError("failure")):
            with self.assertRaises(OSError):
                save(self.path, 2)
        self.assertEqual(load(self.path), 1)
        self.assertEqual(list(self.path.parent.iterdir()), [self.path])

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            load(self.path)


if __name__ == "__main__":
    unittest.main()
