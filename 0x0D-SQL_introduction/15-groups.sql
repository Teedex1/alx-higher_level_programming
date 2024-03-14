-- lists the number odf records with the same score in the table second_table of the database hbtn_0c_0 of the MySQL.

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
