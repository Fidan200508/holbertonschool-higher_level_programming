-- a script that lists all records of the table second_table of the database hbtn_0c_0
-- a script that lists all records of the table second_table of the database hbtn_0c_0
SELECT
SCORE as "score",
NAME as "name"
 FROM second_table
WHERE NAME IS NOT NULL
ORDER BY SCORE DESC;
