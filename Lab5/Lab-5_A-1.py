# Lab-5_A-1

# create global variable
course_name = "Python2026"

# create_function creating local variable with same name as global variable.
def course():
    course_name = "Python2026"
    print(course_name)

print(course_name) # prints global course name variable.
course() # prints local variable from course-function.

