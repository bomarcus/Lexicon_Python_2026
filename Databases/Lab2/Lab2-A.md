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