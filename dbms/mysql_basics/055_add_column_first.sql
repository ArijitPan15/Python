-- Program 055: add column first
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE students (name VARCHAR(60));
ALTER TABLE students ADD COLUMN id INT FIRST;
DESCRIBE students;
