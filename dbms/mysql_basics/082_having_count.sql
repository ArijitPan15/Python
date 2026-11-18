-- Program 082: having count
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE students (id INT PRIMARY KEY, city VARCHAR(30));
INSERT INTO students VALUES (1,'Delhi'),(2,'Delhi'),(3,'Pune');
SELECT city,COUNT(*) AS students FROM students GROUP BY city HAVING COUNT(*)>1;
