"""CSV profiling with Python's standard library."""
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path
from statistics import mean, median


def profile_csv(path: str | Path, numeric_columns: list[str] | None = None) -> dict:
    """Summarize CSV rows, blank cells, and selected numeric columns."""
    numeric_columns = list(dict.fromkeys(numeric_columns or []))
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("CSV must contain a nonempty header")
        columns = reader.fieldnames
        if any(not column or not column.strip() for column in columns):
            raise ValueError("CSV headers must not be blank")
        if len(set(columns)) != len(columns):
            raise ValueError("CSV headers must be unique")
        unknown = sorted(set(numeric_columns) - set(columns))
        if unknown:
            raise ValueError(f"Unknown numeric columns: {', '.join(unknown)}")

        missing = Counter({column: 0 for column in columns})
        numeric_values: dict[str, list[float]] = {column: [] for column in numeric_columns}
        row_count = 0
        for row_count, row in enumerate(reader, start=1):
            if None in row:
                raise ValueError(f"Row {row_count + 1} contains extra fields")
            if any(row[column] is None for column in columns):
                raise ValueError(f"Row {row_count + 1} contains missing fields")
            for column in columns:
                value = row[column].strip()
                if not value:
                    missing[column] += 1
                    continue
                if column in numeric_values:
                    try:
                        number = float(value)
                    except ValueError as exc:
                        raise ValueError(
                            f"Row {row_count + 1}, column {column!r}: invalid number {value!r}"
                        ) from exc
                    if not math.isfinite(number):
                        raise ValueError(
                            f"Row {row_count + 1}, column {column!r}: number must be finite"
                        )
                    numeric_values[column].append(number)

    summary = {}
    for column, values in numeric_values.items():
        summary[column] = (
            {"count": len(values), "min": min(values), "max": max(values),
             "mean": mean(values), "median": median(values)}
            if values else {"count": 0, "min": None, "max": None,
                            "mean": None, "median": None}
        )
    return {"rows": row_count, "columns": columns, "missing": dict(missing),
            "numeric": summary}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Profile CSV missing values and numeric columns")
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--numeric", default="", help="Comma-separated numeric column names")
    arguments = parser.parse_args(argv)
    selected = [item.strip() for item in arguments.numeric.split(",") if item.strip()]
    try:
        report = profile_csv(arguments.csv_file, selected)
    except (OSError, ValueError, csv.Error) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
