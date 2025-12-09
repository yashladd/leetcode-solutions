-- Write your PostgreSQL query statement below
SELECT 
    CASE 
        -- If ID is even, it goes to the previous seat (id - 1)
        WHEN id % 2 = 0 THEN id - 1
        -- If ID is odd AND it's the last one, it stays (id)
        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM Seat) THEN id
        -- If ID is odd and NOT the last one, it goes to the next seat (id + 1)
        ELSE id + 1
    END AS id,
    student
FROM Seat
ORDER BY id ASC;