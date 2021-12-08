select id_b, name, author, genre, cost, image from Books
join Library using (id_b)
where Books.id_b = '$item_id'
