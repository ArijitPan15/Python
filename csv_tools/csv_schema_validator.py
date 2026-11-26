"""Validate CSV records against a small, explicit schema.

No third-party dependencies. Run with:
    python csv_schema_validator.py input.csv --required name age --integer age
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ValidationIssue:
    row: int
    column: str
    message: str


def validate_csv(
    path: str | Path,
    required: set[str],
    integer_columns: set[str] | None = None,
) -> list[ValidationIssue]:
    """Return all issues; row numbers match physical CSV header + data rows.

    Empty files and duplicate header names are reported instead of silently
    accepted. Values are stripped for validation but source data is untouched.
    """
    integer_columns = integer_columns or set()
    issues: list[ValidationIssue] = []
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader, None)
        if header is None:
            return [ValidationIssue(1, "*", "missing header")]
        names = [name.strip() for name in header]
        for name in set(names):
            if names.count(name) > 1:
                issues.append(ValidationIssue(1, name, "duplicate column"))
        for name in sorted((required | integer_columns) - set(names)):
            if name not in names:
                issues.append(ValidationIssue(1, name, "missing column"))
        for row_number, values in enumerate(reader, start=2):
            if len(values) != len(names):
                issues.append(ValidationIssue(row_number, "*", "column count mismatch"))
            record = dict(zip(names, values))
            for name in sorted(required):
                if name in names and not record.get(name, "").strip():
                    issues.append(ValidationIssue(row_number, name, "required value is empty"))
            for name in sorted(integer_columns):
                if name in names and record.get(name, "").strip():
                    try:
                        int(record[name].strip())
                    except ValueError:
                        issues.append(ValidationIssue(row_number, name, "not an integer"))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--required", nargs="*", default=[])
    parser.add_argument("--integer", nargs="*", default=[])
    args = parser.parse_args()
    try:
        issues = validate_csv(args.file, set(args.required), set(args.integer))
    except (OSError, UnicodeError, csv.Error) as exc:
        parser.error(str(exc))
    for issue in issues:
        print(f"row {issue.row}, {issue.column}: {issue.message}")
    if not issues:
        print("CSV validation passed")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
