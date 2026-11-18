-- Program 023: where less equal
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE students(id INT PRIMARY KEY,marks INT);
INSERT INTO students VALUES(1,50),(2,80);
SELECT * FROM students WHERE marks <= 50;
