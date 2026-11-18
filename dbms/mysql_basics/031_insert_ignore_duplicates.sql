-- Program 031: insert ignore duplicates
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE students(id INT PRIMARY KEY,name VARCHAR(40));
INSERT INTO students VALUES(1,'Asha');
INSERT IGNORE INTO students VALUES(1,'Another');
SELECT * FROM students;
