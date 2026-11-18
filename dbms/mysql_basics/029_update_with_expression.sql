-- Program 029: update with expression
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE products(id INT PRIMARY KEY,price DECIMAL(8,2));
INSERT INTO products VALUES(1,100.00),(2,200.00);
UPDATE products SET price=price*1.10 WHERE id=1;
SELECT * FROM products;
