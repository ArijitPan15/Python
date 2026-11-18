-- Program 087: insert from select
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(40), marks INT);
CREATE TABLE honors (id INT PRIMARY KEY, name VARCHAR(40));
INSERT INTO students VALUES (1,'Asha',95),(2,'Ravi',50);
INSERT INTO honors SELECT id,name FROM students WHERE marks>=90;
SELECT * FROM honors;
