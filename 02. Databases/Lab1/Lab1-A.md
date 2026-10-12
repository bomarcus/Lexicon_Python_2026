1.
SELECT first_name, email FROM customers;
2.
SELECT  name  FROM products WHERE category = 'Shoes';
3.
SELECT  first_name, city  FROM customers WHERE city = 'Uppsala' ;
4.
SELECT  name FROM products WHERE price = 199 ;
5.
SELECT * FROM products ORDER BY name DESC;
6.
SELECT * FROM  customers ORDER BY joined_date; 
7.
SELECT * FROM products WHERE stock  = 0; 
8.
SELECT * FROM customers ORDER BY joined_date LIMIT  3;
9.
SELECT * FROM customers  WHERE city IN ('Stockholm', 'Göteborg');
10.
SELECT name AS product, price AS price_sek FROM products;

-

11.
SELECT * FROM products WHERE (category = 'Clothing' OR category =  'Shoes') AND price >= 1000;
12.

