-- Program 057: change column name type
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE students (id INT PRIMARY KEY, age_text VARCHAR(10));
ALTER TABLE students CHANGE COLUMN age_text age INT;
DESCRIBE students;
