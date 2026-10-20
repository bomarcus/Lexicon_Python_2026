from api_client import get_json

print(get_json("https://fakestoreapi.com/productz"))
print(get_json("https://fakestoreapi.com", timeout=0.001))
print(get_json("https://doghair-xyz-123456.com"))
