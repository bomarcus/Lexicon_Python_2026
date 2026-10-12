# Lab-2_A-6

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_b = list_a
list_b.append(7)
print(list_b)
print(list_a)
list_c = [1, 2, 3]
list_d = [4, 5, 6]
list_d = list_c.copy()
list_d.append(7)
print(list_c)
print(list_d)
# list_b = list_a points to the same list in memory. they are the same.
# .copy() creates a new list.