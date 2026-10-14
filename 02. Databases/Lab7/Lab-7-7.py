from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

for order in db.orders.find({"items.product_id": 2}):
    print(order["_id"])
