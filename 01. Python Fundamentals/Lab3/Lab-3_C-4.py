# Lab-3_C-4

# find the largest number in a list manually without using max() 
list_of_numbers = [
    1,
    4,
    3,
    5,
    6,
    7,
    10,
    12
]
# create a variable for the largest number found and set it to the first value in the list.
largest_number_found = list_of_numbers[0]
# for each number in list,  
for number in list_of_numbers:
    #if number is larger than current largest_number found.
    if number > largest_number_found:
        # largest number found is set equal to number.
        largest_number_found = number
print(largest_number_found)