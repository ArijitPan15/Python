-- 005: LEFT JOIN preserves customers with no orders.
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, total NUMERIC);
INSERT INTO customers VALUES (1,'Mina'),(2,'Rohit'),(3,'No orders');
INSERT INTO orders VALUES (10,1,250),(11,1,120);
-- Verification: includes customer 3 with zero orders.
SELECT c.id, c.name, COUNT(o.id) AS order_count, COALESCE(SUM(o.total),0) AS spend
FROM customers c LEFT JOIN orders o ON o.customer_id = c.id
GROUP BY c.id, c.name ORDER BY c.id;
