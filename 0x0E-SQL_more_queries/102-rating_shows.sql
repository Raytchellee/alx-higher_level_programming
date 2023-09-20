-- lists all ratings from hbtn_0d_tvshows_rate by their rating
SELECT s.title, SUM(r.rate) rating FROM tv_shows s
	LEFT JOIN tv_show_ratings r ON r.show_id = s.id
	GROUP BY s.title ORDER BY rating DESC;
