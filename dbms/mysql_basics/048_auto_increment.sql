-- Program 048: auto increment
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE tickets (id INT AUTO_INCREMENT PRIMARY KEY, subject VARCHAR(80));
INSERT INTO tickets (subject) VALUES ('Login'),('Password reset');
SELECT * FROM tickets;
