-- lists all genres contained in hbtn_0d_tvshows
SELECT s.title FROM tv_genres g JOIN tv_show_genres sg ON sg.genre_id = g.id
	JOIN tv_shows s ON sg.show_id = s.id
	WHERE g.name = 'Comedy'
	ORDER BY s.title ASC;
