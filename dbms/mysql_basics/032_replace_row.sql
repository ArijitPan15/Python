-- Program 032: replace row
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE settings(id INT PRIMARY KEY,value_text VARCHAR(30));
INSERT INTO settings VALUES(1,'old');
REPLACE INTO settings VALUES(1,'new');
SELECT * FROM settings;
