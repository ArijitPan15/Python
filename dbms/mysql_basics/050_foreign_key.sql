-- Program 050: foreign key
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE departments (id INT PRIMARY KEY);
CREATE TABLE employees (id INT PRIMARY KEY, dept_id INT, FOREIGN KEY (dept_id) REFERENCES departments(id));
INSERT INTO departments VALUES (10);
INSERT INTO employees VALUES (1,10);
SHOW CREATE TABLE employees;
