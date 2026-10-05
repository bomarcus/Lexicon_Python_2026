# Lab-5_C-1

# Create a list [10, 20, 30] and unpack it into a function expecting three positional parameters.


numbers = [10, 20, 30]


def expecting_function(a, b, c):
    return a, b, c


print(expecting_function(*numbers))
