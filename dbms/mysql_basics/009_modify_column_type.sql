-- Program 009: modify column type
-- MySQL 8. Run each file in a separate scratch database; some statements change or remove data.
-- Expected: inspect the final SELECT, SHOW, or DESCRIBE result.
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(20));
ALTER TABLE students MODIFY COLUMN name VARCHAR(100) NOT NULL;
DESCRIBE students;
