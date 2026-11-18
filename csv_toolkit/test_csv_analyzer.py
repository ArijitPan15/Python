"""Tests for CSV profiling. Run from this folder using unittest discover."""
import tempfile
import unittest
from pathlib import Path
from csv_analyzer import profile_csv


class CsvAnalyzerTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "sample.csv"

    def write(self, content):
        self.path.write_text(content, encoding="utf-8")

    def test_numeric_summary_and_missing_values(self):
        self.write("name,age\nAda,20\nBob,\nCara,30\n")
        report = profile_csv(self.path, ["age"])
        self.assertEqual(report["rows"], 3)
        self.assertEqual(report["missing"]["age"], 1)
        self.assertEqual(report["numeric"]["age"]["mean"], 25)
        self.assertEqual(report["numeric"]["age"]["median"], 25)

    def test_empty_file_rejected(self):
        self.write("")
        with self.assertRaisesRegex(ValueError, "header"):
            profile_csv(self.path)

    def test_duplicate_header_rejected(self):
        self.write("id,id\n1,2\n")
        with self.assertRaisesRegex(ValueError, "unique"):
            profile_csv(self.path)

    def test_unknown_numeric_column_rejected(self):
        self.write("id\n1\n")
        with self.assertRaisesRegex(ValueError, "Unknown"):
            profile_csv(self.path, ["price"])

    def test_invalid_numeric_value_rejected(self):
        self.write("price\nabc\n")
        with self.assertRaisesRegex(ValueError, "Row 2"):
            profile_csv(self.path, ["price"])

    def test_extra_csv_fields_rejected(self):
        self.write("name\nAda,extra\n")
        with self.assertRaisesRegex(ValueError, "extra fields"):
            profile_csv(self.path)

    def test_missing_csv_fields_rejected(self):
        self.write("name,age\nAda\n")
        with self.assertRaisesRegex(ValueError, "missing fields"):
            profile_csv(self.path)

    def test_no_numeric_values(self):
        self.write("price\n\n")
        report = profile_csv(self.path, ["price"])
        self.assertEqual(report["numeric"]["price"]["count"], 0)
        self.assertIsNone(report["numeric"]["price"]["mean"])

    def test_non_finite_values_rejected(self):
        self.write("price\nnan\n")
        with self.assertRaisesRegex(ValueError, "finite"):
            profile_csv(self.path, ["price"])


if __name__ == "__main__":
    unittest.main()
