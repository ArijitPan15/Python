-- Program 003: create table
-- MySQL 8. Run each file in a separate scratch database; some statements change or remove data.
-- Expected: inspect the final SELECT, SHOW, or DESCRIBE result.
CREATE TABLE IF NOT EXISTS students (id INT PRIMARY KEY, name VARCHAR(60));
SHOW TABLES;
