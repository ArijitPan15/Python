-- Program 081: group by category
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE products (id INT PRIMARY KEY, category VARCHAR(30));
INSERT INTO products VALUES (1,'Books'),(2,'Books'),(3,'Pens');
SELECT category,COUNT(*) AS item_count FROM products GROUP BY category;
