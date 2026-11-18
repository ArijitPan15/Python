-- Program 014: insert multiple rows
-- MySQL 8. Run each file in a separate scratch database; some statements change or remove data.
-- Expected: inspect the final SELECT, SHOW, or DESCRIBE result.
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(60));
INSERT INTO students VALUES (1,'Asha'),(2,'Ravi'),(3,'Mira');
SELECT * FROM students;
