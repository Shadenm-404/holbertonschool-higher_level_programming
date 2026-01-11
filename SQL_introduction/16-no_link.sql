-- Lists all records with a valid name from second_table
-- Select records where name is not null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
