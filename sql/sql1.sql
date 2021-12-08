SELECT id_b, name, price, quantity FROM Delivery
JOIN Books USING (id_b)
WHERE YEAR(del_date)='$gener';
