-- Program 097: begin commit
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE accounts (id INT PRIMARY KEY, balance DECIMAL(10,2));
INSERT INTO accounts VALUES (1,100.00);
START TRANSACTION;
UPDATE accounts SET balance=balance+25 WHERE id=1;
COMMIT;
SELECT * FROM accounts;
