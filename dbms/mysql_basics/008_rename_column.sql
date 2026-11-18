-- Program 008: rename column
-- MySQL 8. Run each file in a separate scratch database; some statements change or remove data.
-- Expected: inspect the final SELECT, SHOW, or DESCRIBE result.
CREATE TABLE students (id INT PRIMARY KEY, student_name VARCHAR(60));
ALTER TABLE students RENAME COLUMN student_name TO full_name;
DESCRIBE students;
