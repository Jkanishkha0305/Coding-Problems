-- # Write your MySQL query statement below
SELECT customer_number
FROM (
    SELECT customer_number, COUNT(customer_number) AS customer_count
    FROM Orders 
    GROUP BY customer_number
) AS count_table 
ORDER BY customer_count DESC
LIMIT 1;


-- SCHEMA
-- Create table If Not Exists orders (order_number int, customer_number int)
-- Truncate table orders
-- insert into orders (order_number, customer_number) values ('1', '1')
-- insert into orders (order_number, customer_number) values ('2', '2')
-- insert into orders (order_number, customer_number) values ('3', '3')
-- insert into orders (order_number, customer_number) values ('4', '3')