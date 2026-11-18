-- Program 095: subquery in
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(40), dept_id INT);
CREATE TABLE departments (id INT PRIMARY KEY, name VARCHAR(40));
INSERT INTO departments VALUES (1,'IT'),(2,'HR');
INSERT INTO students VALUES (10,'Asha',1),(11,'Mira',2);
SELECT name FROM students WHERE dept_id IN (SELECT id FROM departments WHERE name='IT');
