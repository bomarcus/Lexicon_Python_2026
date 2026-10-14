from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


for product in db.products.find({"tags": "sport"}, {"name": 1, "tags": 1, "_id": 0}):
    print(product["name"], product["tags"])
