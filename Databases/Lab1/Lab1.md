Install DB Browser for SQLite
Go to sqlitebrowser.org/dl
Download the version for your computer:
Windows: "DB Browser for SQLite – Standard installer for 64-bit Windows". Open the file and click Next until it's done. If the computer says you need admin rights, download the PortableApp version on the same page instead. It works without installing.
Mac: download the .dmg file, open it, and drag DB Browser for SQLite into the Applications folder. The first time you start it, right-click the app and choose Open, then click Open again. A normal double-click gets blocked by macOS the first time.
Linux: open a terminal and type sudo apt install sqlitebrowser
Start the program. On Windows it's in the Start menu as "DB Browser (SQLite)".
Open webshop.db

Save the file first. Download webshop.db from where it was shared (Teams --> Database channel) and save it in a folder you can find again, for example Documents/SQL. If it comes in a zip file, unzip it first.

In DB Browser, click Open Database in the toolbar at the top (or press Ctrl+O, Mac: Cmd+O).
Find webshop.db, select it and click Open.

Check that it worked: click the Database Structure tab. You should see Tables (2) with customers and products.

Go to the Execute SQL tab to write your queries.

Next time: the file is in File > Recent Files, so you don't have to search for it again.
If something goes wrong:
You see no tables: you probably opened the zip file or another file. Open the real webshop.db again.

Changes are gone when you reopen the file: you forgot to save the data. Press Ctrl+S (Write Changes) after you change data.

LAB1:
1. Show the first name and email of all customers. (10 rows)
2. Show all products in the Shoes category. (3 rows)
3. Which customers live in Uppsala? (3 rows)
4. Which product costs exactly 199 kr? (1 row)
5. Show all products sorted by name, A to Z. (12 rows)
6. Show all customers, the one who joined first at the top. (10 rows)
7. Which products are sold out (stock is 0)? (2 rows)
8. Show the 3 newest customers. (3 rows)
9. Show customers from Stockholm or Göteborg. Use IN. (4 rows)
10. Show product name and price, but call the columns product and price_sek. (12 rows)


Bonus questions:
Show products that are Clothing or Shoes and cost more than 1000 kr. Hint: you need brackets. Try without them too: why is the answer different? (3 rows)
For every product in stock, show name, price, stock and the total value of the stock (price × stock) as stock_value. Highest value first. (10 rows)
Which customers have a first name with exactly 4 letters? Hint: _ in LIKE means "exactly one character". (4 rows)
Sort the products by price, cheapest first, and show only products number 6 to 10. Hint: look up OFFSET. (5 rows)
Show customers who joined before 2025 and don't live in Uppsala. Sort by city, and by last name within the same city. (4 rows)