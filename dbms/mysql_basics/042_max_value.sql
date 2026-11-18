-- Program 042: max value
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE scores (id INT PRIMARY KEY, marks INT);
INSERT INTO scores VALUES (1,80),(2,50);
SELECT MAX(marks) AS maximum_marks FROM scores;
