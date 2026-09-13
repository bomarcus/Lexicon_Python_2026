# Lab-3_B-3

# create list of blocked usernames and reject if username appears in list.
blocked_usernames = [
    "death",
    "stalin",
    "Uno",
    "Birgit"
]

user_input = input("input username: ")
if user_input in blocked_usernames:
    print("username rejected.")
else:
    print("logging in")