-- lists all genres contained in hbtn_0d_tvshows
SELECT g.name genre, count(sg.genre_id) number_of_shows FROM tv_genres g JOIN tv_show_genres sg ON sg.genre_id = g.id
	GROUP BY g.name ORDER BY number_of_shows DESC;
