-- Program 079: case expression
-- MySQL 8. Run independently in a scratch schema.
CREATE TABLE scores (id INT PRIMARY KEY, marks INT);
INSERT INTO scores VALUES (1,85),(2,40);
SELECT id,CASE WHEN marks>=50 THEN 'Pass' ELSE 'Fail' END AS result FROM scores;
