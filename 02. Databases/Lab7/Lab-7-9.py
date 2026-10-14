from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# restock date
# restock_date (datetime.now())
# add tag new

# check for rain jacket:
rain_jacket = db.products.find_one({"name": "Rain Jacket"})
print(rain_jacket)

# add tag new and field
db.products.update_one(
    {"name": "Rain Jacket"},
    {"$addToSet": {"tags": "new"}, "$set": {"restock_date": datetime.now()}},
)

# check update
rain_jacket = db.products.find_one({"name": "Rain Jacket"})
print(rain_jacket)
