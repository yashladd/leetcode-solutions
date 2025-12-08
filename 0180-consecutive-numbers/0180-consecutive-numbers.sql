-- Write your PostgreSQL query statement below
select distinct e1.num as ConsecutiveNums
from Logs e1
join Logs e2 on e1.id + 1 = e2.id
join Logs e3 on e2.id + 1 = e3.id
where e1.num = e2.num and e2.num = e3.num;
