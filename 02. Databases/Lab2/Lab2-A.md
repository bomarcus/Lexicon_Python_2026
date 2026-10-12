1.
CREATE TABLE books (
	book_id	INTEGER PRIMARY KEY,
    title   TEXT NOT NULL,
    author	TEXT,
    year    INTEGER
);

2.
2.1 
DROP TABLE books
2.2
CREATE TABLE books (
	book_id	INTEGER PRIMARY KEY,
    title   TEXT NOT NULL,
    author	TEXT,
    year    INTEGER CHECK (year > 1400)
);

3.
ALTER TABLE books ADD COLUMN isbn TEXT;

4.
DROP TABLE books

5.
CREATE TABLE reviews (
	review_id INTEGER PRIMARY KEY,
	product_id INTEGER,
	rating INTEGER CHECK (rating BETWEEN 1 AND 5),
	comment TEXT,

	FOREIGN KEY (product_id) REFERENCES products(product_id)
);

6.
INSERT INTO reviews (review_id, product_id, rating)
VALUES (1, 1, 6);
-----------------------------------------------------
    Execution finished with errors.
    Result: CHECK constraint failed: rating BETWEEN 1 AND 5
    At line 1:
    INSERT INTO reviews (review_id, product_id, rating)
    VALUES (1, 1, 6);

7.
INSERT INTO reviews (review_id, product_id, rating)
VALUES (1, 50, 3);
-----------------------------------------------------
    Execution finished with errors.
    Result: FOREIGN KEY constraint failed
    At line 1:
    INSERT INTO reviews (review_id, product_id, rating)
    VALUES (1, 50, 3);

8.
costumers
products
orders -> customer_id
order_items -> order_id
order_items -> product_id
