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
UPDATE orders SET status = 'shipped' WHERE order_id = 12;

6.
UPDATE products SET stock = 50 WHERE product_id = 5;

7.
UPDATE products SET price = price * 1.1 WHERE category = 'Accessories';

8.
SELECT * FROM orders WHERE status = 'cancelled';
DELETE FROM order_items WHERE order_id = 7;
DELETE FROM orders WHERE status = 'cancelled';
---FOREIGN KEY constraint failed

9.
15 orders

10.
student | phone_numbers | course1 | course2 | course3

- name phone_numbers might indicate that more than one value is permitted per cell.
- courses are repeating groups.

11.
orders
order | customer | email | city | total
 1
 2

order_items
order_no | product | quantity
1
1
4
4

12.
