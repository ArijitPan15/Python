-- Program 047: primary key
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE departments (department_id INT PRIMARY KEY, name VARCHAR(60));
INSERT INTO departments VALUES (1,'IT');
SHOW KEYS FROM departments WHERE Key_name = 'PRIMARY';
