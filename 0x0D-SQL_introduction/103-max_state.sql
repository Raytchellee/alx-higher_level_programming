-- displays the max temperature of each state (ordered by State)
SELECT state, MAX(value) max_temp FROM temperatures 
	GROUP  BY state
	ORDER BY state ASC 
	LIMIT 3;
