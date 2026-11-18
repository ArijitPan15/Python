-- Program 012: drop table
-- MySQL 8. Run each file in a separate scratch database; some statements change or remove data.
-- Expected: inspect the final SELECT, SHOW, or DESCRIBE result.
CREATE TABLE temporary_students (id INT PRIMARY KEY);
DROP TABLE IF EXISTS temporary_students;
SHOW TABLES LIKE 'temporary_students';
