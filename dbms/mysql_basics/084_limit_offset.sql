-- Program 084: limit offset
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE products (id INT PRIMARY KEY, name VARCHAR(30));
INSERT INTO products VALUES (1,'Pen'),(2,'Book'),(3,'Bag'),(4,'Pencil');
SELECT * FROM products ORDER BY id LIMIT 2 OFFSET 1;
