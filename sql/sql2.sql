SELECT id_b, Books.name FROM Books
JOIN Delivery using (id_b)
JOIN Publishing using (id_con)
WHERE Publishing.name = '$gener1' AND  Delivery.del_date = '$gener2';
