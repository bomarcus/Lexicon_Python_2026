# Lab-5-10

-- check first 
SELECT c.first_name, c.email, c.customer_id
FROM customers c
WHERE c.customer_id = "2"

-- do it
UPDATE customers 
SET email = "erik.johansson@example.com"
WHERE customer_id = 2;