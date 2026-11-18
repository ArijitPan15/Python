-- Program 053: drop unique index
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE users (id INT PRIMARY KEY, email VARCHAR(100), CONSTRAINT uq_email UNIQUE (email));
ALTER TABLE users DROP INDEX uq_email;
SHOW INDEX FROM users;
