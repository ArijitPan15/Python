-- Program 011: truncate table
-- MySQL 8. Run each file in a separate scratch database; some statements change or remove data.
-- Expected: inspect the final SELECT, SHOW, or DESCRIBE result.
CREATE TABLE students (id INT PRIMARY KEY);
INSERT INTO students VALUES (1),(2);
TRUNCATE TABLE students;
SELECT COUNT(*) AS remaining FROM students;
