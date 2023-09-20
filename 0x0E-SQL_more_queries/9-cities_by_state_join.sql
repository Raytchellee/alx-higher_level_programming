-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT c.id, c.name, s.name FROM cities c JOIN states s ON s.id = c.state_id ORDER BY c.id ASC;
