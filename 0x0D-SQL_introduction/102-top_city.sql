--  lists average of cities
SELECT city, AVG(value) avg_temp FROM temperatures GROUP BY city 
	ORDER BY avg_temp DESC LIMIT 3;
