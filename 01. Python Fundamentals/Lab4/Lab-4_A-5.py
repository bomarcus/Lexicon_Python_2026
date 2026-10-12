# Lab-4_A-5

# create function calculate_area(width, height) and use return value in another calculation.

width = 200
height = 100

# calculate area
def calculate_area(width, height):
    return width * height

# save as variable
area = calculate_area(width, height)

# use area variable in new function with parameters area and times
def double_area(area, times):
    return area * times

# print
print(double_area(area, 2))
    








