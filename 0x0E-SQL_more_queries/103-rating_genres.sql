-- lists all ratings from hbtn_0d_tvshows_rate by their rating
SELECT g.name, SUM(r.rate) rating FROM tv_genres g
	LEFT JOIN tv_show_genres sg ON g.id = sg.genre_id
	LEFT JOIN tv_show_ratings r ON r.show_id = sg.show_id
	GROUP BY g.name ORDER BY rating DESC;
