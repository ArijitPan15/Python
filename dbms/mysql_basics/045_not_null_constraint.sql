-- Program 045: not null constraint
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE employees (id INT PRIMARY KEY, name VARCHAR(60) NOT NULL);
INSERT INTO employees VALUES (1,'Asha');
DESCRIBE employees;
