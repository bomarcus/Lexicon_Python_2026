# Lab-5_A-4

# Create a nested function and demonstrate a simple enclosing-scope lookup.

def outer():
    outside = "outside"

    def inner():
        inside = "inside"
        print(inside)
        print(outside)
    inner()


outer()  # prints outside
