-- Program 025: where not in
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE students(id INT PRIMARY KEY,city VARCHAR(30));
INSERT INTO students VALUES(1,'Delhi'),(2,'Pune'),(3,'Kolkata');
SELECT * FROM students WHERE city NOT IN ('Delhi','Pune');
