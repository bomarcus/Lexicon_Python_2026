# Lab-9-1

from api_client import get_json

products = get_json("https://fakestoreapi.com/products")


def get_price(product):
    return product["price"]


sorted_products = sorted(products, key=get_price)

for product in sorted_products:
    print(f"{product['price']} - {product['title']}")
