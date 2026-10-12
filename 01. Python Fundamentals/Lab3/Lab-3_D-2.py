# Lab-3_D-2

# generate the multiplication table for a number supplied by the user.

user_input = int(input("Input a number: "))
table_range = range(1, 11, 1)

for number in table_range:
    print(user_input, "x", number, "=", user_input * number)
