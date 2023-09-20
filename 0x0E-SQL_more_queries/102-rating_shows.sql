-- lists all ratings from hbtn_0d_tvshows_rate by their rating
SELECT s.title, SUM(r.rate) rating FROM tv_show_genres sg
	JOIN tv_shows s ON sg.show_id = s.id 
	JOIN tv_show_ratings r ON r.show_id = s.id
	GROUP BY s.title ORDER BY rating DESC;
