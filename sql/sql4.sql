SELECT del_date FROM Delivery
JOIN Publishing USING (id_con)
WHERE Publishing.city = '$gener4';
