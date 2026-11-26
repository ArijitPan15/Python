# CSV Toolkit — Python Standard Library

A dependency-free CLI for CSV validation, missing-value counts, and numeric summaries (`count`, `min`, `max`, `mean`, `median`).

Create `sample.csv` with columns `name,age,salary` and sample rows, then run:

    python csv_analyzer.py sample.csv --numeric age,salary

From Python:

    from csv_analyzer import profile_csv
    report = profile_csv('sample.csv', numeric_columns=['age'])

Run tests from this directory:

    python -m unittest discover -s . -p 'test_*.py' -v

Python 3.10+; standard library only. The tool validates headers, row widths, unknown numeric columns, and non-finite values. Numeric values in selected columns are kept in memory for descriptive statistics.
