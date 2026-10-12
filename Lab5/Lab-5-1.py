import sqlite3

conn = sqlite3.connect("Lab5/Lab-5_webshop.db")
cursor = conn.cursor()
cursor.execute("SELECT first_name, last_name, city FROM customers")


result = cursor.fetchall()
for row in result:
    print(f"{row[0]} {row[1]} ({row[2]})")

conn.close()
