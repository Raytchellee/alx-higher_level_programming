-- lists all genres contained in hbtn_0d_tvshows
SELECT g.name FROM tv_genres g WHERE g.name NOT IN
	(SELECT g.name FROM tv_show_genres sg
	JOIN tv_shows s ON sg.show_id = s.id
	JOIN tv_genres g ON g.id = sg.genre_id
	AND s.title='Dexter')
	ORDER BY g.name ASC;
