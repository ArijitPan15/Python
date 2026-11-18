-- 004: INNER JOIN matches rows with corresponding keys.
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), total NUMERIC NOT NULL);
INSERT INTO customers VALUES (1,'Mina'),(2,'Rohit'),(3,'No orders');
INSERT INTO orders VALUES (10,1,250),(11,1,120),(12,2,400);
-- Verification: three matched order rows; customer 3 is excluded.
SELECT c.name, o.id AS order_id, o.total
FROM customers c INNER JOIN orders o ON o.customer_id = c.id
ORDER BY o.id;
