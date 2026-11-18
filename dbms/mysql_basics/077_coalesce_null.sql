-- Program 077: coalesce null
-- MySQL 8. Run independently in a scratch schema.
CREATE TABLE contacts (id INT PRIMARY KEY, phone VARCHAR(20));
INSERT INTO contacts VALUES (1,NULL),(2,'1234567890');
SELECT id,COALESCE(phone,'Not provided') AS phone_display FROM contacts;
