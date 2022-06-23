SELECT 
wc.id,
wc.CountryCode,
wc.name,
wc.Population,
c.name AS "country name",
wcl.language,
wcl.percentage

FROM  world.city wc

JOIN world.countrylanguage wcl
		ON  wc.CountryCode=wcl.CountryCode
JOIN world.country c
	ON c.Code = wc.CountryCode
    -- AND --> weitere Dinge möglich, die aber hier nicht passen
    
WHERE wc.Population BETWEEN 100000 AND 150000

ORDER BY wc.name