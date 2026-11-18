-- Program 091: left join intro
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE departments (id INT PRIMARY KEY, name VARCHAR(40));
CREATE TABLE employees (id INT PRIMARY KEY, name VARCHAR(40), dept_id INT);
INSERT INTO departments VALUES (1,'IT');
INSERT INTO employees VALUES (10,'Asha',1),(11,'Ravi',NULL);
SELECT e.name,d.name AS department FROM employees e LEFT JOIN departments d ON e.dept_id=d.id;
