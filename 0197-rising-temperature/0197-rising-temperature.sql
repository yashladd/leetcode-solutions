-- Write your PostgreSQL query statement below
select w.id as id
from weather w
left join weather v
on w.recordDate = v.recordDate + 1 
where w.temperature > v.temperature;