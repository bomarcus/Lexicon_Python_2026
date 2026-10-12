# Lab-7_A-2

# Create a Laptop class with brand, model,
# sram_gb and price. Create three separate objects and change the price of one object.

class Laptop:
    def __init__(self, brand, model, ram_gb, price):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

laptop1 = Laptop("HP", "latest", 16, 10000)
laptop2 = Laptop("Dell", "quite old", 32, 250000)
laptop3 = Laptop("Apple", "brand new", 8, 30000)

laptops = [laptop1, laptop2, laptop3]

for laptop in laptops:
    print(
        f"Brand: {laptop.brand}.",
        f"Model: {laptop.model}.",
        f"RAM: {laptop.ram_gb}.",
        f"Price: {laptop.price}."
    )

laptop1.price = 8000

for laptop in laptops:
    print(
        f"Brand: {laptop.brand}.",
        f"Model: {laptop.model}.",
        f"RAM: {laptop.ram_gb}.",
        f"Price: {laptop.price}."
    )

