-- 009: CTE organizes multi-stage calculations.
CREATE TABLE purchases (customer TEXT, amount INTEGER);
INSERT INTO purchases VALUES ('Asha',50),('Asha',75),('Ravi',10),('Mina',120);
WITH totals AS (
    SELECT customer, SUM(amount) AS total FROM purchases GROUP BY customer
)
SELECT customer, total FROM totals WHERE total >= 100 ORDER BY total DESC;
-- Verification: Asha 125, Mina 120.
