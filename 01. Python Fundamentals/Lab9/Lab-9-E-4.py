# Lab-9_E-4

# Create at least three Product objects and print them.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"


products = [
    Product("Schampoo", 400),
    Product("Soap", 25),
    Product("Toothpaste", 35)
]

for product in products:
    print(product)
