-- lists all genres contained in hbtn_0d_tvshows
SELECT g.name FROM tv_genres g JOIN tv_show_genres sg ON sg.genre_id = g.id
	JOIN tv_shows s ON sg.show_id = s.id
	WHERE s.title = 'DEXTER'
	ORDER BY g.name ASC;
