# Lab-1_C-4

# username generator using first and last name input.
# remove spaces
# convert to lowercase
# create username using first three letters of first name and first 5 letters of the last name

# ask for firstname then lastname
first_name = input("Firstname? ")
last_name = input("Lastname? ")

# strip
first_name = first_name.strip()
last_name = last_name.strip()
# make lowercase
first_name = first_name.lower()
last_name = last_name.lower()
# slice
first_name = first_name[0:3]
last_name = last_name[0:5]
# Concatenate
username = first_name + last_name

print(f"Your username is: {username}")