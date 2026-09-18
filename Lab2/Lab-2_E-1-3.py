# Lab-2_E-1

book_list = [
    {
        "title": "Philosopher's Stone",
        "author": "JK Rowling",
        "pages": 223,
        "available": True
    },

    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "pages": 310,
        "available": True
    },

    {
        "title": "1984",
        "author": "George Orwell",
        "pages": 328,
        "available": False
    },

    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "pages": 432,
        "available": True
    },

    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "pages": 180,
        "available": False
    }

]

# Lab-2_E-2
# access book 3 title and availability of last book.
print(book_list[2]["title"])
print(book_list[-1]["available"])

# Lab-2_E-3
# change nested value
print(book_list[-2]["pages"])
book_list[-2]["pages"] = 520
print(book_list[-2]["pages"])
# add new key to one book.
book_list[0]["good?"] = True
print(book_list[0])

