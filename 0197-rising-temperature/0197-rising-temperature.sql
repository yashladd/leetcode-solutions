SELECT w.id as id
FROM weather w
WHERE w.temperature > (
    SELECT w1.temperature 
    FROM weather w1
    WHERE w1.recordDate = w.recordDate - INTERVAL '1 day'
);