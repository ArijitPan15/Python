-- Program 062: column concatenation
-- MySQL 8. Run independently in a scratch schema.
CREATE TABLE people (first_name VARCHAR(40), last_name VARCHAR(40));
INSERT INTO people VALUES ('Asha','Sen');
SELECT CONCAT(first_name,' ',last_name) AS full_name FROM people;
