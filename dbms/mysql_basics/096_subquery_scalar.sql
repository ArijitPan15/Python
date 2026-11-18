-- Program 096: subquery scalar
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(40), marks INT);
INSERT INTO students VALUES (1,'Asha',90),(2,'Ravi',60),(3,'Mira',75);
SELECT name FROM students WHERE marks > (SELECT AVG(marks) FROM students);
