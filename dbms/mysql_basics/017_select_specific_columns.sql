-- Program 017: select specific columns
-- MySQL 8. Run each file in a separate scratch database; some statements change or remove data.
-- Expected: inspect the final SELECT, SHOW, or DESCRIBE result.
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(60), age INT);
INSERT INTO students VALUES (1,'Asha',20);
SELECT name,age FROM students;
