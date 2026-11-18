-- 007: Correlated subquery finds employees earning above department average.
CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER);
INSERT INTO employees VALUES
(1,'Asha','IT',70000),(2,'Ravi','IT',50000),
(3,'Mira','HR',45000),(4,'Nila','HR',55000);
-- Verification: Asha and Nila.
SELECT e.name, e.dept, e.salary FROM employees e
WHERE e.salary > (
    SELECT AVG(inner_e.salary) FROM employees inner_e WHERE inner_e.dept = e.dept
)
ORDER BY e.name;
