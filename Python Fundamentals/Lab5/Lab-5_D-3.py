# Lab-5_D-3

# Write build_product(name, price, **metadata) returning a dictionary.


def build_product(name, price, **metadata):
    return {"name": name, "price": price, **metadata}


print(build_product(name="laptop", price=200, details="very good"))
