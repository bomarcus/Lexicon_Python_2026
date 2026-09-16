# Lab-1_E-1

# program that collects first name, last name, city,
#  year of birth and fave programming language

# first_name = input("whats your name? ")
# last_name = input("...and last name? ")
# birth_year = int(input("...when where you born? "))
# city = input("...and where do you live? ")
# fave_language = input("favourite programming language? ")


# Lab-1_E-2
# normalize text intput to remove accidental surrounding spaces.
first_name = input("whats your name? ").strip()
last_name = input("...and last name? ").strip()
birth_year = int(input("...when where you born? ").strip())
city = input("...and where do you live? ").strip()
fave_language = input("favourite programming language? ").strip()

print(
    "\n"
    "Input: ",
    first_name,
    last_name,
    birth_year,
    city,
    fave_language
    )

# Lab-1_E-3
# create username from
# first two chars of first_name, 
# first three of last_name, 
# convert birth_year to string then use last two chars.
#  make them all lowercase.
user_id = (first_name[0:2] + last_name[0:3] + str(birth_year)[-2:]).lower()

print("Your username is: ", user_id)

# Lab-1_E-4
# print clean summary using f-strings

print(
    "\n"
    "Summary: " "\n"
    f"{first_name} {last_name}." "\n"
    f"Born in {birth_year}." "\n"
    f"From {city}." "\n"
    f"Favourite programming language is {fave_language}."
    )


# Lab-1_E-5
# print initials
print(first_name[0] + (last_name[0]))
# print full name lenght excluding space
print(len(first_name + (last_name)))
# favourite language reversed
print(fave_language[::-1])

# Lab-1_E-6
print(f"You are around {2026 - birth_year} years old!")
print(f"{city} has {len(city)} characters in its name.")
print(f"stating that your first name is longer than your last name would be {(len(first_name) > len(last_name))}.")