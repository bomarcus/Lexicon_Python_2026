# Lab-5-3

import sqlite3

conn = sqlite3.connect("Lab5/Lab-5_webshop.db")
cursor = conn.cursor()

category = input("choose category: ")
cursor.execute("SELECT COUNT(*) FROM products WHERE category = ?", (category,))


rows = cursor.fetchone()

print(f"{category} - {rows[0]}")

conn.close()
