-- lists all shows contained in hbtn_0d_tvshows
SELECT s.title FROM tv_shows s WHERE s.title NOT IN 
	(SELECT s.title FROM tv_show_genres sg 
	JOIN tv_shows s ON sg.show_id = s.id 
	JOIN tv_genres g ON g.id = sg.genre_id
	AND g.name = 'Comedy')
	ORDER BY s.title ASC;
