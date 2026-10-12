# Lab-5_C-2

# Create a tuple containing first_name, last_name, city and call a function using *tuple.

info = (
    "marcus",
    "ohlsson",
    "stockholm"
)


def calling_tuple(*info):
    return info


print(calling_tuple(*info))
