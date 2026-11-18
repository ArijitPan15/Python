-- 001: Create relational tables with primary, foreign, and CHECK constraints.
-- Goal: model students and courses with valid enrollment relationships.
PRAGMA foreign_keys = ON;
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL CHECK(length(trim(full_name)) > 0),
    email TEXT NOT NULL UNIQUE
);
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL UNIQUE,
    credits INTEGER NOT NULL CHECK(credits BETWEEN 1 AND 6)
);
CREATE TABLE enrollments (
    student_id INTEGER NOT NULL REFERENCES students(student_id),
    course_id INTEGER NOT NULL REFERENCES courses(course_id),
    grade TEXT CHECK(grade IN ('A','B','C','D','F')),
    PRIMARY KEY (student_id, course_id)
);
INSERT INTO students VALUES (1, 'Asha Sen', 'asha@example.test');
INSERT INTO courses VALUES (10, 'Database Systems', 4);
INSERT INTO enrollments VALUES (1, 10, 'A');
-- Verification: expect 1 row.
SELECT s.full_name, c.course_name, e.grade
FROM enrollments e
JOIN students s USING(student_id)
JOIN courses c USING(course_id);
