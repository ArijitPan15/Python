-- 006: GROUP BY and HAVING filter aggregated groups.
CREATE TABLE sales (id INTEGER PRIMARY KEY, region TEXT, amount INTEGER);
INSERT INTO sales VALUES (1,'East',100),(2,'East',300),(3,'West',90),(4,'West',110),(5,'North',40);
-- Verification: East (400) and West (200).
SELECT region, SUM(amount) AS total_sales
FROM sales GROUP BY region
HAVING SUM(amount) >= 200
ORDER BY total_sales DESC;
