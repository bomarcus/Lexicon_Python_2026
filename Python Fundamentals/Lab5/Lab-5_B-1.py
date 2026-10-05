# Lab-5_B-1

# write  add_all(*numbers) returning sum without sum()

numbers = [1, 2, 3, 4]


def add_all(*numbers):
    total = 0
    for number in numbers:
        total = number + total
    return total


print(add_all(*numbers))
