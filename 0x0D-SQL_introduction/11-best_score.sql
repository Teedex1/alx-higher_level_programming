-- lists all record with a score >= 10 in the tale second_table of the database hbtn_0c_0 in the MySQL server.

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
