-- Program 099: savepoint example
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE inventory (id INT PRIMARY KEY, quantity INT) ENGINE=InnoDB;
INSERT INTO inventory VALUES (1,10);
START TRANSACTION;
UPDATE inventory SET quantity=9 WHERE id=1;
SAVEPOINT before_second_change;
UPDATE inventory SET quantity=0 WHERE id=1;
ROLLBACK TO SAVEPOINT before_second_change;
COMMIT;
SELECT * FROM inventory;
