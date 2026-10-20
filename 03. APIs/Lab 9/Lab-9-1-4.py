# Lab-9-4

import requests


new_product = {
    "title": "Coffee Maker",
    "price": 13.5,
    "description": "Coffee Maker",
    "image": "https://artilleriet.centracdn.net/client/dynamic/images/59611_4f51827110-aarke-coffee-maker-black-1-zoom.jpg",
    "category": "electronics",
}

response = requests.post(
    "https://fakestoreapi.com/products", json=new_product, timeout=5
)
print(response.status_code)
print(response.json())
print(response.request.headers["Content-Type"])
print(response.request.body)

patch_response = requests.patch(
    "https://fakestoreapi.com/products/7",
    json={
        "price": 23.5,
    },
    timeout=5,
)

print(patch_response.status_code)
print(patch_response.json())
