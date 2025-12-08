CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT 
            -- Return the salary only if N >= 1, otherwise the outer SELECT will evaluate to NULL.
            CASE WHEN N >= 1 THEN
                (
                    SELECT DISTINCT e.salary
                    FROM Employee e
                    ORDER BY e.salary DESC
                    LIMIT 1
                    OFFSET (N - 1)
                )
            ELSE
                NULL
            END
  );
END;
$$ LANGUAGE plpgsql;