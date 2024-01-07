-- # Write your MySQL query statement below
SELECT E.name AS Employee
FROM Employee E
JOIN Employee M ON E.managerId = M.id
WHERE E.salary > M.salary;

-- SCHEMA
-- Create table If Not Exists Employee (id int, name varchar(255), salary int, managerId int)
-- Truncate table Employee
-- insert into Employee (id, name, salary, managerId) values ('1', 'Joe', '70000', '3')
-- insert into Employee (id, name, salary, managerId) values ('2', 'Henry', '80000', '4')
-- insert into Employee (id, name, salary, managerId) values ('3', 'Sam', '60000', 'None')
-- insert into Employee (id, name, salary, managerId) values ('4', 'Max', '90000', 'None')