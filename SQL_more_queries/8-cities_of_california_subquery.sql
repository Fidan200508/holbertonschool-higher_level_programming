-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id,
       name
FROM cities c
    WHERE c.state_id = (SELECT s.id
                        FROM states s WHERE s.name = "California")
ORDER BY c.id;
