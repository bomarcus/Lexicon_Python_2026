# Lab-1_B-1

# create variable called name and ask for user input
name = input("Whats your name? ")
# prints name 
print("Hello", name, ".")
# create variable birth_year and ask for user input
birth_year = input("What year where you born? ")
# create current year variable
current_year = 2026
# create new variable called age which converts birth_year to an integer, then subtracts it from current_year.
age = current_year - int(birth_year)
# prints name and approximate age
print(name, "you are approximately", age, "years old.")