# Lab-5_B-2
# Write average(*numbers). Decide what should happen when no numbers are supplied.

def average(*numbers):
    if len(numbers) == 0:
        return "NO NUMBERS"
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


print(average(1, 2, 3, 4))
