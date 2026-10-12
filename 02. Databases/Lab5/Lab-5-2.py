# Lab-5-2

import sqlite3

conn = sqlite3.connect("Lab5/Lab-5_webshop.db")
cursor = conn.cursor()

user_maxprice = input("whats you max price? ")
cursor.execute("SELECT name, price FROM products WHERE price < ?", (user_maxprice,))


rows = cursor.fetchall()

for name, price in rows:
    print(f"{name} - {price}")

conn.close()
