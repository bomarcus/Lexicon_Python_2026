# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:
# 1
for product in products:
    print(product)

# 2
for product in products:
    if product["stock"] > 0:
        print(product["name"])

# 3
total_value = 0

for product in products:
    total_value += product["price"] * product["stock"]

# 4
print(total_value)

# 5
current_highest_price = 0
highest_price_name = ""

for product in products:
    if product["stock"] > 0 and product["price"] > current_highest_price:
        current_highest_price = product["price"] 
        highest_price_name = product["name"]

print(highest_price_name)




# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:

def calculate_average(scores):
    return sum(scores) / len(scores)

def create_result(scores):
    if calculate_average(scores) >= 70:
        return "PASS"
    else:
        return "FAIL"

print(calculate_average(scores))
print(create_result(scores))

# ==================================================    
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:

def calculate_order(name, *product_prices, **order_settings):
    subtotal = sum(product_prices)
    final_total = subtotal
    if "discount" in order_settings:
        final_total = final_total - order_settings["discount"] * subtotal / 100
    if "shipping" in order_settings:
        final_total = final_total + order_settings["shipping"]
    return {
        "customer" : name,
        "subtotal" : subtotal,
        "final_total" : final_total,
        "settings" : order_settings
    }

print(calculate_order("Anna", *product_prices, **order_settings))




# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:

new_players = []

for player in players:
    cleaned_name = player["name"].strip().capitalize()
    new_players.append(cleaned_name)

#print(new_players)

newlist = [player["name"].strip().capitalize() for player in players]

print(newlist)

active_players = [
    player
    for player in players
    if player["active"] == True
    and player["score"] >= 80
]

print(active_players)

new_players = []

for player in players:
    cleaned_name = player["name"].strip().capitalize()
    new_players.append(cleaned_name)


newlist = [player["name"].strip().capitalize() for player in players]

print(newlist)

#3 
sorted_players = sorted(players, key= lambda player: player["score"], reverse = True)

print(sorted_players)

for ranking, player in enumerate(sorted_players, start=1):
    print(f"{ranking}. {player['name'].strip().capitalize()} - {player['score']}")

# 5

player_names = []
player_scores = []

for player in players:
    player_names.append(player["name"].strip().capitalize())

print(player_names)

for player in players:
    player_scores.append(player["score"])

print(player_scores)

names_score = list(zip(player_names, player_scores))
for name, score in names_score:
    print(name, score)