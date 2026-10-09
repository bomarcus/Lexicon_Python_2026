1.
SELECT  orders.order_id, customers.first_name, customers.last_name, orders.status
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;

2.
SELECT  orders.order_id, customers.first_name, customers.last_name, orders.status
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
WHERE customers.first_name = 'Erik';

3.
SELECT  o.order_id, c.first_name, c.last_name, o.status, c.city, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.city = 'Göteborg'
ORDER BY o.order_date DESC;

4.
SELECT oi.order_id, p.name, p.category
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id;

5.
SELECT oi.order_id, p.name
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE p.category = 'Shoes';

6.
SELECT oi.order_id, oi.quantity, oi.unit_price, p.name, (oi.quantity * oi.unit_price) AS line_total
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE oi.order_id = 10;

7.
SELECT o.order_date, c.first_name, p.name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE p.name = 'Hoodie Black';

8.
SELECT o.customer_id, c.first_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

9.
SELECT p.name, oi.quantity
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.product_id
WHERE oi.product_id IS NULL;

10.
SELECT c.first_name, c.city, p.name, oi.quantity
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE c.city = 'Uppsala';