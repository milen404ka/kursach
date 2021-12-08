select id_b, name, author, genre, b_availability, cost, image from Books
join Library using (id_b)
