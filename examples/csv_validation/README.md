# CSV validation toolkit

A dependency-free Python example demonstrating `csv.DictReader`, dataclasses, input validation, structured error reporting and unit tests.

## Usage

```bash
python examples/csv_validation/validator.py examples/csv_validation/sample.csv
python -m unittest discover -s examples/csv_validation -p 'test_*.py'
```

The CLI exits with status 1 when validation issues are found, making it suitable for scripts. Required headers are `name,email,age`. Empty required values, invalid email shapes, ages outside 0–130 and extra columns are reported with line numbers. Email validation is intentionally lightweight and not a standards-compliant deliverability check.

The parser accepts UTF-8 BOM and quoted CSV fields. It collects valid rows separately from row-level issues rather than aborting at the first invalid row.
