-- Program 041: min value
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE scores (id INT PRIMARY KEY, marks INT);
INSERT INTO scores VALUES (1,80),(2,50);
SELECT MIN(marks) AS minimum_marks FROM scores;
