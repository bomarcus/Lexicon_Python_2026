from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


# run once:
# result = db.customers.insert_one(
#     {
#         "first_name": "Marcus",
#         "last_name": "Ohlsson",
#         "email": "mo@mail.com",
#         "city": "Uppsala",
#     }
# )
# print(result.inserted_id)

marcus = db.customers.find_one({"email": "mo@mail.com"})
pprint.pp(marcus)
