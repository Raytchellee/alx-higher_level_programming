--  lists average of cities
SELECT city, AVG(value) avg_temp FROM temperatures 
	WHERE month between 7 and 8
	GROUP BY city 
	ORDER BY avg_temp DESC LIMIT 3;
