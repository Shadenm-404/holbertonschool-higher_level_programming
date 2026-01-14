-- Lists all cities of California using a subquery
-- Results are sorted by cities.id in ascending order

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
