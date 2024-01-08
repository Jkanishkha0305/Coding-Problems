-- # Write your MySQL query statement below
SELECT *,
       CASE
           WHEN X + Y > Z AND X + Z > Y AND Y + Z > X THEN 'Yes'
           ELSE 'No'
       END AS triangle
FROM Triangle;


-- SCHEMA
-- Create table If Not Exists Triangle (x int, y int, z int)
-- Truncate table Triangle
-- insert into Triangle (x, y, z) values ('13', '15', '30')
-- insert into Triangle (x, y, z) values ('10', '20', '15')