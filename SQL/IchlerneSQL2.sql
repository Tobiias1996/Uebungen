SELECT * 
FROM world.country
WHERE Population BETWEEN 1 AND 100000 AND Code REGEXP "s"
ORDER by Population
LIMIT 10