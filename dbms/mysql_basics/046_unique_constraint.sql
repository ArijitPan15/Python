-- Program 046: unique constraint
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE employees (id INT PRIMARY KEY, email VARCHAR(100) UNIQUE);
INSERT INTO employees VALUES (1,'asha@example.test');
SHOW INDEX FROM employees;
