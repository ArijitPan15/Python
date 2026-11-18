-- Program 059: drop index
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE students (id INT PRIMARY KEY, city VARCHAR(60), INDEX idx_city(city));
DROP INDEX idx_city ON students;
SHOW INDEX FROM students;
