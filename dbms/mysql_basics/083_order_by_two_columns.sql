-- Program 083: order by two columns
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE students (id INT PRIMARY KEY, city VARCHAR(30), name VARCHAR(30));
INSERT INTO students VALUES (1,'Delhi','Zara'),(2,'Delhi','Asha'),(3,'Pune','Mira');
SELECT * FROM students ORDER BY city ASC,name ASC;
