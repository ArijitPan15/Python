-- 008: EXISTS checks whether a related row is present.
CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE books (id INTEGER PRIMARY KEY, author_id INTEGER, title TEXT);
INSERT INTO authors VALUES (1,'Asha'),(2,'Mina'),(3,'Ravi');
INSERT INTO books VALUES (10,1,'SQL Basics'),(11,1,'Indexes'),(12,3,'Python');
-- Verification: Asha and Ravi.
SELECT a.name FROM authors a
WHERE EXISTS (SELECT 1 FROM books b WHERE b.author_id = a.id)
ORDER BY a.name;
