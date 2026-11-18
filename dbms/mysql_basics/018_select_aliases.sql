-- Program 018: select aliases
-- MySQL 8. Run each file in a separate scratch database; some statements change or remove data.
-- Expected: inspect the final SELECT, SHOW, or DESCRIBE result.
CREATE TABLE students (id INT PRIMARY KEY, full_name VARCHAR(60));
INSERT INTO students VALUES (1,'Asha Sen');
SELECT full_name AS student_name FROM students;
