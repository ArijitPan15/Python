-- Program 089: drop view
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(40));
CREATE VIEW student_names AS SELECT name FROM students;
DROP VIEW student_names;
SHOW FULL TABLES WHERE Table_type='VIEW';
