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

phone_numbers
- The plural name suggests several numbers in one cell, i.e. a list. That breaks 1NF (one value per cell).
- It's also unclear what kind of number each one is (home, work, mobile).
- Fix: a separate phones table, 1:N (one student has many phone numbers).

course1, course2, course3
- A repeating group, which breaks 1NF.
- A fourth course doesn't fit without changing the table, and empty slots become NULL.
- Hard to query: "how many students take SQL?" means checking all three columns.
- Fix: students and courses are N:M, so a middle table (enrollments) links them.

No primary key
- Nothing uniquely identifies a student, so two students with the same name can't be told apart.

11.
seprate products into own table and rename order_sheet "orders" and create a order_items table to hold ordered items.

12.
customer email should be in a customers table.
if a custumer has multiple orders and changes their email and not all orders are updated we create a 
update anomaly

13.

Students teachers lessons date time room instrument

