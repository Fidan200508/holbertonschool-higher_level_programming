-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT
    g.name AS genre,
    count(*) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
JOIN tv_shows s ON sg.show_id = s.id
GROUP BY g.name
