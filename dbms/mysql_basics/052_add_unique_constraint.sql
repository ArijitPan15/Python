-- Program 052: add unique constraint
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE users (id INT PRIMARY KEY, email VARCHAR(100));
ALTER TABLE users ADD CONSTRAINT uq_users_email UNIQUE (email);
SHOW INDEX FROM users;
