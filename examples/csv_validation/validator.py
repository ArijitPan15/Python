"""Dependency-free CSV validation with row-level diagnostics."""
import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Issue:
    row: int
    column: str
    message: str


def validate_csv(path, required=("name", "email", "age")):
    """Return (valid_records, issues). Row numbers refer to physical CSV lines."""
    records, issues = [], []
    with Path(path).open("r", newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        headers = reader.fieldnames or []
        missing = [field for field in required if field not in headers]
        if missing:
            return [], [Issue(1, field, "missing required header") for field in missing]
        if len(headers) != len(set(headers)):
            return [], [Issue(1, "*", "duplicate headers")]
        for row in reader:
            number = reader.line_num
            row_issues = []
            if None in row:
                row_issues.append(Issue(number, "*", "extra fields"))
            for field in required:
                if not (row.get(field) or "").strip():
                    row_issues.append(Issue(number, field, "value required"))
            email = (row.get("email") or "").strip()
            if email and (email.count("@") != 1 or "." not in email.split("@")[-1]):
                row_issues.append(Issue(number, "email", "invalid email format"))
            age = (row.get("age") or "").strip()
            if age:
                try:
                    value = int(age)
                    if not 0 <= value <= 130:
                        raise ValueError
                except ValueError:
                    row_issues.append(Issue(number, "age", "must be an integer from 0 to 130"))
            if row_issues:
                issues.extend(row_issues)
            else:
                records.append({key: value.strip() if isinstance(value, str) else value
                                for key, value in row.items()})
    return records, issues


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Validate a CSV of name,email,age records")
    parser.add_argument("path")
    args = parser.parse_args()
    valid, errors = validate_csv(args.path)
    print(f"Valid rows: {len(valid)}; issues: {len(errors)}")
    for issue in errors:
        print(f"line {issue.row}, {issue.column}: {issue.message}")
    raise SystemExit(1 if errors else 0)
