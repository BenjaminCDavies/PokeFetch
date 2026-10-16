SELECT *
FROM pokemon
ORDER BY pokedex_number
LIMIT :limit OFFSET :offset;