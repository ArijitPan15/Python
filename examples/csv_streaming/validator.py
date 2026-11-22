"""Streaming CSV schema validation using only the Python standard library."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterator, TextIO


@dataclass(frozen=True)
class Problem:
    row: int
    column: str
    message: str


def validate(stream: TextIO, required: tuple[str, ...], unique: str | None = None) -> Iterator[Problem]:
    """Yield problems without loading the entire CSV into memory.

    Row numbers are logical CSV record numbers, including the header (row 1).
    Duplicate detection uses memory proportional to distinct values in the
    selected unique column. Other validation is streaming.
    """
    reader = csv.DictReader(stream)
    if reader.fieldnames is None:
        yield Problem(1, "*", "missing header")
        return
    names = reader.fieldnames
    for name in required:
        if name not in names:
            yield Problem(1, name, "missing required column")
    if unique is not None and unique not in names:
        yield Problem(1, unique, "missing unique column")
    if len(names) != len(set(names)):
        yield Problem(1, "*", "duplicate header names")
    seen: set[str] = set()
    for number, record in enumerate(reader, start=2):
        if None in record:
            yield Problem(number, "*", "too many fields")
        for name in required:
            if name in names and (record.get(name) is None or not str(record[name]).strip()):
                yield Problem(number, name, "empty required value")
        if unique in names if unique is not None else False:
            value = record.get(unique)
            if value is not None and value.strip():
                if value in seen:
                    yield Problem(number, unique, "duplicate value")
                seen.add(value)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate CSV columns and rows")
    parser.add_argument("path", type=Path)
    parser.add_argument("--required", action="append", default=[], metavar="COLUMN")
    parser.add_argument("--unique", metavar="COLUMN")
    args = parser.parse_args(argv)
    try:
        with args.path.open("r", encoding="utf-8-sig", newline="") as stream:
            problems = list(validate(stream, tuple(args.required), args.unique))
    except (OSError, UnicodeError, csv.Error) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2
    for problem in problems:
        print(json.dumps(asdict(problem)))
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
