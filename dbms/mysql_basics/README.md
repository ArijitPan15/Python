# MySQL DBMS: 100 Beginner Programs

This folder contains **100 separately numbered SQL files** (`001`–`100`) for **MySQL 8**. The exercises start with basic database and table operations and progress gradually through filtering, constraints, functions, introductory joins, and transactions.

## Getting started

1. Install MySQL 8 and connect using MySQL CLI or Workbench.
2. Create a disposable practice database:
   ```sql
   CREATE DATABASE dbms_basic_lab;
   USE dbms_basic_lab;
   ```
3. Open **one** numbered SQL file and run it in the practice schema.
4. Inspect the last `SELECT`, `DESCRIBE`, or `SHOW` output.
5. Reset your scratch schema before trying another exercise that creates a table with the same name.

> **Warning:** Some exercises intentionally use `DELETE`, `DROP TABLE`, `DROP COLUMN`, `TRUNCATE`, and other destructive statements. Never run these examples against a real or production database.

## Learning path

| Programs | Topics |
| --- | --- |
| 001–012 | CREATE DATABASE, CREATE TABLE, ALTER TABLE ADD/DROP/RENAME/MODIFY COLUMN, TRUNCATE and DROP |
| 013–040 | INSERT, SELECT, WHERE, LIKE, ORDER BY, UPDATE, DELETE and introductory expressions |
| 041–060 | Aggregate functions, constraints, keys, indexes, and column positioning |
| 061–080 | String, numeric, date, NULL, and conditional functions |
| 081–100 | GROUP BY, HAVING, joins, UNION, subqueries, views, transactions, and review |

## Example: add a column

```sql
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(60));
ALTER TABLE students ADD COLUMN email VARCHAR(120);
DESCRIBE students;
```

## Example: delete a column

```sql
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(60), nickname VARCHAR(30));
ALTER TABLE students DROP COLUMN nickname;
DESCRIBE students;
```

## Important notes

- The `dbms/sqlite` folder contains separate SQLite examples; SQL dialects are not interchangeable.
- `CREATE TABLE ... AS SELECT` does not automatically copy source primary keys and indexes.
- `REPLACE INTO` deletes and reinserts a conflicting row; understand its implications before using it outside practice.
- The examples are learning material, not production migration scripts.
- SQL execution against MySQL has not been verified in this environment.
