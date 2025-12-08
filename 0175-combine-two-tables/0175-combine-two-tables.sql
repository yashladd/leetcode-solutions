-- Write your PostgreSQL query statement below
-- select p.fristName, p.lastName, o.city, o.state
-- from person as p join on address as o
-- where p.personId == o.personId;

SELECT p.firstName, p.lastName, o.city, o.state
FROM Person p
LEFT JOIN Address o ON p.personId = o.personId;