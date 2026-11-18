-- Program 006: add multiple columns
-- MySQL 8. Run each file in a separate scratch database; some statements change or remove data.
-- Expected: inspect the final SELECT, SHOW, or DESCRIBE result.
CREATE TABLE students (id INT PRIMARY KEY);
ALTER TABLE students ADD COLUMN name VARCHAR(60), ADD COLUMN age INT;
DESCRIBE students;
