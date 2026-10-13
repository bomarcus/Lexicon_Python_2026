from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


sandals = db.products.find_one({"name": "Sandals"})
if sandals:  # skips print if nothing is found/ find_one returns None.
    print(sandals["stock"], "Sandals in stock")
