-- Program 100: basic practice review
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, marks INT CHECK(marks BETWEEN 0 AND 100));
ALTER TABLE students ADD COLUMN city VARCHAR(30) DEFAULT 'Kolkata';
INSERT INTO students (name,marks) VALUES ('Asha',85),('Ravi',65),('Mira',35);
UPDATE students SET marks=70 WHERE name='Ravi';
DELETE FROM students WHERE marks<40;
SELECT name,marks,city FROM students ORDER BY marks DESC;
ALTER TABLE students DROP COLUMN city;
DESCRIBE students;
