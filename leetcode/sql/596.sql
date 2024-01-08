-- # Write your MySQL query statement below
SELECT class
FROM (
    SELECT class, COUNT(class) AS students
    FROM Courses 
    GROUP BY class
) AS student_count_table 
WHERE students >= 5;

-- ALTERNATE SOLUTION
-- SELECT class
-- FROM Courses
-- GROUP BY class
-- HAVING COUNT(class) >= 5;

-- SCHEMA
-- Create table If Not Exists Courses (student varchar(255), class varchar(255))
-- Truncate table Courses
-- insert into Courses (student, class) values ('A', 'Math')
-- insert into Courses (student, class) values ('B', 'English')
-- insert into Courses (student, class) values ('C', 'Math')
-- insert into Courses (student, class) values ('D', 'Biology')
-- insert into Courses (student, class) values ('E', 'Math')
-- insert into Courses (student, class) values ('F', 'Computer')
-- insert into Courses (student, class) values ('G', 'Math')
-- insert into Courses (student, class) values ('H', 'Math')
-- insert into Courses (student, class) values ('I', 'Math')