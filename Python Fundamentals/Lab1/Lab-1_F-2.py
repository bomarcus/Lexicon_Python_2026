# Lab-1_F-2

four_digits = 1234

# extract and print each digit without converting to string.

first = four_digits // 1000
second = four_digits // 100 % 10
third = four_digits % 100 // 10
fourth = four_digits % 10

print(first)
print(second)
print(third)
print(fourth)
