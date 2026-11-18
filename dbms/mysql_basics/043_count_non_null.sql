-- Program 043: count non null
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE contacts (id INT PRIMARY KEY, email VARCHAR(80));
INSERT INTO contacts VALUES (1,NULL),(2,'a@example.test');
SELECT COUNT(email) AS email_count FROM contacts;
