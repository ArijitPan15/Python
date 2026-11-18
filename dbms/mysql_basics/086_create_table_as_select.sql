-- Program 086: create table as select
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(40), marks INT);
INSERT INTO students VALUES (1,'Asha',85),(2,'Ravi',35);
CREATE TABLE passed_students AS SELECT id,name FROM students WHERE marks>=40;
SELECT * FROM passed_students;
