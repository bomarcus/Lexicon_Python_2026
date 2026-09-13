# Lab-1_B-4

# ask user for length input and save to variable. use float.
length_of_room = float(input("What's the length of this room? "))
# ask user for witdh input and save to variable. use float.
width_of_room = float(input("What's the width of this room? "))
# calculate area and save to variable.
area = length_of_room * width_of_room
# calculate perimeter and save to variable.
perimeter = (length_of_room * 2) + (width_of_room * 2)
# print outputs.
print(" The area of that room is ", area)
print(" The perimeter of that room is ", perimeter)