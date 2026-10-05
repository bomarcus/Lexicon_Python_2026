# Lab-7_A-1

# Create a Book class with title, author and pages.
# Create at least four Book objects and print their attributes.


class Book:
     def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("Philosopher's Stone", "JK Rowling", 223)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book3 = Book("1984", "George Orwell", 328)
book4 = Book("Pride and Prejudice", "Jane Austen", 432)

books = [book1, book2, book3, book4]

for book in books: 
    print(f"Title: {book.title}. Author: {book.author}. Pages:{book.pages}")