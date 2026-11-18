-- Program 049: check constraint
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE products (id INT PRIMARY KEY, price DECIMAL(10,2) CHECK (price >= 0));
INSERT INTO products VALUES (1,10.50);
SHOW CREATE TABLE products;
