-- Program 038: sort by alias
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE products(id INT PRIMARY KEY,price INT,quantity INT);
INSERT INTO products VALUES(1,10,2),(2,15,3);
SELECT id,price*quantity AS total FROM products ORDER BY total DESC;
