# Lab-9_D-3-4-5

# Use isinstance() to check whether the object is an AdminUser, a User and a string.

class User:
    def __init__(self):
        pass


class AdminUser(User):
    def __init__(self):
        pass


admin_user = AdminUser()

print(isinstance(admin_user, AdminUser))
print(isinstance(admin_user, User))
print(isinstance(admin_user, str))

# AdminUser is a subclass of User. So a Admin_User object is also an instance of User
