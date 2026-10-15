# Lab-5-9

SELECT DISTINCT p.name
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON oi.product_id = p.product_id
WHERE c.first_name = "Anna";