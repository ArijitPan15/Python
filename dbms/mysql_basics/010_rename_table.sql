-- Program 010: rename table
-- MySQL 8. Run each file in a separate scratch database; some statements change or remove data.
-- Expected: inspect the final SELECT, SHOW, or DESCRIBE result.
CREATE TABLE learners (id INT PRIMARY KEY);
RENAME TABLE learners TO students;
SHOW TABLES;
