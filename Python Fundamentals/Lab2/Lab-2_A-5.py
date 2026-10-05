# Lab-2_A-5

# sort one list ascending
one_list = [1, 4, 5, 2, 3]
print(sorted(one_list))
one_list.sort()
print(one_list)
# sort another list descending
another_list = [1, 4, 5, 2, 3]
print(sorted(another_list, reverse = True))
another_list.sort(reverse = True)
print(another_list)

# sorted always returns a sorteed list.
# sorted does not affect the original sequence.
# sort can only be used with lists.
# sort makes changes to the original.