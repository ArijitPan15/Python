"""Regression tests for the CSV schema validator.

Run: python -m unittest discover -s csv_tools -p 'test_*.py'
"""
import tempfile
import unittest
from pathlib import Path

from csv_schema_validator import validate_csv


class CSVSchemaValidatorTests(unittest.TestCase):
    def check_csv(self, content, required=None, integers=None):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "sample.csv"
            file.write_text(content, encoding="utf-8")
            return validate_csv(file, set(required or []), set(integers or []))

    def test_valid_csv(self):
        self.assertEqual(self.check_csv("name,age\nAna,23\nBob,-2\n", {"name"}, {"age"}), [])

    def test_missing_header(self):
        issues = self.check_csv("")
        self.assertEqual((issues[0].row, issues[0].message), (1, "missing header"))

    def test_missing_required_column(self):
        issues = self.check_csv("age\n12\n", {"name"})
        self.assertIn("missing column", [issue.message for issue in issues])

    def test_empty_required_and_invalid_integer(self):
        issues = self.check_csv("name,age\n ,abc\n", {"name"}, {"age"})
        self.assertEqual({issue.message for issue in issues},
                         {"required value is empty", "not an integer"})

    def test_ragged_rows(self):
        issues = self.check_csv("name,age\nAna\n", {"name"}, {"age"})
        self.assertIn("column count mismatch", [issue.message for issue in issues])

    def test_duplicate_headers(self):
        issues = self.check_csv("name,name\nA,B\n")
        self.assertIn("duplicate column", [issue.message for issue in issues])

    def test_bom_and_whitespace(self):
        issues = self.check_csv("\ufeffname,age\n Ana , 4 \n", {"name"}, {"age"})
        self.assertEqual(issues, [])


if __name__ == "__main__":
    unittest.main()
