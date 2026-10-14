from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

for customer in db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}):
    print(customer["_id"], customer["first_name"])
