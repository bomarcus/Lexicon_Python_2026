# 8-3

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


# required
str("email")
