-- a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT
    s.title,
    g.name
FROM tv_genres g
RIGHT JOIN tv_show_genres sg ON g.id = sg.genre_id
RIGHT JOIN tv_shows s ON sg.show_id = s.id
ORDER BY s.title, g.name
