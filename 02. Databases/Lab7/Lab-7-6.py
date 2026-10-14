from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


for product in db.products.find({}, {"name": 1, "price": 1}).sort("price", 1).limit(5):
    print(f"{product['name']}: {product['price']} kr")
