-- Program 040: limit one
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE scores(id INT PRIMARY KEY,marks INT);
INSERT INTO scores VALUES(1,80),(2,95);
SELECT * FROM scores ORDER BY marks DESC LIMIT 1;
