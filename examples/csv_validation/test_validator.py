"""Run: python -m unittest discover -s examples/csv_validation -p 'test_*.py'"""
import tempfile
import unittest
from pathlib import Path
from validator import validate_csv


class CSVValidationTests(unittest.TestCase):
    def check(self, content):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.csv"
            path.write_text(content, encoding="utf-8")
            return validate_csv(path)

    def test_valid_and_invalid_rows(self):
        valid, issues = self.check("name,email,age\nAda,ada@example.com,37\nBob,invalid,200\n")
        self.assertEqual(len(valid), 1)
        self.assertEqual(len(issues), 2)
        self.assertEqual({issue.column for issue in issues}, {"email", "age"})

    def test_missing_header(self):
        valid, issues = self.check("name,email\nAda,ada@example.com\n")
        self.assertFalse(valid)
        self.assertEqual(issues[0].column, "age")

    def test_extra_fields(self):
        valid, issues = self.check("name,email,age\nAda,ada@example.com,30,extra\n")
        self.assertFalse(valid)
        self.assertEqual(issues[0].message, "extra fields")

    def test_bom_and_quoted_commas(self):
        valid, issues = self.check("\ufeffname,email,age\n\"Lovelace, Ada\",ada@example.com,30\n")
        self.assertFalse(issues)
        self.assertEqual(valid[0]["name"], "Lovelace, Ada")


if __name__ == "__main__":
    unittest.main()
