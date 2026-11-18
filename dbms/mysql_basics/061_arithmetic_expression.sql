-- Program 061: arithmetic expression
-- MySQL 8. Run independently in a scratch schema.
CREATE TABLE products (id INT PRIMARY KEY, price DECIMAL(8,2), quantity INT);
INSERT INTO products VALUES (1,20.00,3);
SELECT id,price*quantity AS total FROM products;
