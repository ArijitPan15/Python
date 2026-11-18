-- Program 030: delete all rows
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE scratch(id INT PRIMARY KEY);
INSERT INTO scratch VALUES(1),(2);
DELETE FROM scratch;
SELECT COUNT(*) AS remaining FROM scratch;
