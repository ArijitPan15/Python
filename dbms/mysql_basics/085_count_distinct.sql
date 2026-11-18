-- Program 085: count distinct
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE students (id INT PRIMARY KEY, city VARCHAR(30));
INSERT INTO students VALUES (1,'Delhi'),(2,'Delhi'),(3,'Pune');
SELECT COUNT(DISTINCT city) AS city_count FROM students;
