# Lab-9_E-3

# Add __str__ so printing the Product gives a useful human-readable description

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"


produkt = Product("Schampoo", 400)

print(produkt)
