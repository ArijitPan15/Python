-- Program 015: insert selected columns
-- MySQL 8. Run each file in a separate scratch database; some statements change or remove data.
-- Expected: inspect the final SELECT, SHOW, or DESCRIBE result.
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(60), city VARCHAR(60) DEFAULT 'Kolkata');
INSERT INTO students (id,name) VALUES (1,'Asha');
SELECT * FROM students;
