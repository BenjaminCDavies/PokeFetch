SELECT *
FROM pokemon
WHERE LOWER(name) = LOWER(:name)
LIMIT 1;