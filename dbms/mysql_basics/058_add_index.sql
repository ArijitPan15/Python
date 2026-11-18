-- Program 058: add index
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE students (id INT PRIMARY KEY, city VARCHAR(60));
CREATE INDEX idx_students_city ON students(city);
SHOW INDEX FROM students;
