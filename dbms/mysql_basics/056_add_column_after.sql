-- Program 056: add column after
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(60));
ALTER TABLE students ADD COLUMN age INT AFTER name;
DESCRIBE students;
