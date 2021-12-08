SELECT id_con, con_date, name, city FROM Publishing
LEFT JOIN (SELECT * FROM Delivery WHERE YEAR(del_date)='$gener3') k USING(id_con) WHERE id_del IS NULL;
