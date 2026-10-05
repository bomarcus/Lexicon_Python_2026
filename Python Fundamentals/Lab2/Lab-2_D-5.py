# Lab-2_D-5

# five course names to number of study hours
# calculate total hours using the dictionary rules.

course_names_hours = {
    "Math A": 20,
    "Math B": 30,
    "Math C": 10,
    "Math D": 40,
    "Math E": 15
}

hours = 0

for value in course_names_hours.values():
    hours += value
print(hours, "total study hours")

# or
print(sum(course_names_hours.values()))
