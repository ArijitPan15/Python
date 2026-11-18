-- Program 039: sort null values
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE contacts(id INT PRIMARY KEY,email VARCHAR(40));
INSERT INTO contacts VALUES(1,NULL),(2,'a@example.test');
SELECT * FROM contacts ORDER BY email IS NULL,email;
