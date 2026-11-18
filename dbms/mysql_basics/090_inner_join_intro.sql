-- Program 090: inner join intro
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE departments (id INT PRIMARY KEY, name VARCHAR(40));
CREATE TABLE employees (id INT PRIMARY KEY, name VARCHAR(40), dept_id INT);
INSERT INTO departments VALUES (1,'IT'),(2,'HR');
INSERT INTO employees VALUES (10,'Asha',1),(11,'Mira',2);
SELECT e.name,d.name AS department FROM employees e INNER JOIN departments d ON e.dept_id=d.id;
