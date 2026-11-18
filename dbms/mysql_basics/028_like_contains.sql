-- Program 028: like contains
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE courses(name VARCHAR(60));
INSERT INTO courses VALUES('Database Systems'),('Python'),('Advanced Database');
SELECT name FROM courses WHERE name LIKE '%Database%';
