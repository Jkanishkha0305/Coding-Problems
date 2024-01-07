-- # Write your MySQL query statement below
SELECT P.email
FROM Person P
GROUP BY P.email
HAVING COUNT(*) > 1;


-- SCHEMA
-- Create table If Not Exists Person (id int, email varchar(255))
-- Truncate table Person
-- insert into Person (id, email) values ('1', 'a@b.com')
-- insert into Person (id, email) values ('2', 'c@d.com')
-- insert into Person (id, email) values ('3', 'a@b.com')