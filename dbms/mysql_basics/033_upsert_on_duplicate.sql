-- Program 033: upsert on duplicate
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE stock(sku VARCHAR(20) PRIMARY KEY,quantity INT);
INSERT INTO stock VALUES('P01',10);
INSERT INTO stock VALUES('P01',5) ON DUPLICATE KEY UPDATE quantity=quantity+VALUES(quantity);
SELECT * FROM stock;
