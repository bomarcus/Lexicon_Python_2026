# Lab-3_A-4

# given a score from 0-100. print a grade using atleast five ranges.
score = 89
# E - 0 - 19
if score <= 19:
    print("E")
# D - 20 - 39
elif score <= 39:
    print("D")
# C - 40 - 59
elif score <= 59:
    print("C")
# B - 60 - 89
elif score <= 89:
    print("B")
# A - 90 - 100
else:
    print("A")