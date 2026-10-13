from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

uppsalabor = db.customers.count_documents({"city": "Uppsala"})
print("Uppsalabor:", uppsalabor)
