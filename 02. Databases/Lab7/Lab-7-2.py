from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

for order in db.orders.find({"status": {"$ne": "delivered"}}):
    print(order["_id"], order["status"])
