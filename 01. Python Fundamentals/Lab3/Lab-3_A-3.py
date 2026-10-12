# Lab-3_A-3

# create login check using a stored username and password. Both must match.
# create dictionary with username and password.
login_credentials = {
    "username" : "admin",
    "password" : "12345"
    }
# ask user to input username, then password.
username = input("username: ")
password = input("password: ")
# check if both username and password matches the values in in dictionary
if username == login_credentials["username"] and password == login_credentials["password"]:
    print("Success!")
else:
    print("Wrong username and/or password")