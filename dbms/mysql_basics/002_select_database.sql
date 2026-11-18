-- Program 002: select database
-- MySQL 8. Run each file in a separate scratch database; some statements change or remove data.
-- Expected: inspect the final SELECT, SHOW, or DESCRIBE result.
CREATE DATABASE IF NOT EXISTS dbms_practice;
USE dbms_practice;
SELECT DATABASE();
