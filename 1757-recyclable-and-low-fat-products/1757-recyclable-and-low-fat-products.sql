-- Write your PostgreSQL query statement below
select p.product_id from products as p
where p.low_fats = 'Y' and p.recyclable = 'Y';
