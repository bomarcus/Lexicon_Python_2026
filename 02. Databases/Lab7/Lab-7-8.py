from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

print("BEFORE PRICE HIKE")
for product in db.products.find({"category": "Accessories"}):
    print(product["name"], product["price"])

print("AFTER PRICE HIKE")
price_increase = db.products.update_many(
    {"category": "Accessories"}, {"$inc": {"price": 20}}
)
print(price_increase.modified_count)
for product in db.products.find({"category": "Accessories"}):
    print(product["name"], product["price"])
