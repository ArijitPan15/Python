-- 002: Practice INSERT, UPDATE, and DELETE with transaction boundaries.
CREATE TABLE inventory (sku TEXT PRIMARY KEY, item TEXT NOT NULL, quantity INTEGER NOT NULL CHECK(quantity >= 0));
BEGIN;
INSERT INTO inventory VALUES ('P01','Pen',20),('N01','Notebook',10);
UPDATE inventory SET quantity = quantity - 3 WHERE sku = 'P01';
DELETE FROM inventory WHERE sku = 'N01';
COMMIT;
-- Verification: one Pen row with quantity 17.
SELECT sku, item, quantity FROM inventory ORDER BY sku;
