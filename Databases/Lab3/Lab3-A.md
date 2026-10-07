1.
INSERT INTO customers (customer_id, first_name, last_name, email, city, joined_date)
VALUES (11, 'Marcus', 'Ohlsson', 'marcus@email.com', 'Stckholm', '2020-01-01');

2.
INSERT INTO products (name, category, price, stock) VALUES
('Scarf', 'Accessories', 229, 15),
('Gloves', 'Accessories', 199, 20);

3.
INSERT INTO orders (order_id, customer_id, order_date)
VALUES (16, 7, '2020-01-01');

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (16, 10 , 2, 179);

4.
CHECK constraint failed: quantity > 0

5.

