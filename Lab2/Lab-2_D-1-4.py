# Lab-2_D-1-4

# create dict with brand, model, ram, storage and price

laptop = {
    "brand" : "Acer",
    "model" : "A4000",
    "ram" : "512mb",
    "storage" : "256mb",
    "price" : 250
}

# read each value by key
print(laptop["brand"], laptop["model"], laptop["price"], laptop["ram"], laptop["storage"])

# D-2
# update the price
laptop["price"] = 300
print(laptop.values())

# add operating_system
laptop["operating_system"] = "Ubuntu"
print(laptop.values())

# remove one key
laptop.pop("storage")
print(laptop.items())

# D-3
# use .get() for both exissting and missing key
print(laptop.get("ram"))
print(laptop.get("color")) #produce None
# print(laptop["color"]) #produce KeyError

# D-4
# print keys
print(laptop.keys())

# print values
print(laptop.values())
# print items
print(laptop.items())

