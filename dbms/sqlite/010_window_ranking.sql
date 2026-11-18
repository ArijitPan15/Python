-- 010: ROW_NUMBER and DENSE_RANK within departments.
CREATE TABLE employees (name TEXT, dept TEXT, salary INTEGER);
INSERT INTO employees VALUES ('Asha','IT',70000),('Ravi','IT',70000),('Mina','IT',50000),('Nila','HR',60000);
SELECT name, dept, salary,
       ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC, name) AS row_num,
       DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS salary_rank
FROM employees ORDER BY dept, row_num;
-- Verification: IT employees with equal salaries share salary_rank 1.
