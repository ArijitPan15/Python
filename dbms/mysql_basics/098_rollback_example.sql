-- Program 098: rollback example
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE accounts (id INT PRIMARY KEY, balance DECIMAL(10,2)) ENGINE=InnoDB;
INSERT INTO accounts VALUES (1,100.00);
START TRANSACTION;
UPDATE accounts SET balance=0 WHERE id=1;
ROLLBACK;
SELECT * FROM accounts;
