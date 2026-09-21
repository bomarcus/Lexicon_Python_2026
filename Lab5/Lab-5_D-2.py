# Lab-5_D-2

# Write create_user(username, **details) returning one dictionary containing username plus all supplied details.


def create_user(username, **details):
    return {"username": username, **details}


print(create_user("mao", name="Marcus", lastname="ohlsson"))
