-- 003: WHERE, BETWEEN, LIKE, ORDER BY, and LIMIT.
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL);
INSERT INTO products VALUES
(1,'USB Cable','Electronics',9.50),
(2,'USB Hub','Electronics',25.00),
(3,'Notebook','Stationery',4.25),
(4,'Wireless Mouse','Electronics',18.00);
-- Verification: Mouse and Hub, ordered by descending price.
SELECT name, price FROM products
WHERE category = 'Electronics' AND price BETWEEN 15 AND 30
ORDER BY price DESC LIMIT 5;
