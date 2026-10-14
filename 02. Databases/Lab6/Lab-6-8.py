from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


# run once:
# add_products = db.products.insert_many(
#     [
#         {
#             "_id": 13,
#             "name": "Beanie Grey",
#             "category": "Accessories",
#             "price": 179,
#             "stock": 30,
#             "tags": ["winter", "wool"],
#         },
#         {
#             "_id": 14,
#             "name": "Running Shorts",
#             "category": "Clothing",
#             "price": 349,
#             "stock": 18,
#             "tags": ["summer", "sport"],
#         },
#     ]
# )


print(db.products.count_documents({}))
