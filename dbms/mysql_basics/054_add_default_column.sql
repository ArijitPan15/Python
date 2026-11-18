-- Program 054: add default column
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE tasks (id INT PRIMARY KEY);
ALTER TABLE tasks ADD COLUMN status VARCHAR(20) NOT NULL DEFAULT 'pending';
DESCRIBE tasks;
