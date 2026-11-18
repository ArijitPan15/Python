-- Program 044: default constraint
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE users (id INT PRIMARY KEY, status VARCHAR(20) DEFAULT 'active');
INSERT INTO users (id) VALUES (1);
SELECT * FROM users;
