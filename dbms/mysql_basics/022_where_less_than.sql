-- Program 022: where less than
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE students(id INT PRIMARY KEY,marks INT);
INSERT INTO students VALUES(1,90),(2,40);
SELECT * FROM students WHERE marks < 50;
