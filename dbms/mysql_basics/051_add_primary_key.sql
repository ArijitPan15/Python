-- Program 051: add primary key
-- MySQL 8. Execute independently in a clean practice schema.
CREATE TABLE subjects (id INT NOT NULL, title VARCHAR(50));
ALTER TABLE subjects ADD PRIMARY KEY (id);
SHOW KEYS FROM subjects;
