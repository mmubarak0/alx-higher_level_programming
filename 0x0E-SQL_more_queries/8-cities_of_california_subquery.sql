-- lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id, name FROM cities AS c
WHERE state_id = (SELECT DISTINCT id FROM states WHERE name = "California")
ORDER BY c.id;
