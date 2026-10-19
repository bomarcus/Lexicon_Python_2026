from api_client import get_json

categories = get_json("https://fakestoreapi.com/products/categories")

print(categories)


user_input = input("Type a category: ")

selected_category = get_json(f"https://fakestoreapi.com/products/category/{user_input}")

amount_in_category = len(selected_category)


def get_price(product):
    return product["price"]


sorted_products = sorted(selected_category, key=get_price)

cheapest = sorted_products[0]

print(
    f"{user_input} has {amount_in_category} products, the cheapest one is {cheapest['title']} at{cheapest['price']}."
)


# Indexerror list index out of range.
