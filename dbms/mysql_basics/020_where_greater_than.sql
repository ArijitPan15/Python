-- Program 020: where greater than
-- MySQL 8. Run each file in a separate scratch database; some statements change or remove data.
-- Expected: inspect the final SELECT, SHOW, or DESCRIBE result.
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(60), marks INT);
INSERT INTO students VALUES (1,'Asha',85),(2,'Ravi',55);
SELECT name FROM students WHERE marks > 60;
