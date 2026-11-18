-- Program 026: where not between
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE scores(id INT PRIMARY KEY,marks INT);
INSERT INTO scores VALUES(1,30),(2,60),(3,90);
SELECT * FROM scores WHERE marks NOT BETWEEN 40 AND 80;
