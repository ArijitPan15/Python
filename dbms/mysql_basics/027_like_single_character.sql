-- Program 027: like single character
-- MySQL 8. Execute in a clean practice schema.
CREATE TABLE words(word VARCHAR(30));
INSERT INTO words VALUES('cat'),('cot'),('coat');
SELECT word FROM words WHERE word LIKE 'c_t';
