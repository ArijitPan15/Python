# Streaming CSV validation (standard library)

A small Python CLI and reusable generator for checking CSV files without
third-party packages. It checks required columns, non-empty values, duplicate
headers, extra fields and optional uniqueness.

## Usage

```bash
python examples/csv_streaming/validator.py contacts.csv --required id --required name --unique id
python -m unittest discover -s examples/csv_streaming -v
```

Each validation error is emitted as one JSON object per line, with `row`,
`column` and `message`. Exit status is **0** for valid input, **1** for
validation errors and **2** for file/decoding/CSV read failures.

The generator uses constant memory for ordinary required-field checks; the
optional uniqueness check stores observed values in a set. CSV record numbers
count logical records, not physical lines for quoted multiline fields.

This example is intended for learning and small ETL jobs. It does not enforce
data types or normalize Unicode; add those rules for production pipelines.
