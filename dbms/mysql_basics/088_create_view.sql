-- Program 088: create view
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(40), marks INT);
INSERT INTO students VALUES (1,'Asha',85),(2,'Ravi',35);
CREATE VIEW passing_students AS SELECT name,marks FROM students WHERE marks>=40;
SELECT * FROM passing_students;
