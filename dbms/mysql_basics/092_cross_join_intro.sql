-- Program 092: cross join intro
-- MySQL 8. Run independently in a fresh practice schema.
CREATE TABLE sizes (size VARCHAR(5));
CREATE TABLE colors (color VARCHAR(10));
INSERT INTO sizes VALUES ('S'),('M');
INSERT INTO colors VALUES ('Red'),('Blue');
SELECT size,color FROM sizes CROSS JOIN colors;
