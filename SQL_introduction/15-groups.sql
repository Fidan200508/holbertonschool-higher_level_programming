-- a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0
-- a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0
SELECT
SCORE as "score",
COUNT(*) AS "number"
FROM second_table
GROUP BY SCORE
ORDER BY SCORE DESC LIMIT 10;
