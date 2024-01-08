-- # Write your MySQL query statement below
SELECT T.id 
FROM Weather T, Weather Y
WHERE T.recordDate = Y.recordDate + INTERVAL 1 DAY
AND T.temperature > Y.temperature


-- SCHEMA
-- Create table If Not Exists Weather (id int, recordDate date, temperature int)
-- Truncate table Weather
-- insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10')
-- insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25')
-- insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20')
-- insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30')