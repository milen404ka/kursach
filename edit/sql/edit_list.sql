select name, author, genre, b_availability, cost from Books
join Library using (id_b)
