"""Unit tests: python -m unittest discover -s examples/csv_streaming -v."""
import io
import unittest

from validator import Problem, validate


class CSVValidationTests(unittest.TestCase):
    def check(self, csv_text, required=("id", "name"), unique="id"):
        return list(validate(io.StringIO(csv_text), required, unique))

    def test_valid_records(self):
        self.assertEqual(self.check("id,name\n1,Alice\n2,Bob\n"), [])

    def test_missing_header(self):
        self.assertEqual(self.check(""), [Problem(1, "*", "missing header")])

    def test_missing_column(self):
        self.assertEqual(self.check("id\n1\n"), [Problem(1, "name", "missing required column")])

    def test_blank_and_duplicate(self):
        errors = self.check("id,name\n1,Alice\n1, \n")
        self.assertIn(Problem(3, "name", "empty required value"), errors)
        self.assertIn(Problem(3, "id", "duplicate value"), errors)

    def test_extra_fields(self):
        self.assertIn(Problem(2, "*", "too many fields"), self.check("id,name\n1,A,B\n"))

    def test_duplicate_headers(self):
        self.assertIn(Problem(1, "*", "duplicate header names"),
                      self.check("id,id,name\n1,2,A\n"))

    def test_multiline_quoted_field(self):
        self.assertEqual(self.check('id,name\n1,"Alice\nSmith"\n'), [])

    def test_missing_unique_column(self):
        self.assertIn(Problem(1, "other", "missing unique column"),
                      self.check("id,name\n1,A\n", unique="other"))


if __name__ == "__main__":
    unittest.main()
