-- Write your PostgreSQL query statement below
select w.id as id
from weather w
left join weather v
on w.recordDate = v.recordDate + interval '1 day'
where w.temperature > v.temperature;