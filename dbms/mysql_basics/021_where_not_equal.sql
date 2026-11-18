-- Program 021: where not equal
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE students(id INT PRIMARY KEY,name VARCHAR(40));
INSERT INTO students VALUES(1,'Asha'),(2,'Ravi');
SELECT * FROM students WHERE id <> 1;
