# DBMS Practice: 200 Exercises

A structured, practical DBMS learning track. Each exercise is numbered and includes a learning objective, runnable SQL, and a verification query where applicable.

## Database dialect
Exercises 001–020 use SQLite 3 (including recursive CTE and window-function features supported in modern SQLite). Run with `sqlite3 :memory: < dbms/sqlite/001_schema_and_constraints.sql` from the repository root.

## Roadmap
- 001–020: relational schema, constraints, CRUD, filtering, joins, grouping, subqueries, views, CTEs, windows, and transactions
- 021–040: indexes, query plans, integrity, and performance
- 041–060: advanced joins, set operations, and analytic SQL
- 061–080: normalization, functional dependencies, and schema refactoring
- 081–100: transactions, isolation, concurrency, and recovery
- 101–120: PostgreSQL functions, procedures, and triggers
- 121–140: database security and access control
- 141–160: Python sqlite3 integration and parameterized queries
- 161–180: reporting, analytics, and ETL
- 181–200: mini-projects and practical database design

The roadmap describes planned topics; only files present in this directory are implemented.

## How to run
```bash
sqlite3 :memory: < dbms/sqlite/001_schema_and_constraints.sql
```

SQLite is required for SQL examples. Use an isolated practice database; some examples create and modify tables.

## Contributions
Prefer coherent, tested exercises with clear explanations. Commits do not automatically count toward GitHub's contribution graph.
